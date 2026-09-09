# DittoBot / Voxel Box
Programmable matter voxel lattice. Design owned by Craig. Started Nov/Dec 2025.

**This repository is the 25 mm cubic cell variant.**
It is **not** the locked Phase 0 Single-Face Demonstrator (20 mm hybrid face, 4× Ø5 EPM, 1.8 mm pin, 6 contacts, 12 V / 1.25 A / ≥40 N shear). Do not mix those numbers into this repo, and do not paste these numbers into Phase 0 docs.

---

## Status — 2026-09-09

The original coil / driver line in this repo was a first-pass parts list, not a measured latch.

| Item | First pass (superseded as a build target) | 25 mm revision target |
| :--- | :--- | :--- |
| Envelope | 25 mm cube | unchanged |
| EPM pocket | Ø8.2 × 4.0 mm, centered, 6 faces | geometry frozen until winding window is chosen |
| Coil | 120 turns AWG 34, 0.15 mm | redesign to the real annulus; do not blindly double turns |
| Driver | DRV8837C, 1.8 A pk / 11 V abs | **DRV8871** (3.6 A pk, 6.5–45 V) or DRV8212 |
| Pulse | 25 ms @ ±1.2 A | short pulse, current-limited; width set after R/L measure |
| Face / coil rail | written as 3.3–5.0 V | **12 V coil rail**; 3.3 V stays on the XIAO only |
| Ampere-turns | 120 × 1.2 = **144 AT** | first-pass 144 AT is below Alnico 5 *H_c* |
| Paper hold | 28.8 N at 1.2 T / 0.1 mm | **theoretical only — not a measured force** |

Why the first-pass coil is marked broken: Alnico 5 coercivity is ~50 kA/m. Over a ~4 mm path, 144 AT gives *H* ≈ 36 kA/m. That does not reliably reverse the Alnico. A spec with a known-weak coil reads as a known-weak project.

See `COIL_REVISION.md` for the winding-window problem, the driver swap, and what still has to be measured.

Firmware pin dance (IN1/IN2, pulse, then both LOW) is unchanged. Only the silicon and the rail change.

---

## 1. Mechanical Architecture

Cubic unit cell for FDM/SLA or later molding.

### Geometric Dimensions (unchanged this commit)
* **External Envelope:** 25.0 mm × 25.0 mm × 25.0 mm
* **Internal Electronics Cavity:** 21.8 mm × 21.8 mm × 21.8 mm
* **Nominal Wall Thickness:** 1.6 mm
* **Latching Core Bore:** Ø 8.2 mm × 4.0 mm depth, centered on all 6 faces
* **Interconnect Port Clearance:** 4-pin radial pitch at r = 6.0 mm, bore Ø 2.5 mm × 1.2 mm counterbore

### Mating
* Centering pocket for shear keying when neighbors engage.
* Exterior chamfers 0.5 mm × 45° on all 12 edges for neighbor-roll.

OpenSCAD source is the file `openscad` (no extension). Pocket geometry is frozen until the coil vs magnet stack is picked — see `COIL_REVISION.md`.

---

## 2. Magnetic Latching (EPM)

Pair a high-coercivity NdFeB with a low-coercivity Alnico 5, pulse the Alnico, hold with zero steady current.

### First-pass core line (still the published magnet stack; coil is what changes)
* **Permanent element:** NdFeB N52 (*B_r* ≈ 1.4 T)
* **Switchable element:** Alnico 5 (*B_r* ≈ 1.25 T, *H_c* ≈ 50 kA/m)
* **First-pass coil (do not build as the latch):** 120 turns, 0.15 mm (AWG 34)
* **First-pass drive (do not build as the latch):** 25 ms @ ±1.2 A through DRV8837C

### Paper force (Maxwell stress — not a test report)

    F = B² A / (2 μ₀)

* Pole area for an 8 mm diameter face: π (0.004 m)² ≈ 5.03×10⁻⁵ m²
* If *B_on* were 1.20 T at 0.1 mm gap: *F* ≈ 28.8 N
* If *B_off* were 0.14 T: *F_residual* ≈ 0.37 N

Those tesla values are assumed, not measured. They are invalid if the Alnico never switches. `python` prints the same paper sweep and now says so on stdout.

---

## 3. Electrical (25 mm revision target)

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

DRV8837C is retired as the 25 mm build target. Its 11 V ceiling and 1.8 A peak cannot feed a 12 V / multi-amp switch pulse. DRV8871 minimum VM is 6.5 V — the old 5 V face bus cannot run it. Split the rails.

### Face interconnect (unchanged pin names)

| Pad | Signal | Notes |
| :---: | :--- | :--- |
| 1 | `VBUS` | Neighbor power. Treat as **up to 12 V** on this revision. Do not feed 12 V into the XIAO 3V3 pin. |
| 2 | `GND` | Common ground |
| 3 | `DATA_A` | SDA / UART TX |
| 4 | `DATA_B` | SCL / UART RX |

BOM / netlist: file `text`.
Firmware pulse routine: file `cpp`.

---

## 4. State transition

Hold current after the pulse is zero. That part of the first pass is still correct.

    * Latch: IN1 HIGH, IN2 LOW for the measured pulse width, then both LOW.
    * Release: IN1 LOW, IN2 HIGH for the same width, then both LOW.
    * Quiescent: driver inputs low, coil current 0, hold is remanence only.

Start at 25 ms. Stretch only if the measured current has not peaked (L/R too slow). Do not run the coil continuous.

---

## What this repo is not

Phase 0 Independent Fab Package (20 mm aluminum face, 4× Ø5 EPM, cap-dump / IRLZ44N, ≥3 N ON, 40 N shear, 1.25 A × 10 min) lives in the project artifacts, not in these six files. Two stacks. Two number sets.
