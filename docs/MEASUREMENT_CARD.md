# 25 mm cell — measurement card

Design owned by Craig.  
**Current baseline (2026-11-19, magnet updated 2026-11-23):** Nd disc Ø6.0 mm × 2–3 mm hold (coil release-only, Alnico off), axial pin hard-lock, cavity potting, pulse-only, face coatings.  
Pocket locked Ø8.2 × 4.0 mm.

This card is only for the public 25 mm cell. Do not mix with Phase 0 numbers.

Status: **blank until measured.** No latch claim until the table is filled.

## Geometry under test
- Pocket: Ø8.2 mm × 4.0 mm (locked)
- Magnet: Nd disc Ø6.0 mm × 2–3 mm
- Coil: 2–4× AWG 36 parallel (pulse-only default)
- Driver: DRV8871, 12 V
- Logic: XIAO RP2040, 3.3 V
- Hard-lock: axial pin + receptacle
- Sealing: full cavity potting + PTFE lip + coatings

## Card (fill what you actually measured)

| Field | Value | Unit / notes |
| :---- | :---- | :-------- |
| Builder | | |
| Date | | |
| Turns on bobbin | | |
| Wire / strands | | |
| Cold R | | Ω |
| Magnet | | Nd disc Ø6.0 × 2–3 mm (record thickness and grade) |
| Gap | | mm |
| Pulse bank V | | 36–48 V |
| Peak I | | A |
| I_release | | A (lowest pulse current that releases) |
| Pulse width | | ms |
| ON force | | N (coil off) |
| OFF force | | N (after pulse) |
| Pin engagement | | mm or confirmed |
| Coil / plate temp | | °C after N pulses |
| Notes | | potting, coating, wear |

One row per coil. Credit follows the measurement.

See BUILD.md and BASELINE_UPGRADES.md for the full current build.

---

# Phase 0 face — measurement card (rev 2026-11-23b, 20 mm redesign)

Design owned by Craig. 20 mm sliding-pin face, Option A release. NdFeB N52 Ø6.0 × 2–3 mm Nd disc (coil release-only, Alnico off). 3-pin latch (7075-T6 plate) + Option A Ø2.0 mm sliding release pin. 4× non-magnetic phosphor-bronze/BeCu springs, 1.0 N/mm combined, 5 mm preload (5.00 N seated). DRV8871 driver. Approach placement 0.42 mm at 1-sigma. Cams deferred — see GATE5_SUPERSEDED.

Status: **blank until measured.** Simulation (98.04% all-pass) passed; hardware numbers go here.

## Geometry under test
- Face: 20.00 × 20.00 mm, 7075-T6 1.00 mm
- Magnet: NdFeB N52 Ø6.0 × 2–3 mm disc in Ø8.2 × 4.0 pocket (coil around disc, release-only)
- Coil: DRV8871 driver, sized for I_release, pulse-only, zero hold current
- Release: Option A sliding pin Ø2.0 mm, magnet-pull retention ≥ 1.8 N — positions per cad/voxel_cell_phase0_20mm.scad
- Latch: 3× hardened steel pins Ø1.80 in Ø1.85 bores, 7075-T6 plate
- Seating spring: 5.00 N total (4 springs)
- Contacts: 6× pogo/leaf on hex ring r = 6.25 mm at 50/110/170/230/290/350°
- Bus: 12 V nominal, 1.25 A continuous ≥ 10 min
- Driver: DRV8871, pulse bank
- MCU: XIAO RP2040
- Cycles: 2 000 locked spec
- Gates: T3 lat 1.5 mm, vel 0.5 m/s, spring 5.00 N, shear bar 40 N, all-pass 98.04%

## Card (fill what you actually measured)

| Field | Value | Unit / notes |
| :---- | :---- | :-------- |
| Builder | | |
| Date | | |
| Magnet grade / size | | NdFeB N52 Ø6.0 × 2–3 mm (record thickness) |
| Coil turns / wire | | / |
| Cold R | | Ω |
| Pulse bank V | | V |
| Peak I | | A |
| Pulse width | | µs–ms |
| Snap force (centered, 0.5 mm) | | N (sim: 34.6) |
| Snap off-axis 1.5 mm | | N (sim: 26) |
| Snap at 60 °C | | N (sim: ~32) |
| Release / retention | | N (sim: ≥ 1.8, magnet-pull + sliding pin) |
| Sliding-pin wear after N cycles | | µm |
| Shear | | N (sim: 5 028, earlier 2-pin build) |
| Soft-dock capture rate | | % at ≤ 2.5 mm |
| Insertion force | | N (sim: 5) |
| Bus temp after 10 min @ 1.25 A | | °C |
| Plate temp near contact | | °C |
| Plate temp near magnet | | °C |
| Pin engagement (3/3) | | mm or confirmed |
| Cycles completed | | / 2 000 |
| Notes | | sliding-pin material, oxide, tip swap |

One row per test. Credit follows the measurement. Simulation numbers in parentheses are not credit — they are the bar to beat.
