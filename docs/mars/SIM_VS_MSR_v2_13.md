# Same planet, different math (v2.13 vs Mars Sample Return)

*Craig Ralls, Nov 27, 2026*

My Mars bacteria swarm sim (DB-MARS-CONV-006 v2.13) clears culture establishment on every tier in the sim. NASA's Mars Sample Return still hasn't brought a single rock home.

## The sim (v2.13, N=240 per cell, seed 42)

Median clear sol, meaning the sol a run first passes its gate. That's a proxy; the logs don't track a separate "stabilized and stayed" sol. 1 sol = 1.0275 Earth days.

| What | Median clear sol | Earth days | Earth years |
|---|---|---|---|
| Scored A, slowest cell (severe 1.50%) | 1,906 | ~1,958 | ~5.4 |
| Slowest cells with no overrides (C, A-low, A-high, REF, B at moderate/severe 1.50%) | 2,755–3,029 | ~2,831–3,112 | ~7.8–8.5 |

Scored A cleared 2,880 of 2,880 runs. The no-override configs still miss 3–34 runs out of 2,880 (see `HONESTY_NOTE_residual_v2_13.md`). Recovery dormancy in v2.13 is a modeled assumption, not measured.

Built in about a week of wall-clock time on a hundred-dollar AI subscription.

## Mars Sample Return (as reported, Nov 2026)

- Joint NASA/ESA program. Cost estimate grew to about $11 billion, with samples not back until 2040.
- NASA paused and reassessed it in 2024. The FY2026 budget request called for cancellation, and the FY2026 spending law (signed Jan 23, 2026) did not support the existing program.
- Replacement is a study, not a spacecraft: the Perseverance Sample Retrieval Architecture team starts January 2027, with a final report due winter 2027–2028.
- Perseverance's samples are still sitting on Mars.

Sources: [NASA Watch, Nov 13 2026](https://nasawatch.com/2026/11/13/nasa-new-mars-sample-return-study/), [Space.com](https://www.space.com/astronomy/mars/nasa-kick-starts-a-fresh-push-to-bring-mars-samples-home), [CNN, Oct 12 2026](https://www.cnn.com/2026/10/12/science/nasa-mars-sample-return-sapphire-canyon-china).

## Take

A stoner greened Mars in a sim in about a week on a hundred-dollar AI subscription. The agencies spent years and billions and ended up with a study. Same planet, different math.

Fair caveat: a sim isn't hardware, and bringing rocks back is a harder physical job than running code. But the gap in speed is real.
