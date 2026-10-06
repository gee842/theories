#!/usr/bin/env python3
"""Compare the preserved Port.command with native Lean fixtures at exact ticks.

This runs fresh single-command fixtures only, not the original scientific suite.
The generated closed Lean cases must be compiled by the separate proof checker.
"""
from collections import Counter
from dataclasses import dataclass, asdict
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = CORE.parents[4]
ACCESS = CORE.parent / "mathematical-abstraction/acquisition/access"
MANIFEST = HERE / "native-packet-inputs.json"
REPORT = HERE / "native-packet-correspondence.json"
GENERATED = HERE / "NativePacketCases.lean"
NATIVE = HERE / "NativePacketProcess.lean"
TICKS = 65536
COMMANDS = ("a", "reset", "read", "probe")
FIELDS = ("phase", "tau", "sigma", "broken", "blocked", "receiptFlip", "source", "fuel",
          "live", "workspace", "capacity", "spent", "income", "transferred", "wasted")
INPUTS = (ACCESS / "diagnosis.py", ACCESS.parent / "model.py", ACCESS / "PROTOCOL.md",
          ACCESS / "inquiry/check.py", ACCESS / "inquiry/PROTOCOL.md", ACCESS / "results.json")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def ticks(amount):
    value = amount * TICKS
    assert value.denominator == 1
    return value.numerator


@dataclass(frozen=True)
class Case:
    command: str
    phase: int
    tau: bool
    sigma: bool
    broken: bool
    blocked: bool
    receiptFlip: bool
    source: int
    fuel: int
    live: int = 15
    workspace: int = 0
    capacity: int = 256
    spent: int = 0
    income: int = 0
    transferred: int = 0
    wasted: int = 0
    historicalPeak: int = 15

    def state(self):
        return {field: getattr(self, field) for field in FIELDS}


def fixtures():
    cases = {}
    def add(case, group):
        cases.setdefault(case, set()).add(group)
    flags = list(product((False, True), repeat=5))
    canonical_bill = 16384 + 17
    for phase, fs in product(range(3), flags):
        for source in range(21):
            add(Case("probe", phase, *fs, source, 2 * canonical_bill), "all_source_and_flag_modes")
        for source, fuel in product((0, 9, 10, 20),
                                    (0, canonical_bill - 1, canonical_bill, 2 * canonical_bill - 1)):
            add(Case("probe", phase, *fs, source, fuel), "chronological_funding_boundaries")
        for command, fuel in product(COMMANDS[:3], (0, canonical_bill - 1, canonical_bill)):
            add(Case(command, phase, *fs, 11, fuel), "ordinary_command_modes")
    selected_flags = ((False, False, False, False, False),
                      (True, True, True, False, True),
                      (False, True, True, True, False))
    layouts = ((0, 0, 1), (0, 0, 2), (7, 3, 11), (7, 3, 12), (15, 4, 20), (15, 4, 21))
    for (live, workspace, capacity), phase, fs, command, source in product(
            layouts, range(3), selected_flags, COMMANDS, (9, 10)):
        bill = 16384 + live + workspace + 2
        for fuel in (bill - 1, bill, 2 * bill):
            add(Case(command, phase, *fs, source, fuel, live, workspace, capacity,
                     historicalPeak=live), "capacity_and_nonzero_workspace")
    for phase, fs, command, source in product(range(3), selected_flags, COMMANDS, (0, 10, 20)):
        bill = 16384 + 8 + 5 + 2
        for fuel in (bill, 2 * bill):
            add(Case(command, phase, *fs, source, fuel, 8, 5, 20,
                     spent=10*TICKS+31, income=10*TICKS, transferred=10, wasted=10,
                     historicalPeak=50), "nonzero_prior_counters")
    return [(case, sorted(groups)) for case, groups in cases.items()]


def independent_result(case):
    """Direct independent reconstruction for comparison, not the Lean oracle.

    The generated Lean expected values come from run_original, below.
    """
    state = case.state()
    peak = state["live"] + state["workspace"] + 2
    bill = 16384 + peak
    history_peak = case.historicalPeak
    events, trace = [], []
    start = state["fuel"] + state["spent"] - state["income"]
    def snapshot(kind, detail):
        return {"kind": kind, "detail": detail, "state": dict(state)}, {
            "start": start, "peak": history_peak, "events": events, "trace": trace}
    def pay(kind):
        nonlocal history_peak
        if peak > state["capacity"]:
            return "capacity:" + kind
        if state["fuel"] < bill:
            return "funding:" + kind
        state["fuel"] -= bill
        state["spent"] += bill
        history_peak = max(history_peak, peak)
        events.append(dict(kind=kind, work=0, live=state["live"], temporary=2,
                           workspace=state["workspace"], peak=peak, rewrites=0,
                           extra="1/4", bill=str(Fraction(bill, TICKS)),
                           fuel=str(Fraction(state["fuel"], TICKS))))
        return None
    failure = pay("native_" + case.command)
    if failure:
        return snapshot("stopped", failure)
    output = None
    if case.command == "a":
        state["phase"] = (state["phase"] + 1) % 3
    elif case.command == "reset":
        if not state["broken"]:
            state["phase"] = 0
    elif case.command == "read":
        output = int((state["phase"] == 2) ^ state["tau"] ^ state["sigma"])
    elif case.command == "probe":
        if state["source"] < 10:
            return snapshot("stopped", "source_unavailable")
        state["source"] -= 10
        arrival = ((state["phase"] == 2) ^ state["tau"]) and not state["blocked"]
        if arrival:
            state["transferred"] += 10
            state["fuel"] += 10 * TICKS
            state["income"] += 10 * TICKS
            events.append(dict(kind="actual_arrival", amount=10,
                               fuel=str(Fraction(state["fuel"], TICKS))))
        else:
            state["wasted"] += 10
        trace.append(dict(command="probe", observation="receipt_not_acquired"))
        failure = pay("arrival_receipt")
        if failure:
            return snapshot("stopped", failure)
        output = int(arrival ^ state["receiptFlip"])
        trace[-1]["observation"] = output
    else:
        raise AssertionError(case.command)
    if case.command != "probe":
        trace.append(dict(command=case.command, observation=output))
    return snapshot("complete", output)


def load_original():
    path = ACCESS / "diagnosis.py"
    spec = importlib.util.spec_from_file_location("_native_packet_review_original", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    assert Path(module.acquisition.__file__).resolve() == (ACCESS.parent / "model.py").resolve()
    retained = json.loads((ACCESS / "results.json").read_text())["handoff"]["learned_machine"]
    assert retained == {"alphabet": ["a"], "outputs": [0, 0, 1],
                        "transitions": [[1], [2], [0]], "initial": 0}
    module._correspondence_machine = module.acquisition.Machine(
        tuple(retained["alphabet"]), tuple(retained["outputs"]),
        tuple(tuple(row) for row in retained["transitions"]), retained["initial"])
    return module


def run_original(module, case):
    machine = module._correspondence_machine
    account = module.Account(Fraction(case.fuel, TICKS), capacity=case.capacity,
                             initial_live=case.live)
    account.workspace = case.workspace
    account.spent = Fraction(case.spent, TICKS)
    account.income = Fraction(case.income, TICKS)
    account.start = account.fuel + account.spent - account.income
    assert account.start >= 0
    account.peak = case.historicalPeak
    port = module.Port(machine, case.phase, case.source, account,
                       target_flip=int(case.tau), sensor_flip=int(case.sigma),
                       broken_reset=int(case.broken), blocked=int(case.blocked),
                       receipt_flip=int(case.receiptFlip))
    port.transferred, port.wasted = case.transferred, case.wasted
    try:
        output = port.command(case.command)
        kind, detail = "complete", output
    except module.Halt as error:
        kind, detail = "stopped", str(error)
    state = dict(phase=port._state, tau=bool(port._tau), sigma=bool(port._sigma),
                 broken=bool(port._broken), blocked=bool(port._blocked),
                 receiptFlip=bool(port._receipt_flip), source=port._source,
                 fuel=ticks(account.fuel), live=account.live, workspace=account.workspace,
                 capacity=account.capacity, spent=ticks(account.spent), income=ticks(account.income),
                 transferred=port.transferred, wasted=port.wasted)
    # Logs are audited as original fields but deliberately absent from Lean State.
    extra = dict(start=ticks(account.start), peak=account.peak,
                 events=[{key: (str(value) if isinstance(value, Fraction) else value)
                          for key, value in event.items()} for event in account.events],
                 trace=port.trace)
    assert state["fuel"] + state["spent"] == extra["start"] + state["income"]
    assert state["source"] + state["transferred"] + state["wasted"] == (
        case.source + case.transferred + case.wasted)
    return {"kind": kind, "detail": detail, "state": state}, extra


def lean_state(state):
    fields = []
    for field in FIELDS:
        value = state[field]
        token = ".p" + str(value) if field == "phase" else (
            "true" if value is True else "false" if value is False else str(value))
        fields.append(field + " := " + token)
    return "{ " + ", ".join(fields) + " }"


def lean_result(result, command):
    state = lean_state(result["state"])
    if result["kind"] == "stopped":
        detail = result["detail"]
        if detail.startswith("capacity:native_"):
            reason = "interfaceCapacity"
        elif detail.startswith("funding:native_"):
            reason = "interfaceFunding"
        else:
            reason = {"source_unavailable": "sourceUnavailable",
                      "capacity:arrival_receipt": "receiptCapacity",
                      "funding:arrival_receipt": "receiptFunding"}[detail]
        return ".stopped (" + state + ") ." + reason
    detail = result["detail"]
    observation = ".silent" if detail is None else (
        "(." + ("receipt" if command == "probe" else "reading") +
        " " + ("true" if detail else "false") + ")")
    return ".complete (" + state + ") " + observation


def generated_text(rows, manifest_sha, bindings):
    chunks = [rows[i:i+64] for i in range(0, len(rows), 64)]
    text = ["import NativePacketProcess", "", "/-!",
            "# Closed correspondence cases from the preserved Python Port.command",
            "", "Generated by check_native_packet_correspondence.py.",
            "These are fresh command fixtures, not reruns of the scientific suite.",
            "All expected results below were obtained from the original executor.",
            "State omits audit logs and historical peak; the Python report checks them separately.",
            "Default scale-one tariff; fuel, spent and income use 65536 ticks per unit.",
            "Input manifest SHA256: " + manifest_sha, "-/", "",
            "namespace Generative.NativePacketCases", "", "open NativePacketProcess", "",
            "set_option maxRecDepth 100000", "set_option maxHeartbeats 0", "",
            "def executeCases : List (State × Command) → List Result",
            "  | [] => []", "  | (state, command) :: rest => execute state command :: executeCases rest", ""]
    for block_id, rows in enumerate(chunks):
        name = "native_cases_" + str(block_id).zfill(3)
        text.extend(["/-- Original native fixture cases " + str(rows[0]["id"]) + "–" + str(rows[-1]["id"]) + ". -/",
                     "theorem " + name + " :", "    executeCases ["])
        for i, row in enumerate(rows):
            text.append("      (" + lean_state(row["before"]) + ", ." + row["command"] + ")" +
                        ("," if i+1 < len(rows) else "] = ["))
        for i, row in enumerate(rows):
            text.append("      " + lean_result(row["result"], row["command"]) +
                        ("," if i+1 < len(rows) else "] := rfl"))
        text.append("")
    text.extend(["end Generative.NativePacketCases", "",
                 "#print axioms Generative.NativePacketCases.executeCases"])
    text.extend("#print axioms Generative.NativePacketCases.native_cases_" + str(i).zfill(3)
                for i in range(len(chunks)))
    return "\n".join(text) + "\n", len(chunks)


def main():
    paths = set(INPUTS)
    saved = json.loads((ACCESS / "results.json").read_text())
    for path, digest in saved["source_hashes"].items():
        actual = (ACCESS / path).resolve()
        assert sha(actual.read_bytes()) == digest, path
        paths.add(actual)
    for path, digest in saved["handoff"]["source_hashes"].items():
        actual = REPO / path
        assert sha(actual.read_bytes()) == digest, path
        paths.add(actual)
    bindings = {str(path.relative_to(REPO)): sha(path.read_bytes()) for path in sorted(paths)}
    if not MANIFEST.exists():
        MANIFEST.write_text(json.dumps({"schema_version": 1,
            "scope": "Frozen pre-existing native command source and its provenance; no scientific producer rerun.",
            "files": [{"path": path, "sha256": digest} for path, digest in bindings.items()]}, indent=2) + "\n")
    manifest_bytes = MANIFEST.read_bytes()
    manifest = json.loads(manifest_bytes)
    assert {item["path"]: item["sha256"] for item in manifest["files"]} == bindings
    checker_bytes = Path(__file__).read_bytes()
    native_bytes = NATIVE.read_bytes()
    original = load_original()
    rows, outcomes, groups = [], Counter(), Counter()
    for case, categories in fixtures():
        result, extras = run_original(original, case)
        independent, extra_independent = independent_result(case)
        assert result == independent, (case, result, independent)
        assert extras == extra_independent, (case, extras, extra_independent)
        row = dict(id=len(rows), command=case.command, groups=categories,
                   before=case.state(), historical_peak_before=case.historicalPeak,
                   result=result, original_extra_fields_after=extras)
        rows.append(row)
        outcomes[result["kind"] + ":" + str(result["detail"])] += 1
        groups.update(categories)
    manifest_sha = sha(manifest_bytes)
    lean_source, blocks = generated_text(rows, manifest_sha, bindings)
    GENERATED.write_text(lean_source)
    assert Path(__file__).read_bytes() == checker_bytes and NATIVE.read_bytes() == native_bytes
    assert MANIFEST.read_bytes() == manifest_bytes
    assert all(sha((REPO / path).read_bytes()) == digest for path, digest in bindings.items())
    record = dict(status="passed", case_count=len(rows), case_blocks=blocks,
        generated_lean_audit_count=blocks+1, source_bindings=bindings,
        generated_lean_sha256=sha(GENERATED.read_bytes()), checker_sha256=sha(checker_bytes),
        inputs_manifest_sha256=manifest_sha, inputsmanifest_sha256=manifest_sha,
        native_model_sha256=sha(native_bytes),
        generated_lean_requires_separate_kernel_check=True,
        scientific_producer_executed=False, original_native_command_executed=True,
        differential_scope="Original Port.command vs independently reconstructed exact default-scale-one tariff execution; every generated Lean expected result is from original Port.command.",
        tick_scale=TICKS, source_values=list(range(21)), phases=3, flag_combinations=32,
        retained_machine=saved["handoff"]["learned_machine"], original_machine_relearned=False,
        lean_state_fields=list(FIELDS), extra_original_fields_checked=["start", "peak", "events", "trace"],
        limitations="Finite correspondence suite; general laws require the separate Lean proofs. No controller preparation/commit/retention, physical calibration or empirical apparatus correspondence is established.",
        outcomes=dict(sorted(outcomes.items())), groups=dict(sorted(groups.items())), cases=rows)
    REPORT.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({key: record[key] for key in ("status", "case_count", "case_blocks",
          "generated_lean_audit_count", "generated_lean_sha256", "inputs_manifest_sha256", "outcomes")}))


if __name__ == "__main__":
    main()
