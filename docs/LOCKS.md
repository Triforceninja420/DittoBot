# DittoBot paper locks — updated 2026-11-23

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

This file stamps process. It does **not** change Phase 0 geometry, winding SOP, drivers, or success tests. It does **not** enlarge the 25 mm pocket. It does **not** create V2.0. It does **not** certify a companion robot.

Two stacks stay unmixed.

| Stack | What it is | Where |
| :---- | :---------- | :---- |
| Phase 0 | 20 mm sliding-pin face, Option A release, cams deferred 2026-11-23b (size committed 2026-11-23; CAD redesign landed 2026-11-23) | `docs/PHASE0.md`, public spec, Phase0 package |
| 25 mm cell | Public GitHub coupon, 2026-11-19 baseline | `README.md`, `docs/BASELINE_UPGRADES.md`, `docs/BUILD.md`, `cad/voxel_cell.scad` |

Do not paste 25 mm coil / driver / magnet / hold numbers into Phase 0. Do not paste Phase 0 numbers into the 25 mm files.

Phase 0 tests the 20 mm face. The 25 mm cube is the cell body spec. They are not the same article.

**Exception (Craig's brief, 2026-11-23):** `docs/HARDWARE_MAPPING.md` is allowed to map Phase 0 sim parameters and gates onto the 25 mm cell hardware. That file is the only exception; every other file keeps the two stacks unmixed.

**Current 25 mm baseline (2026-11-19, magnet updated 2026-11-23):** Nd disc Ø6.0 mm × 2–3 mm hold in the Ø8.2 × 4.0 pocket (coil around the disc, release-only, sized for I_release; Alnico off this cell), axial pin hard-lock, full cavity potting, PTFE lip + coatings, pulse-only drive with thermal governor, 36 V nominal pulse bank into DRV8871 (stay under 45 V abs). Pocket locked Ø8.2 × 4.0 mm.

**Current Phase 0 baseline (2026-11-21, face size + CAD updated 2026-11-23, release architecture updated 2026-11-23b):** 20 mm face, NdFeB N52 Ø6.0 × 2–3 mm Nd disc in Ø8.2 × 4.0 pocket (coil release-only, Alnico off), 40-turn coil via DRV8871, Option A sliding-pin release (magnet-pull retention ≥ 1.8 N, single Ø2.0 mm sliding pin, no cams on face), 3-pin latch (7075-T6), 4× non-magnetic springs 5.00 N total. Simulated 98.04% all-pass. Shear bar 40 N. Snap 34.6 N. Thermal < 1.5 K. Mass 9.2 g. Cams and the +65.7 N cam-release figures are retired — see `docs/GATE5_SUPERSEDED.md`.

Earlier 20 mm 4×EPM face and the Ø6 mm Nd/Alnico flip-stack 25 mm descriptions are superseded. The Ø6.0 × 2–3 mm Nd disc alone (no Alnico) is the current 25 mm hold magnet (2026-11-23). Dual-cam Phase 0 face retired 2026-11-23b.

---

## Count

**18 paper locks.** 9 already-frozen hardware / stack rules + 9 companion *gates*.

---

## Already frozen (9) — do not reopen

1. **Phase 0 test 1** — Snap 34.6 N axial at 0.5 mm gap on mild steel; off-axis and 60 °C still holds.
2. **Phase 0 test 2** — Soft-dock ≥ 90 % capture at ≤ 2.5 mm lateral, insertion ≤ 5 N.
3. **Phase 0 test 3** — Hard-lock ≥ 95 % with all three pins seated.
4. **Phase 0 test 4** — Shear ≥ 40 N through pins without plate yield. Simulated 5 028 N (earlier 2-pin build).
5. **Phase 0 test 5** — Release: magnet-pull retention ≥ 1.8 N via Option A sliding pin; cams deferred to Option A / 25 mm cell (rev 2026-11-23b).
6. **Phase 0 test 6** — 1.25 A through the contact bus ≥ 10 min. Log plate temp. 41 °C skin cap.
7. **Phase 0 test 7** — 2 000 dock / undock cycles on pins + sliding pin + contacts.
8. **Two stacks unmixed.** Phase 0 (20 mm, Nd disc Ø6.0×2–3, DRV8871 pulse, 3-pin, Option A sliding pin) is not the 25 mm cell (Nd disc Ø6.0 × 2–3 hold, DRV8871 pulse, axial pin, potting). Do not mix numbers. Exception: `docs/HARDWARE_MAPPING.md` (Craig's brief, 2026-11-23).
9. **Drive discipline.** Hold current after switch is **zero**. Pulse-duty only. Coil sized for release, not hold. Thermal governor required on the 25 mm cell. Pulse bank voltage stays under the driver absolute maximum.

Phase 0 drive is a 40-turn 34 AWG coil (~0.75 Ω cold) pulsed by a DRV8871, as in `docs/PHASE0.md`. The earlier capacitor-dump / IRLZ44N class, 220 µF charged 30–36 V drive was superseded (documented in `phase0/retired/`; already absent from `docs/PHASE0.md` when that file first landed in this repo, `7d0fd8f`, 2026-11-27). A 2026-11-23 handoff in `retired/CHANGES.md` already recorded that this LOCKS note should be replaced with DRV8871.

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
9. **20 mm face is committed** (Craig, 2026-11-23; replaces "30 mm face is committed"). CAD redesign landed in `cad/voxel_cell_phase0_20mm.scad`. Do not change face size again without a new lock.

---

## Explicitly not locked

- V2.0 as a product
- Node count for a swarm or suit
- Measured hold on either stack (credit follows data)
- Enlarging the 25 mm Ø8.2 pocket
- Mixing files or stacks
- Sliding-pin wear model (deferred; cam-era Hertz/wear figures archived in GATE5_SUPERSEDED)
- Polymer tip chemistry (POM validated; alternatives OK if margin holds) — retained for Option A / 25 mm cell context

---

## What to do next

- 25 mm: wind parallel AWG 36, count turns, pulse from the 36 V bank through DRV8871, pull ON/OFF, confirm pin seats, write `docs/MEASUREMENT_CARD.md`.
- Phase 0: machine the 20 mm plate (CAD in `cad/voxel_cell_phase0_20mm.scad`), press NdFeB magnet, wind coil, seat 3 pins + Option A Ø2.0 mm sliding release pin + 4-spring 5.00 N seating, pulse, pull snap, verify ≥ 1.8 N retention, soak 1.25 A / 10 min, run 2 000 cycles.

Paper hold claims do not move either baseline. Simulation numbers are the bar, not the credit.
