# Honesty Note — Residual Failures in DB-MARS-CONV-006 v2.12

**Date:** 2026-11-27  
**Sim:** `sims/mars_bacteria_swarm_sim_v2_12.py`  
**Status:** Documented residual. Not forced. Scored A remains the control.  
**Run:** default `main()`, seed 42, INOCULUM 1e12, scav 5e-3, DOUBLING_SOLS 8.72, habitat and adaptive on, throttle mode, N=240, 12 cells.

## What clears cleanly

With the light thermal buffer (`habitat_active` no longer checks `HABITAT_ENABLED`, so the buffer stays on in cabin mode for insulated / insulated_heated tiers) and `HARD_REDUCTASE_FLOOR` raised to 0.62, this v2.12 N=240 `main()` run found:

- Scored A (combined, overrides on, scav 5e-3, D 8.72): 12/12 cells, 2880/2880 clears. ALL GATES PASS. Freeze crossings 0/2880.
- E4 P-import fallback and E5 vent mode: 12/12 cells, 2880/2880. E2/E3 CO2-ordering check changed 0/12 cells vs A.

The v2.11 note also cited multi-seed habitat grids, inoculum size sweeps (1e12 → 1e4), and cabin-style (habitat flag off) at 12/12, 2880/2880. Those sweeps are not part of `main()` and were not re-run here, so they are not re-claimed as v2.12 results.

## The residual

When oxidative overrides are turned off (config C in `main()`: scored-A scav 5e-3 and D 8.72, habitat flag still on):

- 12/12 cells still marked PASS, but total clears drop to 2837/2880 (43 individual run failures).
- That is 5 fewer misses than the v2.11 residual of 48 misses / 2832/2880, under the same no-override control. The residual is smaller, not gone.
- Failures are not uniformly distributed. They fall on five cells of the 12-cell (tier × perchlorate) grid:

  - moderate 0.50%: 231/240 (9 extinct)
  - moderate 0.75%: 232/240 (8 extinct)
  - moderate 1.00%: 231/240 (7 extinct, 2 timeout)
  - moderate 1.50%: 232/240 (4 extinct, 4 timeout)
  - severe 1.50%: 231/240 (9 extinct)

  The v2.11 note described the residual as concentrated on oxidative + radiation axes (ox10, combo_all, combo_ox_rad, rad5). Those names are not cell keys in this grid. The v2.12 misses sit on the moderate-tier cells (tier oxidative factor 0.97, overrides off) plus severe 1.50%.

## Failed attempts to close the residual

1. Dose-gated reductase bump (scales with cumulative radiation): reductase rose on the failing cells, but survival efficiency stayed insufficient against the steep oxidative damage coefficient. No net rescue. Scored-A control showed no regression (noise only). Not re-run in this v2.12 ensemble; carried forward as previously tested and failed.
2. Further static floor raises would require values that begin to look like biology retuning. Rejected.

## Interpretation

The 43-miss residual is the honest limit of the current v2.12 model under no-override, scored-A conditions (habitat flag on; thermal buffer active for moderate and severe). It is not hidden. It is not forced to 240/240. The uglier number is the accurate one. Closing 5 of v2.11's 48 misses does not close the residual.

Next real milestone remains Earth-analog chamber / lab-screen data (measurement card). Simulation does not substitute for that.

Design owned by Craig. Paper until measured.
