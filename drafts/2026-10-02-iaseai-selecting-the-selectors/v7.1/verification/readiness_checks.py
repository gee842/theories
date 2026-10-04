"""V7.1 readiness witnesses, using only the standard library.

run_checks() returns one result per successful group and raises on any failure.
The witnesses bound stronger claims; they are not empirical estimates or a
proof checker. Exact arithmetic establishes the periodic selection example,
and an RK4 host integration checks its path independently at two step sizes.
"""

import json
import math
from fractions import Fraction


def logistic(z):
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    ez = math.exp(z)
    return ez / (1.0 + ez)


def periodic_host(response, cycles, step):
    """Integrate the host with exact logit motion within each liability phase."""
    z = math.log(0.001 / 0.999)
    host, minimum, time, first_crossing = 1.0, 1.0, 0.0, None
    for _ in range(cycles):
        for gap, duration in ((1.0, 1.0), (-2.0, 0.4)):
            count = round(duration / step)
            dt, slope = duration / count, response(gap)
            for _ in range(count):
                def velocity(value, offset):
                    return value * (0.05 * (1.0 - value)
                                    - 0.08 * logistic(z + slope * offset))

                k1 = velocity(host, 0.0)
                k2 = velocity(host + dt * k1 / 2, dt / 2)
                k3 = velocity(host + dt * k2 / 2, dt / 2)
                k4 = velocity(host + dt * k3, dt)
                host += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
                z += slope * dt
                time += dt
                minimum = min(minimum, host)
                if first_crossing is None and host < 0.3:
                    first_crossing = time
    return {"minimum_host": minimum, "final_host": host,
            "final_logit": z, "final_race_share": logistic(z),
            "first_floor_crossing": first_crossing}


def cumulative_counterexample():
    phase = ((Fraction(1), Fraction(1)), (Fraction(-2), Fraction(2, 5)))
    duration = sum(t for _, t in phase)
    b_increment = sum(g * t for g, t in phase)
    logit_increment = sum((g + g ** 3) * t for g, t in phase)
    average_liability = sum((1 - g) * t for g, t in phase) / duration
    assert b_increment == Fraction(1, 5)
    assert logit_increment == -2
    assert average_liability == Fraction(6, 7) < 1
    # Algebraically f(g)/g = 1+g^2 >= 1 for either positive ordered gap.
    for g in (0.0001, 0.1, 1.0, 2.0, 100.0):
        assert g + g ** 3 >= g and (-g) + (-g) ** 3 < 0
    maximum_share = logistic(math.log(0.001 / 0.999) + 2)
    invariant_floor = 1 - 0.08 / 0.05 * maximum_share
    assert 0.08 > 0.05 * (1 - 0.3)  # The manuscript's (reach).
    assert invariant_floor > 0.988 > 0.3
    coarse = periodic_host(lambda g: g + g ** 3, 100, 0.01)
    fine = periodic_host(lambda g: g + g ** 3, 100, 0.005)
    assert fine["minimum_host"] >= invariant_floor
    assert fine["first_floor_crossing"] is None
    assert fine["final_race_share"] < 1e-80
    assert abs(fine["final_logit"] - (math.log(0.001 / 0.999) - 200)) < 1e-8
    assert abs(coarse["minimum_host"] - fine["minimum_host"]) < 1e-7
    return {"cycle_B": float(b_increment), "cycle_logit": -2,
            "average_liability": float(average_liability),
            "analytic_host_lower_bound": invariant_floor, **fine}


def constant_speed_replicator():
    # Across either sign, log(p_r/p_k)(t) - log(p_r/p_k)(0) = s B(t).
    initial = math.log(0.001 / 0.999)
    for speed in (0.25, 1.0, 3.0):
        signed_response = speed * 1.0 + speed * (-2.0) * 0.4
        assert math.isclose(signed_response, 0.2 * speed, abs_tol=1e-15)
    coarse = periodic_host(lambda g: g, 150, 0.01)
    fine = periodic_host(lambda g: g, 150, 0.005)
    assert abs(fine["final_logit"] - (initial + 30)) < 1e-8
    assert fine["final_race_share"] > 0.999999999
    assert fine["first_floor_crossing"] is not None
    assert fine["final_host"] < 0.3
    assert abs(coarse["minimum_host"] - fine["minimum_host"]) < 1e-7
    assert abs(coarse["first_floor_crossing"] - fine["first_floor_crossing"]) < 0.011
    return {"cycle_B": 0.2, "speed": 1.0, **fine}


def narrowing_without_concentration():
    # Fixed prize, linear ratio success, beta=1/2, d=1/5, kappa*Omega=1.
    # Total stock five is invariant; direct nonlinear updates give gap'=0.9 gap.
    x, y = 2.6, 2.4
    for _ in range(100):
        p = x / (x + y)
        x, y = 0.8 * x + 0.25 + 0.5 * p, 0.8 * y + 0.25 + 0.5 * (1 - p)
    gap = abs(x - y)
    assert math.isclose(x + y, 5.0, abs_tol=1e-13)
    assert math.isclose(gap, 0.2 * 0.9 ** 100, abs_tol=1e-13)
    gamma = Fraction(1, 2)
    discounted_gain = Fraction(9, 10) * Fraction(1, 5) * gamma / (
        1 - Fraction(9, 10) * Fraction(4, 5))
    relative_price = discounted_gain / (1 - discounted_gain)
    common_price = 0
    assert discounted_gain == Fraction(9, 28)
    assert relative_price == Fraction(9, 19) > common_price
    assert gamma < 1 and gap < 0.000006
    return {"Gamma": float(gamma), "Gamma_delta": float(discounted_gain),
            "relative_price": float(relative_price), "common_price": common_price,
            "initial_gap": 0.2, "gap_after_100": gap}


def fixed_total_scope():
    def quadratic(profile, matrix):
        return sum(profile[i] * matrix[i][j] * profile[j]
                   for i in range(2) for j in range(2))

    def selected_capacity(yield_, correction):
        # Numerically locate the maximum of q*Y/d - q^2/2 on q >= 0.
        low, high = 0.0, 8.0
        for _ in range(90):
            left, right = low + (high - low) / 3, high - (high - low) / 3
            value = lambda q: q * yield_ / correction - q * q / 2
            if value(left) < value(right):
                low = left
            else:
                high = right
        return (low + high) / 2

    def correction_threshold(yield_):
        low, high = 0.25, 2.0
        for _ in range(60):
            mid = (low + high) / 2
            # Separate evaluation domain: inbound coefficients (1,1), B=1.
            if selected_capacity(yield_, mid) / mid > 1:
                low = mid
            else:
                high = mid
        return (low + high) / 2

    concentrated, spread = (1.0, 0.0), (0.5, 0.5)
    diagonal, cross_domain = ((1, 0), (0, 1)), ((1, 2), (2, 1))
    yields = [quadratic(profile, matrix) for matrix in (diagonal, cross_domain)
              for profile in (concentrated, spread)]
    assert yields == [1.0, 0.5, 1.0, 1.5]
    thresholds = [correction_threshold(y) for y in yields]
    for y, d in zip(yields, thresholds):
        assert math.isclose(d, math.sqrt(y), abs_tol=3e-8)
    assert thresholds[1] < thresholds[0] and thresholds[3] > thresholds[2]
    return {"diagonal_returns": yields[:2], "diagonal_thresholds": thresholds[:2],
            "cross_domain_returns": yields[2:], "cross_domain_thresholds": thresholds[2:]}


def functional_without_cognitive():
    # Common protection adds the same term to both payoffs and cancels.
    # Correlated local benefit 0.2 exceeds trait cost 0.1, with no cognition state.
    initial, cost, local_benefit, common_benefit = 0.1, 0.1, 0.2, 0.3
    final = logistic(math.log(initial / (1 - initial)) + (local_benefit - cost) * 100)
    common_term = common_benefit * initial
    pay_protect = 1 + common_term + local_benefit - cost
    pay_other = 1 + common_term
    assert pay_protect > pay_other and final > 0.9995
    # The retained otherwise-alike claim: pure common benefit with cost loses.
    assert (1 + common_term - cost) - (1 + common_term) < 0
    return {"protective_share_at_100": final, "local_payoff_advantage": 0.1,
            "otherwise_alike_protective_advantage": -0.1}


def fixed_verified_containment():
    delta, gain, cooperation, decisive, punishment = 0.9, 0.1, 1.0, 100.0, 0.0

    def bellman(escape):
        value = 0.0
        deviate = (1 - delta) * (cooperation + gain) + delta * (
            escape * decisive + (1 - escape) * punishment)
        for _ in range(1000):
            next_value = max((1 - delta) * cooperation + delta * value, deviate)
            if abs(next_value - value) < 1e-14:
                return next_value, deviate
            value = next_value
        raise AssertionError("Bellman iteration did not converge")

    safe_value, safe_deviation = bellman(0.001)
    failing_value, failing_deviation = bellman(0.02)
    threshold = (delta * (cooperation - punishment) - (1 - delta) * gain) / (
        delta * (decisive - punishment))
    assert 0.001 < threshold < 0.02
    assert math.isclose(safe_value, cooperation, abs_tol=1e-12)
    assert safe_deviation < cooperation < failing_deviation
    assert math.isclose(failing_value, failing_deviation, abs_tol=1e-12)
    # Punishment credibility is a premise, not proved by this decision problem.
    return {"fixed_escape_probability": 0.001, "escape_threshold": threshold,
            "cooperation_value": safe_value, "deviation_value": safe_deviation,
            "failed_control_deviation_value": failing_deviation}


def noncompetitive_growth():
    # Hazardous variety Y_t=2^t; coverage U_t=t+1. No competition variable.
    # For t>=3 U/Y<=1/2, then it decreases: u_t>=1/2 and h_t>=0.005.
    assert math.ldexp(4.0, -3) == 0.5
    log_survival = 0.0
    previous = 1.0
    for t in range(1000):
        coverage = min(1.0, math.ldexp(float(t + 1), -t))
        assert coverage <= previous
        previous = coverage
        hazard = 0.01 * (1 - coverage)
        if t >= 3:
            assert hazard >= 0.005
        log_survival += math.log1p(-hazard)
    assert log_survival <= 997 * math.log1p(-0.005)
    return {"residual_hazard_lower_bound_from_t3": 0.005,
            "survival_at_1000": math.exp(log_survival),
            "limiting_survival": 0.0}


def zero_tax_without_safety():
    # Zero tax makes two variants neutral; it does not change a hazard primitive.
    compliant_share, alignment_tax, hazard = 0.5, 0.0, 0.01
    derivative = -alignment_tax * compliant_share * (1 - compliant_share)
    assert derivative == 0
    survival = math.exp(1000 * math.log1p(-hazard))
    assert 0 < survival < 0.00005
    return {"alignment_tax": alignment_tax, "share_derivative": derivative,
            "survival_at_1000": survival, "limiting_survival": 0.0}


def run_checks():
    checks = (cumulative_counterexample, constant_speed_replicator,
              narrowing_without_concentration, fixed_total_scope,
              functional_without_cognitive, fixed_verified_containment,
              noncompetitive_growth, zero_tax_without_safety)
    return {check.__name__: check() for check in checks}


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
