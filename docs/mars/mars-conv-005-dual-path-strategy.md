# DB-MARS-CONV-005: Dual-Path Strategy Spec v1.1

**Executive Summary:** Turns the CO₂-depletion ugly flag (DB-MARS-CONV-004) into a loop. Path 1: direct water splitting — electrolyzers pull O₂ from ice, park H₂ as fuel (kills CO₂ burn rate). Path 2: carbon import from Phobos/Deimos when CO₂ drops below 40% of 25×10¹² t starting pool. Sabatier loop: CO₂ + H₂ → CH₄ + H₂O; Bosch: CO₂ + H₂ → C + H₂O. Per-unit (v5): 0.24 kg O₂/sol at 20 W, 2 kWh/kg. 50×10⁹ units @ 1 TW = 12×10⁶ t O₂/sol. CO₂ alone supplies 9.1×10¹² t — exceeds 5.25×10¹⁵ kg target on mass but timeline is ~437,000 sols (1,200 Earth yr) at 1 TW; ~35,000 sols (100 Earth yr) at 12 TW. CO₂ drawdown: 25→~10×10¹² t.

**Design Owner:** Craig. Paper/simulation only.

---

## 1. Overview

Two sequenced paths. Path 1 is primary; Path 2 is the gated backstop.

## 2. Path 1: Direct Water Splitting

Electrolyzers split water ice (DB-MARS-ICE-001 supply). O₂ → atmosphere. H₂ parked as fuel, not recycled into CO₂ loop. Eliminates net CO₂ consumption for primary production.

## 3. Path 2: Carbon Import (gated)

Trigger: atmospheric CO₂ < 40% of 25×10¹² t. Mass drivers haul carbon-rich regolith from Phobos (>10×10¹⁵ kg [source: Phobos bulk density/volume estimates]) and Deimos. Regenerates greenhouse gas.

## 4. Loop Logic (Sabatier + Bosch)

- CO₂ split → O₂ + CO
- CO + H₂ (from ice miners) → Sabatier → CH₄ + H₂O
- H₂O split → H₂ + O₂ (O₂ to atmosphere, H₂ recycles)
- Bosch variant: CO₂ + H₂ → C (graphite for structures/fuel) + H₂O
- Net: CO₂ is working fluid, not fuel tank

## 5. Per-Unit Numbers (v5)

| Parameter | Value | Unit |
| :-------- | :---- | :--- |
| O₂ output | 0.24 | kg/sol/unit |
| Power | 20 | W |
| Specific energy | 2 | kWh/kg O₂ |
| Fleet @ 50×10⁹ units, 1 TW | 12×10⁶ | t O₂/sol |
| CO₂ supply | 9.1×10¹² | t (exceeds target mass) |
| Timeline @ 1 TW | ~437,000 | sols (1,200 Earth yr) |
| Timeline @ 12 TW | ~35,000 | sols (100 Earth yr) |
| CO₂ drawdown | 25→~10 | ×10¹² t |

## 6. Cross-References

- DB-MARS-CONV-004 (base architecture)
- DB-MARS-ICE-001 (water for Path 1)
- DB-MARS-GOV-001 (governors)
- DB-MARS-CONV-006 (bacteria swarm, long game)
