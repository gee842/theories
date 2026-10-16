#!/usr/bin/env python3
"""Verify owned documentation, row and retained proof bindings; do not rerun science."""
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
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"
THEORY = ROOT / "theories/becoming/chapters"
RESULT = HERE / "CLASSIFICATION-REVISION-CHECKS.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True).encode()


def main():
    RESULT.write_text('{"status":"checking"}\n')
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / "CLASSIFICATION-REVISION-INDEX-EDITS.json").read_text())
    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "M20")
    assert entry == edits["entry_after"], "Owned row changed; review required"
    expected_row = next(x for x in chain.render(data).splitlines() if x.startswith("| M20 |"))
    actual_row = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| M20 |"))
    assert expected_row == actual_row
    for name, expected in edits["owned_reviewed_sources"].items():
        assert digest((ROOT / name).read_bytes()) == expected, name
        assert data["reviewed_sources"][name] == expected, name

    docs = [THEORY / "GOAL-FORMATION-AND-REVISION.md",
            HERE / "CLASSIFICATION-REVISION-INTEGRATION.md",
            ROOT / "sources/15-codex-theory-conversations/2026-10-08-goal-formation-and-revision.md"]
    passages = [(p, p.read_text()) for p in docs]
    fragment_status = {}
    for name, info in edits["shared_fragments"].items():
        p = ROOT / name
        text = p.read_text()
        assert text.count(info["fragment"]) == 1, name
        assert info["other_bytes_preserved"], name
        passages.append((p, info["fragment"]))
        fragment_status[name] = {
            "owned_insertion_present": True,
            "other_bytes_match_insertion_baseline": digest(text.replace(info["fragment"], "", 1).encode()) == info["before_sha256"],
            "full_source_review_refreshed": False,
        }
    local_links = []
    for p, text in passages:
        for reference in re.findall(r"\]\(([^\s)]+)\)", text):
            if re.match(r"[a-zA-Z]+:", reference):
                continue
            name, _, fragment = reference.partition("#")
            target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT) and target.exists(), (p, reference)
            if fragment:
                assert unquote(fragment) in chain.heading_ids(target), (p, reference)
            local_links.append({"from": str(p.relative_to(ROOT)), "reference": reference})
    for link in entry["links"]:
        target, fragment = chain.local_target(link["path"])
        assert target.exists(), link
        if fragment:
            assert fragment in chain.heading_ids(target), link

    receipt = json.loads((LEAN / "classification-revision-verification.json").read_text())
    assert receipt["status"] == "passed" and receipt["source_unchanged_during_check"]
    paths = {"PracticalJudgment": LEAN / "PracticalJudgment.lean",
             "ClassificationRevision": LEAN / "ClassificationRevision.lean"}
    retained = LEAN / receipt["retained_run"]
    for name, expected in receipt["source_sha256"].items():
        assert digest(paths[name].read_bytes()) == expected, name
        assert digest((retained / (name + ".lean")).read_bytes()) == expected, name
    for name, expected in receipt["checker_sha256"].items():
        assert digest((LEAN / name).read_bytes()) == expected, name
    for name, expected in receipt["artifact_sha256"].items():
        assert digest((retained / name).read_bytes()) == expected, name
    modules = {m["module"]: m for m in receipt["modules"]}
    assert modules["ClassificationRevision"]["theorems"] == 16
    assert len(modules["ClassificationRevision"]["declarations"]) == 32
    assert sum(m["theorems"] for k, m in modules.items() if k != "ClassificationRevision") == 30
    assert sum(len(m["declarations"]) for k, m in modules.items() if k != "ClassificationRevision") == 46
    source = paths["ClassificationRevision"].read_text()
    integration = (HERE / "CLASSIFICATION-REVISION-INTEGRATION.md").read_text()
    for name in re.findall(r"`([a-z][a-z_]*_[a-z_]+)`", integration):
        assert re.search(r"\b(?:def|theorem) " + re.escape(name) + r"\b", source) or name in {"decide", "native_decide", "propext"}, name

    others = [e for s in data["sections"] for e in s["entries"] if e["id"] != "M20"]
    other_lines = "".join(x for x in chain.OUTPUT.read_text().splitlines(keepends=True) if not x.startswith("| M20 |"))
    result = {
        "status": "passed", "scope": "Owned integration, M20, local links and frozen Lean source/artifact bindings; no full-table certification or new empirical validation",
        "new_theorems": 16, "new_declaration_audits": 32,
        "inherited_theorems": 30, "inherited_declaration_audits": 46,
        "proof_receipt": str((LEAN / "classification-revision-verification.json").relative_to(ROOT)),
        "retained_artifacts_bound": len(receipt["artifact_sha256"]),
        "local_links_checked": len(local_links), "links": local_links,
        "owned_row_matches_canonical_renderer": True,
        "unrelated_entries_match_edit_baseline": digest(canonical(others)) == edits["unrelated_entries_sha256"],
        "unrelated_table_lines_match_edit_baseline": digest(other_lines.encode()) == edits["other_table_lines_sha256"],
        "shared_fragments": fragment_status,
        "pending_global_review": chain.changes(data),
        "owned_file_sha256": {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in docs + [Path(__file__)]},
        "independent_agent_review": False,
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "new_theorems", "new_declaration_audits", "local_links_checked", "retained_artifacts_bound", "owned_row_matches_canonical_renderer"]}))


if __name__ == "__main__":
    main()
