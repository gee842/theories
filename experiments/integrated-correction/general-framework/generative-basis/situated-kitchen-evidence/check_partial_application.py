#!/usr/bin/env python3
"""Check the owned study's links, frozen proof bindings and paired C23 row.

This is documentary validation. It does not rerun the inherited mathematics or
certify other sessions' pending source reviews or any empirical/ethical claim.
"""
from datetime import datetime, timezone
import copy
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
ROOT = HERE.parents[4]
STUDY = ROOT / "_process/research/2026-10-05-generative-foundation-review/root-foundation"
LEAN = HERE.parent / "lean/universal-ethics/generative-capacity"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", STUDY / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    page = STUDY / "SITUATED-KITCHEN-PARTIAL-INFORMATION.md"
    output = STUDY / "SITUATED-KITCHEN-PARTIAL-CHECKS.json"
    edits = json.loads((STUDY / "SITUATED-KITCHEN-PARTIAL-INDEX-EDITS.json").read_text())
    docs = [page, STUDY / "SITUATED-KITCHEN-EVIDENCE.md"]
    passages = [(p, p.read_text()) for p in docs]
    # Validate the full owned study and source application, plus only the owned
    # inserted navigation passages in shared files.
    for item in edits["navigation_edits"]:
        path = ROOT / item["path"]
        assert item["new"] in path.read_text(), item["path"]
        if path not in docs:
            passages.append((path, item["new"]))
    checked_links = []
    for path, body in passages:
        for ref in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            if re.match(r"[a-zA-Z]+:", ref):
                continue
            name, _, fragment = unquote(ref).partition("#")
            target = (path.parent / name).resolve() if name else path
            assert target.is_relative_to(ROOT) and (target.is_file() or target == output), (path, ref)
            if fragment and target.suffix == ".md":
                assert fragment in chain.heading_ids(target), (path, ref)
            checked_links.append({"from": str(path.relative_to(ROOT)), "to": ref})
    new = json.loads((LEAN / "kitchen-transitions-verification.json").read_text())
    assert new["status"] == "passed"
    assert new["source_sha256"]["KitchenTransitions"] == digest(LEAN / "KitchenTransitions.lean")
    assert len(new["modules"]) == 1
    module = new["modules"][0]
    assert module["theorems"] == 7 and len(module["declarations"]) == 12
    retained = LEAN / new["retained_run"]
    for name, expected in new["artifact_sha256"].items():
        assert digest(retained / name) == expected, name
    for name, expected in new["checker_sha256"].items():
        assert digest(LEAN / name) == expected, name
    inherited = json.loads((LEAN / "situated-kitchen-verification.json").read_text())
    assert inherited["status"] == "passed"
    for name, expected in inherited["source_sha256"].items():
        assert digest(LEAN / (name + ".lean")) == expected, name
    empirical = json.loads((HERE / "transition-checks.json").read_text())
    assert empirical["status"] == "passed"
    assert empirical["source_sha256"] == digest(ROOT / "sources/community-kitchen-evidence/sahyoun-2019.xml")
    assert empirical["checker_sha256"] == digest(HERE / "check_transitions.py")
    assert empirical["lean_verification_sha256"] == digest(LEAN / "kitchen-transitions-verification.json")
    assert len(empirical["binary_tables"]) == 14
    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "C23")
    assert entry == edits["after"]
    scoped = copy.deepcopy(data)
    scoped["sections"] = [{"entries": [entry]}]
    assert not chain.validate(scoped), chain.validate(scoped)
    expected_row = next(row for row in chain.render(data).splitlines() if row.startswith("| C23 |"))
    actual_row = next(row for row in chain.OUTPUT.read_text().splitlines() if row.startswith("| C23 |"))
    assert expected_row == actual_row
    for name, version in edits["reviewed_sources"].items():
        assert digest(ROOT / name) == version == data["reviewed_sources"][name], name
    assert all(name in data["known_discovery_paths"] for name in edits["discovery_added"])
    # Attempt the maintained full renderer/checker as required, preserving its
    # pending-review result rather than stamping concurrent changes as reviewed.
    global_checks = []
    for mode in ["--render", "--check"]:
        process = subprocess.run([sys.executable, str(STUDY / "build_generative_chain.py"), mode],
                                 cwd=ROOT, capture_output=True, text=True, timeout=30)
        global_checks.append({"mode": mode, "exit_code": process.returncode,
                              "stdout": process.stdout, "stderr": process.stderr})
    result = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Owned documentary links, source/receipt bindings and paired row; concurrent table status is separate.",
        "checker_sha256": digest(Path(__file__)),
        "new_lean_theorems": 7, "new_explicit_declaration_audits": 12,
        "new_axiom_dependencies": module["axiom_dependencies"],
        "inherited_sources_unchanged": list(inherited["source_sha256"]),
        "anonymous_tables": 14, "checked_local_links": checked_links,
        "paired_row": "C23", "reviewed_sources": edits["reviewed_sources"],
        "global_checks": global_checks, "pending_global_changes": chain.changes(chain.read_data()),
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    assert output.is_file() and json.loads(output.read_text())["status"] == "passed"
    print(json.dumps({"status": "passed", "links": len(checked_links), "theorems": 7, "audits": 12,
                      "source_bound_tables": 14, "row": "C23", "global_exit_codes": [r["exit_code"] for r in global_checks]}))


if __name__ == "__main__":
    main()
