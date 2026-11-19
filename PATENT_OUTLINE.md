# Provisional Patent Outline — DittoBot Cell (25mm Option A)

**Status:** Draft for attorney review. Not legal advice. File before publishing measured data.

**Inventor:** Craig Ralls
**Priority date target:** Before first public disclosure of measured latch/release forces.

## Title
Modular Electromagnetic Cell with Compliant Pole Tips, Carbide Detent Ridge, and Electrostatic Dust Bias for Extreme-Environment Docking

## Background
- Modular robotic systems require cells that dock and undock repeatedly under dust, thermal cycling, and vacuum.
- Prior art: electromagnetic docking (e.g., CubeSat interfaces), mechanical latches, passive magnetic couplers. None combine active EPM latching with compliant pole tips, a replaceable carbide consumable ridge, and electrostatic groove bias.

## Summary of the Invention
A 25 mm cubic cell using an electromagnet (EPM) for active ON/OFF latching against a ferromagnetic keeper, with three hardening layers:

1. **Compliant pole tips** — silicone or spring-steel layer (~188 kN/m stiffness) absorbing dust grains and angular misalignment up to ~2° without opening the magnetic gap.
2. **Carbide ridge + replaceable consumable shim** — groove depth 0.3 mm, minimum engagement 0.15 mm, target 0.25–0.30 mm. Tungsten-carbide or ceramic ridge face limits shim wear to ~0.05 µm/cycle; shim swapped every ~250 cycles before engagement falls below minimum. OFF-load floor remains >40 N (structural gate) throughout 2000-cycle runs.
3. **Electrostatic groove bias (Mars variant only)** — small DC bias on groove walls repelling electrostatically sticky ~1 µm grains in low-pressure CO2 before they pack the 0.3 mm gap.

Magnet: SmCo (samarium cobalt) for coercivity retention across −125 °C to +80 °C. NdFeB optional for Earth-only builds where residual force matters more than thermal range.

Release: reverse-field pulse bank, 36–48 V polypropylene-film capacitors (ESR-stable at cryo), delivering 0.5–0.8 T reverse field to clear SmCo's operating point. 12 V rail insufficient; 48 V clears with margin.

Thermal: pulse-only coil drive on Mars/vacuum; firmware governor blocks continuous soak above plate-temp threshold. Radiation to cold ambient is the heatsink.

Driver: TI MSP430FR5969-SP (space-grade FRAM, SEL-immune to 72 MeV, 50 krad TID) for Mars variant; standard MCU acceptable for Earth.

Mechanical capture of PTFE wiper lip into ridge (no adhesive — PTFE surface energy ~18 mN/m; etched bond strips at cryo). Chamfered groove entry for self-cleaning geometry.

## Independent Claims (draft)
1. A docking cell comprising an electromagnet, a ferromagnetic keeper, and a compliant pole tip disposed between magnet and keeper, the tip having stiffness sufficient to compress a dust grain of at least 50 µm under less than the residual magnetic force of the cell.
2. A docking cell as in claim 1, further comprising a groove-and-ridge mechanical detent with a replaceable consumable shim, the shim having a wear rate below 0.1 µm per dock cycle against a carbide or ceramic ridge face.
3. A docking cell as in claim 2, further comprising an electrostatic bias electrode on at least one groove wall configured to repel micron-scale charged particles in a CO2 atmosphere below 1 kPa.
4. A method of releasing a docked cell by discharging a capacitor bank of at least 36 V through the electromagnet coil to generate a reverse field exceeding the coercivity of the magnet at operating temperature.

## Dependent Claims (key ones)
- SmCo magnet with Br retention above 4 N residual at −125 °C.
- Polypropylene-film pulse capacitors rated ≥100 V, capacitance ≥440 µF.
- PTFE wiper lip mechanically captured (swaged/molded) into ridge, no adhesive.
- Firmware thermal governor inhibiting continuous coil current when plate temperature exceeds threshold.
- Boost stage 12 V→48 V at ≤1 W, mass ≤10 g.
- Rad-hardened MCU with SEL immunity ≥70 MeV for space variant.

## Prior Art to Distinguish
- CubeSat electromagnetic docking (e.g., iBoss, Astrobee interfaces) — no compliant tips or consumable ridge.
- Passive magnetic couplers (Magswitch-style) — no active release pulse, no detent.
- Electrostatic dust mitigation (e.g., lunar regolith studies) — applied to surfaces, not groove geometry.
- Consumable shims in tooling — not combined with magnetic latching cells.

## Filing Notes
- Provisional: 12-month priority, ~$75–300 USPTO fee (micro entity), no formal claims required but outline above strengthens it.
- Convert to non-provisional before 12 months or lose priority.
- Public GitHub disclosure starts a 12-month clock in the US (grace period) but kills foreign priority — file before any further public posts of measured data.
- Attorney needed for final claims language and drawings.

## Open Items for Attorney
- Exact claim scope on electrostatic bias (may be too narrow/obvious alone).
- Whether consumable shim constitutes patentable subject matter as a method vs. apparatus.
- International filing (PCT) decision before 12 months.
