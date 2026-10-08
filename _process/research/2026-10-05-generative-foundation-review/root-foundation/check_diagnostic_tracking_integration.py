#!/usr/bin/env python3
"""Check owned diagnostic-tracking integration and bind all three checked Lean modules."""
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESULT = HERE / "DIAGNOSTIC-TRACKING-CHECKS.json"
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True).encode()


def main():
    RESULT.write_text('{"status":"checking"}\n')
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / "DIAGNOSTIC-TRACKING-INDEX-EDITS.json").read_text())
    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "M20")
    for key, suffix in edits["owned_suffixes"].items():
        assert entry[key].count(suffix) == 1, key
        assert edits["entry_before"][key] + suffix == edits["entry_after"][key]
    for link in edits["entry_before"]["links"] + edits["added_links"]:
        assert link in entry["links"], link
    expected = next(x for x in chain.render(data).splitlines() if x.startswith("| M20 |"))
    actual = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| M20 |"))
    assert actual == expected

    passages = []
    for name, fingerprint in edits["owned_reviewed_sources"].items():
        p = ROOT / name
        assert digest(p.read_bytes()) == fingerprint, name
        assert data["reviewed_sources"][name] == fingerprint, name
        if name in edits["prior_content"]:
            info = edits["prior_content"][name]
            assert p.read_text().count(info["addition"]) == 1
            old = p.read_text().replace(info["addition"], "", 1)
            assert digest(old.encode()) == info["prior_sha256"], name
            passages.append((p, info["addition"]))
        elif p.suffix == ".md":
            passages.append((p, p.read_text()))
    for name, info in edits["shared_fragments"].items():
        p = ROOT / name
        assert p.read_text().count(info["fragment"]) == 1, name
        assert info["other_bytes_preserved"]
        passages.append((p, info["fragment"]))
    for name in edits["added_discovery_paths"]:
        assert name in data["known_discovery_paths"] and (ROOT / name).exists()

    links = []
    for p, passage in passages:
        for reference in re.findall(r"\]\(([^\s)]+)\)", passage):
            if re.match(r"[a-zA-Z]+:", reference):
                continue
            name, _, fragment = reference.partition("#")
            target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT) and target.exists(), (p, reference)
            if fragment:
                assert unquote(fragment) in chain.heading_ids(target), (p, reference)
            links.append({"from": str(p.relative_to(ROOT)), "reference": reference})
    for link in edits["added_links"]:
        p, fragment = chain.local_target(link["path"])
        assert p.exists() and (not fragment or fragment in chain.heading_ids(p)), link

    receipt = json.loads((LEAN / "diagnostic-tracking-verification.json").read_text())
    assert receipt["status"] == "passed" and receipt["source_unchanged_during_check"]
    retained = LEAN / receipt["retained_run"]
    for name, fingerprint in receipt["source_sha256"].items():
        assert digest((LEAN / (name + ".lean")).read_bytes()) == fingerprint
        assert digest((retained / (name + ".lean")).read_bytes()) == fingerprint
    for name, fingerprint in receipt["checker_sha256"].items():
        helper = Path(receipt["support_source"]) if name == "declaration_audit_support.py" else LEAN / name
        assert helper.is_relative_to(ROOT)
        assert digest(helper.read_bytes()) == fingerprint
    for name, fingerprint in receipt["artifact_sha256"].items():
        assert digest((retained / name).read_bytes()) == fingerprint, name
    assert len(receipt["modules"]) == 3
    model = next(m for m in receipt["modules"] if m["module"] == "DiagnosticTracking")
    inherited = [m for m in receipt["modules"] if m["module"] != "DiagnosticTracking"]
    assert model["kernel_checked"] and all(m["kernel_checked"] for m in inherited)
    assert model["theorems"] == 17 and len(model["declarations"]) == 21
    assert [(m["module"], m["theorems"], len(m["declarations"])) for m in inherited] == [
        ("SituatedTracking", 15, 19), ("ActionAwareTracking", 17, 22)]
    previous = json.loads((LEAN / "action-aware-tracking-verification.json").read_text())
    assert previous["status"] == "passed"
    for m in inherited:
        name = m["module"]
        assert previous["source_sha256"][name] == receipt["source_sha256"][name]
        assert Counter(tuple(a) for a in m["axiom_dependencies"].values()) == Counter({
            ("propext", "Classical.choice", "Quot.sound"): len(m["declarations"])})
    dependencies = Counter(tuple(a) for a in model["axiom_dependencies"].values())
    assert dependencies == Counter({("propext", "Classical.choice", "Quot.sound"): 21})
    signatures = (retained / "DiagnosticTrackingSignatures.log").read_text()
    theorem_names = [d["name"] for d in model["declarations"] if d["kind"] == "theorem"]
    assert len(theorem_names) == 17
    for name in theorem_names:
        assert name in signatures
    for name, fingerprint in receipt["direct_import_sha256"].items():
        assert digest(Path(name).read_bytes()) == fingerprint
    assert receipt["mathlib_revision"] == "ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa"
    assert not receipt["upstream_rebuilt"] and receipt["inherited_project_theorems_rebuilt"] == 32
    assert len(receipt["artifact_sha256"]) == 22
    assert (retained / "verification.json").read_bytes() == (LEAN / "diagnostic-tracking-verification.json").read_bytes()

    others = [e for s in data["sections"] for e in s["entries"] if e["id"] != "M20"]
    other_lines = "".join(x for x in chain.OUTPUT.read_text().splitlines(keepends=True)
                          if not x.startswith("| M20 |"))
    result = {
        "status": "passed", "scope": edits["scope"], "new_theorems": 17,
        "new_explicit_declaration_audits": 21, "inherited_project_theorems": 32,
        "inherited_explicit_declaration_audits": 41,
        "axiom_audits": [{"dependencies": list(k), "declarations": v} for k, v in dependencies.items()],
        "retained_proof_artifacts_bound": len(receipt["artifact_sha256"]),
        "prior_documents_preserved": len(edits["prior_content"]),
        "owned_M20_additions_and_renderer_match": True,
        "other_entries_preserved_at_mutation": edits["other_entries_preserved_at_mutation"],
        "unrelated_entries_match_edit_baseline": digest(canonical(others)) == edits["unrelated_entries_sha256"],
        "other_table_lines_match_edit_baseline": digest(other_lines.encode()) == edits["other_table_lines_sha256"],
        "local_links_checked": len(links), "links": links,
        "source_sha256": edits["owned_reviewed_sources"],
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "pending_global_review": chain.changes(data),
        "new_independent_review": False, "new_empirical_validation": False,
        "complete_situational_awareness_certified": False,
        "empirical_calibration_certified": False, "arbitrary_concept_formation_certified": False,
        "ethical_risk_limit_certified": False, "inevitable_goal_convergence_certified": False,
        "whole_table_certified": False,
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "new_theorems", "new_explicit_declaration_audits",
                                            "prior_documents_preserved", "local_links_checked",
                                            "retained_proof_artifacts_bound"]}))


if __name__ == "__main__":
    main()
