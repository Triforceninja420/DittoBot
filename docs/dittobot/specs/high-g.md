# High-g / Shock / Vibration — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Later-version inheritance target for high-g / shock / vibration.

From the parent:

- Pin and detent already provide positive lock.
- Add secondary shear keys or lattice-level damping zones.
- Potting helps component retention under acceleration.

No g-level, shock pulse, or vibration spectrum is stated in the parent.

## Inheritance

Inherits the locked 25 mm cell core, unchanged ([DESIGN.md](../../DESIGN.md), [PAPER_STATUS.md](../../PAPER_STATUS.md)):

- 25 mm cube envelope
- Centered Ø8.2 × 4.0 mm pocket (locked)
- Nd disc Ø6.0 × 2–3 mm hold; coil around the disc, release-only (Alnico off this cell)
- DRV8871, 12 V, pulse-only
- Axial pin hard-lock
- Full cavity potting and face coatings
- XIAO RP2040, 3.3 V; 36–48 V pulse bank

This paper spec does not retune that core, change Phase 0 locks or CAD, or rewrite measurement cards. Mode-specific layers sit on top. Dock compatibility with earlier cells is preserved where the parent already says so.

## Test gates

TBD, no pass bar set. No high-g or vibration test IDs exist in the repo for this inheritance target.

## Assumptions

- Secondary shear keys and lattice-level damping zones are paper additions, modeled, not measured.
- No acceleration, shock, or vibration rating is stated in the parent, and none is added here.

## Parent

[EXTREME_ENVIRONMENTS.md — High-g / shock / vibration](../../EXTREME_ENVIRONMENTS.md#high-g--shock--vibration).

Paper until measured. Credit follows data.
