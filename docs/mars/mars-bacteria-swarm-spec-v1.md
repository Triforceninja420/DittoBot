# DB-MARS-CONV-006: Bacteria Swarm Spec v1.1

## Overview
Engineered cyanobacteria swarm for planetary-scale O2 production. Zero power draw, self-replicating, grows on sunlight Mars already has. Trades speed for autonomy.

## Genetic Engineering (3 Stacked Traits + 3 Survival Fixes)

### Core Traits
1. **Radiation resistance**: DNA repair suite from Deinococcus radiodurans spliced in. Shrugs off radiation doses that shred normal cells.
2. **Cold tolerance**: Antifreeze proteins from Arctic fish. Cell membranes stay fluid below freezing instead of cracking.
3. **UV shielding**: Engineered to produce thick layer of mycosporine-like amino acids (natural sunscreens). Blocks UV that would fry anything on Martian surface.

### Survival Fixes (v1.1)
1. **Deployment volume**: Land 1 billion units instead of 1 million. Even at 8% survival, 80 million survivors restart exponential growth.
2. **Sporulation**: Bacillus subtilis endospores survive vacuum, radiation, centuries of dormancy. Wake up when conditions improve. Dim-sun years become waiting rooms, not death sentences.
3. **Metabolic flexibility**: Switch from sunlight to hydrogen when sun's too weak.

## Simulation Results

### v1.0 (20 runs)
- 7 of 8 scenarios cleared
- Base case: 669 sols (1 Mars year), 79% survival, hit 1-quintillion-unit cap
- High radiation: ~6,500 sols (~18 Earth years)
- Deep cold: ~6,500 sols
- UV spike: 35,000 sols (~97 Earth years), 32% survival
- Low inoculum: <1,200 sols (replication compounds fast)
- Dust-storm years: 914 sols
- Best case: 330 sols (half a Mars year)
- Worst case FAILED: radiation 50%, cold 50%, UV 40%, tiny inoculum, dim sun. 8% survival, never recovered. 200,000 sols, 548 Earth years, 7,000 kg O2.
- CO2 held 10-11 trillion tonnes in every cleared run (from 25T pool)

### v1.1 Improved (20 runs)
- ALL 20 runs cleared
- Best, worst, average: 96 sols (~1/3 Mars year)
- Average survival: 11% (up from 8%)
- Sporulation + metabolic flexibility doing heavy lifting in worst case
- Billion-unit deployment gives seed mass to compound from

## Role in Green Mars Stack
- Converters (DB-MARS-CONV-005) handle habitat-scale O2 in months
- Bacteria handle planetary scale over decades to a century
- Bacteria burn CO2 slower than converters — the whole point
- Zero power draw, self-replicating

## Open Questions
- Genetic stability across Martian generations
- Horizontal gene transfer risks
- Containment if traits escape to Earth-origin microbes
- Long-term ecosystem effects of engineered organisms

## Cross-References
- DB-MARS-CONV-005 (dual-path, bacteria as long game)
- DB-MARS-SEED-001 (deployment via seed bots)
- DB-MARS-GOV-001 (density governor applies to bot swarm, not bacteria)