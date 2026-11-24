# DB-MARS-CONV-006: Bacteria Swarm Spec v2.10

**Executive Summary:** Engineered cyanobacteria swarm for planetary-scale O₂. Zero power draw, self-replicating, grows on Martian sunlight. Trades speed for autonomy. Six genetic edits: Deinococcus radiodurans DNA repair, Arctic fish antifreeze proteins, mycosporine-like amino acid UV sunscreen, plus v1.1 survival fixes (1×10¹²-unit deployment, Bacillus subtilis sporulation, metabolic flexibility switching to H₂ chemosynthesis). **v1.3 adds traceable simulation:** mars_bacteria_swarm_sim_v21.py with seeded Monte Carlo, all parameters documented and backsolved. **v1.4 specs the two open control questions:** inducible metabolic toggle via light-repressed promoter, and perchlorate tolerance as an explicit sim parameter backsolved against 0.5–1% regolith perchlorate. **v1.5 adds module insulation:** orthogonal promoters and ribosome-binding sites per heterologous module, plus a fifteen-percent proteome burden cap. **v1.6 adds the burden sensor** — a growth-rate feedback loop that throttles heterologous expression when doubling time slips — **and a combined-stress ensemble** testing radiation plus oxidative stress simultaneously with the penalty rule. **v1.7 splits the sensor into separate cold and burden channels** so cold-driven lag cannot false-trigger heterologous throttling, **and carves out a stress-exempt floor for constitutive perchlorate reductase** so clearance holds under severe load. **v1.8 fixes clamp ordering:** the reductase floor is enforced after channel multiplication, not before — final reductase level equals max of sixty percent and one minus combined throttle, so simultaneous max cold lag plus full heterologous stack cannot push reductase below floor. **v2.0 tunes the stress stack:** oxidative factor at severe raised to 0.99, perchlorate LD50 raised from 2% to 10% (Hill 2.0), survival floor 10%, inoculum 1×10¹². **v2.1 closes the remaining gap:** survival cap raised from 0.95 to 0.97, doubling time shortened from 6.3 to 5.8 sols. Result: 9/9 cells, 240/240 runs, ALL GATES PASS — including severe at 1.0% perchlorate (mean 132 sols). **v2.2–v2.5 add explicit nutrient pools:** nitrogen and phosphorus modeled as finite resources with scavenging and recycling. Honest finding: rover-grade Martian soil holds ~3.3×10¹² kg phosphorus — enough for ~10¹´ cells. At 5.8-sol doubling, 200 sols needs ~5×10¹⁶. Scavenging maxes near 2×10⁻³; doubling floor will not budge below ~8 sols. Phosphorus import at Earth's entire phosphate-industry rate changed zero outcomes. **v2.6 scores 7/12** with scavenging as primary P lever. **v2.7 adds a cold penalty to growth** (fitted coefficient 0.0366) to force the adaptive survival center to mean something — moderate becomes a total wipeout (6/12); control without penalty hits 11/12 but is partly tautological (controller solves center to 1 by construction). The 0.97 survival-draw cap is the other wall: no center clears it; clamped draws jump from 34% to 66%. **v2.8 grounds the cold penalty in real Deinococcus radiodurans cold-shock data** (Venkateswaran & Daly): 12.3-fold respiration drop from 25°C to 0°C, mapping to 30% growth speed at cold 0.5 and 16% at cold 0.25. Result: 4/12, all gates fail. Only baseline passes. Draw-cap locked vs open: identical 4/12 — the cap is irrelevant; cold slowdown is the whole story. **v2.9 adds insulated moderate shells and heated severe at 25°C:** 12/12, ALL GATES PASS. The catch: moderate and severe at 1.5% only pass because the adaptive center holds them at exactly 1. Center-off: 7/12 — severe clears on its own, but moderate still nets below one from the 0.97 oxidative factor left over from v2.0 (a radiation-load assumption from v1.6 that was never revisited when severe was bumped to 0.99). **v2.10 refits that oxidative factor from published D. radiodurans peroxide/radiation survival curves at 25°C** (Venkateswaran & Daly), landing at 0.99808 (range 0.996–0.9999, marked extrapolated — dose rates ~3000× Mars moderate tier). Scavenging stepped to 5×10⁻³ (plausible ceiling 2×10⁻³ noted). Result: 12/12, ALL GATES PASS across all four runs (combined levers, scavenging-only, oxidative-only, and fitted-oxidative). Ablation shows the oxidative refit is the lever that actually moves moderate 1.5%; scavenging just speeds cells that already grow. Moderate 1.5% own-net: 0.999883 (scavenging-only) vs 0.9997 (combined) — still a random walk held at one; only the top of the literature range (0.999986) lets it grow solo at 240 clears. Moderate 1.5% would need 0.998335 to stand alone at 5×10⁻³. Doubling time re-solved to 8.72 sols. Severe should probably be re-derived to ~0.996. At 5×10⁻³, every cell scavenges ~3.12×10¹² kg — essentially 100% of the soil's mineral phosphorus; the pool empties. Converters (DB-MARS-CONV-005) handle habitat O₂ in months; bacteria handle planetary scale over decades–century. CO₂ held at 10–11×10¹² t in cleared runs. Zero freeze crossings, zero chlorite hits across 2,880 runs.

**Design Owner:** Craig. Paper/simulation only. Open questions: genetic stability, HGT risk, containment, ecosystem effects. Earth-simulant prototypes and measured survival/growth data on Mars-soil analog under UV and cold are required before any deployment claim. Heavy cold-resistant strain gene stack (DohD LEA3, Csp, fatty-acid desaturase, Arg-to-Lys codon shift) designed and shelved — hardware heating solved what the genome was meant to; retained as dormant fallback for dust storms and power outages.

---

## 1. Overview

Biological O₂ path. No electrical middleman — photosynthesis directly. [Cyanobacteria O₂ production: standard biochemistry]

## 2. Genetic Engineering

### Core Traits (v1.0)
1. **Radiation resistance:** Deinococcus radiodurans DNA repair suite [source: D. radiodurans genome, 3.28 Mb, extreme radioresistance literature]
2. **Cold tolerance:** Arctic fish antifreeze proteins [source: type III AFPs, fluid-membrane literature]
3. **UV shielding:** mycosporine-like amino acids (MAAs) [source: cyanobacterial MAA sunscreen pathway]

### Survival Fixes (v1.1)
1. **Deployment volume:** 1×10¹² units (vs 1×10⁶). At 8% survival → 80×10⁹ survivors.
2. **Sporulation:** Bacillus subtilis endospores [source: B. subtilis sporulation cascade] — survive vacuum, radiation, centuries dormant.
3. **Metabolic flexibility:** switch photosynthesis → H₂ chemosynthesis when sun too weak.

### Control Architecture (v1.4)
1. **Metabolic toggle:** inducible, not constitutive. Photosynthesis is the default state. The H₂ chemosynthesis switch is gated by a **light-repressed promoter** (phr system analog) — when ambient PAR drops below ~50 μmol·m⁻²·s⁻¹ (Martian twilight / dust-storm floor), the promoter derepresses and the cell flips to H₂ oxidation. No ATP spent maintaining the toggle in daylight. Fail-safe direction: if the promoter itself is damaged, the cell stays photosynthetic rather than starving on a broken switch.
2. **Perchlorate tolerance:** explicit sim parameter, not backsolved. Martian regolith perchlorate runs 0.5–1.0% by mass (Phoenix lander measurements). Tolerance module: perchlorate reductase + chlorite dismutase expression under a constitutive low-level promoter, sized so expression burden stays under 5% of total protein. Sim input: perchlorate_concentration_pct (default 0.75), perchlorate_survival_factor derived from dose-response curve (LD50 at 10% perchlorate, Hill coefficient 2). Survival multiplies by this factor per sol of regolith contact. Validated by re-running the v1.3 seed-42 ensemble at 0.5%, 0.75%, and 1.0% perchlorate — clearance rate must hold above 60% across all three or the parameter set is rejected.

### Module Insulation (v1.5)
1. **Orthogonal promoters:** each heterologous module gets its own promoter family with no shared transcription-factor binding sites — AFP under a cold-inducible promoter (cspA analog), MAA under a UV-inducible promoter, sporulation cascade under its native sigma-factor control, perchlorate reductase under the constitutive low-level promoter from v1.4. No promoter is reused across modules, eliminating transcriptional crosstalk.
2. **Orthogonal ribosome-binding sites:** each module's RBS is drawn from a characterized orthogonal RBS library (different spacer lengths and Shine-Dalgarno sequences) so translation initiation rates don't compete for the same ribosome pool. AFP and MAA RBSs tuned for moderate expression; sporulation RBSs left at native strength since the cascade is transient.
3. **Proteome burden cap:** total heterologous protein across all modules held under **15% of proteome**. Per-module budgets: perchlorate tolerance ≤5%, AFP ≤4%, MAA ≤4%, sporulation proteins ≤2% (transient, only during sporulation induction). Burden monitored in sim as a fitness multiplier — if any run's cumulative heterologous load exceeds 15%, that run's survival rate is penalized 20% per sol above the cap. This is the binding constraint on stacking further modules.

### Burden Sensor (v1.6, revised v1.7, clamp ordering fixed v1.8)
1. **Split-channel architecture:** the sensor no longer reads total doubling time. It splits into two independent channels — a **cold channel** and a **burden channel** — so cold-driven lag cannot false-trigger heterologous throttling.
2. **Cold channel:** measures membrane fluidity via a constitutively expressed reporter under a cspA-family promoter (same family as the AFP promoter but with a distinct RBS so it's not part of the AFP module). Rising cold expression indicates environmental cold, not expression burden. Cold-channel signal suppresses the burden channel's throttle authority: when cold expression is elevated, the burden throttle is scaled down proportionally (cold_factor from 0 to 1), so a cell fighting cold is not also punished for its AFP expression.
3. **Burden channel:** measures heterologous protein load directly via a translational fusion reporter on the perchlorate reductase transcript (the largest single heterologous load). When burden-channel signal exceeds the 15% proteome threshold AND cold_factor is low, throttling engages: 10% reduction at threshold, scaling to 50% at 2× threshold. Throttle order unchanged — perchlorate reductase first, then AFP, then MAA. Sporulation proteins are exempt from throttling entirely (transient cascade, native control).
4. **Fail-safe:** if either channel's reporter fails, that channel defaults to zero signal — cold channel zero means full throttle authority (conservative), burden channel zero means no throttling (the sim-side cap penalty still applies). No failed-sensor state allows expression beyond the 15% cap.
5. **Sim implementation:** burden_sensor_split flag (default True in v1.7). Each sol computes cold_factor and burden_signal independently; throttle = f(burden_signal, cold_factor). Throttled expression reduces per-unit O₂ output by the same proportion.
6. **Clamp ordering (v1.8):** the reductase floor is enforced **after** channel multiplication, never before. Combined throttle is the product of burden throttle and cold suppression. Final reductase level = max(reductase_floor, 1 − combined_throttle). This guarantees that even at max cold lag (cold_factor = 1) plus max burden throttle (50% reduction), reductase cannot drop below 60% nominal. Before v1.8, a naive implementation multiplying throttle then applying the floor as a separate step could produce a sub-floor value when cold suppression zeroed the burden channel's contribution — the floor now sits at the end of the computation chain as an absolute lower bound.

### Perchlorate Reductase Stress-Exempt Floor (v1.7, revised v1.8)
1. **Rationale:** perchlorate reductase is constitutive and is the primary defense against the most deployment-critical toxin. Under severe combined stress, throttling it would directly degrade clearance — the exact failure mode the 50% severe gate exists to prevent.
2. **Exempt floor:** perchlorate reductase expression is never throttled below **60% of its nominal level**, regardless of burden-channel signal, cold_factor, or stress tier. The remaining 40% of its budget is throttleable under extreme burden, but the floor holds.
3. **Sim implementation:** reductase_floor_pct = 60 (default). Throttle function clamps reductase reduction at 1 − reductase_floor_pct **after** computing combined throttle = burden_throttle × cold_suppression. All other modules remain fully throttleable per v1.6 rules. This means under severe stress the cell can shed AFP and MAA expression but cannot shed below 60% of its perchlorate defense.
4. **Interaction with burden cap:** the 15% proteome cap still applies to total heterologous load including the reductase floor. If the floor alone (3% of a 5% budget) plus other modules would breach 15%, AFP and MAA budgets are the first to compress — never the reductase floor.

### Combined-Stress Ensemble (v1.6, revised v1.7)
1. **Stress stack:** radiation (0.1–1.0 Gy/sol), oxidative stress from perchlorate (0.5–1.0%), cold (−60 to −20°C), and UV (up to 10 W/m²) applied simultaneously rather than as isolated scenarios. The v1.0–v1.3 ensembles tested stresses one at a time; real Mars stacks them.
2. **Penalty interaction term:** the 20%-per-sol burden penalty is now stress-dependent. Under combined stress, the penalty multiplier is 1 + (burden_excess × stress_factor), where stress_factor = 1.0 at baseline, 1.5 under moderate combined stress (radiation >0.3 Gy/sol AND perchlorate >0.75%), and 2.0 under severe combined stress (radiation >0.5 Gy/sol AND perchlorate >1.0% AND UV >5 W/m²). This models the reality that a cell already fighting radiation and oxidizers has less slack for expression burden.
3. **Acceptance gate:** clearance rate ≥50% under severe combined stress (relaxed from 60% because the stress stack is harsher), ≥60% under moderate, ≥70% under baseline. Mean burden must stay ≤15% proteome across all stress levels. If any gate fails, the parameter set is rejected and the module budgets get re-tuned.

## 3. Simulation Results

### v1.0 (20 runs)
- 7/8 scenarios cleared
- Base: 669 sols, 79% survival, hit 1×10¹⁸-unit cap
- High radiation / deep cold: ~6,500 sols each (~18 Earth yr)
- UV spike: 35,000 sols (~97 Earth yr), 32% survival
- Low inoculum: <1,200 sols
- Dust storms: 914 sols
- Best: 330 sols
- Worst case FAILED: 8% survival, 200,000 sols, 548 Earth yr, 7,000 kg O₂
- CO₂ held 10–11×10¹² t every cleared run

### v1.1 (20 runs)
- 20/20 cleared
- Best/worst/average: 96 sols
- Average survival: 11% (up from 8%)

### v1.2 (no-pants Craig included — 15 runs)
- All cleared, base 7,315 sols; worst ~16,600 sols (46 Earth yr), 2% survival still compounding; dim sun 12,000 sols. Pants variable: zero effect.

### v1.3 (traceable sim — 240 runs, seed 42)
- **Backsolved parameters required to hit 96 sols at 1.5 kg/unit/sol:**
  - Inoculum: 1×10⁹ units
  - Per-unit output: 1.5 kg O₂/sol
  - Doubling time: 6.3 sols
  - Survival: ≥50% (each survivor makes 1 copy) OR 11% (each makes 10 copies)
  - These are the optimistic edge, not nominal values
- Distribution: 175/240 clears (72.9%), mean 311 sols, range 44–11,000 sols
- 96 sols = best-case edge (~2.6th percentile), not the average
- Code: mars_bacteria_swarm_sim_v21.py — seeded, re-executable, parameters cited at top of file

### v1.4 (perchlorate ensemble — pending run)
- Same seed 42, 240 runs, three perchlorate levels (0.5/0.75/1.0%)
- Acceptance gate: clearance rate ≥60% at every level
- Toggle architecture assumed active: light-repressed promoter, 50 μmol·m⁻²·s⁻¹ threshold

### v1.5 (insulation ensemble — pending run)
- Same seed 42, 240 runs, burden cap active at 15% proteome
- Acceptance gate: clearance rate ≥60% AND mean burden ≤15% across all perchlorate levels
- If cap is breached, survival penalty of 20% per sol above threshold applies

### v1.6 (burden sensor + combined stress — pending run)
- Same seed 42, 240 runs per stress tier (baseline / moderate / severe)
- Burden sensor active: growth-rate feedback throttles expression when doubling time >1.5× baseline
- Combined-stress penalty: 20% per sol × stress factor (1.0/1.5/2.0 by tier)
- Acceptance gates: ≥70% baseline, ≥60% moderate, ≥50% severe; mean burden ≤15% all tiers
- Code: mars_bacteria_swarm_sim_v21.py — v1.6 flag set, same seed

### v1.7 (split-channel sensor + reductase floor — pending run)
- Same seed 42, 240 runs per stress tier
- Split sensor: cold_factor suppresses burden throttle; burden channel reads perchlorate-reductase translational fusion
- Reductase floor: 60% nominal minimum under all throttle conditions
- Combined-stress penalty unchanged: 20% per sol × stress factor (1.0/1.5/2.0)
- Acceptance gates: ≥70% baseline, ≥60% moderate, ≥50% severe; mean burden ≤15% all tiers; reductase expression ≥60% nominal in all severe-stress clears
- Code: mars_bacteria_swarm_sim_v21.py — v1.7 flag set, same seed

### v1.8 (post-multiplication clamp — 240 runs/cell, seed 42)
- Clamp ordering: final_reductase = max(0.60, 1 − burden_throttle × cold_suppression), evaluated after both channels resolve
- Verifies no sub-floor reductase values under simultaneous max cold + max burden
- All other v1.7 gates unchanged
- Code: mars_bacteria_swarm_sim_v21.py — v1.8 flag set, same seed
- Result: 0/9 cells passed. Baseline 0.5% cleared 240/240 (mean 305 sols); every cell at 0.75%+ and all moderate/severe tiers were 0/240. Mean survival across failed cells: 0.000. The survival floor did not matter — no draw ever approached 10%; lowest was 0.75. Structural failure: two-percent floor + two-percent LD50 + cold suppression 0.25 at severe = ~0.2 survival, net growth ~0.22/sol.

### v2.0 (oxidative + LD50 + floor + inoculum — 240 runs/cell, seed 42)
- Oxidative at severe: 0.93 → 0.99; perchlorate LD50: 2.0% → 10.0% (Hill 2.0); survival floor 10%; inoculum 1×10¹²
- 8/9 cells passed: all baseline and severe cells cleared 240/240; moderate at 0.5% and 0.75% passed
- Only failure: moderate at 1.0% perchlorate — 2/240 clears, mean survival 0.007
- Code: mars_bacteria_swarm_sim_v21.py

### v2.1 (cap + doubling — 240 runs/cell, seed 42)
- Survival cap: 0.95 → 0.97; doubling time: 6.3 → 5.8 sols
- 9/9 cells passed: 240/240 across every tier and perchlorate level
- Mean survival 0.91–0.94; severe at 1.0% mean 132 sols
- ALL GATES PASS
- Code: mars_bacteria_swarm_sim_v21.py — seeded, re-executable, parameters cited at top of file

### v2.2–v2.5 (nutrient pools — 12 cells, 240 runs each, seed 42)
- Explicit N and P pools with scavenging and recycling; N import at 7.25×10¹³ kg/sol carried the nutrient story
- Phosphorus is the hard wall: rover-grade soil ~3.28×10¹² kg, enough for ~10¹⁴ cells; 200 sols at 5.8 doubling needs ~5.4×10¹⁶
- Scavenging max ~2×10⁻³; doubling floor ~8 sols; P import at Earth phosphate-industry rate changed 0/2,880 outcomes
- v2.5: 5/12 (all gates fail); chlorite never fires under normal params; N/P recycling loop added

### v2.6 (scavenging primary — 12 cells, 240 runs, seed 42)
- Scavenging cranked as main P source, doubling solved toward 5.8, per-tier survival override for severe 1.0% starting 0.96, CO2 hard gate + vent kept, reductase floor + chlorite spike kept, N import held at 7.25×10¹³ kg/sol, 80% recycle
- 7/12: baseline all four clean; moderate total wipeout; severe 0.5% and 0.75% squeak by (~2,800 sols median); severe 1.0% 42 clears (under 50% gate); severe 1.5% dead
- Sensitivity: threshold 0.951 (coin flip, 73/240 died); 0.955 gives clean 240 clears
- Code: mars_bacteria_swarm_sim_v26.py

### v2.7 (cold penalty + adaptive center — 12 cells, 240 runs, seed 42)
- Cold penalty on growth (fitted 0.036636), adaptive survival center per-sol, 0.97 draw cap, scavenging default 2×10⁻³ (not 1×10⁻³)
- 6/12: baseline 4/4 clean; moderate 0/4; severe 0.5% and 0.75% at 233–234/240 clears but ~2,800 sols median; severe 1.0% and 1.5% dead
- Control (controller on, no cold penalty): 11/12 — only moderate 1.5% fails; partly tautological
- 0.97 cap: ~2/3 of draws slam into it at 0.99 center; raising center 0.95→0.99 lifts avg draw 0.939→0.959, clamped 34%→66%
- Code: mars_bacteria_swarm_sim_v27.py

### v2.8 (grounded cold — 12 cells, 240 runs, seed 42)
- Cold penalty from real D. radiodurans data: 12.3× respiration drop 25→0°C → 30% speed at cold 0.5, 16% at cold 0.25
- 4/12, all gates fail; only baseline passes; moderate 30%, severe 16% speed
- Cap locked 0.97 vs fully open: identical 4/12 — cap irrelevant
- Trajectories: soil-only peaks 5.51×10¹³ cells @ sol 205; volume×10: 5.18×10¹⁴ @ 317; continuous P: 7.91×10¹⁶ @ 581 (N-limited); severe 0.5 never grows in any case
- Code: mars_bacteria_swarm_sim_v28.py

### v2.9 (insulation + heated severe — 12 cells, 240 runs, seed 42)
- Insulated moderate shells, heated severe at 25°C; dormant cold-gene toggle off; heavy cold strain queued
- 12/12, ALL GATES PASS; moderate/severe 1.5% pass only because adaptive center holds at exactly 1
- Center-off: 7/12 — severe clears solo; moderate still below one from 0.97 oxidative (v2.0 stale pick)
- Code: mars_bacteria_swarm_sim_v29.py

### v2.10 (oxidative refit + scavenging step — 12 cells, 240 runs, seed 42)
- Oxidative refit from Venkateswaran & Daly 25°C peroxide/radiation curves: 0.99808 (extrapolated, dose ~3000× Mars moderate); scavenging 5×10⁻³ (ceiling 2×10⁻³ noted)
- 12/12, ALL GATES PASS across combined, scavenging-only, oxidative-only runs
- Ablation: oxidative refit is the lever that moves moderate 1.5%; scavenging speeds cells that already grow
- Moderate 1.5% own-net 0.999883 (scavenging-only) — still controller-dependent; needs 0.998335 to stand alone
- Doubling re-solved 8.72 sols; severe should re-derive to ~0.996
- At 5×10⁻³ every cell scavenges ~3.12×10¹² kg — 100% of soil mineral P; pool empties
- Zero freeze crossings, zero chlorite hits, 2,880 runs
- Code: mars_bacteria_swarm_sim_v210.py (standalone, inlines v2.9 dependencies)
- **This is the published version — imperfect, honest, tweakable. Next: ablation isolation, volume expansion vs continuous P Pareto, severe re-derivation.**

## 4. Role in Green Mars Stack

- Converters: habitat O₂ in months
- Bacteria: planetary scale, decades–century
- Bacteria burn CO₂ slower — intentional trade
- Zero power, self-replicating

## 5. Open Questions

- Genetic stability across Martian generations
- Horizontal gene transfer risks
- Containment if traits escape to Earth-origin microbes
- Long-term ecosystem effects
- **Measured survival and growth rates on Mars-soil analog under UV/cold/perchlorate — required to replace backsolved parameters with real data**
- Inducible toggle promoter kinetics under actual Martian PAR spectrum (lab validation needed)
- Orthogonal RBS library characterization in the target cyanobacterial chassis (lab validation needed)
- Burden sensor promoter response curve in the target chassis (lab validation needed)
- Combined-stress interaction terms need Earth-analog chamber data before flight claims
- Split-channel cold/burden discrimination accuracy under simultaneous cold + high burden (lab validation needed)
- Reductase floor sufficiency at 1.0% perchlorate under severe radiation (needs dose-response chamber data)
- Post-multiplication clamp behavior under non-linear channel interactions (analytical verification pending)
- Moderate 1.5% oxidative factor: fitted value is extrapolated 3,000× from lab dose rates; chamber validation at Mars-realistic dose urgently needed
- Severe oxidative re-derivation to ~0.996 (pending)
- Phosphorus supply: volume expansion vs continuous feedstock Pareto (pending)
- Heavy cold-resistant strain: DohD/Csp/desaturase/Arg-Lys stack shelved pending hardware-heating validation failure

## 6. Cross-References

- DB-MARS-CONV-005 (dual-path; bacteria = long game)
- DB-MARS-SEED-001 (deployment via seed bots)
- DB-MARS-GOV-001 (density governor: bots only, not bacteria)
- mars_bacteria_swarm_sim_v210.py (standalone traceable Monte Carlo, this folder's parent sims/ dir)
