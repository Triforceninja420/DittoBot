# Self-Healing Coating — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual**

Optional Community Enhancement Suite, listed in the parent as **optional and zero-impact** on locked Phase 0 criteria, 25 mm option A geometry, process locks in `LOCKS.md`, force targets, or measurement cards. Suites do not mint V2.0. Two stacks stay unmixed.

The parent lists this item under Near-term optional (bench / early lattice) and does not define a mechanism, dimensions, or test gates beyond the name and that grouping. This paper spec records that listing only; it does not add a design.

The parent listing is the name only: “Self-healing coating.” No chemistry, thickness, trigger, or repair-time figure is given.

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

TBD, no pass bar set. The parent defines no test IDs for this suite and states that no suite is required for a measured latch or a filled measurement card.

## Assumptions

- Presence of the suite name in the parent is not a measured capability.
- Any implementation details not written in the parent are out of scope here and remain TBD, modeled, not measured.

## Parent

[COMMUNITY_ENHANCEMENT_SUITES.md — Near-term optional (bench / early lattice)](../../COMMUNITY_ENHANCEMENT_SUITES.md#near-term-optional-bench--early-lattice).

Paper until measured. Credit follows data.
