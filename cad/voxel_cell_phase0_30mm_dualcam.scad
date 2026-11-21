// DittoBot Phase 0 Face — 30 mm dual-cam staggered (rev 2026-11-21)
// Design owned by Craig. Programmable matter. Paper only until measured.
//
// Envelope: 30.00 x 30.00 mm, 6061-T6, 1.00 mm nominal
// Magnet: NdFeB N52 Ø6.0 x 6.0 mm, axial, centered
// Coil: 40 turns 34 AWG around magnet (~0.75 ohm cold)
// Cams: dual 8 mm radius, staggered (8,8) + (22,22), steel-backed polymer tips
// Latch: 2x hardened steel pins + retraction actuator
// Seating spring: 5 N
// Contacts: 6x pogo/leaf on hex ring r=4.20 mm
// Corner mounts: 4x Ø1.70 mm at (±12.80, ±12.80)
// Capture: ±2.50 mm lateral, ±6-7 deg, chamfer + side ridges
//
// Units: mm. Origin at face center, Z out of docking face.
// Render: F6. Export STL for fab. Do not mix with 25 mm cell numbers.
// Magnet pocket: BLIND 0.75 mm deep (not through) — heat spreader back intact.

$fn = 64;

// ---------- Parameters ----------
plate_x = 30.0;
plate_y = 30.0;
plate_t = 1.0;
edge_break = 0.25;

magnet_d = 6.0;
magnet_h = 6.0;
pocket_d = magnet_d + 0.10; // 6.10 mm
pocket_depth = 0.75; // blind, per spec (0.70–0.80 accept)
coil_turns = 40;
coil_wire_d = 0.16; // 34 AWG approx
coil_wind_od = magnet_d + 2 * 3 * coil_wire_d; // rough 3-layer wind
coil_wind_h = magnet_h + 2 * coil_wire_d;

cam_r = 8.0;
cam_core_t = 2.0;
cam_tip_t = 1.5; // polymer tip thickness, steel-backed
cam_tip_w = 8.0; // contact width
cam1 = [8, 8];
cam2 = [22, 22];

pin_d = 1.80;
pin_bore = 1.85;
pin_engagement = 3.0;
retraction_coil_d = 4.0;
retraction_coil_h = 6.0;

spring_force_n = 5.0; // seating spring, perimeter representation

contact_ring_r = 4.20;
contact_hole_d = 1.10;
contact_angles = [30, 90, 150, 210, 270, 330];

mount_d = 1.70;
mount_pos = 12.80;

chamfer = 0.50;
ridge_h = 0.50;
ridge_w = 0.60;

// ---------- Plate ----------
module plate() {
    difference() {
        // main body with edge break
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

// ---------- Blind magnet pocket (0.75 mm deep, back stays heat spreader) ----------
module magnet_pocket() {
    // cut from docking face (top, +Z) down 0.75 mm; does NOT break through
    translate([0, 0, plate_t/2 - pocket_depth/2])
    cylinder(d=pocket_d, h=pocket_depth, center=true);
    // optional Ø1.20 mm lead exit at inner pocket edge (spec: optional)
    // translate([pocket_d/2, 0, plate_t/2 - pocket_depth])
    // cylinder(d=1.20, h=0.5, center=true);
}

// ---------- Dual staggered cams ----------
module cam_core(pos) {
    // steel/stainless core, 8 mm radius disc, 2 mm thick
    color("Silver")
    translate([pos[0]-15, pos[1]-15, plate_t/2 + cam_core_t/2])
    cylinder(r=cam_r, h=cam_core_t, center=true);
}

module cam_tip(pos) {
    // polymer tip, steel-backed, 8 mm contact width, 1.5 mm thick
    color("LightBlue")
    translate([pos[0]-15, pos[1]-15, plate_t/2 + cam_core_t + cam_tip_t/2])
    cylinder(r=cam_r, h=cam_tip_t, center=true);
}

module cam(pos) {
    cam_core(pos);
    cam_tip(pos);
}

// ---------- Latch pins (2) ----------
module pin_bore_hole() {
    cylinder(d=pin_bore, h=plate_t+1, center=true);
}

module retraction_actuator() {
    // small solenoid ~1/3 g, represented as coil cylinder beside pin bore
    color("DarkGreen")
    cylinder(d=retraction_coil_d, h=retraction_coil_h, center=true);
}

// ---------- Seating spring (5 N, perimeter ring representation) ----------
module seating_spring() {
    color("Gold")
    for (a = [0:45:315]) {
        translate([14.5*cos(a), 14.5*sin(a), 0])
        rotate([90, 0, a])
        cylinder(d=0.8, h=2.0, center=true);
    }
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
    // chamfer on top face edge
    color("Orange")
    difference() {
        cube([plate_x, plate_y, chamfer], center=true);
        translate([0, 0, -chamfer/2])
        cube([plate_x - 2*chamfer, plate_y - 2*chamfer, chamfer+0.1], center=true);
    }
    // side ridges 0.50 mm high, 0.60 mm wide
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
        cam(cam1);
        cam(cam2);
        seating_spring();
        capture_features();
        // retraction actuators beside pin bores (schematic positions)
        translate([3, 0, plate_t/2 + retraction_coil_h/2]) retraction_actuator();
        translate([-3, 0, plate_t/2 + retraction_coil_h/2]) retraction_actuator();
    }
    // BLIND magnet pocket — 0.75 mm deep from docking face, back intact as heat spreader
    magnet_pocket();
    // pin bores (2)
    translate([2, 1, 0]) pin_bore_hole();
    translate([-2, -1, 0]) pin_bore_hole();
    // contact holes
    for (a = contact_angles) contact_hole(a);
    // corner mounts
    mount_hole(mount_pos, mount_pos);
    mount_hole(mount_pos, -mount_pos);
    mount_hole(-mount_pos, mount_pos);
    mount_hole(-mount_pos, -mount_pos);
}

// dimension callouts (commented — enable in OpenSCAD for 2D export)
// # projection(cut=true) children();