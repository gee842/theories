#!/usr/bin/env python3
"""Freeze and kernel-check the relational-formation necessity and scope tests."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
MODULE = "RelationalFormation"
DECLARATIONS = """Rectangular Post Separate Factorizes Reach Full Diagonal Copy Identity Select Reset
rectangular_transport product_rectangular separate_post_rectangular factorized_post_rectangular
new_restriction_excludes_factorization separate_reach_rectangular restricted_target_has_no_separate_history
full_rectangular diagonal_not_rectangular copy_post_iff_diagonal copy_does_not_factorize identity_post_iff
identity_factorizes inherited_restriction_without_new_coupling selection_iff_diagonal
selection_can_introduce_restriction fixed_common_mode_rectangular varying_common_mode_not_rectangular
reset_erases_restriction""".split()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, check=True, timeout=60)


def main():
    toolchain = (HERE / "lean-toolchain").read_text().strip()
    command = ["lean", "+" + toolchain]
    version = run(command + ["--version"], HERE).stdout.strip()
    assert "version 4.29.1," in version
    prefix = Path(run(command + ["--print-prefix"], HERE).stdout.strip())
    compiler = prefix / "bin/lean"
    source = HERE / (MODULE + ".lean")
    frozen = source.read_bytes()
    checker = Path(__file__).read_bytes()
    code = frozen.decode()
    assert re.findall(r"^import (.+)$", code, re.M) == ["Init"]
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
    assert not re.search(r"^\s*(axiom|constant|opaque)\s", code, re.M)
    assert len(re.findall(r"^theorem ", code, re.M)) == 19
    assert set(re.findall(r"^(?:theorem|def) (\w+)", code, re.M)) == set(DECLARATIONS)
    assert re.findall(r"^#print axioms (\w+)$", code, re.M) == DECLARATIONS
    build = HERE / "relational-formation-checks" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build.mkdir(parents=True)
    (build / source.name).write_bytes(frozen)
    (build / Path(__file__).name).write_bytes(checker)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    result = run([str(compiler), "-o", MODULE + ".olean", source.name],
                 build, dict(os.environ, LEAN_PATH=str(build)))
    (build / "compiler.txt").write_text(result.stdout)
    assert "warning:" not in result.stdout
    audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", result.stdout)
    expected = [MODULE + "." + name for name in DECLARATIONS]
    assert [name for name, _ in audits] == expected
    assert all(not axioms.strip() for _, axioms in audits)
    assert source.read_bytes() == frozen and Path(__file__).read_bytes() == checker
    receipt = {
        "passed": True, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "lean_version": version, "compiler_sha256": sha(compiler.read_bytes()),
        "module": MODULE, "source_sha256": sha(frozen), "checker_sha256": sha(checker),
        "log_sha256": sha(result.stdout.encode()), "imports": ["Init"],
        "new_theorems": 19, "definition_audits": 11,
        "audits": [{"declaration": name, "axioms": []} for name in expected],
        "run_directory": str(build.relative_to(HERE)),
        "scope": "A universally quantified restriction on independent formation, with explicit domain/recombination hypotheses; finite iteration and inherited, selected, shared-mode and erasure controls. No statistical or universal causal identification is inferred.",
        "logical_basis": "Lean 4.29.1 type theory and Init remain the checking framework. Actual modal domains, coordinate meanings and transition correspondence are not derived.",
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (HERE / "relational-formation-verification.json").write_text(serialized)
    print(json.dumps({"passed": True, "new_theorems": 19, "empty_audits": 30,
                      "receipt": str(build / "receipt.json")}))


if __name__ == "__main__":
    main()
