# Changelog

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
