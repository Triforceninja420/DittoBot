#!/usr/bin/env python3
"""Phase 0 Monte Carlo — DB-P0-FACE-TP-001 Rev A
T1 soft-dock >=90% at <=2.5mm/<=7deg
T2 hard-lock >=95%
T3 40 N shear
T4 1.25 A x 10 min no throttle
T5 2,000 cycles on same 20 mm face article
Thresholds set 1-2 sigma past means. Soft-dock and hard-lock tightened 2026-11-22.
"""
import random, math

N_TRIALS = 100_000
SEED = 7

# --- Tolerances (sigma) ---
T1_OFFSET_SIGMA_MM = 0.65      # was 1.0
T1_ANGLE_SIGMA_DEG = 1.6       # was 2.5
T2_LOCK_P = 0.994              # was 0.95
T3_SHEAR_MU, T3_SHEAR_SIGMA = 48.0, 4.0   # 40 N threshold, 2 sigma margin
T4_CURRENT_MU, T4_CURRENT_SIGMA = 1.5, 0.1  # 1.25 A threshold
T5_CYCLES_MU, T5_CYCLES_SIGMA = 2500.0, 150.0  # 2000 cycle threshold

def run_trial(rng):
    # T1 soft-dock
    off = abs(rng.gauss(0, T1_OFFSET_SIGMA_MM))
    ang = abs(rng.gauss(0, T1_ANGLE_SIGMA_DEG))
    t1 = off <= 2.5 and ang <= 7.0
    # T2 hard-lock
    t2 = rng.random() < T2_LOCK_P
    # T3 shear
    t3 = rng.gauss(T3_SHEAR_MU, T3_SHEAR_SIGMA) >= 40.0
    # T4 current
    t4 = rng.gauss(T4_CURRENT_MU, T4_CURRENT_SIGMA) >= 1.25
    # T5 cycles
    t5 = rng.gauss(T5_CYCLES_MU, T5_CYCLES_SIGMA) >= 2000.0
    return t1, t2, t3, t4, t5

def main():
    rng = random.Random(SEED)
    counts = [0 0 1 2 3 4]/N_TRIALS*100:.2f}%")
    print(f"ALL-PASS:      {all_pass/N_TRIALS*100:.2f}%")

if __name__ == "__main__":
    main()