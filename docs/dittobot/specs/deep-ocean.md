# Deep Ocean / High Pressure — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Later-version inheritance target for deep ocean / high pressure, described in the parent as greater than 200 m to full ocean depth.

From the parent:

- External pressure hull sleeve or lattice-level pressure vessel that the cells dock inside, or pressure-compensated oil-filled cells with flexible membranes.
- Mechanical pin and detent already carry load; the hull takes the hydrostatic force.
- Target, already written as paper in the parent: cells remain functional at 4 km+. That figure is a paper target, not a measured or locked pass bar, and is not restated as a gate here.

The current baseline plus Mars path already notes moderate underwater (potting + pin load path) to ~200 m on paper. This item is the later, deeper target.

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

TBD, no pass bar set. The 4 km+ figure in the parent is a paper target, not a test ID or measured gate.

## Assumptions

- Hull sleeve, lattice-level pressure vessel, and oil-filled compensated cells are paper options, modeled, not measured.
- The 4 km+ functional target and the ~200 m moderate-underwater note are paper figures from the parent, modeled, not measured.

## Parent

[EXTREME_ENVIRONMENTS.md — Deep ocean / high pressure](../../EXTREME_ENVIRONMENTS.md#deep-ocean--high-pressure-200-m-to-full-ocean-depth).

Paper until measured. Credit follows data.
