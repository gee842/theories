#!/usr/bin/env python3
"""Check the finite-basis interpretation reduction in the unchanged calculus."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
MODULE = "JointInterpretation"
DECLARATIONS = """package package_derivable package_iff_list package_iff_basis
basis_iff_relative_closure common_basis_iff_common_closure
pointwise_closure_iff_common pointwise_closure_gives_common_relative
incompatibleRows separate_basis_rows_fit
separate_rows_have_no_common_interpretation
separate_rows_do_not_cover_full_closure""".split()
BASELINE = HERE / "formation-compilation-checks/20261008T095838.361177Z/receipt.json"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    command = ["lean", "+leanprover/lean4:v4.29.1"]
    version = subprocess.check_output(command + ["--version"], text=True).strip()
    assert "version 4.29.1," in version
    compiler = Path(subprocess.check_output(command + ["--print-prefix"], text=True).strip()) / "bin/lean"
    baseline_bytes = BASELINE.read_bytes()
    baseline = json.loads(baseline_bytes)
    inherited = baseline["modules"]["GenerativeClosure"]
    sources = {name:(HERE / (name+".lean")).read_bytes() for name in ["GenerativeClosure", MODULE]}
    assert sha(sources["GenerativeClosure"]) == inherited["source_sha256"]
    assert sha((BASELINE.parent/"GenerativeClosure.lean").read_bytes()) == inherited["source_sha256"]
    assert sha((BASELINE.parent/"GenerativeClosure.log").read_bytes()) == inherited["log_sha256"]
    code = sources[MODULE].decode()
    assert re.findall(r"^import (.+)$", code, re.M) == ["GenerativeClosure"]
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
    assert not re.search(r"^\s*(axiom|constant|opaque)\s", code, re.M)
    assert re.findall(r"^(?:theorem|def) (\w+)", code, re.M) == DECLARATIONS
    assert re.findall(r"^#print axioms (\w+)$", code, re.M) == DECLARATIONS
    checker = Path(__file__).read_bytes()
    build = HERE/"joint-interpretation-checks"/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build.mkdir(parents=True)
    for name,data in sources.items():
        (build/(name+".lean")).write_bytes(data)
    (build/Path(__file__).name).write_bytes(checker)
    (build/"lean-toolchain").write_text("leanprover/lean4:v4.29.1\n")
    modules = {}
    for name,data in sources.items():
        result = subprocess.run([str(compiler), "-o", name+".olean", name+".lean"], cwd=build,
                                env=dict(os.environ, LEAN_PATH=str(build)), text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=60)
        (build/(name+".log")).write_text(result.stdout)
        if result.returncode:
            print(result.stdout)
        assert result.returncode == 0 and "warning:" not in result.stdout, name
        reports = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", result.stdout)
        expected = list(inherited["audits"]) if name == "GenerativeClosure" else ["InquiryRoot.JointInterpretation."+decl for decl in DECLARATIONS]
        assert [decl for decl,_ in reports] == expected
        assert all(not deps.strip() for _,deps in reports)
        modules[name] = {"source_sha256":sha(data), "log_sha256":sha(result.stdout.encode()), "audits":{decl:[] for decl in expected}}
    for name,data in sources.items():
        assert (HERE/(name+".lean")).read_bytes() == data
    assert Path(__file__).read_bytes() == checker
    theorem_count = len(re.findall(r"^theorem ", code, re.M))
    receipt = {
        "passed":True, "checked_at_utc":datetime.now(timezone.utc).isoformat(),
        "lean_version":version, "compiler_sha256":sha(compiler.read_bytes()),
        "checker_sha256":sha(checker), "modules":modules,
        "new_theorems":theorem_count, "new_definitions":len(DECLARATIONS)-theorem_count,
        "new_empty_audits":len(DECLARATIONS), "inherited_empty_audits":len(inherited["audits"]),
        "total_empty_audits":len(DECLARATIONS)+len(inherited["audits"]),
        "run_directory":str(build.relative_to(HERE)),
        "baseline_receipt":str(BASELINE.relative_to(HERE)), "baseline_sha256":sha(baseline_bytes),
        "scope":"Migration of the finite-basis joint-interpretation argument into the existing calculus. Full pointwise closed-theory coverage yields one common admitted interpretation; separate row matching does not. Local premises remain conditional.",
        "logical_basis":"Lean 4.29.1 and unchanged GenerativeClosure. The interpretation carrier, admission predicate, basis and covering finite list remain explicit. No common actual process law or actual admissibility is established.",
    }
    serialized = json.dumps(receipt, indent=2)+"\n"
    (build/"receipt.json").write_text(serialized)
    (HERE/"joint-interpretation-verification.json").write_text(serialized)
    print(json.dumps({key:receipt[key] for key in ["passed","new_theorems","new_definitions","new_empty_audits","inherited_empty_audits","total_empty_audits","run_directory"]}))


if __name__ == "__main__":
    main()
