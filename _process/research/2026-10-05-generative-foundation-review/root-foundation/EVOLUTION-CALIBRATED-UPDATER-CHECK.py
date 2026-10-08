#!/usr/bin/env python3
"""Documentary verification only; the separate Lean checker validates proofs."""
from pathlib import Path
import hashlib
import copy
import importlib.util
import json
import re
from datetime import datetime, timezone
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PACKAGE = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism"
OUTPUT = HERE / "EVOLUTION-CALIBRATED-UPDATER-CHECKS.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / "EVOLUTION-CALIBRATED-UPDATER-INDEX-EDITS.json").read_text())
    receipt_path = PACKAGE / "calibrated-updater-verification.json"
    proof = json.loads(receipt_path.read_text())
    assert proof["status"] == "passed" and not proof["source_changed_during_run"]
    assert (proof["new_theorems"], proof["new_audits"], proof["total_audits"]) == (30, 59, 201)
    snapshot = ROOT / proof["snapshot"]
    assert json.loads((snapshot / "verification.json").read_text()) == proof
    module_checks = []
    for module in proof["modules"]:
        source = ROOT / module["source"]
        assert digest(source) == module["source_sha256"]
        assert digest(snapshot / "sources" / source.name) == module["source_sha256"]
        assert len(module["declarations"]) == module["audits"]
        assert sum(d["kind"] == "theorem" for d in module["declarations"]) == module["theorems"]
        for axioms in module["nonempty_audits"].values():
            assert set(axioms) <= {"propext", "Classical.choice", "Quot.sound"}
        module_checks.append({"module": module["module"], "theorems": module["theorems"],
                              "audits": module["audits"], "source_sha256": digest(source)})
    assert digest(PACKAGE / "check_calibrated_updater.py") == proof["checker_sha256"]
    assert digest(snapshot / "check_calibrated_updater.py") == proof["checker_sha256"]
    for name, value in proof["log_sha256"].items():
        assert digest(snapshot / name) == value
    assert digest(snapshot / "lake-manifest.json") == proof["manifest_sha256"]
    assert digest(Path(proof["commands"][0][0])) == proof["compiler_sha256"]
    old = json.loads((PACKAGE / "connectionist-recovery-verification.json").read_text())
    old_module = next(m for m in old["modules"] if m["module"] == "ConnectionistRecovery")
    assert old_module["source_sha256"] == module_checks[0]["source_sha256"]
    memory = json.loads((PACKAGE / "developmental-memory-verification.json").read_text())
    memory_module = next(m for m in memory["modules"] if m["module"] == "DevelopmentalMemory")
    assert memory_module["source_sha256"] == module_checks[1]["source_sha256"]
    updater = json.loads((PACKAGE / "updater-consequences-verification.json").read_text())
    updater_module = next(m for m in updater["modules"] if m["module"] == "UpdaterConsequences")
    assert updater_module["source_sha256"] == module_checks[2]["source_sha256"]

    source_dir = ROOT / "sources/evolutionary-selection/comparative-direction"
    provenance = json.loads((source_dir / "watson2014.provenance.json").read_text())
    pdf = source_dir / "watson2014.pdf"
    assert pdf.stat().st_size == provenance["bytes"]
    assert digest(pdf) == provenance["sha256"]

    owned_texts = []
    for edit in edits["edits"]:
        path = ROOT / edit["path"]
        text = path.read_text()
        for passage in edit["passages"]:
            new = passage["new"]
            if new:
                assert new in text, (path, "owned passage changed")
                owned_texts.append((path, new))
    for name in ["EVOLUTION-CALIBRATED-UPDATER.md", "EVOLUTION-CALIBRATED-UPDATER-PROTOCOL.md"]:
        path = HERE / name
        owned_texts.append((path, path.read_text()))

    links = set()
    for path, text in owned_texts:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"^[a-zA-Z][\w+.-]*:", target):
                continue
            filename, _, fragment = unquote(target).partition("#")
            resolved = (path.parent / filename).resolve() if filename else path
            assert resolved.is_relative_to(ROOT)
            assert resolved.exists() or resolved == OUTPUT, (path, target)
            if fragment and resolved.suffix == ".md":
                assert fragment in chain.heading_ids(resolved), (path, target)
            links.add((str(path.relative_to(ROOT)), target))

    data = chain.read_data()
    scoped = copy.deepcopy(data)
    for section in scoped["sections"]:
        section["entries"] = [e for e in section["entries"] if e["id"] == "C14"]
    assert not chain.validate(scoped)
    entry = next(e for section in data["sections"] for e in section["entries"] if e["id"] == "C14")
    assert entry == edits["chain"]["after"], "C14 changed; review its new version before updating this check"
    expected_row = next(line for line in chain.render(data).splitlines() if line.startswith("| C14 |"))
    actual_row = next(line for line in chain.OUTPUT.read_text().splitlines() if line.startswith("| C14 |"))
    assert actual_row == expected_row
    for name, fingerprint in edits["chain"]["reviewed_sources"].items():
        assert digest(ROOT / name) == fingerprint
        assert data["reviewed_sources"][name] == fingerprint
    chapter = ROOT / "theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md"
    assert len(re.findall(r"^\| \*\*[1-6] ", chapter.read_text(), re.M)) == 6
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed",
        "scope": "Owned acquired-calibration/constructed-updater proof bindings, links, source preservation and C14 integration; no new compilation or full-table review certification.",
        "proof_receipt_sha256": digest(receipt_path),
        "proof_modules": module_checks,
        "new_theorems": 30, "new_audits": 59, "inherited_audits": 142,
        "owned_local_links_checked": len(links),
        "original_pdf_sha256": digest(pdf),
        "six_broad_completion_requirements_preserved": True,
        "other_entries_preserved_at_mutation": edits["chain"]["other_entries_preserved"],
        "other_rendered_lines_preserved_at_mutation": edits["chain"]["other_rendered_lines_preserved"],
        "C14_render_matches": True,
        "full_render_matches_observation_only": chain.OUTPUT.read_text() == chain.render(data),
        "pending_global_review": chain.changes(data),
        "global_structural_validation_observation_only": chain.validate(data),
        "owned_reviewed_sources": edits["chain"]["reviewed_sources"],
        "documentary_checker_sha256": digest(Path(__file__)),
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "local_links": len(links),
                      "new_theorems": 30, "new_audits": 59, "inherited_audits": 142,
                      "other_entries_preserved": result["other_entries_preserved_at_mutation"]}))


if __name__ == "__main__":
    main()
