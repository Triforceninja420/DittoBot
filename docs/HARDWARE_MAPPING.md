# Phase 0 hardware mapping — sim parameters and gates → 25 mm cell hardware

Design owned by Craig. Added 2026-11-23. Paper only — credit follows measured data.

This file maps every parameter and gate in `sims/phase0_monte_carlo.py` (DB-P0-FACE-TP-001 Rev A) to physical hardware, tolerances, and lab checks for the 25 mm GitHub cell core.

**No sim number is changed here.** It adds no CAD, firmware, or BOM edits. Values marked **(proposed)** or **TBD** are design proposals, not locks. Where a proposed value conflicts with a lock in `docs/LOCKS.md`, the lock wins until Craig re-locks.

---

## 0. Locked inputs (from `sims/phase0_monte_carlo.py` at commit 74ded02)

| Constant | Value | Meaning in the sim |
| :--- | :--- | :--- |
| `N_TRIALS` / `SEED` / `FORENSIC_SEED` | 100 000 / 7 / 13 | Sim bookkeeping, no hardware |
| `T1_OFFSET_SIGMA_MM` / `T1_ANGLE_SIGMA_DEG` | 0.65 mm / 1.6° | Soft-dock misalignment; gate ≤ 2.5 mm and ≤ 7° |
| `T2_LOCK_P` | 0.994 | Hard-lock probability; target ≥ 95 % |
| `T3_SHEAR_MU`, `T3_SHEAR_SIGMA` | 72.8 N, 4.0 N | Joint shear capacity (7075-T6) |
| T3 shear bar | 40 N | Evaluated on `shear_eff` |
| `VEL_SIGMA_M_S` | 0.10 m/s | Contact velocity, half-normal |
| `LAT_OFFSET_SIGMA_MM` | 0.55 mm | Lateral offset at latch, half-normal |
| `SPRING_SIGMA_N` (nominal 5.00 N) | 0.25 N | Seating-spring force spread |
| `T3_LAT_LIMIT_MM` / `T3_VEL_LIMIT_MS` | 1.5 mm / 0.5 m/s | T3 acceptance window |
| `RIDGE_W_MM` / `RIDGE_H_MM` / `CHAMFER_MM` | 1.0 / 1.0 / 1.0 mm | Capture geometry |
| `PIN_COUNT` / `PIN_LOAD_FACTOR` | 3 / 2/3 | Load distribution, not added strength |
| `VEL_DEGRADATION` | 2.0 N per m/s | Shear lost per unit contact velocity |
| `OFFSET_DEGRADATION` | 0.6 N per mm | Shear lost per mm of uncaptured offset |
| `SPRING_BENEFIT` | 0.15 N per N | Shear gained per N of seating force |
| `T4_CURRENT_MU`, `T4_CURRENT_SIGMA` | 1.5 A, 0.1 A | Bus capability; gate ≥ 1.25 A for 10 min, no throttle |
| `T5_CYCLES_MU`, `T5_CYCLES_SIGMA` | 2 500, 150 | Cycle life; gate ≥ 2 000 |
| Result (100k) | all-pass 98.04 %, T3 99.30 %, 702 T3 fails | Locked baseline |

T3 model, as written in the sim:

```
ridge_benefit   = 0.3·min(lat, 1.0) + 0.15·min(lat, 1.0)
chamfer_benefit = 0.2·min(lat, 1.0)
shear_eff = (shear − 2.0·vel − 0.6·max(0, lat − ridge_benefit − chamfer_benefit) + 0.15·spr) × 2/3
T3 pass  ⇔  lat ≤ 1.5 mm  AND  vel ≤ 0.5 m/s  AND  shear_eff ≥ 40 N
```

## 0.1 Scope note: source conflicts — all four resolved (2026-11-23)

When this file was first committed (aae92a7), Craig's 2026-11-23 brief clashed with older repo docs in four places. Craig confirmed the brief as the source of truth, and all four clashes are now resolved in the docs:

| # | Clash | Resolution | Commit |
| :- | :--- | :--- | :--- |
| 1 | 25 mm cell magnet: brief says Nd disc Ø6.0 × 2–3 mm; docs said SmCo 2:17 Ø7.5 × 3.0 and called Ø6 Nd superseded | Docs now state the Nd disc Ø6.0 × 2–3 mm hold in the Ø8.2 × 4.0 pocket, coil around the disc release-only (sized for I_release), Alnico off this cell. Updated BUILD, DESIGN, COIL_REVISION, MIN_PARTS, MEASUREMENT_CARD (25 mm card), BASELINE_UPGRADES, PAPER_STATUS, README, LOCKS. | [a627841](https://github.com/Triforceninja420/DittoBot/commit/a6278416cf573302c0a77d1feb345b52abc08cef) |
| 2 | Phase 0 face size: brief and sim say 20 mm; PHASE0/LOCKS said "30 mm committed" | PHASE0 and LOCKS now commit the face at 20 mm. **Geometry changed:** CAD redesign landed 2026-11-23 in `cad/voxel_cell_phase0_20mm.scad`; faceplate SVG `CAD/DittoBot_Phase0_FacePlate_20mm.svg`; dimension table `CAD/DittoBot_Phase0_FacePlate_Dimensions.txt`. All 30 × 30 geometry (cams at (8,8)/(22,22), corner mounts ±12.80) is superseded. | [86cb726](https://github.com/Triforceninja420/DittoBot/commit/86cb726) |
| 3 | Pins/material: PHASE0 body said 2 pins and 6061-T6; sim and CAD use 3 pins and 7075-T6 | PHASE0 body now says 3 pins and 7075-T6. The 5 028 N figure is labelled as the earlier 2-pin simulation. | [433b9c0](https://github.com/Triforceninja420/DittoBot/commit/433b9c070b2d5e8d339c54d5791ec8c0e523fd12) |
| 4 | LOCKS rule against Phase 0 numbers in 25 mm files | LOCKS now carries an explicit exception for this file (Craig's brief, 2026-11-23). | The commit that adds this table |

How this file uses the sources:

- The Phase 0 docking-face protocol (contacts, pins, ridge/chamfer, spring, gates) is called "the face" below. Face dimensions are read from `cad/voxel_cell_phase0_20mm.scad` (rev 2026-11-23, 20 mm redesign) as they stand. Nothing here re-dimensions the face.
- The 25 mm cell core supplies the magnet pocket (Ø8.2 × 4.0, locked), the Nd disc hold, the release coil, and the DRV8871.
- This is a **mapping** document, allowed under the LOCKS exception. It does not change the numbers in the 25 mm cell files.

---

## 1. `LAT_OFFSET_SIGMA_MM = 0.55` → alignment, machining, and assembly stack-up

### 1.1 What the number means physically

`lat` is the residual lateral offset between the mating faces at the moment the pins engage, after the chamfer and ridges have done their capture work. The sim draws it as |N(0, 0.55 mm)|. So the hardware has to deliver a **1σ lateral placement error of ≤ 0.55 mm** at pin engagement, summed over every contributor.

- Gate: 1.5 mm ÷ 0.55 mm = **2.73σ**.
- Two-sided normal tail beyond 2.73σ ≈ 0.63% per side, ~1.27% two-sided — consistent with the sim's T3 fail rate of 0.70% (702/100k).

### 1.2 Contributor stack (RSS)

| Contributor | 1σ (mm) | Source / note |
| :---- | :---- | :---- |
| A. Approach placement | 0.42 | Motion controller + rail + fiducial alignment; the dominant term |
| B. Mount / plate flatness | 0.20 | 7075-T6 plate flatness ≤ 0.10 mm per face, two faces |
| C. Pin-bore true position | 0.15 | Drill/ream tolerance on Ø1.85 bores |
| D. Pin OD tolerance | 0.12 | Ø1.80 pin, ±0.01 |
| E. Ridge/chamfer geometry | 0.05 | Optical comparator ±0.05 |
| F. Cell centering in pocket | 0.087 | Nd disc Ø6.0 in Ø8.2 pocket, +0.10 on diameter |
| G. Spring seating variation | 0.03 | 4× springs, 1.0 N/mm, 5 mm preload |
| H. Thermal expansion (lab, 20 °C) | 0.004 | 7075-T6 α ≈ 23 µm/m·K over ±5 °C |
| **RSS total** | **0.514** | ≤ 0.55 mm gate — **passes** |

Contributor A (0.42 mm) is the single largest term. Everything else combined is 0.28 mm RSS. If approach placement can be tightened to 0.30 mm, total RSS drops to ~0.42 mm — 3.6σ on the 1.5 mm gate.

---

## 2. `VEL_SIGMA_M_S = 0.10` → motion profile and eddy brake

Contact velocity at latch is half-normal |N(0, 0.10)|. Gate: max < 0.5 m/s (5σ). Abort logic trips at 0.25 m/s in the creep zone (last 3 mm), commanded 0.05 m/s.

**Passive damper 2 — eddy braking from coil short.** Drive DRV8871 IN1 = IN2 = 1 (brake: both low-side FETs on) during approach. The shorted coil acts as a velocity-dependent damper on the approaching face. This is a **proposed** technique; verify on the fixture before relying on it. It does not change any sim number.

---

## 3. Spring: 5.00 N nominal, SPRING_SIGMA_N = 0.25 N

4× non-magnetic compression springs (phosphor-bronze or BeCu), 1.0 N/mm combined rate, 5 mm preload, 1.0 mm working travel. ±10% per spring at length. Verify on force tester, 100%.

Spring benefit in the T3 model: +0.15 N shear per N of seating force. At 5.00 N nominal, +0.75 N — margin only, not counted in the 40 N bar.

---

## 4. Shear: T3_SHEAR_MU = 72.8 N, SIGMA = 4.0 N; bar 40 N

7075-T6 plate, pin retention. Joint mean ≥ 72.8 N, σ ≤ 4.0 N, −3σ ≥ 60.8 N. Safety factor 1.82 mean, ≥ 1.5 at −3σ. Proof 50 N × 10 s. Shear rig, 4 directions. Pins carry 100% of the bar; the 5 028 N figure is the earlier 2-pin simulation.

### 4a. Degradation slopes (measured, not sim)

| Slope | Sim value | Hardware check |
| :---- | :---- | :---- |
| VEL_DEGRADATION | 2.0 N per m/s | Measured slope ≤ 2.0 (T3 grid regression) |
| OFFSET_DEGRADATION | 0.6 N per mm | Measured slope ≤ 0.6 (T3 grid regression) |
| SPRING_BENEFIT | 0.15 N per N | Measured slope ≥ 0.15 (margin only) |

---

## 4b. I_release coil sizing (25 mm cell)

The 25 mm cell coil is sized for **release**, not hold. Hold current after switch is zero (LOCKS rule 9). The coil sits around the Ø6.0 × 2–3 mm Nd disc in the Ø8.2 × 4.0 pocket.

- Estimated: ≈ 48 turns 2-in-hand AWG 36, ≈ 0.74 Ω cold
- I_release ≤ 2.4 A, pulse-only, thermal governor gated
- R_ILIM 21.5 kΩ (2.72–3.24 A trip)
- Verify: OFF-force vs current sweep on mild-steel plate + force scale (MIN_PARTS item 7); I_release = first current meeting the §4b step-6 criterion

---

## 5. Lab fixtures

| Check | Fixture | Instrumentation | Method |
| :---- | :---- | :---- | :---- |
| Lateral offset at latch | XY stage + fiducials | Dial indicator / CMM | 30-dock offset log, n ≥ 30 |
| Contact velocity | Motion rail + laser | High-speed video / laser displacement | Creep 0.05 m/s, abort 0.25 m/s, max < 0.5 |
| Spring force | Force tester | Load cell | 100% at length, ±10% |
| Shear | Shear rig, 4 directions | Load cell | ≥ 40 N, slip ≤ 0.10 mm, no yield; proof 50 N × 10 s |
| Thermal soak | Face power contacts + bus | INA219 + TMP117/NTC | 1.25 A × 10 min, ≤ 41 °C skin |
| Cycle life | Cycle rig | Counter + wear log | 2 000 cycles; spring loss ≤ 2%; cam tip wear log |
| I_release (25 mm cell) | Mild-steel plate + force scale (MIN_PARTS item 7) on a gap shim | Scope + current probe; force scale | Sweep pulse current 0.5–2.4 A; record OFF force vs I; I_release = first current meeting §4b step 6 |

---

## 6. Summary table

| Parameter | Sim value | Hardware element | Tolerance / spec | How to verify |
| :---- | :---- | :---- | :---- | :---- |
| `T1_OFFSET_SIGMA_MM` | 0.65 mm (gate 2.5 mm = 3.85σ) | Chamfer + ridges + approach placement | Natural soft-dock offset σ ≤ 0.65 mm | XY stage capture test, n = 29 at corner |
| `T1_ANGLE_SIGMA_DEG` | 1.6° (gate 7° = 4.4σ) | Chamfer, ridge height, approach fixture | Angle σ ≤ 1.6° | Goniometer capture test |
| `T2_LOCK_P` | 0.994 (gate ≥ 95 %) | 3 pins + retraction actuators + receptacles | All 3 seat every dock | Per-pin seat sensors, n = 59 |
| `T3_SHEAR_MU` / `T3_SHEAR_SIGMA` | 72.8 / 4.0 N | 7075-T6 plate, pin retention | Joint mean ≥ 72.8 N, σ ≤ 4.0 N, −3σ ≥ 60.8 N | Destructive pulls, ≥ 10 coupons |
| T3 shear bar | 40 N on `shear_eff` | Docked joint (pins carry 100 %) | SF 1.82 mean, ≥ 1.5 at −3σ; proof 50 N | Shear rig, 4 directions |
| `LAT_OFFSET_SIGMA_MM` | 0.55 mm | Approach + mount + cell + disc centering + pins | RSS 0.514 mm (A 0.42, B 0.20, C 0.15, D 0.12, E 0.05, F 0.087, G 0.03, H 0.004) | CMM per contributor + 30-dock offset log |
| `T3_LAT_LIMIT_MM` | 1.5 mm (2.73σ) | Same | No dock with lat > 1.5 mm | Offset log |
| `VEL_SIGMA_M_S` | 0.10 m/s | Motion profile + creep zone + eddy brake + spring | Contact velocity σ ≤ 0.10 m/s; creep 0.05 m/s commanded, last 3 mm | Laser displacement / high-speed video |
| `T3_VEL_LIMIT_MS` | 0.5 m/s (5σ) | Abort logic at 0.25 m/s in creep zone | Max contact velocity < 0.5 m/s | Same |
| Spring nominal / `SPRING_SIGMA_N` | 5.00 N / 0.25 N | 4× non-magnetic compression springs | k 1.0 N/mm total, 5 mm preload, 1.0 mm working travel, ±10% per spring at length | Force tester, 100% |
| `RIDGE_W_MM` / `RIDGE_H_MM` | 1.0 / 1.0 mm | Face side ridges | ±0.05 mm | Optical comparator |
| `CHAMFER_MM` | 1.0 mm | Face edge chamfer | ±0.10 mm, 45° ±1° | Optical comparator |
| `PIN_COUNT` / `PIN_LOAD_FACTOR` | 3 / 2/3 | Ø1.80 hardened pins in Ø1.85 bores | Engagement ≥ 2.5 mm; worst pin ≤ 1.5× equal share | Gauges; strain or pull test |
| `VEL_DEGRADATION` | 2.0 N per m/s | Impact on seating/pin entry | Measured slope ≤ 2.0 | T3 grid regression |
| `OFFSET_DEGRADATION` | 0.6 N per mm | Uncaptured offset → pin preload | Measured slope ≤ 0.6 | T3 grid regression |
| `SPRING_BENEFIT` | 0.15 N per N | Seating friction | Measured slope ≥ 0.15 (margin only) | T3 grid regression |
| `T4_CURRENT_MU` / σ / gate | 1.5 / 0.1 / 1.25 A | Face power contacts, bus, fuse | 1.25 A × 10 min, ≤ 41 °C skin; each power path carries 1.25 A alone; coil pulse from local bank, recharge ≤ 0.25 A | INA219 + TMP117/NTC soak |
| `T5_CYCLES_MU` / σ / gate | 2 500 / 150 / 2 000 | Pins, cams, contacts, spring, tip epoxy | 2 000 cycles; spring loss ≤ 2% | Cycle rig with checkpoints |
| Release coil (25 mm cell) | — (not a sim param) | Coil around Ø6 Nd disc, DRV8871 | ≈ 48 turns 2-in-hand AWG 36 (est.), ≈ 0.74 Ω, I_release ≤ 2.4 A, R_ILIM 21.5 kΩ (2.72–3.24 A trip) | OFF-force vs current sweep; measurement card |
| Result | all-pass 98.04 %, T3 99.30 %, 702 fails | — | Locked; hardware must reproduce these input distributions to claim them | Fill MEASUREMENT_CARD |

Simulation numbers are the bar, not the credit.
