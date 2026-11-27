# Application Modes — Inheritance Path

Design owner: Craig.  
Date: 2026-11-26.  
Status: speculative inheritance roadmap for v5+. Does not change current baseline geometry, Phase 0 locks, or measurement cards.

All modes inherit the 25 mm cell (Nd disc Ø6.0 × 2–3 mm hold, coil release-only, axial pin hard-lock, full cavity potting, face coatings, pulse-only). They add specialized faces, density behaviors, or power paths on top. Dock compatibility with earlier cells is preserved where possible. Paper until measured. Credit follows the measurement.

See EXTREME_ENVIRONMENTS.md for environmental inheritance and POST_2040_OUTLOOK.md for scale-change mechanisms these modes use.

## Modular components (Phase 0 face compatible, paper)
These are drop-in modules that mate via the locked Phase 0 20 mm face. Full specs:
- [EX_MOD.md](EX_MOD.md) — Extinguisher module (suppressant cartridge, heat/smoke stub).
- [BAR_MOD.md](BAR_MOD.md) — Barrier module (deployable panel for walls / containment).
- [SAR_MODES.md](SAR_MODES.md) — Search / Rescue / Signal mode package (sensor stubs + lattice behaviors).

All three remain paper until the Phase 0 face article exists and the measurement card is filled. Credit follows measured data.

## Flight Suit Mode (v5+)
Lattice forms a wearable full-body shell around a human payload (torso, limbs, helmet volume). Variable density: denser at joints, shoulders, hips, and primary load paths; lighter panels elsewhere. Axial pin + detent carry the suit’s own weight and acceleration loads. Soft inner clearance or optional compliant layer protects the wearer. Can collapse back into a dense transport brick using the existing inward-compaction path.

- Propulsion: dedicated thruster, ducted-fan, or high-thrust module cells dock into the back, palms, and boot soles. Shared power bus with a denser energy-cell zone (torso or backpack). Stabilization runs on the existing mesh (a few cells carry IMUs; the rest follow).
- Power & thermal: thrusters use a separate high-power path. Thermal budget is the real constraint under sustained thrust; lattice can form temporary radiator tiles. Structural cells stay on the baseline pulse-only budget.
- Control: wearer intent (IMU, simple gesture, or control app) maps to thrust vector and attitude. Safe-reserve and thermal cutoffs still apply.
- Status: paper. Flight claim requires measured thruster-module cards plus structural-cell cards.

## 1. Pure Exoskeleton / Strength Amplification Mode (no flight)
Same wearable full-body shell as the flight suit, minus thruster faces. Focus is load sharing and force multiplication at joints for lifting, carrying, or sustained posture.

- Structure: denser cells at shoulders, elbows, hips, knees, and spine. Lighter panels on limbs and torso. Pin + detent carry external loads; soft inner layer stays.
- Power: stays on the baseline bus (no separate thruster path). Optional denser energy zone in the torso or lower back for longer duty cycles.
- Behavior: local mesh coordinates joint-level assistance. Can lock into rigid support postures or stay partially compliant. Optional soft safety skin remains active on human-proximate surfaces.
- Reconfiguration: can still compact into a dense brick for transport. No propulsion faces required.
- Status: paper intermediate. Useful stepping stone before flight modules exist. Measured cards for structural cells are still the gate.

## 2. Armored / Protective Shell Mode
Higher-density outer layer optimized for impact, abrasion, or environmental protection. Can reconfigure density on the fly using the variable-density zones already outlined in the post-2040 outlook.

- Structure: outer cells use harder coatings or sacrificial face tiles. Inner layer stays softer or compliant. Pin hard-lock carries shear and impact loads.
- Behavior: density can shift toward high-threat faces (e.g., denser front and shoulders under impact risk). Lattice can form temporary thicker plates by stacking or nesting in localized zones.
- Inheritance: same potting, coatings, and pin path as baseline. Optional replaceable face tiles from the high-abrasion notes.
- Status: paper. No armor claim until measured impact/shear data exists on the filled cards.

## 3. Soft Companion / Clothing Mode
Sparse, low-force lattice that drapes or wraps instead of forming a rigid shell. Aimed at continuous wear, light sensing, or gentle assistance.

- Structure: low packing density, compliant docking, and mandatory soft safety skin on all human-proximate faces. 35 N human-contact interrupt stays active.
- Behavior: can follow body motion with minimal resistance, carry small specialized modules (sensors, low-power effectors, or light energy cells), or form temporary soft supports. Still uses the same pin hard-lock for any higher-load moments.
- Power: baseline bus only. Thermal and safe-reserve rules unchanged.
- Status: paper. Soft-skin and interrupt behavior already sketched in the community suites and post-2040 outlook; this mode just makes the wearable sparse configuration explicit.

## 4. Vehicle / Rideable Mode
Larger lattice forms a platform, open vehicle, or cargo carrier around one or more people or objects. Uses the same split/merge and expansion paths already written.

- Structure: dense structural and energy zones for the chassis and load paths; sparser panels for seating, cargo volume, or open deck. Pin + detent carry vehicle loads and acceleration.
- Mobility: optional specialized faces (wheels, tracks, or thrusters) dock into the lattice. Propulsion is additive, same as the flight suit. Can also be towed or pushed without its own drive.
- Behavior: can expand from a dense transport brick into rideable form, or split into smaller independent platforms. Mesh handles coordination and safe-reserve across subgroups.
- Status: paper. Requires measured structural-cell cards plus any propulsion or mobility-module cards.

## 5. Habitat / Shelter Mode
Expanded lattice forms an enclosed volume with sealed faces, basic thermal management, and optional pressure or environmental control. Builds directly on the extreme-environment inheritance paths.

- Structure: denser outer shell for sealing and load, lighter internal partitions or furniture zones. Sealed interconnects and coatings from the corrosive/chemical notes. Can incorporate pressure-compensated or oil-filled cells for higher-pressure variants.
- Behavior: uses outward expansion and variable-density zones to form walls, floor, and roof from a dense brick. Optional radiator tiles or thermal-rejection faces for heat. Soft safety skin on any internal human-proximate surfaces.
- Inheritance: potting, pin hard-lock, and coatings as the floor. Agency-interest gates (traceability, measured data) apply if the use case is sensitive.
- Status: paper. Sealing and environmental performance claims wait on filled measurement cards.

## Inheritance rule (all modes)
Any later version (v5+) must:
1. Keep the 25 mm envelope and Ø8.2 mm pocket unless a new lock is written
2. Inherit potting, pulse-only, Nd disc, pin hard-lock, and coatings as the floor
3. Add mode-specific layers on top without breaking dock compatibility with earlier cells where possible

Paper until measured. Credit follows data.
