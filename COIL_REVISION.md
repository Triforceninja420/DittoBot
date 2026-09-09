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
* Claimed 28.8 N hold at 1.2 T / 0.1 mm

Ampere-turns: 120 × 1.2 = **144 AT**.

If the Alnico path length is ~4 mm:

    H ≈ NI / ℓ = 144 / 0.004 = 36 000 A/m = 36 kA/m

Alnico 5 *H_c* ≈ 50 kA/m. 36 kA/m is below coercivity. The Alnico does not reliably flip. Maxwell-stress 28.8 N assumes a 1.2 T gap field that this pulse cannot produce.

The coil was an inherited first pass. It is not the locked design of this project.

## Driver swap

| | First pass | Revision target |
| :--- | :--- | :--- |
| IC | DRV8837C (1.8 A pk, 11 V abs) | **DRV8871** (3.6 A pk, 6.5–45 V, resistor current limit) |
| Alternate | — | DRV8212 (~4 A), same job |
| Coil rail | 5 V (cannot feed DRV8871) | **12 V** |
| Logic rail | 3.3 V XIAO | 3.3 V XIAO, unchanged |
| Pulse duty | short EPM pulse | still short; peak rating is for the pulse, not DC |

IN1 / IN2 polarity in `cpp` stays the same. Set the DRV8871 current-limit resistor for the current you can actually reach in the coil, not for 3.6 A by default.

A 12 V rail on VM does not mean the XIAO or a 5 V-rated neighbor pad should see 12 V. Local regulators stay.

## Do not blindly double the turns

Whiteboard shortcut from the public thread: double turns, keep 12 V, land on 288 AT.

288 AT over 4 mm is only ~72 kA/m — about 1.4× *H_c*. Still marginal for a short pulse with leakage.

If you also raise current (e.g. 160 t × 3.2 A ≈ 512 AT → ~128 kA/m, or 160 t × 3.6 A ≈ 576 AT → ~144 kA/m), the switch field becomes real **only if** the winding window and L/R let that current exist at the end of the pulse.

### Winding window (the actual blocker)

Published at the same time:

* Pocket: Ø8.2 mm × 4.0 mm deep
* Magnet stack: D8 mm × 4 mm (NdFeB + Alnico)

Radial clearance if both numbers are literal: 0.1 mm per side. That is not a 120-turn winding window. The first-pass coil count and the first-pass pocket/core diameters are not consistent with each other.

Pick one before cutting more plastic:

* **A.** Smaller magnet stack (Ø5–6 mm class) inside the Ø8.2 mm pocket so the coil lives in the annulus.
* **B.** Keep an ~8 mm magnet stack and deepen / widen the pocket (OpenSCAD change).
* **C.** Put the coil behind the face, magnet stack flush in the 4 mm pocket.

OpenSCAD (`openscad`) is not changed in this drop. Geometry stays until A, B, or C is chosen.

Doubling to 240 turns of 0.15 mm inside the current 4 mm height is not a drop-in. Finer wire raises R. A taller winding needs a deeper pocket. Measure DC resistance and inductance on the coil you actually wind.

## What to measure before claiming a latch

1. DC resistance of the wound coil.
2. Approximate inductance (or time-to-peak current on a 12 V step).
3. Peak current during the real pulse (scope / current probe / sense resistor).
4. ON force and OFF force on a fixture, same air gap, same mating plate.
5. Coil and driver temperature after N pulses at the planned cadence.

Paper tesla and 28.8 N do not move the baseline. Publish the five numbers above.

## What this file does not do

* Does not unfreeze Phase 0.
* Does not change Phase 0 winding SOP (34/32 AWG, 160–200 t, 220 µF / 30–36 V cap-dump, IRLZ44N).
* Does not change Phase 0 success criteria (≥3 N ON, <0.3 N OFF, ≥40 N shear, 1.25 A × 10 min, 2 000 cycles).
