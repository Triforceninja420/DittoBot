#!/usr/bin/env python3
"""
DittoBot Phase 0 estimate (paper only)
Maxwell-style force estimate + simple I²R thermal rise.
NOT a full docking or shear simulation.
NOT a substitute for the locked measured gates in docs/PHASE0.md.

Design owned by Craig. 2026-11-06.
Updated 2026-11-21: stale Ø5 mm Alnico/NdFeB hybrid example replaced with
current 30 mm dual-cam Phase 0 numbers (NdFeB N52 Ø6×6, 40 turns 34 AWG).
Updated 2026-11-23: Phase 0 face size committed at 20 mm (was 30 mm). Estimate
inputs and outputs unchanged.
"""

import math

MU_0 = 4.0 * math.pi * 1e-7

def maxwell_force_n(b_t: float, area_m2: float) -> float:
    """Paper Maxwell stress force. Assumes uniform B."""
    return (b_t ** 2 * area_m2) / (2.0 * MU_0)

def thermal_rise_c(i_a: float, r_ohm: float, minutes: float, mass_g: float = 7.4, cp: float = 0.9) -> float:
    """Very rough adiabatic rise estimate. Ignores conduction to plate."""
    power_w = i_a ** 2 * r_ohm
    energy_j = power_w * minutes * 60.0
    mass_kg = mass_g / 1000.0
    rise = energy_j / (mass_kg * cp * 1000.0)
    return rise

def main():
    print("=" * 60)
    print("DittoBot Phase 0 estimate — PAPER ONLY")
    print("Not a measured result. Not a full docking/shear sim.")
    print("Locked gates live in docs/PHASE0.md (measure on fixture).")
    print("=" * 60)

    # Current Phase 0: NdFeB N52 Ø6 mm pole face, 1.2 T assumed (optimistic paper)
    area = math.pi * (0.003 ** 2)  # Ø6 mm
    b = 1.2
    f = maxwell_force_n(b, area)
    print(f"Paper Maxwell force (Ø6 mm face @ {b} T): {f:.1f} N")
    print("(Phase 0 locked snap gate is 34.6 N simulated; 40 N shear is pin structure.)")

    print()
    # Thermal example: 1.25 A, 0.75 Ω coil (40 turns 34 AWG), 10 min, ~7.4 g module
    rise = thermal_rise_c(1.25, 0.75, 10.0)
    print(f"Crude adiabatic rise estimate (1.25 A, 0.75 Ω, 10 min, ~7.4 g): {rise:.0f} °C")
    print("(Pulse-duty is the default; this continuous-duty case is the stress test.)")
    print(" Measure plate temp on the real article.")

    print()
    print("See docs/SIM_NOTES.md for context.")
    print("Build the public fixture and measure. Credit follows data.")

if __name__ == "__main__":
    main()
