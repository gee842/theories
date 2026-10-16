#!/usr/bin/env python3
"""Compile one frozen source closure; report inherited axioms without erasing them."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
REPOSITORY = HERE.parents[5]
PATTERN = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
STANDARD = {"propext", "Quot.sound", "Classical.choice"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    manifest_bytes = (HERE / "INPUTS.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    checker_bytes = Path(__file__).read_bytes()
    snapshots = {}
    for item in manifest["sources"]:
        live = REPOSITORY / item["path"]
        saved = HERE / item["snapshot"]
        original = saved.read_bytes()
        assert digest(original) == item["sha256"], item["module"]
        assert live.read_bytes() == original, "Source changed: " + item["path"]
        snapshots[item["module"]] = original

    seen = set()
    for item in manifest["sources"]:
        source = snapshots[item["module"]].decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), item["module"]
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M), item["module"]
        for imported in re.findall(r"^import\s+(\S+)\s*$", source, re.M):
            assert imported == "Std" or imported in seen, (item["module"], imported)
        seen.add(item["module"])

    compiler = Path(manifest["compiler"])
    assert digest(compiler.read_bytes()) == manifest["compiler_sha256"]
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    assert "version 4.29.1," in version
    (HERE / "logs").mkdir(exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix="connected-generative-model-") as temporary:
        build = Path(temporary)
        for name, source in snapshots.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for item in manifest["sources"]:
            name = item["module"]
            proc = subprocess.run([str(compiler), "-o", name + ".olean", name + ".lean"],
                                  cwd=build, env=env, text=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT, timeout=900)
            output = HERE / "logs" / (name + ".txt")
            output.write_text(proc.stdout)
            audits = [(n, sorted(a.strip() for a in group.split(",") if a.strip()))
                      for n, group in PATTERN.findall(proc.stdout)]
            requested = re.findall(r"^#print axioms (\S+)", snapshots[name].decode(), re.M)
            matches = len(requested) == len(audits) and all(
                actual == expected or actual.endswith("." + expected)
                for (actual, _), expected in zip(audits, requested))
            unexpected = sorted({a for _, deps in audits for a in deps} - STANDARD)
            expected_empty = set(item.get("require_empty", []))
            empty_contract = expected_empty <= {n for n, deps in audits if not deps}
            clean = (proc.returncode == 0 and matches and bool(audits) and
                     not unexpected and empty_contract and "warning:" not in proc.stdout)
            result = {"module": name, "source": item["path"], "source_sha256": item["sha256"],
                      "exit_code": proc.returncode, "audit_order_matches": matches,
                      "axioms_by_declaration": dict(audits), "unexpected_dependencies": unexpected,
                      "specified_constructive_functions_empty": empty_contract,
                      "log": str(output.relative_to(HERE)), "log_sha256": digest(output.read_bytes()),
                      "checked": clean}
            results.append(result)
            print(json.dumps({"module": name, "checked": clean, "audits": len(audits)}), flush=True)
            if not clean:
                print(proc.stdout, flush=True)
                break

    sources_unchanged = all((REPOSITORY / x["path"]).read_bytes() == snapshots[x["module"]]
                            for x in manifest["sources"])
    unchanged = (sources_unchanged and (HERE / "INPUTS.json").read_bytes() == manifest_bytes and
                 Path(__file__).read_bytes() == checker_bytes)
    passed = len(results) == len(manifest["sources"]) and unchanged and all(x["checked"] for x in results)
    axioms = sorted({a for r in results for deps in r["axioms_by_declaration"].values() for a in deps})
    record = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "build_status": "passed" if passed else "failed",
              "scope": "One compiled, source-bound closure over the existing Process/Trace law, "
                       "actual acquired-successor continuation and separately identified constructive "
                       "decision replacements. Proof checking does not derive the supplied physical "
                       "law, normative grounds or empirical interpretation. Not complete alignment.",
              "manifest_sha256": digest(manifest_bytes), "checker_sha256": digest(checker_bytes),
              "compiler": str(compiler), "compiler_sha256": manifest["compiler_sha256"],
              "lean_version": version, "fresh_temporary_build": True,
              "local_precompiled_imports_used": False, "inputs_unchanged": unchanged,
              "modules": results, "named_axiom_dependencies": axioms,
              "no_custom_axiom_declarations": True,
              "whole_closure_has_empty_axiom_dependencies": not axioms,
              "assumption_free_foundation_established": False}
    (HERE / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"build_status": record["build_status"], "modules": len(results),
                      "named_axiom_dependencies": axioms,
                      "assumption_free_foundation_established": False}), flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
