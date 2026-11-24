#!/usr/bin/env python3
"""DB-MARS-CONV-006 v2.11 CANDIDATE traceable Monte Carlo sim.

STANDALONE CONSOLIDATION (2026-11-23): this file runs on its own, with no import or
dependency on the v2.9 or v2.8 sim files (stdlib only). The v2.9
reference code used by the REF-vs-v2.9 CONTROL check is inlined verbatim
below (v2.9 lines 1-1632: constants, run_once, run_cell, run_ensemble and all
helpers; v2.9 main() omitted, so its own v2.8 check is not carried) in
_V29_REFERENCE_SOURCE and executed into an isolated namespace by
_load_v29_reference(), so its globals stay separate from v2.10's exactly
as a module import would. v2.10 logic and stdout are unchanged.

v2.10 updates (2026-11-23, t65u) - two USER-CHOSEN levers on v2.9:
1. SCAV_KG_P_PER_KG_DRY_PER_SOL 1e-3 -> 5e-3 (above the 2e-3 "top of
   Mars-plausible" bound set in v2.5). DOUBLING_SOLS re-solved at 5e-3 by
   the v2.5 200-sol criterion (baseline-driven).
2. Per-cell oxidative override: moderate 1.50% only, 0.97 -> 1.0
   (OX_PERCELL_OVERRIDE, toggled by OX_PERCELL_OVERRIDE_ENABLED).
   Frame: below detection limit at moderate-tier dose rates, bounded
   by ISS 3-year exposure data (~715 mGy, no measurable survival
   effect). Mars surface background 76-96 mGy/year; moderate-tier
   dose over a 200-sol run is ~43-54 mGy, ~13-17x (≥~13x) below
   that ISS anchor. See constants block. Other moderate cells stay
   0.97; severe 0.99 unchanged.
Hard 60% reductase floor locked. Everything else as v2.9. Setting scav 1e-3,
D 8.82 and override off reproduces v2.9 bit-exactly.
Provenance note on 0.97: introduced v1.6 as the "Radiation/UV oxidative load
factor on survival (tier-scaled)" {1.0, 0.97, 0.93}; v2.0 lifted severe to
0.99 as a tuning lever and left moderate at 0.97; never traced to data.
v2.10 (2026-11-24): scored moderate 1.50% override moved 0.99808 -> 1.0
and the t66u data-fitted (extrapolated) slope language was replaced by
the ISS detection-floor framing above. Other v2.10 constants unchanged.

v2.11 CANDIDATE (2026-11-24, t124u) — pending Craig landing; ox10 remains
the canonical scored A run until this candidate is accepted.
Expands OX_PERCELL_OVERRIDE from moderate 1.50% only to the four binding
cells plus moderate 1.50%. The four binding-cell values are the lowest
tested overrides from the UNSCORED ox_sweep12 sweep that cleared 240/240
at seed 42, INOCULUM 1e12 (moderate 0.50: 0.979, moderate 0.75: 0.9865,
moderate 1.00: 0.9895, severe 1.50: 0.9989). These are fitted survival
TARGETS for the lab screen, not measured values. Unaided thresholds
(the 6-decimal ox values that actually cross net 1.0) are 0.978822,
0.9819, 0.986145 and 0.998349. Margin above the threshold matters:
moderate 0.75 at 0.982 (just above 0.9819) cleared only 239/240 (one
timeout). Moderate 1.50% keeps the ISS detection-floor override of 1.0
(same ISS footnote numbers as v2.10 scored A). No MAA repair boost, no
staged support, no rescue pulse, no mineral-P spine, no inoculum bump.
INOCULUM 1e12, scav 5e-3, DOUBLING_SOLS 8.72, habitat and adaptive on,
throttle mode, 240 runs/cell, seed 42. CONTROL vs the inlined v2.9
reference is unchanged.

v2.9 updates (2026-11-23) — thermal habitat model on v2.8:
1. HABITAT_ENABLED with HABITAT_MODE per tier:
     baseline "ambient"           (cold 1.0 = 25 C already, unchanged)
     moderate "insulated"         insulated shell, interior 25 C
     severe   "insulated_heated"  insulation + supplemental heat, 25 C
   Inside a habitat the effective cold factor is the interior temperature
   mapped back through the v2.8 linear map (0 C -> 0, 25 C -> 1), so
   HABITAT_INTERIOR_C 25 gives cold 1.0: the grounded Arrhenius growth
   rate (Ea 67.99 kJ/mol) is fully restored (r = 1). The two habitat
   modes are thermally identical in the sim; the label records HOW the
   25 C is held. No energy budget, no heater failure, no thermal mass:
   the interior is an ASSUMED constant 25 C.
2. HABITAT_RESTORES_PROTEOME (default True). In v1.8-v2.8 the cold
   factor also scales the burden-sensor throttle in proteome_levels.
   Physically the interior cold factor is 1.0, so by default the
   proteome also sees 1.0. NOTE this is not "baseline-equivalent":
   at stress 1.5/2.0 with cold 1.0 the sensor throttles fully and the
   reductase drops to the 60% hard floor (0.75 at ambient cold), which
   lowers O2 output per unit. False keeps the ambient proteome
   (reductase 0.75) and only restores the growth rate; both reported.
3. NOT thermal, unchanged: oxidative factor (moderate 0.97 — a v2.0
   setting left untouched — severe 0.99), perchlorate Hill factor,
   survival draw shoulder, adaptive center, nutrients, freeze gate.
4. HABITAT_ENABLED False reproduces v2.8 run-for-run (checked in main).
5. New diagnostics: per-run peak population; per-cell survival draw
   distribution (mean, median, p5, p95, min, fraction above the 0.98
   knee) from a 0.001-wide histogram of every per-sol draw.

v2.8 updates (2026-11-23) — two fixes on v2.7, everything else held:
1. Survival draw cap. SURVIVAL_CAP_MODE:
     "soft" (DEFAULT) — a smooth shoulder that only engages above
        SURVIVAL_SOFT_KNEE (0.98): y = x for x <= knee, else
        y = knee + (1-knee) tanh((x-knee)/(1-knee)). Continuous with
        slope 1 at the knee; approaches but never exceeds 1.0 (a
        survival fraction cannot exceed 1). No artificial 0.97 ceiling.
     "none" — only the physical limit: hard clamp at 1.0.
     "hard097" — legacy v2.1-v2.7 clamp at SURVIVAL_CAP 0.97 (control).
   The 0.10 floor is unchanged. ADAPTIVE_CENTER_MAX stays 0.99; with no
   0.97 cap a 0.99 center gives an expected draw of ~0.977 (soft).
2. Cold penalty grounded in Deinococcus radiodurans data. COLD_MODEL:
     "arrhenius_growth" (DEFAULT) — cold slows the replication RATE:
        growth per sol = 2^(r(cold)/D), r = Arrhenius rate ratio vs 25 C.
     "arrhenius_survival" — same r applied to per-sol survival (the
        v2.7 placement), comparison only.
     "linear_fitted" — legacy v2.7 f_cold = 1 - 0.036636 (1 - cold).
   Grounding (Symeonidou et al. 2024, Extremophiles,
   doi 10.1007/s00792-024-01351-5, PMC11266278, Table 2): D.
   radiodurans control-culture CO2 production 812.63 ug/day at 25 C vs
   66.03 ug/day at 0 C, ratio 12.31. Two-point Arrhenius gives
   Ea = R ln(12.31) / (1/273.15 - 1/298.15) = 68.0 kJ/mol, Q10 = 2.73
   over 0-25 C. Cross-check: Price & Sowers 2004 PNAS 101:4631 report
   ~110 kJ for microbial community growth/maintenance/survival.
   MAPPING (an ASSUMPTION, stated plainly): the dimensionless cold
   factor maps LINEARLY onto the study's two temperatures,
   T = 0 C + cold x 25 C, so cold 1.0 = 25 C (rate 1), cold 0.0 = 0 C
   (rate 1/12.31). Tier values: baseline 1.0 = 25 C, moderate 0.5 =
   12.5 C, severe 0.25 = 6.25 C, cold 0.95 = 23.75 C.
   Placement: the measurement is a metabolic RATE, and the same study
   reports longer survival / higher CFU at 0 C than 25 C in most
   treatments, so the slowdown is applied to growth, not to survival.
   Mortality is NOT slowed by cold (conservative; noted as a caveat).
3. Scored scavenging rate 1e-3 (user brief); D re-solved under the soft
   cap at each rate (baseline cold 1.0 -> r = 1, so the cold model does
   not enter the solve, but the cap change does).
4. Control: SURVIVAL_CAP_MODE "hard097" + COLD_MODEL "linear_fitted" at
   rate 2e-3 / D 8.05 reproduces v2.7 E1 run-for-run (checked in main).

v2.7 updates (2026-11-23) — adaptive per-sol survival center on v2.6:
1. ADAPTIVE_SURVIVAL (default True) replaces the static survival center.
   Every sol the run READS the cold suppression factor, then sets the
   lognormal center to the value whose EXPECTED clamped draw (geo-mean
   of min(SURVIVAL_CAP, max(SURVIVAL_FLOOR, LN(log c, SPREAD)))) makes
   expected net growth = ADAPTIVE_NET_TARGET (1.0), given that sol's
   cold factor, oxidative factor, perchlorate Hill factor, burden
   penalty, chlorite factor and 2^(1/D). The solved center is clipped
   to [lower, ADAPTIVE_CENTER_MAX]; lower = max(ADAPTIVE_CENTER_MIN,
   the v2.6 static per-cell center), so a cell that already nets >= 1
   "relaxes" back to exactly its v2.6 center. The per-sol draw is then
   taken exactly as in v2.6 and still clamped at SURVIVAL_CAP 0.97.
   ADAPTIVE_CENTER_MAX 0.99 sits ABOVE the cap: raising the center past
   0.97 only pushes more draws into the cap, so the reachable expected
   draw tops out near 0.959 (center 0.99). Cells that need more than
   that stay below net 1 and are reported, not forced.
   HONESTY NOTE: a center solved to hold net >= 1 makes survival pass
   by construction wherever it is reachable. It is a controller
   target, not a measured or modelled biology.
2. Cold coupling (NEW, an assumption, documented). In v2.6 the cold
   suppression factor does NOT enter the net-growth product; it only
   scales the burden-sensor throttle inside proteome_levels (reductase
   level). With no coupling the adaptive center would ignore cold
   entirely. To make "read cold, set the center" meaningful, v2.7 adds
   a linear cold net factor applied to per-sol survival:
       f_cold = 1 - COLD_NET_COUPLING * (1 - cold)
   COLD_NET_COUPLING is CALIBRATED (not measured) so that cold 0.25 at
   severe 0.50% (the mildest severe cell, D 8.05) needs center exactly
   COLD_CALIBRATION_CENTER = 0.98. Cold 1.0 gives f_cold = 1 (baseline
   untouched); cold 0.95 gives f_cold ~0.998 and the center relaxes.
   The coupling is a NEW penalty that v2.6 did not have; a variant with
   COLD_NET_COUPLING = 0 (pure v2.6 physics + controller) is reported
   alongside the scored run.
3. Cold read per sol: cold = tier value x exp(COLD_VARIATION_SPREAD x
   N(0,1)) clipped to [COLD_MIN, COLD_MAX], quantised to
   COLD_READ_RESOLUTION. Default spread 0 -> cold is constant per tier
   and results are reproducible; a spread>0 sensitivity draws cold from
   a SEPARATE per-run RNG so survival draws stay paired with v2.6. The
   per-sol cold value drives f_cold and the center only; proteome
   levels (reductase 0.75 at moderate/severe) stay tier-static as v2.6.
4. ADAPTIVE_SURVIVAL=False with COLD_NET_COUPLING=0 reproduces v2.6
   run-for-run (checked in main against the v2.6 module).
5. All other v2.6 levers kept unchanged.


v2.6 updates (2026-11-23) — nutrient-growth coupling overhaul on v2.5:
1. Scavenging rate cranked and made a swept lever: SCAV_RATE_OPTIONS =
   (5e-4, 1e-3, 2e-3) kg P / kg dry / sol. Default
   SCAV_KG_P_PER_KG_DRY_PER_SOL = 2e-3, the TOP of the v2.5 Mars-plausible
   range (~1e-4 to 2e-3). Every option gets its own solved doubling time
   and its own full 12-cell ensemble.
2. Doubling time re-solved toward v2.4's 5.8 sols with scavenging
   carrying P, SAME criterion as v2.5 (geo-mean baseline 0.50% growth
   unclipped >200 sols on rover-grade soil, P import 0). The solve
   cannot reach 5.8: the binding limit is the total rover-grade P
   inventory in the working volume, not the conversion rate. D=5.8 is
   run as a labelled, UNSCORED sensitivity case.
3. Per-cell survival-center override: SURVIVAL_CENTER_SEVERE_1PCT = 0.96
   applies to the severe 1.00% cell only (all other cells keep
   SURVIVAL_CENTER 0.95). Draws still clamp at SURVIVAL_CAP 0.97.
4. Kept: CO2 hard gate with throttle (default) / vent / off; 60% hard
   reductase floor; 18% chlorite burden spike; RECYCLE_FRACTION 0.8;
   N_IMPORT_KG_PER_SOL 7.251e13 (v2.5 value, held — NOT zero);
   P_IMPORT_KG_PER_SOL 0 with P_IMPORT_REALISTIC_MAX_KG_PER_SOL
   (8.47e7) as the fallback-only lever.


v2.5 updates (2026-11-23) — four fixes, all named constants below:
1. CO2 freeze is a HARD GATE from sol 1 (FREEZE_HARD_GATE). Every sol
   the CO2 inventory is tested BEFORE the O2 target; a run whose CO2
   drops below FREEZE_CO2_T on any sol is a failure whatever its O2
   total. The v2.4 O2-first order is kept only as a labelled
   comparison mode (run_once(..., o2_first=True)), never as default.
   Freeze control (FREEZE_CONTROL_MODE):
     "throttle" (DEFAULT) — the swarm down-regulates O2 output so the
        cumulative O2 never exceeds O2_CEILING_KG = freeze-equivalent
        O2 x (1 - FREEZE_MARGIN_FRAC). The ceiling sits above the O2
        target, so a throttled run can still clear.
     "vent" — a thermal vent / non-photochemical quench sheds up to
        VENT_SHED_CAPACITY_KG_O2_PER_SOL of over-ceiling production per
        sol as heat; any excess beyond that capacity still fixes CO2
        and can trip the hard gate. Finite-capacity sensitivity only.
     "off" — no control (used for the ordering comparison).
2. Phosphorus scavenging trait (SCAV_ENABLED, SCAV_KG_P_PER_KG_DRY_PER_SOL).
   Each unit solubilises mineral P (apatite/merrillite) from the
   rover-grade regolith at a specific rate per kg of dry biomass,
   first-order in the mineral P still remaining. The mineral reservoir
   is the rover-grade P in the default working volume
   (REGOLITH_P2O5_WT_PCT) minus the already-labile INITIAL_P_POOL_KG.
   The module costs SCAV_PROTEOME of heterologous proteome.
3. Slower growth: DOUBLING_SOLS is SOLVED (binary search, shown in
   stdout) as the shortest doubling time at which geo-mean growth at
   baseline 0.50% stays unclipped for >200 sols on rover-grade soil
   alone (scavenging on, P import 0, N import and recycle held).
4. P import kept as a fallback lever, default 0. Its realistic upper
   bound P_IMPORT_REALISTIC_MAX_KG_PER_SOL is the ENTIRE present-day
   Earth phosphate-rock industry transposed to Mars (~8.5e7 kg P/sol),
   ~1.2e5x below the v2.4 requirement-sized 9.887e12 kg P/sol.
Other changes required by the fixes (documented):
- The v2.4 "hopeless" shortcut (growth ended and constant production
  cannot reach the target) is no longer a valid bound once scavenged P
  can re-feed growth after a clip, so it is removed. Runs now end by
  clear, freeze, extinction (units < EXTINCTION_UNITS), or MAX_SOLS.
- RNG layout: each cell draws N_RUNS per-run seeds from Random(SEED);
  run i always gets the same per-sol survival draws in every variant,
  so the ordering comparison is paired run-for-run. Per-sol draws are
  therefore not the identical stream v2.4 used.
- Mean survival is now the mean of EVERY per-sol clamped draw (v2.4
  reported the last-sol draw; that column is kept as mean_last_s).
  Worst per-sol draw is the min over every sol of every run.

v2.4 updates (2026-11-23):
- Phosphorus import: named constant P_IMPORT_KG_PER_SOL replenishes
  the environmental P pool each sol. The default, 9.887e12 kg P/sol,
  is SIZED (binary search, not a guess) so that, with N_IMPORT already
  at 7.251e13, the enlarged INITIAL_P_POOL_KG already in place, and
  RECYCLE_FRACTION at 0.8, geo-mean unconstrained growth at baseline
  0.50% lasts at least 200 sols at the default 1.0e12 m3 volume.
  Not a physical flux (~6x a global 1 m rind at 0.15% P over 200 sols).
- Enlarged initial P pool: INITIAL_P_POOL_KG = 1.5e11 (matches the N
  pool mass; 0.01% elemental P = 0.0229 wt% P2O5).
- v2.4 passed 12/12 only because O2 was tested before CO2 freeze:
  265/2,880 clears crossed freeze on the same sol.

v2.3 updates (2026-11-23):
- Atmospheric N import N_IMPORT_KG_PER_SOL = 7.251e13 (requirement-
  sized, not fixation physics) and RECYCLE_FRACTION = 0.8 of dead-unit
  N and P (including chlorite-killed units).

v2.2 updates (2026-11-23):
- Explicit N and P pools in a documented accessible-regolith volume;
  1.5% perchlorate column; hard 60% reductase floor with chlorite
  rapid-kill; parallel lattice thermal-cycling sim (Earth years).

v2.1: survival cap 0.95 -> 0.97; doubling 6.3 -> 5.8 sols.
v2.0: oxidative factor at severe 0.93 -> 0.99; perchlorate LD50 3 -> 10%.
v1.9: survival floor 2% -> 10%; LD50 2 -> 3%; inoculum 1e10 -> 1e12.
v1.8 mechanisms retained: light-repressed toggle, orthogonal
promoters/RBSs, 15% proteome cap, burden sensor with cold suppression,
reductase 60% post-multiplication floor, combined-stress ensemble.

Seed fixed for reproducibility.
Target: 5.25e15 kg O2 (planetary breathable threshold).
"""

import math
import random
from collections import Counter

TARGET_KG = 5.25e15
PER_UNIT_KG = 2.0
INOCULUM = 1e12
# v2.6: re-solved at the v2.6 default scavenging rate (2e-3). v2.5 fix 3: SOLVED, not guessed. Shortest doubling time (rounded UP
# to 0.01 sol) for which geo-mean growth at baseline 0.50% stays
# unclipped for >200 sols on rover-grade soil alone (scavenging on,
# P import 0, N import and recycle held). See solve_doubling_sols()
# and the "v2.5 doubling-time solve" block in stdout.
DOUBLING_SOLS = 8.72   # v2.10: re-solved at rate 5e-3 (v2.9: 8.82 at 1e-3)
V25_DOUBLING_SOLS = 8.50
V24_DOUBLING_SOLS = 5.8
SURVIVAL_CENTER = 0.95
# v2.6 per-cell override: severe tier at 1.00% perchlorate only.
# ASSUMPTION (a design target, not a measured survival): the v2.5 sweep
# put that cell's geo-mean net=1 crossing at 0.95145 (D 8.50).
SURVIVAL_CENTER_SEVERE_1PCT = 0.96
SURVIVAL_SPREAD = 0.05

# --- v2.7 adaptive per-sol survival center ---
ADAPTIVE_SURVIVAL = True
ADAPTIVE_NET_TARGET = 1.0
ADAPTIVE_CENTER_MIN = 0.95   # v2.6 default center
ADAPTIVE_CENTER_MAX = 0.99   # above SURVIVAL_CAP on purpose; cap unchanged
# Lower bound is max(ADAPTIVE_CENTER_MIN, v2.6 static per-cell center).
ADAPTIVE_FLOOR_AT_STATIC = True
# --- v2.7 cold read and cold net coupling (ASSUMPTIONS) ---
COLD_CALIBRATION_CENTER = 0.98
COLD_CALIBRATION_CELL = ("severe", 0.50)
# f_cold = 1 - COLD_NET_COUPLING * (1 - cold). Calibrated value; the
# calibration is recomputed and printed in main() (calibrate_cold_coupling).
COLD_NET_COUPLING = 0.036636   # legacy v2.7 fitted value, "linear_fitted" only
COLD_VARIATION_SPREAD = 0.0
COLD_MIN = 0.05
COLD_MAX = 1.0
COLD_READ_RESOLUTION = 0.001
CO2_START_T = 25e12
CO2_PER_KG_O2 = 2.75
FREEZE_CO2_T = 10e12
MAX_SOLS = 200_000
N_RUNS = 240
SEED = 42

PERCH_LEVELS = [0.50, 0.75, 1.00, 1.50]
# The v2.5 brief lists 0.50/0.75/1.00%; 1.50% is kept from v2.2-v2.4 so
# the ensemble stays 12 cells and comparable. Reported as its own column.
BRIEF_PERCH_LEVELS = [0.50, 0.75, 1.00]
STRESS_TIERS = ["baseline", "moderate", "severe"]
STRESS_FACTOR = {"baseline": 1.0, "moderate": 1.5, "severe": 2.0}
GATE = {"baseline": 0.70, "moderate": 0.60, "severe": 0.50}
SURVIVAL_FLOOR = 0.10
SURVIVAL_CAP = 0.97          # used only by SURVIVAL_CAP_MODE "hard097"
# --- v2.8 fix 1: survival draw cap ---
SURVIVAL_CAP_MODE = "soft"   # "soft" | "none" | "hard097"
SURVIVAL_SOFT_KNEE = 0.98
SURVIVAL_CEILING = 1.0       # physical limit, survival fraction <= 1

# --- v2.8 fix 2: grounded cold model ---
COLD_MODEL = "arrhenius_growth"   # | "arrhenius_survival" | "linear_fitted"
GAS_R = 8.314462618
# Symeonidou et al. 2024 Extremophiles (PMC11266278) Table 2, control.
DR_CO2_UG_PER_DAY_25C = 812.63
DR_CO2_UG_PER_DAY_0C = 66.03
COLD_T_WARM_C = 25.0         # cold factor 1.0
COLD_T_COLD_C = 0.0          # cold factor 0.0
COLD_EA_J_PER_MOL = (GAS_R * math.log(DR_CO2_UG_PER_DAY_25C / DR_CO2_UG_PER_DAY_0C)
                     / (1.0 / (273.15 + COLD_T_COLD_C) - 1.0 / (273.15 + COLD_T_WARM_C)))

# --- v2.5 fix 1: CO2 freeze hard gate and freeze control ---
# Hard gate: CO2 below FREEZE_CO2_T on ANY sol = failure, tested
# before the O2 target. Must stay True for scored results.
FREEZE_HARD_GATE = True
# "throttle" (default) | "vent" | "off"
FREEZE_CONTROL_MODE = "throttle"
# Throttle ceiling sits this fraction below the freeze-equivalent O2.
# 1% of 5.4545e15 kg leaves the ceiling (5.40e15) above the 5.25e15
# target. Assumption: control precision of ~1% of cumulative output.
FREEZE_MARGIN_FRAC = 0.01
# Vent mode only: max over-ceiling production shed as heat per sol
# (kg O2-equivalent). ASSUMPTION, unvalidated; sensitivity only.
VENT_SHED_CAPACITY_KG_O2_PER_SOL = 5.0e13
# A run whose standing population falls below this is extinct (fail).
EXTINCTION_UNITS = 1.0

# Hard floor cannot be removed by lowering REDUCTASE_FLOOR.
HARD_REDUCTASE_FLOOR = 0.60
REDUCTASE_FLOOR = 0.60
REDUCTASE_PROTEOME = 0.03
AFP_PROTEOME = 0.04
MAA_PROTEOME = 0.04
BURDEN_CAP = 0.15
PENALTY_RATE = 0.20
BURDEN_TRIGGER = 1.5
CHLORITE_BURDEN_SPIKE = 0.18
# Remaining fraction after 10 sols = 0.10 => 90% dead in 10 sols.
CHLORITE_SURVIVAL_PER_SOL = 0.10 ** (1.0 / 10.0)

PERCH_LD50 = 10.0
PERCH_HILL = 2.0

COLD_SUPPRESSION = {"baseline": 1.0, "moderate": 0.5, "severe": 0.25}
# --- v2.9 thermal habitat (ASSUMPTIONS: constant interior, no energy budget) ---
HABITAT_ENABLED = True
HABITAT_MODE = {"baseline": "ambient", "moderate": "insulated",
                "severe": "insulated_heated"}
HABITAT_INTERIOR_C = 25.0
HABITAT_RESTORES_PROTEOME = True
DRAW_HIST_BINS = 1000
OXIDATIVE_FACTOR = {"baseline": 1.0, "moderate": 0.97, "severe": 0.99}
# --- v2.11 CANDIDATE lever 2 (2026-11-24, t124u; pending Craig landing):
# per-cell oxidative override on the four binding cells plus moderate
# 1.50%. Every other cell keeps OXIDATIVE_FACTOR[tier] (baseline 1.0,
# moderate 0.97, severe 0.99). ox_factor uses dict.get(); missing keys
# fall back to the tier default. This is a CANDIDATE default, not yet
# the canonical scored run (scored A remains ox10 until Craig lands
# this). No MAA repair boost is present or enabled.
#
# Binding-cell values are the lowest tested overrides from the UNSCORED
# ox_sweep12 sweep that cleared 240/240 at seed 42, INOCULUM 1e12:
#   moderate 0.50%  0.979    (unaided threshold 0.978822)
#   moderate 0.75%  0.9865   (unaided threshold 0.9819)
#   moderate 1.00%  0.9895   (unaided threshold 0.986145)
#   severe   1.50%  0.9989   (unaided threshold 0.998349)
# These are fitted survival TARGETS for the lab screen, not measured
# values. A 240/240 at these numbers shows the threshold math works,
# not that a real strain has been shown to hit them at Mars dose rates.
# Margin above the unaided threshold matters: moderate 0.75% at 0.982
# (just above 0.9819; expected net 1.000130) cleared only 239/240, with
# a single timeout on run 96. The mid point 0.9865 was the lowest tested
# value that actually cleared 240/240.
#
# moderate 1.50% keeps the v2.10 scored ISS detection-floor bound of 1.0
# (no oxidative/radiation survival penalty):
#   ISS detection-floor bound: a three-year ISS exposure of ~715 mGy
#   showed no measurable survival effect.
#   Mars surface background radiation: 76-96 mGy/year.
#   200 sols = 200 * 88775.244 s / 86400 s/day = 205.498 Earth days
#   ≈ 205.5 d ≈ 0.5626 Earth years (sols per Earth year =
#   365.25 * 86400 / 88775.244 ≈ 355.48), cited as ≈ 0.563 yr.
#   Moderate-tier dose over a 200-sol run:
#   76 mGy/yr * 0.563 yr ≈ 43 mGy, 96 mGy/yr * 0.563 yr ≈ 54 mGy
#   (~43-54 mGy).
#   That dose sits ~13-17x below the ISS anchor (715/54 ≈ 13.2,
#   715/43 ≈ 16.6; ≥~13x).
#   Therefore the moderate 1.50% override is 1.0. Supersedes t66u's
#   0.99808, which used an extrapolated slope from high-dose-rate
#   D. radiodurans curves and is retired.
# Retired t66u fit constants (not the candidate override). Kept so the
# A-low / A-high range-end ablations in main() still run. Those
# ablations temporarily replace the whole dict with moderate 1.50 only.
OX_FIT_DOSE_GY_PER_SOL = 0.5
OX_FIT_SLOPE_LOG10_PER_GY = 5.0 / 3000.0
OX_FIT_ACUTE_SLOPE_LOG10_PER_GY = 1.0 / 8000.0
OX_MODERATE_FITTED = round(10.0 ** (-OX_FIT_DOSE_GY_PER_SOL * OX_FIT_SLOPE_LOG10_PER_GY), 5)
OX_MODERATE_RANGE_LOW = round(10.0 ** (-1.0 * OX_FIT_SLOPE_LOG10_PER_GY), 5)          # 1.0 Gy/sol
OX_MODERATE_RANGE_HIGH = round(10.0 ** (-0.5 * OX_FIT_ACUTE_SLOPE_LOG10_PER_GY), 5)   # acute D10
OX_PERCELL_OVERRIDE_ENABLED = True
OX_PERCELL_OVERRIDE = {
    ("moderate", 0.50): 0.979,
    ("moderate", 0.75): 0.9865,
    ("moderate", 1.00): 0.9895,
    ("moderate", 1.50): 1.0,
    ("severe", 1.50): 0.9989,
}


def ox_factor(tier, perch):
    if OX_PERCELL_OVERRIDE_ENABLED:
        v = OX_PERCELL_OVERRIDE.get((tier, round(perch, 2)))
        if v is not None:
            return v
    return OXIDATIVE_FACTOR[tier]

# --- Nutrient inventory (ASSUMPTIONS, not measured) ---
# Default volume is a 1000 km x 1000 km x 1 m regional rind (unchanged).
N_REGOLITH_PCT = 0.01
P_REGOLITH_PCT = 0.005  # v2.2/v2.3 value, comparison only
REGOLITH_DENSITY_KG_M3 = 1500.0
ACCESSIBLE_REGOLITH_M3 = 1.0e12
UNIT_DRY_KG = 2.0
BIOMASS_N_FRAC = 0.11   # typical cyanobacterial dry-mass N
BIOMASS_P_FRAC = 0.015  # typical cyanobacterial dry-mass P
NUTRIENT_VIABLE_UNITS = 1.0
# Atmospheric N import (kg N / sol), v2.3 requirement-sized value, held.
N_IMPORT_KG_PER_SOL = 7.251e13
# Labile (already bioavailable) environmental P at t=0, v2.4 value, held.
# v2.5 treats it as the labile 4.6% slice of the rover-grade inventory.
INITIAL_P_POOL_KG = 1.5e11
# Fraction of dead-unit N and P returned to the environmental pools.
RECYCLE_FRACTION = 0.8

# --- v2.5 fix 2: phosphorus scavenging trait (ASSUMPTIONS) ---
# Rover-grade soil P. Approximate published APXS soil figures sit in a
# ~0.3-1.0 wt% P2O5 window (many Gale soils ~0.8-1.0 wt%). 0.50 wt%
# P2O5 (= 0.218% elemental P) is a deliberately below-Gale-average
# central value. Sensitivity at 0.3 and 1.0 is printed.
REGOLITH_P2O5_WT_PCT = 0.50
P_MASS_FRAC_IN_P2O5 = 61.973762 / 141.944522   # 0.4366
SCAV_ENABLED = True
# kg P solubilised per kg dry biomass per sol, x (mineral P left /
# mineral P at t=0). Grounding (order of magnitude, assumptions):
#  - Earth phosphate-solubilising bacteria in NBRIP broth at 28 C with
#    10 g/L glucose release ~15-58 mg P/L from rock phosphate in 3-7
#    days (75-420 mg/L from the far more soluble Ca3(PO4)2), i.e.
#    ~2-19 mg P/L/day. Assuming ~1-2 g/L dry bacterial biomass (not
#    reported in those assays) gives ~1e-3 to 2e-2 kg P/kg dry/day.
#  - Mars penalty: cold (~30-60 C below the assay), thin liquid-water
#    films, no free glucose (organic acids must come from fixed carbon),
#    igneous apatite/merrillite rather than sedimentary rock phosphate.
#    Assumed >=10x slower -> ~1e-4 to 2e-3 kg P/kg dry/sol.
#  - Default 5e-4 is roughly the geometric middle of that Mars range.
#    1 sol ~ 1.03 Earth days (ignored).
SCAV_KG_P_PER_KG_DRY_PER_SOL = 5.0e-3   # v2.10 lever 1 (USER-CHOSEN, t65u); ABOVE the 2e-3 top of the v2.5 plausible range. v2.9: 1e-3
# v2.6 swept options; each gets its own solved doubling and ensemble.
SCAV_RATE_OPTIONS = (5.0e-4, 1.0e-3, 2.0e-3, 5.0e-3)
# Heterologous proteome cost of the scavenging module (organic-acid /
# gcd-pqq glucose-dehydrogenase + phytase/phosphatase export).
# ASSUMPTION. Baseline (reductase 1.0) total becomes exactly 0.15 =
# the cap (0.05+0.04+0.04+0.02; penalty applies only ABOVE the cap,
# so zero headroom, no penalty); moderate/severe 0.1375.
SCAV_PROTEOME = 0.02

# --- v2.5 fix 4: P import fallback, realistic bound ---
SOLS_PER_EARTH_YEAR = 365.25 * 86400.0 / 88775.244
# Present-day world phosphate-rock mine output ~220-240 Mt/yr (USGS
# Mineral Commodity Summaries order of magnitude) at ~30 wt% P2O5
# marketable grade. ASSUMPTIONS.
WORLD_PHOSPHATE_ROCK_KG_PER_EARTH_YR = 2.3e11
PHOSPHATE_ROCK_P2O5_FRAC = 0.30
# Realistic upper bound: the WHOLE Earth phosphate industry, delivered
# to Mars every year (far beyond any launch or ISRU plan; a generous
# bound, not a forecast). = 2.3e11 * 0.30 * 0.4366 / 355.48 kg P/sol.
P_IMPORT_REALISTIC_MAX_KG_PER_SOL = (
    WORLD_PHOSPHATE_ROCK_KG_PER_EARTH_YR * PHOSPHATE_ROCK_P2O5_FRAC
    * P_MASS_FRAC_IN_P2O5 / SOLS_PER_EARTH_YEAR)
# Default 0: growth must not depend on an import line. Fallback runs
# use P_IMPORT_REALISTIC_MAX_KG_PER_SOL. Never exceed that bound.
P_IMPORT_KG_PER_SOL = 0.0
V24_P_IMPORT_KG_PER_SOL = 9.887e12  # reference only, NOT used

# --- Lattice long-horizon (ASSUMPTIONS, not measured; unchanged) ---
LATTICE_CYCLES_PER_EARTH_YEAR = 365.25 * 86400.0 / 88775.244
LATTICE_LOSS_PER_CYCLE = 1.0e-5
LATTICE_DUST_TAU_YEARS = 20.0
CASCADE_UNLOCK_INTEGRITY = 0.50
LATTICE_TEAR_INTEGRITY = 0.25
LATTICE_HORIZON_YEARS = 15.0


def unit_n_kg():
    return UNIT_DRY_KG * BIOMASS_N_FRAC


def unit_p_kg():
    return UNIT_DRY_KG * BIOMASS_P_FRAC


def initial_nutrient_pools():
    mass = ACCESSIBLE_REGOLITH_M3 * REGOLITH_DENSITY_KG_M3
    n_pool = mass * (N_REGOLITH_PCT / 100.0)
    p_pool = INITIAL_P_POOL_KG
    return mass, n_pool, p_pool


def implied_p_regolith_pct():
    mass = ACCESSIBLE_REGOLITH_M3 * REGOLITH_DENSITY_KG_M3
    return 100.0 * INITIAL_P_POOL_KG / mass


def p_wt_pct_as_p2o5(p_wt_pct):
    """Elemental P wt% -> P2O5 wt%. P2O5 is 43.64% P by mass."""
    return p_wt_pct * (141.944522 / 61.973762)


def reductase_survival(perchlorate_pct):
    return 1.0 / (1.0 + (perchlorate_pct / PERCH_LD50) ** PERCH_HILL)


def effective_reductase_floor():
    """60% hard bound; lowering REDUCTASE_FLOOR cannot punch through."""
    return max(HARD_REDUCTASE_FLOOR, REDUCTASE_FLOOR)


def chlorite_kill_factor(reductase, total_het, floor_override=None):
    """Rapid kill if reductase is below the hard floor or burden > 18%.

    Normal ensemble never enters this branch because proteome_levels
    clamps reductase to the hard floor and total heterologous load stays
    under 15%. floor_override lets the breach demo bypass the clamp.
    """
    r = reductase if floor_override is None else floor_override
    if r < HARD_REDUCTASE_FLOOR or total_het > CHLORITE_BURDEN_SPIKE:
        return CHLORITE_SURVIVAL_PER_SOL
    return 1.0




def proteome_levels(stress_factor, cold_factor):
    """v1.8 clamp logic, plus the v2.5 scavenging module's proteome."""
    burden_throttle = min(1.0, max(0.0, (stress_factor - 1.0) / 1.0))
    combined = burden_throttle * cold_factor
    floor = effective_reductase_floor()
    reductase = max(floor, 1.0 - combined)
    residual = max(0.0, combined - (1.0 - floor))
    afp = max(0.0, AFP_PROTEOME * (1.0 - min(1.0, residual * 2.0)))
    maa = max(0.0, MAA_PROTEOME * (1.0 - min(1.0, max(0.0, residual * 2.0 - 1.0))))
    scav = SCAV_PROTEOME if SCAV_ENABLED else 0.0
    total = REDUCTASE_PROTEOME * (reductase / floor) + afp + maa + scav
    return reductase, afp, maa, total, combined


def rover_total_p_kg(p2o5_wt_pct=None):
    """Elemental P in the default working volume at rover-grade P2O5."""
    if p2o5_wt_pct is None:
        p2o5_wt_pct = REGOLITH_P2O5_WT_PCT
    mass = ACCESSIBLE_REGOLITH_M3 * REGOLITH_DENSITY_KG_M3
    return mass * (p2o5_wt_pct / 100.0) * P_MASS_FRAC_IN_P2O5


def mineral_p0_kg(p2o5_wt_pct=None):
    """Mineral (not yet labile) P = rover-grade total - labile pool."""
    return max(0.0, rover_total_p_kg(p2o5_wt_pct) - INITIAL_P_POOL_KG)


def survival_center_for(tier, perch):
    """v2.6: per-cell survival center (override for severe 1.00% only)."""
    if tier == "severe" and abs(perch - 1.00) < 1e-9:
        return SURVIVAL_CENTER_SEVERE_1PCT
    return SURVIVAL_CENTER


def habitat_active(tier):
    return HABITAT_ENABLED and HABITAT_MODE.get(tier, "ambient") != "ambient"


def cold_from_temp_c(t_c):
    """Inverse of the v2.8 linear map (0 C -> 0, 25 C -> 1), clipped."""
    c = (t_c - COLD_T_COLD_C) / (COLD_T_WARM_C - COLD_T_COLD_C)
    return min(1.0, max(0.0, c))


def tier_cold(tier):
    """Effective cold factor for growth/survival/center (habitat-aware)."""
    if habitat_active(tier):
        return cold_from_temp_c(HABITAT_INTERIOR_C)
    return COLD_SUPPRESSION[tier]


def tier_prot_cold(tier):
    """Cold factor seen by proteome_levels."""
    if habitat_active(tier) and HABITAT_RESTORES_PROTEOME:
        return cold_from_temp_c(HABITAT_INTERIOR_C)
    return COLD_SUPPRESSION[tier]


def cold_temp_c(cold):
    """ASSUMED linear map: cold 1.0 -> 25 C, cold 0.0 -> 0 C."""
    return COLD_T_COLD_C + cold * (COLD_T_WARM_C - COLD_T_COLD_C)


def cold_rate_ratio(cold):
    """Arrhenius metabolic rate at the mapped temperature / rate at 25 C."""
    if cold >= 1.0:
        return 1.0
    t = 273.15 + cold_temp_c(cold)
    tw = 273.15 + COLD_T_WARM_C
    return math.exp(-COLD_EA_J_PER_MOL / GAS_R * (1.0 / t - 1.0 / tw))


def cold_net_factor(cold):
    """Cold factor applied to per-sol SURVIVAL."""
    if COLD_MODEL == "linear_fitted":
        return 1.0 - COLD_NET_COUPLING * (1.0 - cold)
    if COLD_MODEL == "arrhenius_survival":
        return cold_rate_ratio(cold)
    return 1.0


def cold_growth_mult(cold):
    """Cold multiplier on the replication RATE (exponent of 2^(1/D))."""
    if COLD_MODEL == "arrhenius_growth":
        return cold_rate_ratio(cold)
    return 1.0


def cell_growth(cold, doubling):
    return 2 ** (cold_growth_mult(cold) / doubling)


def survival_transform(raw):
    """v2.8 draw map: floor, then cap per SURVIVAL_CAP_MODE."""
    if SURVIVAL_CAP_MODE == "hard097":
        return min(SURVIVAL_CAP, max(SURVIVAL_FLOOR, raw))
    if SURVIVAL_CAP_MODE == "none":
        return min(SURVIVAL_CEILING, max(SURVIVAL_FLOOR, raw))
    if SURVIVAL_CAP_MODE == "soft":
        x = max(SURVIVAL_FLOOR, raw)
        k = SURVIVAL_SOFT_KNEE
        if x <= k:
            return x
        w = SURVIVAL_CEILING - k
        return k + w * math.tanh((x - k) / w)
    raise ValueError(SURVIVAL_CAP_MODE)


def shoulder_threshold():
    if SURVIVAL_CAP_MODE == "hard097":
        return SURVIVAL_CAP
    if SURVIVAL_CAP_MODE == "soft":
        return SURVIVAL_SOFT_KNEE
    return SURVIVAL_CEILING


_QZ = [-9.0 + 18.0 * i / 3600 for i in range(3601)]
_QW = [math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi) * (18.0 / 3600) for z in _QZ]
_EG_CACHE = {}


def expected_geo_draw(center):
    """Geo-mean of the transformed draw at a center, current cap mode."""
    if SURVIVAL_CAP_MODE == "hard097":
        return geo_clamped_analytic(center, cap=SURVIVAL_CAP)
    if SURVIVAL_CAP_MODE == "none":
        return geo_clamped_analytic(center, cap=SURVIVAL_CEILING)
    key = (center, SURVIVAL_SOFT_KNEE, SURVIVAL_SPREAD, SURVIVAL_FLOOR)
    v = _EG_CACHE.get(key)
    if v is None:
        mu = math.log(center)
        e = sum(w * math.log(survival_transform(math.exp(mu + SURVIVAL_SPREAD * z)))
                for z, w in zip(_QZ, _QW))
        v = math.exp(e)
        _EG_CACHE[key] = v
    return v


def cold_rng_for(rng):
    """Separate per-run RNG for cold variation. Seeded from a COPY of the
    survival RNG state so the survival draw stream is not consumed."""
    st = random.Random()
    st.setstate(rng.getstate())
    return random.Random(st.getrandbits(64) ^ 0xC01D)


def read_cold(tier_cold, cold_rng=None):
    """Per-sol cold suppression reading (quantised)."""
    c = tier_cold
    if cold_rng is not None and COLD_VARIATION_SPREAD > 0.0:
        c = tier_cold * math.exp(COLD_VARIATION_SPREAD * cold_rng.gauss(0.0, 1.0))
    c = min(COLD_MAX, max(COLD_MIN, c))
    if COLD_READ_RESOLUTION > 0.0:
        c = round(c / COLD_READ_RESOLUTION) * COLD_READ_RESOLUTION
    return c


def geo_clamped_analytic(center, cap=None, floor=None, spread=None):
    """Exact geo-mean of the clamped lognormal draw (closed form)."""
    cap = SURVIVAL_CAP if cap is None else cap
    floor = SURVIVAL_FLOOR if floor is None else floor
    sd = SURVIVAL_SPREAD if spread is None else spread
    mu, a, b = math.log(center), math.log(floor), math.log(cap)
    al, be = (a - mu) / sd, (b - mu) / sd
    cdf = lambda x: 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))
    pdf = lambda x: math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)
    e = (a * cdf(al) + b * (1.0 - cdf(be)) + mu * (cdf(be) - cdf(al))
         + sd * (pdf(al) - pdf(be)))
    return math.exp(e)


def cap_clamp_prob(center):
    """P(raw lognormal draw > shoulder threshold) at a given center
    (0.97 cap for hard097, knee for soft, 1.0 for none)."""
    z = (math.log(shoulder_threshold()) - math.log(center)) / SURVIVAL_SPREAD
    return 0.5 * (1.0 - math.erf(z / math.sqrt(2.0)))


def non_draw_factor(tier, perch, cold, doubling):
    """Everything in expected net growth except the clamped draw."""
    r, a, m, tot, c = proteome_levels(STRESS_FACTOR[tier], tier_prot_cold(tier))
    f = ox_factor(tier, perch) * cold_net_factor(cold)
    if tot > BURDEN_CAP:
        f *= 1.0 - min(0.9, PENALTY_RATE * (tot - BURDEN_CAP) * STRESS_FACTOR[tier])
    f *= reductase_survival(perch) * chlorite_kill_factor(r, tot)
    return f * cell_growth(cold, doubling)


_ADAPT_CACHE = {}


def adaptive_lower(tier, perch):
    if ADAPTIVE_FLOOR_AT_STATIC:
        return max(ADAPTIVE_CENTER_MIN, survival_center_for(tier, perch))
    return ADAPTIVE_CENTER_MIN


def adaptive_center(tier, perch, cold, doubling=None):
    """Center whose expected clamped draw gives expected net = target,
    clipped to [lower, ADAPTIVE_CENTER_MAX]. Returns (center,
    expected_net_at_center, hit_max)."""
    if doubling is None:
        doubling = DOUBLING_SOLS
    key = (tier, perch, cold, doubling, ADAPTIVE_NET_TARGET, COLD_NET_COUPLING,
           ADAPTIVE_CENTER_MIN, ADAPTIVE_CENTER_MAX, ADAPTIVE_FLOOR_AT_STATIC,
           SURVIVAL_CAP, SURVIVAL_CENTER_SEVERE_1PCT, SURVIVAL_CENTER,
           SURVIVAL_CAP_MODE, SURVIVAL_SOFT_KNEE, COLD_MODEL,
           HABITAT_ENABLED, HABITAT_RESTORES_PROTEOME, HABITAT_INTERIOR_C,
           ox_factor(tier, perch))
    hit = _ADAPT_CACHE.get(key)
    if hit is not None:
        return hit
    k = non_draw_factor(tier, perch, cold, doubling)
    lo, hi = adaptive_lower(tier, perch), ADAPTIVE_CENTER_MAX
    net = lambda c: expected_geo_draw(c) * k
    if net(lo) >= ADAPTIVE_NET_TARGET:
        out = (lo, net(lo), False)
    elif net(hi) < ADAPTIVE_NET_TARGET:
        out = (hi, net(hi), True)
    else:
        a, b = lo, hi
        for _ in range(60):
            mid = 0.5 * (a + b)
            if net(mid) >= ADAPTIVE_NET_TARGET:
                b = mid
            else:
                a = mid
        out = (b, net(b), False)
    _ADAPT_CACHE[key] = out
    return out


def calibrate_cold_coupling(doubling=None):
    """COLD_NET_COUPLING such that the calibration cell at its tier cold
    needs exactly COLD_CALIBRATION_CENTER."""
    if doubling is None:
        doubling = DOUBLING_SOLS
    tier, perch = COLD_CALIBRATION_CELL
    cold = COLD_SUPPRESSION[tier]
    saved = globals()["COLD_NET_COUPLING"]
    globals()["COLD_NET_COUPLING"] = 0.0
    k0 = non_draw_factor(tier, perch, cold, doubling)
    globals()["COLD_NET_COUPLING"] = saved
    need_f = ADAPTIVE_NET_TARGET / (expected_geo_draw(COLD_CALIBRATION_CENTER) * k0)
    return (1.0 - need_f) / (1.0 - cold)


def o2_ceiling_kg():
    return freeze_o2_kg() * (1.0 - FREEZE_MARGIN_FRAC)


def grow_one_sol(units, s_eff, growth, n_rem, p_rem, m_rem, m0,
                 p_import, scav_rate):
    """One sol of nutrient bookkeeping + replication (shared by the
    stochastic ensemble and the deterministic geo-mean solves).

    Order: N import, P import, P scavenging (mineral -> labile, by the
    standing population at the start of the sol), mortality, recycle,
    replication limited by N and P. Returns the new state and the clip
    reason (None if growth was not nutrient-limited this sol).
    """
    n_per = UNIT_DRY_KG * BIOMASS_N_FRAC
    p_per = UNIT_DRY_KG * BIOMASS_P_FRAC
    n_viable = NUTRIENT_VIABLE_UNITS * n_per
    p_viable = NUTRIENT_VIABLE_UNITS * p_per
    n_rem += N_IMPORT_KG_PER_SOL
    p_rem += p_import
    scav = 0.0
    if scav_rate > 0.0 and m_rem > 0.0 and m0 > 0.0:
        scav = scav_rate * UNIT_DRY_KG * units * (m_rem / m0)
        if scav > m_rem:
            scav = m_rem
        m_rem -= scav
        p_rem += scav
    survivors = units * s_eff
    dead = units - survivors
    if dead < 0.0:
        dead = 0.0
        survivors = units
    n_rem += dead * n_per * RECYCLE_FRACTION
    p_rem += dead * p_per * RECYCLE_FRACTION
    reason = None
    if (n_rem > n_viable) and (p_rem > p_viable):
        proposed = survivors * growth
        added = proposed - survivors
        avail_n = n_rem - n_viable
        avail_p = p_rem - p_viable
        max_add = min(added, avail_n / n_per, avail_p / p_per)
        if max_add < added:
            rs = []
            if avail_n / n_per < added:
                rs.append("N")
            if avail_p / p_per < added:
                rs.append("P")
            reason = "+".join(rs) if rs else "clip"
            added = max(0.0, max_add)
            proposed = survivors + added
        n_rem = max(0.0, n_rem - added * n_per)
        p_rem = max(0.0, p_rem - added * p_per)
        units = proposed
    else:
        rs = []
        if not (n_rem > n_viable):
            rs.append("N")
        if not (p_rem > p_viable):
            rs.append("P")
        reason = "+".join(rs) if rs else "floor"
        units = survivors
    return units, n_rem, p_rem, m_rem, scav, reason


def apply_freeze_control(o2, prod, mode, ceiling, vent_cap):
    """Return (prod_after_control, shed_kg, throttled_flag)."""
    if mode == "off" or o2 + prod <= ceiling:
        return prod, 0.0, False
    excess = o2 + prod - ceiling
    if mode == "throttle":
        return max(0.0, prod - excess), excess, True
    if mode == "vent":
        shed = min(excess, vent_cap)
        return prod - shed, shed, True
    raise ValueError(f"unknown FREEZE_CONTROL_MODE {mode!r}")


def run_once(rng, perchlorate_pct, tier, stop_on_targets=True, max_sols=None,
             doubling=None, p_import=None, scav_rate=None, control=None,
             o2_first=False, vent_cap=None, record_traj=False):
    """One stochastic run. Returns a dict.

    o2_first=False (default, v2.5 hard gate): every sol, CO2 < freeze
    is tested first and is a failure regardless of O2.
    o2_first=True reproduces the v2.4 order (O2 >= target tested first)
    for the ordering comparison only.
    """
    if doubling is None:
        doubling = DOUBLING_SOLS
    if p_import is None:
        p_import = P_IMPORT_KG_PER_SOL
    if scav_rate is None:
        scav_rate = SCAV_KG_P_PER_KG_DRY_PER_SOL if SCAV_ENABLED else 0.0
    if control is None:
        control = FREEZE_CONTROL_MODE
    if vent_cap is None:
        vent_cap = VENT_SHED_CAPACITY_KG_O2_PER_SOL
    if max_sols is None:
        max_sols = MAX_SOLS
    hard_gate = FREEZE_HARD_GATE and not o2_first
    units = INOCULUM
    o2 = 0.0
    co2_t = CO2_START_T
    perch_factor = reductase_survival(perchlorate_pct)
    sf = STRESS_FACTOR[tier]
    cf = tier_cold(tier)
    ox = ox_factor(tier, perchlorate_pct)
    growth = 2 ** (1.0 / doubling)
    sum_log_growth = 0.0
    peak_units = INOCULUM
    hist = [0] * (DRAW_HIST_BINS + 1)
    shoulder = shoulder_threshold()
    reductase, afp, maa, total_het, combined = proteome_levels(sf, tier_prot_cold(tier))
    _, n_rem, _ = initial_nutrient_pools()
    p_rem = INITIAL_P_POOL_KG
    m0 = mineral_p0_kg()
    m_rem = m0
    ceiling = o2_ceiling_kg()
    log_c = math.log(survival_center_for(tier, perchlorate_pct))
    adaptive = ADAPTIVE_SURVIVAL
    cold_rng = None
    if COLD_VARIATION_SPREAD > 0.0:
        cold_rng = cold_rng_for(rng)
    sum_center = 0.0
    min_center = 9.0
    max_center = 0.0
    at_max_sols = 0
    capped_draws = 0
    sum_log_eff = 0.0
    sum_cold = 0.0
    below_target_sols = 0
    burden_excess_acc = 0.0
    growth_end_sol = None
    growth_end_reason = None
    chlorite_hits = 0
    min_draw = 1.0
    min_eff = 1.0
    sum_draw = 0.0
    sum_eff = 0.0
    n_draws = 0
    s = 0.0
    crossed_freeze = False
    first_freeze_sol = None
    throttled_sols = 0
    shed_total = 0.0
    scav_total = 0.0
    traj = [] if record_traj else None
    outcome = "timeout"
    sol = 0
    for sol in range(1, max_sols + 1):
        cold = read_cold(cf, None if habitat_active(tier) else cold_rng)
        fc = cold_net_factor(cold)
        growth = cell_growth(cold, doubling)
        sum_log_growth += math.log(growth)
        if adaptive:
            cen, exp_net, at_max = adaptive_center(tier, perchlorate_pct, cold,
                                                   doubling)
            log_c = math.log(cen)
            if at_max:
                at_max_sols += 1
            if exp_net < ADAPTIVE_NET_TARGET - 1e-9:
                below_target_sols += 1
        else:
            cen = math.exp(log_c)
        sum_center += cen
        if cen < min_center:
            min_center = cen
        if cen > max_center:
            max_center = cen
        sum_cold += cold
        raw = rng.lognormvariate(log_c, SURVIVAL_SPREAD)
        if raw > shoulder:
            capped_draws += 1
        draw = survival_transform(raw)
        hist[min(DRAW_HIST_BINS, int(draw * DRAW_HIST_BINS))] += 1
        s = draw * ox * fc
        if total_het > BURDEN_CAP:
            excess = total_het - BURDEN_CAP
            burden_excess_acc += excess
            penalty = min(0.9, PENALTY_RATE * excess * sf)
            s = s * (1.0 - penalty)
        kill = chlorite_kill_factor(reductase, total_het)
        if kill < 1.0:
            chlorite_hits += 1
        s_eff = s * perch_factor * kill
        if draw < min_draw:
            min_draw = draw
        if s_eff < min_eff:
            min_eff = s_eff
        sum_draw += draw
        sum_eff += s_eff
        sum_log_eff += math.log(s_eff) if s_eff > 0.0 else -50.0
        n_draws += 1
        units, n_rem, p_rem, m_rem, scav, reason = grow_one_sol(
            units, s_eff, growth, n_rem, p_rem, m_rem, m0, p_import, scav_rate)
        scav_total += scav
        if units > peak_units:
            peak_units = units
        if reason is not None and growth_end_sol is None:
            growth_end_sol = sol
            growth_end_reason = reason
        prod = units * PER_UNIT_KG * reductase
        prod, shed, thr = apply_freeze_control(o2, prod, control, ceiling,
                                               vent_cap)
        if thr:
            throttled_sols += 1
            shed_total += shed
        o2 += prod
        co2_t -= prod * CO2_PER_KG_O2 / 1000.0
        if co2_t < FREEZE_CO2_T and not crossed_freeze:
            crossed_freeze = True
            first_freeze_sol = sol
        if record_traj:
            traj.append((sol, units, n_rem, p_rem, m_rem, o2, co2_t,
                         growth_end_sol, growth_end_reason))
        if stop_on_targets:
            if hard_gate:
                if co2_t < FREEZE_CO2_T:
                    outcome = "freeze"
                    break
                if o2 >= TARGET_KG:
                    outcome = "clear"
                    break
            else:
                if o2 >= TARGET_KG:
                    outcome = "clear"
                    break
                if co2_t < FREEZE_CO2_T:
                    outcome = "freeze"
                    break
            if units < EXTINCTION_UNITS:
                outcome = "extinct"
                break
    else:
        outcome = "timeout" if stop_on_targets else "horizon"
    return {
        "sol": sol, "ok": outcome == "clear", "outcome": outcome,
        "last_s": s, "units": units, "o2": o2, "co2_t": co2_t,
        "burden_excess": burden_excess_acc,
        "growth_end": growth_end_sol, "growth_reason": growth_end_reason,
        "chlorite_hits": chlorite_hits, "n_rem": n_rem, "p_rem": p_rem,
        "m_rem": m_rem, "m0": m0, "scav_total": scav_total,
        "min_draw": min_draw, "min_eff": min_eff,
        "sum_draw": sum_draw, "sum_eff": sum_eff, "n_draws": n_draws,
        "crossed_freeze": crossed_freeze, "first_freeze_sol": first_freeze_sol,
        "throttled_sols": throttled_sols, "shed_total": shed_total,
        "traj": traj,
        "sum_center": sum_center, "min_center": min_center,
        "max_center": max_center, "at_max_sols": at_max_sols,
        "capped_draws": capped_draws, "sum_log_eff": sum_log_eff,
        "sum_cold": sum_cold, "below_target_sols": below_target_sols,
        "growth": growth, "sum_log_growth": sum_log_growth,
        "peak_units": peak_units, "hist": hist,
    }


_GEO_S_CACHE = {}


def geo_s_clamped(center=None):
    if center is None:
        center = SURVIVAL_CENTER
    key = (center, SURVIVAL_CAP, SURVIVAL_FLOOR, SURVIVAL_SPREAD)
    if key not in _GEO_S_CACHE:
        _GEO_S_CACHE[key] = clamped_s_stats(*key[:2], key[2], key[3])
    return _GEO_S_CACHE[key]


def geo_s_eff(perch, tier, doubling=None):
    """Geo-mean per-sol survival incl. ox, perchlorate, burden penalty.
    v2.7: with ADAPTIVE_SURVIVAL the center is the adaptive center at the
    tier cold value (analytic geo-mean when the center is lifted above
    its lower bound; the v2.6 sampled geo-mean when it sits on it)."""
    cen = survival_center_for(tier, perch)
    if ADAPTIVE_SURVIVAL:
        cen, _, _ = adaptive_center(tier, perch, tier_cold(tier), doubling)
    if SURVIVAL_CAP_MODE != "hard097":
        geo = expected_geo_draw(cen)
    elif ADAPTIVE_SURVIVAL and cen > adaptive_lower(tier, perch) + 1e-15:
        geo = geo_clamped_analytic(cen)
    else:
        _, geo = geo_s_clamped(cen)
    s = geo * ox_factor(tier, perch) * cold_net_factor(tier_cold(tier))
    r, a, m, tot, c = proteome_levels(STRESS_FACTOR[tier], tier_prot_cold(tier))
    if tot > BURDEN_CAP:
        s *= 1.0 - min(0.9, PENALTY_RATE * (tot - BURDEN_CAP) * STRESS_FACTOR[tier])
    return s * reductase_survival(perch) * chlorite_kill_factor(r, tot)


def deterministic_run(doubling, p_import=0.0, scav_rate=None, p2o5=None,
                      perch=0.50, tier="baseline", max_sols=400):
    """Geo-mean trajectory (no stochastic draws, no stop on targets).

    Returns dict with growth_end (first clipped sol or None), reason,
    o2_target_sol (first sol cumulative O2 >= target, uncontrolled),
    freeze_sol, units at end, mineral P left fraction.
    """
    if scav_rate is None:
        scav_rate = SCAV_KG_P_PER_KG_DRY_PER_SOL if SCAV_ENABLED else 0.0
    growth = cell_growth(tier_cold(tier), doubling)
    s_eff = geo_s_eff(perch, tier, doubling)
    reductase = proteome_levels(STRESS_FACTOR[tier], tier_prot_cold(tier))[0]
    _, n_rem, _ = initial_nutrient_pools()
    p_rem = INITIAL_P_POOL_KG
    m0 = mineral_p0_kg(p2o5)
    m_rem = m0
    units = INOCULUM
    o2 = 0.0
    ge = None
    ge_reason = None
    t_sol = None
    f_sol = None
    peak = units
    freeze_eq = freeze_o2_kg()
    for sol in range(1, max_sols + 1):
        units, n_rem, p_rem, m_rem, scav, reason = grow_one_sol(
            units, s_eff, growth, n_rem, p_rem, m_rem, m0, p_import, scav_rate)
        if reason is not None and ge is None:
            ge, ge_reason = sol, reason
        peak = max(peak, units)
        o2 += units * PER_UNIT_KG * reductase
        if t_sol is None and o2 >= TARGET_KG:
            t_sol = sol
        if f_sol is None and o2 >= freeze_eq:
            f_sol = sol
    return {"growth_end": ge, "reason": ge_reason, "o2_target_sol": t_sol,
            "freeze_sol": f_sol, "units": units, "peak": peak,
            "m_left_frac": (m_rem / m0) if m0 > 0 else 0.0,
            "p_rem": p_rem, "n_rem": n_rem}


def solve_doubling_sols(horizon=200, p_import=0.0, scav_rate=None, p2o5=None,
                        perch=0.50, tier="baseline", tol=1e-6):
    """Shortest doubling time (sols) with geo-mean growth unclipped for
    > horizon sols. Bisection on D; ok(D) is monotone (slower growth
    never exhausts P sooner), checked by a scan in main()."""
    def ok(d):
        r = deterministic_run(d, p_import, scav_rate, p2o5, perch, tier,
                              max_sols=horizon + 1)
        return r["growth_end"] is None or r["growth_end"] > horizon

    lo, hi = 1.0, V24_DOUBLING_SOLS
    if ok(lo):
        return lo
    while not ok(hi):
        lo = hi
        hi *= 1.5
        if hi > 1e4:
            return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if ok(mid):
            hi = mid
        else:
            lo = mid
        if hi - lo < tol:
            break
    return hi


def solve_doubling_no_clip_before_target(p_import=0.0, scav_rate=None,
                                         p2o5=None, max_sols=3000):
    """Alternative criterion (diagnostic only): shortest D at which the
    baseline-0.50% geo-mean trajectory reaches the O2 target before (or
    without) any nutrient clip."""
    def ok(d):
        r = deterministic_run(d, p_import, scav_rate, p2o5, max_sols=max_sols)
        if r["o2_target_sol"] is None:
            return False
        return r["growth_end"] is None or r["growth_end"] > r["o2_target_sol"]

    lo, hi = 1.0, V24_DOUBLING_SOLS
    if ok(lo):
        return lo
    while not ok(hi):
        lo = hi
        hi *= 1.25
        if hi > 200:
            return None
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if ok(mid):
            hi = mid
        else:
            lo = mid
        if hi - lo < 1e-5:
            break
    return hi


def clamped_s_stats(center, cap, floor, spread, n=100000, seed=0):
    rng = random.Random(seed)
    xs = [min(cap, max(floor, rng.lognormvariate(math.log(center), spread)))
          for _ in range(n)]
    arith = sum(xs) / n
    geo = math.exp(sum(math.log(x) for x in xs) / n)
    return arith, geo


def min_survival_center_for_net(tier, perch, n=100000):
    """Smallest SURVIVAL_CENTER giving geo-mean net > 1, other v2.1 levers fixed."""
    ox = ox_factor(tier, perch)
    growth = 2 ** (1.0 / DOUBLING_SOLS)
    pf = reductase_survival(perch)
    lo, hi = 0.50, 1.20

    def gnet(c):
        _, geo = clamped_s_stats(c, SURVIVAL_CAP, SURVIVAL_FLOOR, SURVIVAL_SPREAD, n=n)
        return geo * ox * pf * growth

    if gnet(hi) <= 1.0:
        return None, gnet(hi)
    for _ in range(36):
        mid = (lo + hi) / 2.0
        if gnet(mid) > 1.0:
            hi = mid
        else:
            lo = mid
    return hi, gnet(hi)


def run_chlorite_demo(sols=10, forced_reductase=0.0, forced_burden=0.20):
    """Deliberate breach: floor bypassed and/or burden > 18%."""
    units = INOCULUM
    hist = []
    for sol in range(1, sols + 1):
        kill = chlorite_kill_factor(forced_reductase, forced_burden,
                                    floor_override=forced_reductase)
        units = units * kill
        frac = units / INOCULUM
        hist.append((sol, frac, 1.0 - frac, kill))
    return hist


def lattice_integrity(t_years, dust_tau=LATTICE_DUST_TAU_YEARS,
                      loss_per_cycle=LATTICE_LOSS_PER_CYCLE):
    cycle_term = math.exp(-loss_per_cycle * LATTICE_CYCLES_PER_EARTH_YEAR * t_years)
    dust_term = math.exp(-t_years / dust_tau) if dust_tau > 0.0 else 0.0
    return cycle_term * dust_term


def first_crossing(threshold, dust_tau, horizon=LATTICE_HORIZON_YEARS, dt=0.01):
    prev_t, prev_i = 0.0, lattice_integrity(0.0, dust_tau)
    if prev_i <= threshold:
        return 0.0
    t = dt
    while t <= horizon + 1e-12:
        i = lattice_integrity(t, dust_tau)
        if i <= threshold:
            # linear interpolate
            frac = (prev_i - threshold) / (prev_i - i) if prev_i != i else 1.0
            return prev_t + frac * (t - prev_t)
        prev_t, prev_i = t, i
        t += dt
    # extrapolate closed form if not yet crossed
    # I = exp(-a t) * exp(-t/tau) = exp(-t (a+1/tau))
    a = loss_per_cycle_year = LATTICE_LOSS_PER_CYCLE * LATTICE_CYCLES_PER_EARTH_YEAR
    k = a + 1.0 / dust_tau
    if k <= 0.0:
        return None
    t_cross = -math.log(threshold) / k
    return t_cross


def run_lattice_horizon():
    a = LATTICE_LOSS_PER_CYCLE * LATTICE_CYCLES_PER_EARTH_YEAR
    print("Lattice long-horizon (Earth years). Rates are unvalidated assumptions.")
    print(f"  diurnal cycles/Earth year: {LATTICE_CYCLES_PER_EARTH_YEAR:.2f}")
    print(f"  loss per cycle: {LATTICE_LOSS_PER_CYCLE:.1e}  -> {100*a:.3f}%/Earth year from dock/magnet fatigue")
    print(f"  dust/static tau: {LATTICE_DUST_TAU_YEARS:.1f} Earth years")
    print(f"  cascade unlock threshold: {CASCADE_UNLOCK_INTEGRITY:.2f}")
    print(f"  lattice tear threshold:    {LATTICE_TEAR_INTEGRITY:.2f}")
    print(f"  {'year':6s} {'integrity':10s}")
    t = 0.0
    while t <= LATTICE_HORIZON_YEARS + 1e-12:
        print(f"  {t:6.1f} {lattice_integrity(t):10.4f}")
        t += 1.0
    unlock = first_crossing(CASCADE_UNLOCK_INTEGRITY, LATTICE_DUST_TAU_YEARS)
    tear = first_crossing(LATTICE_TEAR_INTEGRITY, LATTICE_DUST_TAU_YEARS)
    print(f"  Nominal (tau={LATTICE_DUST_TAU_YEARS:.0f} yr): cascade unlock at {unlock:.2f} Earth years, "
          f"tear at {tear:.2f} Earth years")
    # sensitivity, clearly not a fit
    for tau in (8.0, 12.0, 20.0, 30.0):
        u = first_crossing(CASCADE_UNLOCK_INTEGRITY, tau)
        tr = first_crossing(LATTICE_TEAR_INTEGRITY, tau)
        in_window = (tr is not None and 8.0 <= tr <= 12.0)
        print(f"  Sensitivity tau={tau:.0f} yr: unlock={u:.2f}, tear={tr:.2f}  "
              f"{'(tear inside 8-12 yr window)' if in_window else '(tear not in 8-12 yr window)'}")
    return unlock, tear


def nutrient_volume_table():
    """Unconstrained (v2.1-style) geo-mean exhaustion times for several volumes."""
    growth = 2 ** (1.0 / DOUBLING_SOLS)
    _, geo_s = clamped_s_stats(SURVIVAL_CENTER, SURVIVAL_CAP, SURVIVAL_FLOOR,
                               SURVIVAL_SPREAD)
    n_per = unit_n_kg()
    p_per = unit_p_kg()
    print("Nutrient exhaustion under unconstrained geo-mean growth (diagnostic,")
    print("not a fit to 200 sols). N is limiting at these mass fractions.")
    print(f"  geo_s={geo_s:.6f}  N/unit={n_per:.3f} kg  P/unit={p_per:.3f} kg")
    volumes = [
        ("default 1000x1000 km x 1 m", 1.0e12),
        ("100x100 km x 1 m", 1.0e10),
        ("global 1 m (1.44e8 km^2)", 1.44e8 * 1.0e6),
        ("global 10 m", 1.44e9 * 1.0e6),
    ]
    # sols for N exhaustion: inoc*(net^t - 1)*n_per = n_pool
    def t_ex(net, n_pool):
        if net <= 1.0:
            return float("inf")
        rhs = 1.0 + n_pool / (INOCULUM * n_per)
        return math.log(rhs) / math.log(net)

    nets = {}
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            nets[(tier, p)] = (geo_s * ox_factor(tier, p)
                               * reductase_survival(p) * growth)
    print(f"  {'volume':28s} {'N_pool_kg':11s} {'base 0.50':>10s} {'sev 1.50':>10s}")
    density = REGOLITH_DENSITY_KG_M3
    for name, vol in volumes:
        n_pool = vol * density * (N_REGOLITH_PCT / 100.0)
        t0 = t_ex(nets[("baseline", 0.50)], n_pool)
        t1 = t_ex(nets[("severe", 1.50)], n_pool)
        print(f"  {name:28s} {n_pool:11.3e} {t0:10.2f} {t1:10.2f}")
    # volume that would exhaust at 200 sols at baseline 0.50
    net = nets[("baseline", 0.50)]
    n_pool_200 = INOCULUM * n_per * (net ** 200 - 1.0)
    vol_200 = n_pool_200 / ((N_REGOLITH_PCT / 100.0) * density)
    area_1m_km2 = vol_200 / 1.0e6
    depth_global = vol_200 / (1.44e8 * 1.0e6)
    print(f"  Volume that would exhaust at 200 sols (baseline 0.50, geo_net={net:.6f}):")
    print(f"    N_pool={n_pool_200:.4e} kg, volume={vol_200:.4e} m3,")
    print(f"    {area_1m_km2:.4e} km2 at 1 m depth, or {depth_global:.1f} m if global "
          f"(Mars area 1.44e8 km2).")


def mars_atmospheric_n_kg():
    """Rough Mars atmospheric N inventory. 2.7% N2 by volume (brief);
    610 Pa, g=3.71 m/s^2, R=3389.5 km. Not a high-precision climate value.
    """
    area = 4.0 * math.pi * (3389.5e3) ** 2
    column = 610.0 / 3.71
    atm_mass = area * column
    # mole fractions, then mass: N2 2.7%, CO2 95.3%, Ar 1.6%
    xn2, xco2, xar = 0.027, 0.953, 0.016
    s = xn2 + xco2 + xar
    xn2, xco2, xar = xn2 / s, xco2 / s, xar / s
    mu = xn2 * 28.0 + xco2 * 44.0 + xar * 39.9
    n2_mass_frac = (xn2 * 28.0) / mu
    return atm_mass, n2_mass_frac, atm_mass * n2_mass_frac




def freeze_o2_kg():
    """O2 (kg) at which co2_t would sit exactly on FREEZE_CO2_T."""
    return (CO2_START_T - FREEZE_CO2_T) * 1000.0 / CO2_PER_KG_O2


def rover_p_reference_kg(elem_p_wt_frac=0.0015):
    """P mass in the default working volume and in a global 1 m rind.

    elem_p_wt_frac default 0.0015 is ~0.15% elemental P, i.e. ~0.34 wt%
    P2O5 — a mid-range figure in the approximate published APXS soil
    window (~0.3-1.0 wt% P2O5).
    """
    mass = ACCESSIBLE_REGOLITH_M3 * REGOLITH_DENSITY_KG_M3
    working = mass * elem_p_wt_frac
    # Mars surface area ~1.44e8 km2
    global_1m = 1.44e8 * 1.0e6 * REGOLITH_DENSITY_KG_M3 * elem_p_wt_frac
    return working, global_1m




def run_cell(tier, perch, **kw):
    """240 paired-seed runs for one cell. Returns a stats dict."""
    master = random.Random(SEED)
    seeds = [master.getrandbits(64) for _ in range(N_RUNS)]
    rs = [run_once(random.Random(sd), perch, tier, **kw) for sd in seeds]
    clears = sorted(r["sol"] for r in rs if r["ok"])
    outcomes = Counter(r["outcome"] for r in rs)
    ges = [r["growth_end"] for r in rs if r["growth_end"] is not None]
    reasons = Counter(r["growth_reason"] for r in rs
                      if r["growth_end"] is not None)
    n_draws = sum(r["n_draws"] for r in rs)
    o2_clear = [r["o2"] for r in rs if r["ok"]]
    rate = len(clears) / N_RUNS
    st = {
        "tier": tier, "perch": perch, "runs": rs,
        "clears": len(clears), "rate": rate, "gate": GATE[tier],
        "passed": rate >= GATE[tier],
        "clear_min": clears[0] if clears else None,
        "clear_med": clears[len(clears) // 2] if clears else None,
        "clear_mean": (sum(clears) / len(clears)) if clears else None,
        "clear_max": clears[-1] if clears else None,
        "outcomes": outcomes,
        "mean_draw": sum(r["sum_draw"] for r in rs) / n_draws,
        "mean_eff": sum(r["sum_eff"] for r in rs) / n_draws,
        "worst_draw": min(r["min_draw"] for r in rs),
        "worst_eff": min(r["min_eff"] for r in rs),
        "mean_last_s": sum(r["last_s"] for r in rs) / N_RUNS,
        "mean_o2": sum(r["o2"] for r in rs) / N_RUNS,
        "mean_o2_clear": (sum(o2_clear) / len(o2_clear)) if o2_clear else 0.0,
        "max_o2": max(r["o2"] for r in rs),
        "freeze_cross": sum(1 for r in rs if r["crossed_freeze"]),
        "freeze_cross_on_clear": sum(1 for r in rs
                                     if r["crossed_freeze"] and r["ok"]),
        "throttled_runs": sum(1 for r in rs if r["throttled_sols"] > 0),
        "shed_mean": sum(r["shed_total"] for r in rs) / N_RUNS,
        "ge_n": len(ges),
        "ge_min": min(ges) if ges else None,
        "ge_max": max(ges) if ges else None,
        "ge_mean": (sum(ges) / len(ges)) if ges else None,
        "reasons": reasons,
        "growing_at_clear": sum(1 for r in rs if r["ok"]
                                and (r["growth_end"] is None
                                     or r["growth_end"] > r["sol"])),
        "scav_mean": sum(r["scav_total"] for r in rs) / N_RUNS,
        "m_left_mean": sum((r["m_rem"] / r["m0"]) if r["m0"] > 0 else 0.0
                           for r in rs) / N_RUNS,
        "mean_sols": sum(r["sol"] for r in rs) / N_RUNS,
        "chlorite": sum(r["chlorite_hits"] for r in rs),
        # v2.7 adaptive-center diagnostics (per-sol, pooled over runs)
        "center_mean": sum(r["sum_center"] for r in rs) / n_draws,
        "center_min": min(r["min_center"] for r in rs),
        "center_max": max(r["max_center"] for r in rs),
        "frac_at_max": sum(r["at_max_sols"] for r in rs) / n_draws,
        "frac_capped": sum(r["capped_draws"] for r in rs) / n_draws,
        "frac_below_target": sum(r["below_target_sols"] for r in rs) / n_draws,
        "cold_mean": sum(r["sum_cold"] for r in rs) / n_draws,
        "net_realised": math.exp((sum(r["sum_log_eff"] for r in rs)
                                  + sum(r["sum_log_growth"] for r in rs)) / n_draws),
        "n_draws": n_draws,
    }
    pk = sorted(r["peak_units"] for r in rs)
    st["peak_med"] = pk[len(pk) // 2]
    st["peak_max"] = pk[-1]
    h = [0] * (DRAW_HIST_BINS + 1)
    for r in rs:
        for i, v in enumerate(r["hist"]):
            if v:
                h[i] += v
    tot = sum(h)

    def q(f):
        acc, tgt = 0, f * tot
        for i, v in enumerate(h):
            acc += v
            if acc >= tgt:
                return (i + 0.5) / DRAW_HIST_BINS
        return 1.0
    st["draw_p5"], st["draw_med"], st["draw_p95"] = q(0.05), q(0.50), q(0.95)
    knee_bin = int(SURVIVAL_SOFT_KNEE * DRAW_HIST_BINS)
    st["draw_above_knee"] = sum(h[knee_bin:]) / tot if tot else 0.0
    for r in rs:
        r["hist"] = None
    return st


def run_ensemble(label, **kw):
    cells = {}
    for tier in STRESS_TIERS:
        for perch in PERCH_LEVELS:
            cells[(tier, perch)] = run_cell(tier, perch, **kw)
    return cells


def _fmt(v, f="{}"):
    return "-" if v is None else f.format(v)


def _reasons(c):
    return ",".join(f"{k}:{v}" for k, v in sorted(c.items())) or "none"


def print_gate_grid(title, cells):
    print(title)
    hdr = f"  {'tier':9s} {'gate':>5s}" + "".join(
        f"  {('%.2f%%' % p) + (' *' if p not in BRIEF_PERCH_LEVELS else ''):>16s}"
        for p in PERCH_LEVELS)
    print(hdr)
    for tier in STRESS_TIERS:
        row = f"  {tier:9s} {GATE[tier]*100:4.0f}%"
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            row += f"  {c['clears']:3d}/{N_RUNS} {'PASS' if c['passed'] else 'FAIL':>4s}{'':5s}"
        print(row)
    brief_pass = sum(1 for (t, p), c in cells.items()
                     if p in BRIEF_PERCH_LEVELS and c["passed"])
    col15 = sum(1 for (t, p), c in cells.items()
                if p not in BRIEF_PERCH_LEVELS and c["passed"])
    allp = sum(1 for c in cells.values() if c["passed"])
    print(f"  * 1.50% column kept from v2.2-v2.4 (not in the v2.5 brief list).")
    print(f"  Brief 9 cells (0.50/0.75/1.00%): {brief_pass}/9 pass.  "
          f"1.50% column: {col15}/3 pass.  All 12: {allp}/12 pass.  "
          f"ALL GATES {'PASS' if allp == 12 else 'FAIL'}")


def print_cell_detail(title, cells):
    print(title)
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            oc = c["outcomes"]
            print(f"  {tier:9s} perch={p:.2f}%: clears {c['clears']}/{N_RUNS} "
                  f"({100*c['rate']:.1f}%) gate {100*c['gate']:.0f}% "
                  f"{'PASS' if c['passed'] else 'FAIL'}  "
                  f"clear_sol min/med/mean/max="
                  f"{_fmt(c['clear_min'])}/{_fmt(c['clear_med'])}/"
                  f"{_fmt(c['clear_mean'], '{:.1f}')}/{_fmt(c['clear_max'])}")
            print(f"      outcomes: clear={oc.get('clear',0)} "
                  f"freeze={oc.get('freeze',0)} extinct={oc.get('extinct',0)} "
                  f"timeout={oc.get('timeout',0)}  mean run length "
                  f"{c['mean_sols']:.1f} sols")
            print(f"      survival: mean_draw={c['mean_draw']:.4f} "
                  f"worst_draw={c['worst_draw']:.4f}  "
                  f"mean_eff={c['mean_eff']:.4f} worst_eff={c['worst_eff']:.4f}  "
                  f"mean_last_s(v2.4-style)={c['mean_last_s']:.4f}")
            print(f"      O2: mean_final={c['mean_o2']:.4e} "
                  f"mean_at_clear={c['mean_o2_clear']:.4e} "
                  f"max={c['max_o2']:.4e} kg  freeze_crossings={c['freeze_cross']} "
                  f"(on clears {c['freeze_cross_on_clear']})  "
                  f"throttled_runs={c['throttled_runs']} "
                  f"mean_shed={c['shed_mean']:.3e} kg")
            print(f"      growth_end n={c['ge_n']} min={_fmt(c['ge_min'])} "
                  f"max={_fmt(c['ge_max'])} "
                  f"mean={_fmt(c['ge_mean'], '{:.1f}')} "
                  f"limit={_reasons(c['reasons'])} "
                  f"growing_at_clear={c['growing_at_clear']}  "
                  f"P scavenged mean={c['scav_mean']:.3e} kg  "
                  f"mineral P left mean={100*c['m_left_mean']:.1f}%")


def print_summary_table(title, cells):
    print(title)
    print(f"  {'cell':17s} {'clears':>7s} {'gate':>4s} {'P/F':>4s} "
          f"{'mean_s':>7s} {'worst_s':>7s} {'mean_O2_kg':>10s} "
          f"{'ge_mean':>7s} {'limit':>12s} {'frz':>4s} {'ext':>4s} "
          f"{'clr_med':>7s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            lim = _reasons(c["reasons"])
            print(f"  {tier:9s} {p:5.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['clears']:3d}/{N_RUNS} {100*c['gate']:3.0f}% "
                  f"{'PASS' if c['passed'] else 'FAIL':>4s} "
                  f"{c['mean_draw']:7.4f} {c['worst_draw']:7.4f} "
                  f"{c['mean_o2']:10.3e} {_fmt(c['ge_mean'], '{:.1f}'):>7s} "
                  f"{lim:>12s} {c['freeze_cross']:4d} "
                  f"{c['outcomes'].get('extinct',0):4d} "
                  f"{_fmt(c['clear_med']):>7s}")


def run_horizon(tier, perch, **kw):
    master = random.Random(SEED)
    seeds = [master.getrandbits(64) for _ in range(N_RUNS)]
    still = 0
    ends = []
    reasons = Counter()
    for sd in seeds:
        r = run_once(random.Random(sd), perch, tier, stop_on_targets=False,
                     max_sols=200, **kw)
        if r["growth_end"] is None:
            still += 1
        else:
            ends.append(r["growth_end"])
            reasons[r["growth_reason"]] += 1
    return still, ends, reasons


def net_table(doubling, label):
    growth = 2 ** (1.0 / doubling)
    print(f"  Geo-mean net growth per sol ({label}, D={doubling}, growth "
          f"{growth:.6f}; '<' = below 1, population shrinks):")
    print("    " + f"{'tier':9s}" + "".join(f"  {p:>8.2f}%" for p in PERCH_LEVELS))
    for tier in STRESS_TIERS:
        row = f"    {tier:9s}"
        for p in PERCH_LEVELS:
            net = geo_s_eff(p, tier, doubling) * cell_growth(tier_cold(tier), doubling)
            row += f"  {net:8.5f}{'<' if net < 1.0 - 1e-9 else ' '}"
        print(row)


def compact_rows(cells, doubling):
    growth = 2 ** (1.0 / doubling)
    print(f"  {'cell':17s} {'clears':>7s} {'gate':>4s} {'P/F':>4s} "
          f"{'net/sol':>8s} {'center':>6s} {'mean_eff':>8s} {'worst_s':>7s} "
          f"{'clr_med':>7s} {'ext':>4s} {'frz':>4s} {'chl':>4s} "
          f"{'scav_kg':>9s} {'min_left':>8s} {'limit':>9s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            net = geo_s_eff(p, tier) * growth
            print(f"  {tier:9s} {p:5.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['clears']:3d}/{N_RUNS} {100*c['gate']:3.0f}% "
                  f"{'PASS' if c['passed'] else 'FAIL':>4s} {net:8.5f} "
                  f"{survival_center_for(tier, p):6.3f} {c['mean_eff']:8.4f} "
                  f"{c['worst_draw']:7.4f} {_fmt(c['clear_med']):>7s} "
                  f"{c['outcomes'].get('extinct', 0):4d} {c['freeze_cross']:4d} "
                  f"{c['chlorite']:4d} {c['scav_mean']:9.3e} "
                  f"{100*c['m_left_mean']:7.1f}% {_reasons(c['reasons']):>9s}")


class with_globals:
    """Temporarily set module constants (restored on exit)."""
    def __init__(self, **kw):
        self.kw = kw
        self.saved = {}

    def __enter__(self):
        g = globals()
        for k, v in self.kw.items():
            self.saved[k] = g[k]
            g[k] = v
        return self

    def __exit__(self, *a):
        globals().update(self.saved)
        return False


def rows_v27(cells, doubling):
    print(f"  {'cell':15s} {'clears':>7s} {'P/F':>4s} {'expnet':>7s} "
          f"{'realnet':>7s} {'c_mean':>6s} {'c_min':>6s} {'c_max':>6s} "
          f"{'@max':>5s} {'capped':>6s} {'clr_med':>7s} {'ext':>3s} "
          f"{'frz':>3s} {'chl':>3s} {'scav_kg':>9s} {'m_left':>6s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            en = geo_s_eff(p, tier, doubling) * cell_growth(tier_cold(tier), doubling)
            print(f"  {tier:8s} {p:4.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['clears']:3d}/{N_RUNS} {'PASS' if c['passed'] else 'FAIL':>4s} "
                  f"{en:7.5f} {c['net_realised']:7.5f} {c['center_mean']:6.4f} "
                  f"{c['center_min']:6.4f} {c['center_max']:6.4f} "
                  f"{100*c['frac_at_max']:4.0f}% {100*c['frac_capped']:5.1f}% "
                  f"{_fmt(c['clear_med']):>7s} {c['outcomes'].get('extinct', 0):3d} "
                  f"{c['freeze_cross']:3d} {c['chlorite']:3d} {c['scav_mean']:9.3e} "
                  f"{100*c['m_left_mean']:5.1f}%")


def grid_line(label, cells):
    allp = sum(1 for c in cells.values() if c["passed"])
    s = " ".join(f"{c['clears']:3d}" for c in cells.values())
    return f"  {label:34s} {allp:2d}/12 pass | clears (b.5 b.75 b1 b1.5 m.. s..): {s}"


def center_map_table(doubling, title):
    print(title)
    colds = (0.25, 0.50, 0.75, 0.95, 1.00)
    print("    cell            " + "".join(f"  cold {c:4.2f}" for c in colds))
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            row = f"    {tier:8s} {p:4.2f}%  "
            for cold in colds:
                cen, net, hit = adaptive_center(tier, p, cold, doubling)
                row += f"  {cen:6.4f}{'^' if hit else ' '}  "
            print(row)
    print("    ^ = hit ADAPTIVE_CENTER_MAX (expected net still < target)")


def rows_v29(cells, doubling):
    print(f"  {'cell':15s} {'clears':>7s} {'P/F':>4s} {'expnet':>7s} {'realnet':>7s} "
          f"{'center':>6s} {'@max':>4s} {'clr_med':>7s} {'ext':>3s} {'tmo':>3s} "
          f"{'peak_med':>9s} {'peak_max':>9s} {'scav_kg':>9s} {'m_left':>6s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            en = geo_s_eff(p, tier, doubling) * cell_growth(tier_cold(tier), doubling)
            print(f"  {tier:8s} {p:4.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['clears']:3d}/{N_RUNS} {'PASS' if c['passed'] else 'FAIL':>4s} "
                  f"{en:7.5f} {c['net_realised']:7.5f} {c['center_mean']:6.4f} "
                  f"{100*c['frac_at_max']:3.0f}% {_fmt(c['clear_med']):>7s} "
                  f"{c['outcomes'].get('extinct', 0):3d} {c['outcomes'].get('timeout', 0):3d} "
                  f"{c['peak_med']:9.3e} {c['peak_max']:9.3e} {c['scav_mean']:9.3e} "
                  f"{100*c['m_left_mean']:5.1f}%")


def draw_rows(cells):
    print(f"  {'cell':15s} {'mean':>6s} {'median':>6s} {'p5':>6s} {'p95':>6s} "
          f"{'min':>6s} {'>0.98':>6s} {'draws':>9s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            print(f"  {tier:8s} {p:4.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['mean_draw']:6.4f} {c['draw_med']:6.4f} {c['draw_p5']:6.4f} "
                  f"{c['draw_p95']:6.4f} {c['worst_draw']:6.4f} "
                  f"{100*c['draw_above_knee']:5.1f}% {c['n_draws']:9d}")


def solved_d(rate):
    d = solve_doubling_sols(200, scav_rate=rate)
    return d, math.ceil(d * 100.0 - 1e-9) / 100.0


TRAJ_VOLUME_MULTIPLIER = 10.0
TRAJ_CONTINUOUS_P_KG_PER_SOL = 1.0e25
TRAJ_SOLS = (0, 50, 100, 200, 500)
TRAJ_HORIZON = 1000


def trajectory_diag(tier, perch, label, p_import=None, vol_mult=1.0):
    with with_globals(ACCESSIBLE_REGOLITH_M3=ACCESSIBLE_REGOLITH_M3 * vol_mult):
        master = random.Random(SEED)
        seeds = [master.getrandbits(64) for _ in range(N_RUNS)]
        trajs, ges, rsn = [], [], []
        for sd in seeds:
            r = run_once(random.Random(sd), perch, tier, stop_on_targets=False,
                         max_sols=TRAJ_HORIZON, p_import=p_import, record_traj=True)
            trajs.append([INOCULUM] + [t[1] for t in r["traj"]])
            ges.append(r["growth_end"])
            rsn.append(r["growth_reason"])
        cell = run_cell(tier, perch, p_import=p_import)
        mp0 = mineral_p0_kg()
    med = []
    for i in range(TRAJ_HORIZON + 1):
        col = sorted(t[i] for t in trajs)
        med.append(col[len(col) // 2])
    pk = max(range(len(med)), key=lambda i: med[i])
    clipped = sorted(g for g in ges if g is not None)
    rc = Counter(x for x in rsn if x is not None)
    ge_txt = (f"median {clipped[len(clipped)//2]} ({len(clipped)}/{N_RUNS} clipped, limit {_reasons(rc)})"
              if clipped else f"never (0/{N_RUNS} clipped in {TRAJ_HORIZON} sols)")
    pts = "  ".join(f"sol {t}: {med[t]:.3e}" for t in TRAJ_SOLS)
    print(f"  {tier} {perch:.2f}% [{label}] mineral P {mp0:.3e} kg")
    print(f"    median cells  {pts}")
    print(f"    peak {med[pk]:.3e} at sol {pk}; growth stops {ge_txt}; clears "
          f"{cell['clears']}/{N_RUNS}, median clear sol {_fmt(cell['clear_med'])}, "
          f"extinct {cell['outcomes'].get('extinct', 0)}")


def run_config(label, scav, doubling, override):
    with with_globals(SCAV_KG_P_PER_KG_DRY_PER_SOL=scav, DOUBLING_SOLS=doubling,
                      OX_PERCELL_OVERRIDE_ENABLED=override):
        cells = run_ensemble(label)
        print(f"=== {label}: scav {scav:.0e}, D {doubling:.2f}, moderate 1.50% ox "
              f"{ox_factor('moderate', 1.50)} ===")
        print_gate_grid(f"{label} gate grid:", cells)
        rows_v29(cells, doubling)
        m0 = mineral_p0_kg()
        print(f"  mineral P inventory {m0:.4e} kg; mineral P USED per cell (mean):")
        for k, c in cells.items():
            print(f"    {k[0]:8s} {k[1]:4.2f}%: used {100*(1-c['m_left_mean']):5.1f}% "
                  f"({(1-c['m_left_mean'])*m0:.3e} kg), scavenged {c['scav_mean']:.3e} kg, "
                  f"timeouts {c['outcomes'].get('timeout', 0)}")
        print(f"  freeze crossings {sum(c['freeze_cross'] for c in cells.values())}/"
              f"{12*N_RUNS}; throttled runs {sum(c['throttled_runs'] for c in cells.values())}; "
              f"chlorite hits {sum(c['chlorite'] for c in cells.values())}")
        print()
    return cells


# ---------------------------------------------------------------------------
# Inlined v2.9 reference (standalone consolidation). Verbatim copy of
# mars_bacteria_swarm_sim_v29.py up to (not including) its main(). Run in its
# own namespace so v2.9 constants (OXIDATIVE_FACTOR moderate 0.97, scav 1e-3,
# D 8.82, no per-cell override) and caches are independent of v2.10's.
# ---------------------------------------------------------------------------
_V29_REFERENCE_SOURCE = r'''#!/usr/bin/env python3
"""DB-MARS-CONV-006 v2.9 traceable Monte Carlo sim.

v2.9 updates (2026-11-23) — thermal habitat model on v2.8:
1. HABITAT_ENABLED with HABITAT_MODE per tier:
     baseline "ambient"           (cold 1.0 = 25 C already, unchanged)
     moderate "insulated"         insulated shell, interior 25 C
     severe   "insulated_heated"  insulation + supplemental heat, 25 C
   Inside a habitat the effective cold factor is the interior temperature
   mapped back through the v2.8 linear map (0 C -> 0, 25 C -> 1), so
   HABITAT_INTERIOR_C 25 gives cold 1.0: the grounded Arrhenius growth
   rate (Ea 67.99 kJ/mol) is fully restored (r = 1). The two habitat
   modes are thermally identical in the sim; the label records HOW the
   25 C is held. No energy budget, no heater failure, no thermal mass:
   the interior is an ASSUMED constant 25 C.
2. HABITAT_RESTORES_PROTEOME (default True). In v1.8-v2.8 the cold
   factor also scales the burden-sensor throttle in proteome_levels.
   Physically the interior cold factor is 1.0, so by default the
   proteome also sees 1.0. NOTE this is not "baseline-equivalent":
   at stress 1.5/2.0 with cold 1.0 the sensor throttles fully and the
   reductase drops to the 60% hard floor (0.75 at ambient cold), which
   lowers O2 output per unit. False keeps the ambient proteome
   (reductase 0.75) and only restores the growth rate; both reported.
3. NOT thermal, unchanged: oxidative factor (moderate 0.97 — a v2.0
   setting left untouched — severe 0.99), perchlorate Hill factor,
   survival draw shoulder, adaptive center, nutrients, freeze gate.
4. HABITAT_ENABLED False reproduces v2.8 run-for-run (checked in main).
5. New diagnostics: per-run peak population; per-cell survival draw
   distribution (mean, median, p5, p95, min, fraction above the 0.98
   knee) from a 0.001-wide histogram of every per-sol draw.

v2.8 updates (2026-11-23) — two fixes on v2.7, everything else held:
1. Survival draw cap. SURVIVAL_CAP_MODE:
     "soft" (DEFAULT) — a smooth shoulder that only engages above
        SURVIVAL_SOFT_KNEE (0.98): y = x for x <= knee, else
        y = knee + (1-knee) tanh((x-knee)/(1-knee)). Continuous with
        slope 1 at the knee; approaches but never exceeds 1.0 (a
        survival fraction cannot exceed 1). No artificial 0.97 ceiling.
     "none" — only the physical limit: hard clamp at 1.0.
     "hard097" — legacy v2.1-v2.7 clamp at SURVIVAL_CAP 0.97 (control).
   The 0.10 floor is unchanged. ADAPTIVE_CENTER_MAX stays 0.99; with no
   0.97 cap a 0.99 center gives an expected draw of ~0.977 (soft).
2. Cold penalty grounded in Deinococcus radiodurans data. COLD_MODEL:
     "arrhenius_growth" (DEFAULT) — cold slows the replication RATE:
        growth per sol = 2^(r(cold)/D), r = Arrhenius rate ratio vs 25 C.
     "arrhenius_survival" — same r applied to per-sol survival (the
        v2.7 placement), comparison only.
     "linear_fitted" — legacy v2.7 f_cold = 1 - 0.036636 (1 - cold).
   Grounding (Symeonidou et al. 2024, Extremophiles,
   doi 10.1007/s00792-024-01351-5, PMC11266278, Table 2): D.
   radiodurans control-culture CO2 production 812.63 ug/day at 25 C vs
   66.03 ug/day at 0 C, ratio 12.31. Two-point Arrhenius gives
   Ea = R ln(12.31) / (1/273.15 - 1/298.15) = 68.0 kJ/mol, Q10 = 2.73
   over 0-25 C. Cross-check: Price & Sowers 2004 PNAS 101:4631 report
   ~110 kJ for microbial community growth/maintenance/survival.
   MAPPING (an ASSUMPTION, stated plainly): the dimensionless cold
   factor maps LINEARLY onto the study's two temperatures,
   T = 0 C + cold x 25 C, so cold 1.0 = 25 C (rate 1), cold 0.0 = 0 C
   (rate 1/12.31). Tier values: baseline 1.0 = 25 C, moderate 0.5 =
   12.5 C, severe 0.25 = 6.25 C, cold 0.95 = 23.75 C.
   Placement: the measurement is a metabolic RATE, and the same study
   reports longer survival / higher CFU at 0 C than 25 C in most
   treatments, so the slowdown is applied to growth, not to survival.
   Mortality is NOT slowed by cold (conservative; noted as a caveat).
3. Scored scavenging rate 1e-3 (user brief); D re-solved under the soft
   cap at each rate (baseline cold 1.0 -> r = 1, so the cold model does
   not enter the solve, but the cap change does).
4. Control: SURVIVAL_CAP_MODE "hard097" + COLD_MODEL "linear_fitted" at
   rate 2e-3 / D 8.05 reproduces v2.7 E1 run-for-run (checked in main).

v2.7 updates (2026-11-23) — adaptive per-sol survival center on v2.6:
1. ADAPTIVE_SURVIVAL (default True) replaces the static survival center.
   Every sol the run READS the cold suppression factor, then sets the
   lognormal center to the value whose EXPECTED clamped draw (geo-mean
   of min(SURVIVAL_CAP, max(SURVIVAL_FLOOR, LN(log c, SPREAD)))) makes
   expected net growth = ADAPTIVE_NET_TARGET (1.0), given that sol's
   cold factor, oxidative factor, perchlorate Hill factor, burden
   penalty, chlorite factor and 2^(1/D). The solved center is clipped
   to [lower, ADAPTIVE_CENTER_MAX]; lower = max(ADAPTIVE_CENTER_MIN,
   the v2.6 static per-cell center), so a cell that already nets >= 1
   "relaxes" back to exactly its v2.6 center. The per-sol draw is then
   taken exactly as in v2.6 and still clamped at SURVIVAL_CAP 0.97.
   ADAPTIVE_CENTER_MAX 0.99 sits ABOVE the cap: raising the center past
   0.97 only pushes more draws into the cap, so the reachable expected
   draw tops out near 0.959 (center 0.99). Cells that need more than
   that stay below net 1 and are reported, not forced.
   HONESTY NOTE: a center solved to hold net >= 1 makes survival pass
   by construction wherever it is reachable. It is a controller
   target, not a measured or modelled biology.
2. Cold coupling (NEW, an assumption, documented). In v2.6 the cold
   suppression factor does NOT enter the net-growth product; it only
   scales the burden-sensor throttle inside proteome_levels (reductase
   level). With no coupling the adaptive center would ignore cold
   entirely. To make "read cold, set the center" meaningful, v2.7 adds
   a linear cold net factor applied to per-sol survival:
       f_cold = 1 - COLD_NET_COUPLING * (1 - cold)
   COLD_NET_COUPLING is CALIBRATED (not measured) so that cold 0.25 at
   severe 0.50% (the mildest severe cell, D 8.05) needs center exactly
   COLD_CALIBRATION_CENTER = 0.98. Cold 1.0 gives f_cold = 1 (baseline
   untouched); cold 0.95 gives f_cold ~0.998 and the center relaxes.
   The coupling is a NEW penalty that v2.6 did not have; a variant with
   COLD_NET_COUPLING = 0 (pure v2.6 physics + controller) is reported
   alongside the scored run.
3. Cold read per sol: cold = tier value x exp(COLD_VARIATION_SPREAD x
   N(0,1)) clipped to [COLD_MIN, COLD_MAX], quantised to
   COLD_READ_RESOLUTION. Default spread 0 -> cold is constant per tier
   and results are reproducible; a spread>0 sensitivity draws cold from
   a SEPARATE per-run RNG so survival draws stay paired with v2.6. The
   per-sol cold value drives f_cold and the center only; proteome
   levels (reductase 0.75 at moderate/severe) stay tier-static as v2.6.
4. ADAPTIVE_SURVIVAL=False with COLD_NET_COUPLING=0 reproduces v2.6
   run-for-run (checked in main against the v2.6 module).
5. All other v2.6 levers kept unchanged.


v2.6 updates (2026-11-23) — nutrient-growth coupling overhaul on v2.5:
1. Scavenging rate cranked and made a swept lever: SCAV_RATE_OPTIONS =
   (5e-4, 1e-3, 2e-3) kg P / kg dry / sol. Default
   SCAV_KG_P_PER_KG_DRY_PER_SOL = 2e-3, the TOP of the v2.5 Mars-plausible
   range (~1e-4 to 2e-3). Every option gets its own solved doubling time
   and its own full 12-cell ensemble.
2. Doubling time re-solved toward v2.4's 5.8 sols with scavenging
   carrying P, SAME criterion as v2.5 (geo-mean baseline 0.50% growth
   unclipped >200 sols on rover-grade soil, P import 0). The solve
   cannot reach 5.8: the binding limit is the total rover-grade P
   inventory in the working volume, not the conversion rate. D=5.8 is
   run as a labelled, UNSCORED sensitivity case.
3. Per-cell survival-center override: SURVIVAL_CENTER_SEVERE_1PCT = 0.96
   applies to the severe 1.00% cell only (all other cells keep
   SURVIVAL_CENTER 0.95). Draws still clamp at SURVIVAL_CAP 0.97.
4. Kept: CO2 hard gate with throttle (default) / vent / off; 60% hard
   reductase floor; 18% chlorite burden spike; RECYCLE_FRACTION 0.8;
   N_IMPORT_KG_PER_SOL 7.251e13 (v2.5 value, held — NOT zero);
   P_IMPORT_KG_PER_SOL 0 with P_IMPORT_REALISTIC_MAX_KG_PER_SOL
   (8.47e7) as the fallback-only lever.


v2.5 updates (2026-11-23) — four fixes, all named constants below:
1. CO2 freeze is a HARD GATE from sol 1 (FREEZE_HARD_GATE). Every sol
   the CO2 inventory is tested BEFORE the O2 target; a run whose CO2
   drops below FREEZE_CO2_T on any sol is a failure whatever its O2
   total. The v2.4 O2-first order is kept only as a labelled
   comparison mode (run_once(..., o2_first=True)), never as default.
   Freeze control (FREEZE_CONTROL_MODE):
     "throttle" (DEFAULT) — the swarm down-regulates O2 output so the
        cumulative O2 never exceeds O2_CEILING_KG = freeze-equivalent
        O2 x (1 - FREEZE_MARGIN_FRAC). The ceiling sits above the O2
        target, so a throttled run can still clear.
     "vent" — a thermal vent / non-photochemical quench sheds up to
        VENT_SHED_CAPACITY_KG_O2_PER_SOL of over-ceiling production per
        sol as heat; any excess beyond that capacity still fixes CO2
        and can trip the hard gate. Finite-capacity sensitivity only.
     "off" — no control (used for the ordering comparison).
2. Phosphorus scavenging trait (SCAV_ENABLED, SCAV_KG_P_PER_KG_DRY_PER_SOL).
   Each unit solubilises mineral P (apatite/merrillite) from the
   rover-grade regolith at a specific rate per kg of dry biomass,
   first-order in the mineral P still remaining. The mineral reservoir
   is the rover-grade P in the default working volume
   (REGOLITH_P2O5_WT_PCT) minus the already-labile INITIAL_P_POOL_KG.
   The module costs SCAV_PROTEOME of heterologous proteome.
3. Slower growth: DOUBLING_SOLS is SOLVED (binary search, shown in
   stdout) as the shortest doubling time at which geo-mean growth at
   baseline 0.50% stays unclipped for >200 sols on rover-grade soil
   alone (scavenging on, P import 0, N import and recycle held).
4. P import kept as a fallback lever, default 0. Its realistic upper
   bound P_IMPORT_REALISTIC_MAX_KG_PER_SOL is the ENTIRE present-day
   Earth phosphate-rock industry transposed to Mars (~8.5e7 kg P/sol),
   ~1.2e5x below the v2.4 requirement-sized 9.887e12 kg P/sol.
Other changes required by the fixes (documented):
- The v2.4 "hopeless" shortcut (growth ended and constant production
  cannot reach the target) is no longer a valid bound once scavenged P
  can re-feed growth after a clip, so it is removed. Runs now end by
  clear, freeze, extinction (units < EXTINCTION_UNITS), or MAX_SOLS.
- RNG layout: each cell draws N_RUNS per-run seeds from Random(SEED);
  run i always gets the same per-sol survival draws in every variant,
  so the ordering comparison is paired run-for-run. Per-sol draws are
  therefore not the identical stream v2.4 used.
- Mean survival is now the mean of EVERY per-sol clamped draw (v2.4
  reported the last-sol draw; that column is kept as mean_last_s).
  Worst per-sol draw is the min over every sol of every run.

v2.4 updates (2026-11-23):
- Phosphorus import: named constant P_IMPORT_KG_PER_SOL replenishes
  the environmental P pool each sol. The default, 9.887e12 kg P/sol,
  is SIZED (binary search, not a guess) so that, with N_IMPORT already
  at 7.251e13, the enlarged INITIAL_P_POOL_KG already in place, and
  RECYCLE_FRACTION at 0.8, geo-mean unconstrained growth at baseline
  0.50% lasts at least 200 sols at the default 1.0e12 m3 volume.
  Not a physical flux (~6x a global 1 m rind at 0.15% P over 200 sols).
- Enlarged initial P pool: INITIAL_P_POOL_KG = 1.5e11 (matches the N
  pool mass; 0.01% elemental P = 0.0229 wt% P2O5).
- v2.4 passed 12/12 only because O2 was tested before CO2 freeze:
  265/2,880 clears crossed freeze on the same sol.

v2.3 updates (2026-11-23):
- Atmospheric N import N_IMPORT_KG_PER_SOL = 7.251e13 (requirement-
  sized, not fixation physics) and RECYCLE_FRACTION = 0.8 of dead-unit
  N and P (including chlorite-killed units).

v2.2 updates (2026-11-23):
- Explicit N and P pools in a documented accessible-regolith volume;
  1.5% perchlorate column; hard 60% reductase floor with chlorite
  rapid-kill; parallel lattice thermal-cycling sim (Earth years).

v2.1: survival cap 0.95 -> 0.97; doubling 6.3 -> 5.8 sols.
v2.0: oxidative factor at severe 0.93 -> 0.99; perchlorate LD50 3 -> 10%.
v1.9: survival floor 2% -> 10%; LD50 2 -> 3%; inoculum 1e10 -> 1e12.
v1.8 mechanisms retained: light-repressed toggle, orthogonal
promoters/RBSs, 15% proteome cap, burden sensor with cold suppression,
reductase 60% post-multiplication floor, combined-stress ensemble.

Seed fixed for reproducibility.
Target: 5.25e15 kg O2 (planetary breathable threshold).
"""

import math
import random
from collections import Counter

TARGET_KG = 5.25e15
PER_UNIT_KG = 2.0
INOCULUM = 1e12
# v2.6: re-solved at the v2.6 default scavenging rate (2e-3). v2.5 fix 3: SOLVED, not guessed. Shortest doubling time (rounded UP
# to 0.01 sol) for which geo-mean growth at baseline 0.50% stays
# unclipped for >200 sols on rover-grade soil alone (scavenging on,
# P import 0, N import and recycle held). See solve_doubling_sols()
# and the "v2.5 doubling-time solve" block in stdout.
DOUBLING_SOLS = 8.82   # v2.8: re-solved at rate 1e-3 under the soft cap (v2.7: 8.05 at 2e-3)
V25_DOUBLING_SOLS = 8.50
V24_DOUBLING_SOLS = 5.8
SURVIVAL_CENTER = 0.95
# v2.6 per-cell override: severe tier at 1.00% perchlorate only.
# ASSUMPTION (a design target, not a measured survival): the v2.5 sweep
# put that cell's geo-mean net=1 crossing at 0.95145 (D 8.50).
SURVIVAL_CENTER_SEVERE_1PCT = 0.96
SURVIVAL_SPREAD = 0.05

# --- v2.7 adaptive per-sol survival center ---
ADAPTIVE_SURVIVAL = True
ADAPTIVE_NET_TARGET = 1.0
ADAPTIVE_CENTER_MIN = 0.95   # v2.6 default center
ADAPTIVE_CENTER_MAX = 0.99   # above SURVIVAL_CAP on purpose; cap unchanged
# Lower bound is max(ADAPTIVE_CENTER_MIN, v2.6 static per-cell center).
ADAPTIVE_FLOOR_AT_STATIC = True
# --- v2.7 cold read and cold net coupling (ASSUMPTIONS) ---
COLD_CALIBRATION_CENTER = 0.98
COLD_CALIBRATION_CELL = ("severe", 0.50)
# f_cold = 1 - COLD_NET_COUPLING * (1 - cold). Calibrated value; the
# calibration is recomputed and printed in main() (calibrate_cold_coupling).
COLD_NET_COUPLING = 0.036636   # legacy v2.7 fitted value, "linear_fitted" only
COLD_VARIATION_SPREAD = 0.0
COLD_MIN = 0.05
COLD_MAX = 1.0
COLD_READ_RESOLUTION = 0.001
CO2_START_T = 25e12
CO2_PER_KG_O2 = 2.75
FREEZE_CO2_T = 10e12
MAX_SOLS = 200_000
N_RUNS = 240
SEED = 42

PERCH_LEVELS = [0.50, 0.75, 1.00, 1.50]
# The v2.5 brief lists 0.50/0.75/1.00%; 1.50% is kept from v2.2-v2.4 so
# the ensemble stays 12 cells and comparable. Reported as its own column.
BRIEF_PERCH_LEVELS = [0.50, 0.75, 1.00]
STRESS_TIERS = ["baseline", "moderate", "severe"]
STRESS_FACTOR = {"baseline": 1.0, "moderate": 1.5, "severe": 2.0}
GATE = {"baseline": 0.70, "moderate": 0.60, "severe": 0.50}
SURVIVAL_FLOOR = 0.10
SURVIVAL_CAP = 0.97          # used only by SURVIVAL_CAP_MODE "hard097"
# --- v2.8 fix 1: survival draw cap ---
SURVIVAL_CAP_MODE = "soft"   # "soft" | "none" | "hard097"
SURVIVAL_SOFT_KNEE = 0.98
SURVIVAL_CEILING = 1.0       # physical limit, survival fraction <= 1

# --- v2.8 fix 2: grounded cold model ---
COLD_MODEL = "arrhenius_growth"   # | "arrhenius_survival" | "linear_fitted"
GAS_R = 8.314462618
# Symeonidou et al. 2024 Extremophiles (PMC11266278) Table 2, control.
DR_CO2_UG_PER_DAY_25C = 812.63
DR_CO2_UG_PER_DAY_0C = 66.03
COLD_T_WARM_C = 25.0         # cold factor 1.0
COLD_T_COLD_C = 0.0          # cold factor 0.0
COLD_EA_J_PER_MOL = (GAS_R * math.log(DR_CO2_UG_PER_DAY_25C / DR_CO2_UG_PER_DAY_0C)
                     / (1.0 / (273.15 + COLD_T_COLD_C) - 1.0 / (273.15 + COLD_T_WARM_C)))

# --- v2.5 fix 1: CO2 freeze hard gate and freeze control ---
# Hard gate: CO2 below FREEZE_CO2_T on ANY sol = failure, tested
# before the O2 target. Must stay True for scored results.
FREEZE_HARD_GATE = True
# "throttle" (default) | "vent" | "off"
FREEZE_CONTROL_MODE = "throttle"
# Throttle ceiling sits this fraction below the freeze-equivalent O2.
# 1% of 5.4545e15 kg leaves the ceiling (5.40e15) above the 5.25e15
# target. Assumption: control precision of ~1% of cumulative output.
FREEZE_MARGIN_FRAC = 0.01
# Vent mode only: max over-ceiling production shed as heat per sol
# (kg O2-equivalent). ASSUMPTION, unvalidated; sensitivity only.
VENT_SHED_CAPACITY_KG_O2_PER_SOL = 5.0e13
# A run whose standing population falls below this is extinct (fail).
EXTINCTION_UNITS = 1.0

# Hard floor cannot be removed by lowering REDUCTASE_FLOOR.
HARD_REDUCTASE_FLOOR = 0.60
REDUCTASE_FLOOR = 0.60
REDUCTASE_PROTEOME = 0.03
AFP_PROTEOME = 0.04
MAA_PROTEOME = 0.04
BURDEN_CAP = 0.15
PENALTY_RATE = 0.20
BURDEN_TRIGGER = 1.5
CHLORITE_BURDEN_SPIKE = 0.18
# Remaining fraction after 10 sols = 0.10 => 90% dead in 10 sols.
CHLORITE_SURVIVAL_PER_SOL = 0.10 ** (1.0 / 10.0)

PERCH_LD50 = 10.0
PERCH_HILL = 2.0

COLD_SUPPRESSION = {"baseline": 1.0, "moderate": 0.5, "severe": 0.25}
# --- v2.9 thermal habitat (ASSUMPTIONS: constant interior, no energy budget) ---
HABITAT_ENABLED = True
HABITAT_MODE = {"baseline": "ambient", "moderate": "insulated",
                "severe": "insulated_heated"}
HABITAT_INTERIOR_C = 25.0
HABITAT_RESTORES_PROTEOME = True
DRAW_HIST_BINS = 1000
OXIDATIVE_FACTOR = {"baseline": 1.0, "moderate": 0.97, "severe": 0.99}

# --- Nutrient inventory (ASSUMPTIONS, not measured) ---
# Default volume is a 1000 km x 1000 km x 1 m regional rind (unchanged).
N_REGOLITH_PCT = 0.01
P_REGOLITH_PCT = 0.005  # v2.2/v2.3 value, comparison only
REGOLITH_DENSITY_KG_M3 = 1500.0
ACCESSIBLE_REGOLITH_M3 = 1.0e12
UNIT_DRY_KG = 2.0
BIOMASS_N_FRAC = 0.11   # typical cyanobacterial dry-mass N
BIOMASS_P_FRAC = 0.015  # typical cyanobacterial dry-mass P
NUTRIENT_VIABLE_UNITS = 1.0
# Atmospheric N import (kg N / sol), v2.3 requirement-sized value, held.
N_IMPORT_KG_PER_SOL = 7.251e13
# Labile (already bioavailable) environmental P at t=0, v2.4 value, held.
# v2.5 treats it as the labile 4.6% slice of the rover-grade inventory.
INITIAL_P_POOL_KG = 1.5e11
# Fraction of dead-unit N and P returned to the environmental pools.
RECYCLE_FRACTION = 0.8

# --- v2.5 fix 2: phosphorus scavenging trait (ASSUMPTIONS) ---
# Rover-grade soil P. Approximate published APXS soil figures sit in a
# ~0.3-1.0 wt% P2O5 window (many Gale soils ~0.8-1.0 wt%). 0.50 wt%
# P2O5 (= 0.218% elemental P) is a deliberately below-Gale-average
# central value. Sensitivity at 0.3 and 1.0 is printed.
REGOLITH_P2O5_WT_PCT = 0.50
P_MASS_FRAC_IN_P2O5 = 61.973762 / 141.944522   # 0.4366
SCAV_ENABLED = True
# kg P solubilised per kg dry biomass per sol, x (mineral P left /
# mineral P at t=0). Grounding (order of magnitude, assumptions):
#  - Earth phosphate-solubilising bacteria in NBRIP broth at 28 C with
#    10 g/L glucose release ~15-58 mg P/L from rock phosphate in 3-7
#    days (75-420 mg/L from the far more soluble Ca3(PO4)2), i.e.
#    ~2-19 mg P/L/day. Assuming ~1-2 g/L dry bacterial biomass (not
#    reported in those assays) gives ~1e-3 to 2e-2 kg P/kg dry/day.
#  - Mars penalty: cold (~30-60 C below the assay), thin liquid-water
#    films, no free glucose (organic acids must come from fixed carbon),
#    igneous apatite/merrillite rather than sedimentary rock phosphate.
#    Assumed >=10x slower -> ~1e-4 to 2e-3 kg P/kg dry/sol.
#  - Default 5e-4 is roughly the geometric middle of that Mars range.
#    1 sol ~ 1.03 Earth days (ignored).
SCAV_KG_P_PER_KG_DRY_PER_SOL = 1.0e-3   # v2.8 scored (v2.6/v2.7: 2e-3)
# v2.6 swept options; each gets its own solved doubling and ensemble.
SCAV_RATE_OPTIONS = (5.0e-4, 1.0e-3, 2.0e-3)
# Heterologous proteome cost of the scavenging module (organic-acid /
# gcd-pqq glucose-dehydrogenase + phytase/phosphatase export).
# ASSUMPTION. Baseline (reductase 1.0) total becomes exactly 0.15 =
# the cap (0.05+0.04+0.04+0.02; penalty applies only ABOVE the cap,
# so zero headroom, no penalty); moderate/severe 0.1375.
SCAV_PROTEOME = 0.02

# --- v2.5 fix 4: P import fallback, realistic bound ---
SOLS_PER_EARTH_YEAR = 365.25 * 86400.0 / 88775.244
# Present-day world phosphate-rock mine output ~220-240 Mt/yr (USGS
# Mineral Commodity Summaries order of magnitude) at ~30 wt% P2O5
# marketable grade. ASSUMPTIONS.
WORLD_PHOSPHATE_ROCK_KG_PER_EARTH_YR = 2.3e11
PHOSPHATE_ROCK_P2O5_FRAC = 0.30
# Realistic upper bound: the WHOLE Earth phosphate industry, delivered
# to Mars every year (far beyond any launch or ISRU plan; a generous
# bound, not a forecast). = 2.3e11 * 0.30 * 0.4366 / 355.48 kg P/sol.
P_IMPORT_REALISTIC_MAX_KG_PER_SOL = (
    WORLD_PHOSPHATE_ROCK_KG_PER_EARTH_YR * PHOSPHATE_ROCK_P2O5_FRAC
    * P_MASS_FRAC_IN_P2O5 / SOLS_PER_EARTH_YEAR)
# Default 0: growth must not depend on an import line. Fallback runs
# use P_IMPORT_REALISTIC_MAX_KG_PER_SOL. Never exceed that bound.
P_IMPORT_KG_PER_SOL = 0.0
V24_P_IMPORT_KG_PER_SOL = 9.887e12  # reference only, NOT used

# --- Lattice long-horizon (ASSUMPTIONS, not measured; unchanged) ---
LATTICE_CYCLES_PER_EARTH_YEAR = 365.25 * 86400.0 / 88775.244
LATTICE_LOSS_PER_CYCLE = 1.0e-5
LATTICE_DUST_TAU_YEARS = 20.0
CASCADE_UNLOCK_INTEGRITY = 0.50
LATTICE_TEAR_INTEGRITY = 0.25
LATTICE_HORIZON_YEARS = 15.0


def unit_n_kg():
    return UNIT_DRY_KG * BIOMASS_N_FRAC


def unit_p_kg():
    return UNIT_DRY_KG * BIOMASS_P_FRAC


def initial_nutrient_pools():
    mass = ACCESSIBLE_REGOLITH_M3 * REGOLITH_DENSITY_KG_M3
    n_pool = mass * (N_REGOLITH_PCT / 100.0)
    p_pool = INITIAL_P_POOL_KG
    return mass, n_pool, p_pool


def implied_p_regolith_pct():
    mass = ACCESSIBLE_REGOLITH_M3 * REGOLITH_DENSITY_KG_M3
    return 100.0 * INITIAL_P_POOL_KG / mass


def p_wt_pct_as_p2o5(p_wt_pct):
    """Elemental P wt% -> P2O5 wt%. P2O5 is 43.64% P by mass."""
    return p_wt_pct * (141.944522 / 61.973762)


def reductase_survival(perchlorate_pct):
    return 1.0 / (1.0 + (perchlorate_pct / PERCH_LD50) ** PERCH_HILL)


def effective_reductase_floor():
    """60% hard bound; lowering REDUCTASE_FLOOR cannot punch through."""
    return max(HARD_REDUCTASE_FLOOR, REDUCTASE_FLOOR)


def chlorite_kill_factor(reductase, total_het, floor_override=None):
    """Rapid kill if reductase is below the hard floor or burden > 18%.

    Normal ensemble never enters this branch because proteome_levels
    clamps reductase to the hard floor and total heterologous load stays
    under 15%. floor_override lets the breach demo bypass the clamp.
    """
    r = reductase if floor_override is None else floor_override
    if r < HARD_REDUCTASE_FLOOR or total_het > CHLORITE_BURDEN_SPIKE:
        return CHLORITE_SURVIVAL_PER_SOL
    return 1.0




def proteome_levels(stress_factor, cold_factor):
    """v1.8 clamp logic, plus the v2.5 scavenging module's proteome."""
    burden_throttle = min(1.0, max(0.0, (stress_factor - 1.0) / 1.0))
    combined = burden_throttle * cold_factor
    floor = effective_reductase_floor()
    reductase = max(floor, 1.0 - combined)
    residual = max(0.0, combined - (1.0 - floor))
    afp = max(0.0, AFP_PROTEOME * (1.0 - min(1.0, residual * 2.0)))
    maa = max(0.0, MAA_PROTEOME * (1.0 - min(1.0, max(0.0, residual * 2.0 - 1.0))))
    scav = SCAV_PROTEOME if SCAV_ENABLED else 0.0
    total = REDUCTASE_PROTEOME * (reductase / floor) + afp + maa + scav
    return reductase, afp, maa, total, combined


def rover_total_p_kg(p2o5_wt_pct=None):
    """Elemental P in the default working volume at rover-grade P2O5."""
    if p2o5_wt_pct is None:
        p2o5_wt_pct = REGOLITH_P2O5_WT_PCT
    mass = ACCESSIBLE_REGOLITH_M3 * REGOLITH_DENSITY_KG_M3
    return mass * (p2o5_wt_pct / 100.0) * P_MASS_FRAC_IN_P2O5


def mineral_p0_kg(p2o5_wt_pct=None):
    """Mineral (not yet labile) P = rover-grade total - labile pool."""
    return max(0.0, rover_total_p_kg(p2o5_wt_pct) - INITIAL_P_POOL_KG)


def survival_center_for(tier, perch):
    """v2.6: per-cell survival center (override for severe 1.00% only)."""
    if tier == "severe" and abs(perch - 1.00) < 1e-9:
        return SURVIVAL_CENTER_SEVERE_1PCT
    return SURVIVAL_CENTER


def habitat_active(tier):
    return HABITAT_ENABLED and HABITAT_MODE.get(tier, "ambient") != "ambient"


def cold_from_temp_c(t_c):
    """Inverse of the v2.8 linear map (0 C -> 0, 25 C -> 1), clipped."""
    c = (t_c - COLD_T_COLD_C) / (COLD_T_WARM_C - COLD_T_COLD_C)
    return min(1.0, max(0.0, c))


def tier_cold(tier):
    """Effective cold factor for growth/survival/center (habitat-aware)."""
    if habitat_active(tier):
        return cold_from_temp_c(HABITAT_INTERIOR_C)
    return COLD_SUPPRESSION[tier]


def tier_prot_cold(tier):
    """Cold factor seen by proteome_levels."""
    if habitat_active(tier) and HABITAT_RESTORES_PROTEOME:
        return cold_from_temp_c(HABITAT_INTERIOR_C)
    return COLD_SUPPRESSION[tier]


def cold_temp_c(cold):
    """ASSUMED linear map: cold 1.0 -> 25 C, cold 0.0 -> 0 C."""
    return COLD_T_COLD_C + cold * (COLD_T_WARM_C - COLD_T_COLD_C)


def cold_rate_ratio(cold):
    """Arrhenius metabolic rate at the mapped temperature / rate at 25 C."""
    if cold >= 1.0:
        return 1.0
    t = 273.15 + cold_temp_c(cold)
    tw = 273.15 + COLD_T_WARM_C
    return math.exp(-COLD_EA_J_PER_MOL / GAS_R * (1.0 / t - 1.0 / tw))


def cold_net_factor(cold):
    """Cold factor applied to per-sol SURVIVAL."""
    if COLD_MODEL == "linear_fitted":
        return 1.0 - COLD_NET_COUPLING * (1.0 - cold)
    if COLD_MODEL == "arrhenius_survival":
        return cold_rate_ratio(cold)
    return 1.0


def cold_growth_mult(cold):
    """Cold multiplier on the replication RATE (exponent of 2^(1/D))."""
    if COLD_MODEL == "arrhenius_growth":
        return cold_rate_ratio(cold)
    return 1.0


def cell_growth(cold, doubling):
    return 2 ** (cold_growth_mult(cold) / doubling)


def survival_transform(raw):
    """v2.8 draw map: floor, then cap per SURVIVAL_CAP_MODE."""
    if SURVIVAL_CAP_MODE == "hard097":
        return min(SURVIVAL_CAP, max(SURVIVAL_FLOOR, raw))
    if SURVIVAL_CAP_MODE == "none":
        return min(SURVIVAL_CEILING, max(SURVIVAL_FLOOR, raw))
    if SURVIVAL_CAP_MODE == "soft":
        x = max(SURVIVAL_FLOOR, raw)
        k = SURVIVAL_SOFT_KNEE
        if x <= k:
            return x
        w = SURVIVAL_CEILING - k
        return k + w * math.tanh((x - k) / w)
    raise ValueError(SURVIVAL_CAP_MODE)


def shoulder_threshold():
    if SURVIVAL_CAP_MODE == "hard097":
        return SURVIVAL_CAP
    if SURVIVAL_CAP_MODE == "soft":
        return SURVIVAL_SOFT_KNEE
    return SURVIVAL_CEILING


_QZ = [-9.0 + 18.0 * i / 3600 for i in range(3601)]
_QW = [math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi) * (18.0 / 3600) for z in _QZ]
_EG_CACHE = {}


def expected_geo_draw(center):
    """Geo-mean of the transformed draw at a center, current cap mode."""
    if SURVIVAL_CAP_MODE == "hard097":
        return geo_clamped_analytic(center, cap=SURVIVAL_CAP)
    if SURVIVAL_CAP_MODE == "none":
        return geo_clamped_analytic(center, cap=SURVIVAL_CEILING)
    key = (center, SURVIVAL_SOFT_KNEE, SURVIVAL_SPREAD, SURVIVAL_FLOOR)
    v = _EG_CACHE.get(key)
    if v is None:
        mu = math.log(center)
        e = sum(w * math.log(survival_transform(math.exp(mu + SURVIVAL_SPREAD * z)))
                for z, w in zip(_QZ, _QW))
        v = math.exp(e)
        _EG_CACHE[key] = v
    return v


def cold_rng_for(rng):
    """Separate per-run RNG for cold variation. Seeded from a COPY of the
    survival RNG state so the survival draw stream is not consumed."""
    st = random.Random()
    st.setstate(rng.getstate())
    return random.Random(st.getrandbits(64) ^ 0xC01D)


def read_cold(tier_cold, cold_rng=None):
    """Per-sol cold suppression reading (quantised)."""
    c = tier_cold
    if cold_rng is not None and COLD_VARIATION_SPREAD > 0.0:
        c = tier_cold * math.exp(COLD_VARIATION_SPREAD * cold_rng.gauss(0.0, 1.0))
    c = min(COLD_MAX, max(COLD_MIN, c))
    if COLD_READ_RESOLUTION > 0.0:
        c = round(c / COLD_READ_RESOLUTION) * COLD_READ_RESOLUTION
    return c


def geo_clamped_analytic(center, cap=None, floor=None, spread=None):
    """Exact geo-mean of the clamped lognormal draw (closed form)."""
    cap = SURVIVAL_CAP if cap is None else cap
    floor = SURVIVAL_FLOOR if floor is None else floor
    sd = SURVIVAL_SPREAD if spread is None else spread
    mu, a, b = math.log(center), math.log(floor), math.log(cap)
    al, be = (a - mu) / sd, (b - mu) / sd
    cdf = lambda x: 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))
    pdf = lambda x: math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)
    e = (a * cdf(al) + b * (1.0 - cdf(be)) + mu * (cdf(be) - cdf(al))
         + sd * (pdf(al) - pdf(be)))
    return math.exp(e)


def cap_clamp_prob(center):
    """P(raw lognormal draw > shoulder threshold) at a given center
    (0.97 cap for hard097, knee for soft, 1.0 for none)."""
    z = (math.log(shoulder_threshold()) - math.log(center)) / SURVIVAL_SPREAD
    return 0.5 * (1.0 - math.erf(z / math.sqrt(2.0)))


def non_draw_factor(tier, perch, cold, doubling):
    """Everything in expected net growth except the clamped draw."""
    r, a, m, tot, c = proteome_levels(STRESS_FACTOR[tier], tier_prot_cold(tier))
    f = OXIDATIVE_FACTOR[tier] * cold_net_factor(cold)
    if tot > BURDEN_CAP:
        f *= 1.0 - min(0.9, PENALTY_RATE * (tot - BURDEN_CAP) * STRESS_FACTOR[tier])
    f *= reductase_survival(perch) * chlorite_kill_factor(r, tot)
    return f * cell_growth(cold, doubling)


_ADAPT_CACHE = {}


def adaptive_lower(tier, perch):
    if ADAPTIVE_FLOOR_AT_STATIC:
        return max(ADAPTIVE_CENTER_MIN, survival_center_for(tier, perch))
    return ADAPTIVE_CENTER_MIN


def adaptive_center(tier, perch, cold, doubling=None):
    """Center whose expected clamped draw gives expected net = target,
    clipped to [lower, ADAPTIVE_CENTER_MAX]. Returns (center,
    expected_net_at_center, hit_max)."""
    if doubling is None:
        doubling = DOUBLING_SOLS
    key = (tier, perch, cold, doubling, ADAPTIVE_NET_TARGET, COLD_NET_COUPLING,
           ADAPTIVE_CENTER_MIN, ADAPTIVE_CENTER_MAX, ADAPTIVE_FLOOR_AT_STATIC,
           SURVIVAL_CAP, SURVIVAL_CENTER_SEVERE_1PCT, SURVIVAL_CENTER,
           SURVIVAL_CAP_MODE, SURVIVAL_SOFT_KNEE, COLD_MODEL,
           HABITAT_ENABLED, HABITAT_RESTORES_PROTEOME, HABITAT_INTERIOR_C)
    hit = _ADAPT_CACHE.get(key)
    if hit is not None:
        return hit
    k = non_draw_factor(tier, perch, cold, doubling)
    lo, hi = adaptive_lower(tier, perch), ADAPTIVE_CENTER_MAX
    net = lambda c: expected_geo_draw(c) * k
    if net(lo) >= ADAPTIVE_NET_TARGET:
        out = (lo, net(lo), False)
    elif net(hi) < ADAPTIVE_NET_TARGET:
        out = (hi, net(hi), True)
    else:
        a, b = lo, hi
        for _ in range(60):
            mid = 0.5 * (a + b)
            if net(mid) >= ADAPTIVE_NET_TARGET:
                b = mid
            else:
                a = mid
        out = (b, net(b), False)
    _ADAPT_CACHE[key] = out
    return out


def calibrate_cold_coupling(doubling=None):
    """COLD_NET_COUPLING such that the calibration cell at its tier cold
    needs exactly COLD_CALIBRATION_CENTER."""
    if doubling is None:
        doubling = DOUBLING_SOLS
    tier, perch = COLD_CALIBRATION_CELL
    cold = COLD_SUPPRESSION[tier]
    saved = globals()["COLD_NET_COUPLING"]
    globals()["COLD_NET_COUPLING"] = 0.0
    k0 = non_draw_factor(tier, perch, cold, doubling)
    globals()["COLD_NET_COUPLING"] = saved
    need_f = ADAPTIVE_NET_TARGET / (expected_geo_draw(COLD_CALIBRATION_CENTER) * k0)
    return (1.0 - need_f) / (1.0 - cold)


def o2_ceiling_kg():
    return freeze_o2_kg() * (1.0 - FREEZE_MARGIN_FRAC)


def grow_one_sol(units, s_eff, growth, n_rem, p_rem, m_rem, m0,
                 p_import, scav_rate):
    """One sol of nutrient bookkeeping + replication (shared by the
    stochastic ensemble and the deterministic geo-mean solves).

    Order: N import, P import, P scavenging (mineral -> labile, by the
    standing population at the start of the sol), mortality, recycle,
    replication limited by N and P. Returns the new state and the clip
    reason (None if growth was not nutrient-limited this sol).
    """
    n_per = UNIT_DRY_KG * BIOMASS_N_FRAC
    p_per = UNIT_DRY_KG * BIOMASS_P_FRAC
    n_viable = NUTRIENT_VIABLE_UNITS * n_per
    p_viable = NUTRIENT_VIABLE_UNITS * p_per
    n_rem += N_IMPORT_KG_PER_SOL
    p_rem += p_import
    scav = 0.0
    if scav_rate > 0.0 and m_rem > 0.0 and m0 > 0.0:
        scav = scav_rate * UNIT_DRY_KG * units * (m_rem / m0)
        if scav > m_rem:
            scav = m_rem
        m_rem -= scav
        p_rem += scav
    survivors = units * s_eff
    dead = units - survivors
    if dead < 0.0:
        dead = 0.0
        survivors = units
    n_rem += dead * n_per * RECYCLE_FRACTION
    p_rem += dead * p_per * RECYCLE_FRACTION
    reason = None
    if (n_rem > n_viable) and (p_rem > p_viable):
        proposed = survivors * growth
        added = proposed - survivors
        avail_n = n_rem - n_viable
        avail_p = p_rem - p_viable
        max_add = min(added, avail_n / n_per, avail_p / p_per)
        if max_add < added:
            rs = []
            if avail_n / n_per < added:
                rs.append("N")
            if avail_p / p_per < added:
                rs.append("P")
            reason = "+".join(rs) if rs else "clip"
            added = max(0.0, max_add)
            proposed = survivors + added
        n_rem = max(0.0, n_rem - added * n_per)
        p_rem = max(0.0, p_rem - added * p_per)
        units = proposed
    else:
        rs = []
        if not (n_rem > n_viable):
            rs.append("N")
        if not (p_rem > p_viable):
            rs.append("P")
        reason = "+".join(rs) if rs else "floor"
        units = survivors
    return units, n_rem, p_rem, m_rem, scav, reason


def apply_freeze_control(o2, prod, mode, ceiling, vent_cap):
    """Return (prod_after_control, shed_kg, throttled_flag)."""
    if mode == "off" or o2 + prod <= ceiling:
        return prod, 0.0, False
    excess = o2 + prod - ceiling
    if mode == "throttle":
        return max(0.0, prod - excess), excess, True
    if mode == "vent":
        shed = min(excess, vent_cap)
        return prod - shed, shed, True
    raise ValueError(f"unknown FREEZE_CONTROL_MODE {mode!r}")


def run_once(rng, perchlorate_pct, tier, stop_on_targets=True, max_sols=None,
             doubling=None, p_import=None, scav_rate=None, control=None,
             o2_first=False, vent_cap=None, record_traj=False):
    """One stochastic run. Returns a dict.

    o2_first=False (default, v2.5 hard gate): every sol, CO2 < freeze
    is tested first and is a failure regardless of O2.
    o2_first=True reproduces the v2.4 order (O2 >= target tested first)
    for the ordering comparison only.
    """
    if doubling is None:
        doubling = DOUBLING_SOLS
    if p_import is None:
        p_import = P_IMPORT_KG_PER_SOL
    if scav_rate is None:
        scav_rate = SCAV_KG_P_PER_KG_DRY_PER_SOL if SCAV_ENABLED else 0.0
    if control is None:
        control = FREEZE_CONTROL_MODE
    if vent_cap is None:
        vent_cap = VENT_SHED_CAPACITY_KG_O2_PER_SOL
    if max_sols is None:
        max_sols = MAX_SOLS
    hard_gate = FREEZE_HARD_GATE and not o2_first
    units = INOCULUM
    o2 = 0.0
    co2_t = CO2_START_T
    perch_factor = reductase_survival(perchlorate_pct)
    sf = STRESS_FACTOR[tier]
    cf = tier_cold(tier)
    ox = OXIDATIVE_FACTOR[tier]
    growth = 2 ** (1.0 / doubling)
    sum_log_growth = 0.0
    peak_units = INOCULUM
    hist = [0] * (DRAW_HIST_BINS + 1)
    shoulder = shoulder_threshold()
    reductase, afp, maa, total_het, combined = proteome_levels(sf, tier_prot_cold(tier))
    _, n_rem, _ = initial_nutrient_pools()
    p_rem = INITIAL_P_POOL_KG
    m0 = mineral_p0_kg()
    m_rem = m0
    ceiling = o2_ceiling_kg()
    log_c = math.log(survival_center_for(tier, perchlorate_pct))
    adaptive = ADAPTIVE_SURVIVAL
    cold_rng = None
    if COLD_VARIATION_SPREAD > 0.0:
        cold_rng = cold_rng_for(rng)
    sum_center = 0.0
    min_center = 9.0
    max_center = 0.0
    at_max_sols = 0
    capped_draws = 0
    sum_log_eff = 0.0
    sum_cold = 0.0
    below_target_sols = 0
    burden_excess_acc = 0.0
    growth_end_sol = None
    growth_end_reason = None
    chlorite_hits = 0
    min_draw = 1.0
    min_eff = 1.0
    sum_draw = 0.0
    sum_eff = 0.0
    n_draws = 0
    s = 0.0
    crossed_freeze = False
    first_freeze_sol = None
    throttled_sols = 0
    shed_total = 0.0
    scav_total = 0.0
    traj = [] if record_traj else None
    outcome = "timeout"
    sol = 0
    for sol in range(1, max_sols + 1):
        cold = read_cold(cf, None if habitat_active(tier) else cold_rng)
        fc = cold_net_factor(cold)
        growth = cell_growth(cold, doubling)
        sum_log_growth += math.log(growth)
        if adaptive:
            cen, exp_net, at_max = adaptive_center(tier, perchlorate_pct, cold,
                                                   doubling)
            log_c = math.log(cen)
            if at_max:
                at_max_sols += 1
            if exp_net < ADAPTIVE_NET_TARGET - 1e-9:
                below_target_sols += 1
        else:
            cen = math.exp(log_c)
        sum_center += cen
        if cen < min_center:
            min_center = cen
        if cen > max_center:
            max_center = cen
        sum_cold += cold
        raw = rng.lognormvariate(log_c, SURVIVAL_SPREAD)
        if raw > shoulder:
            capped_draws += 1
        draw = survival_transform(raw)
        hist[min(DRAW_HIST_BINS, int(draw * DRAW_HIST_BINS))] += 1
        s = draw * ox * fc
        if total_het > BURDEN_CAP:
            excess = total_het - BURDEN_CAP
            burden_excess_acc += excess
            penalty = min(0.9, PENALTY_RATE * excess * sf)
            s = s * (1.0 - penalty)
        kill = chlorite_kill_factor(reductase, total_het)
        if kill < 1.0:
            chlorite_hits += 1
        s_eff = s * perch_factor * kill
        if draw < min_draw:
            min_draw = draw
        if s_eff < min_eff:
            min_eff = s_eff
        sum_draw += draw
        sum_eff += s_eff
        sum_log_eff += math.log(s_eff) if s_eff > 0.0 else -50.0
        n_draws += 1
        units, n_rem, p_rem, m_rem, scav, reason = grow_one_sol(
            units, s_eff, growth, n_rem, p_rem, m_rem, m0, p_import, scav_rate)
        scav_total += scav
        if units > peak_units:
            peak_units = units
        if reason is not None and growth_end_sol is None:
            growth_end_sol = sol
            growth_end_reason = reason
        prod = units * PER_UNIT_KG * reductase
        prod, shed, thr = apply_freeze_control(o2, prod, control, ceiling,
                                               vent_cap)
        if thr:
            throttled_sols += 1
            shed_total += shed
        o2 += prod
        co2_t -= prod * CO2_PER_KG_O2 / 1000.0
        if co2_t < FREEZE_CO2_T and not crossed_freeze:
            crossed_freeze = True
            first_freeze_sol = sol
        if record_traj:
            traj.append((sol, units, n_rem, p_rem, m_rem, o2, co2_t,
                         growth_end_sol, growth_end_reason))
        if stop_on_targets:
            if hard_gate:
                if co2_t < FREEZE_CO2_T:
                    outcome = "freeze"
                    break
                if o2 >= TARGET_KG:
                    outcome = "clear"
                    break
            else:
                if o2 >= TARGET_KG:
                    outcome = "clear"
                    break
                if co2_t < FREEZE_CO2_T:
                    outcome = "freeze"
                    break
            if units < EXTINCTION_UNITS:
                outcome = "extinct"
                break
    else:
        outcome = "timeout" if stop_on_targets else "horizon"
    return {
        "sol": sol, "ok": outcome == "clear", "outcome": outcome,
        "last_s": s, "units": units, "o2": o2, "co2_t": co2_t,
        "burden_excess": burden_excess_acc,
        "growth_end": growth_end_sol, "growth_reason": growth_end_reason,
        "chlorite_hits": chlorite_hits, "n_rem": n_rem, "p_rem": p_rem,
        "m_rem": m_rem, "m0": m0, "scav_total": scav_total,
        "min_draw": min_draw, "min_eff": min_eff,
        "sum_draw": sum_draw, "sum_eff": sum_eff, "n_draws": n_draws,
        "crossed_freeze": crossed_freeze, "first_freeze_sol": first_freeze_sol,
        "throttled_sols": throttled_sols, "shed_total": shed_total,
        "traj": traj,
        "sum_center": sum_center, "min_center": min_center,
        "max_center": max_center, "at_max_sols": at_max_sols,
        "capped_draws": capped_draws, "sum_log_eff": sum_log_eff,
        "sum_cold": sum_cold, "below_target_sols": below_target_sols,
        "growth": growth, "sum_log_growth": sum_log_growth,
        "peak_units": peak_units, "hist": hist,
    }


_GEO_S_CACHE = {}


def geo_s_clamped(center=None):
    if center is None:
        center = SURVIVAL_CENTER
    key = (center, SURVIVAL_CAP, SURVIVAL_FLOOR, SURVIVAL_SPREAD)
    if key not in _GEO_S_CACHE:
        _GEO_S_CACHE[key] = clamped_s_stats(*key[:2], key[2], key[3])
    return _GEO_S_CACHE[key]


def geo_s_eff(perch, tier, doubling=None):
    """Geo-mean per-sol survival incl. ox, perchlorate, burden penalty.
    v2.7: with ADAPTIVE_SURVIVAL the center is the adaptive center at the
    tier cold value (analytic geo-mean when the center is lifted above
    its lower bound; the v2.6 sampled geo-mean when it sits on it)."""
    cen = survival_center_for(tier, perch)
    if ADAPTIVE_SURVIVAL:
        cen, _, _ = adaptive_center(tier, perch, tier_cold(tier), doubling)
    if SURVIVAL_CAP_MODE != "hard097":
        geo = expected_geo_draw(cen)
    elif ADAPTIVE_SURVIVAL and cen > adaptive_lower(tier, perch) + 1e-15:
        geo = geo_clamped_analytic(cen)
    else:
        _, geo = geo_s_clamped(cen)
    s = geo * OXIDATIVE_FACTOR[tier] * cold_net_factor(tier_cold(tier))
    r, a, m, tot, c = proteome_levels(STRESS_FACTOR[tier], tier_prot_cold(tier))
    if tot > BURDEN_CAP:
        s *= 1.0 - min(0.9, PENALTY_RATE * (tot - BURDEN_CAP) * STRESS_FACTOR[tier])
    return s * reductase_survival(perch) * chlorite_kill_factor(r, tot)


def deterministic_run(doubling, p_import=0.0, scav_rate=None, p2o5=None,
                      perch=0.50, tier="baseline", max_sols=400):
    """Geo-mean trajectory (no stochastic draws, no stop on targets).

    Returns dict with growth_end (first clipped sol or None), reason,
    o2_target_sol (first sol cumulative O2 >= target, uncontrolled),
    freeze_sol, units at end, mineral P left fraction.
    """
    if scav_rate is None:
        scav_rate = SCAV_KG_P_PER_KG_DRY_PER_SOL if SCAV_ENABLED else 0.0
    growth = cell_growth(tier_cold(tier), doubling)
    s_eff = geo_s_eff(perch, tier, doubling)
    reductase = proteome_levels(STRESS_FACTOR[tier], tier_prot_cold(tier))[0]
    _, n_rem, _ = initial_nutrient_pools()
    p_rem = INITIAL_P_POOL_KG
    m0 = mineral_p0_kg(p2o5)
    m_rem = m0
    units = INOCULUM
    o2 = 0.0
    ge = None
    ge_reason = None
    t_sol = None
    f_sol = None
    peak = units
    freeze_eq = freeze_o2_kg()
    for sol in range(1, max_sols + 1):
        units, n_rem, p_rem, m_rem, scav, reason = grow_one_sol(
            units, s_eff, growth, n_rem, p_rem, m_rem, m0, p_import, scav_rate)
        if reason is not None and ge is None:
            ge, ge_reason = sol, reason
        peak = max(peak, units)
        o2 += units * PER_UNIT_KG * reductase
        if t_sol is None and o2 >= TARGET_KG:
            t_sol = sol
        if f_sol is None and o2 >= freeze_eq:
            f_sol = sol
    return {"growth_end": ge, "reason": ge_reason, "o2_target_sol": t_sol,
            "freeze_sol": f_sol, "units": units, "peak": peak,
            "m_left_frac": (m_rem / m0) if m0 > 0 else 0.0,
            "p_rem": p_rem, "n_rem": n_rem}


def solve_doubling_sols(horizon=200, p_import=0.0, scav_rate=None, p2o5=None,
                        perch=0.50, tier="baseline", tol=1e-6):
    """Shortest doubling time (sols) with geo-mean growth unclipped for
    > horizon sols. Bisection on D; ok(D) is monotone (slower growth
    never exhausts P sooner), checked by a scan in main()."""
    def ok(d):
        r = deterministic_run(d, p_import, scav_rate, p2o5, perch, tier,
                              max_sols=horizon + 1)
        return r["growth_end"] is None or r["growth_end"] > horizon

    lo, hi = 1.0, V24_DOUBLING_SOLS
    if ok(lo):
        return lo
    while not ok(hi):
        lo = hi
        hi *= 1.5
        if hi > 1e4:
            return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if ok(mid):
            hi = mid
        else:
            lo = mid
        if hi - lo < tol:
            break
    return hi


def solve_doubling_no_clip_before_target(p_import=0.0, scav_rate=None,
                                         p2o5=None, max_sols=3000):
    """Alternative criterion (diagnostic only): shortest D at which the
    baseline-0.50% geo-mean trajectory reaches the O2 target before (or
    without) any nutrient clip."""
    def ok(d):
        r = deterministic_run(d, p_import, scav_rate, p2o5, max_sols=max_sols)
        if r["o2_target_sol"] is None:
            return False
        return r["growth_end"] is None or r["growth_end"] > r["o2_target_sol"]

    lo, hi = 1.0, V24_DOUBLING_SOLS
    if ok(lo):
        return lo
    while not ok(hi):
        lo = hi
        hi *= 1.25
        if hi > 200:
            return None
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if ok(mid):
            hi = mid
        else:
            lo = mid
        if hi - lo < 1e-5:
            break
    return hi


def clamped_s_stats(center, cap, floor, spread, n=100000, seed=0):
    rng = random.Random(seed)
    xs = [min(cap, max(floor, rng.lognormvariate(math.log(center), spread)))
          for _ in range(n)]
    arith = sum(xs) / n
    geo = math.exp(sum(math.log(x) for x in xs) / n)
    return arith, geo


def min_survival_center_for_net(tier, perch, n=100000):
    """Smallest SURVIVAL_CENTER giving geo-mean net > 1, other v2.1 levers fixed."""
    ox = OXIDATIVE_FACTOR[tier]
    growth = 2 ** (1.0 / DOUBLING_SOLS)
    pf = reductase_survival(perch)
    lo, hi = 0.50, 1.20

    def gnet(c):
        _, geo = clamped_s_stats(c, SURVIVAL_CAP, SURVIVAL_FLOOR, SURVIVAL_SPREAD, n=n)
        return geo * ox * pf * growth

    if gnet(hi) <= 1.0:
        return None, gnet(hi)
    for _ in range(36):
        mid = (lo + hi) / 2.0
        if gnet(mid) > 1.0:
            hi = mid
        else:
            lo = mid
    return hi, gnet(hi)


def run_chlorite_demo(sols=10, forced_reductase=0.0, forced_burden=0.20):
    """Deliberate breach: floor bypassed and/or burden > 18%."""
    units = INOCULUM
    hist = []
    for sol in range(1, sols + 1):
        kill = chlorite_kill_factor(forced_reductase, forced_burden,
                                    floor_override=forced_reductase)
        units = units * kill
        frac = units / INOCULUM
        hist.append((sol, frac, 1.0 - frac, kill))
    return hist


def lattice_integrity(t_years, dust_tau=LATTICE_DUST_TAU_YEARS,
                      loss_per_cycle=LATTICE_LOSS_PER_CYCLE):
    cycle_term = math.exp(-loss_per_cycle * LATTICE_CYCLES_PER_EARTH_YEAR * t_years)
    dust_term = math.exp(-t_years / dust_tau) if dust_tau > 0.0 else 0.0
    return cycle_term * dust_term


def first_crossing(threshold, dust_tau, horizon=LATTICE_HORIZON_YEARS, dt=0.01):
    prev_t, prev_i = 0.0, lattice_integrity(0.0, dust_tau)
    if prev_i <= threshold:
        return 0.0
    t = dt
    while t <= horizon + 1e-12:
        i = lattice_integrity(t, dust_tau)
        if i <= threshold:
            # linear interpolate
            frac = (prev_i - threshold) / (prev_i - i) if prev_i != i else 1.0
            return prev_t + frac * (t - prev_t)
        prev_t, prev_i = t, i
        t += dt
    # extrapolate closed form if not yet crossed
    # I = exp(-a t) * exp(-t/tau) = exp(-t (a+1/tau))
    a = loss_per_cycle_year = LATTICE_LOSS_PER_CYCLE * LATTICE_CYCLES_PER_EARTH_YEAR
    k = a + 1.0 / dust_tau
    if k <= 0.0:
        return None
    t_cross = -math.log(threshold) / k
    return t_cross


def run_lattice_horizon():
    a = LATTICE_LOSS_PER_CYCLE * LATTICE_CYCLES_PER_EARTH_YEAR
    print("Lattice long-horizon (Earth years). Rates are unvalidated assumptions.")
    print(f"  diurnal cycles/Earth year: {LATTICE_CYCLES_PER_EARTH_YEAR:.2f}")
    print(f"  loss per cycle: {LATTICE_LOSS_PER_CYCLE:.1e}  -> {100*a:.3f}%/Earth year from dock/magnet fatigue")
    print(f"  dust/static tau: {LATTICE_DUST_TAU_YEARS:.1f} Earth years")
    print(f"  cascade unlock threshold: {CASCADE_UNLOCK_INTEGRITY:.2f}")
    print(f"  lattice tear threshold:    {LATTICE_TEAR_INTEGRITY:.2f}")
    print(f"  {'year':6s} {'integrity':10s}")
    t = 0.0
    while t <= LATTICE_HORIZON_YEARS + 1e-12:
        print(f"  {t:6.1f} {lattice_integrity(t):10.4f}")
        t += 1.0
    unlock = first_crossing(CASCADE_UNLOCK_INTEGRITY, LATTICE_DUST_TAU_YEARS)
    tear = first_crossing(LATTICE_TEAR_INTEGRITY, LATTICE_DUST_TAU_YEARS)
    print(f"  Nominal (tau={LATTICE_DUST_TAU_YEARS:.0f} yr): cascade unlock at {unlock:.2f} Earth years, "
          f"tear at {tear:.2f} Earth years")
    # sensitivity, clearly not a fit
    for tau in (8.0, 12.0, 20.0, 30.0):
        u = first_crossing(CASCADE_UNLOCK_INTEGRITY, tau)
        tr = first_crossing(LATTICE_TEAR_INTEGRITY, tau)
        in_window = (tr is not None and 8.0 <= tr <= 12.0)
        print(f"  Sensitivity tau={tau:.0f} yr: unlock={u:.2f}, tear={tr:.2f}  "
              f"{'(tear inside 8-12 yr window)' if in_window else '(tear not in 8-12 yr window)'}")
    return unlock, tear


def nutrient_volume_table():
    """Unconstrained (v2.1-style) geo-mean exhaustion times for several volumes."""
    growth = 2 ** (1.0 / DOUBLING_SOLS)
    _, geo_s = clamped_s_stats(SURVIVAL_CENTER, SURVIVAL_CAP, SURVIVAL_FLOOR,
                               SURVIVAL_SPREAD)
    n_per = unit_n_kg()
    p_per = unit_p_kg()
    print("Nutrient exhaustion under unconstrained geo-mean growth (diagnostic,")
    print("not a fit to 200 sols). N is limiting at these mass fractions.")
    print(f"  geo_s={geo_s:.6f}  N/unit={n_per:.3f} kg  P/unit={p_per:.3f} kg")
    volumes = [
        ("default 1000x1000 km x 1 m", 1.0e12),
        ("100x100 km x 1 m", 1.0e10),
        ("global 1 m (1.44e8 km^2)", 1.44e8 * 1.0e6),
        ("global 10 m", 1.44e9 * 1.0e6),
    ]
    # sols for N exhaustion: inoc*(net^t - 1)*n_per = n_pool
    def t_ex(net, n_pool):
        if net <= 1.0:
            return float("inf")
        rhs = 1.0 + n_pool / (INOCULUM * n_per)
        return math.log(rhs) / math.log(net)

    nets = {}
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            nets[(tier, p)] = (geo_s * OXIDATIVE_FACTOR[tier]
                               * reductase_survival(p) * growth)
    print(f"  {'volume':28s} {'N_pool_kg':11s} {'base 0.50':>10s} {'sev 1.50':>10s}")
    density = REGOLITH_DENSITY_KG_M3
    for name, vol in volumes:
        n_pool = vol * density * (N_REGOLITH_PCT / 100.0)
        t0 = t_ex(nets[("baseline", 0.50)], n_pool)
        t1 = t_ex(nets[("severe", 1.50)], n_pool)
        print(f"  {name:28s} {n_pool:11.3e} {t0:10.2f} {t1:10.2f}")
    # volume that would exhaust at 200 sols at baseline 0.50
    net = nets[("baseline", 0.50)]
    n_pool_200 = INOCULUM * n_per * (net ** 200 - 1.0)
    vol_200 = n_pool_200 / ((N_REGOLITH_PCT / 100.0) * density)
    area_1m_km2 = vol_200 / 1.0e6
    depth_global = vol_200 / (1.44e8 * 1.0e6)
    print(f"  Volume that would exhaust at 200 sols (baseline 0.50, geo_net={net:.6f}):")
    print(f"    N_pool={n_pool_200:.4e} kg, volume={vol_200:.4e} m3,")
    print(f"    {area_1m_km2:.4e} km2 at 1 m depth, or {depth_global:.1f} m if global "
          f"(Mars area 1.44e8 km2).")


def mars_atmospheric_n_kg():
    """Rough Mars atmospheric N inventory. 2.7% N2 by volume (brief);
    610 Pa, g=3.71 m/s^2, R=3389.5 km. Not a high-precision climate value.
    """
    area = 4.0 * math.pi * (3389.5e3) ** 2
    column = 610.0 / 3.71
    atm_mass = area * column
    # mole fractions, then mass: N2 2.7%, CO2 95.3%, Ar 1.6%
    xn2, xco2, xar = 0.027, 0.953, 0.016
    s = xn2 + xco2 + xar
    xn2, xco2, xar = xn2 / s, xco2 / s, xar / s
    mu = xn2 * 28.0 + xco2 * 44.0 + xar * 39.9
    n2_mass_frac = (xn2 * 28.0) / mu
    return atm_mass, n2_mass_frac, atm_mass * n2_mass_frac




def freeze_o2_kg():
    """O2 (kg) at which co2_t would sit exactly on FREEZE_CO2_T."""
    return (CO2_START_T - FREEZE_CO2_T) * 1000.0 / CO2_PER_KG_O2


def rover_p_reference_kg(elem_p_wt_frac=0.0015):
    """P mass in the default working volume and in a global 1 m rind.

    elem_p_wt_frac default 0.0015 is ~0.15% elemental P, i.e. ~0.34 wt%
    P2O5 — a mid-range figure in the approximate published APXS soil
    window (~0.3-1.0 wt% P2O5).
    """
    mass = ACCESSIBLE_REGOLITH_M3 * REGOLITH_DENSITY_KG_M3
    working = mass * elem_p_wt_frac
    # Mars surface area ~1.44e8 km2
    global_1m = 1.44e8 * 1.0e6 * REGOLITH_DENSITY_KG_M3 * elem_p_wt_frac
    return working, global_1m




def run_cell(tier, perch, **kw):
    """240 paired-seed runs for one cell. Returns a stats dict."""
    master = random.Random(SEED)
    seeds = [master.getrandbits(64) for _ in range(N_RUNS)]
    rs = [run_once(random.Random(sd), perch, tier, **kw) for sd in seeds]
    clears = sorted(r["sol"] for r in rs if r["ok"])
    outcomes = Counter(r["outcome"] for r in rs)
    ges = [r["growth_end"] for r in rs if r["growth_end"] is not None]
    reasons = Counter(r["growth_reason"] for r in rs
                      if r["growth_end"] is not None)
    n_draws = sum(r["n_draws"] for r in rs)
    o2_clear = [r["o2"] for r in rs if r["ok"]]
    rate = len(clears) / N_RUNS
    st = {
        "tier": tier, "perch": perch, "runs": rs,
        "clears": len(clears), "rate": rate, "gate": GATE[tier],
        "passed": rate >= GATE[tier],
        "clear_min": clears[0] if clears else None,
        "clear_med": clears[len(clears) // 2] if clears else None,
        "clear_mean": (sum(clears) / len(clears)) if clears else None,
        "clear_max": clears[-1] if clears else None,
        "outcomes": outcomes,
        "mean_draw": sum(r["sum_draw"] for r in rs) / n_draws,
        "mean_eff": sum(r["sum_eff"] for r in rs) / n_draws,
        "worst_draw": min(r["min_draw"] for r in rs),
        "worst_eff": min(r["min_eff"] for r in rs),
        "mean_last_s": sum(r["last_s"] for r in rs) / N_RUNS,
        "mean_o2": sum(r["o2"] for r in rs) / N_RUNS,
        "mean_o2_clear": (sum(o2_clear) / len(o2_clear)) if o2_clear else 0.0,
        "max_o2": max(r["o2"] for r in rs),
        "freeze_cross": sum(1 for r in rs if r["crossed_freeze"]),
        "freeze_cross_on_clear": sum(1 for r in rs
                                     if r["crossed_freeze"] and r["ok"]),
        "throttled_runs": sum(1 for r in rs if r["throttled_sols"] > 0),
        "shed_mean": sum(r["shed_total"] for r in rs) / N_RUNS,
        "ge_n": len(ges),
        "ge_min": min(ges) if ges else None,
        "ge_max": max(ges) if ges else None,
        "ge_mean": (sum(ges) / len(ges)) if ges else None,
        "reasons": reasons,
        "growing_at_clear": sum(1 for r in rs if r["ok"]
                                and (r["growth_end"] is None
                                     or r["growth_end"] > r["sol"])),
        "scav_mean": sum(r["scav_total"] for r in rs) / N_RUNS,
        "m_left_mean": sum((r["m_rem"] / r["m0"]) if r["m0"] > 0 else 0.0
                           for r in rs) / N_RUNS,
        "mean_sols": sum(r["sol"] for r in rs) / N_RUNS,
        "chlorite": sum(r["chlorite_hits"] for r in rs),
        # v2.7 adaptive-center diagnostics (per-sol, pooled over runs)
        "center_mean": sum(r["sum_center"] for r in rs) / n_draws,
        "center_min": min(r["min_center"] for r in rs),
        "center_max": max(r["max_center"] for r in rs),
        "frac_at_max": sum(r["at_max_sols"] for r in rs) / n_draws,
        "frac_capped": sum(r["capped_draws"] for r in rs) / n_draws,
        "frac_below_target": sum(r["below_target_sols"] for r in rs) / n_draws,
        "cold_mean": sum(r["sum_cold"] for r in rs) / n_draws,
        "net_realised": math.exp((sum(r["sum_log_eff"] for r in rs)
                                  + sum(r["sum_log_growth"] for r in rs)) / n_draws),
        "n_draws": n_draws,
    }
    pk = sorted(r["peak_units"] for r in rs)
    st["peak_med"] = pk[len(pk) // 2]
    st["peak_max"] = pk[-1]
    h = [0] * (DRAW_HIST_BINS + 1)
    for r in rs:
        for i, v in enumerate(r["hist"]):
            if v:
                h[i] += v
    tot = sum(h)

    def q(f):
        acc, tgt = 0, f * tot
        for i, v in enumerate(h):
            acc += v
            if acc >= tgt:
                return (i + 0.5) / DRAW_HIST_BINS
        return 1.0
    st["draw_p5"], st["draw_med"], st["draw_p95"] = q(0.05), q(0.50), q(0.95)
    knee_bin = int(SURVIVAL_SOFT_KNEE * DRAW_HIST_BINS)
    st["draw_above_knee"] = sum(h[knee_bin:]) / tot if tot else 0.0
    for r in rs:
        r["hist"] = None
    return st


def run_ensemble(label, **kw):
    cells = {}
    for tier in STRESS_TIERS:
        for perch in PERCH_LEVELS:
            cells[(tier, perch)] = run_cell(tier, perch, **kw)
    return cells


def _fmt(v, f="{}"):
    return "-" if v is None else f.format(v)


def _reasons(c):
    return ",".join(f"{k}:{v}" for k, v in sorted(c.items())) or "none"


def print_gate_grid(title, cells):
    print(title)
    hdr = f"  {'tier':9s} {'gate':>5s}" + "".join(
        f"  {('%.2f%%' % p) + (' *' if p not in BRIEF_PERCH_LEVELS else ''):>16s}"
        for p in PERCH_LEVELS)
    print(hdr)
    for tier in STRESS_TIERS:
        row = f"  {tier:9s} {GATE[tier]*100:4.0f}%"
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            row += f"  {c['clears']:3d}/{N_RUNS} {'PASS' if c['passed'] else 'FAIL':>4s}{'':5s}"
        print(row)
    brief_pass = sum(1 for (t, p), c in cells.items()
                     if p in BRIEF_PERCH_LEVELS and c["passed"])
    col15 = sum(1 for (t, p), c in cells.items()
                if p not in BRIEF_PERCH_LEVELS and c["passed"])
    allp = sum(1 for c in cells.values() if c["passed"])
    print(f"  * 1.50% column kept from v2.2-v2.4 (not in the v2.5 brief list).")
    print(f"  Brief 9 cells (0.50/0.75/1.00%): {brief_pass}/9 pass.  "
          f"1.50% column: {col15}/3 pass.  All 12: {allp}/12 pass.  "
          f"ALL GATES {'PASS' if allp == 12 else 'FAIL'}")


def print_cell_detail(title, cells):
    print(title)
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            oc = c["outcomes"]
            print(f"  {tier:9s} perch={p:.2f}%: clears {c['clears']}/{N_RUNS} "
                  f"({100*c['rate']:.1f}%) gate {100*c['gate']:.0f}% "
                  f"{'PASS' if c['passed'] else 'FAIL'}  "
                  f"clear_sol min/med/mean/max="
                  f"{_fmt(c['clear_min'])}/{_fmt(c['clear_med'])}/"
                  f"{_fmt(c['clear_mean'], '{:.1f}')}/{_fmt(c['clear_max'])}")
            print(f"      outcomes: clear={oc.get('clear',0)} "
                  f"freeze={oc.get('freeze',0)} extinct={oc.get('extinct',0)} "
                  f"timeout={oc.get('timeout',0)}  mean run length "
                  f"{c['mean_sols']:.1f} sols")
            print(f"      survival: mean_draw={c['mean_draw']:.4f} "
                  f"worst_draw={c['worst_draw']:.4f}  "
                  f"mean_eff={c['mean_eff']:.4f} worst_eff={c['worst_eff']:.4f}  "
                  f"mean_last_s(v2.4-style)={c['mean_last_s']:.4f}")
            print(f"      O2: mean_final={c['mean_o2']:.4e} "
                  f"mean_at_clear={c['mean_o2_clear']:.4e} "
                  f"max={c['max_o2']:.4e} kg  freeze_crossings={c['freeze_cross']} "
                  f"(on clears {c['freeze_cross_on_clear']})  "
                  f"throttled_runs={c['throttled_runs']} "
                  f"mean_shed={c['shed_mean']:.3e} kg")
            print(f"      growth_end n={c['ge_n']} min={_fmt(c['ge_min'])} "
                  f"max={_fmt(c['ge_max'])} "
                  f"mean={_fmt(c['ge_mean'], '{:.1f}')} "
                  f"limit={_reasons(c['reasons'])} "
                  f"growing_at_clear={c['growing_at_clear']}  "
                  f"P scavenged mean={c['scav_mean']:.3e} kg  "
                  f"mineral P left mean={100*c['m_left_mean']:.1f}%")


def print_summary_table(title, cells):
    print(title)
    print(f"  {'cell':17s} {'clears':>7s} {'gate':>4s} {'P/F':>4s} "
          f"{'mean_s':>7s} {'worst_s':>7s} {'mean_O2_kg':>10s} "
          f"{'ge_mean':>7s} {'limit':>12s} {'frz':>4s} {'ext':>4s} "
          f"{'clr_med':>7s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            lim = _reasons(c["reasons"])
            print(f"  {tier:9s} {p:5.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['clears']:3d}/{N_RUNS} {100*c['gate']:3.0f}% "
                  f"{'PASS' if c['passed'] else 'FAIL':>4s} "
                  f"{c['mean_draw']:7.4f} {c['worst_draw']:7.4f} "
                  f"{c['mean_o2']:10.3e} {_fmt(c['ge_mean'], '{:.1f}'):>7s} "
                  f"{lim:>12s} {c['freeze_cross']:4d} "
                  f"{c['outcomes'].get('extinct',0):4d} "
                  f"{_fmt(c['clear_med']):>7s}")


def run_horizon(tier, perch, **kw):
    master = random.Random(SEED)
    seeds = [master.getrandbits(64) for _ in range(N_RUNS)]
    still = 0
    ends = []
    reasons = Counter()
    for sd in seeds:
        r = run_once(random.Random(sd), perch, tier, stop_on_targets=False,
                     max_sols=200, **kw)
        if r["growth_end"] is None:
            still += 1
        else:
            ends.append(r["growth_end"])
            reasons[r["growth_reason"]] += 1
    return still, ends, reasons


def net_table(doubling, label):
    growth = 2 ** (1.0 / doubling)
    print(f"  Geo-mean net growth per sol ({label}, D={doubling}, growth "
          f"{growth:.6f}; '<' = below 1, population shrinks):")
    print("    " + f"{'tier':9s}" + "".join(f"  {p:>8.2f}%" for p in PERCH_LEVELS))
    for tier in STRESS_TIERS:
        row = f"    {tier:9s}"
        for p in PERCH_LEVELS:
            net = geo_s_eff(p, tier, doubling) * cell_growth(tier_cold(tier), doubling)
            row += f"  {net:8.5f}{'<' if net < 1.0 - 1e-9 else ' '}"
        print(row)


def compact_rows(cells, doubling):
    growth = 2 ** (1.0 / doubling)
    print(f"  {'cell':17s} {'clears':>7s} {'gate':>4s} {'P/F':>4s} "
          f"{'net/sol':>8s} {'center':>6s} {'mean_eff':>8s} {'worst_s':>7s} "
          f"{'clr_med':>7s} {'ext':>4s} {'frz':>4s} {'chl':>4s} "
          f"{'scav_kg':>9s} {'min_left':>8s} {'limit':>9s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            net = geo_s_eff(p, tier) * growth
            print(f"  {tier:9s} {p:5.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['clears']:3d}/{N_RUNS} {100*c['gate']:3.0f}% "
                  f"{'PASS' if c['passed'] else 'FAIL':>4s} {net:8.5f} "
                  f"{survival_center_for(tier, p):6.3f} {c['mean_eff']:8.4f} "
                  f"{c['worst_draw']:7.4f} {_fmt(c['clear_med']):>7s} "
                  f"{c['outcomes'].get('extinct', 0):4d} {c['freeze_cross']:4d} "
                  f"{c['chlorite']:4d} {c['scav_mean']:9.3e} "
                  f"{100*c['m_left_mean']:7.1f}% {_reasons(c['reasons']):>9s}")


class with_globals:
    """Temporarily set module constants (restored on exit)."""
    def __init__(self, **kw):
        self.kw = kw
        self.saved = {}

    def __enter__(self):
        g = globals()
        for k, v in self.kw.items():
            self.saved[k] = g[k]
            g[k] = v
        return self

    def __exit__(self, *a):
        globals().update(self.saved)
        return False


def rows_v27(cells, doubling):
    print(f"  {'cell':15s} {'clears':>7s} {'P/F':>4s} {'expnet':>7s} "
          f"{'realnet':>7s} {'c_mean':>6s} {'c_min':>6s} {'c_max':>6s} "
          f"{'@max':>5s} {'capped':>6s} {'clr_med':>7s} {'ext':>3s} "
          f"{'frz':>3s} {'chl':>3s} {'scav_kg':>9s} {'m_left':>6s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            en = geo_s_eff(p, tier, doubling) * cell_growth(tier_cold(tier), doubling)
            print(f"  {tier:8s} {p:4.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['clears']:3d}/{N_RUNS} {'PASS' if c['passed'] else 'FAIL':>4s} "
                  f"{en:7.5f} {c['net_realised']:7.5f} {c['center_mean']:6.4f} "
                  f"{c['center_min']:6.4f} {c['center_max']:6.4f} "
                  f"{100*c['frac_at_max']:4.0f}% {100*c['frac_capped']:5.1f}% "
                  f"{_fmt(c['clear_med']):>7s} {c['outcomes'].get('extinct', 0):3d} "
                  f"{c['freeze_cross']:3d} {c['chlorite']:3d} {c['scav_mean']:9.3e} "
                  f"{100*c['m_left_mean']:5.1f}%")


def grid_line(label, cells):
    allp = sum(1 for c in cells.values() if c["passed"])
    s = " ".join(f"{c['clears']:3d}" for c in cells.values())
    return f"  {label:34s} {allp:2d}/12 pass | clears (b.5 b.75 b1 b1.5 m.. s..): {s}"


def center_map_table(doubling, title):
    print(title)
    colds = (0.25, 0.50, 0.75, 0.95, 1.00)
    print("    cell            " + "".join(f"  cold {c:4.2f}" for c in colds))
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            row = f"    {tier:8s} {p:4.2f}%  "
            for cold in colds:
                cen, net, hit = adaptive_center(tier, p, cold, doubling)
                row += f"  {cen:6.4f}{'^' if hit else ' '}  "
            print(row)
    print("    ^ = hit ADAPTIVE_CENTER_MAX (expected net still < target)")


def rows_v29(cells, doubling):
    print(f"  {'cell':15s} {'clears':>7s} {'P/F':>4s} {'expnet':>7s} {'realnet':>7s} "
          f"{'center':>6s} {'@max':>4s} {'clr_med':>7s} {'ext':>3s} {'tmo':>3s} "
          f"{'peak_med':>9s} {'peak_max':>9s} {'scav_kg':>9s} {'m_left':>6s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            en = geo_s_eff(p, tier, doubling) * cell_growth(tier_cold(tier), doubling)
            print(f"  {tier:8s} {p:4.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['clears']:3d}/{N_RUNS} {'PASS' if c['passed'] else 'FAIL':>4s} "
                  f"{en:7.5f} {c['net_realised']:7.5f} {c['center_mean']:6.4f} "
                  f"{100*c['frac_at_max']:3.0f}% {_fmt(c['clear_med']):>7s} "
                  f"{c['outcomes'].get('extinct', 0):3d} {c['outcomes'].get('timeout', 0):3d} "
                  f"{c['peak_med']:9.3e} {c['peak_max']:9.3e} {c['scav_mean']:9.3e} "
                  f"{100*c['m_left_mean']:5.1f}%")


def draw_rows(cells):
    print(f"  {'cell':15s} {'mean':>6s} {'median':>6s} {'p5':>6s} {'p95':>6s} "
          f"{'min':>6s} {'>0.98':>6s} {'draws':>9s}")
    for tier in STRESS_TIERS:
        for p in PERCH_LEVELS:
            c = cells[(tier, p)]
            print(f"  {tier:8s} {p:4.2f}%{'*' if p not in BRIEF_PERCH_LEVELS else ' '} "
                  f"{c['mean_draw']:6.4f} {c['draw_med']:6.4f} {c['draw_p5']:6.4f} "
                  f"{c['draw_p95']:6.4f} {c['worst_draw']:6.4f} "
                  f"{100*c['draw_above_knee']:5.1f}% {c['n_draws']:9d}")


def solved_d(rate):
    d = solve_doubling_sols(200, scav_rate=rate)
    return d, math.ceil(d * 100.0 - 1e-9) / 100.0


TRAJ_VOLUME_MULTIPLIER = 10.0
TRAJ_CONTINUOUS_P_KG_PER_SOL = 1.0e25
TRAJ_SOLS = (0, 50, 100, 200, 500)
TRAJ_HORIZON = 1000


def trajectory_diag(tier, perch, label, p_import=None, vol_mult=1.0):
    with with_globals(ACCESSIBLE_REGOLITH_M3=ACCESSIBLE_REGOLITH_M3 * vol_mult):
        master = random.Random(SEED)
        seeds = [master.getrandbits(64) for _ in range(N_RUNS)]
        trajs, ges, rsn = [], [], []
        for sd in seeds:
            r = run_once(random.Random(sd), perch, tier, stop_on_targets=False,
                         max_sols=TRAJ_HORIZON, p_import=p_import, record_traj=True)
            trajs.append([INOCULUM] + [t[1] for t in r["traj"]])
            ges.append(r["growth_end"])
            rsn.append(r["growth_reason"])
        cell = run_cell(tier, perch, p_import=p_import)
        mp0 = mineral_p0_kg()
    med = []
    for i in range(TRAJ_HORIZON + 1):
        col = sorted(t[i] for t in trajs)
        med.append(col[len(col) // 2])
    pk = max(range(len(med)), key=lambda i: med[i])
    clipped = sorted(g for g in ges if g is not None)
    rc = Counter(x for x in rsn if x is not None)
    ge_txt = (f"median {clipped[len(clipped)//2]} ({len(clipped)}/{N_RUNS} clipped, limit {_reasons(rc)})"
              if clipped else f"never (0/{N_RUNS} clipped in {TRAJ_HORIZON} sols)")
    pts = "  ".join(f"sol {t}: {med[t]:.3e}" for t in TRAJ_SOLS)
    print(f"  {tier} {perch:.2f}% [{label}] mineral P {mp0:.3e} kg")
    print(f"    median cells  {pts}")
    print(f"    peak {med[pk]:.3e} at sol {pk}; growth stops {ge_txt}; clears "
          f"{cell['clears']}/{N_RUNS}, median clear sol {_fmt(cell['clear_med'])}, "
          f"extinct {cell['outcomes'].get('extinct', 0)}")
'''


def _load_v29_reference():
    """Build the inlined v2.9 code as an isolated namespace (no file import)."""
    import types
    mod = types.ModuleType("_v29_reference")
    exec(compile(_V29_REFERENCE_SOURCE, "<inlined v2.9 reference>", "exec"), mod.__dict__)
    return mod


def main():
    print("DB-MARS-CONV-006 v2.11 CANDIDATE ensemble (pending Craig landing; ox10 remains scored A)")
    print(f"Runs/cell {N_RUNS}, seed {SEED}; habitat {HABITAT_ENABLED} {HABITAT_MODE}; "
          f"adaptive center {ADAPTIVE_SURVIVAL} [{ADAPTIVE_CENTER_MIN}, {ADAPTIVE_CENTER_MAX}]")
    print(f"Override {OX_PERCELL_OVERRIDE} (v2.11 CANDIDATE: lowest ox_sweep12 values "
          f"that cleared 240/240 at seed 42 on the four binding cells, as lab-screen "
          f"survival TARGETS not measured values; moderate 1.50% keeps the ISS "
          f"detection-floor 1.0); "
          f"OXIDATIVE_FACTOR {OXIDATIVE_FACTOR}")
    print(f"N import {N_IMPORT_KG_PER_SOL:.4e}, recycle {RECYCLE_FRACTION:.0%}, P import "
          f"fallback {P_IMPORT_REALISTIC_MAX_KG_PER_SOL:.4e}; floor {HARD_REDUCTASE_FLOOR:.0%} "
          f"locked; gate {FREEZE_HARD_GATE} '{FREEZE_CONTROL_MODE}'")
    print()
    print("Doubling-time solve (v2.5 criterion, baseline-driven):")
    solved = {}
    for rate in SCAV_RATE_OPTIONS:
        d, dr = solved_d(rate)
        solved[rate] = dr
        chk = deterministic_run(dr, scav_rate=rate, max_sols=400)
        print(f"  rate {rate:.1e}: D_min {d:.6f} -> {dr:.2f} sols; growth_end "
              f"{chk['growth_end']} ({chk['reason']}), geo O2 target sol {chk['o2_target_sol']}")
    print(f"  DOUBLING_SOLS constant = {DOUBLING_SOLS}")
    print()
    D5 = solved[5.0e-3]
    assert abs(D5 - DOUBLING_SOLS) < 1e-9, (D5, DOUBLING_SOLS)
    D1 = 8.82
    A = run_config("A COMBINED (v2.11 CANDIDATE)", 5.0e-3, D5, True)
    print("A survival draw distribution:")
    draw_rows(A)
    print()
    B = run_config("B ablation: scav 1e-3, override kept", 1.0e-3, D1, True)
    C = run_config("C ablation: ox 0.97, scav 5e-3 kept", 5.0e-3, D5, False)
    R = run_config("REF v2.9 (neither lever)", 1.0e-3, D1, False)
    for lab, v in (("A-low", OX_MODERATE_RANGE_LOW), ("A-high", OX_MODERATE_RANGE_HIGH)):
        with with_globals(OX_PERCELL_OVERRIDE={("moderate", 1.50): v}):
            run_config(f"{lab} range end ox {v}, scav 5e-3", 5.0e-3, D5, True)
    v29 = _load_v29_reference()
    ref = v29.run_ensemble("v29")
    diff = sum(1 for k in R for ra, rb in zip(R[k]["runs"], ref[k]["runs"])
               if (ra["sol"], ra["outcome"], ra["o2"], ra["units"], ra["scav_total"]) !=
               (rb["sol"], rb["outcome"], rb["o2"], rb["units"], rb["scav_total"]))
    print(f"CONTROL: REF vs v2.9 module bit-exact differing runs {diff}/{12*N_RUNS} -> "
          f"{'REPRODUCES v2.9' if diff == 0 else 'MISMATCH'}")
    print()
    print("Summary grid lines:")
    for lab, c in (("A v2.11 CANDIDATE", A), ("B scav 1e-3 + ox", B), ("C scav 5e-3 only", C),
                   ("REF v2.9", R)):
        print(grid_line(lab, c))
    print()
    e2 = run_ensemble("E2", control="off")
    e3 = run_ensemble("E3", control="off", o2_first=True)
    ch = sum(1 for k in A if (A[k]["passed"] != e3[k]["passed"]) or (e2[k]["passed"] != e3[k]["passed"]))
    print(f"CO2 ordering check on A config: cells changed {ch}/12; E3 clears frozen "
          f"{sum(c['freeze_cross_on_clear'] for c in e3.values())}")
    e4 = run_ensemble("E4", p_import=P_IMPORT_REALISTIC_MAX_KG_PER_SOL)
    d14 = sum(1 for k in A for ra, rb in zip(A[k]["runs"], e4[k]["runs"]) if ra["ok"] != rb["ok"])
    print(grid_line("E4 P import fallback", e4))
    print(f"  runs whose pass/fail differs from A: {d14}/{12*N_RUNS}")
    e5 = run_ensemble("E5", control="vent")
    print(grid_line("E5 vent mode", e5))
    print(f"  freeze crossings {sum(c['freeze_cross'] for c in e5.values())}")
    print()
    hist = run_chlorite_demo()
    print(f"Chlorite demo: after 10 sols {hist[-1][2]:.1%} dead.")
    for tier in STRESS_TIERS:
        r, a, m, tot, c = proteome_levels(STRESS_FACTOR[tier], tier_prot_cold(tier))
        print(f"  {tier:9s} reductase {r:.2f} total_het {tot:.4f}")
    allp = all(c["passed"] for c in A.values()) and sum(c["freeze_cross"] for c in A.values()) == 0
    print(f"ALL GATES (A v2.11 CANDIDATE): {'PASS' if allp else 'FAIL'}")
    print()
    run_lattice_horizon()


if __name__ == "__main__":
    main()
