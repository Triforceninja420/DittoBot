# DittoBot Post-2040 Outlook — Scale Change Modes

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

This is a **post-2040 speculative outlook**. It does **not** change locked Phase 0 criteria, 25 mm option A geometry, process locks in `LOCKS.md`, or any current build target. Two stacks stay unmixed. No V2.0 claim. No measured numbers here. Credit follows data when it arrives.

A mature lattice can change its occupied volume by orders of magnitude through coordinated reconfiguration. Individual cell envelopes stay the nominal size (20 mm Phase 0 face or 25 mm option A). Volume change comes from packing density, nesting, zoning, and node-count changes — not from shrinking or growing the cells themselves.

Matching optional suites that support these modes (energy, sync, sensing, recovery, soft skin, etc.) are listed by phase in [docs/COMMUNITY_ENHANCEMENT_SUITES.md](COMMUNITY_ENHANCEMENT_SUITES.md). All remain zero-impact on locked criteria.

---

## 1. Inward Compaction / Shrink Mode (Car → Basketball)

A car-scale (or larger) assembly collapses interstitial volume by moving modules inward and locking into a high-density packing whose outer envelope is roughly basketball-sized.

**Intent**  
Preserve every functional module (energy, structure, compute, mobility faces). End state is a dense, transportable or storable form that can later redeploy.

**Mechanism (outlook)**  
Release selected faces → translate or fold neighbors inward along lattice axes or free-form paths → nest/interlock into reduced void fraction → re-lock with bus and mesh continuity. Collective inward motion, not uniform cell scaling.

---

## 2. Outward Expansion / Deployment Mode (Basketball → Car and Beyond)

Exact inverse of inward compaction. A dense packing opens outward into vehicle-scale or larger structures in a coordinated sequence.

**Intent**  
Rapid deploy from storage or transport. One compact unit becomes a full structure without external scaffolding.

**Mechanism (outlook)**  
Release selected faces → modules translate or unfold outward along planned axes or free-form paths → expand void fraction while maintaining connectivity → re-lock into the target geometry. Same hybrid faces (EPM + pin) run in reverse. Energy and safe-reserve rules stay binding throughout the sequence.

---

## 3. Hierarchical Nesting

Future modules can accept or become sub-voxels. A single outer cell envelope holds a denser sub-lattice, giving multi-level volume change.

**Intent**  
Deeper shrink and finer expand without changing the outer 20 mm or 25 mm nominal. Enables extreme density packing and high-resolution surface detail from the same base cell.

**Mechanism (outlook)**  
Outer cells dock and form a stable envelope. Internal volume is filled by smaller sub-modules (or the same modules reconfigured into tighter hierarchical packing). Power, data, and mechanical continuity propagate through both levels. Sub-lattice can later eject or re-expand independently.

---

## 4. Variable-Density Zones

One continuous assembly maintains different packing densities in different regions at the same time.

**Intent**  
Keep a dense structural or energy core while growing a sparse outer shell for reach, surface area, or soft interaction. Or the reverse: sparse core with dense load-bearing shell.

**Mechanism (outlook)**  
Local groups of modules decide packing density based on role. Dense zones stay locked for strength and power distribution. Sparse zones expand for volume or compliance. Boundaries remain continuously docked so the lattice stays one mechanical and electrical body. Soft safety skin and 35 N human-contact interrupt remain active on any human-proximate surface.

---

## 5. Split / Merge Swarm Scaling

Change total volume by changing node count, not just packing density.

**Intent**  
One dense form splits into several smaller independent lattices. Multiple compact units merge into one larger structure. Scales from basketball-sized units to multi-vehicle or habitat-scale assemblies (and back) without permanent loss of modules.

**Mechanism (outlook)**  
Coordinated undock along a planned cut plane → subgroups re-form independent meshes and power domains → each subgroup can compact, expand, or travel separately. Merge is the reverse: approach, soft-dock, verify, hard-lock, then unified mesh and bus. Safe-reserve and brownout rules apply to every subgroup throughout.

---

## Shared Constraints (all modes)

- Phase 0 (20 mm hybrid face) and 25 mm option A geometry stay frozen.
- No change to EPM windings, drivers, force targets, or measurement cards.
- Community Enhancement Suites remain optional and zero-impact on locked criteria. See [docs/COMMUNITY_ENHANCEMENT_SUITES.md](COMMUNITY_ENHANCEMENT_SUITES.md).
- Energy budget, thermal limits, and safe-reserve rules apply to every sequence. No mode may drop below safe reserve.
- Soft safety skin, 35 N human-contact interrupt, and companion gates stay in force for any human-proximate use.
- Two stacks stay unmixed. No V2.0 claim.

## What is required later (not now)

- Higher-bandwidth local sensing and planning for coordinated multi-node motion.
- Proven dense-packing and hierarchical topologies that preserve power, data, and mechanical continuity.
- Measured reliability of repeated expand / compact / split / merge cycles.
- Optional secondary micro-actuation or compliant elements (kept optional).

Until those exist, these remain outlooks.

---

## Relation to current work

All near-term work stays on the locked baselines:
- 25 mm cell: fill `MEASUREMENT_CARD.md` (turns, R, peak I, ON/OFF).
- Phase 0: aluminum face plate, four EPMs to SOP, force and soak data.

These scale-change modes are additive future capability for a mature programmable-matter lattice. They do not reopen any lock.

---

*Updated 2026-11-06. Outlook only. Five modes: inward shrink, outward expansion, hierarchical nesting, variable-density zones, split/merge swarm scaling. Matching optional suites mapped in COMMUNITY_ENHANCEMENT_SUITES.md.*
