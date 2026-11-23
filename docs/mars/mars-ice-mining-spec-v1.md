# DB-MARS-ICE-001: Ice Mining Spec v1.0

## Overview
Fastest route is orbital-first. Use HiRISE and SHARAD imagery to pick three candidate sites at mid-latitudes where ice is shallowest (under 1 meter of regolith). Land one seed bot at each as a scout.

## Scout Protocol
1. Orbital targeting: HiRISE + SHARAD pick 3 mid-latitude sites
2. Three scout seed bots, each drills a shallow core with thermal probe
3. Beams back whether ice is within reach
4. Winning site gets the full swarm
5. No waiting on second launch window — one scout mission, three holes, one winner

## Mining Hardware
- Scoop arm added to seed bot design
- Heated hopper sublimates ice straight into vapor for converters or storage tanks
- Bots already have print heads and magnetic rakes

## Throughput Math
- 1,000 bots mining 2-5 tonnes per sol
- 3,500 tonnes of water per sol (rounding error vs converter demand)

## Open Questions
- Dust filtration in sublimation hopper
- Polar fallback sites if mid-latitudes disappoint
- Ice purity verification from orbital data alone

## Cross-References
- DB-MARS-SEED-001 (seed bot base)
- DB-MARS-CONV-001 (converter demand for water)
- Sabatier/Bosch loop coupling (DB-MARS-CONV-005)