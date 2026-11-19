# BUILD.md — 25 mm cell, current baseline

Handoff page for the 2026-11-19 baseline.  
Design owner: Craig.  
Status: SmCo Ø7.5 mm, axial pin hard-lock, cavity potting, pulse-only, face coatings. Pocket locked Ø8.2 × 4.0 mm.

## What you're building

One 25 mm cube.  
Hold is SmCo 2:17 Ø7.5 mm × 3.0 mm.  
Coil is release pulse only.  
Short axial pin engages after magnetic soft-dock and carries external load.  
Cavity is fully potted. Faces have PTFE lip + conformal coating.  
Driver: DRV8871 on 12 V. Logic: XIAO RP2040 at 3.3 V.  
Pulse bank: 36–48 V polypropylene film capacitors.

Do not build earlier NdFeB / Alnico or Ø6 mm stacks.

## 1. Magnet
- SmCo 2:17 Ø7.5 mm × 3.0 mm, axial, NiCuNi or equivalent
- Fits the locked Ø8.2 mm pocket with reduced winding window
- Paper residual hold range ~16–47 N (area-scaled)

## 2. Mechanical hard-lock
- Short axial pin + receptacle (Ø1.5–2.0 mm × 2.5–3.0 mm engagement)
- Engages only after magnetic soft-dock closes the final gap
- Once seated, pin carries axial / pressure load
- Existing carbide shim and PTFE lip remain

## 3. Sealing
- Full electronics cavity potting (low-outgassing compound)
- PTFE lip (0.1–0.2 mm) on detent ridge, mechanically captured
- Thin conformal coating or hard finish on exposed metal faces

## 4. Drive
- Pulse-only is default
- Firmware thermal governor required (refuse continuous duty above plate-temp threshold)
- Parallel-strand wind for any sustained pulse train
- 36–48 V PP film pulse bank (100 V rating recommended)

## 5. Parts list (current baseline)
- Magnet: SmCo 2:17 Ø7.5 × 3.0 mm
- Wire: AWG 36, 2–4 parallel strands
- Pulse bank: PP film, 36–48 V, 100 V rating, potted
- Driver: DRV8871
- MCU: XIAO RP2040
- Pocket: Ø8.2 × 4.0 mm (locked)
- Axial pin + receptacle
- Carbide or 440C shear shim
- PTFE lip + face coating
- Potting compound for cavity

## 6. Success criteria
Nothing is a measured latch until disc, turns, R, peak I, I_release, ON N, and OFF N are published in MEASUREMENT_CARD.md.

See BASELINE_UPGRADES.md, DESIGN.md, and PAPER_STATUS.md for the full locked set.
