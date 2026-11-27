# v2.11 scored candidate — four ox_sweep12 targets, m0.50 at 0.984

**v2.11 CANDIDATE — pending Craig landing. Not yet the canonical scored run (scored A = ox10).**

Local package only. Nothing in this directory has been pushed. Suggested branch name: `v2.11-scored-candidate`.

The prior 0.979 file is kept as `retired/mars_bacteria_swarm_sim_v2_11_m050_0979.py` (sha256 `0c1080382d5138180259bf84f675f086d7314560d406f216fb125421365302de`), with matching stdout and docs suffixed `_m050_0979`.

## Override dict (hard-set defaults)

```python
OX_PERCELL_OVERRIDE = {
    ("moderate", 0.50): 0.984,
    ("moderate", 0.75): 0.9865,
    ("moderate", 1.00): 0.9895,
    ("moderate", 1.50): 1.0,
    ("severe", 1.50): 0.9989,
}
```

All other cells use `OXIDATIVE_FACTOR` tier values (baseline 1.0, moderate 0.97, severe 0.99). No MAA repair boost. No staged support, rescue pulse, mineral-P spine, or inoculum bump. INOCULUM 1e12, scav 5e-3, D 8.72, habitat on, adaptive on, throttle, 240 runs/cell.

Moderate 0.75, 1.00, and severe 1.50 are the lowest tested overrides from the UNSCORED ox_sweep12 sweep that cleared 240/240 at seed 42. Moderate 0.50 uses the ox_sweep12 mid point 0.984, not the low point 0.979: 0.979 cleared 240/240 at seed 42 but left 239/240 at seeds 7 (r31 timeout) and 123 (r146 extinct). These are fitted survival TARGETS for the lab screen, not measured values. Unaided thresholds: 0.978822, 0.9819, 0.986145, 0.998349. Margin above the threshold matters: moderate 0.75 at 0.982 cleared only 239/240 in that sweep. Moderate 1.50 keeps the ISS detection-floor 1.0 (same ISS footnote numbers as v2.10 scored A).

## Results (m0.50 at 0.984)

```
seed 42 (main() and seed-grid wrapper)  240 x 12
  ext 0  tmo 0  thr 4  freeze 0/2880  ALL GATES PASS
  CONTROL: REF vs v2.9  0/2880  REPRODUCES v2.9
  moderate 0.50 expnet 1.00529

seed  42   240 240 240 240 / 240 240 240 240 / 240 240 240 240   ext 0 tmo 0 thr 4  PASS  12x240
seed   1   240 240 240 240 / 240 240 240 240 / 240 240 240 240   ext 0 tmo 0 thr 3  PASS  12x240
seed   7   240 240 240 240 / 240 240 240 240 / 240 240 240 240   ext 0 tmo 0 thr 6  PASS  12x240
seed 123   240 240 240 240 / 240 240 240 240 / 240 240 240 240   ext 0 tmo 0 thr 1  PASS  12x240
seed 2024  240 240 240 240 / 240 240 240 240 / 240 240 240 240   ext 0 tmo 0 thr 2  PASS  12x240
```

No cell below 240 on any of the five seeds. Run 55 does not reappear. The seed-7 and seed-123 shorts at 0.979 are gone.

main() ablations of note (seed 42): B (scav 1e-3, override kept) is now 240 in moderate 0.50 but still leaves severe 1.50 at 228. C (override off) is unchanged: 231 231 231 232 / 230 on the binding and moderate 1.50 cells. The candidate itself is specified at scav 5e-3.

## Files

- `mars_bacteria_swarm_sim_v2_11.py` — current candidate (m0.50 = 0.984)
- `retired/mars_bacteria_swarm_sim_v2_11_m050_0979.py` — 0.979 backup
- `v211_main_seed42.stdout` — full main() at seed 42, including CONTROL
- `v211_seed_grids.stdout` — 12-cell grids at seeds 42, 1, 7, 123, 2024
