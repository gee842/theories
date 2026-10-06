#!/usr/bin/env python3
"""Compile the unchanged public model with the additive role-free interface."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
CORE = HERE.parent / "lean"
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    original_receipt = (CORE / "verification.json").read_bytes()
    inherited = json.loads(original_receipt)
    assert inherited["status"] == "passed"
    checker = Path(__file__).read_bytes()
    compiler = Path(inherited["compiler_binary"])
    assert sha(compiler.read_bytes()) == inherited["compiler_sha256"]
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    assert "version 4.29.1," in version
    sources = {}
    paths = {}
    for module in inherited["modules"]:
        name = module["module"]
        paths[name] = CORE / module["source"]
        sources[name] = paths[name].read_bytes()
        assert sha(sources[name]) == module["source_sha256"], name
    for name in ("NondualCore", "GenerativeNondualModel"):
        paths[name] = CORE / (name + ".lean")
        sources[name] = paths[name].read_bytes()
    seen = set()
    for name, data in sources.items():
        source = data.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M), name
        for dependency in re.findall(r"^import (\S+)$", source, re.M):
            assert dependency == "Std" or dependency in seen, (name, dependency)
        seen.add(name)
    # Ethical contracts stay downstream: the public core extension imports none.
    assert not ({"GroundingContract", "PatientConcern", "NondualConcernAdapter"} & seen)
    results = []
    log_dir = HERE / "nondual-model-logs"
    log_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="generative-nondual-public-") as temporary:
        build = Path(temporary)
        for name, data in sources.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        old = {m["module"]: m for m in inherited["modules"]}
        for name, data in sources.items():
            result = subprocess.run([str(compiler), "-o", name + ".olean", name + ".lean"],
                                    cwd=build, env=env, text=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, timeout=180)
            log = log_dir / (name + ".txt")
            log.write_text(result.stdout)
            audits = {n: sorted(a.strip() for a in deps.split(",") if a.strip())
                      for n, deps in AUDIT.findall(result.stdout)}
            expected = re.findall(r"^#print axioms (\S+)$", data.decode(), re.M)
            assert len(audits) == len(expected) and all(
                actual == requested or actual.endswith("." + requested)
                for actual, requested in zip(audits, expected)
            ), (name, audits, expected, result.stdout)
            if name in old:
                assert audits == old[name]["axioms_by_declaration"], name
            else:
                assert all(not a for a in audits.values()), (name, audits)
            clean = result.returncode == 0 and "warning:" not in result.stdout
            results.append({"module": name, "source": str(paths[name].relative_to(HERE.parent)),
                            "source_sha256": sha(data), "axioms_by_declaration": audits,
                            "exit_code": result.returncode, "passed": clean,
                            "log": str(log.relative_to(HERE)), "log_sha256": sha(log.read_bytes())})
            print(json.dumps({"module": name, "passed": clean, "audits": len(audits)}), flush=True)
            if not clean:
                print(result.stdout)
                break
    unchanged = all(path.read_bytes() == sources[name] for name, path in paths.items())
    unchanged = unchanged and (CORE / "verification.json").read_bytes() == original_receipt
    unchanged = unchanged and Path(__file__).read_bytes() == checker
    passed = len(results) == len(sources) and all(r["passed"] for r in results) and unchanged
    record = {"status": "passed" if passed else "failed",
              "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "compiler": str(compiler), "compiler_sha256": sha(compiler.read_bytes()),
              "lean_version": version, "checker_sha256": sha(checker),
              "inherited_receipt_sha256": sha(original_receipt),
              "fresh_temporary_build": True, "inputs_unchanged": unchanged,
              "role_free_import_closure": True, "modules": results,
              "new_public_declarations": 2,
              "scope": "Unchanged public model plus NondualCore and two endpoint-sensitive wrappers. "
                       "Inherited proof dependencies retained; no actual sensing, subjectivity, "
                       "ethical authority or assumption-free ontology derived."}
    (HERE / "nondual-model-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    assert passed, record["status"]


if __name__ == "__main__":
    main()
