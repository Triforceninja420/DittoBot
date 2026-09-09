# 25 mm cell — measurement card

Project i started Nov/Dec 2025. Design owned by Craig. Programmable matter.

**This card is only for the public 25 mm cubic cell in this repository.**
It is not the locked Phase 0 20 mm hybrid face. Do not paste Phase 0 ON / OFF / shear / cap-dump numbers here. Do not paste these numbers into `PHASE0.md`.

Status: **blank until measured.** No latch claim until the table is filled. 28.8 N is retired on this cell.

Geometry under test (option A, 2026-09-09):
- Pocket: Ø8.2 mm × 4.0 mm (file `openscad`, unchanged)
- Magnet stack: Ø6.0 mm × 4.0 mm (NdFeB N52 + Alnico 5)
- Coil target: AWG 36, 160–180 turns counted on the bobbin
- Driver: DRV8871, VM = 12 V, ILIM ~3.0 A
- Logic: 3.3 V XIAO RP2040. Do not put 12 V on U1 VCC.

See `COIL_REVISION.md` for the wind window and why the first-pass 120 t / DRV8837C / 28.8 N line is dead.

---

## Card (fill what you actually measured)

| Field | Value | Unit / notes |
| :--- | :--- | :--- |
| Builder name / handle | | credit travels with the measurement |
| Date | | YYYY-MM-DD |
| Turns on bobbin | | count them; do not write the target |
| Wire | | AWG + enamel type |
| Cold R | | Ω, coil only, room temp |
| Magnet stack | | OD × height, grades if known |
| Mating plate | | material, thickness, finish |
| Gap | | mm. Same gap for ON and OFF |
| Coil rail V | | V at the DRV8871 VM pin during the pulse |
| Peak I | | A, scoped on the real pulse |
| Time to peak I | | ms |
| Pulse width used | | ms. Set from peak-I, not from paper 25 ms |
| ON force | | N |
| OFF force | | N, same plate, same gap, after OFF pulse |
| Coil temp after N pulses | | °C, state N and cadence |
| Driver temp after N pulses | | °C, state N and cadence |
| Photo / scope shot | | link or filename |

One row per coil. Add rows; do not overwrite someone else's numbers.

```
Turns on bobbin:
Cold R:
Peak I on 12 V DRV8871 pulse:
Pulse width at that peak:
ON N and OFF N (same plate / same gap):
Coil + driver temp after N pulses:
```

---

## How to take the numbers

1. Wind AWG 36 in the 1.1 mm annulus. Count turns on the bobbin. Publish the count you got, even if it is not 170.
2. Measure DC resistance cold, coil disconnected from the driver.
3. 12 V step on DRV8871. Scope current. Record time-to-peak. That time is the first pulse width. Stretch only if current has not peaked.
4. Pulse ON. Pull force on a luggage scale or fixture against mild steel at the logged gap.
5. Pulse OFF. Same plate, same gap. Log residual.
6. Repeat N pulses at the planned cadence. Log coil and DRV8871 case temperature.

If peak current never reaches ~3 A, ampere-turns never clear Alnico 5 *H_c* (~50 kA/m) and force will not decide geometry. Fix the pulse first.

---

## Who can fab this on $0–small cash

Not a lattice. One coil, one magnet stack, one driver, one plate.

- University lab with a winding jig and a force stand
- Makerspace with a grant or member-tools night
- Hardware hackathon that covers parts
- One person who can count turns and borrow a scope + luggage scale

Minimum parts (bench, not a breadboard farm): Ø6.0 × 4.0 magnet stack, AWG 36 magnet wire, DRV8871 breakout, 12 V supply, XIAO RP2040, mild-steel plate, luggage scale. Pulse firmware is `cpp`.

---

## What this file does not do

- Does not unfreeze Phase 0
- Does not change Phase 0 winding SOP (34/32 AWG, 160–200 t, 220 µF / 30–36 V cap-dump, IRLZ44N)
- Does not change Phase 0 success criteria (≥3 N ON, <0.3 N OFF, ≥40 N shear, 1.25 A × 10 min, 2 000 cycles)
- Does not restore 28.8 N on the 25 mm cell
