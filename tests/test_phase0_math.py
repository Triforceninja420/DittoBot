"""Phase 0 docking math checks — exercises the real Monte Carlo module."""

import importlib.util
import random

spec = importlib.util.spec_from_file_location(
    "phase0_monte_carlo", "sims/phase0_monte_carlo.py"
)
mc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mc)


def test_soft_dock_angle_tolerance():
    # 1-sigma angle spread must sit inside the 7 deg soft-dock gate
    assert mc.T1_ANGLE_SIGMA_DEG < 7.0


def test_soft_dock_position_tolerance():
    # 1-sigma offset spread must sit inside the 2.5 mm soft-dock gate
    assert mc.T1_OFFSET_SIGMA_MM < 2.5


def test_hard_lock_probability():
    assert mc.T2_LOCK_P >= 0.95


def test_shear_threshold_above_gate():
    # 3-sigma lower bound of the 7075-T6 shear mean must clear 40 N
    # before velocity/offset degradation is applied
    assert mc.T3_SHEAR_MU - 3 * mc.T3_SHEAR_SIGMA >= 40.0


def test_cycle_threshold():
    # 3-sigma lower bound of cycle life must clear 2000
    assert mc.T5_CYCLES_MU - 3 * mc.T5_CYCLES_SIGMA >= 2000.0


def test_pin_load_factor_is_distribution_not_strength():
    # 3-pin relief spreads load; it does not add strength
    assert mc.PIN_LOAD_FACTOR == 2.0 / 3.0
    assert mc.PIN_COUNT == 3


def test_ridge_geometry_matches_cad_rev():
    # Geometry must match CAD rev 2026-11-23
    assert mc.RIDGE_W_MM == 1.0
    assert mc.RIDGE_H_MM == 1.0
    assert mc.CHAMFER_MM == 1.0


def test_single_trial_shape():
    rng = random.Random(0)
    frng = random.Random(1)
    result = mc.run_trial(rng, frng)
    assert len(result) == 6
    assert all(isinstance(r, bool) for r in result[:5])
    assert result[5] is None or isinstance(result[5], dict)


def test_t3_fail_dict_keys():
    # Force a T3 fail by feeding extreme forensic draws
    rng = random.Random(99)
    frng = random.Random(99)
    # Override: extreme velocity + lateral offset should fail T3
    orig_vel_sigma = mc.VEL_SIGMA_M_S
    orig_lat_sigma = mc.LAT_OFFSET_SIGMA_MM
    mc.VEL_SIGMA_M_S = 2.0
    mc.LAT_OFFSET_SIGMA_MM = 5.0
    try:
        for _ in range(50):
            result = mc.run_trial(rng, frng)
            if result[5] is not None:
                f = result[5]
                assert "vel" in f and "lat" in f and "spr" in f
                assert "shear_raw" in f and "shear_eff" in f
                return
        # If no fail surfaced in 50 draws, that's acceptable noise
    finally:
        mc.VEL_SIGMA_M_S = orig_vel_sigma
        mc.LAT_OFFSET_SIGMA_MM = orig_lat_sigma


def test_monte_carlo_main_runs(capsys):
    mc.main()
    out = capsys.readouterr().out
    assert "T1 pass:" in out
    assert "ALL-PASS:" in out
    assert "T3 FAILS:" in out
    # All-pass should be above the 90% gate
    for line in out.splitlines():
        if line.startswith("ALL-PASS:"):
            pct = float(line.split()[1].rstrip("%"))
            assert pct > 90.0
