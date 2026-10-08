#!/usr/bin/env python3
"""Check documentary preservation and the owned M20 continuation only.

Binds the actual retained proof run without a scientific rerun or independent acceptance.
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
    edits = json.loads((HERE / "RISK-CONDITIONING-INDEX-EDITS.json").read_text())
    receipt = HERE / "RISK-CONDITIONING-CHECKS.json"
    docs = [ROOT / p for p in edits["documents"]]
    passages = [(p, p.read_text()) for p in docs]
    for item in edits["navigation_edits"]:
        p = ROOT / item["path"]
        assert item["owned_content"] in p.read_text(), p
        passages.append((p, item["owned_content"]))

    for item in edits["navigation_edits"]:
        path = ROOT / item["path"]
        # At mutation, removing the exact owned insertion recovered all prior bytes.
        assert item["other_content_preserved"]
    assert edits["other_rendered_lines_preserved_at_mutation"]
    chapter = docs[0].read_text()
    notice = edits["chapter_notice"]
    assert chapter.count(notice) == 1
    without = chapter.replace(notice + "\n\n", "", 1)
    prefix = without[:edits["chapter_prior_length"]]
    assert hashlib.sha256(prefix.encode()).hexdigest() == edits["chapter_prior_prefix_sha256"]
    assert edits["chapter_prior_prefix_preserved"]
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

    proof_path = ROOT / edits["proof_receipt"]
    proof = json.loads(proof_path.read_text())
    assert proof["status"] == "passed" and proof["kernel_checked"]
    assert proof["new_theorems"] == 10 and proof["declaration_audits"] == 21
    assert all(set(deps) <= {"propext", "Quot.sound", "Classical.choice"} for deps in proof["axiom_dependencies"].values())
    assert sum(not deps for deps in proof["axiom_dependencies"].values()) == 16
    assert digest(proof_path.parent / "RiskConditioning.lean") == proof["source_sha256"]
    for name, version in proof["checker_sha256"].items():
        assert digest(proof_path.parent / name) == version, name
    retained = proof_path.parent / proof["retained_run"]
    assert json.loads((retained / "verification.json").read_text()) == proof
    for name, version in proof["artifact_sha256"].items():
        assert digest(retained / name) == version, name

    global_checks = []
    for flag in ("--render", "--check"):
        result = subprocess.run([sys.executable, str(HERE / "build_generative_chain.py"), flag],
                                cwd=ROOT, text=True, capture_output=True)
        global_checks.append({"flag": flag, "exit_code": result.returncode,
                              "stdout": result.stdout, "stderr": result.stderr})
    result = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Owned documentary and frozen-proof binding checks; actual mathematical validation is recorded in the linked Lean receipt. No new empirical replication or independent acceptance.",
        "checker_sha256": digest(Path(__file__)),
        "documents": {str(p.relative_to(ROOT)): digest(p) for p in docs},
        "new_theorems": 10, "declaration_audits": 21, "prior_content_preserved_at_mutation": True,
        "local_links": links, "paired_row": "M20",
        "unchanged_during_integration": edits["preservation_window_start"],
        "other_entries_preserved_at_mutation": edits["other_entries_preserved_at_mutation"],
        "proof_receipt": edits["proof_receipt"], "proof_receipt_sha256": digest(proof_path),
        "global_checks": global_checks,
        "pending_global_changes": chain.changes(chain.read_data()),
    }
    receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "passed", "local_links": len(links),
                      "prior_content_preserved_at_mutation": True, "new_theorems": 10, "declaration_audits": 21,
                      "global_exit_codes": [c["exit_code"] for c in global_checks]}))


if __name__ == "__main__":
    main()
