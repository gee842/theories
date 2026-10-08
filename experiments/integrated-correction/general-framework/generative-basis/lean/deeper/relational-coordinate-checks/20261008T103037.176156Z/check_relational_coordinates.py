#!/usr/bin/env python3
"""Freeze and check coordinate covariance against unchanged proof dependencies."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
MODULE = "RelationalCoordinates"
DECLARATIONS = """ReadingDomain mix ResetLeft CopyRight resetProcess copyProcess
reading_domain_transport meaningful_recombination_preserved mix_involutive mix_injective
reset_factorizes copy_right_image_iff_diagonal reset_left_image_iff_first_false copy_right_does_not_factorize
reset_step_iff_encoded_copy copy_step_iff_decoded_reset reset_trace_encodes copy_trace_decodes
complete_trace_equivalence infinite_path_equivalence complete_outcome_equivalence
same_paths_different_coordinate_factorization complete_image_correspondence
old_aspect_meanings_still_recombine displayed_restriction_with_preserved_meanings""".split()
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, check=True, timeout=60)


def main():
    baselines = {
        "GenerativeCore": HERE.parent / "inquiry-root/formation-compilation-checks/20261008T095838.361177Z/receipt.json",
        "RelationalFormation": HERE / "relational-formation-checks/20261008T101142.156219Z/receipt.json",
    }
    paths = {"GenerativeCore": HERE.parent / "GenerativeCore.lean",
             "RelationalFormation": HERE / "RelationalFormation.lean", MODULE: HERE / (MODULE + ".lean")}
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    baseline_reports, baseline_bindings = {}, {}
    for name, path in baselines.items():
        data = path.read_bytes()
        receipt = json.loads(data)
        assert receipt["passed"]
        source_hash = receipt["sources"][name]["sha256"] if name == "GenerativeCore" else receipt["source_sha256"]
        assert sha(frozen[name]) == source_hash
        assert (path.parent / (name + ".lean")).read_bytes() == frozen[name]
        audits = receipt["modules"][name]["audits"] if name == "GenerativeCore" else {
            a["declaration"]: a["axioms"] for a in receipt["audits"]}
        baseline_reports[name] = audits
        baseline_bindings[name] = {"receipt": os.path.relpath(path, HERE), "sha256": sha(data)}
    code = frozen[MODULE].decode()
    assert re.findall(r"^import (.+)$", code, re.M) == ["GenerativeCore", "RelationalFormation"]
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
    assert not re.search(r"^\s*(axiom|constant|opaque)\s", code, re.M)
    assert len(re.findall(r"^theorem ", code, re.M)) == 19
    assert set(re.findall(r"^(?:theorem|def) (\w+)", code, re.M)) == set(DECLARATIONS)
    assert re.findall(r"^#print axioms (\w+)$", code, re.M) == DECLARATIONS

    toolchain = (HERE / "lean-toolchain").read_text().strip()
    version = run(["lean", "+" + toolchain, "--version"], HERE).stdout.strip()
    assert "version 4.29.1," in version
    prefix = Path(run(["lean", "+" + toolchain, "--print-prefix"], HERE).stdout.strip())
    compiler = prefix / "bin/lean"
    build = HERE / "relational-coordinate-checks" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
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
        if name in baselines:
            assert audits == baseline_reports[name]
        else:
            assert list(audits) == [MODULE + "." + n for n in DECLARATIONS]
        results[name] = {"source_sha256": sha(frozen[name]), "audits": audits,
                         "log_sha256": sha(result.stdout.encode())}
        print(name + ": " + str(len(audits)) + " empty audits", flush=True)
    assert all(path.read_bytes() == frozen[name] for name, path in paths.items())
    assert Path(__file__).read_bytes() == checker
    for name, path in baselines.items():
        assert sha(path.read_bytes()) == baseline_bindings[name]["sha256"]
    receipt = {
        "passed": True, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "lean_version": version, "compiler_sha256": sha(compiler.read_bytes()),
        "checker_sha256": sha(checker), "modules": results,
        "new_theorems": 19, "new_definitions": 6, "new_empty_audits": 25,
        "inherited_empty_audits": 49, "total_empty_audits": sum(len(m["audits"]) for m in results.values()),
        "baseline_bindings": baseline_bindings, "run_directory": str(build.relative_to(HERE)),
        "scope": "An invertible recoding preserves all model states, steps, finite labelled histories, infinite stepwise histories and decoded endpoint questions while changing displayed coordinate factorization. Transported reading meanings preserve the joint-domain criterion. No physical coordinate choice, actuality or modal exhaustiveness is derived.",
        "logical_basis": "Lean 4.29.1 type theory remains the checking framework; the declared mathematical transition laws and actual interpretation are separate.",
    }
    assert receipt["total_empty_audits"] == 74
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (HERE / "relational-coordinate-verification.json").write_text(serialized)
    print(json.dumps({"passed": True, "new_theorems": 19, "new_empty_audits": 25,
                      "inherited_empty_audits": 49, "run_directory": receipt["run_directory"]}))


if __name__ == "__main__":
    main()
