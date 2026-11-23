# DB-MARS-SEED-001: Mars Seed Bot Spec v1.1

**Executive Summary:** One-kilogram solar-powered seed bot that self-replicates from Martian regolith. Carries a 1 m Fresnel lens (sintering, not melting), magnetic rake (iron as magnetite, no reduction), and toaster-sized kiln. Three seeds land, build a kiln ring, cast a chassis, and Bot 1 (5 kg) begins exponential copying. Conservative doubling: 10–14 sols per copy; optimistic: 5–7 sols. Energy: 2–4 kWh per tile, 30–50 kWh per full replication.

**Design Owner:** Craig. Paper/simulation only. Credit follows measured data.

---

## 1. Overview

Seed bot for Mars surface deployment. Mass: 1 kg. Power: solar only (small capacitor bank, no battery). Payload: 1 m Fresnel lens, magnetic rake, toaster-sized kiln. No arms, legs, or joints — sits on surface, bakes, stacks.

## 2. Phase Zero Deployment

Three seeds land. Each prints sintered regolith tiles (~0.3 m diameter) in a spiral ring around its lens for shading and dust blocking. Ring complete → tighter focus → hotter kiln → cast tubes, plates, brackets → bolt into frame for larger kiln → cast Bot 1 chassis (5 kg, real print head) from dirt and sunlight.

## 3. Bot 1 and Replication

Bot 1 makes copies from existing tiles and brackets. Exponential growth: one seed → one ring → one chassis → one factory.

| Parameter | Value | Unit |
| :-------- | :---- | :--- |
| Conservative doubling time | 10–14 | sols/copy |
| Optimistic doubling time | 5–7 | sols/copy |
| Energy per tile | 2–4 | kWh |
| Energy per full replication | 30–50 | kWh |
| Theoretical ceiling @ 10-day doubling | ~1×10¹² | units in ~11 yr (before physical limits) |

## 4. Materials (from local regolith/ice)

| Element | Use | Source note |
| :------ | :-- | :---------- |
| Silicon | Compute, structure | Regolith |
| Iron | Magnetic structures | Magnetite in regolith — no reduction needed |
| Aluminum | Oxidized structure | Regolith |
| Oxygen | Atmospheric byproduct | Released during sintering |
| Magnesium, Calcium | Alloy components | Regolith |

## 5. Energy Strategy

Sintering (800–1,200 °C) instead of full melting (1,500+ °C). Fresnel concentrators reach sintering temps at a fraction of melt power. Magnetic separator extracts iron before sintering. Staged growth: each kiln builds a slightly larger bot.

## 6. Mars-Specific Safety: RTG Hybrid

Earth-made plutonium core (cannot be synthesized from regolith); Mars-made housing, thermocouple legs, radiator fins (cast from regolith metals). One cargo drop per RTG heart.

## 7. Open Questions

- Doubling time validation needs Earth-simulant prototype
- Thermal cycling durability of sintered regolith on Mars
- RTG heart supply chain logistics

## 8. Next Steps

- Earth prototype on Mars simulant to lock energy numbers
- Cross-link Phase 0 docking protocol (DB-P0-FACE-TP-001)
- Credit: designer Craig (locked), builder TBD

## 9. Cross-References

- DB-MARS-CONV-001..006 (converter chain)
- DB-MARS-ICE-001 (ice mining)
- DB-MARS-GOV-001 (governors)
- DB-P0-FACE-TP-001 Rev A (Phase 0)
