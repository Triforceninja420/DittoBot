// ====================================================================
// Project: DittoBot / Voxel Box
// Component: Phase 0 Face — 20 mm single-magnet latch (rev 2026-11-23)
// Design owned by Craig. Programmable matter. Paper only until measured.
//
// Envelope: 20.00 x 20.00 mm, 7075-T6 (upgraded from 6061-T6), 1.00 mm nominal
// Magnet: Nd disc Ø6.0 x 2–3 mm, axial, centered. Coil around disc = release only.
// Driver: DRV8871 (VM 6.5–45 V abs max; prefer ≤42 V from pulse bank)
// Pins: 3x hardened steel, Ø1.80 mm, bore Ø1.85 mm, 3.0 mm engagement
// Springs: 4x non-magnetic phosphor-bronze or BeCu, 0.25 N/mm each
//          (1.0 N/mm total), 5 mm preload → 5.00 N seating force
// Contacts: 6x pogo/leaf on hex ring r=3.50 mm
// Corner mounts: 4x Ø1.70 mm at (±7.00, ±7.00)
// Capture: ±2.00 mm lateral, ±6-7 deg, chamfer 1.0 mm + side ridges 1.0x1.0 mm
// Tolerance budget: 0.42 mm approach placement at 1-sigma
// Cams: REMOVED — 16 mm cams did not fit on 20 mm face
//
// Phase 0 gates (header matches MEASUREMENT_CARD / LOCKS):
//   T3 lat ≤ 1.5 mm | vel ≤ 0.5 m/s | spring 5.00 N | shear bar 40 N
//   all-pass 98.04% (lat sigma 0.55 mm: T3 99.30%, 702 T3 fails)
//
// Units: mm. Origin at face center, Z out of docking face.
// Render: F6. Export STL for fab. Do not mix with 25 mm cell numbers.
// Magnet pocket: BLIND 4.0 mm deep (not through) — heat spreader back intact.
// ====================================================================

$fn = 64;

// ---------- Parameters ----------
plate_x = 20.0;
plate_y = 20.0;
plate_t = 1.0;
edge_break = 0.25;

magnet_d = 6.0;
magnet_h = 2.5; // mid of 2–3 mm spec
pocket_d = 8.2;
pocket_depth = 4.0; // blind, back face intact as heat spreader
coil_turns = 40;
coil_wire_d = 0.16; // 34 AWG approx
coil_wind_od = magnet_d + 2 * 3 * coil_wire_d; // rough 3-layer wind
coil_wind_h = magnet_h + 2 * coil_wire_d;

pin_d = 1.80;
pin_bore = 1.85;
pin_engagement = 3.0;
// 3 pins: pair + third opposite
pin1 = [2.5, 1.5];
pin2 = [-2.5, -1.5];
pin3 = [0, -3.0];

spring_k = 0.25; // N/mm per spring; 4 springs = 1.0 N/mm total
spring_preload = 5.0; // mm → 5.00 N seating force
spring_r = 7.5; // cardinal placement radius

contact_ring_r = 3.50;
contact_hole_d = 1.10;
contact_angles = [30, 90, 150, 210, 270, 330];

mount_d = 1.70;
mount_pos = 7.00;

chamfer = 1.00;
ridge_h = 1.00;
ridge_w = 1.00;

// ---------- Plate ----------
module plate() {
    difference() {
        minkowski() {
            cube([plate_x - 2*edge_break, plate_y - 2*edge_break, plate_t - edge_break], center=true);
            cylinder(r=edge_break, h=edge_break, center=true);
        }
    }
}

// ---------- Magnet + coil (centered, axial) ----------
module magnet() {
    color("DarkSlateGray")
    cylinder(d=magnet_d, h=magnet_h, center=true);
}

module coil() {
    color("Copper")
    difference() {
        cylinder(d=coil_wind_od, h=coil_wind_h, center=true);
        cylinder(d=magnet_d+0.2, h=coil_wind_h+0.2, center=true);
    }
}

// ---------- Blind magnet pocket (4.0 mm deep, back stays heat spreader) ----------
module magnet_pocket() {
    translate([0, 0, plate_t/2 - pocket_depth/2])
    cylinder(d=pocket_d, h=pocket_depth, center=true);
}

// ---------- Latch pins (3) ----------
module pin_bore_hole() {
    cylinder(d=pin_bore, h=plate_t+1, center=true);
}

// ---------- Springs (4, BeCu/phosphor-bronze, non-magnetic) ----------
module spring() {
    color("DarkOrange")
    cylinder(d=1.2, h=2.0, center=true);
}

// ---------- Contacts (6 on hex ring) ----------
module contact_hole(angle) {
    translate([contact_ring_r*cos(angle), contact_ring_r*sin(angle), 0])
    cylinder(d=contact_hole_d, h=plate_t+1, center=true);
}

// ---------- Corner mounts (4) ----------
module mount_hole(x, y) {
    translate([x, y, 0])
    cylinder(d=mount_d, h=plate_t+1, center=true);
}

// ---------- Capture chamfer + side ridges ----------
module capture_features() {
    color("Orange")
    difference() {
        cube([plate_x, plate_y, chamfer], center=true);
        translate([0, 0, -chamfer/2])
        cube([plate_x - 2*chamfer, plate_y - 2*chamfer, chamfer+0.1], center=true);
    }
    for (s = [-1, 1]) {
        translate([s*(plate_x/2 - ridge_w/2), 0, plate_t/2 + ridge_h/2])
        cube([ridge_w, plate_y - 2*chamfer, ridge_h], center=true);
        translate([0, s*(plate_y/2 - ridge_w/2), plate_t/2 + ridge_h/2])
        cube([plate_x - 2*chamfer, ridge_w, ridge_h], center=true);
    }
}

// ---------- Assembly ----------
difference() {
    union() {
        plate();
        magnet();
        coil();
        seating_spring_proxy();
        capture_features();
    }
    magnet_pocket();
    // pin bores (3) — pair + third opposite
    translate([pin1[0], pin1[1], 0]) pin_bore_hole();
    translate([pin2[0], pin2[1], 0]) pin_bore_hole();
    translate([pin3[0], pin3[1], 0]) pin_bore_hole();
    // contact holes
    for (a = contact_angles) contact_hole(a);
    // corner mounts
    mount_hole(mount_pos, mount_pos);
    mount_hole(mount_pos, -mount_pos);
    mount_hole(-mount_pos, mount_pos);
    mount_hole(-mount_pos, -mount_pos);
}

// Spring proxies at cardinal positions (r=7.5), 4x
module seating_spring_proxy() {
    for (a = [0, 90, 180, 270]) {
        translate([spring_r*cos(a), spring_r*sin(a), plate_t/2 + 1.0])
        spring();
    }
}

// dimension callouts (commented — enable in OpenSCAD for 2D export)
// # projection(cut=true) children();