# DittoBot paper locks — updated 2026-11-19

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

This file stamps process. It does **not** change Phase 0 geometry, winding SOP, drivers, or success tests. It does **not** enlarge the 25 mm pocket. It does **not** create V2.0. It does **not** certify a companion robot.

Two stacks stay unmixed.

| Stack | What it is | Where |
| :--- | :--- |
| Phase 0 | Frozen 20 mm hybrid face | `docs/PHASE0.md`, public spec, Phase0 package |
| 25 mm cell | Public GitHub coupon, 2026-11-19 baseline | `README.md`, `docs/BASELINE_UPGRADES.md`, `docs/BUILD.md`, `cad/voxel_cell.scad` |

Do not paste 25 mm coil / driver / magnet / hold numbers into Phase 0. Do not paste Phase 0 numbers into the 25 mm files.

**Current 25 mm baseline (2026-11-19):** SmCo 2:17 Ø7.5 mm × 3.0 mm residual hold, axial pin hard-lock, full cavity potting, PTFE lip + coatings, pulse-only drive with thermal governor, 36 V nominal pulse bank into DRV8871 (stay under 45 V abs). Pocket locked Ø8.2 × 4.0 mm.

Earlier Ø6 mm Nd / Alnico descriptions are superseded for the 25 mm cell.

---

## Count

**16 paper locks.** 8 already-frozen hardware / stack rules + 8 companion *gates*.

---

## Already frozen (8) — do not reopen

1. **Phase 0 test 1** — EPM ON ≥ 3.0 N at zero gap on mild steel; OFF residual < 0.3 N; four coils.
2. **Phase 0 test 2** — Soft-dock ≥ 90 % capture at ≤ 2.5 mm lateral.
3. **Phase 0 test 3** — Hard-lock ≥ 95 % with pin seated.
4. **Phase 0 test 4** — Shear ≥ 40 N through pin + receptacle without plate yield.
5. **Phase 0 test 5** — 1.25 A through the contact bus ≥ 10 min. Log plate temp.
6. **Phase 0 test 6** — 2 000 dock / undock cycles on pin + contacts.
7. **Two stacks unmixed.** Phase 0 (4× Ø5 EPM, 1.8 mm pin, 6 contacts, IRLZ44N cap-dump) is not the 25 mm cell (SmCo Ø7.5 residual, DRV8871 pulse, axial pin, potting). Do not mix numbers.
8. **Drive discipline.** Hold current after switch is **zero**. Pulse width set from measured peak current. Thermal governor required on the 25 mm cell. Pulse bank voltage stays under the driver absolute maximum.

Phase 0 drive remains capacitor dump, IRLZ44N class, 220 µF charged 30–36 V, 34/32 AWG, 160–200 turns. Those numbers live only in `docs/PHASE0.md`.

---

## Companion gates (8) — no CAD change

These do not relax any number above.

1. **No companion claim** until a filled `docs/MEASUREMENT_CARD.md` exists.
2. **35 N is the human-contact interrupt.** **40 N is docked structural shear.** They are not the same.
3. **41 °C skin** is the paper contact-temperature cap.
4. **Soft safety skin is mandatory** on any human-proximate build.
5. **Skills, mesh, community hooks cannot override** the 35 N interrupt or coil-fire interlock.
6. **Pulse bank and face bus stay fixture-side** until contacts are covered or isolated.
7. **One coil at a time** until headroom is measured.
8. **Community Enhancement Suites stay optional and zero-impact.**

---

## Explicitly not locked

- V2.0 as a product
- Node count for a swarm or suit
- Measured hold on either stack (credit follows data)
- Enlarging the 25 mm Ø8.2 pocket
- Mixing files or stacks

---

## What to do next

- 25 mm: wind parallel AWG 36, count turns, pulse from the 36 V bank through DRV8871, pull ON/OFF, confirm pin seats, write `docs/MEASUREMENT_CARD.md`.
- Phase 0: machine the 20 mm plate, wind four EPMs to the SOP, pulse, pull ≥ 3 N, soak 1.25 A / 10 min.

Paper hold claims do not move either baseline.
