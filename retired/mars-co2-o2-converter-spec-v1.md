# DB-MARS-CONV-001: CO2-to-O2 Converter Spec v1.1

**Executive Summary:** Solid-oxide electrolysis cell (SOEC) at 800 °C splits CO₂ into CO + O₂. Catalyst bed (doped zirconia/perovskite) lowers energy per molecule. Cold trap or membrane captures O₂ before recombination. Carbon stored as graphite. Unit: 50 kW, ~0.05 kg O₂/kWh → ~2.5 kg O₂/sol. Scaling to 5.25×10¹⁵ kg target needs 4×10⁶ units (200 TW) producing only 0.2×10⁹ kg/sol — 26-million-fold shortfall, ~38,000 Mars years. This v1 is the baseline that every later revision improves on.

**Design Owner:** Craig. Paper/simulation only. Constants cited below.

---

## 1. Overview

Electrolysis chamber splitting CO₂. Running temperature: 800 °C. [SOEC operating range: 700–900 °C, standard solid-oxide literature]

## 2. Core Components

1. **Electrolysis chamber:** SOEC at 800 °C → CO₂ → CO + O₂
2. **Catalyst bed:** doped zirconia or perovskite — lowers activation energy per molecule
3. **O₂ capture:** cold trap or membrane on output side, prevents recombination
4. **Carbon byproduct:** vented or stored as graphite

## 3. Unit Design

| Parameter | Value | Unit |
| :-------- | :---- | :--- |
| Power per unit | 50 | kW |
| O₂ yield | 0.05 | kg/kWh |
| O₂ per sol per unit | 2.5 | kg |
| Cell material | zirconia (YSZ) | castable from regolith by seed bots |

## 4. Scaling Math (to 5.25×10¹⁵ kg O₂ target)

| Parameter | Value | Unit |
| :-------- | :---- | :--- |
| Target O₂ | 5.25×10¹⁵ | kg |
| Units needed @ 50 kW | 4×10⁶ | units |
| Total draw | 200 | TW |
| O₂ produced | 0.2×10⁹ | kg/sol |
| Shortfall | 26×10⁶ | × |
| Timeline | ~38,000 | Mars years |

Mars atmospheric CO₂ inventory: ~25×10¹² t [source: standard Mars atmosphere models, e.g. NASA]. Splitting it all yields ~13×10¹² t O₂ — this is the CO₂ depletion ugly flag addressed in DB-MARS-CONV-004/005.

## 5. Bot Integration

Seed bot shells (DB-MARS-SEED-001) host converter units. Bots cast zirconia cells from regolith.

## 6. Open Questions

- Catalyst degradation rate over time
- Dust survival of membrane and cold trap
- Thermal management at 800 °C in 6 mbar atmosphere

## 7. Cross-References

- DB-MARS-SEED-001 (seed bot)
- DB-MARS-GOV-001 (governors)
- DB-MARS-CONV-002 (high-output tower, v2)

---
*RETIRED 2026-11-22. Superseded by mars-co2-o2-converter-spec-v3.md (DB-MARS-CONV-003) and mars-co2-o2-converter-spec-v4.md (DB-MARS-CONV-004). Kept for audit trail.*