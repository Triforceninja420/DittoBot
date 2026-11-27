# Pure Exoskeleton / Strength Amplification Mode — Paper Spec

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**

Same wearable full-body shell as the flight suit, minus thruster faces. Focus is load sharing and force multiplication at joints for lifting, carrying, or sustained posture.

From the parent:

- Structure: denser cells at shoulders, elbows, hips, knees, and spine. Lighter panels on limbs and torso. Pin + detent carry external loads; soft inner layer stays.
- Power: stays on the baseline bus (no separate thruster path). Optional denser energy zone in the torso or lower back for longer duty cycles.
- Behavior: local mesh coordinates joint-level assistance. Can lock into rigid support postures or stay partially compliant. Optional soft safety skin remains active on human-proximate surfaces. See [soft-safety-skin.md](soft-safety-skin.md).
- Reconfiguration: can still compact into a dense brick for transport. No propulsion faces required.

The parent calls this a paper intermediate and a useful stepping stone before flight modules exist. Measured cards for structural cells are still the gate.

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

TBD, no pass bar set. The parent names measured structural-cell cards as the gate. No exoskeleton-specific test IDs exist in the repo.

## Assumptions

- Joint-level force multiplication, assistance behavior, and optional denser energy zoning are paper inheritance, modeled, not measured.
- No strength-amplification ratio or load rating is stated in the parent, and none is added here.

## Parent

[MODES.md — Pure Exoskeleton / Strength Amplification Mode](../../MODES.md#1-pure-exoskeleton--strength-amplification-mode-no-flight).

Paper until measured. Credit follows data.
