#!/usr/bin/env python3
"""Fresh Lean verification against saved native event/state histories.

The producer is neither imported nor executed. Finite correspondence does not
claim compiler refinement for every Python input or an assumption-free theory.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

from check_purpose import code_without_comments

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
NATIVE = REPO / ("experiments/shared-renewal-capability/regulation/retention/formation/"
                 "learning-interface/recording/continuing-dependency")
EVENTS = dict(form_a="formA", form_h="formH", bind_a="associateA", bind_h="associateH",
              repair="repair", capture="capture", copy_a="localCopyA", copy_h="localCopyH",
              bulk_a="bulkCopyA", bulk_h="bulkCopyH", wear_a="wearFreeA", wear_h="wearFreeH",
              wear_resident="wearResident", damage="damage", leak_common="leakCommon", leak_local="leakLocal")
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def seq(xs):
    return "[" + ",".join(str(x) for x in xs) + "]"


def boolstr(value):
    return "true" if value else "false"


def event(name):
    if name == "admit":
        return ".bindTask"
    return "(.plant ." + EVENTS[name[7:]] + ")" if name.startswith("native:") else "." + name


def fixtures(results):
    lines = ["import AcquiredPurposeCriterion", "", "namespace CriterionFixtures",
             "open Generative.AcquiredPurposeCriterion.Native",
             "set_option maxRecDepth 65536", "set_option maxHeartbeats 16000000", ""]
    audits = []
    ancestor = results["ancestry"]
    assert ancestor["initial"] == [0, 0, 0, 0, 0, 360, 230]
    current = ancestor["initial"]
    snapshots = [current]
    for e, row in zip(ancestor["events"], ancestor["steps"], strict=True):
        assert row["event"] == e and row["before"] == current
        current = row["after"]
        snapshots.append(current)
    assert current == ancestor["final"]
    lines += ["def ancestorStart : FormedSelection.State := ⟨0,0,.empty,false,false,360,230⟩",
              "def ancestorWord : List FormedSelection.Event := " + seq("." + EVENTS[e] for e in ancestor["events"]),
              "def ancestorStates : List (List Nat) := " + seq(seq(x) for x in snapshots),
              "theorem ancestor_correspondence : plantAdmitted 78 ancestorStart ancestorWord = true ∧",
              "    plantVectors ancestorStart ancestorWord = ancestorStates ∧",
              "    plantRun ancestorStart ancestorWord = initial.plant := by decide",
              "theorem ancestor_is_actual_trace : Generative.Trace (plantProcess 78) ancestorStart",
              "    ancestorWord initial.plant := by",
              "  have h := plant_admitted_is_actual_trace 78 ancestorStart ancestorWord ancestor_correspondence.1",
              "  rw [ancestor_correspondence.2.2] at h", "  exact h", ""]
    audits += ["ancestor_correspondence", "ancestor_is_actual_trace"]
    total_events = 0
    total_snapshots = 0
    denials = 0
    for case in results["cases"]:
        name = case["name"]
        assert re.fullmatch(r"[a-z_]+", name)
        cfg = case["config"]
        lines += [f"def {name}_config : Config := {{ receiptMode := {cfg['receipt_mode']}, "
                  f"clamp := {boolstr(cfg['clamp'])}, laterRepair := {boolstr(cfg['later_repair'])}, "
                  f"forceBulk := {boolstr(cfg['force_bulk'])} }}",
                  f"def {name}_word : List Event := " + seq(event(e) for e in case["events"])]
        current = case["initial"]
        assert current == [38,39,1,1,1,293,216,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0]
        snapshots = [current]
        for e, row in zip(case["events"], case["steps"], strict=True):
            assert row["event"] == e and row["before"] == current
            current = row["after"]
            assert len(current) == 23 and all(type(x) is int and x >= 0 for x in current)
            snapshots.append(current)
        assert current == case["final"]
        assert all(v in snapshots for v in case["milestones"].values())
        lines += [f"def {name}_states : List (List Nat) := " + seq(seq(x) for x in snapshots)]
        claims = [f"admitted {name}_config initial {name}_word = true",
                  f"vectors {name}_config initial {name}_word = {name}_states",
                  f"vector (run {name}_config initial {name}_word) = " + seq(case["final"])]
        for denied in case["denied"]:
            assert denied["state"] in snapshots
            index = snapshots.index(denied["state"])
            claims.append(f"enabled (run {name}_config initial ({name}_word.take {index})) "
                          f"{name}_config {event(denied['event'])} = false")
            denials += 1
        if name == "faithful":
            claims.append(f"{name}_word = faithfulWord")
        if name == "clamped":
            claims.append(f"{name}_word = clampedWord")
        lines += [f"theorem {name}_correspondence : " + " ∧\n    ".join(claims) + " := by decide", ""]
        audits.append(f"{name}_correspondence")
        total_events += len(case["events"])
        total_snapshots += len(snapshots)
    lines += ["end CriterionFixtures", ""]
    lines += ["#print axioms CriterionFixtures." + a for a in audits]
    return "\n".join(lines) + "\n", dict(cases=len(results["cases"]), wrapper_events=total_events,
        wrapper_states=total_snapshots, coordinates_per_state=23, denied_events=denials,
        ancestral_events=len(ancestor["events"]), ancestral_states=len(ancestor["events"])+1)


def main():
    result_path = NATIVE / "criterion-results.json"
    result_bytes = result_path.read_bytes()
    results = json.loads(result_bytes)
    assert results["status"] == "passed"
    bindings = {REPO / p: digest for p, digest in results["source_hashes"].items()}
    for path, digest in bindings.items():
        assert sha(path.read_bytes()) == digest, path
    fixture_source, counts = fixtures(results)
    paths = dict(GenerativeCore=HERE.parent / "lean/GenerativeCore.lean",
                 FormedSelection=REPO / "experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean",
                 AcquiredPurposeCriterion=HERE / "AcquiredPurposeCriterion.lean")
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    frozen["CriterionFixtures"] = fixture_source.encode()
    new = {"AcquiredPurposeCriterion", "CriterionFixtures"}
    requested = {}
    seen = set()
    for name, data in frozen.items():
        code = code_without_comments(data.decode())
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", code, re.M), name
        assert set(re.findall(r"^import (\S+)$", code, re.M)) <= seen | {"Std"}, name
        seen.add(name)
        requested[name] = re.findall(r"^#print axioms (\S+)$", code, re.M)
        if name in new:
            names = set(re.findall(r"^\s*(?:theorem|lemma) (\w+)", code, re.M))
            assert names == {n.rsplit(".", 1)[-1] for n in requested[name]}, name
    compiler_record_bytes = (HERE / "coformation-verification.json").read_bytes()
    compiler_record = json.loads(compiler_record_bytes)
    compiler = Path(compiler_record["compiler"])
    assert sha(compiler.read_bytes()) == compiler_record["compiler_sha256"]
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    assert "version 4.29.1," in version
    checker = Path(__file__).read_bytes()
    helper_path = HERE / "check_purpose.py"
    helper_bytes = helper_path.read_bytes()
    attempt = HERE / "criterion-checks" / str(time.time_ns())
    attempt.mkdir(parents=True)
    (attempt / "check_criterion.py").write_bytes(checker)
    (attempt / "check_purpose.py").write_bytes(helper_bytes)
    for name, data in frozen.items():
        (attempt / (name + ".lean")).write_bytes(data)
    source_bindings = {name: dict(source=str(paths[name].relative_to(REPO)) if name in paths else
        str((attempt / (name + ".lean")).relative_to(REPO)), sha256=sha(data)) for name, data in frozen.items()}
    (attempt / "inputs.json").write_text(json.dumps(source_bindings, indent=2) + "\n")
    rows = []
    with tempfile.TemporaryDirectory(prefix="criterion-fresh-lean-") as directory:
        build = Path(directory)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in frozen:
            result = subprocess.run([str(compiler), "-o", name + ".olean", name + ".lean"],
                cwd=build, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
            log = attempt / (name + ".txt")
            log.write_text(result.stdout)
            audits = {n: sorted(a.strip() for a in deps.split(",") if a.strip()) for n, deps in AUDIT.findall(result.stdout)}
            passed = result.returncode == 0 and "warning:" not in result.stdout
            passed = passed and list(audits) == requested[name]
            passed = passed and all(set(a) <= {"propext", "Quot.sound", "Classical.choice"} for a in audits.values())
            rows.append(dict(module=name, **source_bindings[name], new=name in new, passed=passed,
                exit_code=result.returncode, axioms_by_declaration=audits,
                log=str(log.relative_to(HERE)), log_sha256=sha(log.read_bytes())))
            print(json.dumps(dict(module=name, passed=passed, audits=len(audits))), flush=True)
            if not passed:
                print(result.stdout, flush=True)
                break
    stable = all(path.read_bytes() == frozen[name] for name, path in paths.items())
    stable = stable and result_path.read_bytes() == result_bytes
    stable = stable and all(sha(path.read_bytes()) == digest for path, digest in bindings.items())
    stable = stable and Path(__file__).read_bytes() == checker and helper_path.read_bytes() == helper_bytes
    passed = len(rows) == len(frozen) and all(r["passed"] for r in rows) and stable
    record = dict(status="passed" if passed else "failed", checked_at_utc=datetime.now(timezone.utc).isoformat(),
        compiler=str(compiler), compiler_sha256=sha(compiler.read_bytes()), version=version,
        checker_sha256=sha(checker), checker_helper_sha256=sha(helper_bytes),
        native_results=str(result_path.relative_to(REPO)), native_results_sha256=sha(result_bytes),
        native_source_bindings={str(p.relative_to(REPO)): d for p,d in bindings.items()},
        fresh_temporary_build=True, inputs_unchanged=stable, correspondence=counts, modules=rows,
        new_audits=sum(len(r["axioms_by_declaration"]) for r in rows if r["new"]),
        scope="Acquired finite-family dependency, changed operational completion, original material ancestry, "
              "all saved native histories and controls. Not universal Python refinement, "
              "genesis of maintenance scope or universal ethical justification.")
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        (HERE / "criterion-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print("RECEIPT " + str(attempt / "receipt.json"), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
