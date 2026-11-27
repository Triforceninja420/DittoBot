# Honesty Note — Residual Failures in DB-MARS-CONV-006 v2.15 (per-cell fix routing)

**Date:** 2026-11-27 (t232u)
**Sim:** `sims/mars_bacteria_swarm_sim_v2_15.py` (v2.14 mechanics, ROUTED per cell; no fix parameter changed)
**Status:** Documented. Not forced. Scored A (routed) is 2880/2880; the fixes-OFF reference is bit-identical to v2.13.
**Run:** default `main()`, seed 42, N=240, 12 cells, habitat + adaptive on, throttle mode.

## What changed in v2.15

No fix PARAMETER changed from v2.14. v2.15 only ROUTES which fix is active per cell:

- **severe 1.50% cell of every config → Fix 2 (sub-populations) only.**
- **all other 11 cells of every config → Fix 1 (adaptive reductase) only.**

Scored A fixes-OFF REFERENCE (= v2.13 scored A) is printed alongside. `FIX_ROUTING`
None (default) falls back to the v2.14 ENABLED flags, so the v2.14 and bit-exact
flag-off code paths are unchanged. `_V29_REFERENCE_SOURCE` is byte-identical and the
v2.9 CONTROL (REF, no fix, recovery off) is preserved.

### Scored A is no longer bit-identical to v2.13 (Craig's call)
Craig asked for Fix 1 on scored A. Under routing, scored A runs Fix 1 on its 11
non-(severe 1.50%) cells and Fix 2 on severe 1.50%. Fix 1 changes scored A on
**1680/2880 runs** vs the fixes-OFF reference, but scored A still clears
**2880/2880, 12/12 cells PASS** (reference also 2880/2880). Median clear sol on the
severe 1.50% cell is essentially unchanged (routed 1918 vs reference 1906).
Recovery never fires in scored A (0/2880). The fixes-OFF reference remains the
v2.13 control and is bit-identical to it.

## The B diagnosis that motivated routing

Instrumented N=240 seed 42 on the v2.14 B config severe 1.50% cell (both fixes,
110 extinctions / 240). Per-sol detail and CSVs in /workspace/v214/diag/.

- **Root cause: Fix 1's growth cost is ALWAYS-ON with no matching benefit.** That
  cell's override makes ox ≈ 0.9989, so per-sol oxidative damage is ~0.0011.
  Cumulative damage still climbs over tens of thousands of sols, so induction
  SATURATES (ind at failure med 0.297 of the 0.30 cap), charging ~1.49%/sol of
  replication rate permanently from ~sol 5000, while the protection it buys is
  ~0.0003. In B's marginal scav-1e-3 regime (net ≈ 1.003/sol) that drag flips net
  growth below replacement.
- **Slow LATE declines, not early collapse.** Extinction sol (n=110): min 27,701,
  p25 51,006, median 60,351, p75 72,154, max 136,789. No timeouts.
- **Resistant sub-pop dies first.** Carrying both the Fix-2 (4% slower) and Fix-1
  (~1.5%) costs, resistant is the slowest grower; its fraction → ~0.00 by sol
  ~5000 in every failed run, so Fix 2's insurance is gone before collapse.
- **Not resource/water/O2/thermal:** mineral-P plateaus ~9% left, clip reason None
  through the decline; no freeze/throttle. Recovery fired (1.38/run, all 110) but
  rescued none (fired-then-cleared 0).
- **Fix 2 alone (same seeds): 0 extinctions** — isolates Fix 1 as the sole cause.
  (Fix 1 alone: 131 extinctions, gate-fails at 109/240.)
- **The same mechanism hits scored A's own severe 1.50% cell** (also override ox
  ≈ 0.9989): with Fix 1 it dropped to 200/240 (39 extinct, 1 timeout), i.e. scored
  A 2840/2880. That is why severe 1.50% is routed to Fix 2 in EVERY config,
  including scored A.

## Residual, v2.13 → v2.14 → v2.15 (N=240, misses out of 2880)

| Config | v2.13 | v2.14 | v2.15 | v2.15 miss cells (ext/tmo) |
|---|---|---|---|---|
| A scored | 0 | 0 | **0** | — (routed; reference also 0) |
| C no-override | 19 | 0 | **5** | severe 1.50% 235/240 (2 ext, 3 tmo) |
| A-low | 18 | 9 | **13** | moderate 1.50% 232/240 (3 ext, 5 tmo); severe 1.50% 235/240 (2 ext, 3 tmo) |
| A-high | 14 | 0 | **5** | severe 1.50% 235/240 (2 ext, 3 tmo) |
| REF | 34 | 0 | **5** | severe 1.50% 235/240 (2 ext, 3 tmo) |
| B (scav 1e-3) | 3 | 110 | **0** | — (severe 1.50% routed to Fix 2 = 240/240) |

All configs pass all 12 gates. The v2.9 CONTROL (REF, no fix, recovery off) clears
2820/2880 and still differs 1920/2880 from the inlined v2.9 module (unchanged; the
0.62 floor + thermal buffer, not the fixes). E2/E3 CO2-ordering 0/12 changed; E4
P-import 0/2880 differ from A; E5 freeze crossings 0.

### HONESTY FLAG: the tradeoff routing makes
Routing severe 1.50% to Fix 2 is what saves scored A (and B), but Fix 2 alone is
weaker than Fix 1 on that cell: it leaves ~5 misses (2 extinct + 3 timeout). So vs
v2.14, C/REF/A-high tick up 0 → 5 and A-low 9 → 13 (A-low also keeps its moderate
1.50% residual, which uses Fix 1). This is a deliberate, documented tradeoff:
+ scored A restored to 2880/2880, B fixed 110 → 0;
- a small residual reopened on the severe 1.50% cell of C/REF/A-high/A-low.
Every config is still far better than the v2.13 baseline except B, which is now
perfect. Nothing was tuned to drive these to zero.

## Alternative considered but NOT adopted (Craig's call)

Make Fix 1's growth cost SCALE with the current oxidative-damage level
(`cost · min(1, (1-ox_base)/0.03)`) instead of always-on. In a diagnosis-only
N=240 screen this cleared **everything** — B severe 1.50% → 0, C/REF/A-high → 0,
A-low → 0 — and leaves scored A unharmed because the cost ≈ 0 where ox ≈ 1. It was
NOT adopted here (it changes the Fix-1 mechanism and adds a reference-damage
constant). It remains available if the reopened severe-1.50% residuals matter more
than keeping the fix parameters untouched.

## New modeled assumptions in v2.15

None beyond v2.14's. v2.15 adds only a routing rule (which cell uses which existing
fix); no new biological constant. The v2.14 assumptions (inducible antioxidant
Hill-1 induction, max protection 0.3, half-sat 0.5, 5% induction growth cost;
sub-population split 15/70/15 with 0.3 resistant protection and 4% growth cost)
carry over unchanged.
