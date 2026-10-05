"""Outcome-based revision of an admission rule within a supplied rule grammar.

No learning function receives a world label, hidden truth table, or true risk.
Environment generation is confined to draw_task()/observe(). Rule edits are
syntactic; discovery and independent outer checking use observed paid losses.
"""
from dataclasses import dataclass, asdict, replace
from fractions import Fraction as F
from itertools import combinations, product
from math import log, sqrt
from pathlib import Path
import hashlib
import json
import random

ROWS = tuple(product((0, 1), repeat=3))
SINGLES = tuple(combinations(range(3), 1))
PAIRS = tuple(combinations(range(3), 2))

@dataclass(frozen=True)
class Rule:
    require_improving_prefix: bool = True
    require_final_training_improvement: bool = True
    require_fresh_local_validation: bool = True

@dataclass(frozen=True)
class Config:
    horizon: int = 64
    penalty: F = F(1, 32)
    fit_cost: F = F(1, 4)
    label_cost: F = F(1)
    field_cost: F = F(1, 50)
    discovery_pairs: int = 32
    checking_pairs: int = 256
    alpha: float = .05

@dataclass(frozen=True)
class Task:
    # Hidden environment state. Never passed to generate(), edit_rule(),
    # choose_from_discovery(), or check_reports().
    truth: tuple
    noise: F

@dataclass(frozen=True)
class Candidate:
    fields: tuple
    predictions: tuple
    training_score: F

@dataclass(frozen=True)
class Report:
    expense: F
    prediction_errors: int
    proposed: bool
    adopted: bool
    fields: tuple
    @property
    def observed_loss(self):
        return self.expense + self.prediction_errors

def edit_rule(rule):
    # Generic bounded AST edit: delete the optional prefix-evidence requirement.
    # Final empirical improvement and fresh validation are preserved.
    return [replace(rule, require_improving_prefix=False)] if rule.require_improving_prefix else []

def fit(fields, labels, cfg):
    table = {}
    for key in product((0, 1), repeat=len(fields)):
        ys = [y for row, y in zip(ROWS, labels)
              if tuple(row[j] for j in fields) == key]
        table[key] = int(2 * sum(ys) > len(ys))
    pred = tuple(table[tuple(row[j] for j in fields)] for row in ROWS)
    err = F(sum(y != p for y, p in zip(labels, pred)), len(ROWS))
    return Candidate(fields, pred, err + cfg.penalty * (2 ** len(fields) - 1))

def ranking(candidate):
    return candidate.training_score, candidate.fields, candidate.predictions

def generate(rule, labels, cfg):
    # This entire function observes only records and the installed rule.
    coarse = fit((), labels, cfg)
    singles = [fit(fs, labels, cfg) for fs in SINGLES]
    single = min(singles, key=ranking)
    expense = 8 * cfg.label_cost + 3 * cfg.fit_cost
    if rule.require_improving_prefix:
        if single.training_score >= coarse.training_score:
            return coarse, None, expense
        pairs = [fs for fs in PAIRS if single.fields[0] in fs]
    else:
        pairs = PAIRS
    fitted = [fit(fs, labels, cfg) for fs in pairs]
    expense += len(pairs) * cfg.fit_cost
    best = min([coarse] + singles + fitted, key=ranking)
    if rule.require_final_training_improvement and best.training_score >= coarse.training_score:
        return coarse, None, expense
    return coarse, best, expense

def draw_task(profile, rng):
    complement = rng.randrange(2)
    if profile in ("interaction", "noisy_interaction", "mixed"):
        if profile == "mixed" and rng.randrange(2):
            return Task((0,) * 8, F(1, 2))
        pair = rng.choice(PAIRS)
        truth = tuple(row[pair[0]] ^ row[pair[1]] ^ complement for row in ROWS)
        return Task(truth, F(1, 4) if profile == "noisy_interaction" else F(0))
    if profile == "single":
        field = rng.randrange(3)
        return Task(tuple(row[field] ^ complement for row in ROWS), F(0))
    if profile == "constant":
        return Task((complement,) * 8, F(0))
    if profile == "null":
        return Task((0,) * 8, F(1, 2))
    raise ValueError(profile)

def observe(task, row_indices, rng):
    return tuple(task.truth[i] ^ int(rng.randrange(task.noise.denominator) < task.noise.numerator)
                 for i in row_indices)

def run_policy(rule, task, cfg, rng):
    labels = observe(task, range(8), rng)
    coarse, candidate, expense = generate(rule, labels, cfg)
    installed, adopted = coarse, False
    if candidate is not None:
        if rule.require_fresh_local_validation:
            ys = observe(task, range(8), rng)
            expense += 8 * cfg.label_cost
            adopted = sum(y == p for y, p in zip(ys, candidate.predictions)) >= 7
        else:
            adopted = True
        if adopted:
            installed = candidate
    # Routine deployment reveals outcomes after forecasts, at no added label
    # acquisition charge. Contexts are balanced; each noisy outcome is fresh.
    ix = tuple(i % 8 for i in range(cfg.horizon))
    ys = observe(task, ix, rng)
    errors = sum(y != installed.predictions[i] for i, y in zip(ix, ys))
    expense += cfg.horizon * len(installed.fields) * cfg.field_cost
    return Report(expense, errors, candidate is not None, adopted, installed.fields)

def choose_from_discovery(paired_reports):
    # No hidden task property is read. One generated edit is screened by loss.
    gain = sum(a.observed_loss - b.observed_loss for a, b in paired_reports)
    return gain > 0

def loss_difference_bound(cfg):
    minimum_expense = 8 * cfg.label_cost + 3 * cfg.fit_cost
    maximum_expense = 16 * cfg.label_cost + 6 * cfg.fit_cost + 2 * cfg.horizon * cfg.field_cost
    # Every paired difference lies in [-B,B], hence range width 2B.
    return F(cfg.horizon) + maximum_expense - minimum_expense

def check_reports(paired_reports, cfg):
    n = len(paired_reports)
    differences = [a.observed_loss - b.observed_loss for a, b in paired_reports]
    bound = loss_difference_bound(cfg)
    assert all(-bound <= d <= bound for d in differences)
    mean = sum(differences) / n
    radius = float(2 * bound) * sqrt(log(1 / cfg.alpha) / (2 * n))
    return {"pairs": n, "mean_observed_gain": pack(mean),
            "bound_absolute_difference": pack(bound),
            "one_sided_Hoeffding_radius": radius,
            "lower_confidence_bound": float(mean) - radius,
            "pass": float(mean) - radius > 0}

def pack(value):
    return {"exact": str(value), "decimal": float(value)}

def summarize(pairs):
    result = {}
    for index, key in ((0, "incumbent"), (1, "edited")):
        rs = [p[index] for p in pairs]
        result[key] = {"count": len(rs),
            "expense": pack(sum(r.expense for r in rs)),
            "errors": sum(r.prediction_errors for r in rs),
            "proposals": sum(r.proposed for r in rs),
            "adoptions": sum(r.adopted for r in rs),
            "observed_loss": pack(sum(r.observed_loss for r in rs))}
    return result

def run_study(profile, opening, budget, seed, cfg=Config()):
    incumbent = Rule()
    alternatives = edit_rule(incumbent)
    edited = alternatives[0]
    # Separate RNGs make the freshness boundary operational and auditable.
    pilot_rng = random.Random(seed + 11)
    discovery_rng = random.Random(seed + 101)
    checking_rng = random.Random(seed + 1009)
    spent = F(0)
    events = []
    answer = {"profile": profile, "opening": opening, "seed": seed,
              "starting_budget": pack(budget), "initial_rule": asdict(incumbent),
              "syntactically_generated_edit": asdict(edited)}
    if opening == "incumbent_gate":
        pilot_price = 8 * cfg.label_cost + 3 * cfg.fit_cost
        if budget < pilot_price:
            answer.update(status="pilot_unfunded", final_rule=asdict(incumbent), spent=pack(spent))
            return answer
        spent += pilot_price
        pilot = draw_task(profile, pilot_rng)
        ys = observe(pilot, range(8), pilot_rng)
        constant = fit((), ys, cfg)
        best_single = min([fit(fs, ys, cfg) for fs in SINGLES], key=ranking)
        if best_single.training_score >= constant.training_score:
            answer.update(status="probe_blocked_by_incumbent", final_rule=asdict(incumbent), spent=pack(spent))
            return answer
        events.append("Incumbent singleton gate permitted a meta-probe.")
    elif opening != "protected_probe":
        raise ValueError(opening)
    # Reserve every possible monetary payment before starting. Outcome loss is
    # the selection criterion, not a cash balance; it is reported separately.
    max_expense = 16 * cfg.label_cost + 6 * cfg.fit_cost + 2 * cfg.horizon * cfg.field_cost
    reserve = 2 * (cfg.discovery_pairs + cfg.checking_pairs) * max_expense
    answer["required_worst_case_reserve"] = pack(reserve)
    if budget - spent < reserve:
        answer.update(status="probe_unfunded", final_rule=asdict(incumbent), spent=pack(spent), events=events)
        return answer
    def collect(n, rng):
        nonlocal spent
        collected = []
        for _ in range(n):
            task = draw_task(profile, rng)
            # Two actual independent outcome streams, shared task type. Their
            # expenses are both paid, rather than silently reusing free data.
            pair = (run_policy(incumbent, task, cfg, rng), run_policy(edited, task, cfg, rng))
            spent += sum(r.expense for r in pair)
            assert spent <= budget
            collected.append(pair)
        return collected
    discovery = collect(cfg.discovery_pairs, discovery_rng)
    answer["discovery"] = summarize(discovery)
    if not choose_from_discovery(discovery):
        answer.update(status="edit_failed_discovery", final_rule=asdict(incumbent), spent=pack(spent), events=events)
        return answer
    checking = collect(cfg.checking_pairs, checking_rng)
    answer["checking"] = summarize(checking)
    answer["fresh_outer_check"] = check_reports(checking, cfg)
    if answer["fresh_outer_check"]["pass"]:
        incumbent = edited
        status = "rule_revised"
        events.append("Deleted prefix-gain requirement after separate fresh outer check.")
    else:
        status = "edit_failed_fresh_check"
    answer.update(status=status, final_rule=asdict(incumbent), spent=pack(spent), events=events)
    all_pairs = discovery + checking
    total_observed_loss = sum(a.observed_loss + b.observed_loss for a, b in all_pairs)
    matched_incumbent_estimate = 2 * sum(a.observed_loss for a, _ in all_pairs)
    answer["study_service_accounting"] = {
        "prediction_blocks_delivered": 2 * len(all_pairs),
        "total_observed_loss_including_priced_expense": pack(total_observed_loss),
        "matched_two_incumbent_streams_loss_estimate": pack(matched_incumbent_estimate),
        "incremental_observed_loss_estimate": pack(total_observed_loss - matched_incumbent_estimate),
        "interpretation": "One observed incumbent stream supplies the counterfactual mean for two matched service streams. Exact in noiseless interaction; otherwise an estimate using selected data, not an independent confidence statement. Cash expense is already included in observed loss.",
    }
    return answer

def run_transfer(final_rule_dict, cfg, count=512, seed=20271109):
    """Actually execute the learned rule on fresh prospective tasks, including shifts."""
    installed = Rule(**final_rule_dict)
    output = []
    for number, profile in enumerate(("interaction", "single", "constant", "null", "noisy_interaction")):
        rng = random.Random(seed + 10000 * number)
        pairs = []
        for _ in range(count):
            task = draw_task(profile, rng)
            pairs.append((run_policy(Rule(), task, cfg, rng), run_policy(installed, task, cfg, rng)))
        row = {"future_profile": profile, "pairs": count, "executed_rule": asdict(installed),
               "reports": summarize(pairs),
               "mean_observed_gain_vs_incumbent": pack(sum(a.observed_loss - b.observed_loss for a, b in pairs) / count)}
        output.append(row)
    return {"seed": seed, "rule_frozen_after_study": True, "records": output,
            "limitation": "The learner does not re-open its standard after shift in this implementation; these are prospective transfer executions, not a drift-detection guarantee."}

def exact_controls(cfg):
    # Exhaust all three interacting pairs and both outcome complements.
    # The learner receives records only; truth used here solely by the audit.
    for pair in PAIRS:
        for flip in (0, 1):
            ys = tuple(row[pair[0]] ^ row[pair[1]] ^ flip for row in ROWS)
            old, c0, e0 = generate(Rule(), ys, cfg)
            _, c1, e1 = generate(edit_rule(Rule())[0], ys, cfg)
            assert c0 is None and c1.fields == pair and c1.predictions == ys
            assert e0 == F(35, 4) and e1 == F(19, 2)
    # Independent fair labels: frozen local rule passes with 9/256 exactly.
    frozen = (0, 1, 0, 1, 1, 0, 1, 0)
    passes = sum(sum(y == p for y, p in zip(ys, frozen)) >= 7 for ys in product((0, 1), repeat=8))
    assert passes == 9
    return {"all_6_interaction_orientations_checked": True,
            "conditional_local_false_adoption": "9/256",
            "deterministic_interaction_gain_per_episode": pack(F(cfg.horizon, 2) - 2 * cfg.horizon * cfg.field_cost - F(35, 4)),
            "fresh_outer_check_guarantee": "Under declared IID task distribution, fixed config, independent fresh checking, probability of accepting a nonpositive-mean-gain edit is at most alpha; one edit/one check only."}

def main():
    cfg = Config()
    jobs = [("interaction", "protected_probe", F(12000), 20261005, cfg),
            ("interaction", "incumbent_gate", F(12000), 20261005, cfg),
            ("interaction", "protected_probe", F(100), 20261005, cfg),
            ("single", "protected_probe", F(12000), 20261005, cfg),
            ("constant", "protected_probe", F(12000), 20261005, cfg),
            ("null", "protected_probe", F(12000), 20261005, cfg),
            ("noisy_interaction", "protected_probe", F(12000), 20261005, cfg),
            ("mixed", "protected_probe", F(12000), 20261005, cfg),
            ("interaction", "protected_probe", F(40000), 20261005,
             replace(cfg, field_cost=F(3, 10))),
            # Follow-up sample-size design chosen after the first study.
            # Fresh seed/streams; do not extend the failed checking prefix.
            ("mixed", "protected_probe", F(45000), 912867,
             replace(cfg, checking_pairs=1024))]
    records = [run_study(*job) for job in jobs]
    assert records[0]["status"] == "rule_revised"
    assert records[1]["status"] == "probe_blocked_by_incumbent"
    assert records[2]["status"] == "probe_unfunded"
    assert records[3]["status"] == records[4]["status"] == "edit_failed_discovery"
    assert records[-2]["status"] == "edit_failed_discovery"
    configs = {"default": {k: str(v) if isinstance(v, F) else v for k, v in asdict(cfg).items()},
               "high_field_cost": "3/10"}
    source = Path(__file__)
    result = {"configurations": configs, "exact_controls": exact_controls(cfg),
              "records": records, "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
    source.with_name("standard-revision-results.json").write_text(json.dumps(result, indent=2) + "\n")
    transfer = run_transfer(records[0]["final_rule"], cfg)
    source.with_name("standard-transfer-results.json").write_text(json.dumps(transfer, indent=2) + "\n")
    for row in records:
        chk = row.get("fresh_outer_check", {})
        print(row["profile"], row["opening"], row["starting_budget"]["exact"],
              row["status"], "spent", row["spent"]["decimal"],
              "check_mean", chk.get("mean_observed_gain", {}).get("decimal"),
              "lower", chk.get("lower_confidence_bound"))
    for row in transfer["records"]:
        print("transfer", row["future_profile"], row["mean_observed_gain_vs_incumbent"]["decimal"])

if __name__ == "__main__":
    main()
