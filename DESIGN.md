DittoBot Design Specs + BOM Backup
Project: DittoBot / Voxel Box Bot
Inventor: Craig Edward Ralls
Status: Fully Green-lit (Paper Baseline)
Date: August 3, 2026

───

1. Core Architecture (All Versions)

• Heterogeneous modules: Energy / Structural / Compute
• Hybrid docking: Electro-permanent magnets (EPM) + mechanical pin lock
• 12 V nominal power-sharing bus
• 5-state docking machine per face: Approach → Soft Dock → Verify → Hard Lock → Operational (+ Fault)
• Safe Reserve energy rule (no reconfiguration if it drops below safe threshold)
• Layered safety interlocks
• Non-critical path only for lunar/Mars use (snowball / opportunistic)

───

2. Version Specs

V0.9 (Phase 0–2) — Lab Baseline (2026–2029)
• Node size: 20 × 20 × 20 mm (8 cm³)
• EPM normal force: ≥ 12 N (zero power)
• Hard-lock shear: ≥ 40 N
• Alignment capture: ±2.5 mm lateral / ±6–7° (with passive chamfers)
• Cycle life target: 2,000–3,000 cycles
• Continuous face current: 1.25 A (15 W)
• Energy Module capacity: ~1.9 Wh (at ~600 Wh/L)
• Primary goal: Prove latch, power transfer, thermal behavior, and basic multi-module docking

V1.0–V1.2 (Phase 3) — Supervised Industrial (2029–2035)
• Node size: Still primarily 8 cm³ (optional 6–7 cm³ later)
• Cycle life: ≥ 5,000
• Face current: 1.5–2.0 A
• Energy Module capacity: 2.5–3.5 Wh
• Scale: 60–200 modules
• Focus: Reliable supervised industrial use on Earth

V1.3–V1.5 (Phase 4) — Capability Growth (2035–2040)
• Node size: Mix of 8 cm³ + new 4–5 cm³ nodes
• Higher autonomy, reduced supervision
• Scale: 200–1,000+ modules
• Outdoor + early planetary-analog capability

V2.0 (Phase 5) — Dense Programmable Matter (Post-2040)
• Node size: ≤ 4 cm³ dominant
• High-density, high-autonomy swarms
• Scale: Thousands of modules
• Mature industrial + companion forms

───

3. Phase 0 Single-Face Demonstrator (First Hardware Target)

Contents of one 20 mm face:
• • 4× EPMs: AlNiCo 5 Ø5.0×8.0 + NdFeB N42 Ø5.0×8.0, 1018 poles 1.00×8.00×11.0 mm, finished height 8.0 mm, 180±10 t 34 AWG
• Central mechanical pin lock (1.8 mm hardened pin, ~3+ mm engagement)
• Short-stroke actuator for the pin
• 6× redundant gold-plated spring power contacts (wipe action)
• Passive alignment chamfers / ridges
• Basic sensing: current, temperature, lock state, continuity
• Small MCU for state machine + logging

Success Criteria:
• Soft-dock capture ≥ 90% at ≤ 2.5 mm offset
• Hard-lock success ≥ 95% after valid soft-dock
• Sustained shear ≥ 40 N with no permanent deformation
• 1.25 A continuous for ≥ 10 minutes without thermal throttle
• 2,000 docking cycles with acceptable degradation

───

4. High-Level Bill of Materials (Phase 0 / V0.9)


Category
Key Requirements
Notes

Electro-permanent magnets
• 4× EPM as locked in PHASE0.md (N42 + AlNiCo 5 Ø5×8, 1018 poles) | Critical path. N35 substitute only if N42 stock is gone.

Mechanical lock pin
1.8 mm hardened steel (or equivalent), 3+ mm engagement
Precision ground or custom

Pin actuator
Short-stroke, low-profile (solenoid or micro-cam)
Must fit remaining volume

Power contacts
6× gold-plated spring contacts, ≥0.5 A each, wipe action
Pogo or leaf spring

Face plate
0.8–1.2 mm aluminum or stainless (heat spreading)
Machined or laser-cut

Alignment features
Chamfers / shallow ridges on mating face
Integrated into face plate

Local reinforcement
Metal inserts around pin and receptacle
For 40 N shear load path

Sensing
Current, temperature, lock state
Minimal set

Microcontroller
Small MCU capable of 5-state machine + sensing
Test control and data logging

Local energy buffer
Small cell or supercap on Structural/Compute modules
Ride-through only

Energy Module battery
Higher volume fraction, targeting ~1.9 Wh
Main energy reservoir



Exact vendor part numbers are not frozen yet. The table defines required performance and form factors.

───

5. Key Design Rules That Carry Forward

• Evidence before shrinking node size
• Interface and protocol stability preferred across versions
• Energy safety rules are never removed
• Safety interlocks are only strengthened, never weakened
• Heterogeneity preferred over pure homogeneous modules
• Lunar/Mars use remains strictly opportunistic and non-critical-path

───

6. Residual-Hold Hardening (stacked, 2026-11-19)

Sim (2026-11-18) found the 25 mm cell's zero-hold path rests on ~5.7 N residual
against a clean keeper at ~0.1 mm gap. Dust, tilt, or a worn shim collapses it.
Three levers stack without touching locked option-A geometry (Ø8.2 pocket, Ø6 disc):

1. SmCo 2:17 upgrade path — swap the NdFeB half of the Ø6 × 4 stack for
   samarium-cobalt (Br ~1.05 T, H_c ~720 kA/m, 350 °C max operating temp).
   NdFeB N52 stays the ON-state workhorse (Br ~1.45 T). SmCo's job is
   environmental stability: residual flux holds across temperature swings and
   corrosion that would degrade NdFeB above ~80–150 °C. Same Ø6 × 4 envelope,
   so the pocket and coil annulus are untouched. ON force scales down ~28%
   with the lower Br — that is the trade for a hold that survives Mars-class
   thermal cycling. Not a room-temp residual upgrade; a thermal-stability one.

2. Compliant pole tips — 0.2–0.4 mm silicone or spring-steel washer bonded
   to the latch face. Absorbs dust particles and face tilt up to ~2° before
   the magnetic gap opens. Must be non-magnetic and thin enough that ON
   Maxwell stress is not diluted below the 3 N Phase-0-class gate when adapted.
   This is the biggest lever for the dust/gap failure mode the sim flagged.

3. Passive mechanical detent — shallow annular groove (0.3 mm deep) in the
   carbide/440C shim paired with a matching ridge on the mating plate.
   Magnetism does capture and positioning; the detent does the final
   mechanical lock. Shear load path moves from magnetic friction to geometry,
   which is what the 40 N shear gate was always really about.

Any one lever roughly doubles dust/tilt tolerance. Stacking two makes the
5.7 N residual a floor, not a cliff. None of this changes option-A
dimensions, coil winding, driver, or success tests — it hardens the
interface around them.

Open question for the bench: does the SmCo half need its own OFF-pulse
current, or does the existing reverse-polarity pulse (0.292 T release
threshold from sim) still clear it? Measure before freezing.

───

This is the complete backup package. You can copy everything above straight to your phone.

(Design is from August 3rd, 2026. Info may have been updated since)