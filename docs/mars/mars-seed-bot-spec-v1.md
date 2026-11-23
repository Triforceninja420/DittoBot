# DB-MARS-SEED-001: Mars Seed Bot Spec v1.0

## Overview
Seed bot for Mars surface deployment. One kilo, solar-powered, no battery beyond small capacitor bank. Carries: 1-meter Fresnel lens, magnetic rake for iron extraction, kiln size of a toaster. No arms, no legs, no fancy joints.

## Phase Zero
Three seeds land, each with a 1-meter Fresnel lens, magnetic rake, and shoebox kiln. They print sintered regolith tiles (~dinner-plate size) and stack them in a spiral ring around the lens to shade it and block dust. Once stable, the lens focuses tighter and the kiln runs hotter, casting tubes, plates, and brackets. Those bolt into a frame for a bigger kiln. Bigger kiln means denser sinter and a cast chassis — bot number four, built from dirt and sunlight.

## Bot 1
Five kilos, real print head, starts making copies of itself from tiles and brackets already in the dirt. From there exponential: one seed, one ring, one chassis, one factory.

## Replication Logic
- Conservative doubling: 10-14 days per copy
- Optimistic doubling: 5-7 days per copy
- Energy per tile: 2-4 kWh
- Energy per full bot replication: 30-50 kWh
- At 10-day doubling: 1 trillion units in ~11 years (theoretical ceiling before physical limits)

## Materials Table (from local regolith/ice)
- Silicon: compute and structure
- Iron: magnetic structures (already present as magnetite, no reduction needed)
- Aluminum: oxidized for structure
- Oxygen: atmospheric byproduct
- Magnesium, Calcium: alloy components

## Energy Budget
- Sintering instead of full melting: 800-1200 C instead of 1500+ C
- Solar concentrators with Fresnel lenses hit that with fraction of power
- Magnetic separator before sintering for iron
- Seed bot: 1 kg with small lens array, magnetic rake, basic print head
- Staged growth: slightly bigger kiln builds slightly bigger bot

## Mars-Specific Safety
- RTG hybrid: Earth-made plutonium heart, Mars-made housing/thermocouple/radiator fins
- One cargo drop per RTG heart, bots build the rest around it
- Keeps Earth supply chain to one small high-value item

## Open Questions
- Exact doubling time depends on replication logic and materials table validation
- Energy-per-copy numbers need Earth-simulant prototype lock
- Thermal cycling durability of sintered regolith in Mars environment

## Next Steps
- Earth prototype test on Mars simulant to verify energy numbers
- Cross-link to Phase 0 docking protocol (DB-P0-FACE-TP-001) and Master Notebook
- Credit split: designer (Craig) name locked, builder TBD

## Cross-References
- DB-MARS-CONV-001 through DB-MARS-CONV-006 (converter chain)
- DB-MARS-ICE-001 (ice mining)
- DB-MARS-GOV-001 (governors)
- Phase 0: DB-P0-FACE-TP-001 Rev A