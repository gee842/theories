#!/usr/bin/env python3
"""Scoped document, table, model-record and retained-proof binding checks."""
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FORMAL = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    docs = [HERE / "CORRECTION-INFRASTRUCTURE-INTEGRATION.md", HERE / "CORRECTION-INFRASTRUCTURE-PROTOCOL.md"]
    linked = 0
    for path in docs:
        for ref in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if re.match(r"[a-z]+://", ref):
                continue
            name, _, anchor = ref.partition("#")
            target = (path.parent / name).resolve() if name else path
            assert target.is_file(), (str(path), ref)
            if anchor:
                assert anchor in chain.heading_ids(target), (str(path), ref)
            linked += 1

    receipt = json.loads((FORMAL / "correction-infrastructure-verification.json").read_text())
    assert receipt["status"] == "passed"
    retained = FORMAL / receipt["retained_run"]
    for name, fingerprint in receipt["source_sha256"].items():
        assert digest(FORMAL / (name + ".lean")) == fingerprint
        assert digest(retained / (name + ".lean")) == fingerprint
    for name, fingerprint in receipt["checker_sha256"].items():
        assert digest(FORMAL / name) == fingerprint
        assert digest(retained / name) == fingerprint
    for name, fingerprint in receipt["artifact_sha256"].items():
        assert digest(retained / name) == fingerprint
    assert receipt == json.loads((retained / "verification.json").read_text())
    mod = receipt["modules"][0]
    assert mod["theorems"] == 34 and len(mod["declarations"]) == 56
    assert all(set(v) <= {"propext", "Quot.sound", "Classical.choice"}
               for v in mod["axiom_dependencies"].values())

    models = json.loads((FORMAL / "correction-infrastructure-model-checks.json").read_text())
    assert models["status"] == "passed"
    assert models["protocol_sha256"] == digest(docs[1])
    assert models["runner_sha256"] == digest(FORMAL / "compare_correction_infrastructure.py")
    assert models["lean_source_sha256"] == digest(FORMAL / "CorrectionInfrastructure.lean")
    records_path = FORMAL / "correction-infrastructure-model-records.jsonl"
    assert models["records_sha256"] == digest(records_path)
    records = [json.loads(line) for line in records_path.read_text().splitlines()]
    assert len(records) == 12960
    assert len({(r["model"], r["horizon"], r["initial"]) for r in records}) == len(records)
    assert sum(r["feasible"] for r in records) == 11136
    assert len({r["model"] for r in records}) == 1296
    for name, expected in models["metrics"].items():
        feasible = [r["policies"][name] for r in records if r["feasible"]]
        assert sum(not r["safe"] for r in feasible) == expected["unsafe_on_feasible"]
        assert sum(r["safe"] and r["regret"] > 0 for r in feasible) == expected["suboptimal_on_feasible"]
        assert max((r["regret"] for r in feasible if r["safe"]), default=0) == expected["maximum_regret"]

    data = chain.read_data()
    rows = {e["id"]: e for s in data["sections"] for e in s["entries"]}
    generated = chain.render(data).splitlines()
    table = chain.OUTPUT.read_text().splitlines()
    for ident in ("M23", "F29"):
        expected = next(x for x in generated if x.startswith("| " + ident + " |"))
        assert expected in table
        for link in rows[ident]["links"]:
            path, fragment = chain.local_target(link["path"])
            assert path.is_file()
            if fragment:
                assert fragment in chain.heading_ids(path)
    assert next(x for x in generated if "indexed entries**" in x) in table
    report = {"status": "passed", "scope": "Local bindings, not independent scientific acceptance",
              "document_links": linked, "proof_theorems": 34, "declaration_audits": 56,
              "model_records": len(records), "scoped_rows": ["M23", "F29"],
              "owned_document_sha256": {str(p.relative_to(ROOT)): digest(p) for p in docs},
              "shared_index_pending": chain.changes(data)}
    (HERE / "CORRECTION-INFRASTRUCTURE-CHECKS.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in
                      {"owned_document_sha256", "shared_index_pending"}}, indent=2))


if __name__ == "__main__":
    main()
