# OPTION_A_RELEASE_SPEC — Sliding-Pin Release Architecture

Design owned by Craig. Started 2026-11-23. Status: **defined, not fabricated**.
Credit follows measured data. Sim numbers are the bar, not the credit.

This file defines the **Option A release** shared by the Phase 0 20 mm cell and the 25 mm cell. It replaces the retired dual-cam latch (see `GATE5_SUPERSEDED.md` and `phase0/retired/`).

---

## 1. Architecture

- **Retention:** NdFeB disc magnet-pull. Zero-power hold.
- **Release:** Single axial sliding pin. Breaks magnet contact; generates no torque.
- **No cams.** Cam-torque release (65.7 N) is retired for both cell sizes.
- Gate 5 is reframed as a **retention spec**: magnet pull strong enough to survive launch shock and handling, expressed as holding force under a few g's rather than newtons of release torque.

## 2. Locked numbers (Phase 0 20 mm)

- Retention target: **1.8 N** (magnet pull, 9.2 g mass, 10 g load, 2× safety factor)
- Pin diameter: **2.0 mm**
- Pin travel: **3.0 mm**
- Pin material: hardened steel
- Receptacle depth in mating module: **≥ 2.5 mm** (pin engages 3 mm, plate eats 1 mm; 2.5 mm gives tolerance margin on both faces)
- Backing disc: 2.0 mm thick, solid back face as heat spreader behind the 8.2 mm through-hole magnet pocket
- Contact ring: r 6.25 mm; pins at r 7.45 mm, 73° / 155° / 328° (asymmetric to clear spring seats and contacts)

## 3. 25 mm cell (Option A scale-up)

- Same sliding-pin architecture, scaled.
- 25 mm release coil: ~48 turns 2-in-hand AWG 36, ~0.74 Ω, 2.4 A release current (see `HARDWARE_MAPPING.md` part 2).
- M4 OFF-force bar and M8 cycle bar in `PROTOTYPE_PLAN_25MM.md` reference this file, not the retired 65.7 N cam number.
- Cam-tip-wear bar (0.19 µm) is retired; replaced by pin-wear criterion TBD after first article.

## 4. Actuation

- **Phase 0:** manual — finger or flat tool on the pin. Metrology only.
- **Phase 1 / production:** solenoid or retraction actuator (TBD). Phase 1 interlock refuses release pulses while the joint is powered.

## 5. What this spec does not cover

- Pin wear model under 2000 cycles (pending first-article data)
- Actuator sizing for automated release
- Genderless / reversible face variants

**End of Option A release spec.**