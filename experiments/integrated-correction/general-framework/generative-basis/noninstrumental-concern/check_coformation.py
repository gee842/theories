#!/usr/bin/env python3
"""Fresh source-bound check of joint occurrence descriptions and actual histories."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
CORE = HERE.parent / "lean"
PLASTICITY = REPO / (
    "experiments/shared-renewal-capability/regulation/retention/formation/selectors/"
    "updaters/prediction/recipient-correction/identification/recording/reason-consumer/"
    "action/revision/evaluation/plasticity/formal"
)
NEW = {"CoupledOccurrence", "CoupledConcernHistory"}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    inherited_bytes = (PLASTICITY / "verification.json").read_bytes()
    inherited = json.loads(inherited_bytes)
    assert inherited["status"] == "passed"
    compiler = Path(inherited["compiler"])
    assert sha(compiler.read_bytes()) == inherited["compiler_sha256"]
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    assert "version 4.29.1," in version
    paths = {row["module"]: REPO / row["source"] for row in inherited["modules"]}
    paths["CoupledOccurrence"] = CORE / "CoupledOccurrence.lean"
    paths["CoupledConcernHistory"] = HERE / "CoupledConcernHistory.lean"
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    for row in inherited["modules"]:
        assert sha(frozen[row["module"]]) == row["sha256"], row["module"]
    checker = Path(__file__).read_bytes()
    seen = set()
    for name, data in frozen.items():
        source = data.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M), name
        assert set(re.findall(r"^import (\S+)$", source, re.M)) <= seen | {"Std"}, name
        seen.add(name)
    assert re.findall(r"^import (\S+)$", frozen["CoupledOccurrence"].decode(), re.M) == ["GenerativeCore"]
    attempt = HERE / "coformation-checks" / str(time.time_ns())
    attempt.mkdir(parents=True)
    (attempt / "inputs.json").write_text(json.dumps(
        {name: {"source": str(paths[name].relative_to(REPO)), "sha256": sha(data)}
         for name, data in frozen.items()}, indent=2) + "\n")
    rows = []
    with tempfile.TemporaryDirectory(prefix="generative-coformation-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name, data in frozen.items():
            try:
                result = subprocess.run([str(compiler), "-o", name + ".olean", name + ".lean"],
                                        cwd=build, env=env, text=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, timeout=240)
            except subprocess.TimeoutExpired as error:
                output = error.stdout or ""
                if isinstance(output, bytes):
                    output = output.decode(errors="replace")
                result = subprocess.CompletedProcess([], 124, output + "\nCompilation timeout after 240s\n")
            log = attempt / (name + ".txt")
            log.write_text(result.stdout)
            requested = re.findall(r"^#print axioms (\S+)$", data.decode(), re.M)
            audits = {n: sorted(a.strip() for a in deps.split(",") if a.strip())
                      for n, deps in AUDIT.findall(result.stdout)}
            clean = result.returncode == 0 and "warning:" not in result.stdout
            clean = clean and len(audits) == len(requested) and all(
                actual == expected or actual.endswith("." + expected)
                for actual, expected in zip(audits, requested))
            clean = clean and all(set(a) <= {"propext", "Quot.sound", "Classical.choice"}
                                  for a in audits.values())
            rows.append({"module": name, "source": str(paths[name].relative_to(REPO)),
                         "sha256": sha(data), "new": name in NEW, "passed": clean,
                         "exit_code": result.returncode, "axioms_by_declaration": audits,
                         "log": str(log.relative_to(HERE)), "log_sha256": sha(log.read_bytes())})
            print(json.dumps({"module": name, "passed": clean, "audits": len(audits)}), flush=True)
            if not clean:
                print(result.stdout, flush=True)
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in paths.items())
    unchanged = unchanged and Path(__file__).read_bytes() == checker
    unchanged = unchanged and (PLASTICITY / "verification.json").read_bytes() == inherited_bytes
    passed = len(rows) == len(paths) and all(row["passed"] for row in rows) and unchanged
    record = {"status": "passed" if passed else "failed",
              "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "compiler": str(compiler), "compiler_sha256": sha(compiler.read_bytes()),
              "version": version, "checker_sha256": sha(checker),
              "inherited_receipt_sha256": sha(inherited_bytes),
              "fresh_temporary_build": True, "inputs_unchanged": unchanged,
              "core_imports_only_generative_core": True, "modules": rows,
              "new_audits": sum(len(row["axioms_by_declaration"]) for row in rows if row["new"]),
              "scope": "Conservative joint occurrence descriptions of the existing Process/Trace; "
                       "actual unchanged plasticity histories, intermediate decrease retention and "
                       "endpoint-summary insufficiency. No new controller, internal observation "
                       "mechanism, experience realization or ethical necessity is established."}
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        (HERE / "coformation-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print("RECEIPT " + str(attempt / "receipt.json"), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
