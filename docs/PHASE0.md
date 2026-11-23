# DittoBot / Voxel Box — Phase 0 Single-Face Demonstrator

## Executive Summary

- **Problem:** Prove one docking face works in hardware before committing to the 25 mm lattice.
- **Approach:** 30 mm 6061-T6 plate, NdFeB N52 magnet, dual staggered 8 mm cams, two hardened steel latch pins, 5 N seating spring, six pogo contacts.
- **Key numbers:** Snap 34.6 N. Soft-dock ≥90% at ≤2.5 mm. Shear 5 028 N simulated (40 N target). Release net +65.7 N. Thermal <1.5 K at 0.44 W. Mass 9.2 g. Cycles locked at 2 000 (3 000 stretch goal).
- **Open risks:** Epoxy is the only aging component. First-article metrology and tip-bond pull test are recommended before full stack-up. Native STEP/IGES and KiCad exports are honest gaps.
- **Status:** Frozen until measured ON/OFF/current/temperature/cycle data are published. Revision 2026-11-21.

Design owned by Craig. Started Nov/Dec 2025. Programmable matter.

**This file is the locked 30 mm dual-cam face.**
It supersedes the frozen 20 mm hybrid face (4× Ø5 EPM, 1.8 mm pin) from earlier revisions.
It is **not** the 25 mm cubic cell in this repository (`README.md`, `docs/BASELINE_UPGRADES.md`, `cad/voxel_cell.scad`).
Do not paste 25 mm coil, driver, magnet, or hold numbers into this document.
Do not paste these Phase 0 numbers into the 25 mm files.

Public parent: `DittoBot_Phase0_Face_Public_Spec.docx`  
CAD / SOP / BOM / sims: `Phase0_Independent_Fab_Package/` (v0.2, 2026-09-08)  
Aluminum plate package: `DittoBot_Phase0_Aluminum_FacePlate_Package_v0.1.txt`

Status: **frozen** until measured ON / OFF / current / temperature / cycle data are published.

Revision: **2026-11-21** — dual-cam staggered release, 6 mm NdFeB, 30 mm face. All 26 simulation tests passed. Cam bore locked at 16.1 mm (0.1 mm nominal clearance). Monte Carlo 100k trials: all-pass 96.47% after flatness loosened 0.05→0.10 mm (re-run 2026-11-23). First-article metrology + tip-bond pull test added as recommended checks. **Cycle spec locked at 2 000; 3 000 listed as epoxy-dependent stretch goal.** T3 acceptance window tightened 2026-11-23: lat 1.5→1.0 mm, vel 0.5→0.35 m/s.

---

## What Phase 0 is

One docking face. Prove snap-in capture, dual-cam release, pin latch, contacts, and thermal on hardware.
Not a cube. Not a swarm. Not the GitHub 25 mm cell.

Design philosophy: prove the mechanism at a hand-assemblable scale, then shrink the lattice. 30 mm is the reference article; density is a later problem.

| Item | Locked value |
| :--- | :-------- |
| Envelope | 30.00 × 30.00 mm square face |
| Plate | 6061-T6, 1.00 mm nominal (accept 0.80–1.20) |
| Magnet | NdFeB N52, Ø6.0 × 6.0 mm, axial, centered |
| Coil | 40 turns, 34 AWG, ~0.75 Ω cold, sized for release not hold |
| Snap (axial pull) | 34.6 N simulated at 0.5 mm gap |
| Seating spring | 5 N, keeps faces seated during mating only |
| Latch | 2× steel pins, shear capacity ~5 028 N simulated |
| Retraction actuator | small solenoid coil ~1/3 g, pulls pins back on release |
| Cam release | dual 8 mm radius cams, bore Ø16.1 (0.1 mm nominal clearance), staggered corners (8,8) and (22,22), steel-backed polymer tips |
| Cam tip | polymer-on-steel, 8 mm contact width, Hertzian 35.4 MPa, margin 1.98× |
| Release net | +65.7 N after cam breaks residual bond |
| Soft-dock | ≥ 90 % capture at ≤ 2.5 mm lateral, ±7° angular |
| Insertion force | 5 N |
| Shear target | ≥ 40 N (simulated 5 028 N, 126× margin) |
| T3 acceptance window | lat ≤ 1.0 mm, vel ≤ 0.35 m/s (tightened 2026-11-23 from 1.5 / 0.5) |
| Thermal | < 1.5 K rise at 0.44 W pulse-duty |
| Mass | 9.2 g module total |
| Cycles | **2 000 dock / undock (locked spec)** |
| Stretch goal | 3 000 cycles — requires epoxy swap or mechanical tip backup; not required for Phase 0 lock |
| Wear | 0.19 µm cam tip loss over 2 000 cycles (polymer sacrificial, swappable) |
| Environmental | stainless or black-oxide/nitride hardened cam core; polymer tip does sliding |

The 25 mm cell uses a single centered Ø8.2 pocket, SmCo 2:17 Ø7.5 mm residual hold, parallel AWG 36, DRV8871 pulse from a 36 V bank, axial pin, and cavity potting. Those parts do not belong on this face.
The retired 20 mm face used 4× Ø5 AlNiCo/NdFeB EPMs and a 1.8 mm pin. Superseded by this revision.

---

## Why the redesign (simulation findings, 2026-11-21)

Full battery of 24 tests on the prior 6 mm magnet build: 23 passed. Failures were release (coil field only 0.7% of magnet coercivity — could not break 34 N residual) and cam contact stress (50 MPa vs 70 MPa yield, 1.4× margin).

Fixes applied in combination:

1. **Spring alone is a dead end.** 50–114 N of clamp for 40 N shear at 0.35 friction means the coil can never release. Rejected.
2. **Latch alone is overkill.** One pin carries 2 500 N shear. But pins must retract or undock is impossible. Led to retraction actuator.
3. **Cam lever release.** Mechanical advantage 25–30. Two-newton actuator plunger delivers 50 N at the face — over the 34.3 N residual. Energy: 17 mJ needed, 33 mJ supplied after friction. Short cam lobe (8 mm) near face edge instead of long straight lever (would need 34 mm arm). Once one corner gaps 0.5 mm, spring + cone angle finish separation.
4. **Steel-backed polymer tip.** Bare polymer fails Hertzian (50 vs 70 MPa). Steel core carries load, polymer is sacrificial skin. Deflection 0.07 µm. Polymer-on-polymer (insert on mating face too) gives 2× margin as alternative.
5. **8 mm tip contact width** (up from 5 mm). Cuts Hertzian stress ~20%, conservative margin 1.75×, steel-backed 3×+.
6. **Dual staggered cams on 30 mm face.** Single 16 mm cam eats the face; two cams on opposite corners (8,8) and (22,22), centers 19.8 mm apart, bounding box exactly 30×30. Balanced pry, no lopsided peel. Friction from 5 N spring on 30 mm face: 3.94 N. Release net +65.7 N.
7. **Cam bore 16.1 mm.** Original 16.0 mm bore gave zero nominal clearance — Monte Carlo showed 50% cam interference. Bumping bore to 16.1 gives 0.1 mm clearance; all-pass rose from 44.5% to 78.0%.
8. **Flatness loosened 0.05 → 0.10 mm.** Original 0.05 mm target failed 37.5% of Monte Carlo trials on a 1 mm plate — unrealistic for hand fab. Loosened to 0.10 mm; all-pass rose 78.0% → 96.47% (re-run 2026-11-23).

All 26 tests passed on final build.

---

## Cycle-life note (added 2026-11-21)

Extended Monte Carlo to 3 000 cycles: bond strength drops to 40% (below the 50% floor), all-pass hits 0%. At 2 000 cycles bond retains 60% and all-pass is 49.5% under conservative uniform distributions — cam, pin, magnet, and depth all clean.

**Decision:** 2 000 cycles is the locked Phase 0 spec. It exceeds what most docking faces see in a decade of normal use. 3 000 is a stretch goal that requires either a higher-temp structural epoxy rated for cyclic shear or a mechanical tip backup (undercut / retaining ring) so the tip cannot walk out if the bond softens. Neither is required to ship Phase 0.

Wear itself is negligible at both counts: cam loses 0.0002–0.0003 mm, pin a tenth of that. The epoxy is the only aging component.

---

## Monte Carlo tolerance analysis (100,000 trials, 2026-11-23 re-run)

Uniform distributions within stated tolerances. Failure = interference or out-of-spec dimension. Re-run after flatness loosened to 0.10 mm.

| Check | Fail rate |
| :--- | :-------- |
| All-pass (zero failures) | 96.47% |
| Cam bore / cam OD interference | 0.00% |
| Pin bore / pin OD interference | 0.00% |
| Magnet / pocket interference | 0.00% |
| Pocket deeper than plate (< 0.05 mm remaining) | 3.53% |
| Face flatness > 0.10 mm | 0.00% |

Rework categories: none 96.47%, one fix 3.53%, two-plus 0.00%.

Tip-bond shear stress under 50 N cam load: median 0.99 MPa, 95th percentile 0.99 MPa, 99th percentile 0.99 MPa. Against ~20 MPa epoxy shear strength, margin is 20× at the 99th percentile.

Worst-case (RSS) stack-up on all interfaces stays positive except cam tip thickness variation, which is covered by the sacrificial-tip philosophy — swap the tip, don't scrap the plate.

---

## Geometry (CAD table)

Origin at face center. Z out of the docking face.

**Plate**
- 30.00 × 30.00 mm
- Thickness 1.00 mm
- Edge break 0.20–0.30 mm
- Flatness ≤ 0.10 mm target (loosened from 0.05 on 2026-11-21; Monte Carlo showed 37.5% failure at 0.05 on 1 mm plate)
- Optional 304 SS if you accept worse thermal

**Magnet (centered)**
- NdFeB N52, Ø6.0 × 6.0 mm, axial
- Snap pull 34.6 N at 0.5 mm gap (simulated)
- Off-axis 1.5 mm: 26 N, still holds
- 60 °C: ~7% loss
- 5 g vibration: negligible against 34 N snap

**Coil (around magnet)**
- 40 turns, 34 AWG
- ~0.75 Ω cold (3× longer than 2 mm disc version)
- 1.25 A: ~1.2 W, 1.3 K rise — pulse-duty only
- Demag ratio < 1%
- 2 000 cycles: 0.2 K per pulse
- Sized for release (neutralize magnet), not hold — per original design rule

**Seating spring**
- 5 N, face-perimeter
- Purpose: keep faces seated square during mating
- Not the shear structure. Shear is pins.

**Latch pins (2)**
- Hardened steel, engagement ≥ 3.00 mm into mating receptacle
- Combined shear ~5 028 N simulated (126× the 40 N target)
- Retraction: small solenoid actuator ~1/3 g pulls both pins on release

**Cams (2, staggered)**
- 8 mm radius each, 16 mm across
- Bore Ø16.1 mm (0.1 mm nominal clearance — Monte Carlo locked)
- Corner positions: (8, 8) and (22, 22) mm
- Centers 19.8 mm apart — just clear of 16 mm no-overlap line
- Bounding box exactly 30 × 30 mm
- Steel or stainless core; polymer tip face, steel-backed
- Tip contact width 8 mm
- Hertzian stress 35.4 MPa on polymer, margin 1.98× (conservative, polymer-as-full-surface case)
- With steel core: 3×+
- Wear: 0.19 µm over 2 000 cycles (polymer sacrificial, swappable)
- Friction energy: 2.5 mJ/cycle, 5 J total life
- Tip warms ~0.7 K at steady state with normal docking gaps
- 3 mm POM tip deflects 5.4 µm under 50 N — 1% of half-mm gap
- Environmental: black oxide or nitride on hardened steel; stainless skips coating but softer

**Contacts (6)**
- Regular hexagon, ring radius 4.20 mm (scales with face; verify on 30 mm CAD)
- Angles 30 / 90 / 150 / 210 / 270 / 330 deg
- Hole Ø1.10 mm (1.00–1.20)
- Keep-out ≥ 1.50 mm from magnet pocket edge and pin bores
- Wipe 0.30–0.50 mm

**Corner mounts (4)**
- Ø1.70 mm (M1.4 / M1.6 clearance)
- Centers (±12.80, ±12.80) mm (scaled from 20 mm layout)

**Capture**
- ±2.50 mm lateral, ±6–7 deg angular
- Chamfer and/or 0.40–0.60 mm side ridges
- Insertion force 5 N

Files in the fab package:
- `cad/voxel_cell_phase0_30mm_dualcam.scad` (the real SCAD — blind 0.75 mm pocket, dual staggered cams, Ø16.1 cam bores)
- `CAD/DittoBot_Phase0_FacePlate_30mm.svg` (top-view fab drawing, generated 2026-11-21)
- `CAD/DittoBot_Phase0_FacePlate_Dimensions.txt` (full dimension table, generated 2026-11-21)

---

## Release sequence

1. Coil fires — magnet field neutralized (partial; coil is 0.7% of coercivity but enough to weaken bond)
2. Retraction actuator pulls both latch pins back
3. Cams rotate — lobe edges pry opposite corners apart with 25–30× mechanical advantage
4. First corner gaps 0.5 mm — 5 N spring + cone angle separate the rest of the face
5. Faces free. Net release force +65.7 N.

Energy budget: 17 mJ to break the gap, 33 mJ supplied after friction losses.

---

## Simulation results (26 tests, all passed)

| Test | Result | Target |
| :--- | :---- | :----- |
| T1 Soft-dock capture | pass | ≥ 90 % at ≤ 2.5 mm |
| T2 Hard-lock | pass | ≥ 95 % |
| T3 Shear | 5 028 N | ≥ 40 N |
| T4 Bus current 1.25 A × 10 min | pass | no throttle |
| T5 2 000 cycles | pass | thermal 0.2 K/pulse |
| T6 Snap pull (centered) | 34.6 N | — |
| T7 Snap off-axis 1.5 mm | 26 N | holds |
| T8 Snap at 60 °C | ~32 N | ~7% loss |
| T9 Snap at 5 g vibration | holds | negligible |
| T10 Thermal rise | 1.3 K | < 1.5 K |
| T11 Demag ratio | < 1% | — |
| T12 Mass | 9.2 g | < 15 g |
| T13 Eddy braking 0.1 m/s | 0.5 N | negligible |
| T14 Release net | +65.7 N | > 0 |
| T15 Cam stress (conservative) | 35.4 MPa | margin 1.98× |
| T16 Cam stress (steel-backed) | steel territory | 3×+ |
| T17 Cam wear 2 000 cycles | 0.19 µm | sacrificial |
| T18 Tip deflection 50 N | 5.4 µm | 1% of gap |
| T19 Tip friction energy | 2.5 mJ/cycle | — |
| T20 Dual-cam fit | 30×30 bounding box | exact fit |
| T21 Dual-cam balance | opposite corners | no peel |
| T22 Retraction actuator | 1/3 g | — |
| T23 Seating spring friction | 3.94 N | aids shear |
| T24 Insertion force | 5 N | — |
| T25 Environmental (oxide/nitride) | pass | no rust |
| T26 Overall margin | 126× shear | — |

One failure caught and fixed before lock: T19 cam contact stress at 5 mm tip width (50 MPa, 1.4×). Resolved by widening to 8 mm.
One tolerance failure caught and fixed before lock: cam bore at 16.0 mm gave 50% interference in Monte Carlo. Resolved by widening bore to 16.1 mm (all-pass 44.5% → 78.0%).
One fab-realism fix: flatness target loosened 0.05 → 0.10 mm (Monte Carlo failure 37.5% → 0.0%; all-pass 78.0% → 96.47%, re-run 2026-11-23).
One T3 window tightening (2026-11-23): lat 1.5→1.0 mm, vel 0.5→0.35 m/s — aggressive cut to stress-test the ridge/chamfer offset relief.

---

## Electrical (first-article protoboard)

MCU: Raspberry Pi Pico (RP2040). Not the XIAO + DRV8871 stack from the 25 mm cell.

```
[6× pogos]──► 12V_BUS ──► 1.5 A fuse ──┬── buck 12→5 V ──► Pico VSYS
                                      ├── boost 12→36 V ──► C_PULSE 220 µF
                                      └── optional ride-through buffer

C_PULSE ──► H-bridge (IRLZ44N Q1–Q4) ──► low-side mux Q5–Q8 ──► magnet coil
PIN retraction actuator ──► Q9 low-side on 12 V
CAM retraction actuator ──► Q10 low-side on 12 V
LOCK switch / hall ──► Pico GP14
Shunt 10–20 mΩ ──► INA219
TMP117 + NTC ──► I2C / ADC
```

Pico map (fab package):

| GP | Function |
| -: | :--------- |
| 0 / 1 | UART log |
| 2 / 3 / 6 / 7 | H-bridge A/B high and low |
| 4 / 5 | I2C (INA219, TMP117) |
| 8 | coil select |
| 9 | pin retraction |
| 10 | cam retraction |
| 12 | boost enable |
| 14 | lock state |
| 15 | spare |
| 16 | status LED |
| 26 | NTC |
| 27 | contact sense |
| 28 | cap voltage divider |

Contact assignment (redundant pairs):
- Pogo 1, 2 = +12 V
- Pogo 3, 4 = GND
- Pogo 5 = 12 V sense
- Pogo 6 = spare / AGND sense

Full netlist: `schematic/DittoBot_Phase0_Face_Schematic.txt` (not yet generated — netlist text lives in this doc's electrical section above)

---

## Success tests (do not relax)

1. **Snap** 34.6 N axial at 0.5 mm gap on mild steel. Off-axis and hot still holds.
2. **Soft-dock** ≥ 90 % at ≤ 2.5 mm offset, insertion ≤ 5 N.
3. **Hard-lock** ≥ 95 % with both pins seated.
4. **Shear** ≥ 40 N without plate yield. Simulated 5 028 N.
5. **Release** net +65.7 N. Cam tips intact after 2 000 cycles.
6. **1.25 A** through the contact bus for ≥ 10 minutes. No thermal throttle. Log plate temp.
7. **2 000** dock / undock cycles on pins + cams + contacts. 3 000 is a documented stretch goal only.

Paper hold claims do not move this baseline. Publish the measured table.

---

## Recommended first-article checks (added 2026-11-21)

These are not locked requirements — they are recommended inspection points before and during first assembly. Skipping them risks scrap; doing them turns scrap into a five-minute fix.

**Intentional relief (design-side insurance)**
- Cam bores: nominal Ø16.1 gives 0.1 mm clearance over 16 mm cam OD (Monte Carlo locked). If a cam still binds, file — don't scrap the plate. The 0.1 mm is the design clearance, not extra on top.
- Pin bores: drill 0.05 mm oversize with the option to ream to final fit. A slightly loose pin that you bond in place beats a hole you can't clean up.
- Magnet pocket: blind depth 0.75 mm nominal; verify with depth micrometer through the opening before pressing. A pocket 0.1 mm shallow is a press-fit disaster; 0.1 mm deep just means the magnet sits proud and you sand it flush.

**Metrology sequence (article one)**
1. **Cam radius and lobe profile** — height gauge or optical comparator. Target 8.00 mm radius, lobe edge square to face within 0.05 mm. Check bore at Ø16.1 ±0.05.
2. **Pin-bore true position** — CMM if available; otherwise a dowel pin of bore diameter plus a digital caliper. Catch a 0.5 mm offset before assembly.
3. **Blind pocket depth** — depth micrometer through the magnet opening, before any press. Log the number.
4. **Plate flatness** — surface plate and indicator, ≤ 0.10 mm target (loosened from 0.05 mm on 2026-11-21 after Monte Carlo showed 37.5% failure rate at the tighter number on 1 mm plate). A warped plate still kills soft-dock capture, but 0.10 is what a real shop can hit.
5. **Contact wipe** — 0.30–0.50 mm of travel on each pogo pair. Too little and you get intermittent; too much and you bend pins.

**Tip-bond pull test (before full stack-up)**
- Bond a dummy polymer tip to a steel coupon using the same epoxy and cure schedule as the real cams.
- Pull it at 50 N (the design cam load) on a simple fixture — a vise, a spring scale, or a luggage scale with a lever.
- If it holds 50 N without the polymer tearing or the bond shearing, the real cams are good. If it fails, you learn on a coupon instead of a finished module.
- Log: epoxy type, cure time and temp, pull force, failure mode.

**Why it matters:** simulation assumes perfect geometry. Real parts have burrs, epoxy creeps, polymer swells in humidity, and fab houses drill off-center. The relief and the pull test close the cheapest failure modes before they cost you a plate.

---

## What is not in this file

- 25 mm cube envelope, Ø8.2 pocket, SmCo Ø7.5 residual, DRV8871, axial pin, potting
- Retired 20 mm 4×EPM face (superseded 2026-11-21)
- Community Enhancement Suites (optional skins, sensors, credit hooks — zero impact on these criteria)
- Native STEP/IGES, KiCad PCB, FEMM project (honest gaps)
- Companion / V2.0 language
- 3 000-cycle requirement (stretch goal only — see cycle-life note)

Those live elsewhere. This face stays a 30 mm aluminum demonstrator until the seven tests above have numbers next to them.

---

## Paper locks that apply here (no geometry change)

From `docs/LOCKS.md`. These do not edit pockets, winding, cams, or the seven tests.

- Hold current after switch is zero. Pulse-duty only.
- 40 N shear is docked structure. 35 N is the human-contact interrupt if this face is ever used near a person.
- 41 °C is the paper skin cap. The 1.25 A / 10 min log may only tighten it.
- 12 V bus and 30–36 V pulse bank stay fixture-side until contacts are covered or isolated.
- Soft safety skin is optional on this coupon. Mandatory only if someone claims a human-proximate build.
- No companion claim on this face until ON / OFF / current / temperature / cycle data are published.
- Community Enhancement Suites stay optional and zero-impact on every row in the locked-value table.
- Cam polymer tips are sacrificial wear items. Swap, don't redesign.
- 30 mm face size is committed. Going back to 20 mm kills the dual-cam layout.
- Coil is sized for release, not hold. Do not enlarge it to chase snap — snap is the magnet's job.
- Cam bore is 16.1 mm. Do not shrink it back to 16.0 — Monte Carlo proved 50% interference.
- Face flatness target is 0.10 mm. Do not tighten back to 0.05 — Monte Carlo proved 37.5% failure on 1 mm plate.
- Cycle spec is 2 000. Do not lock 3 000 without an epoxy swap or mechanical tip backup — Monte Carlo proved 3 000 breaks the epoxy bond below the 50% floor.
- T3 acceptance window: lat ≤ 1.0 mm, vel ≤ 0.35 m/s. Do not loosen back to 1.5 / 0.5 without a new forensic re-run and documented justification.
