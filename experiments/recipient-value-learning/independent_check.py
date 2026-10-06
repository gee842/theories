#!/usr/bin/env python3
"""Independent raw-record audit; never imports the producer.

The raw reconstruction and estimators were written before the new outcome
aggregation.  The command is deliberately opt-in after the protocol freeze.
Run with the bundled scientific Python and --execute-after-freeze.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import re
from collections import Counter, defaultdict
from datetime import datetime
from fractions import Fraction as F
from pathlib import Path

from scipy.stats import t as student_t


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "sources/32-mental-state-reward-learning-2026-10-06"
EXP = SOURCE / "originals/Experiment_3"
CELLS = ((1, 1), (0, 1), (1, 0), (0, 0))
MISSING = {"", "NA", "NaN", "nan", "None"}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def absent(value):
    return value is None or value.strip() in MISSING


def number(value):
    return None if absent(value) else F(value)


def integer(value):
    result = number(value)
    assert result is not None and result.denominator == 1, value
    return int(result)


def single(rows, field):
    values = {r[field] for r in rows if not absent(r.get(field))}
    assert len(values) == 1, (field, values)
    return values.pop()


def option_kind(filename):
    match = re.fullmatch(r"giftcard_(like|dislike)\d+\.png", Path(filename).name)
    assert match is not None, filename
    return match.group(1)


def source_records():
    """Decode author rules directly, without reading prepared/audit outputs."""
    survey_path = EXP / "data_raw_primary/Qualtrics/post_task_survey_3_anonymized.csv"
    surveys = {}
    flow = Counter()
    for row in read_csv(survey_path):
        flow["survey_rows"] += 1
        if row["Progress"] != "100":
            continue
        end = datetime.strptime(row["EndDate"], "%m/%d/%y %H:%M")
        if end < datetime(2023, 12, 5):
            flow["completed_before_cutoff"] += 1
            continue
        flow["completed_after_cutoff"] += 1
        pid = row["Connect.ID"]
        if not re.fullmatch(r"P\d+", pid):
            flow["completed_no_task_id"] += 1
            continue
        assert pid not in surveys, ("duplicate survey", pid)
        attention = row["attention_check"][:1]
        assert attention.isdigit(), ("attention", pid)
        awareness = row["X2_outcome_relationship"]
        awareness = 1 if awareness.startswith("Yes") else -1 if awareness.startswith("No") else None
        surveys[pid] = {"attention": int(attention), "awareness": awareness}
    assert len(surveys) == 385

    records, seen = [], set()
    files = sorted((EXP / "data_raw_primary/Pavlovia").glob("*.csv"))
    for path in files:
        rows = read_csv(path)
        pid = single(rows, "Connect.ID")
        assert pid not in seen, ("duplicate task", pid)
        seen.add(pid)
        if pid not in surveys:
            continue
        survey = surveys[pid]
        p_code, i_code = single(rows, "experimental_condition"), single(rows, "condition_DM")
        assert p_code in ("A", "B") and i_code in ("C", "D")
        p, i = int(p_code == "A"), int(i_code == "C")
        conditioning = [r for r in rows if not absent(r.get("Congruent"))]
        assert len(conditioning) == 40
        assert sorted(integer(r["pav_trials.thisN"]) for r in conditioning) == list(range(40))
        conditioning_missing = sum(absent(r["acknowledge_resp.rt"]) for r in conditioning)
        offered = [r for r in rows if not absent(r.get("n_trial"))]
        offered.sort(key=lambda r: integer(r["n_trial"]))
        assert len(offered) == 32
        assert [integer(r["n_trial"]) for r in offered] == list(range(32))
        trials = []
        for row in offered:
            left, right = option_kind(row["left_pic"]), option_kind(row["right_pic"])
            assert {left, right} == {"like", "dislike"}
            key = row["DM_choice_component.keys"]
            rt = number(row["DM_choice_component.rt"])
            assert (key in ("e", "i")) == (rt is not None), ("key/RT mismatch", pid, row["n_trial"])
            if rt is None:
                assert absent(key), ("unexpected key", pid, key)
                liked, optimal = None, None
            else:
                assert rt >= 0, ("negative RT", pid)
                liked = int((left if key == "e" else right) == "like")
                optimal = liked if i else 1 - liked
            trials.append({"trial": integer(row["n_trial"]), "rt": rt,
                           "liked": liked, "optimal": optimal})
        answered = sum(t["rt"] is not None for t in trials)
        liked = sum(t["liked"] == 1 for t in trials)
        rt_trials = [t for t in trials if t["rt"] is not None and t["rt"] >= F(1, 5)]
        eligible = conditioning_missing < 8 and 32 - answered < 7 and survey["attention"] < 4
        records.append({
            "source_id": pid, "source_file": path.relative_to(ROOT).as_posix(),
            "source_sha256": sha(path), "P": p, "I": i,
            "condition": p_code, "condition_dm": i_code,
            "conditioning_missing": conditioning_missing,
            "decision_missing": 32 - answered, "attention": survey["attention"],
            "eligible": eligible, "awareness": survey["awareness"],
            "offered": 32, "answered": answered, "liked": liked,
            "optimal": sum(t["optimal"] == 1 for t in trials),
            "rt_qualified_answered": len(rt_trials),
            "rt_qualified_liked": sum(t["liked"] == 1 for t in rt_trials),
            "rt_qualified_optimal": sum(t["optimal"] == 1 for t in rt_trials),
            "trials": trials,
        })
    assert set(surveys) <= seen
    assert len(records) == 385 and sum(r["eligible"] for r in records) == 333
    flow.update({"task_files": len(files), "saved_matched": len(records),
                 "eligible": sum(r["eligible"] for r in records)})
    return records, dict(flow), files + [survey_path]


def clean_reconciliation(records):
    """Check the source-script filename mapping against every clean trial."""
    clean_path = EXP / "data_clean/data_3.csv"
    groups = defaultdict(list)
    for row in read_csv(clean_path):
        groups[integer(row["ID_anonymous"])].append(row)
    eligible = [r for r in records if r["eligible"]]
    assert set(groups) == set(range(1, len(eligible) + 1))
    count = 0
    max_rt_error = 0.0
    for aid, record in enumerate(eligible, 1):
        record["ID_anonymous"] = aid
        clean = sorted(groups[aid], key=lambda r: integer(r["n_trial"]))
        raw = [t for t in record["trials"] if t["rt"] is not None]
        assert len(clean) == len(raw)
        for c, t in zip(clean, raw):
            assert integer(c["n_trial"]) == t["trial"]
            assert integer(c["condition_recode"]) == 2 * record["P"] - 1
            assert integer(c["condition_dm_recode"]) == 2 * record["I"] - 1
            assert integer(c["condition_change_recode"]) == (-1 if record["P"] == record["I"] else 1)
            assert integer(c["optimal"]) == t["optimal"]
            assert number(c["contingency_awareness_1_recode"]) == record["awareness"]
            error = abs(float(number(c["DM_choice_component.rt"]) - t["rt"]))
            max_rt_error = max(max_rt_error, error)
            assert error < 1e-12
            count += 1
    assert count == 10532
    return {"participants": len(eligible), "answered_trials": count,
            "max_rt_absolute_error": max_rt_error,
            "mapping": "Author sorted filename order, validated against all clean assignments/trial IDs/choices/RT/awareness"}


def moments(values):
    n = len(values)
    assert n >= 2
    mean = sum(values, F(0)) / n
    variance = sum((v - mean) ** 2 for v in values) / (n - 1)
    return {"n": n, "mean": float(mean), "mean_exact": str(mean),
            "variance": float(variance), "variance_exact": str(variance),
            "sd": math.sqrt(float(variance))}


def contrast(values, weights):
    means, parts, dfs = [], [], []
    for cell, weight in zip(CELLS, weights):
        if weight == 0:
            continue
        m = moments(values[cell])
        means.append(weight * F(m["mean_exact"]))
        v = weight ** 2 * F(m["variance_exact"]) / m["n"]
        parts.append(v)
        dfs.append(v * v / (m["n"] - 1))
    estimate = sum(means, F(0))
    variance = sum(parts, F(0))
    if variance == 0:
        se, df, critical = 0.0, None, None
        lower = upper = float(estimate)
    else:
        se = math.sqrt(float(variance))
        df = float(variance ** 2 / sum(dfs, F(0)))
        critical = float(student_t.ppf(0.975, df))
        lower, upper = float(estimate) - critical * se, float(estimate) + critical * se
    return {"estimate": float(estimate), "estimate_exact": str(estimate),
            "se": se, "df": df, "t_critical": critical, "ci95": [lower, upper]}


def analysis(records, mode):
    sample = records if mode == "all_saved_offered" else [r for r in records if r["eligible"]]
    skipped = sum(r["answered"] == 0 for r in sample) if mode == "eligible_answered" else 0
    if mode == "eligible_answered":
        sample = [r for r in sample if r["answered"]]
    l, response, optimal = (defaultdict(list) for _ in range(3))
    groups = defaultdict(list)
    for r in sample:
        cell = r["P"], r["I"]
        groups[cell].append(r)
        if mode == "eligible_rt_offered":
            a, liked, opt, denominator = r["rt_qualified_answered"], r["rt_qualified_liked"], r["rt_qualified_optimal"], 32
        else:
            a, liked, opt = r["answered"], r["liked"], r["optimal"]
            denominator = a if mode == "eligible_answered" else 32
        l[cell].append(F(liked, denominator))
        response[cell].append(F(a, denominator))
        optimal[cell].append(F(opt, denominator))
        assert F(opt, denominator) == (F(liked, denominator) if r["I"] else F(a - liked, denominator))
    out = {"participants": len(sample), "zero_answer_exclusions": skipped, "cells": {}}
    for cell in CELLS:
        key = f"P{cell[0]}_I{cell[1]}"
        out["cells"][key] = {
            **moments(l[cell]), "response": moments(response[cell]), "optimal": moments(optimal[cell]),
            "offered_trials": 32 * len(groups[cell]),
            "total_liked": sum(r["rt_qualified_liked"] if mode == "eligible_rt_offered" else r["liked"] for r in groups[cell]),
            "total_answered": sum(r["rt_qualified_answered"] if mode == "eligible_rt_offered" else r["answered"] for r in groups[cell]),
            "source_ids": [r["source_id"] for r in groups[cell]],
        }
    half = F(1, 2)
    out["standardized_training_effect"] = contrast(l, (half, -half, half, -half))
    out["effect_within_I1"] = contrast(l, (F(1), F(-1), F(0), F(0)))
    out["effect_within_I0"] = contrast(l, (F(0), F(0), F(1), F(-1)))
    out["response_effect_I0"] = contrast(response, (F(0), F(0), F(1), F(-1)))
    out["optimal_no_reversal_minus_reversal"] = contrast(optimal, (half, -half, -half, half))
    expected = F(out["standardized_training_effect"]["estimate_exact"]) - half * F(out["response_effect_I0"]["estimate_exact"])
    assert expected == F(out["optimal_no_reversal_minus_reversal"]["estimate_exact"])
    out["optimal_response_adjustment_identity_exact"] = True
    return out


def reconstruct():
    records, flow, input_files = source_records()
    clean_check = clean_reconciliation(records)
    analyses = {name: analysis(records, name) for name in (
        "eligible_offered", "all_saved_offered", "eligible_answered", "eligible_rt_offered")}
    awareness = {}
    exclusion = {}
    for p, i in CELLS:
        key = f"P{p}_I{i}"
        group = [r for r in records if (r["P"], r["I"]) == (p, i)]
        eligible = [r for r in group if r["eligible"]]
        awareness[key] = {str(a): sum(r["awareness"] == a for r in eligible) for a in (1, -1, None)}
        exclusion[key] = {"saved": len(group), "eligible": len(eligible),
                          "conditioning_rule_pass": sum(r["conditioning_missing"] < 8 for r in group),
                          "decision_rule_pass": sum(r["decision_missing"] < 7 for r in group),
                          "attention_rule_pass": sum(r["attention"] < 4 for r in group)}
    participants = [{k: v for k, v in r.items() if k != "trials"} for r in records]
    input_files += [EXP / "data_clean/data_3.csv", EXP / "code/cleaning_3.R",
                    EXP / "code/analysis_3.R", HERE / "PROTOCOL.md", SOURCE / "manifest.json"]
    return {"scope": "Independent raw CSV reconstruction and participant-level risk-difference analysis; no producer import or GLMM",
            "flow": flow, "clean_reconciliation": clean_check,
            "analyses": analyses, "awareness_eligible": awareness, "exclusion_by_cell": exclusion,
            "participants": participants,
            "inputs": {p.relative_to(ROOT).as_posix(): sha(p) for p in input_files},
            "independent_checker_sha256": sha(__file__), "python": platform.python_version()}


def compare_producer():
    """Added after independent-results.json was saved; imports no producer."""
    before_hash = sha(HERE / "independent-results.json")
    independent = json.loads((HERE / "independent-results.json").read_text())
    current = reconstruct()
    for key in current:
        if key != "independent_checker_sha256":
            assert current[key] == independent[key], ("independent replay changed", key)
    records, _, _ = source_records()
    clean_reconciliation(records)
    prepared = json.loads((HERE / "participants.json").read_text())
    trial_rows = read_csv(HERE / "prepared-trials.csv")
    published = json.loads((HERE / "results.json").read_text())
    producer_receipt = json.loads((HERE / "verification.json").read_text())
    counts = Counter()
    max_error = 0.0

    def eq(a, b, category, label):
        nonlocal max_error
        counts[category] += 1
        if isinstance(a, (float, F)) or isinstance(b, (float, F)):
            if a is None or b is None:
                assert a is b, label
            else:
                error = abs(float(a) - float(b))
                max_error = max(max_error, error)
                assert error <= 1e-12, (label, a, b, error)
        else:
            assert a == b, (label, a, b)

    # Bind each prepared record by its actual source file, independently of its
    # convenient output ID; then validate all per-participant sufficient counts.
    by_source = {r["source_file"]: r for r in records}
    by_record_id = {}
    fields = {"author_id": "ID_anonymous", "training": "P", "current": "I",
              "eligible": "eligible", "conditioning_misses": "conditioning_missing",
              "decision_misses": "decision_missing", "attention_code": "attention",
              "offered": "offered", "liked": "liked", "responded": "answered",
              "optimal": "optimal", "rt_qualified_liked": "rt_qualified_liked",
              "rt_qualified_responded": "rt_qualified_answered",
              "rt_qualified_optimal": "rt_qualified_optimal", "source_sha256": "source_sha256"}
    assert len(prepared) == len(records) == 385
    assert len({p["record_id"] for p in prepared}) == 385
    assert len({p["source_file"] for p in prepared}) == 385
    for p in prepared:
        source_path = (SOURCE / p["source_file"]).relative_to(ROOT).as_posix()
        raw = by_source[source_path]
        by_record_id[p["record_id"]] = raw
        for out_key, raw_key in fields.items():
            eq(p[out_key], raw.get(raw_key), "participant_fields", (p["record_id"], out_key))
        eq(p["awareness"], {1: "yes", -1: "no", None: "missing"}[raw["awareness"]],
           "participant_fields", (p["record_id"], "awareness"))

    # Re-read each offered trial, including missing responses.  Original raw RT
    # decimal parsing uses Fraction; tolerance allows only output float rounding.
    assert len(trial_rows) == 385 * 32
    seen = set()
    for trial in trial_rows:
        rid, n = trial["record_id"], integer(trial["trial"])
        assert (rid, n) not in seen
        seen.add((rid, n))
        r = by_record_id[rid]
        t = r["trials"][n]
        expect = {
            "author_id": str(r.get("ID_anonymous", "")), "training": str(r["P"]),
            "current": str(r["I"]), "responded": str(t["rt"] is not None),
            "liked": "" if t["liked"] is None else str(t["liked"]),
            "optimal": "" if t["optimal"] is None else str(t["optimal"]),
            "rt_qualified": str(t["rt"] is not None and t["rt"] >= F(1, 5)),
        }
        for key, val in expect.items():
            actual = trial[key]
            if key in ("liked", "optimal"):
                actual = {"True": "1", "False": "0"}.get(actual, actual)
            eq(actual, val, "offered_trial_fields", (rid, n, key))
        eq(number(trial["rt"]), t["rt"], "offered_trial_fields", (rid, n, "rt"))

    def check_contrast(observed, expected, label):
        for key in ("estimate", "se", "df"):
            eq(observed[key], expected[key], "aggregate_fields", (label, key))
        for k in (0, 1):
            eq(observed["ci95"][k], expected["ci95"][k], "aggregate_fields", (label, "ci95", k))
        eq(observed["degenerate_zero_variance"], expected["se"] == 0,
           "aggregate_fields", (label, "zero variance"))

    outputs = {"eligible_offered": published["primary"],
               "all_saved_offered": published["sensitivities"]["all_saved"],
               "eligible_answered": published["sensitivities"]["answered"],
               "eligible_rt_offered": published["sensitivities"]["rt_qualified"]}
    for name, observed in outputs.items():
        expected = independent["analyses"][name]
        eq(observed["participants"], expected["participants"], "aggregate_fields", name)
        eq(len(observed["zero_answer_exclusions"]), expected["zero_answer_exclusions"], "aggregate_fields", name)
        assert [(c["training"], c["current"]) for c in observed["cells"]] == list(CELLS)
        for cell in observed["cells"]:
            key = f'P{cell["training"]}_I{cell["current"]}'
            own = expected["cells"][key]
            for lhs, rhs in {"participants": "n", "mean_liked_fraction": "mean",
                             "sd_liked_fraction": "sd", "offered_trials": "offered_trials",
                             "numerator_liked_responses": "total_liked",
                             "qualifying_responses": "total_answered"}.items():
                eq(cell[lhs], own[rhs], "aggregate_fields", (name, key, lhs))
            eq(cell["mean_response_fraction"], own["response"]["mean"], "aggregate_fields", (name, key, "response"))
            eq(cell["mean_offered_response_fraction"], F(own["total_answered"], own["offered_trials"]),
               "aggregate_fields", (name, key, "offered response"))
        check_contrast(observed["standardized_training_contrast"], expected["standardized_training_effect"], (name, "training"))
        eq(observed["components"]["current_congruent"], expected["effect_within_I1"]["estimate"], "aggregate_fields", (name, "I1"))
        eq(observed["components"]["current_incongruent"], expected["effect_within_I0"]["estimate"], "aggregate_fields", (name, "I0"))
        coding = observed["coding_reconciliation"]
        eq(coding["current_incongruent_response_contrast"], expected["response_effect_I0"]["estimate"], "aggregate_fields", (name, "response contrast"))
        eq(coding["response_adjusted_identity_error"], 0.0, "aggregate_fields", (name, "identity"))
        check_contrast(coding["optimal_no_reversal_minus_reversal"], expected["optimal_no_reversal_minus_reversal"], (name, "optimal"))

    for row in published["awareness_descriptive_only"]:
        key = f'P{row["training"]}_I{row["current"]}'
        own = independent["awareness_eligible"][key]
        for pub_key, own_key in (("yes", "1"), ("no", "-1"), ("missing", "None")):
            eq(row[pub_key], own[own_key], "awareness_fields", (key, pub_key))
        eq(row["participants"], sum(own.values()), "awareness_fields", (key, "n"))
    assert all(published[k] is False for k in (
        "full_randomized_ITT_identified", "glmm_reproduced", "mechanistic_mediation_identified"))

    freeze = json.loads((HERE / "protocol-freeze.json").read_text())
    assert freeze["approved_for_execution"] is True
    interpretation_path = "_process/research/2026-10-05-concern-theory/reward-association/IDENTIFICATION.md"
    preserved_interpretation = "_process/research/2026-10-05-concern-theory/reward-association/development/IDENTIFICATION-before-reporting-clarification.md"
    for path, expected_hash in freeze["inputs_sha256"].items():
        # Interpretation was narrowly clarified after results, not represented
        # as part of the pre-output text. Verify the preserved original against
        # the freeze and bind the reviewed current text separately below.
        frozen_path = preserved_interpretation if path == interpretation_path else path
        eq(sha(ROOT / frozen_path), expected_hash, "hash_checks", frozen_path)
    for path, expected_hash in producer_receipt["source_hashes"].items():
        eq(sha(SOURCE / path), expected_hash, "hash_checks", path)
    for path, expected_hash in producer_receipt["outputs"].items():
        eq(sha(HERE / path), expected_hash, "hash_checks", path)
    eq(sha(HERE / "analysis.py"), producer_receipt["analysis_sha256"], "hash_checks", "producer source")
    eq(sha(HERE / "protocol-freeze.json"), producer_receipt["protocol_freeze_sha256"], "hash_checks", "freeze")
    eq(sha(HERE / "independent-results.json"), before_hash, "hash_checks", "independent result unchanged")
    eq(sha(HERE / "development/independent-before-comparison.py"), independent["independent_checker_sha256"],
       "hash_checks", "precomparison estimator")
    bound = ["independent_check.py", "independent-results.json", "analysis.py", "results.json", "participants.json",
             "prepared-trials.csv", "verification.json", "PROTOCOL.md", "protocol-freeze.json",
             "development/independent-before-comparison.py", "independent-execution-log.json"]
    import scipy
    receipt = {"status": "passed", "scope": "Independent raw reconstruction and comparison; no producer imports, GLMM, mediation or full randomized ITT claim",
               "independence": "Estimator and original independent results saved before reading producer outputs; comparison adapter added afterward",
               "participants": 385, "eligible": 333, "offered_trials": len(trial_rows),
               "clean_answered_trials": independent["clean_reconciliation"]["answered_trials"],
               "counts": dict(counts), "maximum_absolute_numeric_discrepancy": max_error,
               "tolerance": 1e-12, "four_fixed_analyses": list(outputs),
               "descriptive_publication_discrepancy": {
                   "paper_location": "Preserved primary paper, page 16, awareness paragraph",
                   "reported_unaware": 187, "reported_percent": 56.1,
                   "raw_and_clean_eligible_unaware": sum(r["eligible"] and r["awareness"] == -1 for r in records),
                   "raw_and_clean_eligible_aware": sum(r["eligible"] and r["awareness"] == 1 for r in records),
                   "eligible_with_zero_rt_qualified_answers": sum(r["eligible"] and r["rt_qualified_answered"] == 0 for r in records),
                   "status": "Unresolved one-person reporting discrepancy; no recoding, exclusions, awareness-selected outcomes or primary changes"},
               "python": platform.python_version(), "scipy": scipy.__version__,
               "post_output_interpretation_clarification": {
                   "scope": "Task-history equivalence requires a shared reporting law to extend to post-task questionnaires; no source, code estimand or result change",
                   "frozen_original": preserved_interpretation,
                   "frozen_original_sha256": sha(ROOT / preserved_interpretation),
                   "current_interpretation": interpretation_path,
                   "current_interpretation_sha256": sha(ROOT / interpretation_path)},
               "input_hashes": {p: sha(HERE / p) for p in bound}}
    (HERE / "independent-check.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: v for k, v in receipt.items() if k != "input_hashes"}, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute-after-freeze", action="store_true")
    parser.add_argument("--compare-producer", action="store_true")
    args = parser.parse_args()
    assert args.execute_after_freeze, "Explicit post-freeze execution flag required"
    assert (HERE / "protocol-freeze.json").is_file(), "Protocol freeze not present"
    if args.compare_producer:
        compare_producer()
        return
    output = reconstruct()
    result_path = HERE / "independent-results.json"
    if result_path.exists():
        saved = json.loads(result_path.read_text())
        for key in output:
            if key != "independent_checker_sha256":
                assert output[key] == saved[key], ("independent replay changed", key)
        status = "independent reconstruction reproduced; original pre-comparison result preserved"
    else:
        result_path.write_text(json.dumps(output, indent=2) + "\n")
        status = "independent reconstruction complete; producer comparison pending"
    print(json.dumps({"status": status,
                      "flow": output["flow"], "clean_reconciliation": output["clean_reconciliation"]}, indent=2))


if __name__ == "__main__":
    main()
