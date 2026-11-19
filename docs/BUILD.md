# BUILD.md — 25 mm cell, disc + release coil

This is the handoff page. Everything below is buildable from this repo alone.
Design owner: Craig. Started Nov/Dec 2025. Status: clean core swap, 2026-09-10.
Thermal revision 2026-11-06: parallel-strand coil for continuous duty.
Residual-hold hardening 2026-11-19: SmCo path, compliant pole tips, passive detent + minimum engagement depth.
Earth-optimized 2026-11-19: Mars-derived improvements folded in as the new baseline — SmCo default, PP pulse caps, PTFE wiper, mechanical lip capture, 36–48 V pulse bank, thermal governor. Rad-hardening and boost stage dropped (Earth-only).

## What you're building

One 25 mm cube. Hold is a small samarium-cobalt disc. Coil around that disc is
the release pulse only. Driver: DRV8871 on a 12 V rail, 3.3 V logic on a
XIAO RP2040. Pulse bank: 36–48 V polypropylene film caps charged off the 12 V
bus. Pocket stays Ø8.2 × 4.0 mm.

The old 120-turn / 5 V / 28.8 N numbers are retired. The 2026-09-09
Nd+Alnico flip stack on this cell is superseded. Do not build those.
NdFeB is not the default magnet anymore — SmCo 2:17 is. See §1.

**2026-11-06 addition:** if you are running the 1.25 A × 10 min continuous
soak (T4), wind the coil as **2–4× AWG 36 in parallel** or 1× AWG 30.
Single-strand fine wire is pulse-only — sim showed 444 °C at 1.25 A.
See `docs/COIL_REVISION.md` Rev 2026-11-06.

**2026-11-19 addition:** residual-hold hardening stack — SmCo 2:17 default
magnet, 0.2–0.4 mm compliant pole tip, passive mechanical detent, PTFE wiper
lip on the ridge. See `docs/DESIGN.md` §6–§7 and `docs/COIL_REVISION.md`
SmCo section.

## 1. Magnet: SmCo 2:17 is the default

NdFeB N42/N52 is retired as the primary path. Two reasons from the Mars
sims that apply on Earth too: NdFeB's coercivity is thermally fragile —
a hot garage or a 80 °C soak can push it toward the edge of reliable
release — and its residual drops with temperature while SmCo's barely moves.
SmCo 2:17 (H_c ~720 kA/m, Br tempco -0.03%/C) is stable from minus one
hundred twenty-five to plus three hundred fifty Celsius, which covers every
Earth environment you'll ever put this cell in.

- Stack: SmCo 2:17 Ø6.0 × 2.0–3.0 mm, axial, NiCuNi plating
- No NdFeB anywhere in the magnetic circuit
- Residual at 25 °C, zero point one millimeter gap: ~5.7 N clean;
  ~4.1 N is the SmCo number at the same gap (lower Br than NdFeB, but
  the detent carries the load anyway — see §3)
- If you must prototype with NdFeB for cost, treat it as a disposable
  test article, not a shippable build

## 2. Pulse bank: 36–48 V, not the 12 V rail

The baseline 0.292 T reverse-pulse threshold does NOT clear SmCo 2:17.
SmCo's operating point in a tight magnetic circuit sits at roughly zero point
six to zero point eight Tesla. Nulling that takes a reverse field of zero
point five to zero point eight Tesla.

| Pulse bank | Effective B in magnet volume (10–30% coupling) |
| :--- | :--- |
| 12 V DRV8871 (old Earth rail) | 0.19–0.33 T — cannot clear SmCo |
| 30 V cap dump | 0.47–0.81 T — borderline |
| 36 V cap dump | 0.56–0.98 T — clears at good coupling |
| 48 V cap dump | 0.75–1.30 T — clears with margin at all couplings |

**Specification: 36–48 V polypropylene film capacitor bank, 100 V rating,
potted, charged by a 12→48 V boost stage off the 12 V bus** (or from an
existing 48 V supply if your bench has one — the boost is only mandatory
when 48 V isn't already present). The 12 V rail stays for logic and driver
VM only. Scope the actual release on first article before freezing width.

### 2b. Pulse-bank capacitors

Energy target: 50 mJ at 48 V → 43 µF minimum.

| Dielectric | Capacitance retained (cold) | Spec action |
| :--- | :--- | :--- |
| X7R ceramic | ~25% | REJECT — ESR rises 5–10×, pulse current
  starves, cap body self-heats |
| C0G/NP0 ceramic | ~97% | Viable but volume explodes at 48 V rating |
| PET film | ~90% | Marginal |
| **PP film** | **~95%** | **SPEC** — best balance: stable C,
  2–3× ESR (acceptable for a 1 ms pulse), self-healing,
  rated -55 to +105 °C continuous |

**Specification: 440 µF PP film bank (2× oversize for derating + ESR
margin), 100 V rating, potted.** Navy SD-18 derates film caps to 55% of
rated voltage below 0 °C — at -40 °C a 63 V cap sees an effective ~35 V
ceiling. Use 100 V PP parts and you clear 48 V charge with margin at any
Earth ambient.

## 3. Detent minimum engagement depth

Sim (2026-11-18) sized the detent groove at 0.30 mm deep with a matching
ridge on the mating plate. Full engagement gives ~8 950 N shear — 200× the
40 N structural gate. Half-seated gives roughly a quarter, ~2 200 N, which
still clears 40 N but leaves no margin for wear or debris.

**Specification:**

- Groove depth: 0.30 mm (target). Ridge height: 0.30 mm.
- **Minimum engagement depth: 0.15 mm.** Below this, the detent is not
  load-bearing — magnetic residual and pole-tip compression carry the cell,
  which is the soft spot this hardening stack exists to eliminate.
- **Target engagement: 0.25–0.30 mm** (83–100 % of groove depth).
- Measure engagement with a depth gauge or by sectioning a witness coupon
  after the first dock. Do not rely on feel.
- If engagement reads below 0.15 mm after seating, re-machine or re-bond.
  Do not shim it in place — a shim under the ridge recreates the gap the
  detent was meant to close.
- Wear allowance: the carbide shim wears ~0.5 µm/cycle. At 2 000 cycles
  that is 1.0 mm, which would consume the entire 0.30 mm groove. The 100 µm
  wear budget from the T5 criterion still applies to the shim face; the
  detent groove sits outside that wear path only if the ridge contacts the
  groove wall, not the shim face. Verify ridge-to-groove-wall contact in
  the CAD before cutting.

## 4. PTFE wiper lip on the detent ridge

Shop dust is the Earth analog of Martian silt — finer than you think,
electrostatically clingy, and it packs grooves. A bare 0.30 mm groove will
silt up over repeated dock cycles.

- Add a thin PTFE lip (0.1–0.2 mm) on the detent ridge. It sweeps the
  groove clean on every undock.
- PTFE preferred over PEEK: both survive any Earth ambient, but PTFE's
  higher wear coefficient is offset by self-renewal via transfer film —
  over 2 000 cycles at 2 N contact the lip loses ~0.1% of its volume, and
  the transferred PTFE may lubricate the groove rather than just clean it.
  PEEK wears less but can stiffen and crack with thermal cycling.
- Lip must not add more than 0.05 mm to the ridge height or it recreates
  the gap the detent closes. Verify in CAD.
- Groove entry edge: 0.10 mm chamfer at 45° so dust arriving off-angle is
  deflected outward. No added part, zero wear — but alone it only handles
  entry-path dust.
- **Hybrid spec:** chamfered groove entry PLUS PTFE lip. Chamfer handles
  geometry; lip handles the abrasive sweep.

### 4b. PTFE lip attachment

Untreated PTFE will not bond — surface energy ~18 mN/m. Sodium-naphthalene
etching raises it to 60–70 mN/m and gives epoxy lap-shear of 10–20 MPa, but
the etched layer is only 10–50 nm deep and fails by stripping under thermal
cycling due to CTE mismatch (PTFE ~100+ ppm/K vs epoxy ~50–70). Cryo-rated
epoxies help but don't eliminate the risk over 2 000 cycles.

**Specification: mechanically captured PTFE lip — molded or swaged into the
ridge as one piece, zero adhesive.** If bonding is unavoidable, sodium-etch
the PTFE, use a low-outgassing epoxy, and roughen before etching. Bond
within 4 hours of etch; the activated surface re-contaminates.

## 5. Pole tip

0.2–0.4 mm non-magnetic silicone or spring-steel washer bonded to the latch
face. At 188 kN/m it takes 9.4 N to compress a 50-micron dust grain — more
than double the magnetic residual. Dust stops being a cliff and becomes
something the silicone eats. Two degrees of tilt, same story. This is
hardening lever 2 from `docs/DESIGN.md` §6 and it stays.

## 6. Coil drive and thermal governor

- Default: pulse-only. The coil is a release actuator, not a holding
  magnet — size it for the cancel peak, not for holding force.
- **Thermal governor (firmware):** refuse continuous soak unless plate temp
  (TMP117 or NTC near coil) is under 40 °C. This was a Mars rule but it's
  good hygiene on Earth too — the 444 °C T4 failure mode doesn't need a
  vacuum to happen, just still air and a single-strand wind.
- If a continuous load is ever required, duty-cycle it — e.g. 1.25 A for
  30 s, off 90 s — and log plate temp.
- Parallel-strand wind (2–4× AWG 36 or 1× AWG 30) still required for any
  sustained pulse train or T4 soak.
- Release: the IN1/IN2 polarity that bucks the disc, for the measured
  width, then both LOW. Opposite polarity kept in firmware so you can find
  which way drops the plate. Start in the 50–200 ms band. Stretch only
  until measured current has peaked.

## 7. Driver and MCU (Earth-optimized)

- Driver: DRV8871, VM = 12 V, ILIM set near 3.0 A (3.6 A is the peak
  rating). Commercial part is fine on Earth — no radiation concern.
- MCU: XIAO RP2040, 3.3 V logic only — never put 12 V on U1 VCC. The
  space-grade MSP430FR5969-SP from the Mars variant is overkill here;
  keep it for the Mars build only.
- No aluminum shielding, no rad-tolerant FET swap. Earth GCR is ~0.25 rad/day
  and your TID budget is effectively infinite on a bench.

## 8. Parts list

- Magnet: SmCo 2:17 Ø6.0 × 2.0–3.0 mm, axial, NiCuNi plating
- Wire: AWG 36 first (parallel strands for continuous duty), 28–30 AWG
  backup — count turns, publish the real count
- Pulse bank: 440 µF PP film, 100 V, potted (2× 220 µF is an acceptable
  split)
- Boost stage (if no 48 V supply): 12→48 V, ~8 g, 90% efficiency — or
  skip if your bench rail already provides 36–48 V
- Driver: DRV8871, VM = 12 V
- MCU: XIAO RP2040, 3.3 V logic
- Pocket: Ø8.2 × 4.0 mm, unchanged — see `cad/voxel_cell.scad`
- Latch shim: carbide or 440C, Ø6.0 × 0.50 mm, clip-in (wear item, swap
  at 100 µm)
- Pole tip: 0.2–0.4 mm silicone or spring-steel washer, bonded to latch face
- Detent: 0.30 mm deep annular groove in shim + matching ridge on mating
  plate, PTFE lip mechanically captured on ridge, 0.10 mm 45° chamfer on
  groove entry
- Temp sensor: TMP117 or NTC near coil for the thermal governor

## 9. Wind and test sequence

1. Wind around the disc. Count turns. If building for T4 continuous soak,
   wind parallel strands.
2. Measure DC resistance (total across strands if parallel).
3. Step 12 V and capture time-to-peak current (or L).
4. Charge the pulse bank to 36–48 V. Fire the real pulse; record peak
   current. Confirm the cell releases — scope it, don't assume.
5. Measure ON force (coil off) and OFF force (after release) on a fixture,
   same gap, same plate.
6. Find I_release min that drops the mate. Both polarities. Then 80%
   margin.
7. Log coil + driver temperature after N pulses at your planned cadence.
   T4 pass: < 85 °C after 1.25 A × 10 min, 25 °C ambient, no airflow.
8. Seat carbide shim. Verify ≤ 0.10 mm clearance. Log wear depth at 2 000
   cycles.
9. Bond pole tip, machine detent groove + ridge, capture PTFE lip,
   verify engagement depth ≥ 0.15 mm (target 0.25–0.30 mm). Section a
   witness coupon after the first dock.
10. Run the thermal governor test: attempt a continuous soak with plate temp
    above 40 °C and confirm firmware refuses.

## 10. Success criteria

Nothing is a measured latch until disc, turns, R, peak I, **I_release**, ON N, and OFF N are published. Fill in `docs/MEASUREMENT_CARD.md`.
T4 thermal: coil + driver under 85 °C after 1.25 A × 10 min.
T5 cycle: shim wear ≤ 100 µm over 2 000 cycles; swap shim if clearance opens past 0.15 mm.
Detent: engagement ≥ 0.15 mm measured; ridge-to-groove-wall contact confirmed in CAD.
Pulse bank: 36–48 V confirmed at the cap terminals under load, PP dielectric,
100 V rating.
PTFE lip: mechanically captured, no adhesive; lip height adds ≤ 0.05 mm to ridge.
Thermal governor: refuses soak above 40 °C plate temp.

## 11. Files in this repo

- `docs/COIL_REVISION.md` — why the first pass failed, disc + release lock, parallel-strand thermal fix, SmCo path
- `docs/DESIGN.md` — architecture, version ladder, residual-hold hardening §6, Mars variant §7
- `docs/MARS_VARIANT.md` — the space-hardened build (rad-tolerant MCU, 3 mm Al shield, boost stage mandatory). Do not mix Mars and Earth numbers.
- `docs/PHASE0.md` — the separate 20 mm face (do not mix these numbers in)
- `docs/MEASUREMENT_CARD.md` — blank until filled; includes SmCo soak step
- `cad/voxel_cell.scad` — pocket geometry, do not edit for this lock
- `firmware/pulse_driver.cpp` — pulse routine + thermal governor
- `bom/bom_netlist.txt` — BOM / netlist
- `tools/force_sweep.py` — paper force sweep (warning only)

## 12. Ask

If you build it, open an issue with your measured numbers. Questions go
there too — the design is coherent on paper; the first snag is where it
gets real.
