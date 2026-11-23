# DittoBot paper locks — updated 2026-11-21

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

This file stamps process. It does **not** change Phase 0 geometry, winding SOP, drivers, cams, or success tests. It does **not** enlarge the 25 mm pocket. It does **not** create V2.0. It does **not** certify a companion robot.

Two stacks stay unmixed.

| Stack | What it is | Where |
| :---- | :---------- | :---- |
| Phase 0 | 20 mm dual-cam face (size committed 2026-11-23; CAD still 30 × 30, rev 2026-11-21) | `docs/PHASE0.md`, public spec, Phase0 package |
| 25 mm cell | Public GitHub coupon, 2026-11-19 baseline | `README.md`, `docs/BASELINE_UPGRADES.md`, `docs/BUILD.md`, `cad/voxel_cell.scad` |

Do not paste 25 mm coil / driver / magnet / hold numbers into Phase 0. Do not paste Phase 0 numbers into the 25 mm files.

**Exception (Craig's brief, 2026-11-23):** `docs/HARDWARE_MAPPING.md` is allowed to map Phase 0 sim parameters and gates onto the 25 mm cell hardware. That file is the only exception; every other file keeps the two stacks unmixed.

**Current 25 mm baseline (2026-11-19, magnet updated 2026-11-23):** Nd disc Ø6.0 mm × 2–3 mm hold in the Ø8.2 × 4.0 pocket (coil around the disc, release-only, sized for I_release; Alnico off this cell), axial pin hard-lock, full cavity potting, PTFE lip + coatings, pulse-only drive with thermal governor, 36 V nominal pulse bank into DRV8871 (stay under 45 V abs). Pocket locked Ø8.2 × 4.0 mm.

**Current Phase 0 baseline (2026-11-21, face size updated 2026-11-23):** 20 mm face (was 30 mm; CAD re-dimension pending), NdFeB N52 Ø6 × 6 mm magnet, 40-turn 34 AWG coil (~0.75 Ω), dual staggered 8 mm cams with steel-backed polymer tips, 2-pin latch + retraction actuator, 5 N seating spring. Simulated 26/26 pass. Shear 5 028 N. Snap 34.6 N. Release net +65.7 N. Thermal < 1.5 K. Mass 9.2 g.

Earlier 20 mm 4×EPM face and the Ø6 mm Nd/Alnico flip-stack 25 mm descriptions are superseded. The Ø6.0 × 2–3 mm Nd disc alone (no Alnico) is the current 25 mm hold magnet (2026-11-23).

---

## Count

**18 paper locks.** 9 already-frozen hardware / stack rules + 9 companion *gates*.

---

## Already frozen (9) — do not reopen

1. **Phase 0 test 1** — Snap 34.6 N axial at 0.5 mm gap on mild steel; off-axis and 60 °C still holds.
2. **Phase 0 test 2** — Soft-dock ≥ 90 % capture at ≤ 2.5 mm lateral, insertion ≤ 5 N.
3. **Phase 0 test 3** — Hard-lock ≥ 95 % with both pins seated.
4. **Phase 0 test 4** — Shear ≥ 40 N through pins without plate yield. Simulated 5 028 N.
5. **Phase 0 test 5** — Release net +65.7 N via dual-cam + retraction actuator sequence.
6. **Phase 0 test 6** — 1.25 A through the contact bus ≥ 10 min. Log plate temp. 41 °C skin cap.
7. **Phase 0 test 7** — 2 000 dock / undock cycles on pins + cams + contacts. Cam tip wear 0.19 µm simulated.
8. **Two stacks unmixed.** Phase 0 (20 mm dual-cam, NdFeB Ø6×6, IRLZ44N cap-dump) is not the 25 mm cell (Nd disc Ø6.0 × 2–3 hold, DRV8871 pulse, axial pin, potting). Do not mix numbers. Exception: `docs/HARDWARE_MAPPING.md` (Craig's brief, 2026-11-23).
9. **Drive discipline.** Hold current after switch is **zero**. Pulse-duty only. Coil sized for release, not hold. Thermal governor required on the 25 mm cell. Pulse bank voltage stays under the driver absolute maximum.

Phase 0 drive remains capacitor dump, IRLZ44N class, 220 µF charged 30–36 V, 34 AWG, 40 turns. Those numbers live only in `docs/PHASE0.md`.

---

## Companion gates (9) — no CAD change

These do not relax any number above.

1. **No companion claim** until a filled `docs/MEASUREMENT_CARD.md` exists.
2. **35 N is the human-contact interrupt.** **40 N is docked structural shear.** They are not the same.
3. **41 °C skin** is the paper contact-temperature cap.
4. **Soft safety skin is mandatory** on any human-proximate build.
5. **Skills, mesh, community hooks cannot override** the 35 N interrupt or coil-fire interlock.
6. **Pulse bank and face bus stay fixture-side** until contacts are covered or isolated.
7. **One coil at a time** until headroom is measured.
8. **Community Enhancement Suites stay optional and zero-impact.**
9. **20 mm face is committed** (Craig, 2026-11-23; replaces "30 mm face is committed"). Matches the sim's 20 mm face article. The dual-cam layout must be re-fitted to 20 mm; `cad/voxel_cell_phase0_30mm_dualcam.scad` still dimensions 30 × 30 until then. Do not change face size again without a new lock.

---

## Explicitly not locked

- V2.0 as a product
- Node count for a swarm or suit
- Measured hold on either stack (credit follows data)
- Enlarging the 25 mm Ø8.2 pocket
- Mixing files or stacks
- Exact cam material (stainless vs hardened+oxide — both acceptable)
- Polymer tip chemistry (POM validated; alternatives OK if margin holds)

---

## What to do next

- 25 mm: wind parallel AWG 36, count turns, pulse from the 36 V bank through DRV8871, pull ON/OFF, confirm pin seats, write `docs/MEASUREMENT_CARD.md`.
- Phase 0: re-dimension the CAD to 20 mm, machine the 20 mm plate, press NdFeB magnet, wind 40-turn coil, machine dual cams with steel-backed polymer tips, seat pins + retraction actuator + 5 N spring, pulse, pull snap, verify release net, soak 1.25 A / 10 min, run 2 000 cycles.

Paper hold claims do not move either baseline. Simulation numbers are the bar, not the credit.
