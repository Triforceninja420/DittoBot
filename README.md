# DittoBot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Docs](https://img.shields.io/badge/docs-living-brightgreen.svg)](docs/)

**Programmable Matter Voxel Lattice Robot** — modular cubes that dock, lock, pass power & data, and form structures. 25 mm cell is the main design.

![Voxel Render](Voxel_Render.jpg)

Design owned by Craig. Paper until measured. Credit follows data. Mars path is an inheritance and extension of the baseline.

## Quick Start

- **Phase 0 first article** (build this next): [docs/PUBLIC_ARTICLE.md](docs/PUBLIC_ARTICLE.md)
- **Current sim status**: [docs/STATUS.md](docs/STATUS.md)
- **Full changelog**: [docs/CHANGELOG.md](docs/CHANGELOG.md)
- Run Phase 0 Monte Carlo: `python sims/phase0_monte_carlo.py`
- Run Mars bacteria swarm: `python sims/mars_bacteria_swarm_sim_v2_11.py`

## Directory Structure

```
.
├── bom/                 # Bill of materials & netlist
├── cad/                 # OpenSCAD + SVG face plates
├── docs/                # All living design docs & specs
│   └── mars/            # Speculative Mars extensions
├── firmware/            # pulse_driver.cpp for XIAO RP2040
├── phase0/              # Phase 0 notes & retired CAD
├── retired/             # Archived older designs & early sims
├── sims/                # Re-runnable, seeded Monte Carlos
├── tests/               # pytest Phase 0 math checks
├── Voxel_Render.jpg     # Hero render
└── ...
```

## Documentation Index

All current design sources live in `docs/`.

### Current baseline (25 mm cell) — main design

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

### Environment and future paths

| Doc | What it is |
| :-- | :-- |
| [MARS_VARIANT.md](docs/MARS_VARIANT.md) | Mars / space hardened 25 mm path (inherits baseline) |
| [mars/](docs/mars/) | Speculative Mars extensions — seed bots, converters, bacteria swarm (DB-MARS-CONV-006), governors. Paper/sim only. |
| [EXTREME_ENVIRONMENTS.md](docs/EXTREME_ENVIRONMENTS.md) | Ocean, cryo, heat, rad, flight/exoskeleton, agency gates |
| [MODES.md](docs/MODES.md) | Application modes: flight suit, pure exoskeleton, armored shell, soft companion, vehicle, habitat (paper inheritance) |
| [POST_2040_OUTLOOK.md](docs/POST_2040_OUTLOOK.md) | Scale-change modes (speculative) |
| [COMMUNITY_ENHANCEMENT_SUITES.md](docs/COMMUNITY_ENHANCEMENT_SUITES.md) | Optional zero-impact suites |

### Separate stack

- [PHASE0.md](docs/PHASE0.md) — Locked 20 mm sliding-pin face, Option A release, cams deferred (do not mix with 25 mm; face size committed 2026-11-23, was 30 mm)

## Re-runnable sims

- [sims/mars_bacteria_swarm_sim_v2_11.py](sims/mars_bacteria_swarm_sim_v2_11.py) — Current scored candidate for DB-MARS-CONV-006. 12/12 cells, ALL GATES PASS. See [docs/STATUS.md](docs/STATUS.md).
- [sims/phase0_monte_carlo.py](sims/phase0_monte_carlo.py) — Phase 0 docking confirmation Monte Carlo (~98% all-pass).

---

Funky fresh as of 2026-11-26. Organized for clarity and speed.
