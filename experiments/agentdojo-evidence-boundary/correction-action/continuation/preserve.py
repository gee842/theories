"""Preserve all completed case bytes, deduplicating declared repository inputs.

This is provenance, not a scientific checker or complete host-activity record.
Cases JSON is a list of {id, case_dir}. Run only after the episodes are terminal.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PARENT = HERE.parents[1]
SOURCE = ROOT / "sources/28-agentdojo-evidence-2026-10-06"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def original_lookup() -> dict:
    paths = [p for p in SOURCE.rglob("*") if p.is_file()]
    paths += [p for p in PARENT.iterdir() if p.is_file()]
    paths += [p for p in (PARENT / "review-history/counterparty-uniqueness").iterdir() if p.is_file()]
    result = {}
    for path in sorted(paths):
        if path.is_symlink():
            raise ValueError(f"Unexpected source symlink: {path}")
        result.setdefault(digest(path), str(path.relative_to(ROOT)))
    return result


def preserve(cases_file: Path) -> dict:
    destination = HERE / "preservation.json"
    if destination.exists():
        raise ValueError("Refusing to replace a preservation record")
    cases = json.loads(cases_file.read_text())
    original = original_lookup()
    blobs, cases_out = {}, []
    for case in cases:
        base = Path(case["case_dir"]).resolve()
        assert base.is_dir() and not base.is_relative_to(ROOT)
        records = {}
        for path in sorted(base.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Unexpected case symlink: {path}")
            if not path.is_file():
                continue
            sha = digest(path)
            if sha in original:
                location = {"kind": "repository_bytes", "path": original[sha]}
            else:
                blob = HERE / "preserved/sha256" / sha
                if not blob.exists():
                    blob.parent.mkdir(parents=True, exist_ok=True)
                    blob.write_bytes(path.read_bytes())
                assert digest(blob) == sha
                location = {"kind": "preserved_bytes", "path": str(blob.relative_to(ROOT))}
                blobs[sha] = {"path": location["path"], "bytes": path.stat().st_size}
            records[str(path.relative_to(base))] = {
                "sha256": sha, "bytes": path.stat().st_size, **location,
            }
        cases_out.append({"id": case["id"], "case_dir_at_capture": str(base), "files": records})
    result = {
        "schema_version": 1,
        "scope": "All regular case files at terminal capture; not complete native operation history",
        "repository_bytes_meaning": "Byte-identical reconstruction reference, not an independent source or a claim of causal execution",
        "cases_file": str(cases_file.resolve()),
        "cases_file_sha256": digest(cases_file),
        "preserver_sha256": digest(Path(__file__)),
        "cases": cases_out,
        "unique_preserved_blobs": blobs,
    }
    dump(destination, result)
    return verify(destination)


def verify(path: Path) -> dict:
    record = json.loads(path.read_text())
    seen, count = {}, 0
    for case in record["cases"]:
        for relative, entry in case["files"].items():
            assert not Path(relative).is_absolute() and ".." not in Path(relative).parts
            target = ROOT / entry["path"]
            assert target.resolve().is_relative_to(ROOT)
            if entry["path"] not in seen:
                seen[entry["path"]] = (digest(target), target.stat().st_size)
            assert seen[entry["path"]] == (entry["sha256"], entry["bytes"]), entry["path"]
            count += 1
    return {"status": "preserved_bytes_verified", "cases": len(record["cases"]),
            "case_file_references": count, "distinct_stored_paths": len(seen),
            "unique_new_blobs": len(record["unique_preserved_blobs"]),
            "preservation_sha256": digest(path)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases-json", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    if bool(args.cases_json) == bool(args.verify):
        parser.error("Choose exactly one of --cases-json or --verify")
    print(json.dumps(verify(args.verify) if args.verify else preserve(args.cases_json), indent=2))
