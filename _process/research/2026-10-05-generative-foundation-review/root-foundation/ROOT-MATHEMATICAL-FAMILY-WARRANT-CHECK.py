"""Check the owned integration, links and binding to an existing Lean receipt.

This validates documents and existing receipt bindings; it does not rerun Lean.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREFIX = "ROOT-MATHEMATICAL-FAMILY-WARRANT-"
MANIFEST = HERE / (PREFIX + "EDITS.json")
OUTPUT = HERE / (PREFIX + "CHECKS.json")
PACKAGE = ROOT / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def anchors(path):
    used, result = {}, set()
    for line in path.read_text().splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            slug = re.sub(r"[^\w\s-]", "", match[1].lower())
            slug = re.sub(r"\s", "-", slug)
            count = used.get(slug, 0)
            result.add(slug if count == 0 else f"{slug}-{count}")
            used[slug] = count + 1
    return result


def main():
    manifest = json.loads(MANIFEST.read_text())
    errors, segments, additions = [], [], []
    for entry in manifest["edits"]:
        path = ROOT / entry["path"]
        data, block = path.read_bytes(), entry["block"].encode()
        if data.count(block) != 1 or sha(block) != entry["block_sha256"]:
            errors.append(f"Changed owned insertion: {entry['path']}")
        additions.append({
            "path": entry["path"],
            "insertion_present": data.count(block) == 1,
            "prior_bytes_preserved_at_write": entry["preserved_prior_bytes_at_write"],
            "prior_content_still_matches": sha(data.replace(block, b"", 1)) == entry["before_sha256"],
        })
        segments.append((path, entry["block"]))
    owned = [HERE / (PREFIX + "REASSESSMENT.md"), ROOT / "sources/15-codex-theory-conversations/2026-10-07-whole-family-warrant-continuation.md"]
    hashes = {}
    for path in owned:
        if not path.exists():
            errors.append(f"Missing owned document: {path}")
            continue
        hashes[str(path.relative_to(ROOT))] = sha(path.read_bytes())
        segments.append((path, path.read_text()))
    links, fragments = 0, 0
    for path, content in segments:
        if any(line.rstrip() != line for line in content.splitlines()):
            errors.append(f"Trailing whitespace: {path.name}")
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
            if re.match(r"[a-zA-Z][\w+.-]*:", target):
                continue
            rel, _, fragment = unquote(target).partition("#")
            destination = (path.parent / rel).resolve() if rel else path
            links += 1
            if destination == OUTPUT:
                continue  # Produced by this invocation.
            if not destination.exists():
                errors.append(f"Missing link in {path.name}: {target}")
            elif fragment and destination.suffix == ".md":
                fragments += 1
                if fragment not in anchors(destination):
                    errors.append(f"Missing heading in {path.name}: {target}")
    for group in ["preserved_prior_proof_assets"]:
        for rel, expected in manifest[group].items():
            if sha((ROOT / rel).read_bytes()) != expected:
                errors.append(f"Prior asset changed: {rel}")
    receipts = {}
    for rel, expected in manifest["preserved_prior_proof_assets"].items():
        if rel.endswith("/verification.json"):
            receipts[rel] = {"sha256": expected, "unchanged": sha((ROOT / rel).read_bytes()) == expected}
    report = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Owned document, source-binding and preservation checks; no new Lean run, empirical test or metaphysical proof.",
        "owned_document_sha256": hashes,
        "shared_additions": additions,
        "local_links_checked": links,
        "heading_fragments_checked": fragments,
        "previous_proof_assets_preserved": len(manifest["preserved_prior_proof_assets"]),
        "existing_receipt_bindings": receipts,
        "new_mathematical_theorems": 0,
        "new_lean_runs": 0,
        "internal_review": manifest["internal_review"],
        "concurrent_change_observation": manifest.get("concurrent_change_observation"),
        "manifest_sha256": sha(MANIFEST.read_bytes()),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "errors": errors,
        "passed": not errors,
    }
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ["passed", "local_links_checked", "heading_fragments_checked", "errors"]}))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
