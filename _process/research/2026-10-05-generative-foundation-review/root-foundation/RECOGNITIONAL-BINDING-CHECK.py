#!/usr/bin/env python3
"""Check this continuation's frozen Lean evidence and owned integration only."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/deeper"
THEORY = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATED-LOGIC.md"
SOURCE = ROOT / "sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md"
BEFORE = HERE / "development/recognitional-binding-before"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    helper_path = HERE / "CONTEXTUAL-LOGIC-CHECK.py"
    helper = module("prior_evidence_checker", helper_path)
    proof = LEAN / "recognitional-binding-checks/20261008T120159.334011Z/receipt.json"
    receipt = json.loads(proof.read_text())
    assert receipt["passed"] and receipt["total_empty_axiom_audits"] == 21
    checker = LEAN / "check_recognitional_binding.py"
    assert sha(checker.read_bytes()) == receipt["checker_sha256"]
    expected = {"InferentialGrounds.lean": 10, "GroundRelationTransport.lean": 4,
                "RecognitionalBinding.lean": 7}
    assert [Path(m["source"]).name for m in receipt["modules"]] == list(expected)
    for item in receipt["modules"]:
        source, snapshot = ROOT / item["source"], ROOT / item["snapshot"]
        assert item["passed"] and item["source_unchanged_during_check"] and item["exit_code"] == 0
        assert sha(source.read_bytes()) == sha(snapshot.read_bytes()) == item["sha256"]
        log = (ROOT / item["log"]).read_text()
        assert sha(log.encode()) == item["log_sha256"]
        names = re.findall(r"^#print axioms (\S+)$", source.read_text(), re.M)
        parsed = re.findall(r"'([^']+)' does not depend on any axioms", log)
        assert parsed == item["empty_axiom_audits"]
        assert all(n == q or n.endswith("." + q) for n, q in zip(parsed, names))
        assert len(names) == len(parsed) == len(set(parsed)) == expected[source.name]
        assert "warning:" not in log and "error:" not in log and "depends on axioms" not in log
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b|^\s*(axiom|constant)\s", source.read_text(), re.M)
    assert len(re.findall(r"^theorem ", (LEAN / "RecognitionalBinding.lean").read_text(), re.M)) == 7
    inherited_proof = LEAN / "ground-relation-transport-checks/20261007T231357.510101Z/receipt.json"
    inherited = json.loads(inherited_proof.read_text())
    assert inherited["passed"] and inherited["total_empty_axiom_audits"] == 14
    for new, old in zip(receipt["modules"][:2], inherited["modules"]):
        assert new["source"] == old["source"] and new["sha256"] == old["sha256"]
        assert new["empty_axiom_audits"] == old["empty_axiom_audits"]
        assert sha((ROOT / old["snapshot"]).read_bytes()) == old["sha256"]
        assert sha((ROOT / old["log"]).read_bytes()) == old["log_sha256"]
    totals = dict(all=21, empty=21, new=7, new_empty=7, inherited=14)
    # Earlier source/log snapshots retain their historical scope. Record whether
    # present sources still match, without rewriting another session's files.
    historical = []
    for relative in ["generated-contraction-checks/20261008T101759.536385Z/receipt.json",
                     "contextual-logic-checks/20261008T103742.401003Z/receipt.json",
                     "reconfigurable-logic-checks/20261008T105809.742208Z/receipt.json",
                     "acquired-support-use-checks/20261008T112000.799032Z/receipt.json"]:
        path = LEAN / relative
        old = json.loads(path.read_text())
        assert old["passed"]
        current_matches = {}
        for item in old["modules"]:
            source = ROOT / item["source"]
            frozen = path.parent / "sources" / source.name
            assert sha(frozen.read_bytes()) == item["sha256"]
            log = (path.parent / (source.stem + ".log")).read_text()
            parsed = {n: [] for n in re.findall(r"'([^']+)' does not depend on any axioms", log)}
            parsed.update({n: [x.strip() for x in xs.split(",")]
                           for n, xs in re.findall(r"'([^']+)' depends on axioms: \[(.*?)\]", log, re.S)})
            assert parsed == helper.audits(item)
            current_matches[item["source"]] = sha(source.read_bytes()) == item["sha256"]
        historical.append(dict(receipt=str(path.relative_to(ROOT)), sha256=sha(path.read_bytes()),
                               frozen_sources_and_audits_valid=True, current_source_matches=current_matches))
    previous_proof = LEAN / "reflective-identity-checks/20261008T114343.985843Z/receipt.json"
    previous = json.loads(previous_proof.read_text())
    assert previous["passed"] and previous["exit_code"] == 0
    assert sha((ROOT / previous["snapshot"]).read_bytes()) == previous["source_sha256"]
    assert sha((ROOT / previous["log"]).read_bytes()) == previous["log_sha256"]
    parsed = re.findall(r"'([^']+)' does not depend on any axioms", (ROOT / previous["log"]).read_text())
    assert parsed == previous["empty_axiom_audits"] and len(parsed) == 11
    historical.append(dict(receipt=str(previous_proof.relative_to(ROOT)),
                           sha256=sha(previous_proof.read_bytes()), frozen_sources_and_audits_valid=True,
                           current_source_matches={previous["source"]: sha((ROOT / previous["source"]).read_bytes()) == previous["source_sha256"]}))
    manifest = json.loads((BEFORE / "manifest.json").read_text())
    for item in manifest:
        assert sha((ROOT / item["snapshot"]).read_bytes()) == item["sha256"]
    old_report = json.loads((BEFORE / "REFLECTIVE-IDENTITY-CHECKS.json").read_text())
    for item in manifest:
        if item["path"] in old_report["documents"]:
            assert old_report["documents"][item["path"]] == item["sha256"]
    assert SOURCE.read_bytes().startswith((BEFORE / SOURCE.name).read_bytes())
    assert re.findall(r"^## (\d+)\.", THEORY.read_text(), re.M) == [str(i) for i in range(1, 15)]

    chain = module("chain", HERE / "build_generative_chain.py")
    data = chain.read_data()
    edits = json.loads((HERE / "RECOGNITIONAL-BINDING-INDEX-EDITS.json").read_text())
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "F01")
    assert entry == edits["entry_after"]
    expected = next(x for x in chain.render(data).splitlines() if x.startswith("| F01 |"))
    current = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| F01 |"))
    assert current == expected == edits["new_rendered_row"]
    assert edits["other_entries_preserved"] and edits["other_rendered_lines_preserved"]
    for name, fingerprint in edits["authored_fingerprints"].items():
        assert data["reviewed_sources"][name] == sha((ROOT / name).read_bytes()) == fingerprint
    for item in edits["shared_fragments"]:
        assert (ROOT / item["path"]).read_text().count(item["text"]) == 1
        assert item["insertion_only"]
    assert all(p in data["known_discovery_paths"] for p in edits["owned_discovery_paths"])

    documents = [THEORY, SOURCE, HERE / "RECOGNITIONAL-BINDING-INTEGRATION.md"]
    snippets = [(p, p.read_text()) for p in documents]
    snippets += [(ROOT / f["path"], f["text"]) for f in edits["shared_fragments"]]
    links = []
    for doc, text in snippets:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://")):
                continue
            name, _, anchor = unquote(target).partition("#")
            dest = (doc.parent / name).resolve() if name else doc
            assert dest.is_relative_to(ROOT) and dest.exists(), (doc, target)
            if anchor and dest.suffix == ".md":
                assert anchor in chain.heading_ids(dest), (doc, target)
            links.append(dict(document=str(doc.relative_to(ROOT)), target=target))
    pending = chain.changes(data)
    global_errors = chain.validate(data)
    combined = {}
    if pending["modified_sources"] or pending["missing_sources"]:
        unchanged = chain.OUTPUT.read_bytes()
        for mode in ("--render", "--check"):
            result = subprocess.run([sys.executable, str(HERE / "build_generative_chain.py"), mode],
                                    cwd=ROOT, text=True, capture_output=True)
            assert result.returncode == 2
            combined[mode] = json.loads(result.stdout)
        assert chain.OUTPUT.read_bytes() == unchanged
    report = dict(passed_owned_scope=True, audit_totals=totals,
                  proof_receipt=str(proof.relative_to(ROOT)), proof_sha256=sha(proof.read_bytes()),
                  inherited_receipt=str(inherited_proof.relative_to(ROOT)),
                  inherited_sources_unchanged=True,
                  evidence_helper_sha256=sha(helper_path.read_bytes()), historical_proofs=historical,
                  historical_editions=manifest,
                  documents={str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in documents},
                  local_links=links, paired_entry="F01", owned_edits_preserved=True,
                  pending_shared_reviews=pending, global_link_validation_errors=global_errors,
                  combined_renderer_checks=combined, whole_table_certified=False,
                  independent_agent_review=False, complete_assumption_free_grounding=False)
    (HERE / "RECOGNITIONAL-BINDING-CHECKS.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(passed_owned_scope=True, new_theorems=totals["new"],
                         total_audits=totals["all"], local_links=len(links),
                         pending_shared_sources=len(pending["modified_sources"]),
                         global_link_errors=len(global_errors), whole_table_certified=False)))


if __name__ == "__main__":
    main()
