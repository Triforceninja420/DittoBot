# BUILD.md — 25 mm cell, option A

This is the handoff page. Everything below is buildable from this repo alone.
Design owner: Craig. Started Nov/Dec 2025. Status: option A locked, 2026-09-09.

## What you're building

One 25 mm cube with a switchable electro-permanent magnet on each face.
Magnet: Ø6.0 mm × 4.0 mm stack (NdFeB N52 + Alnico 5), coil in the 1.1 mm
annulus. Driver: DRV8871 on a 12 V rail, 3.3 V logic on a XIAO RP2040.

The old 120-turn / 5 V / 28.8 N numbers are retired. Do not build them.

## Parts

- Magnet stack: Ø6.0 × 4.0 mm, NdFeB N52 + Alnico 5 (split height as wound)
- Wire: AWG 36 enamel, 160–180 turns — count them, publish the real count
- Driver: DRV8871, VM = 12 V, ILIM set near 3.0 A (3.6 A is the peak rating)
- MCU: XIAO RP2040, 3.3 V logic only — never put 12 V on U1 VCC
- Pocket: Ø8.2 × 4.0 mm, unchanged — see `openscad`

## Wind

1. Wind 160–180 turns of AWG 36 in the 1.1 mm annulus.
2. Measure DC resistance.
3. Step 12 V and capture time-to-peak current (or L).
4. Fire the real pulse; record peak current.
5. Measure ON force and OFF force on a fixture, same gap, same mating plate.
6. Log coil + driver temperature after N pulses at your planned cadence.

Target if the pulse peaks: 170 t × 3.0 A = 510 AT ≈ 128 kA/m — clears
Alnico 5's \~50 kA/m coercivity. If it doesn't peak, the wind or the ILIM
is the problem, not the whiteboard.

## Pulse

- Latch: IN1 HIGH, IN2 LOW for the measured width, then both LOW.
- Release: IN1 LOW, IN2 HIGH, same width, then both LOW.
- Start at 25 ms. Stretch only until measured current has peaked.
- Never run the coil continuous.

## Success criteria

Nothing is a measured latch until turns, R, peak I, ON N, and OFF N are
published. Fill in `MEASUREMENT_CARD.md` with your numbers.

## Files in this repo

- `COIL_REVISION.md` — why the first pass failed, option A lock
- `DESIGN.md` — architecture and version ladder
- `PHASE0.md` — the separate 20 mm face (do not mix these numbers in)
- `openscad` — pocket geometry, do not edit for this lock
- `cpp` — pulse routine
- `text` — BOM / netlist
- `python` — force sweep (prints the retired 8 mm numbers as a warning)

## Ask

If you build it, open an issue with your measured numbers. Questions go
there too — the design is coherent on paper; the first snag is where it
gets real.