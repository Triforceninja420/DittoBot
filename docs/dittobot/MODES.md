# Feature Modes — Marble, Repair, Beacon

Design owner: Craig.
Date: 2026-11-27.
Status: **conceptual roadmap additions**. Not committed Phase 0 or Phase 1 work. Does not change locked Phase 0 face geometry, the Phase 1 docking protocol, 25 mm baseline, process locks, measurement cards, or any sim number.

These three modes are swarm and lattice behaviors sketched for later, after Phase 0 hardware learnings exist (`DB-P0-FACE-TP-001`) and Phase 1 two-module docking (`DB-P1-DOCK-TP-001`) has been measured. Paper until tested. Credit follows data.

Do not confuse this file with:

- [MODES.md](../MODES.md) — wearable / application inheritance (flight suit, exo, armored shell, companion, vehicle, habitat)
- [SAR_MODES.md](../SAR_MODES.md) — Search / Rescue / Signal package
- [POST_2040_OUTLOOK.md](../POST_2040_OUTLOOK.md) — multi-module inward compaction and outward expansion (many rigid voxels packing tighter, not one voxel collapsing)

Any packing ratios, ranges, or cycle counts below are **illustrative / TBD**, not measured. No test results are claimed.

---

## 1. Marble Mode

A single voxel collapses into a dense sphere for compact transport and re-expands into a dockable lattice cell on arrival.

**Intent.** Mars swarm logistics: ship modules compact, deploy spread out. Same idea applies to any tight payload volume — a crate, a lander bay, a backpack — then a later re-expansion into a face-compatible cell.

**Relation to existing outlook.** [POST_2040_OUTLOOK.md](../POST_2040_OUTLOOK.md) already describes an inward-compaction path in which *many* modules release selected faces, move inward, and lock into a denser packing (car-scale down to roughly basketball-sized). That path keeps each cell envelope at its nominal size (20 mm Phase 0 face or 25 mm baseline). Marble Mode is a different, later idea: *one* voxel changing its own occupied volume. The two should not be mixed.

**Physical concept (conceptual, pending Phase 0 hardware learnings).**
The locked hardware is a rigid cell: 25 mm cube baseline, or the Phase 0 20 mm sliding-pin face (Nd disc Ø6.0 × 2–3 mm hold, coil release-only, 7075-T6 plate, 3 hardened-steel latch pins). That article cannot collapse today. Marble Mode would need a later collapsible architecture built only after that face is measured.

A rough mechanism, not a selected design: hinged, scissor, or tensegrity members fold the faces inward around a dense core (magnet, pins, compute, energy). A latch holds the packed sphere for transport. The reverse sequence re-expands the members, re-locks the faces, and restores a dockable envelope so the cell can soft-dock and hard-lock again. Packing fraction, packed diameter, unfold time, and cycle life are all TBD.

**Open questions that wait on Phase 0.** Whether a collapsing face can still meet soft-dock, hard-lock, shear, and cycle gates after re-expansion. Pin alignment and contact clocking after a fold. Magnet / coil survival through fold cycles. Mass and whether the packed form is actually a sphere or just a rounded brick.

**Status.** Conceptual until tested. No packing-ratio claim, no launch-stow claim, no Phase 0 work.

---

## 2. Repair Mode

Damaged or dead voxels get cannibalized — the swarm consumes its own broken parts as raw material to rebuild functional ones.

**Honest parallel.** This is the hardware analogue of the Mars bacteria swarm sim's near-extinction dormancy recovery in v2.13 (a spore-like / akinete pool that germinates when the live population drops). That mechanic is itself a **modeled assumption, not a measurement** — no akinete formation rate or dormant survival has been measured for the strain under Mars-habitat conditions. See [mars/HONESTY_NOTE_residual_v2_13.md](../mars/HONESTY_NOTE_residual_v2_13.md). Repair Mode inherits the same honesty rule: conceptual until tested. The sim recovery is not evidence this works in hardware.

**Material-flow concept (paper).**

1. **Diagnose** — flag a voxel as damaged or dead (no heartbeat, bus drop, failed dock, or a failed face check).
2. **Isolate** — undock it from the live lattice and remove it from load and power paths before anyone starts taking it apart.
3. **Disassemble** — release pins, faces, and fasteners.
4. **Sort / salvage** — keep what can be reused; scrap or store the rest.
5. **Rebuild / reintegrate** — assemble a functional cell from salvaged parts plus remaining stores, then soft-dock, hard-lock, and rejoin the mesh.

**What is realistically salvageable vs not** (paper judgment, not measured):

- **Likely reusable after inspection:** Nd discs (Ø6.0 × 2–3 mm), latch pins, Option A sliding release pin, fasteners, seating springs, and undeformed face plates (7075-T6).
- **Maybe reusable:** electronics (for example XIAO RP2040, DRV8871, sensors) if they still pass a bench check; pogo contacts if not bent.
- **Not re-manufacturable in the field without a fab:** printed or polymer structural parts, potting, damaged coils, deformed plates, failed magnets. Repair Mode is salvage and reassembly, not in-situ reprinting. A later fab or seed-bot path is a separate paper track (`docs/mars/`) and is out of scope here.

**Safety.** Never cannibalize critical structural or load-path nodes. Require a structural check before removal: the remaining lattice must still carry load after the node is taken out (pin hard-lock on the remaining joints; no removal that opens a required shear path or drops the assembly below safe reserve). Isolate electrically first. A later undock order can follow the Phase 1 pattern (`DB-P1-DOCK-TP-001`); that is a pattern to reuse, not a Phase 1 requirement today.

**Status.** Conceptual until tested. No reuse-rate or rebuild-time claim.

---

## 3. Beacon Mode

One voxel stays fixed and emits a ping; the rest of the swarm navigates toward it. Literal search-and-rescue application: distress-signal convergence.

**Why this is the closest of the three to real-world use.** It needs a fixed emitter, a receiver on mobile nodes, and a walk-uphill rule. It does not need collapsing cells or a salvage fab. It is still conceptual. **Do not claim SAR certification or real-world readiness.**

Related to, but not the same as, [SAR_MODES.md](../SAR_MODES.md): Search already sketches a sensor-gradient climb, and Signal flashes an LED or tone for location marking. Beacon Mode is swarm *convergence on a designated node*.

**Navigation concept (paper).**

- The beacon node stays anchored (docked or otherwise fixed) and emits a periodic ping. Carrier is TBD: RF RSSI, acoustic, or IR. A low-power RF discovery beacon is already listed as an optional suite in [COMMUNITY_ENHANCEMENT_SUITES.md](../COMMUNITY_ENHANCEMENT_SUITES.md); this mode would use something in that family, not a new locked radio.
- Other nodes sample signal strength and move toward an increasing gradient.
- **Noise handling:** average more than one sample; ignore one-sample spikes; require more than one heading sample to agree before a move. If the gradient is flat, run a short search or spiral, then resume.
- **Stopping / aggregation:** approach until the signal is above a latch threshold (TBD) or the node is close enough to attempt a dock. Soft-dock capture on the Phase 0 face is ≤ 2.5 mm lateral — that is a face-dock number, not a beacon-range number, and is not a Beacon Mode spec. Stop short of climbing onto the beacon or dismantling it. Form a perimeter or join the lattice.
- **Failures:** lost ping → hold last heading or return to last good fix (rule TBD). Multiple beacons need an ID so the swarm does not split (TBD).

**Status.** Conceptual until tested. Closest of the three to a later software-and-sensor demo, once Phase 0 / Phase 1 docking is measured. Still not a fielded SAR system.

---

## What this does not change

- Phase 0 locked 20 mm sliding-pin face, Nd disc Ø6.0 × 2–3 mm, 3 latch pins, test plan `DB-P0-FACE-TP-001`
- Phase 1 two-module docking, test plan `DB-P1-DOCK-TP-001`
- 25 mm baseline, `LOCKS.md`, measurement cards
- Mars sim numbers or honesty notes, except the v2.13 recovery parallel cited above
- The existing content of `MODES.md`, `SAR_MODES.md`, and `POST_2040_OUTLOOK.md`

Paper until measured. Credit follows data.
