"""Check this round's preservation and links; execute no scientific model."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "INQUIRY-SUFFICIENCY-CHECKS.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchor(heading):
    heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"[^\w\- ]", "", heading.lower())
    return heading.replace(" ", "-")


def check_links(document, content):
    result = []
    for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        target = raw.strip("<>")
        if urlsplit(target).scheme:
            continue
        name, _, fragment = target.partition("#")
        path = (document.parent / unquote(name)).resolve() if name else document
        exists = path.exists() or path == OUTPUT
        fragment_ok = True
        if exists and fragment and path.suffix == ".md":
            headings = re.findall(r"^#{1,6} (.+)$", path.read_text(), re.M)
            fragment_ok = unquote(fragment) in {anchor(h) for h in headings}
        result.append({"document": str(document.relative_to(ROOT)),
                       "target": target, "exists": exists,
                       "fragment_ok": fragment_ok})
    return result


extraction = json.loads((HERE / "development/inquiry-sufficiency/PREFIX-EVIDENCE.json").read_text())
bindings = {}
for binding in extraction["bindings"].values():
    for item in [binding["results"], binding["prior_check"],
                 *binding["producer"], *binding["independent"]]:
        bindings[item["path"]] = item["sha256"]
analysis = HERE / "development/inquiry-sufficiency/analyze_saved_prefixes.py"
bindings[str(analysis.relative_to(ROOT))] = extraction["script_sha256"]
source_checks = [{"file": p, "sha256": h, "matches": digest(ROOT / p) == h}
                 for p, h in sorted(bindings.items())]
# Independently traverse the archived transition matrices from each saved cursor.
prediction_checks = []
for prefix in extraction["four_feedback_prefixes"]:
    for item in prefix["predictions"]:
        code, cursor = item["candidate"]
        machine = extraction["source_machines"][code // 2]
        first = machine["transitions"][cursor][0]
        second = machine["transitions"][first][0]
        actual = [machine["outputs"][first] ^ (code % 2),
                  machine["outputs"][second] ^ (code % 2)]
        prediction_checks.append({"prefix": prefix["acquisition_read_number"],
                                  "candidate": item["candidate"],
                                  "matches": actual == item["next_two_readings"]})

edits = json.loads((HERE / "INQUIRY-SUFFICIENCY-CANONICAL-EDITS.json").read_text())
insertions = []
links = []
for edit in edits["changes"]:
    path = ROOT / edit["file"]
    # Other sessions may prepend their own entries at the same heading.
    # Verify our exact addition, not its adjacency to an unchanged anchor.
    addition = edit["new_text"].replace(edit["old_text"], "", 1)
    assert addition and addition != edit["new_text"]
    insertions.append({"file": edit["file"], "inserted_text_present": addition in path.read_text()})
    links.extend(check_links(path, edit["new_text"]))
notes = sorted(HERE.glob("INQUIRY-SUFFICIENCY-*.md"))
for path in notes:
    links.extend(check_links(path, path.read_text()))

passed = (all(c["matches"] for c in source_checks)
          and all(c["matches"] for c in prediction_checks)
          and all(c["inserted_text_present"] for c in insertions)
          and all(c["exists"] and c["fragment_ok"] for c in links))
report = {"status": "passed" if passed else "failed",
          "scope": "Source preservation, exact additive integration and local links only. No simulation, proof compiler, statistical reanalysis or ethical certification.",
          "prior_source_bindings": source_checks,
          "independent_prefix_predictions": prediction_checks,
          "canonical_insertions": insertions,
          "local_links": links,
          "local_link_count": len(links),
          "note_sha256": {p.name: digest(p) for p in notes},
          "prefix_evidence_sha256": digest(HERE / "development/inquiry-sufficiency/PREFIX-EVIDENCE.json"),
          "checker_sha256": digest(Path(__file__))}
OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"status": report["status"], "source_bindings": len(source_checks),
                  "prefix_predictions": len(prediction_checks), "insertions": len(insertions),
                  "local_links": len(links)}))
if not passed:
    raise SystemExit(1)
