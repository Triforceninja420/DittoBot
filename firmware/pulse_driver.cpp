// ====================================================================
// Project: DittoBot / Voxel Box
// Component: Release-coil pulse driver
// Target: Seeed Studio XIAO RP2040 (Dual ARM Cortex-M0+)
// Driver IC: TI DRV8871 (VM 6.5–45 V abs max; prefer ≤42 V from pulse bank)
// Variant: 25 mm cubic cell — SmCo 2:17 Ø7.5 mm residual hold, coil is RELEASE only
//           NOT Phase 0 30 mm dual-cam face (rev 2026-11-21)
// Author: Craig Edward Ralls (2026)
// License: MIT
// Baseline: 2026-11-19 (pulse-only + thermal governor stub)
// ====================================================================

#include <Arduino.h>

// Driver H-Bridge Logic Pins
const uint8_t PIN_EPM_IN1 = 0; // GPIO 0 -> H-Bridge IN1
const uint8_t PIN_EPM_IN2 = 1; // GPIO 1 -> H-Bridge IN2

// Start in the 50–200 ms band. Set from measured time-to-peak on the real coil.
// This pulse only has to buck the residual field of the SmCo disc.
const uint32_t SWITCH_PULSE_MS = 100;

// Thermal governor stub — replace with real plate-temperature sensor (NTC / TMP117 / etc.).
// Returns true if a pulse is allowed. Refuse continuous or high-cadence duty when hot
bool thermal_ok() {
    // TODO: read actual temperature and return false if above threshold (e.g. 60–70 °C plate).
    // Placeholder always allows for first articles.
    return true;
}

/**
 * Pulses the coil around the SmCo disc.
 * Hold is the residual of the disc. This pulse only releases.
 * Immediately de-asserts driver inputs so static coil current is 0.
 *
 * @param engage TRUE  = opposite polarity (find which way drops)
 *               FALSE = release polarity (buck the residual)
 */
void pulse_epm_latch(bool engage) {
    if (!thermal_ok()) {
        // Refuse pulse if thermal governor says no.
        // Optional: log or set an error flag.
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

    // Quench — no continuous heating. Hold is the SmCo residual.
    digitalWrite(PIN_EPM_IN1, LOW);
    digitalWrite(PIN_EPM_IN2, LOW);
}

void setup() {
    pinMode(PIN_EPM_IN1, OUTPUT);
    pinMode(PIN_EPM_IN2, OUTPUT);

    // Initial safe state: try release polarity
    pulse_epm_latch(false);
}

void loop() {
    // Face contact handshakes and lattice neighbor polling execute here.
    // Call thermal_ok() before any sustained pulse train.
}
