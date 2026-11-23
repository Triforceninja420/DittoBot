# Mars Path — Speculative Extensions of the DittoBot Baseline

Design owned by Craig.  
Started from the main DittoBot 25 mm cell (2026-11-19 baseline).  
**Paper / simulation only.** Credit follows measured data when hardware arrives.  
Two stacks stay unmixed — Phase 0 (30 mm dual-cam) is separate. This folder does not reopen any locked geometry.

These documents explore how the core programmable-matter lattice (residual-hold faces, self-replicating modules, local-material fabrication) can scale to Mars surface operations and long-term greening. The main design remains the Earth/lab 25 mm cell. Everything here inherits that baseline.

## Index (DB-MARS series)

| ID | File | What it is |
| :--- | :--- | :--- |
| DB-MARS-SEED-001 | [mars-seed-bot-spec-v1.md](mars-seed-bot-spec-v1.md) | 1 kg seed bot: Fresnel lens + magnetic rake + toaster kiln. Self-replicates from regolith. |
| DB-MARS-ICE-001 | [mars-ice-mining-spec-v1.md](mars-ice-mining-spec-v1.md) | Orbital scouting + scoop/hopper ice mining. |
| DB-MARS-CONV-001..004 | converter specs | Progressive CO₂→O₂ solid-oxide and catalytic-matrix designs. |
| DB-MARS-CONV-005 | [mars-conv-005-dual-path-strategy.md](mars-conv-005-dual-path-strategy.md) | Water-splitting primary + Phobos carbon import backstop. |
| DB-MARS-GOV-001 | [mars-swarm-governors-spec-v1.md](mars-swarm-governors-spec-v1.md) | Density + power governors so the swarm does not eat the planet. |
| **DB-MARS-CONV-006** | **[mars-bacteria-swarm-spec-v1.md](mars-bacteria-swarm-spec-v1.md)** | **Engineered cyanobacteria swarm (Deinococcus repair + antifreeze + UV sunscreen + sporulation + metabolic flexibility). Zero-power, self-replicating. Sim average ~96 sols to atmospheric O₂ under v1.1.** |

## Role relative to main DittoBot

- Seed bots and lattice modules use the same docking/face philosophy as the 25 mm cell.  
- Bacteria swarm is a complementary biological path for planetary-scale O₂ once infrastructure exists.  
- Habitat-scale oxygen can come from the converter chain in months; full greening (stable water, soil chemistry, UV protection for plants) remains a multi-decade to ~200-year process.  
- All numbers are simulation bounds. Earth-simulant prototypes and measured data are still required.

See also the higher-level [../MARS_VARIANT.md](../MARS_VARIANT.md) for the hardened 25 mm inheritance path.

Funky fresh as of 2026-11-22. Still the same DittoBot.
