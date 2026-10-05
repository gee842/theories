"""Independent protocol checks; only seeds >=40000; no result-folder writes."""
import math
import unittest

import numpy as np

import experiment as e


SEEDS = tuple(range(40000, 40006))
PARAMS = {'confidence': {}, 'periodic': {}, 'innovation': {'threshold': 2.},
          'hybrid': {'threshold': 2.}, 'anchor_filter': {'q_b': .0025}}
C = {v: k for k, v in enumerate(e.TRACE_COLS)}
M = {v: k for k, v in enumerate(e.METRICS)}


def run(seed, world, policy, **kwargs):
    assert seed >= 40000
    return e.run(seed, world, policy, PARAMS[policy], trace=True, **kwargs)


class RunnerChecks(unittest.TestCase):
    def test_all_policy_budgets_opportunities_protected_samples_and_counts(self):
        for seed in SEEDS:
            for world in e.WORLDS:
                for policy in e.POLICIES:
                    vals, tr, buy, alarm, fast = run(seed, world, policy)
                    self.assertLessEqual(int(buy.sum()), 6)
                    self.assertTrue(np.all(np.flatnonzero(buy) % 5 == 0))
                    self.assertTrue(np.array_equal(buy, np.isfinite(tr[:, C['z']])))
                    self.assertEqual(vals[M['sense_count']], buy.sum())
                    self.assertEqual(vals[M['fast_updates']], fast.sum())
                    self.assertEqual(vals[M['alarm_steps']], alarm.sum())
                    self.assertTrue(np.all(np.abs(tr[:, C['u']]) <= 2.))
                    if policy in ['periodic', 'anchor_filter']:
                        np.testing.assert_array_equal(np.flatnonzero(buy), [0, 10, 20, 35, 45, 55])
                    if policy == 'hybrid':
                        self.assertTrue(np.all(buy[[0, 25, 55]]))
                        self.assertLessEqual(int(buy.sum())-3, 3)
                    self.assertEqual(vals[M['monitor_steps']], 59 if policy in ['innovation', 'hybrid'] else 0)

    def test_hybrid_reservations_survive_immediate_discretionary_exhaustion(self):
        p = e.ScalarPolicy('hybrid', threshold=2.)
        bought = []
        for t in range(60):
            p.begin(t, 0.)
            p.latch = 100.  # worst-case persistent alarms, including after budget use
            buy = p.wants_reference()
            if buy:
                bought.append(t)
            p.finish(0. if buy else None)
        self.assertEqual(bought, [0, 5, 10, 15, 25, 55])
        self.assertEqual(p.discretionary, 3)
        self.assertEqual(p.purchases, 6)

    def test_hidden_reference_values_cannot_affect_any_decision_or_trace(self):
        for seed in SEEDS:
            for policy in e.POLICIES:
                original = run(seed, 'change_g1_d1', policy)
                eta = e.data(seed)[6].copy()
                eta[~original[2]] += 1000.
                changed = run(seed, 'change_g1_d1', policy, override={'eta': eta})
                for left, right in zip(original, changed):
                    self.assertTrue(np.array_equal(left, right, equal_nan=True))

    def test_latch_preserves_nonopportunity_alarm_and_clears_on_decline(self):
        p = e.ScalarPolicy('innovation', threshold=2.)
        p.begin(0, 0.)
        self.assertTrue(p.wants_reference())
        p.finish(0.)
        p.begin(1, 10.)
        self.assertGreater(p.score, 2.)
        latched = p.latch
        self.assertFalse(p.wants_reference())  # time1 cannot buy or clear latch
        self.assertEqual(p.latch, latched)
        p.finish(None)
        for t in range(2, 6):
            neutral_y = .8*p.last_y + p.last_u + .2*p.h
            p.begin(t, neutral_y)
            self.assertAlmostEqual(p.score, 0., places=12)
            if t < 5:
                self.assertFalse(p.wants_reference())
                p.finish(None)
        self.assertTrue(p.wants_reference())  # t5 buys solely from earlier score
        self.assertEqual(p.latch, 0.)
        p.finish(p.y)
        # A subthreshold latch is also cleared at a declined opportunity.
        p.begin(10, .8*p.last_y+p.last_u+.2*p.h)
        p.latch = 1.
        self.assertFalse(p.wants_reference())
        self.assertEqual(p.latch, 0.)

    def test_score_reconstruction_uses_preupdate_h_and_current_inflated_ph(self):
        for seed in SEEDS:
            for policy in ['innovation', 'hybrid']:
                _, tr, buy, alarm, fast = run(seed, 'change_g1_d1', policy)
                h, ph = 0., 1.
                for t, row in enumerate(tr):
                    ph += .0025 if t else 0.
                    if t:
                        previous = tr[t-1]
                        numerator = row[C['y']]-.8*previous[C['y']]-previous[C['u']]-.2*h
                        expected = abs(numerator)/math.sqrt(.0025+1.64*.0625+.04*ph)
                        self.assertAlmostEqual(row[C['score']], expected, places=12)
                        self.assertEqual(alarm[t], expected > 2.)
                    if buy[t]:
                        residual = row[C['y']]-row[C['z']]-h
                        expected_fast = abs(residual) > 2*math.sqrt(ph+.0625+.0025)
                        self.assertEqual(fast[t], expected_fast)
                        alpha = 1. if expected_fast else .2
                        expected_v = (1-alpha)**2*(ph+.0625)+alpha**2*.0025
                        ph = (1-alpha)**2*ph+alpha**2*(.0625+.0025)
                        h = (1-alpha)*h+alpha*(row[C['y']]-row[C['z']])
                    else:
                        expected_v = ph+.0625
                    self.assertAlmostEqual(row[C['h']], h, places=12)
                    self.assertAlmostEqual(row[C['ph']], ph, places=12)
                    self.assertAlmostEqual(row[C['variance']], expected_v, places=12)

    def test_score_and_gate_fixed_before_current_reference_update(self):
        p = e.ScalarPolicy('innovation', threshold=2.)
        p.begin(0, 0.)
        p.wants_reference()
        p.finish(0.)
        p.begin(5, 10.)
        score = p.score
        self.assertTrue(p.wants_reference())
        p.finish(-100.)  # extreme correction cannot revise the earlier score
        self.assertEqual(p.score, score)
        self.assertGreater(p.h, 50.)

    def test_metrics_reconstructed_from_trace(self):
        for seed in SEEDS:
            for world in e.WORLDS:
                for policy in e.POLICIES:
                    vals, tr, buy, _, _ = run(seed, world, policy)
                    col = lambda name: tr[:, C[name]]
                    x, b, d, h, dhat = (col(k) for k in ['x', 'b', 'd', 'h', 'dhat'])
                    xn, u, xhat, variance = (col(k) for k in ['x_next', 'u', 'xhat', 'variance'])
                    state = sum(float(v)**2 for v in xn)
                    effort = sum(float(v)**2 for v in u)
                    control = state+.05*effort
                    self.assertAlmostEqual(vals[M['state_loss']], state, places=12)
                    self.assertAlmostEqual(vals[M['action_effort']], effort, places=12)
                    self.assertAlmostEqual(vals[M['control_loss']], control, places=12)
                    self.assertAlmostEqual(vals[M['total_loss']], control+.02*buy.sum(), places=12)
                    self.assertAlmostEqual(vals[M['relative_bias_mse']], np.mean(((h-dhat)-(b-d))**2), places=12)
                    self.assertAlmostEqual(vals[M['absolute_bias_mse']], np.mean((h-b)**2), places=12)
                    self.assertAlmostEqual(vals[M['ref_bias_mse']], np.mean((dhat-d)**2), places=12)
                    self.assertAlmostEqual(vals[M['estimate_mse']], np.mean((xhat-x)**2), places=12)
                    mu, pv = .8*xhat+u, .64*variance+.0025
                    self.assertAlmostEqual(vals[M['coverage90']], np.mean(abs(xn-mu)<=1.6448536269514722*np.sqrt(pv)), places=14)
                    self.assertAlmostEqual(vals[M['interval_width90']], np.mean(2*1.6448536269514722*np.sqrt(pv)), places=12)
                    self.assertAlmostEqual(vals[M['normalized_forecast_error']], np.mean((xn-mu)**2/pv), places=11)

    def test_change_delays_and_censoring_reconstructed_from_trace(self):
        for seed in SEEDS:
            tau = e.data(seed)[4]
            for world in e.WORLDS:
                for policy in e.POLICIES:
                    vals, tr, buy, _, _ = run(seed, world, policy)
                    if not world.startswith('change'):
                        self.assertTrue(math.isnan(vals[M['access_delay']]))
                        self.assertTrue(math.isnan(vals[M['recovery_delay']]))
                        continue
                    samples = np.flatnonzero(buy[tau:])
                    self.assertEqual(vals[M['sample_found']], bool(len(samples)))
                    self.assertEqual(vals[M['access_delay']], samples[0] if len(samples) else 60-tau)
                    self.assertEqual(vals[M['prechange_purchases']], buy[:tau].sum())
                    self.assertEqual(vals[M['postchange_purchases']], buy[tau:].sum())
                    good = abs(tr[tau:, C['x_next']]) <= .2
                    # Completion clock = index of fifth state +1, not first-state index.
                    completions = [j+1 for j in range(4, len(good)) if np.all(good[j-4:j+1])]
                    self.assertEqual(vals[M['recovered']], bool(completions))
                    self.assertEqual(vals[M['recovery_delay']], completions[0] if completions else 60-tau)

    def test_known_delay_examples_use_completed_recovery_and_access_censor(self):
        zero = np.zeros(60)
        overrides = {'x0': 0., 'b0': 0, 'tau': 8, 'eps': zero, 'eta': zero,
                     'w': zero, 'g': 0., 'd': 0.}
        vals, *_ = run(40000, 'change_g0_d0', 'periodic', override=overrides)
        self.assertEqual(vals[M['access_delay']], 2.)
        self.assertEqual(vals[M['sample_found']], 1.)
        self.assertEqual(vals[M['recovery_delay']], 5.)
        self.assertEqual(vals[M['recovered']], 1.)
        vals, *_ = run(40000, 'change_g0_d0', 'innovation', override=overrides)
        self.assertEqual(vals[M['access_delay']], 52.)
        self.assertEqual(vals[M['sample_found']], 0.)

    def test_current_outcome_not_used_in_current_forecast_or_action(self):
        seed, change_t = 40000, 10
        changed_w = e.data(seed)[7].copy()
        changed_w[change_t] += 1.
        before_outcome = [k for k, name in enumerate(e.TRACE_COLS) if name != 'x_next']
        for policy in e.POLICIES:
            _, original, *_ = run(seed, 'change_g1_d1', policy)
            _, changed, *_ = run(seed, 'change_g1_d1', policy, override={'w': changed_w})
            self.assertTrue(np.array_equal(original[:change_t], changed[:change_t], equal_nan=True))
            self.assertTrue(np.array_equal(original[change_t, before_outcome], changed[change_t, before_outcome], equal_nan=True))
            self.assertAlmostEqual(changed[change_t, C['x_next']]-original[change_t, C['x_next']], 1., places=14)


if __name__ == '__main__':
    print('Independent correction-access runner audit; only seeds >=40000; no result writes.', flush=True)
    unittest.main(verbosity=2)
