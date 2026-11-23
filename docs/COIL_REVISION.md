# 25 mm cell — coil / driver revision
2026-09-09
Updated 2026-11-06: parallel-strand thermal fix.
Updated 2026-11-19: Current baseline is SmCo 2:17 Ø7.5 mm residual hold (coil release only). Earlier Ø6 mm stacks superseded.
Updated 2026-11-21: Stale 20 mm hybrid-face cross-reference removed. Phase 0 is the 20 mm dual-cam face — see docs/PHASE0.md.
Updated 2026-11-23 (Craig): hold magnet is a Ø6.0 × 2–3 mm Nd disc in the locked Ø8.2 × 4.0 mm pocket. Coil wound around the disc, release-only, sized for I_release (not hold). Alnico is off this cell. Replaces the SmCo 2:17 Ø7.5 × 3.0 mm baseline of 2026-11-19.

Project started Nov/Dec 2025. Design owned by Craig. Programmable matter.

This file applies **only** to the public 25 mm cubic cell in this repository.
It does not change the locked Phase 0 20 mm face.

## What was wrong (historical)

First pass used 120 turns AWG 34, DRV8837C, and claimed numbers that the pulse could not support. Those are retired. See earlier commits for the full analysis.

## Current geometry lock (2026-11-19 baseline, magnet updated 2026-11-23)

Pocket remains locked:

* Pocket: **Ø8.2 mm × 4.0 mm** (`cad/voxel_cell.scad` — do not enlarge)
* Magnet: **Nd disc Ø6.0 mm × 2–3 mm** hold
* Annulus: (8.2 − 6.0) / 2 = **1.10 mm per side** — winding window for the release coil; the bobbin must center the disc
* Axial pin receptacle added in CAD (engages after magnetic soft-dock)

Alnico is off this cell (no Nd+Alnico flip stack). The SmCo 2:17 Ø7.5 × 3.0 mm stack of 2026-11-19 is replaced by the Nd disc.

## Coil and drive (current baseline)

* Wire: **2–4× AWG 36 in parallel** (or single thicker equivalent). Pulse-only default.
* Turns: wind what fits the reduced annulus; count and publish the actual number.
* Driver: **DRV8871**, VM from pulse bank **36 V nominal** (stay ≤ 42 V; absolute max 45 V). ILIM ~3.0 A.
* Pulse bank: polypropylene film capacitors, 100 V rating preferred, potted.
* Logic: 3.3 V XIAO RP2040. Never put coil voltage on the MCU.
* Hold current after pulse = 0. The Nd disc provides zero-power hold.
* Coil is release-only and sized for I_release, not hold. See `docs/HARDWARE_MAPPING.md` §4b for the I_release method against DRV8871 ILIM.
* Firmware thermal governor required (see `firmware/pulse_driver.cpp`).

Parallel strands remain preferred for any pulse train so that a single fine wire does not overheat.

## Thermal and wear notes (retained)

Single-strand continuous duty was flagged hot in earlier analysis. Pulse-only + parallel strands + thermal governor address it. Replaceable carbide shear shim remains a wear item on the latch face.

## What to measure before claiming a latch

1. Turns actually wound.
2. Cold R (total parallel).
3. Peak current and pulse width on the real bank.
4. ON force (coil off) and OFF force (after release pulse) at the intended gap.
5. Pin engagement confirmation.
6. Plate / coil temperature after a representative pulse train.
7. Potting and coating integrity.

Paper estimates do not move the baseline. Fill `docs/MEASUREMENT_CARD.md`.

## What this file does not do

* Does not unfreeze Phase 0 (20 mm face, rev 2026-11-23).
* Does not change the locked Ø8.2 × 4.0 mm pocket.
* Does not mint V2.0 or a companion.
