# Extreme Environments — Inheritance Path

Design owner: Craig.  
Date: 2026-11-19.  
Status: speculative inheritance roadmap. Does not change current baseline geometry or locks.

The 25 mm cell is already sealed, pulse-only, SmCo, mechanically pinned, and coated. Later versions inherit those and add the following so the same lattice concept can survive the long run in every environment we can name.

## Already covered by current baseline + Mars path
- Vacuum / space thermal (radiation + conduction)
- Cold-weld and outgassing
- Mars dust and low pressure
- Moderate underwater (potting + pin load path to ~200 m paper)
- Radiation (Mars rad-hard MCU path)

## Later-version inheritance targets

### Deep ocean / high pressure (>200 m to full ocean depth)
- External pressure hull sleeve or lattice-level pressure vessel that the cells dock inside
- Or pressure-compensated oil-filled cells with flexible membranes
- Mechanical pin and detent already carry load; hull takes the hydrostatic force
- Target: cells remain functional at 4 km+ (paper)

### Cryogenic / extreme cold (below −125 °C)
- All-SmCo already helps
- Low-temperature lubricants or dry-film on pin and detent
- Capacitor and MCU cold-start heaters or fully cryo-rated parts
- Inherited from Mars pulse bank derating notes

### Extreme heat / high ambient
- Higher-temperature potting and coatings
- Active or passive thermal rejection faces (radiator tiles the lattice can form)
- Pulse governor already limits coil heat; extend threshold logic

### High radiation / deep space / nuclear
- Full rad-hard or rad-tolerant electronics path (already started in Mars variant)
- Shielding mass traded at lattice level (outer cells become sacrificial shield)
- Optical or hardened data links if copper fails

### Corrosive / chemical / saltwater long-term
- Full conformal + sacrificial anode options
- Ceramic or polymer face plates instead of bare metal
- Sealed interconnects with gold or equivalent contacts

### High-g / shock / vibration
- Pin and detent already provide positive lock
- Add secondary shear keys or lattice-level damping zones
- Potting helps component retention under acceleration

### Biofouling / biological
- Anti-fouling coatings on external faces
- Smooth or actively wiped surfaces (PTFE lip already a start)
- Sealed design prevents internal growth

### High-abrasion / industrial grit
- Carbide shim and PTFE lip already present
- Replaceable face tiles the lattice can swap
- Harder coatings as standard on later versions

## Inheritance rule
Any later version (v5+) must:
1. Keep the 25 mm envelope and Ø8.2 mm pocket unless a new lock is written
2. Inherit potting, pulse-only, SmCo, pin hard-lock, and coatings as the floor
3. Add environment-specific layers on top without breaking dock compatibility with earlier cells where possible

The goal is one lattice family that can be configured or upgraded to hold in ocean, space, cryo, heat, radiation, corrosion, shock, and bio environments for the long run. Paper until measured.

See BASELINE_UPGRADES.md and MARS_VARIANT.md for the current floor this builds on.
