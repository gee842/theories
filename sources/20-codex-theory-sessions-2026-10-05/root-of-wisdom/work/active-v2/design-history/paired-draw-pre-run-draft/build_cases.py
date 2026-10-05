"""Construct the finite active-inquiry cases; no participant execution."""
import copy
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SEED = 2026100502
RULES = (
    "Each case is independent. The hidden world is sampled from the listed prior. "
    "You know the full model below but not the selected world. At each turn choose "
    "exactly one listed query ID or terminal action ID. A query returns only its "
    "listed response in the hidden world. Queries are deterministic, may not be "
    "repeated, and at most two may be used. All listed prerequisite queries must "
    "already have been completed. A terminal action ends the case. "
    "All fees and residual losses use loss units; one cash unit pays one fee unit. "
    "Minimize expected total loss: all query fees plus terminal action fee plus "
    "world-dependent residual loss. Cash budget covers upfront query and action "
    "fees only, not residual loss. Durations add sequentially, and the terminal "
    "action must finish by the deadline. Time has no additional loss charge. "
    "A choice is feasible only if it fits remaining cash and time and satisfies "
    "query limits and prerequisites. The fallback always costs zero cash and time. "
    "No external tools or evidence are available. Tables give values in world "
    "order. Fractions are exact. All worlds, responses, fees and losses are specified."
)


def query(qid, fee, duration, responses, worlds, prerequisites=()):
    return {"id": qid, "fee": str(fee), "duration": duration,
            "prerequisites": list(prerequisites),
            "response_by_world": dict(zip(worlds, responses))}


def action(aid, fee, duration, residuals, worlds):
    return {"id": aid, "fee": str(fee), "duration": duration,
            "residual_loss_by_world": dict(zip(worlds, map(str, residuals)))}


def pair_one(case_id, price):
    worlds = ["w00", "w01", "w10", "w11"]
    return {
        "case_id": case_id,
        "worlds": [{"id": w, "prior": "1/4"} for w in worlds],
        "queries": [
            query("share_a", price, 1, ["0", "1", "0", "1"], worlds),
            query("share_b", price, 1, ["0", "1", "1", "0"], worlds),
            query("status", "1/2", 1, ["ready"] * 4, worlds),
        ],
        "actions": [
            action("choose_0", 1, 1, [0, 0, 12, 12], worlds),
            action("choose_1", 1, 1, [12, 12, 0, 0], worlds),
            action("fallback", 0, 0, [8] * 4, worlds),
        ],
        "constraints": {"max_queries": 2, "cash_budget": "10", "deadline": 5},
    }


def pair_two(case_id, deadline):
    worlds = ["fault_0", "fault_1"]
    return {
        "case_id": case_id,
        "worlds": [{"id": w, "prior": "1/2"} for w in worlds],
        "queries": [
            query("open_panel", 1, 1, ["opened"] * 2, worlds),
            query("diagnose", 1, 2, worlds, worlds, ["open_panel"]),
            query("status", "1/2", 1, ["online"] * 2, worlds),
        ],
        "actions": [
            action("repair_0", 1, 3, [0, 20], worlds),
            action("repair_1", 1, 3, [20, 0], worlds),
            action("fallback", 0, 0, [8] * 2, worlds),
        ],
        "constraints": {"max_queries": 2, "cash_budget": "4", "deadline": deadline},
    }


def pair_three(case_id, second_b_loss):
    worlds = ["state_0", "state_1"]
    return {
        "case_id": case_id,
        "worlds": [{"id": w, "prior": "1/2"} for w in worlds],
        "queries": [
            query("inspect", 1, 1, worlds, worlds),
            query("status", "1/2", 1, ["calibrated"] * 2, worlds),
        ],
        "actions": [
            action("option_a", 1, 1, [0, 8], worlds),
            action("option_b", 1, 1, [6, second_b_loss], worlds),
            action("fallback", 0, 0, [10] * 2, worlds),
        ],
        "constraints": {"max_queries": 2, "cash_budget": "4", "deadline": 3},
    }


def render_public_case(case):
    ids = [w["id"] for w in case["worlds"]]
    prior = ", ".join(f"{w['id']}:{w['prior']}" for w in case["worlds"])
    c = case["constraints"]
    lines = [
        f"World order: {', '.join(ids)}. Prior: {prior}.",
        f"Cash budget: {c['cash_budget']}; deadline: {c['deadline']} time units; "
        f"maximum queries: {c['max_queries']}.",
        "Query table: ID | fee | duration | prerequisites | responses in world order.",
    ]
    for q in case["queries"]:
        prerequisites = ",".join(q["prerequisites"]) or "none"
        answers = ", ".join(q["response_by_world"][w] for w in ids)
        lines.append(f"{q['id']} | {q['fee']} | {q['duration']} | {prerequisites} | {answers}")
    lines.append("Terminal action table: ID | fee | duration | residual losses in world order.")
    for a in case["actions"]:
        losses = ", ".join(a["residual_loss_by_world"][w] for w in ids)
        lines.append(f"{a['id']} | {a['fee']} | {a['duration']} | {losses}")
    return {"case_id": case["case_id"], "statement": "\n".join(lines),
            "query_ids": [q["id"] for q in case["queries"]],
            "action_ids": [a["id"] for a in case["actions"]],
            "budgets": copy.deepcopy(c)}


def main():
    cases = [pair_one("A01", 1), pair_one("A02", 4),
             pair_two("A03", 6), pair_two("A04", 5),
             pair_three("A05", 9), pair_three("A06", 0)]
    rng = random.Random(SEED)
    # Each matched pair shares one draw. Marginally, each case has its listed prior.
    selected = []
    for idx in [0, 2, 4]:
        choices = [w["id"] for w in cases[idx]["worlds"]]
        chosen = choices[rng.randrange(len(choices))]
        selected.append(chosen)
        for case in cases[idx:idx + 2]:
            case["private"] = {"selected_world": chosen}
    environment = {
        "schema_version": "active-inquiry-v2.1",
        "public_rules": RULES,
        "matched_pairs": [
            {"case_ids": ["A01", "A02"], "construct": "complementary evidence",
             "only_model_difference": "share_a and share_b fees: 1 versus 4"},
            {"case_ids": ["A03", "A04"], "construct": "diagnosis consumes action time",
             "only_model_difference": "deadline: 6 versus 5"},
            {"case_ids": ["A05", "A06"], "construct": "decision sufficiency despite uncertainty",
             "only_model_difference": "option_b residual loss in state_1: 9 versus 0"},
        ],
        "private_realization": {
            "seed": SEED,
            "method": "Python random.Random(seed); for the three pairs in file order, "
                      "draw randrange(number of worlds), using the listed world order; "
                      "use that same world for both members of each pair.",
            "balancing": "No balancing or resampling; matched members share the draw. "
                         "Each pair draw is independent and has its listed uniform prior.",
            "selected_worlds_by_pair": selected,
            "disclosure": "Private; never include this object, selected worlds, or oracle "
                          "results in participant material. Pair structure and cross-case "
                          "coupling are also private; run each case with fresh isolated context."
        },
        "cases": cases,
    }
    public = {"schema_version": environment["schema_version"],
              "shared_instructions": RULES,
              "cases": [render_public_case(c) for c in cases]}
    (ROOT / "environment.json").write_text(json.dumps(environment, indent=2) + "\n")
    (ROOT / "public-cases.json").write_text(json.dumps(public, indent=2) + "\n")


if __name__ == "__main__":
    main()
