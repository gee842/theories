"""Finite exact illustration of experience-dependent concept generation.

The generator receives no world identity, XOR rule, or true risk. It fits
majority-label tables for every accessible singleton/pair partition. The
evaluator enumerates worlds separately. All numeric calculations are exact.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import json
from pathlib import Path

ROWS = tuple(product((0, 1), repeat=3))
LABELS = tuple(product((0, 1), repeat=8))
SINGLES = tuple(combinations(range(3), 1))
PAIRS = tuple(combinations(range(3), 2))
PENALTY = F(1, 32)
SEARCH_COST = F(1, 4)
FEATURE_COST = F(1, 50)

def fit(fields, labels):
    table = {}
    for key in product((0, 1), repeat=len(fields)):
        selected = [y for row, y in zip(ROWS, labels)
                    if tuple(row[j] for j in fields) == key]
        table[key] = int(2 * sum(selected) > len(selected))
    preds = tuple(table[tuple(row[j] for j in fields)] for row in ROWS)
    error = F(sum(p != y for p, y in zip(preds, labels)), 8)
    return (error + PENALTY * (2 ** len(fields) - 1), fields, preds)

def generate(labels, procedure):
    # No signal-specific feature/rule is present in these operations.
    coarse = fit((), labels)
    single_fits = [fit(fields, labels) for fields in SINGLES]
    best_single = min(single_fits)
    cost = F(8) + 3 * SEARCH_COST
    if procedure == "greedy":
        if best_single[0] >= coarse[0]:
            return None, cost
        pair_fields = [pair for pair in PAIRS if best_single[1][0] in pair]
    else:
        pair_fields = PAIRS
    cost += len(pair_fields) * SEARCH_COST
    best = min([coarse] + single_fits + [fit(p, labels) for p in pair_fields])
    if best[0] >= coarse[0]:
        return None, cost
    return best, cost + 8  # Pay for fresh validation only when a candidate exists.

def match_tail(eps, underlying_matches):
    probs = [1 - eps] * underlying_matches + [eps] * (8 - underlying_matches)
    count = [F(1)]
    for p in probs:
        nxt = [F(0)] * (len(count) + 1)
        for k, w in enumerate(count):
            nxt[k] += w * (1 - p)
            nxt[k + 1] += w * p
        count = nxt
    return sum(count[7:])

def packed(x):
    return {"exact": str(x), "decimal": float(x)}

def evaluate(eps, procedure):
    # World generation belongs only to this evaluator.
    truth = tuple(row[0] ^ row[1] for row in ROWS)
    tails = [match_tail(eps, k) for k in range(9)]
    mass = proposal = adoption = gain = cost = F(0)
    generated = {}
    for labels in LABELS:
        noise_count = sum(y != z for y, z in zip(labels, truth))
        w = eps ** noise_count * (1 - eps) ** (8 - noise_count)
        if not w:
            continue
        mass += w
        chosen, expense = generate(labels, procedure)
        cost += w * expense
        if chosen is None:
            continue
        proposal += w
        _, fields, preds = chosen
        generated[str(fields)] = generated.get(str(fields), F(0)) + w
        k = sum(p == z for p, z in zip(preds, truth))
        accept = tails[k]
        adoption += w * accept
        risk = F(k, 8) * eps + F(8 - k, 8) * (1 - eps)
        gain += w * accept * (F(1, 2) - risk - len(fields) * FEATURE_COST)
    assert mass == 1
    if eps == F(1, 2):
        assert adoption == proposal * F(9, 256)
    return {
        "noise": packed(eps), "procedure": procedure,
        "proposal_probability": packed(proposal),
        "adoption_probability": packed(adoption),
        "expected_inquiry_cost": packed(cost),
        "expected_net_gain_per_future_decision": packed(gain),
        "extra_expected_loss_100_future_decisions": packed(cost - 100 * gain),
        "break_even_future_decisions": packed(cost / gain) if gain > 0 else None,
        "selected_fields_probability": {k: packed(v) for k, v in generated.items()},
    }

def checks():
    truth = tuple(row[0] ^ row[1] for row in ROWS)
    assert generate(truth, "greedy")[0] is None
    selected, expense = generate(truth, "compositional")
    assert selected[1] == (0, 1) and selected[2] == truth
    assert expense == F(35, 2)
    # Independently enumerate every validation label vector for every possible
    # number of correct underlying predictions; compare to the DP tail.
    eps = F(1, 4)
    for k in range(9):
        preds = (0,) * k + (1,) * (8 - k)
        brute = F(0)
        for ys in LABELS:
            weight = eps ** sum(ys) * (1 - eps) ** (8 - sum(ys))
            if sum(y == p for y, p in zip(ys, preds)) >= 7:
                brute += weight
        assert brute == match_tail(eps, k)
    assert match_tail(F(1, 2), 0) == F(9, 256)
    return {"exact_validation_tail_checks": 9, "greedy_XOR_plateau": True,
            "generic_generator_recovers_pair": True, "fair_null_tail": "9/256"}

def main():
    result = {"checks": checks(), "parameters": {
        "training": "One observation at each of the 8 three-bit contexts",
        "validation": "Fresh observation at each context, accept >=7/8 correct",
        "grammar": "All singleton and pair partitions, fitted majority tables",
        "penalty_per_extra_cell": str(PENALTY),
        "cost_per_candidate_fit": str(SEARCH_COST),
        "cost_per_outcome": "1",
        "deployment_cost_per_retained_feature": str(FEATURE_COST),
        "loss": "0-1 prediction loss; deployment context uniform on 8 rows",
        "tie_rule": "Majority ties predict zero; score ties lexicographic",
    }, "results": [evaluate(eps, proc)
        for eps in (F(0), F(1, 10), F(1, 4), F(1, 2))
        for proc in ("greedy", "compositional")]}
    destination = Path(__file__).with_name("concept-generation-results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    for row in result["results"]:
        print(row["noise"]["exact"], row["procedure"],
              "propose", row["proposal_probability"]["decimal"],
              "adopt", row["adoption_probability"]["decimal"],
              "cost", row["expected_inquiry_cost"]["decimal"],
              "net_future", row["expected_net_gain_per_future_decision"]["decimal"],
              "extra100", row["extra_expected_loss_100_future_decisions"]["decimal"])

if __name__ == "__main__":
    main()
