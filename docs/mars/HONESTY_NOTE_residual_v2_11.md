# Honesty Note — Residual Failures in DB-MARS-CONV-006 v2.11 / v2.12

**Date:** 2026-11-27  
**Status:** Documented residual. Not forced. Scored A remains the control.

## What clears cleanly

With the light thermal buffer (habitat_active returns True even when HABITAT_ENABLED is False) and HARD_REDUCTASE_FLOOR raised to 0.62:

- Combined stress, multi-seed habitat grids, P-import / ISRU sweeps, inoculum size sweeps (1e12 → 1e4): 12/12 cells, 2880/2880 clears at N=240.
- Cabin-style (habitat flag off): now 12/12, 2880/2880. The heavy failure set is closed.

## The residual

When oxidative overrides are turned off (scored-A style control):

- 12/12 cells still marked PASS, but total clears drop to 2832/2880 (48 individual run failures).
- Failures are concentrated on oxidative + radiation axes (ox10, combo_all, combo_ox_rad, rad5). Not uniformly distributed.

## Failed attempts to close the residual

1. Dose-gated reductase bump (scales with cumulative radiation): reductase rose on the failing cells, but survival efficiency stayed insufficient against the steep oxidative damage coefficient. No net rescue. Scored-A control showed no regression (noise only).
2. Further static floor raises would require values that begin to look like biology retuning. Rejected.

## Interpretation

The 48-miss residual is the honest limit of the current model under no-habitat + no-override conditions. It is not hidden. It is not forced to 240/240. The uglier number is the accurate one.

Next real milestone remains Earth-analog chamber / lab-screen data (measurement card). Simulation does not substitute for that.

Design owned by Craig. Paper until measured.
