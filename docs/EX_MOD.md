# EX-MOD — Extinguisher Module

Design owner: Craig.  
Date: 2026-11-27.  
Status: **paper only**. Depends on the locked Phase 0 20 mm face article and a populated measurement card. Does not change baseline geometry, Phase 0 locks, or existing measurement cards.

Drop-in suppressant module that mates to any Structural or Energy node via the existing Phase 0 docking face. Provides short-duration fire suppression without new latch mechanics.

## Form factor & interface
- Envelope: 4–8 cm³ node class (compatible with current baseline).
- Docking face: identical to the locked Phase 0 20 mm article (DB-P0-FACE-TP-001).
- Hold: Ø6.0 × 2–3 mm Nd disc, coil release-only (same as 25 mm cell and Phase 0).
- Mass budget (paper): ≤ 45 g total so docked shear stays inside the Phase 0 40 N target.

## Payload
- Primary: single-use or refillable cartridge (paper options: 15–20 ml water-mist bladder, stacked dry-chemical pellets, or micro CO₂ cartridge).
- Discharge: 8–15 s continuous or pulsed.
- Nozzle: fixed orifice aimed outward from the free face. No new actuators beyond the existing release coil path.

## Electrical / pinout (measurement-card side)
- Driver: existing DRV8871 for release coil and optional burst solenoid.
- Sense: 2 spare pins on the measurement card for optional heat/smoke stub (can be left open).
- Power: drawn from Energy module bus. Peak ≤ 1.25 A × 10 min (already inside Phase 0 T4).

## Activation & control
- Compute node asserts a digital line → solenoid or burst disk opens.
- Optional local timer for auto-cutoff.
- No new firmware required beyond a one-line mode flag on the existing pulse path.

## Lattice behavior
- Single EX-MOD sprays in one direction.
- Two or more can dock into a short chain and sequence pulses so the swarm walks a suppressant path.
- After discharge the empty module remains a structural node.

## Failure modes (paper)
- Cartridge leak → mass increase; still inside shear if ≤ 10 g extra.
- Nozzle clog → pressure rise contained by bladder burst disk.
- False trigger → wasted charge; no structural damage.

## Dependencies
- Phase 0 face article built and T1–T5 numbers recorded.
- Measurement card populated with at least the two sense pins.

Paper until measured. Credit follows data. See PHASE0.md, MEASUREMENT_CARD.md, and MODES.md.
