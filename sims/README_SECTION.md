# v2.10 option B — ISS detection-floor bound (uniform 1.0)

**UNSCORED sensitivity — not the canonical scored run (scored A = ox10).**

This is a local package for a parallel public branch. It does not replace the scored ox10 defaults (`OX_PERCELL_OVERRIDE = {("moderate", 1.50): 1.0}` on the ISS detection-floor framing, moderate 1.50% only). Nothing in this directory has been pushed; Craig or the owner lands the branch.

Suggested branch name: `sens/v2.10-ox-iss-floor`

The parallel UNSCORED package is `sims-local/branch_A_t66u_fit/` (`sens/v2.10-ox-percell-t66u`).

## Fitting basis

ISS detection-floor reference. A three-year ISS exposure of ~715 mGy showed no measurable survival effect. Mars surface background is 76–96 mGy/year. Over the 200-sol doubling-time calibration horizon (≈ 0.563 Earth years), that is ~43–54 mGy, about 13–17× below the ISS anchor. This is not the ensemble run duration: the reported slowest-cell median is 1,162 sols, and runs can continue up to 200,000 sols.

The model has no per-tier or per-perch mGy dose rates in this frame — only that single surface-background band. Holding every override at 1.0 throughout longer runs is an additional UNSCORED no-penalty sensitivity assumption, not a demonstrated below-anchor bound or a true per-cell fit. The retired v2.2 0.1–1.0 Gy/sol stack is a different, much higher assumed dose (20–200 Gy over 200 sols, ~28–280× above the anchor) and is not used here; if it were, the detection-floor rule would not grant 1.0.

Hard-set override dict:

```
{('baseline', 0.5): 1.0, ('baseline', 0.75): 1.0, ('baseline', 1.0): 1.0, ('baseline', 1.5): 1.0, ('moderate', 0.5): 1.0, ('moderate', 0.75): 1.0, ('moderate', 1.0): 1.0, ('moderate', 1.5): 1.0, ('severe', 0.5): 1.0, ('severe', 0.75): 1.0, ('severe', 1.0): 1.0, ('severe', 1.5): 1.0}
```

`DOUBLING_SOLS` is held at 8.72 (the scored A value). Baseline ox is 1.0, so the v2.5 re-solve stays 8.72.

## Results (seed 42, 240 runs/cell, scav 5e-3, D 8.72)

At inoculum 1e12 (`main()` of this package; confirm against the earlier ox_allcells option-B wrapper):

```
clears (b.5 b.75 b1 b1.5 m.. s..): 240 240 240 240 240 240 240 240 240 240 240 240
0 extinctions, 0 timeouts, 4 throttled, freeze 0/2880, ALL GATES PASS
slowest-cell median 1,162 sols (moderate 1.50%)
no failing runs
```

Vs scored A (clears 240 240 240 240 231 231 231 240 240 240 240 230): 37 of 2,880 runs differ, exactly the 37 scored-A failures, all rescued.

At inoculum 2.5e13 (the knee; earlier UNSCORED wrapper on the same override values):

```
clears: 240 in all 12
0 extinctions, 0 timeouts, 63 throttled, freeze 0/2880, ALL GATES PASS
slowest-cell median 147 sols (moderate 1.50% and severe 1.50%)
```

The 1e12 result is the telling one. 2.5e13 already cleared 12×240 even without these per-cell overrides, so the knee run is margin, not a new clearance.

## Comparison note

A (parallel branch `sens/v2.10-ox-percell-t66u`) rescues the three moderate cells 0.50/0.75/1.00 but leaves moderate 1.50 at 228 and severe 1.50 at 229. B clears all twelve at 1e12 but is a uniform 1.0, not a true per-cell fit. The lab screen would have to back the "below detection at Mars dose rates" claim; the sim itself only has the single surface-background band.

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

- `sims/mars_bacteria_swarm_sim_v2_10.py` — sim with option B hard-set
- `COMMIT_MSG.txt` — suggested commit message for Craig or the owner to land
- `BRANCH_NAME.txt` — suggested branch name
