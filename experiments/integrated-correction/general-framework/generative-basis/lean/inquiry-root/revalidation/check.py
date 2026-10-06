#!/usr/bin/env python3
"""Revalidate the original four-module inquiry package without rewriting history.

The existing checker runs unchanged in an isolated copied directory layout and
creates its own fresh nested build. Only this revalidation directory is written.
All receipt paths are relative to this directory except repository input keys
and the installed compiler path. A failed run is preserved and exits nonzero.
"""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT.parent
REPOSITORY = next(p for p in ROOT.parents if (p / "RESEARCH.md").is_file())
MODULES = ("GenerativeCore", "Depletion", "GenerativeClosure", "InquiryFamilies")
INHERITED = frozenset(MODULES[:2])
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
PIN = "leanprover/lean4:v4.29.1"
AUDIT = re.compile(
    r"^'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])$",
    re.MULTILINE,
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def relative(path):
    return path.relative_to(REPOSITORY).as_posix()


def main():
    sources = {
        name: (PACKAGE.parent if name in INHERITED else PACKAGE) / (name + ".lean")
        for name in MODULES
    }
    checker = PACKAGE / "check.py"
    toolchain = PACKAGE / "lean-toolchain"
    historical_receipt = PACKAGE / "verification.json"
    historical = json.loads(historical_receipt.read_bytes())
    require(tuple(m["module"] for m in historical["modules"]) == MODULES,
            "Historical module contract changed")
    require((historical["new_audited_declarations"],
             historical["inherited_audited_declarations"]) == (27, 23),
            "Historical audit-count contract changed")
    contract = {m["module"]: m for m in historical["modules"]}
    inputs = {path: path.read_bytes() for path in (*sources.values(), checker, toolchain)}
    preserved_paths = [historical_receipt, checker, toolchain]
    preserved_paths += [PACKAGE / contract[name]["output"] for name in MODULES]
    preserved = {path: path.read_bytes() for path in preserved_paths}
    runner_bytes = Path(__file__).read_bytes()
    require(inputs[toolchain].decode().strip() == PIN, "Unexpected toolchain pin")
    require(sha(inputs[checker]) == historical["checker_sha256"],
            "Original checker no longer matches historical receipt")
    compiler = Path(historical["compiler_binary"])
    require(compiler.is_file(), "Recorded installed compiler is unavailable; no installation attempted")
    compiler_hash = sha(compiler.read_bytes())
    require(compiler_hash == historical["compiler_sha256"], "Installed compiler hash changed")
    version = subprocess.run([str(compiler), "--version"], check=True, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             timeout=30).stdout.strip()
    require(version == historical["lean_version"], "Installed compiler version changed")
    for name, path in sources.items():
        text = inputs[path].decode()
        require(not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text),
                f"Forbidden proof construct in {name}")
        require(not re.search(r"^\s*(axiom|constant)\s", text, re.MULTILINE),
                f"Custom axiom declaration in {name}")
        imports = re.findall(r"^import\s+(.+)$", text, re.MULTILINE)
        require(all(item in {"Std", *MODULES} for item in imports),
                f"Unrecorded import in {name}: {imports}")

    run_name = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    destination = ROOT / "runs" / run_name
    destination.mkdir(parents=True, exist_ok=False)
    snapshots = destination / "sources"
    staged_package = snapshots / "inquiry-root"
    staged_package.mkdir(parents=True)
    snapshot_paths = {}
    for name, path in sources.items():
        parent = snapshots if name in INHERITED else staged_package
        snapshot = parent / path.name
        snapshot.write_bytes(inputs[path])
        snapshot_paths[relative(path)] = snapshot.relative_to(ROOT).as_posix()
    (staged_package / checker.name).write_bytes(inputs[checker])
    (staged_package / toolchain.name).write_bytes(inputs[toolchain])
    for path in (checker, toolchain):
        snapshot_paths[relative(path)] = (staged_package / path.name).relative_to(ROOT).as_posix()
    artifacts = {}

    def register(path):
        artifacts[path.relative_to(ROOT).as_posix()] = sha(path.read_bytes())

    for path in snapshots.rglob("*"):
        if path.is_file():
            register(path)

    record = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "failed",
        "checker_sha256": sha(runner_bytes),
        "inputs": {relative(p): sha(b) for p, b in inputs.items()},
        "snapshots": snapshot_paths,
        "preserved_historical": {relative(p): sha(b) for p, b in preserved.items()},
        "run_record": (destination / "verification.json").relative_to(ROOT).as_posix(),
        "compiler_binary": str(compiler),
        "compiler_sha256": compiler_hash,
        "lean_version": version,
        "toolchain": PIN,
        "artifacts": artifacts,
        "modules": [],
        "new_audited_declarations": 0,
        "inherited_audited_declarations": 0,
        "historical_source_differences": [
            {"module": name, "historical_sha256": contract[name]["source_sha256"],
             "current_sha256": sha(inputs[path])}
            for name, path in sources.items()
            if sha(inputs[path]) != contract[name]["source_sha256"]
        ],
        "scope": "Fresh current-source validation of the original GenerativeCore, Depletion, "
                 "GenerativeClosure and InquiryFamilies package: 27 package and 23 inherited "
                 "declaration audits. No new theorem, core-tree/sufficiency validation, "
                 "empirical result, ethical proof or whole-foundation necessity claim.",
        "standard_library_scope": "Std and its transitive dependencies are provided by the "
                                  "installed pinned Lean distribution; they are not rebuilt here.",
    }
    errors = []
    try:
        with tempfile.TemporaryDirectory(prefix="inquiry-root-revalidation-") as temporary:
            layout = Path(temporary) / "lean"
            shutil.copytree(snapshots, layout)
            copied_package = layout / "inquiry-root"
            env = dict(os.environ)
            for key in ("LEAN_PATH", "LEAN_SRC_PATH", "LEAN_SYSROOT"):
                env.pop(key, None)
            # The original checker selects its pinned compiler through the installed
            # elan shim; its actual compiler path/hash are independently checked below.
            shim = Path.home() / ".elan" / "bin"
            require((shim / "lean").is_file(), "Installed elan shim unavailable")
            env["PATH"] = str(shim) + os.pathsep + env.get("PATH", "")
            result = subprocess.run([sys.executable, str(copied_package / "check.py")],
                                    cwd=copied_package, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    timeout=780)
            stdout = destination / "checker-stdout.txt"
            stdout.write_text(result.stdout)
            register(stdout)
            record["original_checker_exit_code"] = result.returncode
            fresh_path = copied_package / "verification.json"
            if fresh_path.is_file():
                saved = destination / "original-checker-verification.json"
                saved.write_bytes(fresh_path.read_bytes())
                register(saved)
                fresh = json.loads(saved.read_bytes())
                record["fresh_build"] = fresh
                for item in fresh["modules"]:
                    source_log = copied_package / item["output"]
                    target_log = destination / "logs" / source_log.name
                    target_log.parent.mkdir(exist_ok=True)
                    target_log.write_bytes(source_log.read_bytes())
                    register(target_log)
                require(result.returncode == 0 and fresh["status"] == "passed",
                        "Original checker failed")
                require(tuple(m["module"] for m in fresh["modules"]) == MODULES,
                        "Fresh module contract mismatch")
                require(fresh["compiler_binary"] == str(compiler)
                        and fresh["compiler_sha256"] == compiler_hash,
                        "Actual compiler does not match preflight")
                require(fresh["checker_sha256"] == sha(inputs[checker])
                        and fresh["toolchain_sha256"] == sha(inputs[toolchain]),
                        "Copied checker/toolchain mismatch")
                require(fresh["fresh_temporary_build"]
                        and fresh["source_unchanged_during_check"], "Nested build not clean")
                for item in fresh["modules"]:
                    name = item["module"]
                    log = destination / "logs" / Path(item["output"]).name
                    output = log.read_text()
                    parsed = AUDIT.findall(output)
                    names = [name for name, _ in parsed]
                    axioms = sorted({a.strip() for _, group in parsed
                                     for a in group.split(",") if a.strip()})
                    require(names == contract[name]["audited_declarations"],
                            f"Qualified audit identities changed for {name}")
                    require(names == item["audited_declarations"]
                            and axioms == item["axioms"]
                            and set(axioms) <= ALLOWED_AXIOMS,
                            f"Independent output audit mismatch for {name}")
                    require("warning:" not in output and "error:" not in output,
                            f"Compiler diagnostic in {name}")
                    require(item["source_sha256"] == sha(inputs[sources[name]])
                            and item["output_sha256"] == sha(log.read_bytes())
                            and item["exit_code"] == 0 and item["clean_dependency_audit"],
                            f"Source/log/result mismatch for {name}")
                    record["modules"].append({
                        "module": name, "inherited": name in INHERITED,
                        "source": relative(sources[name]),
                        "source_sha256": sha(inputs[sources[name]]),
                        "audited_declarations": names, "axioms": axioms,
                        "exit_code": 0, "clean_dependency_audit": True,
                        "output": log.relative_to(ROOT).as_posix(),
                        "output_sha256": sha(log.read_bytes()),
                    })
            else:
                raise RuntimeError("Original checker produced no receipt")
        for field, inherited in (("new_audited_declarations", False),
                                 ("inherited_audited_declarations", True)):
            record[field] = sum(len(m["audited_declarations"]) for m in record["modules"]
                                if m["inherited"] == inherited)
        require((record["new_audited_declarations"], record["inherited_audited_declarations"])
                == (27, 23), "Independent audit counts changed")
        require((fresh["new_audited_declarations"], fresh["inherited_audited_declarations"])
                == (27, 23), "Original checker's counts changed")
    except Exception as exc:
        errors.append(f"{type(exc).__name__}: {exc}")
    record["source_unchanged_during_check"] = all(p.read_bytes() == b for p, b in inputs.items())
    record["historical_files_preserved"] = all(p.read_bytes() == b for p, b in preserved.items())
    record["wrapper_unchanged_during_check"] = Path(__file__).read_bytes() == runner_bytes
    record["compiler_unchanged_during_check"] = sha(compiler.read_bytes()) == compiler_hash
    for field in ("source_unchanged_during_check", "historical_files_preserved",
                  "wrapper_unchanged_during_check", "compiler_unchanged_during_check"):
        if not record[field]:
            errors.append(field + " failed")
    record["errors"] = errors
    record["status"] = "passed" if not errors else "failed"
    payload = (json.dumps(record, indent=2) + "\n").encode()
    (destination / "verification.json").write_bytes(payload)
    (ROOT / "verification.json").write_bytes(payload)
    print(json.dumps({"status": record["status"], "run_record": record["run_record"],
                      "new": record["new_audited_declarations"],
                      "inherited": record["inherited_audited_declarations"],
                      "errors": errors}, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
