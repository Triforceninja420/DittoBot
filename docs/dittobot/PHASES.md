# DittoBot phases

Design owner: Craig.
Date: 2026-11-27.
Status: **proposed / paper only**. Credit follows measured data.

This file indexes the numbered phases and defines Phase 2. It does not change Phase 0 locks, Phase 1 docking criteria (P1-T1…T14), the locked 25 mm cell core, any existing spec status, or [PHASE1.md](../PHASE1.md). Every value below is **proposed** unless it is quoted from an existing locked source. **TBD** means a number must be chosen or measured before Phase 2 test start. No pass bars are invented here.

Paper until measured. Credit follows data.

---

## Index

- **Phase 0** — one 20 mm docking face. See [PHASE0.md](../PHASE0.md). Test plan `DB-P0-FACE-TP-001`.
- **Phase 1** — two-module docking on the unchanged Phase 0 face protocol, plus scheduled Marble Mode joint work. See [PHASE1.md](../PHASE1.md). Test plan `DB-P1-DOCK-TP-001` (P1-T1…T14).
- **Phase 2** — four-module lattice demos, defined below.
- **Phase 3+** — not defined yet.

---

## Inheritance (all numbered phases)

The locked 25 mm cell core is unchanged ([DESIGN.md](../DESIGN.md), [PAPER_STATUS.md](../PAPER_STATUS.md)):

- 25 mm cube envelope
- Centered Ø8.2 × 4.0 mm pocket (locked)
- Nd disc Ø6.0 × 2–3 mm hold; coil around the disc, release-only (Alnico off this cell)
- DRV8871, 12 V, pulse-only
- Axial pin hard-lock; full cavity potting and face coatings

Phase 2 uses the unchanged Phase 0 face protocol. It does not retune that core, rewrite Phase 0 or Phase 1 gates, or mix the two stacks except as already allowed in `HARDWARE_MAPPING.md`.

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

## Phase 3+

Phase 3 and later numbered phases are **not defined yet**. Nothing in this file implies a Phase 3 scope, schedule, or test plan.

---

Paper until measured. Credit follows data.
