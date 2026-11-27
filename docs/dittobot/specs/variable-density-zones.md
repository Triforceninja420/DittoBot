# Variable-Density Zones — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual**

Post-2040 speculative outlook. One continuous assembly maintains different packing densities in different regions at the same time.

Intent, from the parent: keep a dense structural or energy core while growing a sparse outer shell for reach, surface area, or soft interaction — or the reverse: sparse core with dense load-bearing shell.

Mechanism (outlook): local groups of modules decide packing density based on role. Dense zones stay locked for strength and power distribution. Sparse zones expand for volume or compliance. Boundaries remain continuously docked so the lattice stays one mechanical and electrical body. Soft safety skin and the 35 N human-contact interrupt remain active on any human-proximate surface (existing lock, not a new bar).

Armored Shell, Habitat, and related wearable modes already point at this zoning. See [armored-shell.md](armored-shell.md) and [habitat-shelter.md](habitat-shelter.md).

Shared constraints already written in the parent apply: Phase 0 (20 mm sliding-pin face) and 25 mm option A geometry stay frozen; no change to drivers, force targets, or measurement cards; energy budget, thermal limits, and safe-reserve rules apply to every sequence (no mode may drop below safe reserve); soft safety skin, the 35 N human-contact interrupt, and companion gates stay in force for any human-proximate use; two stacks stay unmixed; no V2.0 claim.

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

TBD, no pass bar set. No variable-density test IDs exist in the repo. The 35 N interrupt is an existing lock, not a new zone gate.

## Assumptions

- Simultaneous dense and sparse zones in one assembly, and role-based packing decisions, are outlook, modeled, not measured.
- No density ratio or zone-size figure is stated in the parent, and none is added here.

## Parent

[POST_2040_OUTLOOK.md §4](../../POST_2040_OUTLOOK.md#4-variable-density-zones).

Paper until measured. Credit follows data.
