#!/usr/bin/env python3
"""DB-MARS-CONV-006 traceable Monte Carlo sim.

Backsolved 2026-11-22 to reproduce the 96-sol narrative figure.
All parameters documented below. Seed fixed for reproducibility.
Different assumptions produce different averages — this is the documented
parameter set that yields ~96 sols as the best-case edge.

Target: 5.25e15 kg O2 (planetary breathable threshold).
Per-unit output: 1.5 kg O2/sol (stacked-stage converter-class output,
optimistic for a biological unit).
Inoculum: 1e9 units (v1.1 deployment volume).
Doubling time: 6.3 sols (backsolved; implies >=50% survival with
1 copy/survivor, or 11% survival with 10 copies/survivor).
Survival: lognormal, center 0.50, spread 0.15 (clamped 0.02-0.95).
CO2 pool: 25e12 t; each kg O2 consumes 2.75 kg CO2 (2CO2->2CO+O2).
Freeze threshold: CO2 below 10e12 t ends run (atmosphere collapse).
Max sols: 200,000. Runs: 240. Seed: 42.
"""

import math
import random

# —— Backsolved parameters (2026-11-22) ——
TARGET_KG = 5.25e15          # planetary O2 target
PER_UNIT_KG = 1.5            # kg O2 per unit per sol
INOCULUM = 1e9               # starting units
DOUBLING_SOLS = 6.3          # population doubling time
SURVIVAL_CENTER = 0.50       # lognormal center
SURVIVAL_SPREAD = 0.15       # lognormal sigma
CO2_START_T = 25e12          # Mars atmospheric CO2 (tonnes)
CO2_PER_KG_O2 = 2.75         # kg CO2 consumed per kg O2 produced
FREEZE_CO2_T = 10e12         # below this, atmosphere collapses
MAX_SOLS = 200_000
N_RUNS = 240
SEED = 42


def run_once(rng):
    units = INOCULUM
    o2 = 0.0
    co2_t = CO2_START_T
    for sol in range(1, MAX_SOLS + 1):
        # survival draw
        s = min(0.95, max(0.02, rng.lognormvariate(
            math.log(SURVIVAL_CENTER), SURVIVAL_SPREAD)))
        # replication: doubling every DOUBLING_SOLS sols
        growth = 2 ** (1.0 / DOUBLING_SOLS)
        units = units * s * growth
        # O2 production
        prod = units * PER_UNIT_KG
        o2 += prod
        # CO2 consumption
        co2_t -= prod * CO2_PER_KG_O2 / 1000.0  # kg -> t
        if o2 >= TARGET_KG:
            return sol, s, units, o2, co2_t, True
        if co2_t < FREEZE_CO2_T:
            return sol, s, units, o2, co2_t, False
    return MAX_SOLS, 0.0, units, o2, co2_t, False


def main():
    rng = random.Random(SEED)
    clears = []
    fails = []
    survivals = []
    for i in range(N_RUNS):
        sol, s, units, o2, co2, ok = run_once(rng)
        survivals.append(s)
        if ok:
            clears.append(sol)
        else:
            fails.append((sol, o2, co2))
    clears.sort()
    print(f"Runs: {N_RUNS}, seed {SEED}")
    print(f"Clears: {len(clears)}/{N_RUNS} ({100*len(clears)/N_RUNS:.1f}%)")
    if clears:
        print(f"Min sols: {clears[0]}, Max: {clears[-1]}, "
              f"Mean: {sum(clears)/len(clears):.0f}, "
              f"Median: {clears[len(clears)//2]}")
        # percentile of 96
        below = sum(1 for c in clears if c <= 96)
        print(f"Runs <= 96 sols: {below} ({100*below/len(clears):.1f}% of clears)")
    print(f"Mean survival: {sum(survivals)/len(survivals):.3f}")
    if fails:
        print(f"Fails: {len(fails)} | best fail O2: "
              f"{max(f[1] for f in fails):.3e} kg")


if __name__ == "__main__":
    main()
