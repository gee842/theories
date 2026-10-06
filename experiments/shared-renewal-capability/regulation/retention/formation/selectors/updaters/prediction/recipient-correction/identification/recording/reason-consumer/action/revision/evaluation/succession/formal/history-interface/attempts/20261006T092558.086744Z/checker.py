#!/usr/bin/env python3
"""Fresh audit of the history abstraction; preserve every compilation attempt."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
REPO = next(p for p in ROOT.parents if (p / "AGENTS.md").exists())
NEW = "SuccessionHistoryInterface"
ALLOWED = {"propext", "Quot.sound", "Classical.choice"}
DEPENDENCIES = {
    "EvaluativeSuccession.step_retains_native_and_history",
    "EvaluativeSuccession.trace_retains_native_and_history",
    "EvaluativeSuccession.trace_energy",
    "EvaluativeSuccession.trace_run",
    "SuccessionWitness.suffix_trace",
    "SuccessionWitness.actual_new_publication",
    "SuccessionWitness.actual_selected_action",
    "SuccessionWitness.actual_fresh_reasons",
    "SuccessionWitness.selected_current_reason",
    "SuccessionWitness.actual_effect_from_fresh_evidence",
    "SuccessionWitness.unavailable_influence_attempt_is_paid",
    "SuccessionWitness.access_cut_invalidates_pending_read",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def invoke(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=240)


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    attempt = ROOT / "attempts" / stamp
    attempt.mkdir(parents=True)
    checker_bytes = Path(__file__).read_bytes()
    parent_checker_bytes = (PARENT / "check.py").read_bytes()
    parent_receipt_bytes = (PARENT / "verification.json").read_bytes()
    receipt = json.loads(parent_receipt_bytes)
    assert receipt["status"] == "passed"
    sources = dict(runpy.run_path(str(PARENT / "check.py"))["SOURCES"])
    parent_rows = {item["module"]: item for item in receipt["modules"]}
    assert set(parent_rows) == set(sources)
    sources[NEW] = PARENT / (NEW + ".lean")
    frozen = {name: path.read_bytes() for name, path in sources.items()}
    parent_match = {name: sha(data) == parent_rows[name]["source_sha256"]
                    for name, data in frozen.items() if name != NEW}
    assert all(parent_match.values()), parent_match
    (attempt / (NEW + ".lean")).write_bytes(frozen[NEW])
    (attempt / "checker.py").write_bytes(checker_bytes)
    toolchain_bytes = (PARENT / "lean-toolchain").read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    version = invoke(["lean", "+" + toolchain, "--version"], PARENT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    prefix = invoke(["lean", "+" + toolchain, "--print-prefix"], PARENT)
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin/lean"
    expected = {}
    for name, data in frozen.items():
        source = data.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), name
        assert not re.search(r"^\s*(axiom|constant)\s", source, re.M), name
        imports = re.findall(r"^import\s+(.+)$", source, re.M)
        assert set(imports).issubset({"Std"} | set(sources)), (name, imports)
        declared = set(re.findall(r"^theorem\s+(\w+)", source, re.M))
        audits = re.findall(r"^#print axioms\s+([\w.]+)\s*$", source, re.M)
        expected[name] = set(audits)
        shorts = {q.rsplit(".", 1)[-1] for q in audits}
        assert len(audits) == len(shorts)
        if name == "GenerativeCore":
            assert shorts and shorts.issubset(declared)
        else:
            assert shorts == declared, (name, shorts ^ declared)
    assert DEPENDENCIES.issubset(set().union(*(expected[n] for n in expected if n != NEW)))
    results = []
    observed = set()
    try:
        with tempfile.TemporaryDirectory(prefix="succession-history-interface-") as temporary:
            build = Path(temporary)
            for name, data in frozen.items():
                (build / (name + ".lean")).write_bytes(data)
            env = dict(os.environ, LEAN_PATH=str(build))
            for name, path in sources.items():
                command = [str(compiler), "-o", name + ".olean", name + ".lean"]
                result = invoke(command, build, env)
                log = attempt / (name + ".txt")
                log.write_text(result.stdout)
                audits = re.findall(
                    r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                    result.stdout)
                names = {qualified for qualified, _ in audits}
                observed.update(names)
                audited_shorts = {q.rsplit(".", 1)[-1] for q in names}
                expected_shorts = {q.rsplit(".", 1)[-1] for q in expected[name]}
                qualified_requests = {q for q in expected[name] if "." in q}
                axioms = sorted({a.strip() for _, group in audits
                                 for a in group.split(",") if a.strip()})
                clean = (result.returncode == 0 and "warning:" not in result.stdout
                         and "sorryAx" not in result.stdout
                         and audited_shorts == expected_shorts
                         and qualified_requests.issubset(names)
                         and len(audits) == len(expected[name])
                         and set(axioms).issubset(ALLOWED))
                results.append({
                    "module": name, "role": "new interface" if name == NEW else "frozen parent",
                    "source": str(path.relative_to(REPO)), "source_sha256": sha(frozen[name]),
                    "command": command, "exit_code": result.returncode,
                    "clean_dependency_audit": clean,
                    "audited_declarations": sorted(names), "dependency_audits": len(audits),
                    "axioms": axioms, "output": str(log.relative_to(ROOT)),
                    "output_sha256": sha(log.read_bytes()),
                })
                print(json.dumps({"module": name, "passed": clean}), flush=True)
                if not clean:
                    break
    except subprocess.TimeoutExpired as error:
        timeout_output = error.stdout or ""
        if isinstance(timeout_output, bytes):
            timeout_output = timeout_output.decode(errors="replace")
        (attempt / "timeout.txt").write_text(timeout_output)
    unchanged = (all(path.read_bytes() == frozen[name] for name, path in sources.items())
                 and (PARENT / "verification.json").read_bytes() == parent_receipt_bytes
                 and (PARENT / "check.py").read_bytes() == parent_checker_bytes
                 and (PARENT / "lean-toolchain").read_bytes() == toolchain_bytes
                 and Path(__file__).read_bytes() == checker_bytes)
    passed = (len(results) == len(sources) and unchanged
              and all(r["clean_dependency_audit"] for r in results)
              and DEPENDENCIES.issubset(observed))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "attempt": str(attempt.relative_to(ROOT)),
        "toolchain": toolchain, "toolchain_sha256": sha(toolchain_bytes),
        "lean_version": version.stdout.strip(), "compiler_binary": str(compiler),
        "compiler_sha256": sha(compiler.read_bytes()), "checker_sha256": sha(checker_bytes),
        "parent_checker_sha256": sha(parent_checker_bytes),
        "parent_receipt_sha256": sha(parent_receipt_bytes),
        "parent_receipt_status": receipt["status"], "parent_source_matches": parent_match,
        "source_unchanged_during_check": unchanged,
        "source_sha256": {name: sha(data) for name, data in frozen.items()},
        "fresh_temporary_build": True, "project_objects_only_from_frozen_sources": True,
        "required_named_dependencies": sorted(DEPENDENCIES),
        "all_named_dependencies_audited": DEPENDENCIES.issubset(observed),
        "modules": results,
        "new_audited_declarations": sum(r["dependency_audits"] for r in results if r["module"] == NEW),
        "scope": "Unchanged-law finite continuation interface for replacing only dormant history; "
                 "exact guards, transition, expenditure and live outcome, with actual post-handoff suffix. "
                 "No alternative reachable ancestry, physical erasure, donor disappearance, moral "
                 "equivalence, unrestricted external scheduler, new event law or normative axiom.",
    }
    data = json.dumps(record, indent=2) + "\n"
    (attempt / "verification.json").write_text(data)
    (ROOT / "verification.json").write_text(data)
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "record": str(ROOT / "verification.json")}), flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
