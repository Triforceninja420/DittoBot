#!/usr/bin/env python3
"""Sanity checks for sims/mars_bacteria_swarm_sim_v2_11.py.

Loads the sim by file path (not as a package import) so the inlined
v2.9 reference block doesn't collide with anything else. First load can
take a few seconds — that's expected.
"""
import importlib.util
import math
import os
import random
import sys
import unittest

SIM_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "sims",
    "mars_bacteria_swarm_sim_v2_11.py",
)


def _load_sim():
    spec = importlib.util.spec_from_file_location("mars_swarm_v211", SIM_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["mars_swarm_v211"] = mod
    spec.loader.exec_module(mod)
    return mod


class TestMarsSwarmSimConstants(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sim = _load_sim()

    def test_key_constants_exist_and_are_sane(self):
        s = self.sim
        self.assertGreater(s.TARGET_KG, 0)
        self.assertGreater(s.PER_UNIT_KG, 0)
        self.assertGreater(s.INOCULUM, 0)
        self.assertGreater(s.DOUBLING_SOLS, 0)
        self.assertLess(s.SURVIVAL_FLOOR, s.SURVIVAL_CEILING)
        self.assertEqual(len(s.PERCH_LEVELS), 4)
        self.assertEqual(s.STRESS_TIERS, ["baseline", "moderate", "severe"])
        self.assertTrue(s.OX_PERCELL_OVERRIDE_ENABLED)
        # Only binding cells are in the override dict; baseline uses the default factor.
        self.assertGreaterEqual(len(s.OX_PERCELL_OVERRIDE), 4)

    def test_oxidative_override_covers_binding_cells(self):
        s = self.sim
        binding = [
            ("moderate", 0.50), ("moderate", 0.75),
            ("moderate", 1.00), ("moderate", 1.50), ("severe", 1.50),
        ]
        for cell in binding:
            self.assertIn(cell, s.OX_PERCELL_OVERRIDE)
            val = s.OX_PERCELL_OVERRIDE[cell]
            self.assertGreaterEqual(val, 0.97)
            self.assertLessEqual(val, 1.0)


class TestMarsSwarmSimRunOnce(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sim = _load_sim()

    def test_single_run_returns_finite_dict(self):
        s = self.sim
        rng = random.Random(42)
        # run_once(rng, perchlorate_pct, tier, ...)
        result = s.run_once(rng, 0.50, "baseline")
        self.assertIsInstance(result, dict)
        for key, val in result.items():
            if isinstance(val, (int, float)):
                self.assertFalse(math.isnan(val), f"{key} is NaN")
                self.assertFalse(math.isinf(val), f"{key} is inf")


if __name__ == "__main__":
    unittest.main()
