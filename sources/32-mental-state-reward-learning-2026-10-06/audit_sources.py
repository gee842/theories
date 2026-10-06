"""Audit preserved source bytes and eligibility, without estimating outcomes.

Run with Python's standard library from any working directory. This script does
not download, modify originals, aggregate choices, or fit a statistical model.
"""
from pathlib import Path
import csv
import datetime as dt
import hashlib
import json
import re


BASE = Path(__file__).resolve().parent
ORIGINALS = BASE / "originals"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def missing(value):
    return value.strip() in ("", "NA", "NaN", "nan")


def main():
    manifest = json.loads((BASE / "manifest.json").read_text())
    for record in manifest["selected_archive_members"] + [manifest["paper"]]:
        data = (BASE / record["path"]).read_bytes()
        assert len(data) == record["bytes"], record["path"]
        assert hashlib.sha256(data).hexdigest() == record["sha256"], record["path"]

    survey_rows = read_csv(ORIGINALS / "Experiment_3/data_raw_primary/Qualtrics/post_task_survey_3_anonymized.csv")
    surveys = {}
    early = complete_after = without_id = 0
    cutoff = dt.datetime(2023, 12, 5)
    for row in survey_rows:
        if row["Progress"] != "100":
            continue
        try:
            date = dt.datetime.strptime(row["EndDate"], "%m/%d/%y %H:%M")
        except ValueError:
            continue
        if date < cutoff:
            early += 1
            continue
        complete_after += 1
        if not re.fullmatch(r"P[0-9]+", row["Connect.ID"]):
            without_id += 1
            continue
        assert row["Connect.ID"] not in surveys
        surveys[row["Connect.ID"]] = row

    participants = []
    for path in sorted((ORIGINALS / "Experiment_3/data_raw_primary/Pavlovia").glob("*.csv")):
        rows = read_csv(path)
        pid = rows[0]["Connect.ID"]
        conditioning = [row for row in rows if row.get("Congruent", "") not in ("", "NA")]
        decisions = [row for row in rows if not missing(row.get("n_trial", ""))]
        pmiss = sum(missing(row.get("acknowledge_resp.rt", "")) for row in conditioning)
        dmiss = sum(missing(row.get("DM_choice_component.rt", "")) for row in decisions)
        survey = surveys.get(pid)
        attention = int(survey["attention_check"][0]) if survey and survey["attention_check"] and survey["attention_check"][0].isdigit() else None
        eligible = bool(survey and pmiss < 8 and dmiss < 7 and attention is not None and attention < 4)
        participants.append({
            "source_file": path.relative_to(BASE).as_posix(), "source_id": pid,
            "post_date_complete": bool(survey), "conditioning_trials": len(conditioning),
            "missing_conditioning_responses": pmiss, "decision_trials": len(decisions),
            "missing_decision_responses": dmiss, "attention_numeric": attention,
            "author_eligible": eligible, "condition": rows[0].get("experimental_condition"),
            "condition_dm": rows[0].get("condition_DM"),
        })
    complete = [p for p in participants if p["post_date_complete"]]
    eligible = [p for p in participants if p["author_eligible"]]
    # This follows the source script's filename order. It is a provisional map
    # until the separate analysis checks the raw-to-clean trial correspondence.
    for index, participant in enumerate(eligible, 1):
        participant["ID_anonymous"] = index
    clean = read_csv(ORIGINALS / "Experiment_3/data_clean/data_3.csv")
    report = {
        "scope": "Metadata, missing-response counts and prescribed eligibility only; no choice aggregation or effect estimation",
        "preserved_original_hash_checks": len(manifest["selected_archive_members"]) + 1,
        "qualtrics_rows_including_two_metadata_rows": len(survey_rows),
        "completed_before_2023_12_05": early,
        "completed_after_cutoff": complete_after,
        "postcutoff_missing_anonymous_id": without_id,
        "postcutoff_complete_ids": len(surveys),
        "pavlovia_files": len(participants), "saved_complete_responders": len(complete),
        "author_eligible": len(eligible),
        "clean_csv_participants": len({row["ID_anonymous"] for row in clean}),
        "clean_csv_rows": len(clean),
        "criteria_pass_among_saved_complete": {
            "conditioning_misses_lt8": sum(p["missing_conditioning_responses"] < 8 for p in complete),
            "decision_misses_lt7": sum(p["missing_decision_responses"] < 7 for p in complete),
            "attention_lt4": sum(p["attention_numeric"] is not None and p["attention_numeric"] < 4 for p in complete),
        },
        "anonymous_id_map_status": "Provisional source-script filename order; no outcome correspondence checked in this audit",
        "eligibility": participants,
        "privacy": {
            "actual_name_email_external_reference_nonempty": {
                key: sum(bool(row[key].strip()) for row in survey_rows[2:])
                for key in ("RecipientLastName", "RecipientFirstName", "RecipientEmail", "ExternalReference")
            },
            "free_text_email_regex_hits": sum(bool(re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", json.dumps(row), re.I)) for row in survey_rows[2:]),
            "retained_public_fields": "Anonymous P-number and response IDs, dates, demographics and free-text remain in the original public source. No identifying text is reproduced in the report.",
            "limit": "A structural check and email-pattern scan do not prove that every free-text response is nonidentifying.",
        },
    }
    (BASE / "source-schema-audit.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items() if key not in ("eligibility", "privacy")}))


if __name__ == "__main__":
    main()
