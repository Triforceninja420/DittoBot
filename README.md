# DittoBot Documentation Index

All current design sources live here.
Design owned by Craig. Programmable matter voxel lattice. 25 mm cell is the main design.

## Current baseline (25 mm cell) — main design

| Doc | What it is |
| :-- | :-- |
| [BASELINE_UPGRADES.md](docs/BASELINE_UPGRADES.md) | 2026-11-19 upgrades now standard |
| [DESIGN.md](docs/DESIGN.md) | Architecture, version ladder, lock philosophy |
| [BUILD.md](docs/BUILD.md) | Fab handoff |
| [CONTROL_APP.md](docs/CONTROL_APP.md) | Mobile + PC control system outline |
| [PAPER_STATUS.md](docs/PAPER_STATUS.md) | What is fixed without measurements |
| [COIL_REVISION.md](docs/COIL_REVISION.md) | Coil and thermal history |
| [LOCKS.md](docs/LOCKS.md) | Process locks (18 total, 9+9) |
| [MEASUREMENT_CARD.md](docs/MEASUREMENT_CARD.md) | Fill with measured data |
| [MIN_PARTS.md](docs/MIN_PARTS.md) | Minimum kit |
| [SIM_NOTES.md](docs/SIM_NOTES.md) | Paper vs measured context |

## Environment and future paths

| Doc | What it is |
| :-- | :-- |
| [MARS_VARIANT.md](docs/MARS_VARIANT.md) | Mars / space hardened 25 mm path (inherits baseline) |
| [mars/](docs/mars/) | Speculative Mars extensions — seed bots, converters, bacteria swarm (DB-MARS-CONV-006), governors. Paper/sim only. |
| [EXTREME_ENVIRONMENTS.md](docs/EXTREME_ENVIRONMENTS.md) | Ocean, cryo, heat, rad, flight/exoskeleton, agency gates |
| [POST_2040_OUTLOOK.md](docs/POST_2040_OUTLOOK.md) | Scale-change modes (speculative) |
| [COMMUNITY_ENHANCEMENT_SUITES.md](docs/COMMUNITY_ENHANCEMENT_SUITES.md) | Optional zero-impact suites |

## Separate stack

- [PHASE0.md](docs/PHASE0.md) — Locked 20 mm sliding-pin face, Option A release, cams deferred (do not mix with 25 mm; face size committed 2026-11-23, was 30 mm)

## Re-runnable sims

- [sims/mars_bacteria_swarm_sim_v2_10.py](sims/mars_bacteria_swarm_sim_v2_10.py) — Standalone traceable Monte Carlo for DB-MARS-CONV-006. Seeded RNG, documented backsolved parameters, 240 runs. v2.10: 12/12 cells, ALL GATES PASS under insulated/heated shells with grounded Deinococcus cold data and oxidative refit from published survival curves. Five cells controller-dependent; scavenging at 5e-3 empties soil P pool — flagged, not hidden. Published imperfect, tweakable. Also sims/phase0_monte_carlo.py for the DittoBot Phase 0 docking confirmation Monte Carlo.

---

Paper until measured. Credit follows data.
DittoBot is the main design. Mars path is an inheritance and extension of it.

Funky fresh as of 2026-11-24.
