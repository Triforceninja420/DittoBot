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
| 2 | Phase 0 face size: brief and sim say 20 mm; PHASE0/LOCKS said "30 mm committed" | PHASE0 and LOCKS now commit the face at 20 mm. **Geometry not changed:** the CAD, fab drawing, and PHASE0 geometry tables still dimension 30 × 30 mm (file `cad/voxel_cell_phase0_30mm_dualcam.scad`, cams at (8,8)/(22,22)). Re-dimensioning is pending Craig. | [33c0670](https://github.com/Triforceninja420/DittoBot/commit/33c0670266f02a4cbd441127a4637f07df95420f) |
| 3 | Pins/material: PHASE0 body said 2 pins and 6061-T6; sim and CAD use 3 pins and 7075-T6 | PHASE0 body now says 3 pins and 7075-T6. The 5 028 N figure is labelled as the earlier 2-pin simulation. | [433b9c0](https://github.com/Triforceninja420/DittoBot/commit/433b9c070b2d5e8d339c54d5791ec8c0e523fd12) |
| 4 | LOCKS rule against Phase 0 numbers in 25 mm files | LOCKS now carries an explicit exception for this file (Craig's brief, 2026-11-23). | The commit that adds this table |

How this file uses the sources:

- The Phase 0 docking-face protocol (contacts, pins, ridge/chamfer, spring, gates) is called "the face" below. Face dimensions are read from `cad/voxel_cell_phase0_30mm_dualcam.scad` (rev 2026-11-23) as they stand. Nothing here re-dimensions the face, so any figure tied to 30 × 30 geometry (for example, corner mounts at ±12.80) must be re-checked when the CAD moves to 20 mm.
- The 25 mm cell core supplies the magnet pocket (Ø8.2 × 4.0, locked), the Nd disc hold, the release coil, and the DRV8871.
- This is a **mapping** document, allowed under the LOCKS exception. It does not change the numbers in the 25 mm cell files.

---

## 1. `LAT_OFFSET_SIGMA_MM = 0.55` → alignment, machining, and assembly stack-up

### 1.1 What the number means physically

`lat` is the residual lateral offset between the mating faces at the moment the pins engage, after the chamfer and ridges have done their capture work. The sim draws it as |N(0, 0.55 mm)|. So the hardware has to deliver a **1σ lateral placement error of ≤ 0.55 mm** at pin engagement, summed over every contributor.

- Gate: 1.5 mm ÷ 0.55 mm = **2.73σ**.
- Two-sided normal tail beyond 2.73σ ≈ 0.64 %, about 639 per 100k.
- That accounts for most of the 702 locked T3 fails. The rest are shear-tail fails, about 63.
- The velocity gate (5σ) contributes about 0.

**Consequence:** at this σ the lat gate is the T3 driver. Every 0.01 mm of σ taken out of the budget below buys margin. Every 0.01 mm added costs roughly 50–60 fails per 100k. That figure is an analytic estimate, not a re-run.

### 1.2 Worked RSS budget (1σ, mm)

Contributors are independent and combined root-sum-square. Values are **proposed** allocations for first articles. Each must be confirmed by first-article metrology (§5).

| # | Contributor | Physical source | Allocation (1σ) | Var share |
| :- | :--- | :--- | -: | -: |
| A | Approach placement | Positioning of the approaching module (manipulator, rail, or hand jig) at pin engagement. This is the residual after chamfer/ridge capture, not raw approach error. | 0.42 | 66.8 % |
| B | Face-to-cell mount | Face plate on the 25 mm cell via 4× Ø1.70 corner holes at (±12.80, ±12.80) with M1.4/M1.6 screws. Clearance float is 0.05–0.15 mm radial. Dowel or shoulder screws are recommended. | 0.20 | 15.1 % |
| C | Cell envelope machining | 25 mm cube face datum → face-plate seat. Wall 1.6 mm. Machined or high-res printed, ±0.15 mm. | 0.15 | 8.5 % |
| D | Disc centering in Ø8.2 pocket | Ø6.0 disc in Ø8.2 pocket leaves 1.10 mm radial annulus, so the disc **must** be centered by the coil bobbin, not the pocket wall. Bobbin ID/OD ±0.05; coaxiality to pocket ≤ 0.10. Magnetic center offset biases capture. | 0.12 | 5.5 % |
| E | Pin-bore true position | Face plate pin bores (Ø1.85 for Ø1.80 pins). CNC true position ≤ Ø0.10, so about 0.05 radial 1σ. | 0.05 | 0.9 % |
| F | Pin/receptacle clearance | 25 mm cell receptacle is +0.15 mm radial over the pin (`voxel_cell.scad`). Uniform ±0.15 gives σ = 0.15/√3. | 0.087 | 2.8 % |
| G | Plate flatness / tilt | Flatness ≤ 0.10 mm (PHASE0 lock) → lateral walk at the pin tip under seat. | 0.03 | 0.3 % |
| H | Thermal growth | 7075-T6, α ≈ 23.6 µm/m·K, 15 mm half-span, ΔT 20 K → 7 µm max, ≈ 0.004 1σ | 0.004 | ~0 % |
| | **RSS total** | √(Σ σ²) = √0.2642 | **0.514** | 100 % |
| | **Budget** | `LAT_OFFSET_SIGMA_MM` | **0.55** | |
| | **Reserve** | √(0.55² − 0.514²) | **0.196 (1σ)** | |

Reading the budget:

- **A dominates (two-thirds of variance).** Machining is not the problem. Approach placement is. That is why the chamfer/ridge capture (§1.3) and the approach-control path (§2) carry the gate.
- **B is the largest fixable assembly term.** Screw-clearance float can be replaced by 2× Ø1.0 mm dowels (proposed, TBD on fit in the 30 mm face corners) or shoulder screws. That drops B to about 0.05 and the RSS to about 0.47 mm.
- **D is specific to this cell.** With Ø6.0 Nd in a Ø8.2 pocket, an un-bobbined disc can sit up to 1.10 mm off center. That alone would blow the budget. The bobbin (or a potted centering sleeve) is a **required** centering feature.
- If any measured contributor comes in over its allocation, the reserve (0.196 1σ) absorbs it first. Past that, the sim's locked σ is no longer representative of the hardware.

### 1.3 Capture geometry (ridge 1.0 × 1.0, chamfer 1.0)

In the sim, ridge and chamfer subtract up to 0.65 mm of effective offset (0.3 + 0.15 + 0.2 per mm, capped at 1.0 mm each) before `OFFSET_DEGRADATION` applies. Hardware tolerances that keep that benefit real (**proposed**):

| Feature | Nominal (CAD) | Tolerance (proposed) | Why |
| :--- | :--- | :--- | :--- |
| Side ridge width | 1.00 mm | ±0.05 | Sets centering contact width |
| Side ridge height | 1.00 mm | ±0.05 | Below 0.95 mm it loses tilted-approach capture |
| Edge chamfer | 1.00 mm × 45° | ±0.10, angle ±1° | Lead-in for the 2.5 mm T1 window |
| Ridge-to-pin-bore position | from CAD | ≤ 0.05 true position | Ridge must center the pins, not just the plate |

---

## 2. `VEL_SIGMA_M_S = 0.10` and the 0.5 m/s gate → approach-velocity control

### 2.1 What the numbers mean

`vel` is the closing speed at first face contact, drawn as |N(0, 0.10 m/s)|.

- Mean |v| = σ·√(2/π) = **0.080 m/s**.
- The gate 0.5 m/s is **5σ**, about 0.06 trials per 100k, so velocity almost never fails T3 at this σ.
- In the shear model, `VEL_DEGRADATION = 2.0` costs 2.0 N of raw shear per m/s. That is 1.0 N at the gate and 0.16 N at the mean.

**Hardware requirement:** contact velocity distribution with **1σ ≤ 0.10 m/s** and a hard ceiling of **0.5 m/s**.

### 2.2 Kinetic energy to absorb

KE = ½ m v²:

| Module mass | 0.10 m/s | 0.22 m/s | 0.50 m/s (gate) |
| :--- | -: | -: | -: |
| 9.2 g (Phase 0 module, PHASE0.md) | 0.05 mJ | 0.22 mJ | 1.15 mJ |
| 25 g (25 mm cell, **TBD** — weigh it) | 0.13 mJ | 0.61 mJ | 3.13 mJ |

Even at the gate this is small compared with the 17 mJ cam-release budget. The 5 N seating spring alone stops a 25 g cell from 0.5 m/s in about 0.6 mm (KE ÷ F). Velocity control is about **seating consistency and pin entry**, not crash protection.

### 2.3 Control stack (proposed)

| Layer | Hardware element | Spec (proposed) |
| :--- | :--- | :--- |
| Motion profile | Trapezoidal or S-curve approach on whatever moves the module (bench rail, manipulator, or neighbour actuator) | Cruise speed TBD. **Terminal creep zone: last 3.0 mm at commanded 0.05 m/s.** Abort/retry if measured speed exceeds 0.25 m/s inside the creep zone. |
| Passive damper 1 | Seating spring (§3) | 5.00 N at seated length; absorbs the KE in §2.2 over ≤ 1 mm |
| Passive damper 2 | **Eddy braking from coil short.** Drive DRV8871 IN1 = IN2 = 1 (brake: both low-side FETs on) during approach so the coil around the Nd disc is shorted | Gives free velocity-proportional damping. Phase 0 T13 measured order: 0.5 N at 0.1 m/s on the 30 mm stack. 25 mm value TBD. Zero standby power; the coil stays release-only (no hold current). |
| Optional damper | Elastomer bumper pad at the face perimeter (material TBD) | Only if measured σ > 0.10 m/s after the above |
| Sensing (in loop) | Hall sensor on the receiving face (PHASE0 electrical already has "LOCK switch / hall → GP14") reads the approaching Nd field. dB/dt gives proximity rate in the last few mm. Optional ToF range sensor (part TBD) for the far approach. | Velocity estimate update ≥ 1 kHz in the creep zone |
| Sensing (lab truth) | See §5: laser displacement sensor or high-speed camera | Resolution ≤ 0.01 m/s |

---

## 3. Spring 5.00 N ± 0.25 N (1σ) → physical spring spec

### 3.1 Requirement from the sim

`spr ~ N(5.00, 0.25)`. ±3σ = **±0.75 N (±15 %)**. `SPRING_BENEFIT = 0.15` gives +0.75 N of raw shear at nominal. The T3 forensic score penalizes force below 5.0 N. PHASE0 role: keep faces seated square during mating; it is **not** the shear structure.

### 3.2 Spring spec (proposed)

| Property | Spec (proposed) | Rationale |
| :--- | :--- | :--- |
| Type | 4× helical compression springs at the face perimeter, 90° apart (CAD shows a perimeter ring representation at r ≈ 14.5 mm). Alternative: one perimeter wave spring. | Even, square seating; no single-point tilt |
| Total force at seated (working) length | **5.00 N** (1.25 N each) | Sim nominal |
| Force tolerance at seated length | **±10 % per spring** at a specified length (precision class, e.g. DIN EN 15800 grade 1 or equivalent), 100 % force-checked and sorted | ±10 % as 3σ gives σ ≈ 0.17 N for the set, inside 0.25 |
| Total rate k | **1.0 N/mm** (0.25 N/mm each) | Low rate keeps force insensitive to seat-height error: σ_h 0.05 mm → 0.05 N |
| Preload | Seated deflection 5.0 mm from free length | 5.0 N = 1.0 N/mm × 5.0 mm |
| Working travel | **1.0 mm** (first contact → seated; matches the 1.0 mm ridge/chamfer depth) | Force rises from 4.0 N at first contact to 5.0 N seated |
| Contact wipe | Inside the working travel: 0.30–0.50 mm pogo wipe (PHASE0) | Pogos are not counted in the 5.00 N. Measure their preload separately and add it to the seating budget (TBD). |
| Material | **Non-magnetic: phosphor bronze or beryllium copper (preferred).** 316 stainless acceptable if measured stray pull from the Nd disc ≤ 0.05 N. **No music wire or carbon steel** (ferromagnetic next to the Nd disc biases force and capture). | Magnetic neutrality near the hold disc |
| Wire Ø / coil OD / free length | **TBD** from spring maker against the rate and space; must fit the cell wall zone (25 mm cube, 1.6 mm wall) | Not invented here |
| Life | ≥ 2 000 cycles (T5), stress ≤ 45 % of tensile (proposed). Relaxation ≤ 2 % after 2 000 cycles. | Spring must not drift below 4.75 N (−1σ) over life |

### 3.3 Combined force spread check

σ_total = √(0.17² (maker tolerance) + 0.05² (seat height) + 0.05² (relaxation, TBD)) ≈ **0.18 N ≤ 0.25 N**. Margin is held for pogo-preload variation.

---

## 4. 40 N shear bar → physical shear/latch requirement with safety factor

### 4.1 What the sim checks

Gate: `shear_eff ≥ 40 N`, where `shear_eff = (shear − 2.0·vel − 0.6·max(0, lat − capture) + 0.15·spr) × 2/3`. Per the sim docstring, the 2/3 pin factor is **load distribution, not added strength**. The 72.8 N mean (7075-T6) stands alone.

| Quantity | Value | Derivation |
| :--- | -: | :--- |
| Raw shear mean / σ | 72.8 N / 4.0 N | `T3_SHEAR_MU`, `T3_SHEAR_SIGMA` |
| Nominal `shear_eff` | **48.9 N** | (72.8 − 2.0·0.080 + 0.15·5.0) × 2/3 |
| Margin to 40 N bar | 8.9 N = **3.3σ** of effective shear | σ_eff = 4.0 × 2/3 = 2.67 N |
| Raw shear needed at worst in-gate condition (lat 1.5, vel 0.5, spring 5.0) | **60.8 N** | 40 × 3/2 + 2.0·0.5 + 0.6·(1.5 − 0.65) − 0.75 |
| Raw-shear −3σ floor | **60.8 N** | 72.8 − 3 × 4.0. Lines up with the worst-case need, so the 4.0 N σ is the tightest allowable. |
| Mean margin over bar | **72.8 / 40 = 1.82** | |

### 4.2 Physical requirement (proposed)

| Item | Requirement (proposed) |
| :--- | :--- |
| Minimum docked shear (gate) | **≥ 40 N** in the face plane, any direction, without pin disengagement, slip > 0.10 mm, or plate yield |
| Design target (joint, mean) | **≥ 72.8 N** first-slip/disengagement load, with lot σ ≤ 4.0 N |
| Design floor (−3σ) | ≥ 60.8 N, so the worst in-window condition still clears 40 N effective |
| Safety factor | **SF 1.8 on mean** (72.8/40), **SF ≥ 1.5 at −3σ** (60.8/40). Proof load **50 N** (1.25 × 40), held 10 s, no permanent set > 0.02 mm (proposed). |
| Human-contact interrupt | Separate 35 N rule (LOCKS companion gate 2). Not the 40 N structural bar; do not merge them. |

### 4.3 Load sharing: 3 pins + Nd hold

- **Pins carry the shear.** Three hardened-steel Ø1.80 mm pins (CAD positions (2, 1), (−2, −1), (0, 2.5)), engagement 3.0 mm (face). The 25 mm cell receptacle is Ø1.8 pin / 2.8 mm engagement per `voxel_cell.scad`.
  - Equal share: 40 N / 3 = 13.3 N per pin.
  - With a clearance-driven unequal-share factor of 1.5 (proposed, worst pin): **20 N per pin**.
- **Metal is not the limit.**
  - Pin shear area π·0.9² = 2.54 mm² → 7.9 MPa at 20 N. Hardened steel has hundreds of MPa of shear capacity.
  - 7075-T6 bearing in a 1.0 mm plate: 1.8 mm² → 11 MPa at 20 N.
  - PHASE0's 5 028 N simulated pin shear is consistent with this.
  - The 72.8 N joint figure is therefore the **retention/disengagement** capacity: pins walking out, retraction-actuator back-drive, or ridge ride-up under prying. It is not metal shear. **This interpretation is proposed** and must be confirmed by the T3 pull test (§5).
- **Retention requirements that follow (proposed):**
  - Retraction actuator must not back-drive under 60.8 N lateral load: the pin-tip radial force must hold position.
  - Pin engagement ≥ 2.5 mm at worst stack.
  - Pin/bore radial clearance ≤ 0.15 mm (F in §1.2). More clearance worsens both share factor and lat.
- **Nd disc hold.** The Ø6.0 × 2–3 mm Nd disc provides axial clamp, which keeps pins fully engaged and faces seated.
  - Its friction contribution to shear is μ·F_axial. With μ ≈ 0.35 (the friction value PHASE0 uses) and an axial hold TBD (expected well below the 34.6 N of the Ø6 × 6 Phase 0 magnet), friction is a few N at most.
  - **No credit is taken for magnetic friction in the 40 N requirement.** Pins carry 100 %. Magnetic and spring friction are margin only.
- **Seating spring** adds 0.15 N/N per the sim (0.75 N at 5.00 N). Margin only.

### 4.4 Material

Face plate **7075-T6** (CAD rev 2026-11-23; sim mean raised 52 → 72.8 for it). Verify with mill cert and a hardness spot-check (§5). 6061-T6 parts are not valid T3 articles under the locked sim.

---

## 4b. I_release coil-sizing note (25 mm cell, DRV8871)

**Rule:** the coil goes around the Ø6.0 × 2–3 mm Nd disc and is **release-only**. Hold is the disc. Static coil current after any pulse is 0. Size for I_release, never for hold.

### Method

1. **Winding window.** Pocket Ø8.2, disc Ø6.0 → 1.10 mm radial annulus. Allow 0.10 mm bobbin wall → **1.0 mm radial × ≈ 2.5 mm high** (disc 2–3 mm; pocket 4.0 deep).
2. **Turns that fit.** AWG 36: bare 0.127 mm, insulated ≈ 0.14 mm (TBD per wire datasheet). That gives ~7 layers × ~17 turns ≈ 120 ideal, ≈ 95 at 0.8 practical fill. Wound 2-in-hand (2× AWG 36 parallel, COIL_REVISION): **≈ 48 turns per strand (proposed; count and publish the real number).**
3. **Resistance.**
   - Mean turn Ø ≈ 7.2 mm → 22.6 mm per turn.
   - 48 turns ≈ 1.09 m per strand × 1.36 Ω/m ≈ 1.48 Ω per strand.
   - **≈ 0.74 Ω parallel** (estimate; measure cold R).
4. **Driver limits (DRV8871 datasheet).**
   - VM 6.5–45 V. Repo rule: bank ≤ 42 V, 36 V nominal.
   - Peak rating 3.6 A. Repo ILIM setpoint ~3.0 A (BOM).
   - Current chopping: I_TRIP = 64 kV / R_ILIM (kΩ), V_ILIM 59–69 kV, R_ILIM ≥ 15 kΩ.
   - Rds(on) HS+LS ≈ 0.57 Ω typ, 0.68 Ω max.
5. **Set I_release at the measured release point, capped at 80 % of the ILIM floor.**
   - With R_ILIM = 21.5 kΩ (1 %), I_TRIP is 2.72–3.24 A (nominal 2.98 A). The design cap is **I_release ≤ 2.4 A (proposed)**, so chopping never truncates the release pulse.
   - If ILIM regulation is wanted as the release current itself, R_ILIM = 64/2.4 ≈ 26.7 kΩ → 2.18–2.61 A.
   - At 36 V into ≈ 1.4 Ω (coil + FETs), the unrestricted current is far above ILIM, so the DRV8871 chopper sets the current.
6. **Field check (paper).**
   - NI = 48 × 2.4 ≈ 115 A-turns.
   - Finite short-solenoid center field B ≈ μ0·NI/√(ℓ² + D²) = 1.2566e-6 × 115 / √(2.5² + 7.2²) mm ≈ **0.019 T**.
   - That is a small fraction of an N-grade disc's surface field. **On paper the coil alone cannot cancel the Nd hold.** This matches the PHASE0 finding (coil ≈ 0.7 % of coercivity). Release relies on the coil weakening the bond, plus pin retraction, plus the 5 N spring and cam/cone separation. I_release is therefore defined as **the current at which the measured OFF force drops below the available separation force (spring + mechanical assist), at the intended gap**, not as a full-cancellation current. If no current ≤ 2.4 A reaches that, the release path needs the mechanical assist (TBD for the 25 mm cell). Do not raise hold current to compensate.
7. **Pulse energy and thermal.**
   - At 2.4 A in 0.74 Ω: 4.3 W.
   - Firmware default 100 ms (`firmware/pulse_driver.cpp`) → 0.43 J per pulse into ≈ 0.25 g of copper → ≈ 4 K adiabatic rise per pulse.
   - The coil inductance is small (µH-class, TBD), so 10–20 ms should reach peak. Set from measured time-to-peak (proposed).
   - The thermal governor stays mandatory.
8. **Tie to T4 (1.25 A bus).**
   - T4 is the **face contact bus**: ≥ 1.25 A continuous for 10 min, no throttle. The sim draws capability ~N(1.5, 0.1), so the gate sits at 2.5σ, ~0.6 % fails.
   - The release pulse (up to ~2.4–3.0 A) must come from the **local pulse bank**, never directly through the face contacts.
   - Bank recharge from the bus is limited to **≤ 0.25 A (proposed)**, so pass-through load + recharge stays ≤ 1.25 A.
   - Each 12 V power contact path is rated to carry the full 1.25 A alone (proposed), so one bad contact cannot fail T4.

Fill the 25 mm measurement card (turns, cold R, peak I, I_release, ON N, OFF N) before any claim.

---

## 5. Sensors and lab fixtures per gate

Sample sizes use zero-failure success-run testing at 95 % confidence: n = ln(0.05)/ln(R).

| Gate / param | Fixture | Sensors / instruments | Procedure and pass criterion |
| :--- | :--- | :--- | :--- |
| **T1** soft-dock ≤ 2.5 mm / ≤ 7° (σ 0.65 mm / 1.6°) | XY micrometer stage (0.01 mm) + tilt goniometer (±10°) holding the passive face; linear rail for the active module | Stage micrometers; Hall/lock sensor for capture; optional camera | Approach at set offsets 0–2.5 mm and angles 0–7°. Pass: capture at 2.5 mm / 7° corner. ≥ 90 % → **n = 29 at the corner with 0 misses** (95 % conf). Separately log the natural offset/angle distribution → σ ≤ 0.65 mm / 1.6°. |
| **T2** hard-lock ≥ 95 % (sim p 0.994) | Same rail | Per-pin seat sensor (Hall or micro-switch on each of 3 pins, TBD), continuity on the sense contact | All 3 pins seated after each dock. ≥ 95 % → **n = 59 with 0 misses**. |
| **T3** shear ≥ 40 N | Shear pull rig: docked pair clamped, lateral pull through a load cell on a lead-screw stage. Offset preset by the XY stage. | Load cell ≥ 100 N range, ≤ 0.1 N resolution; dial indicator or LVDT for slip (0.01 mm) | Pull in 0°/90°/180°/270°. Pass: ≥ 40 N with slip ≤ 0.10 mm and no yield. Proof 50 N, 10 s. Destructive pulls on ≥ 10 coupons to estimate mean ≥ 72.8 N, σ ≤ 4.0 N. |
| `LAT_OFFSET_SIGMA_MM` 0.55 | First-article metrology + dock-repeat test | CMM or optical comparator (contributors B–G); witness-mark or camera measurement of offset at pin engagement over ≥ 30 docks | Measured contributors ≤ allocations (§1.2); measured lat σ ≤ 0.55 mm; no dock with lat > 1.5 mm |
| `VEL_SIGMA_M_S` 0.10 / gate 0.5 | Approach rail with the production motion profile | Laser displacement sensor (≥ 5 kHz) or high-speed camera (≥ 1 000 fps) with scale; resolution ≤ 0.01 m/s | Over ≥ 30 docks: σ of contact velocity ≤ 0.10 m/s, max < 0.5 m/s |
| Spring 5.00 ± 0.25 N | Spring force tester / force gauge on a height stand | Force gauge ≤ 0.01 N resolution; height gauge | 100 % check each spring at seated length (±10 %). Set sum 5.00 N; lot σ ≤ 0.25 N. Re-check after 2 000 cycles (≤ 2 % loss). |
| Ridge / chamfer 1.0 | Metrology | Optical comparator / height gauge | Per §1.3 tolerances |
| `PIN_COUNT` 3, engagement | Metrology + assembly check | Depth micrometer, go/no-go pin gauges | 3 pins present, engagement ≥ 2.5 mm, bore Ø1.85 (pin 1.80) |
| 7075-T6 | Incoming inspection | Mill cert; hardness tester | Cert matches 7075-T6; hardness within T6 range (cert value) |
| `VEL_DEGRADATION`, `OFFSET_DEGRADATION`, `SPRING_BENEFIT` | T3 rig on a designed grid: vel {0.05, 0.25, 0.5} m/s × lat {0, 0.75, 1.5} mm × spring {4.5, 5.0, 5.5} N | As T3 | Fit slopes by regression. Sim values (2.0 N per m/s, 0.6 N/mm, 0.15 N/N) are the bar; report measured slopes. **Do not edit the sim from this test without Craig's sign-off.** |
| **T4** 1.25 A × 10 min (μ 1.5, σ 0.1) | Docked pair on a 12 V bench supply into an electronic load through the face contacts | Shunt + INA219 (PHASE0 electrical); TMP117 + NTC on plate; thermocouple at contacts; 4-wire contact-drop measurement | Pass: 1.25 A for ≥ 10 min, no throttle, skin ≤ 41 °C. Also step to 1.5 A to confirm the capability mean. |
| **T5** 2 000 cycles (μ 2 500, σ 150) | Cycle rig: rail + actuator, automatic dock/lock/release, counter | Cycle counter; per-cycle lock sensor log; contact resistance every 100 cycles; T3 proof at 0/500/1 000/1 500/2 000 | Pass: 2 000 cycles, all locks seated, T3 proof passes at each checkpoint, cam tip wear logged (µm). 3 000 stays a stretch goal. |
| I_release (25 mm cell) | Mild-steel plate + force scale (MIN_PARTS item 7) on a gap shim | Scope + current probe; force scale | Sweep pulse current 0.5–2.4 A; record OFF force vs I; I_release = first current meeting §4b step 6 |

---

## 6. Summary table

| Parameter | Sim value | Hardware element | Tolerance / spec | How to verify |
| :--- | :--- | :--- | :--- | :--- |
| `T1_OFFSET_SIGMA_MM` | 0.65 mm (gate 2.5 mm = 3.85σ) | Chamfer + ridges + approach placement | Natural soft-dock offset σ ≤ 0.65 mm | XY stage capture test, n = 29 at corner |
| `T1_ANGLE_SIGMA_DEG` | 1.6° (gate 7° = 4.4σ) | Chamfer, ridge height, approach fixture | Angle σ ≤ 1.6° | Goniometer capture test |
| `T2_LOCK_P` | 0.994 (gate ≥ 95 %) | 3 pins + retraction actuators + receptacles | All 3 seat every dock | Per-pin seat sensors, n = 59 |
| `T3_SHEAR_MU` / `T3_SHEAR_SIGMA` | 72.8 / 4.0 N | 7075-T6 plate, pin retention | Joint mean ≥ 72.8 N, σ ≤ 4.0 N, −3σ ≥ 60.8 N | Destructive pulls, ≥ 10 coupons |
| T3 shear bar | 40 N on `shear_eff` | Docked joint (pins carry 100 %) | SF 1.82 mean, ≥ 1.5 at −3σ; proof 50 N | Shear rig, 4 directions |
| `LAT_OFFSET_SIGMA_MM` | 0.55 mm | Approach + mount + cell + disc centering + pins | RSS 0.514 mm (A 0.42, B 0.20, C 0.15, D 0.12, E 0.05, F 0.087, G 0.03, H 0.004) | CMM per contributor + 30-dock offset log |
| `T3_LAT_LIMIT_MM` | 1.5 mm (2.73σ) | Same | No dock with lat > 1.5 mm | Offset log |
| `VEL_SIGMA_M_S` | 0.10 m/s | Motion profile + creep zone + eddy brake + spring | Contact velocity σ ≤ 0.10 m/s; creep 0.05 m/s commanded, last 3 mm | Laser displacement / high-speed video |
| `T3_VEL_LIMIT_MS` | 0.5 m/s (5σ) | Abort logic at 0.25 m/s in creep zone | Max contact velocity < 0.5 m/s | Same |
| Spring nominal / `SPRING_SIGMA_N` | 5.00 N / 0.25 N | 4× non-magnetic compression springs | k 1.0 N/mm total, 5 mm preload, 1.0 mm working travel, ±10 % per spring at length | Force tester, 100 % |
| `RIDGE_W_MM` / `RIDGE_H_MM` | 1.0 / 1.0 mm | Face side ridges | ±0.05 mm | Optical comparator |
| `CHAMFER_MM` | 1.0 mm | Face edge chamfer | ±0.10 mm, 45° ±1° | Optical comparator |
| `PIN_COUNT` / `PIN_LOAD_FACTOR` | 3 / 2/3 | Ø1.80 hardened pins in Ø1.85 bores | Engagement ≥ 2.5 mm; worst pin ≤ 1.5× equal share | Gauges; strain or pull test |
| `VEL_DEGRADATION` | 2.0 N per m/s | Impact on seating/pin entry | Measured slope ≤ 2.0 | T3 grid regression |
| `OFFSET_DEGRADATION` | 0.6 N per mm | Uncaptured offset → pin preload | Measured slope ≤ 0.6 | T3 grid regression |
| `SPRING_BENEFIT` | 0.15 N per N | Seating friction | Measured slope ≥ 0.15 (margin only) | T3 grid regression |
| `T4_CURRENT_MU` / σ / gate | 1.5 / 0.1 / 1.25 A | Face power contacts, bus, fuse | 1.25 A × 10 min, ≤ 41 °C skin; each power path carries 1.25 A alone; coil pulse from local bank, recharge ≤ 0.25 A | INA219 + TMP117/NTC soak |
| `T5_CYCLES_MU` / σ / gate | 2 500 / 150 / 2 000 | Pins, cams, contacts, spring, tip epoxy | 2 000 cycles; spring loss ≤ 2 % | Cycle rig with checkpoints |
| Release coil (25 mm cell) | — (not a sim param) | Coil around Ø6 Nd disc, DRV8871 | ≈ 48 turns 2-in-hand AWG 36 (est.), ≈ 0.74 Ω, I_release ≤ 2.4 A, R_ILIM 21.5 kΩ (2.72–3.24 A trip) | OFF-force vs current sweep; measurement card |
| Result | all-pass 98.04 %, T3 99.30 %, 702 fails | — | Locked; hardware must reproduce these input distributions to claim them | Fill MEASUREMENT_CARD |

Simulation numbers are the bar, not the credit.
