# DESIGN.md — 25 mm cell architecture

Design owner: Craig. Started Nov/Dec 2025.
Status: clean core swap, 2026-09-10. Thermal revision 2026-11-06.
Residual-hold hardening 2026-11-19. Mars variant 2026-11-19.

## 1. Cell envelope

25 mm cube. One centered Ø8.2 × 4.0 mm pocket. One Ø6.0 mm magnet stack.
One coil. One release pulse. Driver DRV8871, 12 V. Logic XIAO RP2040, 3.3 V.

## 2. Lock philosophy

The magnet holds. The coil only releases. Size the coil for the cancel peak,
not for holding force. Nothing is a measured latch until disc, turns, R,
peak I, I_release, ON N, and OFF N are published in MEASUREMENT_CARD.md.

## 3. Version ladder

- v0: 120-turn / 5 V / 28.8 N — retired
- v1: 2026-09-09 Nd+Alnico flip stack — superseded, do not build
- v2: 2026-09-10 clean core swap, DRV8871, parallel-strand thermal fix
- v3: 2026-11-19 residual-hold hardening (this file, §6)
- v4: 2026-11-19 Mars variant — see MARS_VARIANT.md

## 4. Files

- BUILD.md — fab handoff
- COIL_REVISION.md — why the first pass failed, wind math, SmCo path
- PHASE0.md — locked 20 mm face (do not mix numbers)
- MEASUREMENT_CARD.md — blank until filled
- MARS_VARIANT.md — Mars adaptations (all-SmCo, pulse-only governor,
  detent wiper, rad-hardened driver)
- cad/voxel_cell.scad — pocket geometry, locked
- firmware/pulse_driver.cpp — pulse routine
- bom/bom_netlist.txt — BOM
- tools/force_sweep.py — paper sweep, warning only

## 5. Paper locks

See LOCKS.md (16 locks, 2026-09-14). No geometry change without a new lock.

## 6. Residual-hold hardening (2026-11-19)

Sim (2026-11-18) found the zero-power residual (~5.7 N clean-gap) as the
soft spot: any dust or misalignment and it drops fast.

Three levers, stacked:

1. **SmCo 2:17 alternate path** — higher coercivity, thermally stable Br.
   Clean-gap residual drops to ~4.1 N (lower Br) but holds ~4.0 N at 80 °C
   where NdFeB slides to 5.3 N. The win is stability, not peak.
2. **Compliant pole tip** — 0.2–0.4 mm silicone or spring-steel washer on the
   latch face. Stiffness ~188 kN/m. Compresses a 50 µm dust grain at 9.4 N
   (more than double the magnetic residual) and absorbs ≤2° tilt. Dust stops
   being a cliff.
3. **Groove-and-ridge detent** — 0.30 mm deep annular groove in the shim,
   matching ridge on the mating plate. Full-engagement shear ~8 950 N
   (200× the 40 N gate). Magnetism positions; geometry locks. Minimum
   engagement 0.15 mm, target 0.25–0.30 mm — see BUILD.md detent section.

Stacked worst-case floor (dusty, 80 °C, 0.15 mm gap): ~18.6 N magnetic plus
detent. The detent means even zero magnetic residual does not drop the cell.

## 7. Mars variant (2026-11-19)

See MARS_VARIANT.md for full spec. Summary:

- All-SmCo stack mandatory — NdFeB coercivity collapses below minus sixty Celsius
- Pulse-only coil with firmware thermal governor (no convection at 0.6 kPa)
- PTFE/PEEK wiper lip on detent ridge (dust packing, ~1 µm abrasive)
- Rad-hardened MCU + driver (GCR/SEP; magnets and steel unaffected)
- Stacked floor at polar winter: ~4 500 N vs 40 N gate, 112× margin
