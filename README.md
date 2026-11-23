# DittoBot / Voxel Box

Programmable matter voxel lattice. 25 mm cubic cell.
Design owned by Craig. Started November/December 2025.

**Current baseline (2026-11-19, magnet updated 2026-11-23):** Nd disc Ø6.0 × 2–3 mm hold (coil release-only, Alnico off), mechanical pin hard-lock, cavity potting, pulse-only drive with thermal governor, face coatings. Pocket and envelope unchanged. Paper only — credit follows measured data.

Phase 0 is the separate 30 mm dual-cam staggered face (rev 2026-11-21) — see [docs/PHASE0.md](docs/PHASE0.md). Two stacks stay unmixed.

---

## Start here

| Document | What it is |
| :--- | :-------- |
| [docs/BASELINE_UPGRADES.md](docs/BASELINE_UPGRADES.md) | 2026-11-19 standard (magnet, pin, potting, pulse-only) |
| [docs/DESIGN.md](docs/DESIGN.md) | Current 25 mm architecture and version ladder |
| [docs/BUILD.md](docs/BUILD.md) | Fab handoff |
| [docs/EXTREME_ENVIRONMENTS.md](docs/EXTREME_ENVIRONMENTS.md) | Inheritance path for ocean, space, cryo, flight/exoskeleton |
| [docs/MARS_VARIANT.md](docs/MARS_VARIANT.md) | Mars / space hardened path (inherits baseline) |
| [docs/mars/](docs/mars/) | Speculative Mars extensions: seed bots, O₂ converters, engineered bacteria swarm |
| [docs/MEASUREMENT_CARD.md](docs/MEASUREMENT_CARD.md) | Blank card — fill with real data |
| [sims/mars_bacteria_swarm_sim.py](sims/mars_bacteria_swarm_sim.py) | Traceable Monte Carlo sim for DB-MARS-CONV-006 (seeded, re-runnable) |
| [sims/phase0_monte_carlo.py](sims/phase0_monte_carlo.py) | Phase 0 face protocol Monte Carlo (DB-P0-FACE-TP-001, seeded, re-runnable) |

Full index: [docs/README.md](docs/README.md)

---

## Repository layout

```
cad/                  OpenSCAD (voxel_cell.scad + Phase 0 30 mm dual-cam)
phase0/               Phase 0 force fixture and coil geometry
firmware/             Pulse driver with thermal governor stub (XIAO RP2040)
tools/                Paper estimates (force_sweep.py, phase0_estimate.py)
tests/                CI test suite (Phase 0 math)
sims/                 Re-runnable Monte Carlo sims (Phase 0 + bacteria swarm)
bom/                  Netlist (synced to 2026-11-19 baseline)
docs/                 All current specifications and notes
  mars/               Speculative Mars seed / converter / bacteria path
.github/              CI workflow + issue templates
Voxel_Render.jpg      Example render
```

## Status

- **CI:** pytest + flake8 on every push and PR (Phase 0 math)
- **Tests:** 5 passing on main (Phase 0 docking tolerances)
- **Issue templates:** bug report + feature request, docs-first routing
- **Paper status:** all specs are simulation bounds pending Earth-simulant prototypes

License: MIT

Funky fresh. Still DittoBot. 2026-11-23.
