# CONTROL_APP.md — Lattice control system

Design owner: Craig.  
Date: 2026-11-19.  
Status: outline. Not implemented. Compatible with the current 25 mm baseline.

A lightweight control app that talks to one leader cell (or a USB/serial bridge) and commands the lattice. Same core logic on mobile and PC so the interface stays consistent.

## Platforms
- **Mobile** (iOS / Android): primary field tool. Touch lattice builder, status at a glance, collapse button.
- **PC** (Windows / macOS / Linux): same UI in a window or browser. Better for larger assemblies and logging.

Both talk to the same protocol. A web version can serve both if preferred.

## Core features
- Visual lattice builder: place, move, and delete cells in a 3D or 2.5D grid. Push the resulting docking plan.
- Per-face status: soft-dock, hard-lock (pin seated), fault, temperature.
- Pulse and thermal controls: fire release pulse, view plate temp, enforce the governor.
- Collapse to brick: one button that runs the inward-compaction sequence already described in POST_2040_OUTLOOK.md.
- Power and mesh health: shared bus voltage, leader status, simple battery estimate if energy cells are present.
- Later hooks (do not build yet): thruster face enable, pressure-hull mode, rad-hard telemetry.

## Control flow
1. App connects to leader cell (BLE, Wi-Fi, or USB serial).
2. User builds or loads a shape.
3. App sends state-machine commands (Approach → Soft Dock → Verify → Hard Lock).
4. Cells report lock state and temperature back up the mesh.
5. App shows live status and blocks unsafe moves (low power, over-temp, incomplete lock).

## What it does not do
- Does not replace the measurement card.
- Does not claim flight, deep-ocean, or suit mode until those faces exist.
- Does not change the locked pocket or pin geometry.

## Implementation notes
- Start with a Python script or simple web UI that talks over serial to the existing pulse driver firmware.
- Mobile can wrap the same API later (React Native, Flutter, or a progressive web app).
- Keep the command set small and documented so any language can drive it.

See BUILD.md, DESIGN.md, and firmware/pulse_driver.cpp for the current cell interface this app would drive.

Paper until the first multi-cell demo exists.
