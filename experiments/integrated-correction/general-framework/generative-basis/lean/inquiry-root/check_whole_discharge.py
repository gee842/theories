#!/usr/bin/env python3
"""Freeze and check the three-module whole-discharge dependency closure."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
MODULES = ["GenerativeClosure", "CoreTreeRearticulation", "WholeTheoryDischarge"]
IMPORTS = {"GenerativeClosure": ["Std"],
           "CoreTreeRearticulation": ["GenerativeClosure"],
           "WholeTheoryDischarge": ["CoreTreeRearticulation"]}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          check=True, timeout=60)


def main():
    toolchain = (ROOT.parent / "lean-toolchain").read_text().strip()
    command = ["lean", "+" + toolchain]
    version = run(command + ["--version"], ROOT).stdout.strip()
    assert "version 4.29.1," in version
    compiler = Path(run(command + ["--print-prefix"], ROOT).stdout.strip()) / "bin/lean"
    frozen = {m: (ROOT / (m + ".lean")).read_bytes() for m in MODULES}
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build = ROOT / "whole-discharge-checks" / stamp
    build.mkdir(parents=True)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    results = []
    for module in MODULES:
        code = frozen[module].decode()
        assert re.findall(r"^import (.+)$", code, re.M) == IMPORTS[module]
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", code, re.M)
        requests = re.findall(r"^#print axioms (\S+)", code, re.M)
        assert requests and len(requests) == len(set(requests))
        (build / (module + ".lean")).write_bytes(frozen[module])
        checked = run([str(compiler), "-o", module + ".olean", module + ".lean"],
                      build, dict(os.environ, LEAN_PATH=str(build)))
        (build / (module + ".txt")).write_text(checked.stdout)
        found = AUDIT.findall(checked.stdout)
        assert [name for name, _ in found] == requests
        audits = [{"declaration": name,
                   "axioms": [s.strip() for s in raw.split(",") if s.strip()]}
                  for name, raw in found]
        allowed = set() if module == "WholeTheoryDischarge" else {"propext"}
        assert all(set(item["axioms"]) <= allowed for item in audits)
        if module == "WholeTheoryDischarge":
            assert len(re.findall(r"^theorem ", code, re.M)) == 5
            assert len(audits) == 7
        results.append({"module": module, "source_sha256": sha(frozen[module]),
                        "audits": audits})
    assert all((ROOT / (m + ".lean")).read_bytes() == frozen[m] for m in MODULES)
    receipt = {"checked_at": datetime.now(timezone.utc).isoformat(),
               "lean_version": version, "compiler_sha256": sha(compiler.read_bytes()),
               "checker_sha256": sha(Path(__file__).read_bytes()),
               "modules": results, "new_checked_theorems": 5,
               "new_content_scope": "Four discharge results plus an axiom-free reproof of inherited soundness.",
               "new_declaration_audits": 7, "new_axioms": [],
               "run_directory": str(build.relative_to(ROOT)),
               "scope": "Well-founded proof substitution; no instance for the actual foundational process law.",
               "logical_basis": "The existing calculus and Lean 4.29.1 remain the formal framework."}
    text = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(text)
    (ROOT / "whole-discharge-verification.json").write_text(text)
    inherited = [a for m in results[:-1] for a in m["audits"]]
    print(json.dumps({"new_theorems": 5, "new_empty_audits": 7,
                      "inherited_audits": len(inherited),
                      "inherited_empty": sum(not a["axioms"] for a in inherited),
                      "inherited_propext": sum(bool(a["axioms"]) for a in inherited),
                      "receipt": str(build / "receipt.json")}))


if __name__ == "__main__":
    main()
