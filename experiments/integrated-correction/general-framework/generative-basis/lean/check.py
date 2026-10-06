#!/usr/bin/env python3
"""Fresh canonical build after conservative elimination of named axiom dependencies."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "verification-history/2026-10-06-before-axiom-removal"
ARCHIVE_SHA256 = "269635cef5f1fab71dd4d375c4a4fa93bc9b33a41bbffc1656fca00b9a6d5764"
REPAIRED = {"Depletion", "RootRealization"}
MODULE_PATHS = {
    "GenerativeCore": "GenerativeCore.lean",
    "BoundaryModels": "BoundaryModels.lean",
    "Depletion": "Depletion.lean",
    "RootRealization": "RootRealization.lean",
    "ProductTower": "deeper/ProductTower.lean",
    "DynamicUnderdetermination": "deeper/DynamicUnderdetermination.lean",
    "GeneratedPaths": "deeper/GeneratedPaths.lean",
    "HistoryRealization": "deeper/HistoryRealization.lean",
    "DynamicSymmetry": "deeper/DynamicSymmetry.lean",
    "DynamicConsequences": "deeper/DynamicConsequences.lean",
    "DynamicClassification": "deeper/DynamicClassification.lean",
    "GeneratedSelf": "GeneratedSelf.lean",
    "EthicalOrientation": "EthicalOrientation.lean",
    "OutcomeContinuation": "OutcomeContinuation.lean",
    "GenerativeModel": "GenerativeModel.lean",
    "GenerativeOutcomeModel": "GenerativeOutcomeModel.lean",
}

AUDIT_PATTERN = re.compile(
    r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
KEY_DEFINITIONS = {
    "Generative.Realization.selector", "Generative.Realization.supported",
    "Generative.Realization.law", "Generative.Realization.process",
    "Generative.Realization.cycleState", "Generative.Realization.cycleEvent",
    "Generative.Realization.decoratedProcess",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)


def parse_audits(output):
    return [(name, sorted(a.strip() for a in group.split(",") if a.strip()))
            for name, group in AUDIT_PATTERN.findall(output)]


def without_comments(source):
    # These two frozen sources contain no nested block comments or string syntax.
    return re.sub(r"--[^\n]*", "", re.sub(r"/\-.*?\-/", "", source, flags=re.S))


def declaration_contract(source):
    source = without_comments(source)
    pattern = re.compile(r"^(?:(?:private|protected)\s+)?(theorem|def|inductive|structure)\s+(\w+)\b", re.M)
    starts = list(pattern.finditer(source))
    out = {}
    for i, match in enumerate(starts):
        block = source[match.start():starts[i + 1].start() if i + 1 < len(starts) else len(source)]
        kind, name = match.groups()
        if kind in {"inductive", "structure"}:
            # Constructors and deriving clauses are part of the retained data definition.
            header = re.split(r"^#print|^end\b", block, maxsplit=1, flags=re.M)[0]
        else:
            # The old signatures use no default-value binders or nested := syntax.
            header = re.split(r":=|^\s*\|", block, maxsplit=1, flags=re.M)[0]
        out[name] = (kind, " ".join(header.split()))
    return out



def definition_bodies(source):
    source = without_comments(source)
    starts = list(re.finditer(r"^(?:private\s+)?(?:def|theorem|inductive|structure)\s+(\w+)\b", source, re.M))
    return {match.group(1): " ".join(source[match.start():starts[i + 1].start() if i + 1 < len(starts) else len(source)].split())
            for i, match in enumerate(starts) if source[match.start():].startswith("def ")}


def historical_comparison_source(old_source):
    source = without_comments(old_source)
    starts = list(re.finditer(r"^(def|theorem)\s+(\w+)\b", source, re.M))
    wanted = {x.rsplit(".", 1)[-1] for x in KEY_DEFINITIONS}
    definitions = []
    for i, match in enumerate(starts):
        if match.group(1) == "def" and match.group(2) in wanted:
            block = source[match.start():starts[i + 1].start() if i + 1 < len(starts) else len(source)]
            definitions.append(block.strip())
    assert len(definitions) == len(wanted)
    guards = []
    phases = ["initial", "depleted", "revised", "ready", "terminal"]
    for phase in phases:
        guards.append(f"#guard_expr Generative.Realization.supported .{phase} =~ supported .{phase}")
        guards.append(f"#guard_expr Generative.Realization.selector .{phase} =~ selector .{phase}")
    for supplied in ["false", "true"]:
        for start in phases:
            for event in ["use", "revise", "restore", "abandon"]:
                for finish in phases:
                    args = f"{supplied} .{start} .{event} .{finish}"
                    guards.append(f"#guard_expr Generative.Realization.law {args} =~ law {args}")
    assert len(guards) == 210
    return ("import RootRealization\n\nnamespace Generative.Realization.HistoricalComparison\n\n" +
            "\n\n".join(definitions) + "\n\n" +
            "-- Closed definitional equality checks against exact archived definition bodies.\n" +
            "-- No new theorem or axiom is declared by these checks.\n" +
            "\n".join(guards) + "\nend Generative.Realization.HistoricalComparison\n")



def main():
    checker_bytes = Path(__file__).read_bytes()
    manifest_bytes = (ARCHIVE / "manifest.json").read_bytes()
    assert digest(manifest_bytes) == ARCHIVE_SHA256
    manifest = json.loads(manifest_bytes)
    for item in manifest["files"]:
        assert digest((ARCHIVE / item["snapshot"]).read_bytes()) == item["sha256"], item["snapshot"]
    previous = json.loads((ARCHIVE / "default/verification.json").read_text())
    assert previous["status"] == "passed" and len(previous["modules"]) == 16
    baseline = {m["module"]: m for m in previous["modules"]}
    assert set(MODULE_PATHS) == set(baseline)
    old_names = {n for m in baseline.values() for n in m["audited_declarations"]}
    assert len(old_names) == 179
    sources = {name: ROOT / path for name, path in MODULE_PATHS.items()}
    frozen = {name: path.read_bytes() for name, path in sources.items()}
    contracts = {}
    for name, data in frozen.items():
        original = (ARCHIVE / "sources" / (name + ".lean")).read_bytes()
        assert digest(original) == baseline[name]["source_sha256"]
        if name in REPAIRED:
            old_contract, current_contract = declaration_contract(original.decode()), declaration_contract(data.decode())
            assert all(current_contract.get(n) == spec for n, spec in old_contract.items()), name
            contracts[name] = {"all_original_named_signatures_and_datatypes_preserved": True,
                               "original_declarations": len(old_contract),
                               "new_declarations": sorted(set(current_contract) - set(old_contract))}
            old_context = re.findall(r"^(?:namespace|universe|variable|import)\b.*$", without_comments(original.decode()), re.M)
            new_context = re.findall(r"^(?:namespace|universe|variable|import)\b.*$", without_comments(data.decode()), re.M)
            assert old_context == new_context, (name, "Global signature context changed")
            if name == "RootRealization":
                old_bodies, current_bodies = definition_bodies(original.decode()), definition_bodies(data.decode())
                fixed = {"selector", "process", "cycleState", "cycleEvent", "decoratedProcess"}
                assert all(old_bodies[n] == current_bodies[n] for n in fixed), "Changed an unapproved definition body"
                contracts[name]["unchanged_definition_bodies"] = sorted(fixed)
                assert set(current_contract) - set(old_contract) == {
                    "mod_go_fuel_congr", "modCore_eq", "modCore_eq_mod", "mod_eq", "mod_two_add_two", "parity_transition"}
            else:
                assert current_contract == old_contract, "Unexpected depletion declarations"
        else:
            assert data == original, name
    toolchain_bytes = (ROOT / "lean-toolchain").read_bytes()
    assert digest(toolchain_bytes) == previous["toolchain_sha256"]
    compiler = Path(previous["compiler_binary"])
    assert digest(compiler.read_bytes()) == previous["compiler_sha256"]
    version = run([str(compiler), "--version"], ROOT)
    version.check_returncode()
    assert version.stdout.strip() == previous["lean_version"]
    requests, seen = {}, {"Std"}
    for name, data in frozen.items():
        source = data.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M), name
        imports = re.findall(r"^import\s+(\S+)\s*$", source, re.M)
        assert set(imports) <= seen, (name, imports)
        seen.add(name)
        requests[name] = re.findall(r"^#print axioms (\S+)\s*$", source, re.M)
        assert len(requests[name]) == len(set(requests[name])), name
        old_shorts = {n.rsplit(".", 1)[-1] for n in baseline[name]["audited_declarations"]}
        requested_shorts = {n.rsplit(".", 1)[-1] for n in requests[name]}
        assert old_shorts <= requested_shorts, (name, "Dropped audit")
        if name in REPAIRED:
            theorem_names = set(re.findall(r"^(?:private\s+)?theorem\s+(\w+)\b", source, re.M))
            assert theorem_names <= requested_shorts, (name, "Unaudited theorem")
    requested_all = {n for names in requests.values() for n in names}
    assert KEY_DEFINITIONS <= requested_all, "Missing direct definition audits"
    historical_source = historical_comparison_source((ARCHIVE / "sources/RootRealization.lean").read_text())
    attempt = ROOT / "verification-runs" / str(time.time_ns())
    (attempt / "sources").mkdir(parents=True)
    (attempt / "check.py").write_bytes(checker_bytes)
    (attempt / "lean-toolchain").write_bytes(toolchain_bytes)
    (attempt / "archive-manifest.json").write_bytes(manifest_bytes)
    for name, data in frozen.items():
        (attempt / "sources" / (name + ".lean")).write_bytes(data)
    (attempt / "HistoricalRealizationComparison.lean").write_text(historical_source)
    results, historical = [], None
    with tempfile.TemporaryDirectory(prefix="constructive-generative-model-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in MODULE_PATHS:
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            result = run(command, build, env)
            log = attempt / (name + ".txt")
            log.write_text(result.stdout)
            audits = parse_audits(result.stdout)
            matches = (len(audits) == len(requests[name]) == len(dict(audits)) and bool(audits) and
                       all(actual == expected or actual.endswith("." + expected)
                           for (actual, _), expected in zip(audits, requests[name])))
            old_retained = set(baseline[name]["audited_declarations"]) <= set(dict(audits))
            clean = result.returncode == 0 and "warning:" not in result.stdout and matches and old_retained and all(not a for _, a in audits)
            results.append({"module": name, "source": MODULE_PATHS[name],
                "source_sha256": digest(frozen[name]), "command": command,
                "exit_code": result.returncode, "dependency_audits": len(audits),
                "audited_declarations": [n for n, _ in audits], "axioms": sorted({a for _, aa in audits for a in aa}),
                "axioms_by_declaration": dict(audits), "added_axiom_dependencies": {},
                "original_audit_names_retained": old_retained, "clean_dependency_audit": clean,
                "output": str(log.relative_to(ROOT)), "output_sha256": digest(log.read_bytes()),
                "source_snapshot": str((attempt / "sources" / (name + ".lean")).relative_to(ROOT))})
            print(json.dumps({"module": name, "passed": clean, "audits": len(audits)}), flush=True)
            if not clean:
                print(result.stdout, flush=True)
                break
        if len(results) == len(MODULE_PATHS) and all(r["clean_dependency_audit"] for r in results):
            (build / "HistoricalRealizationComparison.lean").write_text(historical_source)
            result = run([str(compiler), "HistoricalRealizationComparison.lean"], build, env)
            log = attempt / "HistoricalRealizationComparison.txt"
            log.write_text(result.stdout)
            clean = result.returncode == 0 and not result.stdout.strip()
            historical = {"passed": clean,
                          "scope": "210 closed default-transparency definitional equality checks: every200 Bool/Phase/Event/Phase law input plus5support and5selector inputs, using exact archived definition bodies. No named theorem is added by the comparison.",
                          "finite_law_inputs_checked": 200, "supported_inputs_checked": 5,
                          "selector_inputs_checked": 5, "named_theorems_added": 0,
                          "source": str((attempt / "HistoricalRealizationComparison.lean").relative_to(ROOT)),
                          "source_sha256": digest(historical_source.encode()), "log": str(log.relative_to(ROOT)),
                          "log_sha256": digest(log.read_bytes()), "exit_code": result.returncode}
            if not clean: print(result.stdout, flush=True)
    unchanged = (all(path.read_bytes() == frozen[name] for name, path in sources.items()) and
                 Path(__file__).read_bytes() == checker_bytes and (ROOT / "lean-toolchain").read_bytes() == toolchain_bytes and
                 (ARCHIVE / "manifest.json").read_bytes() == manifest_bytes and
                 all(digest((ARCHIVE / x["snapshot"]).read_bytes()) == x["sha256"] for x in manifest["files"]))
    names = {n for r in results for n in r["audited_declarations"]}
    passed = (unchanged and len(results) == 16 and all(r["clean_dependency_audit"] for r in results) and
              old_names <= names and KEY_DEFINITIONS <= names and historical is not None and historical["passed"])
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(), "status": "passed" if passed else "failed",
        "lean_version": version.stdout.strip(), "compiler_binary": str(compiler), "compiler_sha256": digest(compiler.read_bytes()),
        "toolchain": toolchain_bytes.decode().strip(), "toolchain_sha256": digest(toolchain_bytes), "checker_sha256": digest(checker_bytes),
        "checker_unchanged_during_check": unchanged, "source_unchanged_during_check": unchanged,
        "fresh_temporary_build": True, "local_precompiled_imports_used": False,
        "axiom_policy": "Every current public-closure audit and required definition audit must have an empty dependency report; no grandfathered exceptions.",
        "preservation_archive": str(ARCHIVE.relative_to(ROOT)), "preservation_manifest_sha256": digest(manifest_bytes),
        "historical_evidence_hashes_match": unchanged, "preserved_historical_files": len(manifest["files"]),
        "unchanged_modules": sorted(set(MODULE_PATHS) - REPAIRED), "conservative_declaration_contracts": contracts,
        "original_audited_declarations": len(old_names), "original_audit_names_retained": old_names <= names,
        "key_definition_audits": sorted(KEY_DEFINITIONS), "modules": results,
        "audited_declarations": sum(r["dependency_audits"] for r in results), "new_audited_declarations": len(names - old_names),
        "new_axiom_dependencies": sorted({a for r in results for a in r["axioms"]}),
        "whole_current_audited_closure_empty": all(not r["axioms"] for r in results) and len(results) == 16,
        "historical_definition_correspondence": historical,
        "scope": "Canonical unchanged Process/Trace structural closure with conservative implementation/proof repair; all original179 audits retained. Exact finite law and full original theorem signatures preserved. Empty named dependencies do not establish an assumption-free ontology, empirical realization, acquired criterion or ethical necessity.",
    }
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        output = ROOT / "verification"
        output.mkdir(exist_ok=True)
        for row in results:
            (output / (row["module"] + ".txt")).write_bytes((ROOT / row["output"]).read_bytes())
        (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results), "audits": record["audited_declarations"],
                      "historical_correspondence": bool(historical and historical["passed"]),
                      "receipt": str((attempt / "receipt.json").relative_to(ROOT))}), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
