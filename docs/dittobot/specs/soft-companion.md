# Soft Companion / Clothing Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Sparse, low-force lattice that drapes or wraps instead of forming a rigid shell. Aimed at continuous wear, light sensing, or gentle assistance.

From the parent:

- Structure: low packing density, compliant docking, and mandatory soft safety skin on all human-proximate faces. The 35 N human-contact interrupt stays active (existing lock in [LOCKS.md](../../LOCKS.md), not a new bar). See [soft-safety-skin.md](soft-safety-skin.md).
- Behavior: can follow body motion with minimal resistance, carry small specialized modules (sensors, low-power effectors, or light energy cells), or form temporary soft supports. Still uses the same pin hard-lock for any higher-load moments.
- Power: baseline bus only. Thermal and safe-reserve rules unchanged.

The parent status is paper. Soft-skin and interrupt behavior are already sketched in the community suites and post-2040 outlook; this mode makes the wearable sparse configuration explicit.

## Inheritance

Inherits the locked 25 mm cell core, unchanged ([DESIGN.md](../../DESIGN.md), [PAPER_STATUS.md](../../PAPER_STATUS.md)):

- 25 mm cube envelope
- Centered Ø8.2 × 4.0 mm pocket (locked)
- Nd disc Ø6.0 × 2–3 mm hold; coil around the disc, release-only (Alnico off this cell)
- DRV8871, 12 V, pulse-only
- Axial pin hard-lock
- Full cavity potting and face coatings
- XIAO RP2040, 3.3 V; 36–48 V pulse bank

This paper spec does not retune that core, change Phase 0 locks or CAD, or rewrite measurement cards. Mode-specific layers sit on top. Dock compatibility with earlier cells is preserved where the parent already says so.

## Test gates

TBD, no pass bar set. The 35 N human-contact interrupt is an existing lock, not a new mode gate. No companion-mode test IDs exist in the repo.

## Assumptions

- Sparse draping behavior, compliant docking, and continuous-wear use are paper inheritance, modeled, not measured.
- No contact-pressure, drape, or duty-cycle figures beyond the existing 35 N interrupt are stated in the parent, and none is added here.

## Parent

[MODES.md — Soft Companion / Clothing Mode](../../MODES.md#3-soft-companion--clothing-mode).

Paper until measured. Credit follows data.
