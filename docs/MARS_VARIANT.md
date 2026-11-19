# MARS VARIANT — 25 mm cell, residual-hold hardening + Mars / space adaptations

Mars-specific build of the 25 mm cell. Design owner: Craig.
Baseline now includes the 2026-11-19 upgrades (see BASELINE_UPGRADES.md).
Mars sim: 2026-11-18. Pulse/wiper sims: 2026-11-19.
Status: paper only, no hardware.

The Mars variant is the natural space-hardened path. Low pressure, extreme cold, dust, and radiation on Mars cover the majority of deep-space and vacuum challenges. The baseline potting, coatings, Ø7.5 mm SmCo, and mechanical pin are inherited here so the cell handles both Mars surface and pure space better without a third variant.

## What is now standard (inherited from baseline)

- SmCo 2:17 Ø7.5 mm × 3.0 mm stack (stronger residual, cold-stable)
- Short axial pin + receptacle for mechanical hard-lock after magnetic soft-dock
- Full cavity potting (low-outgassing, water- and vacuum-resistant)
- PTFE lip + conformal coating / hard finish on exposed faces
- Pulse-only drive + thermal governor
- 36–48 V PP film pulse bank

These close water intrusion (if any residual moisture), cold-weld risk, outgassing, and thermal runaway in vacuum. The Mars-specific items below build on top of them.

## Mars / space specific additions

### All-SmCo (already baseline) + residual at cryo
SmCo remains mandatory. At −125 °C the larger Ø7.5 mm stack improves residual hold margin versus the prior Ø6 mm numbers. No NdFeB anywhere.

### Pulse-only + thermal governor (already baseline)
No convection at 0.6 kPa or in hard vacuum. Governor and pulse-only are now the default everywhere; Mars just makes them non-negotiable.

### Detent ridge wiper + coatings
PTFE lip retained and now paired with the baseline conformal coating. Together they handle Mars dust and reduce metal-to-metal contact for cold-welding in vacuum.

### Rad-hardened driver side
Unchanged from prior Mars notes: MSP430FR5969-SP or equivalent, shielding, rad-tolerant path for the H-bridge. Magnets and carbide remain hard. This is the piece that makes the cell usable beyond low-Earth or Mars surface.

### Boost stage and pulse bank
36–48 V PP film bank and 12→48 V boost remain. Both are vacuum- and cold-compatible with the potting already specified.

## Space handling notes

- Thermal: radiation + conduction only. Pulse-only governor prevents coil hotspots.
- Cold-weld / outgassing: potting + coatings + PTFE lip close the primary paths.
- Free-float docking: magnetic soft-dock + mechanical pin provide the final latch; residual velocity still helps first contact.
- Radiation: rad-hard MCU path + shielding already in the Mars variant.

The same cell that survives polar-winter Mars now covers the bulk of pure-space environmental loads without further geometry changes.

## Mass and power

Mass budget rises modestly with the larger magnet and pin, but the prior ~40 g Mars total still holds as a paper ceiling. Power remains pulse-dominated and low.

Credit follows measured data. See BASELINE_UPGRADES.md for the shared mechanical and sealing details.
