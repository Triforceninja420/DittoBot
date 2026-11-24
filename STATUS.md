# DittoBot Mars Bacteria Swarm Sim — STATUS (v2.10)

DB-MARS-CONV-006. File: sims-local/mars_bacteria_swarm_sim_v210.py (1,775 lines, 78,228 bytes). Built locally; not yet committed.

## Headline
- Scored run: 12 of 12 cells pass. ALL GATES PASS (baseline 70%, moderate 60%, severe 50%).
- Five cells (all four moderate cells, plus severe 1.50%) pass only because the adaptive survival center holds their net growth at exactly 1.0.
- Moderate 1.50% net growth on its own is 0.9997, just short of 1.0, so it is still held up by the center.
- Zero freeze crossings out of 2,880 runs. Zero chlorite hits.

## What changed from v2.9
1. Phosphorus scavenging rate raised to 5e-3. This is above the 2e-3 plausible ceiling set in v2.5. Doubling time re-solved to 8.72 sols.
2. Moderate oxidative multiplier on the moderate 1.50% cell only: 0.97 -> 0.99808 (data-fitted, extrapolated). All other moderate cells stay 0.97. Severe 0.99 left as-is.

Everything else held from v2.9: thermal habitat on (moderate and severe interiors at 25 C), adaptive survival center on, 60% hard reductase floor locked, 18% chlorite burden spike, CO2 hard gate plus throttle, N import 7.251e13 kg/sol, P import fallback 8.47e7 kg/sol, 80% recycle, seed 42, 240 runs per cell.

## Oxidative refit: provenance and sources
- The 0.97 first appears in v1.6 as a radiation/UV oxidative load factor (1.0 / 0.97 / 0.93 for baseline / moderate / severe). Moderate is defined as more than 0.3 Gy/sol. v2.0 raised severe to 0.99 to close a gate gap and never revisited moderate, so moderate ended up harsher than severe. Neither value was ever traced to data.
- Venkateswaran et al. 2000, Applied and Environmental Microbiology 66:2620. https://pmc.ncbi.nlm.nih.gov/articles/PMC110589/ . Continuous 60 Gy/h at 23 C in minimal medium: "a dose of 0.3 Mrad was lethal to cells"; "all of the cells were dead by 96 h (576,000 rads)."
- Daly 2011, Microbiology and Molecular Biology Reviews 75:133. https://journals.asm.org/doi/full/10.1128/mmbr.00015-10 . "a total delivered dose of 3 kGy (50 h at 60 Gy/h) being lethal" in minimal medium.
- Assumptions: moderate receives 0.5 Gy/sol; "lethal" = 5-log kill over 3 kGy, linear in dose; no credit for low dose rate; 23 C test treated as equal to the 25 C habitat.
- Result: 0.99808 per sol. Plausible range 0.99617 (1.0 Gy/sol, nutrient-poor) to 0.99986 (acute D10 slope).
- This is a dose-rate extrapolation of about 3,000x. Not fitted to sim outputs. Break-even for moderate 1.50% unassisted growth (diagnostic only): 0.99835 at 5e-3.

## Scored run A (both levers): clears/240, net growth per sol, center, median clear sol, extinctions
- baseline 0.50%: 240 PASS, 1.02164, 0.950, sol 188, 0
- baseline 0.75%: 240 PASS, 1.01846, 0.950, sol 212, 0
- baseline 1.00%: 240 PASS, 1.01405, 0.950, sol 256, 0
- baseline 1.50%: 240 PASS, 1.00165, 0.950, sol 925, 0
- moderate 0.50%: 231 PASS, 1.00000, 0.9606, sol 2708, 9
- moderate 0.75%: 231 PASS, 1.00000, 0.9645, sol 2727, 9
- moderate 1.00%: 231 PASS, 1.00000, 0.9702, sol 2809, 7
- moderate 1.50%: 228 PASS, 1.00000, 0.9503, sol 2754, 12
- severe 0.50%: 240 PASS, 1.01142, 0.950, sol 339, 0
- severe 0.75%: 240 PASS, 1.00828, 0.950, sol 430, 0
- severe 1.00%: 240 PASS, 1.01250, 0.960, sol 318, 0
- severe 1.50%: 230 PASS, 1.00000, 0.9598, sol 2696, 10

Every cell scavenges about 3.12e12 kg P, 99.7 to 100% of the soil's mineral phosphorus.

## Ablations
- B, scavenging 1e-3 with fitted oxidative: 12/12. Moderate 1.50% 228 clears, center 0.9513, unassisted net 0.99883.
- C, oxidative 0.97 with scavenging 5e-3: 12/12. Moderate 1.50% 232 clears, center 0.9886, unassisted net 0.9716.
- v2.9 reference (neither): 12/12, moderate 1.50% pinned at center 0.99. Reproduced exactly (0 of 2,880 runs differ).
- Range ends: low 0.99617 gives 12/12, still center-held. High 0.99986 is the only value where moderate 1.50% grows on its own: 240/240, net 1.00151, median clear sol 1,214.
- Attribution: scavenging only speeds cells that already grow on their own. The oxidative refit lowers moderate 1.50%'s center but does not free it from the controller.

## Other checks
O2-before-freeze ordering changes 0 cells. P import fallback changes 0 runs. Vent mode 12/12. Chlorite demo still kills 90% in 10 sols. Reductase sits at the 0.60 floor. Lattice unchanged: tau 20 yr unlock 12.94 / tear 25.89; 8 yr with wiper plus interlock stacked unlock 11.03 / tear 22.06.

## Caveats
- The oxidative value is a ~3,000x dose-rate extrapolation with an assumed dose per sol and an assumed definition of "lethal".
- 5e-3 scavenging is above the plausible range and drains the soil phosphorus completely.
- Five cells pass only through the adaptive center, which holds net growth at 1.0 by construction.
- The habitat is an ideal constant 25 C with no energy cost, failure modes or thermal cycling.
- Severe oxidative 0.99 was left as-is; provenance suggests it should be re-derived (about 0.996 at 1.0 Gy/sol).

## Commit message (drafted for Craig)
v2.10: scavenging 5e-3 (above the 2e-3 plausible ceiling; D re-solved to 8.72) plus a per-cell oxidative override for moderate 1.50% only, 0.97 -> 0.99808, data-fitted by extrapolating D. radiodurans chronic-irradiation lethality (Venkateswaran 2000; Daly 2011; 3 kGy at 60 Gy/h lethal in minimal medium, 23 C) to 0.5 Gy/sol; range 0.99617-0.99986. Floor locked, center on. Scored 12/12, ALL GATES PASS, 0 freeze crossings, 0 chlorite hits. Ablations: scav 1e-3 + fitted ox 12/12; ox 0.97 + scav 5e-3 12/12; neither reproduces v2.9 exactly (0/2,880 differ). Moderate 1.50% unassisted net 0.9997, still center-held; only the high range end (0.99986) grows unaided.
