# DittoBot / Voxel Box
Programmable matter voxel lattice. Design owned by Craig. Started Nov/Dec 2025.

**This repository is the 25 mm cubic cell variant.**
It is **not** the locked Phase 0 Single-Face Demonstrator (20 mm hybrid face, 4× Ø5 EPM, 1.8 mm pin, 6 contacts, 12 V / 1.25 A / ≥40 N shear). Do not mix those numbers into this repo, and do not paste these numbers into Phase 0 docs.

---

## Status — 2026-09-10  disc + release coil

Architecture / version ladder: [DESIGN.md](DESIGN.md) (Aug 3 2026 paper baseline).  
This page is the 25 mm cell only.

Clean swap, not a redesign. Cell 25 mm, pocket Ø8.2 × 4.0, DRV8871 stay.
The coil is no longer the holding actor.

| Item | First pass (do not build) | This lock (build target) |
| :--- | :--- | :--- |
| Envelope | 25 mm cube | unchanged |
| Pocket | Ø8.2 × 4.0 mm, 6 faces | **unchanged** (`openscad` not edited) |
| Hold | D8 / then Ø6 Nd+Alnico flip | **NdFeB disc Ø6.0 × 2.0–3.0 mm** |
| Coil | 120 t AWG 34 (hold/switch) | **wound around the disc, release only** |
| Driver | DRV8837C, 1.8 A / 11 V | **DRV8871**, ILIM \~3.0 A (or DRV8212) |
| Coil rail | 3.3–5.0 V | **12 V**; 3.3 V stays on the XIAO |
| Pulse | 25 ms @ ±1.2 A | short pulse sized to **overpower the disc** |
| Paper hold | 28.8 N | **retired on this cell** |

The measurement card still needs **I_release**. Holding force is the disc. Do not size the coil from hold.

Do **not** publish 180 t AWG 33 as if it packs in this annulus. Count the turns you actually wind. Details in `COIL_REVISION.md`.

Nothing on this cell is a measured latch until disc, turns, R, peak I, I_release, ON N, and OFF N are published. Fill MEASUREMENT_CARD.md.

---

## 1. Mechanical Architecture

Cubic unit cell for FDM/SLA or later molding.

### Geometric Dimensions
* **External Envelope:** 25.0 mm × 25.0 mm × 25.0 mm
* **Internal Electronics Cavity:** 21.8 mm × 21.8 mm × 21.8 mm
* **Nominal Wall Thickness:** 1.6 mm
* **Latching Core Bore:** Ø 8.2 mm × 4.0 mm depth, centered on all 6 faces — **unchanged**
* **Hold disc (2026-09-10):** Ø 6.0 mm × 2.0–3.0 mm NdFeB, coil in the remaining annulus
* **Interconnect Port Clearance:** 4-pin radial pitch at r = 6.0 mm, bore Ø 2.5 mm × 1.2 mm counterbore

### Mating
* Centering pocket for shear keying when neighbors engage.
* Exterior chamfers 0.5 mm × 45° on all 12 edges for neighbor-roll.

OpenSCAD source is the file `openscad` (no extension). Pocket stays Ø8.2 × 4.0. Options B (bigger pocket) and C (coil behind the face) are not this lock.

---

## 2. Magnetic Latching (25 mm cell)

Permanent disc holds. Coil around the disc bucks the field for release. Hold current after the pulse is zero.

### Core
* **Permanent element:** NdFeB N42/N52 disc, Ø6.0 × 2.0–3.0 mm first build
* **Switchable element:** none on this cell (no Alnico flip here)
* **Coil:** counted turns around the disc, DCR 2–6 Ω target
* **Drive:** DRV8871, 12 V, ILIM \~3.0 A
* If 3 A cannot release, shrink the disc before changing the cell or the driver

### First pass (retired)
* 120 t AWG 34, 25 ms @ 1.2 A, DRV8837C, D8 mm stack — do not build
* 2026-09-09 Ø6 Nd+Alnico flip + 160–180 t AWG 36 — superseded on this cell only

### Force
Maxwell stress *F = B²A / (2μ₀)* is paper. Do not quote 28.8 N. `python` still prints an old 8 mm sweep as a warning, not a spec. Fixture ON (coil off) / OFF (after pulse) only. The card number is I_release.

---

## 3. Electrical

    +-----------------------+
    |      XIAO RP2040      |
    |  3.3 V local rail     |
    | GPIO0 (IN1)           |
    | GPIO1 (IN2)           |
    | GPIO6 (SDA)  GPIO7    |
    +-----------+-----------+
                |
                v
    +-----------------------+
    |   DRV8871 H-bridge    |
    |   VM = 12 V coil rail |
    | OUT1 ----[ COIL ]---- OUT2 |
    +-----------------------+

DRV8837C is retired on this cell. DRV8871 VM min is 6.5 V — the old 5 V bus cannot run it. Split the rails.

### Face interconnect

| Pad | Signal | Notes |
| :---: | :--- | :--- |
| 1 | `VBUS` | Neighbor power. Up to 12 V on this revision. Not the XIAO 3V3 pin. |
| 2 | `GND` | Common ground |
| 3 | `DATA_A` | SDA / UART TX |
| 4 | `DATA_B` | SCL / UART RX |

BOM / netlist: `text`.  
Pulse routine: `cpp`.  
Wind and window: `COIL_REVISION.md`.

---

## 4. State transition

    * Release: the IN1/IN2 polarity that bucks the disc, for the measured pulse width, then both LOW.
    * Opposite polarity kept in firmware so you can find which way drops the plate.
    * Quiescent: coil current 0. Hold is the disc only.

Start in the 50–200 ms band. Stretch only if measured current has not peaked. Do not run the coil continuous.

---

## What this repo is not

Phase 0 Independent Fab Package (20 mm aluminum face, 4× Ø5 EPM, cap-dump / IRLZ44N, ≥3 N ON, 40 N shear, 1.25 A × 10 min) is a different stack. Two number sets. Do not mix them.

Locked 20 mm face: [PHASE0.md](PHASE0.md).  
Architecture / version ladder: [DESIGN.md](DESIGN.md).