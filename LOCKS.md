# DittoBot paper locks — 2026-09-14

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

This file stamps process. It does **not** change Phase 0 geometry, winding SOP, drivers, or success tests. It does **not** change 25 mm option A geometry. It does **not** create V2.0. It does **not** certify a companion robot.

Two stacks stay unmixed.

| Stack | What it is | Where |
| :--- | :--- | :--- |
| Phase 0 | Frozen 20 mm hybrid face | `PHASE0.md`, public spec `.docx`, `Phase0_Independent_Fab_Package/` |
| 25 mm cell | Public GitHub coupon, option A | `README.md`, `COIL_REVISION.md`, `MEASUREMENT_CARD.md`, `MIN_PARTS.md`, `openscad` |

Do not paste 25 mm coil / driver / magnet / hold numbers into Phase 0. Do not paste Phase 0 ON / OFF / shear / cap-dump numbers into the 25 mm files. **28.8 N is retired** on the 25 mm cell.

---

## Count

**16 paper locks.** 8 already-frozen hardware / stack rules + 8 companion *gates*.

A companion claim, a node count, a suit, ISO 10218 as a cert, child / pet use, pinch maps, and V2.0 are **not** in this count.

---

## Already frozen (8) — do not reopen

1. **Phase 0 test 1** — EPM ON ≥ 3.0 N at zero gap on mild steel; OFF residual < 0.3 N; four coils.
2. **Phase 0 test 2** — Soft-dock ≥ 90 % capture at ≤ 2.5 mm lateral.
3. **Phase 0 test 3** — Hard-lock ≥ 95 % with pin seated.
4. **Phase 0 test 4** — Shear ≥ 40 N through pin + receptacle without plate yield. 40 N is a receptacle / housing problem, not a pin-steel problem.
5. **Phase 0 test 5** — 1.25 A through the contact bus ≥ 10 min. Log plate temp near a contact and near an EPM pocket. No thermal throttle.
6. **Phase 0 test 6** — 2 000 dock / undock cycles on pin + contacts.
7. **Two stacks unmixed.** 20 mm hybrid face (4× Ø5 EPM, 1.8 mm pin, 6 contacts, 12 V / 1.25 A, IRLZ44N cap-dump) is not the 25 mm cell (Ø8.2 pocket, Ø6.0 × 4.0 stack, AWG 36, DRV8871 @ 12 V). 28.8 N stays retired on the 25 mm cell.
8. **Drive discipline.** Hold current after switch is **zero**. Phase 0 fires **one coil at a time** on one cap bank until cap + bus headroom is measured. Do not shrink the 25 mm Ø6 disc until measured \(I_\text{release}\) exists. Pulse width is set from peak-I, not from leftover paper 25 ms.

Phase 0 drive remains capacitor dump, IRLZ44N class, 220 µF charged 30–36 V, 34 AWG preferred / 32 accept, 160–200 turns, cold R 2.5–6 Ω, peak I ≥ 4 A (6–10 A target). Those numbers live only in `PHASE0.md`.

---

## Companion gates (8) — lock tonight, no CAD change

These do not relax any number above. They only say when the word “companion” is allowed.

1. **No companion claim** until a filled `MEASUREMENT_CARD.md` exists for the stack under discussion (turns, cold R, peak I, pulse width, ON N, OFF N, temps). Blank card = bench coupon, not a pet.
2. **35 N is the human-contact interrupt.** **40 N is docked structural shear.** They are not the same limit. On a human path, 35 N wins (magnetic softening / unlatch). On a seated dock path, 40 N stays. Do not average them. Do not use 40 N as a “safe squeeze.”
3. **41 °C skin** is the paper contact-temperature cap. Soak data may only tighten it. It does not replace the Phase 0 1.25 A / 10 min log.
4. **Soft safety skin is mandatory** on any human-proximate build. It stays optional on bench coupons and fixture faces. Soft skin must still pass locked soft-dock, pin engagement, and contact wipe if it is on a docking face.
5. **Skills, mesh, community hooks, and behavior libraries cannot override** the 35 N interrupt, brownout / fall unlatch, or coil-fire interlock.
6. **12 V face bus and Phase 0 30–36 V pulse bank stay fixture-side** until contacts are covered or isolated. No exposed companion face with a live dump cap or bare pogos.
7. **One coil at a time** until that stack’s cap / VM / bus headroom is measured and written. Applies to Phase 0 four-coil select and to any later multi-face cell.
8. **Community Enhancement Suites stay optional and zero-impact.** Adding a skin, sensor, credit hook, or haptic does not mint V2.0 and does not move Phase 0 or 25 mm option A numbers.

---

## Explicitly not locked

- V2.0 as a product or file
- Node count for a swarm or suit
- ISO 10218 / ISO 25785 as a certification (V1.12 names them as intent only)
- Child-safe / pet-safe use
- Pinch / crush maps for two faces closing
- Measured hold on either stack
- Shrinking the 25 mm Ø8.2 pocket or Ø6 disc
- Mixing files

---

## What to do next

Same physical gate as before.

- 25 mm: wind AWG 36, count turns, 12 V DRV8871 pulse, pull ON/OFF, write `MEASUREMENT_CARD.md`.
- Phase 0: machine the 20 mm plate, wind four EPMs to the SOP, pulse, pull ≥ 3 N, soak 1.25 A / 10 min.

Paper hold claims do not move either baseline.
