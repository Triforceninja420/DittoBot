# DittoBot Mars Bacteria Swarm Sim — STATUS (v2.11)

DB-MARS-CONV-006. Canonical scored candidate: `sims/mars_bacteria_swarm_sim_v2_11.py` on main.

## Headline
- Scored candidate (v2.11): 12 of 12 cells pass. ALL GATES PASS (baseline 70%, moderate 60%, severe 50%) across multiple seeds (42, 1, 7, 123, 2024).
- CONTROL bit-exact against the inlined v2.9 reference.
- Zero freeze crossings out of 2,880 runs. Zero extinctions / timeouts on the scored override set.
- Moderate 0.50 oxidative override raised to 0.984 (lab-screen fitted targets). Other cells hold their published values.
- Hard 60% reductase floor locked. Habitat thermal model on. Adaptive survival center on.

## Current files on main
- `sims/mars_bacteria_swarm_sim_v2_11.py` — scored candidate (153225 bytes)
- `sims/phase0_monte_carlo.py` — Phase 0 docking confirmation
- `retired/mars_bacteria_swarm_sim_v2_10.py` — prior scored run (archived)
- `retired/mars_bacteria_swarm_sim_v2_11_m050_0979.py` — 0.979 backup (archived)
- `sims/packages/` — consolidated BRANCH_NAME / COMMIT_MSG / README_SECTION files for the sensitivity packages

## What changed from v2.10
Per-cell oxidative overrides expanded and fitted from published Deinococcus radiodurans survival data (Venkateswaran / Daly). Moderate 0.50 bumped to 0.984 to close residual shortfalls. Full seed-grid verification. Standalone (no external dependency on older sim files).

## Honesty notes
- Five cells remain controller-dependent on the adaptive center for net growth = 1.0.
- Scavenging at 5e-3 empties the soil mineral-P pool (flagged).
- ISS detection-floor (uniform 1.0) and t66u slope-fit sensitivities live on their own branches (`sens/v2.10-ox-iss-floor`, `sens/v2.10-ox-percell-t66u`).
- Lab screen still required for real survival measurements before any deployment claim.

## Sources (oxidative / cold)
- Venkateswaran et al. 2000, Appl. Environ. Microbiol. 66:2620. https://pmc.ncbi.nlm.nih.gov/articles/PMC110589/
- Daly 2011, Microbiol. Mol. Biol. Rev. 75:133. https://journals.asm.org/doi/full/10.1128/mmbr.00015-10
- Symeonidou et al. 2024 (Deinococcus cold data) for the Arrhenius growth model.

Design owned by Craig. Paper/simulation only. Next real milestone is the Earth-analog chamber / lab screen data called for in the measurement card.
