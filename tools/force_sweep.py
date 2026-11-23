#!/usr/bin/env python3
"""
Project: DittoBot / Voxel Box
Component: Maxwell Stress Tensor paper sweep (WARNING ONLY)
Variant: 25 mm cubic cell — NOT Phase 0 20 mm face
Author: Craig Edward Ralls (2026)
License: MIT

This prints PAPER force from assumed B, not a measured latch.
Current baseline (2026-11-23): Nd disc Ø6.0×2–3 mm residual hold, coil release only.
Older SmCo Ø7.5 and Alnico flip numbers are superseded.
Measure real ON/OFF force and I_release. Do not use this sweep as spec.
28.8 N is retired.
"""

import numpy as np

MU_0 = 4.0 * np.pi * 1e-7
BR_ND = 1.22  # typical NdFeB N52
CORE_RADIUS_M = 0.003  # Ø6.0 mm current baseline
CORE_AREA_M2 = np.pi * (CORE_RADIUS_M ** 2)
PATH_LEN_M = 0.004

def calculate_magnetic_force(air_gap_mm: float, residual: bool = True) -> float:
    """Paper Maxwell stress from assumed remanence * gap decay. Not a test."""
    air_gap_m = air_gap_mm * 1e-3
    reluctance_decay = np.exp(-air_gap_m / 0.001)

    b_effective = BR_ND * reluctance_decay if residual else 0.1 * reluctance_decay
    force_newtons = (b_effective ** 2 * CORE_AREA_M2) / (2.0 * MU_0)
    return round(force_newtons, 3)

def run_verification_sweep():
    print("=" * 64)
    print("DittoBot / Voxel Box: PAPER residual-hold force sweep (25 mm cell)")
    print("Not a measured force. Not Phase 0.")
    print("Current baseline 2026-11-23: Nd disc Ø6.0×2–3 mm residual hold, coil release only.")
    print("Measure real ON N (coil off) / OFF N (after pulse) / I_release on a fixture.")
    print(f"Paper core diameter: {CORE_RADIUS_M * 2000:.1f} mm | Static hold power: 0.00 W")
    print("=" * 64)
    print(f"{'Gap (mm)':<10} | {'Paper residual (N)':<20}")
    print("-" * 64)

    for gap in (0.05, 0.10, 0.20, 0.50):
        f = calculate_magnetic_force(gap, residual=True)
        print(f"{gap:<10.2f} | {f:<20.2f}")

    print("=" * 64)
    print("Paper only. Credit follows measured data in MEASUREMENT_CARD.md.")

if __name__ == "__main__":
    run_verification_sweep()
