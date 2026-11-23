# DESIGN.md — 25 mm cell architecture

Design owner: Craig. Started Nov/Dec 2025.  
Status: 2026-11-19 baseline locked on paper; magnet updated 2026-11-23.

Updated 2026-11-23 (Craig): hold magnet is a Ø6.0 × 2–3 mm Nd disc in the locked Ø8.2 × 4.0 mm pocket. Coil wound around the disc, release-only, sized for I_release (not hold). Alnico is off this cell. Replaces the SmCo 2:17 Ø7.5 × 3.0 mm baseline of 2026-11-19.

## 1. Cell envelope
25 mm cube. Centered Ø8.2 × 4.0 mm pocket (locked).  
Nd disc Ø6.0 mm × 2–3 mm hold magnet; coil around the disc, release-only. Alnico off this cell.  
Axial pin hard-lock. Full cavity potting. Face coatings.  
DRV8871, 12 V. XIAO RP2040, 3.3 V. 36–48 V pulse bank.

## 2. Lock philosophy
Magnet provides soft-dock and zero-power residual hold.  
Coil only releases.  
Axial pin carries external load once seated.  
Nothing is a measured latch until the measurement card is filled.

## 3. Version ladder
- v0–v2: retired / superseded
- v3: residual-hold hardening
- v4: current baseline (Nd disc Ø6.0 × 2–3 mm hold, pin, potting, coatings, pulse-only) + Mars/space inheritance. Magnet changed from SmCo Ø7.5 × 3.0 to the Nd disc on 2026-11-23.

## 4. Key files
- BASELINE_UPGRADES.md
- BUILD.md
- PAPER_STATUS.md
- MARS_VARIANT.md
- EXTREME_ENVIRONMENTS.md
- MEASUREMENT_CARD.md
- cad/voxel_cell.scad (pocket locked; pin receptacle added)

Credit follows measured data.
