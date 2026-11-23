# DB-MARS-GOV-001: Swarm Governors Spec v1.1

**Executive Summary:** Two governors control swarm growth. Either can halt alone; both must clear before resume. Density cap: 1 bot/m² usable surface (raised to 600×10⁹ units/m² for CONV-004 scaling). Power cap: hard pause at 1.5 PW (full stop, no soft restart), soft reroute (halted bots feed converters), resume after 10 sols under cap. Stress test (15 runs @ 12 TW): base 245 sols, worst case 309 sols/26 pauses, best 189 sols. All governors hold; nothing exceeds one Mars year.

**Design Owner:** Craig. Paper/simulation only.

---

## 1. Overview

Governors prevent the swarm from eating the planet or brown-outing the grid.

## 2. Governor 1: Density Cap

- Cap: 1 bot per m² usable surface (base); raised to 600×10⁹ units/m² for CONV-004 matrix scaling test
- At cap: new seeds stop; existing switch to converter production only
- Prevents planetary carpeting

## 3. Governor 2: Power Cap

- **Hard pause:** ALL replication killed instantly at 1.5 PW draw. No soft restart.
- **Soft reroute:** halted bots' output → running converters. Nothing idles.
- **Resume:** only after 10 consecutive sols under cap.

## 4. Stress Test Results (15 runs @ 12 TW)

| Scenario | Result | Notes |
| :------- | :----- | :---- |
| Base | 245 sols | 186K towers, 1.15 PW peak, 0 pauses |
| 10% noise | 244–245 sols | same tower counts |
| 25% noise | 244–245 sols | same tower counts |
| Low efficiency (50%) | 259 sols | 9 pauses, 2 PW spike |
| Tight cap (0.75 PW) | 245 sols | 9 pauses, clears via reroute |
| Slow start (0.1× seeds) | 292 sols | — |
| Big start (10× seeds) | 197 sols | — |
| Worst case | 309 sols | 26 pauses |
| Best case | 189 sols | — |

All governors hold. Nothing exceeds one Mars year.

## 5. Cross-References

- DB-MARS-SEED-001 (replication governed)
- DB-MARS-CONV-003..005 (power draw governed)
- DB-MARS-CONV-006 (bacteria swarm — separate from bot governors)
