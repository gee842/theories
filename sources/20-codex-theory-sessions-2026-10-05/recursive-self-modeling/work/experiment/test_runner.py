"""Independent runner checks using ONLY test seeds 7000..7010.

No dev/evaluate/freeze functions are called, and no result directories are written.
Run directly; redirect stdout/stderr to runner-tests.txt for the audit record.
The scalar variance test checks the fixed-alpha algebra; an audit-selected alpha
does not make that plug-in expression an exact post-selection variance.
"""

import math
import unittest
from unittest.mock import patch

import numpy as np

import experiment as e


SEEDS = tuple(range(7000, 7011))
PARAMS = {
    'raw': {}, 'direct': {},
    'retained': {'alpha': .5}, 'flat': {'alpha': .5}, 'repeat': {'alpha': .5},
    'audit': {'slow': .2, 'fast': .8, 'threshold': 2.},
    'joint': {'q_b': .0025}, 'joint_y_only': {'q_b': .0025},
}
COLS = ['t', 'x', 'b', 'y', 'z', 'xhat', 'v', 'h', 'u', 'xn', 'mu', 'pv', 'prob', 'buy']
C = {name: i for i, name in enumerate(COLS)}
M = {name: i for i, name in enumerate(e.METRICS)}


def checked_run(seed, world, policy, stage):
    if seed not in SEEDS:
        raise ValueError('Runner tests may use only seeds 7000..7010')
    return e.run(seed, world, policy, PARAMS[policy], stage, trace=True)


class RunnerChecks(unittest.TestCase):
    def test_nested_flat_exact_trace_metric_and_block_equality(self):
        for seed in SEEDS:
            for world in e.WORLD_NAMES:
                for stage in e.STAGES:
                    with self.subTest(seed=seed, world=world, stage=stage):
                        rv, rt, rb = checked_run(seed, world, 'retained', stage)
                        fv, ft, fb = checked_run(seed, world, 'flat', stage)
                        self.assertTrue(np.array_equal(rt, ft, equal_nan=True))
                        self.assertTrue(np.array_equal(rv, fv, equal_nan=True))
                        self.assertEqual(rb, fb)

    def test_repeat_same_behavior_and_exact_expected_extra_work(self):
        expected_units = e.HORIZON * 3 * e.WEIGHTS['estimate']
        expected_price = expected_units * e.WORK_PRICE
        self.assertAlmostEqual(expected_price, .018, places=15)
        for seed in SEEDS:
            for world in e.WORLD_NAMES:
                for stage in e.STAGES:
                    rv, rt, rb = checked_run(seed, world, 'retained', stage)
                    pv, pt, pb = checked_run(seed, world, 'repeat', stage)
                    self.assertTrue(np.array_equal(rt, pt, equal_nan=True))
                    for metric in e.METRICS:
                        if metric in ['work_units', 'work_cost', 'total_loss']:
                            continue
                        np.testing.assert_equal(rv[M[metric]], pv[M[metric]])
                    self.assertEqual(pv[M['work_units']] - rv[M['work_units']], expected_units)
                    self.assertAlmostEqual(pv[M['work_cost']] - rv[M['work_cost']], expected_price, places=13)
                    self.assertAlmostEqual(pv[M['total_loss']] - rv[M['total_loss']], expected_price, places=12)
                    self.assertEqual(pb['estimate'] - rb['estimate'], 180)
                    self.assertEqual({k: v for k, v in pb.items() if k != 'estimate'},
                                     {k: v for k, v in rb.items() if k != 'estimate'})

    def test_purchase_schedules_limits_and_action_limit(self):
        for seed in SEEDS:
            for world in e.WORLD_NAMES:
                for policy in e.POLICIES:
                    for stage in e.STAGES:
                        values, tr, blocks = checked_run(seed, world, policy, stage)
                        buys = tr[:, C['buy']].astype(bool)
                        self.assertTrue(np.all(np.flatnonzero(buys) % 5 == 0))
                        self.assertTrue(np.array_equal(buys, np.isfinite(tr[:, C['z']])))
                        self.assertEqual(values[M['sense_count']], int(np.sum(buys)))
                        self.assertTrue(np.all(np.abs(tr[:, C['u']]) <= 2.0))
                        if stage == 'matched':
                            self.assertEqual(int(np.sum(buys)), 12)
                        else:
                            self.assertLessEqual(int(np.sum(buys)), 6)
                            if policy in ['raw', 'joint_y_only']:
                                self.assertEqual(int(np.sum(buys)), 0)

    def test_ledger_and_scores_recompute_from_recorded_trace(self):
        for seed in SEEDS:
            for world in e.WORLD_NAMES:
                for policy in e.POLICIES:
                    for stage in e.STAGES:
                        values, tr, blocks = checked_run(seed, world, policy, stage)
                        u, xn = tr[:, C['u']], tr[:, C['xn']]
                        xhat, x = tr[:, C['xhat']], tr[:, C['x']]
                        mu, pv, prob = tr[:, C['mu']], tr[:, C['pv']], tr[:, C['prob']]
                        state = sum(float(v) ** 2 for v in xn)
                        effort = sum(float(v) ** 2 for v in u)
                        work = sum(e.WEIGHTS[key] * n for key, n in blocks.items())
                        sense = int(np.sum(tr[:, C['buy']])) * .02
                        control = state + .05 * effort
                        self.assertAlmostEqual(values[M['state_loss']], state, places=12)
                        self.assertAlmostEqual(values[M['action_effort']], effort, places=12)
                        self.assertAlmostEqual(values[M['control_loss']], control, places=12)
                        self.assertEqual(values[M['work_units']], work)
                        self.assertAlmostEqual(values[M['work_cost']], .0001 * work, places=14)
                        self.assertAlmostEqual(values[M['sense_cost']], sense, places=14)
                        self.assertAlmostEqual(values[M['total_loss']], control + sense + .0001 * work, places=12)
                        self.assertAlmostEqual(values[M['estimate_mse']], float(np.mean((xhat - x) ** 2)), places=12)
                        self.assertAlmostEqual(values[M['forecast_mse']], float(np.mean((mu - xn) ** 2)), places=12)
                        self.assertAlmostEqual(values[M['brier']], float(np.mean((prob - (np.abs(xn) > .5)) ** 2)), places=12)
                        self.assertEqual(values[M['coverage90']], float(np.mean(np.abs(xn - mu) <= 1.6448536269514722 * np.sqrt(pv))))
                        self.assertAlmostEqual(values[M['max_abs_x']], float(max(abs(x[0]), np.max(np.abs(xn)))), places=12)
                        self.assertTrue(np.all((prob >= 0) & (prob <= 1)))
                        self.assertTrue(np.all(pv > 0))

    def test_forecast_precedes_current_transition_outcome(self):
        """Changing w[10] cannot change prediction or action made at t=10."""
        seed, change_t = 7000, 10
        original = e.data(seed)
        changed = tuple(v.copy() if isinstance(v, np.ndarray) else v for v in original)
        changed[4][change_t] += 1.0
        preoutcome_columns = [C[key] for key in COLS if key != 'xn']
        for policy in e.POLICIES:
            for stage in e.STAGES:
                _, baseline, _ = checked_run(seed, 'constant', policy, stage)
                with patch.object(e, 'data', return_value=changed):
                    _, perturbed, _ = checked_run(seed, 'constant', policy, stage)
                self.assertTrue(np.array_equal(baseline[:change_t], perturbed[:change_t], equal_nan=True))
                self.assertTrue(np.array_equal(baseline[change_t, preoutcome_columns], perturbed[change_t, preoutcome_columns], equal_nan=True))
                self.assertAlmostEqual(perturbed[change_t, C['xn']] - baseline[change_t, C['xn']], 1.0, places=14)

    def test_reference_gate_precedes_reference_observation(self):
        """Changing the unobserved initial reference cannot change its purchase."""
        seed = 7001
        changed_eta = e.data(seed)[3].copy()
        changed_eta[0] += 1000.0
        for policy in e.POLICIES:
            for stage in e.STAGES:
                _, baseline, _ = checked_run(seed, 'constant', policy, stage)
                _, perturbed, _ = e.run(seed, 'constant', policy, PARAMS[policy], stage,
                                         trace=True, eta_override=changed_eta)
                self.assertEqual(baseline[0, C['buy']], perturbed[0, C['buy']])
                self.assertEqual(baseline[0, C['y']], perturbed[0, C['y']])

    def test_fixed_alpha_variance_accounts_for_reusing_current_y(self):
        h, ph, y, z = .4, .3, 1.3, .2
        for alpha in [0., .2, .5, .8, 1.]:
            p = e.Policy('retained', {'alpha': alpha})
            p.set_hv(h, ph)
            p.begin(0, y)
            xhat, v, new_h, *_ = p.finish(z)
            expected_xhat = (1 - alpha) * (y - h) + alpha * z
            expected_v = (1 - alpha)**2 * (ph + .25**2) + alpha**2 * .05**2
            expected_bias_variance = (1 - alpha)**2 * ph + alpha**2 * (.25**2 + .05**2)
            self.assertAlmostEqual(xhat, expected_xhat, places=14)
            self.assertAlmostEqual(v, expected_v, places=14)
            self.assertAlmostEqual(p.get_hv()[1], expected_bias_variance, places=14)
            # The tempting RY + new_ph overcounts by 2*alpha*RY.
            self.assertAlmostEqual(.25**2 + p.get_hv()[1] - v, 2 * alpha * .25**2, places=14)

    def test_variance_formula_independently_by_linear_noise_propagation(self):
        # Orthogonal covariance propagation checks all cross terms independently
        # of the scalar implementation expression.
        for alpha in [.2, .5, .8, 1.]:
            old_bias_variance = .3
            covariance = np.diag([old_bias_variance, .25**2, .05**2])
            # Error = (1-alpha)*old_bias_error +(1-alpha)*eps+alpha*eta.
            weights = np.array([1-alpha, 1-alpha, alpha])
            exact_variance = float(weights @ covariance @ weights)
            p = e.Policy('retained', {'alpha': alpha})
            p.set_hv(.4, old_bias_variance)
            p.begin(0, 1.3)
            reported_variance = p.finish(.2)[1]
            self.assertAlmostEqual(reported_variance, exact_variance, places=14)

    def test_no_reference_scalar_variance_and_bias_prediction(self):
        p = e.Policy('retained', {'alpha': .5})
        p.set_hv(.4, .3)
        p.begin(1, 1.3)
        xhat, v, h, *_ = p.finish(None)
        self.assertAlmostEqual(xhat, .9, places=14)
        self.assertAlmostEqual(h, .4, places=14)
        self.assertAlmostEqual(v, .3 + .0025 + .25**2, places=14)

    def test_forecast_formula_uses_estimate_uncertainty_and_known_action(self):
        for policy in e.POLICIES:
            values, tr, _ = checked_run(7002, 'reference_bias', policy, 'matched')
            np.testing.assert_allclose(tr[:, C['mu']], .8 * tr[:, C['xhat']] + tr[:, C['u']], atol=1e-14)
            np.testing.assert_allclose(tr[:, C['pv']], .8**2 * tr[:, C['v']] + .05**2, atol=1e-14)


if __name__ == '__main__':
    print('Independent runner audit: test seeds 7000..7010 only.', flush=True)
    print('No development/evaluation functions called; no result-folder writes.', flush=True)
    print('Audit-selected-alpha uncertainty is plug-in, not exact post-selection variance.', flush=True)
    unittest.main(verbosity=2)
