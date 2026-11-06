# 25 mm cell — measurement card

Project i started Nov/Dec 2025. Design owned by Craig. Programmable matter.

**This card is only for the public 25 mm cubic cell in this repository.**
It is not the locked Phase 0 20 mm hybrid face. Do not paste Phase 0 ON / OFF / shear / cap-dump numbers here. Do not paste these numbers into `PHASE0.md`.

Status: **blank until measured.** No latch claim until the table is filled. **No companion claim** until this table is filled. 28.8 N is retired on this cell.

Process stamps that do not change option A geometry: `LOCKS.md` (16 paper locks, 2026-09-14).

Geometry under test (option A, 2026-09-09; thermal revision 2026-11-06):
- Pocket: Ø8.2 mm × 4.0 mm (file `openscad`, unchanged)
- Magnet stack: Ø6.0 mm × 4.0 mm (NdFeB N52 + Alnico 5)
- Coil target: **2–4× AWG 36 in parallel** (or 1× AWG 30 equivalent), 160–180 turns counted on the bobbin. Single-strand AWG 36 is retired — sim hit 444 °C at 1.25 A × 10 min.
- Driver: DRV8871, VM = 12 V, ILIM ~3.0 A
- Logic: 3.3 V XIAO RP2040. Do not put 12 V on U1 VCC.
- Latch face: replaceable carbide or 440C shim, 0.50 mm thick, clip-in. Wear item — swap at 100 µm or 2 000 cycles.

See `COIL_REVISION.md` Rev 2026-11-06 for the wind window, parallel-strand math, and why the first-pass 120 t / DRV8837C / 28.8 N line is dead.

---

## Card (fill what you actually measured)

| Field | Value | Unit / notes |
| :--- | :--- | :--- |
| Builder name / handle | | credit travels with the measurement |
| Date | | YYYY-MM-DD |
| Turns on bobbin | | count them; do not write the target |
| Wire | | AWG + enamel type + strand count (parallel) |
| Cold R | | Ω, coil only, room temp (total across parallel strands) |
| Magnet stack | | OD × height, grades if known |
| Mating plate | | material, thickness, finish |
| Gap | | mm. Same gap for ON and OFF |
| Coil rail V | | V at the DRV8871 VM pin during the pulse |
| Peak I | | A, scoped on the real pulse |
| Time to peak I | | ms |
| Pulse width used | | ms. Set from peak-I, not from paper 25 ms |
| ON force | | N |
| OFF force | | N, same plate, same gap, after OFF pulse |
| Coil temp after N pulses | | °C, state N and cadence. T4 pass line: < 85 °C after 1.25 A × 10 min at 25 °C ambient |
| Driver temp after N pulses | | °C, state N and cadence |
| Shim wear depth | | µm after 2 000 cycles or at service interval |
| Photo / scope shot | | link or filename |

One row per coil. Add rows; do not overwrite someone else's numbers.

```
Turns on bobbin:
Cold R (total, all strands):
Strand count + AWG:
Peak I on 12 V DRV8871 pulse:
Pulse width at that peak:
ON N and OFF N (same plate / same gap):
Coil + driver temp after N pulses:
Shim wear depth:
```

---

## How to take the numbers

1. Wind **parallel strands** (2× AWG 36 or 1× AWG 30) in the 1.1 mm annulus. Count turns on the bobbin. Publish the count you got, even if it is not 170. Single-strand fine wire is pulse-only — do not use it for the 1.25 A continuous soak.
2. Measure DC resistance cold, coil disconnected from the driver. Total across all parallel strands.
3. 12 V step on DRV8871. Scope current. Record time-to-peak. That time is the first pulse width. Stretch only if current has not peaked.
4. Pulse ON. Pull force on a luggage scale or fixture against mild steel at the logged gap.
5. Pulse OFF. Same plate, same gap. Log residual.
6. Repeat N pulses at the planned cadence. Log coil and DRV8871 case temperature. **T4 pass: coil + driver under 85 °C after 1.25 A × 10 min, 25 °C ambient, no forced airflow.**
7. After 2 000 cycles (or if clearance opens past 0.15 mm), measure shim wear depth. Swap shim if worn past budget.

If peak current never reaches ~3 A, ampere-turns never clear Alnico 5 *H_c* (~50 kA/m) and force will not decide geometry. Fix the pulse first.

---

## Who can fab this on $0–small cash

Not a lattice. One coil, one magnet stack, one driver, one plate.

- University lab with a winding jig and a force stand
- Makerspace with a grant or member-tools night
- Hardware hackathon that covers parts
- One person who can count turns and borrow a scope + luggage scale

Minimum parts (bench, not a breadboard farm): Ø6.0 × 4.0 magnet stack, AWG 36 magnet wire (parallel wind), DRV8871 breakout, 12 V supply, XIAO RP2040, mild-steel plate, luggage scale, carbide/440C shim. Pulse firmware is `cpp`.

---

## What this file does not do

- Does not unfreeze Phase 0
- Does not change Phase 0 winding SOP (34/32 AWG, 160–200 t, 220 µF / 30–36 V cap-dump, IRLZ44N)
- Does not change Phase 0 success criteria (≥3 N ON, <0.3 N OFF, ≥40 N shear, 1.25 A × 10 min, 2 000 cycles)
- Does not restore 28.8 N on the 25 mm cell
- Does not mint V2.0 or a companion robot
- Does not shrink the Ø6 disc or the Ø8.2 pocket

Human-contact interrupt on a later proximate build is 35 N. That number is not a 25 mm hold claim. Do not write it in the ON-force box.
