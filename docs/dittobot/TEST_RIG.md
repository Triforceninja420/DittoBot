# Test Rig — Phase 0 bench spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**. This is a bench and procedure paper mapped to existing Phase 0 gates. It is not a measured result, and it does not invent pass bars.

Version is **v0.1** because this is a brand-new document, consistent with the other new top-level papers in `docs/dittobot/`. It is written in the same template style as the v0.2 per-mode specs. It is not a v0.2 revision of a prior test-rig doc in this folder.

Phase: Phase 0 bench only. The article is the **20 mm** sliding-pin face in [PHASE0.md](../PHASE0.md), test plan `DB-P0-FACE-TP-001`. This file does not retune locked values, rewrite [PHASE0.md](../PHASE0.md) or [LOCKS.md](../LOCKS.md), or mix in 25 mm coil / driver / hold numbers except where [HARDWARE_MAPPING.md](../HARDWARE_MAPPING.md) already maps a check.

Paper until measured. Credit follows data.

---

## Inheritance

The locked 25 mm cell core is unchanged and is **not** the article on this bench, except as a separate coupon under HARDWARE_MAPPING:

- 25 mm cube envelope
- Centered Ø8.2 × 4.0 mm pocket (locked)
- Nd disc Ø6.0 × 2–3 mm hold; coil around the disc, release-only (Alnico off this cell)
- DRV8871, 12 V, pulse-only
- Axial pin hard-lock
- Full cavity potting and face coatings
- XIAO RP2040, 3.3 V; 36–48 V pulse bank

The Phase 0 article itself is the 20 × 20 mm, 7075-T6 face in [PHASE0.md](../PHASE0.md). Two stacks stay unmixed. Phase 0 tests the 20 mm face. The 25 mm cube is the cell body spec.

---

## What this bench is for

Prove one docking face on hardware: capture, hard-lock, shear, contact-bus soak, and cycle life, using the **existing** Phase 0 protocol IDs and bars. The face partner is a second 20 mm face or a fixture plate that presents mating receptacles, pin bores, and six contacts. See [BILL_OF_MATERIALS.md](BILL_OF_MATERIALS.md) for the article parts list.

Craig's brief listed T1–T5 as soft-dock, hard-lock, 40 N shear, 1.25 A × 10 min, and 2 000 cycles. Those map to **P0-T1…P0-T5** in [PHASE1.md §6.1](../PHASE1.md#61-inherited-gates-unchanged) (gates from `DB-P0-FACE-TP-001`). [PHASE0.md](../PHASE0.md) itself numbers a longer locked list as **Success tests 1–7** (it also locks Snap and Release). This file uses the repo's IDs and wording. Differences are reported in the mapping table. **No new bars are invented.** Equipment range and resolution figures that are not in the repo are labeled **ASSUMED**.

---

## Equipment

Items already named in [HARDWARE_MAPPING.md §5](../HARDWARE_MAPPING.md#5-lab-fixtures), [PHASE0.md](../PHASE0.md), [MIN_PARTS.md](../MIN_PARTS.md), or [PROTOTYPE_PLAN_25MM.md](../PROTOTYPE_PLAN_25MM.md) are cited from those files. Models, ranges, and resolutions not in the repo are **ASSUMED**.

| Equipment | Role | Repo source | ASSUMED spec (not a lock) |
| :-- | :-- | :-- | :-- |
| Fixture holding the 20 mm face article | Locates the article and the face partner or mating plate | [PHASE0.md](../PHASE0.md) (the 20 mm article); [HARDWARE_MAPPING.md §5](../HARDWARE_MAPPING.md#5-lab-fixtures) | A rigid plate or clamp that does not warp the 1.00 mm face. Print/machine details **ASSUMED**. A retired 4×EPM fixture lives in `phase0/retired/phase0_10_minute_Force_Fixture.txt` — adapt, do not copy blind ([PROTOTYPE_PLAN_25MM.md](../PROTOTYPE_PLAN_25MM.md)). |
| Alignment jig / XY stage + fiducials | Set and log lateral offset and angle for soft-dock and the T3 window | HARDWARE_MAPPING §5 (XY stage, dial indicator / CMM; goniometer for angle) | Ability to present the locked soft-dock window of ≤ 2.5 mm / ≤ 7°, and to log whether a trial stayed inside the T3 limits lat ≤ 1.5 mm, vel ≤ 0.5 m/s. Stage resolution **ASSUMED**. |
| Motion rail (creep / abort) | Controlled approach for contact velocity | HARDWARE_MAPPING §5 and §2: creep 0.05 m/s over last 3 mm, abort at 0.25 m/s, contact max < 0.5 m/s | High-speed video or laser displacement as already listed. Rail brand **ASSUMED**. |
| Load cell / force gauge | Soft-dock insertion, snap/release (success tests 1 and 5), shear (P0-T3), spring check | PHASE0 success tests; HARDWARE_MAPPING shear rig and spring tester; MIN_PARTS “mild-steel plate + force scale” for ON/OFF on the 25 mm coupon | Must cover the locked 40 N shear bar and the 34.6 N snap figure, and the HARDWARE_MAPPING proof of 50 N × 10 s. A retired note suggested a “digital force gauge 20–100 N” (`phase0/retired/phase0_10_minute_Force_Fixture.txt`). **ASSUMED** if used: 0–100 N class, resolution 0.1 N. That range/resolution is not a lock. |
| Mild-steel target plate + 0.5 mm shim | Snap / ON-OFF axial pull at 0.5 mm gap | PHASE0 success test 1; PROTOTYPE_PLAN / MIN_PARTS | |
| Bench power supply (face bus) | 12 V onto the contact bus for the soak, only after lock | 12 V bus in DESIGN / PHASE1; soak 1.25 A | **ASSUMED:** a current-limit-capable 12 V supply that can hold **1.25 A for ≥ 10 min** without being itself the unit under test. Do not exceed the locked soak. |
| Pulse-bank charger | Charge the local 36 V nominal PP-film bank (stay ≤ 42 V into the DRV8871, 45 V abs) | LOCKS / bom netlist | **ASSUMED** charger or supply used only to charge the bank. The bank is never connected to a face contact. |
| Multimeter | Coil R, contact resistance, bus voltage | FIRST_ARTICLE M2 / M9 (4-wire R; Kelvin at 1.25 A, bar TBD after first measurement) | **ASSUMED:** a DMM (or a 4-wire / Kelvin setup) able to measure ~0.75 Ω class coil R and the 12 V bus. Model **ASSUMED**. |
| INA219 or shunt + scope | Bus current during P0-T4; peak pulse current on release | HARDWARE_MAPPING §5; FIRST_ARTICLE M5 | Optional INA219 in firmware is off by default; the fixture still needs a current measurement. |
| TMP117 and/or NTC (not a thermocouple unless you add one) | Plate / skin temperature for the soak and the 41 °C cap | PHASE0 test 6 / P0-T4; HARDWARE_MAPPING §5 “INA219 + TMP117/NTC”; firmware NTC on A0 (β=3950, 10 kΩ pull-up), optional TMP117 | The repo's skin-temp sensors are **TMP117 / NTC**, not a thermocouple. A thermocouple is **ASSUMED** only if used as an extra logger; it does not replace the 41 °C cap or the named sensors. Sample rate 1 Hz is already suggested for 25 mm M6. |
| Cycle rig + counter | 2 000 dock/undock on the same 20 mm article | PHASE0 success test 7 / P0-T5; HARDWARE_MAPPING §5 “cycle rig, counter + wear log” | Automated or manual log is already allowed. Counter model **ASSUMED**. |
| Per-pin seat sensors or a 3/3 seating check | Hard-lock: all three pins seated | P0-T2; HARDWARE_MAPPING T2 row | Method may be sensors or a verified manual/gauge check. Sensor PN **ASSUMED** if used. |
| 1.5 A fuse or PTC (proposed) | Upstream of the face-bus switch | PHASE1 §4.2 (proposed) | Proposed, not a Phase 0 success-test line. |

---

## Wiring

Keep the two rails separate. [LOCKS.md](../LOCKS.md): pulse bank and face bus stay fixture-side until contacts are covered or isolated. [PHASE1.md §4](../PHASE1.md#4-inter-module-power-handoff-proposed) (proposed, on the Phase 0 face, **unchanged here**) assigns:

- Pogos 1, 2: +12 V
- Pogos 3, 4: GND
- Pogo 5: 12 V sense
- Pogo 6: data (or spare / AGND sense on the Phase 0 assignment Phase 1 cites)

PHASE1 notes that it points at a “PHASE0.md electrical section” for that assignment; the current [PHASE0.md](../PHASE0.md) file specifies pogo **geometry** and the contact-bus soak, and does not itself contain that electrical table. Use the assignment as Phase 1 states it, and do not put pulse-bank or coil voltage on any face contact.

Suggested fixture hookup (paper, not a new lock):

1. Mechanical ground / chassis of the fixture tied to bus GND.
2. 12 V bench supply → proposed 1.5 A fuse or eFuse → load switch → pogos 1/2, **only after 3/3 hard-lock**. Kelvin or sense on pogo 5. INA219 or a shunt in that path for the soak.
3. Local pulse bank charged to 36 V nominal (≤ 42 V into DRV8871) → driver VM, with the repo C3 bulk cap and the datasheet 0.1 µF bypass at the driver. Coil leads to the face coil only. **Never across the joint.**
4. XIAO at 3.3 V from its own regulator, not from the coil rail. NTC (and optional TMP117) on the plate. Thermal governor in `firmware/pulse_driver.cpp` active from first power-up.
5. Hold current after the pulse is zero. One coil at a time until headroom is measured.

Power is off before any pin moves ([PHASE1.md](../PHASE1.md) undock rule, reused as a pattern, not rewritten).

---

## Mapping Craig's T1–T5 to the repo

Use the repo bars. IDs **P0-T1…P0-T5** are the inherited gates in [PHASE1.md §6.1](../PHASE1.md#61-inherited-gates-unchanged), from `DB-P0-FACE-TP-001`. [PHASE0.md — Success tests (locked)](../PHASE0.md#success-tests-locked) uses a 1–7 numbering that also includes Snap and Release.

| Craig's brief | Repo ID | Repo wording (quoted) | Match? |
| :-- | :-- | :-- | :-- |
| T1 soft-dock ≥90% at ≤2.5 mm/≤7° | **P0-T1**; PHASE0 **success test 2**; LOCKS “Phase 0 test 2” | PHASE0 success test 2: “Soft-dock — ≥ 90 % capture at ≤ 2.5 mm lateral, ±7° angular; insertion ≤ 5 N.” P0-T1: “Soft-dock ≥ 90 % at ≤ 2.5 mm / ≤ 7°.” LOCKS test 2 names capture and insertion, and does not restate ±7° in that one line. | **Bars match** on ≥ 90 %, ≤ 2.5 mm, and ≤ 7°. The repo also locks **insertion ≤ 5 N**, which Craig's list did not mention. Use the repo (include insertion ≤ 5 N). |
| T2 hard-lock ≥95% | **P0-T2**; PHASE0 **success test 3**; LOCKS “Phase 0 test 3” | PHASE0: “Hard-lock — ≥ 95 % with all three pins seated.” P0-T2: “Hard-lock ≥ 95 %, all 3 pins seated.” | **Match.** |
| T3 40 N shear | **P0-T3**; PHASE0 **success test 4**; LOCKS “Phase 0 test 4” | PHASE0: “Shear — ≥ 40 N through pins without plate yield. Simulated 5 028 N.” P0-T3: “Shear ≥ 40 N with lat ≤ 1.5 mm, vel ≤ 0.5 m/s.” PHASE0 also locks the T3 acceptance window: “lat ≤ 1.5 mm, vel ≤ 0.5 m/s.” | **40 N matches.** The repo also locks the **lat / vel window**, which Craig's short list did not mention. Use the full repo bar. The 5 028 N figure is a simulated earlier 2-pin result, not the pass bar. HARDWARE_MAPPING §5 also lists slip ≤ 0.10 mm and a proof 50 N × 10 s for the shear *check*; those stay in that mapping file and are not restated as new bars here. |
| T4 1.25 A × 10 min no throttle | **P0-T4**; PHASE0 **success test 6**; LOCKS “Phase 0 test 6” | PHASE0: “Thermal — 1.25 A through the contact bus ≥ 10 min. Log plate temp. 41 °C skin cap.” P0-T4: “1.25 A × 10 min, no throttle, ≤ 41 °C skin.” | **1.25 A × 10 min matches.** “No throttle” is in P0-T4 / the sim gate, not in the PHASE0 success-test 6 sentence. The **41 °C skin cap** is in PHASE0 / LOCKS / P0-T4 and was not in Craig's short list. Use the repo (no throttle **and** ≤ 41 °C). |
| T5 2,000 cycles on the same 20 mm face article | **P0-T5**; PHASE0 **success test 7**; LOCKS “Phase 0 test 7” | PHASE0: “Cycles — 2 000 dock / undock on pins + sliding pin + contacts.” P0-T5: “2 000 dock/undock cycles.” Revision note: cycle spec locked at 2 000; 3 000 is an epoxy-dependent **stretch goal**, not the lock. | **2 000 cycles match**, on the same 20 mm face article. Use 2 000, not 3 000, as the bar. |

**Also locked, not in Craig's T1–T5 list** (run them; do not drop them):

- PHASE0 **success test 1** / LOCKS Phase 0 test 1: “Snap — 34.6 N axial at 0.5 mm gap on mild steel; off-axis and 60 °C still holds.”
- PHASE0 **success test 5** / LOCKS Phase 0 test 5: “Release — magnet-pull retention ≥ 1.8 N via Option A sliding pin.”

This file adds no bars for those tests and does not retune them.

---

## Procedures (existing bars only)

Record every trial in [MEASUREMENT_CARD.md](../MEASUREMENT_CARD.md) (creating or filling that card is not this commit). Paper and sim numbers are the bar. Measured numbers are the credit. Sample sizes already written in HARDWARE_MAPPING / PHASE1 (for example n ≥ 30 offset log, n = 29 at the soft-dock corner, n = 59 hard-lock) stay in those documents; this paper does not invent new sample sizes.

### PHASE0 success test 1 — Snap (not a P0-T1…T5 ID)

Article in the fixture, 0.5 mm gap to a mild-steel target. Measure axial pull. The locked wording is “34.6 N axial at 0.5 mm gap on mild steel; off-axis and 60 °C still holds.” Do not invent a new gap, steel grade, or temperature bar.

### P0-T1 — Soft-dock (PHASE0 success test 2)

1. Mount the 20 mm article and the face partner (or mating plate) in the fixture and alignment jig.
2. Present offsets and angles inside the locked window: ≤ 2.5 mm lateral, ≤ 7° (PHASE0 writes “±7° angular”).
3. Approach on the existing motion profile if you have the rail (creep 0.05 m/s over the last 3 mm, abort 0.25 m/s; those are HARDWARE_MAPPING / Phase 1 approach figures, not new bars).
4. Record capture yes/no and insertion force. Pass is the existing wording: **≥ 90 % capture at ≤ 2.5 mm lateral, ±7° angular; insertion ≤ 5 N.**

### P0-T2 — Hard-lock (PHASE0 success test 3)

After a soft-dock, extend the three latch pins. Record seating at each pin. Pass is the existing wording: **≥ 95 % with all three pins seated.**

### P0-T3 — Shear (PHASE0 success test 4)

On a docked, hard-locked joint, apply shear with the load cell / shear rig (HARDWARE_MAPPING: four directions). Log lateral offset and contact velocity against the locked window. Pass is the existing P0-T3 wording: **≥ 40 N with lat ≤ 1.5 mm, vel ≤ 0.5 m/s**, and the PHASE0 wording “through pins without plate yield.” Do not treat the simulated 5 028 N figure as the bar.

### P0-T4 — Thermal / bus soak (PHASE0 success test 6)

1. 3/3 lock first. Then enable the 12 V face bus only, through the fixture wiring above.
2. Run **1.25 A through the contact bus for ≥ 10 min**. Log current (INA219 or shunt) and plate temperature (TMP117 / NTC).
3. Pass is the existing P0-T4 wording: **1.25 A × 10 min, no throttle, ≤ 41 °C skin.** Never exceed the locked soak current or the 41 °C skin cap. Coil pulses, if any, come from the local bank; they are not this soak, and bank recharge stays inside the inherited budget where Phase 1 already states it (≤ 0.25 A, counted inside 1.25 A) — not retuned here.

### P0-T5 — Cycles (PHASE0 success test 7)

On the **same 20 mm face article**, run **2 000 dock / undock** cycles on pins + sliding pin + contacts. Use the cycle rig and counter. Log wear. The locked bar is 2 000. 3 000 is a stretch goal only. HARDWARE_MAPPING's “spring loss ≤ 2%” stays in that mapping file; this paper does not promote it to a new Phase 0 success-test bar.

### PHASE0 success test 5 — Release (not a P0-T1…T5 ID)

Pulse the release coil from the local bank at I_release, pulse-only, thermal governor on, never across the joint. The locked wording is “magnet-pull retention ≥ 1.8 N via Option A sliding pin.” I_release itself is a measurement to record, not a new bar invented here (HARDWARE_MAPPING discusses a 25 mm sweep method separately).

---

## Safety

### Nd magnets (Ø6.0 × 2–3 mm discs, and any larger shop stock)

- Pinch: these discs can snap together or onto steel tools and catch skin. Slide, do not slam, and keep a spacer in the kit.
- Shattering: NdFeB is brittle and can chip or shatter on impact, throwing sharp fragments. Wear **eye protection** when handling, pressing into a pocket, or prying magnets apart.
- Keep magnets away from pacemakers and other implanted medical devices, magnetic storage, and magnetic-stripe cards.
- Do not let two magnets snap together uncontrolled. Do not leave loose discs near the steel fixture plate or the force-gauge armature.
- Press into the pocket only after the pocket depth has been measured ([PHASE0.md](../PHASE0.md) recommended checks). A shallow pocket can shatter a disc or yield a plate.

### Coils and power

- The coil and the 36–48 V pulse bank can get hot. Use the thermal governor; do not bypass it. Honor the **41 °C skin cap**.
- Inductive kickback: the coil is an inductive load. Use the DRV8871 as specified, with VM bypass and bulk capacitance, and do not hot-unplug the coil under pulse.
- Current limits: stay inside the driver's ILIM setpoint (~3.0 A, not the 3.6 A peak rating as a target). Do not command continuous coil current. Hold current after the pulse is zero.
- Fusing: use the proposed 1.5 A face-bus fuse or eFuse on the 12 V path. Shorted contacts are a fire and device-kill risk.
- **Never exceed the locked soak values:** 1.25 A through the contact bus, 10 min class test, ≤ 41 °C skin, no throttle as a pass condition — not a license to run hotter or longer. Never put the pulse bank on a face contact. Stay ≤ 42 V into the DRV8871 (45 V absolute maximum).
- One coil at a time until headroom is measured. Power off before any pin moves. Eye protection on the bench; no jewelry near the bus or the magnets.

---

## Test gates

TBD, no pass bar set, for anything not already locked or proposed in the sources cited above. This paper adds no IDs and no bars. Existing IDs: PHASE0 success tests 1–7; P0-T1…P0-T5.

---

## Assumptions

- Equipment models, ranges, and resolutions not quoted from the repo are ASSUMED and are not locks.
- The face-partner fixture (second 20 mm face vs a custom mating plate) is a choice, not specified as a single official jig in the repo.
- A thermocouple is not the repo's skin-temp sensor.
- Phase 1 wiring assignments and undock order are cited as existing proposed language and are not changed here.

---

## Related

- [PHASE0.md](../PHASE0.md)
- [PHASE1.md §6.1](../PHASE1.md#61-inherited-gates-unchanged) (P0-T1…P0-T5)
- [HARDWARE_MAPPING.md §5](../HARDWARE_MAPPING.md#5-lab-fixtures)
- [LOCKS.md](../LOCKS.md)
- [BILL_OF_MATERIALS.md](BILL_OF_MATERIALS.md)
- [MEASUREMENT_CARD.md](../MEASUREMENT_CARD.md)
- [FIRST_ARTICLE.md](../FIRST_ARTICLE.md)
- [OPTION_A_RELEASE_SPEC.md](../OPTION_A_RELEASE_SPEC.md)

Paper until measured. Credit follows data.
