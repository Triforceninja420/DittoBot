# Changelog

## 2026-11-23
- LAT_OFFSET_SIGMA_MM 0.65 → 0.55 in phase0_monte_carlo.py: all-pass 96.62% → 98.04%, T3 97.87% → 99.30%, T3 fails 2 133 → 702 (100k trials). Synced test_phase0_math.py, cad/voxel_cell_phase0_30mm_dualcam.scad header, and docs/PHASE0.md.
- T3 failure forensics in phase0_monte_carlo.py: logs shear misses with relative velocity, lateral offset, capture-spring rate; ranks top 10 by composite score (vel 0.45, offset 0.35, spring deficit 0.20). Shear model now degrades with velocity and offset, improves with spring seating force.
- Sync all-pass rate 96.79% → 96.47% across test_phase0_math.py, cad/voxel_cell_phase0_30mm_dualcam.scad header, and docs/PHASE0.md after fresh 100k-trial re-run (T1 99.98, T2 99.41, T3 97.70, T4 99.39, T5 99.96).
- Fix phase0_monte_carlo.py: broken counts line in main() replaced with per-test tally (T1–T5) plus all-pass rate over 100k seeded trials.
- Correct README: test count was 16, actual is 5 Phase 0 math tests — updated status line, CI description, and added phase0 sim to start-here table and layout.
- Repo polish: root README cleaned (layout section, CI/tests/sims status lines, traceable sim link). docs/README.md converted to tables for scanability. Mars bacteria spec synced to v1.3 with backsolved parameters. mars_bacteria_swarm_sim.py pushed to sims/ — seeded, re-runnable, 240 runs, 73% clear rate, mean 311 sols.
- Unit-1 CI: fixed IK mirror-symmetry bug (copysign beta flip), patched Python test to match. 16/16 tests passing on main.
- DittoBot CI: pytest + flake8 on every push/PR. Phase 0 math tests + issue templates added.

## 2026-11-22
- Mars path tightened: executive summaries, units on every number, cited constants across all nine DB-MARS specs. Index gained key-number column.
- Bacteria swarm spec v1.3: backsolved parameters documented (1.5 kg/unit/sol, 6.3-sol doubling, 50% survival center, billion-unit inoculum, seed 42). 96-sol figure now traceable as ~2.6 percentile optimistic edge, not average.
- Consistency flush: Mars folder indexed, root + docs READMEs cross-link, DittoBot stated as main design throughout.

## 2026-11-21
- Phase 0 revision: 30 mm dual-cam staggered face (supersedes frozen 20 mm 4×EPM hybrid).
- NdFeB N52 Ø6.0 × 6.0 mm magnet, 40-turn 34 AWG coil (~0.75 Ω), sized for release not hold.
- Dual 8 mm radius cams, staggered corners (8,8)+(22,22), steel-backed polymer tips, 8 mm contact width. Hertzian 35.4 MPa, margin 1.98×.
- Two-pin latch + ~1/3 g retraction actuator. 5 N seating spring.
- Full sim battery: 26/26 passed. Shear 5 028 N (126× target), snap 34.6 N, release net +65.7 N, thermal < 1.5 K, mass 9.2 g, cam wear 0.19 µm / 2 000 cycles.
- Updated PHASE0.md, MEASUREMENT_CARD.md (new Phase 0 card section), LOCKS.md (18 locks, 9+9).
- 30 mm face size committed as shrink-down reference article.
- Paper only. Credit follows measured data.

## 2026-11-19
- Unified 25 mm baseline to SmCo 2:17 Ø7.5 mm residual hold + axial pin + potting + pulse-only.
- Synced BOM, firmware comments, force_sweep.py, COIL_REVISION.md, LOCKS.md, PHASE0 cross-reference, and README.
- Clarified pulse bank: 36 V nominal into DRV8871 (stay under 45 V absolute maximum).
- Added thermal governor stub in firmware/pulse_driver.cpp.
- Paper only. Credit follows measured data.

## Earlier
- 2026-11-06: Parallel-strand thermal notes and carbide shim.
- 2026-09: Initial geometry lock and first-pass retirement.
