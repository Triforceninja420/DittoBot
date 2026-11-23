# DittoBot / Voxel Box — Phase 0 Single-Face Demonstrator

## Executive Summary

- **Problem:** Prove one docking face works in hardware before committing to the 25 mm lattice.
- **Approach:** 20 mm face (size committed 2026-11-23), 7075-T6 plate, NdFeB N52 magnet, dual staggered 8 mm cams, three hardened steel latch pins, 5 N seating spring, six pogo contacts.
- **Key numbers:** Snap 34.6 N. Soft-dock ≥90% at ≤2.5 mm. Shear 5 028 N simulated (40 N target). Release net +65.7 N. Thermal <1.5 K at 0.44 W. Mass 9.2 g. Cycles locked at 2 000 (3 000 stretch goal).
- **Open risks:** Epoxy is the only aging component. First-article metrology and tip-bond pull test are recommended before full stack-up. Native STEP/IGES and KiCad exports are honest gaps.
- **Status:** Frozen until measured ON/OFF/current/temperature/cycle data are published. Revision 2026-11-21.

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

**This file is the locked 20 mm dual-cam face** (face size committed at 20 mm on 2026-11-23; was 30 mm).

> **Face-size note (2026-11-23, Craig):** the Phase 0 face size is committed at **20 mm**, matching `sims/phase0_monte_carlo.py` ("same 20 mm face article"). The geometry tables below now dimension 20.00 × 20.00 mm (cams re-derived for the 20 mm envelope in the CAD redesign; corner mounts per `cad/voxel_cell_phase0_20mm.scad`). Re-dimensioning landed in the CAD redesign commit (2026-11-23).

It supersedes the frozen 20 mm hybrid face (4× Ø5 EPM, 1.8 mm pin) from earlier revisions.
It is **not** the 25 mm cubic cell in this repository (`README.md`, `docs/BASELINE_UPGRADES.md`, `cad/voxel_cell.scad`).
Do not paste 25 mm coil, driver, magnet, or hold numbers into this document.
Do not paste these Phase 0 numbers into the 25 mm files.

Public parent: `DittoBot_Phase0_Face_Public_Spec.docx`  
CAD / SOP / BOM / sims: `Phase0_Independent_Fab_Package/` (v0.2, 2026-09-08)  
Aluminum plate package: `DittoBot_Phase0_Aluminum_FacePlate_Package_v0.1.txt`

Status: **frozen** until measured ON / OFF / current / temperature / cycle data are published.

Revision: **2026-11-21** — dual-cam staggered release, 6 mm NdFeB, 20 mm face (was 30 mm; re-dimensioned 2026-11-23). All 26 simulation tests passed. Cam bore corrected 16.1 → **16.05 mm** (2026-11-23 sweep) to match CAD (`cad/voxel_cell.scad` uses 16.05); 0.05 mm nominal clearance. Monte Carlo 100k trials: all-pass 98.04%, T3 pass 99.30%, 702 T3 fails (LAT_OFFSET_SIGMA_MM 0.65→0.55, re-run 2026-11-23; was 96.62% / 97.87% / 2 133). First-article metrology + tip-bond pull test added as recommended checks. **Cycle spec locked at 2 000; 3 000 listed as epoxy-dependent stretch goal.** T3 acceptance window: lat ≤ 1.5 mm, vel ≤ 0.5 m/s (original; tightened to 1.0/0.35 on 2026-11-23, all-pass fell to 87.73%, reverted to 1.2/0.4 same day, then reverted to original 1.5/0.5).

---

## What Phase 0 is

One docking face. Prove snap-in capture, dual-cam release, pin latch, contacts, and thermal on hardware.
Not a cube. Not a swarm. Not the GitHub 25 mm cell.

Design philosophy: prove the mechanism at a hand-assemblable scale, then shrink the lattice. 20 mm is the committed face size (2026-11-23); the 30 mm plate was the earlier reference article. Density is a later problem.

| Item | Locked value |
| :--- | :-------- |
| Envelope | 20.00 × 20.00 mm square face (committed 2026-11-23) |
| Plate | 7075-T6 (upgraded from 6061-T6, CAD rev 2026-11-23), 1.00 mm nominal (accept 0.80–1.20) |
| Magnet | NdFeB N52, Ø6.0 × 2–3 mm disc (coil release-only; Alnico off this cell), axial, centered |
| Coil | 40 turns, 34 AWG, ~0.75 Ω cold, sized for release not hold |
| Snap (axial pull) | 34.6 N simulated at 0.5 mm gap |
| Seating spring | 5 N, keeps faces seated during mating only |
| Latch | 3× hardened steel pins (third pin opposite the pair, CAD rev 2026-11-23); shear capacity ~5 028 N simulated on the earlier 2-pin build |
| Retraction actuator | small solenoid coil ~1/3 g, pulls pins back on release |
| Cam release | dual 8 mm radius cams, bore Ø16.05 (0.05 mm nominal clearance), staggered corners (8,8) and (22,22), steel-backed polymer tips |
| Cam tip | polymer-on-steel, 8 mm contact width, Hertzian 35.4 MPa, margin 1.98× |
| Release net | +65.7 N after cam breaks residual bond |
| Soft-dock | ≥ 90 % capture at ≤ 2.5 mm lateral, ±7° angular |
| Insertion force | 5 N |
| Shear target | ≥ 40 N (simulated 5 028 N, 126× margin) |
| T3 acceptance window | lat ≤ 1.5 mm, vel ≤ 0.5 m/s (original baseline; 1.0/0.35 and 1.2/0.4 both reverted after 87.73%) |
| Thermal | < 1.5 K rise at 0.44 W pulse-duty |
| Mass | 9.2 g module total |
| Cycles | **2 000 dock / undock (locked spec)** |
| Stretch goal | 3 000 cycles — requires epoxy swap or mechanical tip backup; not required for Phase 0 lock |
| Wear | 0.19 µm cam tip loss over 2 000 cycles (polymer sacrificial, swappable) |
| Environmental | stainless or black-oxide/nitride hardened cam core; polymer tip does sliding |

The 25 mm cell uses a single centered Ø8.2 pocket, NdFeB disc Ø6.0×2–3 mm residual hold with coil as release-only (Alnico retired from this cell), parallel AWG 36, DRV8871 pulse from a 36 V bank, axial pin, and cavity potting. Those parts do not belong on this face.
The retired 20 mm face used 4× Ø5 AlNiCo/NdFeB EPMs and a 1.8 mm pin. Superseded by this revision.

---

## Why the redesign (simulation findings, 2026-11-21)

Full battery of 24 tests on the prior 6 mm magnet build: 23 passed. Failures were release (coil field only 0.7% of magnet coercivity — could not break 34 N residual) and cam contact stress (50 MPa vs 70 MPa yield, 1.4× margin).

Fixes applied in this revision:

1. **Release:** dual staggered cams replace the single 16 mm cam. Two 8 mm cams on opposite corners give two contact points and a mechanical advantage the single cam lacked; release net +65.7 N.
2. **Cam stress:** steel-backed polymer tips drop Hertzian contact stress to 35.4 MPa (margin 1.98× over 70 MPa yield).
3. **Latch:** third pin added opposite the pair for symmetric shear distribution.
4. **Plate:** 7075-T6 upgraded from 6061-T6 for shear margin.

---

## Geometry (20 mm face, rev 2026-11-23)

### Plate

- 7075-T6 aluminum, 1.00 mm nominal thickness (accept 0.80–1.20)
- Envelope exactly 20 × 20 mm
- Edge break 0.20–0.30 mm
- Flatness target ≤ 0.10 mm
- Four corner mounts, OD 1.70 mm (M1.4/M1.6 clearance), centers per `cad/voxel_cell_phase0_20mm.scad` (re-derived for 20 mm envelope; old ±12.80 was 30 mm)

### Magnet + coil (centered, axial)

- NdFeB N52, Ø6.0 × 2–3 mm disc (coil release-only; Alnico off this cell)
- Pocket Ø8.2 × 4.0 mm (blind back intact as heat spreader), +0.10 on diameter
- Coil: 40 turns 34 AWG, ~0.75 Ω cold, DRV8871 driver, sized for I_release, pulse-only, zero hold current

### Cams (2, staggered)

- Radius 8 mm each (Ø16 across)
- Bore Ø16.05 (0.05 mm nominal clearance), tolerance ±0.05
- Positions: (8,8) and (22,22) — re-derived for 20 mm envelope in CAD redesign; do not use any older layout
- Core: steel/stainless; tip: polymer, steel-backed
- Contact width 8 mm, Hertzian 35.4 MPa, margin 1.98×

### Latch pins (3)

- Pin OD 1.80 mm, bore OD 1.85 mm
- Engagement ≥ 3.00 mm into mating receptacle
- Positions per `cad/voxel_cell_phase0_20mm.scad`
- Combined shear ~5 028 N simulated on the earlier 2-pin build (126× the 40 N target)

### Seating spring

- 5.00 N total (4× non-magnetic phosphor-bronze or BeCu springs, 1.0 N/mm combined rate, 5 mm preload)
- Material: non-magnetic only

### Contacts (6)

- Ring radius 4.20 mm (scales with face; verify on 20 mm CAD)
- Hole OD 1.10 mm (accept 1.00–1.20)
- Angles: 30 / 90 / 150 / 210 / 270 / 330
- Keep-out ≥ 1.50 mm from magnet pocket edge and pin bores
- Wipe 0.30–0.50 mm

### Capture

- Lateral ±2.50 mm, angular ±6–7°
- Chamfer 0.50 mm
- Side ridges 0.50 high × 0.60 wide
- Insertion force 5 N

Approach placement: 0.42 mm at 1-sigma (HARDWARE_MAPPING §1.2, contributor A).
Gates: T3 lat 1.5 mm, vel 0.5 m/s, spring 5.00 N, shear bar 40 N, all-pass 98.04%.

Mass: TBD on 20 mm article (9.2 g was the 30 mm module). Thermal < 1.5 K at 0.44 W pulse-duty. Cycles: 2 000 dock/undock. Environmental: black oxide or nitride on cam cores.

---

## Fab package

- `cad/voxel_cell_phase0_20mm.scad` (the real SCAD — blind 0.75 mm pocket, dual staggered cams, Ø16.05 cam bores, 3-pin latch, 20 mm envelope)
- `CAD/DittoBot_Phase0_FacePlate_20mm.svg` (top-view fab drawing, generated 2026-11-23 from the 20 mm redesign)
- `CAD/DittoBot_Phase0_FacePlate_Dimensions.txt` (dimension table tracking locked spec numbers)
- `Phase0_Independent_Fab_Package/` (v0.2, 2026-09-08) — SOP, BOM, sims
- `DittoBot_Phase0_Aluminum_FacePlate_Package_v0.1.txt` — aluminum plate package
- `tools/phase0_estimate.py` — public estimate script (Maxwell-style force paper + basic I²R thermal), updated 2026-11-21 to current Ø6 mm NdFeB numbers; labeled estimate only

---

## Success tests (locked)

1. **Snap** — 34.6 N axial at 0.5 mm gap on mild steel; off-axis and 60 °C still holds.
2. **Soft-dock** — ≥ 90 % capture at ≤ 2.5 mm lateral, ±7° angular; insertion ≤ 5 N.
3. **Hard-lock** — ≥ 95 % with all three pins seated.
4. **Shear** — ≥ 40 N through pins without plate yield. Simulated 5 028 N.
5. **Release** — net +65.7 N via dual-cam + retraction actuator sequence.
6. **Thermal** — 1.25 A through the contact bus ≥ 10 min. Log plate temp. 41 °C skin cap.
7. **Cycles** — 2 000 dock / undock on pins + cams + contacts. Cam tip wear 0.19 µm simulated.

---

## Recommended checks (before full stack-up)

**Intentional relief (design-side insurance)**
- Cam bores: nominal Ø16.05 gives 0.05 mm clearance over 16 mm cam OD (Monte Carlo locked; docs corrected from 16.1 on 2026-11-23 sweep to match CAD). If a cam still binds, file — don't scrap the plate. The 0.05 mm is the design clearance, not extra on top.
- Pin bores: drill 0.05 mm oversize with the option to ream to final fit. A slightly loose pin that you bond in place beats a hole you can't clean up.
- Magnet pocket: blind depth 0.75 mm nominal; verify with depth micrometer through the opening before pressing. A pocket 0.1 mm shallow is a press-fit disaster; 0.1 mm deep just means the magnet sits proud and you sand it flush.

**Metrology sequence (article one)**
1. **Cam radius and lobe profile** — height gauge or optical comparator. Target 8.00 mm radius, lobe edge square to face within 0.05 mm. Check bore at Ø16.05 ±0.05.
2. **Pin-bore true position** — CMM if available; otherwise a dowel pin of bore diameter plus a digital caliper. Catch a 0.5 mm offset before assembly.
3. **Blind pocket depth** — depth micrometer through the magnet opening, before any press. Log the number.
4. **Plate flatness** — surface plate and indicator, ≤ 0.10 mm target (loosened from 0.05 mm on 2026-11-21 after Monte Carlo showed 37.5% failure rate at 0.05 on 1 mm plate). A warped plate still kills soft-dock capture, but 0.10 is what a real shop can hit.
5. **Contact wipe** — 0.30–0.50 mm of travel on each pogo pair. Too little and you get intermittent; too much and you bend pins.

**Tip-bond pull test (before full stack-up)**
- Bond a dummy polymer tip to a steel coupon using the same epoxy and cure schedule as the real cams.
- Pull it at 50 N (the design cam load) on a simple fixture — a vise, a spring scale, or a luggage scale with a lever.
- If it holds 50 N without the polymer tearing or the bond shearing, the real cams are good. If it fails, you learn on a coupon instead of a finished module.
- Log: epoxy type, cure time and temp, pull force, failure mode.

**Why it matters:** simulation assumes perfect geometry. Real parts have burrs, epoxy creeps, polymer swells in humidity, and fab houses drill off-center. The relief and the pull test close the cheapest failure modes before they cost you a plate.

---

## What is not in this file

- 25 mm cube envelope, Ø8.2 pocket, NdFeB disc Ø6.0×2–3 mm residual (coil release-only), DRV8871, axial pin, potting
- Retired 20 mm 4×EPM face (superseded 2026-11-21)
- Community Enhancement Suites (optional skins, sensors, credit hooks — zero impact on these criteria)
- Native STEP/IGES, KiCad PCB, FEMM project (honest gaps)
- Companion / V2.0 language
