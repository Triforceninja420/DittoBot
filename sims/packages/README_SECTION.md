# v2.10 option A — per-cell t66u extrapolated-slope fit

**UNSCORED sensitivity — not the canonical scored run (scored A = ox10).**

This is a local package for a parallel public branch. It does not replace the scored ox10 defaults (`OX_PERCELL_OVERRIDE = {("moderate", 1.50): 1.0}` on the ISS detection-floor framing, moderate 1.50% only). Nothing in this directory has been pushed; Craig or the owner lands the branch.

Suggested branch name: `sens/v2.10-ox-percell-t66u`

The parallel UNSCORED package is `sims-local/branch_B_iss_floor/` (`sens/v2.10-ox-iss-floor`).

## Fitting basis

Retired t66u extrapolated-slope fit, applied to all 12 `(tier, perch)` cells:

    ox(tier, perch) = round(10 ** (-dose(tier) * (5.0/3000.0)), 5)

Dose is tier-scaled only. Perch (perchlorate) is a separate Hill-function stressor and does not enter the radiation dose, so all four perch levels in a tier share one value.

| tier | dose (Gy/sol) | source | ox |
|---|---|---|---|
| baseline | 0.1 | low end of the v2.2 0.1–1.0 Gy/sol stack (not stated explicitly in the t66u comments) | 0.99962 |
| moderate | 0.5 | documented t66u assumption ("moderate tier = 0.5 Gy/sol") | 0.99808 (recovers `OX_MODERATE_FITTED`) |
| severe | 1.0 | t66u STATUS provenance ("about 0.996 at 1.0 Gy/sol") | 0.99617 |

Sources: Venkateswaran et al. 2000, Appl. Environ. Microbiol. 66:2620; Daly 2011, MMBR 75:133. "Lethal" = 5 log10 kill over 3 kGy, dose-proportional, no dose-rate sparing. This is a ~3,000× dose-rate extrapolation, not a clean fit, and is not fitted to sim outputs. 23 C test treated as equal to the 25 C habitat.

Hard-set override dict:

```
{('baseline', 0.5): 0.99962, ('baseline', 0.75): 0.99962, ('baseline', 1.0): 0.99962, ('baseline', 1.5): 0.99962, ('moderate', 0.5): 0.99808, ('moderate', 0.75): 0.99808, ('moderate', 1.0): 0.99808, ('moderate', 1.5): 0.99808, ('severe', 0.5): 0.99617, ('severe', 0.75): 0.99617, ('severe', 1.0): 0.99617, ('severe', 1.5): 0.99617}
```

`DOUBLING_SOLS` is held at 8.72 (the scored A value). A re-solve at option-A baseline ox 0.99962 would move it to 8.68.

## Results (seed 42, 240 runs/cell, scav 5e-3, D 8.72)

At inoculum 1e12 (`main()` of this package; confirm against the earlier ox_allcells option-A run):

```
clears (b.5 b.75 b1 b1.5 m.. s..): 240 240 240 240 240 240 240 228 240 240 240 229
23 extinctions, 0 timeouts, 2 throttled, freeze 0/2880, ALL GATES PASS
CONTROL still reproduces v2.9 (0/2880)
slowest-cell median 2,754 sols (moderate 1.50%)
```

Failing runs (0-based index): moderate 1.50% r9, r54, r55, r96, r99, r104, r106, r107, r143, r161, r211, r215 (12 extinct); severe 1.50% r9, r54, r55, r96, r104, r106, r107, r143, r161, r211, r215 (11 extinct).

At inoculum 2.5e13 (the knee; earlier UNSCORED wrapper on the same override values):

```
clears: 240 in all 12
0 extinctions, 0 timeouts, 50 throttled, freeze 0/2880, ALL GATES PASS
slowest-cell median 167 sols (severe 1.50%)
```

The 1e12 result is the telling one. 2.5e13 already cleared 12×240 even without these per-cell overrides, so the knee run is margin, not a new clearance.

## Comparison note

A rescues the three moderate cells 0.50/0.75/1.00 (scored A 231 → 240) but leaves moderate 1.50 at 228 and severe 1.50 at 229. Both stay below the 0.998349 unaided-growth target (A gives 0.99808 and 0.99617). Vs scored A (clears 240 240 240 240 231 231 231 240 240 240 240 230), 40 of 2,880 runs differ: the 27 scored-A failures in moderate 0.50/0.75/1.00 are rescued, moderate 1.50 picks up 12 new extinctions (ox 1.0 → 0.99808), and severe 1.50 picks up one new extinction (r106) on top of the original 10.

Option B (parallel branch `sens/v2.10-ox-iss-floor`) clears all twelve at 1e12 but is a uniform 1.0, not a true per-cell fit.

## Inoculum and seed checks (scored-A config)

These findings are from an UNSCORED sensitivity on the scored-A config (ox10: moderate 1.50% ox 1.0, other cells at tier defaults). Neither option A nor option B was itself re-run at low inoculum.

The eight unaided cells (baseline ×4, moderate 1.50, severe 0.50/0.75/1.00) stay 240/240 down to inoculum 1e6. The four binding cells (moderate 0.50/0.75/1.00 and severe 1.50) do not:

| inoculum | starter mass (UNIT_DRY_KG 2.0) | clears (m0.50 / m0.75 / m1.00 / s1.50) | gates |
|---|---|---|---|
| 1e12 | 2e12 kg | 231 / 231 / 231 / 230 | PASS |
| 1e9 | 2e9 kg | 154 / 154 / 154 / 154 | PASS |
| 1e8 | 2e8 kg | 131 / 132 / 133 / 130 | FAIL (moderate cells below the 60% gate) |
| 1e7 | 2e7 kg | 119 / 119 / 117 / 118 | FAIL |
| 1e6 | 2e6 kg | 103 / 103 / 104 / 103 | FAIL |

So a flyable starter is well below the unaided 12/12 line on scored A: the four binding cells still pass at 1e9 (2 billion kg) but fail the moderate 60% gate at 1e8 (200 million kg) and below.

A seed check at inoculum 1e12 (seeds 42, 1, 7, 123, 2024) found the four binding cells clearing 225–233/240, and all still passing their gates. Failures are a shared bad-draw set of 7–16 run indices per seed, not a single index and not r55-only. Seed 42 is not a special quirk; the same cells fail under other seeds, with a small cluster of unlucky draws rather than one unique run.


## Files

- `sims/mars_bacteria_swarm_sim_v2_10.py` — sim with option A hard-set
- `COMMIT_MSG.txt` — suggested commit message for Craig or the owner to land
- `BRANCH_NAME.txt` — suggested branch name
