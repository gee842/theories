"""Exact/finite checks supporting formal-memo.md; standard library only."""
from fractions import Fraction as F
from itertools import product
from math import comb
import json
from pathlib import Path


def laws(n=4, denominator=4):
    for weights in product(range(denominator + 1), repeat=n):
        if sum(weights) == denominator:
            yield tuple(F(w, denominator) for w in weights)


def tail(n, k, p):
    return sum((F(comb(n, j)) * p**j * (1-p)**(n-j)
                for j in range(k, n+1)), F(0))


def cutoff(n, alpha):
    # Direct tail summation gives exact thresholds, with no normal approximation.
    acc = F(0)
    boundary = n + 1
    for k in range(n, -1, -1):
        acc += F(comb(n, k), 2**n)
        if acc <= alpha:
            boundary = k
        else:
            break
    return boundary


def crossing(nmax, p, boundaries):
    alive = {0: F(1)}
    rejected = F(0)
    by_time = {}
    for n in range(1, nmax+1):
        nxt = {}
        for k, mass in alive.items():
            for y, prob in ((0, 1-p), (1, p)):
                count = k+y
                branch = mass*prob
                if boundaries(n, count):
                    rejected += branch
                else:
                    nxt[count] = nxt.get(count, F(0)) + branch
        alive = nxt
        assert rejected + sum(alive.values(), F(0)) == 1
        if n in (20, 50, 100, 200):
            by_time[n] = float(rejected)
    return by_time


def run():
    all_laws = list(laws())
    test_count = 0
    for p in all_laws:
        for q in all_laws:
            tv = sum((abs(a-b) for a, b in zip(p, q)), F(0))/2
            risks = []
            for decisions in product((0, 1), repeat=4):
                alpha = sum((a*d for a, d in zip(p, decisions)), F(0))
                beta = sum((b*(1-d) for b, d in zip(q, decisions)), F(0))
                assert alpha + beta >= 1-tv
                risks.append((alpha+beta)/2)
                test_count += 1
            assert min(risks) == (1-tv)/2
            if p != q:
                assert any(b > a for a, b in zip(p, q))
                assert any(b < a for a, b in zip(p, q))

    n, p0, p1 = 20, F(1, 2), F(4, 5)
    bin0 = [F(comb(n, k))*p0**k*(1-p0)**(n-k) for k in range(n+1)]
    bin1 = [F(comb(n, k))*p1**k*(1-p1)**(n-k) for k in range(n+1)]
    tv = sum((abs(a-b) for a, b in zip(bin0, bin1)), F(0))/2
    alpha = tail(n, 15, p0)
    power = tail(n, 15, p1)
    assert alpha + 1-power >= 1-tv

    fixed_bounds = {n: cutoff(n, F(1, 20)) for n in range(1, 201)}
    spending_bounds = {n: cutoff(n, F(1, 20*n*(n+1))) for n in range(1, 201)}
    peek = lambda n, k: k >= fixed_bounds[n]
    spend = lambda n, k: k >= spending_bounds[n]
    safe = lambda n, k: F(8, 5)**k * F(2, 5)**(n-k) >= 20

    result = {
        "finite_tv_check": {"laws": len(all_laws), "tests": test_count, "all_exact": True},
        "binomial_n20_p0_0.5_p1_0.8": {
            "cutoff": 15, "type_I": float(alpha), "power": float(power),
            "TV": float(tv), "minimum_equal_prior_risk": float((1-tv)/2),
            "all_finite_sequences_positive_probability": True},
        "fresh_independent_100_exact_0.05_tests_FWER": float(1-F(19, 20)**100),
        "optional_peeking": {
            "ordinary_fixed_time_tests_null_crossing": crossing(200, p0, peek),
            "ordinary_fixed_time_tests_alternative_crossing": crossing(200, p1, peek),
            "alpha_spending_null_crossing": crossing(200, p0, spend),
            "alpha_spending_alternative_crossing": crossing(200, p1, spend),
            "safe_likelihood_ratio_null_crossing": crossing(200, p0, safe),
            "safe_likelihood_ratio_alternative_crossing": crossing(200, p1, safe),
            "conditions": "iid Bernoulli, p0=0.5, p1=0.8; every n=1..200; exact rational recursion"
        },
        "calibration_counterexample": {"outcomes": "0,1 repeating", "constant_forecast": 0.5,
            "overall_observed_frequency": 0.5, "constant_Brier": 0.25, "perfect_Brier": 0.0},
    }
    assert result["optional_peeking"]["safe_likelihood_ratio_null_crossing"][200] <= .05
    assert result["optional_peeking"]["alpha_spending_null_crossing"][200] <= .05
    assert result["optional_peeking"]["ordinary_fixed_time_tests_null_crossing"][200] > .05
    out = Path(__file__).with_name("results.json")
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
