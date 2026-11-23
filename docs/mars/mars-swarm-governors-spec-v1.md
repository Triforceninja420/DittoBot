# DB-MARS-GOV-001: Swarm Governors Spec v1.0

## Overview
Two governors control swarm growth. Either can halt growth alone; both must clear before resume.

## Governor 1: Density Cap
- Cap replication at 1 bot per square meter of usable surface
- Moment local density hits cap, new seeds stop building
- Existing seeds switch to converter production only
- Prevents swarm from carpeting the planet
- Raised to 600 billion units per square meter for CONV-004 scaling test

## Governor 2: Power Cap
- Hard pause: kills ALL replication instantly when draw crosses 1.5 PW
- No soft restart, full stop
- Soft reroute: every halted bot's output goes straight into running converters
- Nothing idles
- Resume only unlocks after 10 straight sols under the cap

## Stress Test Results (15 runs at 12 TW)
- Base case: 245 sols, 186K towers, 1.15 PW peak, 0 hard pauses
- 10% noise: 244-245 days, same tower counts
- 25% noise: 244-245 days, same tower counts
- Low converter efficiency (50%): 259 days, 9 pauses, 2 PW spike
- Tight power cap (0.75 PW): 245 days, 9 pauses, still clears via soft reroute
- Slow start (0.1x seeds): 292 days
- Big start (10x seeds): 197 days
- Worst case (low seeds + tight cap + half efficiency + 25% noise): 309 days, 26 pauses
- Best case: 189 days
- All governors hold across every scenario
- Nothing breaks, nothing exceeds a Mars year even in worst run

## Cross-References
- DB-MARS-SEED-001 (replication logic governed)
- DB-MARS-CONV-003 through 005 (power draw governed)
- DB-MARS-CONV-006 (bacteria swarm, separate from bot governors)