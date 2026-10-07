#!/usr/bin/env python3
"""Fresh, portable Lean 4.29.1 build of whole-port support and its direct closure.

No repository .olean is reused. Every audited declaration must have an empty
axiom report. New modules must audit every definition and theorem. The receipt
records source hashes and raw compiler output, not a claim of empirical or
metaphysical necessity. Set LEAN to the pinned compiler executable if needed.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = CORE.parents[4]
ROOTS = [HERE, CORE, CORE / "conditional", CORE / "conditional/native-port",
         CORE / "conditional/renewal", REPO / "experiments/valuation-development/lean"]
TARGETS = ["WholePortContinuation", "PortRenewalBoundary"]
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def modules():
    ordered, seen = [], set()

    def visit(name):
        if name in seen or name.split(".")[0] in {"Init", "Std", "Lean"}:
            return
        candidates = [root / (name + ".lean") for root in ROOTS
                      if (root / (name + ".lean")).is_file()]
        assert len(candidates) == 1, (name, candidates)
        path = candidates[0]
        seen.add(name)
        for line in re.findall(r"^import (.+)$", path.read_text(), re.M):
            for dependency in line.split():
                visit(dependency)
        ordered.append((name, path))

    for target in TARGETS:
        visit(target)
    return ordered


def main():
    lean = os.environ.get("LEAN") or shutil.which("lean")
    assert lean, "lean not found"
    version = subprocess.run([lean, "--version"], capture_output=True, text=True, check=True).stdout.strip()
    assert "version 4.29.1," in version, version
    rows, passed = [], True
    closure = modules()
    with tempfile.TemporaryDirectory(prefix="whole-port-continuation-") as tmp:
        build = Path(tmp)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name, path in closure:
            data = path.read_bytes()
            (build / (name + ".lean")).write_bytes(data)
            source = re.sub(r"/-.*?-/|--[^\n]*", "", data.decode(), flags=re.S)
            forbidden = re.findall(r"\b(sorry|admit|native_decide)\b|^\s*(?:axiom|opaque|constant)\s+\S+",
                                   source, re.M)
            result = subprocess.run([lean, "-o", name + ".olean", name + ".lean"],
                                    cwd=build, env=env, capture_output=True, text=True, timeout=600)
            output = result.stdout + result.stderr
            audits = AUDIT.findall(output)
            nonempty = {n: a for n, a in audits if a.strip()}
            declarations = re.findall(r"^(?:theorem|def) (\w+)", source, re.M)
            audited = {n.rsplit(".", 1)[-1] for n, _ in audits}
            missing = [n for n in declarations if n not in audited] if name in TARGETS else []
            clean = result.returncode == 0 and not forbidden and not nonempty and not missing
            if name in TARGETS:
                clean = clean and "warning" not in output and bool(audits)
            rows.append({"module": name, "source": str(path.relative_to(REPO)),
                         "source_sha256": sha(data), "exit_code": result.returncode,
                         "audits": len(audits), "nonempty_audits": nonempty,
                         "unaudited_new_declarations": missing, "clean": clean,
                         "compiler_output": output})
            print(json.dumps({"module": name, "clean": clean, "audits": len(audits)}), flush=True)
            if not clean:
                print(output)
                passed = False
                break
    passed = passed and len(rows) == len(closure)
    record = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "passed" if passed else "failed", "lean_version": version,
              "modules": rows, "total_audits": sum(r["audits"] for r in rows),
              "scope": "Conditional whole-port conservation, sustain laws and finite continuation; "
                       "formation without the interface draw is a tested rival, not a physical derivation. "
                       "No normative warrant is proved."}
    (HERE / "whole-port-continuation-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(rows), "audits": record["total_audits"]}))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
