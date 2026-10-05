"""Independent checks for the optional anchor benchmark; no development data."""

import unittest

import numpy as np

from anchor_filter import AnchorFilter


class AnchorFilterChecks(unittest.TestCase):
    def test_defaults_and_known_control_prediction(self):
        f = AnchorFilter(q_b=.04)
        np.testing.assert_array_equal(f.mean, np.zeros(3))
        np.testing.assert_array_equal(f.covariance, np.diag([1., 1., .0625]))
        f.predict(.2)
        np.testing.assert_allclose(f.mean, [.2, 0, 0])
        np.testing.assert_allclose(f.covariance, np.diag([.6425, 1.04, .0625]))

    def test_sequential_posterior_matches_independent_batch_conditioning(self):
        rng = np.random.default_rng(41000)
        h = np.array([[1., 1., 0.], [1., 0., 1.]])
        r = np.diag([.25**2, .05**2])
        for _ in range(100):
            factor = rng.normal(size=(3, 3))
            p = factor @ factor.T + .03 * np.eye(3)
            mean, obs = rng.normal(size=3), rng.normal(size=2)
            f = AnchorFilter(mean=mean, covariance=p).update_y(obs[0]).update_z(obs[1])
            gain = np.linalg.solve(h @ p @ h.T + r, h @ p).T
            np.testing.assert_allclose(f.mean, mean + gain @ (obs - h @ mean), atol=1e-11)
            np.testing.assert_allclose(f.covariance, p - gain @ h @ p, atol=1e-11)

    def test_positive_semidefinite_covariance_for_each_candidate_qb(self):
        rng = np.random.default_rng(41001)
        for q_b in [0., .0025, .04]:
            f = AnchorFilter(q_b=q_b)
            for t in range(1000):
                if t:
                    f.predict(rng.normal())
                f.update_y(rng.normal())
                if t % 10 == 0:
                    f.update_z(rng.normal())
                np.testing.assert_allclose(f.covariance, f.covariance.T, atol=1e-14)
                self.assertGreaterEqual(np.linalg.eigvalsh(f.covariance).min(), -1e-13)

    def test_noiseless_known_forcing_identifies_both_offsets(self):
        # Three independent scalar observations suffice: y0,z0,y1 with known u0.
        x, b, d, u = 1.2, -.7, .3, -.25
        f = AnchorFilter(q_x=0., q_b=0., r_y=0., r_z=0.)
        f.update_y(x+b).update_z(x+d)
        self.assertGreater(f.x_variance, 0.)  # one instant leaves a shared shift
        x = .8*x + u
        f.predict(u).update_y(x+b)
        np.testing.assert_allclose(f.mean, [x, b, d], atol=1e-12)
        np.testing.assert_allclose(f.covariance, np.zeros((3, 3)), atol=1e-12)

    def test_reference_offset_learnable_under_known_forcing_with_noise(self):
        # A reproducible noisy sequence checks mean identification in a favorable
        # correctly specified world, not frequency calibration or the experiment's
        # hard worlds. No development or evaluation seeds are used.
        rng = np.random.default_rng(41002)
        f = AnchorFilter(q_x=0., q_b=0.)
        x, b, d = 1.2, -.7, .3
        for t in range(600):
            if t:
                u = .1*np.sin(t/9.)
                x = .8*x+u
                f.predict(u)
            f.update_y(x+b+rng.normal(0, .25))
            if t % 10 == 0:
                f.update_z(x+d+rng.normal(0, .05))
        np.testing.assert_allclose(f.mean, [x, b, d], atol=.04)

    def test_a_equals_one_preserves_unobservable_common_shift(self):
        h = np.array([[1., 1., 0.], [1., 0., 1.]])
        shift = np.array([1., -1., -1.])
        f = AnchorFilter(a=1., q_x=0., q_b=0., r_y=.0625, r_z=.0025)
        for _ in range(100):
            f.predict(0.).update_y(.5).update_z(1.5)
        np.testing.assert_array_equal(h @ shift, np.zeros(2))
        observability = np.vstack([h, h @ np.diag([1., 1., 1.])])
        self.assertEqual(np.linalg.matrix_rank(observability), 2)
        self.assertGreater(float(shift @ f.covariance @ shift), .1)
        self.assertEqual(np.linalg.matrix_rank(np.vstack([h, h @ np.diag([.8, 1., 1.])])), 3)

    def test_unknown_forcing_shift_is_exactly_observationally_equivalent(self):
        a, x, b, d, g, c = .8, 1.2, -.7, .3, .15, .9
        shifted_x, shifted_b, shifted_d = x+c, b-c, d-c
        shifted_g = g + (1-a)*c
        f, shifted_f = AnchorFilter(), AnchorFilter()
        # Same observable streams lead to the same filter means even though the
        # two underlying true x trajectories remain separated by c.
        for t in range(60):
            if t:
                u = .2*np.sin(t)
                x = a*x + u + g
                shifted_x = a*shifted_x + u + shifted_g
                f.predict(u)
                shifted_f.predict(u)
            self.assertAlmostEqual(shifted_x-x, c, places=12)
            self.assertAlmostEqual(x+b, shifted_x+shifted_b, places=12)
            self.assertAlmostEqual(x+d, shifted_x+shifted_d, places=12)
            f.update_y(x+b)
            shifted_f.update_y(shifted_x+shifted_b)
            if t % 10 == 0:
                f.update_z(x+d)
                shifted_f.update_z(shifted_x+shifted_d)
            np.testing.assert_allclose(f.mean, shifted_f.mean, atol=1e-12)
        self.assertAlmostEqual((shifted_x-shifted_f.x_mean) - (x-f.x_mean), c, places=12)

    def test_input_validation_copies_and_accounting(self):
        mean, covariance = np.zeros(3), np.eye(3)
        f = AnchorFilter(mean=mean, covariance=covariance)
        mean[:] = 100
        covariance[:] = 100
        f.mean[:] = 100
        f.covariance[:] = 100
        np.testing.assert_array_equal(f.mean, np.zeros(3))
        np.testing.assert_array_equal(f.covariance, np.eye(3))
        f.predict(.1).update_y(.4).update_z(.3)
        self.assertEqual(f.counts, {'predict': 1, 'update_y': 1, 'update_z': 1})
        for bad in [{'q_b': -1}, {'mean': [0, 0]}, {'r_y': float('nan')},
                    {'covariance': np.diag([-1., 1., 1.])}]:
            with self.assertRaises(ValueError):
                AnchorFilter(**bad)
        before = f.mean
        with self.assertRaises(ValueError):
            f.update_y(float('nan'))
        np.testing.assert_array_equal(before, f.mean)


if __name__ == '__main__':
    unittest.main(verbosity=2)
