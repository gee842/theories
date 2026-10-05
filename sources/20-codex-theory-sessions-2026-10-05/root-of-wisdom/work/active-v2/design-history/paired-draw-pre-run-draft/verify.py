"""Validate public model and solve finite-horizon Bellman recurrences exactly.

No external packages, participant execution, or dependence on realized world.
Fractions represent both probabilities and all monetary/loss quantities.
"""
import copy
import hashlib
import json
import random
import re
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

from build_cases import render_public_case

ROOT = Path(__file__).resolve().parent


def fraction_string(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def public_model(case):
    return {key: copy.deepcopy(value) for key, value in case.items() if key != "private"}


def solve(case):
    """Return exact continuation loss, feasible choices and all optimal ties.

    State=(posterior support, completed query IDs, cash spent, elapsed time).
    Deterministic observations mean prior restricted to support is sufficient.
    Query/action fees affect both objective and cash feasibility. Residual loss
    affects only objective. Returned values exclude already sunk query fees.
    """
    # Deliberately strip realized world before defining the oracle.
    case = public_model(case)
    priors = {w["id"]: F(w["prior"]) for w in case["worlds"]}
    constraints = case["constraints"]
    cache_states = {}

    @lru_cache(None)
    def bellman(support, completed, spent, elapsed):
        mass = sum(priors[w] for w in support)
        posterior = {w: priors[w] / mass for w in support}
        candidates = {}
        branches_by_query = {}
        for a in case["actions"]:
            if spent + F(a["fee"]) > F(constraints["cash_budget"]):
                continue
            if elapsed + a["duration"] > constraints["deadline"]:
                continue
            candidates[a["id"]] = F(a["fee"]) + sum(
                posterior[w] * F(a["residual_loss_by_world"][w]) for w in support)
        if len(completed) < constraints["max_queries"]:
            for q in case["queries"]:
                if q["id"] in completed or not set(q["prerequisites"]) <= set(completed):
                    continue
                if spent + F(q["fee"]) > F(constraints["cash_budget"]):
                    continue
                if elapsed + q["duration"] > constraints["deadline"]:
                    continue
                partitions = {}
                for w in support:
                    partitions.setdefault(q["response_by_world"][w], []).append(w)
                qvalue = F(q["fee"])
                branches = []
                for response, worlds in sorted(partitions.items()):
                    probability = sum(posterior[w] for w in worlds)
                    next_support = tuple(sorted(worlds))
                    next_completed = tuple(sorted((*completed, q["id"])))
                    continuation = bellman(next_support, next_completed,
                                           spent + F(q["fee"]), elapsed + q["duration"])
                    qvalue += probability * continuation["value"]
                    branches.append({"response": response,
                                     "probability": fraction_string(probability),
                                     "continuation_value": fraction_string(continuation["value"]),
                                     "optimal_next_choices": continuation["optimal_choices"]})
                candidates[q["id"]] = qvalue
                branches_by_query[q["id"]] = branches
        assert "fallback" in candidates, "safe fallback must always be feasible"
        value = min(candidates.values())
        result = {"value": value,
                  "optimal_choices": sorted(k for k, v in candidates.items() if v == value),
                  "choice_values": candidates,
                  "query_branches": branches_by_query}
        key = json.dumps([support, completed, fraction_string(spent), elapsed])
        cache_states[key] = {
            "support": list(support), "completed_queries": list(completed),
            "spent_cash": fraction_string(spent), "elapsed_time": elapsed,
            "posterior": {w: fraction_string(p) for w, p in posterior.items()},
            "value": fraction_string(value), "optimal_choices": result["optimal_choices"],
            "choice_values": {k: fraction_string(v) for k, v in candidates.items()},
            "query_branches": branches_by_query,
        }
        return result

    initial = bellman(tuple(sorted(priors)), (), F(0), 0)
    return {
        "case_id": case["case_id"],
        "bellman_value": fraction_string(initial["value"]),
        "optimal_first_choices": initial["optimal_choices"],
        "first_choice_values": {k: fraction_string(v) for k, v in initial["choice_values"].items()},
        "first_query_branches": initial["query_branches"],
        "evaluated_states": len(cache_states),
        "states": [cache_states[k] for k in sorted(cache_states)],
    }


def validate_case(case):
    worlds = [w["id"] for w in case["worlds"]]
    assert len(worlds) == len(set(worlds))
    assert sum(F(w["prior"]) for w in case["worlds"]) == 1
    assert all(F(w["prior"]) > 0 for w in case["worlds"])
    query_ids = {q["id"] for q in case["queries"]}
    action_ids = {a["id"] for a in case["actions"]}
    assert len(query_ids) == len(case["queries"])
    assert len(action_ids) == len(case["actions"])
    assert not query_ids & action_ids
    assert case["constraints"]["max_queries"] == 2
    assert F(case["constraints"]["cash_budget"]) >= 0
    assert case["constraints"]["deadline"] >= 0
    for q in case["queries"]:
        assert set(q["response_by_world"]) == set(worlds)
        assert all(isinstance(r, str) for r in q["response_by_world"].values())
        assert set(q["prerequisites"]) <= query_ids - {q["id"]}
        assert F(q["fee"]) >= 0 and q["duration"] >= 0
    for a in case["actions"]:
        assert set(a["residual_loss_by_world"]) == set(worlds)
        assert F(a["fee"]) >= 0 and a["duration"] >= 0
        assert all(F(loss) >= 0 for loss in a["residual_loss_by_world"].values())
    fallback = next(a for a in case["actions"] if a["id"] == "fallback")
    assert F(fallback["fee"]) == 0 and fallback["duration"] == 0
    assert len(set(fallback["residual_loss_by_world"].values())) == 1
    assert case["private"]["selected_world"] in worlds


def matched_pair_checks(cases):
    a, b, c, d, e, f = map(public_model, cases)
    for case in [a, b, c, d, e, f]:
        case.pop("case_id")
    for q in b["queries"]:
        if q["id"] in ["share_a", "share_b"]:
            q["fee"] = "1"
    d["constraints"]["deadline"] = 6
    next(x for x in f["actions"] if x["id"] == "option_b")["residual_loss_by_world"]["state_1"] = "9"
    assert a == b and c == d and e == f


def main():
    environment_path = ROOT / "environment.json"
    public_path = ROOT / "public-cases.json"
    environment = json.loads(environment_path.read_text())
    public = json.loads(public_path.read_text())
    cases = environment["cases"]
    assert len(cases) == 6
    assert public == {"schema_version": environment["schema_version"],
                      "shared_instructions": environment["public_rules"],
                      "cases": [render_public_case(c) for c in cases]}
    public_text = public["shared_instructions"] + "\n" + "\n".join(c["statement"] for c in public["cases"])
    # Include all alphanumeric/numeric tokens, including table entries; stricter
    # than whitespace word count for this compact public representation.
    words = len(re.findall(r"\b[\w/]+\b", public_text))
    assert words < 1800, words
    assert "private" not in public_path.read_text()
    rng = random.Random(environment["private_realization"]["seed"])
    realized = []
    for i in [0, 2, 4]:
        world_ids = [w["id"] for w in cases[i]["worlds"]]
        expected = world_ids[rng.randrange(len(world_ids))]
        realized.append(expected)
        assert cases[i]["private"]["selected_world"] == expected
        assert cases[i + 1]["private"]["selected_world"] == expected
    assert realized == environment["private_realization"]["selected_worlds_by_pair"]
    for case in cases:
        validate_case(case)
    matched_pair_checks(cases)
    results = [solve(case) for case in cases]
    expected_first = {
        "A01": ("3", ["share_a", "share_b"]),
        "A02": ("7", ["choose_0", "choose_1"]),
        "A03": ("3", ["open_panel"]),
        "A04": ("8", ["fallback"]),
        "A05": ("5", ["option_a"]),
        "A06": ("2", ["inspect"]),
    }
    for result in results:
        assert (result["bellman_value"], result["optimal_first_choices"]) == expected_first[result["case_id"]]
    # Changing the private realized world cannot change any oracle output.
    for case, result in zip(cases, results):
        changed = copy.deepcopy(case)
        for world in case["worlds"]:
            changed["private"]["selected_world"] = world["id"]
            assert solve(changed) == result
    out = {
        "status": "all_checks_passed",
        "exact_arithmetic": "fractions.Fraction",
        "objective": "Expected sum of query fees, terminal fee, and terminal residual loss",
        "public_word_count": words,
        "word_count_method": "regex alphanumeric/numeric tokens over shared instructions and six statements",
        "checks": ["normalized rational priors", "complete finite response/loss tables",
                   "unique disjoint query/action IDs", "maximum two nonrepeatable queries",
                   "cash and deadline feasibility including terminal action",
                   "prerequisites enforced", "fallback always feasible",
                   "exact controlled matched-pair differences", "public rendering matches public model",
                   "all optimal initial ties retained", "reproducible fixed-seed private worlds",
                   "oracle invariant to every private world selection", "public statements under 1800 words"],
        "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in [environment_path, public_path, ROOT / "verify.py", ROOT / "build_cases.py"]},
        "results": results,
    }
    (ROOT / "verification.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"status": out["status"], "public_word_count": words,
                      "cases": [{k: r[k] for k in ["case_id", "bellman_value", "optimal_first_choices"]}
                                for r in results]}, indent=2))


if __name__ == "__main__":
    main()
