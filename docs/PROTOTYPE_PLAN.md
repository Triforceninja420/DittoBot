# PROTOTYPE_PLAN — First-Article Metrology (25 mm cell)

Design owned by Craig. Started 2026-11-23. Status: **planned, not started**.
Credit follows measured data. Sim numbers are the bar, not the credit.

This file covers the **first 25 mm article only**. Phase 0 20 mm face metrology
is a separate plan (see `docs/PHASE0.md` public fixture package).

---

## 1. What to build

One 25 mm cubic cell per `cad/voxel_cell.scad` and `bom/bom_netlist.txt`:

- Nd disc Ø6.0 × 2–3 mm in the locked Ø8.2 × 4.0 pocket (coil around disc, release-only)
- Parallel 2–4× AWG 36 coil, counted turns, pulse-only via DRV8871
- Axial pin Ø1.5–2.0 mm hard-lock
- Full cavity potting, PTFE lip + coatings
- XIAO RP2040 + thermal governor firmware (`firmware/pulse_driver.cpp`)
- 36 V nominal pulse bank (polypropylene film, ≤ 42 V into driver)

## 2. Metrology sequence (do in order)

| Step | Measurement | Method | Pass bar (sim) |
| :--- | :--------- | :----- | :------------- |
| M1 | Magnet axial field at pocket face | Gaussmeter at 0.5 mm gap on mild steel | ≥ snap target |
| M2 | Coil DC resistance | 4-wire at room temp | ~0.74 Ω (2× AWG 36 parallel est.) |
| M3 | ON force (snap) | Force gauge, axial, 0.5 mm gap | 34.6 N sim bar |
| M4 | OFF force (release) | Same fixture, pulse at I_release | retention ≥ 1.8 N sim bar (magnet-pull + sliding pin) |
| M5 | Peak pulse current | INA219 or shunt + scope | ≤ 3.6 A DRV8871 peak |
| M6 | Plate temperature after 10 min at 1.25 A | TMP117 / NTC log | ≤ 41 °C skin cap |
| M7 | Pin engagement | Depth gauge / witness marks | ≥ 2.5–3.0 mm |
| M8 | 2 000 dock/undock cycles | Automated fixture or manual log | sliding-pin and contact wear logged |
| M9 | Contact resistance across face bus | Kelvin at 1.25 A | TBD after first measurement |

## 3. Fixtures

- Axial force rig: mild-steel target plate, 0.5 mm shim stack, force gauge
  (see `phase0/retired/phase0_10_minute_Force_Fixture.txt` for the retired
  20 mm 4×EPM sequence — adapt, don't copy blind).
- Pulse bank: polypropylene film caps, charged 30–36 V, DRV8871, XIAO trigger.
- Thermal log: TMP117 on plate back face, 1 Hz sample during M6.

## 4. What not to do

- No continuous coil current. Pulse-only. Thermal governor must refuse sustained duty.
- No Alnico on this cell. Nd disc only.
- No enlarging the Ø8.2 pocket.
- No mixing Phase 0 20 mm numbers into this build.

## 5. Exit criteria

- M1–M8 all logged with raw data in `docs/MEASUREMENT_CARD.md`.
- Any sim bar missed gets a design response (like the T4/T5 fixes), not a
  lowered bar.
- Credit follows the card. Not the sim.

**End of 25 mm first-article plan.**
