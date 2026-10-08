#!/usr/bin/env python3
"""Check proof-only inquiry repairs against the compiled closure baseline."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
TARGETS = {"GenerativeClosure", "CoreTreeRearticulation", "WholeTheoryDischarge", "InquiryFamilies"}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=60)


def main():
    edits_path = HERE / "inquiry-repair-proof-edits.json"
    edits = json.loads(edits_path.read_text())
    baseline_path = REPO / edits["baseline_receipt"]
    assert sha(baseline_path.read_bytes()) == edits["baseline_receipt_sha256"]
    baseline = json.loads(baseline_path.read_text())
    assert baseline["passed"] and baseline["audit_count"] == 423
    paths = [(name, REPO / item["path"]) for name, item in baseline["sources"].items()]
    frozen = {name: path.read_bytes() for name, path in paths}
    for name, _ in paths:
        old = (baseline_path.parent / (name + ".lean")).read_bytes()
        assert sha(old) == baseline["sources"][name]["sha256"]
        if name != "InquiryFamilies":
            assert frozen[name] == old, "Concurrent source change: " + name
    previous = (baseline_path.parent / "InquiryFamilies.lean").read_bytes()
    assert sha(previous) == edits["before_sha256"]
    replay = previous.decode()
    for edit in edits["proof_replacements"]:
        match = re.search(r"^theorem " + edit["theorem"] + r"\b[\s\S]*?:= by\n", replay, re.M)
        assert match
        end = re.search(r"\n(?=theorem |def |structure |/--|#print)", replay[match.end():])
        assert end
        stop = match.end() + end.start()
        assert replay[match.end():stop] == edit["old_body"]
        replay = replay[:match.end()] + edit["new_body"] + replay[stop:]
    term = edits["term_replacement"]
    assert replay.count(term["old"]) == 1
    replay = replay.replace(term["old"], term["new"])
    replay = replay.replace("theorem threshold_available_iff", edits["added_helper"] + "theorem threshold_available_iff")
    replay = replay.replace("#print axioms InquiryRoot.threshold_available_iff",
                            edits["added_audit"] + "#print axioms InquiryRoot.threshold_available_iff")
    assert replay.encode() == frozen["InquiryFamilies"]
    assert sha(frozen["InquiryFamilies"]) == edits["after_sha256"]
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", replay)
    assert not re.search(r"^\s*(axiom|constant|opaque)\s", replay, re.M)
    old_names = set(re.findall(r"^theorem (\w+)", previous.decode(), re.M))
    new_names = set(re.findall(r"^theorem (\w+)", replay, re.M))
    assert len(old_names) == 15 and new_names - old_names == {"unit_replicate_length"}

    toolchain = (HERE.parent / "lean-toolchain").read_text().strip()
    command = ["lean", "+" + toolchain]
    version = run(command + ["--version"], HERE)
    assert version.returncode == 0 and "version 4.29.1," in version.stdout
    prefix = run(command + ["--print-prefix"], HERE)
    assert prefix.returncode == 0
    compiler = Path(prefix.stdout.strip()) / "bin/lean"
    build = HERE / "inquiry-repair-checks" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    build.mkdir(parents=True)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    (build / Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    (build / edits_path.name).write_bytes(edits_path.read_bytes())
    for name, _ in paths:
        (build / (name + ".lean")).write_bytes(frozen[name])
    results, reductions = {}, []
    for name, _ in paths:
        result = run([str(compiler), "-o", name + ".olean", name + ".lean"],
                     build, dict(os.environ, LEAN_PATH=str(build)))
        (build / (name + ".log")).write_text(result.stdout)
        assert result.returncode == 0 and "warning:" not in result.stdout, name + "\n" + result.stdout
        requests = re.findall(r"^#print axioms (\S+)", frozen[name].decode(), re.M)
        audits = {n: [x.strip() for x in a.split(",") if x.strip()]
                  for n, a in AUDIT.findall(result.stdout)}
        assert len(audits) == len(requests)
        for requested, actual in zip(requests, audits):
            assert actual == requested or actual.endswith("." + requested)
        before = baseline["modules"][name]["audits"]
        assert set(audits) == set(before) | ({"InquiryRoot.unit_replicate_length"} if name == "InquiryFamilies" else set())
        for declaration, dependencies in audits.items():
            assert set(dependencies) <= set(before.get(declaration, []))
            if declaration in before and before[declaration] != dependencies:
                reductions.append({"module": name, "declaration": declaration,
                                   "before": before[declaration], "after": dependencies})
        if name in TARGETS:
            assert all(not a for a in audits.values())
            theorem_names = set(re.findall(r"^theorem (\w+)", frozen[name].decode(), re.M))
            assert theorem_names <= {n.split(".")[-1] for n in audits}
        results[name] = {"audits": audits, "log_sha256": sha(result.stdout.encode())}
        print(name + ": " + str(len(audits)) + " audits", flush=True)
    assert all(path.read_bytes() == frozen[name] for name, path in paths)
    assert len(reductions) == 13 and all(r["module"] == "InquiryFamilies" and not r["after"] for r in reductions)
    all_audits = [a for m in results.values() for a in m["audits"].values()]
    target_audits = [a for m in TARGETS for a in results[m]["audits"].values()]
    assert len(all_audits) == 424 and len(target_audits) == 40
    receipt = {"passed": True, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
               "lean_version": version.stdout.strip(), "compiler_sha256": sha(compiler.read_bytes()),
               "checker_sha256": sha(Path(__file__).read_bytes()), "proof_edits_sha256": sha(edits_path.read_bytes()),
               "sources": {n: {"path": str(p.relative_to(REPO)), "sha256": sha(frozen[n])} for n, p in paths},
               "modules": results, "module_count": len(results), "audit_count": len(all_audits),
               "empty_audits": sum(not a for a in all_audits),
               "standard_dependency_audits": sum(bool(a) for a in all_audits),
               "target_audits": len(target_audits), "target_empty_audits": sum(not a for a in target_audits),
               "existing_inquiry_theorems": 15, "supporting_reproofs_added": 1,
               "dependency_reductions": reductions, "baseline_receipt": str(baseline_path.relative_to(REPO)),
               "baseline_receipt_sha256": sha(baseline_path.read_bytes()),
               "scope": "Original clipped-observation and spending proofs, without altered definitions or existing statements. This does not derive the actual universal process law.",
               "logical_basis": "Lean 4.29.1 type theory remains the checking framework. Other implementation proofs retain explicitly reported standard dependencies.",
               "run_directory": str(build.relative_to(REPO))}
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (HERE / "inquiry-repair-verification.json").write_text(serialized)
    print(json.dumps({k: receipt[k] for k in ["passed", "module_count", "audit_count", "empty_audits", "standard_dependency_audits", "target_empty_audits", "run_directory"]}))


if __name__ == "__main__":
    main()
