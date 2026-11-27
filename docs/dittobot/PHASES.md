# DittoBot phases

Design owner: Craig.
Date: 2026-11-27.
Status: **proposed / paper only**. Credit follows measured data.

This file indexes the numbered phases and defines Phase 2, Phase 3, and Phase 4. It does not change Phase 0 locks, Phase 1 docking criteria (P1-T1…T14), the locked 25 mm cell core for Phases 0–3, any existing spec status, or [PHASE1.md](../PHASE1.md). Every value below is **proposed** unless it is quoted from an existing locked source. **TBD** means a number must be chosen or measured before the relevant phase's test start. No pass bars are invented here.

Paper until measured. Credit follows data.

---

## Index

- **Phase 0** — one 20 mm docking face. See [PHASE0.md](../PHASE0.md). Test plan `DB-P0-FACE-TP-001`.
- **Phase 1** — two-module docking on the unchanged Phase 0 face protocol, plus scheduled Marble Mode joint work. See [PHASE1.md](../PHASE1.md). Test plan `DB-P1-DOCK-TP-001` (P1-T1…T14).
- **Phase 2** — four-module lattice demos, defined below.
- **Phase 3** — 60–200 module field trial, defined below.
- **Phase 4** — post-2040 / V2.0-territory work, defined below.
- **Phase 5+** — not defined yet.

---

## Inheritance (all numbered phases)

The locked 25 mm cell core is unchanged for Phases 0–3 ([DESIGN.md](../DESIGN.md), [PAPER_STATUS.md](../PAPER_STATUS.md)):

- 25 mm cube envelope
- Centered Ø8.2 × 4.0 mm pocket (locked)
- Nd disc Ø6.0 × 2–3 mm hold; coil around the disc, release-only (Alnico off this cell)
- DRV8871, 12 V, pulse-only
- Axial pin hard-lock; full cavity potting and face coatings

Phases 2 and 3 use the unchanged Phase 0 face protocol. They do not retune that core, rewrite Phase 0 or Phase 1 gates, or mix the two stacks except as already allowed in `HARDWARE_MAPPING.md`. A 1 cm node density may be targeted in Phase 4 only; it is not locked or validated, and it does not unlock or retune the 25 mm cell for Phases 0–3.

---

## Phase 2 — four-module lattice demos

### Goal

A four-module build with working demos:

- docking between modules
- power sharing across the lattice
- at least one payload swap (an [EX-MOD](../EX_MOD.md) or [BAR-MOD](../BAR_MOD.md) actually firing)

Phase 2 proves the lattice scales past two nodes without breaking the Phase 0 face protocol. It also earns the right to talk about Marble Mode, because a collapsing joint between modules becomes testable at that size. See the overlap note below — Marble is already scheduled in Phase 1, and this phase carries that work forward at four-module scale rather than quietly moving it.

### Entry criteria

**Phase 1 complete**, as defined by [PHASE1.md §6.3 Exit criteria for Phase 1 start](../PHASE1.md#63-exit-criteria-for-phase-1-start):

- inherited P0-T1…T5 pass on both faces
- P1-T1…T14 pass

Those IDs and their bars live in [PHASE1.md](../PHASE1.md) and are not restated here.

Phase 1's scheduled Marble items P1-M1…P1-M4 are **not** part of the §6.3 exit. Completing Phase 1 start does not require the Marble joint to have been demonstrated. Any Phase 1 Marble progress (or lack of it) is carried into Phase 2 as context, not as a rewritten entry gate.

### Exit criteria

All of the following. The Marble item may instead be **explicitly deferred with a written reason**, recorded against P2-T9.

1. **Four modules docked** into one lattice on the unchanged Phase 0 face protocol (P2-T1…P2-T3).
2. **Power shared** across that lattice, beyond the Phase 1 single-joint handoff (P2-T4).
3. **One payload fired** — an EX-MOD actually discharges, or a BAR-MOD panel actually deploys, after being docked into the lattice (P2-T6, P2-T7).
4. **Marble joint demonstrated** at four-module scale (P2-T9), **or** explicitly deferred with a reason.

Results go into a Phase 2 section of a measurement card. Creating that card is a separate commit; it is not part of this file. Paper and sim numbers are not the credit. Measured numbers are the credit.

### Scope and honesty

- Not a swarm, not a chain of five or more, not a genderless-face redesign, not a V2.0 claim.
- Not Phase 3+.
- Power-sharing architecture is not yet designed. [specs/power-sharing.md](specs/power-sharing.md) records the mid-term listing in [COMMUNITY_ENHANCEMENT_SUITES.md](../COMMUNITY_ENHANCEMENT_SUITES.md#mid-term-lattice-support-small-assemblies) only; this phase requires a working share demo, not a new invented topology or current rating.
- Payload performance figures in [EX_MOD.md](../EX_MOD.md) and [BAR_MOD.md](../BAR_MOD.md) are paper. They are not Phase 2 pass bars.
- Existing soak and shear numbers (including the 1.25 A × 10 min gate and the 40 N shear target) stay inherited. They are not retuned and are not restated as new Phase 2 bars.

### Marble overlap with Phase 1

[PHASE1.md](../PHASE1.md#deliverables) already schedules Marble Mode as a Phase 1 deliverable, with proposed tests P1-M1…P1-M4 in [§6.4](../PHASE1.md#64-marble-mode-collapsing-joint-proposed--tbd). That work is additive and is **not** a §6.3 exit criterion. The current Phase 0 face is still rigid and cannot collapse; a collapsing architecture remains later work. See also [specs/marble-mode.md](specs/marble-mode.md).

This file does **not** move Marble out of Phase 1, rewrite P1-M1…P1-M4, or edit those documents. Phase 2's Marble item (P2-T9) is the **inter-module collapsing-joint demo at four-module scale**, building on and carrying forward the Phase 1 joint work. Whether Marble should be formally moved from Phase 1 to Phase 2 is a separate decision and is not made here.

### Test plan (proposed / TBD)

Every threshold below is **TBD, no pass bar set**. None is a measured gate. Numbers must be chosen or measured before Phase 2 test start.

| ID | Intent | Proposed measurement | Pass bar |
| :-- | :-- | :-- | :-- |
| P2-T1 | Four-module dock | Assemble four modules into one lattice on the unchanged Phase 0 face protocol. Record, for each joint: dock attempt, capture result, and any Phase 0 / Phase 1 protocol error. | TBD, no pass bar set |
| P2-T2 | Four-module hard-lock | Record pin seating at every joint (3/3 or not) after the dock sequence. | TBD, no pass bar set |
| P2-T3 | Face protocol unchanged | Confirm the four-module lattice still uses the Phase 0 20 mm sliding-pin face protocol (no genderless redesign, no rewritten T1–T5). Record a protocol checklist against [PHASE0.md](../PHASE0.md) and the inherited gates. | TBD, no pass bar set |
| P2-T4 | Power sharing across the lattice | With four modules docked, share power across the lattice (more than the Phase 1 single-joint A→B handoff). Log which nodes source and sink, and bus voltage and current at each joint during a share interval. Current, duration, and topology are TBD. Do not retune inherited bus gates. See [specs/power-sharing.md](specs/power-sharing.md). | TBD, no pass bar set |
| P2-T5 | Share behavior when a joint opens | Open or undock one joint while a share is in progress. Record whether the remaining lattice holds lock and how power behaves (continues, isolates, or shuts down). The required behavior is TBD. | TBD, no pass bar set |
| P2-T6 | Payload swap into the lattice | Dock at least one [EX-MOD](../EX_MOD.md) or [BAR-MOD](../BAR_MOD.md) into the four-module lattice on the Phase 0 face. Record which payload, which node, and dock / lock state. | TBD, no pass bar set |
| P2-T7 | Payload fire | With that payload docked, actually fire it: EX-MOD discharges, or BAR-MOD panel deploys. Record the activation command and the observed discharge or deployment. Paper duration or size figures in those docs are not Phase 2 bars. | TBD, no pass bar set |
| P2-T8 | Lattice intact after fire | After the payload fires, record lock state at every remaining joint and any bus drop. | TBD, no pass bar set |
| P2-T9 | Marble joint at four-module scale | Demonstrate a collapsing joint on at least one module in the four-module lattice: pack and latch, then re-expand, and record whether the re-expanded face can still attempt a Phase 0 dock. This carries forward [PHASE1.md §6.4](../PHASE1.md#64-marble-mode-collapsing-joint-proposed--tbd) (P1-M1…P1-M4); it does not replace those IDs. If the demo is not run, record an explicit deferral reason instead. | TBD, no pass bar set |

---

## Phase 3 — 60–200 module field trial

### Goal

A 60–200 module lattice in the field, still on the locked 25 mm cell and the unchanged Phase 0 face protocol, with:

- real field payloads: an [EX-MOD](../EX_MOD.md) used on an actual fire, and/or a [BAR-MOD](../BAR_MOD.md) blocking a real breach
- one physical prototype each of a companion mode and a tool mode ([COMPANION_TOOL_MODES.md](COMPANION_TOOL_MODES.md))
- a first honest field trial, even a backyard SAR drill ([SAR_MODES.md](../SAR_MODES.md))

Craig's brief for this phase calls 60–200 modules the V1.0 industrial range from the original roadmap. **That range and the label “V1.0 industrial range” were not found as existing roadmap language in this repository.** [LOCKS.md](../LOCKS.md) explicitly lists “Node count for a swarm or suit” as not locked. This document therefore adopts 60–200 modules as the Phase 3 range defined here, not as a prior lock.

### Entry criteria

**Phase 2 complete**, as defined by the Phase 2 exit criteria above:

- four modules docked (P2-T1…P2-T3)
- power shared across that lattice (P2-T4)
- one payload fired (P2-T6, P2-T7)
- the Marble joint demonstrated at four-module scale, or explicitly deferred with a reason (P2-T9)

Those IDs and their bars live in the Phase 2 section and are not restated here. A recorded P2-T9 deferral does not rewrite Phase 2; it is carried into Phase 3 as context.

### Exit criteria

All of the following:

1. **60–200 modules operating** as one lattice (or a documented set of jointly operated lattices) on the locked 25 mm cell and the Phase 0 face protocol (P3-T1).
2. **At least one real payload fired in field conditions** — EX-MOD on an actual fire, or BAR-MOD blocking a real breach (P3-T3 and/or P3-T4).
3. **One companion-mode prototype and one tool-mode prototype**, each physical, not paper-only (P3-T5, P3-T6).
4. **One field trial completed** with documented results, even if the trial is a backyard SAR drill (P3-T7, P3-T8).

Results go into a Phase 3 section of a measurement card. Creating that card is a separate commit. Paper and sim numbers are not the credit. Measured numbers are the credit. No fielded-capability claim is made until those results are documented.

### Safety

Live-fire and breach tests run only under supervision and with any required permits. They are proposed field measurements, not a license to improvise. Companion and tool prototypes remain subject to the existing companion gates in [LOCKS.md](../LOCKS.md) (including the 35 N human-contact interrupt and “no companion claim” until a filled measurement card exists). Nothing in this phase certifies a companion robot, a fire-suppression product, or a fielded SAR system.

### Scope and honesty

- The locked 25 mm cell core and the Phase 0 face protocol stay unchanged in Phase 3. This phase is a scale and field step, not a cell redesign.
- Payload figures in [EX_MOD.md](../EX_MOD.md) and [BAR_MOD.md](../BAR_MOD.md) remain paper. They are not Phase 3 pass bars.
- [COMPANION_TOOL_MODES.md](COMPANION_TOOL_MODES.md) is a conceptual catalog. Phase 3 asks for one physical companion prototype and one physical tool prototype from that catalog (or from the already-specified EX-MOD / BAR-MOD tool entries). It does not promote the rest of the catalog.
- [SAR_MODES.md](../SAR_MODES.md) is paper / software + sensor-stub only. A backyard drill with documented results is an honest first trial, not a SAR certification.

### Test plan (proposed / TBD)

Every threshold below is **TBD, no pass bar set**. None is a measured gate. Numbers must be chosen or measured before Phase 3 test start.

| ID | Intent | Proposed measurement | Pass bar |
| :-- | :-- | :-- | :-- |
| P3-T1 | 60–200 modules operating | Assemble and operate a lattice of 60–200 modules on the locked 25 mm cell and the Phase 0 face protocol. Record the operating node count, and a joint dock / lock summary. | TBD, no pass bar set |
| P3-T2 | Continuity at that scale | With that lattice operating, record whether power and the inter-module link still function across the set (source/sink or bus log, and any joint dropouts). Current, duration, and topology remain TBD. Do not retune inherited bus gates. | TBD, no pass bar set |
| P3-T3 | EX-MOD on an actual fire | Under supervision and with any required permits, use a docked [EX-MOD](../EX_MOD.md) on an actual fire. Record the setting, supervision/permit, activation, and the observed effect. Paper discharge figures in that doc are not Phase 3 bars. | TBD, no pass bar set |
| P3-T4 | BAR-MOD on a real breach | Under supervision and with any required permits, use a docked [BAR-MOD](../BAR_MOD.md) to block a real breach. Record the setting, supervision/permit, deployment, and the observed effect. Paper panel figures in that doc are not Phase 3 bars. Exit requires at least one of P3-T3 or P3-T4. | TBD, no pass bar set |
| P3-T5 | Physical companion-mode prototype | Build one physical prototype of a companion mode from [COMPANION_TOOL_MODES.md](COMPANION_TOOL_MODES.md#companion-modes) (the wearable soft-companion paper spec may be the basis, but the prototype itself must be physical). Record which mode, that it is hardware, and any measurement-card / companion-gate notes. | TBD, no pass bar set |
| P3-T6 | Physical tool-mode prototype | Build one physical prototype of a tool mode from [COMPANION_TOOL_MODES.md](COMPANION_TOOL_MODES.md#tool-modes). Record which mode and that it is hardware. A Phase 2 EX-MOD or BAR-MOD fire demo is not, by itself, this prototype unless the Phase 3 article is itself a physical tool build and is recorded as such. | TBD, no pass bar set |
| P3-T7 | First honest field trial | Run one field trial with documented results, even a backyard drill using the Search / Rescue / Signal package in [SAR_MODES.md](../SAR_MODES.md). Record the setting, procedure, what was attempted, what happened, and what failed. This is not a SAR certification. | TBD, no pass bar set |
| P3-T8 | Documented results; no fielded claim | File the Phase 3 results (payload, prototypes, and trial) in the measurement-card section. Record that no fielded-capability claim is made until that documentation exists. | TBD, no pass bar set |

---

## Phase 4 — post-2040 / V2.0 territory

### Goal

Phase 4 is post-2040, V2.0-territory work. [POST_2040_OUTLOOK.md](../POST_2040_OUTLOOK.md) is a **post-2040 speculative outlook** and states **No V2.0 claim**; it does not change locked Phase 0 criteria, 25 mm option A geometry, process locks, or any current build target. [LOCKS.md](../LOCKS.md) likewise does **not** create V2.0, and lists **V2.0 as a product** as explicitly not locked. No other V2.0 product roadmap text was found in the repository. This phase is where that later territory is now being numbered; it does not mint a V2.0 product by writing the heading.

This phase aims for:

- denser nodes targeting **1 cm cubes** (a target only — see Node size below)
- [hierarchical nesting](specs/hierarchical-nesting.md) and [split-merge](specs/split-merge.md) as the **default organization**
- Marble Mode at scale, **expected if** the Phase 1 / Phase 2 results hold, not as already solved
- the companion line moving from the Phase 3 prototype to a **household product**, which is the original motivation for this phase

### Node size

**1 cm is a target, not locked or validated.** The 25 mm cell stays locked for Phases 0–3.

The repository does not describe a “current 4–8 cm” linear node. The only 4–8 wording is in [EX_MOD.md](../EX_MOD.md) and [BAR_MOD.md](../BAR_MOD.md): **“Envelope: 4–8 cm³ node class (compatible with current baseline).”** That is a **volume** class (cubic centimetres), not an edge length. The locked cell is a **25 mm cube** (2.5 cm edge; 15.625 cm³ volume). Those three figures are not the same: 4–8 cm as a linear size is not in the repo; 4–8 cm³ is smaller than the locked 25 mm cube’s volume, even though the payload docs call that class compatible with the baseline. Phase 4 uses the repo’s wording and does not treat 4–8 cm as the current node edge.

A further tension: [POST_2040_OUTLOOK.md](../POST_2040_OUTLOOK.md) says individual cell envelopes stay the nominal size (20 mm Phase 0 sliding-pin face or 25 mm option A), and that volume change comes from packing density, nesting, zoning, and node-count changes — **not from shrinking or growing the cells themselves**. The 1 cm density target is therefore a new Phase 4 goal, not a size already unlocked by the outlook. It does not rewrite that outlook, and it does not unlock the 25 mm cell for earlier phases.

### Entry criteria

**Phase 3 complete**, as defined by the Phase 3 exit criteria above:

- 60–200 modules operating (P3-T1)
- at least one real payload fired in field conditions (P3-T3 and/or P3-T4)
- one physical companion prototype and one physical tool prototype (P3-T5, P3-T6)
- one field trial completed with documented results (P3-T7, P3-T8)

Those IDs and their bars live in the Phase 3 section and are not restated here.

### Exit criteria

All of the following:

1. **1 cm node density achieved** as a measured result against the 1 cm target (P4-T1). Achieving it does not lock 1 cm, and it does not change the 25 mm lock for Phases 0–3.
2. **Hierarchical nesting and split-merge as the default organization** (P4-T2, P4-T3).
3. **Marble Mode working at scale** (P4-T4), expected if the Phase 1 / Phase 2 Marble results hold; not treated as already solved at entry.
4. **Companion product in households** (P4-T5), still subject to the companion gates in [LOCKS.md](../LOCKS.md).

Results go into a Phase 4 section of a measurement card. Creating that card is a separate commit. Paper and sim numbers are not the credit. Measured numbers are the credit.

### Scope and honesty

- This phase does not rewrite [POST_2040_OUTLOOK.md](../POST_2040_OUTLOOK.md), [LOCKS.md](../LOCKS.md), [PHASE1.md](../PHASE1.md), or the Phase 2 / Phase 3 sections above.
- [specs/hierarchical-nesting.md](specs/hierarchical-nesting.md) and [specs/split-merge.md](specs/split-merge.md) remain conceptual paper specs until Phase 4 measurements exist. Making them the default organization is an exit goal, not a present fact.
- Marble overlap continues to be handled as in the Phase 2 section: Marble is already scheduled in Phase 1 (P1-M1…P1-M4, not a §6.3 exit) and carried forward at four-module scale by P2-T9 (or explicitly deferred). Phase 4 does not move those IDs, does not treat the collapsing joint as already solved, and only asks for scale if the earlier results hold.
- Companion as a household product remains subject to “no companion claim” until a filled measurement card exists, the 35 N human-contact interrupt, and the other companion gates. [LOCKS.md](../LOCKS.md) still does not certify a companion robot, and V2.0 as a product remains not locked.

### Test plan (proposed / TBD)

Every threshold below is **TBD, no pass bar set**. None is a measured gate. Numbers must be chosen or measured before Phase 4 test start.

| ID | Intent | Proposed measurement | Pass bar |
| :-- | :-- | :-- | :-- |
| P4-T1 | 1 cm node density | Measure the envelope of the denser node against the 1 cm cube target. Record the measured edge (or bounding box) and that 1 cm is a target, not a lock. Record that the 25 mm cell remains locked for Phases 0–3. | TBD, no pass bar set |
| P4-T2 | Hierarchical nesting as default organization | Operate a lattice whose default organization is hierarchical nesting, as described in [specs/hierarchical-nesting.md](specs/hierarchical-nesting.md) and [POST_2040_OUTLOOK.md §3](../POST_2040_OUTLOOK.md#3-hierarchical-nesting). Record that nesting is the default, and a count or description of outer envelopes and sub-lattices. | TBD, no pass bar set |
| P4-T3 | Split-merge as default organization | Under that same default organization, perform a split and a merge as described in [specs/split-merge.md](specs/split-merge.md) and [POST_2040_OUTLOOK.md §5](../POST_2040_OUTLOOK.md#5-split--merge-swarm-scaling). Record the cut / join, and whether each subgroup (and the merged lattice) remains a working organization. | TBD, no pass bar set |
| P4-T4 | Marble Mode at scale | If the Phase 1 (P1-M1…P1-M4) and Phase 2 (P2-T9) Marble results hold, demonstrate Marble Mode working at the Phase 4 lattice scale: pack and latch, then re-expand, and record whether re-expanded faces can still attempt a dock. If those earlier results do not hold, or if P2-T9 was deferred and was not later completed, record that and do not treat scale Marble as demonstrated. This is expected-if, not already solved. See [specs/marble-mode.md](specs/marble-mode.md). | TBD, no pass bar set |
| P4-T5 | Companion as household product | Take the Phase 3 companion prototype line to a household-product configuration, against [COMPANION_TOOL_MODES.md](COMPANION_TOOL_MODES.md#companion-modes). Record the configuration, the household setting, and the companion-gate / measurement-card notes. This is not a companion certification until those gates are met. | TBD, no pass bar set |
| P4-T6 | 1 cm target and 25 mm lock recorded | Confirm in the Phase 4 results that 1 cm remains a target (not locked or validated) and that the 25 mm cell stays locked for Phases 0–3. Record that this phase does not mint a V2.0 product by existing. | TBD, no pass bar set |

---

## Phase 5+

Phase 5+ is not defined yet.

---

Paper until measured. Credit follows data.
