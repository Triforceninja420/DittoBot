# DittoBot / Voxel Box — Phase 0 Single-Face Demonstrator

## Executive Summary

- **Problem:** Prove one docking face works in hardware before committing to the 25 mm lattice.
- **Approach:** 20 mm face (size committed 2026-11-23), 7075-T6 plate, NdFeB N52 magnet, Option A sliding-pin release, three hardened steel latch pins, 5 N seating spring, six pogo contacts.
- **Key numbers:** Snap 34.6 N. Soft-dock ≥90% at ≤2.5 mm. Shear 5 028 N simulated (40 N target). Release: magnet-pull retention ≥ 1.8 N via Option A sliding pin. Thermal <1.5 K at 0.44 W. Mass 9.2 g. Cycles locked at 2 000 (3 000 stretch goal).
- **Open risks:** Epoxy is the only aging component. First-article metrology is recommended before full stack-up. Native STEP/IGES and KiCad exports are honest gaps.
- **Status:** Frozen until measured ON/OFF/current/temperature/cycle data are published. Revision 2026-11-23b.

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

**This file is the locked 20 mm sliding-pin face** (face size committed at 20 mm on 2026-11-23; was 30 mm). Dual-cam era retired 2026-11-23b — see `docs/GATE5_SUPERSEDED.md`.

> **Face-size note (2026-11-23, Craig):** the Phase 0 face size is committed at **20 mm**, matching `sims/phase0_monte_carlo.py` ("same 20 mm face article"). Geometry tables dimension 20.00 × 20.00 mm; corner mounts per `cad/voxel_cell_phase0_20mm.scad`.

It supersedes the frozen 20 mm hybrid face (4× Ø5 EPM, 1.8 mm pin) from earlier revisions.
It is **not** the 25 mm cubic cell in this repository (`README.md`, `docs/BASELINE_UPGRADES.md`, `cad/voxel_cell.scad`).
Do not paste 25 mm coil, driver, magnet, or hold numbers into this document.
Do not paste these Phase 0 numbers into the 25 mm files.

> **Option A note (2026-11-23, Craig):** Phase 0 release is the sliding-pin architecture defined in `docs/OPTION_A_RELEASE_SPEC.md` — magnet-pull retention (≥ 1.8 N), single Ø2.0 mm sliding pin, no cams on the face. Cams are deferred to Option A / the 25 mm cell and documented as superseded in `docs/GATE5_SUPERSEDED.md`.

Public parent: `DittoBot_Phase0_Face_Public_Spec.docx`  
CAD / SOP / BOM / sims: `Phase0_Independent_Fab_Package/` (v0.2, 2026-09-08)  
Aluminum plate package: DittoBot_Phase0_Aluminum_FacePlate_Package_v0.1.txt (offline package, not in this repo)

Status: **frozen** until measured ON / OFF / current / temperature / cycle data are published.

Revision: **2026-11-23b** — Option A sliding-pin release (cams retired), 6 mm NdFeB, 20 mm face (was 30 mm). Monte Carlo 100k trials: all-pass 98.04%, T3 pass 99.30%, 702 T3 fails (LAT_OFFSET_SIGMA_MM 0.65→0.55). First-article metrology added as recommended check. **Cycle spec locked at 2 000; 3 000 listed as epoxy-dependent stretch goal.** T3 acceptance window: lat ≤ 1.5 mm, vel ≤ 0.5 m/s.

---

## What Phase 0 is

One docking face. Prove snap-in capture, Option A sliding-pin release, pin latch, contacts, and thermal on hardware.
Not a cube. Not a swarm. Not the GitHub 25 mm cell.

Design philosophy: prove the mechanism at a hand-assemblable scale, then shrink the lattice. 20 mm is the committed face size (2026-11-23); the 30 mm plate was the earlier reference article. Density is a later problem.

| Item | Locked value |
| :--- | :-------- |
| Envelope | 20.00 × 20.00 mm square face (committed 2026-11-23) |
| Plate | 7075-T6 (upgraded from 6061-T6, CAD rev 2026-11-23), 1.00 mm nominal (accept 0.80–1.20) |
| Magnet | NdFeB N52, Ø6.0 × 2–3 mm disc (coil release-only; Alnico off this cell), axial, centered |
| Coil | 40 turns, 34 AWG, ~0.75 Ω cold, sized for release not hold |
| Snap (axial pull) | 34.6 N simulated at 0.5 mm gap |
| Seating spring | 5.00 N total (4× non-magnetic phosphor-bronze or BeCu springs, 1.0 N/mm combined rate, 5 mm preload) |
| Latch | 3× hardened steel pins (third pin opposite the pair, CAD rev 2026-11-23); shear capacity ~5 028 N simulated on the earlier 2-pin build |
| Release | Option A sliding pin, Ø2.0 mm single axial; magnet-pull retention ≥ 1.8 N; no cams on face |
| Soft-dock | ≥ 90 % capture at ≤ 2.5 mm lateral, ±7° angular |
| Insertion force | 5 N |
| Shear target | ≥ 40 N (simulated 5 028 N, 126× margin) |
| T3 acceptance window | lat ≤ 1.5 mm, vel ≤ 0.5 m/s |
| Thermal | < 1.5 K rise at 0.44 W pulse-duty |
| Mass | 9.2 g module total |
| Cycles | **2 000 dock / undock (locked spec)** |
| Stretch goal | 3 000 cycles — requires epoxy swap or mechanical tip backup; not required for Phase 0 lock |
| Environmental | stainless or black-oxide/nitride on hardened pin cores |

The 25 mm cell uses a single centered Ø8.2 pocket, NdFeB disc Ø6.0×2–3 mm residual hold with coil as release-only (Alnico retired from this cell), parallel AWG 36, DRV8871 pulse from a 36 V bank, axial pin, and cavity potting. Those parts do not belong on this face.
The retired 20 mm face used 4× Ø5 AlNiCo/NdFeB EPMs and a 1.8 mm pin. Superseded by this revision. The dual-cam face (rev 2026-11-21) is retired — `docs/GATE5_SUPERSEDED.md`.

---

## Why the redesign (simulation findings, 2026-11-21)

Full battery of 24 tests on the prior 6 mm magnet build: 23 passed. Failures were release (coil field only 0.7% of magnet coercivity — could not break 34 N residual) and cam contact stress (50 MPa vs 70 MPa yield, 1.4× margin).

Fixes applied in rev 2026-11-21:

1. **Release:** dual staggered cams replace the single 16 mm cam. Two 8 mm cams on opposite corners give two contact points and a mechanical advantage the single cam lacked; release net +65.7 N.
2. **Cam stress:** steel-backed polymer tips drop Hertzian contact stress to 35.4 MPa (margin 1.98× over 70 MPa yield).
3. **Latch:** third pin added opposite the pair for symmetric shear distribution.
4. **Plate:** 7075-T6 upgraded from 6061-T6 for shear margin.

Rev 2026-11-23b retired the cams: Phase 0 release is now the Option A sliding-pin architecture (magnet-pull retention ≥ 1.8 N, single Ø2.0 mm sliding pin). Cam-era numbers (65.7 N net, 16.05 bore, 0.19 µm wear, Hertzian 35.4 MPa) are archived in `docs/GATE5_SUPERSEDED.md` and do not apply to the current build.

---

## Geometry (20 mm face, rev 2026-11-23b)

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

### Release (Option A sliding pin — cams deferred)

- Single Ø2.0 mm sliding release pin, axial
- Magnet-pull retention ≥ 1.8 N
- No cam bores on Phase 0 face

### Latch pins (3)

- Pin OD 1.80 mm, bore OD 1.85 mm
- Engagement ≥ 3.00 mm into mating receptacle; receptacle depth ≥ 2.5 mm (Craig, 2026-11-23 — plate is 1.0 mm, pin travels 3.0 mm, so 2.5 mm gives margin on both faces)
- Positions per `cad/voxel_cell_phase0_20mm.scad` (r 7.45 at 73° / 155° / 328°)
- Combined shear ~5 028 N simulated on the earlier 2-pin build (126× the 40 N target)

### Seating spring

- 5.00 N total (4× non-magnetic phosphor-bronze or BeCu springs, 1.0 N/mm combined rate, 5 mm preload)
- Material: non-magnetic only

### Contacts (6)

- Ring radius 6.25 mm
- Hole OD 1.10 mm (accept 1.00–1.20)
- Angles: 50 / 110 / 170 / 230 / 290 / 350
- Keep-out ≥ 1.50 mm from magnet pocket edge and pin bores
- Wipe 0.30–0.50 mm

### Capture

- Lateral ±2.50 mm, angular ±6–7°
- Chamfer 0.50 mm
- Side ridges 0.50 high × 0.60 wide
- Insertion force 5 N

Approach placement: 0.42 mm at 1-sigma (HARDWARE_MAPPING §1.2, contributor A).
Gates: T3 lat 1.5 mm, vel 0.5 m/s, spring 5.00 N, shear bar 40 N, all-pass 98.04%.

Mass: 9.2 g module. Thermal < 1.5 K at 0.44 W pulse-duty. Cycles: 2 000 dock/undock.

---

## Fab package

- `cad/voxel_cell_phase0_20mm.scad` (the real SCAD — blind 0.75 mm pocket, Option A sliding-pin release, 3-pin latch, 20 mm envelope)
- `cad/DittoBot_Phase0_FacePlate_20mm.svg` (top-view fab drawing, generated 2026-11-23 from the 20 mm redesign)
- `cad/DittoBot_Phase0_FacePlate_Dimensions.txt` (dimension table tracking locked spec numbers)
- `Phase0_Independent_Fab_Package/` (v0.2, 2026-09-08) — SOP, BOM, sims
- DittoBot_Phase0_Aluminum_FacePlate_Package_v0.1.txt — aluminum plate package (offline package, not in this repo)
- `tools/phase0_estimate.py` — public estimate script (Maxwell-style force paper + basic I²R thermal), updated 2026-11-21 to current Ø6 mm NdFeB numbers; labeled estimate only

---

## Success tests (locked)

1. **Snap** — 34.6 N axial at 0.5 mm gap on mild steel; off-axis and 60 °C still holds.
2. **Soft-dock** — ≥ 90 % capture at ≤ 2.5 mm lateral, ±7° angular; insertion ≤ 5 N.
3. **Hard-lock** — ≥ 95 % with all three pins seated.
4. **Shear** — ≥ 40 N through pins without plate yield. Simulated 5 028 N.
5. **Release** — magnet-pull retention ≥ 1.8 N via Option A sliding pin.
6. **Thermal** — 1.25 A through the contact bus ≥ 10 min. Log plate temp. 41 °C skin cap.
7. **Cycles** — 2 000 dock / undock on pins + sliding pin + contacts.

---

## Recommended checks (before full stack-up)

**Intentional relief (design-side insurance)**
- Sliding-pin bore: Ø2.0 mm nominal; verify roundness and finish before assembly.
- Pin bores: drill 0.05 mm oversize with the option to ream to final fit. A slightly loose pin that you bond in place beats a hole you can't clean up.
- Magnet pocket: blind depth 0.75 mm nominal; verify with depth micrometer through the opening before pressing. A pocket 0.1 mm shallow is a press-fit disaster; 0.1 mm deep just means the magnet sits proud and you sand it flush.

**Metrology sequence (article one)**
1. **Pin-bore true position** — CMM if available; otherwise a dowel pin of bore diameter plus a digital caliper. Catch a 0.5 mm offset before assembly.
2. **Blind pocket depth** — depth micrometer through the magnet opening, before any press. Log the number.
3. **Plate flatness** — surface plate and indicator, ≤ 0.10 mm target (loosened from 0.05 mm on 2026-11-21 after Monte Carlo showed 37.5% failure rate at 0.05 on 1 mm plate). A warped plate still kills soft-dock capture, but 0.10 is what a real shop can hit.
4. **Contact wipe** — 0.30–0.50 mm of travel on each pogo pair. Too little and you get intermittent; too much and you bend pins.
5. **Sliding-pin fit** — verify smooth travel and retention ≥ 1.8 N on a coupon before installing in the article.

**Why it matters:** simulation assumes perfect geometry. Real parts have burrs, epoxy creeps, and fab houses drill off-center. The relief and metrology close the cheapest failure modes before they cost you a plate.

---

## What is not in this file

- 25 mm cube envelope, Ø8.2 pocket, NdFeB disc Ø6.0×2–3 mm residual (coil release-only), DRV8871, axial pin, potting
- Retired 20 mm 4×EPM face (superseded 2026-11-21)
- Dual-cam face (superseded 2026-11-23b — `docs/GATE5_SUPERSEDED.md`)
- Community Enhancement Suites (optional skins, sensors, credit hooks — zero impact on these criteria)
- Native STEP/IGES, KiCad PCB, FEMM project (honest gaps)
- Companion / V2.0 language
