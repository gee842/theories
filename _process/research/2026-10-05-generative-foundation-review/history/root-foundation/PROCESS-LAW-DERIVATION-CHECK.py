#!/usr/bin/env python3
"""Reconcile the accepted process-law proof, original evidence and owned edits."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
CORE = REPO / "experiments/integrated-correction/general-framework/generative-basis/lean"
S = CORE / "inquiry-root/sufficiency"
RUN = S / "process-law-runs/1791291483950888000"
OUTPUT = HERE / "PROCESS-LAW-DERIVATION-CHECKS.json"
RECEIPT_SHA = "2dd47104443f4eb3495f6336438a3ca8a3171eab5c67a69379588a1d581a37a0"
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
hashes = []


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check_hash(path, expected):
    digest = sha(path.read_bytes())
    assert digest == expected, path
    hashes.append({"path": str(path.relative_to(REPO)), "sha256": digest})


def headings(text):
    out, seen = set(), {}
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        index = seen.get(slug, 0)
        seen[slug] = index + 1
        out.add(slug + (f"-{index}" if index else ""))
    return out


def main():
    check_hash(S / "process-law-verification.json", RECEIPT_SHA)
    check_hash(RUN / "receipt.json", RECEIPT_SHA)
    receipt = json.loads((RUN / "receipt.json").read_text())
    assert receipt["status"] == "passed" and receipt["inputs_unchanged"]
    assert len(receipt["modules"]) == 32 and receipt["audits"] == 599 and receipt["new_audits"] == 190
    assert receipt["all_previous409_audit_names_retained"] and receipt["whole_current_audited_closure_empty"]
    assert receipt["fresh_temporary_build"] and not receipt["local_precompiled_imports_used"]
    assert not receipt["old_scientific_producers_executed"]
    assert receipt["native_original_port_executed_by_correspondence_checker"]
    assert receipt["native_case_certificates_compiled_in_this_closure"]
    for root in (S, RUN):
        check_hash(root / "check_process_law.py", receipt["checker_sha256"])
        check_hash(root / "check_native_packet_correspondence.py", receipt["native_checker_sha256"])
        check_hash(root / "native-packet-inputs.json", receipt["native_manifest_sha256"])
        check_hash(root / "native-packet-correspondence.json", receipt["native_correspondence_sha256"])
    check_hash(CORE / "lean-toolchain", receipt["toolchain_sha256"])
    check_hash(RUN / "lean-toolchain", receipt["toolchain_sha256"])
    assert sha(Path(receipt["compiler"]).read_bytes()) == receipt["compiler_sha256"]
    baseline_path = REPO / receipt["baseline"]
    check_hash(baseline_path, receipt["baseline_sha256"])
    check_hash(S / receipt["baseline_snapshot"], receipt["baseline_sha256"])
    baseline = json.loads(baseline_path.read_text())
    assert baseline["status"] == "passed" and baseline["audits"] == 409
    old = {m["module"]: m for m in baseline["modules"]}
    modules = {m["module"]: m for m in receipt["modules"]}
    assert len(old) == 28 and old.keys() <= modules.keys()
    total = 0
    for module in receipt["modules"]:
        assert module["passed"] and module["audit_complete"] and module["exact_dependency_contract"]
        assert all(not d for d in module["axioms_by_declaration"].values())
        check_hash(REPO / module["source"], module["source_sha256"])
        check_hash(S / module["source_snapshot"], module["source_sha256"])
        check_hash(S / module["log"], module["log_sha256"])
        source = (S / module["source_snapshot"]).read_text()
        log = (S / module["log"]).read_text()
        assert "warning:" not in log
        requests = re.findall(r"^#print axioms (\S+)\s*$", source, re.M)
        audited = [(name, [d.strip() for d in ds.split(",") if d.strip()])
                   for name, ds in AUDIT.findall(log)]
        assert len(audited) == len(requests) == len(module["axioms_by_declaration"])
        assert dict(audited) == module["axioms_by_declaration"]
        assert all(actual == requested or actual.endswith("." + requested)
                   for (actual, _), requested in zip(audited, requests))
        total += len(audited)
        if module["module"] in old:
            prior = old[module["module"]]
            assert module["source_sha256"] == prior["source_sha256"]
            assert module["axioms_by_declaration"] == prior["axioms_by_declaration"]
        else:
            declared = set(re.findall(r"^(?:private\s+)?(?:theorem|def|abbrev|inductive|structure)\s+(\w+)\b", source, re.M))
            assert declared == {name.rsplit(".", 1)[-1] for name in requests}
    assert total == 599
    counts = {kind: sum(row[kind] for row in receipt["new_declarations"].values())
              for kind in ("theorem", "def", "abbrev", "inductive", "structure")}
    assert counts == {"theorem": 146, "def": 36, "abbrev": 1, "inductive": 6, "structure": 1}
    check_hash(RUN / "attainable-inputs.json", receipt["evidence_manifest_sha256"])
    check_hash(baseline_path.parent / "attainable-inputs.json", receipt["evidence_manifest_sha256"])
    evidence = json.loads((RUN / "attainable-inputs.json").read_text())["files"]
    earlier_path = REPO / baseline["baseline"]
    check_hash(earlier_path, baseline["baseline_sha256"])
    assert len(evidence) == receipt["preserved_evidence_files"] == 16
    for row in evidence:
        check_hash(REPO / row["path"], row["sha256"])
        check_hash(earlier_path.parent / "evidence" / row["path"], row["sha256"])
    native_files = json.loads((RUN / "native-packet-inputs.json").read_text())["files"]
    assert len(native_files) == 12 and len({r["path"] for r in native_files}) == 12
    for row in native_files:
        check_hash(REPO / row["path"], row["sha256"])
        check_hash(RUN / "native-evidence" / row["path"], row["sha256"])
    native = json.loads((RUN / "native-packet-correspondence.json").read_text())
    assert native["status"] == "passed" and native["original_native_command_executed"]
    assert not native["scientific_producer_executed"] and not native["original_machine_relearned"]
    assert native["generated_lean_requires_separate_kernel_check"]
    assert native["inputs_manifest_sha256"] == receipt["native_manifest_sha256"]
    assert native["checker_sha256"] == receipt["native_checker_sha256"]
    assert native["source_bindings"] == {r["path"]: r["sha256"] for r in native_files}
    assert native["generated_lean_sha256"] == modules["NativePacketCases"]["source_sha256"]
    assert native["native_model_sha256"] == modules["NativePacketProcess"]["source_sha256"]
    assert native["case_count"] == len(native["cases"]) == receipt["new_native_conformance_cases"] == 5928
    assert [case["id"] for case in native["cases"]] == list(range(5928))
    assert native["case_blocks"] == 93 and native["generated_lean_audit_count"] == 94
    assert len(modules["NativePacketCases"]["axioms_by_declaration"]) == 94
    assert len(modules["NativePacketProcess"]["axioms_by_declaration"]) == 45
    assert len(modules["PacketLawDerivation"]["axioms_by_declaration"]) == 51
    edits = json.loads((HERE / "PROCESS-LAW-DERIVATION-EDITS.json").read_text())["edits"]
    fragments = []
    for edit in edits:
        path = REPO / edit["path"]
        assert sha(edit["fragment"].encode()) == edit["fragment_sha256"]
        assert edit["fragment"] in path.read_text(), (path, "Owned fragment missing")
        fragments.append((path, edit["fragment"]))
    for name in ("PROCESS-LAW-DERIVATION.md", "PROCESS-LAW-DERIVATION-REVIEW.md"):
        path = HERE / name
        fragments.append((path, path.read_text()))
    links = []
    for path, content in fragments:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"[a-zA-Z]+:", target):
                continue
            file, _, anchor = unquote(target).partition("#")
            actual = (path.parent / file).resolve() if file else path
            # The only forward reference allowed is this checker's output.
            assert actual.exists() or (actual == OUTPUT and not anchor), (path, target)
            if anchor and actual.suffix == ".md":
                assert anchor in headings(actual.read_text()), (path, target)
            links.append({"from": str(path.relative_to(REPO)), "target": target})
    document_hashes = {str(path.relative_to(REPO)): sha(path.read_bytes()) for path, _ in fragments}
    result = {"status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Saved proof/evidence and owned document reconciliation only; no Lean or scientific rerun.",
        "modules": 32, "audits": 599, "new_audits": 190, "new_declarations": counts,
        "all_audited_dependencies_empty": True, "all_previous409_audits_retained": True,
        "native_original_command_cases": 5928, "native_evidence_files": 12, "prior_evidence_files": 16,
        "owned_fragments": len(edits), "owned_files": len({e["path"] for e in edits}),
        "links_checked": len(links), "hash_comparisons": len(hashes),
        "compiler_hash_verified": True, "assumption_free_foundation_established": False,
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "document_hashes_at_check": document_hashes, "hashes": hashes, "links": links}
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in {"document_hashes_at_check", "hashes", "links"}}))


if __name__ == "__main__":
    main()
