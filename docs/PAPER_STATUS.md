# Paper Status — What Is Fixed Without Measurements

Design owner: Craig. 2026-11-19.

All items below are resolved at the documentation and geometry-note level. No filled measurement card is required.

## Resolved
- Baseline is unified: Nd disc Ø6.0 × 2–3 mm hold (coil release-only, Alnico off; updated 2026-11-23 from SmCo 2:17 Ø7.5 × 3.0), axial pin hard-lock, full cavity potting, PTFE lip + coatings, pulse-only + thermal governor stub, 36 V nominal pulse bank (stay under DRV8871 45 V abs max).
- Pocket remains locked at Ø8.2 × 4.0 mm. CAD updated with pin receptacle notes and clearance.
- BOM, firmware comments, COIL_REVISION.md, LOCKS.md, force_sweep.py, and PHASE0 cross-references were synchronized to the 2026-11-19 baseline. The 2026-11-23 magnet change is synced in docs only; bom/, firmware/ comments, tools/force_sweep.py and cad/voxel_cell.scad comments still say SmCo Ø7.5 (pending).
- Mars / space path inherits the full baseline. No separate geometry.
- Open thermal, cold-weld, dust, and vacuum paths closed on paper by potting + coatings + pulse-only.
- Agency interest gates (traceability, open notes, tamper baseline) documented.
- Extreme-environment and exoskeleton/flight inheritance paths written and cross-linked.
- Root legacy files removed. All live sources are in docs/ with a clear index. See CHANGELOG.md.

## Still requires hardware
- Actual ON/OFF force, release current, cycle life, plate temperature under pulse train.
- Pin engagement wear and potting moisture/vacuum integrity.
- Any claim of flight, deep-ocean pressure hull, or rad-hard flight units.

Credit follows measured data. This file only confirms the paper design is internally consistent.
