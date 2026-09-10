# BUILD.md — 25 mm cell, disc + release coil

This is the handoff page. Everything below is buildable from this repo alone.
Design owner: Craig. Started Nov/Dec 2025. Status: clean core swap, 2026-09-10.

## What you're building

One 25 mm cube. Hold is a small neodymium disc. Coil around that disc is
the release pulse only. Driver: DRV8871 on a 12 V rail, 3.3 V logic on a
XIAO RP2040. Pocket stays Ø8.2 × 4.0 mm.

The old 120-turn / 5 V / 28.8 N numbers are retired. The 2026-09-09
Nd+Alnico flip stack on this cell is superseded. Do not build those.

## Parts

- Disc: Ø6.0 × 2.0–3.0 mm NdFeB N42/N52 (drop to Ø6×2 or Ø5×2 if 3 A cannot release)
- Wire: AWG 36 first, 28–30 AWG backup — count turns, publish the real count
- Driver: DRV8871, VM = 12 V, ILIM set near 3.0 A (3.6 A is the peak rating)
- MCU: XIAO RP2040, 3.3 V logic only — never put 12 V on U1 VCC
- Pocket: Ø8.2 × 4.0 mm, unchanged — see `openscad`

## Wind

1. Wind around the disc. Count turns.
2. Measure DC resistance.
3. Step 12 V and capture time-to-peak current (or L).
4. Fire the real pulse; record peak current.
5. Measure ON force (coil off) and OFF force (after release) on a fixture, same gap, same plate.
6. Find I_release min that drops the mate. Both polarities. Then 80 % margin.
7. Log coil + driver temperature after N pulses at your planned cadence.

Size the coil for the cancel peak, not for holding force. The disc holds.

## Pulse

- Release: the IN1/IN2 polarity that bucks the disc, for the measured width, then both LOW.
- Opposite polarity kept in firmware so you can find which way drops the plate.
- Start in the 50–200 ms band. Stretch only until measured current has peaked.
- Never run the coil continuous.

## Success criteria

Nothing is a measured latch until disc, turns, R, peak I, **I_release**, ON N, and OFF N are published. Fill in `MEASUREMENT_CARD.md`.

## Files in this repo

- `COIL_REVISION.md` — why the first pass failed, disc + release lock
- `DESIGN.md` — architecture and version ladder
- `PHASE0.md` — the separate 20 mm face (do not mix these numbers in)
- `openscad` — pocket geometry, do not edit for this lock
- `cpp` — pulse routine
- `text` — BOM / netlist
- `python` — paper force sweep (warning only)

## Ask

If you build it, open an issue with your measured numbers. Questions go
there too — the design is coherent on paper; the first snag is where it
gets real.