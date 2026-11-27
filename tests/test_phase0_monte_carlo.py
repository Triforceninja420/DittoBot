#!/usr/bin/env python3
"""Sanity checks for sims/phase0_monte_carlo.py."""
import importlib.util
import os
import sys
import unittest

SIM_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "sims",
    "phase0_monte_carlo.py",
)


def _load_sim():
    spec = importlib.util.spec_from_file_location("phase0_mc", SIM_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["phase0_mc"] = mod
    spec.loader.exec_module(mod)
    return mod


class TestPhase0MonteCarlo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sim = _load_sim()

    def test_constants(self):
        s = self.sim
        self.assertEqual(s.N_TRIALS, 100_000)
        self.assertEqual(s.SEED, 7)
        self.assertEqual(s.FORENSIC_SEED, 13)
        self.assertGreater(s.T1_OFFSET_SIGMA_MM, 0)
        self.assertGreater(s.T1_ANGLE_SIGMA_DEG, 0)
        self.assertGreater(s.T3_SHEAR_SIGMA, 0)
        self.assertGreater(s.T5_CYCLES_SIGMA, 0)
        self.assertGreater(s.T3_LAT_LIMIT_MM, 0)
        self.assertGreater(s.T3_VEL_LIMIT_MS, 0)

    def test_run_trial_signature(self):
        s = self.sim
        import random
        rng = random.Random(7)
        frng = random.Random(13)
        saw_pass = saw_fail = False
        for _ in range(200):
            result = s.run_trial(rng, frng)
            self.assertIsInstance(result, tuple)
            # t1..t5 plus the T3 forensic record
            self.assertEqual(len(result), 6)
            for item in result[:5]:
                self.assertIsInstance(item, bool)
            # 6th element is T3 failure dict or None (None iff T3 passed)
            t3_fail = result[5]
            if result[2]:
                self.assertIsNone(t3_fail)
                saw_pass = True
            else:
                self.assertIsInstance(t3_fail, dict)
                for key in ("vel", "lat", "spr", "shear_raw", "shear_eff"):
                    self.assertIn(key, t3_fail)
                saw_fail = True
            if saw_pass and saw_fail:
                break
        self.assertTrue(saw_pass)
        self.assertTrue(saw_fail)


if __name__ == "__main__":
    unittest.main()
