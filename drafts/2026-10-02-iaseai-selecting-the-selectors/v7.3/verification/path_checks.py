"""V7.3 constructive reform-path witnesses, using only the standard library.

The parameter witness is illustrative, not empirically calibrated. The analytic
certificate is checked against joint RK4 and an independent exponential-midpoint
scheme that integrates the frozen support/host equations exactly. No check
models political adoption or proves preservation of implementation authority.
"""

from dataclasses import dataclass, replace
import json
import math


@dataclass(frozen=True)
class Model:
    a: float = 1.0
    c: float = 1.0
    epsilon: float = 6.0
    zeta: float = 10.0
    d0: float = 0.6
    boost: float = 5.0
    maintenance: float = 0.5
    b0: float = 1.2
    repaired_b: float = 0.2
    delay: float = 0.15
    capture0: float = 0.9
    support0: float = 1.8
    capture_bound: float = 0.3
    support_bound: float = 0.7
    liability: float = 4.0
    advantage: float = 1.0
    selection: float = 6.0
    high_load: float = 0.9
    race_share0: float = 0.85
    rho: float = 1.0
    host_loading: float = 1.0
    host0: float = 0.95
    host_floor: float = 0.3
    correction_unit_cost: float = 1.0
    capital_cost: float = 2.0
    rule_upkeep: float = 0.1
    peak_capacity: float = 5.0
    build_rate: float = 30.0


def logistic(value):
    if value >= 0:
        return 1.0 / (1.0 + math.exp(-value))
    exponential = math.exp(value)
    return exponential / (1.0 + exponential)


def logit(share):
    return math.log(share / (1.0 - share))


def host_at_fixed_load(host, load, duration, model):
    rate = model.rho - model.host_loading * load
    if abs(rate) < 1e-12:
        reciprocal = 1.0 / host + model.rho * duration
    else:
        factor = math.exp(-rate * duration)
        reciprocal = factor / host - model.rho * math.expm1(-rate * duration) / rate
    return 1.0 / reciprocal


def certificate(model):
    m = model
    assert 0 < m.capture0 < 1 and 0 < m.capture_bound < 1
    assert 0 < m.race_share0 < 1 and 0 < m.host_floor < m.host0 <= 1
    assert 0 <= m.repaired_b <= m.b0
    assert 0 < m.d0 <= m.boost and 0 < m.maintenance <= m.boost
    assert m.repaired_b / m.maintenance < m.support_bound < m.c / m.a
    assert m.delay > 0
    delta = m.liability * (1.0 - m.capture_bound) - m.advantage
    assert delta > 0
    safe_load = m.rho * (1.0 - m.host_floor) / m.host_loading
    assert 0 < safe_load < m.high_load
    safe_race_share = safe_load / m.high_load
    decay = math.exp(-m.epsilon * m.d0 * m.delay)
    support_after_delay = (m.b0 / m.d0
                           + (m.support0 - m.b0 / m.d0) * decay)
    support_integral_delay = (m.b0 / m.d0 * m.delay
                              + (m.support0 - m.b0 / m.d0)
                              * (1.0 - decay) / (m.epsilon * m.d0))
    boost_equilibrium = m.repaired_b / m.boost
    if support_after_delay > m.support_bound:
        support_time = math.log((support_after_delay - boost_equilibrium)
                                / (m.support_bound - boost_equilibrium)) / (
                                    m.epsilon * m.boost)
    else:
        support_time = 0.0
    support_integral_boost = (boost_equilibrium * support_time
                             + (support_after_delay - boost_equilibrium)
                             * (-math.expm1(-m.epsilon * m.boost * support_time))
                             / (m.epsilon * m.boost))
    capture_logit_bound = (logit(m.capture0)
                           + m.zeta * (m.a * (support_integral_delay
                                              + support_integral_boost)
                                       - m.c * (m.delay + support_time)))
    capture_time = max(0.0, capture_logit_bound - logit(m.capture_bound)) / (
        m.zeta * (m.c - m.a * m.support_bound))
    release = m.delay + support_time + capture_time
    load_time = max(0.0, logit(m.race_share0)
                    + m.selection * m.high_load * m.advantage * release
                    - logit(safe_race_share)) / (
                        m.selection * m.high_load * delta)
    entry = release + load_time
    worst_host = host_at_fixed_load(m.host0, m.high_load, entry, m)
    operating_integral = ((m.d0 + m.boost) * m.delay / 2
                          + m.boost * (support_time + capture_time)
                          + m.maintenance * load_time)
    total_cost = (m.capital_cost + m.correction_unit_cost * operating_integral
                  + m.rule_upkeep * entry)
    recurring_cost = (m.correction_unit_cost * m.maintenance + m.rule_upkeep)
    return {"support_after_delay_bound": support_after_delay,
            "support_integral_delay_bound": support_integral_delay,
            "support_time": support_time, "capture_time": capture_time,
            "boost_release": release, "load_time": load_time, "entry_time": entry,
            "safe_load": safe_load, "safe_race_share": safe_race_share,
            "liability_margin": delta,
            "worst_case_host_at_entry": worst_host,
            "transition_cost": total_cost, "recurring_cost": recurring_cost,
            "post_reform_gain": m.a * m.repaired_b / (m.c * m.maintenance),
            "build_rate_required": (m.boost - m.d0) / m.delay,
            "certified": (worst_host >= m.host_floor
                          and m.boost <= m.peak_capacity
                          and (m.boost - m.d0) / m.delay <= m.build_rate)}


def simulate(model, release, entry, horizon=30.0, max_step=0.002,
             method="rk4", repaired_b=None, after_release=None):
    """Piecewise policy integration, with all policy changes as mesh endpoints."""
    m = model
    b_after = m.repaired_b if repaired_b is None else repaired_b
    d_after = m.maintenance if after_release is None else after_release
    assert release >= m.delay and horizon >= entry >= release
    stages = [(0.0, m.delay, "build"),
              (m.delay, release, "boost"),
              (release, entry, "maintenance"),
              (entry, horizon, "maintenance")]
    state = (logit(m.capture0), m.support0, logit(m.race_share0), m.host0)
    records = [(0.0, state)]

    def controls(time, stage):
        if stage == "build":
            return m.b0, m.d0 + (m.boost - m.d0) * time / m.delay
        return b_after, m.boost if stage == "boost" else d_after

    def rhs(time, current, stage):
        capture_logit, support, race_logit, host = current
        b, d = controls(time, stage)
        effective_liability = m.liability * logistic(-capture_logit)
        return (m.zeta * (m.a * support - m.c),
                m.epsilon * (b * logistic(capture_logit) - d * support),
                m.selection * m.high_load * (m.advantage - effective_liability),
                host * (m.rho * (1.0 - host)
                        - m.host_loading * m.high_load * logistic(race_logit)))

    def linear_support(support, capture_logit, b, d, dt):
        source = b * logistic(capture_logit)
        if d == 0:
            return support + m.epsilon * source * dt
        equilibrium = source / d
        return equilibrium + (support - equilibrium) * math.exp(-m.epsilon * d * dt)

    for start, stop, stage in stages:
        if stop <= start:
            continue
        count = max(1, math.ceil((stop - start) / max_step))
        dt = (stop - start) / count
        for index in range(count):
            time = start + index * dt
            if method == "rk4":
                k1 = rhs(time, state, stage)
                k2 = rhs(time + dt / 2, tuple(y + dt * k / 2
                                             for y, k in zip(state, k1)), stage)
                k3 = rhs(time + dt / 2, tuple(y + dt * k / 2
                                             for y, k in zip(state, k2)), stage)
                k4 = rhs(time + dt, tuple(y + dt * k
                                         for y, k in zip(state, k3)), stage)
                state = tuple(y + dt * (a + 2 * b + 2 * c + d) / 6
                              for y, a, b, c, d in zip(state, k1, k2, k3, k4))
            elif method == "exponential_midpoint":
                cx, support, cy, host = state
                b_start, d_start = controls(time, stage)
                cx_half = cx + dt / 2 * m.zeta * (m.a * support - m.c)
                z_half = linear_support(support, cx, b_start, d_start, dt / 2)
                cy_half = cy + dt / 2 * m.selection * m.high_load * (
                    m.advantage - m.liability * logistic(-cx))
                b_mid, d_mid = controls(time + dt / 2, stage)
                state = (cx + dt * m.zeta * (m.a * z_half - m.c),
                         linear_support(support, cx_half, b_mid, d_mid, dt),
                         cy + dt * m.selection * m.high_load * (
                             m.advantage - m.liability * logistic(-cx_half)),
                         host_at_fixed_load(host, m.high_load * logistic(cy_half), dt, m))
            else:
                raise ValueError(method)
            assert all(math.isfinite(value) for value in state)
            records.append((time + dt, state))
    return records


def summarize(records, model, release, entry):
    m = model
    at_release = min(records, key=lambda item: abs(item[0] - release))[1]
    at_entry = min(records, key=lambda item: abs(item[0] - entry))[1]
    return {"minimum_host": min(state[3] for _, state in records),
            "peak_capture": max(logistic(state[0]) for _, state in records),
            "release_capture": logistic(at_release[0]),
            "release_support": at_release[1],
            "entry_capture": logistic(at_entry[0]),
            "entry_support": at_entry[1],
            "entry_load": m.high_load * logistic(at_entry[2]),
            "entry_host": at_entry[3],
            "final_capture": logistic(records[-1][1][0]),
            "final_host": records[-1][1][3]}


def constructive_entry_and_continuation():
    m = Model()
    bounds = certificate(m)
    assert bounds["certified"]
    assert m.capture0 > m.capture_bound and m.support0 > m.c / m.a
    assert m.high_load * m.race_share0 > bounds["safe_load"]
    assert m.a * m.b0 / (m.c * m.d0) > 1
    assert m.liability * (1.0 - m.capture0) < m.advantage
    paths = [simulate(m, bounds["boost_release"], bounds["entry_time"],
                      max_step=step, method=method)
             for method, step in (("rk4", 0.002), ("rk4", 0.001),
                                  ("exponential_midpoint", 0.001),
                                  ("exponential_midpoint", 0.0005))]
    summaries = [summarize(path, m, bounds["boost_release"], bounds["entry_time"])
                 for path in paths]
    for summary in summaries:
        assert summary["minimum_host"] >= bounds["worst_case_host_at_entry"]
        assert summary["release_capture"] <= m.capture_bound
        assert summary["release_support"] <= m.support_bound
        assert summary["entry_load"] <= bounds["safe_load"]
        assert summary["entry_host"] >= m.host_floor
    for _, state in paths[1]:
        assert state[3] >= m.host_floor
    for time, state in paths[1]:
        if time >= bounds["entry_time"]:
            assert logistic(state[0]) <= m.capture_bound
            assert state[1] <= m.c / m.a
            assert m.high_load * logistic(state[2]) <= bounds["safe_load"]
    rk_error = max(abs(summaries[0][key] - summaries[1][key]) for key in summaries[0])
    independent_error = max(abs(summaries[3][key] - summaries[1][key]) for key in summaries[0])
    endpoint_keys = tuple(key for key in summaries[0]
                          if key not in ("minimum_host", "peak_capture"))
    coarse_endpoint_error = max(abs(summaries[2][key] - summaries[1][key])
                                for key in endpoint_keys)
    fine_endpoint_error = max(abs(summaries[3][key] - summaries[1][key])
                              for key in endpoint_keys)
    assert rk_error < 1e-7
    assert independent_error < 2e-5
    # Extrema sampled on different grids need not show clean order reduction;
    # common fixed-time states do, and all extrema retain absolute-error checks.
    assert fine_endpoint_error < coarse_endpoint_error / 3
    return {**bounds, **summaries[1], "rk_refinement_error": rk_error,
            "independent_integrator_error": independent_error,
            "endpoint_error_refinement_ratio": coarse_endpoint_error / fine_endpoint_error}


def full_cost_and_actuator_feasibility():
    m = Model()
    bounds = certificate(m)
    release, entry = bounds["boost_release"], bounds["entry_time"]
    # Independent quadrature pays ALL operations, including the baseline, and
    # keeps capital and rule-maintenance costs explicit.
    cost = m.capital_cost
    for start, stop, stage in ((0.0, m.delay, "build"),
                               (m.delay, release, "boost"),
                               (release, entry, "maintenance")):
        count = 1000
        dt = (stop - start) / count
        for index in range(count):
            time = start + (index + 0.5) * dt
            d = (m.d0 + (m.boost - m.d0) * time / m.delay if stage == "build"
                 else m.boost if stage == "boost" else m.maintenance)
            cost += dt * (m.correction_unit_cost * d + m.rule_upkeep)
    assert abs(cost - bounds["transition_cost"]) < 1e-10
    assert bounds["transition_cost"] < 11.0
    assert bounds["recurring_cost"] == 0.6
    assert 11.0 > bounds["transition_cost"] > 8.0
    assert 0.7 >= bounds["recurring_cost"] > 0.4
    assert not certificate(replace(m, peak_capacity=4.0))["certified"]
    assert not certificate(replace(m, build_rate=20.0))["certified"]
    return {"full_transition_cost": cost, "available_transition_budget": 11.0,
            "recurring_cost": bounds["recurring_cost"], "recurring_revenue": 0.7,
            "required_peak": m.boost, "required_build_rate": bounds["build_rate_required"],
            "insufficient_budget_example": 8.0, "insufficient_revenue_example": 0.4}


def bounded_certificate_is_not_necessity():
    # Slightly slower capture adjustment loses the conservative maximal-load
    # certificate; this does not establish actual failure of the same policy.
    m = replace(Model(), zeta=8.0)
    bounds = certificate(m)
    assert not bounds["certified"]
    path = simulate(m, bounds["boost_release"], bounds["entry_time"], max_step=0.001)
    result = summarize(path, m, bounds["boost_release"], bounds["entry_time"])
    assert bounds["worst_case_host_at_entry"] < m.host_floor
    assert result["minimum_host"] > m.host_floor
    return {"conservative_host_bound": bounds["worst_case_host_at_entry"],
            "actual_model_minimum_host": result["minimum_host"],
            "floor": m.host_floor}


def no_structural_repair_after_short_pulse():
    m = Model()
    # Installation is followed by withdrawal before the computed dwell, while
    # the old conversion channel remains. The baseline cannot undo this basin.
    release = m.delay
    entry = release
    coarse = simulate(m, release, entry, max_step=0.002, repaired_b=m.b0)
    fine = simulate(m, release, entry, max_step=0.001, repaired_b=m.b0)
    first = summarize(coarse, m, release, entry)
    result = summarize(fine, m, release, entry)
    assert result["final_capture"] > 0.99999
    assert result["minimum_host"] < m.host_floor
    assert abs(first["minimum_host"] - result["minimum_host"]) < 1e-6
    return {"post_withdrawal_gain": m.a * m.b0 / (m.c * m.maintenance),
            "release_time": release, **result}


def slow_construction_loses_the_floor():
    m = replace(Model(), delay=5.0)
    bounds = certificate(m)
    assert not bounds["certified"]
    horizon = bounds["entry_time"] + 5.0
    paths = [simulate(m, bounds["boost_release"], bounds["entry_time"],
                      horizon=horizon, max_step=step) for step in (0.002, 0.001)]
    summaries = [summarize(path, m, bounds["boost_release"], bounds["entry_time"])
                 for path in paths]
    assert summaries[1]["minimum_host"] < m.host_floor
    assert summaries[1]["final_host"] > 0.99
    assert summaries[1]["entry_capture"] <= m.capture_bound
    assert summaries[1]["entry_load"] <= bounds["safe_load"]
    assert abs(summaries[0]["minimum_host"] - summaries[1]["minimum_host"]) < 1e-6
    return {"installation_delay": m.delay, "entry_deadline": bounds["entry_time"],
            "post_reform_gain": bounds["post_reform_gain"], **summaries[1]}


def defunding_does_not_itself_prove_recapture():
    m = Model()
    bounds = certificate(m)
    # The prescribed maintenance policy is no longer feasible. In this deeply
    # suppressed self-coupled witness, however, the remaining source decays and
    # does not build support up to c/a. Certificate loss is not actual failure.
    path = simulate(m, bounds["boost_release"], bounds["entry_time"],
                    horizon=100.0, max_step=0.002, after_release=0.0)
    result = summarize(path, m, bounds["boost_release"], bounds["entry_time"])
    support_after_release = [state[1] for time, state in path
                             if time >= bounds["boost_release"]]
    assert max(support_after_release) < 0.00001 < m.c / m.a
    assert result["minimum_host"] > m.host_floor
    assert result["final_capture"] < 1e-100
    return {"maintenance_after_release": 0.0,
            "maximum_post_release_support": max(support_after_release), **result}


def run_checks():
    checks = (constructive_entry_and_continuation,
              full_cost_and_actuator_feasibility,
              bounded_certificate_is_not_necessity,
              no_structural_repair_after_short_pulse,
              slow_construction_loses_the_floor,
              defunding_does_not_itself_prove_recapture)
    return {check.__name__: check() for check in checks}


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
