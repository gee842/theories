"""Optional Gaussian moment benchmark with state (x, ordinary_bias, ref_bias).

Assumed model: x_next = a*x + known_u + w, b_next = b + v, d_next = d.
Unknown forcing g is deliberately absent: the assumed value is zero. Observation
rows are y=x+b+eps and z=x+d+eta. Default variances are q_x=.05**2,
q_b=configured, r_y=.25**2 and r_z=.05**2. Prior means are zero and prior
covariance is diag(1, 1, .25**2). The prior bias moments do not assert that the
experiment's generating distributions are Gaussian. This is a descriptive
moment-model benchmark, not a guarantee of Bayesian calibration under mismatch.

Chronology: at t=0 update_y and optionally update_z; before subsequent t, call
predict(u_previous). Reference access must be chosen by the caller, separately
from the filter. No ground truth, actual forcing, or actual reference bias enters
this API. An observation update uses Joseph covariance propagation.

Known dynamics can provide an absolute anchor when a != 1 and forcing is known.
If arbitrary unknown constant forcing g is allowed, x->x+c, b->b-c, d->d-c,
g->g+(1-a)c preserves both observation streams. This filter excludes that family
by assuming g=0; its apparent identifiability depends on this assumption.

Accounting counts distinct predict/update_y/update_z blocks, not measured FLOPs
or runtime. Persistent belief: three means plus six independent covariance
entries = nine real scalars, excluding parameters, counters, and temporary arrays.
"""

from __future__ import annotations

import math
from typing import Iterable

import numpy as np


class AnchorFilter:
    """Three-state Gaussian moment filter with no unknown-forcing latent state."""

    state_dimension = 3
    persistent_belief_scalars = 9

    def __init__(
        self, q_b: float = 0.0, *, a: float = .8, q_x: float = .05**2,
        r_y: float = .25**2, r_z: float = .05**2,
        mean: Iterable[float] | None = None,
        covariance: Iterable[Iterable[float]] | None = None,
    ) -> None:
        self.a = self._finite(a, 'a')
        self.q_x = self._variance(q_x, 'q_x')
        self.q_b = self._variance(q_b, 'q_b')
        self.r_y = self._variance(r_y, 'r_y')
        self.r_z = self._variance(r_z, 'r_z')
        self._mean = np.array([0., 0., 0.] if mean is None else mean, dtype=float)
        self._covariance = np.array(
            np.diag([1., 1., .25**2]) if covariance is None else covariance,
            dtype=float,
        )
        if self._mean.shape != (3,) or not np.all(np.isfinite(self._mean)):
            raise ValueError('mean must contain three finite scalars')
        p = self._covariance
        if p.shape != (3, 3) or not np.all(np.isfinite(p)):
            raise ValueError('covariance must be a finite 3-by-3 matrix')
        if not np.allclose(p, p.T, atol=1e-12, rtol=0.):
            raise ValueError('covariance must be symmetric')
        self._covariance = .5 * (p + p.T)
        if np.linalg.eigvalsh(self._covariance).min() < -1e-12:
            raise ValueError('covariance must be positive semidefinite')
        self._counts = {'predict': 0, 'update_y': 0, 'update_z': 0}

    @staticmethod
    def _finite(value: float, name: str) -> float:
        result = float(value)
        if not math.isfinite(result):
            raise ValueError(f'{name} must be finite')
        return result

    @classmethod
    def _variance(cls, value: float, name: str) -> float:
        result = cls._finite(value, name)
        if result < 0.:
            raise ValueError(f'{name} must be nonnegative')
        return result

    @property
    def mean(self) -> np.ndarray:
        return self._mean.copy()

    @property
    def covariance(self) -> np.ndarray:
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
    def ref_bias_mean(self) -> float:
        return float(self._mean[2])

    @property
    def counts(self) -> dict[str, int]:
        return dict(self._counts)

    def predict(self, u: float = 0.) -> AnchorFilter:
        u = self._finite(u, 'u')
        a = np.diag([self.a, 1., 1.])
        self._mean = a @ self._mean + np.array([u, 0., 0.])
        self._covariance = a @ self._covariance @ a.T + np.diag([self.q_x, self.q_b, 0.])
        self._counts['predict'] += 1
        return self

    def _update(self, observation: float, h: np.ndarray, r: float, count: str) -> None:
        observation = self._finite(observation, 'observation')
        p = self._covariance
        ph = p @ h
        s = float(h @ ph + r)
        innovation = observation - float(h @ self._mean)
        if s <= 0.:
            if s < -1e-12:
                raise ArithmeticError('negative innovation variance')
            if abs(innovation) > 1e-12:
                raise ValueError('observation contradicts an exactly known noiseless value')
            self._counts[count] += 1
            return
        k = ph / s
        residual_map = np.eye(3) - np.outer(k, h)
        new_p = residual_map @ p @ residual_map.T + r * np.outer(k, k)
        self._mean = self._mean + k * innovation
        self._covariance = .5 * (new_p + new_p.T)
        self._counts[count] += 1

    def update_y(self, y: float) -> AnchorFilter:
        self._update(y, np.array([1., 1., 0.]), self.r_y, 'update_y')
        return self

    def update_z(self, z: float) -> AnchorFilter:
        self._update(z, np.array([1., 0., 1.]), self.r_z, 'update_z')
        return self
