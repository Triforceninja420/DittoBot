# Honesty Note — Residual Failures in DB-MARS-CONV-006 v2.13

**Date:** 2026-11-27  
**Sim:** `sims/mars_bacteria_swarm_sim_v2_13.py` (v2.12 + near-extinction dormancy recovery)  
**Status:** Documented residual. Not forced. Scored A remains the control.  
**Run:** default `main()`, seed 42, INOCULUM 1e12, scav 5e-3, DOUBLING_SOLS 8.72, habitat and adaptive on, throttle mode, N=240, 12 cells.

## What changed in v2.13

One mechanic, no other sim number changed. A dormant, spore-like (akinete) pool:

| Constant | Value | Meaning |
|---|---|---|
| `EXTINCTION_RECOVERY_ENABLED` | True | toggle for controls |
| `EXTINCTION_RECOVERY_THRESHOLD` | 1e6 units | live population that triggers germination |
| `DORMANT_FRACTION` | 1e-4 | share of each sol's dying cells that enter dormancy |
| `DORMANT_SURVIVAL_PER_SOL` | 0.9999 | pool decay (~6,900 sols, ~19 Earth-yr half-life); the pool never grows |
| `DORMANT_GERMINATION_FRACTION` | 0.5 | share of the pool that germinates per firing (and leaves the pool) |
| `EXTINCTION_RECOVERY_MAX` | 3 | firings per run |
| `EXTINCTION_RECOVERY_COOLDOWN_SOLS` | 1000 | minimum sols between firings |

The pool is taken from the 20% of dead biomass that `RECYCLE_FRACTION` already counts as lost, so it is not free population and no nutrient is double counted. At steady state it is about 8% of the live population. It uses no RNG draws.

## What clears cleanly

- Scored A (combined, overrides on): 12/12 cells, 2880/2880, 240/240 in every cell. ALL GATES PASS. Freeze crossings 0/2880.
- Recovery never fired in scored A. `main()` re-runs A with recovery off: 0/2880 runs differ bit-exact. Scored-A biology is untouched.
- E4 P-import fallback and E5 vent mode: 2880/2880. E2/E3 CO2-ordering check changed 0/12 cells.
- The REF-vs-v2.9 bit-exact CONTROL runs with recovery off. It still differs on 1920/2880, as in v2.12, because of the 0.62 floor and the thermal buffer. Recovery adds nothing to that mismatch.

## Correction to the v2.11 and v2.12 notes

The v2.11 note's "48 misses / 2832/2880 with overrides off" was v2.11's **A-low** result, not its no-override result. A re-run of v2.11 on 2026-11-27 puts its real no-override (config C) result at **45 misses / 2835**. The v2.12 note said v2.12 closed 5 of 48. The like-for-like change was 45 → 43, so it closed **2**.

## Residual, v2.11 → v2.12 → v2.13 (N=240, misses out of 2880)

| Config | v2.11 | v2.12 | v2.13 |
|---|---|---|---|
| A scored | 0 | 0 | 0 |
| C no-override (ox 0.97) | 45 | 43 | **19** (2861) |
| A-low | 48 | 46 | **18** (2862) |
| A-high | 37 | 35 | **14** (2866) |
| REF (neither lever) | 63 | 60 | **34** (2846) |
| B (scav 1e-3) | 12 | 12 | **3** (2877) |

All configs still pass 12/12 cells.

## What still misses (v2.13)

C no-override, by cell:

- moderate 0.50%: 236/240 (3 timeout, 1 extinct)
- moderate 0.75%: 237/240 (2 timeout, 1 extinct)
- moderate 1.00%: 237/240 (2 timeout, 1 extinct)
- moderate 1.50%: 235/240 (4 timeout, 1 extinct)
- severe 1.50%: 236/240 (3 timeout, 1 extinct)

The residual changed in kind: v2.12's misses were mostly extinctions, and v2.13's are mostly **timeouts** at MAX_SOLS 200,000. The populations in these runs drift down over about 20,000 sols. Recovery buys time but does not fix the slow decline under ox 0.97. REF moderate 1.50% still has 20 misses (8 extinct, 12 timeout).

## What recovery adds, and why it should not be over-read

- It is a **modeled dormancy assumption, not a measurement**. No akinete formation rate or dormant survival has been measured for this strain under Mars-habitat conditions.
- The result depends mostly on how long the dormant pool is assumed to last. Sensitivity on C's five miss cells (N=240, v2.12 = 43):

| DORMANT_FRACTION | DORMANT_SURVIVAL_PER_SOL | C misses |
|---|---|---|
| 1e-4 | 0.999 (~1.9 Earth-yr half-life) | 43 (no effect) |
| 1e-3 | 0.999 | 42 |
| **1e-4** | **0.9999 (default)** | **19** |
| 1e-3 | 0.9999 (pool ≈ live population) | 4 |
| 1e-2 | 0.9999 | 2 |

  The default was chosen after this scan. It is the smallest pool (about 8% of live) that had an effect. Larger fractions were rejected because they make the pool as big as the live population. Shorter dormancy recovers nothing.
- The pool is shadow bookkeeping. It is not subtracted from live units, which keeps scored A bit-identical, so it is an approximation.

## Earlier attempts that failed (carried forward)

1. Dose-gated reductase bump: tested and failed. Not re-run.
2. Further static floor raises: rejected as biology retuning.

## Interpretation

v2.13 cuts the no-override residual from 43 to 19, but only under an untested dormancy assumption. Scored A is unchanged. The residual is not closed, and most of what is left are timeouts. Next real milestone: Earth-analog chamber or lab-screen data, including akinete formation and dormant viability. Simulation does not substitute for that.

Design owned by Craig. Paper until measured.
