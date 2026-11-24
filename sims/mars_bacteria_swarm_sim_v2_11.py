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
cells plus moderate 1.50%. Three binding-cell values are the lowest
tested overrides from the UNSCORED ox_sweep12 sweep that cleared 240/240
at seed 42, INOCULUM 1e12 (moderate 0.75: 0.9865, moderate 1.00: 0.9895,
severe 1.50: 0.9989). Moderate 0.50 uses the ox_sweep12 mid point 0.984,
not the low point 0.979: 0.979 cleared 240/240 at seed 42 but left
239/240 at seeds 7 (r31 timeout) and 123 (r146 extinct). These are
fitted survival TARGETS for the lab screen, not measured values. Unaided
thresholds (the 6-decimal ox values that actually cross net 1.0) are
0.978822, 0.9819, 0.986145 and 0.998349. Margin above the threshold
matters: moderate 0.75 at 0.982 cleared only 239/240 in the sweep, and
moderate 0.50 at 0.979 showed the same thin-margin pattern across seeds.
Moderate 1.50% keeps the ISS detection-floor override of 1.0
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
