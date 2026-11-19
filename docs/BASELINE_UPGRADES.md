# DittoBot 25 mm Cell — Baseline Upgrades (Underwater + Space Standard)

Design owner: Craig  
Date: 2026-11-19  
Status: Paper baseline update. Pocket geometry unchanged.

These changes fold into the normal build. No separate variant required.

## 1. Magnet stack
- Standard: SmCo 2:17 Ø7.5 mm × 3.0 mm (NiCuNi or equivalent)
- Replaces previous Ø6 mm stack
- Residual hold paper range: ~15–48 N (area-scaled from prior Ø6 estimates)
- Still fits Ø8.2 mm pocket; winding window reduced accordingly
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
- CAD update required only for pin/receptacle features and magnet OD

## Measurement card additions
- Record ON/OFF force with new Ø7.5 mm SmCo
- Record pin engagement force and cycle wear
- Confirm potting integrity (no moisture path)
- Thermal: pulse train temperature rise in still air and vacuum chamber if available

Credit follows measured data.
