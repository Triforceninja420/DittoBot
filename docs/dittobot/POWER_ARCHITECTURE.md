# Power Architecture

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual**
Phase: unassigned. This is an architecture paper, not a numbered-phase placement and not a selected design. [PHASES.md](PHASES.md) already says the power-sharing architecture is not yet designed; Phase 2 requires a working share demo (P2-T4, P2-T5), not a new invented topology or current rating.

How a single cell charges, stores, and shares energy across the lattice. This file catalogs options and cites existing language. It does not retune the locked 25 mm cell core, change Phase 0 locks or CAD, rewrite [PHASE1.md](../PHASE1.md) or [PHASES.md](PHASES.md), or add a sharing architecture that [specs/power-sharing.md](specs/power-sharing.md) already declined to invent.

Paper until measured. Credit follows data.

---

## Inheritance

Inherits the locked 25 mm cell core, unchanged ([DESIGN.md](../DESIGN.md), [PAPER_STATUS.md](../PAPER_STATUS.md)):

- 25 mm cube envelope
- Centered Ø8.2 × 4.0 mm pocket (locked)
- Nd disc Ø6.0 × 2–3 mm hold; coil around the disc, release-only (Alnico off this cell)
- DRV8871, 12 V, pulse-only
- Axial pin hard-lock
- Full cavity potting and face coatings
- XIAO RP2040, 3.3 V; 36–48 V pulse bank

This paper does not retune that core. [LOCKS.md](../LOCKS.md) states the 36 V nominal pulse bank into the DRV8871 (stay under 45 V abs), and that the pulse bank and face bus stay fixture-side until contacts are covered or isolated. Those rules stay in force here.

---

## What the repo already says

The locked and proposed power language this paper may cite, and must not rewrite:

- Nominal cell / face bus is **12 V**. The pulse bank is **36–48 V** and is for coil release; [PHASE1.md §4.2](../PHASE1.md#42-voltage-and-current-limits) says the pulse bank is never on any face contact, and that a release-coil pulse never crosses the joint. Bank recharge from the bus is proposed at ≤ 0.25 A, counted inside the 1.25 A joint budget.
- Inherited soak / thermal gate: **1.25 A through the contact bus ≥ 10 min**, 41 °C skin cap. Same wording in [PHASE0.md](../PHASE0.md) success test 6, [LOCKS.md](../LOCKS.md) Phase 0 test 6, and inherited gate P0-T4 / [PHASE1.md](../PHASE1.md) P1-T7 (1.25 A × 10 min through the joint). This paper does not retune that gate.
- [PHASE1.md §4](../PHASE1.md#4-inter-module-power-handoff-proposed) is the proposed two-module power handoff on the Phase 0 face (pogos 1/2 = +12 V, 3/4 = GND, 5 = sense, 6 = data, as Phase 1 states it). Continuous transfer is proposed at ≤ 1.25 A per joint. Those values stay in their source document. Phase 1 is two modules and one joint; it is not a lattice architecture.
- [specs/power-sharing.md](specs/power-sharing.md) records the mid-term listing “Short-range inter-node power sharing” only. It does not define current, range, or topology, and it does not retune the 1.25 A soak gate.
- [COMMUNITY_ENHANCEMENT_SUITES.md — Mid-term lattice support](../COMMUNITY_ENHANCEMENT_SUITES.md#mid-term-lattice-support-small-assemblies) also lists, as names only: “Expanded local energy buffer,” “Swarm recovery / brownout consensus support,” and “Lattice-level simple load balancing hooks.” None of those bullets defines a mechanism, capacity, or threshold.
- [CONTROL_APP.md](../CONTROL_APP.md) (outline, not implemented) mentions “a simple battery estimate if energy cells are present.” It does not specify a cell chemistry or a storage size.

---

## Per-cell energy source options

No on-cell energy source is selected in the locked core. The options below are a catalog. **None is a design choice.** Capacities, charge rates, and efficiencies are **TBD**. Any figure that is not already in a source cited above would be a modeled assumption, not a measurement; this paper does not introduce one.

- **Battery.** Not specified in [DESIGN.md](../DESIGN.md) or [LOCKS.md](../LOCKS.md). [CONTROL_APP.md](../CONTROL_APP.md) allows for a battery estimate if energy cells are present. Chemistry, pack size, charge rate, and cycle life are TBD, modeled, not measured.
- **Supercapacitor.** Distinct from the existing 36–48 V polypropylene-film **pulse bank**, which is for coil release and must not appear on face contacts. A lattice energy buffer built from supercapacitors would be a new option under the “Expanded local energy buffer” listing, not a retune of that pulse bank. Capacitance and stored energy are TBD, modeled, not measured.
- **Kinetic.** Not present in the repo as a source. Catalogued here as an option only. Mechanism, harvested power, and efficiency are TBD, modeled, not measured.
- **RF harvesting.** Not present in the repo as a power source. A low-power RF discovery beacon is a communications / suite listing ([specs/rf-discovery-beacon.md](specs/rf-discovery-beacon.md)), not an energy harvester. If RF harvesting is ever considered, it is a separate modeled option; frequency, incident power, and efficiency are TBD, and it is not a locked radio.

**Charging.** How a standalone cell charges is TBD. In Phase 1, module A is fed from the fixture supply, per the LOCKS rule that the 12 V bus stays fixture-side. Any later on-cell charge from the 12 V face bus must stay inside the inherited joint current and must not put pulse-bank voltage on a face contact. Charge current, time, and efficiency are TBD, modeled, not measured.

**Storage.** The optional “Expanded local energy buffer” listing has no size. Buffer capacity is TBD. The pulse bank remains a release-only store at 36–48 V and is not the lattice energy reserve.

---

## Inter-cell sharing topology

No topology is selected. [PHASES.md](PHASES.md) states that current, duration, and topology for the Phase 2 share demo are **TBD**, and that inherited bus gates are not retuned. [specs/power-sharing.md](specs/power-sharing.md) likewise adds no architecture. The options below are a catalog, **modeled, not measured**.

- **Daisy chain.** Share only through successive docked joints, each joint still on the Phase 0 face bus. Each joint remains subject to the inherited ≤ 1.25 A continuous transfer (proposed Phase 1 wording, not retuned here). Hop count and per-path drop are TBD.
- **Bus.** A common 12 V path across more than one joint. This does not raise the inherited 1.25 A soak gate, and it does not invent a new current rating. How a multi-joint bus is fused, switched, or sectioned is TBD.
- **Wireless.** Not in the repo as a power path. Catalogued as an option only. It would not replace the wired 12 V pogo bus for Phases 0–3. Feasibility, range, and efficiency are TBD, modeled, not measured.

Phase 2 measurements that apply, without new bars: [P2-T4](PHASES.md#phase-2--four-module-lattice-demos) (share across a four-module lattice; log source/sink and bus V/I) and [P2-T5](PHASES.md#phase-2--four-module-lattice-demos) (open one joint during a share; remaining lock and power behavior). The required behavior on P2-T5 is already TBD.

---

## Safe-reserve rules

**No locked numeric safe-reserve threshold was found in the repository.**

The exact existing rule, from [POST_2040_OUTLOOK.md — Shared Constraints](../POST_2040_OUTLOOK.md#shared-constraints-all-modes), is: “Energy budget, thermal limits, and safe-reserve rules apply to every sequence. No mode may drop below safe reserve.” The same qualitative sentence is repeated in the post-2040 paper specs (including [specs/hierarchical-nesting.md](specs/hierarchical-nesting.md) and [specs/split-merge.md](specs/split-merge.md)): no mode may drop below safe reserve. [COMMUNITY_ENHANCEMENT_SUITES.md](../COMMUNITY_ENHANCEMENT_SUITES.md) lists brownout-consensus and energy-buffer *names* only. [LOCKS.md](../LOCKS.md), [DESIGN.md](../DESIGN.md), [PHASE0.md](../PHASE0.md), [PHASE1.md](../PHASE1.md), and [specs/power-sharing.md](specs/power-sharing.md) do not state a reserve percentage, voltage, or charge level.

This paper does **not** invent a threshold. Sharing, load balancing, charging, and harvest must not drop a node below safe reserve **once a threshold is chosen or measured**. Until then the threshold itself is **TBD, no pass bar set**.

[PHASE1.md §4.5](../PHASE1.md#45-fault-isolation) already has proposed under-voltage behavior at the two-module joint (B load off below 10.0 V; operating window 10.8–13.2 V). Those are proposed Phase 1 bus-window figures, not a lattice safe-reserve lock, and they are not restated as a new bar here.

---

## Load balancing across nodes

[COMMUNITY_ENHANCEMENT_SUITES.md](../COMMUNITY_ENHANCEMENT_SUITES.md#mid-term-lattice-support-small-assemblies) lists “Lattice-level simple load balancing hooks” with no mechanism. This paper does not add one.

A modeled policy, not a measurement and not a pass bar: prefer to source a share from nodes that still have headroom above safe reserve, and do not ask a node at or below reserve to source. Because the reserve threshold is not locked, that policy cannot be turned into a number here.

Thermal limits stay inherited. A thermal event is not “balanced” into a hotter path. [specs/thermal-isolation.md](specs/thermal-isolation.md) records the “Local thermal runaway isolation” listing only and does not change the 41 °C skin cap in [LOCKS.md](../LOCKS.md). Proposed Phase 1 F-THERM derates and then cuts a joint if the plate hits that cap; this paper does not retune that response.

---

## Single-cell power failure

At the two-module joint, [PHASE1.md §4.5](../PHASE1.md#45-fault-isolation) already proposes: over-current on B cuts that face’s power (A’s other faces and A’s logic stay up; lock held); under/over-voltage drops B’s load; link loss (F-LINK) removes power, keeps the mechanical lock, and allows re-handshake. Link loss alone does not undock. Those responses stay in Phase 1; this paper does not change them.

At lattice scale the behavior is **modeled, not measured**, and has no new bar:

- Isolate the failed node’s power path so a short or dead cell does not drag down neighbors.
- Remaining joints stay locked unless an explicit undock is later commanded.
- Remaining nodes may continue a share if they still have power. [P2-T5](PHASES.md#phase-2--four-module-lattice-demos) is the existing four-module measurement of “share behavior when a joint opens”; the required behavior is already TBD, no pass bar set.
- “Swarm recovery / brownout consensus support” remains an optional suite name, not a designed protocol.

A dead cell is a power and mesh event, not an automatic pin release.

---

## Test gates

TBD, no pass bar set. This paper adds no test IDs and no bars.

Existing IDs that already speak to power, and that this file does not rewrite: inherited P0-T4 / P1-T7 (1.25 A × 10 min soak), and Phase 2 [P2-T4](PHASES.md#phase-2--four-module-lattice-demos) and [P2-T5](PHASES.md#phase-2--four-module-lattice-demos).

---

## Assumptions

- No on-cell source, buffer size, topology, or safe-reserve number is selected in this paper. Those remain TBD, modeled, not measured.
- Catalog options (battery, supercapacitor, kinetic, RF harvest; daisy chain, bus, wireless) are not a design choice and are not measured capabilities.
- Inherited and proposed Phase 0 / Phase 1 bus figures (12 V, 1.25 A soak, 36–48 V pulse bank, proposed Phase 1 windows and fault responses) stay in their source documents. They are not new assumptions and are not retuned.
- Presence of a Community Enhancement Suite name is not a measured capability.

---

## Related

- [specs/power-sharing.md](specs/power-sharing.md)
- [specs/thermal-isolation.md](specs/thermal-isolation.md)
- [PHASES.md](PHASES.md) (P2-T4, P2-T5)
- [PHASE1.md §4](../PHASE1.md#4-inter-module-power-handoff-proposed)
- [COMMUNICATION_PROTOCOL.md](COMMUNICATION_PROTOCOL.md)
- [COMMUNITY_ENHANCEMENT_SUITES.md](../COMMUNITY_ENHANCEMENT_SUITES.md#mid-term-lattice-support-small-assemblies)
- [POST_2040_OUTLOOK.md](../POST_2040_OUTLOOK.md#shared-constraints-all-modes)
- [LOCKS.md](../LOCKS.md), [DESIGN.md](../DESIGN.md)

Paper until measured. Credit follows data.
