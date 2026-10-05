"""Export the committed unified theory as a reading bundle with working local citations."""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[3]
    source = repo / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05"
    output = args.output.resolve()
    if source == output or source in output.parents:
        raise ValueError("Export must be outside the canonical package")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
    dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo, text=True)
    if dirty:
        raise RuntimeError("Commit the source repository before making a release")
    output.mkdir(parents=True, exist_ok=True)
    substitutions = 0
    source_documents = {}
    experiment = repo / "experiments/constructed-correction"
    def export_markdown(path, destination):
        def replace(match):
            nonlocal substitutions
            raw = match.group(2).strip().strip("<>")
            if urlsplit(raw).scheme or raw.startswith("#"):
                return match.group(0)
            target, sep, anchor = raw.partition("#")
            resolved = (path.parent / unquote(target)).resolve()
            assert resolved.exists(), resolved
            if resolved.is_relative_to(source):
                mapped = output / resolved.relative_to(source)
                new_target = os.path.relpath(mapped, destination.parent)
            elif resolved.is_relative_to(experiment):
                mapped = output / "formation-study" / resolved.relative_to(experiment)
                new_target = os.path.relpath(mapped, destination.parent)
            else:
                new_target = str(resolved)
            substitutions += 1
            if new_target == raw:
                return match.group(0)
            return f"[{match.group(1)}](<{new_target}{sep}{anchor}>)"
        exported = re.sub(r"\[([^\]\n]*)\]\(([^\)\n]+)\)", replace, path.read_text())
        destination.write_text(exported)
    for path in sorted(source.glob("*.md")):
        export_markdown(path, output / path.name)
        source_documents[path.name] = digest(path)
    shutil.copytree(source / "verification", output / "verification", dirs_exist_ok=True)
    shutil.copy2(source / "verification/release-checks.json", output / "verification/canonical-release-checks.json")
    reviews = output / "reviews"
    reviews.mkdir(exist_ok=True)
    for name in ["formal-review-final.md", "editorial-review-final.md", "main-review-direction.md"]:
        shutil.copy2(Path(__file__).parent / name, reviews / name)
    if experiment.exists():
        shutil.copytree(experiment, output / "formation-study", dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        for path in experiment.rglob("*.md"):
            export_markdown(path, output / "formation-study" / path.relative_to(experiment))
        development_reviews = reviews / "development-01"
        development_reviews.mkdir(exist_ok=True)
        for name in ["formal-final-review.md", "integration-final-review.md", "independent-game-review.md"]:
            path = Path(__file__).parent / "development-01" / name
            export_markdown(path, development_reviews / name)
    (output / "PACKAGE.md").write_text(f"""# Unified theory reading bundle

Start with [the short guide](START-HERE.md), then read [the full theory](THEORY.md) and [formal core](FORMAL-CORE.md). The [claim register](CLAIMS.md) and [source map](SOURCE-MAP.md) identify what each conclusion rests on. The [synthesis record](SYNTHESIS-RECORD.md) explains integration, verification, and the remaining research frontier.

The theory and proof appendices are self-contained. This edition includes [Development 1](FORMATION.md), its [new proofs](FORMATION-MATH.md), the [ethical foundation](ETHICAL-FOUNDATION.md), and the full [formation study](formation-study/README.md) with code, data, and independent checks. Source citations outside this package point to the preserved repository on this computer. The archive does not duplicate the 338 MB earlier source snapshot. These citation destinations may need adjustment if the reading bundle is moved to another computer; the manifest records the canonical source location and commit.

The [original formal review](reviews/formal-review-final.md), [original editorial review](reviews/editorial-review-final.md), and [original direction review](reviews/main-review-direction.md) cover the first synthesis. The [new proof review](reviews/development-01/formal-final-review.md), [integration review](reviews/development-01/integration-final-review.md), and [game audit](reviews/development-01/independent-game-review.md) cover Development 1. Requested precision edits were applied before release. These are collaborating AI agents' reviews, distinct from external peer review and empirical validation.

From the unpacked package directory, the two mathematical check programs run with Python's standard library:

```text
python3 verification/check_integration.py
python3 verification/check_mechanisms.py
python3 verification/check_formation_math.py
python3 verification/check_release.py --local-only
```

The last command checks the exported documents and internal links without requiring the source repository. It replaces the local release-check result; the original canonical record is separately retained in [canonical-release-checks.json](verification/canonical-release-checks.json). [DELIVERY.json](DELIVERY.json) records package file hashes and provenance.

The pre-synthesis checkpoints are `003cd2a` and `38f8022`; the original completed integration is `dd8ad7c`. The Development 1 protocol was committed as `1929eb5` before enumeration. This edition is committed as `{commit}`. The repository was clean when this bundle was exported.
""")
    manifest_path = output / "DELIVERY.json"
    manifest_path.write_text("{}\n")
    subprocess.run([sys.executable, str(output / "verification/check_release.py"), "--repository", str(repo)], check=True)
    files = [p for p in sorted(output.rglob("*")) if p.is_file() and p != manifest_path]
    manifest = {
        "title": "Relational generativity and the conditions of wisdom",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "canonical_repository": str(repo),
        "canonical_package": str(source),
        "pre_synthesis_checkpoints": ["003cd2a2e2d95a8b7a46314299342d977aa94d8a", "38f8022eab23e1c08c847163e2daec9a425549c6"],
        "integration_commit": commit,
        "source_repository_clean": True,
        "source_document_sha256": source_documents,
        "local_citations_resolved": substitutions,
        "files": [{"path": p.relative_to(output).as_posix(), "bytes": p.stat().st_size, "sha256": digest(p)} for p in files],
        "scope": "The updated synthesis, proofs, ethical development, exact formation study and data, internal reviews, independent check programs and records. Earlier source corpus is preserved in the separate committed repository.",
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    archive = output.with_suffix(".zip")
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(output.rglob("*")):
            if path.is_file():
                zf.write(path, Path(output.name) / path.relative_to(output))
    with zipfile.ZipFile(archive) as zf:
        assert zf.testzip() is None
        assert len(zf.namelist()) == len(files) + 1
    for record in manifest["files"]:
        path = output / record["path"]
        assert path.stat().st_size == record["bytes"] and digest(path) == record["sha256"]
    print(json.dumps({"output": str(output), "archive": str(archive), "archive_bytes": archive.stat().st_size, "files": len(files) + 1, "integration_commit": commit, "status": "passed"}, indent=2))


if __name__ == "__main__":
    main()
