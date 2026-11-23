# DittoBot Phase 0: one 20 mm docking face, and why it has to be built next

DittoBot is a long-horizon programmable-matter project: small modules that dock to each other, lock, and pass power and data across the joint. That's the end goal. Phase 0 is a much smaller goal: **one docking face** that snaps in, locks, carries current, stays cool, lets go when told to, and does it 2 000 times. It is not a cube, a swarm, or a lattice. Until one face works on a bench, there's no point designing the rest.

Everything below is either a locked design value or a simulation result. Simulations set the bar to beat. They don't earn credit. The project's rule is that **credit follows the measurement card**, and the measurement card is still blank.

## What it is

The Phase 0 article is a 20.00 × 20.00 mm face plate, 1.0 mm thick, machined from 7075-T6 aluminium. Here's what's on it:

| Item | Phase 0 value |
| :--- | :--- |
| Face | 20.00 × 20.00 mm, 7075-T6, 1.00 mm (accept 0.80–1.20) |
| Magnet | NdFeB N52 disc, Ø6.0 × 2–3 mm, axial, centered |
| Magnet pocket | Ø8.2 through-hole, closed by a separate backing disc with a 2.0 mm solid back face |
| Coil | 40 turns of 34 AWG, ~0.75 Ω cold, driven by a TI DRV8871, pulse-only |
| Retention (gate 5) | F_hold ≥ 0.0092 kg × 10 × 9.81 × 2 = 1.805 N → **≥ 1.8 N** |
| Release | Option A: one Ø2.0 mm sliding pin, 3.0 mm travel, Ø2.05 bore at (+6.65, +3.50) |
| Latch | 3 hardened pins, Ø1.80 in Ø1.85 bores, r 7.45 mm, at 73° / 155° / 328° |
| Contacts | 6 Mill-Max 0906 pogos on a 6.25 mm-radius ring (50/110/170/230/290/350°) |
| Seating springs | 4 non-magnetic springs, **5.00 N total** (1.0 N/mm combined, 5 mm preload) |
| Capture | 1.0 mm chamfer, 1.0 × 1.0 mm side ridges, ±2.50 mm lateral |
| Mounts | 4 × Ø1.70 at (±7.00, ±7.00) |
| Module mass | 9.2 g |
| Controller | Seeed Studio XIAO RP2040 running `firmware/pulse_driver.cpp` |

Every feature on the face sits at least 0.5 mm edge-to-edge from its neighbours. The worst case is 0.578 mm, between two contacts and their nearest spring seats. That's a tight face, and it's tight on purpose.

## Why 20 mm

The lattice cell the project is aiming at is a 25 mm cube, which is a later build. Phase 0 isn't trying to be small. It's trying to be **hand-assemblable and measurable**: prove the mechanism at a scale you can drill, populate with off-the-shelf pogos and pins, and put calipers and a force gauge on, then shrink. The Monte Carlo sim was written for "the same 20 mm face article", so the size was committed to match it on 2026-11-23. An earlier 30 mm plate served as the reference article before that.

Density is a later problem. Phase 0's job is to prove the mechanism works.

## The locking mechanism

Each part on the face has one job.

**Retention: the magnet.** An N52 disc sits in an Ø8.2 through-hole. You can't keep a 4 mm-deep blind pocket in a 1 mm plate, so the hole goes all the way through. A separate backing disc closes it from behind with a 2.0 mm solid back face, and that disc doubles as the heat spreader. The magnet holds the joint at zero power. Gate 5 sets the retention requirement from first principles. Take the 9.2 g module, assume 10 g of acceleration, and add a safety factor of 2. That gives 0.0092 × 10 × 9.81 × 2 = 1.805 N, so **F_hold must be at least 1.8 N**. It's a modest number next to the 34.6 N simulated snap pull, and gate 5 exists to prove that on a gauge rather than in a spreadsheet.

**Release: Option A.** Release doesn't fight the magnet with brute force. A single Ø2.0 mm pin slides 3.0 mm in a Ø2.05 bore and breaks contact, and the coil pulse bucks the magnet's residual field while it does. The pin only breaks contact: it carries no torque and has no linkage. There are no cams. On the first article you push the pin by hand, with a finger or a flat tool. Solenoid or actuator drive is deferred to later work (see [docs/OPTION_A.md](docs/OPTION_A.md)).

**Structure: three pins.** Shear load goes through three hardened Ø1.80 mm pins in Ø1.85 bores on a 7.45 mm radius. The angles are **73°, 155° and 328°**, deliberately not 120° apart. A symmetric layout left only 0.52 mm worst-case clearance against the 0.5 mm rule, which is too close to call it margin. The asymmetric layout comes with a bonus: the pattern isn't rotationally symmetric, so the face can only seat one way. The pins do the contact clocking for free. Pin engagement is 3.00 mm by design and at least 2.5 mm for acceptance, and the mating receptacle must be at least 2.5 mm deep. The shear bar is ≥ 40 N in four directions.

**Seating and capture.** Four non-magnetic BeCu or phosphor-bronze springs give 5.00 N in total. That's 5.00 N for all four combined, not 5 N each. They keep the faces seated during mating. A 1.0 mm chamfer and 1.0 × 1.0 mm ridges pull the faces into alignment from up to 2.5 mm off-centre and 7° off-angle. The six pogos on the 6.25 mm ring carry power, ground, sense and, in Phase 1, data.

## Thermal

The coil is **pulse-only**. It switches the joint and then turns off, and nothing in the design ever holds current in it. Thermal limits are still enforced in two places:

- **On paper:** a 41 °C skin cap, and less than 1.5 K rise at 0.44 W pulse duty. Gate 6 runs 1.25 A through the contact bus for at least 10 minutes and logs the plate temperature.
- **In firmware:** a governor reads an NTC thermistor on pin **A0** (beta 3950, 10 kΩ pull-up). At **41 °C** it latches off and refuses pulses until the plate drops below **36 °C** (5 °C hysteresis). Separately, after **20 consecutive pulses** it forces a **5 s cooldown** regardless of temperature.

If the NTC is missing, open or shorted, the reading is forced to 999 °C. The governor then refuses to pulse rather than dividing by zero. Failing hot is the only acceptable way to fail here.

The firmware also has a **3.6 A** overcurrent flag, which is the DRV8871's peak rating. That check depends on an optional INA219 current sensor, and the INA219 is switched off by default (`USE_INA219 = false`). On a board without the INA219, the current fault never fires. In that case the 3.6 A figure is only a datasheet limit that you're trusting the driver to respect.

## Firmware

`firmware/pulse_driver.cpp` targets the Seeed Studio XIAO RP2040, a dual Cortex-M0+ board, using the Arduino framework. It drives the DRV8871 H-bridge on GPIO 0/1 and reads the six contacts on GPIO 2–7. It runs the thermal governor above and a stub dock/undock state machine. It also has a 115200-baud serial console for manual commands and status. Error flags are a single byte with thermal, current, contact and watchdog bits. The watchdog arms only after setup finishes, so the USB wait at boot can't trip a false fault.

It compiles. With arduino-cli 1.6.0 and the Earle Philhower RP2040 core 6.4.0, targeting `rp2040:rp2040:seeed_xiao_rp2040`, the build comes out at **60,636 bytes of flash (2% of 2 MB) and 9,124 bytes of RAM**. It produces no warnings with `-Wall -Wextra`. Nobody has flashed it onto a real board yet. A compiler is not a bench.

## Simulation

The Phase 0 Monte Carlo (`sims/phase0_monte_carlo.py`, test plan DB-P0-FACE-TP-001 Rev A) runs 100,000 seeded trials against five tests:

- **T1** soft-dock capture
- **T2** hard-lock
- **T3** 40 N shear under lateral offset and approach velocity
- **T4** 1.25 A for 10 minutes without throttling
- **T5** 2 000 cycles

The current result is **98.04% all-pass**, with T3 at 99.30% (702 T3 failures in 100k trials). T3's acceptance window is 1.5 mm lateral and 0.5 m/s. That window was tightened, partly loosened, and then put back exactly where it started, which at least shows someone checked it. The 98% is the bar the hardware has to meet with real input distributions. It doesn't count as a result until it does.

## Metrology

The bench plan is [docs/PROTOTYPE_PLAN.md](docs/PROTOTYPE_PLAN.md). It starts with eight pre-assembly checks, **A1–A8**:

- plate thickness and flatness
- through-hole and backing-disc recess
- the 2.0 mm back face
- pin-bore true position
- free travel of the release pin
- contact holes and pogo wipe
- coil resistance
- a backing-disc bond pull test on a coupon

Then come seven gates, in order:

1. **Snap:** axial pull at a 0.5 mm gap against mild steel, to the 34.6 N sim bar.
2. **Soft-dock:** at least 90% capture over at least 30 tries, at ≤ 2.5 mm and ±7°.
3. **Hard-lock:** at least 95% three-pin seating, with ≥ 2.5 mm engagement.
4. **Shear:** ≥ 40 N in four directions, with ≤ 0.10 mm slip and a 50 N proof load.
5. **Retention:** ≥ 1.8 N, then a clean release with the pin.
6. **Thermal:** ≤ 41 °C after 10 minutes at 1.25 A.
7. **Cycles:** 2 000 dock/undock cycles, with ≤ 2% spring loss.

(The repo also contains a separate M1–M9 sequence. That one is for the later 25 mm cube cell and doesn't apply to this face.)

Every number goes into [docs/MEASUREMENT_CARD.md](docs/MEASUREMENT_CARD.md), raw. If the hardware misses a bar, the design changes. The bar doesn't come down.

## The Phase 1 boundary

[docs/PHASE1.md](docs/PHASE1.md) is deliberately short on ambition. It covers **two modules, face to face, one joint**, and handing power and data across that single joint. It doesn't cover chains of three or more, lattice behaviour, or genderless faces. It is paper-only and proposed until Phase 0 has measured data.

The dock runs through a nine-state table, **S0–S8**:

| State | What happens |
| :--- | :--- |
| S0 | Idle |
| S1 | Align |
| S2 | Creep at 0.05 m/s over the last 3 mm |
| S3 | Soft-dock |
| S4 | Hard-lock, 3/3 pins or retry |
| S5 | Presence and polarity probe on pogo 5 |
| S6 | 12 V soft-start onto pogos 1/2 |
| S7 | Link-up |
| S8 | Docked, up to 1.25 A with a heartbeat |

Data runs as **single-wire, half-duplex UART on pogo 6 at 115200 baud**, 3.3 V open-drain, referenced to the ground pogos 3/4. After power-good, module A sends `HELLO` every 20 ms and expects `HELLO_ACK` **within 200 ms**. If three tries fail, power goes off and the lock stays engaged. A lost link can never drop the joint, and a confused one can never energise it.

## The open call

Everything that can be done on a laptop has been done:

- The geometry clears its own rules.
- The sim passes.
- The firmware compiles.
- The bench plan is written down to a fill-in-the-blanks log template.

What's missing is the physical **first coupon**: one machined 7075 plate with a magnet, a backing disc, three pins, a sliding pin, four springs, six pogos and a XIAO, taken through A1–A8 and gates 1–7.

If you can machine small aluminium parts, have a force gauge and a load cell, or can fund a short run of plates and a handful of DigiKey parts, that's the help this project needs. The CAD is [cad/voxel_cell_phase0_20mm.scad](cad/voxel_cell_phase0_20mm.scad), the parts list is [bom/bom_netlist.txt](bom/bom_netlist.txt), and the full spec is [docs/PHASE0.md](docs/PHASE0.md). Open an issue on the repo or contact the owner. If you build one, fill in the measurement card, good numbers or bad.

The design is frozen until it's measured. **Hardware is the only remaining gate.**
