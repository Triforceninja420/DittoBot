// ====================================================================
// Project: DittoBot / Voxel Box
// Component: Release-coil pulse driver
// Target: Seeed Studio XIAO RP2040 (Dual ARM Cortex-M0+)
// Driver IC: TI DRV8871
// Variant: 25 mm cubic cell — Nd disc hold, coil is RELEASE only
//           NOT Phase 0 20 mm face
// Author: Craig Edward Ralls (2026)
// License: MIT
// ====================================================================

#include <Arduino.h>

// Driver H-Bridge Logic Pins (same IN1/IN2 map as the first pass)
const uint8_t PIN_EPM_IN1 = 0; // GPIO 0 -> H-Bridge IN1
const uint8_t PIN_EPM_IN2 = 1; // GPIO 1 -> H-Bridge IN2

// Start in the 50–200 ms band. Set from measured time-to-peak on the real coil.
// This pulse has to overpower the disc. It is not an Alnico-flip width.
const uint32_t SWITCH_PULSE_MS = 100;

/**
 * Pulses the coil around the Nd disc.
 * Hold is the disc. This pulse only has to buck it.
 * Immediately de-asserts driver inputs so static coil current is 0.
 *
 * @param engage TRUE  = opposite polarity (kept so you can find which way drops)
 *               FALSE = release polarity (buck the disc)
 */
void pulse_epm_latch(bool engage) {
    if (engage) {
        digitalWrite(PIN_EPM_IN1, HIGH);
        digitalWrite(PIN_EPM_IN2, LOW);
    } else {
        digitalWrite(PIN_EPM_IN1, LOW);
        digitalWrite(PIN_EPM_IN2, HIGH);
    }

    delay(SWITCH_PULSE_MS);

    // Quench — no continuous heating. Hold is the disc.
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
    // Face contact handshakes and lattice neighbor polling execute here
}