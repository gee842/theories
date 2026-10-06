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
from types import SimpleNamespace

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


def state_literal(v):
    assert len(v) == 51
    resident = [".empty", ".active", ".alternative"][v[2]]
    p = f"⟨{v[0]},{v[1]},{resident},{boolstr(v[3])},{boolstr(v[4])},{v[5]},{v[6]}⟩"
    core_names = ["parts","targetA","episode","historical","closed","finished","blockedSeen","restoredSeen",
                  "phase","pending","observed","candidates","criterionActive","selected","commonSpent","totalSpent"]
    core_bool = {11,12,13,14,19}
    fields = ["plant := "+p] + [n+" := "+(boolstr(v[i]) if i in core_bool else str(v[i])) for i,n in enumerate(core_names,7)]
    core = "{" + ", ".join(fields) + "}"
    scope_names = ["readers","a","b","recordA","recordB","snapshotA","snapshotB","lastTarget","lastPayload","selected","pc","commonSpent","totalSpent"]
    parent = "{" + ", ".join(["core := "+core]+[n+" := "+str(v[i]) for i,n in enumerate(scope_names,23)]) + "}"
    names = ["parts","trialA","newB","targetA","phase","binding","pending","observed","formFamily","finishFamily","recordB","selected","pc","commonSpent","totalSpent"]
    return "{" + ", ".join(["parent := "+parent]+[n+" := "+str(v[i]) for i,n in enumerate(names,36)]) + "}"


def fixtures(results):
    c = "Generative.AcquiredPurposeCriterion.Native."
    lines = ["import AcquiredInitiationConstraint", "", "namespace InitiationFixtures",
             "open Generative.AcquiredInitiationConstraint",
             "set_option maxRecDepth 65536", "set_option maxHeartbeats 16000000", ""]
    audits = []
    def rows(data):
        current = data["initial"]
        states = [current]
        for e, row in zip(data["events"], data["steps"], strict=True):
            assert row["event"] == e and row["before"] == current
            current = row["after"]
            assert all(type(x) is int and x >= 0 for x in current)
            states.append(current)
        assert current == data["final"]
        return states
    ancestor = results["ancestry"]["native"]
    assert ancestor["initial"] == [0,0,0,0,0,360,230]
    lines += ["def ancestorStart : FormedSelection.State := ⟨0,0,.empty,false,false,360,230⟩",
              "def ancestorWord : List FormedSelection.Event := " + seq("." + EVENTS[e] for e in ancestor["events"]),
              "def ancestorStates : List (List Nat) := " + seq(seq(x) for x in rows(ancestor)),
              f"theorem ancestor_correspondence : {c}plantAdmitted 78 ancestorStart ancestorWord = true ∧",
              f"    {c}plantVectors ancestorStart ancestorWord = ancestorStates ∧",
              f"    {c}plantRun ancestorStart ancestorWord = {c}initial.plant := by decide", ""]
    audits.append("ancestor_correspondence")
    training = results["ancestry"]["criterion_training"]
    assert training["config"] == dict(receipt_mode=0,clamp=False,later_repair=False,force_bulk=False)
    assert training["initial"][:7] == ancestor["final"]
    lines += [f"def trainingConfig : {c}Config := {{laterRepair := false}}",
              f"def trainingWord : List {c}Event := " + seq(event(e) for e in training["events"]),
              "def trainingStates : List (List Nat) := " + seq(seq(x) for x in rows(training)),
              f"theorem training_correspondence : {c}admitted trainingConfig {c}initial trainingWord = true ∧",
              f"    {c}vectors trainingConfig {c}initial trainingWord = trainingStates ∧",
              f"    {c}run trainingConfig {c}initial trainingWord = Generative.AcquiredActivityScope.initial.core ∧",
              f"    trainingWord = {c}training := by decide", ""]
    audits.append("training_correspondence")
    parent = results["ancestry"]["scope_prefix"]
    assert parent["config"] == dict(contact_mode=0,clamp=False)
    assert parent["initial"] == training["final"] + [0]*13
    scope = "Generative.AcquiredActivityScope."
    lines += [f"def parentWord : List {scope}Event := " + seq(event(e) for e in parent["events"]),
              "def parentStates : List (List Nat) := " + seq(seq(x) for x in rows(parent)),
              f"theorem parent_correspondence : {scope}admitted {{}} {scope}initial parentWord = true ∧",
              f"    {scope}vectors {{}} {scope}initial parentWord = parentStates ∧",
              f"    {scope}run {{}} {scope}initial parentWord = initial.parent ∧",
              "    parentWord = inheritedWord := by decide", ""]
    audits.append("parent_correspondence")
    first_initial = results["cases"][0]["initial"]
    lines += ["def fixtureInitial : State := " + state_literal(first_initial),
              "theorem fixture_initial_is_actual : fixtureInitial = initial := by decide", ""]
    audits.append("fixture_initial_is_actual")
    n_events = n_states = n_denials = 0
    for case in results["cases"]:
        name = case["name"]
        assert re.fullmatch(r"[A-Za-z_]+", name)
        cfg = case["config"]
        assert set(cfg) == {"form_mode", "finish_mode", "clamp"}
        assert case["initial"] == parent["final"] + [0]*8 + [7,7] + [0]*5
        states = rows(case)
        assert all(len(x)==51 for x in states)
        lines += [f"def {name}_config : Config := {{formMode := {cfg['form_mode']}, finishMode := {cfg['finish_mode']}, clamp := {boolstr(cfg['clamp'])}}}",
                  f"def {name}_word : List Event := " + seq(event(e) for e in case["events"]),
                  f"def {name}_states : List (List Nat) := " + seq(seq(x) for x in states)]
        claims = [f"admitted {name}_config fixtureInitial {name}_word = true",
                  f"vectors {name}_config fixtureInitial {name}_word = {name}_states",
                  f"vector (run {name}_config fixtureInitial {name}_word) = " + seq(case["final"]),
                  f"(run {name}_config fixtureInitial {name}_word).parent.a = 3",
                  f"(run {name}_config fixtureInitial {name}_word).parent.b = 3",
                  f"(run {name}_config fixtureInitial {name}_word).trialA = 3"]
        for denied in case["denied"]:
            index = states.index(denied["state"])
            claims.append(f"enabled (run {name}_config fixtureInitial ({name}_word.take {index})) {name}_config {event(denied['event'])} = false")
            n_denials += 1
        for milestone, value in case["milestones"].items():
            assert re.fullmatch(r"[a-z_A-Z]+",milestone)
            index = states.index(value)
            lines.append(f"def {name}_{milestone} : State := run {name}_config fixtureInitial ({name}_word.take {index})")
        lines += [f"theorem {name}_correspondence : " + " ∧\n    ".join(claims) + " := by decide", ""]
        audits.append(name+"_correspondence")
        n_events += len(case["events"]); n_states += len(states)
    lines += ["theorem same_records_different_use :",
        "    scarce_faithful_decision = scarce_clamped_decision ∧",
        "    scarce_faithful_selected.selected = 1 ∧ scarce_clamped_selected.selected = 2 ∧",
        "    scarce_faithful_final.newB = 3 ∧ scarce_clamped_final.newB = 2 ∧",
        "    scarce_faithful_final.targetA = 0 ∧ scarce_clamped_final.targetA = 1 := by decide", ""]
    audits.append("same_records_different_use")
    lines += ["theorem ample_success_and_its_unfinished_new_activity :",
        "    ample_faithful_final.newB = 3 ∧ ample_faithful_final.targetA = 1 ∧",
        "    (plant ample_faithful_final).fuel = 0 ∧",
        "    (plant ample_faithful_final).intact = false ∧ (plant ample_faithful_final).localFuel = false ∧",
        "    enabled ample_faithful_final ample_faithful_config .primeTargetA = false ∧",
        "    enabled ample_faithful_final ample_faithful_config .finishTargetA = false := by decide", ""]
    audits.append("ample_success_and_its_unfinished_new_activity")
    lines += ["theorem same_protected_completion_different_generated_relation :",
        "    scarce_faithful_final.newB = ample_faithful_final.newB ∧",
        "    Generative.AcquiredPurposeCriterion.support (plant scarce_faithful_final) =",
        "      Generative.AcquiredPurposeCriterion.support (plant ample_faithful_final) ∧",
        "    (plant scarce_faithful_final).intact = (plant ample_faithful_final).intact ∧",
        "    scarce_faithful_final.targetA = 0 ∧ ample_faithful_final.targetA = 1 := by decide", ""]
    audits.append("same_protected_completion_different_generated_relation")
    lines += ["theorem actual_start_can_remove_B_completion :",
        "    (∃ t, Generative.Trace (process scarce_clamped_config) scarce_clamped_selected [.finishNewB] t ∧ t.newB = 3) ∧",
        "    Generative.Trace (process scarce_clamped_config) scarce_clamped_selected [.formTargetA]",
        "      (advance scarce_clamped_selected scarce_clamped_config .formTargetA) ∧",
        "    (∀ events t, Generative.Trace (process scarce_clamped_config)",
        "      (advance scarce_clamped_selected scarce_clamped_config .formTargetA) events t → t.newB = 2) := by",
        "  exact one_unit_start_forecloses_B (by decide) (by decide) (by decide) (by decide)", ""]
    audits.append("actual_start_can_remove_B_completion")
    lines += ["end InitiationFixtures", ""]
    lines += ["#print axioms InitiationFixtures."+a for a in audits]
    return "\n".join(lines)+"\n", dict(cases=len(results["cases"]), wrapper_events=n_events,
        wrapper_states=n_states, coordinates_per_state=51, denied_events=n_denials,
        ancestral_events=len(ancestor["events"]), ancestral_states=len(ancestor["events"])+1,
        inherited_training_events=len(training["events"]), inherited_training_states=len(training["events"])+1,
        inherited_scope_events=len(parent["events"]), inherited_scope_states=len(parent["events"])+1)


def main():
    result_path = NATIVE / "initiation-results.json"
    result_bytes = result_path.read_bytes()
    results = json.loads(result_bytes)
    assert results["status"] == "passed"
    bindings = {REPO / p: digest for p, digest in results["source_hashes"].items()}
    for path, digest in bindings.items():
        assert sha(path.read_bytes()) == digest, path
    fixture_source, counts = fixtures(results)
    paths = dict(GenerativeCore=HERE.parent / "lean/GenerativeCore.lean",
                 FormedSelection=REPO / "experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean",
                 AcquiredPurposeCriterion=HERE / "AcquiredPurposeCriterion.lean",
                 AcquiredActivityScope=HERE / "AcquiredActivityScope.lean",
                 AcquiredInitiationConstraint=HERE / "AcquiredInitiationConstraint.lean")
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    frozen["InitiationFixtures"] = fixture_source.encode()
    new = {"AcquiredInitiationConstraint", "InitiationFixtures"}
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
    attempt = HERE / "initiation-checks" / str(time.time_ns())
    attempt.mkdir(parents=True)
    (attempt / "check_initiation.py").write_bytes(checker)
    (attempt / "check_purpose.py").write_bytes(helper_bytes)
    for name, data in frozen.items():
        (attempt / (name + ".lean")).write_bytes(data)
    source_bindings = {name: dict(source=str(paths[name].relative_to(REPO)) if name in paths else
        str((attempt / (name + ".lean")).relative_to(REPO)), sha256=sha(data)) for name, data in frozen.items()}
    (attempt / "inputs.json").write_text(json.dumps(source_bindings, indent=2) + "\n")
    rows = []
    with tempfile.TemporaryDirectory(prefix="initiation-fresh-lean-") as directory:
        build = Path(directory)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in frozen:
            timed_out = False
            started = time.monotonic()
            command = [str(compiler), "-s", "65536", "-o", name + ".olean", name + ".lean"]
            try:
                result = subprocess.run(command, cwd=build, env=env, text=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
            except subprocess.TimeoutExpired as exc:
                timed_out = True
                partial = exc.stdout or ""
                if isinstance(partial, bytes):
                    partial = partial.decode(errors="replace")
                error = dict(type="TimeoutExpired", command=command, timeout_seconds=exc.timeout,
                    elapsed_seconds=time.monotonic()-started, partial_stdout=partial)
                (attempt / (name + "-exception.json")).write_text(json.dumps(error,indent=2)+"\n")
                result = SimpleNamespace(returncode=124, stdout=partial+"\nTimeoutExpired after 300 seconds.\n")
            log = attempt / (name + ".txt")
            log.write_text(result.stdout)
            audits = {n: sorted(a.strip() for a in deps.split(",") if a.strip()) for n, deps in AUDIT.findall(result.stdout)}
            passed = result.returncode == 0 and "warning:" not in result.stdout
            passed = passed and len(audits) == len(requested[name]) and all(
                actual == expected or actual.endswith("." + expected)
                for actual, expected in zip(audits, requested[name]))
            passed = passed and all(set(a) <= {"propext", "Quot.sound", "Classical.choice"} for a in audits.values())
            rows.append(dict(module=name, **source_bindings[name], new=name in new, passed=passed,
                exit_code=None if timed_out else result.returncode, timed_out=timed_out, axioms_by_declaration=audits,
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
        compiler_arguments=["-s", "65536"],
        checker_sha256=sha(checker), checker_helper_sha256=sha(helper_bytes),
        native_results=str(result_path.relative_to(REPO)), native_results_sha256=sha(result_bytes),
        native_source_bindings={str(p.relative_to(REPO)): d for p,d in bindings.items()},
        fresh_temporary_build=True, inputs_unchanged=stable, correspondence=counts, modules=rows,
        new_audits=sum(len(r["axioms_by_declaration"]) for r in rows if r["new"]),
        scope="Actual cost-channel acquisition and operative initiation constraint under a supplied local "
              "non-foreclosure rule. Original ancestry and inherited criterion/scope prefix, all nine saved histories, "
              "and failure controls. Supplied one-unit channel family, reaction/contact/reader/transfer laws, "
              "initial conditions and schedules remain. Not universal Python refinement or ethical priority.")
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        (HERE / "initiation-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print("RECEIPT " + str(attempt / "receipt.json"), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
