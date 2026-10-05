"""Three supplied phases; actual bidirectional revision of one carried rule.

Schedule, phase funding, counts, seed, and alpha allocation are fixed here before
running. The learner's decisions depend on observed reports, not phase labels.
The previously audited single-study code is imported without modification.
"""
from dataclasses import asdict, replace
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import random
import revise_standard as m

SCHEDULE = (
    ("interaction", 256, F(17000)),
    ("null", 8192, F(340000)),
    ("interaction", 256, F(17000)),
)
DISCOVERY_PAIRS = 128
POST_TASKS = 32
SEED = 7140301

def toggle(rule):
    # Symmetric, fixed grammar independent of any environment description.
    return replace(rule, require_improving_prefix=not rule.require_improving_prefix)

def phase_run(current, profile, checking_pairs, budget, phase):
    cfg = replace(m.Config(), discovery_pairs=DISCOVERY_PAIRS,
                  checking_pairs=checking_pairs, alpha=.05 / 3)
    candidate = toggle(current)
    max_expense = 16 * cfg.label_cost + 6 * cfg.fit_cost + 2 * cfg.horizon * cfg.field_cost
    reserve = (2 * (cfg.discovery_pairs + cfg.checking_pairs) + POST_TASKS) * max_expense
    answer = {"phase": phase, "external_task_profile": profile,
              "opening": "externally scheduled protected probe", "initial_rule": asdict(current),
              "generated_edit": asdict(candidate), "available_budget": m.pack(budget),
              "required_worst_case_reserve_including_post_tasks": m.pack(reserve),
              "discovery_pairs": cfg.discovery_pairs, "checking_pairs": cfg.checking_pairs,
              "alpha": cfg.alpha}
    if budget < reserve:
        answer.update(status="unfunded", final_rule=asdict(current), expense=m.pack(F(0)))
        return current, answer
    spent = F(0)
    def collect(n, stream):
        nonlocal spent
        rng = random.Random(SEED + 1000000 * phase + stream)
        reports = []
        for _ in range(n):
            task = m.draw_task(profile, rng)
            pair = (m.run_policy(current, task, cfg, rng), m.run_policy(candidate, task, cfg, rng))
            spent += sum(r.expense for r in pair)
            assert spent <= budget
            reports.append(pair)
        return reports
    discovery = collect(cfg.discovery_pairs, 11)
    answer["discovery"] = m.summarize(discovery)
    all_study = list(discovery)
    if m.choose_from_discovery(discovery):
        checking = collect(cfg.checking_pairs, 101)
        all_study += checking
        answer["checking"] = m.summarize(checking)
        answer["fresh_outer_check"] = m.check_reports(checking, cfg)
        if answer["fresh_outer_check"]["pass"]:
            current = candidate
            status = "rule_revised"
        else:
            status = "edit_failed_fresh_check"
    else:
        status = "edit_failed_discovery"
    # Enact the actual installed rule on new service tasks after each decision.
    rng = random.Random(SEED + 1000000 * phase + 1009)
    post = []
    for _ in range(POST_TASKS):
        task = m.draw_task(profile, rng)
        report = m.run_policy(current, task, cfg, rng)
        spent += report.expense
        assert spent <= budget
        post.append(report)
    answer["post_decision_execution"] = {
        "actual_rule": asdict(current), "tasks": len(post),
        "expense": m.pack(sum(r.expense for r in post)),
        "errors": sum(r.prediction_errors for r in post),
        "proposals": sum(r.proposed for r in post), "adoptions": sum(r.adopted for r in post)}
    total_study_loss = sum(a.observed_loss + b.observed_loss for a, b in all_study)
    matched_loss_estimate = 2 * sum(a.observed_loss for a, _ in all_study)
    answer["matched_study_service_accounting"] = {
        "blocks": 2 * len(all_study), "actual_study_loss": m.pack(total_study_loss),
        "two_incumbent_streams_loss_estimate": m.pack(matched_loss_estimate),
        "incremental_loss_estimate": m.pack(total_study_loss - matched_loss_estimate),
        "caveat": "Reuses study reports; exact on deterministic interaction, an uncorrected descriptive estimator on stochastic null. Not a second inferential claim."}
    answer.update(status=status, final_rule=asdict(current), expense=m.pack(spent))
    return current, answer

def main():
    installed = m.Rule()
    records = []
    for phase, (profile, checks, budget) in enumerate(SCHEDULE, 1):
        installed, record = phase_run(installed, profile, checks, budget, phase)
        records.append(record)
    # The outcome is reported, never forced. No seed search or continuation.
    source = Path(__file__)
    result = {"seed": SEED, "fixed_before_execution": True,
              "grammar": "Toggle the same prefix-gain precondition in either direction",
              "discovery_pairs_per_phase": DISCOVERY_PAIRS, "post_decision_tasks_per_phase": POST_TASKS,
              "familywise_alpha_budget": .05,
              "conditional_guarantee": "At most .05 probability of one or more nonpositive-mean-gain revisions across these three scheduled checks, under independent fresh phase pairs conditional on prior history, stable within-phase task laws, bounded stated losses, fixed counts, and no further tests.",
              "records": records, "final_rule": asdict(installed),
              "total_priced_expense": m.pack(sum(F(r["expense"]["exact"]) for r in records)),
              "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
    source.with_name("repeated-revision-results.json").write_text(json.dumps(result, indent=2) + "\n")
    for row in records:
        check = row.get("fresh_outer_check", {})
        print(row["phase"], row["external_task_profile"], row["status"],
              row["initial_rule"]["require_improving_prefix"], "->", row["final_rule"]["require_improving_prefix"],
              "mean", check.get("mean_observed_gain", {}).get("decimal"),
              "lower", check.get("lower_confidence_bound"), "expense", row["expense"]["decimal"])
    print("total", result["total_priced_expense"])

if __name__ == "__main__":
    main()
