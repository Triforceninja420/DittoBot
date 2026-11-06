# 25 mm cell — minimum parts for one counted coil

Project i started Nov/Dec 2025. Design owned by Craig. Programmable matter.

**This list is only for the public 25 mm cubic cell.**
One coil. One pulse. One fixture pull. Not a lattice. Not a breadboard farm. Not Phase 0.

Fill `MEASUREMENT_CARD.md` with whatever this kit measures. No latch claim until that card is filled. **No companion claim** until that card is filled. 28.8 N is retired on this cell.

Process stamps: `LOCKS.md` (16 paper locks, 2026-09-14). This kit stays a fixture coupon. Soft safety skin is not on this order.

Geometry (option A, 2026-09-09; thermal revision 2026-11-06):
- Pocket: Ø8.2 mm × 4.0 mm (`openscad`, do not enlarge)
- Magnet stack: Ø6.0 mm × 4.0 mm
- Coil: **2–4× AWG 36 in parallel** (or 1× AWG 30 equivalent), count the turns you actually wind. Single-strand AWG 36 retired — 444 °C sim failure at 1.25 A × 10 min.
- Driver: DRV8871, 12 V on VM only
- Logic: 3.3 V XIAO. Do not put 12 V on U1 VCC
- Latch face shim: carbide or 440C, 0.50 mm thick, clip-in (wear item)

Full cell BOM / netlist stays in `text`. Wind math stays in `COIL_REVISION.md`. Phase 0 stays in `PHASE0.md`.

---

## Buy or borrow (7 items)

| # | Item | Spec | Why it is here | Skip / substitute |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Magnet stack | Ø6.0 mm × 4.0 mm total. NdFeB N52 + Alnico 5, split height as wound | This is the latch. D8 does not fit the pocket | Do not order D8 mm for this cell |
| 2 | Magnet wire | **2 spools AWG 36 enamel** (≈0.13 mm bare) or 1 spool AWG 30 | Parallel strands split 1.25 A continuous; single strand hits 444 °C | AWG 33 packs \~100 t here. Use it only as a backup and write 100 t on the card |
| 3 | Driver | DRV8871 breakout or DRV8871DDAR + ILIM resistor set \~3.0 A | 12 V coil rail. 3.6 A is the peak rating, not the setpoint | DRV8212 is the listed alternate. DRV8837C is retired |
| 4 | Logic | Seeed XIAO RP2040 + 3.3 V | Runs `cpp`. GPIO0 = IN1, GPIO1 = IN2 | Any 3.3 V RP2040 is fine. Keep 12 V off this rail |
| 5 | 12 V source | Bench supply, pack, or boost. Feeds driver VM only | DRV8871 VM min is 6.5 V. Old 5 V bus cannot run it | Put ≥100 µF on VM next to the driver |
| 6 | Fixture | Mild-steel plate + luggage scale (or a force stand) | ON N and OFF N, same plate, same gap | Kitchen scale in newtons / grams is enough for a first pull |
| 7 | Latch shim | Carbide or 440C hardened steel, Ø6.0 mm × 0.50 mm, clip-in | Wear item for 2 000-cycle budget; swap without re-winding | Hardened steel acceptable if carbide unavailable |

That is the kit. Contacts, cube print, and face bus are not required to fill the card.

---

## Current street prices (2026-11-06)

Ranges for one counted coil. Prices move; check the source before ordering.

| Item | Typical price | Sources / notes |
| :--- | :--- | :--- |
| NdFeB disc Ø6.0 × 2–3 mm N52/N45 | $0.20–0.50 ea in small packs (often 20–40 for $8–15) | Amazon, UMAGNETS, Guy's Magnets, Element Games. BUILD.md prefers pure Nd disc hold + coil release. |
| Alnico 5 rod Ø5–6 mm (if used) | $1–4 ea | Guitar-pickup suppliers, MagnetShop, Magna-C. Not required for the pure-Nd path. |
| AWG 36 enamel spool ×2 | $16–32 for two 2–4 oz spools | Remington Industries, Amazon, surplus. One 160–180 t parallel coil uses only a few meters per strand. |
| AWG 30 enamel spool (alternate) | $10–20 | One spool replaces two AWG 36. |
| DRV8871 breakout | $7.50 (Adafruit #3190) | Adafruit in stock. Clones / multi-packs $10–15. Set ILIM near 3 A. |
| Seeed XIAO RP2040 | \~$5 official / \~$9–10 Amazon | Pre-soldered versions available. Keep 12 V off this rail. |
| 12 V source | Borrow or $10–20 | Bench, pack, or tool-battery adapter. ≥100 µF on VM next to the driver. |
| Fixture | Borrow or $15–30 | Scrap mild steel + luggage/kitchen scale. |
| Carbide/440C shim Ø6 × 0.5 mm | $5–15 (small pack) | McMaster-Carr, Amazon carbide blanks. Clip-in retention. |

**New-buy cash for one coil + driver + logic + wire + a pack of discs + shim:** roughly $40–70. Fixture and scope can be borrowed. Contacts, cube print, and face bus are still not required to fill the card.

---

## Already in the repo (do not repurchase)

- Pulse routine: `cpp`
- Pocket: `openscad`
- Blank card: `MEASUREMENT_CARD.md`
- Wind window: `COIL_REVISION.md`

---

## Borrow if cash is zero

- Scope or current probe — peak I and time-to-peak. A cheap shunt + phone scope app is enough to start.
- Luggage scale and a scrap steel plate — force.
- Winding jig — a drill chuck and a 6 mm mandrel works for one coil.
- 12 V supply — lab, makerspace, or a tool-battery adapter.

University lab, makerspace night, or a hardware hackathon that covers parts can run this list without a protoboard wall.

---

## Do not put on this order

- DRV8837C
- D8 mm magnet stack
- AWG 33 billed as 180 t
- **Single-strand AWG 36 for the 1.25 A continuous soak** (pulse-only duty)
- Phase 0 parts: IRLZ44N, 220 µF / 30–36 V cap-dump, Ø5 EPM set, 1.8 mm pin, Pico netlist
- A full 25 mm cube print before the coil has numbers
- Another Community Enhancement Suite
- Soft safety skin, companion housing, or live face-bus for a person
- A second coil fired with the first before VM headroom is written on the card

---

## Bench order

1. Wind **parallel strands** on the Ø6 stack. Count turns. Write the count and strand count.
2. Cold R, coil off the driver (total across strands).
3. 12 V on VM. Pulse from `cpp`. Scope peak I. Set pulse width from that.
4. ON pull, then OFF pull, same plate, same gap.
5. N pulses at planned cadence. Log coil and driver temperature. T4 pass: < 85 °C after 1.25 A × 10 min.
6. Seat carbide shim, verify ≤ 0.10 mm clearance. Log shim wear at 2 000 cycles.
7. Paste the numbers into `MEASUREMENT_CARD.md`.

If peak I never reaches \~3 A, stop and fix the pulse. Force will not decide geometry until the current arrives.
