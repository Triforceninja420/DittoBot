#!/usr/bin/env python3
"""
DittoBot Phase 0 estimate (paper only)
Maxwell-style force estimate + simple I²R thermal rise.
NOT a full docking or shear simulation.
NOT a substitute for the locked measured gates in docs/PHASE0.md.

Design owned by Craig. 2026-11-06.
"""

import math

MU_0 = 4.0 * math.pi * 1e-7

def maxwell_force_n(b_t: float, area_m2: float) -> float:
    """Paper Maxwell stress force. Assumes uniform B."""
    return (b_t ** 2 * area_m2) / (2.0 * MU_0)

def thermal_rise_c(i_a: float, r_ohm: float, minutes: float, mass_g: float = 5.0, cp: float = 0.9) -> float:
    """Very rough adiabatic rise estimate. Ignores conduction to plate."""
    power_w = i_a ** 2 * r_ohm
    energy_j = power_w * minutes * 60.0
    mass_kg = mass_g / 1000.0
    # Specific heat ~0.9 J/g·K for copper-ish; this is intentionally crude.
    rise = energy_j / (mass_kg * cp * 1000.0)
    return rise

def main():
    print("=" * 60)
    print("DittoBot Phase 0 estimate — PAPER ONLY")
    print("Not a measured result. Not a full docking/shear sim.")
    print("Locked gates live in docs/PHASE0.md (measure on fixture).")
    print("=" * 60)

    # Example: Ø5 mm pole face, 1.2 T assumed (optimistic paper)
    area = math.pi * (0.0025 ** 2)  # Ø5 mm
    b = 1.2
    f = maxwell_force_n(b, area)
    print(f"Paper Maxwell force (Ø5 mm face @ {b} T): {f:.1f} N")
    print("(Phase 0 locked EPM ON gate is ≥ 3.0 N measured. 40 N shear is structure.)")

    print()
    # Thermal example: 1.25 A, 4 Ω coil, 10 min, rough 5 g thermal mass
    rise = thermal_rise_c(1.25, 4.0, 10.0)
    print(f"Crude adiabatic rise estimate (1.25 A, 4 Ω, 10 min, ~5 g): {rise:.0f} °C")
    print("(Single-strand continuous duty was flagged high in private analysis.")
    print(" Parallel-strand wind or pulse-only duty addresses it. Measure plate temp.)")

    print()
    print("See docs/SIM_NOTES.md for context.")
    print("Build the public fixture and measure. Credit follows data.")

if __name__ == "__main__":
    main()
