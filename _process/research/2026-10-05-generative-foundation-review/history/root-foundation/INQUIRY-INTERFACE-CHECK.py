"""Check this round's preservation and links; execute no scientific model."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "INQUIRY-INTERFACE-CHECKS.json"


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


extraction = json.loads((HERE / "development/inquiry-interface/INQUIRY-EVIDENCE.json").read_text())
bindings = {}
for binding in extraction["bindings"].values():
    for item in [binding["results"], binding["prior_independent_check"],
                 *binding["verified_source_bindings"],
                 *binding["prior_independent_check"]["verified_source_bindings"]]:
        bindings[item["path"]] = item["sha256"]
for item in extraction["verified_handoff_source_bindings"]:
    bindings[item["path"]] = item["sha256"]
extractor = HERE / "development/inquiry-interface/extract_inquiry_evidence.py"
bindings[str(extractor.relative_to(ROOT))] = extraction["extractor_sha256"]
source_checks = [{"file": p, "sha256": h, "matches": digest(ROOT / p) == h}
                 for p, h in sorted(bindings.items())]

package = ROOT / "sources/40-inquiry-interface-2026-10-06"
manifest = json.loads((package / "manifest.json").read_text())
package_checks = [{"file": f["path"],
                   "hash_matches": digest(package / f["path"]) == f["sha256"],
                   "size_matches": (package / f["path"]).stat().st_size == f["bytes"]}
                  for f in manifest["files"]]

edits = json.loads((HERE / "INQUIRY-INTERFACE-CANONICAL-EDITS.json").read_text())
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
notes = sorted(HERE.glob("INQUIRY-INTERFACE-*.md"))
for path in notes:
    links.extend(check_links(path, path.read_text()))
links.extend(check_links(package / "README.md", (package / "README.md").read_text()))

passed = (all(c["matches"] for c in source_checks)
          and all(c["hash_matches"] and c["size_matches"] for c in package_checks)
          and all(c["inserted_text_present"] for c in insertions)
          and all(c["exists"] and c["fragment_ok"] for c in links))
report = {"status": "passed" if passed else "failed",
          "scope": "Source preservation, exact additive integration and local links only. No simulation, proof compiler, statistical reanalysis or ethical certification.",
          "prior_source_bindings": source_checks,
          "primary_package_files": package_checks,
          "canonical_insertions": insertions,
          "local_links": links,
          "local_link_count": len(links),
          "note_sha256": {p.name: digest(p) for p in notes},
          "source_manifest_sha256": digest(package / "manifest.json"),
          "checker_sha256": digest(Path(__file__))}
OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"status": report["status"], "source_bindings": len(source_checks),
                  "primary_files": len(package_checks), "insertions": len(insertions),
                  "local_links": len(links)}))
if not passed:
    raise SystemExit(1)
