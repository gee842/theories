"""Two-state linear estimator used by the recursive self-modeling experiment.

Assumed state: s=(x,b). Dynamics: x_next=a*x+u+w, b_next=b+v,
with independent zero-mean noises of variances q_x and q_b. Ordinary
observations are y=x+b+epsilon (variance r_y); purchased reference observations
are assumed to be z=x+eta (variance r_z). Any actual reference bias d is
deliberately absent from this estimator. Ground truth is never an input.

Chronology: initialize at the prior for time zero; call update_y(y_0), optionally
update_z(z_0); for each subsequent time call predict(u_previous), update_y(y_t),
and optionally update_z(z_t). Reference value is queried after update_y and
before acquiring z. predict() never reads a current or future observation.

For scalar h, innovation variance S=h P h^T+r and gain K=P h^T/S follow by
conditioning a joint Gaussian. Mean update is m+K(obs-h m). The implementation
uses the Joseph covariance identity (I-Kh)P(I-Kh)^T+r K K^T. No external
theorem about subjective experience is implied by this numerical model.

Accounting: counts records four distinct abstract work blocks: predict,
update_y, update_z, and reference_value. These are NOT measured FLOPs or equal
costs across different estimator architectures. Costs can be attached explicitly
to each block by a calling experiment. A reference_value query does no latent
state update and no observation acquisition. The persistent belief requires two
means and three independent covariance entries (five real scalars); this excludes
parameters, bookkeeping, and temporary arrays. Array storage uses six scalars.

Run this file directly for deterministic independent mathematical checks.
"""

from __future__ import annotations

import math
from typing import Iterable

import numpy as np


class KalmanBiasFilter:
    """Gaussian two-state estimator; all variances are in squared state units."""

    state_dimension = 2
    persistent_belief_scalars = 5

    def __init__(
        self,
        q_b: float = 0.0,
        *,
        a: float = 0.8,
        q_x: float = 0.05**2,
        r_y: float = 0.25**2,
        r_z: float = 0.05**2,
        mean: Iterable[float] | None = None,
        covariance: Iterable[Iterable[float]] | None = None,
    ) -> None:
        self.a = self._finite(a, "a")
        self.q_x = self._variance(q_x, "q_x")
        self.q_b = self._variance(q_b, "q_b")
        self.r_y = self._variance(r_y, "r_y")
        self.r_z = self._variance(r_z, "r_z")
        self._mean = np.array([0.0, 0.0] if mean is None else mean, dtype=float)
        self._covariance = np.array(
            [[1.0, 0.0], [0.0, 2.0 / 3.0]] if covariance is None else covariance,
            dtype=float,
        )
        if self._mean.shape != (2,) or not np.all(np.isfinite(self._mean)):
            raise ValueError("mean must contain two finite scalars")
        p = self._covariance
        if p.shape != (2, 2) or not np.all(np.isfinite(p)):
            raise ValueError("covariance must be a finite 2-by-2 matrix")
        if not np.allclose(p, p.T, atol=1e-12, rtol=0.0):
            raise ValueError("covariance must be symmetric")
        self._covariance = (p + p.T) / 2.0
        if np.linalg.eigvalsh(self._covariance).min() < -1e-12:
            raise ValueError("covariance must be positive semidefinite")
        self._counts = {"predict": 0, "update_y": 0, "update_z": 0, "reference_value": 0}

    @staticmethod
    def _finite(value: float, name: str) -> float:
        number = float(value)
        if not math.isfinite(number):
            raise ValueError(f"{name} must be finite")
        return number

    @classmethod
    def _variance(cls, value: float, name: str) -> float:
        number = cls._finite(value, name)
        if number < 0.0:
            raise ValueError(f"{name} must be nonnegative")
        return number

    @property
    def mean(self) -> np.ndarray:
        """Return a copy of the current mean, in order (x,b)."""
        return self._mean.copy()

    @property
    def covariance(self) -> np.ndarray:
        """Return a copy of the current covariance."""
        return self._covariance.copy()

    @property
    def x_mean(self) -> float:
        return float(self._mean[0])

    @property
    def x_variance(self) -> float:
        return float(self._covariance[0, 0])

    @property
    def bias_mean(self) -> float:
        return float(self._mean[1])

    @property
    def counts(self) -> dict[str, int]:
        return dict(self._counts)

    def predict(self, u: float = 0.0) -> KalmanBiasFilter:
        """Advance one step using the known control applied at the previous time."""
        u = self._finite(u, "u")
        a = np.diag([self.a, 1.0])
        self._mean = a @ self._mean + np.array([u, 0.0])
        self._covariance = a @ self._covariance @ a.T + np.diag([self.q_x, self.q_b])
        self._counts["predict"] += 1
        return self

    def _update(self, observation: float, h: np.ndarray, r: float, count: str) -> None:
        observation = self._finite(observation, "observation")
        p = self._covariance
        ph = p @ h
        innovation_variance = float(h @ ph + r)
        innovation = observation - float(h @ self._mean)
        if innovation_variance <= 0.0:
            if innovation_variance < -1e-12:
                raise ArithmeticError("negative innovation variance")
            if abs(innovation) > 1e-12:
                raise ValueError("observation contradicts an exactly known noiseless value")
            self._counts[count] += 1
            return
        k = ph / innovation_variance
        new_mean = self._mean + k * innovation
        residual_map = np.eye(2) - np.outer(k, h)
        new_covariance = residual_map @ p @ residual_map.T + r * np.outer(k, k)
        self._mean = new_mean
        self._covariance = (new_covariance + new_covariance.T) / 2.0
        self._counts[count] += 1

    def update_y(self, y: float) -> KalmanBiasFilter:
        """Condition on an ordinary y=x+b observation."""
        self._update(y, np.array([1.0, 1.0]), self.r_y, "update_y")
        return self

    def update_z(self, z: float) -> KalmanBiasFilter:
        """Condition on a purchased reference, assumed unbiased for x."""
        self._update(z, np.array([1.0, 0.0]), self.r_z, "update_z")
        return self

    def expected_reference_x_variance_reduction(self) -> float:
        """Return P_xx^2/(P_xx+r_z) without observing z or changing the belief.

        This is a model-predicted posterior variance reduction, not a guaranteed
        improvement in realized squared error when model assumptions are wrong.
        In this linear model it depends on covariance, not the observed values.
        """
        p_xx = max(0.0, self.x_variance)
        denominator = p_xx + self.r_z
        result = 0.0 if denominator == 0.0 else p_xx**2 / denominator
        self._counts["reference_value"] += 1
        return result


def run_tests() -> int:
    """Run checks against batch Gaussian conditioning and analytic cases."""
    import inspect
    import unittest

    class FilterChecks(unittest.TestCase):
        def test_default_prior(self):
            f = KalmanBiasFilter()
            np.testing.assert_array_equal(f.mean, [0.0, 0.0])
            np.testing.assert_array_equal(f.covariance, np.diag([1.0, 2.0 / 3.0]))

        def test_sequential_equals_independent_batch_conditioning(self):
            rng = np.random.default_rng(514)
            h = np.array([[1.0, 1.0], [1.0, 0.0]])
            r = np.diag([0.25**2, 0.05**2])
            for _ in range(100):
                l = rng.normal(size=(2, 2))
                p = l @ l.T + np.eye(2) * 0.02
                m = rng.normal(size=2)
                observations = rng.normal(size=2)
                f = KalmanBiasFilter(mean=m, covariance=p)
                f.update_y(observations[0]).update_z(observations[1])
                batch_gain = np.linalg.solve(h @ p @ h.T + r, h @ p).T
                expected_mean = m + batch_gain @ (observations - h @ m)
                expected_covariance = p - batch_gain @ h @ p
                np.testing.assert_allclose(f.mean, expected_mean, atol=3e-12, rtol=1e-11)
                np.testing.assert_allclose(f.covariance, expected_covariance, atol=3e-12, rtol=1e-11)

        def test_measurement_order_independence(self):
            f = KalmanBiasFilter().update_y(3.1).update_z(-0.2)
            g = KalmanBiasFilter().update_z(-0.2).update_y(3.1)
            np.testing.assert_allclose(f.mean, g.mean, atol=1e-12)
            np.testing.assert_allclose(f.covariance, g.covariance, atol=1e-12)

        def test_covariance_symmetry_and_positive_semidefiniteness(self):
            rng = np.random.default_rng(651)
            for q_b in [0.0, 0.0025, 0.04]:
                f = KalmanBiasFilter(q_b=q_b)
                for t in range(1000):
                    f.predict(rng.normal()).update_y(rng.normal())
                    if t % 7 == 0:
                        f.update_z(rng.normal())
                    np.testing.assert_allclose(f.covariance, f.covariance.T, atol=1e-15)
                    self.assertGreaterEqual(np.linalg.eigvalsh(f.covariance).min(), -1e-14)

        def test_noiseless_identification_with_positive_innovation_variance(self):
            f = KalmanBiasFilter(q_x=0, q_b=0, r_y=0, r_z=0)
            f.update_y(3.0).update_z(1.0)
            np.testing.assert_allclose(f.mean, [1.0, 2.0], atol=1e-14)
            np.testing.assert_allclose(f.covariance, np.zeros((2, 2)), atol=1e-14)
            f.predict(0.2)
            np.testing.assert_allclose(f.mean, [1.0, 2.0], atol=1e-14)

        def test_exactly_known_noiseless_value(self):
            f = KalmanBiasFilter(mean=[1, 2], covariance=np.zeros((2, 2)), r_y=0, r_z=0)
            f.update_y(3).update_z(1)
            self.assertEqual(f.expected_reference_x_variance_reduction(), 0.0)
            with self.assertRaises(ValueError):
                f.update_z(2)
            np.testing.assert_array_equal(f.mean, [1, 2])

        def test_analytic_prediction_and_control_chronology(self):
            f = KalmanBiasFilter(q_b=0.04, mean=[2, -1], covariance=[[2, 0.3], [0.3, 4]])
            f.predict(0.5)
            np.testing.assert_allclose(f.mean, [2.1, -1.0])
            np.testing.assert_allclose(f.covariance, [[1.2825, 0.24], [0.24, 4.04]])

        def test_reference_value_matches_realized_covariance_reduction(self):
            for z in [-100.0, -0.2, 0.0, 4.0, 100.0]:
                f = KalmanBiasFilter().update_y(1.2)
                initial = f.x_variance
                expected = f.expected_reference_x_variance_reduction()
                f.update_z(z)
                self.assertAlmostEqual(initial - f.x_variance, expected, places=13)

        def test_reference_query_reads_no_observation_or_mean_and_preserves_belief(self):
            f = KalmanBiasFilter().update_y(3.0)
            g = KalmanBiasFilter().update_y(-30.0)
            before_mean, before_covariance = f.mean, f.covariance
            method = KalmanBiasFilter.expected_reference_x_variance_reduction
            self.assertEqual(list(inspect.signature(method).parameters), ["self"])
            self.assertEqual(f.expected_reference_x_variance_reduction(), g.expected_reference_x_variance_reduction())
            np.testing.assert_array_equal(f.mean, before_mean)
            np.testing.assert_array_equal(f.covariance, before_covariance)
            self.assertEqual(f.counts["update_z"], 0)

        def test_belief_properties_and_initial_inputs_do_not_alias(self):
            m, p = np.array([1.0, 2.0]), np.eye(2)
            f = KalmanBiasFilter(mean=m, covariance=p)
            m[:] = 100.0
            p[:] = 100.0
            returned_m, returned_p = f.mean, f.covariance
            returned_m[:] = 100.0
            returned_p[:] = 100.0
            np.testing.assert_array_equal(f.mean, [1.0, 2.0])
            np.testing.assert_array_equal(f.covariance, np.eye(2))

        def test_accounting_includes_only_executed_blocks(self):
            f = KalmanBiasFilter().update_y(1).predict(0).update_y(2)
            f.expected_reference_x_variance_reduction()
            f.update_z(0.5)
            self.assertEqual(f.counts, {"predict": 1, "update_y": 2, "update_z": 1, "reference_value": 1})
            f.counts["predict"] = 999
            self.assertEqual(f.counts["predict"], 1)

        def test_invalid_inputs_fail_without_state_changes(self):
            for kwargs in [{"q_b": -1}, {"r_z": float("nan")}, {"covariance": [[1, 2], [0, 1]]}, {"covariance": [[1, 2], [2, 1]]}, {"mean": [0]}]:
                with self.assertRaises(ValueError):
                    KalmanBiasFilter(**kwargs)
            f = KalmanBiasFilter()
            initial_mean, initial_covariance, initial_counts = f.mean, f.covariance, f.counts
            for operation in [f.predict, f.update_y, f.update_z]:
                with self.assertRaises(ValueError):
                    operation(float("nan"))
            np.testing.assert_array_equal(f.mean, initial_mean)
            np.testing.assert_array_equal(f.covariance, initial_covariance)
            self.assertEqual(f.counts, initial_counts)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(FilterChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(run_tests())
