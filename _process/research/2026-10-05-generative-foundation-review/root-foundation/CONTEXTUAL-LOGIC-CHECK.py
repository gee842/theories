#!/usr/bin/env python3
"""Validate frozen evidence and this continuation's owned integration.

Does not rerun Lean, refresh unread sources, or certify the whole shared table.
The first pilot's documentary receipt remains tied to its preserved editions.
"""
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
BEFORE = HERE / "development/contextual-logic-before"
NEW = {"ContextualLeaseRules.lean", "ContextualLogicAbstraction.lean"}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def audits(item):
    if "axiom_audits" in item:
        return item["axiom_audits"]
    result = {name: [] for name in item["empty_axiom_audits"]}
    assert not (result.keys() & item["standard_axiom_audits"].keys())
    result.update(item["standard_axiom_audits"])
    return result


def check_receipt(path, checker, new_names):
    receipt = json.loads(path.read_text())
    assert receipt["passed"]
    assert sha(checker.read_bytes()) == receipt["checker_sha256"]
    totals = dict(all=0, empty=0, new=0, new_empty=0)
    for item in receipt["modules"]:
        source = ROOT / item["source"]
        frozen = path.parent / "sources" / source.name
        assert item["passed"] and item["source_unchanged_during_check"]
        assert sha(source.read_bytes()) == sha(frozen.read_bytes()) == item["sha256"]
        recorded = audits(item)
        names = re.findall(r"^#print axioms (\S+)$", source.read_text(), re.M)
        assert set(names) == set(recorded) and len(names) == len(recorded)
        log = (path.parent / (source.stem + ".log")).read_text()
        parsed = {n: [] for n in re.findall(r"'([^']+)' does not depend on any axioms", log)}
        parsed.update({n: [x.strip() for x in xs.split(",")]
                       for n, xs in re.findall(r"'([^']+)' depends on axioms: \[(.*?)\]", log, re.S)})
        assert parsed == recorded
        assert all(set(xs) <= {"propext", "Quot.sound", "Classical.choice"}
                   for xs in recorded.values())
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b|^\s*(axiom|constant)\s",
                             source.read_text(), re.M)
        totals["all"] += len(recorded)
        totals["empty"] += sum(not xs for xs in recorded.values())
        if source.name in new_names:
            assert len(re.findall(r"^theorem ", source.read_text(), re.M)) == len(recorded)
            assert all("Classical.choice" not in xs for xs in recorded.values())
            totals["new"] += len(recorded)
            totals["new_empty"] += sum(not xs for xs in recorded.values())
    return receipt, totals


def main():
    proof = LEAN / "contextual-logic-checks/20261008T103742.401003Z/receipt.json"
    receipt, totals = check_receipt(proof, LEAN / "check_contextual_logic.py", NEW)
    assert totals == {"all": 220, "empty": 124, "new": 37, "new_empty": 12}
    old = LEAN / "generated-contraction-checks/20261008T101759.536385Z/receipt.json"
    _, old_totals = check_receipt(old, LEAN / "check_generated_contraction.py",
                                  {"GeneratedContraction.lean", "ContractionMechanisms.lean"})
    assert old_totals == {"all": 65, "empty": 51, "new": 38, "new_empty": 24}

    baseline = LEAN / "explanatory-jointness-checks/20261008T082735.042695Z/receipt.json"
    base = json.loads(baseline.read_text())
    inherited = [m for m in receipt["modules"] if Path(m["source"]).name not in NEW]
    by_name = {m["source"]: m for m in base["modules"]}
    assert len(inherited) == len(by_name) == 12
    comparison = []
    for item in inherited:
        former = by_name[item["source"]]
        row = dict(source=item["source"], same_source=item["sha256"] == former["sha256"],
                   same_empty_audits=item["empty_axiom_audits"] == former["empty_axiom_audits"],
                   same_standard_audits=item["standard_axiom_audits"] == former["standard_axiom_audits"])
        assert all(value is True for key, value in row.items() if key != "source")
        comparison.append(row)
    assert comparison == json.loads((BEFORE / "inherited-proof-comparison.json").read_text())

    first_edits = json.loads((HERE / "GENERATED-LOGIC-INDEX-EDITS.json").read_text())
    manifest = json.loads((BEFORE / "manifest.json").read_text())
    for item in manifest:
        assert sha((ROOT / item["snapshot"]).read_bytes()) == item["sha256"]
        assert first_edits["authored_fingerprints"][item["path"]] == item["sha256"]
    assert SOURCE.read_bytes().startswith((BEFORE / SOURCE.name).read_bytes())
    assert re.findall(r"^## (\d+)\.", THEORY.read_text(), re.M) == [str(i) for i in range(1, 11)]

    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    data = chain.read_data()
    edits = json.loads((HERE / "CONTEXTUAL-LOGIC-INDEX-EDITS.json").read_text())
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "F01")
    assert entry == edits["entry_after"]
    current = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| F01 |"))
    expected = next(x for x in chain.render(data).splitlines() if x.startswith("| F01 |"))
    assert current == expected == edits["new_rendered_row"]
    assert edits["other_entries_preserved"] and edits["other_rendered_lines_preserved"]
    for name, digest in edits["authored_fingerprints"].items():
        assert data["reviewed_sources"][name] == sha((ROOT / name).read_bytes()) == digest
    for fragment in edits["shared_fragments"]:
        assert (ROOT / fragment["path"]).read_text().count(fragment["text"]) == 1
        assert fragment["insertion_only"]
    assert all(p in data["known_discovery_paths"] for p in edits["owned_discovery_paths"])

    documents = [THEORY, SOURCE, HERE / "GENERATED-LOGIC-INTEGRATION.md",
                 HERE / "CONTEXTUAL-LOGIC-INTEGRATION.md"]
    snippets = [(doc, doc.read_text()) for doc in documents]
    snippets += [(ROOT / f["path"], f["text"]) for f in edits["shared_fragments"]]
    links = []
    for doc, content in snippets:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://")):
                continue
            name, _, anchor = unquote(target).partition("#")
            p = (doc.parent / name).resolve() if name else doc
            assert p.is_relative_to(ROOT) and p.exists(), (doc, target)
            if anchor and p.suffix == ".md":
                assert anchor in chain.heading_ids(p), (doc, target)
            links.append({"document": str(doc.relative_to(ROOT)), "target": target})

    global_errors = chain.validate(data)
    pending = chain.changes(data)
    combined = {}
    if pending["modified_sources"] or pending["missing_sources"]:
        original = chain.OUTPUT.read_bytes()
        for mode in ("--render", "--check"):
            result = subprocess.run([sys.executable, str(HERE / "build_generative_chain.py"), mode],
                                    cwd=ROOT, text=True, capture_output=True)
            assert result.returncode == 2
            combined[mode] = json.loads(result.stdout)
        assert chain.OUTPUT.read_bytes() == original
    report = dict(
        passed_owned_scope=True,
        scope="Frozen proof bindings, historical editions, owned insertions and canonical F01 only",
        proof_receipt=str(proof.relative_to(ROOT)), proof_receipt_sha256=sha(proof.read_bytes()),
        audit_totals=totals, preserved_pilot_audit_totals=old_totals,
        inherited_baseline=str(baseline.relative_to(ROOT)),
        inherited_baseline_sha256=sha(baseline.read_bytes()),
        inherited_sources_and_audits_identical=True, historical_editions=manifest,
        documents={str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in documents},
        local_links=links, paired_entry="F01", owned_edits_preserved=True,
        global_link_validation_errors=global_errors, pending_shared_reviews=pending,
        combined_renderer_checks=combined, whole_table_certified=False,
        independent_agent_review=False)
    (HERE / "CONTEXTUAL-LOGIC-CHECKS.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(passed_owned_scope=True, new_theorems=totals["new"],
                         total_audits=totals["all"], local_links=len(links),
                         pending_shared_sources=len(pending["modified_sources"]),
                         global_link_errors=len(global_errors), whole_table_certified=False)))


if __name__ == "__main__":
    main()
