# Gate 5 — Superseded Dual-Cam Release (archived)

**Status:** Historical. Documents the retired dual-cam Gate 5 release target and what
replaced it. This file records only what the repository and its history show; it does
not introduce new rationale. See citations at the end.

## What Gate 5 was

Gate 5 was the Phase 0 face **release** gate. In the dual-cam era it was expressed as a
net release force target of **+65.7 N**, produced by dual cams. Cam-era figures recorded
in the repo: Ø16.05 mm cam bore, Hertzian contact ~35.4 MPa, wear ~0.19 µm. These
numbers appear in `docs/PHASE0.md` (archived there as cam-era values that "do not apply
to the current build") and in the handoff log `retired/CHANGES.md`.

## Why it was superseded

Per `retired/CHANGES.md` (Issue 1) and `docs/OPTION_A_RELEASE_SPEC.md`: the Ø16.05 mm
dual cams cannot fit the 20 mm face with ≥ 0.5 mm clearance. Ø16.05 / Ø12.05 / Ø10.05
miss by about 12.95 / 8.12 / 5.71 mm against the backing disc, and the largest feasible
cam radius in a full-layout search is about 1.9 mm (2.66 mm absolute ceiling) — too
small to carry the old Gate 5. The face size had been committed at 20 mm on 2026-11-23
(previously 30 mm).

## What replaced it

Gate 5 was **reframed as a retention spec** (authorized by Craig as a lock change, not a
sim tweak): the magnet pull must be strong enough to survive launch shock and handling,
expressed as a holding force rather than a cam release force.

- **F_hold ≥ m × N × 9.81 × SF = 0.0092 kg × 10 × 9.81 × 2 = 1.805 N → ≥ 1.8 N.**
- The old "+65.7 N via dual-cam" target is marked superseded (2026-11-23b), not deleted.
- Current Phase 0 release is the **Option A sliding-pin architecture**: magnet-pull
  retention (≥ 1.8 N), a single Ø2.0 mm sliding pin (3.0 mm travel, Ø2.05 bore), no cams
  on the face. It is defined in `docs/OPTION_A_RELEASE_SPEC.md`.
- Cams are deferred to Option A / the 25 mm cell.

The current locked Phase 0 baseline is summarized in `docs/LOCKS.md` and `docs/PHASE0.md`.

## Source commits (repository history)

- `b1460bf` — "Add Option A release spec; reframe 25mm M4/M8 bars off retired cam
  numbers" (introduced `docs/OPTION_A_RELEASE_SPEC.md`, which reframes Gate 5 as a
  retention spec).
- `815e198`, `cf6aeee`, `bbae8ee` — doc sweep that removed the dual-cam / +65.7 N
  numbers from the active specs and retained the cam-era references only in `retired/`
  and `phase0/retired/`; `docs/PHASE0.md` rewritten for the Option A sliding-pin release.
- `retired/CHANGES.md` — dated handoff log (rev 2026-11-23b) that recorded the Gate 5
  reframe (1.805 N → ≥ 1.8 N) and listed `docs/GATE5_SUPERSEDED.md` as a file to add.

This file is that archive entry.
