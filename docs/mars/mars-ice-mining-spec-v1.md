# DB-MARS-ICE-001: Ice Mining Spec v1.1

**Executive Summary:** Orbital-first ice scouting using HiRISE and SHARAD imagery to pick three mid-latitude sites where ice is under 1 m of regolith. One scout seed bot per site drills a shallow core with a thermal probe and beams results. Winning site gets the full swarm — no second launch window. Mining hardware: scoop arm + heated hopper sublimating ice to vapor. Throughput: 1,000 bots × 2–5 t/sol = 3,500 t water/sol (rounding error vs converter demand).

**Design Owner:** Craig. Paper/simulation only.

---

## 1. Overview

Fastest route is orbital targeting, not blind drilling. Ice is the water supply for Path 1 of DB-MARS-CONV-005 (direct water splitting).

## 2. Scout Protocol

1. **Orbital targeting:** HiRISE (NASA/JPL Mars Reconnaissance Orbiter) + SHARAD (Mars Reconnaissance Orbiter radar) pick 3 mid-latitude sites [source: NASA PDS orbital datasets]
2. Three scout seed bots, each drills shallow core with thermal probe
3. Beam back: ice within reach? (yes/no + depth)
4. Winning site gets full swarm
5. One scout mission, three holes, one winner — no second launch window

## 3. Mining Hardware

- Scoop arm added to seed bot design (DB-MARS-SEED-001)
- Heated hopper sublimates ice → vapor for converters or storage tanks
- Bots already carry print heads and magnetic rakes

## 4. Throughput Math

| Parameter | Value | Unit |
| :-------- | :---- | :--- |
| Bots mining | 1,000 | units |
| Per-bot rate | 2–5 | t water/sol |
| Fleet rate | 3,500 | t water/sol |
| vs converter demand | rounding error | — |

## 5. Open Questions

- Dust filtration in sublimation hopper
- Polar fallback if mid-latitudes disappoint
- Ice purity from orbital data alone (needs ground truth)

## 6. Cross-References

- DB-MARS-SEED-001 (seed bot base)
- DB-MARS-CONV-001 (converter water demand)
- DB-MARS-CONV-005 (Sabatier/Bosch loop coupling)
