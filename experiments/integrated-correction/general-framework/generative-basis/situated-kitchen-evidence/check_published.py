#!/usr/bin/env python3
"""Audit published aggregate kitchen evidence; no participant-data reanalysis.

Only document extraction, count consistency and descriptive arithmetic are checked.
Published p-values are transcribed, not reproduced. No new proof claim is made.
"""
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCE = ROOT / "sources/community-kitchen-evidence"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def content(node):
    return re.sub(r"\s+", " ", "".join(node.itertext())).strip()


def percentage(n, d):
    return str((Decimal(n) * 100 / Decimal(d)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def main():
    primary = SOURCE / "sahyoun-2019.xml"
    abstract = SOURCE / "loopstra-2013-record.xml"
    for path, provenance in [(primary, "sahyoun-2019-provenance.json"),
                             (abstract, "loopstra-2013-provenance.json")]:
        assert digest(path) == json.loads((SOURCE / provenance).read_text())["sha256"]
    tree = ET.parse(primary).getroot()
    sections = {s.get("id"): content(s) for s in tree.findall(".//body//sec")}
    rows = [[content(c) for c in row] for row in tree.findall(".//table-wrap[@id='Tab2']//tr")]
    by_label = {row[0]: row for row in rows if len(row) == 4}
    selected = {
        "affss": "AFFSS score, median [IQR]",
        "food_secure": "Food secure, n (%)",
        "moderate": "Moderately food insecure, n (%)",
        "severe": "Severely food insecure, n (%)",
        "major_decisions": "Major household expenditures, n (%)",
        "mental_health": "Mental health inventory score, median [IQR]",
        "social_support": "Social support score (DSSI), median [IQR]",
        "expenditure_per_capita": "Household expenditure, total monthly USD per capita, median [IQR]",
    }
    records = {key: by_label[label] for key, label in selected.items()}
    count = lambda key, column: int(re.match(r"\d+", records[key][column])[0])
    flow = {
        "initial": int(re.search(r"sample of (\d+) women", sections["Sec10"])[1]),
        "early_exit": int(re.search(r"(\d+) women dropped out", sections["Sec10"])[1]),
        "matched": int(re.search(r"months, (\d+) women participated", sections["Sec10"])[1]),
    }
    assert "One further woman did not complete the endline questionnaire" in sections["Sec10"]
    flow["endline_missing"] = 1
    flow["continued_after_week_one"] = flow["initial"] - flow["early_exit"]
    assert flow["initial"] == flow["early_exit"] + flow["matched"] + flow["endline_missing"]
    assert sum(count(k, 1) for k in ["food_secure", "moderate", "severe"]) == flow["matched"]
    assert sum(count(k, 2) for k in ["food_secure", "moderate", "severe"]) == flow["matched"]
    assert [count(k, 1) for k in ["food_secure", "moderate", "severe"]] == [14, 12, 6]
    assert [count(k, 2) for k in ["food_secure", "moderate", "severe"]] == [19, 8, 5]
    assert records["affss"][3] == "0.006"
    assert all(records[k][3] == "NS" for k in ["food_secure", "moderate", "severe", "mental_health", "social_support"])
    assert [count("major_decisions", c) for c in [1, 2]] == [3, 13]
    assert records["major_decisions"][3] == "0.038"
    improved = int(re.search(r"(\d+)/32 women had some level of increase", sections["Sec14"])[1])
    decreased = int(re.search(r"(\d+)/32 women had a decrease", sections["Sec14"])[1])
    assert improved + decreased == flow["matched"]
    assert "no counterfactual" in sections["Sec16"]
    assert "did not measure household food consumption" in sections["Sec16"]
    assert "13%" in sections["Sec11"]
    nonparticipant = ET.parse(abstract).find(".//result")
    assert nonparticipant.findtext("id") == "23618120"
    abst = nonparticipant.findtext("abstractText")
    initial_families = int(re.search(r"among (\d+) families", abst)[1])
    followed_families = int(re.search(r"study, (\d+) families", abst)[1])
    kitchen_users = int(re.search(r"(\d+) in a community kitchen", abst)[1])
    assert (initial_families, followed_families, kitchen_users) == (485, 371, 16)
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed",
        "scope": "Published aggregate extraction and arithmetic, not raw-data statistical replication, causal identification, field intervention or mathematical proof.",
        "sources": {p.name: digest(p) for p in [primary, abstract]},
        "checker_sha256": digest(Path(__file__)),
        "sahyoun_2019": {
            "flow": flow,
            "early_exit_percent_of_initial": percentage(flow["early_exit"], flow["initial"]),
            "matched_percent_of_initial": percentage(flow["matched"], flow["initial"]),
            "selected_table2_rows": records,
            "food_insecure_baseline_count": count("moderate", 1) + count("severe", 1),
            "food_insecure_endline_count": count("moderate", 2) + count("severe", 2),
            "net_fewer_food_insecure_count": count("moderate", 1) + count("severe", 1) - count("moderate", 2) - count("severe", 2),
            "interpretation": "Five is a net aggregate decrease, not five identified transitions or five causal successes. Category tests are NS; the score test is reported separately.",
            "mental_health_direction_counts": {"increase": improved, "decrease": decreased},
            "published_rounding_note": "Table 2 gives 19/32 as 59.3%; ordinary one-decimal rounding is 59.4%. Original bytes and counts remain unchanged.",
            "estimand_note": "The text's 13% total household expenditure change is not the relative change between the table's per-capita medians. No discrepancy correction or individual change is inferred from their difference.",
        },
        "loopstra_2013_abstract": {
            "initial_families": initial_families, "followed_families": followed_families,
            "kitchen_users": kitchen_users,
            "kitchen_users_percent_of_followed": percentage(kitchen_users, followed_families),
            "scope": "Observed uptake in the followed community sample, not acceptance among invited kitchen applicants or a causal effect; full text not inspected.",
        },
        "unavailable": "Participant data and paired transitions are not public in Sahyoun 2019; no data request or participant contact was sent.",
    }
    (HERE / "published-evidence-checks.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "flow": flow,
                      "early_exit_percent": result["sahyoun_2019"]["early_exit_percent_of_initial"],
                      "table_rows": len(records), "mental_health_directions": [improved, decreased],
                      "community_kitchen_uptake": [kitchen_users, followed_families]}, indent=2))


if __name__ == "__main__":
    main()
