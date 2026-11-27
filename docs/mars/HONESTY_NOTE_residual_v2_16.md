# Honesty Note — Residual Failures in DB-MARS-CONV-006 v2.16 (damage-scaled Fix-1 cost, both fixes every cell)

**Date:** 2026-11-27 (t236u)
**Sim:** `sims/mars_bacteria_swarm_sim_v2_16.py` (v2.15 mechanics + one new behavior: Fix-1 growth cost scales with current oxidative damage)
**Status:** Documented. Not forced. Scored A (both fixes, cost-scaled) is 2880/2880, 12/12 cells PASS; the fixes-OFF reference (= v2.13 scored A) is bit-identical to v2.13.
**Run:** default `main()`, seed 42, N=240, 12 cells, habitat + adaptive on, throttle mode.

## What changed in v2.16

v2.16 replaces v2.15's per-cell ROUTING with a single uniform policy: **both fixes
active in every cell of every config** (scored A, B, C, REF, A-low, A-high), plus one
new behavior on Fix 1:

- **Fix-1 growth cost now scales with current oxidative damage.** The cost factor is
  multiplied by `cost_scale = min(1, (1 - ox_base) / ADAPT_OX_COST_REF)` with
  `ADAPT_OX_COST_REF = 0.03`. Where oxidative damage is high (low-ox cells), the full
  cost applies; where ox ≈ 1 (very low damage, e.g. the severe/moderate 1.50% override
  cells at ox ≈ 0.9989, damage ≈ 0.0011), `cost_scale ≈ 0.037`, so Fix 1's growth
  penalty is almost entirely waived — which is the regime where Fix 1 bought almost no
  benefit but was charging the full ~1.49%/sol always-on cost that killed B in v2.14.

This is exactly the "Candidate B" that the B diagnosis identified and that was listed
as the alternative-not-adopted in the v2.15 note. Craig asked to adopt it ("try the
cost scaling version"). No other fix parameter changed. `_V29_REFERENCE_SOURCE` is
byte-identical; the v2.9 CONTROL is preserved; recovery is on; locked constants
unchanged. With `FIX_ROUTING = None` and both ENABLE flags off, the code path is
bit-exact to v2.13 (verified 0/96 differing cells).

### Scored A is no longer bit-identical to v2.13 (Craig's call)
Scored A now runs BOTH fixes (cost-scaled) in all 12 cells. Fix 1 changes scored A on
**2880/2880 runs** vs the fixes-OFF reference, yet scored A still clears
**2880/2880, 12/12 cells PASS** (the printed reference, = v2.13 scored A, also 2880/2880).
Median clear sol on the severe 1.50% cell actually improves (v2.16 1801 vs reference
1906) because the waived cost speeds recovery slightly; moderate 1.50% 1142 vs 1145.
Recovery never fires in scored A (0/2880). The fixes-OFF reference remains the v2.13
control and is bit-identical to it.

## How ADAPT_OX_COST_REF = 0.03 was chosen (the one new constant)

`0.03` is the moderate-tier oxidative damage level: the no-override moderate/C cells
model ox ≈ 0.97, i.e. per-sol damage `1 - ox = 0.03`. That is the damage level at which
Fix 1's protection vs cost tradeoff is already favorable in the baseline runs, so it is
used as the reference where the full Fix-1 cost applies; cells with less damage pay a
proportionally smaller cost. This value is taken directly from the diagnosis (no tuning
beyond that one number); it was not swept or fit to drive gate counts to zero.

## Residual, v2.13 -> v2.14 -> v2.15 -> v2.16 (N=240, misses out of 2880)

| Config | v2.13 | v2.14 | v2.15 | v2.16 | v2.16 miss cells (ext/tmo) |
|---|---|---|---|---|---|
| A scored | 0 | 0 | 0 | **0** | — (both fixes; reference also 0) |
| C no-override | 19 | 0 | 5 | **0** | — all 12 cells 240/240 |
| A-low | 18 | 9 | 13 | **0** | — all 12 cells 240/240 |
| A-high | 14 | 0 | 5 | **0** | — all 12 cells 240/240 |
| REF | 34 | 0 | 5 | **0** | — all 12 cells 240/240 |
| B (scav 1e-3) | 3 | 110 | 0 | **0** | — all 12 cells 240/240 |

**Every config now clears all 12 gates with zero misses at N=240.** This is the first
version where B is fixed (110 -> 0) AND the severe-1.50% residuals that v2.15's routing
reopened on C/REF/A-high/A-low are also back to 0 — because Fix 1 is active on those
cells again, but without its previously-fatal always-on cost. The v2.9 CONTROL (REF,
no fix, recovery off) clears 2820/2880 and still differs from the inlined v2.9 module
(unchanged; the 0.62 floor + thermal buffer, not the fixes).

## Residual that remains / honest caveats

- **No gate residual remains at N=240, seed 42.** That is not a proof of zero
  extinction probability — it means no cell crossed its pass threshold in these 240
  seeds. Rare tail extinctions below the gate are still possible and were not forced to
  zero; nothing was tuned to the gate.
- **A is no longer bit-identical to v2.13** (documented above), per Craig's explicit
  request to apply the fixes to scored A as well.
- **`ADAPT_OX_COST_REF = 0.03` is a modeled assumption** — a single new constant tied
  to the moderate-tier damage level, not a measured biological quantity.

## New modeled assumptions in v2.16

1. **Fix-1 growth cost scales linearly with oxidative damage up to a reference level
   (`ADAPT_OX_COST_REF = 0.03`), then saturates at the full cost.** Rationale: the cost
   of maintaining inducible antioxidant machinery should track how much damage is
   actually being countered; charging the full cost where there is almost no damage
   (and almost no benefit) was the v2.14 mechanism that drove B to extinction.

All v2.14/v2.15 assumptions carry over unchanged (Hill-1 inducible antioxidant, max
protection 0.3, half-sat 0.5, 5% induction growth cost; sub-population split 15/70/15
with 0.3 resistant protection and 4% growth cost). v2.16 adds only the cost-scaling
behavior and its one reference constant.
