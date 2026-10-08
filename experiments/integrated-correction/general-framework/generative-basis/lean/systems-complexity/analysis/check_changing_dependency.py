#!/usr/bin/env python3
"""Fresh changing-dependency build against the pinned, installed Mathlib cache.

No downloads, installs or changes to the dependency checkout are performed.
SYSTEMS_MATHLIB_PROJECT selects a checkout with the pinned lake-manifest.json;
SYSTEMS_REAL_LEAN can select the already installed matching Lean compiler.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
STD = ROOT.parent
CORE = STD.parent
MATHLIB_REV = "ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa"
EXPECTED_TOOLCHAIN = "leanprover/lean4:v4.30.0-rc2"
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
MODULES = {
    "GenerativeCore": CORE / "GenerativeCore.lean",
    "SystemsOrganization": STD / "SystemsOrganization.lean",
    "RelationsAcrossScales": ROOT / "RelationsAcrossScales.lean",
    "RemainingDependency": CORE.parent / "mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/RemainingDependency.lean",
    "ScaleRevision": ROOT / "ScaleRevision.lean",
    "InquiryChoice": ROOT / "InquiryChoice.lean",
    "ChangingDependency": ROOT / "ChangingDependency.lean",
}
NEW_MODULES = {"ChangingDependency"}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(args, cwd, env=None):
    return subprocess.run(args, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)


def main():
    project = Path(os.environ.get("SYSTEMS_MATHLIB_PROJECT", str(Path.home() / "repos/生生不息"))).resolve()
    manifest_path = project / "lake-manifest.json"
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    mathlib_record = next(p for p in manifest["packages"] if p["name"] == "mathlib")
    assert mathlib_record["rev"] == MATHLIB_REV
    packages = project / manifest.get("packagesDir", ".lake/packages")
    mathlib = packages / "mathlib"
    head = run(["git", "rev-parse", "HEAD"], mathlib)
    assert head.returncode == 0 and head.stdout.strip() == MATHLIB_REV
    toolchain_bytes = (ROOT / "lean-toolchain").read_bytes()
    assert toolchain_bytes.decode().strip() == EXPECTED_TOOLCHAIN
    assert (mathlib / "lean-toolchain").read_text().strip() == EXPECTED_TOOLCHAIN
    default = Path.home() / ".elan/toolchains/leanprover--lean4---v4.30.0-rc2/bin/lean"
    compiler = Path(os.environ.get("SYSTEMS_REAL_LEAN", str(default))).resolve()
    compiler_hash = sha(compiler.read_bytes())
    checker_hash = sha(Path(__file__).read_bytes())
    version = run([str(compiler), "--version"], ROOT)
    assert version.returncode == 0 and "version 4.30.0-rc2," in version.stdout
    libraries = sorted(p / ".lake/build/lib/lean" for p in packages.iterdir()
                       if (p / ".lake/build/lib/lean").is_dir())
    inputs = {name: path.read_bytes() for name, path in MODULES.items()}
    requested = {}
    for name, data in inputs.items():
        source = data.decode()
        if name != "GenerativeCore":
            assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source)
            assert not re.search(r"^\s*(axiom|constant)\s", source, re.M)
            declared = re.findall(r"^theorem\s+(\w+)\b", source, re.M)
            prints = re.findall(r"^#print axioms ([\w.]+)\s*$", source, re.M)
            assert len(declared) == len(set(declared))
            assert len(prints) == len(declared)
            assert set(declared) == {p.rsplit(".", 1)[-1] for p in prints}
        requested[name] = re.findall(r"^#print axioms ([\w.]+)\s*$", source, re.M)
        if name in {"ResourceContinuation", "RemainingDependency"}:
            requested[name] = [("RemainingDependency." if name == "RemainingDependency" else "Generative.Conditional.") + n if "." not in n else n
                               for n in requested[name]]
    verification = ROOT / "changing-dependency-verification"
    verification.mkdir(exist_ok=True)
    frozen = verification / "sources"
    frozen.mkdir(exist_ok=True)
    for name, data in inputs.items():
        (frozen / f"{name}.lean").write_bytes(data)
    modules = []
    passed = True
    direct_imports = []
    with tempfile.TemporaryDirectory(prefix="changing-dependency-") as tmp:
        build = Path(tmp)
        for name, data in inputs.items():
            (build / f"{name}.lean").write_bytes(data)
        env = dict(os.environ, LEAN_PATH=":".join([str(build)] + [str(p) for p in libraries]))
        for name, data in inputs.items():
            result = run([str(compiler), "-o", f"{name}.olean", f"{name}.lean"], build, env)
            log = verification / f"{name}.txt"
            log.write_text(result.stdout)
            audits = [{"name": n, "axioms": sorted(a.strip() for a in aa.split(",") if a.strip())}
                      for n, aa in AUDIT.findall(result.stdout)]
            names = [a["name"] for a in audits]
            deps = {x for a in audits for x in a["axioms"]}
            clean = (result.returncode == 0 and "warning:" not in result.stdout
                     and "error:" not in result.stdout and "sorryAx" not in result.stdout
                     and names == requested[name] and deps <= ALLOWED)
            modules.append({"module": name, "exit_code": result.returncode, "passed": clean,
                            "source_sha256": sha(data), "output_sha256": sha(log.read_bytes()),
                            "audits": audits, "new_in_this_adaptive_extension": name in NEW_MODULES})
            passed = passed and clean
            if not clean:
                print(result.stdout)
                break
        if passed:
            fingerprints = {}
            for target in NEW_MODULES:
                dep_result = run([str(compiler), "--deps", f"{target}.lean"], build, env)
                assert dep_result.returncode == 0, dep_result.stdout
                for line in dep_result.stdout.splitlines():
                    p = Path(line.strip())
                    if p.is_file():
                        label = str(p) if not p.is_relative_to(build) else p.name
                        fingerprints[label] = sha(p.read_bytes())
            direct_imports = [{"path": p, "sha256": h} for p, h in sorted(fingerprints.items())]
    unchanged = all(path.read_bytes() == inputs[name] for name, path in MODULES.items())
    unchanged = unchanged and sha(compiler.read_bytes()) == compiler_hash
    unchanged = unchanged and sha(Path(__file__).read_bytes()) == checker_hash
    unchanged = unchanged and manifest_path.read_bytes() == manifest_bytes
    unchanged = unchanged and (ROOT / "lean-toolchain").read_bytes() == toolchain_bytes
    passed = passed and unchanged
    adaptive_audits = [a for m in modules if m["new_in_this_adaptive_extension"] for a in m["audits"]]
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "fresh_local_source_build": True,
        "inputs_unchanged": unchanged, "toolchain": EXPECTED_TOOLCHAIN,
        "lean_version": version.stdout.strip(), "compiler_path": str(compiler),
        "compiler_sha256": compiler_hash, "checker_sha256": checker_hash,
        "toolchain_sha256": sha(toolchain_bytes), "mathlib_revision": MATHLIB_REV,
        "dependency_project": str(project), "manifest_sha256": sha(manifest_bytes),
        "upstream_libraries": "Existing pinned cache used; upstream Mathlib was not rebuilt.",
        "direct_import_fingerprints": direct_imports, "modules": modules,
        "new_audits": len(adaptive_audits),
        "replayed_inherited_audits": sum(len(m["audits"]) for m in modules) - len(adaptive_audits),
        "new_axioms": sorted({a for r in adaptive_audits for a in r["axioms"]}),
        "scope": "Acquired total discrepancy and new coordinate cause an actual description revision, with continued drift during inquiry, inherited resource accounting and a bounded additive response; matched causal and failure controls.",
        "limits": "Supplied observation/response laws, fixed inquiry schedule and thresholds; no empirical validation, automatic discovery of the missing coordinate, full controller synthesis or ancestral numerical replay.",
    }
    (ROOT / "changing-dependency-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ["status", "new_audits", "replayed_inherited_audits", "new_axioms", "inputs_unchanged"]}))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
