# Mars Path — Speculative Extensions of the DittoBot Baseline

Design owned by Craig. Started from the main DittoBot 25 mm cell (2026-11-19 baseline). Paper/simulation only — credit follows measured data when hardware arrives. Two stacks stay unmixed (Phase 0 20 mm sliding-pin face is separate). This folder does not reopen locked geometry.

How the programmable-matter lattice scales to Mars surface ops and long-term greening. Main design remains the Earth/lab 25 mm cell; everything here inherits that baseline.

## Index (DB-MARS series)

| ID | File | What it is | Key number |
| :-- | :-- | :-- | :-- |
| DB-MARS-SEED-001 | [mars-seed-bot-spec-v1.md](mars-seed-bot-spec-v1.md) | 1 kg seed: Fresnel lens + magnetic rake + toaster kiln. Self-replicates from regolith. | 10–14 sols/copy (conservative) |
| DB-MARS-ICE-001 | [mars-ice-mining-spec-v1.md](mars-ice-mining-spec-v1.md) | Orbital scouting (HiRISE/SHARAD) + scoop/hopper mining. | 3,500 t water/sol @ 1,000 bots |
| DB-MARS-CONV-001 | [mars-co2-o2-converter-spec-v1.md](../../retired/mars-co2-o2-converter-spec-v1.md) | SOEC @ 800 °C baseline. 50 kW, 2.5 kg O₂/sol. | 26×10⁶-fold shortfall → drives v2 |
| DB-MARS-CONV-002 | [mars-high-output-converter-spec-v1.md](../../retired/mars-high-output-converter-spec-v1.md) | Vertical towers @ 1,100 °C. ~2,700 towers. | 112-yr claim retracted (37,000 Earth yr real) |
| DB-MARS-CONV-003 | [mars-co2-o2-converter-spec-v3.md](mars-co2-o2-converter-spec-v3.md) | 50× @ 1,400 °C. 1,760 towers, 74 GW. | Habitat-scale O₂ only |
| DB-MARS-CONV-004 | [mars-co2-o2-converter-spec-v4.md](mars-co2-o2-converter-spec-v4.md) | Distributed matrix pivot. 50×10⁹ units, 1 PW, 0.3% surface. | ~260 sols base w/ governors |
| DB-MARS-CONV-005 | [mars-conv-005-dual-path-strategy.md](mars-conv-005-dual-path-strategy.md) | Water-splitting primary + Phobos carbon import. | 12 TW → ~100 Earth yr |
| DB-MARS-GOV-001 | [mars-swarm-governors-spec-v1.md](mars-swarm-governors-spec-v1.md) | Density + power governors. | 15 runs, worst 309 sols |
| **DB-MARS-CONV-006** | **[mars-bacteria-swarm-spec-v1.md](mars-bacteria-swarm-spec-v1.md)** | **Engineered cyanobacteria (6 edits). Zero power.** | **v2.11: 12/12 cells, ALL GATES PASS. Grounded cold data (12.3× drop), oxidative refit 0.99808, scavenging 5e-3. 5 cells controller-dependent; P pool empties at max scavenging. Published imperfect.** |

## Role vs main DittoBot

- Seed bots/lattice modules share docking/face philosophy with 25 mm cell.
- Bacteria swarm = complementary biological path for planetary O₂ once infrastructure exists.
- Habitat O₂ from converters in months; full greening (water/soil/UV-for-plants) = under one Earth year per sim.
- All numbers = simulation bounds. Earth-simulant prototypes + measured data required.

See [../MARS_VARIANT.md](../MARS_VARIANT.md) for hardened 25 mm inheritance path.

Funky fresh as of 2026-11-23. Still DittoBot.
