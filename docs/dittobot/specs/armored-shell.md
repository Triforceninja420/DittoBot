# Armored / Protective Shell Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.2
Status: **paper spec**
Phase: unassigned, would require new assumptions: a numbered phase after Phase 1. The parent places this as a v5+ speculative inheritance roadmap; v5+ is a version-ladder label ([DESIGN.md](../../DESIGN.md) §3, current baseline is v4), not a defined phase. The repo defines only Phase 0 (one face) and Phase 1 (two-module dock + scheduled Marble).
Phase basis: [MODES.md](../../MODES.md) status line (“speculative inheritance roadmap for v5+”) and [Armored / Protective Shell Mode](../../MODES.md#2-armored--protective-shell-mode); inheritance rule at [Inheritance rule (all modes)](../../MODES.md#inheritance-rule-all-modes). No Phase 2+ document exists.

Higher-density outer layer optimized for impact, abrasion, or environmental protection. Can reconfigure density on the fly using the variable-density zones already outlined in the post-2040 outlook. See [variable-density-zones.md](variable-density-zones.md).

From the parent:

- Structure: outer cells use harder coatings or sacrificial face tiles. Inner layer stays softer or compliant. Pin hard-lock carries shear and impact loads.
- Behavior: density can shift toward high-threat faces (for example denser front and shoulders under impact risk). The lattice can form temporary thicker plates by stacking or nesting in localized zones.
- Inheritance: same potting, coatings, and pin path as baseline. Optional replaceable face tiles from the high-abrasion notes. See [high-abrasion.md](high-abrasion.md).

The parent status is paper. No armor claim until measured impact/shear data exists on the filled cards.

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

TBD, no pass bar set. The parent defers any armor claim until measured impact/shear data exists on filled cards. No armor-specific test IDs exist in the repo.

## Assumptions

- Harder coatings, sacrificial or replaceable face tiles, and on-the-fly density shift are paper inheritance, modeled, not measured.
- No impact rating, areal density, or armor class is stated in the parent, and none is added here.

## Parent

[MODES.md — Armored / Protective Shell Mode](../../MODES.md#2-armored--protective-shell-mode).

Paper until measured. Credit follows data.
