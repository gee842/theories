#!/usr/bin/env python3
"""Check operation-derived distinctions with all three unchanged dependencies."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
MODULE = "OperationRoles"
BASELINE = HERE / "relational-coordinate-checks/20261008T103037.176156Z/receipt.json"
DECLARATIONS = """MergedBy Invariant FibreConstant Idempotent Fixed retainedView reset copy
merged_distinctions_stay_merged invariant_reading_is_fibre_constant fibre_constant_is_invariant
invariant_iff_fibre_constant attained_iff_fixed retained_view_stable retained_view_covers_fixed
invariant_iff_factors_through_retained_view retained_factor_unique_pointwise
merged_iff_all_invariant_readings merged_relation_covariant fixed_relation_covariant
reset_graph_is_existing_law copy_graph_is_existing_law reset_is_idempotent copy_is_idempotent
native_operations_conjugate native_merged_relation_preserved reset_retains_exactly_second_distinctions
copy_retains_exactly_second_distinctions original_first_reading_is_not_invariant
original_second_reading_is_invariant toggle_attains_a_state_without_fixing_it
every_reset_word_feasible retained_difference_without_action_word_difference""".split()
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, check=True, timeout=60)


def main():
    baseline_bytes = BASELINE.read_bytes()
    baseline = json.loads(baseline_bytes)
    assert baseline["passed"] and baseline["total_empty_audits"] == 74
    paths = {name: (HERE.parent if name == "GenerativeCore" else HERE) / (name + ".lean")
             for name in baseline["modules"]}
    paths[MODULE] = HERE / (MODULE + ".lean")
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    for name, previous in baseline["modules"].items():
        assert sha(frozen[name]) == previous["source_sha256"]
        assert (BASELINE.parent / (name + ".lean")).read_bytes() == frozen[name]
        assert sha((BASELINE.parent / (name + ".log")).read_bytes()) == previous["log_sha256"]
    code = frozen[MODULE].decode()
    assert re.findall(r"^import (.+)$", code, re.M) == ["RelationalCoordinates"]
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
    assert not re.search(r"^\s*(axiom|constant|opaque)\s", code, re.M)
    assert len(re.findall(r"^theorem ", code, re.M)) == 25
    assert set(re.findall(r"^(?:theorem|def) (\w+)", code, re.M)) == set(DECLARATIONS)
    assert re.findall(r"^#print axioms (\w+)$", code, re.M) == DECLARATIONS
    toolchain = (HERE / "lean-toolchain").read_text().strip()
    version = run(["lean", "+" + toolchain, "--version"], HERE).stdout.strip()
    assert "version 4.29.1," in version
    prefix = Path(run(["lean", "+" + toolchain, "--print-prefix"], HERE).stdout.strip())
    compiler = prefix / "bin/lean"
    assert sha(compiler.read_bytes()) == baseline["compiler_sha256"]
    build = HERE / "operation-role-checks" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build.mkdir(parents=True)
    checker = Path(__file__).read_bytes()
    (build / Path(__file__).name).write_bytes(checker)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    results = {}
    for name in paths:
        (build / (name + ".lean")).write_bytes(frozen[name])
        result = run([str(compiler), "-o", name + ".olean", name + ".lean"],
                     build, dict(os.environ, LEAN_PATH=str(build)))
        (build / (name + ".log")).write_text(result.stdout)
        assert "warning:" not in result.stdout
        audits = {n: [a.strip() for a in dependencies.split(",") if a.strip()]
                  for n, dependencies in AUDIT.findall(result.stdout)}
        assert all(not a for a in audits.values())
        if name in baseline["modules"]:
            assert audits == baseline["modules"][name]["audits"]
        else:
            assert list(audits) == [MODULE + "." + n for n in DECLARATIONS]
        results[name] = {"source_sha256": sha(frozen[name]), "audits": audits,
                         "log_sha256": sha(result.stdout.encode())}
        print(name + ": " + str(len(audits)) + " empty audits", flush=True)
    assert all(path.read_bytes() == frozen[name] for name, path in paths.items())
    assert Path(__file__).read_bytes() == checker and BASELINE.read_bytes() == baseline_bytes
    receipt = {
        "passed": True, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "lean_version": version, "compiler_sha256": sha(compiler.read_bytes()),
        "checker_sha256": sha(checker), "modules": results,
        "new_theorems": 25, "new_definitions": 8, "new_empty_audits": 33,
        "inherited_empty_audits": 74, "total_empty_audits": sum(len(m["audits"]) for m in results.values()),
        "baseline_receipt": str(BASELINE.relative_to(HERE)), "baseline_sha256": sha(baseline_bytes),
        "run_directory": str(build.relative_to(HERE)),
        "scope": "An operation determines its merged distinctions covariantly. For idempotent operations, attained fixed representatives characterize all invariant readings with constructive, pointwise-unique factorization. Native reset/copy laws prove the local condition; toggle and action-word controls prevent universal promotion.",
        "logical_basis": "Lean 4.29.1 type theory remains the checking framework. The actual operation, state interface, deterministic scope and physical interpretation remain to be warranted; no universal idempotence or process law is derived.",
    }
    assert receipt["total_empty_audits"] == 107
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (HERE / "operation-role-verification.json").write_text(serialized)
    print(json.dumps({"passed": True, "new_theorems": 25, "new_empty_audits": 33,
                      "inherited_empty_audits": 74, "run_directory": receipt["run_directory"]}))


if __name__ == "__main__":
    main()
