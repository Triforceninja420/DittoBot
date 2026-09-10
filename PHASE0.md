# DittoBot / Voxel Box — Phase 0 Single-Face Demonstrator

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

**This file is the locked 20 mm hybrid face.**
It is **not** the 25 mm cubic cell in this repository (`README.md`, `COIL_REVISION.md`, `openscad`).
Do not paste 25 mm coil, driver, magnet, or hold numbers into this document.
Do not paste these Phase 0 numbers into the 25 mm files.

Public parent: `DittoBot_Phase0_Face_Public_Spec.docx`  
CAD / SOP / BOM / sims: `Phase0_Independent_Fab_Package/` (v0.2, 2026-09-08)  
Aluminum plate package: `DittoBot_Phase0_Aluminum_FacePlate_Package_v0.1.txt`

Status: **frozen** until measured ON / OFF / current / temperature / cycle data are published.

Parts lock (2026-09-09): Nd grade, finished EPM height, pole pieces, coil of record, shear test path. Protocol T1–T5 unchanged.

---

## What Phase 0 is

One docking face. Prove latch, pin, contacts, and thermal on hardware.
Not a cube. Not a swarm. Not the GitHub 25 mm cell.

| Item | Locked value |
| :--- | :--- |
| Envelope | 20.00 × 20.00 mm square face |
| Plate | 6061-T6, 1.00 mm nominal (accept 0.80–1.20) |
| EPMs | 4×, 2×2 at 11.00 mm pitch |
| Magnet stack | AlNiCo 5 Ø5.0 × 8.0 mm + **NdFeB N42** Ø5.0 × 8.0 mm NiCuNi |
| Finished EPM height | **8.0 mm along rod axis** after grind; working face through Ø5.10 pocket |
| Pole pieces | **2× AISI 1018, 1.00 mm thick × 8.00 mm × 11.0 mm** per EPM |
| Pin | 1.80 mm ±0.02 hardened, 1.85 mm through-bore at origin |
| Contacts | 6× pogo / leaf on a 4.20 mm hex ring |
| Bus | 12 V nominal, **1.25 A continuous ≥ 10 min** |
| Shear | **≥ 40 N / 30 s, no permanent set, contacts closed** — pin + receptacle |
| Soft-dock | ≥ 90 % capture at ≤ 2.5 mm lateral |
| Hard-lock | ≥ 95 % |
| Cycles | 2 000 dock / undock |
| EPM ON | **≥ 3.0 N** at zero gap on mild steel |
| EPM OFF | **< 0.3 N** residual |
| Drive | capacitor dump, **IRLZ44N** class FET / H-bridge |
| Pulse bank | 220 µF (100–470 accept), charged **30–36 V** (24–48 accept) |
| Wind | **180 turns ±10, 34 AWG**, on the AlNiCo. Counted turns required. |
| Coil R | 2.5–6 Ω cold |
| Peak I | 6–10 A target, ≥ 4 A measured |
| Hold current after switch | **zero** |

N35 is a stock substitute only if N42 cylinders are unavailable. It is not the build grade.
32 AWG is allowed only if 34 AWG will not pack; turn count stays 180 ±10.

The 25 mm cell uses a single centered Ø8.2 pocket, Ø6.0 × 4.0 magnet stack, AWG 36, and a DRV8871. Those parts do not belong on this face.

---

## Geometry (CAD table)

Origin at face center. Z out of the docking face.

**Plate**
- 20.00 × 20.00 mm
- Thickness 1.00 mm
- Edge break 0.20–0.30 mm
- Flatness ≤ 0.05 mm target
- Optional 304 SS if you accept worse thermal

**EPM pockets (4)**
- Centers (±5.50, ±5.50) mm
- Pocket Ø 5.10 mm × 0.75 mm deep (0.70–0.80)
- Blind preferred so the back stays a heat spreader
- Optional Ø1.20 mm lead exit at inner pocket edge
- Finished pole face ~4.5–5.0 mm, proud or flush after bond

**Pin**
- Bore Ø 1.85 mm through at (0, 0)
- Pin 1.80 mm ±0.02, 17-4 PH / 440C / hardened alloy
- Engagement ≥ 3.00 mm into the mating receptacle
- 40 N is a receptacle problem more than a pin-steel problem

**Contacts (6)**
- Regular hexagon, ring radius 4.20 mm
- Angles 30 / 90 / 150 / 210 / 270 / 330 deg
- Hole Ø 1.10 mm (1.00–1.20)
- Keep-out ≥ 1.50 mm from EPM pocket edge and pin bore
- Wipe 0.30–0.50 mm

**Corner mounts (4)**
- Ø 1.70 mm (M1.4 / M1.6 clearance)
- Centers (±7.80, ±7.80) mm

**Capture**
- ±2.50 mm lateral, ±6–7 deg angular
- Chamfer and/or 0.40–0.60 mm side ridges

Files in the fab package:
- `CAD/DittoBot_Phase0_FacePlate_20mm.scad`
- `CAD/DittoBot_Phase0_FacePlate_20mm.svg` (print at 100 %)
- `CAD/DittoBot_Phase0_FacePlate_Dimensions.txt`

---

## Magnetic latch (4× EPM)

Side-by-side rods between mild-steel pole pieces. Working face presents through the 5.10 mm pocket.

Per EPM (build grade):
- AlNiCo 5 rod Ø5.0 × 8.0 mm, axial
- NdFeB N42 cylinder Ø5.0 × 8.0 mm, axial, NiCuNi
- Two AISI 1018 pole pieces, 1.00 mm × 8.00 mm × 11.0 mm
- Finished height along rod axis: 8.0 mm after grind. Do not add axial slugs.
- Pole working faces ground coplanar ±0.05 mm
- Wind primarily around the AlNiCo, 180 turns ±10 of 34 AWG
- Same winding sense on all four coils relative to the working face
- Log counted turns and cold R on every serial

Pulse:
- Pre-charge 220 µF to 30–36 V
- IRLZ44N (or four-FET H-bridge), 22 Ω gate resistors
- Dead time ≥ 1 µs
- Pulse width 50–150 µs typical (80–120 µs first pass)
- Opposite polarity for OFF
- Sequential coil select on one cap bank. Do not fire two coils at once unless you have measured headroom.
- Energy into the magnetic circuit is typically 5–30 mJ. Stored energy at 220 µF / 36 V is 0.143 J; most of that does not couple.

Force fixture, not Maxwell-stress paper:
1. Pulse ON. Measure ≥ 3.0 N on mild steel at zero gap.
2. Pulse OFF. Residual < 0.3 N.
3. Log turns, cold R, charge V, peak I, ON N, OFF N.

Winding SOP: `winding/DittoBot_Phase0_EPM_Winding_SOP.txt`  
Pulse sim: `sim/epm_pulse_sim.py` (nominal first-pass ~8.2 A peak at 36 V / 220 µF / 4.2 Ω — simulation only).

---

## Electrical (first-article protoboard)

MCU: Raspberry Pi Pico (RP2040). Not the XIAO + DRV8871 stack from the 25 mm cell.

```
[6× pogos]──► 12V_BUS ──► 1.5 A fuse ──┬── buck 12→5 V ──► Pico VSYS
                                      ├── boost 12→36 V ──► C_PULSE 220 µF
                                      └── optional ride-through buffer

C_PULSE ──► H-bridge (IRLZ44N Q1–Q4) ──► low-side mux Q5–Q8 ──► E1..E4
PIN solenoid ──► Q9 low-side on 12 V
LOCK switch / hall ──► Pico GP14
Shunt 10–20 mΩ ──► INA219
TMP117 + NTC ──► I2C / ADC
```

Pico map (fab package):

| GP | Function |
| ---: | :--- |
| 0 / 1 | UART log |
| 2 / 3 / 6 / 7 | H-bridge A/B high and low |
| 4 / 5 | I2C (INA219, TMP117) |
| 8–11 | coil select Q5–Q8 |
| 12 | boost enable |
| 14 | lock state |
| 15 | pin drive |
| 16 | status LED |
| 26 | NTC |
| 27 | contact sense |
| 28 | cap voltage divider |

Contact assignment (redundant pairs):
- Pogo 1, 2 = +12 V
- Pogo 3, 4 = GND
- Pogo 5 = 12 V sense
- Pogo 6 = spare / AGND sense

Full netlist: `schematic/DittoBot_Phase0_Face_Schematic.txt`

---

## Success tests (do not relax)

1. **EPM ON** ≥ 3.0 N, **OFF** < 0.3 N, four coils.
2. **Soft-dock** ≥ 90 % at ≤ 2.5 mm offset.
3. **Hard-lock** ≥ 95 % with pin seated.
4. Shear ≥ 40 N in-plane for 30 s, no permanent set, contacts stay closed. Path is pin + receptacle. Magnetic-only hold is not a pass. T3: N=10 at 0 offset; both axes on half the samples.
5. **1.25 A** through the contact bus for ≥ 10 minutes. No thermal throttle. Log plate temp near a contact and near an EPM pocket.
6. **2 000** dock / undock cycles on the pin + contacts.

Paper hold claims do not move this baseline. Publish the measured table.

---

## What is not in this file

- 25 mm cube envelope, Ø8.2 pocket, Ø6.0 magnet, AWG 36, DRV8871, 28.8 N
- Community Enhancement Suites (optional skins, sensors, credit hooks — zero impact on these criteria)
- Native STEP/IGES, KiCad PCB, FEMM project (honest gaps in v0.2)

Those live elsewhere. This face stays a 20 mm aluminum demonstrator until the six tests above have numbers next to them.

---

## Build order

1. Cut the 6061 plate from the SCAD / SVG / dimension table.
2. Wind four EPMs + one spare: 180 ±10 t of 34 AWG on AlNiCo 5. Log counted turns and R.
3. Pulse on the bench fixture. Record peak I, ON N, OFF N.
4. Wire the Pico protoboard to the netlist.
5. Seat pin, soak 1.25 A / 10 min, log temperature.
6. Run T3 shear (40 N / 30 s) before calling the face done.
7. Publish measurements. Then talk about the next face.
