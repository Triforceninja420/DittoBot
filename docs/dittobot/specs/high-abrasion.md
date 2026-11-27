# High-Abrasion / Industrial Grit — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Later-version inheritance target for high-abrasion / industrial grit.

From the parent:

- Carbide shim and PTFE lip already present.
- Replaceable face tiles the lattice can swap.
- Harder coatings as standard on later versions.

Armored / Protective Shell Mode points at these same optional replaceable face tiles. See [armored-shell.md](armored-shell.md).

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

TBD, no pass bar set. No abrasion or grit test IDs exist in the repo for this inheritance target.

## Assumptions

- Replaceable face tiles and harder later-version coatings are paper inheritance, modeled, not measured.
- The carbide shim and PTFE lip are existing baseline features cited by the parent; this spec does not add wear-life numbers for them.

## Parent

[EXTREME_ENVIRONMENTS.md — High-abrasion / industrial grit](../../EXTREME_ENVIRONMENTS.md#high-abrasion--industrial-grit).

Paper until measured. Credit follows data.
