#!/usr/bin/env python3
"""New exact prediction/identification checks; reuse, do not rerun, the frozen audit.

No workbook extraction, original-notebook execution, fit, random simulation, or
ODE solver. Writes only exact-check.json beside this file. All scientific
inequalities use fractions/integers; decimal strings are presentation only.
"""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
AUDIT = ROOT / "experiments/shared-renewal-capability/rna-identification/audit.json"
AUDIT_SHA = "4da724ddfde3a002d08c10cc4b12e4dbffaa0f0b5882b4e36e01cae8697c1289"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def enc(x: Q) -> str:
    return str(x)


def decimal(x: Q) -> str:
    with localcontext() as ctx:
        ctx.prec = 42
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def law_summary(law, a, b, cap):
    assert sum(w for w, x, y in law) == 1
    assert all(w >= 0 and x >= 0 and y >= 0 and x + y <= cap for w, x, y in law)
    return {
        "law": [{"weight": enc(w), "x": enc(x), "y": enc(y)} for w, x, y in law],
        "mean_x": enc(sum(w * x for w, x, y in law)),
        "mean_y": enc(sum(w * y for w, x, y in law)),
        "joint_probability": enc(sum(w for w, x, y in law if x >= a and y >= b)),
    }


def mean_bound_witness(mx, my, a, b, cap):
    """Attain both ends of the sharp mean+simplex bound; proof is in the note."""
    mx, my, a, b, cap = map(Q, (mx, my, a, b, cap))
    assert a > 0 and b > 0 and mx >= 0 and my >= 0 and mx + my <= cap
    if cap == 0:
        low = [(Q(1), Q(0), Q(0))]
    else:
        low = [(mx / cap, cap, Q(0)), (my / cap, Q(0), cap),
               (1 - (mx + my) / cap, Q(0), Q(0))]
    upper = Q(0) if cap < a + b else min(Q(1), mx / a, my / b)
    if upper == 0:
        high = low
    elif upper == 1:
        high = [(Q(1), mx, my)]
    elif mx / a <= my / b:
        ys = max(b, (my - (1 - upper) * cap) / upper)
        assert ys <= min(cap - a, my / upper)
        high = [(upper, a, ys), (1 - upper, Q(0), (my - upper * ys) / (1 - upper))]
    else:
        xs = max(a, (mx - (1 - upper) * cap) / upper)
        assert xs <= min(cap - b, mx / upper)
        high = [(upper, xs, b), (1 - upper, (mx - upper * xs) / (1 - upper), Q(0))]
    lo, hi = law_summary(low, a, b, cap), law_summary(high, a, b, cap)
    for result in (lo, hi):
        assert Q(result["mean_x"]) == mx and Q(result["mean_y"]) == my
    assert Q(lo["joint_probability"]) == 0
    assert Q(hi["joint_probability"]) == upper
    return {"inputs": dict(zip(("mean_x", "mean_y", "a", "b", "cap"),
                                map(enc, (mx, my, a, b, cap)))),
            "identified_interval": ["0", enc(upper)], "lower_witness": lo,
            "upper_witness": hi}


def main():
    assert sha(AUDIT) == AUDIT_SHA
    prior = json.loads(AUDIT.read_text())
    before = {path: sha(ROOT / path) for path in prior["source_sha256_before_and_after"]}
    assert before == prior["source_sha256_before_and_after"]
    producer = ROOT / "experiments/shared-renewal-capability/rna-identification/audit.py"
    assert sha(producer) == prior["checker_sha256"]

    # These are display-rounding enclosures, not experimental confidence bounds.
    half_unit = Q(1, 2_000_000)
    a_print = Q(str(prior["printed_S23_matrix"][1][1]))
    b_print = Q(str(prior["printed_S23_matrix"][1][3]))
    alo, ahi = a_print - half_unit, a_print + half_unit
    blo, bhi = b_print - half_unit, b_print + half_unit
    assert alo > Q(279, 100)
    assert Q(2046, 1000) < blo / ahi <= bhi / alo < Q(2047, 1000)
    # Monotonicity and integer powers prove 26.9 < 5**(b/a) < 26.99.
    assert 5**2046 * 10**1000 > 269**1000
    assert 5**2047 * 100**1000 < 2699**1000
    qlo, qhi = Q(269, 10), Q(2699, 100)

    # h >= 60 already requires 5h >= C. For h >= 1, p >= 12 also fails.
    assert 5 + qlo * 12 > 300
    success_lo = {(h, p) for h in range(1, 60) for p in range(1, 12)
                  if 5 * h + qhi * p < 300}
    success_hi = {(h, p) for h in range(1, 60) for p in range(1, 12)
                  if 5 * h + qlo * p < 300}
    assert success_lo == success_hi
    max_h = [max((h for h, pp in success_lo if pp == p), default=0)
             for p in range(1, 12)]
    assert max_h == [54, 49, 43, 38, 33, 27, 22, 16, 11, 6, 0]
    assert len(success_lo) == 299

    # A uniform analytic hitting-time bound, not a numerical ODE integration.
    # Integral <= 4/5 + (1/5)ln(120001) < 16/5, as proved in the note.
    exp12_lower = sum((Q(12**n, factorial(n)) for n in range(17)), Q(0))
    assert exp12_lower > 120001
    time_upper = Q(16, 5) / Q(279, 100)
    assert time_upper == Q(320, 279) and time_upper < 2

    # Exact Poisson success weight, including independent retention 1/5.
    weight = sum((Q(10**(h + p), factorial(h) * factorial(p))
                  for h, p in success_lo), Q(0)) / 5
    n = 200
    exp20_lower = sum((Q(20**k, factorial(k)) for k in range(n + 1)), Q(0))
    remainder_upper = Q(20**(n + 1), factorial(n + 1)) / (1 - Q(20, n + 2))
    # All later Taylor term ratios <= 20/(n+2); hence a geometric tail bound.
    prob_lower, prob_upper = weight / (exp20_lower + remainder_upper), weight / exp20_lower
    scale = 10**30
    floor = (prob_lower.numerator * scale) // prob_lower.denominator
    ceil = -((-prob_upper.numerator * scale) // prob_upper.denominator)
    assert Q(floor, scale) < prob_lower <= prob_upper < Q(ceil, scale)
    assert ceil == floor + 1

    # Same initial state and the same full individual trajectory laws can have
    # different joint dependence. Endpoints certify the note's f(t) construction.
    aligned = [(Q(1, 2), Q(5), Q(5)), (Q(1, 2), Q(1), Q(1))]
    opposed = [(Q(1, 2), Q(5), Q(1)), (Q(1, 2), Q(1), Q(5))]
    def marginal(law, index):
        values = sorted({row[index] for row in law})
        return {enc(v): enc(sum(row[0] for row in law if row[index] == v)) for v in values}
    for i in (1, 2):
        assert marginal(aligned, i) == marginal(opposed, i) == {"1": "1/2", "5": "1/2"}
    aligned_result = law_summary(aligned, Q(5), Q(5), Q(10))
    opposed_result = law_summary(opposed, Q(5), Q(5), Q(10))
    assert Q(aligned_result["joint_probability"]) / 5 == Q(1, 10)
    assert Q(opposed_result["joint_probability"]) / 5 == 0

    # Fixed diagnostic cases exercise every constructive case, not a parameter fit
    # or a numerical proof replacing the analytic sharpness argument.
    cases = [(1, 9, 3, 3, 10), (9, 1, 3, 3, 10), (4, 4, 3, 3, 10),
             (0, 5, 3, 3, 10), (1, 2, 3, 4, 10),
             (Q(3, 2), Q(9, 2), 2, 3, 6), (2, 2, 3, 3, 4), (0, 0, 1, 1, 0)]
    mean_witnesses = [mean_bound_witness(*case) for case in cases]

    pair = next(x for x in prior["reconstruction"]
                if x["donor"] == "HL2-228" and x["target"] == "PL2-228")
    paired_rows = pair["replicate_rows"]
    assert [row["row"] for row in paired_rows] == [37, 38, 39]
    assert all(Q(str(row["donor_fold"])) < 5 for row in paired_rows)
    assert all(Q(str(row["target_fold"])) > 5 for row in paired_rows)

    after = {path: sha(ROOT / path) for path in before}
    assert before == after and sha(AUDIT) == AUDIT_SHA
    result = {
        "status": "passed; exact conditional model certificate and identification witnesses",
        "checker_sha256": sha(Path(__file__)),
        "frozen_audit_path": str(AUDIT.relative_to(ROOT)),
        "frozen_audit_sha256_before_and_after": AUDIT_SHA,
        "frozen_audit_producer_sha256": sha(producer),
        "source_sha256_before_and_after": before,
        "scope": "No source extraction rerun, original notebook execution, ODE integration, "
                 "simulation, parameter fit, measured task probability, or physical clock calibration.",
        "conditional_ODE_certificate": {
            "two_RNA_restriction": ["HL2-228", "PL2-228"],
            "coefficient_enclosures": {"a": list(map(enc, (alo, ahi))),
                                       "b": list(map(enc, (blo, bhi)))},
            "enclosure_scope": "Six-decimal S23 rounding only, not experimental uncertainty.",
            "five_to_ratio_bounds": list(map(enc, (qlo, qhi))),
            "capacity": 300, "dilution": 5, "normalized_deadline": 2,
            "initial_law": "independent Poisson(10) counts of the two selected RNAs; other RNAs absent",
            "success_states": len(success_lo), "max_h_for_p_1_through_11": max_h,
            "uniform_success_time_strict_upper": enc(time_upper),
            "exp12_Taylor_terms_0_through": 16,
            "exp12_Taylor_lower_bound": enc(exp12_lower),
            "probability_equals_exp_minus20_times_rational": enc(weight),
            "exp20_Taylor_terms_0_through": n,
            "exp20_Taylor_lower_bound": enc(exp20_lower),
            "exp20_remainder_upper_bound": enc(remainder_upper),
            "probability_strict_lower_fraction": f"{floor}/{scale}",
            "probability_strict_upper_fraction": f"{ceil}/{scale}",
            "probability_decimal_for_display": decimal((prob_lower + prob_upper) / 2),
        },
        "same_marginal_path_law_witness": {
            "initial": [1, 1], "capacity": 10, "dilution": 5,
            "marginal_endpoint_law_each_RNA": marginal(aligned, 1),
            "aligned_endpoint_law": aligned_result, "opposed_endpoint_law": opposed_result,
            "retained_joint_probabilities": ["1/10", "0"],
            "path_extension": "Any common continuous nondecreasing f with f(0)=0,f(T)=1: "
                              "aligned=(1+4Zf,1+4Zf); opposed=(1+4Zf,1+4(1-Z)f); "
                              "Z is a fair Bernoulli variable.",
            "scope": "Endpoint/path-law class; these are not solutions of the fixed published ODE "
                     "or asserted elementary chemical mechanisms.",
        },
        "sharp_mean_bound_constructive_examples": mean_witnesses,
        "paired_source_rows_reused_from_frozen_audit": paired_rows,
        "paired_source_scope": "Three translation-uncoupled bulk assay records all miss the donor "
                               "fivefold threshold. Target folds are negative-control normalized. "
                               "Not three droplet joint replacement/retention trials.",
    }
    output = HERE / "exact-check.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "success_states": len(success_lo),
                      "J_strict_interval": [f"{floor}/{scale}", f"{ceil}/{scale}"],
                      "J_display": result["conditional_ODE_certificate"]["probability_decimal_for_display"],
                      "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
