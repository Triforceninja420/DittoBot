# 25 mm cell — minimum parts for one counted coil

Project i started Nov/Dec 2025. Design owned by Craig. Programmable matter.

**This list is only for the public 25 mm cubic cell.**
One coil. One pulse. One fixture pull. Not a lattice. Not a breadboard farm. Not Phase 0.

Fill `MEASUREMENT_CARD.md` with whatever this kit measures. No latch claim until that card is filled. 28.8 N is retired on this cell.

Geometry (option A, 2026-09-09):
- Pocket: Ø8.2 mm × 4.0 mm (`openscad`, do not enlarge)
- Magnet stack: Ø6.0 mm × 4.0 mm
- Coil: AWG 36, count the turns you actually wind
- Driver: DRV8871, 12 V on VM only
- Logic: 3.3 V XIAO. Do not put 12 V on U1 VCC.

Full cell BOM / netlist stays in `text`. Wind math stays in `COIL_REVISION.md`. Phase 0 stays in `PHASE0.md`.

---

## Buy or borrow (6 items)

| # | Item | Spec | Why it is here | Skip / substitute |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Magnet stack | Ø6.0 mm × 4.0 mm total. NdFeB N52 + Alnico 5, split height as wound | This is the latch. D8 does not fit the pocket | Do not order D8 mm for this cell |
| 2 | Magnet wire | AWG 36 enamel (≈0.13 mm bare). One small spool | 160–180 t only packs in the 1.1 mm annulus on 36 | AWG 33 packs ~100 t here. Use it only as a backup and write 100 t on the card |
| 3 | Driver | DRV8871 breakout or DRV8871DDAR + ILIM resistor set ~3.0 A | 12 V coil rail. 3.6 A is the peak rating, not the setpoint | DRV8212 is the listed alternate. DRV8837C is retired |
| 4 | Logic | Seeed XIAO RP2040 + 3.3 V | Runs `cpp`. GPIO0 = IN1, GPIO1 = IN2 | Any 3.3 V RP2040 is fine. Keep 12 V off this rail |
| 5 | 12 V source | Bench supply, pack, or boost. Feeds driver VM only | DRV8871 VM min is 6.5 V. Old 5 V bus cannot run it | Put ≥100 µF on VM next to the driver |
| 6 | Fixture | Mild-steel plate + luggage scale (or a force stand) | ON N and OFF N, same plate, same gap | Kitchen scale in newtons / grams is enough for a first pull |

That is the kit. Contacts, cube print, and face bus are not required to fill the card.

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
- Phase 0 parts: IRLZ44N, 220 µF / 30–36 V cap-dump, Ø5 EPM set, 1.8 mm pin, Pico netlist
- A full 25 mm cube print before the coil has numbers
- Another Community Enhancement Suite

---

## Bench order

1. Wind AWG 36 on the Ø6 stack. Count turns. Write the count.
2. Cold R, coil off the driver.
3. 12 V on VM. Pulse from `cpp`. Scope peak I. Set pulse width from that.
4. ON pull, then OFF pull, same plate, same gap.
5. N pulses. Log coil and driver temperature.
6. Paste the six numbers into `MEASUREMENT_CARD.md`.

If peak I never reaches ~3 A, stop and fix the pulse. Force will not decide geometry until the current arrives.
