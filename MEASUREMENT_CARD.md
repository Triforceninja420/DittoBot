# 25 mm cell — measurement card

Project i started Nov/Dec 2025. Design owned by Craig. Programmable matter.

**This card is only for the public 25 mm cubic cell in this repository.**
It is not the locked Phase 0 20 mm hybrid face. Do not paste Phase 0 ON / OFF / shear / cap-dump numbers here. Do not paste these numbers into `PHASE0.md`.

Status: **blank until measured.** No latch claim until the table is filled. 28.8 N is retired on this cell.

Geometry under test (disc + release coil, 2026-09-10):
- Pocket: Ø8.2 mm × 4.0 mm (file `openscad`, unchanged)
- Hold: NdFeB disc, first build Ø6.0 × 2.0–3.0 mm N42/N52, axial
- Coil: wound around the disc as release only. Count turns. DCR target 2–6 Ω
- Driver: DRV8871, VM = 12 V, ILIM \~3.0 A
- Logic: 3.3 V XIAO RP2040. Do not put 12 V on U1 VCC.

The number this card still needs is **I_release**, not holding force and not Alnico-flip AT.
See `COIL_REVISION.md`.

---

## Card (fill what you actually measured)

| Field | Value | Unit / notes |
| :--- | :--- | :--- |
| Builder name / handle | | credit travels with the measurement |
| Date | | YYYY-MM-DD |
| Disc | | P/N, OD × thickness, grade |
| Turns on bobbin | | count them; do not write the target |
| Wire | | AWG + enamel type |
| Cold R | | Ω, coil only, room temp |
| Mating plate | | material, thickness, finish |
| Gap | | mm. Same gap for ON and OFF |
| Coil rail V | | V at the DRV8871 VM pin during the pulse |
| Peak I | | A, scoped on the real pulse |
| Time to peak I | | ms |
| Pulse width used | | ms. Set from peak-I |
| **I_release min** | | A that drops the mate. Log both polarities |
| Pulse width at 80 % of I_release | | ms, still drops? |
| ON force | | N, disc only, coil off |
| OFF force | | N, same plate, same gap, after release pulse |
| Coil temp after N pulses | | °C, state N and cadence |
| Driver temp after N pulses | | °C, state N and cadence |
| Photo / scope shot | | link or filename |

One row per coil. Add rows; do not overwrite someone else's numbers.

---

## How to take the numbers

1. Seat the disc in the Ø8.2 pocket. Wind around it. Count turns. Publish the count you got.
2. Measure DC resistance cold, coil disconnected from the driver.
3. 12 V step on DRV8871. Scope current. Record time-to-peak. That time is the first pulse width.
4. Coil off. Pull ON force (disc hold) on a luggage scale or fixture against mild steel at the logged gap.
5. Pulse release. Same plate, same gap. Log residual. Sweep current until it drops. That current is I_release. Repeat the other polarity.
6. Confirm a pulse at 80 % of I_release still drops (or record that it does not).
7. Repeat N pulses at the planned cadence. Log coil and DRV8871 case temperature.

If peak current never reaches the I_release you need, the disc is too strong or the wind DCR is too high. Shrink the disc before you change the cell or the driver.

---

## Who can fab this on $0–small cash

Not a lattice. One coil, one disc, one driver, one plate.

- University lab with a winding jig and a force stand
- Makerspace with a grant or member-tools night
- Hardware hackathon that covers parts
- One person who can count turns and borrow a scope + luggage scale

Minimum parts (bench, not a breadboard farm): Ø6.0 × 2–3 mm Nd disc, magnet wire, DRV8871 breakout, 12 V supply, XIAO RP2040, mild-steel plate, luggage scale. Pulse firmware is `cpp`.

---

## What this file does not do

- Does not unfreeze Phase 0
- Does not change Phase 0 winding SOP (34/32 AWG, 160–200 t, 220 µF / 30–36 V cap-dump, IRLZ44N)
- Does not change Phase 0 success criteria (≥3 N ON, <0.3 N OFF, ≥40 N shear, 1.25 A × 10 min, 2 000 cycles)
- Does not restore 28.8 N on the 25 mm cell