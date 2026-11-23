# DittoBot 25 mm Cell — Baseline Upgrades (Underwater + Space Standard)

Design owner: Craig  
Date: 2026-11-19  
Status: Paper baseline update. Pocket geometry unchanged.

These changes fold into the normal build. No separate variant required.

## 1. Magnet stack
- Standard (updated 2026-11-23): Nd disc Ø6.0 mm × 2–3 mm hold magnet. Replaces the SmCo 2:17 Ø7.5 × 3.0 mm standard set on 2026-11-19.
- Coil wound around the disc, release-only, sized for I_release (not hold). Alnico off this cell.
- Hold force: TBD, measure (no paper range claimed for this disc)
- Fits Ø8.2 × 4.0 mm pocket with a 1.10 mm radial winding annulus
- Pulse bank: 36–48 V polypropylene film capacitors (existing Mars pulse notes now standard)

## 2. Mechanical hard-lock (tighter docking)
- Short axial pin + receptacle on each face
- Pin: Ø1.5–2.0 mm × 2.5–3.0 mm engagement length, centered or offset from magnetic axis
- Engages only after magnetic soft-dock closes the final 0.1–0.2 mm
- Once seated, pin carries axial pressure / external load
- Magnetic residual only required for pull-in and zero-power hold
- Existing carbide shear shim and PTFE lip remain

## 3. Sealing and environmental protection
- Full electronics cavity potting: low-outgassing, water-resistant compound (space-rated silicone or equivalent)
- PTFE lip (0.1–0.2 mm) on detent ridge retained
- Thin conformal coating or hard finish (anodize / nickel) on all exposed metal faces
- Purpose: blocks water intrusion at depth, reduces cold-weld and outgassing in vacuum, keeps faces clean for pin engagement

## 4. Drive and thermal
- Pulse-only coil drive is default
- Firmware thermal governor required (refuse continuous duty unless plate temp below threshold)
- Parallel-strand coil wind retained for any sustained pulse train
- No continuous soak in vacuum or restricted-flow conditions

## 5. Pressure and environment notes
- Up to ~200 m: magnetic soft-dock closes gap; mechanical pin carries pressure force
- Beyond that depth a true pressure hull or external structure is still required
- Space / micro-g: residual magnetic force provides final latch; first contact still benefits from small residual velocity
- Thermal path: radiation + conduction only when no convection available

## Geometry lock
- External envelope: 25.0 mm cube unchanged
- Latching core bore: Ø8.2 mm × 4.0 mm depth unchanged
- Face interconnect and data pads unchanged
- CAD header and notes synced to Nd disc Ø6.0×2–3 mm in the 2026-11-23 sweep; full 20 mm face redesign is a separate commit

## Measurement card additions
- Record ON/OFF force and I_release with the Ø6.0 × 2–3 mm Nd disc
- Record pin engagement force and cycle wear
- Confirm potting integrity (no moisture path)
- Thermal: pulse train temperature rise in still air and vacuum chamber if available

Credit follows measured data.
