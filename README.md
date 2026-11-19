# DittoBot / Voxel Box

Programmable matter voxel lattice. 25 mm cubic cell.  
Design owned by Craig. Started November/December 2025.

**Current baseline (2026-11-19):** SmCo Ø7.5 mm, mechanical pin hard-lock, cavity potting, pulse-only drive, face coatings. Pocket and envelope unchanged. Paper only — credit follows measured data.

This is **not** the locked Phase 0 20 mm hybrid face. Do not mix stacks. See [docs/PHASE0.md](docs/PHASE0.md).

---

## Start here

| Document | What it is |
| :--- | :--- |
| [docs/BASELINE_UPGRADES.md](docs/BASELINE_UPGRADES.md) | 2026-11-19 standard (magnet, pin, potting, pulse-only) |
| [docs/DESIGN.md](docs/DESIGN.md) | Current 25 mm architecture and version ladder |
| [docs/BUILD.md](docs/BUILD.md) | Fab handoff |
| [docs/EXTREME_ENVIRONMENTS.md](docs/EXTREME_ENVIRONMENTS.md) | Inheritance path for ocean, space, cryo, flight/exoskeleton, etc. |
| [docs/MARS_VARIANT.md](docs/MARS_VARIANT.md) | Mars / space hardened path (inherits baseline) |
| [docs/MEASUREMENT_CARD.md](docs/MEASUREMENT_CARD.md) | Blank card — fill with real data |

Full index: [docs/README.md](docs/README.md)

---

## Repository layout

```
cad/                  OpenSCAD (voxel_cell.scad + Phase 0 fixture)
firmware/             Pulse driver (XIAO RP2040)
tools/                Paper estimates (force_sweep.py, phase0_estimate.py)
bom/                  Netlist
docs/                 All current specifications and notes
assets/               Renders (Voxel_Render.jpg at root for now)
```

Root-level `.md` files (DESIGN.md, MEASUREMENT_CARD.md, MIN_PARTS.md, etc.) are legacy backups from earlier dates. Use the versions inside `docs/`.

License: MIT
