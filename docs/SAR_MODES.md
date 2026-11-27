# SAR Mode Package

Design owner: Craig.  
Date: 2026-11-27.  
Status: **paper / software + sensor-stub only**. Runs on existing compute nodes once the Phase 0 face can reliably dock and the measurement card can report. Does not change baseline geometry or Phase 0 locks.

Operational modes (Search, Rescue, Signal) for search-and-rescue use. All inherit the locked Phase 0 face and current structural cells.

## Search mode
- Optional sensor stubs (thermal, CO₂, audio) plug into spare measurement-card pins.
- Swarm runs a simple gradient climb or grid sweep.
- No new actuators.

## Rescue mode
- Uses Structural modules only.
- Forms rigid lattice bridges, ramps, or cradles.
- Force limits = measured Phase 0 shear (40 N target). Documented as “do not exceed measured T3 value.”

## Signal mode
- Compute node flashes LED or emits tone through existing pins.
- Used for location marking or victim signaling.

## Pseudocode (high-level, paper)
```
if mode == SEARCH:
  read_sensor_stub()
  move_toward_gradient()
elif mode == RESCUE:
  form_lattice(target_shape)
  hold_until_measured_shear_ok()
elif mode == SIGNAL:
  pulse_output(pattern)
```

## Failure modes
- Sensor stub missing → mode falls back to pure structural.
- Dock failure → swarm reports the existing Phase 0 error codes.

## Dependencies
- Phase 0 face article exists and has passed T1–T5.
- Measurement card has at least the spare sense pins populated.

Beacon Mode (swarm convergence on a fixed ping) is sketched separately in [dittobot/MODES.md](dittobot/MODES.md). It is conceptual and is not a SAR certification.

Paper until measured. Credit follows data. See PHASE0.md, MEASUREMENT_CARD.md, and MODES.md.
