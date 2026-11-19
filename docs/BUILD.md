# BUILD.md — 25 mm cell, disc + release coil

This is the handoff page. Everything below is buildable from this repo alone.
Design owner: Craig. Started Nov/Dec 2025. Status: clean core swap, 2026-09-10.
Thermal revision 2026-11-06: parallel-strand coil for continuous duty.
Residual-hold hardening 2026-11-19: SmCo path, compliant pole tips, passive detent + minimum engagement depth.

## What you're building

One 25 mm cube. Hold is a small neodymium disc. Coil around that disc is
the release pulse only. Driver: DRV8871 on a 12 V rail, 3.3 V logic on a
XIAO RP2040. Pocket stays Ø8.2 × 4.0 mm.

The old 120-turn / 5 V / 28.8 N numbers are retired. The 2026-09-09
Nd+Alnico flip stack on this cell is superseded. Do not build those.

**2026-11-06 addition:** if you are running the 1.25 A × 10 min continuous
soak (T4), wind the coil as **2–4× AWG 36 in parallel** or 1× AWG 30.
Single-strand fine wire is pulse-only — sim showed 444 °C at 1.25 A.
See `docs/COIL_REVISION.md` Rev 2026-11-06.

**2026-11-19 addition:** residual-hold hardening stack — SmCo 2:17 alternate
magnet path, 0.2–0.4 mm compliant pole tip, and a passive mechanical detent.
See `docs/DESIGN.md` §6 and `docs/COIL_REVISION.md` SmCo section.

## Parts

- Disc: Ø6.0 × 2.0–3.0 mm NdFeB N42/N52 (drop to Ø6×2 or Ø5×2 if 3 A cannot release)
- Wire: AWG 36 first (parallel strands for continuous duty), 28–30 AWG backup — count turns, publish the real count
- Driver: DRV8871, VM = 12 V, ILIM set near 3.0 A (3.6 A is the peak rating)
- MCU: XIAO RP2040, 3.3 V logic only — never put 12 V on U1 VCC
- Pocket: Ø8.2 × 4.0 mm, unchanged — see `cad/voxel_cell.scad`
- Latch shim: carbide or 440C, Ø6.0 × 0.50 mm, clip-in (wear item, swap at 100 µm)
- Pole tip (hardening lever 2): 0.2–0.4 mm non-magnetic silicone or spring-steel washer bonded to latch face. Absorbs dust and ≤2° tilt without opening the magnetic gap.
- Detent (hardening lever 3): 0.30 mm deep annular groove in the shim paired with a matching ridge on the mating plate. Magnetism captures; the detent locks.

## Wind

1. Wind around the disc. Count turns. If building for T4 continuous soak, wind parallel strands.
2. Measure DC resistance (total across strands if parallel).
3. Step 12 V and capture time-to-peak current (or L).
4. Fire the real pulse; record peak current.
5. Measure ON force (coil off) and OFF force (after release) on a fixture, same gap, same plate.
6. Find I_release min that drops the mate. Both polarities. Then 80 % margin.
7. Log coil + driver temperature after N pulses at your planned cadence. T4 pass: < 85 °C after 1.25 A × 10 min, 25 °C ambient, no airflow.
8. Seat carbide shim. Verify ≤ 0.10 mm clearance. Log wear depth at 2 000 cycles.
9. If building the hardening stack: bond pole tip, machine detent groove + ridge, verify engagement depth (see below).

Size the coil for the cancel peak, not for holding force. The disc holds.

## Pulse

- Release: the IN1/IN2 polarity that bucks the disc, for the measured width, then both LOW.
- Opposite polarity kept in firmware so you can find which way drops the plate.
- Start in the 50–200 ms band. Stretch only until measured current has peaked.
- Never run the coil continuous **unless** it is a parallel-strand wind rated for T4.
- SmCo path: the existing reverse-polarity OFF pulse (0.292 T release threshold from sim) may not clear SmCo 2:17 (H_c ~720 kA/m). Scope the release before freezing pulse width. Do not assume.

## Detent minimum engagement depth (added 2026-11-19)

Sim (2026-11-18) sized the detent groove at 0.30 mm deep with a matching
ridge on the mating plate. Full engagement gives ~8 950 N shear — 200× the
40 N structural gate. But the sim also flagged half-seated engagement as the
realistic failure: at 50 % seating you get roughly a quarter of that capacity,
~2 200 N, which still clears 40 N but leaves no margin for wear or debris.

**Specification:**

- Groove depth: 0.30 mm (target). Ridge height: 0.30 mm.
- **Minimum engagement depth: 0.15 mm.** Below this, the detent is not
  load-bearing — magnetic residual and pole-tip compression carry the cell,
  which is the soft spot this hardening stack exists to eliminate.
- **Target engagement: 0.25–0.30 mm** (83–100 % of groove depth). This is
  where the detent alone exceeds the 40 N gate with margin.
- Measure engagement with a depth gauge or by sectioning a witness coupon
  after the first dock. Do not rely on feel.
- If engagement reads below 0.15 mm after seating, re-machine or re-bond.
  Do not shim it in place — a shim under the ridge recreates the gap the
  detent was meant to close.
- Wear allowance: the carbide shim wears ~0.5 µm/cycle. At 2 000 cycles
  that is 1 000 µm = 1.0 mm, which would consume the entire 0.30 mm groove.
  The 100 µm wear budget from the T5 criterion still applies to the shim
  face; the detent groove sits outside that wear path only if the ridge
  contacts the groove wall, not the shim face. Verify ridge-to-groove-wall
  contact in the CAD before cutting.

## Success criteria

Nothing is a measured latch until disc, turns, R, peak I, **I_release**, ON N, and OFF N are published. Fill in `docs/MEASUREMENT_CARD.md`.
T4 thermal: coil + driver under 85 °C after 1.25 A × 10 min.
T5 cycle: shim wear ≤ 100 µm over 2 000 cycles; swap shim if clearance opens past 0.15 mm.
Detent: engagement ≥ 0.15 mm measured; ridge-to-groove-wall contact confirmed in CAD.
SmCo path (if built): OFF residual after 80 °C soak, same plate, same gap.

## Files in this repo

- `docs/COIL_REVISION.md` — why the first pass failed, disc + release lock, parallel-strand thermal fix, SmCo path
- `docs/DESIGN.md` — architecture, version ladder, residual-hold hardening §6
- `docs/PHASE0.md` — the separate 20 mm face (do not mix these numbers in)
- `docs/MEASUREMENT_CARD.md` — blank until filled; includes SmCo soak step
- `cad/voxel_cell.scad` — pocket geometry, do not edit for this lock
- `firmware/pulse_driver.cpp` — pulse routine
- `bom/bom_netlist.txt` — BOM / netlist
- `tools/force_sweep.py` — paper force sweep (warning only)

## Ask

If you build it, open an issue with your measured numbers. Questions go
there too — the design is coherent on paper; the first snag is where it
gets real.
