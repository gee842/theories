"""Check the captured bytes, portable reading editions, and current reading links.

Uses only the repository and Python's standard library. It does not execute
research programs, contact external services, or modify source snapshots.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCE = REPO / "sources/22-research-reconciliation-2026-10-05"
manifest = json.loads((SOURCE / "MANIFEST.json").read_text())
editions = json.loads((HERE / "reading-editions.json").read_text())
errors = []
cache = {}
historical_objects = set()


def digest(relative):
    if relative not in cache:
        path = (REPO / relative).resolve()
        if not path.is_relative_to(REPO) or not path.is_file():
            errors.append(f"Missing or non-repository file: {relative}")
            cache[relative] = None
        else:
            cache[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return cache[relative]


def captured_matches(entry):
    path = REPO / entry["repository_path"]
    if path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]:
        return True
    blob = entry.get("repository_blob")
    if blob:
        # An active study can legitimately advance while its captured Git version remains.
        result = subprocess.run(["git", "cat-file", "blob", blob], cwd=REPO, capture_output=True)
        if result.returncode == 0 and hashlib.sha256(result.stdout).hexdigest() == entry["sha256"]:
            historical_objects.add(blob)
            return True
    return False


for entry in manifest["files"]:
    if not captured_matches(entry):
        errors.append(f"Captured-byte mismatch: {entry['source']}")

member_count = 0
for archive in manifest["archive_members"]:
    for member in archive["members"]:
        member_count += 1
        if not captured_matches(member):
            errors.append(f"Archive member mismatch: {archive['source']}::{member['name']}")

for entry in editions:
    if digest(entry["source_record"]) != entry["source_sha256"]:
        errors.append(f"Reading edition source mismatch: {entry['file']}")
    if digest(entry["file"]) != entry["edition_sha256"]:
        errors.append(f"Reading edition mismatch: {entry['file']}")
    original = (REPO / entry["source_record"]).read_bytes()
    if entry["link_changes"]:
        text = original.decode()
        for change in entry["link_changes"]:
            old = "](" + change["old"] + ")"
            assert old in text, change
            text = text.replace(old, "](" + change["new"] + ")", 1)
        original = text.encode()
    if original != (REPO / entry["file"]).read_bytes():
        errors.append(f"Unrecorded reading edition change: {entry['file']}")

# Freeze this check to the documented reading set; other sessions may add files.
documents = {REPO / name for name in json.loads((HERE / "reading-documents.json").read_text())}

links = 0
for path in sorted(documents):
    if not path.is_file():
        errors.append(f"Missing reading document: {path.relative_to(REPO)}")
        continue
    # Historical genealogy and frozen source internals have their own provenance.
    text = path.read_text()
    if path == REPO / "theories/becoming/README.md":
        text = text.split("## Historical formulation", 1)[0]
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for href in re.findall(r"\]\(([^)]+)\)", text):
        href = href.strip().strip("<>")
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", href) or href.startswith("#"):
            continue
        base = unquote(href.split("#", 1)[0])
        target = (path.parent / base).resolve()
        links += 1
        if base.startswith("/"):
            errors.append(f"Nonportable live link: {path.relative_to(REPO)} -> {href}")
        if not target.is_relative_to(REPO) or not target.exists():
            errors.append(f"Unresolved repository link: {path.relative_to(REPO)} -> {href}")

result = {
    "status": "passed" if not errors else "failed",
    "captured_external_files_verified": len(manifest["files"]),
    "redundant_archive_members_verified": member_count,
    "reading_edition_files_verified": len(editions),
    "local_reading_links_checked": links,
    "reading_documents_checked": len(documents),
    "historical_git_objects_used": len(historical_objects),
    "scope": "Byte preservation, documented link-only transformations and local target portability; not scientific revalidation, rendered layout, external URLs or every historical source link.",
    "errors": errors,
}
print(json.dumps(result, indent=2))
raise SystemExit(bool(errors))
