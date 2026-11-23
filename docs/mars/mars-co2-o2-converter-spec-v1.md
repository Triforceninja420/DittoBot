# DB-MARS-CONV-001: CO2-to-O2 Converter Spec v1.0

## Overview
Electrolysis chamber that splits CO2 into carbon and oxygen using a solid oxide cell (SOEC) running at ~800 C.

## Core Components
1. **Electrolysis chamber**: SOEC at 800 C, splits CO2 into CO + O2
2. **Catalyst bed**: doped zirconia or perovskite, lowers energy per molecule
3. **O2 capture**: cold trap or membrane on output side grabs oxygen before recombination
4. **Carbon byproduct**: vented or stored as graphite

## Unit Design
- 50 kW per unit
- ~0.05 kg O2 per kWh
- ~2.5 kg O2 per sol per unit
- Zirconia cells castable from local materials by seed bots

## Scaling Math
- Target: 5.25 quadrillion kg O2
- 4 million units at 50 kW each = 200 TW draw
- Produces only 0.2 billion kg O2 per sol
- Shortfall: 26-million-fold at that rate
- Timeline: ~38,000 Mars years

## Bot Integration
Seed bot shells host converter units. Bots cast zirconia cells from regolith.

## Open Questions
- Catalyst degradation over time
- Dust survival of membrane and cold trap
- Thermal management at 800 C in thin atmosphere

## Cross-References
- DB-MARS-SEED-001 (seed bot)
- DB-MARS-GOV-001 (governors)
- DB-MARS-CONV-002 (high-output tower version)