# MARS VARIANT — 25 mm cell, residual-hold hardening + Mars adaptations

Mars-specific build of the 25 mm cell. Design owner: Craig.
Baseline: `docs/BUILD.md` (2026-11-19) + `docs/DESIGN.md` §6 hardening stack.
Mars sim: 2026-11-18. Pulse/wiper sims: 2026-11-19.
Open-question sims: 2026-11-19 (MCU, caps, lip bond, boost).
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

**Specification: Mars pulse bank is 36–48 V, polypropylene film capacitors
(see §2c), charged by a 12→48 V boost stage off the 12 V bus** (see §4b).
The 12 V rail stays for logic and driver VM only. Scope the actual release
on first article before freezing width.

### 2c. Pulse-bank capacitors (sim 2026-11-19 — RESOLVED)

Energy target: 50 mJ at 48 V → 43 µF minimum. At minus one twenty-five:

| Dielectric | Capacitance retained | Spec action |
| :--- | :--- | :--- |
| X7R ceramic | ~25% | REJECT — ESR rises 5–10×, pulse current
  starves, cap body self-heats |
| C0G/NP0 ceramic | ~97% | Viable but volume explodes at 48 V rating |
| PET film | ~90% | Marginal |
| **PP film** | **~95%** | **SPEC** — best balance: stable C,
  2–3× ESR (acceptable for a 1 ms pulse), self-healing,
  rated -55 to +105 °C continuous |

**Specification: 440 µF PP film bank (2× oversize for derating + ESR
margin), 63 V or 100 V rating, potted.** Navy SD-18 derates film caps to
55% of rated voltage below 0 °C — at -125 °C a 63 V cap sees an effective
~35 V ceiling, which still clears 48 V charge with margin if you use the
100 V rating instead. Use 100 V PP parts.

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

### 3b. PTFE lip attachment (sim 2026-11-19 — RESOLVED)

Untreated PTFE will not bond — surface energy ~18 mN/m. Sodium-naphthalene
etching raises it to 60–70 mN/m and gives epoxy lap-shear of 10–20 MPa, but
the etched layer is only 10–50 nm deep and fails by stripping at cryo due to
CTE mismatch (PTFE ~100+ ppm/K vs epoxy ~50–70). Cryo-rated epoxies
(MasterBond EP21TCHT-LO class, serviceable to 4 K) help but don't eliminate
the mismatch risk over 2 000 thermal cycles.

**Specification: mechanically captured PTFE lip — molded or swaged into the
ridge as one piece, zero adhesive.** If bonding is unavoidable, sodium-etch
the PTFE, use a cryo-rated low-outgassing epoxy, and roughen before etching.
Bond within 4 hours of etch; the activated surface re-contaminates.

### 4. Rad-hardened driver side

Magnets and 440C/carbide are ceramics and metals — radiation-hard, no
change needed. The XIAO RP2040 and DRV8871 are not.

- **MCU: MSP430FR5969-SP** (TI space-grade FRAM part). FRAM cells are
  inherently SEU-immune, SEL-immune to 72 MeV·cm²/mg at 125 °C, TID lot-
  tested to 50 krad, -55 to +105 °C, 64 KB unified memory, ~100 µA/MHz,
  0.02 µA shutdown. Nonmagnetic. ~$30–50 vs $2 000+ for true rad-hard
  LEON3 parts that draw 1 W+ — overkill for a cell.
- Mars GCR delivers ~0.25 rad/day. 50 krad unshielded = ~550 days. Behind
  3 mm Al the TID budget extends 5–10× → 5–15 year life. **Spec: 3 mm Al
  shield around the MCU, or mount it on the shadowed side of the cell.**
- DRV8871: commercial H-bridge, not rad-rated. Shield behind the same Al
  or swap for a rad-tolerant FET H-bridge (IRLZ44N class is what Phase 0
  already uses — that path is better proven for this).
- 12 V bus and pulse bank are passive; no radiation concern beyond connector
  and cap derating at low temperature (covered in §2c).

### 4b. 48 V boost stage (sim 2026-11-19 — RESOLVED)

Boosting 12→48 V at 1 W out: 1.11 W in, 111 mW loss (90% efficient).
Mass: ~8 g (shielded inductor 2 g, FETs + driver 1 g, caps 2 g, PCB 3 g).
A dedicated 48 V cell pack for even 1 Wh would mass 20 g+ — the boost is
lighter whenever a 12 V bus already exists, which it does.

**Specification: 12→48 V boost, ~8 g, 90% efficiency, thermal-folded into
the pulse-only governor so it only runs when a release is queued.**

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

## Mass budget (Mars cell, all hardening included)

| Part | Mass |
| :--- | :--- |
| SmCo magnet Ø6×2 | 1.5 g |
| Coil (parallel AWG 36) | 2.0 g |
| Carbide shim + detent groove | 1.0 g |
| Pole tip (silicone) | 0.2 g |
| PTFE lip + chamfer | 0.1 g |
| H-bridge (DRV8871 or IRLZ44N) | 0.5 g |
| MSP430FR5969-SP + 3 mm Al | 4.0 g |
| 48 V boost stage | 8.0 g |
| Pulse bank (440 µF PP, 100 V) | 3.0 g |
| TMP117 | 0.1 g |
| PCB + connectors | 5.0 g |
| Al housing (25 mm cube) | 15.0 g |
| **Total** | **40.4 g** |

Earth-baseline equivalent: ~25 g. Mars hardening adds ~15 g.

## Power budget

Idle: ~1 mW (MCU + sensor). Pulse event: 50 mJ + ~5 mJ boost overhead
= 55 mJ. At one pulse per minute that's 0.9 mW average; at one per hour,
15 µW. The cell is power-neutral at any realistic dock rate. The 1.25 A
soak is the only hot path and it is forbidden by spec §2.

## What is NOT in this file

- Phase 0 20 mm face numbers (separate file, do not mix)
- Earth-baseline NdFeB build (stays in BUILD.md)
- voxel_cell.scad geometry (locked; Mars variant is parts and firmware,
  not pocket changes)
- Community Enhancement Suites

## Open questions

- PTFE lip bond strength after 2 000 cryo cycles with mechanical capture
  (verify in environmental chamber before flight).
- 100 V PP cap ESR at -125 °C under 1 ms pulse load (datasheet curves
  stop at -55 °C — extrapolate or test).
- Boost stage cold-start at -125 °C (inductor saturation, FET Rds(on)
  rise — may need a heater or oversized FETs).
- MSP430FR5969-SP availability and lead time for quantity.
