#!/usr/bin/env python3
"""Freeze and check the necessary symmetry restriction and its branching control."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
MODULE = "FormationSymmetry"
DECLARATIONS = """PreservesSteps UniqueAfter fixed_start_unique_end
changed_end_exhibits_alternative asymmetry_excludes_joint_contract
outcome_domain_symmetric step_uniqueness_implies_trace_uniqueness
exchange branching exchange_involutive exchange_fixes_unselected exchange_changes_formed
branching_preserves_exchange formed_branch_retained either_branch_forms_and_continues
formed_branch_cannot_switch symmetric_law_has_retained_asymmetric_outcomes
seededUpdate seededExchange seeded seeded_update_commutes seeded_preserves_exchange seeded_is_deterministic
seed_supplies_initial_asymmetry seeded_step_projects seeded_trace_projects
seeded_formed_retained either_branch_has_seeded_realization
fixed_seed_does_not_cover_other_branch""".split()
BASELINE = HERE / "operation-role-checks/20261008T104327.892143Z/receipt.json"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          check=True, timeout=60)


def main():
    toolchain = (HERE / "lean-toolchain").read_text().strip()
    command = ["lean", "+" + toolchain]
    version = run(command + ["--version"], HERE).stdout.strip()
    assert "version 4.29.1," in version
    compiler = Path(run(command + ["--print-prefix"], HERE).stdout.strip()) / "bin/lean"
    baseline_bytes = BASELINE.read_bytes()
    baseline = json.loads(baseline_bytes)
    core_expected = baseline["modules"]["GenerativeCore"]
    paths = {"GenerativeCore": HERE.parent / "GenerativeCore.lean", MODULE: HERE / (MODULE + ".lean")}
    sources = {name: path.read_bytes() for name, path in paths.items()}
    assert sha(sources["GenerativeCore"]) == core_expected["source_sha256"]
    assert sha((BASELINE.parent / "GenerativeCore.lean").read_bytes()) == core_expected["source_sha256"]
    assert sha((BASELINE.parent / "GenerativeCore.log").read_bytes()) == core_expected["log_sha256"]
    code = sources[MODULE].decode()
    assert re.findall(r"^import (.+)$", code, re.M) == ["GenerativeCore"]
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
    assert not re.search(r"^\s*(axiom|constant|opaque)\s", code, re.M)
    assert re.findall(r"^(?:theorem|def) (\w+)", code, re.M) == DECLARATIONS
    assert re.findall(r"^#print axioms (\w+)$", code, re.M) == DECLARATIONS
    theorem_count = len(re.findall(r"^theorem ", code, re.M))
    checker = Path(__file__).read_bytes()
    build = HERE / "formation-symmetry-checks" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build.mkdir(parents=True)
    for name, data in sources.items():
        (build / (name + ".lean")).write_bytes(data)
    (build / Path(__file__).name).write_bytes(checker)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    modules = {}
    for name in sources:
        result = subprocess.run([str(compiler), "-o", name + ".olean", name + ".lean"],
                                cwd=build, env=dict(os.environ, LEAN_PATH=str(build)),
                                text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                timeout=60)
        (build / (name + ".log")).write_text(result.stdout)
        if result.returncode:
            print(result.stdout)
        assert result.returncode == 0 and "warning:" not in result.stdout, name
        reports = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", result.stdout)
        expected = list(core_expected["audits"]) if name == "GenerativeCore" else [MODULE + "." + decl for decl in DECLARATIONS]
        assert [decl for decl, _ in reports] == expected
        assert all(not dependencies.strip() for _, dependencies in reports)
        modules[name] = {"source_sha256": sha(sources[name]), "log_sha256":sha(result.stdout.encode()),
                         "audits": {decl:[] for decl in expected}}
    for name, path in paths.items():
        assert path.read_bytes() == sources[name]
    assert Path(__file__).read_bytes() == checker
    receipt = {
        "passed": True, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "lean_version": version, "compiler_sha256":sha(compiler.read_bytes()),
        "checker_sha256":sha(checker), "modules":modules,
        "new_theorems":theorem_count, "new_definitions":len(DECLARATIONS)-theorem_count,
        "new_empty_audits":len(DECLARATIONS), "inherited_empty_audits":len(core_expected["audits"]),
        "total_empty_audits":len(DECLARATIONS)+len(core_expected["audits"]),
        "run_directory":str(build.relative_to(HERE)),
        "baseline_receipt":str(BASELINE.relative_to(HERE)), "baseline_sha256":sha(baseline_bytes),
        "scope":"Necessary symmetry restrictions on finite histories, retained asymmetric branches under a symmetric relation, and a seeded refinement that fails uniform lifting. The common actual process law is not derived.",
        "logical_basis":"Lean 4.29.1 and the unchanged GenerativeCore. Configuration identity, transformation, action interface and step relation remain explicit; no universal determinism or symmetry premise is adopted.",
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (HERE / "formation-symmetry-verification.json").write_text(serialized)
    print(json.dumps({key:receipt[key] for key in ["passed", "new_theorems", "new_definitions", "new_empty_audits", "inherited_empty_audits", "total_empty_audits", "run_directory"]}))


if __name__ == "__main__":
    main()
