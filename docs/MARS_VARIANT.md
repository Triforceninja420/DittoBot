# MARS VARIANT — 25 mm cell, residual-hold hardening + Mars / space adaptations

Mars-specific build of the 25 mm cell. Design owner: Craig.  
Baseline now includes the 2026-11-19 upgrades (see BASELINE_UPGRADES.md).  
Status: paper only, no hardware. Open questions from earlier sims are closed at the paper level below.

The Mars variant is the natural space-hardened path. It inherits the full current baseline so the same cell handles Mars surface and pure space without a third variant.

## Inherited baseline (now standard)
- Nd disc Ø6.0×2–3 mm
- Axial pin + receptacle hard-lock
- Full cavity potting
- PTFE lip + conformal coating
- Pulse-only + thermal governor
- 36–48 V PP film pulse bank

## Mars / space additions (paper-closed)
- Rad-hardened MCU path (MSP430FR5969-SP class + shielding) remains the differentiator for long-duration radiation.
- PTFE lip is mechanically captured (no adhesive bond required at cryo).
- Pulse bank uses 100 V PP film parts for cold derating margin.
- Boost stage is thermal-folded into the existing governor.

All prior open questions (lip bond, cap ESR extrapolation, boost cold-start, MCU availability) are treated as implementation details for the first article, not blockers for the paper design. The inheritance path is complete.

## Detailed speculative extensions
See the [mars/](mars/) folder for the full DB-MARS series (seed bots that self-replicate from regolith, CO₂-to-O₂ converter chains, density/power governors, and the engineered cyanobacteria swarm DB-MARS-CONV-006). Those documents explore long-term greening timelines in simulation. They do not change the locked 25 mm geometry or Phase 0.

See BASELINE_UPGRADES.md and PAPER_STATUS.md.
