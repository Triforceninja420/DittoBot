# 25 mm cell — coil / driver revision
2026-09-09

Project i started Nov/Dec 2025. Design owned by Craig. Programmable matter.

This file applies **only** to the public 25 mm cubic cell in this repository.
It does not change the locked Phase 0 20 mm hybrid face.

## What was wrong

Published first pass:

* 120 turns, AWG 34 (0.15 mm)
* DRV8837C, 25 ms, ±1.2 A
* Face bus written 3.3–5.0 V
* Magnet stack written D8 mm in a Ø8.2 mm pocket
* Claimed 28.8 N hold at 1.2 T / 0.1 mm

Ampere-turns: 120 × 1.2 = **144 AT**.

If the Alnico path length is \~4 mm:

    H ≈ NI / ℓ = 144 / 0.004 = 36 000 A/m = 36 kA/m

Alnico 5 *H_c* ≈ 50 kA/m. 36 kA/m is below coercivity. The Alnico does not reliably flip. Maxwell-stress 28.8 N assumes a 1.2 T gap field that this pulse cannot produce.

Radial clearance with a literal D8 mm stack in an Ø8.2 mm pocket: 0.1 mm per side. That is not a 120-turn window. The coil was an inherited first pass. It is not the locked design of this project.

## Geometry lock — option A

Picked 2026-09-09. OpenSCAD pocket is unchanged.

* Pocket: **Ø8.2 mm × 4.0 mm** (file `openscad`, do not edit for this lock)
* Magnet stack: **Ø6.0 mm × 4.0 mm** total (NdFeB N52 + Alnico 5, split height as wound)
* Annulus: (8.2 − 6.0) / 2 = **1.1 mm per side**
* Options B (bigger pocket) and C (coil behind face) stay on the shelf

Ø6 mm pole area is \~56% of an 8 mm face. Paper hold scales down with area. Do not keep quoting 28.8 N on this stack.

## First wind to publish (not yet measured)

Do **not** write “180 t AWG 33” into this hole. AWG 33 (\~0.20 mm insulated) packs about 5 layers × \~20 turns in 4 mm ≈ **100 t**.

| Wire | Insulated ≈ | Layers in 1.1 mm | Turns / layer in 4 mm | Realistic turns |
| :--- | :--- | :--- | :--- | :--- |
| AWG 33 | \~0.20 mm | \~5 | \~20 | \~100 t |
| AWG 36 | \~0.15 mm | \~7 | \~26 | \~160–180 t |

**Build target for the first 25 mm coil:**

* Wire: **AWG 36** (0.13 mm bare, enamel)
* Turns: **160–180 t** (count them; publish the count you actually wound)
* Driver: **DRV8871**, VM = **12 V**, ILIM set near **3.0 A** (3.6 A is the peak rating, not the setpoint)
* Alternate driver: DRV8212
* Pulse: start 25 ms; stretch only until measured current has peaked
* Logic: 3.3 V XIAO, unchanged. Do not put 12 V on U1 VCC

Worked examples after a successful wind (path ℓ ≈ 4 mm):

* 170 t × 3.0 A = 510 AT → H ≈ 128 kA/m
* 180 t × 3.0 A = 540 AT → H ≈ 135 kA/m
* 100 t AWG 33 × 3.6 A = 360 AT → H ≈ 90 kA/m (backup if 36 is unavailable)

All of those clear Alnico 5 *H_c* (\~50 kA/m) **if** the pulse actually reaches that current. L/R and window fill decide that, not the whiteboard.

## Driver swap

| | First pass | A-lock |
| :--- | :--- | :--- |
| IC | DRV8837C (1.8 A pk, 11 V abs) | **DRV8871** (3.6 A pk, 6.5–45 V) |
| Coil rail | 5 V | **12 V** |
| Logic rail | 3.3 V | 3.3 V |
| Magnet OD | 8 mm (no annulus) | **6 mm** |
| Coil | 120 t AWG 34 | **160–180 t AWG 36** |

IN1 / IN2 polarity in `cpp` stays the same.

## What to measure before claiming a latch

1. Turns actually on the bobbin.
2. DC resistance.
3. Time-to-peak current on a 12 V step (or L).
4. Peak current during the real pulse.
5. ON force and OFF force on a fixture, same gap, same mating plate.
6. Coil + driver temperature after N pulses at the planned cadence.

Paper tesla does not move the baseline. 28.8 N is retired on this cell.

## What this file does not do

* Does not unfreeze Phase 0.
* Does not change Phase 0 winding SOP (34/32 AWG, 160–200 t, 220 µF / 30–36 V cap-dump, IRLZ44N).
* Does not change Phase 0 success criteria (≥3 N ON, <0.3 N OFF, ≥40 N shear, 1.25 A × 10 min, 2 000 cycles).
* Does not change `openscad` pocket dimensions.