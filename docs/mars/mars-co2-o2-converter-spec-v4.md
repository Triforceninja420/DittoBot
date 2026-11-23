# DB-MARS-CONV-004: CO2-to-O2 Converter Spec v4.1

**Executive Summary:** Solid towers don't scale to planetary O₂ — 50×10⁹ towers would consume 10% of Mars's top-meter regolith mass. Pivot: thin-film perovskite on 1 mm sintered regolith sheets, 20 kg/unit. 50×10⁹ units cover 5×10⁵ km² (~0.3% of Mars) at 1 PW draw (inside governor cap). Fleet mass: 1×10⁹ t. Fab energy: 40–80 TWh (swarm covers in <1 sol at peak). Ugly flag: Mars CO₂ ~25×10¹² t; splitting all yields ~13×10¹² t O₂ but pressure collapse freezes the planet → fixed by DB-MARS-CONV-005 loop. Projected timeline with governors: ~260 sols base, ~500 sols worst case.

**Design Owner:** Craig. Paper/simulation only.

---

## 1. Overview

Architecture pivot from towers (v3) to distributed catalytic matrix.

## 2. Architecture Change

| Parameter | v3 (towers) | v4 (matrix) |
| :-------- | :---------- | :---------- |
| Form factor | 150 m towers | 1 mm sheets |
| Mass/unit | 1,000 t | 20 kg |
| Units for planetary | 50×10⁹ (10% top-meter mass) | 50×10⁹ (0.3% surface) |
| Power | 200 TW | 1 PW |
| Fleet mass | 1.8×10⁶ t | 1×10⁹ t |
| Fab energy | 3,500–7,000 TWh | 40–80 TWh |

## 3. Ugly Flag (CO₂ Depletion)

Mars atmospheric CO₂: ~25×10¹² t [source: standard Mars GCMs]. Full split → ~13×10¹² t O₂ but pressure collapse kills greenhouse → freeze. **Fix: DB-MARS-CONV-005 dual-path loop** (water splitting + carbon import from Phobos/Deimos, 10×10¹⁵ kg available [source: Phobos mass estimates]).

## 4. Cross-References

- DB-MARS-CONV-003 (tower baseline)
- DB-MARS-CONV-005 (dual-path fix)
- DB-MARS-ICE-001 (water supply)
- DB-MARS-GOV-001 (governors)
