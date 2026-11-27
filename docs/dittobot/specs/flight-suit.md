# Flight Suit Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.2
Status: **paper spec**
Phase: unassigned, would require new assumptions: a numbered phase after Phase 1. The parent places this as a v5+ speculative inheritance roadmap; v5+ is a version-ladder label ([DESIGN.md](../../DESIGN.md) §3, current baseline is v4), not a defined phase. The repo defines only Phase 0 (one face) and Phase 1 (two-module dock + scheduled Marble).
Phase basis: [MODES.md](../../MODES.md) status line and [Flight Suit Mode (v5+)](../../MODES.md#flight-suit-mode-v5); also [EXTREME_ENVIRONMENTS.md — Exoskeleton / Flight](../../EXTREME_ENVIRONMENTS.md#exoskeleton--flight-iron-man-suit-mode) (“inheritance target for v5+ once propulsion faces exist”). No Phase 2+ document exists.

v5+ wearable inheritance. The lattice forms a wearable full-body shell around a human payload (torso, limbs, helmet volume). Variable density: denser at joints, shoulders, hips, and primary load paths; lighter panels elsewhere. Axial pin + detent carry the suit's own weight and acceleration loads. Soft inner clearance or optional compliant layer protects the wearer. Can collapse back into a dense transport brick using the existing inward-compaction path. See [inward-compaction.md](inward-compaction.md).

From the parent:

- Propulsion: dedicated thruster, ducted-fan, or high-thrust module cells dock into the back, palms, and boot soles. Shared power bus with a denser energy-cell zone (torso or backpack). Stabilization runs on the existing mesh (a few cells carry IMUs; the rest follow).
- Power and thermal: thrusters use a separate high-power path. Thermal budget is the real constraint under sustained thrust; the lattice can form temporary radiator tiles. Structural cells stay on the baseline pulse-only budget.
- Control: wearer intent (IMU, simple gesture, or control app) maps to thrust vector and attitude. Safe-reserve and thermal cutoffs still apply.

The parent status is paper. A flight claim requires measured thruster-module cards plus structural-cell cards. Flight is not in the current cell; the related note in [EXTREME_ENVIRONMENTS.md](../../EXTREME_ENVIRONMENTS.md#exoskeleton--flight-iron-man-suit-mode) is the same inheritance target.

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

TBD, no pass bar set. The parent requires measured thruster-module cards and structural-cell cards before any flight claim. No flight-specific test IDs exist in the repo.

## Assumptions

- Thruster, ducted-fan, or high-thrust modules, and a separate high-power path, are paper inheritance, modeled, not measured.
- Wearable geometry, density zoning, and radiator-tile behavior are conceptual until structural-cell cards are filled.
- Safe-reserve and thermal cutoffs are inherited rules, not new measured flight gates.

## Parent

[MODES.md — Flight Suit Mode (v5+)](../../MODES.md#flight-suit-mode-v5). Overlap: [EXTREME_ENVIRONMENTS.md — Exoskeleton / Flight](../../EXTREME_ENVIRONMENTS.md#exoskeleton--flight-iron-man-suit-mode).

Paper until measured. Credit follows data.
