# Cryogenic / Extreme Cold — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Later-version inheritance target for cryogenic / extreme cold, described in the parent as below −125 °C.

From the parent:

- NdFeB N52 retains usable remanence at cryo; the Nd disc is specified with cold-derating margin on the pulse bank.
- Low-temperature lubricants or dry-film on pin and detent.
- Capacitor and MCU cold-start heaters or fully cryo-rated parts.
- Inherited from Mars pulse bank derating notes.

The −125 °C threshold is the parent's own description of this target, not a measured operating limit and not a new pass bar.

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

TBD, no pass bar set. No cryogenic test IDs exist in the repo.

## Assumptions

- Usable remanence at cryo, pulse-bank cold-derating, dry-film lubrication, and heaters or cryo-rated parts are paper inheritance, modeled, not measured.
- The below −125 °C band is the parent's target description, not a measured rating.

## Parent

[EXTREME_ENVIRONMENTS.md — Cryogenic / extreme cold](../../EXTREME_ENVIRONMENTS.md#cryogenic--extreme-cold-below-125-c).

Paper until measured. Credit follows data.
