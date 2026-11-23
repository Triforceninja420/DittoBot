# BUILD.md — 25 mm cell, current baseline

Handoff page for the 2026-11-19 baseline.  
Design owner: Craig.  
Status: Nd disc Ø6.0 × 2–3 mm hold, axial pin hard-lock, cavity potting, pulse-only, face coatings. Pocket locked Ø8.2 × 4.0 mm.

Updated 2026-11-23 (Craig): hold magnet is a Ø6.0 × 2–3 mm Nd disc in the locked Ø8.2 × 4.0 mm pocket. Coil wound around the disc, release-only, sized for I_release (not hold). Alnico is off this cell. Replaces the SmCo 2:17 Ø7.5 × 3.0 mm baseline of 2026-11-19.

## What you're building

One 25 mm cube.  
Hold is an Nd disc Ø6.0 mm × 2–3 mm.  
Coil is wound around the disc, release pulse only, sized for I_release (not hold).  
Short axial pin engages after magnetic soft-dock and carries external load.  
Cavity is fully potted. Faces have PTFE lip + conformal coating.  
Driver: DRV8871 on 12 V. Logic: XIAO RP2040 at 3.3 V.  
Pulse bank: 36–48 V polypropylene film capacitors.

Alnico is off this cell. Do not build Alnico or Nd+Alnico flip stacks, and do not build the retired SmCo Ø7.5 × 3.0 mm stack.

## 1. Magnet
- Nd disc Ø6.0 mm × 2–3 mm, axial (grade TBD, record on the card)
- Sits in the locked Ø8.2 × 4.0 mm pocket; 1.10 mm radial annulus per side for the coil bobbin — the bobbin centers the disc
- Hold force: TBD, measure ON force (no paper range claimed for this disc)

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
- Magnet: Nd disc Ø6.0 × 2–3 mm (hold)
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
