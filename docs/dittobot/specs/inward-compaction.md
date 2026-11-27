# Inward Compaction / Shrink Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual**

Post-2040 speculative outlook. A car-scale (or larger) assembly collapses interstitial volume by moving modules inward and locking into a high-density packing whose outer envelope is roughly basketball-sized. Those scale words are the parent's outlook language, not measured dimensions.

Intent, from the parent: preserve every functional module (energy, structure, compute, mobility faces). End state is a dense, transportable or storable form that can later redeploy.

Mechanism (outlook): release selected faces → translate or fold neighbors inward along lattice axes or free-form paths → nest/interlock into reduced void fraction → re-lock with bus and mesh continuity. Collective inward motion, not uniform cell scaling. Individual cell envelopes stay at the nominal size (20 mm Phase 0 sliding-pin face or 25 mm option A).

This is not Marble Mode. Marble is one voxel collapsing its own envelope. See [marble-mode.md](marble-mode.md).

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

TBD, no pass bar set. The parent lists measured reliability of repeated expand / compact / split / merge cycles as required later, not now. No compaction test IDs exist in the repo.

## Assumptions

- Car-to-basketball scale language, packing fraction, and the reconfiguration sequence are outlook, modeled, not measured.
- Coordinated multi-node motion and proven dense-packing topologies are listed by the parent as later requirements, not present results.

## Parent

[POST_2040_OUTLOOK.md §1](../../POST_2040_OUTLOOK.md#1-inward-compaction--shrink-mode-car--basketball).

Paper until measured. Credit follows data.
