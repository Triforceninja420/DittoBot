# Marble Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **Phase 1 ready**

A single voxel collapses into a dense sphere for compact transport and re-expands into a dockable lattice cell on arrival. Intent, from the parent: Mars swarm logistics — ship modules compact, deploy spread out — or any tight payload volume, then re-expand into a face-compatible cell.

This is not the post-2040 inward-compaction path, in which many rigid modules pack tighter while each cell envelope stays at its nominal size (20 mm Phase 0 face or 25 mm baseline). Marble Mode is one voxel changing its own occupied volume. The two should not be mixed. See [inward-compaction.md](inward-compaction.md).

The locked hardware is a rigid cell. The Phase 0 20 mm sliding-pin face (Nd disc Ø6.0 × 2–3 mm hold, coil release-only, 7075-T6 plate, 3 hardened-steel latch pins) cannot collapse today. A later collapsible architecture is scheduled as a Phase 1 deliverable and cannot be validated until the Phase 0 rigid 20 mm face proof-of-concept (`DB-P0-FACE-TP-001`) has landed.

A rough mechanism, not a selected design: hinged, scissor, or tensegrity members fold the faces inward around a dense core (magnet, pins, compute, energy). A latch holds the packed sphere. The reverse sequence re-expands, re-locks the faces, and restores a dockable envelope. Packing fraction, packed diameter, unfold time, and cycle life are all TBD in the parent. No packing-ratio or launch-stow claim.

**Status note.** The Status field is **Phase 1 ready** only because [PHASE1.md](../../PHASE1.md#deliverables) already schedules this as a Phase 1 deliverable. It does not mean the joint is designed, built, or tested.

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

The only gates the repo already defines for this item are the proposed / TBD joint items in [PHASE1.md §6.4](../../PHASE1.md#64-marble-mode-collapsing-joint-proposed--tbd). They are **not** part of the §6.3 Phase 1 start exit, and they do not change P0-T1…T5 or P1-T1…T14.

| ID | Intent (as written in PHASE1.md) | Pass bar |
| :-- | :-- | :-- |
| P1-M1 | Fold and unfold one collapsing joint | TBD — do not treat any count as a gate |
| P1-M2 | Latch hold while packed | TBD |
| P1-M3 | Alignment after re-expansion; inherited T1–T5 remain the face gates once a re-expanded face is presented | TBD |
| P1-M4 | Joint between two modules, later than and not a substitute for P1-T1…T14 | TBD |

No other pass bar is set here.

## Assumptions

- Mechanism choice (hinged, scissor, or tensegrity) is a modeled option, not a selected or measured design.
- All packing, load, and cycle figures in the parent are illustrative / TBD, modeled, not measured.
- That a collapsing face can still meet soft-dock, hard-lock, shear, and cycle gates after re-expansion is an open question, not a result.

## Parent

Concept and intent: [dittobot/MODES.md §1](../MODES.md#1-marble-mode). Schedule and proposed tests: [PHASE1.md — Deliverables](../../PHASE1.md#deliverables) and [§6.4](../../PHASE1.md#64-marble-mode-collapsing-joint-proposed--tbd).

Paper until measured. Credit follows data.
