# DittoBot Phase 0 20 mm fixes — handoff for Craig (rev 2026-11-23b)

**Base:** main `58a87a2cd26b070a26986a5e2f39e3391ef18ad3`. Main was still at this commit at 12:30 PM PT on 2026-11-23.
**Nothing was pushed to GitHub.** No branch, commits or issues were created.
Every file here is the complete file, built on main's raw content (checked byte for byte), ready to commit as is.
`phase0-20mm-fixes.patch` holds the same changes as one `git apply`-able diff against 58a87a2. It was tested with `git apply --check` on a fresh tarball.

No simulation numbers changed: all-pass 98.04 %, T3 99.30 %, 702 T3 fails, LAT_OFFSET_SIGMA 0.55, T3 lat 1.5 mm, vel 0.5 m/s, spring 5.00 N, shear bar 40 N.

## Also delete (not in the handoff folder)
- `CAD/DittoBot_Phase0_FacePlate_20mm.svg` and `CAD/DittoBot_Phase0_FacePlate_Dimensions.txt` are stale duplicates of the old cad/ copies. Delete them with `git rm -r CAD/`.
- `docs/PROTOTYPE_PLAN_25MM.md` is the old `docs/PROTOTYPE_PLAN.md`, renamed and relabeled. `docs/PROTOTYPE_PLAN.md` is a new Phase 0 plan.

## Suggested commits (in order)

1. **cad: Phase 0 through-hole pocket + 2.0 mm backing disc, Option A release pin, no cams**
   Files: `cad/voxel_cell_phase0_20mm.scad`, `cad/DittoBot_Phase0_FacePlate_20mm.svg`, `cad/DittoBot_Phase0_FacePlate_Dimensions.txt`, `tools/phase0_layout_check.py` (new).
   Changes:
   - Ø8.2 through-hole plus a separate backing disc with a 2.0 mm solid back face (OD 10.2 placeholder). The 4.0 mm blind spec is retired for Phase 0.
   - Cams removed. Single Ø2.0 sliding release pin, 3.0 mm travel, bore Ø2.05, at (+6.65, +3.50).
   - Contacts moved to r 6.25 at 50/110/170/230/290/350°. Pins at r 7.45 (73/155/328°). Mounts at (±7, ±7).
   - Capture chamfer 1.0 mm, ridges 1.0 × 1.0 mm. Coil 40 t 34 AWG, about 0.75 Ω, DRV8871.
   - Every feature is ≥ 0.5 mm from every other (worst 0.578 mm).
   Message note: "Gate 5 reframed by Craig (authorized lock change, not a sim tweak)."
2. **docs: Phase 0 specs — gate 5 retention ≥ 1.8 N, 9.2 g mass, through-hole + backing disc, sliding release pin, cams removed**
   Files: `docs/PHASE0.md`, `docs/MEASUREMENT_CARD.md`, `docs/LOCKS.md`, `docs/HARDWARE_MAPPING.md`, `docs/GATE5_SUPERSEDED.md` (new).
   Changes:
   - Gate 5: F_hold ≥ 0.0092 kg × 10 × 9.81 × 2 = 1.805 N → ≥ 1.8 N. The old +65.7 N dual-cam target is marked superseded with a date, not deleted. Authorized by Craig; not a sim tweak.
   - Mass is 9.2 g everywhere. The TBD markers are gone.
   - PHASE0 gets the clearance table, the backing-disc bond pull test (replaces the cam tip-bond test), and `CAD/` → `cad/` paths.
   - Contact ring 6.25; capture 1.0 / 1.0 × 1.0; pin engagement 3.00 design, ≥ 2.5 acceptance.
   - LOCKS: the capacitor-dump/IRLZ44N drive note is replaced with DRV8871.
   - HARDWARE_MAPPING: §0.1 row 2 rewritten; §4b gets a Phase-0-only pocket note (the 25 mm Ø8.2 × 4.0 pocket is unchanged); §5 gets a retention fixture row; the T5 row now reads "release pin" instead of "cams".
3. **docs: propagate Option A / no-cam wording**
   Files:
   - `docs/FIRST_ARTICLE.md`: Phase 0 table, assembly, metrology and thermal 41/36 °C; links now point to PROTOTYPE_PLAN / PROTOTYPE_PLAN_25MM.
   - `docs/SIM_NOTES.md`, `docs/POST_2040_OUTLOOK.md`, `docs/PHASE1.md` (U5), `docs/COMMUNITY_ENHANCEMENT_SUITES.md`, `phase0/README.md`.
   - `tools/phase0_estimate.py`: dated docstring line only; math unchanged.
4. **bom: retarget to Phase 0 20 mm with DigiKey links; 25 mm BOM kept as a later section** — `bom/bom_netlist.txt`
5. **docs: Phase 0 PROTOTYPE_PLAN; move the 25 mm plan to PROTOTYPE_PLAN_25MM.md** — `docs/PROTOTYPE_PLAN.md`, `docs/PROTOTYPE_PLAN_25MM.md`
6. **firmware: Phase 0 header, 41 °C trip / 36 °C clear, NTC divide-by-zero guard, watchdog armed after setup** — `firmware/pulse_driver.cpp`
   - An open, shorted or missing NTC reads as 999 °C, so the governor refuses pulses (fail-safe).
   - The TMP117/INA219 flags are unchanged.
   - Syntax was checked with g++ against stub Arduino headers only; it has not been compiled for the RP2040.
7. **docs: root README becomes a pointer with root-relative links; index the new docs** — `README.md`, `docs/README.md`, plus `git rm -r CAD/`

## Clearance table (`python3 tools/phase0_layout_check.py`, CLEAR = 0.5 mm, Ø shown as O)

Final layout clearance table (min edge-to-edge clearance, CLEAR = 0.5 mm):
| Feature | x | y | Dia | Nearest neighbour | Clearance (mm) | OK |
| :-- | --: | --: | --: | :-- | --: | --: |
| pin bore 1 O1.85 | +2.18 | +7.12 | 1.85 | spring seat 2 O1.20 | 0.69 | yes |
| pin bore 2 O1.85 | -6.75 | +3.15 | 1.85 | contact 3 O1.10 | 0.67 | yes |
| pin bore 3 O1.85 | +6.32 | -3.95 | 1.85 | mount 4 O1.70 | 1.35 | yes |
| contact 1 O1.10 | +4.02 | +4.79 | 1.10 | backing disc OD10.2 (back, placeholder) | 0.60 | yes |
| contact 2 O1.10 | -2.14 | +5.87 | 1.10 | backing disc OD10.2 (back, placeholder) | 0.60 | yes |
| contact 3 O1.10 | -6.16 | +1.08 | 1.10 | spring seat 3 O1.20 | 0.58 | yes |
| contact 4 O1.10 | -4.02 | -4.79 | 1.10 | backing disc OD10.2 (back, placeholder) | 0.60 | yes |
| contact 5 O1.10 | +2.14 | -5.87 | 1.10 | backing disc OD10.2 (back, placeholder) | 0.60 | yes |
| contact 6 O1.10 | +6.16 | -1.08 | 1.10 | spring seat 1 O1.20 | 0.58 | yes |
| release pin bore O2.05 | +6.65 | +3.50 | 2.05 | ridge inner line | 1.32 | yes |
| mount 1 O1.70 | +7.00 | +7.00 | 1.70 | release pin bore O2.05 | 1.64 | yes |
| mount 2 O1.70 | -7.00 | +7.00 | 1.70 | pin bore 2 O1.85 | 2.08 | yes |
| mount 3 O1.70 | -7.00 | -7.00 | 1.70 | plate edge | 2.15 | yes |
| mount 4 O1.70 | +7.00 | -7.00 | 1.70 | pin bore 3 O1.85 | 1.35 | yes |
| spring seat 1 O1.20 | +7.50 | +0.00 | 1.20 | contact 6 O1.10 | 0.58 | yes |
| spring seat 2 O1.20 | +0.00 | +7.50 | 1.20 | pin bore 1 O1.85 | 0.69 | yes |
| spring seat 3 O1.20 | -7.50 | +0.00 | 1.20 | contact 3 O1.10 | 0.58 | yes |
| spring seat 4 O1.20 | -0.00 | -7.50 | 1.20 | ridge inner line | 0.90 | yes |

Worst clearance: 0.578 mm -> PASS

## Locked values changed (all Craig-approved)
- Phase 0 pocket: Ø8.2 × 4.0 blind → Ø8.2 through-hole + backing disc with a 2.0 mm solid back face.
- Dual cams (Ø16.05 bores) removed. Release is now Option A: a Ø2.0 sliding pin with 3.0 mm travel.
- Gate 5: release net +65.7 N → retention ≥ 1.8 N. Mass TBD → 9.2 g.
- Contact ring r 4.20 → 6.25, with new angles. Corner mounts at (±7.00, ±7.00).
- Capture chamfer 0.50 → 1.0. Ridges 0.50 × 0.60 → 1.0 × 1.0. Pin engagement acceptance ≥ 2.5 (3.00 design).
- LOCKS drive note: capacitor dump → DRV8871. Firmware thermal trip 60 → 41 °C (clear at 36 °C).

## Open questions for Craig
1. **Backing-disc OD** is a 10.2 mm placeholder. Contacts 1/2/4/5 have only 0.60 mm margin to it. Also, a through-bored plate cannot keep its own back face, so the "back face" is read as a separate disc. Please confirm that reading.
2. **Release-pin bore** Ø2.05 (+0.05) is my choice, copied from the latch-pin convention. How the pin is actuated (manual, solenoid, or the retraction actuator) is not defined.
3. **"Option A" is not defined in the repo** for a sliding pin. The 25 mm axial pin is a hard-lock, not a release pin.
4. **Pin load balance:** the pins sit at 73/155/328°, not 120°. A symmetric layout gave only 0.52 mm worst clearance.
5. **Numbers from the cam era** (cam tip wear 0.19 µm; Hertzian 35.4 MPa / 1.98×) are kept as history. Should they be re-simmed for the sliding pin?
6. **Pin engagement** is 3.00 mm into the mating part, but the plate is only 1.0 mm thick. What is the receptacle depth?
7. **Backing-disc bond pull test load:** 50 N, carried over from the cam test. Please confirm.
8. **Mill-Max 0906** has a Ø1.07 mm plunger in a Ø1.10 contact hole. That is tight, so check the fit.
9. **BOM:** P1, P2, P8, P9 and P11–P16 are "supplier TBD". DigiKey blocks scripted fetches, so its links were confirmed only through search-index copies on 2026-11-23. Open each one before ordering.
10. **25 mm tables** in FIRST_ARTICLE / PROTOTYPE_PLAN_25MM still list "net +65.7 N" and "cam tip wear" as bars. These were left untouched because they are not Phase 0.
11. **`docs/COIL_REVISION.md` line 5** says "dual-cam face". It is a dated record and was left as is.

## Draft issues (titles + bodies)

### Issue 1 — Phase 0: cams deferred to Option A / 25 mm; gate 5 reframed as retention ≥ 1.8 N
Ø16.05 dual cams cannot fit the 20 mm face with ≥ 0.5 mm clearance. Ø16.05 / Ø12.05 / Ø10.05 miss by about 12.95 / 8.12 / 5.71 mm against the backing disc. The largest feasible radius is about 1.9 mm in a full-layout search (2.66 mm absolute ceiling), which is too small to carry gate 5.
Craig's decision: drop cams for Phase 0 and defer them to Option A / the 25 mm cell. Retention comes from the magnet's pull. Release is a single sliding pin, Ø2.0 mm with 3.0 mm travel, that only breaks contact.
New gate 5 (authorized, not a sim tweak): F_hold ≥ m × N × 9.81 × SF = 0.0092 kg × 10 × 9.81 × 2 = 1.805 N → **≥ 1.8 N**. The old "+65.7 N via dual-cam" target is superseded 2026-11-23 and kept in `docs/GATE5_SUPERSEDED.md`.
To do: re-sim the cam-era wear and stress numbers, define the release-pin actuation, and define "Option A".

### Issue 2 — Phase 0 magnet pocket: Ø8.2 through-hole + 2.0 mm backing disc
The 4.0 mm blind pocket was deeper than the 1.0 mm plate. The new design is an Ø8.2 through-hole closed by a separate solid backing disc with a 2.0 mm back face, which acts as the heat spreader.
- The recess depth is the disc thickness − 1.0 mm.
- The OD is a 10.2 mm placeholder and still needs a decision. The 0.60 mm contact margin depends on it.
- Interpretation flag: a through-bored plate cannot keep its own back face.
- The 25 mm Ø8.2 × 4.0 pocket is unchanged.

### Issue 3 — Remaining contradictions
- 25 mm tables still use the +65.7 N and cam-wear bars.
- COIL_REVISION has a dated "dual-cam" line.
- `sims/phase0_monte_carlo.py` docstring mentions cam bore clearance (sim file, left untouched).
- Pins are not 120° symmetric.
- 3.00 mm pin engagement vs the 1.0 mm plate.
- The Mill-Max plunger fit in the Ø1.10 hole.
- The backing-disc bond test load.

### Issue 4 — BOM retargeted to Phase 0 20 mm
DigiKey links for DRV8871DDAR, TMP117AIDRVR, INA219AIDR, NTC B57891S0103F008 and Mill-Max 0906. TI DRV8871 samples are noted. The plate, magnet, pins, springs, fasteners, release pin, shim, potting, XIAO and LDO still have no DigiKey/Mouser link ("supplier TBD"). The 25 mm BOM is kept as a later section.

### Issue 5 — PROTOTYPE_PLAN rewritten for Phase 0; 25 mm plan moved to PROTOTYPE_PLAN_25MM.md
The new plan covers gates 1–7 with HARDWARE_MAPPING §5 fixtures, including retention ≥ 1.8 N, and a log template.

### Issue 6 — Firmware: Phase 0 header, 41/36 °C governor, NTC guard, watchdog false trip
- The header said 25 mm. The thermal trip was 60 °C against the 41 °C skin cap.
- The NTC divided by zero, or took log(0), when the sensor was absent.
- The watchdog tripped after setup's 3 s USB wait.
All four are fixed. Still needs an RP2040 build and bench test.

### Issue 7 — Root README duplicated docs/README.md (broken links); stale CAD/ duplicates
The root README is now a pointer with root-relative links. The CAD/ duplicates still need deleting.

### Issue 8 — Value reconciliation (capture, engagement, coil R, drive)
- Capture: chamfer 1.0, ridges 1.0 × 1.0, ±2.50.
- Engagement: 3.00 design, ≥ 2.5 acceptance.
- Coil: Phase 0 about 0.75 Ω (40 t 34 AWG); the 25 mm cell is about 0.74 Ω (2× AWG 36).
- Drive: DRV8871, replacing the capacitor-dump note.
All taken from HARDWARE_MAPPING / FIRST_ARTICLE.
