# Habitat / Shelter Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.2
Status: **paper spec**
Phase: unassigned, would require new assumptions: a numbered phase after Phase 1. The parent places this as a v5+ speculative inheritance roadmap; v5+ is a version-ladder label ([DESIGN.md](../../DESIGN.md) §3, current baseline is v4), not a defined phase. The repo defines only Phase 0 (one face) and Phase 1 (two-module dock + scheduled Marble).
Phase basis: [MODES.md](../../MODES.md) status line (“speculative inheritance roadmap for v5+”) and [Habitat / Shelter Mode](../../MODES.md#5-habitat--shelter-mode); inheritance rule at [Inheritance rule (all modes)](../../MODES.md#inheritance-rule-all-modes). No Phase 2+ document exists.

An expanded lattice forms an enclosed volume with sealed faces, basic thermal management, and optional pressure or environmental control. Builds directly on the extreme-environment inheritance paths.

From the parent:

- Structure: denser outer shell for sealing and load, lighter internal partitions or furniture zones. Sealed interconnects and coatings from the corrosive/chemical notes. Can incorporate pressure-compensated or oil-filled cells for higher-pressure variants. See [corrosion.md](corrosion.md) and [deep-ocean.md](deep-ocean.md).
- Behavior: uses outward expansion and variable-density zones to form walls, floor, and roof from a dense brick. Optional radiator tiles or thermal-rejection faces for heat. Soft safety skin on any internal human-proximate surfaces. See [outward-expansion.md](outward-expansion.md), [variable-density-zones.md](variable-density-zones.md), and [soft-safety-skin.md](soft-safety-skin.md).
- Inheritance: potting, pin hard-lock, and coatings as the floor. Agency-interest gates (traceability, measured data) apply if the use case is sensitive, as already noted in the parent.

The parent status is paper. Sealing and environmental performance claims wait on filled measurement cards.

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

TBD, no pass bar set. The parent defers sealing and environmental performance claims until measurement cards are filled. No habitat-specific test IDs exist in the repo.

## Assumptions

- Enclosed volume, sealed faces, optional pressure or environmental control, and oil-filled high-pressure variants are paper inheritance, modeled, not measured.
- No habitat volume, leak rate, or pressure rating is stated in the parent, and none is added here.

## Parent

[MODES.md — Habitat / Shelter Mode](../../MODES.md#5-habitat--shelter-mode).

Paper until measured. Credit follows data.
