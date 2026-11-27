# Honesty Note — Residual Failures in DB-MARS-CONV-006 v2.14

**Date:** 2026-11-27 (t230u)
**Sim:** `sims/mars_bacteria_swarm_sim_v2_14.py` (v2.13 + two engineering fixes, enabled only on the non-scored configs)
**Status:** Documented. Not forced. Scored A is the control and is bit-identical to v2.13.
**Run:** default `main()`, seed 42, N=240, 12 cells, habitat + adaptive on, throttle mode.

## What changed in v2.14

Two mechanics, each behind its own flag. **Both default OFF.** `main()` turns them
ON only for the non-scored residual configs (C no-override, A-low, A-high, REF, B).
Scored A runs with both flags OFF, so it uses the exact v2.13 code path and numbers.
No locked constant was changed; v2.13 recovery stays on; `_V29_REFERENCE_SOURCE` is
byte-identical. Every new constant is a MODELED assumption, not a measured property.

### Fix 1 — adaptive inducible oxidative defence (`ADAPTIVE_REDUCTASE_ENABLED`)
In v2.13 the oxidative survival factor is a static per-sol multiplier. Fix 1 makes it
respond during the run. An inducible antioxidant pool (SOD/catalase/peroxiredoxin-style
OxyR/SoxRS response) rises with **cumulative** oxidative damage and immediately lowers
the damage rate on later sols:
`ind = ADAPT_OX_PROTECT_MAX * cum / (cum + ADAPT_OX_HALFSAT)`, `ox_eff = 1 - (1-ox_base)*(1-ind)`.
Induction carries a replication-rate **cost** `ADAPT_OX_GROWTH_COST * ind` (not free).

| Constant | Value | Meaning |
|---|---|---|
| `ADAPT_OX_PROTECT_MAX` | 0.3 | max fraction of oxidative damage removed at full induction |
| `ADAPT_OX_HALFSAT` | 0.5 | cumulative damage (sum of per-sol (1-ox_eff)) at half-max induction |
| `ADAPT_OX_GROWTH_COST` | 0.05 | fractional replication-rate cost at full induction |

### Fix 2 — reductase-baseline sub-populations (`SUBPOPULATIONS_ENABLED`)
The inoculum is split into resistant/standard/sensitive sub-populations that **sum to
the total (population conserved)**. Resistant has higher baseline oxidative protection
and a **real growth-rate cost** (slower doubling); sensitive takes more oxidative damage
but grows slightly faster. All sub-pops share one nutrient pool and the single per-sol
survival draw (no extra RNG).

| Constant | Value | Meaning |
|---|---|---|
| `SUBPOP_FRACTIONS` | (0.15, 0.70, 0.15) | resistant / standard / sensitive; sums to 1.0 |
| `SUBPOP_OX_PROTECT` | (0.3, 0.0, -0.3) | fraction of oxidative damage removed(+)/added(-) |
| `SUBPOP_GROWTH_COST` | (0.04, 0.0, -0.01) | replication-rate cost; resistant 4% slower |
| `SUBPOP_PROTECT_MAX` | 0.95 | cap on combined per-sub-pop protection |

### How the strengths were chosen (no forced numbers)
The two oxidative-protection strengths (`ADAPT_OX_PROTECT_MAX`, resistant `SUBPOP_OX_PROTECT`)
were picked by a **rule decided in advance**: scan {0.3, 0.5} x {0.3, 0.5} at N=24 on C and
REF with both fixes on, and take the **smallest** pair that moves the residual, with metabolic
cost strictly > 0. Every scanned setting cleared the N=24 screen (C 1->0, REF 3->0) for all
four combinations, so the smallest, 0.3/0.3, was chosen. Half-sat, fractions, and the growth
costs were fixed from reasoning, not scanned. Nothing was tuned to drive N=240 misses to zero.

## Scored A is untouched (the control)

- Scored A (combined, overrides on, both fixes OFF): **2880/2880, 12/12 cells, ALL GATES PASS, 0 freeze crossings.** Identical to v2.13 (same median clear sols, e.g. moderate 1.50% 1145, severe 1.50% 1906).
- `RECOVERY CHECK`: A recovery on vs off differs 0/2880 (A UNTOUCHED).
- `V2.14 SCORED-A CONTROL CHECK`: A re-run vs A 0/2880 (deterministic); A is bit-identical to v2.13 by construction (the flag-off code path is the exact v2.13 lines, no extra RNG draws). Verified externally: v2.14 (flags off) vs v2.13 `run_once` = 0/120 differing across 12 cells x 5 seeds x override on/off.
- Turning the fixes ON *would* change A on 2880/2880 runs, which is exactly why the fixes are kept OFF for the control.
- `CONTROL: REF (recovery off, fixes off) vs v2.9 module` still differs 1920/2880 (unchanged from v2.13; the 0.62 floor + thermal buffer, not the fixes). E2/E3 CO2-ordering 0/12 changed; E4 P-import 0/2880 differ from A; E5 freeze crossings 0.

## Residual, v2.13 -> v2.14 (N=240, misses out of 2880, both fixes together)

| Config | v2.13 | v2.14 | Change |
|---|---|---|---|
| A scored (control) | 0 | **0** | untouched |
| C no-override (ox 0.97) | 19 | **0** | -19 |
| A-low | 18 | **9** | -9 |
| A-high | 14 | **0** | -14 |
| REF (neither lever) | 34 | **0** | -34 |
| B (scav 1e-3) | 3 | **110** | **+107 (REGRESSION)** |

All configs still pass all 12 gates (the gate is 50-70% clears per cell; B severe 1.50% is 130/240 = 54%).

### Where the residual now lands (v2.14, both fixes)
- **A-low** moderate 1.50%: 231/240 (5 timeout, 4 extinct). Its median clear sol among clears is ~3149 sols. This is A-low's only miss cell.
- **B** severe 1.50%: 130/240 (110 extinct, 0 timeout). Recovery fired on all 110 but none recovered — a genuine collapse, not a slow drift.
- Every other non-scored cell clears 240/240.

### Establishment got faster where the fixes help
Median clear sol, moderate 1.50%: C 2922 -> **421**, REF 3029 -> **423**. Severe 1.50%: C 2755 -> **1329**, REF 2758 -> **1330**. The fixes don't just clear more runs, they establish the culture far sooner on the oxidative-limited cells.

## HONESTY FLAG: the B regression (3 -> 110)

This is the headline caveat. The fixes are **not uniformly beneficial**. On B (low
scavenging 1e-3, low growth margin) the residual got an order of magnitude *worse*.
Ablations isolate the cause:

| Config | fix1 only | fix2 only | both |
|---|---|---|---|
| C | 0 | 5 | 0 |
| REF | 0 | 5 | 0 |
| A-high | 0 | 5 | 0 |
| A-low | 8 | 9 | 9 |
| B | **131 (GATE FAIL, severe 1.50% 109/240 = 45% < 50%)** | **0** | 110 |

- **Fix 1 alone** clears C/REF/A-high to 0 but **fails B's severe-1.50% gate** (109/240). On B's severe 1.50% the oxidative override already makes damage tiny (ox ~0.999), so Fix 1's induction delivers almost no survival benefit while still charging its ~1-2% replication-rate cost over thousands of sols — in a marginal-growth regime that cost tips cells into extinction. Fix 1's cost is not matched to its benefit when oxidative stress is already low.
- **Fix 2 alone** is mild everywhere: it leaves ~5 (severe 1.50%, ~2 extinct + 3 timeout) on C/REF/A-high, 9 on A-low, and is **perfect on B (0)**.
- **Both together**: Fix 1 dominates the harm on B (110 misses), while on C/REF/A-high the two combine to reach 0.
- **Neither fix alone is uniformly sufficient**, and for A-low the combination (9) is marginally worse than Fix 1 alone (8).

Net: the improvement on the oxidative-limited configs (C -19, REF -34, A-high -14, A-low -9) comes from Fix 1; Fix 2 is the safer, milder lever and is the one that protects B. The combined candidate improves four configs and regresses one. This is left documented, not patched over.

## New modeled assumptions introduced (every one is a flag)

1. An inducible antioxidant response exists and saturates as Hill-1 in cumulative damage (Fix 1). No induction kinetics measured for this strain.
2. Full induction removes at most 30% of oxidative damage (`ADAPT_OX_PROTECT_MAX` 0.3). Modeled.
3. Induction half-saturates at cumulative damage 0.5 (`ADAPT_OX_HALFSAT`). Modeled; drives how fast adaptation ramps.
4. Antioxidant induction costs 5% of replication rate at full induction (`ADAPT_OX_GROWTH_COST`). Modeled; this cost is what regresses B.
5. Standing phenotypic variation splits the inoculum 15/70/15 into resistant/standard/sensitive (Fix 2). Modeled; no measured trait distribution.
6. Resistant removes 30% of oxidative damage for a 4% growth-rate cost; sensitive takes 30% more damage for ~1% faster growth. Modeled.
7. Germinated dormant (recovery) cells rejoin as the standard sub-population. Modeled bookkeeping choice.
8. The oxidative-protection terms of the two fixes add linearly (capped at 0.95). Modeled.

## Bottom line

Scored A is untouched and still 2880/2880. The two fixes, as modeled, clear the
oxidative-limited residual (C, REF, A-high to zero; A-low 18->9) but the metabolic
cost of Fix 1 regresses the resource-limited B config from 3 to 110 misses, with
Fix 1 alone failing B's gate. The candidate is honest about that trade-off rather
than hiding it. If B matters more than the oxidative configs, Fix 2 alone (sub-populations)
is the better lever: it clears B and still trims the others slightly.
