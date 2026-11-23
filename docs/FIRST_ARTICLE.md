# First-Article Prototype Build

Design owned by Craig. Started 2026-11-23.
Credit follows measured data. Sim numbers are the bar, not the credit.

This article covers the first-article sequence for both active variants:

- **Phase 0** — 20 mm dual-cam docking face (`docs/PHASE0.md`)
- **25 mm cell** — cubic voxel cell (`docs/PROTOTYPE_PLAN.md`, `bom/bom_netlist.txt`)

Firmware thermal governor: `firmware/pulse_driver.cpp` (NTC + optional TMP117,
state machine, INA219 sensing, pulse trains, error flags).

---

## 1. What you are building

### Phase 0 — 20 mm face

One docking face. Prove snap-in capture, dual-cam release, pin latch,
contacts, and thermal on hardware. Not a cube. Not a swarm.

| Item | Locked value |
| :--- | :-------- |
| Envelope | 20.00 × 20.00 mm square face |
| Plate | 7075-T6, 1.00 mm nominal (accept 0.80–1.20) |
| Magnet | NdFeB N52, Ø6.0 × 2–3 mm disc (coil release-only; Alnico off) |
| Coil | 40 turns, 34 AWG, ~0.75 Ω cold, DRV8871, pulse-only, zero hold |
| Snap (axial) | 34.6 N simulated at 0.5 mm gap |
| Seating spring | 5.00 N total (4× non-magnetic phosphor-bronze/BeCu, 1.0 N/mm) |
| Latch | 3× hardened steel pins Ø1.80 in Ø1.85 bores |
| Cams | Dual 8 mm radius, staggered (8,8) and (22,22), bore Ø16.05 (0.05 mm clearance), steel-backed polymer tips |
| Release net | +65.7 N simulated |
| Soft-dock | ≥ 90% capture at ≤ 2.5 mm lateral, ±7° angular |
| Shear | ≥ 40 N target (simulated 5 028 N on earlier 2-pin build) |
| Thermal | < 1.5 K rise at 0.44 W pulse-duty |
| Cycles | 2 000 dock/undock locked; 3 000 stretch goal (epoxy-dependent) |

### 25 mm cell

One cubic cell per `cad/voxel_cell.scad`:

- Nd disc Ø6.0 × 2–3 mm in locked Ø8.2 × 4.0 mm pocket (coil release-only)
- Parallel 2–4× AWG 36 coil, counted turns, pulse-only via DRV8871
- Axial pin Ø1.5–2.0 mm hard-lock, ≥ 2.5–3.0 mm engagement
- Full cavity potting, PTFE lip + coatings
- XIAO RP2040 + thermal governor firmware
- 36 V nominal pulse bank (polypropylene film, ≤ 42 V into driver)

**Do not mix Phase 0 20 mm numbers into the 25 mm build, or vice versa.**

---

## 2. Order of operations

Do not skip ahead. Each step gates the next.

1. **Order parts** from `bom/bom_netlist.txt` (supplier links and approx.
   prices included; re-verify on DigiKey/Mouser before PO — prices as of
   2026-11-23).
2. **Fab the plate** from `cad/voxel_cell_phase0_20mm.scad` (Phase 0) or
   `cad/voxel_cell.scad` (25 mm). Use the fab drawings in `CAD/`.
3. **Metrology before assembly** — see §3. Log every number.
4. **Tip-bond pull test** (Phase 0) — bond a dummy polymer tip to a steel
   coupon with the same epoxy and cure schedule; pull at 50 N. Learn on a
   coupon, not a finished module.
5. **Assemble** — magnet press (blind pocket, verify depth first), coil wind
   (count turns), pins, cams, springs, pogos, driver, MCU.
6. **Firmware flash** — `firmware/pulse_driver.cpp`. Thermal governor active
   from first power-up. No continuous coil current, ever.
7. **Run the measurement sequence** — §4. Fill the card in
   `docs/MEASUREMENT_CARD.md` as you go.
8. **Cycles** — 2 000 dock/undock. Log cam tip wear.

---

## 3. Metrology before assembly

### Phase 0 plate checks

1. **Cam radius and lobe profile** — height gauge or optical comparator.
   Target 8.00 mm radius, lobe edge square to face within 0.05 mm. Bore at
   Ø16.05 ±0.05.
2. **Pin-bore true position** — CMM if available; otherwise dowel pin plus
   digital caliper. Catch a 0.5 mm offset before assembly.
3. **Blind pocket depth** — depth micrometer through the magnet opening,
   before any press. Log the number. 0.1 mm shallow is a press-fit disaster;
   0.1 mm deep just means the magnet sits proud.
4. **Plate flatness** — surface plate and indicator, ≤ 0.10 mm target.
5. **Contact wipe** — 0.30–0.50 mm of travel on each pogo pair.

Intentional relief: cam bores are nominal Ø16.05 (0.05 mm design clearance).
If a cam binds, file — don't scrap the plate. Pin bores: drill 0.05 mm
oversize with ream-to-fit option.

### 25 mm cell checks (PROTOTYPE_PLAN order)

| Step | Measurement | Method | Pass bar (sim) |
| :--- | :--------- | :----- | :------------- |
| M1 | Magnet axial field at pocket face | Gaussmeter at 0.5 mm gap on mild steel | ≥ snap target |
| M2 | Coil DC resistance | 4-wire at room temp | ~0.74 Ω (2× AWG 36 parallel est.) |
| M3 | ON force (snap) | Force gauge, axial, 0.5 mm gap | 34.6 N |
| M4 | OFF force (release) | Same fixture, pulse at I_release | net +65.7 N |
| M5 | Peak pulse current | INA219 or shunt + scope | ≤ 3.6 A DRV8871 peak |
| M6 | Plate temperature after 10 min at 1.25 A | TMP117 / NTC log | ≤ 41 °C skin cap |
| M7 | Pin engagement | Depth gauge / witness marks | ≥ 2.5–3.0 mm |
| M8 | 2 000 dock/undock cycles | Automated fixture or manual log | cam tip wear ≤ 0.19 µm |
| M9 | Contact resistance across face bus | Kelvin at 1.25 A | TBD after first measurement |

---

## 4. Thermal governor (firmware)

`firmware/pulse_driver.cpp` implements the governor from first flash:

- **NTC** on A0, beta 3950, 10k pull-up to 3.3 V. Optional **TMP117** on
  I2C (addr 0x48) — set `USE_TMP117 = true` if populated.
- **Threshold:** 60 °C with 5 °C hysteresis. Above threshold → thermal latch,
  `ERR_THERMAL` flag, pulses refused until cooled below 55 °C.
- **Pulse limit:** 20 consecutive pulses before forced 5 s cooldown.
- **Current sense:** optional INA219 (addr 0x40). Above 3.6 A (DRV8871 peak
  rating) → `ERR_CURRENT`.
- **Contact detection:** six pogos on GPIO 2–7, active low when mated.
  State machine: IDLE → SOFT_DOCK → HARD_LOCK → POWERED, with ERROR on any
  flag.
- **Pulse parameters:** 100 ms default width, 20 ms inter-pulse gap in trains.
  Start in the 50–200 ms band and tune from measured time-to-peak.
- **Serial at 115200:** `p` release, `e` engage, `t` temp, `c` contacts,
  `i` current, `s` state, `f` errors, `r` reset, `h` help.
- **Watchdog:** loop stall > 2 s → `ERR_WATCHDOG`.

The governor's job is simple: the coil is release-only. Hold is the Nd
residual. Static coil current is zero. If the plate is hot, it says no.

---

## 5. BOM summary (25 mm cell)

Full netlist with supplier links and approx. prices in
`bom/bom_netlist.txt`. Headline lines:

| Item | Part | Approx. USD |
| :--- | :---- | :----------- |
| U1 | XIAO RP2040 | $5–7 |
| U2 | DRV8871 (or DRV8212 alt) | $1–3 |
| MAG1 | Nd disc Ø6.0 × 2–3 mm | $1–3 |
| L1 | Release coil, 2–4× AWG 36 parallel | wire $5–10 spool |
| J1–J4 | Mill-Max 0906 spring contacts | $0.50–1 each |
| U3 | 3.3 V buck/LDO | $1–3 |
| U4 | Pulse bank, polypropylene film 36 V | $2–5 |
| SHIM1 | Carbide shear shim | $3–10 |
| PIN1 | Axial pin + receptacle | $1–5 |
| POT1 | Low-outgassing potting compound | $10–30 |

TI offers free DRV8871 samples — order if lead time allows. Magnet grade
(N52 vs N42) and coating swing the price; verify axial field before ordering.

Phase 0 face parts (plate, cams, pins, springs, pogos) are in the fab
package under `Phase0_Independent_Fab_Package/` (v0.2) and the aluminum
plate package.

---

## 6. What not to do

- No continuous coil current. Pulse-only. The governor must refuse sustained
  duty.
- No Alnico on either active cell. Nd disc only.
- No enlarging the Ø8.2 pocket on the 25 mm cell.
- No mixing Phase 0 and 25 mm numbers across documents.
- No latch claim until `docs/MEASUREMENT_CARD.md` is filled with real data.

---

## 7. Exit criteria

- M1–M8 (25 mm) or the Phase 0 success tests all logged with raw data in
  `docs/MEASUREMENT_CARD.md`.
- Any sim bar missed gets a design response, not a lowered bar.
- **Credit follows the card. Not the sim.**

---

## Minor note

Root still has both `CAD/` and `cad/` directories. Consolidate to one when
convenient — layout otherwise matches.

**End of first-article article.**