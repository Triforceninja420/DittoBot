// ====================================================================
// Project: DittoBot / Voxel Box
// Component: Release-coil pulse driver
// Target: Seeed Studio XIAO RP2040 (Dual ARM Cortex-M0+)
// Driver IC: TI DRV8871 (VM 6.5-45 V abs max; prefer <=42 V from pulse bank)
// Variant: 25 mm cubic cell - Nd disc Ø6.0x2-3 mm residual hold, coil is RELEASE only
//           NOT Phase 0 20 mm face (rev 2026-11-21)
// Author: Craig Edward Ralls (2026)
// License: MIT
// Baseline: 2026-11-19 (pulse-only + thermal governor stub); magnet synced 2026-11-23
// Updated 2026-11-23: thermal governor implemented (NTC + optional TMP117),
//   pulse trains, INA219 sensing, contact detection, state machine, error flags
// ====================================================================

#include <Arduino.h>
#include <Wire.h>

// ------------------------------------------------------------------
// Driver H-Bridge Logic Pins (DRV8871)
// ------------------------------------------------------------------
const uint8_t PIN_EPM_IN1 = 0; // GPIO 0 -> H-Bridge IN1
const uint8_t PIN_EPM_IN2 = 1; // GPIO 1 -> H-Bridge IN2

// ------------------------------------------------------------------
// Thermal governor - NTC on A0, beta 3950, 10k pull-up to 3.3 V
// ------------------------------------------------------------------
const uint8_t PIN_NTC = A0;
const float NTC_BETA = 3950.0;
const float NTC_R25 = 10000.0;
const float NTC_PULLUP = 10000.0;
const float THERMAL_THRESHOLD_C = 60.0;
const float THERMAL_HYSTERESIS_C = 5.0;
const uint8_t THERMAL_PULSE_LIMIT = 20;   // consecutive pulses before forced cooldown
const uint32_t THERMAL_COOLDOWN_MS = 5000;

// Optional TMP117 (I2C, addr 0x48) - set true if populated
const bool USE_TMP117 = false;
const uint8_t TMP117_ADDR = 0x48;

// ------------------------------------------------------------------
// INA219 current sense (I2C, addr 0x40) - set true if populated
// ------------------------------------------------------------------
const bool USE_INA219 = false;
const uint8_t INA219_ADDR = 0x40;

// ------------------------------------------------------------------
// Face contact detection (six pogos, active low when mated)
// ------------------------------------------------------------------
const uint8_t PIN_CONTACT[6] = {2, 3, 4, 5, 6, 7};

// ------------------------------------------------------------------
// Pulse parameters - start in 50-200 ms band, tune from measured
// time-to-peak on the real coil. This pulse only bucks the Nd residual.
// ------------------------------------------------------------------
const uint32_t SWITCH_PULSE_MS = 100;
const uint32_t PULSE_GAP_MS = 20; // inter-pulse gap in a train

// ------------------------------------------------------------------
// State machine
// ------------------------------------------------------------------
enum FaceState {
    FACE_IDLE,
    FACE_SOFT_DOCK,
    FACE_HARD_LOCK,
    FACE_POWERED,
    FACE_ERROR
};
FaceState face_state = FACE_IDLE;

// ------------------------------------------------------------------
// Error flags
// ------------------------------------------------------------------
volatile uint8_t error_flags = 0;
const uint8_t ERR_THERMAL   = 0x01;
const uint8_t ERR_CURRENT   = 0x02;
const uint8_t ERR_CONTACT   = 0x04;
const uint8_t ERR_WATCHDOG  = 0x08;

uint8_t pulse_count = 0;
uint32_t last_pulse_ms = 0;
bool thermal_latched = false; // latched hot until cooldown clears

// ------------------------------------------------------------------
// Thermal governor - returns true if a pulse is allowed
// ------------------------------------------------------------------
float read_ntc_temp_c() {
    int raw = analogRead(PIN_NTC);
    float v = raw * (3.3 / 1023.0);
    float r = NTC_PULLUP * (3.3 / v - 1.0);
    float inv_t = (1.0 / 298.15) + (1.0 / NTC_BETA) * log(r / NTC_R25);
    return (1.0 / inv_t) - 273.15;
}

float read_tmp117_temp_c() {
    // TMP117: 16-bit temp, 0.0078125 C/LSB, reg 0x00
    Wire.beginTransmission(TMP117_ADDR);
    Wire.write(0x00);
    Wire.endTransmission(false);
    Wire.requestFrom(TMP117_ADDR, 2);
    int16_t raw = (Wire.read() << 8) | Wire.read();
    return raw * 0.0078125;
}

float plate_temp_c() {
    if (USE_TMP117) return read_tmp117_temp_c();
    return read_ntc_temp_c();
}

bool thermal_ok() {
    float t = plate_temp_c();
    if (thermal_latched) {
        if (t < THERMAL_THRESHOLD_C - THERMAL_HYSTERESIS_C) {
            thermal_latched = false;
            pulse_count = 0;
        } else {
            return false;
        }
    }
    if (t >= THERMAL_THRESHOLD_C) {
        thermal_latched = true;
        error_flags |= ERR_THERMAL;
        return false;
    }
    if (pulse_count >= THERMAL_PULSE_LIMIT) {
        if (millis() - last_pulse_ms < THERMAL_COOLDOWN_MS) return false;
        pulse_count = 0;
    }
    return true;
}

// ------------------------------------------------------------------
// INA219 current read (mA) - returns -1.0 if not populated
// ------------------------------------------------------------------
float read_ina219_ma() {
    if (!USE_INA219) return -1.0;
    // INA219: shunt voltage reg 0x01, 10 uV/LSB
    Wire.beginTransmission(INA219_ADDR);
    Wire.write(0x01);
    Wire.endTransmission(false);
    Wire.requestFrom(INA219_ADDR, 2);
    int16_t raw = (Wire.read() << 8) | Wire.read();
    float v_shunt = raw * 10e-6; // volts
    // Assume 0.1 ohm shunt (default); adjust per BOM
    return (v_shunt / 0.1) * 1000.0;
}

// ------------------------------------------------------------------
// Contact detection - returns mask of seated contacts (bit i = contact i)
// ------------------------------------------------------------------
uint8_t read_contacts() {
    uint8_t mask = 0;
    for (uint8_t i = 0; i < 6; i++) {
        if (digitalRead(PIN_CONTACT[i]) == LOW) mask |= (1 << i);
    }
    return mask;
}

// ------------------------------------------------------------------
// Pulse the coil. Hold is the Nd residual; this pulse only releases.
// Immediately de-asserts so static coil current is 0.
// ------------------------------------------------------------------
void pulse_epm_latch(bool engage) {
    if (!thermal_ok()) {
        error_flags |= ERR_THERMAL;
        return;
    }

    if (engage) {
        digitalWrite(PIN_EPM_IN1, HIGH);
        digitalWrite(PIN_EPM_IN2, LOW);
    } else {
        digitalWrite(PIN_EPM_IN1, LOW);
        digitalWrite(PIN_EPM_IN2, HIGH);
    }

    delay(SWITCH_PULSE_MS);

    // Quench - no continuous heating. Hold is the Nd residual.
    digitalWrite(PIN_EPM_IN1, LOW);
    digitalWrite(PIN_EPM_IN2, LOW);

    pulse_count++;
    last_pulse_ms = millis();

    float i = read_ina219_ma();
    if (i > 0 && i > 3600.0) { // above DRV8871 3.6 A peak rating
        error_flags |= ERR_CURRENT;
    }
}

// ------------------------------------------------------------------
// Pulse train - N pulses with inter-pulse gap. Used for stubborn release.
// ------------------------------------------------------------------
void pulse_epm_train(bool engage, uint8_t count) {
    for (uint8_t i = 0; i < count; i++) {
        pulse_epm_latch(engage);
        if (i + 1 < count) delay(PULSE_GAP_MS);
        if (!thermal_ok()) break; // abort train if governor trips
    }
}

// ------------------------------------------------------------------
// Dock / undock state machine (stub - flesh out with measured Hall
// threshold and timing on first article)
// ------------------------------------------------------------------
void face_update() {
    uint8_t contacts = read_contacts();
    switch (face_state) {
        case FACE_IDLE:
            if (contacts != 0) face_state = FACE_SOFT_DOCK;
            break;
        case FACE_SOFT_DOCK:
            // Nd disc pulls in; chamfer/ridges center. Wait for seated.
            if (contacts == 0x3F) face_state = FACE_HARD_LOCK;
            break;
        case FACE_HARD_LOCK:
            // 3-pin latch engages here on Phase 0; 25 mm uses axial pin.
            // Presence probe on pogo 5, then power-up.
            face_state = FACE_POWERED;
            break;
        case FACE_POWERED:
            if (contacts == 0) face_state = FACE_IDLE; // undocked
            break;
        case FACE_ERROR:
            // Stay here until operator clear via serial command
            break;
    }
    if (error_flags != 0 && face_state != FACE_ERROR) {
        face_state = FACE_ERROR;
    }
}

// ------------------------------------------------------------------
// Serial command handler (115200)
// ------------------------------------------------------------------
void handle_serial() {
    if (!Serial.available()) return;
    char c = Serial.read();
    switch (c) {
        case 'p': pulse_epm_latch(false); Serial.println("PULSE release"); break;
        case 'e': pulse_epm_latch(true);  Serial.println("PULSE engage"); break;
        case 't': Serial.print("Plate temp: "); Serial.print(plate_temp_c(), 1); Serial.println(" C"); break;
        case 'c': {
            uint8_t m = read_contacts();
            Serial.print("Contacts: 0b");
            for (int8_t i = 5; i >= 0; i--) Serial.print((m >> i) & 1);
            Serial.println();
            break;
        }
        case 'i': {
            float ma = read_ina219_ma();
            Serial.print("INA219: "); Serial.print(ma, 1); Serial.println(" mA");
            break;
        }
        case 's': Serial.print("State: "); Serial.println((int)face_state); break;
        case 'f': Serial.print("Errors: 0x"); Serial.println(error_flags, HEX); break;
        case 'r': error_flags = 0; face_state = FACE_IDLE; Serial.println("Reset"); break;
        case 'h':
            Serial.println("p=pulse release e=pulse engage t=temp c=contacts i=current s=state f=errors r=reset");
            break;
    }
}

// ------------------------------------------------------------------
// Setup / loop
// ------------------------------------------------------------------
void setup() {
    pinMode(PIN_EPM_IN1, OUTPUT);
    pinMode(PIN_EPM_IN2, OUTPUT);
    for (uint8_t i = 0; i < 6; i++) pinMode(PIN_CONTACT[i], INPUT_PULLUP);

    Wire.begin();
    Serial.begin(115200);
    while (!Serial && millis() < 3000); // wait up to 3 s for USB

    // Initial safe state: try release polarity
    pulse_epm_latch(false);

    Serial.println("DittoBot pulse driver ready. Type h for help.");
}

void loop() {
    handle_serial();
    face_update();
    // Watchdog: if loop stalls >2 s, flag it
    static uint32_t last_loop = 0;
    if (millis() - last_loop > 2000) {
        error_flags |= ERR_WATCHDOG;
    }
    last_loop = millis();
    delay(10);
}
