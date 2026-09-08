// ====================================================================
// Project: DittoBot / Voxel Box
// Component: Bi-Stable EPM Pulse Driver Routine
// Target: Seeed Studio XIAO RP2040 (Dual ARM Cortex-M0+)
// Driver IC: TI DRV8837C / Toshiba TC78H660
// Author: Craig Edward Ralls (2026)
// License: MIT
// ====================================================================

#include <Arduino.h>

// Driver H-Bridge Logic Pins
const uint8_t PIN_EPM_IN1 = 0; // GPIO 0 -> H-Bridge IN1
const uint8_t PIN_EPM_IN2 = 1; // GPIO 1 -> H-Bridge IN2

// Switching Threshold: Minimum dwell to flip Alnico 5 magnetic domains
const uint32_t SWITCH_PULSE_MS = 25;

/**
 * Pulses the excitation coil to invert Alnico polarization.
 * Immediately de-asserts driver inputs to guarantee 0.0W static draw.
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
    
    // Quench driver outputs (Coast / Low) - eliminates continuous heating
    digitalWrite(PIN_EPM_IN1, LOW);
    digitalWrite(PIN_EPM_IN2, LOW);
}

void setup() {
    pinMode(PIN_EPM_IN1, OUTPUT);
    pinMode(PIN_EPM_IN2, OUTPUT);
    
    // Establish initial safe state (flux canceled / release mode)
    pulse_epm_latch(false);
}

void loop() {
    // Face contact handshakes and lattice neighbor polling execute here
}
