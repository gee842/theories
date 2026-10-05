#!/usr/bin/env python3
"""Reproduce the opportunity audit's finite-module arithmetic checks.

Uses exact rational arithmetic and no simulator/producer imports. These sampled
checks support the displayed algebra; they do not prove a physical realization,
pay a construction ledger, or replace the note's general mathematical proofs.
Running this file writes opportunity-check.json beside it.
"""

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from random import Random


def sign(value):
    return (value > 0) - (value < 0)


def check():
    rng = Random(837)
    outcomes = {"positive": 0, "zero": 0, "negative": 0}
    parameters = []
    for _ in range(200):
        a, b, mu, nu, gamma = [
            Q(rng.randint(1, 20), rng.randint(1, 10)) for _ in range(5)
        ]
        chi = Q(rng.randint(1, 10), 10)
        r = Q(rng.randint(0, 20), 10)
        parameters.append([str(x) for x in (a, b, mu, nu, gamma, chi, r)])

        a_built = a_bound = chi * a
        b_built, b_bound = b, r * b
        s_built = a_built + b_built + mu
        s_bound = a_bound + b_bound + nu
        denominator = s_built * s_bound - mu * nu
        assert denominator > 0
        p_built = (a_built * s_bound + mu * a_bound) / denominator
        p_bound = (a_bound + nu * p_built) / s_bound
        p0 = a / (a + b)
        p1 = (a + gamma * p_built) / (a + b + gamma)

        assert p_built == (a_built + mu * p_bound) / s_built
        assert p1 - p0 == gamma * (p_built - p0) / (a + b + gamma)
        general = (a + b) * (a_built * s_bound + mu * a_bound) - a * denominator
        subclass = mu * (chi - r) - (1 - chi) * (chi * a + r * b + nu)
        assert general == a * b * subclass
        assert sign(p1 - p0) == sign(general) == sign(subclass)
        outcomes[{1: "positive", 0: "zero", -1: "negative"}[sign(p1 - p0)]] += 1

        # Generator action on functions in states S, B, I, success, failure.
        def generator(v, construction):
            s, built, bound, success, failure = v
            return (
                a * (success - s) + b * (failure - s) + construction * (built - s),
                a_built * (success - built) + b_built * (failure - built)
                + mu * (bound - built),
                a_bound * (success - bound) + b_bound * (failure - bound)
                + nu * (built - bound),
                Q(0), Q(0),
            )

        terminal = (Q(0), Q(0), Q(0), Q(1), Q(0))
        derivative2_with = generator(generator(terminal, gamma), gamma)[0]
        derivative2_without = generator(generator(terminal, Q(0)), Q(0))[0]
        assert derivative2_with - derivative2_without == gamma * (a_built - a)

    case_bytes = json.dumps(parameters, separators=(",", ":")).encode()
    return {
        "status": "passed",
        "arithmetic": "Python fractions.Fraction; exact, no floating-point tolerance",
        "seed": 837,
        "parameter_cases": 200,
        "parameter_domain": {
            "a_b_mu_nu_gamma": "independent randint(1,20)/randint(1,10)",
            "chi": "randint(1,10)/10",
            "r": "randint(0,20)/10",
        },
        "checks_per_case": [
            "positive first-step denominator",
            "built-state first-step equation",
            "construction response identity",
            "exact equality: general criterion = a*b*subclass criterion",
            "success-difference and both criteria have the same sign",
            "second generator derivative difference = gamma*(a_B-a)",
        ],
        "success_difference_sign_counts": outcomes,
        "ordered_parameter_cases_sha256": hashlib.sha256(case_bytes).hexdigest(),
        "source_note": "_process/research/2026-10-05-support-and-shared-generativity/"
        "completion/REGULATION-OPPORTUNITY-AUDIT.md",
        "scope": "Reproducible sampled algebra check for a conditional kinetic module. "
        "Not physical identification, a construction/work ledger, a positive result "
        "for the G network, or an empirical test.",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    result = check()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("opportunity-check.json").write_text(output)
    print(output, end="")
