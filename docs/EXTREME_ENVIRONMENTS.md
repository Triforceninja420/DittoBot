# Extreme Environments — Inheritance Path

Design owner: Craig.  
Date: 2026-11-19.  
Status: speculative inheritance roadmap. Does not change current baseline geometry or locks.

The 25 mm cell is already sealed, pulse-only, Nd disc, mechanically pinned, and coated. Later versions inherit those and add the following so the same lattice concept can survive the long run in every environment we can name.

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
- NdFeB N52 retains usable remanence at cryo; Nd disc specified with cold-derating margin on the pulse bank
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

### Exoskeleton / Flight (Iron Man suit mode)
Later version inheritance. The lattice forms a wearable full-body shell; specialized faces add flight.

- Structure: cells dock into torso, limbs, and helmet volume around a human payload. Variable density — denser at joints and load paths, lighter panels elsewhere. Mechanical pin + detent carry the suit's own weight and acceleration loads. Soft inner clearance or compliant layer protects the wearer.
- Propulsion: dedicated thruster, ducted-fan, or high-thrust module cells dock into back, palms, and boot soles. Shared power bus + denser energy-cell zone (torso or backpack). Stabilization runs on the existing mesh (IMU in a few cells, others follow).
- Reconfiguration: suit can collapse back into a dense transport brick using the same inward-compaction path already outlined in POST_2040_OUTLOOK.md.
- Requirements: inherits baseline potting, pulse-only magnets, Nd disc, and pin hard-lock. Thrusters are a separate power path. Thermal budget becomes real under sustained thrust. Dock compatibility with earlier cells preserved where possible.
- Status: paper. Flight is not in the current cell; it is an inheritance target for v5+ once propulsion faces exist.

### National-security / agency interest requirements
What organizations that have already been pointed at the design (or similar ones) typically want before they move past paper:

- Traceable supply chain on magnets (Nd disc), any rad-tolerant electronics, and critical mechanical parts. Lot traceability and material certs.
- Basic tamper / residue resistance: potting and coatings already help; later versions can add tamper-evident features or residue-limiting face treatments if the use case is sensitive.
- Confirmation the design is fully open: complete fab notes, no hidden process steps, measurement card ready for independent verification.
- Measured data on the public fixture (ON/OFF force, cycles, thermal) before any adoption discussion. Inheritance roadmaps alone are not sufficient.

These do not change the current baseline geometry. They are additional gates and documentation practices for any version aimed at that audience.

## Inheritance rule
Any later version (v5+) must:
1. Keep the 25 mm envelope and Ø8.2 mm pocket unless a new lock is written
2. Inherit potting, pulse-only, Nd disc, pin hard-lock, and coatings as the floor
3. Add environment-specific layers on top without breaking dock compatibility with earlier cells where possible

The goal is one lattice family that can be configured or upgraded to hold in ocean, space, cryo, heat, radiation, corrosion, shock, bio, and wearable flight environments for the long run. Paper until measured.

See BASELINE_UPGRADES.md and MARS_VARIANT.md for the current floor this builds on.
