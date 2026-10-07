"""Check this round's documentation and unchanged prior Lean source hashes.

This does not run Lean or certify philosophical claims. Run from any directory.
Shared-file additions are checked individually so later concurrent work is retained.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MANIFEST = HERE / "WHOLE-CONTINUATION-WARRANT-EDITS.json"
OUTPUT = HERE / "WHOLE-CONTINUATION-WARRANT-CHECKS.json"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def anchors(path):
    used = {}
    result = set()
    for line in path.read_text().splitlines():
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        slug = re.sub(r"[^\w\s-]", "", heading[1].lower())
        slug = re.sub(r"\s", "-", slug)
        suffix = used.get(slug, 0)
        result.add(slug if suffix == 0 else f"{slug}-{suffix}")
        used[slug] = suffix + 1
    return result


def main():
    manifest = json.loads(MANIFEST.read_text())
    errors, segments, shared = [], [], []
    for entry in manifest["edits"]:
        path = ROOT / entry["path"]
        data = path.read_bytes()
        block = entry["block"].encode()
        if data.count(block) != 1 or sha(block) != entry["block_sha256"]:
            errors.append(f"Owned addition changed: {entry['path']}")
        shared.append({
            "path": entry["path"],
            "owned_addition_present": data.count(block) == 1,
            "prior_bytes_preserved_at_write": entry["preserved_prior_bytes_at_write"],
            "prior_content_still_matches": sha(data.replace(block, b"", 1)) == entry["before_sha256"],
        })
        segments.append((path, entry["block"]))
    for rel, expected in manifest["owned_documents"].items():
        path = ROOT / rel
        if sha(path.read_bytes()) != expected:
            errors.append(f"Reviewed document changed: {rel}")
        segments.append((path, path.read_text()))
    links, fragments = 0, 0
    for path, content in segments:
        if any(line.rstrip() != line for line in content.splitlines()):
            errors.append(f"Trailing whitespace: {path.relative_to(ROOT)}")
        for destination in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
            if re.match(r"[a-zA-Z][\w+.-]*:", destination):
                continue
            target, _, fragment = unquote(destination).partition("#")
            resolved = (path.parent / target).resolve() if target else path
            links += 1
            if resolved == OUTPUT:
                # This receipt is produced below, including on a first run.
                continue
            if not resolved.exists():
                errors.append(f"Missing target in {path.name}: {destination}")
            elif fragment and resolved.suffix == ".md":
                fragments += 1
                if fragment not in anchors(resolved):
                    errors.append(f"Missing heading in {path.name}: {destination}")
    formal = ROOT / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal"
    prior = json.loads((formal / "verification.json").read_text())
    for rel, expected in manifest["unchanged_formal_reference"].items():
        path = ROOT / rel
        actual = sha(path.read_bytes())
        if actual != expected or actual != prior["source_sha256"][path.name]:
            errors.append(f"Lean source differs from previous verification: {rel}")
    if sha((formal / "check.py").read_bytes()) != prior["checker_sha256"]:
        errors.append("Previous Lean checker source changed")
    report = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Document integration checks and hashes against existing Lean receipt; no Lean rerun, empirical test or philosophical certification.",
        "owned_documents": manifest["owned_documents"],
        "shared_additions": shared,
        "local_links_checked": links,
        "heading_fragments_checked": fragments,
        "unchanged_lean_modules": len(manifest["unchanged_formal_reference"]),
        "prior_lean_verification_at": prior["checked_at_utc"],
        "manifest_sha256": sha(MANIFEST.read_bytes()),
        "final_internal_review": manifest["final_internal_review"],
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "errors": errors,
        "passed": not errors,
    }
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ["passed", "local_links_checked", "heading_fragments_checked", "unchanged_lean_modules", "errors"]}))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
