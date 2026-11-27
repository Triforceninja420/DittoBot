# Hierarchical Nesting — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual**

Post-2040 speculative outlook. Future modules can accept or become sub-voxels. A single outer cell envelope holds a denser sub-lattice, giving multi-level volume change.

Intent, from the parent: deeper shrink and finer expand without changing the outer 20 mm or 25 mm nominal. Enables extreme density packing and high-resolution surface detail from the same base cell.

Mechanism (outlook): outer cells dock and form a stable envelope. Internal volume is filled by smaller sub-modules (or the same modules reconfigured into tighter hierarchical packing). Power, data, and mechanical continuity propagate through both levels. The sub-lattice can later eject or re-expand independently.

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

TBD, no pass bar set. The parent lists proven hierarchical topologies that preserve power, data, and mechanical continuity as required later, not now. No nesting test IDs exist in the repo.

## Assumptions

- Sub-voxels inside an outer envelope, and independent eject / re-expand of a sub-lattice, are outlook, modeled, not measured.
- No sub-module size, nesting depth, or packing-fraction figure is stated in the parent, and none is added here. The outer envelope stays the locked 20 mm face or 25 mm cell.

## Parent

[POST_2040_OUTLOOK.md §3](../../POST_2040_OUTLOOK.md#3-hierarchical-nesting).

Paper until measured. Credit follows data.
