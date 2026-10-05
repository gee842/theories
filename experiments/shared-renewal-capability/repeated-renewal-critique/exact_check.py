#!/usr/bin/env python3
"""Exact necessary bounds; no simulation and no estimated success probabilities."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SCALE = 10**30


def enclosure(x):
    return {"lower_numerator": x.numerator * SCALE // x.denominator,
            "upper_numerator": -(-x.numerator * SCALE // x.denominator),
            "denominator": SCALE}


def exp_enclosure(x, order=240):
    """Positive Taylor sum, then geometric domination of the remaining terms."""
    x = F(x)
    term = total = F(1)
    for k in range(1, order + 1):
        term *= x / k
        total += term
    first_omitted = term * x / (order + 1)
    ratio = x / (order + 2)
    assert 0 <= ratio < 1
    return total, total + first_omitted / (1 - ratio)


def poisson_tail_bounds(mu, threshold):
    assert threshold >= 1
    term = partial = F(1)
    for k in range(1, threshold):
        term *= F(mu, k)
        partial += term
    exp_lo, exp_hi = exp_enclosure(mu)
    return max(F(0), 1 - partial / exp_lo), 1 - partial / exp_hi


def minimum_equal_rate_material(n, target):
    material = 2
    while F(material - 1, material)**n < target:
        material += 1
    assert F(material - 2, material - 1)**n < target
    return material


def main():
    q = F(3, 4)
    examples = []
    for n in (1, 2, 5, 10, 20):
        examples.append({"cycles": n, "eventual_upper_exact": str(q**n),
                         "eventual_upper_decimal_enclosure": enclosure(q**n)})
    finite = []
    for n in (2, 5, 10):
        for horizon in (1, 3, 10):
            erlang_lo, erlang_hi = poisson_tail_bounds(4*horizon, n)
            capture_lo, capture_hi = poisson_tail_bounds(3*horizon, 6*n)
            race_lo, race_hi = q**n * erlang_lo, q**n * erlang_hi
            finite.append({"cycles": n, "deadline": horizon,
                           "race_bound_lower": enclosure(race_lo)["lower_numerator"],
                           "race_bound_upper": enclosure(race_hi)["upper_numerator"],
                           "capture_bound_lower": enclosure(capture_lo)["lower_numerator"],
                           "capture_bound_upper": enclosure(capture_hi)["upper_numerator"],
                           "joint_event_upper": enclosure(min(race_hi, capture_hi))["upper_numerator"],
                           "denominator": SCALE})
    thresholds = [{"cycles": 10, "required_reliability": str(target),
                   "minimum_N_under_beta_equals_d": minimum_equal_rate_material(10, target)}
                  for target in (F(9, 10), F(19, 20), F(99, 100))]
    assert thresholds[0]["minimum_N_under_beta_equals_d"] == 96
    assert thresholds[1]["minimum_N_under_beta_equals_d"] == 196
    rna = {"capacity": 300, "D": 5, "initial_h": 10, "initial_p": 10,
           "minimum_total_after_two_unpartitioned_rounds": 5**2*(10+10),
           "two_rounds_possible": 5**2*(10+10) <= 300}
    assert not rna["two_rounds_possible"]
    source_names = ["FULL-SUCCESSOR-CRITIQUE.md", "FULL-SUCCESSOR-RESULT.md",
                    "RNA-PARTIAL-IDENTIFICATION.md", "SUCCESSION-DIRECTION-CRITIQUE.md"]
    completion = ROOT / "_process/research/2026-10-05-support-and-shared-generativity/completion"
    record = {
        "scope": "Exact algebraic necessary bounds, not model probabilities or calibration.",
        "git_head_at_check": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_sha256": {name: sha256((completion/name).read_bytes()).hexdigest() for name in source_names},
        "arithmetic": "fractions.Fraction; exp positive Taylor order 240 and geometric remainder; displayed bounds outward at denominator 10^30",
        "eventual_bounds": examples, "finite_deadline_bounds": finite,
        "necessary_material_thresholds": thresholds, "unpartitioned_rna_check": rna,
        "status": "passed"}
    (HERE / "exact-check.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "thresholds": thresholds,
                      "unit_ten_cycle_upper": str(q**10),
                      "finite_deadline_rows": len(finite)}))


if __name__ == "__main__":
    main()
