# Corrosive / Chemical / Saltwater Long-Term — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Later-version inheritance target for corrosive / chemical / saltwater long-term use.

From the parent:

- Full conformal plus sacrificial anode options.
- Ceramic or polymer face plates instead of bare metal.
- Sealed interconnects with gold or equivalent contacts.

Community suites also list corrosion / salt-fog protection as an optional, zero-impact package shared across post-2040 modes. That listing adds no mechanism or bar beyond the parent environment note.

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

TBD, no pass bar set. No salt-fog, immersion, or chemical-exposure test IDs exist in the repo for this inheritance target.

## Assumptions

- Conformal coats, sacrificial anodes, ceramic or polymer faces, and gold or equivalent contacts are paper options, modeled, not measured.
- No exposure duration or corrosion-rate figure is stated in the parent, and none is added here.

## Parent

[EXTREME_ENVIRONMENTS.md — Corrosive / chemical / saltwater long-term](../../EXTREME_ENVIRONMENTS.md#corrosive--chemical--saltwater-long-term).

Paper until measured. Credit follows data.
