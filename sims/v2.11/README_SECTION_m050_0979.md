# v2.11 scored candidate — four winning ox_sweep12 values

**v2.11 CANDIDATE — pending Craig landing. Not yet the canonical scored run (scored A = ox10).**

Local package only. Nothing in this directory has been pushed. Suggested branch name: `v2.11-scored-candidate`.

## Override dict (hard-set defaults)

```python
OX_PERCELL_OVERRIDE = {
    ("moderate", 0.50): 0.979,
    ("moderate", 0.75): 0.9865,
    ("moderate", 1.00): 0.9895,
    ("moderate", 1.50): 1.0,
    ("severe", 1.50): 0.9989,
}
```

All other cells use `OXIDATIVE_FACTOR` tier values (baseline 1.0, moderate 0.97, severe 0.99). No MAA repair boost. No staged support, rescue pulse, mineral-P spine, or inoculum bump. INOCULUM 1e12, scav 5e-3, D 8.72, habitat on, adaptive on, throttle, 240 runs/cell.

The four binding-cell values are the lowest tested overrides from the UNSCORED ox_sweep12 sweep that cleared 240/240 at seed 42. They are fitted survival TARGETS for the lab screen, not measured values. Unaided thresholds: 0.978822, 0.9819, 0.986145, 0.998349. Margin above the threshold matters: moderate 0.75 at 0.982 cleared only 239/240 in that sweep. Moderate 1.50 keeps the ISS detection-floor 1.0 (same ISS footnote numbers as v2.10 scored A).

## Results

```
seed 42 (main() and seed-grid wrapper)  240 x 12
  ext 0  tmo 0  thr 4  freeze 0/2880  ALL GATES PASS
  CONTROL: REF vs v2.9  0/2880  REPRODUCES v2.9

seed  42   240 240 240 240 / 240 240 240 240 / 240 240 240 240   ext 0 tmo 0 thr 4  PASS  12x240
seed   1   240 240 240 240 / 240 240 240 240 / 240 240 240 240   ext 0 tmo 0 thr 3  PASS  12x240
seed   7   240 240 240 240 / 239 240 240 240 / 240 240 240 240   ext 0 tmo 1 thr 6  PASS  m0.50 r31 timeout
seed 123   240 240 240 240 / 239 240 240 240 / 240 240 240 240   ext 1 tmo 0 thr 1  PASS  m0.50 r146 extinct
seed 2024  240 240 240 240 / 240 240 240 240 / 240 240 240 240   ext 0 tmo 0 thr 2  PASS  12x240
```

Run 55 does not reappear on any of the five seeds. The two 239s are different indices, not a shared bad draw. They sit on moderate 0.50 at 0.979, just above its 0.978822 unaided threshold. Bumping that cell to the next sweep point (0.984) is the straightforward way to chase 12x240 on all five seeds.

main() ablations of note (seed 42): B (scav 1e-3, override kept) leaves moderate 0.50 and severe 1.50 at 228. C (override off) matches the ox_sweep12 SET S defaults. The candidate itself is specified at scav 5e-3.

## Files

- `mars_bacteria_swarm_sim_v2_11.py`
- `v211_main_seed42.stdout` — full main() at seed 42, including CONTROL
- `v211_seed_grids.stdout` — 12-cell grids at seeds 42, 1, 7, 123, 2024
