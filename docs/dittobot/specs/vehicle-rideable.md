# Vehicle / Rideable Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.2
Status: **paper spec**
Phase: unassigned, would require new assumptions: a numbered phase after Phase 1. The parent places this as a v5+ speculative inheritance roadmap; v5+ is a version-ladder label ([DESIGN.md](../../DESIGN.md) §3, current baseline is v4), not a defined phase. The repo defines only Phase 0 (one face) and Phase 1 (two-module dock + scheduled Marble).
Phase basis: [MODES.md](../../MODES.md) status line (“speculative inheritance roadmap for v5+”) and [Vehicle / Rideable Mode](../../MODES.md#4-vehicle--rideable-mode); inheritance rule at [Inheritance rule (all modes)](../../MODES.md#inheritance-rule-all-modes). No Phase 2+ document exists.

A larger lattice forms a platform, open vehicle, or cargo carrier around one or more people or objects. Uses the same split/merge and expansion paths already written. See [split-merge.md](split-merge.md) and [outward-expansion.md](outward-expansion.md).

From the parent:

- Structure: dense structural and energy zones for the chassis and load paths; sparser panels for seating, cargo volume, or open deck. Pin + detent carry vehicle loads and acceleration.
- Mobility: optional specialized faces (wheels, tracks, or thrusters) dock into the lattice. Propulsion is additive, same as the flight suit. Can also be towed or pushed without its own drive.
- Behavior: can expand from a dense transport brick into rideable form, or split into smaller independent platforms. Mesh handles coordination and safe-reserve across subgroups.

The parent status is paper. It requires measured structural-cell cards plus any propulsion or mobility-module cards.

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

TBD, no pass bar set. The parent requires measured structural-cell cards plus any propulsion or mobility-module cards. No vehicle-specific test IDs exist in the repo.

## Assumptions

- Wheels, tracks, or thruster faces, chassis zoning, and split/expand behavior are paper inheritance, modeled, not measured.
- No payload, speed, or vehicle-load rating is stated in the parent, and none is added here.

## Parent

[MODES.md — Vehicle / Rideable Mode](../../MODES.md#4-vehicle--rideable-mode).

Paper until measured. Credit follows data.
