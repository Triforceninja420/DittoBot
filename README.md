# DittoBot
Programmable Matter Voxel Lattice Robot
# DittoBot / Voxel Box: Modular Cell Mechanical & Electrical Architecture

This document details the engineering specifications, geometric baselines, electrical layouts, and magnetic flux mechanics for the **DittoBot / Voxel Box** modular robotics platform. 

The design is optimized for autonomous reconfigurability, structural rigidity, and zero steady-state energy consumption across connected lattices.

---

## 1. Mechanical Architecture & Parametric Geometry

The structural frame is built around a cubic unit cell designed for rapid additive manufacturing (FDM/SLA) or precision injection molding.


+-----------------------+
/                       /|
/       [ EPM CORE ]    / |
/      o   (Top)   o    /  |
+-----------------------+   |
|                       |   |
|   o               o   |   |
|                       |   +
|       [ EPM CORE ]    |  /
|         (Front)       | /
|   o               o   |/
+-----------------------+

### Geometric Dimensions
* **External Envelope:** $25.0\text{ mm} \times 25.0\text{ mm} \times 25.0\text{ mm}$
* **Internal Electronics Cavity:** $21.8\text{ mm} \times 21.8\text{ mm} \times 21.8\text{ mm}$ (clearance for MCU, H-bridge driver, power routing)
* **Nominal Wall Thickness:** $1.6\text{ mm}$
* **Latching Core Bore:** $\varnothing 8.2\text{ mm} \times 4.0\text{ mm}$ depth (centered on all 6 faces)
* **Interconnect Port Clearance:** 4-pin radial pitch at radius $r = 6.0\text{ mm}$, bore $\varnothing 2.5\text{ mm} \times 1.2\text{ mm}$ counterbore

### Mating & Self-Alignment Features
* **Centering Pocket:** Recessed magnet pockets provide shear keying when adjacent nodes engage.
* **Hermetic Clearance:** Exterior chamfers ($0.5\text{ mm} \times 45^\circ$) along all 12 outer edges prevent edge binding during neighbor-roll maneuvers.

---

## 2. Magnetic Latching: Bi-Stable EPM Physics

Latching relies on an Electro-Permanent Magnet (EPM) configuration pairing a high-coercivity magnet with a low-coercivity reversible magnet surrounded by an excitation coil.


[ LATCHED STATE ]                      [ RELEASED STATE ]
(Flux loops through target)            (Flux cancels internally)
+---------------+                      +---------------+
|  NdFeB (N52)  |                      |  NdFeB (N52)  |
|     [ N ]     |                      |     [ N ]     |
|     [ S ]     |                      |     [ S ]     |
+---------------+                      +---------------+
|  Alnico 5 (N) |                      |  Alnico 5 (S) |  <-- Inverted by pulse
+---------------+                      +---------------+
|||                                    (X)
[ Mating Voxel ]                       [ Low Fringe Flux ]

### Core Specifications
* **Permanent Element:** Neodymium NdFeB N52 ($B_r \approx 1.4\text{ Tesla}$)
* **Switchable Element:** Alnico 5 ($B_r \approx 1.25\text{ Tesla}, H_c \approx 50\text{ kA/m}$)
* **Coil Winding:** 120 turns of $0.15\text{ mm}$ (AWG 34) enameled copper wire
* **Drive Pulse:** $25\text{ ms}$ at $\pm 1.2\text{ A}$ (transient energy $\approx 150\text{ mJ}$)

### Theoretical Hold Force
Hold force across face air gap $g$ is derived via the Maxwell Stress Tensor:

$$F = \frac{B^2 \cdot A}{2\mu_0}$$

* **Pole Face Area ($A$):** $\pi \cdot (0.004\text{ m})^2 \approx 5.026 \times 10^{-5}\text{ m}^2$
* **Latched Field ($B_{\text{on}}$ at $0.1\text{ mm}$ gap):** $\approx 1.20\text{ T} \implies F_{\text{hold}} \approx 28.8\text{ N}$
* **Released Field ($B_{\text{off}}$ at $0.1\text{ mm}$ gap):** $\approx 0.14\text{ T} \implies F_{\text{residual}} \approx 0.37\text{ N}$
* **Decoupling Ratio:** $> 75:1$

---

## 3. Electrical Architecture & Pinout

Each cell operates as an autonomous microcontroller node capable of driving localized latch pulses and communicating with immediately adjacent neighbors.


+-----------------------+
|      XIAO RP2040      |
|                       |
| GPIO0 (IN1)   3V3/VCC |----+ (Power Rail)
| GPIO1 (IN2)       GND |----| (System Ground)
| GPIO6 (SDA)     GPIO7 |    |
+-----------------------+    |
|          |            |
v          v            |
+-----------------------+    |
|   DRV8837C H-Bridge   |    |
|                       |    |
(Power Rail) -----| VM/VCC            GND |----+
| OUT1             OUT2 |
+-----------------------+
|               |
+---[ COIL ]----+

### Face Interconnect Pin Assignment
Each of the 6 faces features a 4-pad interface arranged quadratically:

| Pad # | Signal | Description |
| :---: | :---: | :--- |
| **1** | `VBUS` | System power bus ($3.3\text{V} - 5.0\text{V}$, continuous $2\text{A}$ rated) |
| **2** | `GND` | Common ground reference |
| **3** | `DATA_A` | Dynamic face-neighbor communication (`SDA` / UART TX) |
| **4** | `DATA_B` | Dynamic face-neighbor synchronization (`SCL` / UART RX) |

---

## 4. State Transition & Power Dissipation Profile

Because both magnetic materials maintain saturation without an applied external field, continuous hold requires **zero current**. Power is only drawn during state transitions.

```text
Current (A)
   ^
1.2|      +---+ (25ms Switch Pulse)
   |      |   |
0.0+------+   +-----------------------------------> Time (t)
          ^   ^
        Pulse End -> Driver set to Hi-Z / LOW
        Power Draw: 0.0 W (Indefinite Hold)

 * Latch Command Issued: Microcontroller pulses IN1 = HIGH, IN2 = LOW for 25\text{ ms}.
 * Polarization: Alnico core aligns parallel to the NdFeB core. High-density magnetic circuit closes through the neighboring cell face.
 * Quench: Microcontroller pulls both IN1 and IN2 to LOW. Driver outputs enter high-impedance/ground state.
 * Passive Retention: Cells remain mechanically bound under full rated force (>28\text{ N}) indefinitely without heat generation.
 * Release Command Issued: Microcontroller pulses IN1 = LOW, IN2 = HIGH for 25\text{ ms} to reverse Alnico polarity, routing internal flux away from the exterior face.

