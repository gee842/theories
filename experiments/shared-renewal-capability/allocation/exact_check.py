#!/usr/bin/env python3
"""Exact check of one algebraically selected allocation-control witness.

No parameter search or trajectory simulation. The successful assay is first
fresh capture with C and total Y present, not endpoint survival at the deadline.
Running this file writes exact-check.json beside it.
"""

from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from math import factorial
from pathlib import Path


P = dict(a=1, b=1, d=1, delta=1, nu=1, g=4, ell=141, beta=3384,
         kappa=162432, mu=159189, k=1, theta=4, alpha=4, rho=1)
S = (2, 0, 1, 0, 1, 0, 0, 0)
ORIGINAL = (0, 1, 1, 1, 1, 0, 0, 0)


def material(x):
    r, c, y, d, f, gate, gf, yg = x
    return r + c + y + d + gate + gf + 2 * yg


def work(x):
    r, c, y, d, f, gate, gf, yg = x
    return f + r + c + y + gate + 2 * gf + 2 * yg


def events(x, constructed, zeta=0):
    r, c, y, d, f, gate, gf, yg = x
    a, b, death, delta, nu, g, ell, beta, kappa, mu, k, theta, alpha, rho = (
        P[name] for name in ("a", "b", "d", "delta", "nu", "g", "ell", "beta",
                            "kappa", "mu", "k", "theta", "alpha", "rho")
    )
    table = [
        ("assemble", a*r, (-1, 1, 0, 0, 0, 0, 0, 0)),
        ("C_wear", b*c, (0, -1, 0, 1, 0, 0, 0, 0)),
        ("reproduce", beta*r*y, (-1, 0, 1, 0, 0, 0, 0, 0)),
        ("bound_reproduce", zeta*beta*r*yg, (-1, 0, 1, 0, 0, 0, 0, 0)),
        ("Y_wear", death*y, (0, 0, -1, 1, 0, 0, 0, 0)),
        ("capture", g*c, (0, 0, 0, 0, 1, 0, 0, 0)),
        ("leak", ell*f, (0, 0, 0, 0, -1, 0, 0, 0)),
        ("recycle_C", k*f*d*c, (1, 0, 0, -1, -1, 0, 0, 0)),
        ("recycle_Y", k*theta*f*d*y, (1, 0, 0, -1, -1, 0, 0, 0)),
        ("build", constructed*kappa*r*f, (-1, 0, 0, 0, -1, 1, 0, 0)),
        ("G_wear", delta*gate, (0, 0, 0, 1, 0, -1, 0, 0)),
        ("bind_F", alpha*gate*f, (0, 0, 0, 0, -1, -1, 1, 0)),
        ("unbind_F", rho*gf, (0, 0, 0, 0, 1, 1, -1, 0)),
        ("bound_leak", ell*gf, (0, 0, 0, 0, 0, 1, -1, 0)),
        ("GF_wear", delta*gf, (0, 0, 0, 1, 1, 0, -1, 0)),
        ("bind_Y", mu*gate*y, (0, 0, -1, 0, 0, -1, 0, 1)),
        ("unbind_Y", nu*yg, (0, 0, 1, 0, 0, 1, 0, -1)),
        ("YG_G_wear", delta*yg, (0, 0, 1, 1, 0, 0, 0, -1)),
        ("YG_Y_wear", death*yg, (0, 0, 0, 1, 0, 1, 0, -1)),
    ]
    return {name: (Q(rate), tuple(v + dv for v, dv in zip(x, change)))
            for name, rate, change in table if rate}


def route(start, names, constructed):
    x, fractions, rates, hazards, work_changes = start, [], [], [], []
    for name in names:
        choices = events(x, constructed)
        rate, successor = choices[name]
        hazard = sum(value[0] for value in choices.values())
        assert all(v >= 0 for v in successor)
        assert material(successor) == material(x) == 3
        fractions.append(rate / hazard)
        rates.append(rate)
        hazards.append(hazard)
        work_changes.append(work(successor) - work(x))
        x = successor
    return x, fractions, rates, hazards, work_changes


def product(values):
    result = Q(1)
    for value in values:
        result *= value
    return result


def check():
    q = Q(P["a"], P["a"]+P["d"]+P["delta"]+P["nu"]) * Q(
        P["g"], P["g"]+P["b"]+P["d"])
    epsilon = q / 8
    c_epsilon = (1-epsilon) / epsilon
    assert (q, epsilon, c_epsilon) == (Q(1, 6), Q(1, 48), Q(47))
    assert P["ell"] == 3*P["d"]*c_epsilon
    assert 2*P["beta"] == c_epsilon*max(2*P["a"]+P["d"]+P["ell"],
                                        P["a"]+2*P["d"]+P["ell"])
    assert 2*P["kappa"] == c_epsilon*(2*P["a"]+2*P["beta"]+P["d"]+P["ell"])
    assert P["mu"] == c_epsilon*(P["a"]+P["beta"]+P["d"]+P["delta"])

    dead, failure_races, _, _, failure_debits = route(
        S, ["reproduce", "reproduce", "leak"], False)
    assert dead == (0, 0, 3, 0, 0, 0, 0, 0)
    assert failure_races == [Q(47, 48)] * 3
    for y in range(4):
        assert set(events((0, 0, y, 3-y, 0, 0, 0, 0), False)) <= {"Y_wear"}

    post_assembly, success_races, _, phase_hazards, success_debits = route(
        S, ["build", "bind_Y", "assemble"], True)
    assert success_races == [Q(47, 48), Q(47, 48), Q(1, 4)]
    assert success_debits == [-1, 0, 0]
    assert post_assembly == (0, 1, 0, 0, 0, 0, 0, 1)

    # Check constant relevant hazards in every possible gate configuration
    # after protected assembly and before fresh capture or C/Y loss.
    post_states = [post_assembly, (0, 1, 1, 0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0, 0, 0, 0)]
    relevant_total = Q(P["g"] + P["b"] + P["d"])
    for x in post_states:
        rates = events(x, True)
        capture = rates["capture"][0]
        c_wear = rates["C_wear"][0]
        y_wear = sum(rate for name, (rate, _) in rates.items()
                     if name in {"Y_wear", "YG_Y_wear"})
        assert (capture, c_wear, y_wear) == (Q(4), Q(1), Q(1))
        for name, (_, nxt) in rates.items():
            if name not in {"capture", "C_wear", "Y_wear", "YG_Y_wear"}:
                assert (nxt[1], nxt[2]+nxt[7], nxt[4]) == (1, 1, 0)
    phase_hazards.append(relevant_total)
    success_races.append(Q(P["g"], relevant_total))
    L = product(success_races)
    B = product(failure_races)

    # Finite deadline: each relevant phase has at least 15/16 probability
    # to finish within H/4. Use a rational lower bound on exp(3), not floats.
    horizon = Q(3)
    assert min(phase_hazards)*horizon/4 == 3
    exp3_lower = sum(Q(3**j, factorial(j)) for j in range(5))
    assert exp3_lower == Q(131, 8) > 16
    assert Q(15, 16)**4 >= Q(3, 4)
    absent_upper, constructed_lower = 1-B, Q(3, 4)*L
    assert absent_upper == Q(6769, 110592)
    assert constructed_lower == Q(6627, 55296)
    assert absent_upper < Q(1, 10) < constructed_lower

    prepared, _, prefix_rates, _, prefix_debits = route(
        ORIGINAL, ["capture", "capture", "C_wear", "recycle_Y", "recycle_Y"], True)
    assert prepared == S
    prefix_product = product(prefix_rates)
    assert prefix_product == 12*P["b"]*P["k"]**2*P["theta"]**2*P["g"]**2

    # Verify the exact local-state equations for the old and new architectures.
    p_b = Q(P["a"], P["a"]+P["beta"]+P["d"])
    v = P["a"]+P["d"]+P["delta"]
    for zeta in (0, 1):
        s_u = v+P["beta"]+P["mu"]
        s_i = v+P["nu"]+zeta*P["beta"]
        denominator = s_u*s_i-P["mu"]*P["nu"]
        common = P["a"]+P["delta"]*p_b
        p_u = common*(s_i+P["mu"])/denominator
        p_i = (common+P["nu"]*p_u)/s_i
        assert p_u*s_u == common+P["mu"]*p_i
        assert p_u-p_b == p_b*P["mu"]*P["beta"]*(1-zeta)/denominator

    # Exact finite generator expansion for the same stopped fresh-capture
    # event. This checks the early disadvantage without approximating H=3.
    def derivatives(constructed):
        @lru_cache(None)
        def power(x, flag, order):
            if order == 0:
                return Q(flag == 1)
            if flag != -1:
                return Q(0)
            base = power(x, flag, order-1)
            total = Q(0)
            for name, (rate, nxt) in events(x, constructed).items():
                nxt_flag = int(nxt[2]+nxt[7] > 0) if name == "capture" else -1
                total += rate*(power(nxt, nxt_flag, order-1)-base)
            return total
        return [power(S, -1, order) for order in range(4)]

    old_derivatives, new_derivatives = derivatives(False), derivatives(True)
    differences = [new-old for new, old in zip(new_derivatives, old_derivatives)]
    expected_third = -2*P["kappa"]*P["a"]*P["g"]
    assert differences == [0, 0, 0, expected_third]

    return {
        "status": "passed",
        "method": "Exact rational arithmetic; one analytically derived witness; no search or simulation",
        "state_order": ["R", "C", "Y", "D", "F", "G", "GF", "YG"],
        "common_preparation": list(S),
        "constructed_zeta": 0,
        "absent_construction_coefficient": 0,
        "matched_parameters_except_construction_availability": P,
        "horizon": str(horizon),
        "target": "First fresh capture by H, with C>=1 and Y+YG>=1 at capture; not terminal survival",
        "failure_race_probabilities": list(map(str, failure_races)),
        "success_race_probabilities": list(map(str, success_races)),
        "relevant_phase_hazards": list(map(str, phase_hazards)),
        "construction_route_work_increments": success_debits,
        "baseline_failure_work_increments": failure_debits,
        "supported_preparation_work_increments": prefix_debits,
        "supported_preparation_rate_product": str(prefix_product),
        "exp_3_certified_lower_bound": str(exp3_lower),
        "absent_success_upper_bound": str(absent_upper),
        "constructed_success_lower_bound": str(constructed_lower),
        "net_improvement_lower_bound": str(constructed_lower-absent_upper),
        "early_success_difference_derivatives_orders_0_through_3": list(map(str, differences)),
        "early_success_difference_h_cubed_coefficient": str(Q(expected_third, 6)),
        "separating_reliability": "1/10",
        "scope": "Declared reaction-law result from S with no initial regulator. "
        "No chemical calibration, all-capability ordering, advantage of fuel switching, "
        "or net comparison from the earlier original preparation is established.",
        "source_note": "_process/research/2026-10-05-support-and-shared-generativity/"
        "completion/ALLOCATION-CONTROL.md",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    result = check()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("exact-check.json").write_text(output)
    print(output, end="")
