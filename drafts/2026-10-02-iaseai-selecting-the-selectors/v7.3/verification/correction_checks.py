"""Reduced joint correction witnesses for V7.2, using the standard library.

These checks exercise a time-varying certified field coupled to replicator load
and host dynamics, an analytic transient failure, and limited selection tests.
They do not estimate a real institutional capacity or certify a general kernel.
"""

import json
import math
from fractions import Fraction


def integrate(rhs, initial, horizon, step):
    """Fixed-step RK4; retain extrema and time series for cross-step checks."""
    count = round(horizon / step)
    dt = horizon / count
    state = tuple(initial)
    history = [state]
    for index in range(count):
        time = index * dt
        k1 = rhs(time, state)
        k2 = rhs(time + dt / 2, tuple(y + dt * k / 2
                                     for y, k in zip(state, k1)))
        k3 = rhs(time + dt / 2, tuple(y + dt * k / 2
                                     for y, k in zip(state, k2)))
        k4 = rhs(time + dt, tuple(y + dt * k
                                 for y, k in zip(state, k3)))
        state = tuple(y + dt * (a + 2 * b + 2 * c + d) / 6
                      for y, a, b, c, d in zip(state, k1, k2, k3, k4))
        assert all(math.isfinite(value) for value in state)
        history.append(state)
    return history


def max_path_disagreement(coarse, fine):
    assert len(fine) == 2 * len(coarse) - 1
    return max(abs(left - right)
               for old, new in zip(coarse, fine[::2])
               for left, right in zip(old, new))


def time_varying_joint_certificate():
    # The focal rule domain receives support from itself and an independently
    # varying external captured domain. Both incoming conversion and correction
    # vary with time; the full row gain is between 0.3 and 0.7.
    def coefficients(time):
        correction = 1.2 + 0.35 * math.sin(0.8 * time)
        gain = 0.5 + 0.2 * math.sin(1.3 * time)
        self_fraction = 0.45 + 0.2 * math.cos(0.6 * time)
        external_share = 0.5 + 0.5 * math.sin(0.9 * time)
        nominal_liability = 2.0 + 0.2 * (1.0 + math.cos(0.7 * time))
        return correction, gain, self_fraction, external_share, nominal_liability

    def rhs(time, state):
        capture, support, race_share, host = state
        correction, gain, self_fraction, external, liability = coefficients(time)
        total_conversion = gain * correction
        inbound = total_conversion * (self_fraction * capture
                                       + (1.0 - self_fraction) * external)
        effective = liability * (1.0 - capture)
        return (capture * (1.0 - capture) * (support - 1.0),
                0.7 * (inbound - correction * support),
                (1.0 - effective) * race_share * (1.0 - race_share),
                host * ((1.0 - host) - race_share))

    # Start simultaneously on the support, capture, load and host boundaries.
    initial = (0.3, 1.0, 0.5, 0.5)
    coarse = integrate(rhs, initial, 20, 0.01)
    fine = integrate(rhs, initial, 20, 0.005)
    disagreement = max_path_disagreement(coarse, fine)
    assert disagreement < 2e-8
    for index, state in enumerate(fine):
        capture, support, race_share, host = state
        correction, gain, _, _, liability = coefficients(index * 0.005)
        assert correction > 0 and gain <= 0.7 + 1e-14
        assert -1e-12 <= capture <= 0.3 + 1e-12
        assert -1e-12 <= support <= 1.0 + 1e-12
        assert -1e-12 <= race_share <= 0.5 + 1e-12
        assert 0.5 - 1e-12 <= host <= 1.0 + 1e-12
        assert liability * (1.0 - capture) >= 1.4 - 1e-12
        if index:
            assert capture <= fine[index - 1][0] + 1e-12
            assert race_share <= fine[index - 1][2] + 1e-12
    return {"max_row_gain_bound": 0.7,
            "minimum_effective_liability_bound": 1.4,
            "minimum_host": min(state[3] for state in fine),
            "final_capture": fine[-1][0],
            "final_load": fine[-1][2],
            "final_host": fine[-1][3],
            "cross_step_max_error": disagreement}


def eventual_correction_transient_failure():
    def rhs(time, state):
        capture, support, race_share, host = state
        effective = 2.0 * (1.0 - capture)
        return (capture * (1.0 - capture) * (support - 1.0),
                0.5 * capture - support,
                (1.0 - effective) * race_share * (1.0 - race_share),
                host * ((1.0 - host) - race_share))

    # Exact analytic boundary calculation, independent of numerical integration.
    effective0 = 2 * (1 - Fraction(4, 5))
    load_derivative0 = (1 - effective0) * Fraction(1, 4)
    host_second_derivative0 = -Fraction(1, 2) * load_derivative0
    assert effective0 == Fraction(2, 5)
    assert load_derivative0 == Fraction(3, 20)
    assert host_second_derivative0 == -Fraction(3, 40)
    initial = (0.8, 0.0, 0.5, 0.5)
    coarse = integrate(rhs, initial, 30, 0.01)
    fine = integrate(rhs, initial, 30, 0.005)
    disagreement = max_path_disagreement(coarse, fine)
    assert disagreement < 2e-8
    assert fine[1][3] < 0.5
    assert min(state[3] for state in fine) < 0.49
    assert fine[-1][0] < 1e-9
    assert fine[-1][3] > 0.99
    # A positive initial host margin does not remove this failure.
    interior = integrate(rhs, (0.8, 0.0, 0.5, 0.5001), 30, 0.005)
    assert min(state[3] for state in interior) < 0.49
    return {"row_gain": 0.5,
            "initial_effective_liability": float(effective0),
            "initial_load_derivative": float(load_derivative0),
            "initial_host_second_derivative": float(host_second_derivative0),
            "minimum_host": min(state[3] for state in fine),
            "final_capture": fine[-1][0],
            "final_host": fine[-1][3],
            "interior_minimum_host": min(state[3] for state in interior),
            "cross_step_max_error": disagreement}


def local_and_coalitional_limits():
    fitness = lambda q: -q + q * q
    assert fitness(Fraction(1, 10)) < 0 < fitness(Fraction(3, 2))
    for delta in (1e-3, 1e-5):
        slope = (fitness(delta) - fitness(-delta)) / (2 * delta)
        assert abs(slope + 1.0) < 1e-10

    def rhs(time, state):
        share, = state
        return (share * (1.0 - share) * (-1.0 + 2.0 * share),)

    minority = integrate(rhs, (0.1,), 20, 0.005)
    coalition = integrate(rhs, (0.6,), 20, 0.005)
    separator = integrate(rhs, (0.5,), 20, 0.005)
    assert minority[-1][0] < 1e-8
    assert coalition[-1][0] > 0.999999
    assert all(state[0] == 0.5 for state in separator)
    return {"local_fitness_derivative": -1,
            "large_deviation_fitness_at_1_5": fitness(1.5),
            "minority_final_share": minority[-1][0],
            "coalition_final_share": coalition[-1][0],
            "unstable_threshold": 0.5}


def partial_and_total_sensitivity():
    # a=c=1, b(u)=1+2u, d(u)=1+u: a policy raises correction but
    # raises appropriable conversion twice as quickly at its starting point.
    ratio = lambda u: (1.0 + 2.0 * u) / (1.0 + u)
    epsilon = 1e-6
    total_derivative = (math.log(ratio(epsilon))
                        - math.log(ratio(-epsilon))) / (2 * epsilon)
    assert abs(total_derivative - 1.0) < 1e-8
    finite_ratio = Fraction(12, 10) / Fraction(11, 10)
    assert finite_ratio == Fraction(12, 11) > 1
    return {"partial_log_sensitivity_to_correction": -1,
            "total_log_sensitivity_to_policy_at_zero": total_derivative,
            "gain_multiplier_at_policy_0_1": float(finite_ratio)}


def run_checks():
    checks = (time_varying_joint_certificate,
              eventual_correction_transient_failure,
              local_and_coalitional_limits,
              partial_and_total_sensitivity)
    return {check.__name__: check() for check in checks}


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
