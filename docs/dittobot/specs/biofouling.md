# Biofouling / Biological — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.2
Status: **paper spec**
Phase: unassigned, would require new assumptions: a numbered phase after Phase 1. The parent lists this as a later-version inheritance target under a v5+ inheritance rule; v5+ is a version-ladder label, not a defined phase. The repo defines only Phase 0 and Phase 1. No Phase 2+ document exists.
Phase basis: [EXTREME_ENVIRONMENTS.md — Biofouling / biological](../../EXTREME_ENVIRONMENTS.md#biofouling--biological) under [Later-version inheritance targets](../../EXTREME_ENVIRONMENTS.md#later-version-inheritance-targets); [Inheritance rule](../../EXTREME_ENVIRONMENTS.md#inheritance-rule).

Later-version inheritance target for biofouling / biological exposure.

From the parent:

- Anti-fouling coatings on external faces.
- Smooth or actively wiped surfaces (PTFE lip already a start).
- Sealed design prevents internal growth.

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

TBD, no pass bar set. No biofouling test IDs exist in the repo.

## Assumptions

- Anti-fouling coatings and actively wiped surfaces are paper inheritance, modeled, not measured.
- That the sealed design prevents internal growth is a paper claim, not a measured result.
- No coating chemistry, wipe cycle, or exposure duration is stated in the parent, and none is added here.

## Parent

[EXTREME_ENVIRONMENTS.md — Biofouling / biological](../../EXTREME_ENVIRONMENTS.md#biofouling--biological).

Paper until measured. Credit follows data.
