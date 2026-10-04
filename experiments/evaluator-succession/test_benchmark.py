"""Structural tests only; no hypothesis outcomes are examined here."""
import json
import unittest

import numpy as np

from benchmark import ACTIONS, ROOT, candidates, choose, evaluate, make_worlds, production, run_arm, softmax


class BenchmarkChecks(unittest.TestCase):
    def setUp(self):
        self.cfg = json.loads((ROOT/"config.json").read_text())
        self.cfg.update(worlds=2, epochs=2, rounds_per_epoch=1, correction_every=1)
        self.worlds = make_worlds(self.cfg)

    def test_action_geometry_and_stable_streams(self):
        self.assertEqual(ACTIONS.shape, (15, 3))
        np.testing.assert_allclose(ACTIONS.sum(-1), 1)
        self.assertTrue((ACTIONS >= 0).all())
        same = make_worlds(self.cfg)
        for k in self.worlds:
            np.testing.assert_array_equal(self.worlds[k], same[k])
        other = make_worlds(self.cfg, donor=True)
        self.assertFalse(np.array_equal(self.worlds["skills"], other["skills"]))

    def test_allocation_normalization_and_floor(self):
        outputs = np.array([[[1., 0., 0.]]*8, [[0., 1., 0.]]*8])
        p, w, _ = evaluate(outputs, np.array([[1., 0., 0.], [0., 1., 0.]]), .75, self.cfg)
        np.testing.assert_allclose(p, 1/8)
        np.testing.assert_allclose(w, [.75, .25])
        outputs[0, 0] = [20., 0., 0.]
        p, _, _ = evaluate(outputs, np.array([[1., 0., 0.], [0., 1., 0.]]), .75, self.cfg)
        np.testing.assert_allclose(p.sum(-1), 1)
        self.assertTrue((p >= self.cfg["allocation_floor"]/8).all())

    def test_vectorized_production_matches_brute_force(self):
        outputs = self.worlds["features"][:, :, 6].copy()
        rubric = np.array([[.6, .3, .1], [.3, .6, .1]])
        uniforms = self.worlds["prod"][:, 0, 0]
        actual = production(outputs, rubric, .75, self.worlds, uniforms, self.cfg)
        for b in range(2):
            for i in range(8):
                values = []
                for a in range(15):
                    trial = outputs[b:b+1].copy()
                    trial[0, i] = self.worlds["features"][b, i, a]
                    p, w, _ = evaluate(trial, rubric[b:b+1], .75, self.cfg)
                    values.append(p[0, i]+self.cfg["common_value_weight"]*w[0])
                chosen = choose(softmax(self.cfg["production_temperature"]*np.array(values)), uniforms[b, i])
                np.testing.assert_allclose(actual[b, i], self.worlds["features"][b, i, chosen])

    def test_neighbor_validity_and_reference(self):
        phi = np.array([[1., 0., 0.], [.5, .5, 0.]])
        proposals, valid = candidates(phi, .25, True, self.cfg)
        self.assertTrue(np.all(proposals[valid] >= -1e-12))
        np.testing.assert_allclose(proposals[valid].sum(-1), 1)
        np.testing.assert_allclose(proposals[:, 7], [[.25, .75, 0.]]*2)
        self.assertTrue(valid[:, 0].all())
        self.assertFalse(candidates(phi, .25, False, self.cfg)[1][:, 7].any())

    def test_rule_timing_replay_and_audit_invariants(self):
        donor = run_arm(self.cfg, make_worlds(self.cfg, donor=True), "stable", "endogenous")
        for arm in ("fixed", "endogenous", "independent", "rotating", "replay", "protected"):
            h = run_arm(self.cfg, self.worlds, "stable", arm, replay=donor if arm == "replay" else None)
            np.testing.assert_allclose(h["before_rubric"][:, 1], h["after_rubric"][:, 0])
            np.testing.assert_allclose(h["after_rubric"].sum(-1), 1)
            self.assertTrue((h["after_rubric"] >= -1e-12).all())
            np.testing.assert_allclose(h["net"], h["gross"]-h["admin_cost"])
            if arm == "fixed":
                np.testing.assert_allclose(h["before_rubric"], np.broadcast_to(self.cfg["initial_rubric"], (2, 2, 3)))
            if arm == "replay":
                np.testing.assert_array_equal(h["before_rubric"], donor["before_rubric"])
                np.testing.assert_array_equal(h["after_rubric"], donor["after_rubric"])
            if arm == "protected":
                self.assertTrue((h["delta_value"] >= -1e-9).all())
                np.testing.assert_array_equal(h["corrected"], h["evidence_valid"])

    def test_frozen_rescoring_receipts(self):
        h = run_arm(self.cfg, self.worlds, "stable", "endogenous")
        for t in range(1):
            p0, w0, _ = evaluate(h["frozen_outputs"][:, t], h["before_rubric"][:, t], .75, self.cfg)
            p1, w1, _ = evaluate(h["frozen_outputs"][:, t], h["after_rubric"][:, t], .75, self.cfg)
            gov = h["governor"][:, t]
            np.testing.assert_allclose(h["delta_value"][:, t], w1-w0, atol=1e-12)
            np.testing.assert_allclose(h["delta_governor"][:, t], (p1-p0)[np.arange(2), gov], atol=1e-12)

    def test_independent_appointments_and_terminal_censoring(self):
        h = run_arm(self.cfg, self.worlds, "stable", "independent")
        np.testing.assert_allclose(h["appointment_probabilities"][:, 0], 1/8)
        expected = choose(np.full((2, 8), 1/8), self.worlds["appointment"][:, 0])
        np.testing.assert_array_equal(h["governor"][:, 0], expected)
        self.assertTrue((h["governor"][:, -1] == -1).all())
        self.assertFalse(h["evidence_valid"][:, -1].any())
        self.assertFalse(h["amended"][:, -1].any())


if __name__ == "__main__":
    unittest.main(verbosity=2)
