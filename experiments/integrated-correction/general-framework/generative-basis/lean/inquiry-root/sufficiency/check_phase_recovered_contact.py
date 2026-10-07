#!/usr/bin/env python3
"""Fresh Lean 4.29.1 build, complete axiom audit, and independent native execution.

Only the new module and its actual import closure are built. Each invocation
preserves sources, compiler/source hashes, logs and correspondence output in a
new receipt directory. Runtime comparison does not replace the kernel proofs.
"""
from __future__ import annotations

import ast
from datetime import datetime, timezone
import hashlib
from itertools import product
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = CORE.parents[4]
SOURCE = HERE / "PhaseRecoveredContact.lean"
NS = "Generative.InquirySufficiency.PhaseRecoveredContact"
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def closure():
    index = {p.stem: p for root in (CORE, CORE / "inquiry-root", HERE) for p in root.glob("*.lean")}
    order, visiting = [], set()
    def visit(name):
        if name in order or name.split(".")[0] in ("Init", "Std", "Lean"):
            return
        assert name not in visiting
        visiting.add(name)
        for imported in re.findall(r"^import\s+(\S+)", index[name].read_text(), re.M):
            visit(imported)
        visiting.remove(name)
        order.append(name)
    visit(SOURCE.stem)
    return [(name, index[name]) for name in order]


class Stopped(Exception):
    """Independent executor keeps the reached state and completed event count."""
    def __init__(self, state, reason):
        self.state, self.reason = dict(state), reason


def draw(s):
    return 16384 + s["live"] + s["workspace"] + 2


def support(s):
    if s["live"] + s["workspace"] + 2 > s["capacity"]:
        raise Stopped(s, "capacity")
    if s["held"] < draw(s):
        raise Stopped(s, "insufficient")
    s["held"] -= draw(s)
    s["enacted"] += draw(s)


def command(s, name):
    support(s)
    if name == "a":
        s["phase"] = (s["phase"] + 1) % 3
        result = None
    elif name == "read":
        result = (s["phase"] == 2) ^ s["tau"] ^ s["sigma"]
    elif name == "probe":
        if s["source"] < 10:
            raise Stopped(s, "source")
        actual = ((s["phase"] == 2) ^ s["tau"]) and not s["blocked"]
        s["source"] -= 10
        s["held"] += 655360 * actual
        s["arrived"] += 655360 * actual
        s["transferred"] += 10 * actual
        s["dissipated"] += 10 * (not actual)
        support(s)
        result = actual ^ s["flip"]
    else:
        raise AssertionError(name)
    s["events"] += 1
    return result


def inquire(s):
    readings = [command(s, "read")]
    for _ in range(2):
        command(s, "a")
        readings.append(command(s, "read"))
    # Inversion cancels in equality; decoder does not inspect phase/tau/sigma.
    phase = 2 if readings[0] == readings[1] else 0 if readings[0] == readings[2] else 1
    shifts = {0: 0, 1: 2, 2: 1}[phase]
    for _ in range(shifts):
        command(s, "a")
    arrivals, receipts = [], []
    for index in range(2):
        if index:
            command(s, "a")
            command(s, "a")
        previous = s["transferred"]
        receipts.append(command(s, "probe"))
        arrivals.append(s["transferred"] > previous)
    return readings, shifts, arrivals, receipts


def start(phase, tau, sigma, broken, blocked, flip):
    return dict(phase=phase, tau=tau, sigma=sigma, broken=broken, blocked=blocked,
                flip=flip, source=40, held=600000, live=0, workspace=0, capacity=10,
                enacted=0, arrived=0, transferred=0, dissipated=0, spare=0,
                recovered=0, events=0)


def loop(s):
    first = inquire(s)
    choose = not any(first[2])
    if choose:
        support(s)
        if 10 * (s["recovered"] + 1) > s["dissipated"]:
            raise Stopped(s, "recovery_material")
        s["spare"] += 1
        s["recovered"] += 1
        s["events"] += 1
        support(s)
        if not s["spare"]:
            raise Stopped(s, "formation_material")
        s["spare"] -= 1
        s["blocked"] = False
        s["events"] += 1
    second = inquire(s)
    return [*map(int, first[0]), first[1], *map(int, first[2]), int(choose),
            *map(int, second[2]), int(first[3][0] ^ first[2][0]),
            *(s[k] for k in ("held", "enacted", "arrived", "source", "transferred",
                            "dissipated", "spare", "recovered", "events"))]


def reconstruction():
    rows = []
    for phase in range(3):
        for parameters in product((False, True), repeat=5):
            s = start(phase, *parameters)
            row = loop(s)
            assert s["blocked"] is False
            assert row[7:9] == [int(parameters[0]), int(not parameters[0])]
            assert row[6] == parameters[3]
            assert row[9] == parameters[4]
            assert s["source"] == 0
            assert s["held"] + s["enacted"] == 600000 + s["arrived"]
            assert s["transferred"] + s["dissipated"] == 40
            rows.append(row)
    failure_rows = []
    for field, value, action in (("held", 0, inquire), ("source", 10, inquire), ("source", 20, loop)):
        s = start(1, True, False, True, True, True)
        s[field] = value
        try:
            action(s)
        except Stopped as stop:
            failure_rows.append(dict(changed_field=field, value=value, reason=stop.reason,
                                     reached=stop.state))
        else:
            raise AssertionError("expected interrupted execution")
    s = start(1, True, False, True, True, True)
    s["source"] = 20
    assert inquire(s)[2] == [False, False]
    return rows, failure_rows


def main():
    source = SOURCE.read_text()
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source)
    assert not re.search(r"^\s*(axiom|constant)\s", source, re.M)
    declarations = re.findall(r"^(?:theorem|def|abbrev|inductive|structure)\s+(\w+)", source, re.M)
    expected = [NS + "." + name for name in declarations]
    assert sorted(re.findall(r"^#print axioms (\S+)", source, re.M)) == sorted(expected)
    lean = shutil.which("lean")
    assert lean, "Lean is required; no enumeration-only success"
    command_prefix = [lean, "+leanprover/lean4:v4.29.1"] if shutil.which("elan") else [lean]
    version = subprocess.run(command_prefix + ["--version"], capture_output=True, text=True, check=True).stdout.strip()
    assert "4.29.1" in version
    compiler_prefix = subprocess.run(command_prefix + ["--print-prefix"],
                                     capture_output=True, text=True, check=True).stdout.strip()
    compiler = str(Path(compiler_prefix) / "bin" / "lean")
    checked = datetime.now(timezone.utc)
    receipt = HERE / "phase-recovered-contact-runs" / checked.strftime("%Y%m%dT%H%M%S.%fZ")
    snapshots = receipt / "sources"
    snapshots.mkdir(parents=True)
    (receipt / "lean-toolchain").write_text("leanprover/lean4:v4.29.1\n")
    (receipt / Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    rows, failures = reconstruction()
    modules, audits, all_audits = [], {}, {}
    expressions = []
    for phase in range(3):
        for parameters in product((False, True), repeat=5):
            args = " ".join("true" if item else "false" for item in parameters)
            expressions.append(f"#eval metrics .p{phase} {args}")
    harness = "import PhaseRecoveredContact\nopen " + NS + "\n" + "\n".join(expressions) + "\n"
    (receipt / "Correspondence.lean").write_text(harness)
    with tempfile.TemporaryDirectory(prefix="phase-recovered-contact-") as temporary:
        build = Path(temporary)
        env = {**os.environ, "LEAN_PATH": str(build)}
        for name, path in closure():
            raw = path.read_bytes()
            (build / (name + ".lean")).write_bytes(raw)
            (snapshots / (name + ".lean")).write_bytes(raw)
            result = subprocess.run(command_prefix + ["-o", name + ".olean", name + ".lean"],
                                    cwd=build, env=env, capture_output=True, text=True, timeout=600)
            output = result.stdout + result.stderr
            (receipt / (name + ".log")).write_text(output)
            modules.append(dict(module=name, source=str(path.relative_to(REPO)), source_sha256=sha(raw),
                                exit_code=result.returncode))
            assert result.returncode == 0 and not re.search(r"\b(error|warning)\b", output), output[-4000:]
            parsed = {name: [a.strip() for a in axs.split(",") if a.strip()] for name, axs in AUDIT.findall(output)}
            all_audits.update(parsed)
            if name == SOURCE.stem:
                audits = parsed
        assert sorted(audits) == sorted(expected)
        assert all(not axioms for axioms in all_audits.values()), all_audits
        (build / "Correspondence.lean").write_text(harness)
        result = subprocess.run(command_prefix + ["Correspondence.lean"], cwd=build, env=env,
                                capture_output=True, text=True, timeout=600)
        (receipt / "Correspondence.log").write_text(result.stdout + result.stderr)
        assert result.returncode == 0, result.stdout + result.stderr
        actual = [ast.literal_eval(line) for line in result.stdout.splitlines() if line.strip()]
        assert actual == rows, "Lean/Python correspondence differs"
    # Fail if concurrent edits changed any built source.
    assert all(sha((REPO / row["source"]).read_bytes()) == row["source_sha256"] for row in modules)
    report = dict(checked_at_utc=checked.isoformat(), status="passed", version=version,
                  compiler=compiler, compiler_sha256=sha(Path(compiler).read_bytes()),
                  checker_sha256=sha(Path(__file__).read_bytes()), source_sha256=sha(SOURCE.read_bytes()),
                  receipt=str(receipt.relative_to(REPO)), modules=modules, new_audits=len(audits),
                  closure_audits=len(all_audits), all_audits_empty=True,
                  correspondence=dict(cases=len(rows), metrics_per_case=len(rows[0]), values=rows),
                  independent_failure_prefixes=failures,
                  scope="Conditional native-law recognition/implementation bridge; no normative warrant or full-foundation completion. Option None is not rollback.")
    (receipt / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    (HERE / "phase-recovered-contact-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ("status", "receipt", "new_audits", "closure_audits")}, indent=2))
    print(f"Matched {len(rows)} cases × {len(rows[0])} metrics; preserved three reached failure prefixes.")


if __name__ == "__main__":
    main()
