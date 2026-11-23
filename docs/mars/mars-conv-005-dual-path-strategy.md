# DB-MARS-CONV-005: Dual-Path Strategy Spec v1.0

## Overview
Turn the CO2 depletion ugly flag into a loop. Two paths sequenced.

## Path 1: Direct Water Splitting
Electrolyzers pull oxygen from ice, park hydrogen as fuel instead of feeding it back into CO2 recycling. Kills the CO2 burn rate problem.

## Path 2: Carbon Import (when necessary)
Import carbon from Phobos and Deimos to top up the atmosphere if CO2 drawdown gets too aggressive.

## Loop Logic
- CO2 split into O2 + CO
- CO goes to Sabatier reactor with H2 from ice miners → methane + water
- Water splits back into H2 + O2
- Cycle repeats

## Per-Unit Numbers (v5)
- Output: 0.24 kg O2 per sol per unit at 20 W, 2 kWh/kg
- 50 billion units at 1 TW = 12 million tonnes O2 per sol
- CO2 alone supplies 9.1 trillion tonnes — more than 5.25 quadrillion kg target
- Timeline: ~437,000 sols (~637 Mars years / 1,200 Earth years) at 1 TW
- At 12 TW: ~35,000 sols (~53 Mars years / 100 Earth years) — inside century
- CO2 drawdown: 25T → ~10T tonnes remaining

## Cross-References
- DB-MARS-CONV-004 (base architecture)
- DB-MARS-ICE-001 (water supply for Path 1)
- DB-MARS-GOV-001 (governors)
- DB-MARS-CONV-006 (bacteria swarm for long game)