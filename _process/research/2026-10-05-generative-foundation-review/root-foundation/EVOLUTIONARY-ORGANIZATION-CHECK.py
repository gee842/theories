#!/usr/bin/env python3
"""Documentary and preservation checks; does not replace the saved Lean run."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
THEORY = ROOT / "theories/becoming/chapters"
PROOFS = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics"
VERIFY = PROOFS / "developmental-reconstruction-verification"
SOURCE = ROOT / "sources/evolutionary-selection/evolutionary-organization"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edit_path = HERE / "EVOLUTIONARY-ORGANIZATION-INDEX-EDITS.json"
    edits = json.loads(edit_path.read_text())
    docs = [THEORY / "EVOLUTIONARY-ORGANIZATION.md",
            HERE / "EVOLUTIONARY-ORGANIZATION-INTEGRATION.md",
            ROOT / "sources/15-codex-theory-conversations/2026-10-08-evolutionary-organization-completion.md",
            SOURCE / "README.md", VERIFY / "README.md"]
    checked_links = []

    def links(path, text):
        for reference in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", reference):
                continue
            name, _, fragment = reference.partition("#")
            target = (path.parent / unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT) and target.is_file(), (path, reference)
            if fragment and target.suffix == ".md":
                assert unquote(fragment) in chain.heading_ids(target), (path, reference)
            checked_links.append({"from": str(path.relative_to(ROOT)), "reference": reference})

    for path in docs:
        links(path, path.read_text())
    for edit in edits["edits"]:
        path = ROOT / edit["path"]
        assert edit["owned_passage"] in path.read_text(), "Owned insertion changed: " + edit["path"]
        links(path, edit["owned_passage"])
    full = (THEORY / "THE-THEORY-OF-EVOLUTION.md").read_text()
    rows = [line for line in full.splitlines() if line.startswith("| **")]
    assert rows == edits["preserved_six_requirement_rows"] and len(rows) == 6

    manifest = json.loads((SOURCE / "manifest.json").read_text())
    source_bindings = {}
    for item in manifest["files"]:
        path = SOURCE / item["file"]
        assert path.stat().st_size == item["bytes"] and sha(path) == item["sha256"]
        source_bindings[str(path.relative_to(ROOT))] = sha(path)
    reused = manifest["reused_source"]
    assert sha(ROOT / reused["path"]) == reused["sha256"]
    source_bindings[reused["path"]] = reused["sha256"]

    receipt = json.loads((VERIFY / "verification.json").read_text())
    assert receipt["status"] == "passed" and receipt["fresh_temporary_build"]
    assert receipt["source_unchanged_during_check"]
    assert receipt["toolchain"] == "leanprover/lean4:v4.29.1"
    assert receipt["new_theorem_count"] == 20
    assert receipt["new_audit_count"] == 44 and receipt["total_audit_count"] == 113
    assert sha(VERIFY / "check.py") == receipt["checker_sha256"]
    for name, digest in receipt["source_sha256"].items():
        assert sha(VERIFY / "sources" / name) == digest, name
        if name in receipt["source_locations"]:
            assert sha(PROOFS.parent / receipt["source_locations"][name]) == digest, name
        elif name == "lean-toolchain":
            assert sha(PROOFS / name) == digest
    for name, digest in receipt["log_sha256"].items():
        assert sha(VERIFY / name) == digest, name
    actual_count = len(re.findall(r"^theorem\s+", (PROOFS / "DevelopmentalReconstruction.lean").read_text(), re.M))
    assert actual_count == receipt["new_theorem_count"]
    audits = receipt["axiom_dependencies"]
    assert sum(map(len, audits.values())) == 113
    assert len(audits["DevelopmentalReconstruction"]) == 44
    for module in audits.values():
        for dependencies in module.values():
            assert set(dependencies) <= {"propext", "Classical.choice", "Quot.sound"}

    data = chain.read_data()
    entry = next(e for section in data["sections"] for e in section["entries"] if e["id"] == "C14")
    assert "20" in entry["scope_zh"] and "20" in entry["scope_en"]
    for name in edits["chain_update"]["new_link_paths"]:
        assert any(link["path"] == name for link in entry["links"])
        assert data["reviewed_sources"][name] == sha(ROOT / name)
    expected_row = next(line for line in chain.render(data).splitlines() if line.startswith("| C14 |"))
    observed_row = next(line for line in chain.OUTPUT.read_text().splitlines() if line.startswith("| C14 |"))
    assert expected_row == observed_row
    maintenance = (HERE / "GENERATIVITY-CHAIN-INDEX-RECORD.md").read_text()
    assert edits["chain_update"]["maintenance_owned_passage"].strip() in maintenance

    bindings = docs + [edit_path, PROOFS / "DevelopmentalReconstruction.lean",
                       VERIFY / "check.py", VERIFY / "verification.json", SOURCE / "manifest.json"]
    result = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Owned links, source preservation, current Lean receipt bindings, eight owned index insertions, six unchanged broader requirements and the paired C14 row; not a whole-repository certification",
        "local_link_count": len(checked_links), "local_links": checked_links,
        "owned_index_insertions": len(edits["edits"]), "full_theory_requirements_preserved": 6,
        "new_theorem_count": actual_count, "new_audit_count": 44, "total_audit_count": 113,
        "lean_rerun_for_document_only_change": False,
        "source_sha256": source_bindings,
        "artifact_sha256": {str(path.relative_to(ROOT)): sha(path) for path in bindings},
        "C14_matches_paired_data": True,
        "other_entries_preserved_at_edit": edits["chain_update"]["other_entries_preserved"],
        "shared_table_structural_errors": chain.validate(data),
        "shared_table_review_pending": chain.changes(data),
        "shared_full_render_matches": chain.OUTPUT.read_text() == chain.render(data),
        "checker_sha256": sha(Path(__file__)),
    }
    (HERE / "EVOLUTIONARY-ORGANIZATION-CHECKS.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ["status", "local_link_count", "owned_index_insertions", "full_theory_requirements_preserved", "new_theorem_count", "new_audit_count", "total_audit_count", "C14_matches_paired_data", "shared_full_render_matches"]}, indent=2))


if __name__ == "__main__":
    main()
