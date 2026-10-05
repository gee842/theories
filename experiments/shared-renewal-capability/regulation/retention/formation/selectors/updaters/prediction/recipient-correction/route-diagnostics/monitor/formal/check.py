#!/usr/bin/env python3
"""Compile frozen Lean sources in a fresh build and audit every new theorem."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
REPO = next(p for p in ROOT.parents if (p / 'AGENTS.md').exists())
SOURCES = {
    "RecipientCorrection": ROOT.parents[2] / "formal/RecipientCorrection.lean",
    "FormedRecipientRoute": ROOT.parents[2] / "transmission/formal/FormedRecipientRoute.lean",
    "SuccessorLearning": ROOT.parents[2] / "successor-learning/formal/SuccessorLearning.lean",
    "RouteDiagnostics": ROOT.parents[1] / "formal/RouteDiagnostics.lean",
    "FormedRouteMonitor": ROOT / "FormedRouteMonitor.lean",
}
PROTOCOL_SHA256 = "41609fa9974c015f44b48b9e25ec6071d8578aef03e7944935faf23384c29af6"
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    protocol_bytes = (ROOT.parent / "PROTOCOL.md").read_bytes()
    assert sha(protocol_bytes) == PROTOCOL_SHA256, "Frozen protocol changed"
    toolchain_bytes = (ROOT / "lean-toolchain").read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    command_prefix = ["lean", "+" + toolchain]
    version = run(command_prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    prefix = run(command_prefix + ["--print-prefix"], ROOT)
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin/lean"
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    declared = {}
    requested_audits = {}
    for name, source in frozen.items():
        source_text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source_text), name
        assert not re.search(r"^\s*(axiom|constant)\s", source_text, re.M), name
        imports = re.findall(r"^import\s+(.+)$", source_text, re.M)
        assert set(imports).issubset({"Std", "RecipientCorrection", "FormedRecipientRoute", "SuccessorLearning", "RouteDiagnostics"}), imports
        declared[name] = set(re.findall(r"^theorem\s+(\w+)", source_text, re.M))
        requested = {qualified.rsplit(".", 1)[-1] for qualified in
                     re.findall(r"^#print axioms\s+([\w.]+)\s*$", source_text, re.M)}
        requested_audits[name] = requested
        assert declared[name] == requested, (name, declared[name] ^ requested)

    results = []
    logs = ROOT / "verification"
    logs.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="formed-monitor-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name, path in SOURCES.items():
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            result = run(command, build, env)
            log = logs / (name + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout)
            audited_short = {name.rsplit(".", 1)[-1] for name, _ in audits}
            dependencies = sorted({axiom.strip() for _, group in audits
                                   for axiom in group.split(",") if axiom.strip()})
            clean = (result.returncode == 0 and "warning:" not in result.stdout
                     and "sorryAx" not in result.stdout
                     and audited_short == requested_audits[name]
                     and len(audits) == len(requested_audits[name])
                     and set(dependencies).issubset(ALLOWED_AXIOMS))
            results.append({
                "module": name,
                "source": str(path.relative_to(REPO)),
                "source_sha256": sha(frozen[name]),
                "role": "existing formal dependency" if name != "FormedRouteMonitor" else "new formalization",
                "command": command,
                "exit_code": result.returncode,
                "clean_dependency_audit": clean,
                "audited_declarations": [qualified for qualified, _ in audits],
                "dependency_audits": len(audits),
                "axioms": dependencies,
                "output": str(log.relative_to(ROOT)),
                "output_sha256": sha(log.read_bytes()),
            })
            if not clean:
                break

    unchanged = (ROOT.parent / "PROTOCOL.md").read_bytes() == protocol_bytes and all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
    passed = (len(results) == len(SOURCES) and unchanged
              and all(item["clean_dependency_audit"] for item in results))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed",
        "protocol_sha256": PROTOCOL_SHA256,
        "toolchain": toolchain,
        "toolchain_sha256": sha(toolchain_bytes),
        "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler),
        "compiler_sha256": sha(compiler.read_bytes()),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "source_unchanged_during_check": unchanged,
        "fresh_temporary_build": True,
        "project_objects_only_from_frozen_sources": True,
        "modules": results,
        "new_audited_declarations": sum(item["dependency_audits"] for item in results
                                        if item["role"] == "new formalization"),
        "scope": "Finite eight-cell monitor with supplied functional credit and bus contacts, "
                 "bounded head and two-frame lease. Ordinary stages compose actual "
                 "SuccessorLearning fund/perform transitions from admitted zero carrier cash. "
                 "Credit transition derives the receipt; physical bits implement the recipient-bit "
                 "projection of RouteDiagnostics.sample. Paid complete frames maintain diagnostic "
                 "summaries. General trace energy/material/floor accounts and actual-reserve "
                 "witnesses. No full stochastic Python refinement, unbounded epoch authentication, "
                 "route replacement, arbitrary absent-channel learning, fault calibration, "
                 "or monitor recipe-origin theorem.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
