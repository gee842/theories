#!/usr/bin/env python3
"""Recheck formation after changing only Lean's sparse-match compilation option.

Historical definitions and equivalence proofs are diagnostic controls, kept out
of the production module closure. They can retain the old propext dependency.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
BASELINE = HERE / "inquiry-repair-checks/20261008T093847.617193Z/receipt.json"
INSERTION = ("import Std\n\n"
             "-- Use ordinary case compilation to avoid an unnecessary propext dependency.\n"
             "set_option backward.match.sparseCases false\n")
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
EQUIVALENCES = {
    "enabled_same": ("(material : Nat) (s : State) (a : Event)",
                     "Legacy.Enabled material s a ↔ FormedSelection.Enabled material s a",
                     "cases s with\n  | mk af hf resident intact localFuel fuel source =>\n"
                     "    cases a <;> cases resident <;> rfl"),
    "advance_same": ("(s : State) (a : Event)",
                     "Legacy.advance s a = FormedSelection.advance s a", "cases a <;> rfl"),
    "step_same": ("(material : Nat) (s t : State) (a : Event)",
                  "Legacy.Step material s a t ↔ FormedSelection.Step material s a t",
                  "cases s with\n  | mk af hf resident intact localFuel fuel source =>\n"
                  "    cases a <;> cases resident <;> rfl"),
    "expenditure_same": ("(a : Event)",
                         "Legacy.expenditure a = FormedSelection.expenditure a", "cases a <;> rfl"),
    "common_expenditure_same": ("(a : Event)",
                                "Legacy.commonExpenditure a = FormedSelection.commonExpenditure a",
                                "cases a <;> rfl"),
    "copy_increment_same": ("(a : Event)",
                            "Legacy.copyIncrement a = FormedSelection.copyIncrement a", "cases a <;> rfl"),
    "rank_drop_same": ("(a : Event)",
                       "Legacy.rankDrop a = FormedSelection.rankDrop a", "cases a <;> rfl"),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=60)


def main():
    baseline_bytes = BASELINE.read_bytes()
    baseline = json.loads(baseline_bytes)
    assert baseline["passed"] and baseline["audit_count"] == 424
    paths = [(n, REPO / s["path"]) for n, s in baseline["sources"].items()]
    frozen = {n: p.read_bytes() for n, p in paths}
    for name, _ in paths:
        old = (BASELINE.parent / (name + ".lean")).read_bytes()
        assert sha(old) == baseline["sources"][name]["sha256"]
        expected = old
        if name == "FormedSelection":
            assert old.count(b"import Std\n") == 1
            expected = old.replace(b"import Std\n", INSERTION.encode(), 1)
        assert frozen[name] == expected, "Unexpected source change: " + name
    original = (BASELINE.parent / "FormedSelection.lean").read_text()
    blocks = re.findall(r"^def [\s\S]*?(?=\n(?:def |theorem |instance |inductive |structure |variable |#print |/--|end )|\Z)", original, re.M)
    definitions = re.findall(r"^def (\w+)", original, re.M)
    assert len(blocks) == len(definitions) == 35
    for text in [frozen["FormedSelection"].decode(), *blocks]:
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text)
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", text, re.M)

    toolchain = (HERE.parent / "lean-toolchain").read_text().strip()
    version = run(["lean", "+" + toolchain, "--version"], HERE)
    assert version.returncode == 0 and "version 4.29.1," in version.stdout
    prefix = run(["lean", "+" + toolchain, "--print-prefix"], HERE)
    assert prefix.returncode == 0
    compiler = Path(prefix.stdout.strip()) / "bin/lean"
    assert sha(compiler.read_bytes()) == baseline["compiler_sha256"]
    build = HERE / "formation-compilation-checks" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build.mkdir(parents=True)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    (build / Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    for name, _ in paths:
        (build / (name + ".lean")).write_bytes(frozen[name])

    def compile_module(name, directory):
        source = directory / (name + ".lean")
        result = run([str(compiler), "-o", name + ".olean", name + ".lean"],
                     directory, dict(os.environ, LEAN_PATH=str(directory)))
        (directory / (name + ".log")).write_text(result.stdout)
        assert result.returncode == 0 and "warning:" not in result.stdout, name + "\n" + result.stdout
        requests = re.findall(r"^#print axioms (\S+)", source.read_text(), re.M)
        audits = {n: [x.strip() for x in a.split(",") if x.strip()]
                  for n, a in AUDIT.findall(result.stdout)}
        assert len(audits) == len(requests)
        for request, actual in zip(requests, audits):
            assert actual == request or actual.endswith("." + request)
        return {"audits": audits, "source_sha256": sha(source.read_bytes()),
                "log_sha256": sha(result.stdout.encode())}

    # Recompile the old native definitions, rather than relying on a copied summary.
    before_dir = build / "before"
    before_dir.mkdir()
    (before_dir / "FormedSelection.lean").write_text(original)
    before_module = compile_module("FormedSelection", before_dir)
    assert before_module["audits"] == baseline["modules"]["FormedSelection"]["audits"]
    definition_source = "import FormedSelection\n" + "\n".join(
        "#print axioms FormedSelection." + n for n in definitions) + "\n"
    (before_dir / "FormationDefinitions.lean").write_text(definition_source)
    before_defs = compile_module("FormationDefinitions", before_dir)

    results, reductions = {}, []
    for name, _ in paths:
        result = compile_module(name, build)
        before = baseline["modules"][name]["audits"]
        assert set(result["audits"]) == set(before)
        for declaration, deps in result["audits"].items():
            assert set(deps) <= set(before[declaration])
            if before[declaration] != deps:
                reductions.append({"module": name, "declaration": declaration,
                                   "before": before[declaration], "after": deps})
        results[name] = result
        print(name + ": " + str(len(result["audits"])) + " audits", flush=True)
    (build / "FormationDefinitions.lean").write_text(definition_source)
    after_defs = compile_module("FormationDefinitions", build)
    assert all(not a for a in after_defs["audits"].values())

    control = ("import FormedSelection\n\nnamespace FormationCompilationControl\n"
               "open FormedSelection\nset_option backward.match.sparseCases true\nnamespace Legacy\n\n"
               + "\n\n".join(b.strip() for b in blocks)
               + "\n\nend Legacy\nset_option backward.match.sparseCases false\n\n")
    for name, (args, proposition, proof) in EQUIVALENCES.items():
        control += f"theorem {name} {args} :\n    {proposition} := by\n  {proof}\n\n"
    control += "\n".join("#print axioms Legacy." + n for n in definitions) + "\n"
    control += "\n".join("#print axioms " + n for n in EQUIVALENCES) + "\nend FormationCompilationControl\n"
    (build / "FormationCompilationControl.lean").write_text(control)
    control_result = compile_module("FormationCompilationControl", build)
    for name in definitions:
        assert control_result["audits"]["FormationCompilationControl.Legacy." + name] == before_defs["audits"]["FormedSelection." + name]
    assert all(set(a) <= {"propext"} for a in control_result["audits"].values())
    assert all(p.read_bytes() == frozen[n] for n, p in paths)
    assert Path(__file__).read_bytes() == (build / Path(__file__).name).read_bytes()
    assert BASELINE.read_bytes() == baseline_bytes
    all_audits = [a for m in results.values() for a in m["audits"].values()]
    assert len(all_audits) == 424
    assert len([r for r in reductions if r["module"] == "FormedSelection" and not r["after"]]) == 7
    receipt = {
        "passed": True, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "lean_version": version.stdout.strip(), "compiler_sha256": sha(compiler.read_bytes()),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "sources": {n: {"path": str(p.relative_to(REPO)), "sha256": sha(frozen[n])} for n, p in paths},
        "modules": results, "module_count": len(results), "audit_count": len(all_audits),
        "empty_audits": sum(not a for a in all_audits),
        "standard_dependency_audits": sum(bool(a) for a in all_audits),
        "dependency_reductions": reductions,
        "definition_audits_before": before_defs, "definition_audits_after": after_defs,
        "control": control_result, "new_control_theorems": len(EQUIVALENCES),
        "control_scope": "Same public State/Event types; all 35 old definition blocks reproduced verbatim under the old match option. Seven pointwise equivalences cover all event constructors and unbounded natural-number states. Legacy definitions and six equivalences retain propext; these diagnostics are not imported by the production model.",
        "baseline_receipt": str(BASELINE.relative_to(REPO)), "baseline_receipt_sha256": sha(baseline_bytes),
        "exact_source_change": {"old": "import Std\n", "new": INSERTION},
        "scope": "Only the compiler option changes; every original equation, proof body, statement and local premise is preserved. This does not derive the actual universal process law or its interpretation.",
        "logical_basis": "Lean 4.29.1 type theory is the checking framework. Empty audits do not derive that framework from nothing.",
        "run_directory": str(build.relative_to(REPO)),
    }
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (HERE / "formation-compilation-verification.json").write_text(serialized)
    print(json.dumps({k: receipt[k] for k in ["passed", "module_count", "audit_count", "empty_audits", "standard_dependency_audits", "run_directory"]}))


if __name__ == "__main__":
    main()
