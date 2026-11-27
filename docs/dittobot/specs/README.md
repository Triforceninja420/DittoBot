# DittoBot per-mode paper specs

Design owner: Craig.
Date: 2026-11-27.
Version: v0.2
Status: index of paper / conceptual specs. Does not change the locked 25 mm cell core, Phase 0 locks, or existing Phase 1 docking criteria.

This folder holds one paper spec per mode or capability that did not already have its own dedicated document. Each spec inherits the locked 25 mm cell core unchanged (Ø8.2 × 4.0 mm pocket, Nd disc Ø6.0 × 2–3 mm hold, DRV8871 pulse-only), and links back to its parent. Test gates are cited only where the repo already defines them. Anything else is TBD, no pass bar set. Assumptions are labeled modeled, not measured.

Numbered phases are indexed in [PHASES.md](../PHASES.md): Phase 0 (one face, [PHASE0.md](../../PHASE0.md)), Phase 1 (two-module dock plus scheduled Marble, [PHASE1.md](../../PHASE1.md)), Phase 2 (four-module lattice demos), Phase 3 (60–200 module field trial), and Phase 4 (post-2040 / V2.0 territory). Phase 5+ is not defined yet. The 27 non-Marble specs in this folder remain v0.2 with Status labels unchanged; any reassignment against Phase 2 is a separate decision and is not made here. Marble Mode remains v0.1 / Phase 1 ready (scheduled, not tested).

Paper until measured. Credit follows data.

## Already had a dedicated document (not duplicated here)

| Item | Existing doc | Parent / notes |
| :-- | :-- | :-- |
| EX-MOD extinguisher | [EX_MOD.md](../../EX_MOD.md) | [MODES.md — Modular components](../../MODES.md#modular-components-phase-0-face-compatible-paper) |
| BAR-MOD barrier | [BAR_MOD.md](../../BAR_MOD.md) | [MODES.md — Modular components](../../MODES.md#modular-components-phase-0-face-compatible-paper) |
| SAR package (Search / Rescue / Signal) | [SAR_MODES.md](../../SAR_MODES.md) | [MODES.md — Modular components](../../MODES.md#modular-components-phase-0-face-compatible-paper) |

## Architecture papers (not in this folder)

Conceptual v0.1 papers in [docs/dittobot/](../). They are not per-mode specs in this folder and they do not change any status label below.

- [POWER_ARCHITECTURE.md](../POWER_ARCHITECTURE.md) — how a single cell charges, stores, and shares energy across the lattice.
- [COMMUNICATION_PROTOCOL.md](../COMMUNICATION_PROTOCOL.md) — how nodes talk.

## New paper specs in this folder

### Feature modes (parent: [dittobot/MODES.md](../MODES.md))

| Spec | Status | Notes |
| :-- | :-- | :-- |
| [marble-mode.md](marble-mode.md) | Phase 1 ready | Scheduled as a Phase 1 deliverable in [PHASE1.md](../../PHASE1.md#deliverables). Status means scheduled, not built or tested. Proposed gates P1-M1…P1-M4, all TBD. |
| [repair-mode.md](repair-mode.md) | conceptual (phase unassigned) | Out of Phase 1 scope. See the spec for the assumption that would be needed. |
| [beacon-mode.md](beacon-mode.md) | conceptual (phase unassigned) | Out of Phase 1 scope. Not a SAR certification. See the spec for the assumption that would be needed. |

### Wearable / application inheritance (parent: [MODES.md](../../MODES.md))

| Spec | Status |
| :-- | :-- |
| [flight-suit.md](flight-suit.md) | paper spec (phase unassigned) |
| [exoskeleton.md](exoskeleton.md) | paper spec (phase unassigned) |
| [armored-shell.md](armored-shell.md) | paper spec (phase unassigned) |
| [soft-companion.md](soft-companion.md) | paper spec (phase unassigned) |
| [vehicle-rideable.md](vehicle-rideable.md) | paper spec (phase unassigned) |
| [habitat-shelter.md](habitat-shelter.md) | paper spec (phase unassigned) |

### Extreme-environment inheritance (parent: [EXTREME_ENVIRONMENTS.md](../../EXTREME_ENVIRONMENTS.md))

| Spec | Status |
| :-- | :-- |
| [deep-ocean.md](deep-ocean.md) | paper spec (phase unassigned) |
| [cryogenic.md](cryogenic.md) | paper spec (phase unassigned) |
| [extreme-heat.md](extreme-heat.md) | paper spec (phase unassigned) |
| [high-radiation.md](high-radiation.md) | paper spec (phase unassigned) |
| [corrosion.md](corrosion.md) | paper spec (phase unassigned) |
| [high-g.md](high-g.md) | paper spec (phase unassigned) |
| [biofouling.md](biofouling.md) | paper spec (phase unassigned) |
| [high-abrasion.md](high-abrasion.md) | paper spec (phase unassigned) |

### Post-2040 scale-change outlook (parent: [POST_2040_OUTLOOK.md](../../POST_2040_OUTLOOK.md))

| Spec | Status |
| :-- | :-- |
| [inward-compaction.md](inward-compaction.md) | conceptual (phase unassigned) |
| [outward-expansion.md](outward-expansion.md) | conceptual (phase unassigned) |
| [hierarchical-nesting.md](hierarchical-nesting.md) | conceptual (phase unassigned) |
| [variable-density-zones.md](variable-density-zones.md) | conceptual (phase unassigned) |
| [split-merge.md](split-merge.md) | conceptual (phase unassigned) |

### Community enhancement suites (parent: [COMMUNITY_ENHANCEMENT_SUITES.md](../../COMMUNITY_ENHANCEMENT_SUITES.md))

These parent entries are mostly one-line listings. The paper specs record the listing; they do not invent a mechanism.

| Spec | Status | Parent name |
| :-- | :-- | :-- |
| [soft-safety-skin.md](soft-safety-skin.md) | conceptual (phase unassigned) | Soft safety skin |
| [self-healing-coating.md](self-healing-coating.md) | conceptual (phase unassigned) | Self-healing coating |
| [dust-tolerance.md](dust-tolerance.md) | conceptual (phase unassigned) | Dust / contamination tolerance |
| [power-sharing.md](power-sharing.md) | conceptual (phase unassigned) | Short-range inter-node power sharing |
| [thermal-isolation.md](thermal-isolation.md) | conceptual (phase unassigned) | Local thermal runaway isolation |
| [rf-discovery-beacon.md](rf-discovery-beacon.md) | conceptual (phase unassigned) | Low-power RF discovery beacon |

### Companion, tool, and specialty modes (parent: [COMPANION_TOOL_MODES.md](../COMPANION_TOOL_MODES.md))

Conceptual v0.1 catalog — one-to-two-sentence entries, not per-mode paper specs in this folder. EX-MOD and BAR-MOD stay on their existing docs above. Every mode in that file is conceptual: no phase assigned, no pass bars.

## Locked core (unchanged)

All new specs inherit, and do not retune:

- 25 mm cube envelope
- Ø8.2 × 4.0 mm pocket
- Nd disc Ø6.0 × 2–3 mm hold, coil release-only
- DRV8871, 12 V, pulse-only

See [DESIGN.md](../../DESIGN.md) and [PAPER_STATUS.md](../../PAPER_STATUS.md).
