# DittoBot / Voxel Box

Programmable matter voxel lattice. Design owned by Craig. Started November/December 2025.

**This repository is the 25 mm cubic cell variant.**

It is **not** the locked Phase 0 Single-Face Demonstrator (20 mm hybrid face, 4× Ø5 EPM, 1.8 mm pin, 6 contacts, 12 V / 1.25 A / ≥40 N shear). Do not mix the two stacks. See [docs/PHASE0.md](docs/PHASE0.md).

---

## Baseline Updates — 2026-11-19

Underwater + space sealing, stronger residual magnet, and mechanical hard-lock are now part of the normal 25 mm cell baseline. Pocket and envelope unchanged.

Full details: [docs/BASELINE_UPGRADES.md](docs/BASELINE_UPGRADES.md)

Summary of what changed:
- Magnet stack: SmCo 2:17 Ø7.5 mm × 3.0 mm (replaces previous Ø6 mm)
- Short axial pin + receptacle for mechanical load path after magnetic soft-dock
- Full cavity potting + face coatings / PTFE lip for water and vacuum protection
- Pulse-only drive + thermal governor as default

Paper estimates only. Credit follows measured data.

Extreme-environment inheritance (deep ocean, cryo, high-rad, corrosive, high-g, bio, etc.) for later versions: [docs/EXTREME_ENVIRONMENTS.md](docs/EXTREME_ENVIRONMENTS.md)

---

## Status — 2026-09-09 (Option A locked), revised 2026-11-06, baseline update 2026-11-19

The original coil / driver line was a first-pass parts list, not a measured latch. Geometry pick for this cell is **A**: shrink the magnet, keep the published pocket.

**2026-11-06 thermal + wear revision:** Private analysis flagged T4 thermal and T5 latch wear. Fixes: wind 2–4× AWG 36 in parallel (or 1× AWG 30) for any continuous-duty use, and seat a replaceable carbide shear shim on the latch face. Details in [docs/COIL_REVISION.md](docs/COIL_REVISION.md) Rev 2026-11-06, [docs/PHASE0.md](docs/PHASE0.md), and [docs/SIM_NOTES.md](docs/SIM_NOTES.md).

**2026-11-19 baseline update:** See [docs/BASELINE_UPGRADES.md](docs/BASELINE_UPGRADES.md) for SmCo Ø7.5 mm, mechanical pin, potting, and pulse-only standard.

| Item | First pass (do not build) | Current baseline |
| :--- | :---- | :---- |
| Envelope | 25 mm cube | unchanged |
| Pocket | Ø8.2 × 4.0 mm, 6 faces | **unchanged** (`cad/voxel_cell.scad`) |
| Magnet stack | D8 mm × 4 mm | **SmCo 2:17 Ø7.5 mm × 3.0 mm** |
| Coil | 120 t AWG 34 | **160–180 t AWG 36**, parallel strands for any sustained pulse |
| Driver | DRV8837C, 1.8 A / 11 V | **DRV8871**, ILIM ~3.0 A (or DRV8212) |
| Coil rail | 3.3–5.0 V | **12 V**; 3.3 V stays on the XIAO |
| Pulse | 25 ms @ ±1.2 A | short pulse; 36–48 V bank for SmCo; width set after peak-I measure |
| Paper hold | 28.8 N at 8 mm / 1.2 T | **~15–48 N** (area-scaled, paper only) |
| Latch face | bare | **carbide or 440C shear shim** + PTFE lip + conformal coating |
| Sealing | open cavity | **full cavity potting** + face coatings |
| Hard-lock | magnetic only | **axial pin + receptacle** after soft-dock |

First-pass 144 AT is below Alnico 5 *H_c* (~50 kA/m). A D8 stack in an Ø8.2 pocket also leaves 0.1 mm radial — no winding window.

Nothing on this cell is a measured latch until turns, R, peak I, ON N, and OFF N are published. Fill [docs/MEASUREMENT_CARD.md](docs/MEASUREMENT_CARD.md).

Hold current after the pulse is zero. Disc holds; coil releases. Pulse-only is now default.

---

## Repository Structure

```
cad/          OpenSCAD geometry (25 mm cell + Phase 0 fixture)
firmware/     Pulse driver for XIAO RP2040
tools/        Analysis scripts (paper force sweep + phase0_estimate.py)
bom/          Bill of materials and netlist
docs/         Specifications, locks, phase notes, build handoff, SIM_NOTES.md, BASELINE_UPGRADES.md, EXTREME_ENVIRONMENTS.md
assets/       Renders
```

## Key Documents

- [docs/BASELINE_UPGRADES.md](docs/BASELINE_UPGRADES.md) — 2026-11-19 underwater + space standard (SmCo Ø7.5, pin hard-lock, potting, pulse-only)
- [docs/EXTREME_ENVIRONMENTS.md](docs/EXTREME_ENVIRONMENTS.md) — Inheritance path for deep ocean, cryo, high-rad, corrosive, high-g, bio, and more (later versions)
- [docs/COIL_REVISION.md](docs/COIL_REVISION.md) — Why the first pass failed, Option A lock, parallel-strand thermal fix, carbide shim
- [docs/BUILD.md](docs/BUILD.md) — Build handoff for the 25 mm cell
- [docs/PHASE0.md](docs/PHASE0.md) — Frozen 20 mm hybrid face (separate stack)
- [docs/LOCKS.md](docs/LOCKS.md) — Process locks (2026-09-14)
- [docs/MEASUREMENT_CARD.md](docs/MEASUREMENT_CARD.md) — Blank card for measured data
- [docs/MIN_PARTS.md](docs/MIN_PARTS.md) — Minimum kit for one counted coil
- [docs/SIM_NOTES.md](docs/SIM_NOTES.md) — Private analysis context vs locked measured gates; public path is measure on the fixture
- [docs/POST_2040_OUTLOOK.md](docs/POST_2040_OUTLOOK.md) — Speculative post-2040 scale-change modes (inward shrink, outward expansion, hierarchical nesting, variable-density zones, split/merge). Does not change locked criteria.
- [docs/COMMUNITY_ENHANCEMENT_SUITES.md](docs/COMMUNITY_ENHANCEMENT_SUITES.md) — Matching optional suites grouped by phase. Zero-impact on locked baselines.
- [tools/phase0_estimate.py](tools/phase0_estimate.py) — Simple public paper estimate (Maxwell force + basic thermal). Not a full docking/shear sim.

## 1. Mechanical Architecture

Cubic unit cell for FDM/SLA or later molding.

### Geometric Dimensions
* **External Envelope:** 25.0 mm × 25.0 mm × 25.0 mm
* **Internal Electronics Cavity:** 21.8 mm × 21.8 mm × 21.8 mm
* **Nominal Wall Thickness:** 1.6 mm
* **Latching Core Bore:** Ø 8.2 mm × 4.0 mm depth, centered on all 6 faces — **unchanged**
* **Magnet stack (current baseline):** SmCo 2:17 Ø7.5 mm × 3.0 mm
* **Interconnect Port Clearance:** 4-pin radial pitch at r = 6.0 mm, bore Ø 2.5 mm × 1.2 mm counterbore

### Mating
* Centering pocket for shear keying when neighbors engage.
* Exterior chamfers 0.5 mm × 45° on all 12 edges for neighbor-roll.
* Short axial pin + receptacle for mechanical hard-lock after magnetic soft-dock (see BASELINE_UPGRADES.md).

OpenSCAD source: [cad/voxel_cell.scad](cad/voxel_cell.scad). Pocket stays Ø8.2 × 4.0. Pin features and magnet OD require CAD update.

---

## 2. Magnetic Latching (EPM)

SmCo 2:17 residual hold. Pulse for release. Hold current after the pulse is zero.

### Current baseline
* **Permanent element:** SmCo 2:17
* **Stack OD × height:** Ø7.5 mm × 3.0 mm
* **Coil:** 160–180 turns AWG 36, counted on the bobbin; **2–4 parallel strands** for any sustained pulse train
* **Drive:** DRV8871, 12 V logic rail, 36–48 V pulse bank, ILIM ~3.0 A
* **Latch face:** carbide or 440C shear shim + PTFE lip + conformal coating
* **Hard-lock:** axial pin engages after soft-dock

### Force
Maxwell stress is paper. Current area-scaled paper hold ~15–48 N. Do not quote older 28.8 N numbers. Fixture ON/OFF only. See [tools/force_sweep.py](tools/force_sweep.py) and [tools/phase0_estimate.py](tools/phase0_estimate.py).

---

## 3. Electrical

```
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
```

Split the rails. Pulse bank is 36–48 V polypropylene film capacitors.

### Face interconnect

| Pad | Signal | Notes |
| :----: | :----: | :---- |
| 1 | `VBUS` | Neighbor power. Up to 12 V on this revision. Not the XIAO 3V3 pin. |
| 2 | `GND` | Common ground |
| 3 | `DATA_A` | SDA / UART TX |
| 4 | `DATA_B` | SCL / UART RX |

BOM / netlist: [bom/bom_netlist.txt](bom/bom_netlist.txt).  
Pulse routine: [firmware/pulse_driver.cpp](firmware/pulse_driver.cpp).  
Wind and window: [docs/COIL_REVISION.md](docs/COIL_REVISION.md).

---

## 4. State transition

* Latch: IN1 HIGH, IN2 LOW for the measured pulse width, then both LOW.
* Release: IN1 LOW, IN2 HIGH for the same width, then both LOW.
* Quiescent: coil current 0. Hold is remanence only.
* Pulse-only is default. Firmware thermal governor required.

Start at 25 ms. Stretch only if measured current has not peaked.

---

## What this repo is not

Phase 0 Independent Fab Package (20 mm aluminum face, 4× Ø5 EPM, cap-dump / IRLZ44N, ≥3 N ON, 40 N shear, 1.25 A × 10 min) is a different stack. Two number sets. Do not mix them. See [docs/PHASE0.md](docs/PHASE0.md).

V2.0, a companion swarm, ISO certification, and Community Enhancement Suites are not this coupon. [docs/LOCKS.md](docs/LOCKS.md) is process only. [docs/MEASUREMENT_CARD.md](docs/MEASUREMENT_CARD.md) stays blank until measured.

License: MIT
