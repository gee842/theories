#!/usr/bin/env python3
"""Check paid contextual recorded-reason composition from frozen source bytes."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
REPOSITORY = next(p for p in ROOT.parents if (p / "AGENTS.md").exists() and (p / "RESEARCH.md").exists())
FORMATION = REPOSITORY / "experiments/shared-renewal-capability/regulation/retention/formation/formal"
NEW_MODULES = ["ReasonReplay"]
MODULES = ["GenerativeCore", "FormedSelection", "RecordedEvidence"] + NEW_MODULES
SOURCES = {
    "GenerativeCore": REPOSITORY / "experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean",
    "FormedSelection": FORMATION / "FormedSelection.lean",
    "RecordedEvidence": ROOT.parents[1] / "formal/RecordedEvidence.lean",
    "ReasonReplay": ROOT / "ReasonReplay.lean",
}
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
NEW_ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    toolchain = (ROOT / "lean-toolchain").read_text().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    prefix = ["lean", "+" + toolchain]
    version = run(prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    compiler_prefix = run(prefix + ["--print-prefix"], ROOT)
    compiler_prefix.check_returncode()
    compiler = Path(compiler_prefix.stdout.strip()) / "bin" / "lean"
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
        imports = re.findall(r"^import\s+(.+)$", text, re.M)
        assert all(item in {"Std", *MODULES}
                   for item in imports), imports
        requested = re.findall(r"^#print axioms (\S+)", text, re.M)
        theorems = re.findall(r"^theorem\s+(\w+)", text, re.M)
        # The inherited core retains its earlier selected audit contract; every
        # newly introduced theorem must appear in this package's audit list.
        if name in NEW_MODULES:
            assert set(theorems) == {item.rsplit(".", 1)[-1] for item in requested}, name
    results = []
    output_dir = ROOT / "verification"
    output_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="recorded-reasons-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in MODULES:
            result = run([str(compiler), "-o", name + ".olean", name + ".lean"], build, env)
            log = output_dir / (name + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout)
            requested = re.findall(r"^#print axioms (\S+)", frozen[name].decode(), re.M)
            names = [theorem for theorem, _ in audits]
            matched = len(names) == len(requested) and all(
                actual == wanted or actual.endswith("." + wanted)
                for actual, wanted in zip(names, requested))
            axioms = sorted({a.strip() for _, group in audits
                             for a in group.split(",") if a.strip()})
            clean = ("sorryAx" not in result.stdout and "warning:" not in result.stdout
                     and matched and bool(audits) and set(axioms) <= (NEW_ALLOWED_AXIOMS if name in NEW_MODULES else ALLOWED_AXIOMS))
            results.append({
                "module": name, "source": os.path.relpath(SOURCES[name], ROOT),
                "source_sha256": digest(frozen[name]), "exit_code": result.returncode,
                "dependency_audits": len(audits), "audited_declarations": names,
                "requested_audits": requested, "axioms": axioms,
                "empty_axiom_audits": sum(not group.strip() for _, group in audits),
                "clean_dependency_audit": clean,
                "output": "verification/" + log.name,
                "output_sha256": digest(log.read_bytes()),
            })
            if result.returncode or not clean:
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
    passed = (len(results) == len(MODULES) and unchanged and
              all(r["exit_code"] == 0 and r["clean_dependency_audit"] for r in results))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler), "compiler_sha256": digest(compiler.read_bytes()),
        "toolchain": toolchain, "toolchain_sha256": digest((ROOT / "lean-toolchain").read_bytes()),
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "source_unchanged_during_check": unchanged, "fresh_temporary_build": True,
        "allowed_standard_axioms": sorted(ALLOWED_AXIOMS),
        "new_allowed_standard_axioms": sorted(NEW_ALLOWED_AXIOMS), "modules": results,
        "audited_declarations": sum(r["dependency_audits"] for r in results),
        "new_audited_declarations": sum(r["dependency_audits"] for r in results
                                        if r["module"] in NEW_MODULES),
        "new_empty_axiom_audits": sum(r["empty_axiom_audits"] for r in results
                                      if r["module"] in NEW_MODULES),
        "scope": "A paid finite three-node contextual reason replay law using actual "
                 "RecordedEvidence storage, prebound six-query metadata, one formed reader "
                 "and working-store pair, and charged context sensing, decoding and rooted "
                 "path checks. Current soundness is conditional on the assay, contextual "
                 "binding, independent anchor and edge-specific relevance premises. A "
                 "cold working successor reuses physical hardware and retained records "
                 "while repaying operational audit costs. No normative standing, general "
                 "n-node closure, strategic equilibrium, noisy calibration, empirical "
                 "assay validity or unbounded physical renewal is established."

    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "new_empty_axiom_audits": record["new_empty_axiom_audits"],
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
