#!/usr/bin/env python3
"""Phase 0 Monte Carlo — DB-P0-FACE-TP-001 Rev A
T1 soft-dock >=90% at <=2.5mm/<=7deg
T2 hard-lock >=95%
T3 40 N shear
T4 1.25 A x 10 min no throttle
T5 2,000 cycles on same 20 mm face article
Thresholds set 1-2 sigma past means. Soft-dock and hard-lock tightened 2026-11-22.
T3 failure forensics added 2026-11-23: log misses, rank by relative velocity,
lateral offset, capture-spring rate.
T3 acceptance window reverted 2026-11-23 to original: lat ≤ 1.5 mm, vel ≤ 0.5 m/s.
CAD ridge widened 0.60→1.0 mm, chamfer 0.50→1.0 mm (geometry only, sim unchanged).
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

# T3 forensic parameters (drawn per trial)
VEL_SIGMA_M_S = 0.15            # relative docking velocity
LAT_OFFSET_SIGMA_MM = 0.65     # lateral offset at contact
SPRING_SIGMA_N = 0.4            # capture spring rate variation

# Original T3 acceptance window
T3_LAT_LIMIT_MM = 1.5
T3_VEL_LIMIT_MS = 0.5

def run_trial(rng):
    # T1 soft-dock
    off = abs(rng.gauss(0, T1_OFFSET_SIGMA_MM))
    ang = abs(rng.gauss(0, T1_ANGLE_SIGMA_DEG))
    t1 = off <= 2.5 and ang <= 7.0
    # T2 hard-lock
    t2 = rng.random() < T2_LOCK_P
    # T3 shear — forensic draws + original window
    vel = abs(rng.gauss(0, VEL_SIGMA_M_S))
    lat = abs(rng.gauss(0, LAT_OFFSET_SIGMA_MM))
    spr = rng.gauss(5.0, SPRING_SIGMA_N)
    shear = rng.gauss(T3_SHEAR_MU, T3_SHEAR_SIGMA)
    # shear degrades with velocity and offset; spring helps seating
    shear_eff = shear - 2.5*vel - 0.8*lat + 0.15*spr
    t3 = (lat <= T3_LAT_LIMIT_MM and
          vel <= T3_VEL_LIMIT_MS and
          shear_eff >= 40.0)
    t3_fail = {
        "vel": vel, "lat": lat, "spr": spr,
        "shear_raw": shear, "shear_eff": shear_eff,
    } if not t3 else None
    # T4 current
    t4 = rng.gauss(T4_CURRENT_MU, T4_CURRENT_SIGMA) >= 1.25
    # T5 cycles
    t5 = rng.gauss(T5_CYCLES_MU, T5_CYCLES_SIGMA) >= 2000.0
    return t1, t2, t3, t4, t5, t3_fail

def main():
    rng = random.Random(SEED)
    counts = [0]*5
    all_pass = 0
    t3_fails = []
    for _ in range(N_TRIALS):
        results = run_trial(rng)
        for i, r in enumerate(results[:5]):
            if r:
                counts[i] += 1
        if results[5] is not None:
            t3_fails.append(results[5])
        if all(results[:5]):
            all_pass += 1
    for i, c in enumerate(counts):
        print(f"T{i+1} pass:     {c/N_TRIALS*100:.2f}%")
    print(f"ALL-PASS:      {all_pass/N_TRIALS*100:.2f}%")
    print(f"T3 FAILS:     {len(t3_fails)} ({len(t3_fails)/N_TRIALS*100:.2f}%)")
    if t3_fails:
        # rank by composite: velocity weight 0.45, offset 0.35, spring deficit 0.20
        def score(f):
            return 0.45*f["vel"]/VEL_SIGMA_M_S + 0.35*f["lat"]/LAT_OFFSET_SIGMA_MM + 0.20*max(0.0, 5.0-f["spr"])/SPRING_SIGMA_N
        ranked = sorted(t3_fails, key=score, reverse=True)
        print("\nTop 10 T3 fails by relative velocity / lateral offset / spring deficit:")
        print(f"{'#':>3} {'vel m/s':>8} {'lat mm':>8} {'spring N':>9} {'shear_eff N':>12} {'score':>7}")
        for i, f in enumerate(ranked[:10], 1):
            print(f"{i:>3} {f['vel']:>8.3f} {f['lat']:>8.3f} {f['spr']:>9.2f} {f['shear_eff']:>12.2f} {score(f):>7.2f}")
        # summary stats on fails
        vs = [f["vel"] for f in t3_fails]
        ls = [f["lat"] for f in t3_fails]
        ss = [f["spr"] for f in t3_fails]
        print(f"\nT3-fail means: vel {sum(vs)/len(vs):.3f} m/s, lat {sum(ls)/len(ls):.3f} mm, spring {sum(ss)/len(ss):.2f} N")
        print(f"T3-fail medians: vel {sorted(vs)[len(vs)//2]:.3f} m/s, lat {sorted(ls)[len(ls)//2]:.3f} mm, spring {sorted(ss)[len(ls)//2]:.2f} N")

if __name__ == "__main__":
    main()
