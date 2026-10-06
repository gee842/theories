#!/usr/bin/env python3
"""Fresh additive build; preserve the default receipt and exact ancestor audits."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
BASELINE = CORE / "verification.json"
BASELINE_SHA256 = "0e446764280518fc43fa040f4325789da2899ebaf8ae7e0493fa3ac42c64e665"
NEW = {
    "InquirySufficiency": HERE / "InquirySufficiency.lean",
    "GenerativeInquirySufficiencyModel": CORE / "GenerativeInquirySufficiencyModel.lean",
}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    baseline_bytes = BASELINE.read_bytes()
    assert sha(baseline_bytes) == BASELINE_SHA256, "Default receipt changed; review the new baseline."
    baseline = json.loads(baseline_bytes)
    assert baseline["status"] == "passed" and len(baseline["modules"]) == 16
    originals = {m["module"]: m for m in baseline["modules"]}
    paths = {name: CORE / m["source"] for name, m in originals.items()}
    paths.update(NEW)
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    for name, original in originals.items():
        assert sha(frozen[name]) == original["source_sha256"], name
    checker_bytes = Path(__file__).read_bytes()
    toolchain_bytes = (CORE / "lean-toolchain").read_bytes()
    assert sha(toolchain_bytes) == baseline["toolchain_sha256"]
    compiler = Path(baseline["compiler_binary"])
    assert sha(compiler.read_bytes()) == baseline["compiler_sha256"]
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    assert version == baseline["lean_version"]

    imports, requests = {}, {}
    for name, data in frozen.items():
        source = data.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M), name
        imports[name] = re.findall(r"^import\s+(\S+)\s*$", source, re.M)
        assert set(imports[name]) <= {"Std", *paths}, name
        requests[name] = re.findall(r"^#print axioms (\S+)\s*$", source, re.M)
        assert len(requests[name]) == len(set(requests[name])), name
    assert imports["InquirySufficiency"] == ["GenerativeCore"]
    assert imports["GenerativeInquirySufficiencyModel"] == ["GenerativeOutcomeModel", "InquirySufficiency"]
    mechanism = frozen["InquirySufficiency"].decode()
    theorem_names = re.findall(r"^theorem\s+(\w+)", mechanism, re.M)
    audited_short = [x.rsplit(".", 1)[-1] for x in requests["InquirySufficiency"]]
    assert set(theorem_names) == set(audited_short) - {"nonemptyDecisionFromList"}
    assert len(theorem_names) == 16 and len(audited_short) == 17
    entry = re.sub(r"/\-.*?\-/", "", frozen["GenerativeInquirySufficiencyModel"].decode(), flags=re.S)
    assert all(re.fullmatch(r"import\s+\w+", line.strip())
               for line in entry.splitlines() if line.strip())
    assert requests["GenerativeInquirySufficiencyModel"] == []

    order, done = [], {"Std"}
    while len(order) < len(paths):
        ready = [name for name in paths if name not in done and set(imports[name]) <= done]
        assert ready, "Cyclic or incomplete imports"
        order.extend(ready)
        done.update(ready)

    attempt = HERE / "runs" / str(time.time_ns())
    attempt.mkdir(parents=True)
    (attempt / "sources").mkdir()
    (attempt / "baseline-verification.json").write_bytes(baseline_bytes)
    (attempt / "check.py").write_bytes(checker_bytes)
    (attempt / "lean-toolchain").write_bytes(toolchain_bytes)
    for name, data in frozen.items():
        (attempt / "sources" / (name + ".lean")).write_bytes(data)
    rows = []
    with tempfile.TemporaryDirectory(prefix="inquiry-sufficiency-fresh-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in order:
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            result = subprocess.run(command, cwd=build, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
            log = attempt / (name + ".txt")
            log.write_text(result.stdout)
            audits = [(decl, sorted(a.strip() for a in deps.split(",") if a.strip()))
                      for decl, deps in AUDIT.findall(result.stdout)]
            audit_map = dict(audits)
            complete = len(audits) == len(audit_map) == len(requests[name]) and all(
                actual == wanted or actual.endswith("." + wanted)
                for (actual, _), wanted in zip(audits, requests[name]))
            contract = (audit_map == originals[name]["axioms_by_declaration"]
                        if name in originals else all(not deps for _, deps in audits))
            passed = result.returncode == 0 and "warning:" not in result.stdout and complete and contract
            rows.append({"module": name, "source": str(paths[name].relative_to(REPO)),
                         "source_sha256": sha(frozen[name]), "new_module": name in NEW,
                         "command": command, "exit_code": result.returncode,
                         "import_only": name == "GenerativeInquirySufficiencyModel",
                         "axioms_by_declaration": audit_map, "audit_complete": complete,
                         "exact_dependency_contract": contract, "passed": passed,
                         "log": str(log.relative_to(HERE)), "log_sha256": sha(log.read_bytes()),
                         "source_snapshot": str((attempt / "sources" / (name + ".lean")).relative_to(HERE))})
            print(json.dumps({"module": name, "passed": passed, "audits": len(audits)}), flush=True)
            if not passed:
                print(result.stdout, flush=True)
                break

    unchanged = (all(path.read_bytes() == frozen[name] for name, path in paths.items()) and
                 BASELINE.read_bytes() == baseline_bytes and Path(__file__).read_bytes() == checker_bytes and
                 (CORE / "lean-toolchain").read_bytes() == toolchain_bytes)
    passed = len(rows) == len(paths) and unchanged and all(row["passed"] for row in rows)
    record = {
        "status": "passed" if passed else "failed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "compiler": str(compiler), "compiler_sha256": baseline["compiler_sha256"], "lean_version": version,
        "checker_sha256": sha(checker_bytes), "toolchain_sha256": sha(toolchain_bytes),
        "baseline": str(BASELINE.relative_to(REPO)), "baseline_sha256": sha(baseline_bytes),
        "baseline_snapshot": str((attempt / "baseline-verification.json").relative_to(HERE)),
        "default_receipt_overwritten": False, "fresh_temporary_build": True,
        "local_precompiled_imports_used": False, "inputs_unchanged": unchanged,
        "modules": rows, "inherited_modules": len(originals),
        "audits": sum(len(row["axioms_by_declaration"]) for row in rows),
        "new_audits": sum(len(row["axioms_by_declaration"]) for row in rows if row["new_module"]),
        "new_axiom_dependencies": sorted({a for row in rows if row["new_module"]
                                           for deps in row["axioms_by_declaration"].values() for a in deps}),
        "scope": "Constructive bounded-policy existence iff explicit live/empty-branch sufficiency; "
                 "actual native execution, all-successor prefix safety, nonvacuity, and equivalence to "
                 "implication-form sufficiency under classified branches. Exact finite enumeration "
                 "supplies local nonemptiness decisions. No added event law or installed learner; "
                 "no derivation of the criterion's meaning, authority, calibration or origin. "
                 "Historical root dependencies remain exact; the whole closure is not claimed axiom-free."
    }
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        (HERE / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(rows),
                      "audits": record["audits"], "new_audits": record["new_audits"],
                      "receipt": str((attempt / "receipt.json").relative_to(REPO))}), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
