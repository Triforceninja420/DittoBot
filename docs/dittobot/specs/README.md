# DittoBot per-mode paper specs

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: index of paper / conceptual specs. Does not change the locked 25 mm cell core, Phase 0 locks, or existing Phase 1 docking criteria.

This folder holds one paper spec per mode or capability that did not already have its own dedicated document. Each new spec is v0.1, inherits the locked 25 mm cell core unchanged (Ø8.2 × 4.0 mm pocket, Nd disc Ø6.0 × 2–3 mm hold, DRV8871 pulse-only), and links back to its parent. Test gates are cited only where the repo already defines them. Anything else is TBD, no pass bar set. Assumptions are labeled modeled, not measured.

Paper until measured. Credit follows data.

## Already had a dedicated document (not duplicated here)

| Item | Existing doc | Parent / notes |
| :-- | :-- | :-- |
| EX-MOD extinguisher | [EX_MOD.md](../../EX_MOD.md) | [MODES.md — Modular components](../../MODES.md#modular-components-phase-0-face-compatible-paper) |
| BAR-MOD barrier | [BAR_MOD.md](../../BAR_MOD.md) | [MODES.md — Modular components](../../MODES.md#modular-components-phase-0-face-compatible-paper) |
| SAR package (Search / Rescue / Signal) | [SAR_MODES.md](../../SAR_MODES.md) | [MODES.md — Modular components](../../MODES.md#modular-components-phase-0-face-compatible-paper) |

## New paper specs in this folder

### Feature modes (parent: [dittobot/MODES.md](../MODES.md))

| Spec | Status | Notes |
| :-- | :-- | :-- |
| [marble-mode.md](marble-mode.md) | Phase 1 ready | Scheduled as a Phase 1 deliverable in [PHASE1.md](../../PHASE1.md#deliverables). Status means scheduled, not built or tested. Proposed gates P1-M1…P1-M4, all TBD. |
| [repair-mode.md](repair-mode.md) | conceptual | Out of Phase 1 scope. |
| [beacon-mode.md](beacon-mode.md) | conceptual | Out of Phase 1 scope. Not a SAR certification. |

### Wearable / application inheritance (parent: [MODES.md](../../MODES.md))

| Spec | Status |
| :-- | :-- |
| [flight-suit.md](flight-suit.md) | paper spec |
| [exoskeleton.md](exoskeleton.md) | paper spec |
| [armored-shell.md](armored-shell.md) | paper spec |
| [soft-companion.md](soft-companion.md) | paper spec |
| [vehicle-rideable.md](vehicle-rideable.md) | paper spec |
| [habitat-shelter.md](habitat-shelter.md) | paper spec |

### Extreme-environment inheritance (parent: [EXTREME_ENVIRONMENTS.md](../../EXTREME_ENVIRONMENTS.md))

| Spec | Status |
| :-- | :-- |
| [deep-ocean.md](deep-ocean.md) | paper spec |
| [cryogenic.md](cryogenic.md) | paper spec |
| [extreme-heat.md](extreme-heat.md) | paper spec |
| [high-radiation.md](high-radiation.md) | paper spec |
| [corrosion.md](corrosion.md) | paper spec |
| [high-g.md](high-g.md) | paper spec |
| [biofouling.md](biofouling.md) | paper spec |
| [high-abrasion.md](high-abrasion.md) | paper spec |

### Post-2040 scale-change outlook (parent: [POST_2040_OUTLOOK.md](../../POST_2040_OUTLOOK.md))

| Spec | Status |
| :-- | :-- |
| [inward-compaction.md](inward-compaction.md) | conceptual |
| [outward-expansion.md](outward-expansion.md) | conceptual |
| [hierarchical-nesting.md](hierarchical-nesting.md) | conceptual |
| [variable-density-zones.md](variable-density-zones.md) | conceptual |
| [split-merge.md](split-merge.md) | conceptual |

### Community enhancement suites (parent: [COMMUNITY_ENHANCEMENT_SUITES.md](../../COMMUNITY_ENHANCEMENT_SUITES.md))

These parent entries are mostly one-line listings. The paper specs record the listing; they do not invent a mechanism.

| Spec | Status | Parent name |
| :-- | :-- | :-- |
| [soft-safety-skin.md](soft-safety-skin.md) | conceptual | Soft safety skin |
| [self-healing-coating.md](self-healing-coating.md) | conceptual | Self-healing coating |
| [dust-tolerance.md](dust-tolerance.md) | conceptual | Dust / contamination tolerance |
| [power-sharing.md](power-sharing.md) | conceptual | Short-range inter-node power sharing |
| [thermal-isolation.md](thermal-isolation.md) | conceptual | Local thermal runaway isolation |
| [rf-discovery-beacon.md](rf-discovery-beacon.md) | conceptual | Low-power RF discovery beacon |

### Companion, tool, and specialty modes (parent: [COMPANION_TOOL_MODES.md](../COMPANION_TOOL_MODES.md))

Conceptual v0.1 catalog — one-to-two-sentence entries, not per-mode paper specs in this folder. EX-MOD and BAR-MOD stay on their existing docs above. Every mode in that file is conceptual: no phase assigned, no pass bars.

## Locked core (unchanged)

All new specs inherit, and do not retune:

- 25 mm cube envelope
- Ø8.2 × 4.0 mm pocket
- Nd disc Ø6.0 × 2–3 mm hold, coil release-only
- DRV8871, 12 V, pulse-only

See [DESIGN.md](../../DESIGN.md) and [PAPER_STATUS.md](../../PAPER_STATUS.md).
