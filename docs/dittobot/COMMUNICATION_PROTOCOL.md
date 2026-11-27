# Communication Protocol

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual**
Phase: unassigned. This is an architecture paper, not a numbered-phase placement and not a rewrite of the Phase 1 face link. [PHASE1.md](../PHASE1.md) already scopes chains of three or more modules, and lattice or swarm behaviour, as out of Phase 1.

How nodes talk. The dock handshake on a Phase 0 face is the existing proposed language in [PHASE1.md §5](../PHASE1.md#5-inter-module-data-handoff-proposed). This paper cites that language and does not change it. Lattice-scale message types, routing, and Beacon use beyond that two-module link are conceptual. Carrier choice for Beacon remains TBD.

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

This paper does not retune that core, change Phase 0 locks or CAD, or rewrite [PHASE0.md](../PHASE0.md) or [PHASE1.md](../PHASE1.md).

---

## Face link and dock handshake (existing language, unchanged)

[PHASE0.md](../PHASE0.md) defines the mechanical face and the six pogo contacts (geometry, wipe, and the 1.25 A contact-bus thermal soak). It does not define a data handshake or a frame format. The existing handshake lives in [PHASE1.md §5](../PHASE1.md#5-inter-module-data-handoff-proposed), on that Phase 0 face, and is **proposed**, not measured. This paper uses that language as-is and does not change it.

As Phase 1 states it:

- **Physical:** single-wire half-duplex UART on pogo 6, open-drain, pull-up to 3.3 V on A (value TBD), referenced to GND pogos 3/4. Logic is 3.3 V (XIAO RP2040). Never put bus or coil voltage on this line. Phase 1 cites the contact assignment as pogo 1, 2 = +12 V; 3, 4 = GND; 5 = 12 V sense; 6 = spare / AGND sense, then uses pogo 6 as DATA. (PHASE1 points at a “PHASE0.md electrical section” for that assignment; the current [PHASE0.md](../PHASE0.md) file defines pogo geometry and the contact-bus soak, and does not itself contain that electrical table. The assignment is used here exactly as Phase 1 states it.)
- **Rate:** 115 200 baud, 8N1 (proposed).
- **Frame (proposed):** `SOF 0x7E | LEN (1) | TYPE (1) | SEQ (1) | PAYLOAD (0–64) | CRC-16/CCITT-FALSE (2)`.
- **Types already named:** `HELLO`, `HELLO_ACK`, `ID`, `ID_ACK`, `HB` (heartbeat), `STATUS`, `PWR_REQ`, `PWR_GRANT`, `UNDOCK_REQ`, `UNDOCK_ACK`, `BYE`, `NAK`.
- **Handshake and ID exchange** ([§5.3](../PHASE1.md#53-handshake-and-id-exchange)): after power good at B (S7), A sends `HELLO` every 20 ms until `HELLO_ACK` arrives, up to 200 ms; then `ID` / `ID_ACK` both ways (64-bit unique ID, face index, role A/B, firmware and protocol version `P1.0`, power capability). Protocol major versions must match, or the link stays in a safe minimum mode: power ≤ 0.25 A, no undock-by-peer. B requests load with `PWR_REQ`; A grants up to min(request, 1.25 A − own recharge) with `PWR_GRANT`. Heartbeat `HB` every 100 ms each way, carrying V, I, plate temperature, and lock state.
- **Arbitration on that joint:** “A is master; B transmits only in response or in its heartbeat slot.” That is a Phase 1 two-module role on one joint (fixed A/B roles; genderless faces out of scope). It is not a lattice-wide master, and this paper does not extend it into one.
- **Error handling** remains as [§5.4](../PHASE1.md#54-error-handling): CRC/framing `NAK` and retransmit; 3 missed heartbeats → F-LINK (power off, lock held, re-handshake from S7); `UNDOCK_REQ` without `UNDOCK_ACK` means no undock.

Dock order is already written in [PHASE1.md §3](../PHASE1.md#3-docking-sequence-proposed): lock (3/3) → sense probe → soft-start power → power good → data handshake. This paper does not change that order.

---

## Message types (lattice catalog)

The Phase 1 TYPE list above is the docked-joint vocabulary and is not rewritten here. For a lattice, the following uses are a catalog. Any new TYPE, payload, or timeout not already in Phase 1 is **TBD**, modeled, not measured, and must not replace the face handshake.

- **Dock handshake.** The Phase 1 `HELLO` / `HELLO_ACK` / `ID` / `ID_ACK` sequence on the Phase 0 face, unchanged. See above.
- **Power share request.** At one joint, this is already `PWR_REQ` / `PWR_GRANT` in Phase 1. A multi-node share request (who sources, who sinks, across more than one joint) is not yet designed; [PHASES.md](PHASES.md) leaves share topology TBD. Any lattice-level share request must still respect inherited bus gates and the safe-reserve rule in [POWER_ARCHITECTURE.md](POWER_ARCHITECTURE.md) (no locked numeric reserve was found; do not invent one).
- **Beacon ping.** A periodic ping from a designated, anchored node, used by Beacon Mode. Carrier is **TBD: RF, acoustic, or IR — not chosen**. See [Beacon SAR use](#beacon-sar-use) below. This is not a new locked radio, and it is not a SAR certification.
- **Command broadcast.** A command that should reach more than one node (for example a later control-app docking plan). Delivery method is TBD. There is no required master node; see [No master node](#no-master-node).
- **Status report.** At one joint, `HB` and `STATUS` already carry V, I, plate temperature, and lock state. Lattice-wide health aggregation is only named as “Node health score aggregation hooks” in [COMMUNITY_ENHANCEMENT_SUITES.md](../COMMUNITY_ENHANCEMENT_SUITES.md#mid-term-lattice-support-small-assemblies). Rate, payload, and aggregation are TBD, modeled, not measured.

---

## Latency and bandwidth assumptions

All lattice-scale latency and bandwidth figures are **modeled, not measured**, and are left **TBD**. This paper does not invent a hop delay, a mesh throughput, or a new baud rate.

The only numeric link figures in the repo for this path are the **proposed** Phase 1 values, cited unchanged and not treated as measured gates in this file: 115 200 baud, 8N1; `HELLO` every 20 ms for up to 200 ms; handshake complete target in P1-T11 of ≤ 200 ms after power good (a Phase 1 proposed bar, not restated here); `HB` every 100 ms; no-reply timeout 50 ms; F-LINK power off ≤ 300 ms after the last good frame (P1-T12). P1-T10 is a proposed frame-error gate on that same 115 200 baud link under the 1.25 A soak. Those IDs and bars stay in [PHASE1.md](../PHASE1.md).

---

## No master node

The lattice has **no required master node**. Routing and command delivery must keep working if any one node is lost.

This does not rewrite the Phase 1 joint rule that A is master on that two-module link. That rule stays a per-joint arbitration detail.

[CONTROL_APP.md](../CONTROL_APP.md) (outline, not implemented) talks to “one leader cell (or a USB/serial bridge)” and shows “leader status.” That is an app-facing contact, not a mesh root this paper promotes to a single point of failure. If the contact node is lost, another reachable node should be able to serve as the app contact. How that handoff works is TBD, modeled, not measured. This paper does not edit CONTROL_APP.md.

Optional listings that already point at shared, not centralized, recovery: “Swarm recovery / brownout consensus support” and “Lattice majority-vote hardware support” in [COMMUNITY_ENHANCEMENT_SUITES.md](../COMMUNITY_ENHANCEMENT_SUITES.md). They remain names only.

---

## Mesh vs hierarchical routing

**Early lattice (through Phase 2, and until a later phase says otherwise):** treat the docked face links as a **mesh**. Each locked joint carries the Phase 1 UART link. There is no selected mesh algorithm, hop limit, or routing metric in the repo; those are TBD, modeled, not measured.

**Hierarchical routing** is later organization, not the current default. It ties to [specs/hierarchical-nesting.md](specs/hierarchical-nesting.md) and [POST_2040_OUTLOOK.md §3](../POST_2040_OUTLOOK.md#3-hierarchical-nesting): an outer envelope holding a denser sub-lattice, with power, data, and mechanical continuity through both levels. [PHASES.md](PHASES.md) makes nesting the default organization only as a Phase 4 exit goal, not as a present fact.

**Split-merge** ([specs/split-merge.md](specs/split-merge.md), [POST_2040_OUTLOOK.md §5](../POST_2040_OUTLOOK.md#5-split--merge-swarm-scaling)) requires subgroups to re-form independent meshes and power domains on a split, and a unified mesh and bus on a merge. Safe-reserve and brownout rules apply to every subgroup; the reserve threshold itself is not locked (see [POWER_ARCHITECTURE.md](POWER_ARCHITECTURE.md)). How routes are cut and rejoined is TBD, modeled, not measured.

---

## What a lost node does

At one joint, Phase 1 already defines link loss: 3 missed heartbeats → F-LINK, power off, lock held, re-handshake from S7; no undock on link loss alone. That stays unchanged.

At lattice scale, **modeled, not measured**, no new bar:

- Neighbors treat missing `HB` / status as a lost node on that joint and isolate that power path, same family of response as F-LINK.
- The remaining mesh should keep carrying status and commands without a master. Reroute method is TBD.
- A lost ping in Beacon Mode already has a parent rule of “hold last heading or return to last good fix (rule TBD)” in [specs/beacon-mode.md](specs/beacon-mode.md) and [MODES.md](MODES.md#3-beacon-mode). This paper does not pick that rule.
- Diagnose flags already named in Repair Mode (no heartbeat, bus drop, failed dock) may mark the node; Repair itself stays conceptual and is not required here.

---

## Beacon SAR use

Beacon Mode is swarm convergence on a designated node, not a SAR certification and not a fielded system. See [specs/beacon-mode.md](specs/beacon-mode.md) and [MODES.md §3](MODES.md#3-beacon-mode).

It is related to, but not the same as, the SAR package in [SAR_MODES.md](../SAR_MODES.md): Search already sketches a sensor-gradient climb, and Signal flashes an LED or tone for location marking. Beacon Mode is convergence on one anchored emitter.

How this protocol is used, all **conceptual**:

- The beacon node stays anchored and emits a periodic **beacon ping**.
- **The Beacon carrier stays TBD (RF, acoustic, or IR, not chosen).** A low-power RF discovery beacon is only an optional suite listing ([specs/rf-discovery-beacon.md](specs/rf-discovery-beacon.md)); Beacon Mode would use something in that family, not a new locked radio. No frequency, power, range, or protocol is given in that listing.
- Other nodes sample the ping (signal strength on whatever carrier is later chosen) and move toward an increasing gradient, with the noise-handling and stop rules already written in the Beacon spec. The Phase 0 soft-dock window (≤ 2.5 mm lateral) is a face-dock gate, not a beacon-range number.
- Lost-ping and multi-beacon ID rules remain TBD in the Beacon parent. This paper does not invent them.

---

## Test gates

TBD, no pass bar set. This paper adds no test IDs and no bars.

Existing IDs that already speak to the face link, and that this file does not rewrite: P1-T10 (data-link integrity), P1-T11 (handshake + ID exchange), P1-T12 (link-loss safety). Phase 2 share logging in [P2-T4](PHASES.md#phase-2--four-module-lattice-demos) / [P2-T5](PHASES.md#phase-2--four-module-lattice-demos) may carry power-share request traffic; those rows stay as written in PHASES.md.

The repo defines no test IDs for Beacon Mode. PHASE1.md lists Beacon Mode as out of Phase 1 scope.

---

## Assumptions

- Lattice-scale types, routing, latency, bandwidth, lost-node reroute, and app-contact handoff are TBD, modeled, not measured.
- The Beacon carrier (RF, acoustic, or IR) is not chosen.
- Proposed Phase 1 link figures and TYPE names are cited from [PHASE1.md](../PHASE1.md) and are not new assumptions, not measured claims in this file, and not retuned.
- Presence of a Community Enhancement Suite name is not a measured capability.
- This is not a SAR certification and is not a fielded system.

---

## Related

- [PHASE1.md §5](../PHASE1.md#5-inter-module-data-handoff-proposed) (dock handshake, unchanged)
- [PHASE0.md](../PHASE0.md) (face and pogo geometry)
- [POWER_ARCHITECTURE.md](POWER_ARCHITECTURE.md)
- [specs/beacon-mode.md](specs/beacon-mode.md)
- [specs/rf-discovery-beacon.md](specs/rf-discovery-beacon.md)
- [SAR_MODES.md](../SAR_MODES.md)
- [specs/hierarchical-nesting.md](specs/hierarchical-nesting.md)
- [specs/split-merge.md](specs/split-merge.md)
- [PHASES.md](PHASES.md) (P2-T4, P2-T5)
- [MODES.md §3](MODES.md#3-beacon-mode)
- [CONTROL_APP.md](../CONTROL_APP.md) (outline; leader as app contact only)
- [COMMUNITY_ENHANCEMENT_SUITES.md](../COMMUNITY_ENHANCEMENT_SUITES.md)

Paper until measured. Credit follows data.
