"""Check the owned research insertions and preserved sources, not ethical validity."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "PRACTICAL-BOUNDARY-CHECKS.json"
SOURCE = ROOT / "sources/37-ethical-minimum-primary-2026-10-06/practical-boundary"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(path):
    found, counts = set(), {}
    for line in path.read_text().splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", match[1]).lower()
            slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
            n = counts.get(slug, 0)
            counts[slug] = n + 1
            found.add(slug if n == 0 else f"{slug}-{n}")
    return found


edits = json.loads((HERE / "PRACTICAL-BOUNDARY-EDITS.json").read_text())["edits"]
notes = [HERE / f"PRACTICAL-BOUNDARY-{suffix}.md" for suffix in (
    "RECONSTRUCTION", "ETHICAL-ARGUMENT", "COUNTERREVIEW", "EVIDENCE", "INTEGRATION"
)] + [SOURCE / "README.md"]
scopes = [(p, p.read_text()) for p in notes]
scopes += [(ROOT / edit["file"], edit["new"]) for edit in edits]
errors, links, hashes = [], [], []
for source, body in scopes:
    targets = re.findall(r"\]\(([^)]+)\)", body)
    targets += re.findall(r"^\[[^]]+\]:\s+(\S+)", body, re.M)
    for target in targets:
        parsed = urlsplit(target.strip("<>"))
        if parsed.scheme or parsed.netloc:
            continue
        path = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
        exists = path.exists() or path == OUTPUT
        fragment = unquote(parsed.fragment)
        valid_anchor = not fragment or (exists and path.suffix == ".md" and fragment in anchors(path))
        passed = exists and valid_anchor
        links.append({"source": str(source.relative_to(ROOT)), "target": target, "passed": passed})
        if not passed:
            errors.append(f"Unresolved link: {source.relative_to(ROOT)} -> {target}")
    if any(line != line.rstrip() for line in body.splitlines()):
        errors.append(f"Trailing whitespace: {source.relative_to(ROOT)}")

# Reverse only exact owned fragments in memory. Never revert unrelated work.
copies = {e["file"]: (ROOT / e["file"]).read_text() for e in edits}
for edit in reversed(edits):
    content = copies[edit["file"]]
    if content.count(edit["new"]) == 1:
        copies[edit["file"]] = content.replace(edit["new"], edit["old"], 1)
    elif edit["new"].startswith(edit["old"]) and edit["new"] != edit["old"]:
        addition = edit["new"][len(edit["old"]):]
        if content.count(addition) == 1 and edit["old"] in content:
            copies[edit["file"]] = content.replace(addition, "", 1)
        else:
            errors.append(f"Insertion not uniquely recoverable: {edit['file']}")
    else:
        errors.append(f"Edit not uniquely recoverable: {edit['file']}")

for item in json.loads((HERE / "development/PRACTICAL-BOUNDARY-BEFORE.json").read_text())["files"]:
    path = ROOT / item["snapshot"]
    actual = digest(path)
    passed = actual == item["sha256"]
    hashes.append({"file": item["snapshot"], "sha256": actual, "passed": passed})
    if not passed:
        errors.append(f"Snapshot changed: {item['snapshot']}")

for item in json.loads((SOURCE / "manifest.json").read_text())["files"]:
    path = SOURCE / item["file"]
    actual = digest(path)
    passed = actual == item["sha256"] and path.stat().st_size == item["bytes"]
    hashes.append({"file": str(path.relative_to(ROOT)), "sha256": actual, "passed": passed})
    if not passed:
        errors.append(f"Source changed: {item['file']}")

result = {
    "scope": "Owned document links, insertion recoverability, source/snapshot preservation only; no scientific rerun or ethical validation.",
    "passed": not errors,
    "owned_edits": len(edits),
    "links_checked": len(links),
    "hashes_checked": len(hashes),
    "links": links,
    "hashes": hashes,
    "document_hashes": {str(p.relative_to(ROOT)): digest(p) for p in notes},
    "errors": errors,
}
OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({key: result[key] for key in (
    "scope", "passed", "owned_edits", "links_checked", "hashes_checked", "errors"
)}, indent=2))
raise SystemExit(bool(errors))
