"""Evaluator-only exact policy values; these truths never enter the learner."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import ceil
import json
import revise_standard as m

def task_family(profile):
    if profile in ("interaction", "noisy_interaction"):
        eps = F(1, 4) if profile == "noisy_interaction" else F(0)
        return [(F(1, 6), m.Task(tuple(row[a] ^ row[b] ^ flip for row in m.ROWS), eps))
                for a, b in m.PAIRS for flip in (0, 1)]
    if profile == "single":
        return [(F(1, 6), m.Task(tuple(row[a] ^ flip for row in m.ROWS), F(0)))
                for a in range(3) for flip in (0, 1)]
    if profile == "constant":
        return [(F(1, 2), m.Task((flip,) * 8, F(0))) for flip in (0, 1)]
    if profile == "null":
        return [(F(1), m.Task((0,) * 8, F(1, 2)))]
    if profile == "mixed":
        return [(w / 2, task) for profile in ("interaction", "null") for w, task in task_family(profile)]
    raise ValueError(profile)

def acceptance(task, predictions):
    dp = [F(1)]
    for truth, prediction in zip(task.truth, predictions):
        p = 1 - task.noise if truth == prediction else task.noise
        out = [F(0)] * (len(dp) + 1)
        for i, weight in enumerate(dp):
            out[i] += weight * (1 - p)
            out[i + 1] += weight * p
        dp = out
    return sum(dp[7:])

def expected_error(task, predictions):
    return sum(task.noise if t == p else 1 - task.noise
               for t, p in zip(task.truth, predictions)) / 8

def exact_value(profile, rule, cfg):
    cost = errors = proposals = adoptions = mass = F(0)
    for task_weight, task in task_family(profile):
        for ys in product((0, 1), repeat=8):
            noisy = sum(y != t for y, t in zip(ys, task.truth))
            w = task_weight * task.noise ** noisy * (1 - task.noise) ** (8 - noisy)
            if not w:
                continue
            mass += w
            coarse, candidate, expense = m.generate(rule, ys, cfg)
            if candidate is None:
                cost += w * expense
                errors += w * cfg.horizon * expected_error(task, coarse.predictions)
                continue
            proposals += w
            p = acceptance(task, candidate.predictions)
            adoptions += w * p
            cost += w * (expense + 8 * cfg.label_cost + p * cfg.horizon * len(candidate.fields) * cfg.field_cost)
            errors += w * cfg.horizon * (p * expected_error(task, candidate.predictions)
                                        + (1 - p) * expected_error(task, coarse.predictions))
    assert mass == 1
    return {"expected_expense": m.pack(cost), "expected_errors": m.pack(errors),
            "expected_loss": m.pack(cost + errors), "proposal_probability": m.pack(proposals),
            "adoption_probability": m.pack(adoptions)}

def main():
    cfg = m.Config()
    rows = []
    for profile in ("interaction", "single", "constant", "null", "noisy_interaction", "mixed"):
        old = exact_value(profile, m.Rule(), cfg)
        new = exact_value(profile, m.edit_rule(m.Rule())[0], cfg)
        gain = F(old["expected_loss"]["exact"]) - F(new["expected_loss"]["exact"])
        rows.append({"profile": profile, "incumbent": old, "edited": new, "true_expected_gain": m.pack(gain)})
    assert rows[0]["true_expected_gain"]["exact"] == "2069/100"
    assert rows[1]["true_expected_gain"]["exact"] == "-1/4"
    assert rows[2]["true_expected_gain"]["exact"] == "-3/4"
    root = Path(__file__).parent
    study = json.loads(root.joinpath("standard-revision-results.json").read_text())["records"][0]
    outlay = F(study["spent"]["exact"])
    gain = F(rows[0]["true_expected_gain"]["exact"])
    lower = study["fresh_outer_check"]["lower_confidence_bound"]
    result = {"status": "Exact evaluator computation, never provided as feedback to learner", "rows": rows,
              "total_outlay_hurdle": {"study_expense": m.pack(outlay),
                  "future_episodes_at_exact_gain": m.pack(outlay / gain),
                  "whole_future_episodes_at_exact_gain": ceil(outlay / gain),
                  "future_episodes_at_confidence_lower_bound": float(outlay) / lower,
                  "whole_future_episodes_at_confidence_lower_bound": ceil(float(outlay) / lower),
                  "interpretation": "Conservative future value required to match every priced study payment, ignoring service value produced during study. Not total net ROI or proof that objective gains become spendable cash. Assumes unchanged task law, costs, horizon, and fixed rule."}}
    root.joinpath("exact-transfer-results.json").write_text(json.dumps(result, indent=2) + "\n")
    for row in rows:
        print(row["profile"], row["true_expected_gain"])
    print("hurdle", result["total_outlay_hurdle"])

if __name__ == "__main__":
    main()
