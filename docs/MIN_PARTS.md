# 25 mm cell — minimum parts for one counted coil (current baseline)

Design owned by Craig.  
Baseline: 2026-11-19 — axial pin, potting, pulse-only. Magnet updated 2026-11-23: Nd disc Ø6.0 × 2–3 mm hold, coil release-only, Alnico off this cell.

This list is for the public 25 mm cell. Fill MEASUREMENT_CARD.md with whatever this kit measures. No latch claim until the card is filled.

## Geometry (locked)
- Envelope: 25 mm cube
- Pocket: Ø8.2 mm × 4.0 mm (do not enlarge)
- Magnet: Nd disc Ø6.0 mm × 2–3 mm (hold)
- Axial pin receptacle added in CAD

## Buy or borrow
| # | Item | Spec | Notes |
| :--- | :--- | :--- | :--- |
| 1 | Magnet | Nd disc Ø6.0 × 2–3 mm | Current hold magnet (2026-11-23). Do not order Alnico or SmCo Ø7.5 for this cell |
| 2 | Magnet wire | 2–4× AWG 36 parallel | Pulse-only default |
| 3 | Driver | DRV8871 | 12 V VM |
| 4 | Logic | XIAO RP2040 | 3.3 V only |
| 5 | Pulse bank | PP film caps, 36–48 V, 100 V rating | Potted |
| 6 | Axial pin + receptacle | Ø1.5–2.0 mm × 2.5–3.0 mm engagement | Mechanical hard-lock |
| 7 | Fixture | Mild-steel plate + force scale | ON/OFF measurement |
| 8 | Potting + coatings | Low-outgassing potting, PTFE lip material, conformal coating | Sealing |

Do not order: D8 mm stacks, single-strand continuous-duty wire, DRV8837C, or Phase 0 parts for this cell.

Bench order: wind, measure R, pulse, record ON/OFF, confirm pin seats after soft-dock, log temperature. Paste into MEASUREMENT_CARD.md.
