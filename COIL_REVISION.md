# 25 mm cell — coil / driver revision
2026-09-10

Project i started Nov/Dec 2025. Design owned by Craig. Programmable matter.

This file applies **only** to the public 25 mm cubic cell in this repository.
It does not change the locked Phase 0 20 mm hybrid face.

## What this revision is

Clean swap, not a redesign.

* Cell stays **25 mm**
* Pocket stays **Ø8.2 mm × 4.0 mm** (`openscad`, do not edit)
* Driver stays **DRV8871**, VM = **12 V**, ILIM \~**3.0 A**
* Logic stays 3.3 V XIAO. Do not put 12 V on U1 VCC

The only change is the core:

* Holding actor: a **small neodymium disc** where the coil used to be the main actor
* Coil: wound **around that disc** as the **release mechanism** only
* Hold current after the pulse is still zero. The magnet holds. The coil only bucks.

This is not an Alnico-flip EPM on this cell. Do not size the wind to flip Alnico 5 *H_c*. Size it so one pulse overpowers the disc at the working face.

## What was wrong (still retired)

Published first pass:

* 120 turns, AWG 34, DRV8837C, 25 ms, ±1.2 A, 3.3–5.0 V face bus
* D8 mm stack in an Ø8.2 mm pocket (0.1 mm radial — no wind window)
* Claimed 28.8 N hold at 1.2 T / 0.1 mm

Then option A (2026-09-09) tried to keep an Nd + Alnico flip stack at Ø6.0 × 4.0 and wind 160–180 t AWG 36 to clear Alnico *H_c*. That stack is **superseded on this cell** by the disc + release-coil swap. Phase 0 on the 20 mm face is unchanged.

28.8 N stays retired on this cell.

## Geometry lock — disc + release coil (2026-09-10)

OpenSCAD pocket is unchanged.

* Pocket: **Ø8.2 mm × 4.0 mm**
* Disc (hold): first build **Ø6.0 mm × 2.0–3.0 mm NdFeB N42/N52**, axial, centered on the old coil axis. If the disc is too strong for a 3 A pulse in this volume, drop to **Ø6 × 2 mm** or **Ø5 × 2 mm** before you change the cell or the driver.
* Coil: wound on the disc OD (thin bobbin or direct on the disc). Annulus is still **(8.2 − disc OD) / 2**.
* Options B (bigger pocket) and C (coil behind face) stay on the shelf

The disc sets hold. The coil does not hold.

## First wind to publish (not yet measured)

Wind for the **cancel peak**, not for continuous hold current.

| Wire | Insulated ≈ | Role |
| :--- | :--- | :--- |
| AWG 36 | \~0.15 mm | First pack in the remaining annulus |
| AWG 28–30 | thicker | Backup if you need lower DCR / higher peak I and will accept fewer turns |

**Build target for the first 25 mm release coil:**

* Wire: **AWG 36** first; **28–30 AWG** if peak I will not arrive
* Turns: **count them**. A realistic first pack in this pocket is **80–180 t** depending on disc OD and AWG. Publish the count on the bobbin.
* DCR target band: **2–6 Ω** so a 12 V DRV8871 pulse can put **1.5–3 A** into the winding
* Driver: **DRV8871**, VM = **12 V**, ILIM set near **3.0 A** (3.6 A is the peak rating, not the setpoint)
* Alternate driver: DRV8212
* Pulse: **50–200 ms** start band. Width is set from measured time-to-peak, not from paper 25 ms. Stretch only until current has peaked.
* Logic: 3.3 V XIAO, unchanged

The number that matters is **I_release** (and the pulse width at that current) that drops the mate against this disc at the logged gap. Ampere-turns to flip Alnico are the wrong metric on this cell.

## Driver — unchanged from option A

| | First pass | This lock |
| :--- | :--- | :--- |
| IC | DRV8837C (1.8 A pk, 11 V abs) | **DRV8871** (3.6 A pk, 6.5–45 V) |
| Coil rail | 5 V | **12 V** |
| Logic rail | 3.3 V | 3.3 V |
| Hold | coil / Alnico flip | **Nd disc, zero coil current** |
| Coil job | switch the stack | **release pulse only** |

IN1 / IN2 polarity in `cpp`: **release polarity is the one that bucks the disc.** Latch polarity is optional on this cell (disc is already holding). Keep both directions in firmware so you can find which way drops the plate.

## What to measure before claiming a latch

The measurement card still needs the release number. Holding force is the disc + gap + keeper. Do not size the coil from that.

1. Disc P/N, OD × thickness, grade.
2. Turns actually on the bobbin.
3. DC resistance.
4. Time-to-peak current on a 12 V step (or L).
5. **I_release min** that drops the mate at the test gap. Both polarities.
6. Pulse width that still drops at 80 % of that current (margin).
7. ON force (disc only, coil off) and OFF force (after release pulse) on the same plate / same gap.
8. Coil + driver temperature after N pulses at the planned cadence.

Paper tesla does not move the baseline. 28.8 N is retired on this cell.

## What this file does not do

* Does not unfreeze Phase 0.
* Does not change Phase 0 winding SOP (34/32 AWG, 160–200 t, 220 µF / 30–36 V cap-dump, IRLZ44N).
* Does not change Phase 0 success criteria (≥3 N ON, <0.3 N OFF, ≥40 N shear, 1.25 A × 10 min, 2 000 cycles).
* Does not change `openscad` pocket dimensions.