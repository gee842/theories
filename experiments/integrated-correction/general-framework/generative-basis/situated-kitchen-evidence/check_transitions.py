#!/usr/bin/env python3
"""Bind source marginals to checked Lean constants and enumerate anonymous tables.

Enumeration is an executable cross-check, not a replacement for the Lean proof.
No participant identity, causal effect or probability over tables is inferred.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEAN = HERE.parent / "lean/universal-ethics/generative-capacity"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def content(node):
    return re.sub(r"\s+", " ", "".join(node.itertext())).strip()


def main():
    source = ROOT / "sources/community-kitchen-evidence/sahyoun-2019.xml"
    provenance = json.loads(source.with_name("sahyoun-2019-provenance.json").read_text())
    assert digest(source) == provenance["sha256"]
    tree = ET.parse(source)
    flow = content(tree.find(".//sec[@id='Sec10']"))
    assert "completed both baseline and endline assessment" in flow
    n = int(re.search(r"months, (\d+) women participated", flow)[1])
    rows = [[content(c) for c in row] for row in tree.findall(".//table-wrap[@id='Tab2']//tr")]
    rows = {row[0]: row for row in rows if len(row) == 4}
    labels = ["Food secure, n (%)", "Moderately food insecure, n (%)", "Severely food insecure, n (%)"]
    counts = [[int(re.match(r"\d+", rows[label][col])[0]) for col in (1, 2)] for label in labels]
    assert all(sum(row[col] for row in counts) == n for col in (0, 1))
    before, after = counts[0]
    lean_source = LEAN / "KitchenTransitions.lean"
    code = lean_source.read_text()
    constants = {name: int(value) for name, value in re.findall(r"^def (sampleSize|beforeSafe|afterSafe) : Nat := (\d+)$", code, re.M)}
    assert constants == {"sampleSize": n, "beforeSafe": before, "afterSafe": after}
    verification = json.loads((LEAN / "kitchen-transitions-verification.json").read_text())
    assert verification["status"] == "passed"
    assert verification["source_sha256"]["KitchenTransitions"] == digest(lean_source)
    assert verification["modules"][0]["theorems"] == 7
    tables = []
    for kept in range(n + 1):
        for lost in range(n + 1):
            for gained in range(n + 1):
                neither = n - kept - lost - gained
                if neither >= 0 and kept + lost == before and kept + gained == after:
                    tables.append({"kept_safe": kept, "safe_to_insecure": lost,
                                   "insecure_to_safe": gained, "kept_insecure": neither})
    tables.sort(key=lambda row: row["safe_to_insecure"])
    assert len(tables) == 14
    assert [row["safe_to_insecure"] for row in tables] == list(range(14))
    assert [row["insecure_to_safe"] for row in tables] == list(range(5, 19))
    assert all(row["insecure_to_safe"] == row["safe_to_insecure"] + after - before for row in tables)
    result = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Source-bound anonymous count possibilities for the reported paired cohort; no recovered actual table, causation, sampling inference or ethical certification.",
        "source_sha256": digest(source), "checker_sha256": digest(Path(__file__)),
        "lean_source_sha256": digest(lean_source),
        "lean_verification_sha256": digest(LEAN / "kitchen-transitions-verification.json"),
        "marginals": constants, "binary_tables": tables,
        "bounds": {"safe_to_insecure": [0, 13], "insecure_to_safe": [5, 18]},
        "preserved_limits": [
            "Assumes the publication correctly describes the same 32 paired records.",
            "Binary coarsening merges moderate and severe insecurity; within-category changes remain unrepresented.",
            "Compatible tables receive no likelihood or probability; endpoints are not estimated actual losses.",
            "The 18 early exits and one missing endpoint are outside this matched-cohort statement.",
            "Survey categories do not certify actual basic protection or a J1/J2 ethical comparison.",
        ],
    }
    (HERE / "transition-checks.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "passed", "tables": len(tables), "marginals": constants, "bounds": result["bounds"]}))


if __name__ == "__main__":
    main()
