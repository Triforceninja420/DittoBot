# Repair Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.2
Status: **conceptual**
Phase: unassigned, would require new assumptions: a numbered phase after Phase 1 that includes swarm salvage and rebuild. Phase 1 explicitly lists Repair Mode as out of scope, and no later numbered phase exists in the repo.
Phase basis: [PHASE1.md](../../PHASE1.md) scope boundary (“Still out of scope: … Repair Mode”); [dittobot/MODES.md §2](../MODES.md#2-repair-mode) (conceptual until tested, no later phase named).

Damaged or dead voxels get cannibalized — the swarm consumes its own broken parts as raw material to rebuild functional ones.

This is the hardware analogue of the Mars bacteria swarm sim's near-extinction dormancy recovery in v2.13 (a spore-like / akinete pool). That mechanic is itself a modeled assumption, not a measurement. The sim recovery is not evidence this works in hardware. See [HONESTY_NOTE_residual_v2_13.md](../../mars/HONESTY_NOTE_residual_v2_13.md).

Material-flow concept from the parent (paper):

1. Diagnose — flag a voxel as damaged or dead (no heartbeat, bus drop, failed dock, or a failed face check).
2. Isolate — undock it from the live lattice and remove it from load and power paths before disassembly.
3. Disassemble — release pins, faces, and fasteners.
4. Sort / salvage — keep what can be reused; scrap or store the rest.
5. Rebuild / reintegrate — assemble a functional cell from salvaged parts plus remaining stores, then soft-dock, hard-lock, and rejoin the mesh.

What the parent already judges as realistically salvageable vs not (paper judgment, not measured):

- Likely reusable after inspection: Nd discs (Ø6.0 × 2–3 mm), latch pins, Option A sliding release pin, fasteners, seating springs, and undeformed face plates (7075-T6).
- Maybe reusable: electronics (for example XIAO RP2040, DRV8871, sensors) if they still pass a bench check; pogo contacts if not bent.
- Not re-manufacturable in the field without a fab: printed or polymer structural parts, potting, damaged coils, deformed plates, failed magnets. This mode is salvage and reassembly, not in-situ reprinting.

Safety, from the parent: never cannibalize critical structural or load-path nodes. Require a structural check before removal. Isolate electrically first. A later undock order may follow the Phase 1 pattern (`DB-P1-DOCK-TP-001`); that is a pattern to reuse, not a Phase 1 requirement today.

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

TBD, no pass bar set. The repo does not define test IDs for Repair Mode. PHASE1.md lists Repair Mode as out of Phase 1 scope.

## Assumptions

- The salvage vs scrap split is a paper judgment, modeled, not measured. No reuse rate or rebuild time has been measured.
- The parallel to v2.13 dormancy recovery is conceptual only; that sim mechanic is itself modeled, not measured.
- Field rebuild without a fab is limited to reassembly of salvaged parts, as the parent already states.

## Parent

[dittobot/MODES.md §2](../MODES.md#2-repair-mode).

Paper until measured. Credit follows data.
