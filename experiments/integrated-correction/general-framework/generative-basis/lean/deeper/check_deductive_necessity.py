#!/usr/bin/env python3
"""Check the deductive-necessity inference audit in a frozen build directory."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
MODULE = "DeductiveNecessity"
DECLARATIONS = [
    "Possible", "Necessary", "actual_gives_possible",
    "return_gives_necessary_possibility",
    "uniform_possibility_transfer_iff_return",
    "uniform_truth_transfer_iff_single_case", "one_way_comparison_separates",
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          check=True, timeout=60)


def main():
    toolchain = (ROOT / "lean-toolchain").read_text().strip()
    command = ["lean", "+" + toolchain]
    version = run(command + ["--version"], ROOT).stdout.strip()
    assert "version 4.29.1," in version, version
    prefix = Path(run(command + ["--print-prefix"], ROOT).stdout.strip())
    compiler = prefix / "bin" / "lean"
    source = ROOT / (MODULE + ".lean")
    frozen = source.read_bytes()
    code = frozen.decode()
    assert re.findall(r"^import (.+)$", code, re.M) == ["Init"]
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
    assert not re.search(r"^\s*(axiom|constant)\s", code, re.M)
    assert len(re.findall(r"^theorem ", code, re.M)) == 5
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build = ROOT / "deductive-necessity-checks" / stamp
    build.mkdir(parents=True)
    (build / source.name).write_bytes(frozen)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    result = run([str(compiler), "-o", MODULE + ".olean", source.name],
                 build, dict(os.environ, LEAN_PATH=str(build)))
    (build / "compiler.txt").write_text(result.stdout)
    audits = re.findall(
        r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
        result.stdout)
    expected = ["Generative.DeductiveNecessity." + name for name in DECLARATIONS]
    assert [name for name, _ in audits] == expected, audits
    assert all(not axioms.strip() for _, axioms in audits), audits
    assert source.read_bytes() == frozen, "Source changed during checking"
    receipt = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "lean_version": version, "compiler_sha256": sha(compiler.read_bytes()),
        "module": MODULE, "source_sha256": sha(frozen),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "imports": ["Init"], "new_theorems": 5,
        "audits": [{"declaration": name, "axioms": []} for name in expected],
        "run_directory": str(build.relative_to(ROOT)),
        "scope": "Inference schemas over a supplied comparison relation; no actual modal or process law established.",
        "logical_basis": "Lean 4.29.1 type theory and Init remain the checking framework.",
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (ROOT / "deductive-necessity-verification.json").write_text(serialized)
    print(json.dumps({"new_theorems": 5, "empty_audits": 7,
                      "receipt": str(build / "receipt.json")}))


if __name__ == "__main__":
    main()
