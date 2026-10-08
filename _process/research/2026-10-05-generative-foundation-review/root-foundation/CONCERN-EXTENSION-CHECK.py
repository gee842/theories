#!/usr/bin/env python3
"""Bind the owned theory, generic proofs and M20 comparison extension.

Source preservation and local checks do not independently accept the philosophy,
its correspondence, or unrelated pending research. No inherited proof rerun.
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
ROOT = HERE.parents[3]
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    output = HERE / "CONCERN-EXTENSION-CHECKS.json"
    edits = json.loads((HERE / "CONCERN-EXTENSION-INDEX-EDITS.json").read_text())
    docs = [HERE / "CONCERN-EXTENSION-INTEGRATION.md",
            ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONCERN-AND-NEW-REASONS.md",
            ROOT / "sources/15-codex-theory-conversations/2026-10-08-concern-expansion-theory.md"]
    passages = [(p, p.read_text()) for p in docs]
    for item in edits["navigation_edits"]:
        path = ROOT / item["path"]
        body = item.get("owned_content", item["new"][len(item["old"]):])
        assert body in path.read_text(), item["path"]
        passages.append((path, body))
    links = []
    for path, body in passages:
        for ref in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            if re.match(r"[a-zA-Z]+:", ref):
                continue
            name, _, fragment = unquote(ref).partition("#")
            target = (path.parent / name).resolve() if name else path
            assert target.is_relative_to(ROOT), (path, ref)
            assert target.is_file() or target == output, (path, ref)
            if fragment and target.suffix == ".md":
                assert fragment in chain.heading_ids(target), (path, ref)
            links.append({"from": str(path.relative_to(ROOT)), "to": ref})
    proof_path = LEAN / "concern-extension-verification.json"
    receipt = json.loads(proof_path.read_text())
    assert receipt["status"] == "passed"
    for name, version in receipt["source_sha256"].items():
        assert digest(LEAN / (name + ".lean")) == version, name
    for name, version in receipt["checker_sha256"].items():
        assert digest(LEAN / name) == version, name
    frozen = LEAN / receipt["retained_run"]
    for name, version in receipt["artifact_sha256"].items():
        assert digest(frozen / name) == version, name
    modules = {m["module"]: m for m in receipt["modules"]}
    new = modules["ConcernExtension"]
    assert new["theorems"] == 8 and len(new["declarations"]) == 9
    assert all(not xs for xs in new["axiom_dependencies"].values())
    assert modules["PracticalJudgment"]["theorems"] == 30
    assert len(modules["PracticalJudgment"]["declarations"]) == 46
    for name, version in edits["concurrent_ethical_learning_preserved"].items():
        assert digest(ROOT / name) == version, name
    for name, version in edits["reviewed_sources"].items():
        assert digest(ROOT / name) == version, name
    data = chain.read_data()
    entry = next(e for section in data["sections"] for e in section["entries"] if e["id"] == "M20")
    assert "新增比较接口" in entry["claim_zh"]
    assert "a new comparison interface" in entry["claim_en"]
    assert all(str(path.relative_to(ROOT)) in data["known_discovery_paths"] for path in docs[:2])
    scoped = copy.deepcopy(data)
    scoped["sections"] = [{"entries": [entry]}]
    assert not chain.validate(scoped), chain.validate(scoped)
    expected = next(line for line in chain.render(data).splitlines() if line.startswith("| M20 |"))
    assert expected in chain.OUTPUT.read_text().splitlines()
    global_checks = []
    for mode in ["--render", "--check"]:
        run = subprocess.run([sys.executable, str(HERE / "build_generative_chain.py"), mode],
                             cwd=ROOT, capture_output=True, text=True, timeout=30)
        global_checks.append({"mode": mode, "exit_code": run.returncode,
                              "stdout": run.stdout, "stderr": run.stderr})
    result = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Owned links, frozen/current proof bindings, concurrent ethical-learning preservation and bilingual M20; no independent philosophical or global research acceptance.",
        "checker_sha256": digest(Path(__file__)),
        "documents": {str(p.relative_to(ROOT)): digest(p) for p in docs},
        "local_links": links,
        "proof_receipt_sha256": digest(proof_path),
        "new_theorems": 8, "new_audits": 9, "new_axiom_dependencies": new["axiom_dependencies"],
        "inherited_theorems": 30, "inherited_audits": 46,
        "concurrent_ethical_learning_preserved": edits["concurrent_ethical_learning_preserved"],
        "paired_row": "M20", "global_checks": global_checks,
        "pending_global_changes": chain.changes(chain.read_data()),
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "passed", "local_links": len(links), "new_theorems": 8,
                      "new_empty_audits": 9, "ethical_learning_preserved": True,
                      "global_exit_codes": [c["exit_code"] for c in global_checks]}))


if __name__ == "__main__":
    main()
