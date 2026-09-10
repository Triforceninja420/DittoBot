# DittoBot / Voxel Box
Programmable matter voxel lattice. Design owned by Craig. Started Nov/Dec 2025.

**This repository is the 25 mm cubic cell variant.**
It is **not** the locked Phase 0 Single-Face Demonstrator (20 mm hybrid face, 4× Ø5 EPM, 1.8 mm pin, 6 contacts, 12 V / 1.25 A / ≥40 N shear). Do not mix those numbers into this repo, and do not paste these numbers into Phase 0 docs.

---

## Status — 2026-09-09  option A locked

Architecture / version ladder: [DESIGN.md](DESIGN.md) (Aug 3 2026 paper baseline).  
This page is the 25 mm cell only.

The original coil / driver line was a first-pass parts list, not a measured latch.
Geometry pick for this cell is **A**: shrink the magnet, keep the published pocket.

| Item | First pass (do not build) | Option A (build target) |
| :--- | :--- | :--- |
| Envelope | 25 mm cube | unchanged |
| Pocket | Ø8.2 × 4.0 mm, 6 faces | **unchanged** (`openscad` not edited) |
| Magnet stack | D8 mm × 4 mm | **Ø6.0 mm × 4.0 mm** (1.1 mm annulus) |
| Coil | 120 t AWG 34 | **160–180 t AWG 36** |
| Driver | DRV8837C, 1.8 A / 11 V | **DRV8871**, ILIM \~3.0 A (or DRV8212) |
| Coil rail | 3.3–5.0 V | **12 V**; 3.3 V stays on the XIAO |
| Pulse | 25 ms @ ±1.2 A | short pulse; width set after peak-I measure |
| Ampere-turns | 144 AT ≈ 36 kA/m | 170 t × 3.0 A = 510 AT ≈ 128 kA/m (if current peaks) |
| Paper hold | 28.8 N at 8 mm / 1.2 T | **retired on this cell** (Ø6 area is \~56% of Ø8) |

First-pass 144 AT is below Alnico 5 *H_c* (\~50 kA/m). A D8 stack in an Ø8.2 pocket also leaves 0.1 mm radial — no winding window.

Do **not** publish 180 t AWG 33 in this annulus. AWG 33 packs \~100 t here. Use AWG 36 for 160–180 t. Details in `COIL_REVISION.md`.

Nothing on this cell is a measured latch until turns, R, peak I, ON N, and OFF N are published. Fill MEASUREMENT_CARD.md.

---

## 1. Mechanical Architecture

Cubic unit cell for FDM/SLA or later molding.

### Geometric Dimensions
* **External Envelope:** 25.0 mm × 25.0 mm × 25.0 mm
* **Internal Electronics Cavity:** 21.8 mm × 21.8 mm × 21.8 mm
* **Nominal Wall Thickness:** 1.6 mm
* **Latching Core Bore:** Ø 8.2 mm × 4.0 mm depth, centered on all 6 faces — **unchanged**
* **Magnet stack (option A):** Ø 6.0 mm × 4.0 mm, coil in the 1.1 mm annulus
* **Interconnect Port Clearance:** 4-pin radial pitch at r = 6.0 mm, bore Ø 2.5 mm × 1.2 mm counterbore

### Mating
* Centering pocket for shear keying when neighbors engage.
* Exterior chamfers 0.5 mm × 45° on all 12 edges for neighbor-roll.

OpenSCAD source is the file `openscad` (no extension). Pocket stays Ø8.2 × 4.0. Options B (bigger pocket) and C (coil behind the face) are not this lock.

---

## 2. Magnetic Latching (EPM)

Pair NdFeB N52 with Alnico 5 (*H_c* ≈ 50 kA/m). Pulse the Alnico. Hold current after the pulse is zero.

### Option A core
* **Permanent element:** NdFeB N52
* **Switchable element:** Alnico 5
* **Stack OD × height:** Ø6.0 mm × 4.0 mm
* **Coil:** 160–180 turns AWG 36, counted on the bobbin
* **Drive:** DRV8871, 12 V, ILIM \~3.0 A

### First pass (retired)
* 120 t AWG 34, 25 ms @ 1.2 A, DRV8837C, D8 mm stack — do not build

### Force
Maxwell stress *F = B²A / (2μ₀)* is paper. Ø6 mm area ≈ 2.83×10⁻⁵ m². Do not quote 28.8 N (that assumed an 8 mm face at 1.2 T). `python` still prints the old 8 mm sweep as a warning, not a spec. Fixture ON/OFF only.

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

    * Latch: IN1 HIGH, IN2 LOW for the measured pulse width, then both LOW.
    * Release: IN1 LOW, IN2 HIGH for the same width, then both LOW.
    * Quiescent: coil current 0. Hold is remanence only.

Start at 25 ms. Stretch only if measured current has not peaked. Do not run the coil continuous.

---

## What this repo is not

Phase 0 Independent Fab Package (20 mm aluminum face, 4× Ø5 EPM, cap-dump / IRLZ44N, ≥3 N ON, 40 N shear, 1.25 A × 10 min) is a different stack. Two number sets. Do not mix them.

Locked 20 mm face: [PHASE0.md](PHASE0.md).  
Architecture / version ladder: [DESIGN.md](DESIGN.md).