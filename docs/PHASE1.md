# Phase 1 — two-module docking on the Phase 0 face protocol (START ONLY)

Design owned by Craig. Started 2026-11-23. Status: **proposed / paper only**. Credit follows measured data.

> **Scope boundary.** This document is the **start of Phase 1 and stops there**. It covers only:
> - docking two modules face-to-face on the unchanged Phase 0 face protocol,
> - the inter-module power and data handoff across that one joint,
> - test plan DB-P1-DOCK-TP-001.
>
> It contains nothing beyond Phase 1: no chains of three or more modules, no lattice or swarm behaviour, no genderless face redesign, no companion or V2.0 claims. It does not change any Phase 0 sim number, lock, CAD file, or existing doc.

Every value below is **proposed** unless it is quoted from an existing locked source. **TBD** means a number must be chosen or measured before Phase 1 test start.

---

## 1. Inputs inherited unchanged

| Source | What Phase 1 inherits |
| :---- | :---- |
| `sims/phase0_monte_carlo.py` (DB-P0-FACE-TP-001 Rev A, commit 74ded02) | **Gates T1–T5 and every constant, unchanged.** <br>• T1: ≤ 2.5 mm / ≤ 7° (σ 0.65 mm / 1.6°) <br>• T2: ≥ 95 % (p 0.994) <br>• T3: ≥ 40 N with lat ≤ 1.5 mm, vel ≤ 0.5 m/s (σ_lat 0.55 mm, σ_vel 0.10 m/s, spring 5.00 ± 0.25 N, shear 72.8 ± 4.0 N, 7075-T6, 3 pins) <br>• T4: 1.25 A × 10 min <br>• T5: 2 000 cycles <br>Results: all-pass 98.04 %, T3 99.30 %, 702 T3 fails / 100k |
| `docs/HARDWARE_MAPPING.md` | Tolerance stack (lat RSS 0.514 ≤ 0.55 mm), approach profile (creep 0.05 m/s over last 3 mm, abort at 0.25 m/s), spring spec, 40 N shear requirement (SF 1.82 mean), I_release note, lab fixtures |
| `cad/voxel_cell_phase0_20mm.scad` (rev 2026-11-23, 20 mm redesign) | Face geometry: 6 contacts on hex ring r = 6.25 mm at 50/110/170/230/290/350°, 3 pins Ø1.80 in Ø1.85 bores at r 7.45 (73° / 155° / 328°), ridge 1.0 × 1.0, chamfer 1.0 |
| `docs/PHASE0.md` electrical section | Contact assignment (pogo 1, 2 = +12 V; 3, 4 = GND; 5 = 12 V sense; 6 = spare / AGND sense); 1.5 A bus fuse; INA219 shunt; TMP117 + NTC |
| `docs/LOCKS.md` | Hold current after switch = 0; 40 N structural vs 35 N human-contact interrupt; 41 °C skin cap; 12 V bus and pulse bank stay fixture-side until contacts are covered or isolated; one coil at a time |

**Face size note.** Craig's brief calls this the "20 mm face". The 20 mm CAD redesign landed 2026-11-23 (`cad/voxel_cell_phase0_20mm.scad`); face size is consistent 20 mm throughout. Phase 1 uses **whatever face DB-P0-FACE-TP-001 is run on, unchanged**. This file does not re-dimension it.

---

## 2. Roles and configuration (proposed)

- **Two modules, one joint.** Module A (active) and module B (passive), docked face-to-face.
- **Fixed roles for Phase 1.**
  - A carries the extending latch pins and is the **power source**. It is fed from the fixture supply, per the LOCKS rule that the 12 V bus stays fixture-side.
  - B carries the receptacles and is the **power sink**.
  - Role swap and genderless faces are out of scope.
- **Orientation keying.** The 3-pin pattern at r 7.45 (73° / 155° / 328°) is not rotationally symmetric, so pins seat in only one orientation. Hard-lock (T2) therefore also proves correct contact clocking. Electrical polarity is still checked before enable (§4.4).

---

## 3. Docking sequence (proposed)

| State | Entry condition | Action | Exit / abort |
| :---- | :---- | :---- | :---- |
| S0 IDLE | Undocked | Face contacts unpowered on both sides. Data line idle (pulled up). Coil off. | Dock command |
| S1 ALIGN | Dock command | Coarse align to ≤ 2.5 mm / ≤ 7° (T1 window). Target the §1.2 allocation in HARDWARE_MAPPING: approach σ ≤ 0.42 mm. | Aligned → S2; timeout TBD → S0 |
| S2 CREEP | Range ≤ 3.0 mm | Commanded 0.05 m/s. A's coil shorted via DRV8871 brake (IN1 = IN2 = 1) for eddy damping. Velocity estimated from Hall dB/dt. | Contact → S3; v > 0.25 m/s → back off, retry (max 3), then S0 + fault |
| S3 SOFT-DOCK | Hall threshold crossed (TBD from measured field) | Nd disc pulls in; chamfer/ridges center; spring compresses through 1.0 mm working travel to 5.00 N seated. | Seated within 500 ms → S4; else release and retry |
| S4 HARD-LOCK | Seated | A extends 3 pins. All 3 seat sensors must read locked. | 3/3 seated → S5; < 3 within 200 ms → retract, back off, retry (max 3) |
| S5 PRESENCE | Locked | A applies a current-limited **sense probe** (≤ 10 mA, proposed) on pogo 5. B echoes presence by a pull-down signature (TBD). Polarity and voltage window checked (§4.4). | Valid → S6; invalid → fault F-POL, stay unpowered, stay locked |
| S6 POWER-UP | Presence valid | A's load switch soft-starts 12 V onto pogos 1/2 (§4.3). | V_B in window within 20 ms → S7; else F-INRUSH / F-UV |
| S7 LINK-UP | Power good at B | B boots. Data handshake and ID exchange (§5). | HELLO/ACK + ID within 200 ms of power good → S8; else retry ×3 → F-LINK (power off, stay locked) |
| S8 DOCKED | Link up | Power transfer enabled up to 1.25 A; heartbeat running | Undock command or fault |

### Undock (reverse order, proposed)

1. **U1** — Either side sends `UNDOCK_REQ`; the peer replies `UNDOCK_ACK`.
2. **U2** — B sheds load; A turns its power switch off. Confirm pogo 1/2 voltage < 1.0 V at A's sense.
3. **U3** — Link goes quiet (`BYE`).
4. **U4** — A retracts pins; seat sensors read 3/3 open.
5. **U5** — Release coil pulse at I_release (≤ 2.4 A, pulse-only, thermal governor gated). Spring and the release mechanism separate the faces (Phase 0: Option A Ø2.0 sliding release pin; cams deferred to Option A / 25 mm, rev 2026-11-23b).
6. **U6** — Hall confirms separation; S0.

**Power is always off before any pin moves.** No undock happens on link loss alone. Link loss removes power but keeps the mechanical lock, because the hold is zero-power.

---

## 4. Inter-module power handoff (proposed)

### 4.1 Contacts

| Pogo | Phase 0 assignment | Phase 1 use (proposed) |
| :---- | :---- | :---- |
| 1, 2 | +12 V | +12 V power, redundant pair. **Each contact path rated ≥ 1.25 A alone** (T4 survives one bad contact). |
| 3, 4 | GND | Power return, redundant pair, same rating |
| 5 | 12 V sense | Presence / polarity sense probe (S5), then Kelvin sense of V_B during transfer |
| 6 | spare / AGND sense | **DATA** (single-wire half-duplex, §5). Signal reference is GND via 3/4. |

- **Mate-first-break-last (proposed):** GND contacts 3/4 seat ≥ 0.2 mm before 1/2 and 5/6, by stroke stagger or pad height (TBD in CAD). All contacts stay within the 0.30–0.50 mm wipe.
- Contact preload adds to the 5.00 N seating budget. Measure it and report separately (HARDWARE_MAPPING §3.2).

### 4.2 Voltage and current limits

| Item | Limit (proposed) |
| :---- | :---- |
| Nominal bus | 12 V (PHASE0 / 25 mm cell bus) |
| Operating window at B | 10.8–13.2 V (±10 %) |
| Under-voltage lockout at B | < 10.0 V → B load off |
| Over-voltage clamp | TVS at each face, clamp ≤ 16 V (part TBD) |
| Continuous transfer | **≤ 1.25 A** per joint (T4 gate) |
| Source current limit (A's load switch / eFuse) | Trip 1.5 A, matching the PHASE0 1.5 A fuse; response ≤ 1 ms (TBD by part) |
| Backup | 1.5 A fuse or PTC per face, upstream of the switch |
| Release-coil pulse | **Never across the joint.** Each module's pulse comes from its own local bank. Bank recharge from the bus ≤ 0.25 A, counted inside the 1.25 A. |
| Pulse bank (30–48 V) | Never on any face contact |

### 4.3 Inrush

- B's input capacitance: ≤ 47 µF total (proposed, TBD).
- A soft-starts the bus at a slew rate ≤ 1 V/ms. Expected capacitive inrush ≈ 0.05 A (C·dV/dt = 47 µF × 1 V/ms). Design budget ≤ **0.6 A** including B's logic, with B's load held off until power good. Hard ceiling **2.0 A for ≤ 10 ms**.
- B holds its loads off until V_B is within window for ≥ 5 ms (power-good delay, proposed).

### 4.4 Polarity and sequencing

- Mechanical keying: 3-pin pattern (§2). Electrical: A enables power only after the S5 probe reads correct polarity and B's signature.
- Each side has reverse-polarity / reverse-current blocking (ideal-diode or P-FET, part TBD). B never back-feeds A.
- **Order on dock:** lock (3/3) → sense probe → soft-start power → power good → data.
- **Order on undock:** data `BYE` → power off → verify < 1.0 V → pins retract → coil pulse.
- Power never makes or breaks under load on a moving contact.

### 4.5 Fault isolation

| Fault | Detection | Response (proposed) |
| :---- | :---- | :---- |
| F-OC over-current / short at B | A's eFuse trip > 1.5 A | A cuts this face's power ≤ 1 ms. Retry after 1 s, max 3, then latch off until operator clear. A's other faces and A's own logic stay up. |
| F-UV / F-OV | B window comparator | B drops its load; reports over data if the link is up |
| F-POL | S5 probe | Never enable; stay locked; report |
| F-THERM | Plate NTC/TMP117 ≥ 41 °C (skin cap) | Derate to 0.5 A, then off at cap + 2 °C (TBD); report |
| F-LINK (3 missed heartbeats) | Heartbeat timeout | A removes power ≤ 300 ms after the last good frame. **Mechanical lock unchanged.** Re-handshake allowed. |
| F-CONTACT (drop > limit) | Kelvin V on pogo 5 vs A's output | Report; derate to 0.5 A if drop > 2× limit |
| Coil-fire interlock | Firmware | No release pulse while the joint is powered (power must be off, LOCKS rule order) |

---

## 5. Inter-module data handoff (proposed)

### 5.1 Link

- **Physical:** single-wire half-duplex UART on pogo 6. Open-drain with a pull-up to 3.3 V on A (value TBD), series resistor and ESD clamp on each side, referenced to GND pogos 3/4. Logic is 3.3 V (RP2040 / XIAO RP2040). Never put bus or coil voltage on this line.
- **Rate:** 115 200 baud, 8N1 (proposed). Leave headroom for contact bounce and the long ground path.
- **Arbitration:** A is master; B transmits only in response or in its heartbeat slot.

### 5.2 Frame (proposed)

```
SOF 0x7E | LEN (1) | TYPE (1) | SEQ (1) | PAYLOAD (0–64) | CRC-16/CCITT-FALSE (2)
```

Types: `HELLO`, `HELLO_ACK`, `ID`, `ID_ACK`, `HB` (heartbeat), `STATUS`, `PWR_REQ`, `PWR_GRANT`, `UNDOCK_REQ`, `UNDOCK_ACK`, `BYE`, `NAK`.

### 5.3 Handshake and ID exchange

1. After power good at B (S7), A sends `HELLO` every 20 ms until `HELLO_ACK` arrives, up to 200 ms.
2. A sends `ID` with:
   - 64-bit unique ID (RP2040 flash unique ID)
   - face index (0–5)
   - role (A/B)
   - firmware version
   - protocol version (`P1.0`)
   - power capability (source mA, sink mA)
3. B replies `ID` with the same fields. Each side replies `ID_ACK`.
4. Rules:
   - Protocol major versions must match, or the link stays in a safe minimum mode: power ≤ 0.25 A, no undock-by-peer.
   - B requests load with `PWR_REQ` (mA). A grants up to min(request, 1.25 A − own recharge) with `PWR_GRANT`. B must not draw above the grant.
5. Heartbeat `HB` every 100 ms each way, carrying V, I, plate temperature, and lock state.

### 5.4 Error handling

| Condition | Handling (proposed) |
| :---- | :---- |
| CRC fail / framing error | Discard; `NAK` with SEQ; sender retransmits up to 3 times |
| No reply within 50 ms | Retransmit; after 3 tries count as a missed heartbeat |
| 3 missed heartbeats | F-LINK: power off (§4.5), lock held, try re-handshake from S7 |
| Duplicate SEQ | Re-ACK, do not re-execute |
| Unknown TYPE | `NAK`, ignore |
| `UNDOCK_REQ` without `UNDOCK_ACK` | No undock. Operator override only on the fixture. |
| Conflicting ID (both claim role A) | Abort to S0 safe state: power off, stay locked, report |

---

## 6. Test plan DB-P1-DOCK-TP-001 Rev A (proposed)

**Extends DB-P0-FACE-TP-001 Rev A.** Every Phase 0 gate is inherited unchanged and must pass on **each** module's face before any Phase 1 test counts. Phase 1 adds two-module tests. Sample sizes are zero-failure success runs at 95 % confidence unless stated. Fixtures are those in `docs/HARDWARE_MAPPING.md` §5 unless stated.

### 6.1 Inherited gates (unchanged)

| ID | Gate (from DB-P0-FACE-TP-001) | Applied to |
| :---- | :---- | :---- |
| P0-T1 | Soft-dock ≥ 90 % at ≤ 2.5 mm / ≤ 7° | Each face; then A↔B |
| P0-T2 | Hard-lock ≥ 95 %, all 3 pins seated | Each face; then A↔B |
| P0-T3 | Shear ≥ 40 N with lat ≤ 1.5 mm, vel ≤ 0.5 m/s | Each face; then A↔B |
| P0-T4 | 1.25 A × 10 min, no throttle, ≤ 41 °C skin | Each face; then through the A↔B joint (P1-T7) |
| P0-T5 | 2 000 dock/undock cycles | Each face; then A↔B (P1-T12) |

### 6.2 New Phase 1 tests

| ID | Test | Method | Pass criteria (proposed) |
| :---- | :---- | :---- | :---- |
| P1-T1 | Module-to-module capture | A approaches B on the rail at the §3 profile, corners at 2.5 mm / 7° | ≥ 90 % capture: **29/29** at the corner; natural σ ≤ 0.65 mm / 1.6° over ≥ 30 docks |
| P1-T2 | Module-to-module hard-lock | Full S0→S4 | **59/59** with 3/3 pins seated |
| P1-T3 | Contact conditions at latch | Laser/high-speed video + offset log over ≥ 30 docks | Velocity σ ≤ 0.10 m/s, max < 0.5 m/s; lat σ ≤ 0.55 mm, max ≤ 1.5 mm |
| P1-T4 | Docked shear, A↔B | Shear rig, 4 directions | ≥ 40 N, slip ≤ 0.10 mm, no yield; proof 50 N × 10 s |
| P1-T5 | Power sequencing | Scope on pogos 1/2/5/6 and seat sensors across 30 docks + 30 undocks | 0 instances of bus voltage (> 1.0 V) before 3/3 lock or after pin-retract start; GND mates first |
| P1-T6 | Inrush | Current probe at A's output, B at max capacitance | Peak ≤ 2.0 A, duration ≤ 10 ms; V_B in window ≤ 20 ms |
| P1-T7 | Power transfer soak | 1.25 A into B's load for 10 min through the joint | No throttle; skin ≤ 41 °C both plates; V_B ≥ 10.8 V; per-path contact drop ≤ 100 mV at 1.25 A (TBD after first measurement) |
| P1-T8 | Single-contact loss | Lift one +12 V pogo (and separately one GND), repeat P1-T7 | Still passes P1-T7 with one path per polarity |
| P1-T9 | Fault isolation | Short B's input; apply 16 V; reverse-polarity source on bench | Over-current trip ≤ 1 ms (TBD by part), A survives and other faces unaffected; OV clamped, no damage; reverse polarity → no enable, no damage |
| P1-T10 | Data link integrity | 10⁶ frames each way at 115 200 baud while P1-T7 runs at 1.25 A | Frame error rate ≤ 10⁻⁵ before retry; 0 undelivered after retries |
| P1-T11 | Handshake + ID exchange | 100 docks | ID exchange complete ≤ 200 ms after power good on 100/100; IDs logged correctly; version mismatch forces safe mode |
| P1-T12 | Link-loss safety | Cut pogo 6 (or jam the line) while docked under load | Power off ≤ 300 ms; lock stays 3/3; re-handshake succeeds after reconnect |
| P1-T13 | Undock order + release | 30 undocks | Order U1→U6 on scope every time; release with I_release ≤ 2.4 A pulse-only; thermal governor never bypassed |
| P1-T14 | Two-module cycle life | 2 000 full cycles (dock → lock → power → link → undock) | 2 000/2 000 complete; first-try handshake ≥ 99.5 %, 100 % within retries; contact drop rise ≤ 50 % of initial (TBD); P1-T4 proof passes at 0/500/1 000/1 500/2 000; spring loss ≤ 2 % |

### 6.3 Exit criteria for Phase 1 start

- All inherited P0-T1…T5 pass on both faces.
- P1-T1…T14 pass.
- Results go into a Phase 1 section of a measurement card, with one row per test. Creating that card is a separate commit; it is not part of this file.
- Sim numbers are the bar. Measured numbers are the credit.

---

## 7. Open items (TBD before test start)

- Face size naming reconciliation: **resolved** — 20 mm throughout (CAD redesign landed 2026-11-23).
- Hall threshold for S3; module masses; B input capacitance.
- Load switch / eFuse, TVS, ideal-diode parts: choose and record in the BOM. No part numbers are proposed here.
- Pogo stagger implementation for mate-first GND.
- Contact drop limit after first measurement.

**End of Phase 1 start. Nothing beyond Phase 1 is specified here.**
