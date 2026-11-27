# Extreme Heat / High Ambient — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Later-version inheritance target for extreme heat / high ambient.

From the parent:

- Higher-temperature potting and coatings.
- Active or passive thermal rejection faces (radiator tiles the lattice can form).
- The pulse governor already limits coil heat; extend threshold logic.

No ambient-temperature band or radiator performance figure is stated in the parent beyond this qualitative target.

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

TBD, no pass bar set. No high-ambient test IDs exist in the repo.

## Assumptions

- Higher-temperature potting and coatings, radiator tiles, and extended governor thresholds are paper inheritance, modeled, not measured.
- No maximum ambient or sustained-heat rating is stated in the parent, and none is added here.

## Parent

[EXTREME_ENVIRONMENTS.md — Extreme heat / high ambient](../../EXTREME_ENVIRONMENTS.md#extreme-heat--high-ambient).

Paper until measured. Credit follows data.
