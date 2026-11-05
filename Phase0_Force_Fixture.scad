// DittoBot / Voxel Box Bot
// Phase 0 Exact Force Fixture — OpenSCAD
// Independent Fab Package addition  |  2026-11-05
// Design owned by Craig. Started Nov/Dec 2025. Programmable matter.
//
// Purpose: clamp one finished EPM with pole faces parallel and exposed
// so any makerspace can pull ≥ 3.0 N ON / < 0.3 N OFF in ten minutes.
// Print in PLA/PETG or machine from plastic/aluminum. Non-magnetic preferred.
//
// Units: millimeters
// Export: F6 render → STL for the clamp body and the steel-target holder.

$fn = 64;

// ---- EPM envelope (finished coil) ----
epm_od          =  8.5;     // max allowed coil OD
epm_length      =  9.0;     // pole height
pole_face_d     =  5.0;

// ---- Clamp body ----
clamp_wall      =  3.0;
clamp_base_z    =  4.0;
clamp_opening   =  epm_od + 0.4;   // slight clearance
pull_hook_d     =  4.0;            // for luggage-scale hook or string

module clamp_body() {
    difference() {
        // outer block
        cube([epm_od + 2*clamp_wall, epm_length + 2*clamp_wall, epm_length + clamp_base_z], center=true);
        // EPM pocket (open toward working face, +Z)
        translate([0, 0, clamp_base_z/2 + 0.1])
            cube([clamp_opening, epm_length + 0.4, epm_length + 1], center=true);
        // pull-hook hole through the base (for axial pull)
        translate([0, 0, -epm_length/2 - clamp_base_z/2 + 1])
            cylinder(h=clamp_base_z + 2, d=pull_hook_d, center=true);
    }
}

// ---- Mild-steel target (reference only — cut real steel separately) ----
// This module is for a 3D-printed alignment jig; the actual target is steel.
module steel_target_jig() {
    difference() {
        cube([30, 30, 4], center=true);
        // recess that seats a 20×20×3 mm mild-steel coupon flush
        translate([0, 0, 0.5])
            cube([20.2, 20.2, 3.2], center=true);
    }
}

// Render both
translate([0, 0, 10]) clamp_body();
translate([40, 0, 0]) steel_target_jig();
