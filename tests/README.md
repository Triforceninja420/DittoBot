# Tests

Sanity checks for the DittoBot sims. These are **not** full regression
suites — they verify the scripts load, key constants are sane, and a
single run produces finite output with no NaNs or infinities.

## Run everything

From the repo root:

```bash
python -m pytest tests/
```

Or without pytest installed:

```bash
python -m unittest discover -s tests -v
```

## What's covered

- **test_mars_swarm_sim.py** — loads `sims/mars_bacteria_swarm_sim_v2_11.py`,
  checks constants (target biomass, inoculum, doubling sols, survival bounds,
  perchlorate levels, stress tiers, oxidative override dict), verifies the
  override covers the four binding cells, and runs one trial with N_RUNS
  patched to 1.
- **test_phase0_monte_carlo.py** — loads `sims/phase0_monte_carlo.py`, checks
  N_TRIALS / seeds / sigma constants, and calls `run_trial` once to confirm
  it returns a 5-tuple of booleans.

## Note

Importing the mars swarm sim pulls in the inlined v2.9 reference block, so
the first test in that file may take a few seconds to load. That's expected,
not a hang.
