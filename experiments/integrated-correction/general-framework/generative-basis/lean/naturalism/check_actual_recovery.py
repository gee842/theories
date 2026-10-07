#!/usr/bin/env python3
"""Fresh-check ActualRecovery and its unchanged naturalism dependency closure.

The original package checker/receipt remain untouched. Every new theorem has an
empty axiom audit. A separate enumeration reconstructs finite activity histories
from the concrete step relation, without importing Lean's computed values.
"""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

import check as naturalism

ROOT = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def independent_check():
    def step(s, a):
        if a == "close":
            assert s is True
            return False
        if a == "restore":
            assert s is False
            return True
        if a == "realize":
            assert s is True
            return True
        assert a == "hold"
        return s

    cases = 0
    for n in range(101):
        for start, word, expected in (
            (True, ["close", "restore"] * n, (n, n, n)),
            (True, ["realize", "hold"] * n, (0, 0, 0)),
            (False, ["hold"] * n, (0, 0, n)),
        ):
            state = start
            losses = recoveries = interruptions = 0
            for action in word:
                following = step(state, action)
                losses += state and not following
                recoveries += not state and following
                interruptions += not following
                state = following
            assert (losses, recoveries, interruptions) == expected
            assert losses + int(state) == recoveries + int(start)
            assert state == start
            cases += 1
    return {"status": "passed", "cases": cases,
            "scope": "n=0..100 for episode, maintained, postponed histories"}


def main():
    toolchain, version, lean = naturalism.compiler()
    sources = dict(naturalism.SOURCES, ActualRecovery=ROOT / "ActualRecovery.lean")
    frozen = {name: path.read_bytes() for name, path in sources.items()}
    receipt = json.loads((ROOT / "verification.json").read_text())
    previous = {module["module"]: module["source_sha256"] for module in receipt["modules"]}
    for name in naturalism.SOURCES:
        assert sha(frozen[name]) == previous[name], f"Changed dependency: {name}"
    own = frozen["ActualRecovery"].decode()
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", own)
    assert not re.search(r"^\s*(axiom|constant)\s", own, re.M)
    theorems = set(re.findall(r"^theorem\s+(\S+)", own, re.M))
    requested = re.findall(r"^#print axioms (\S+)", own, re.M)
    assert theorems == {name.rsplit(".", 1)[-1] for name in requested}
    outputs = ROOT / "actual-recovery-verification"
    outputs.mkdir(exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix="actual-recovery-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in sources:
            result = naturalism.run([str(lean), "-o", name + ".olean", name + ".lean"], build, env)
            log = outputs / (name + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout, re.S)
            clean = result.returncode == 0 and all(
                marker not in result.stdout for marker in ("warning:", "error:", "sorryAx"))
            if name == "ActualRecovery":
                clean = clean and len(audits) == len(requested) and all(not a.strip() for _, a in audits)
            results.append({"module": name, "source_sha256": sha(frozen[name]),
                            "source": os.path.relpath(sources[name], ROOT),
                            "exit_code": result.returncode, "clean": clean,
                            "audits": len(audits), "empty_audits": sum(not a.strip() for _, a in audits),
                            "output": os.path.relpath(log, ROOT), "output_sha256": sha(log.read_bytes())})
            if not clean:
                print(result.stdout)
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in sources.items())
    passed = len(results) == len(sources) and unchanged and all(r["clean"] for r in results)
    independent = independent_check() if passed else {"status": "not run"}
    record = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "passed" if passed else "failed", "lean_version": version,
              "toolchain": toolchain, "compiler_sha256": sha(lean.read_bytes()),
              "checker_sha256": sha(Path(__file__).read_bytes()),
              "inherited_checker_sha256": sha((ROOT / "check.py").read_bytes()),
              "inherited_receipt_sha256": sha((ROOT / "verification.json").read_bytes()),
              "fresh_temporary_build": True, "sources_unchanged": unchanged,
              "modules": results, "independent_reconstruction": independent,
              "scope": "Actual loss/recovery balance, retained interruption, and a finite same-process "
              "counterexample to eventual-level reduction. No ethical ordering or duration metric is derived."}
    (ROOT / "actual-recovery-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audits": results[-1]["audits"] if passed else 0,
                      "independent": independent}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
