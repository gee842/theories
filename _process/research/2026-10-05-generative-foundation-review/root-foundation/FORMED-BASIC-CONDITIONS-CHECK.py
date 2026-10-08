#!/usr/bin/env python3
"""Check documentary preservation and the owned M20 continuation only.

No scientific rerun, proof validation, or independent philosophical acceptance.
"""
import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / "FORMED-BASIC-CONDITIONS-INDEX-EDITS.json").read_text())
    receipt = HERE / "FORMED-BASIC-CONDITIONS-CHECKS.json"
    docs = [ROOT / p for p in edits["reviewed_sources"]]
    passages = [(p, p.read_text()) for p in docs]
    for item in edits["navigation_edits"]:
        p = ROOT / item["path"]
        assert item["owned_content"] in p.read_text(), p
        passages.append((p, item["owned_content"]))

    prior = edits["earlier_chapter"]
    chapter = (ROOT / prior["path"]).read_text()
    restored = chapter.replace("\n\n" + prior["inserted_notice"], "", 1)
    restored = restored.split("\n\n" + prior["append_marker"], 1)[0] + "\n"
    assert hashlib.sha256(restored.encode()).hexdigest() == prior["preserved_prior_sha256"]
    for name, version in edits["reviewed_sources"].items():
        assert digest(ROOT / name) == version, name
    for name, version in edits["preservation_window_start"].items():
        assert digest(ROOT / name) == version, name

    links = []
    for path, body in passages:
        for ref in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            if re.match(r"[a-zA-Z]+:", ref):
                continue
            name, _, fragment = unquote(ref).partition("#")
            target = (path.parent / name).resolve() if name else path
            assert target.is_relative_to(ROOT), (path, ref)
            assert target.is_file() or target == receipt, (path, ref)
            if fragment and target.suffix == ".md":
                assert fragment in chain.heading_ids(target), (path, ref)
            links.append({"from": str(path.relative_to(ROOT)), "to": ref})

    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "M20")
    for field, suffix in edits["paired_suffixes"].items():
        assert suffix in entry[field]
        assert entry[field].startswith(edits["entry_before"][field])
    for link in edits["entry_after"]["links"]:
        assert link in entry["links"]
    assert all(p in data["known_discovery_paths"] for p in edits["owned_discovery"])
    for name, version in edits["reviewed_sources"].items():
        assert data["reviewed_sources"][name] == version
    scoped = copy.deepcopy(data)
    scoped["sections"] = [{"entries": [entry]}]
    assert not chain.validate(scoped), chain.validate(scoped)
    row = next(l for l in chain.render(data).splitlines() if l.startswith("| M20 |"))
    assert row in chain.OUTPUT.read_text().splitlines()

    global_checks = []
    for flag in ("--render", "--check"):
        result = subprocess.run([sys.executable, str(HERE / "build_generative_chain.py"), flag],
                                cwd=ROOT, text=True, capture_output=True)
        global_checks.append({"flag": flag, "exit_code": result.returncode,
                              "stdout": result.stdout, "stderr": result.stderr})
    result = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Owned documentary checks only; no new theorem, empirical replication or independent acceptance.",
        "checker_sha256": digest(Path(__file__)),
        "documents": {str(p.relative_to(ROOT)): digest(p) for p in docs},
        "new_theorems": 0, "prior_chapter_preserved": True,
        "local_links": links, "paired_row": "M20",
        "unchanged_during_integration": edits["preservation_window_start"],
        "other_entries_preserved_at_mutation": edits["other_entries_preserved_at_mutation"],
        "global_checks": global_checks,
        "pending_global_changes": chain.changes(chain.read_data()),
    }
    receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "passed", "local_links": len(links),
                      "prior_chapter_preserved": True, "new_theorems": 0,
                      "global_exit_codes": [c["exit_code"] for c in global_checks]}))


if __name__ == "__main__":
    main()
