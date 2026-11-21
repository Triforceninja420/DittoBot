# 25 mm cell — measurement card

Design owned by Craig.  
**Current baseline (2026-11-19):** SmCo 2:17 Ø7.5 mm × 3.0 mm, axial pin hard-lock, cavity potting, pulse-only, face coatings.  
Pocket locked Ø8.2 × 4.0 mm.

This card is only for the public 25 mm cell. Do not mix with Phase 0 numbers.

Status: **blank until measured.** No latch claim until the table is filled.

## Geometry under test
- Pocket: Ø8.2 mm × 4.0 mm (locked)
- Magnet: SmCo 2:17 Ø7.5 mm × 3.0 mm
- Coil: 2–4× AWG 36 parallel (pulse-only default)
- Driver: DRV8871, 12 V
- Logic: XIAO RP2040, 3.3 V
- Hard-lock: axial pin + receptacle
- Sealing: full cavity potting + PTFE lip + coatings

## Card (fill what you actually measured)

| Field | Value | Unit / notes |
| :--- | :--- | :--- |
| Builder | | |
| Date | | |
| Turns on bobbin | | |
| Wire / strands | | |
| Cold R | | Ω |
| Magnet | | SmCo Ø7.5 × 3.0 mm |
| Gap | | mm |
| Pulse bank V | | 36–48 V |
| Peak I | | A |
| Pulse width | | ms |
| ON force | | N (coil off) |
| OFF force | | N (after pulse) |
| Pin engagement | | mm or confirmed |
| Coil / plate temp | | °C after N pulses |
| Notes | | potting, coating, wear |

One row per coil. Credit follows the measurement.

See BUILD.md and BASELINE_UPGRADES.md for the full current build.

---

# Phase 0 face — measurement card (rev 2026-11-21)

Design owned by Craig. 30 mm dual-cam staggered face. NdFeB N52 Ø6 × 6 mm. Steel-backed polymer-tip cams. Two-pin latch + retraction actuator. 5 N seating spring.

Status: **blank until measured.** Simulation (26 tests) passed; hardware numbers go here.

## Geometry under test
- Face: 30.00 × 30.00 mm, 6061-T6 1.00 mm
- Magnet: NdFeB N52 Ø6.0 × 6.0 mm, axial, centered
- Coil: 40 turns 34 AWG, ~0.75 Ω, pulse-duty
- Cams: dual 8 mm radius, staggered (8,8) + (22,22), steel-backed polymer tips, 8 mm contact width
- Latch: 2× hardened steel pins + ~1/3 g retraction actuator
- Seating spring: 5 N
- Contacts: 6× pogo/leaf on hex ring
- Bus: 12 V nominal, 1.25 A continuous ≥ 10 min
- Driver: IRLZ44N class H-bridge, 220 µF / 30–36 V pulse bank
- MCU: Raspberry Pi Pico RP2040

## Card (fill what you actually measured)

| Field | Value | Unit / notes |
| :--- | :--- | :--- |
| Builder | | |
| Date | | |
| Magnet grade / size | | NdFeB N52 Ø6 × 6 |
| Coil turns / wire | | 40 / 34 AWG |
| Cold R | | Ω |
| Pulse bank V | | 30–36 V |
| Peak I | | A |
| Pulse width | | µs–ms |
| Snap force (centered, 0.5 mm) | | N (sim: 34.6) |
| Snap off-axis 1.5 mm | | N (sim: 26) |
| Snap at 60 °C | | N (sim: ~32) |
| Release net | | N (sim: +65.7) |
| Cam tip wear after N cycles | | µm (sim: 0.19 / 2 000) |
| Shear | | N (sim: 5 028) |
| Soft-dock capture rate | | % at ≤ 2.5 mm |
| Insertion force | | N (sim: 5) |
| Bus temp after 10 min @ 1.25 A | | °C |
| Plate temp near contact | | °C |
| Plate temp near magnet | | °C |
| Pin engagement | | mm or confirmed |
| Cycles completed | | / 2 000 |
| Notes | | cam material, tip swap, oxide |

One row per test. Credit follows the measurement. Simulation numbers in parentheses are not credit — they are the bar to beat.
