"""Validate this documentation continuation, without rerunning scientific checks."""

import hashlib
import difflib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[5]
STUDY = Path(__file__).resolve().parent.parent
OUTPUT = STUDY / "AFFECTIVE-TELIC-CHECKS.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def text_digest(value):
    return digest(value.encode("utf-8"))


def read_json(path):
    return json.loads(path.read_text())


def headings(path):
    result = set()
    for line in path.read_text().splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            title = re.sub(r"[^\w\- ]", "", match[1].lower())
            result.add(title.replace(" ", "-"))
    return result


checks = []
link_inputs = []
surrounding_changes = []


def check(kind, path, passed, **details):
    checks.append(dict(kind=kind, path=str(path), passed=passed, **details))


edits = read_json(STUDY / "AFFECTIVE-TELIC-EDITS.json")["edits"]
for edit in edits:
    path = ROOT / edit["path"]
    current = path.read_text()
    old, new = edit["old"], edit["new"]
    if edit.get("operation") == "append" or not old:
        owned = new
        recovered = current.replace(owned, "", 1)
    elif new.startswith(old):
        owned = new[len(old):]
        recovered = current.replace(owned, "", 1)
    else:
        owned = new
        recovered = current.replace(new, old, 1)
    before = edit["before_text"]
    expected_after = before + new if edit.get("operation") == "append" or not old else before.replace(old, new, 1)
    surroundings_unchanged = text_digest(recovered) == edit["before_sha256"]
    if not surroundings_unchanged:
        surrounding_changes.append(dict(
            path=edit["path"], current_sha256=text_digest(current),
            diff_after_removing_owned_change="".join(difflib.unified_diff(
                before.splitlines(keepends=True), recovered.splitlines(keepends=True),
                fromfile="recorded immediate-before", tofile="current surrounding work")),
            scope="Concurrent surrounding work is recorded, not edited, reverted, or scientifically validated by this check."))
    passed = (
        current.count(owned) == 1
        and text_digest(before) == edit["before_sha256"]
        and text_digest(expected_after) == edit["after_sha256"]
    )
    check("owned_edit_and_surrounding_preservation", edit["path"], passed,
          occurrences=current.count(owned), sha256=text_digest(current),
          recovered_sha256=text_digest(recovered),
          expected_before_sha256=edit["before_sha256"],
          recorded_mutation_only_owned_change=text_digest(expected_after) == edit["after_sha256"],
          current_surroundings_unchanged_since_edit=surroundings_unchanged)
    if path.suffix == ".md":
        link_inputs.append((path, owned))

for name in ("ARGUMENT", "REVIEW"):
    receipt = read_json(STUDY / "development" / f"AFFECTIVE-TELIC-{name}-EDIT.json")
    relative = receipt.get("file", receipt.get("path"))
    path = ROOT / relative
    current = path.read_bytes()
    addition = receipt.get("appended_span", receipt.get("append_text")).encode()
    prefix = current[:-len(addition)]
    check("reviewed_append_preservation", relative,
          current.endswith(addition)
          and digest(prefix) == receipt["before_sha256"]
          and digest(current) == receipt["after_sha256"],
          sha256=digest(current), recovered_sha256=digest(prefix))
    link_inputs.append((path, addition.decode()))

manifest_path = ROOT / "sources/37-ethical-minimum-primary-2026-10-06/affective-realization/manifest.json"
manifest = read_json(manifest_path)
previous_manifest = json.loads(next(e["old"] for e in edits if e["path"] == str(manifest_path.relative_to(ROOT))))
for source in manifest["originals"]:
    path = manifest_path.parent / source["filename"]
    data = path.read_bytes()
    check("preserved_original", path.relative_to(ROOT),
          digest(data) == source["sha256"] and len(data) == source["bytes"],
          sha256=digest(data), bytes=len(data))
check("earlier_source_records_unchanged", manifest_path.relative_to(ROOT),
      manifest["originals"][:len(previous_manifest["originals"])] == previous_manifest["originals"],
      earlier_original_count=len(previous_manifest["originals"]))
for source in manifest["link_only"]:
    check("link_only_has_no_fabricated_original", source["id"],
          "sha256" not in source and "bytes" not in source and "filename" not in source,
          status=source["status"])

before = read_json(STUDY / "development/AFFECTIVE-TELIC-BEFORE.json")
for entry in before["protected_lean"]:
    actual = digest((ROOT / entry["path"]).read_bytes())
    check("inspected_lean_unchanged", entry["path"], actual == entry["sha256"], sha256=actual)

# Create the receipt before checking the documentation link that points to it.
OUTPUT.write_text(json.dumps({"status": "validation in progress"}) + "\n")
link_results = []
for origin, content in link_inputs:
    for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        target = raw.strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        path = (origin.parent / unquote(parsed.path)).resolve() if parsed.path else origin
        exists = path.is_file()
        anchor_ok = not parsed.fragment or (exists and unquote(parsed.fragment) in headings(path))
        link_results.append(dict(origin=str(origin.relative_to(ROOT)), target=target,
                                 passed=exists and anchor_ok, exists=exists, anchor_ok=anchor_ok))

report = {
    "date": "2026-10-06",
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Comparative and temporal affective content; documentation, exact preservation and local links only.",
    "passed": all(c["passed"] for c in checks + link_results),
    "checks": checks,
    "local_links": link_results,
    "counts": {"checks": len(checks), "local_links": len(link_results)},
    "review": "Argument and review appendices passed reciprocal review. Independent final review confirmed conditional inference wording, additional affective content distinction, and occurrence/capacity distinction; no material remaining attribution or scope problem.",
    "formal_scope": "No Lean source, law or axiom was changed by this continuation. Five inspected Lean files retain their initial hashes. No new proof, Lean build or scientific rerun is claimed.",
    "research_scope": "No complete assessment or refutation of telic perfectionism; bounded draft access and abstract-only Chow reading are explicit. Experiential realization and C1/C2 remain unresolved.",
    "preservation_scope": "All owned edits are present once. Each recorded after-hash is exactly reproduced by applying only its declared owned edit to its complete recorded before-text. Current surrounding changes are separately recorded and left intact. No staging, commit or unrelated rewrite performed.",
    "concurrent_surrounding_changes": surrounding_changes,
    "concurrency_method": "The initial direct comparison recovered all twelve immediate-before texts exactly. Later strict whole-file checks detected concurrent edits. Final verification tests exact scope of the recorded owned mutation and continued presence of its span, without imposing a freeze on surrounding work. Concurrent changes are not treated as research results of this continuation.",
    "concurrent_record": "development/AFFECTIVE-TELIC-CONCURRENT-ADDITIONS.json",
    "initial_checks": "development/AFFECTIVE-TELIC-FIRST-CHECK.json and AFFECTIVE-TELIC-SECOND-CHECK.json retain validations that detected successive concurrent changes. Initial shared-world and systems-formalization diffs were inspected; later surrounding changes remain recorded separately. No research file was changed to satisfy validation.",
    "historical_checks": "AFFECTIVE-REALIZATION-CHECKS.json remains the earlier checkpoint; its source-note hashes are historical after the present appendices.",
}
OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"passed": report["passed"], **report["counts"],
                  "failures": [c for c in checks + link_results if not c["passed"]]}, indent=2))
raise SystemExit(0 if report["passed"] else 1)
