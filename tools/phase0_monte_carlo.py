#!/usr/bin/env python3
"""Phase 0 Monte Carlo docking simulation (DB-P0-MC-001).

100 000 seeded trials. T3 shear gate now uses tightened acceptance window:
  - lateral offset ≤ 1.0 mm
  - relative velocity ≤ 0.25 m/s

Paper estimate only. Credit follows measured data.
"""

import random
from statistics import mean, median

# Locked Phase 0 targets (see docs/PHASE0.md)
T1_SOFT_DOCK = 0.90          # ≥ 90 % at ≤ 2.5 mm
T2_HARD_LOCK = 0.95          # ≥ 95 % both pins seated
T3_SHEAR_N = 40.0            # ≥ 40 N through pins
T4_CURRENT_A = 1.25          # 1.25 A ≥ 10 min
T5_CYCLES = 2000             # 2 000 dock/undock

# Tightened T3 acceptance window
T3_LAT_LIMIT_MM = 1.0
T3_VEL_LIMIT_MS = 0.25

N_TRIALS = 100_000
SEED = 42

def run_trial(rng):
    # Sample approach parameters
    vel = rng.uniform(0.05, 0.60)          # m/s
    lat = rng.uniform(0.0, 2.5)            # mm
    spring = rng.gauss(4.98, 0.45)         # N (capture spring)
    spring = max(3.5, min(6.5, spring))

    # Soft-dock (T1)
    t1 = lat <= 2.5 and rng.random() < 0.9998

    # Hard-lock (T2)
    t2 = t1 and rng.random() < 0.9941

    # Shear (T3) — tightened window
    # Effective shear degrades with velocity and lateral offset
    shear_base = 45.0
    shear_eff = shear_base * (1.0 - 0.35 * (vel / 0.5)) * (1.0 - 0.55 * (lat / 2.0))
    shear_eff += 0.8 * (spring - 4.0)   # spring seating credit
    t3 = (lat <= T3_LAT_LIMIT_MM and
          vel <= T3_VEL_LIMIT_MS and
          shear_eff >= T3_SHEAR_N)

    # Current (T4) and cycles (T5) — near-certain on paper
    t4 = rng.random() < 0.9939
    t5 = rng.random() < 0.9996

    all_pass = t1 and t2 and t3 and t4 and t5

    return {
        "t1": t1, "t2": t2, "t3": t3, "t4": t4, "t5": t5,
        "all": all_pass,
        "vel": vel, "lat": lat, "spring": spring, "shear_eff": shear_eff
    }

def main():
    rng = random.Random(SEED)
    results = [run_trial(rng) for _ in range(N_TRIALS)]

    counts = {k: sum(r[k] for r in results) for k in ("t1", "t2", "t3", "t4", "t5", "all")}

    print(f"T1 pass:  {100 * counts['t1'] / N_TRIALS:6.2f}%")
    print(f"T2 pass:  {100 * counts['t2'] / N_TRIALS:6.2f}%")
    print(f"T3 pass:  {100 * counts['t3'] / N_TRIALS:6.2f}%")
    print(f"T4 pass:  {100 * counts['t4'] / N_TRIALS:6.2f}%")
    print(f"T5 pass:  {100 * counts['t5'] / N_TRIALS:6.2f}%")
    print(f"ALL-PASS: {100 * counts['all'] / N_TRIALS:6.2f}%")

    t3_fails = [r for r in results if not r["t3"]]
    print(f"\nT3 FAILS: {len(t3_fails)} ({100 * len(t3_fails) / N_TRIALS:.2f}%)")

    if t3_fails:
        # Rank by composite score (higher = worse)
        def score(r):
            return (r["vel"] / T3_VEL_LIMIT_MS) + (r["lat"] / T3_LAT_LIMIT_MM) + (5.0 - r["spring"]) / 2.0

        t3_fails.sort(key=score, reverse=True)
        print("\nTop 10 T3 fails by relative velocity / lateral offset / spring deficit:")
        print(f"{'#':>3} {'vel m/s':>8} {'lat mm':>7} {'spring N':>9} {'shear_eff N':>12} {'score':>6}")
        for i, r in enumerate(t3_fails[:10], 1):
            print(f"{i:3d} {r['vel']:8.3f} {r['lat']:7.3f} {r['spring']:9.2f} {r['shear_eff']:12.2f} {score(r):6.2f}")

        vels = [r["vel"] for r in t3_fails]
        lats = [r["lat"] for r in t3_fails]
        springs = [r["spring"] for r in t3_fails]
        print(f"\nT3-fail means:   vel {mean(vels):.3f} m/s, lat {mean(lats):.3f} mm, spring {mean(springs):.2f} N")
        print(f"T3-fail medians: vel {median(vels):.3f} m/s, lat {median(lats):.3f} mm, spring {median(springs):.2f} N")

if __name__ == "__main__":
    main()
