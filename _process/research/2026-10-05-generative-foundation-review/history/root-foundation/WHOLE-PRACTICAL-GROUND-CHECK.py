#!/usr/bin/env python3
"""Verify this round's artifacts against its retained Lean run, without rerunning it."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = HERE / "WHOLE-PRACTICAL-GROUND-EDITS.json"
OUTPUT = HERE / "WHOLE-PRACTICAL-GROUND-CHECKS.json"
PROOFS = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def headings(path):
    body = path.read_text()
    result = set(re.findall(r'''<a\b[^>]*\bid=["']([^"']+)["'][^>]*>''', body))
    for line in body.splitlines():
        if re.match(r"^#{1,6}\s+", line):
            title = re.sub(r"^#{1,6}\s+", "", line).strip().lower()
            title = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", title)
            result.add(re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", title)))
    return result


def check_links(path, text):
    checked = []
    for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text):
        parsed = urlsplit(target.strip("<>"))
        if parsed.scheme:
            continue
        resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        assert resolved.exists(), (path, target)
        if parsed.fragment:
            assert unquote(parsed.fragment) in headings(resolved), (path, target, "anchor")
        checked.append({"from": str(path.relative_to(ROOT)), "target": target})
    return checked


def check_regenerative():
    receipt_path = PROOFS / "regenerative-verification.json"
    receipt = json.loads(receipt_path.read_text())
    assert receipt["status"] == "passed" and receipt["source_unchanged_during_check"]
    assert "4.29.1" in receipt["lean"]
    run = PROOFS / receipt["retained_run"]
    assert (run / "verification.json").read_bytes() == receipt_path.read_bytes()
    checker = PROOFS / "check_regenerative.py"
    assert sha(checker.read_bytes()) == receipt["checker_sha256"]
    assert (run / checker.name).read_bytes() == checker.read_bytes()
    assert set(receipt["dependencies"]) == {"GenerativeCore"}
    core = PROOFS.parent / "GenerativeCore.lean"
    dependency = receipt["dependencies"]["GenerativeCore"]
    assert Path(dependency["source"]).resolve() == core.resolve()
    assert sha(core.read_bytes()) == dependency["sha256"]
    assert (run / core.name).read_bytes() == core.read_bytes()
    assert len(receipt["modules"]) == 1
    module = receipt["modules"][0]
    assert module["module"] == "RegenerativeDiversity" and module["kernel_checked"]
    current = PROOFS / "RegenerativeDiversity.lean"
    assert sha(current.read_bytes()) == module["sha256"]
    assert (run / current.name).read_bytes() == current.read_bytes()
    audit = (run / "RegenerativeDiversityAxiomAudit.log").read_text()
    for declaration in module["declarations"]:
        name = declaration["name"]
        match = re.search("'" + re.escape(name) +
                          r"' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                          audit)
        assert match, name
        actual = [] if match[1] is None else [a.strip() for a in match[1].split(",")]
        assert actual == module["axiom_dependencies"][name], name
    axioms = sorted({a for values in module["axiom_dependencies"].values() for a in values})
    assert axioms == module["axioms"] == ["Quot.sound", "propext"]
    theorem_count = sum(d["kind"] == "theorem" for d in module["declarations"])
    assert theorem_count == module["theorems"] == 14
    assert len(module["declarations"]) == 36
    commands = sorted(run.glob("*-command.json"))
    assert len(commands) == 4
    for path in commands:
        assert json.loads(path.read_text())["returncode"] == 0, path
    return {"theorems": theorem_count, "audited_declarations": 36, "axioms": axioms,
            "receipt": str(receipt_path.relative_to(ROOT)),
            "receipt_sha256": sha(receipt_path.read_bytes())}


def main():
    OUTPUT.write_text(json.dumps({"status": "checking", "scope": "Artifact checks only."}) + "\n")
    ledger = json.loads(LEDGER.read_text())
    links, bindings = [], {}
    for record in ledger["edits"]:
        path = ROOT / record["path"]
        fragment = record["inserted_fragment"]
        assert path.read_text().count(fragment) == 1, record["path"]
        assert sha(fragment.encode()) == record["sha256"], record["path"]
        links.extend(check_links(path, fragment))
    for relative in ledger["new_files"]:
        path = ROOT / relative
        if path == OUTPUT:
            continue
        assert path.is_file(), relative
        bindings[relative] = sha(path.read_bytes())
        if path.suffix == ".md":
            links.extend(check_links(path, path.read_text()))
    for relative, expected in ledger["preserved_sources"].items():
        assert sha((ROOT / relative).read_bytes()) == expected, relative

    receipt_path = PROOFS / "practical-verification.json"
    receipt = json.loads(receipt_path.read_text())
    assert receipt["status"] == "passed" and receipt["source_unchanged_during_check"]
    assert "4.29.1" in receipt["lean"]
    run = PROOFS / receipt["retained_run"]
    assert (run / "verification.json").read_bytes() == receipt_path.read_bytes()
    assert sha((PROOFS / "check_practical.py").read_bytes()) == receipt["checker_sha256"]
    assert (run / "check_practical.py").read_bytes() == (PROOFS / "check_practical.py").read_bytes()
    theorem_count = audit_count = 0
    for module in receipt["modules"]:
        name = module["module"]
        current = PROOFS / (name + ".lean")
        assert sha(current.read_bytes()) == module["sha256"]
        assert current.read_bytes() == (run / current.name).read_bytes()
        assert module["kernel_checked"] and module["axioms"] == []
        audit = (run / (name + "AxiomAudit.log")).read_text()
        for declaration in module["declarations"]:
            assert "'" + declaration["name"] + "' does not depend on any axioms" in audit
        theorem_count += sum(d["kind"] == "theorem" for d in module["declarations"])
        audit_count += len(module["declarations"])
    commands = sorted(run.glob("*-command.json"))
    assert len(commands) == 3
    for path in commands:
        assert json.loads(path.read_text())["returncode"] == 0, path
    assert theorem_count == 14 and audit_count == 31
    regenerative = check_regenerative()
    result = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Owned artifact and receipt checks; not a new Lean run or ethical proof.",
        "owned_fragments": len(ledger["edits"]), "local_links": links,
        "theorems": theorem_count, "audited_declarations": audit_count,
        "all_axiom_dependencies_empty": not regenerative["axioms"],
        "original_practical_axioms": [],
        "original_count_scope": "WholePracticalRestriction only; regenerative bundle audited separately.",
        "regenerative_bundle": regenerative,
        "lean_receipt": str(receipt_path.relative_to(ROOT)),
        "lean_receipt_sha256": sha(receipt_path.read_bytes()),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "artifact_sha256": bindings,
        "universal_normative_grounding_proved": False,
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "passed", "owned_fragments": len(ledger["edits"]),
                      "local_links": len(links), "theorems": theorem_count,
                      "audited_declarations": audit_count,
                      "regenerative_bundle": regenerative,
                      "universal_normative_grounding_proved": False}))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        OUTPUT.write_text(json.dumps({"status": "failed", "error": str(error)}, indent=2) + "\n")
        raise
