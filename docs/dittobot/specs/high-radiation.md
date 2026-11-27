# High Radiation / Deep Space / Nuclear — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Later-version inheritance target for high radiation / deep space / nuclear.

From the parent:

- Full rad-hard or rad-tolerant electronics path (already started in the Mars variant).
- Shielding mass traded at lattice level (outer cells become sacrificial shield).
- Optical or hardened data links if copper fails.

The current baseline plus Mars path already notes a Mars rad-hard MCU path. This item is the later, deeper-space / nuclear inheritance. See [MARS_VARIANT.md](../../MARS_VARIANT.md).

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

TBD, no pass bar set. No radiation-dose or SEE test IDs exist in the repo for this inheritance target.

## Assumptions

- Full rad-hard electronics, sacrificial outer-cell shielding, and optical or hardened links are paper inheritance, modeled, not measured.
- No dose, fluence, or shielding-mass figure is stated in the parent, and none is added here.

## Parent

[EXTREME_ENVIRONMENTS.md — High radiation / deep space / nuclear](../../EXTREME_ENVIRONMENTS.md#high-radiation--deep-space--nuclear).

Paper until measured. Credit follows data.
