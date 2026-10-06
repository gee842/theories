#!/usr/bin/env python3
"""Prespecified Experiment 3 participant-level analysis. Originals are read-only.

Do not run before prospective review and protocol-freeze.json approval. Merely
importing this module does not load data or compute results.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.stats import t as student_t


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SOURCE = REPO / "sources/32-mental-state-reward-learning-2026-10-06"
EXPERIMENT = SOURCE / "originals/Experiment_3"
CELL_ORDER = ((1, 1), (0, 1), (1, 0), (0, 0))
WEIGHTS = (0.5, -0.5, 0.5, -0.5)
MISSING = {"", "NA", "NaN", "nan", "None"}
CUTOFF = datetime(2023, 12, 5)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def missing(value: str | None) -> bool:
    return value is None or value.strip() in MISSING


def number(value: str | None) -> float | None:
    if missing(value):
        return None
    answer = float(value)
    require(math.isfinite(answer), "Nonfinite source number")
    return answer


def integer(value: str) -> int:
    answer = number(value)
    require(answer is not None and answer == int(answer), "Noninteger source field")
    return int(answer)


def verify_sources() -> dict[str, str]:
    manifest_path = SOURCE / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    hashes = {"manifest.json": sha256(manifest_path)}
    for entry in manifest["selected_archive_members"] + [manifest["paper"]]:
        path = SOURCE / entry["path"]
        actual = sha256(path)
        require(actual == entry["sha256"], f"Changed original: {entry['path']}")
        require(path.stat().st_size == entry["bytes"], "Original size mismatch")
        hashes[entry["path"]] = actual
    return hashes


def survey_records() -> tuple[dict[str, dict], dict]:
    rows = read_csv(EXPERIMENT / "data_raw_primary/Qualtrics/post_task_survey_3_anonymized.csv")
    records = {}
    counts = Counter()
    for row in rows:
        if row["Progress"] != "100":
            continue
        date = datetime.strptime(row["EndDate"], "%m/%d/%y %H:%M")
        if date < CUTOFF:
            counts["completed_before_cutoff"] += 1
            continue
        counts["completed_after_cutoff"] += 1
        pid = row["Connect.ID"].strip()
        if not pid.startswith("P"):
            counts["postcutoff_without_usable_id"] += 1
            continue
        require(pid not in records, "Duplicate completed survey ID")
        attention = row["attention_check"].strip()
        require(attention and attention[0].isdigit(), "Missing attention coding")
        awareness = row["X2_outcome_relationship"].strip()
        awareness = "yes" if awareness.startswith("Yes") else (
            "no" if awareness.startswith("No") else "missing")
        records[pid] = {"attention": int(attention[0]), "awareness": awareness}
    counts["matched_survey_ids"] = len(records)
    require(counts["completed_after_cutoff"] == 390, "Survey cohort mismatch")
    require(counts["postcutoff_without_usable_id"] == 5, "Missing-ID count mismatch")
    require(len(records) == 385, "Saved survey cohort mismatch")
    return records, dict(counts)


def option_kind(path: str) -> str:
    # Exact source R substr(..., 10, 12), using Python's zero-based slice.
    kind = path[9:12]
    require(kind in ("lik", "dis"), f"Unrecognized option coding: {path!r}")
    return kind


def reconstruct() -> tuple[list[dict], list[dict], dict, dict]:
    """Reconstruct raw rows; source validation precedes group outcome summaries."""
    surveys, cohort = survey_records()
    task_files = sorted((EXPERIMENT / "data_raw_primary/Pavlovia").glob("*.csv"))
    require(len(task_files) == 387, "Unexpected saved task-file count")
    participants, trials, eligibility_rows = [], [], []
    seen = set()
    author_id = 0
    for source_index, path in enumerate(task_files, start=1):
        rows = read_csv(path)
        require(bool(rows), "Empty task source")
        pid = rows[0]["Connect.ID"].strip()
        require(pid and pid not in seen, "Missing or duplicate task participant")
        seen.add(pid)
        assignments = {(r["experimental_condition"], r["condition_DM"])
                       for r in rows if not missing(r.get("experimental_condition"))}
        require(len(assignments) == 1, "Inconsistent assigned condition")
        train_code, current_code = next(iter(assignments))
        require(train_code in ("A", "B") and current_code in ("C", "D"),
                "Invalid assignment codes")
        p, i = int(train_code == "A"), int(current_code == "C")
        conditioning = [r for r in rows if not missing(r.get("Congruent"))]
        offered = [r for r in rows if not missing(r.get("n_trial"))]
        require(len(conditioning) == 40 and len(offered) == 32, "Incomplete trial records")
        labels = [integer(r["n_trial"]) for r in offered]
        require(len(set(labels)) == 32 and sorted(labels) == list(range(min(labels), min(labels) + 32)),
                "Duplicate or nonconsecutive decision trial IDs")
        pmiss = sum(missing(r.get("acknowledge_resp.rt")) for r in conditioning)
        dmiss = sum(missing(r.get("DM_choice_component.rt")) for r in offered)
        survey = surveys.get(pid)
        eligible = bool(survey and pmiss < 8 and dmiss < 7 and survey["attention"] < 4)
        eligibility_rows.append({"source_id": pid, "post_date_complete": survey is not None,
                                 "missing_conditioning_responses": pmiss,
                                 "missing_decision_responses": dmiss,
                                 "author_eligible": eligible})
        if survey is None:
            continue
        if eligible:
            author_id += 1
        record_id = f"rv{source_index:03d}"
        person = {"record_id": record_id, "author_id": author_id if eligible else None,
                  "source_file": path.relative_to(SOURCE).as_posix(),
                  "source_sha256": sha256(path), "training": p, "current": i,
                  "eligible": eligible, "conditioning_misses": pmiss,
                  "decision_misses": dmiss, "attention_code": survey["attention"],
                  "awareness": survey["awareness"], "offered": 32,
                  "liked": 0, "responded": 0, "optimal": 0,
                  "rt_qualified_liked": 0, "rt_qualified_responded": 0,
                  "rt_qualified_optimal": 0}
        for raw in offered:
            left, right = option_kind(raw["left_pic"]), option_kind(raw["right_pic"])
            require({left, right} == {"lik", "dis"}, "Offered pair is not liked/disliked")
            key, rt = raw["DM_choice_component.keys"].strip(), number(raw["DM_choice_component.rt"])
            responded = not missing(key)
            require(responded == (rt is not None), "Key and response-time missingness disagree")
            require(not responded or key in ("e", "i"), "Unexpected choice key")
            require(rt is None or rt >= 0, "Negative response time")
            chosen = (left if key == "e" else right) if responded else None
            liked = chosen == "lik"
            optimal = bool(responded and (liked == bool(i)))
            qualifies = bool(responded and rt >= 0.2)
            person["liked"] += int(liked)
            person["responded"] += int(responded)
            person["optimal"] += int(optimal)
            person["rt_qualified_liked"] += int(liked and qualifies)
            person["rt_qualified_responded"] += int(qualifies)
            person["rt_qualified_optimal"] += int(optimal and qualifies)
            trials.append({"record_id": record_id, "author_id": person["author_id"],
                           "trial": integer(raw["n_trial"]), "training": p, "current": i,
                           "responded": responded, "liked": liked if responded else None,
                           "optimal": optimal if responded else None,
                           "rt": rt, "rt_qualified": qualifies})
        require(person["decision_misses"] == 32 - person["responded"], "Missingness mismatch")
        require(person["optimal"] == (person["liked"] if i else person["responded"] - person["liked"]),
                "Offered-trial optimal identity failed")
        participants.append(person)
    require(set(surveys) <= seen, "Survey respondent without saved task")
    require(len(participants) == 385 and author_id == 333, "Eligibility reconciliation failed")
    # Source auditor's metadata reconstruction is a check, not an eligibility input.
    source_audit = json.loads((SOURCE / "source-schema-audit.json").read_text())
    audited = {r["source_id"]: r for r in source_audit["eligibility"]}
    for row in eligibility_rows:
        require(all(audited[row["source_id"]][key] == value for key, value in row.items()),
                "Independent source eligibility audit disagrees")
    reconciliation = reconcile_cleaned(trials)
    cohort.update({"task_files": len(task_files), "saved_respondents": len(participants),
                   "author_eligible": author_id, "author_excluded": len(participants) - author_id,
                   "raw_offered_trials": len(trials), "eligibility_source_rows_checked": len(eligibility_rows)})
    return participants, trials, cohort, reconciliation


def reconcile_cleaned(trials: list[dict]) -> dict:
    """Fixed filename-order anonymization; never choose a mapping by outcomes."""
    original = read_csv(EXPERIMENT / "data_clean/data_3.csv")
    expected = {(t["author_id"], t["trial"]): t for t in trials
                if t["author_id"] is not None and t["responded"]}
    require(len(original) == len(expected) == 10532, "Cleaned response row count disagrees")
    seen = set()
    for row in original:
        key = (integer(row["ID_anonymous"]), integer(row["n_trial"]))
        require(key in expected and key not in seen, "Author cleaned identity/trial mapping fails")
        seen.add(key)
        raw = expected[key]
        require(integer(row["condition_recode"]) == 2 * raw["training"] - 1, "Training mismatch")
        require(integer(row["condition_dm_recode"]) == 2 * raw["current"] - 1, "Current mismatch")
        require(integer(row["condition_change_recode"]) == (1 if raw["training"] != raw["current"] else -1),
                "Reversal mismatch")
        require(integer(row["optimal"]) == int(raw["optimal"]), "Cleaned optimal coding mismatch")
        require(math.isclose(float(row["DM_choice_component.rt"]), raw["rt"], rel_tol=1e-12, abs_tol=1e-12),
                "Cleaned RT mismatch")
    require(seen == set(expected), "Unmatched raw responses")
    return {"anonymous_mapping": "eligible participants in original sorted task-filename order",
            "mapping_selected_by_outcome": False, "matched_answered_trials": len(seen),
            "fields": ["training", "current", "reversal", "optimal", "response_time"],
            "rt_tolerance": {"relative": 1e-12, "absolute": 1e-12}}


def weighted_contrast(cells: list[list[float]], weights=WEIGHTS) -> dict:
    require(all(len(cell) >= 2 for cell in cells), "Fewer than two participants in a cell")
    means = [float(np.mean(cell)) for cell in cells]
    variances = [float(np.var(cell, ddof=1)) for cell in cells]
    pieces = [w * w * variance / len(cell) for w, variance, cell in zip(weights, variances, cells)]
    estimate = float(sum(w * mean for w, mean in zip(weights, means)))
    variance = sum(pieces)
    if variance == 0:
        return {"estimate": estimate, "se": 0.0, "df": None,
                "ci95": [estimate, estimate], "degenerate_zero_variance": True}
    df = variance * variance / sum(v * v / (len(cell) - 1) for v, cell in zip(pieces, cells))
    se = math.sqrt(variance)
    margin = float(student_t.ppf(0.975, df) * se)
    return {"estimate": estimate, "se": se, "df": df,
            "ci95": [estimate - margin, estimate + margin], "degenerate_zero_variance": False}


def summarize(participants: list[dict], mode: str) -> dict:
    require(mode in ("primary", "all_saved", "answered", "rt_qualified"), "Unknown analysis mode")
    selected = [p for p in participants if mode == "all_saved" or p["eligible"]]
    omitted = [p["record_id"] for p in selected if mode == "answered" and p["responded"] == 0]
    selected = [p for p in selected if p["record_id"] not in omitted]
    numerator = "rt_qualified_liked" if mode == "rt_qualified" else "liked"
    response = "rt_qualified_responded" if mode == "rt_qualified" else "responded"
    optimal = "rt_qualified_optimal" if mode == "rt_qualified" else "optimal"
    by_cell = [[p for p in selected if (p["training"], p["current"]) == cell] for cell in CELL_ORDER]
    denom = lambda p: p["responded"] if mode == "answered" else 32
    values = [[p[numerator] / denom(p) for p in group] for group in by_cell]
    responses = [[p[response] / denom(p) for p in group] for group in by_cell]
    optimals = [[p[optimal] / denom(p) for p in group] for group in by_cell]
    cells = []
    for (p, i), group, value, response_values in zip(CELL_ORDER, by_cell, values, responses):
        require(len(group) >= 2, "Insufficient cell population")
        cells.append({"training": p, "current": i, "participants": len(group),
                      "mean_liked_fraction": float(np.mean(value)),
                      "sd_liked_fraction": float(np.std(value, ddof=1)),
                      "mean_response_fraction": float(np.mean(response_values)),
                      "mean_offered_response_fraction": float(np.mean([x[response] / 32 for x in group])),
                      "offered_trials": 32 * len(group),
                      "numerator_liked_responses": sum(x[numerator] for x in group),
                      "qualifying_responses": sum(x[response] for x in group)})
    delta = weighted_contrast(values)
    means = [c["mean_liked_fraction"] for c in cells]
    r0delta = float(np.mean(responses[2]) - np.mean(responses[3]))
    # No-reversal cells (1,1),(0,0); reversal cells (0,1),(1,0).
    optimum = weighted_contrast(optimals, (0.5, -0.5, -0.5, 0.5))
    require(math.isclose(optimum["estimate"], delta["estimate"] - 0.5 * r0delta, abs_tol=1e-14),
            "Standardized response-adjusted optimal identity failed")
    return {"population": "all_saved_respondents" if mode == "all_saved" else "author_eligible",
            "denominator": "answered_trials" if mode == "answered" else "32_offered_trials",
            "qualifier": "RT >= 0.2" if mode == "rt_qualified" else "all_valid_responses",
            "participants": len(selected), "zero_answer_exclusions": omitted,
            "cells": cells, "standardized_training_contrast": delta,
            "components": {"current_congruent": means[0] - means[1],
                           "current_incongruent": means[2] - means[3]},
            "coding_reconciliation": {"current_incongruent_response_contrast": r0delta,
                "optimal_no_reversal_minus_reversal": optimum,
                "response_adjusted_identity_error": optimum["estimate"] - delta["estimate"] + 0.5 * r0delta,
                "scope": "participant risk difference, not original GLMM coefficient"}}


def awareness_counts(participants: list[dict]) -> list[dict]:
    result = []
    for p, i in CELL_ORDER:
        group = [r for r in participants if r["eligible"] and (r["training"], r["current"]) == (p, i)]
        counts = Counter(r["awareness"] for r in group)
        result.append({"training": p, "current": i, "participants": len(group),
                       **{k: counts[k] for k in ("yes", "no", "missing")}})
    return result


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true", help="Execute after frozen prospective approval")
    args = parser.parse_args()
    require(args.run, "No analysis executed; pass --run only after prospective approval")
    freeze = json.loads((HERE / "protocol-freeze.json").read_text())
    require(freeze["approved_for_execution"] is True, "Protocol has not been approved")
    require(freeze["protocol_sha256"] == sha256(HERE / "PROTOCOL.md"), "Protocol changed after freeze")
    source_hashes = verify_sources()
    participants, trials, cohort, reconciliation = reconstruct()
    results = {"scope": "Retrospective Experiment 3 participant-level assignment contrasts",
               "cohort": cohort, "source_reconciliation": reconciliation,
               "primary": summarize(participants, "primary"),
               "sensitivities": {mode: summarize(participants, mode)
                                 for mode in ("all_saved", "answered", "rt_qualified")},
               "awareness_descriptive_only": awareness_counts(participants),
               "glmm_reproduced": False,
               "mechanistic_mediation_identified": False,
               "full_randomized_ITT_identified": False}
    write_json(HERE / "participants.json", participants)
    write_json(HERE / "results.json", results)
    with (HERE / "prepared-trials.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(trials[0]))
        writer.writeheader()
        writer.writerows(trials)
    receipt = {"completed_utc": datetime.now(timezone.utc).isoformat(),
               "python": sys.version, "python_executable": sys.executable,
               "platform": platform.platform(), "numpy": np.__version__, "scipy": scipy.__version__,
               "analysis_sha256": sha256(Path(__file__)),
               "protocol_sha256": sha256(HERE / "PROTOCOL.md"),
               "protocol_freeze_sha256": sha256(HERE / "protocol-freeze.json"),
               "source_hashes": source_hashes,
               "source_schema_audit_sha256": sha256(SOURCE / "source-schema-audit.json"),
               "outputs": {name: sha256(HERE / name) for name in
                           ("participants.json", "prepared-trials.csv", "results.json")}}
    write_json(HERE / "verification.json", receipt)
    print(json.dumps({"participants": len(participants), "eligible": cohort["author_eligible"],
                      "primary": results["primary"]["standardized_training_contrast"]}, sort_keys=True))


if __name__ == "__main__":
    main()
