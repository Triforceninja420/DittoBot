# Bill of Materials — one 25 mm cell, plus a Phase 0 face-article sketch

Design owner: Craig.
Date: 2026-11-27.
Version: v0.1
Status: **paper spec**. This is a purchasing and cost paper compiled from existing repo language plus clearly marked web lookups. It is not a measured build, not a latch claim, and not a quote. Prices from the repo are approximate as of 2026-11-23 and say to re-verify before a PO.

Version is **v0.1** because this is a brand-new document, consistent with the other new top-level papers in `docs/dittobot/` (POWER_ARCHITECTURE, COMMUNICATION_PROTOCOL, COMPANION_TOOL_MODES). It is written in the same template style as the v0.2 per-mode specs (Status, inheritance, modeled-vs-measured flags). It is not a v0.2 revision of a prior BOM in this folder.

Phase: unassigned. This file does not place the 25 mm cell or the Phase 0 face into a new numbered phase, and it does not retune locked values.

Two stacks stay unmixed ([LOCKS.md](../LOCKS.md)). The primary table is **one locked 25 mm cell**. A Phase 0 **20 mm** single-face test article and a face partner are costed separately below. Craig's brief called this a “locked Phase 0 25 mm cell”; that wording mixes the stacks. See [Mismatches with Craig's wording](#mismatches-with-craigs-wording).

Paper until measured. Credit follows data.

---

## Inheritance

Inherits the locked 25 mm cell core, unchanged ([DESIGN.md](../DESIGN.md), [PAPER_STATUS.md](../PAPER_STATUS.md), [LOCKS.md](../LOCKS.md), [BUILD.md](../BUILD.md), [MIN_PARTS.md](../MIN_PARTS.md)):

- 25 mm cube envelope
- Centered Ø8.2 × 4.0 mm pocket (locked)
- Nd disc Ø6.0 × 2–3 mm hold; coil around the disc, release-only (Alnico off this cell)
- DRV8871, 12 V, pulse-only
- Axial pin hard-lock
- Full cavity potting and face coatings
- XIAO RP2040, 3.3 V; 36–48 V pulse bank

This paper does not retune that core, change Phase 0 locks or CAD, or rewrite [PHASE0.md](../PHASE0.md), [PHASE1.md](../PHASE1.md), or [LOCKS.md](../LOCKS.md).

---

## Mismatches with Craig's wording

Confirmed against [DESIGN.md](../DESIGN.md), [LOCKS.md](../LOCKS.md), and [PHASE0.md](../PHASE0.md):

- **Ø8.2 × 4.0 mm pocket, DRV8871, Ø6.0 × 2–3 mm Nd disc hold, coil around the disc release-only, no Alnico.** All five match the locked 25 mm baseline. Phase 0 also uses an NdFeB N52 Ø6.0 × 2–3 mm disc and, in current [PHASE0.md](../PHASE0.md) geometry, a Ø8.2 × 4.0 mm pocket and a DRV8871, but the Phase 0 article is a **20 mm face**, not a 25 mm cube.
- **“Phase 0 25 mm cell.”** The repo keeps two stacks unmixed. Phase 0 is the 20 mm sliding-pin face ([PHASE0.md](../PHASE0.md): “It is **not** the 25 mm cubic cell”). The 25 mm cell is the public coupon ([BUILD.md](../BUILD.md), [cad/voxel_cell.scad](../../cad/voxel_cell.scad)). This BOM is for one 25 mm cell. The Phase 0 test article is defined from the 20 mm face, later in this file.
- **36–48 V pulse bank vs DRV8871 12 V.** This is two rails, not two different drivers. [DESIGN.md](../DESIGN.md) and [BUILD.md](../BUILD.md) say “DRV8871, 12 V” / “DRV8871 on 12 V” together with a **36–48 V** polypropylene-film pulse bank. [LOCKS.md](../LOCKS.md) and [bom/bom_netlist.txt](../../bom/bom_netlist.txt) say the pulse bank is **36 V nominal into DRV8871 VM**, stay under **45 V abs** (netlist: do not exceed ~42 V). The 12 V rail is the face / cell bus. The coil-release pulse comes from the local pulse bank and must never appear on a face contact ([PHASE1.md §4.2](../PHASE1.md#42-voltage-and-current-limits)). The DRV8871 datasheet VM range is 6.5–45 V, so both 12 V and 36 V are legal VM voltages; the repo's release path uses the pulse bank.
- **Phase 0 drive leftover.** [LOCKS.md](../LOCKS.md) still says “Phase 0 drive remains capacitor dump, IRLZ44N class, 220 µF charged 30–36 V, 34 AWG, 40 turns. Those numbers live only in `docs/PHASE0.md`.” Current [PHASE0.md](../PHASE0.md) lists **40 turns, 34 AWG, ~0.75 Ω, DRV8871** and does not mention IRLZ44N or 220 µF. This file follows current PHASE0.md for the face article and does not put IRLZ44N on the buy list.
- **Coil wire is stack-specific.** 25 mm cell: 2–4× **AWG 36** parallel ([MIN_PARTS.md](../MIN_PARTS.md), [BUILD.md](../BUILD.md)). Phase 0 face: **40 turns, 34 AWG**. Do not mix.
- **Contacts.** 25 mm netlist: **four** Mill-Max `0906-0-15-20-76-14-11-0`. Phase 0 face: **six** pogo contacts, hole OD 1.10 mm, ring radius 6.25 mm, **no part number** in [PHASE0.md](../PHASE0.md).
- **0.75 mm vs 4.0 mm pocket on the Phase 0 plate.** Locked Phase 0 geometry and [cad/voxel_cell_phase0_20mm.scad](../../cad/voxel_cell_phase0_20mm.scad) say Ø8.2 × **4.0 mm** (blind, back intact as heat spreader). The same [PHASE0.md](../PHASE0.md) fab-package blurb and “recommended checks” still say a **0.75 mm** blind pocket. This file does not resolve that; it uses the 4.0 mm geometry wording and flags the 0.75 mm lines as an in-repo inconsistency.

---

## One 25 mm cell — BOM table

Primary source: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) (revised 2026-11-23, supplier links and approximate prices) and the summary in [FIRST_ARTICLE.md §5](../FIRST_ARTICLE.md). “In repo” means the part and the price range already live there. “ASSUMED” means not specified or not priced in the repo; those rows are not to be read as if the repo chose the part.

Unit and ext prices are **USD, approximate, single-unit prototype**, as the netlist states. Shared buys (wire spool, potting tub) are called out so they are not silently treated as a per-cell consume-once cost.

| Item | Part number | Qty | Unit USD | Ext USD | Source | Note |
| :-- | :-- | --: | :-- | :-- | :-- | :-- |
| Logic, XIAO RP2040 (U1) | Seeed Studio XIAO RP2040 | 1 | 5–7 | 5–7 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | 3.3 V only. Do not put coil voltage on VCC. |
| Driver, DRV8871 (U2) | DRV8871DDAR or equiv. | 1 | 1–2 | 1–2 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | 12 V VM wording in BUILD; pulse bank feeds VM at 36 V nom., stay ≤ 42 V / 45 V abs. Set ILIM ~3.0 A. DRV8212 is a listed alternate ($2–3), not the primary. A 2026-11-27 Digi-Key cut-tape check listed DRV8871DDAR at $3.38 qty 1 ([Digi-Key 296-43024](https://www.digikey.com/en/products/detail/texas-instruments/DRV8871DDAR/5639726)), above the repo $1–2 range; this table **keeps the repo figure**. Re-verify before PO. |
| Hold magnet (MAG1) | Nd disc Ø6.0 × 2–3 mm (grade TBD on the card; N52 vs N42 swings price) | 1 | 1–3 | 1–3 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt); [BUILD.md](../BUILD.md) | NiCuNi or equivalent. Fits locked Ø8.2 × 4.0 pocket. No Alnico, no SmCo Ø7.5. |
| Release coil (L1) | 2–4× AWG 36 parallel, counted turns, hand-wound around MAG1 | 1 coil; wire bought as a spool | 5–10 / spool | 5–10 / spool (shared) | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | Pulse-only, sized for I_release. [HARDWARE_MAPPING.md](../HARDWARE_MAPPING.md) estimate ≈ 48 turns 2-in-hand, ≈ 0.74 Ω (est., not measured). Spool is a shared buy, not a per-cell consume-once cost. |
| Face spring contacts (J1–J4) | Mill-Max 0906-0-15-20-76-14-11-0 | 4 | 0.50–1 each | 2–4 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | 4 mm stroke. This is the 25 mm cell (four contacts), not the Phase 0 six-pogo face. |
| 3.3 V buck/LDO for XIAO (U3) | PN not specified | 1 | 1–3 | 1–3 | In repo as a function and price: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | Keep logic at 3.3 V. Exact regulator PN is not in the repo. |
| Pulse bank / coil rail (U4) | PP film caps, 36 V nominal (36–48 V family), 100 V rating preferred | 1 bank | 2–5 | 2–5 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt), [BUILD.md](../BUILD.md) | Feeds U2 VM. Never on a face contact. Exact cap PN and µF of the bank (other than C3 below) are not in the repo. |
| Logic decoupling (C1, C2) | 10 µF+ on 3.3 V (PN not specified) | 2 | 0.10–0.50 each | 0.20–1.00 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | |
| VM pulse reservoir (C3) | ≥100 µF on VM near U2 (PN not specified) | 1 | 0.50–2 | 0.50–2 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | |
| VM ceramic bypass | 0.1 µF, rated for VM, at VM–GND | 1 | ASSUMED, price TBD | ASSUMED, price TBD | **ASSUMED (not in repo) — web lookup TI [DRV8871 datasheet Rev B](https://www.ti.com/lit/ds/symlink/drv8871.pdf), 2026-11-27** | Datasheet pin Functions / VM: “Connect a 0.1-µF bypass capacitor rated for the VM voltage, as well as sufficient bulk capacitance.” Repo already has the bulk (C3); it does not list this 0.1 µF part. |
| Current-limit resistor (R_ILIM) | Per DRV8871 datasheet; [HARDWARE_MAPPING.md](../HARDWARE_MAPPING.md) proposes **21.5 kΩ** (2.72–3.24 A trip) | 1 | 0.05–0.20 | 0.05–0.20 | In repo as a line and price: [bom/bom_netlist.txt](../../bom/bom_netlist.txt). Value 21.5 kΩ is proposed in HARDWARE_MAPPING, not a lock. Datasheet (same lookup, 2026-11-27): ITRIP(A) = VILIM(kV) / RILIM(kΩ), VILIM typ 64 kV (59–69); min RILIM 15 kΩ. 21.5 kΩ ≈ 3.0 A typ. | ~3.0 A setpoint, not the 3.6 A peak rating. Exact stock PN not in the repo. |
| Shear shim (SHIM1) | Carbide (preferred) or 440C, clip-in | 1 | 3–10 | 3–10 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | Wear item. |
| Axial pin + receptacle (PIN1) | Ø1.5–2.0 mm × 2.5–3.0 mm engagement | 1 | 1–5 | 1–5 | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt), [BUILD.md](../BUILD.md) | Custom or off-the-shelf dowel + receptacle. Exact PN not in the repo. |
| Potting (POT1) | Low-outgassing potting compound | 1 tub (shared) | 10–30 / tub | 10–30 / tub (shared) | In repo: [bom/bom_netlist.txt](../../bom/bom_netlist.txt) | Full electronics cavity. Tub is a shared buy. |
| PTFE lip + face coating | PTFE lip 0.1–0.2 mm; thin conformal coating or hard finish | 1 set | ASSUMED, price TBD | ASSUMED, price TBD | Spec in repo: [BUILD.md](../BUILD.md), [MIN_PARTS.md](../MIN_PARTS.md). **No price or PN in the repo.** | |
| Cell body, 25 mm cube | Per [cad/voxel_cell.scad](../../cad/voxel_cell.scad) | 1 | ASSUMED, price TBD | ASSUMED, price TBD | Geometry in repo. **Print/machine material is not specified** (SCAD only says “post-print/machining”). **ASSUMED (not in repo)** — material and process TBD; no web price is offered as a guess. | Do not enlarge the Ø8.2 pocket. |
| NTC on A0 + 10 kΩ pull-up | 10 kΩ NTC, beta 3950, plus 10 kΩ pull-up to 3.3 V | 1 + 1 | ASSUMED, price TBD | ASSUMED, price TBD | Function in repo: [FIRST_ARTICLE.md](../FIRST_ARTICLE.md), `firmware/pulse_driver.cpp`. **PN and price are not in the repo.** **ASSUMED (not in repo).** A specific distributor part is not chosen here. | Firmware default thermal sensor. |
| TMP117 (optional) | e.g. TMP117AIDRVR (example only) | 0 or 1 | 6.29 | 0 or 6.29 | Function in repo (optional, `USE_TMP117 = false` by default). **PN/price not in the repo.** **ASSUMED (not in repo) — web lookup Digi-Key, 2026-11-27**, [TMP117AIDRVR](https://www.digikey.com/en/products/detail/texas-instruments/TMP117AIDRVR/9685284) qty-1 cut tape $6.29. | I2C addr 0x48 in firmware. Also used on the T4 fixture in [HARDWARE_MAPPING.md](../HARDWARE_MAPPING.md) (§5). Not required to populate the cell. |
| INA219 (optional) | e.g. INA219BIDCNT (example only) | 0 or 1 | 3.26 | 0 or 3.26 | Function in repo (optional, `USE_INA219 = false` by default). **PN/price not in the repo.** **ASSUMED (not in repo) — web lookup Digi-Key, 2026-11-27**, [INA219BIDCNT](https://www.digikey.com/en/products/detail/texas-instruments/INA219BIDCNT/296-27898-1-ND/2426061) qty-1 $3.26. | I2C addr 0x40. Fixture instrumentation for the 1.25 A soak may use this instead of (or as well as) an on-cell part. |
| Hookup wiring | Not specified | lot | ASSUMED, price TBD | ASSUMED, price TBD | **ASSUMED (not in repo).** | Face bus and pulse-bank leads stay fixture-side until contacts are covered or isolated ([LOCKS.md](../LOCKS.md)). |
| Face-bus fuse | 1.5 A fuse or PTC per face (proposed) | 1 if used | ASSUMED, price TBD | ASSUMED, price TBD | Proposed in [PHASE1.md §4.2](../PHASE1.md#42-voltage-and-current-limits) (1.5 A, matching a PHASE0 1.5 A fuse cited there). **PN and price not in the 25 mm BOM.** | Proposed, not a 25 mm lock. |
| Bench / fixture power (not inside the cell) | 12 V face-bus supply able to hold the 1.25 A soak; separate charger for the 36 V (≤ 42 V) pulse bank | fixture | ASSUMED, price TBD | ASSUMED, price TBD | Rails in repo; **no PSU model or price.** **ASSUMED (not in repo).** See [TEST_RIG.md](TEST_RIG.md). | Pulse bank and face bus stay fixture-side until contacts are covered or isolated. |

Do not order, per [MIN_PARTS.md](../MIN_PARTS.md) and the netlist superseded list: D8 mm stacks, Alnico or SmCo Ø7.5 for this cell, single-strand continuous-duty wire, DRV8837C, or Phase 0-only parts as if they were this cell.

---

## Cost totals — one 25 mm cell

Repo prices only, as of 2026-11-23, single-unit:

- **On-cell increment** (U1, U2, MAG1, J1–J4, U3, U4, C1–C3, R_ILIM, SHIM1, PIN1 — excluding the shared wire spool and potting tub, and excluding every ASSUMED row): **$17–42**.
- **First-buy of the in-repo lines**, including one AWG 36 spool and one potting tub: **$32–82**.

**Assumed share** (body material, PTFE/coating, 0.1 µF VM bypass, NTC + pull-up, hookup wire, optional TMP117 / INA219, fuse, bench PSU): **not in those totals**. Optional TMP117 + INA219, if bought at the 2026-11-27 Digi-Key qty-1 figures above, add **$9.55**. Everything else in that share is **ASSUMED, price TBD**. A complete cell-plus-fixture number cannot be honestly closed until those TBD rows are priced.

These ranges are paper. They are not a vendor quote and not a latch claim.

---

## Phase 0 single-face test article (one face + one face partner)

Defined from [PHASE0.md](../PHASE0.md), not from the 25 mm cube. The Phase 0 article is a **20 × 20 mm, 7075-T6, 1.00 mm** sliding-pin face (Option A Ø2.0 mm release pin, three Ø1.80 mm hardened-steel latch pins, 4× non-magnetic springs at 5.00 N total, six pogo contacts, NdFeB N52 Ø6.0 × 2–3 mm, 40 turns of 34 AWG, DRV8871 in the current file). Test plan parent: `DB-P0-FACE-TP-001`. CAD: [cad/voxel_cell_phase0_20mm.scad](../../cad/voxel_cell_phase0_20mm.scad).

**What “one cell + one face partner” means here.** The repo does not build Phase 0 gates on a 25 mm cube mated to a 20 mm face. The article under test is the 20 mm face; the partner is a second 20 mm face, or a fixture plate that presents the mating receptacles, pin bores, and six contacts. A 25 mm cell may sit on the same bench (HARDWARE_MAPPING is the only allowed stack-mapping exception) but is not required to run the Phase 0 face tests. The 25 mm cost above is therefore **not** automatically added into the Phase 0 article total.

[FIRST_ARTICLE.md](../FIRST_ARTICLE.md) points Phase 0 face parts at `Phase0_Independent_Fab_Package/` (v0.2) and an aluminum plate package. **Neither package is in this repository tree** (PHASE0.md already says the aluminum package is offline / not in this repo). No in-repo price list was found for the plate, pins, springs, or the six Phase 0 pogos.

| Item | Part number | Qty (one article) | Unit USD | Ext USD | Source | Note |
| :-- | :-- | --: | :-- | :-- | :-- | :-- |
| Face plate | 7075-T6, 20.00 × 20.00 × 1.00 mm (accept 0.80–1.20) | 1 | ASSUMED, price TBD | ASSUMED, price TBD | Spec in [PHASE0.md](../PHASE0.md). **No price in the repo.** | Machine from the 20 mm CAD. |
| Hold magnet | NdFeB N52, Ø6.0 × 2–3 mm | 1 | 1–3 (25 mm netlist range, same disc family) | 1–3 | Disc size/grade in [PHASE0.md](../PHASE0.md); **price taken from the 25 mm netlist, same item family, not a Phase 0 price list.** | Alnico off. |
| Face coil | 40 turns, 34 AWG, ~0.75 Ω cold | 1 | ASSUMED, price TBD | ASSUMED, price TBD | [PHASE0.md](../PHASE0.md). **No 34 AWG spool price in the repo** (the netlist spool is AWG 36). | Do not substitute the 25 mm AWG 36 wind here. |
| Latch pins | Hardened steel, OD 1.80 mm, bore 1.85 mm, engagement ≥ 3.00 mm | 3 | ASSUMED, price TBD | ASSUMED, price TBD | [PHASE0.md](../PHASE0.md). **No PN/price in the repo.** | |
| Option A sliding release pin | Ø2.0 mm, single, axial | 1 | ASSUMED, price TBD | ASSUMED, price TBD | [PHASE0.md](../PHASE0.md), [OPTION_A_RELEASE_SPEC.md](../OPTION_A_RELEASE_SPEC.md). **No PN/price in the repo.** | Retention bar ≥ 1.8 N is a locked test, not a part number. |
| Seating springs | 4× non-magnetic phosphor-bronze or BeCu, 5.00 N total, 1.0 N/mm combined, 5 mm preload | 4 | ASSUMED, price TBD | ASSUMED, price TBD | [PHASE0.md](../PHASE0.md). **No PN/price in the repo.** | |
| Pogo contacts | Six contacts, hole OD 1.10 mm (accept 1.00–1.20), ring r = 6.25 mm, wipe 0.30–0.50 mm | 6 | ASSUMED, price TBD | ASSUMED, price TBD | Geometry in [PHASE0.md](../PHASE0.md). **No PN in the repo.** Using the 25 mm Mill-Max 0906 PN here would be an assumption and is **not** done in this table. | |
| Drive electronics | DRV8871 + XIAO + 36 V pulse bank, fixture-side until contacts are covered | 1 set if not borrowed from the 25 mm kit | see 25 mm table | see 25 mm table | Current [PHASE0.md](../PHASE0.md) names DRV8871; LOCKS leftover IRLZ44N/220 µF is not used as the buy list. | If the same bench already has the 25 mm drive kit, do not double-count it. |

**Face partner (assumed):** a second 20 mm face built to the same PHASE0.md list, **or** a fixture plate with mating receptacles, pin bores, and six contacts. The repo does not specify a partner-only fixture BOM. Cost is therefore **about one more copy of the unique face hardware**, also mostly TBD, or a custom fixture whose price is TBD.

**Rough Phase 0 article + partner total:** only the magnet line currently has a repo-linked price (~$1–3 per face, so ~$2–6 for article + partner). All other unique face hardware is **ASSUMED, price TBD**. Adding a 25 mm cell on the same bench is a separate $17–42 (on-cell increment) or $32–82 (first-buy) as above. This file does not invent a closed dollar total for the face article.

---

## Test gates

This paper adds no test IDs and no bars. Existing Phase 0 gates and the 25 mm measurement sequence live in [PHASE0.md](../PHASE0.md), [PHASE1.md](../PHASE1.md) (P0-T1…T5), [TEST_RIG.md](TEST_RIG.md), and [MEASUREMENT_CARD.md](../MEASUREMENT_CARD.md). TBD, no pass bar set, for anything this file does not already cite from those sources.

---

## Assumptions

- In-repo prices are approximate as of 2026-11-23, single-unit, and must be re-verified before a PO. They are modeled / paper figures, not measured costs and not quotes.
- Every ASSUMED row is not a repo-specified part. Web lookups are dated 2026-11-27 and are marked as such.
- Where a price could not be confirmed, the cell is “ASSUMED, price TBD,” not a guess.
- Coil turn counts and resistances cited from HARDWARE_MAPPING / PHASE0 (~0.74–0.75 Ω) are estimates or paper figures, not measurements.

---

## Related

- [bom/bom_netlist.txt](../../bom/bom_netlist.txt)
- [MIN_PARTS.md](../MIN_PARTS.md), [BUILD.md](../BUILD.md), [DESIGN.md](../DESIGN.md), [LOCKS.md](../LOCKS.md)
- [PHASE0.md](../PHASE0.md), [FIRST_ARTICLE.md](../FIRST_ARTICLE.md), [HARDWARE_MAPPING.md](../HARDWARE_MAPPING.md)
- [TEST_RIG.md](TEST_RIG.md)
- TI [DRV8871 datasheet Rev B](https://www.ti.com/lit/ds/symlink/drv8871.pdf)

Paper until measured. Credit follows data.
