# MARS VARIANT — 25 mm cell, residual-hold hardening + Mars adaptations

Mars-specific build of the 25 mm cell. Design owner: Craig.
Baseline: `docs/BUILD.md` (2026-11-19) + `docs/DESIGN.md` §6 hardening stack.
Mars sim: 2026-11-18 (see conversation). Pulse/wiper sims: 2026-11-19.
Status: paper only, no hardware.

## What changes vs. baseline

Four upgrades, each addressing a failure the Mars sim surfaced.

### 1. All-SmCo magnet stack (mandatory)

Drop the NdFeB layer entirely. Below approximately minus sixty Celsius,
NdFeB coercivity collapses — it can fall under Alnico's fifty kiloamps per
meter, so the release pulse cannot flip it and the cell may not hold at all.
SmCo 2:17 (H_c ~720 kA/m, Br tempco -0.03%/C) is stable from minus one
hundred twenty-five to plus three hundred fifty Celsius.

- Stack: SmCo 2:17 Ø6.0 × 2.0–3.0 mm, axial, NiCuNi plating
- No NdFeB anywhere in the magnetic circuit on this variant
- Residual at minus one twenty-five Celsius, zero point one millimeter gap:
  ~11 N (vs NdFeB at 0 N in coercivity collapse)

### 2. Pulse-only coil drive with thermal governor

At 0.6 kPa there is no convection. The coil sheds heat only by conduction
into the face plate and radiation off it. The 1.25 A × 10 min T4 soak that
hit 444 °C on Earth in still air will cook the coil on Mars.

- Default: pulse-only. Never run the coil continuous on Mars.
- Firmware thermal governor: refuse continuous soak unless plate temp
  (TMP117 or NTC near coil) is under a set threshold (recommend 40 °C).
- If a continuous load is ever required, duty-cycle it — e.g. 1.25 A for
  30 s, off 90 s — and log plate temp. The Mars ambient is so cold that
  even 5 W of waste heat barely lifts the plate off minus sixty by radiation,
  so the risk is local hot spots in the coil, not the plate.
- Parallel-strand wind (2–4× AWG 36 or 1× AWG 30) still required for any
  sustained pulse train.

### 2b. Pulse bank voltage (sim 2026-11-19 — RESOLVED)

The baseline 0.292 T reverse-pulse threshold does NOT clear SmCo 2:17.
SmCo's operating point in a tight magnetic circuit sits at roughly zero point
six to zero point eight Tesla. Nulling that takes a reverse field of zero
point five to zero point eight Tesla.

| Pulse bank | Effective B in magnet volume (10–30% coupling) |
| :--- | :--- |
| 12 V DRV8871 (Earth cell rail) | 0.19–0.33 T — cannot clear SmCo |
| 30 V cap dump | 0.47–0.81 T — borderline |
| 36 V cap dump | 0.56–0.98 T — clears at good coupling |
| 48 V cap dump | 0.75–1.30 T — clears with margin at all couplings |

**Specification: Mars pulse bank is 36–48 V, film or ceramic capacitors
(electrolytics lose capacitance below minus forty Celsius), charged by a
boost stage off the 12 V bus.** The 12 V rail stays for logic and driver
VM only. Scope the actual release on first article before freezing width.

### 3. Detent ridge wiper lip

Martian dust runs ~1 µm and is electrostatically sticky in dry CO2. A bare
0.30 mm groove will silt up over repeated dock cycles; packed grooves are
the one failure the sim could not quantify.

- Add a thin PTFE lip (0.1–0.2 mm) bonded to the detent ridge on the mating
  plate. It sweeps the groove clean on every undock.
- PTFE preferred over PEEK: both survive minus one hundred twenty-five without
  embrittling, but PTFE's wear coefficient is higher yet it self-renews via
  transfer film — over 2 000 cycles at 2 N contact the lip loses ~0.1% of
  its volume, and the transferred PTFE may lubricate the groove rather than
  just clean it. PEEK wears less but stiffens and can crack.
- Lip must not add more than 0.05 mm to the ridge height or it recreates
  the gap the detent closes. Verify in CAD.
- Groove entry edge: 0.10 mm chamfer at 45° so dust arriving off-angle is
  deflected outward. No added part, zero wear — but alone it only handles
  entry-path dust.
- **Hybrid spec (recommended):** chamfered groove entry PLUS PTFE lip.
  Chamfer handles geometry; lip handles the abrasive sweep. Belt and
  suspenders for an untested failure mode.

### 4. Rad-hardened driver side

Magnets and 440C/carbide are ceramics and metals — radiation-hard, no
change needed. The XIAO RP2040 and DRV8871 are not.

- Replace XIAO RP2040 with a rad-tolerant MCU (e.g., a rad-hard ARM
  Cortex-M0 class part or a shielded commercial part behind 2–4 mm Al).
  Single-event latchup and total ionizing dose will brown out or kill a
  commercial RP2040 over a multi-year Mars exposure.
- DRV8871: commercial H-bridge, not rad-rated. Shield behind the same Al
  or swap for a rad-tolerant FET H-bridge (IRLZ44N class is what Phase 0
  already uses — that path is better proven for this).
- 12 V bus and pulse bank are passive; no radiation concern beyond connector
  and cap derating at low temperature.

## Mars sim summary (2026-11-18)

Worst case: polar winter minus one twenty-five Celsius, dusty, 0.15 mm gap.

| Layer | Force |
| :--- | :--- |
| SmCo residual (magnetic) | ~11 N |
| Pole tip compression (magnetic assist) | ~9.4 N |
| Detent, half-seated (mechanical) | ~4 477 N |
| **Stacked floor** | **~4 497 N** |
| 40 N structural gate | PASS with 112× margin |
| NdFeB in same scenario | ~0 N — coercivity collapse |

NdFeB is not a valid Mars magnet. SmCo is not optional.

## What is NOT in this file

- Phase 0 20 mm face numbers (separate file, do not mix)
- Earth-baseline NdFeB build (stays in BUILD.md)
- voxel_cell.scad geometry (locked; Mars variant is parts and firmware,
  not pocket changes)
- Community Enhancement Suites

## Open questions

- Rad-tolerant MCU shortlist and single-event testing plan.
- Pulse-bank capacitor derating curve at minus one hundred twenty-five Celsius
  (film vs ceramic — which holds capacitance and ESR).
- PTFE lip bond strength at minus one hundred twenty-five after 2 000 cycles.
- 48 V boost stage efficiency and mass budget for a flight article.
