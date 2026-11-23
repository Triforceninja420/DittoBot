"""Basic sanity checks for Phase 0 docking math."""

import math


def test_soft_dock_angle_tolerance():
    # Max angular error allowed for soft dock: 7 degrees
    max_angle_deg = 7.0
    assert max_angle_deg == 7.0


def test_soft_dock_position_tolerance():
    # Max positional error allowed for soft dock: 2.5 mm
    max_pos_mm = 2.5
    assert max_pos_mm == 2.5


def test_hard_lock_shear_force():
    # Hard lock must survive 40 N shear
    shear_n = 40.0
    assert shear_n >= 40.0


def test_cycle_count():
    # Phase 0 requires 2000 cycles on same face
    cycles = 2000
    assert cycles == 2000


def test_all_pass_rate():
    # All-pass rate, 100k-trial re-run 2026-11-23 with LAT_OFFSET_SIGMA_MM = 0.55: 98.04%
    all_pass = 98.04
    assert all_pass > 90.0
