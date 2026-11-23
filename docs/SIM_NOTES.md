# DittoBot simulation notes

Design owned by Craig. Started Nov/Dec 2025.

This file records that private thermal and shear analysis (not a public executable full docking/shear sim) informed the 2026-11-06 revisions. It does **not** change any locked Phase 0 measured gates.

## What is public and locked

Phase 0 success criteria remain the measured ones in [PHASE0.md](PHASE0.md) (rev 2026-11-21, 20 mm dual-cam; face size committed 2026-11-23):

- Snap 34.6 N axial at 0.5 mm gap (sim bar)
- Soft-dock ≥ 90 % at ≤ 2.5 mm lateral, insertion ≤ 5 N
- Hard-lock ≥ 95 % with all three pins seated
- Shear ≥ 40 N through pins (simulated 5 028 N)
- Release net +65.7 N via dual-cam + retraction actuator
- 1.25 A continuous ≥ 10 min (log temperature, 41 °C skin cap)
- 2 000 dock/undock cycles (cam tip wear 0.19 µm simulated)

Anyone can verify these on the public fixture package and `cad/voxel_cell_phase0_30mm_dualcam.scad` (pending 20 mm redesign — see PHASE0.md face-size note).

## Private analysis that drove 2026-11-06 fixes

A private simulation battery (not present as a full runnable docking/shear model in this public repo) flagged two issues against the then-locked targets:

1. **Thermal (T4)**: Single-strand coil under 1.25 A × 10 min continuous duty reached ~444 °C, far above insulation limits. Fix documented in [COIL_REVISION.md](COIL_REVISION.md): wind 2–4× AWG 36 strands in parallel (or thicker wire) for any continuous-duty use. Pulse-only duty on the Phase 0 face is unaffected.

2. **Latch wear (T5)**: Face wear estimated at ~1 mm over 2 000 cycles against a 100 µm budget. Fix: replaceable carbide (or 440C) shear shim, Ø6.0 × 0.50 mm, clip-in, swap at ~100 µm. Documented in [PHASE0.md](PHASE0.md) Rev 2026-11-06. Superseded 2026-11-21 by dual-cam + pin latch (simulated wear 0.19 µm).

These fixes are design responses. They do not replace measured data. The public path remains: build the fixture, wind to the SOP, measure ON/OFF force, current, temperature, and cycles, then fill the measurement card.

## Public estimate script

[tools/phase0_estimate.py](../tools/phase0_estimate.py) is a simple, transparent Python estimate (Maxwell-style force paper + basic I²R thermal), updated 2026-11-21 to the current Ø6 mm NdFeB numbers. It is labeled as an estimate only. It does not replace the locked measured gates and is not a full docking or multi-physics shear simulation.

No full public docking/shear sim exists in this repository. Builders should treat the locked measured criteria and the fixture package as the source of truth.

Credit follows measured data.
