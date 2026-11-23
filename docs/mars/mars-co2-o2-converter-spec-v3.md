# DB-MARS-CONV-003: CO2-to-O2 Converter Spec v3.1

**Executive Summary:** 50× output per tower at 1,400 °C. Fleet: 1,760 towers instead of 88,000. Per tower: ~1,375 kg CO₂/sol feed, 2 kWh/kg O₂ specific energy, 42 kW average draw, ~500 kg O₂/sol output. Fleet: 74 GW total — well under 1.5 PW governor cap. Dry mass ~1,000 t/tower (1.8×10⁶ t fleet). Fab energy 2–4 TWh/tower (3,500–7,000 TWh fleet) = 2–5 sols of 1.5 PW swarm output. Honest flag: 1,760 towers is habitat-scale O₂ only. Full planetary O₂ needs tens of billions of towers → DB-MARS-CONV-004 pivot.

**Design Owner:** Craig. Paper/simulation only. All constants derived or cited.

---

## 1. Overview

50× efficiency gain over v2 via higher temperature and denser catalyst packing.

## 2. Per-Tower Numbers

| Parameter | Value | Unit | Derivation |
| :-------- | :---- | :--- | :--------- |
| CO₂ feed | 1,375 | kg/sol | 2CO₂→2CO+O₂ stoichiometry at 50× v1 rate |
| Specific energy | 2 | kWh/kg O₂ | Electrolysis enthalpy + losses |
| Power draw | 42 | kW avg | 500 kg O₂ × 2 kWh/kg ÷ 24 h |
| O₂ output | 500 | kg/sol | 50× v1's 2.5 kg/sol × 20 |

## 3. Fleet Numbers (1,760 towers)

| Parameter | Value | Unit |
| :-------- | :---- | :--- |
| Total power | 74 | GW |
| vs 1.5 PW cap | 0.05× | — |
| Dry mass/tower | ~1,000 | t (sintered regolith ceramic) |
| Fleet dry mass | ~1.8×10⁶ | t |
| Fab energy/tower | 2–4 | TWh |
| Fleet fab energy | 3,500–7,000 | TWh |
| Build time @ 1.5 PW | 2–5 | sols |

## 4. Honest Flag

1,760 towers = habitat/greenhouse O₂. Planetary atmosphere replacement needs tens of billions of towers (mass + land-use limits) → DB-MARS-CONV-004 distributed matrix.

## 5. Cross-References

- DB-MARS-CONV-002 (tower architecture)
- DB-MARS-CONV-004 (matrix pivot)
- DB-MARS-GOV-001 (governors)
- DB-MARS-SEED-001 (fab by seed bots)
