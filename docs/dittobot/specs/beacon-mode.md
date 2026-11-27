# Beacon Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual**

One voxel stays fixed and emits a ping; the rest of the swarm navigates toward it. Literal search-and-rescue application: distress-signal convergence. The parent calls this the closest of Marble, Repair, and Beacon to real-world use, because it needs a fixed emitter, a receiver on mobile nodes, and a walk-uphill rule — not collapsing cells or a salvage fab. It is still conceptual. Do not claim SAR certification or real-world readiness.

Related to, but not the same as, the SAR package ([SAR_MODES.md](../../SAR_MODES.md)): Search already sketches a sensor-gradient climb, and Signal flashes an LED or tone for location marking. Beacon Mode is swarm convergence on a designated node.

Navigation concept from the parent (paper):

- The beacon node stays anchored and emits a periodic ping. Carrier is TBD: RF RSSI, acoustic, or IR. A low-power RF discovery beacon is already listed as an optional suite; this mode would use something in that family, not a new locked radio. See [rf-discovery-beacon.md](rf-discovery-beacon.md).
- Other nodes sample signal strength and move toward an increasing gradient.
- Noise handling: average more than one sample; ignore one-sample spikes; require more than one heading sample to agree before a move. If the gradient is flat, run a short search or spiral, then resume.
- Stopping / aggregation: approach until the signal is above a latch threshold (TBD) or the node is close enough to attempt a dock. Soft-dock capture on the Phase 0 face is ≤ 2.5 mm lateral — that is a face-dock number from the locked Phase 0 gates, not a beacon-range number, and is not a Beacon Mode spec. Stop short of climbing onto the beacon or dismantling it.
- Failures: lost ping → hold last heading or return to last good fix (rule TBD). Multiple beacons need an ID so the swarm does not split (TBD).

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

TBD, no pass bar set. The repo does not define test IDs for Beacon Mode. PHASE1.md lists Beacon Mode as out of Phase 1 scope. The Phase 0 soft-dock window (≤ 2.5 mm lateral) is a face-dock gate, not a Beacon Mode range or RSSI bar.

## Assumptions

- Carrier choice (RF, acoustic, or IR), latch threshold, lost-ping rule, and multi-beacon ID are TBD in the parent, modeled, not measured.
- No range, update rate, or field-readiness figure is claimed.
- This is not a SAR certification and is not a fielded system.

## Parent

[dittobot/MODES.md §3](../MODES.md#3-beacon-mode). Related listing: [COMMUNITY_ENHANCEMENT_SUITES.md](../../COMMUNITY_ENHANCEMENT_SUITES.md#post-2040-enablers-scale-change-modes).

Paper until measured. Credit follows data.
