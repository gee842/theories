#!/usr/bin/env python3
"""Check owned bounded-risk revision integration and bind its two-module Lean receipt."""
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
RESULT = HERE / "BOUNDED-RISK-REVISION-CHECKS.json"
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True).encode()


def main():
    RESULT.write_text('{"status":"checking"}\n')
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / "BOUNDED-RISK-REVISION-INDEX-EDITS.json").read_text())
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

    receipt = json.loads((LEAN / "bounded-risk-revision-verification.json").read_text())
    assert receipt["status"] == "passed" and receipt["source_unchanged_during_check"]
    retained = LEAN / receipt["retained_run"]
    for name, fingerprint in receipt["source_sha256"].items():
        assert digest((LEAN / (name + ".lean")).read_bytes()) == fingerprint
        assert digest((retained / (name + ".lean")).read_bytes()) == fingerprint
    for name, fingerprint in receipt["checker_sha256"].items():
        assert digest((LEAN / name).read_bytes()) == fingerprint
    for name, fingerprint in receipt["artifact_sha256"].items():
        assert digest((retained / name).read_bytes()) == fingerprint, name
    assert len(receipt["modules"]) == 2
    model = next(m for m in receipt["modules"] if m["module"] == "BoundedRiskRevision")
    inherited = next(m for m in receipt["modules"] if m["module"] == "BasicRiskSharing")
    assert model["kernel_checked"] and inherited["kernel_checked"]
    assert model["theorems"] == 9 and len(model["declarations"]) == 13
    assert inherited["theorems"] == 19 and len(inherited["declarations"]) == 36
    inherited_dependencies = Counter(tuple(a) for a in inherited["axiom_dependencies"].values())
    assert inherited_dependencies == Counter({(): 25, ("propext", "Classical.choice", "Quot.sound"): 8,
                                              ("propext", "Quot.sound"): 3})
    dependencies = Counter(tuple(a) for a in model["axiom_dependencies"].values())
    assert dependencies == Counter({(): 6, ("propext", "Classical.choice", "Quot.sound"): 4,
                                    ("propext", "Quot.sound"): 3})
    signatures = (retained / "BoundedRiskRevisionSignatures.log").read_text()
    for name in ["greatest_on_frontier", "dominated_beyond_balance",
                 "no_joint_improvement_on_frontier", "frontier_exact",
                 "intermediate_profiles", "whole_allowance_iff",
                 "four_point_constraint_optimum", "scope_bounds_compose",
                 "resetting_allowance_exceeds_original_scope"]:
        assert "BoundedRiskRevision." + name in signatures
    assert len(receipt["artifact_sha256"]) == 15
    assert (retained / "verification.json").read_bytes() == (LEAN / "bounded-risk-revision-verification.json").read_bytes()

    others = [e for s in data["sections"] for e in s["entries"] if e["id"] != "M20"]
    other_lines = "".join(x for x in chain.OUTPUT.read_text().splitlines(keepends=True)
                          if not x.startswith("| M20 |"))
    result = {
        "status": "passed", "scope": edits["scope"], "new_theorems": 9,
        "new_explicit_declaration_audits": 13, "inherited_project_theorems": 19,
        "inherited_explicit_declaration_audits": 36,
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
        "ethical_risk_allowance_certified": False, "RSL_normative_warrant_proved_by_Lean": False,
        "whole_table_certified": False,
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "new_theorems", "new_explicit_declaration_audits",
                                            "prior_documents_preserved", "local_links_checked",
                                            "retained_proof_artifacts_bound"]}))


if __name__ == "__main__":
    main()
