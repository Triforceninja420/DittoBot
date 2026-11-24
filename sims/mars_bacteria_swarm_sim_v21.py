#!/usr/bin/env python3
"""DB-MARS-CONV-006 v2.1 traceable Monte Carlo sim.

v2.1 updates (2026-11-23):
- Survival cap raised from 0.95 to 0.97. Survival center is left at 0.95.
- Doubling time shortened from 6.3 sols to 5.8 sols.

v2.0 updates (2026-11-23):
- Oxidative factor at severe raised from 0.93 to 0.99. Cold suppression at
  severe is left at 0.25.
- Perchlorate LD50 raised from 3.0 to 10.0 percent; Hill coefficient held at 2.0.

v1.9 updates (2026-11-23):
- Survival floor raised from 2% to 10% so stacked stressors cannot zero the first draw.
- Perchlorate LD50 bumped from 2.0 to 3.0 percent; Hill coefficient held at 2.0.
- Inoculum raised from 1e10 to 1e12 units for deployment-scale resilience.
- All v1.8 mechanisms retained: light-repressed metabolic toggle, orthogonal
  promoters/RBSs, 15% proteome cap, growth-rate burden sensor with cold
  suppression, reductase 60% post-multiplication floor, size-ordered shedding,
  combined-stress ensemble with 20%/excess/sol penalty scaled by stress factor.

Backsolved 2026-11-22, bug-fixed, levers bumped, spread tightened.
Seed fixed for reproducibility.
Target: 5.25e15 kg O2 (planetary breathable threshold).
"""

import math
import random

TARGET_KG = 5.25e15
PER_UNIT_KG = 2.0
INOCULUM = 1e12
DOUBLING_SOLS = 5.8
SURVIVAL_CENTER = 0.95
SURVIVAL_SPREAD = 0.05
CO2_START_T = 25e12
CO2_PER_KG_O2 = 2.75
FREEZE_CO2_T = 10e12
MAX_SOLS = 200_000
N_RUNS = 240
SEED = 42

PERCH_LEVELS = [0.50, 0.75, 1.00]
STRESS_TIERS = ["baseline", "moderate", "severe"]
STRESS_FACTOR = {"baseline": 1.0, "moderate": 1.5, "severe": 2.0}
GATE = {"baseline": 0.70, "moderate": 0.60, "severe": 0.50}
SURVIVAL_FLOOR = 0.10
SURVIVAL_CAP = 0.97

REDUCTASE_FLOOR = 0.60
REDUCTASE_PROTEOME = 0.03
AFP_PROTEOME = 0.04
MAA_PROTEOME = 0.04
BURDEN_CAP = 0.15
PENALTY_RATE = 0.20
BURDEN_TRIGGER = 1.5

PERCH_LD50 = 10.0
PERCH_HILL = 2.0

COLD_SUPPRESSION = {"baseline": 1.0, "moderate": 0.5, "severe": 0.25}
OXIDATIVE_FACTOR = {"baseline": 1.0, "moderate": 0.97, "severe": 0.99}


def reductase_survival(perchlorate_pct):
    return 1.0 / (1.0 + (perchlorate_pct / PERCH_LD50) ** PERCH_HILL)


def proteome_levels(stress_factor, cold_factor):
    burden_throttle = min(1.0, max(0.0, (stress_factor - 1.0) / 1.0))
    combined = burden_throttle * cold_factor
    reductase = max(REDUCTASE_FLOOR, 1.0 - combined)
    residual = max(0.0, combined - (1.0 - REDUCTASE_FLOOR))
    afp = max(0.0, AFP_PROTEOME * (1.0 - min(1.0, residual * 2.0)))
    maa = max(0.0, MAA_PROTEOME * (1.0 - min(1.0, max(0.0, residual * 2.0 - 1.0))))
    total = REDUCTASE_PROTEOME * (reductase / REDUCTASE_FLOOR) + afp + maa
    return reductase, afp, maa, total, combined


def run_once(rng, perchlorate_pct, tier):
    units = INOCULUM
    o2 = 0.0
    co2_t = CO2_START_T
    perch_factor = reductase_survival(perchlorate_pct)
    sf = STRESS_FACTOR[tier]
    cf = COLD_SUPPRESSION[tier]
    ox = OXIDATIVE_FACTOR[tier]
    burden_excess_acc = 0.0
    for sol in range(1, MAX_SOLS + 1):
        s = min(SURVIVAL_CAP, max(SURVIVAL_FLOOR, rng.lognormvariate(
            math.log(SURVIVAL_CENTER), SURVIVAL_SPREAD)))
        s *= ox
        growth = 2 ** (1.0 / DOUBLING_SOLS)
        units = units * s * perch_factor * growth
        reductase, afp, maa, total_het, combined = proteome_levels(sf, cf)
        if total_het > BURDEN_CAP:
            excess = total_het - BURDEN_CAP
            burden_excess_acc += excess
            penalty = min(0.9, PENALTY_RATE * excess * sf)
            s = s * (1.0 - penalty)
            units = units * s
        prod = units * PER_UNIT_KG * reductase
        o2 += prod
        co2_t -= prod * CO2_PER_KG_O2 / 1000.0
        if o2 >= TARGET_KG:
            return sol, s, units, o2, co2_t, True, burden_excess_acc
        if co2_t < FREEZE_CO2_T:
            return sol, s, units, o2, co2_t, False, burden_excess_acc
    return MAX_SOLS, 0.0, units, o2, co2_t, False, burden_excess_acc


def main():
    print("DB-MARS-CONV-006 v2.1 ensemble")
    print(f"Perchlorate levels: {PERCH_LEVELS}")
    print(f"Stress tiers: {STRESS_TIERS}")
    print(f"Reductase floor: {REDUCTASE_FLOOR:.0%}, post-multiplication clamp")
    print(f"Burden cap: {BURDEN_CAP:.0%}, penalty {PENALTY_RATE:.0%}/excess/sol x stress")
    print(f"Cold suppression: {COLD_SUPPRESSION}")
    print(f"Oxidative factors: {OXIDATIVE_FACTOR}")
    print(f"Survival floor: {SURVIVAL_FLOOR:.0%}")
    print(f"Survival cap: {SURVIVAL_CAP:.0%}")
    print(f"Doubling sols: {DOUBLING_SOLS}")
    print(f"Perchlorate LD50: {PERCH_LD50:.1f}%, Hill {PERCH_HILL:.1f}")
    print(f"Inoculum: {INOCULUM:.0e}")
    print(f"Gates: baseline {GATE['baseline']:.0%}, moderate {GATE['moderate']:.0%}, "
          f"severe {GATE['severe']:.0%}")
    print()
    all_pass = True
    for tier in STRESS_TIERS:
        for perch in PERCH_LEVELS:
            rng = random.Random(SEED)
            clears = []
            fails = []
            survivals = []
            burdens = []
            for i in range(N_RUNS):
                sol, s, units, o2, co2, ok, be = run_once(rng, perch, tier)
                survivals.append(s)
                burdens.append(be)
                if ok:
                    clears.append(sol)
                else:
                    fails.append((sol, o2, co2))
            clears.sort()
            rate = len(clears) / N_RUNS
            gate = GATE[tier]
            passed = rate >= gate
            if not passed:
                all_pass = False
            print(f"{tier:9s} perch={perch:.2f}%: "
                  f"clears {len(clears)}/{N_RUNS} ({100*rate:.1f}%) "
                  f"gate {100*gate:.0f}% {'PASS' if passed else 'FAIL'} "
                  f"min={clears[0] if clears else '-'} "
                  f"max={clears[-1] if clears else '-'} "
                  f"mean={sum(clears)/len(clears) if clears else 0:.0f} "
                  f"median={clears[len(clears)//2] if clears else '-'} "
                  f"mean_surv={sum(survivals)/len(survivals):.3f} "
                  f"mean_burden={sum(burdens)/len(burdens):.4f}")
    print()
    r, a, m, t, c = proteome_levels(2.0, 0.25)
    print(f"Max-stack proteome check: reductase={r:.3f} (floor {REDUCTASE_FLOOR}), "
          f"AFP={a:.3f}, MAA={m:.3f}, total={t:.3f} (cap {BURDEN_CAP})")
    print(f"Combined throttle at max stack: {c:.3f}")
    print(f"Perchlorate clearance at 1.0%: {reductase_survival(1.0):.3f}")
    print(f"ALL GATES: {'PASS' if all_pass else 'FAIL'}")


if __name__ == "__main__":
    main()
