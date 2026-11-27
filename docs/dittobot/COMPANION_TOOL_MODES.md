# Companion, Tool, and Specialty Modes

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **conceptual** for every mode in this file. No phase is assigned. No pass bars are set.

Do not confuse this file with:

- [MODES.md](MODES.md) — Marble, Repair, and Beacon feature modes
- [../MODES.md](../MODES.md) — wearable / application inheritance (flight suit, exo, armored shell, companion clothing, vehicle, habitat)
- [specs/README.md](specs/README.md) — per-mode paper specs for those existing tracks

This is a conceptual catalog of companion, tool, and specialty modes. Each entry is one or two sentences. It does not replace the paper specs above, and it does not retune the cell.

---

## Honesty

These are conceptual roadmap entries. Capabilities are modeled / aspirational, not measured. Payload hardware is TBD. Nothing in this file changes the locked 25 mm cell core, Phase 0 locks, measurement cards, or any sim number.

Paper until measured. Credit follows data.

## Locked core (unchanged)

All modes inherit the locked 25 mm cell core, unchanged ([DESIGN.md](../DESIGN.md), [PAPER_STATUS.md](../PAPER_STATUS.md)):

- 25 mm cube envelope
- Centered Ø8.2 × 4.0 mm pocket (locked)
- Nd disc Ø6.0 × 2–3 mm hold; coil around the disc, release-only
- DRV8871, 12 V, pulse-only

Mode-specific layers and swap-in payloads sit on top. The cell is not retuned. Tool modes each swap the payload on the same cell core.

## Caveats

- **Medical modes** are not a medical device. They would need regulatory clearance. They are not for real clinical use.
- **Welding torch, drill, and jack / lift** involve load and heat beyond the cell's tested envelope. The cell is a payload carrier only.
- **Pet, partner, and emotional support** modes have no sensing validated.

---

## Companion modes

Behavioral modes on the same locked cell core. The wearable soft-companion lattice is already a paper spec; this section does not redefine it.

### Soft companion clothing

Hugs without squeezing. Uses the sparse, low-force clothing lattice already written in [Soft Companion / Clothing Mode](../MODES.md#3-soft-companion--clothing-mode) and [specs/soft-companion.md](specs/soft-companion.md); this entry is the gentle-contact behavior, not a new cell.

### Emotional support mode

Reads posture and adjusts warmth. No sensing is validated; this stays conceptual.

### Wake-up mode

Morning greeting with a light pulse. Conceptual only; no alarm hardware is specified.

### Sleep mode

Dims to near-nothing, and stirs only on movement. Conceptual only.

### Massage mode

Rhythmic pressure along the back. Contact force and rhythm are TBD; the existing human-contact interrupt and soft safety skin still apply. No pass bar is set.

### Boredom mode

Sits there being company without demanding anything.

### Pet mode

Follows you around the house, learns routes, and comes when called. No sensing is validated; this stays conceptual.

### Partner mode

Not a toy, not a tool, just something that's there. No sensing is validated; this stays conceptual.

---

## Tool modes

Each swaps the payload on the same locked cell core. Extinguisher and barrier already have their own docs; those are linked, not rewritten.

### Extinguisher (EX-MOD)

Already specified in [EX_MOD.md](../EX_MOD.md). Drop-in suppressant payload on the same cell core and Phase 0 face. This file does not redefine it.

### Barrier (BAR-MOD)

Already specified in [BAR_MOD.md](../BAR_MOD.md). Deployable panel payload on the same cell core and Phase 0 face. This file does not redefine it.

### Welding torch

A welding-torch payload on the same cell core. Load and heat are beyond the cell's tested envelope, so the cell is a payload carrier only.

### Drill

A drill payload on the same cell core. Load and heat are beyond the cell's tested envelope, so the cell is a payload carrier only.

### Gripper arm

A gripper-arm payload for manipulation, swapped onto the same cell core. Reach, grip force, and duty cycle are TBD.

### First-aid kit

A first-aid payload with tourniquet and bandage dispensers, swapped onto the same cell core. This is a dispenser, not a care claim, and it is not a medical device.

### Vacuum

A vacuum payload for dust and debris, swapped onto the same cell core. Suction and filter hardware are TBD.

### Jack / lift

A jack or lift payload for heavy objects, swapped onto the same cell core. Load is beyond the cell's tested envelope, so the cell is a payload carrier only.

---

## Medical modes

Not a medical device. These would need regulatory clearance. They are not for real clinical use. Payload hardware is TBD.

### Triage scanner

Reads vitals through contact. Sensing is not validated, and this is not for real clinical use.

### Drug delivery

Measured dosing through a swap-in payload. No dose, rate, or drug is specified here. Not a medical device, and not for real clinical use.

### Wound-closure

Wound-closure with suture thread, carried as a payload on the same cell core. Not a medical device, and not for real clinical use.

---

## Agricultural modes

### Soil sampler

A soil-sampler payload on the same cell core. Sample volume, depth, and assay method are TBD.

### Seed planter

A seed-planter payload on the same cell core. Spacing, depth, and seed handling are TBD.

### Pollinator mimic

A pollinator-mimic payload for greenhouse use, swapped onto the same cell core. Effectiveness is not measured.

---

## Construction modes

### Brick layer

Places bricks as a construction payload on the same cell core. Placement accuracy and load are TBD.

### Mortar mixer

A mortar-mixer payload on the same cell core. Mix ratio, volume, and duty cycle are TBD.

### Concrete vibrator

A concrete-vibrator payload on the same cell core. Vibration and duty cycle are TBD; load and heat limits are untested for this use.

---

## Entertainment modes

### Projector

A projector payload that unfolds into a screen, swapped onto the same cell core. Optical performance and screen size are TBD.

### Speaker array

A speaker-array payload on the same cell core. Acoustic performance is TBD.

### DJ deck

A DJ-deck payload with lights, swapped onto the same cell core. Control surface and lighting hardware are TBD.

---

## Security modes

### Perimeter patrol

Maps a property and flags movement. Sensing and mapping are not validated; this stays conceptual. Not a security certification.

### Door barricade

A lock-pick-resistant door barricade formed on the same cell core. Resistance is not measured, and no rating is claimed. Related to, but not the same as, [BAR_MOD.md](../BAR_MOD.md).

---

## Scientific modes

### Mars dust sample collector

A sample-collector payload for Mars dust, swapped onto the same cell core. Collection, sealing, and planetary-protection behavior are TBD. This does not change any Mars sim number.

### Spectrometer mount

A mount for a spectrometer payload on the same cell core. The instrument itself is TBD; this entry is the mount, not a spectrometer design.

### Camera rig

A camera rig for documenting everything, carried as a payload on the same cell core. Sensors, storage, and coverage are TBD.

---

## Wildcard

### Self-destruct mode

The swarm disassembles itself back into raw cells for recycling. This is non-explosive, controlled disassembly — not a bang, not a wipe, just taking the lattice apart on purpose and stopping at reusable cells. Most honest mode, since nothing should last forever.

This is not [Repair Mode](MODES.md#2-repair-mode). Repair cannibalizes broken parts to rebuild. Self-destruct takes the swarm apart and leaves the cells as raw stock.

---

## What this does not change

- Locked 25 mm cell core: 25 mm envelope, Ø8.2 × 4.0 mm pocket, Nd disc Ø6.0 × 2–3 mm hold, coil release-only, DRV8871 pulse-only
- Phase 0 locks, measurement cards, or existing Phase 1 docking criteria
- Mars sim numbers or honesty notes
- The existing content of [EX_MOD.md](../EX_MOD.md), [BAR_MOD.md](../BAR_MOD.md), [../MODES.md](../MODES.md), [MODES.md](MODES.md), or the paper specs under [specs/](specs/README.md)

Paper until measured. Credit follows data.
