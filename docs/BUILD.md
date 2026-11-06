# BUILD.md — 25 mm cell, disc + release coil

This is the handoff page. Everything below is buildable from this repo alone.
Design owner: Craig. Started Nov/Dec 2025. Status: clean core swap, 2026-09-10.
Thermal revision 2026-11-06: parallel-strand coil for continuous duty.

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

## Parts

- Disc: Ø6.0 × 2.0–3.0 mm NdFeB N42/N52 (drop to Ø6×2 or Ø5×2 if 3 A cannot release)
- Wire: AWG 36 first (parallel strands for continuous duty), 28–30 AWG backup — count turns, publish the real count
- Driver: DRV8871, VM = 12 V, ILIM set near 3.0 A (3.6 A is the peak rating)
- MCU: XIAO RP2040, 3.3 V logic only — never put 12 V on U1 VCC
- Pocket: Ø8.2 × 4.0 mm, unchanged — see `cad/voxel_cell.scad`
- Latch shim: carbide or 440C, Ø6.0 × 0.50 mm, clip-in (wear item, swap at 100 µm)

## Wind

1. Wind around the disc. Count turns. If building for T4 continuous soak, wind parallel strands.
2. Measure DC resistance (total across strands if parallel).
3. Step 12 V and capture time-to-peak current (or L).
4. Fire the real pulse; record peak current.
5. Measure ON force (coil off) and OFF force (after release) on a fixture, same gap, same plate.
6. Find I_release min that drops the mate. Both polarities. Then 80 % margin.
7. Log coil + driver temperature after N pulses at your planned cadence. T4 pass: < 85 °C after 1.25 A × 10 min, 25 °C ambient, no airflow.
8. Seat carbide shim. Verify ≤ 0.10 mm clearance. Log wear depth at 2 000 cycles.

Size the coil for the cancel peak, not for holding force. The disc holds.

## Pulse

- Release: the IN1/IN2 polarity that bucks the disc, for the measured width, then both LOW.
- Opposite polarity kept in firmware so you can find which way drops the plate.
- Start in the 50–200 ms band. Stretch only until measured current has peaked.
- Never run the coil continuous **unless** it is a parallel-strand wind rated for T4.

## Success criteria

Nothing is a measured latch until disc, turns, R, peak I, **I_release**, ON N, and OFF N are published. Fill in `docs/MEASUREMENT_CARD.md`.
T4 thermal: coil + driver under 85 °C after 1.25 A × 10 min.
T5 cycle: shim wear ≤ 100 µm over 2 000 cycles; swap shim if clearance opens past 0.15 mm.

## Files in this repo

- `docs/COIL_REVISION.md` — why the first pass failed, disc + release lock, parallel-strand thermal fix
- `docs/DESIGN.md` — architecture and version ladder
- `docs/PHASE0.md` — the separate 20 mm face (do not mix these numbers in)
- `cad/voxel_cell.scad` — pocket geometry, do not edit for this lock
- `firmware/pulse_driver.cpp` — pulse routine
- `bom/bom_netlist.txt` — BOM / netlist
- `tools/force_sweep.py` — paper force sweep (warning only)

## Ask

If you build it, open an issue with your measured numbers. Questions go
there too — the design is coherent on paper; the first snag is where it
gets real.
