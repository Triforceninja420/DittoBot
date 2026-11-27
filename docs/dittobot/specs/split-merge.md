# Split / Merge Swarm Scaling — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual**

Post-2040 speculative outlook. Change total volume by changing node count, not just packing density.

Intent, from the parent: one dense form splits into several smaller independent lattices. Multiple compact units merge into one larger structure. Scales from basketball-sized units to multi-vehicle or habitat-scale assemblies (and back) without permanent loss of modules. Those scale words are the parent's outlook language, not measured dimensions.

Mechanism (outlook): coordinated undock along a planned cut plane → subgroups re-form independent meshes and power domains → each subgroup can compact, expand, or travel separately. Merge is the reverse: approach, soft-dock, verify, hard-lock, then unified mesh and bus. Safe-reserve and brownout rules apply to every subgroup throughout.

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

TBD, no pass bar set. The parent lists measured reliability of repeated expand / compact / split / merge cycles as required later, not now. No split/merge test IDs exist in the repo.

## Assumptions

- Cut-plane undock, independent subgroup meshes, and later merge with unified bus are outlook, modeled, not measured.
- Basketball-to-habitat scale language is outlook wording, not a measured node-count or volume figure.

## Parent

[POST_2040_OUTLOOK.md §5](../../POST_2040_OUTLOOK.md#5-split--merge-swarm-scaling).

Paper until measured. Credit follows data.
