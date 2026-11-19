# DESIGN.md — 25 mm cell architecture

Design owner: Craig. Started Nov/Dec 2025.
Status: baseline updated 2026-11-19. Thermal revision 2026-11-06.
Residual-hold hardening 2026-11-19. Mars / space path 2026-11-19.

## 1. Cell envelope

25 mm cube. One centered Ø8.2 × 4.0 mm pocket. One SmCo magnet stack.
One coil. One release pulse. Driver DRV8871, 12 V. Logic XIAO RP2040, 3.3 V.
Cavity potted. Faces coated. Axial pin for hard-lock.

## 2. Lock philosophy

The magnet holds and provides soft-dock. The coil only releases. A short axial pin carries external load once seated. Nothing is a measured latch until disc, turns, R, peak I, I_release, ON N, and OFF N are published in MEASUREMENT_CARD.md.

## 3. Version ladder

- v0: 120-turn / 5 V / 28.8 N — retired
- v1: 2026-09-09 Nd+Alnico flip stack — superseded, do not build
- v2: 2026-09-10 clean core swap, DRV8871, parallel-strand thermal fix
- v3: 2026-11-19 residual-hold hardening
- v4: 2026-11-19 baseline upgrades (SmCo Ø7.5 mm, pin, potting, coatings) + Mars/space path — see BASELINE_UPGRADES.md and MARS_VARIANT.md

## 4. Files

- BUILD.md — fab handoff
- BASELINE_UPGRADES.md — 2026-11-19 underwater + space standard
- COIL_REVISION.md — why the first pass failed, wind math, SmCo path
- PHASE0.md — locked 20 mm face (do not mix numbers)
- MEASUREMENT_CARD.md — blank until filled
- MARS_VARIANT.md — Mars / space adaptations (inherits baseline, adds rad-hard path)
- cad/voxel_cell.scad — pocket geometry, locked (pin and magnet OD need CAD update)
- firmware/pulse_driver.cpp — pulse routine
- bom/bom_netlist.txt — BOM
- tools/force_sweep.py — paper sweep, warning only

## 5. Paper locks

See LOCKS.md (16 locks, 2026-09-14). No geometry change without a new lock. Pocket remains Ø8.2 × 4.0.

## 6. Residual-hold hardening (2026-11-19)

Sim (2026-11-18) found the zero-power residual as the soft spot.

Three levers, stacked, now native:

1. **SmCo 2:17 Ø7.5 mm** — higher coercivity, thermally stable, stronger residual than prior Ø6 mm.
2. **Compliant pole tip + PTFE lip + coating** — dust and cold-weld tolerance.
3. **Groove-and-ridge detent + axial pin** — magnetism positions; geometry and pin lock. Pin carries pressure once seated.

## 7. Mars / space variant (2026-11-19)

See MARS_VARIANT.md. The Mars path now inherits the full baseline upgrades so the same cell handles Mars surface and pure space (vacuum, cold, radiation, free-float) without a separate branch. Rad-hard MCU and shielding remain the Mars-specific addition.

Credit follows measured data.
