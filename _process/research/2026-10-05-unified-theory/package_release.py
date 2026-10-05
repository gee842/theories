"""Export the committed unified theory as a reading bundle with working local citations."""

import argparse
import hashlib
import json
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
    for path in sorted(source.glob("*.md")):
        def replace(match):
            nonlocal substitutions
            raw = match.group(2).strip().strip("<>")
            if urlsplit(raw).scheme or raw.startswith("#"):
                return match.group(0)
            target, sep, anchor = raw.partition("#")
            resolved = (path.parent / unquote(target)).resolve()
            if resolved.is_relative_to(source):
                return match.group(0)
            assert resolved.exists(), resolved
            substitutions += 1
            return f"[{match.group(1)}](<{resolved}{sep}{anchor}>)"
        exported = re.sub(r"\[([^\]\n]*)\]\(([^\)\n]+)\)", replace, path.read_text())
        (output / path.name).write_text(exported)
        source_documents[path.name] = digest(path)
    shutil.copytree(source / "verification", output / "verification", dirs_exist_ok=True)
    shutil.copy2(source / "verification/release-checks.json", output / "verification/canonical-release-checks.json")
    reviews = output / "reviews"
    reviews.mkdir(exist_ok=True)
    for name in ["formal-review-final.md", "editorial-review-final.md", "main-review-direction.md"]:
        shutil.copy2(Path(__file__).parent / name, reviews / name)
    (output / "PACKAGE.md").write_text(f"""# Unified theory reading bundle

Start with [the short guide](START-HERE.md), then read [the full theory](THEORY.md) and [formal core](FORMAL-CORE.md). The [claim register](CLAIMS.md) and [source map](SOURCE-MAP.md) identify what each conclusion rests on. The [synthesis record](SYNTHESIS-RECORD.md) explains integration, verification, and the remaining research frontier.

The theory and proof appendix are self-contained. Source citations outside this package point to the preserved repository on this computer. The archive does not duplicate the 338 MB source snapshot. These citation destinations may need adjustment if the reading bundle is moved to another computer; the manifest records the canonical source location and commit.

The [formal review](reviews/formal-review-final.md), [editorial review](reviews/editorial-review-final.md), and [direction review](reviews/main-review-direction.md) are collaborating AI agents' reviews. The precision edits requested in the editorial review were applied before release. Review is distinct from external peer review and empirical validation.

From the unpacked package directory, the two mathematical check programs run with Python's standard library:

```text
python3 verification/check_integration.py
python3 verification/check_mechanisms.py
python3 verification/check_release.py --local-only
```

The last command checks the exported documents and internal links without requiring the source repository. It replaces the local release-check result; the original canonical record is separately retained in [canonical-release-checks.json](verification/canonical-release-checks.json). [DELIVERY.json](DELIVERY.json) records package file hashes and provenance.

The pre-synthesis checkpoints are `003cd2a` and `38f8022`. The completed integration is committed as `{commit}`. The repository was clean when this bundle was exported.
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
        "external_local_citations_made_absolute": substitutions,
        "files": [{"path": p.relative_to(output).as_posix(), "bytes": p.stat().st_size, "sha256": digest(p)} for p in files],
        "scope": "The synthesis, proofs, internal reviews, independent check programs and records. Source corpus is preserved in the separate committed repository.",
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
