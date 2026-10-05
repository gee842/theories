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
REPO = next(p for p in ROOT.parents if (p / "AGENTS.md").exists())
CORE = REPO / "experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean"
FORMATION = REPO / "experiments/shared-renewal-capability/regulation/retention/formation"
IDENTIFICATION = FORMATION / "selectors/updaters/prediction/recipient-correction/identification"
ARCHIVE = IDENTIFICATION / "recording/formal"
CONSUMER = ROOT.parents[2]
ACTION = CONSUMER / "action/formal"
SOURCES = {
    "GenerativeCore": CORE,
    "FormedSelection": FORMATION / "formal/FormedSelection.lean",
    "RecipientCorrection": IDENTIFICATION.parent / "formal/RecipientCorrection.lean",
    "RecipientIdentification": IDENTIFICATION / "formal/RecipientIdentification.lean",
    "EmissionArchive": ARCHIVE / "EmissionArchive.lean",
    "RecipientArchive": ARCHIVE / "RecipientArchive.lean",
    "ArchivePreparation": ARCHIVE / "ArchivePreparation.lean",
    "PaidArchiveReader": ARCHIVE / "PaidArchiveReader.lean",
    "RecordedEvidence": FORMATION / "learning-interface/recording/formal/RecordedEvidence.lean",
    "ReasonReplay": FORMATION / "learning-interface/recording/reason-replay/formal/ReasonReplay.lean",
    "RecipientReasons": CONSUMER / "formal/RecipientReasons.lean",
    "PaidRecipientReasons": CONSUMER / "formal/PaidRecipientReasons.lean",
    "ReasonPreparation": CONSUMER / "formal/ReasonPreparation.lean",
    "ReasonReplayBridge": CONSUMER / "formal/ReasonReplayBridge.lean",
}
SOURCES["RecipientAction"] = ACTION / "RecipientAction.lean"
SOURCES["ActionPreparation"] = ACTION / "ActionPreparation.lean"
SOURCES["ActionWitness"] = ACTION / "ActionWitness.lean"
for name in ("PublicationSafety", "PublicationBudget", "PublicationBridge"):
    SOURCES[name] = CONSUMER / "publication-safety/formal" / (name + ".lean")
NEW_MODULES = {"RevisionPreparation", "FreshRevision", "RevisionWitness"}
for name in ("RevisionPreparation", "FreshRevision", "RevisionWitness"):
    SOURCES[name] = ROOT / (name + ".lean")

ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
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
        assert set(imports).issubset({"Std"} | set(SOURCES)), imports
        declared[name] = set(re.findall(r"^theorem\s+(\w+)", source_text, re.M))
        requested = {qualified.rsplit(".", 1)[-1] for qualified in
                     re.findall(r"^#print axioms\s+([\w.]+)\s*$", source_text, re.M)}
        requested_audits[name] = requested
        if name == "GenerativeCore":
            assert requested and requested.issubset(declared[name])
        else:
            assert declared[name] == requested, (name, declared[name] ^ requested)

    protocol_path = ROOT.parent / "PROTOCOL.md"
    freeze_path = ROOT.parent / "protocol-freeze.json"
    clarification_path = ROOT.parent / "PROSPECTIVE-CLARIFICATIONS.md"
    freeze = json.loads(freeze_path.read_text())
    contract_files = {str(protocol_path.relative_to(REPO)): protocol_path.read_bytes(),
                      str(freeze_path.relative_to(REPO)): freeze_path.read_bytes(),
                      str(clarification_path.relative_to(REPO)): clarification_path.read_bytes()}
    frozen_predecessors_match = all(sha((REPO/path).read_bytes()) == digest
        for path, digest in freeze["source_sha256"].items())
    assert frozen_predecessors_match
    parent_sources_match = {}
    for name, path in SOURCES.items():
        if name not in NEW_MODULES:
            previous = subprocess.run(["git", "show", freeze["accepted_parent_commit"]+":"+str(path.relative_to(REPO))],
                cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout
            parent_sources_match[name] = previous == frozen[name]
    assert all(parent_sources_match.values())
    results = []
    logs = ROOT / "verification"
    logs.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="recipient-revision-lean-") as temporary:
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
                "role": "new formalization" if name in NEW_MODULES else "existing dependency",
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

    unchanged = (all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
        and all((REPO/path).read_bytes()==data for path,data in contract_files.items())
        and all(sha((REPO/path).read_bytes())==digest for path,digest in freeze["source_sha256"].items()))
    passed = (len(results) == len(SOURCES) and unchanged
              and all(item["clean_dependency_audit"] for item in results))
    record = {
        "protocol_sources_sha256": {path:sha(data) for path,data in contract_files.items()},
        "protocol_frozen_predecessors_match": frozen_predecessors_match,
        "parent_commit": freeze["accepted_parent_commit"],
        "all_inherited_lean_match_parent_commit": parent_sources_match,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed",
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
        "scope": "Prospective M42 preparation and exact old M32 prepared-state resource "
                 "projection; one continuing accepted action core, guarded paid opening, "
                 "two-query recipient-only archive view, actual prebound second acquisition, "
                 "fresh-window factual provenance and arbitrary initialized paid reason "
                 "publication safety; later paid import and action conditional on "
                 "observation-to-use law stability. Selected actual continuation from "
                 "ActionWitness.final retains old backing, original compartments and exact "
                 "services/waste/material accounts. The full stochastic old preparation "
                 "and all Python failure mixtures are not formally refined. Calibration, "
                 "recipient binding, recipes, supplied G, permission, scheduling and stability "
                 "remain explicit local premises. No automatic change detection, ethical "
                 "root, reason necessity or indefinitely renewable archive is established.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
