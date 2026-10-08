#!/usr/bin/env python3
"""Verify owned comparison artifacts and receipt bindings, not global freshness."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASIS = ROOT / "experiments/integrated-correction/general-framework/generative-basis"
PROOFS = BASIS / "lean/universal-ethics"
VERIFY = PROOFS / "evolution-network-comparison-verification"
EXECUTE = BASIS / "ecological-selection/network-comparison"
SOURCES = ROOT / "sources/evolutionary-selection/comparative-direction"
OUT = HERE / "EVOLUTION-NETWORK-COMPARISON-CHECKS.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits_path = HERE / "EVOLUTION-NETWORK-COMPARISON-INDEX-EDITS.json"
    edits = json.loads(edits_path.read_text())
    documents = [HERE / "EVOLUTION-NETWORK-COMPARISON.md", HERE / "EVOLUTION-COMPARISON-PROTOCOL.md",
                 SOURCES / "README.md", EXECUTE / "README.md", VERIFY / "README.md",
                 ROOT / "sources/15-codex-theory-conversations/2026-10-08-evolution-connectionism-comparison.md"]
    checked_links = []

    def check_links(path, content):
        for ref in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", ref):
                continue
            name, _, anchor = ref.partition("#")
            target = (path.parent / unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT)
            assert target.is_file() or target == OUT, (path, ref)
            if anchor and target.suffix == ".md":
                assert unquote(anchor) in chain.heading_ids(target), (path, ref)
            checked_links.append({"from": str(path.relative_to(ROOT)), "reference": ref})

    for path in documents:
        check_links(path, path.read_text())
    for edit in edits["edits"]:
        path = ROOT / edit["path"]
        assert edit["owned_passage"] in path.read_text(), edit["path"]
        check_links(path, edit["owned_passage"])
    full = ROOT / "theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md"
    assert [s for s in full.read_text().splitlines() if s.startswith("| **")] == edits["preserved_six_requirement_rows"]
    assert len(edits["preserved_six_requirement_rows"]) == 6

    proof = json.loads((VERIFY / "verification.json").read_text())
    assert proof["status"] == "passed" and proof["fresh_temporary_build"] and proof["source_unchanged_during_check"]
    assert (proof["new_theorem_count"], proof["new_audit_count"], proof["total_audit_count"]) == (11, 24, 137)
    assert proof["checker_sha256"] == sha(VERIFY / "check.py")
    assert proof["toolchain"] == "leanprover/lean4:v4.29.1"
    for name, expected in proof["source_sha256"].items():
        assert sha(VERIFY / "sources" / name) == expected, name
        if name in proof["source_locations"]:
            assert sha(PROOFS.parent / proof["source_locations"][name]) == expected, name
        elif name == "lean-toolchain":
            assert sha(PROOFS / name) == expected
    for name, expected in proof["log_sha256"].items():
        assert sha(VERIFY / name) == expected, name
    for module in proof["axiom_dependencies"].values():
        for dependencies in module.values():
            assert set(dependencies) <= {"propext", "Quot.sound", "Classical.choice"}
    prior = json.loads((PROOFS / "developmental-reconstruction-verification/verification.json").read_text())
    for name in ("GenerativeCore.lean", "DevelopmentalAssociation.lean", "DevelopmentalReconstruction.lean"):
        assert proof["source_sha256"][name] == prior["source_sha256"][name], name

    code = (PROOFS / "EvolutionNetworkComparison.lean").read_text()
    assert len(re.findall(r"^theorem\s+", code, re.M)) == 11
    for name in ("reaction", "developmentalRun", "sample", "transition", "history", "adaptiveNetwork"):
        match = re.search(r"^def " + name + r"\b.*?(?=^(?:def|theorem|end)\b|\Z)", code, re.S | re.M)
        assert match
        body = re.sub(r"/-.*?-/|--[^\n]*", "", match.group(), flags=re.S)
        assert not re.search(r"DevelopmentalAssociation\.(?:divide|changeRetention|detach|aggregate|step|run)\b|DevelopmentalReconstruction\.(?:transfer|develop|step|run)\b", body), name

    execution = json.loads((EXECUTE / "verification.json").read_text())
    assert execution["status"] == "passed" and execution["mismatches"] == 0
    assert execution["cases"] == {"bounded": 18768, "history_failure": 8000, "history_success": 8000}
    assert execution["successful_outcomes"] + execution["disabled_outcomes"] == 34768
    assert execution["maximum_history_length"] == 80 and execution["seed"] == 20261008
    assert execution["fitted_parameters_each"] == execution["new_biological_observations"] == 0
    assert execution["checker_sha256"] == sha(EXECUTE / "check.py")
    assert execution["protocol_sha256"] == sha(HERE / "EVOLUTION-COMPARISON-PROTOCOL.md")
    for name, expected in execution["source_sha256"].items():
        if name == "Driver.lean":
            assert sha(EXECUTE / name) == expected
        else:
            assert proof["source_sha256"][name] == expected

    manifest = json.loads((SOURCES / "connectionism-manifest.json").read_text())
    for record in manifest["files"]:
        path = SOURCES / record["file"]
        assert path.stat().st_size == record["bytes"] and sha(path) == record["sha256"]
    data = chain.read_data()
    entry = next(e for section in data["sections"] for e in section["entries"] if e["id"] == "C14")
    assert "34,768" in entry["scope_en"] and "34,768" in entry["scope_zh"]
    assert any(link["path"] == edits["chain_update"]["new_link_path"] for link in entry["links"])
    for name in edits["chain_update"]["reviewed_sources"]:
        assert data["reviewed_sources"][name] == sha(ROOT / name), name
    expected_row = next(s for s in chain.render(data).splitlines() if s.startswith("| C14 |"))
    actual_row = next(s for s in chain.OUTPUT.read_text().splitlines() if s.startswith("| C14 |"))
    assert actual_row == expected_row
    assert not chain.validate(data)
    artifact_paths = documents + [edits_path, PROOFS / "EvolutionNetworkComparison.lean",
        VERIFY / "verification.json", VERIFY / "check.py", EXECUTE / "verification.json",
        EXECUTE / "check.py", EXECUTE / "Driver.lean", SOURCES / "connectionism-manifest.json"]
    receipt = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Owned links, frozen proof/execution bindings, unchanged inherited mechanism, paired C14 and six unchanged completion requirements; not global source review",
        "local_link_count": len(checked_links), "local_links": checked_links,
        "owned_index_edits": len(edits["edits"]), "full_completion_requirements_preserved": 6,
        "new_theorems": 11, "new_declaration_audits": 24, "executed_cases": 34768,
        "operative_definitions_do_not_call_original_transitions": True,
        "inherited_mechanism_sources_unchanged": True, "C14_matches_paired_data": True,
        "other_entries_preserved_at_edit": edits["chain_update"]["other_entries_preserved"],
        "shared_review_pending": chain.changes(data),
        "shared_full_render_matches": chain.OUTPUT.read_text() == chain.render(data),
        "artifact_sha256": {str(p.relative_to(ROOT)): sha(p) for p in artifact_paths},
        "checker_sha256": sha(Path(__file__)),
    }
    OUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in ("status", "local_link_count", "owned_index_edits", "full_completion_requirements_preserved", "new_theorems", "executed_cases", "C14_matches_paired_data", "shared_full_render_matches")}, indent=2))


if __name__ == "__main__":
    main()
