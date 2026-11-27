# Outward Expansion / Deployment Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.2
Status: **conceptual**
Phase: unassigned, would require new assumptions: a numbered phase for post-2040 scale-change work. The parent is a post-2040 speculative outlook and says these remain outlooks until later requirements exist. Post-2040 is a time horizon, not a defined Phase N. The repo defines only Phase 0 and Phase 1.
Phase basis: [POST_2040_OUTLOOK.md §2](../../POST_2040_OUTLOOK.md#2-outward-expansion--deployment-mode-basketball--car-and-beyond); opening (“post-2040 speculative outlook”); [What is required later (not now)](../../POST_2040_OUTLOOK.md#what-is-required-later-not-now).

Post-2040 speculative outlook. Exact inverse of inward compaction. A dense packing opens outward into vehicle-scale or larger structures in a coordinated sequence.

Intent, from the parent: rapid deploy from storage or transport. One compact unit becomes a full structure without external scaffolding.

Mechanism (outlook): release selected faces → modules translate or unfold outward along planned axes or free-form paths → expand void fraction while maintaining connectivity → re-lock into the target geometry. The parent says the same hybrid faces (EPM + pin) run in reverse. Energy and safe-reserve rules stay binding throughout the sequence. Individual cell envelopes stay at the nominal size.

See [inward-compaction.md](inward-compaction.md).

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

TBD, no pass bar set. The parent lists measured reliability of repeated expand / compact / split / merge cycles as required later, not now. No expansion test IDs exist in the repo.

## Assumptions

- Vehicle-scale deploy language and the unfold sequence are outlook, modeled, not measured.
- Continuity of power, data, and mechanical connections during expansion is a later requirement in the parent, not a measured result.

## Parent

[POST_2040_OUTLOOK.md §2](../../POST_2040_OUTLOOK.md#2-outward-expansion--deployment-mode-basketball--car-and-beyond).

Paper until measured. Credit follows data.
