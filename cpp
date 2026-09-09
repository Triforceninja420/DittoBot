// ====================================================================
// Project: DittoBot / Voxel Box
// Component: Bi-Stable EPM Pulse Driver Routine
// Target: Seeed Studio XIAO RP2040 (Dual ARM Cortex-M0+)
// Driver IC: TI DRV8871 (revision target). DRV8837C is first-pass only.
// Variant: 25 mm cubic cell — NOT Phase 0 20 mm face
// Author: Craig Edward Ralls (2026)
// License: MIT
// ====================================================================

#include <Arduino.h>

// Driver H-Bridge Logic Pins (same IN1/IN2 map as the first pass)
const uint8_t PIN_EPM_IN1 = 0; // GPIO 0 -> H-Bridge IN1
const uint8_t PIN_EPM_IN2 = 1; // GPIO 1 -> H-Bridge IN2

// Start here. Stretch only after you measure time-to-peak current on the real coil.
// First-pass 25 ms @ 1.2 A through 120 t does not switch Alnico 5 on a 4 mm path.
const uint32_t SWITCH_PULSE_MS = 25;

/**
 * Pulses the excitation coil to invert Alnico polarization.
 * Immediately de-asserts driver inputs so static coil current is 0.
 *
 * @param engage TRUE to align fields (Latch), FALSE to cancel external flux (Release)
 */
void pulse_epm_latch(bool engage) {
    if (engage) {
        // Forward polarity: Alnico aligns parallel to NdFeB
        digitalWrite(PIN_EPM_IN1, HIGH);
        digitalWrite(PIN_EPM_IN2, LOW);
    } else {
        // Reverse polarity: Alnico opposes NdFeB, shunting flux internally
        digitalWrite(PIN_EPM_IN1, LOW);
        digitalWrite(PIN_EPM_IN2, HIGH);
    }

    delay(SWITCH_PULSE_MS);

    // Quench — no continuous heating, hold is remanence only
    digitalWrite(PIN_EPM_IN1, LOW);
    digitalWrite(PIN_EPM_IN2, LOW);
}

void setup() {
    pinMode(PIN_EPM_IN1, OUTPUT);
    pinMode(PIN_EPM_IN2, OUTPUT);

    // Initial safe state: release / flux canceled
    pulse_epm_latch(false);
}

void loop() {
    // Face contact handshakes and lattice neighbor polling execute here
}