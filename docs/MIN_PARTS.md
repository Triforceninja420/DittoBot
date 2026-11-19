# 25 mm cell — minimum parts for one counted coil (current baseline)

Design owned by Craig.  
Baseline: 2026-11-19 — SmCo Ø7.5 mm, axial pin, potting, pulse-only.

This list is for the public 25 mm cell. Fill MEASUREMENT_CARD.md with whatever this kit measures. No latch claim until the card is filled.

## Geometry (locked)
- Envelope: 25 mm cube
- Pocket: Ø8.2 mm × 4.0 mm (do not enlarge)
- Magnet: SmCo 2:17 Ø7.5 mm × 3.0 mm
- Axial pin receptacle added in CAD

## Buy or borrow
| # | Item | Spec | Notes |
| :--- | :--- | :--- | :--- |
| 1 | Magnet | SmCo 2:17 Ø7.5 × 3.0 mm | Current baseline. Do not order Ø6 or NdFeB for shippable builds |
| 2 | Magnet wire | 2–4× AWG 36 parallel | Pulse-only default |
| 3 | Driver | DRV8871 | 12 V VM |
| 4 | Logic | XIAO RP2040 | 3.3 V only |
| 5 | Pulse bank | PP film caps, 36–48 V, 100 V rating | Potted |
| 6 | Axial pin + receptacle | Ø1.5–2.0 mm × 2.5–3.0 mm engagement | Mechanical hard-lock |
| 7 | Fixture | Mild-steel plate + force scale | ON/OFF measurement |
| 8 | Potting + coatings | Low-outgassing potting, PTFE lip material, conformal coating | Sealing |

Do not order: D8 mm stacks, single-strand continuous-duty wire, DRV8837C, or Phase 0 parts for this cell.

Bench order: wind, measure R, pulse, record ON/OFF, confirm pin seats after soft-dock, log temperature. Paste into MEASUREMENT_CARD.md.
