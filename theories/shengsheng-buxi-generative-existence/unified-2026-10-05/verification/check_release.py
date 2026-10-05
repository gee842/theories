"""Check the synthesis package and, optionally, its preserved source corpus.

Run from the package directory:
    python3 verification/check_release.py --repository /path/to/theories

For a downloaded copy without the source repository:
    python3 verification/check_release.py --local-only

To exclude other sessions' untracked drafts in the canonical repository:
    python3 verification/check_release.py --repository /path/to/theories --tracked-only
This checks working-copy contents of index-tracked documents, including staged additions.

This checks packaging and provenance, not mathematical truth or rendered layout.
"""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path)
    parser.add_argument("--local-only", action="store_true")
    parser.add_argument("--tracked-only", action="store_true")
    args = parser.parse_args()
    package = Path(__file__).resolve().parent.parent
    markdown_paths = sorted(package.rglob("*.md"))
    excluded_documents = []
    if args.tracked_only:
        if not args.repository or args.local_only:
            parser.error("--tracked-only requires --repository and cannot accompany --local-only")
        repo = args.repository.resolve()
        if not package.is_relative_to(repo):
            parser.error("--tracked-only requires the canonical package inside the repository")
        tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=repo).decode().split("\0")
        tracked_paths = {repo / path for path in tracked if path}
        excluded_documents = [path.relative_to(package).as_posix() for path in markdown_paths if path not in tracked_paths]
        markdown_paths = [path for path in markdown_paths if path in tracked_paths]
    errors = []
    link_count = 0
    skipped = 0
    documents = {}
    for path in markdown_paths:
        body = path.read_text()
        # The authored package uses simple inline links; no reference-style links.
        for raw in re.findall(r"\[[^\]\n]*\]\(([^\)\n]+)\)", body):
            target = raw.strip().strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            destination = (path.parent / target).resolve()
            if args.local_only and not destination.is_relative_to(package):
                skipped += 1
                continue
            link_count += 1
            if not destination.exists():
                errors.append(f"Missing link in {path.name}: {target}")
        for opening, closing in [(r"\[", r"\]"), (r"\(", r"\)")]:
            if body.count(opening) != body.count(closing):
                errors.append(f"Unbalanced math delimiters in {path.name}: {opening}")
        if re.search(r"\b(?:TODO|TBD|FIXME)\b", body):
            errors.append(f"Unresolved editing marker in {path.name}")
        documents[path.relative_to(package).as_posix()] = {"bytes": path.stat().st_size, "sha256": sha256(path)}

    formal = (package / "FORMAL-CORE.md").read_text()
    source_map = (package / "SOURCE-MAP.md").read_text()
    expected = [f"F{i}" for i in range(1, 14)] + ["F2a", "F2b"]
    for label in expected:
        if not re.search(rf"^##?#+ {label} ", formal, re.M):
            errors.append(f"Missing formal result {label}")
    families = [int(n) for n in re.findall(r"^## S(\d+) ", source_map, re.M)]
    if families != list(range(1, len(families) + 1)):
        errors.append("Source family labels are not consecutive")
    for number in range(1, len(families) + 1):
        if not re.search(rf"^## S{number} ", source_map, re.M):
            errors.append(f"Missing source family S{number}")

    snapshots = []
    historical_text_preserved = None
    formal_review_matches = None
    formation_review_matches = None
    joint_review_matches = None
    joint_model_review_matches = None
    if args.repository:
        repo = args.repository.resolve()
        source = repo / "sources/20-codex-theory-sessions-2026-10-05"
        specifications = [
            (source / "SNAPSHOT-MANIFEST.json", source, "003cd2a2e2d95a8b7a46314299342d977aa94d8a"),
            (source / "completion-supplement/MANIFEST.json", source / "completion-supplement/root-of-wisdom", "38f8022eab23e1c08c847163e2daec9a425549c6"),
        ]
        for manifest_path, payload, commit in specifications:
            manifest = json.loads(manifest_path.read_text())
            total_bytes = 0
            for entry in manifest["files"]:
                path = payload / entry["path"]
                if not path.is_file():
                    errors.append(f"Missing preserved source: {path}")
                    continue
                total_bytes += path.stat().st_size
                if path.stat().st_size != entry["bytes"] or sha256(path) != entry["sha256"]:
                    errors.append(f"Changed preserved source: {path}")
            relative = manifest_path.relative_to(repo).as_posix()
            committed = subprocess.check_output(["git", "show", f"{commit}:{relative}"], cwd=repo)
            if committed != manifest_path.read_bytes():
                errors.append(f"Manifest differs from its checkpoint: {relative}")
            snapshots.append({"manifest": relative, "files": len(manifest["files"]), "bytes": total_bytes, "commit": commit})
        readme = Path("theories/shengsheng-buxi-generative-existence/README.md")
        old = subprocess.check_output(["git", "show", f"38f8022:{readme.as_posix()}"], cwd=repo).decode()
        historical_text_preserved = old.split("\n", 1)[1] in (repo / readme).read_text()
        if not historical_text_preserved:
            errors.append("Earlier canonical README text was not preserved intact")
        review = (repo / "_process/research/2026-10-05-unified-theory/formal-review-final.md").read_text()
        reviewed_hash = re.search(r"SHA-256 of the reviewed version: `([a-f0-9]{64})`", review).group(1)
        formal_review_matches = sha256(package / "FORMAL-CORE.md") == reviewed_hash
        if not formal_review_matches:
            errors.append("Formal appendix differs from the version accepted in final review")
        formation_path = package / "FORMATION-MATH.md"
        if formation_path.exists():
            review = (repo / "_process/research/2026-10-05-unified-theory/development-01/formal-final-review.md").read_text()
            reviewed_hash = re.search(r"Final reviewed SHA-256: `([a-f0-9]{64})`", review).group(1)
            formation_review_matches = sha256(formation_path) == reviewed_hash
            if not formation_review_matches:
                errors.append("Formation appendix differs from its accepted review version")
        joint_path = package / "JOINT-FORMATION-MATH.md"
        if joint_path.exists():
            process = repo / "_process/research/2026-10-05-unified-theory/development-02"
            review = (process / "formal-review-final.md").read_text()
            reviewed_hash = re.search(r"Final reviewed SHA-256: `([a-f0-9]{64})`", review).group(1)
            joint_review_matches = sha256(joint_path) == reviewed_hash
            if not joint_review_matches:
                errors.append("Joint-formation appendix differs from its accepted review version")
            model = package / "joint-study/model.py"
            if not model.exists():
                model = repo / "experiments/joint-formation/model.py"
            review = (process / "independent-game-review.md").read_text()
            reviewed_hash = re.search(r"Production SHA-256: `([a-f0-9]{64})`", review).group(1)
            joint_model_review_matches = sha256(model) == reviewed_hash
            if not joint_model_review_matches:
                errors.append("Joint-game implementation differs from its independently reviewed version")

    result = {
        "status": "passed" if not errors else "failed",
        "scope": "Local links, balanced math delimiters, editorial markers, result/source labels, and optional source provenance; no rendering or theorem-prover validation.",
        "document_selection": "Index-tracked Markdown, working-copy contents" if args.tracked_only else "All package Markdown, working-copy contents",
        "excluded_untracked_documents": excluded_documents,
        "documents": documents,
        "local_links_checked": link_count,
        "external_local_links_skipped": skipped,
        "formal_result_labels": expected,
        "source_families": len(families),
        "snapshots": snapshots,
        "historical_canonical_text_preserved": historical_text_preserved,
        "formal_review_version_matches": formal_review_matches,
        "formation_review_version_matches": formation_review_matches,
        "joint_formation_review_version_matches": joint_review_matches,
        "joint_model_review_version_matches": joint_model_review_matches,
        "errors": errors,
    }
    output = package / "verification/release-checks.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "documents"}, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
