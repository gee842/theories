#!/usr/bin/env python3
"""Fresh, source-bound kernel verification of the composed arbitrary-period proof.

No trust is placed in Python witness selection: all finite coverage/deletion
witnesses and their universal original-game composition are checked by Lean.
"""
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import time
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = CORE.parents[4]
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
NEW = {"PeriodCycleWindows", "PeriodWindowPeriodicity", "PeriodFirstRead", "PeriodCoverRules", "PeriodCoverData",
       "PeriodPolicyCover", "PeriodPrunedCover", "PeriodGeneralProof", "PeriodCostSelection"}

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def imports(text):
    return [name for line in text.splitlines() if line.startswith("import ")
            for name in line.split("--", 1)[0].split()[1:]]

def closure():
    index = {p.stem: p for root in (CORE, CORE / "inquiry-root", HERE) for p in root.glob("*.lean")}
    order = []
    def visit(name):
        if name in order or name.split(".")[0] in ("Init", "Std", "Lean"):
            return
        for imported in imports(index[name].read_text()):
            visit(imported)
        order.append(name)
    visit("PeriodCostSelection")
    visit("PeriodWindowPruning")  # Preserve prior independently checked support.
    return [(name, index[name]) for name in order]

def main():
    lean = shutil.which("lean")
    assert lean
    prefix = [lean, "+leanprover/lean4:v4.29.1"] if shutil.which("elan") else [lean]
    version = subprocess.run(prefix + ["--version"], capture_output=True, text=True, check=True).stdout.strip()
    assert "4.29.1" in version
    compiler_prefix = subprocess.run(prefix + ["--print-prefix"], capture_output=True, text=True, check=True).stdout.strip()
    compiler = Path(compiler_prefix) / "bin" / "lean"
    run_dir = HERE / "period-general-proof-runs" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    (run_dir / "sources").mkdir(parents=True)
    report = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), status="running", version=version,
                  compiler=str(compiler), compiler_sha256=sha(compiler.read_bytes()),
                  receipt=str(run_dir.relative_to(REPO)), checker_sha256=sha(Path(__file__).read_bytes()),
                  scope="Composed arbitrary-positive-period theorems for original bothKnowableWithin: no six-command guarantee, at least seven worst-case commands, seven implies one native/complement cyclic factor triple and repeatsEveryThree, nonrepeating needs eight, and conditional least guaranteed draw without a carrier-size cutoff. Not a claim about every realized branch, average cost, premise-free physical selection, or normative warrant.",
                  modules=[], audits={}, new_audits=0, total_audits=0)
    (run_dir / Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    (run_dir / "lean-toolchain").write_text("leanprover/lean4:v4.29.1\n")
    witnesses = []
    for name in ("generate_period_cover.py", "generate_period_pruned_cover.py", "check_period_general.py", "period_pruned_cover_proofs.txt"):
        path = HERE / name
        if path.exists():
            raw = path.read_bytes()
            (run_dir / name).write_bytes(raw)
            witnesses.append(dict(source=str(path.relative_to(REPO)), source_sha256=sha(raw)))
    report["witness_inputs"] = witnesses
    paths = closure()
    snapshots = {}
    for name, source in paths:
        raw = source.read_bytes()
        snapshots[name] = raw
        (run_dir / "sources" / (name + ".lean")).write_bytes(raw)
        if name in NEW:
            assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", raw.decode())
            assert not re.search(r"^\s*(axiom|constant)\s", raw.decode(), re.M)
            declared = set(re.findall(r"^(?:private\s+)?(?:def|theorem|abbrev|structure|inductive)\s+(\w+)", raw.decode(), re.M))
            printed = {n.rsplit(".", 1)[-1] for n in re.findall(r"^#print axioms (\S+)", raw.decode(), re.M)}
            assert declared <= printed, (name, "unaudited declarations", sorted(declared - printed))
    try:
        with tempfile.TemporaryDirectory(prefix="period-proof-witness-replay-") as temporary:
            replay = Path(temporary)
            for item in witnesses:
                name = Path(item["source"]).name
                (replay / name).write_bytes((run_dir / name).read_bytes())
            outputs = []
            for script in ("generate_period_cover.py", "generate_period_pruned_cover.py"):
                run = subprocess.run([sys.executable, script], cwd=replay, capture_output=True, text=True, timeout=120)
                outputs.append(run.stdout + run.stderr)
                assert run.returncode == 0, outputs[-1]
            replayed = []
            for name in ("PeriodCoverData", "PeriodCoverRules", "PeriodPrunedCover"):
                raw = (replay / (name + ".lean")).read_bytes()
                assert raw == snapshots[name], (name, "generator replay differs from checked source")
                replayed.append(dict(module=name, source_sha256=sha(raw)))
            report["generator_replay"] = dict(exact_source_matches=replayed, input_count=len(witnesses))
            (run_dir / "GeneratorReplay.log").write_text("".join(outputs))
        with tempfile.TemporaryDirectory(prefix="period-general-proof-") as temporary:
            build = Path(temporary)
            env = {**os.environ, "LEAN_PATH": str(build)}
            for name, raw in snapshots.items():
                (build / (name + ".lean")).write_bytes(raw)
            new_audits = {}
            def compile_module(name, source):
                began = time.monotonic()
                run = subprocess.run(prefix + ["-o", name + ".olean", name + ".lean"], cwd=build,
                                     env=env, capture_output=True, text=True, timeout=3600)
                output = run.stdout + run.stderr
                (run_dir / (name + ".log")).write_text(output)
                record = dict(module=name, source=str(source.relative_to(REPO)),
                    source_sha256=sha(snapshots[name]), exit_code=run.returncode,
                    elapsed_seconds=round(time.monotonic() - began, 3))
                parsed = {n: [a.strip() for a in ax.split(",") if a.strip()] for n, ax in AUDIT.findall(output)}
                return record, parsed, output
            pending = dict(paths)
            complete, active = set(), {}
            deps = {name: set(imports(raw.decode())) & set(snapshots) for name, raw in snapshots.items()}
            with ThreadPoolExecutor(max_workers=2) as workers:
                while pending or active:
                    for name, source in list(pending.items()):
                        if len(active) == 2:
                            break
                        if deps[name] <= complete:
                            print(f"Checking {name}", flush=True)
                            active[workers.submit(compile_module, name, source)] = name
                            del pending[name]
                    assert active, ("cyclic import dependencies", pending)
                    done, _ = wait(active, return_when=FIRST_COMPLETED)
                    for future in done:
                        name = active.pop(future)
                        record, parsed, output = future.result()
                        report["modules"].append(record)
                        assert record["exit_code"] == 0 and not re.search(r"\b(error|warning)\b", output), output[-6000:]
                        expected = re.findall(r"^#print axioms (\S+)", snapshots[name].decode(), re.M)
                        assert sorted(parsed) == sorted(expected), (name, "missing audit output")
                        report["audits"].update(parsed)
                        assert all(not ax for ax in parsed.values()), {n:a for n,a in parsed.items() if a}
                        if name in NEW:
                            new_audits.update(parsed)
                        complete.add(name)
                        print(f"Passed {name} ({record['elapsed_seconds']}s)", flush=True)
            assert all(not ax for ax in report["audits"].values()), {n:a for n,a in report["audits"].items() if a}
            for name, source in paths:
                assert sha(source.read_bytes()) == sha(snapshots[name]), (name, "source changed during check")
            report.update(status="passed", all_audits_empty=True, new_audits=len(new_audits),
                          total_audits=len(report["audits"]))
    except Exception as exc:
        report.update(status="failed", failure=str(exc))
        raise
    finally:
        (run_dir / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
        (HERE / "period-general-proof-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k:report[k] for k in ("status", "receipt", "new_audits", "total_audits")}, indent=2))

if __name__ == "__main__":
    main()
