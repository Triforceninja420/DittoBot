// ====================================================================
// Project: DittoBot / Voxel Box
// Component: Modular Unit Cell Parametric Geometry
// Author: Craig Edward Ralls (2026)
// License: MIT
// Baseline: 2026-11-19 (SmCo Ø7.5 mm, axial pin hard-lock, potting)
// Pocket geometry locked: Ø8.2 × 4.0 mm. Do not change without new lock.
// ====================================================================

$fn = 60;

// Primary Unit Cell Envelope (mm)
voxel_size      = 25.0;
wall_thickness  = 1.6;

// Electro-Permanent Magnet (EPM) Core Cavity — LOCKED
epm_pocket_dia   = 8.2;
epm_pocket_depth = 4.0;

// Axial pin hard-lock (engages after magnetic soft-dock)
// Ø1.5–2.0 mm pin, 2.5–3.0 mm engagement. Offset or centered per face.
pin_dia         = 1.8;
pin_engage      = 2.8;
pin_offset      = 4.5;  // radial offset from magnetic axis so it clears the pocket

// 4-Pad Dynamic Face Interconnect
pin_pad_dia     = 2.5;
pin_pitch_radius = 6.0;
pin_pad_depth   = 1.2;

module face_ports() {
    // Centered EPM Core Recess (LOCKED)
    translate([0, 0, (voxel_size / 2) - epm_pocket_depth])
        cylinder(r = epm_pocket_dia / 2, h = epm_pocket_depth + 0.1);
    
    // Axial pin receptacle (one per face, offset)
    translate([pin_offset, 0, (voxel_size / 2) - pin_engage])
        cylinder(r = pin_dia / 2 + 0.15, h = pin_engage + 0.1);  // clearance
    
    // Quadrature Pogo Pin / Contact Pad Cutouts
    for (angle = [0, 90, 180, 270]) {
        rotate([0, 0, angle])
            translate([pin_pitch_radius, 0, (voxel_size / 2) - pin_pad_depth])
                cylinder(r = pin_pad_dia / 2, h = pin_pad_depth + 0.1);
    }
}

difference() {
    // Exterior Solid Shell
    cube([voxel_size, voxel_size, voxel_size], center = true);
    
    // Hollow Electronics & Routing Cavity (potting volume)
    cube([voxel_size - (wall_thickness * 2), 
          voxel_size - (wall_thickness * 2), 
          voxel_size - (wall_thickness * 2)], center = true);
    
    // Project Ports Across All 6 Coordinate Faces
    for (rotation = [
        [0,   0,   0],
        [180, 0,   0],
        [0,   90,  0],
        [0,  -90,  0],
        [90,  0,   0],
        [-90, 0,   0]
    ]) {
        rotate(rotation)
            face_ports();
    }
}

// Notes:
// - Magnet stack is SmCo 2:17 Ø7.5 × 3.0 mm (fits pocket with reduced winding window)
// - Cavity is fully potted in the physical build
// - PTFE lip + coating applied to faces post-print/machining
// - This SCAD adds the pin receptacle; pin itself is a separate inserted part
