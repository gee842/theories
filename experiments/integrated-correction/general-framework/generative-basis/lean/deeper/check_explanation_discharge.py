#!/usr/bin/env python3
"""Check the explanation-to-claim inference, without assuming actual coverage."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
MODULE = "ExplanationDischarge"
DECLARATIONS = [
    "consequence_iff_witness_implication",
    "uniform_discharge_iff_witness",
    "empty_interface_satisfies_every_requirement",
    "covered_targets_inherit_consequence",
]


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
    prefix = Path(run(command + ["--print-prefix"], HERE).stdout.strip())
    compiler = prefix / "bin/lean"
    source = HERE / (MODULE + ".lean")
    frozen = source.read_bytes()
    checker = Path(__file__).read_bytes()
    code = frozen.decode()
    assert re.findall(r"^import (.+)$", code, re.M) == ["Init"]
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
    assert not re.search(r"^\s*(axiom|constant|opaque)\s", code, re.M)
    assert re.findall(r"^(?:theorem|def) (\w+)", code, re.M) == DECLARATIONS
    assert re.findall(r"^#print axioms (\w+)$", code, re.M) == DECLARATIONS
    build = HERE / "explanation-discharge-checks" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build.mkdir(parents=True)
    (build / source.name).write_bytes(frozen)
    (build / Path(__file__).name).write_bytes(checker)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    result = run([str(compiler), "-o", MODULE + ".olean", source.name], build,
                 dict(os.environ, LEAN_PATH=str(build)))
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
        "new_theorems": 4,
        "audits": [{"declaration": name, "axioms": []} for name in expected],
        "run_directory": str(build.relative_to(HERE)),
        "scope": "An exact audit of one inference from requirements on admitted explanations to a claim. Universal discharge needs a witness; coverage and substantive consequence remain separate premises of the positive route. This is not a physical countermodel or an impossibility result for the foundation.",
        "logical_basis": "Lean 4.29.1 type theory and Init. The formal interface does not define adequate explanation or establish any actual generative law. No new foundational premise is adopted.",
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (HERE / "explanation-discharge-verification.json").write_text(serialized)
    print(json.dumps({"passed": True, "new_theorems": 4, "empty_audits": 4,
                      "receipt": str(build / "receipt.json")}))


if __name__ == "__main__":
    main()
