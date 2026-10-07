#!/usr/bin/env python3
"""Build the new common-history entry and its exact import closure from source."""

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
ROOTS = [HERE, CORE, CORE / "inquiry-root", CORE / "deeper", CORE / "naturalism",
         CORE / "conditional", CORE / "conditional/native-port",
         CORE / "conditional/renewal", REPO / "experiments/valuation-development/lean"]
TARGET = "IntegratedPortContinuation"
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def closure():
    ordered, seen = [], set()

    def visit(name):
        if name in seen or name.split(".")[0] in {"Init", "Std", "Lean"}:
            return
        paths = [root / (name + ".lean") for root in ROOTS
                 if (root / (name + ".lean")).is_file()]
        assert len(paths) == 1, (name, paths)
        seen.add(name)
        path = paths[0]
        for line in re.findall(r"^import (.+)$", path.read_text(), re.M):
            for dependency in line.split():
                visit(dependency)
        ordered.append((name, path))

    visit(TARGET)
    return ordered


def main():
    lean = os.environ.get("LEAN") or shutil.which("lean")
    assert lean, "Lean unavailable"
    prefix = [lean]
    if "LEAN" not in os.environ and shutil.which("elan"):
        prefix.append("+leanprover/lean4:v4.29.1")
    version = subprocess.check_output(prefix + ["--version"], text=True).strip()
    assert "version 4.29.1," in version, version
    sources = closure()
    rows = []
    with tempfile.TemporaryDirectory(prefix="integrated-continuation-") as temporary:
        build = Path(temporary)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name, path in sources:
            data = path.read_bytes()
            (build / (name + ".lean")).write_bytes(data)
            result = subprocess.run(prefix + ["-o", name + ".olean", name + ".lean"],
                                    cwd=build, env=env, capture_output=True, text=True,
                                    timeout=600)
            output = result.stdout + result.stderr
            audits = AUDIT.findall(output)
            nonempty = {name: axioms for name, axioms in audits if axioms.strip()}
            missing = []
            if name == TARGET:
                declared = re.findall(r"^(?:theorem|def|abbrev|structure|inductive) (\w+)",
                                      data.decode(), re.M)
                found = {name.rsplit(".", 1)[-1] for name, _ in audits}
                missing = [name for name in declared if name not in found]
            clean = (result.returncode == 0 and not nonempty and not missing
                     and not re.search(r"\b(?:warning|error):", output))
            rows.append({"module": name, "source": str(path.relative_to(REPO)),
                         "source_sha256": sha(data), "exit_code": result.returncode,
                         "audits": len(audits), "nonempty_audits": nonempty,
                         "missing_new_audits": missing, "clean": clean,
                         "compiler_output": output})
            if not clean:
                print(output, flush=True)
                break
    unchanged = all(sha(path.read_bytes()) == row["source_sha256"]
                    for (_, path), row in zip(sources, rows))
    passed = len(rows) == len(sources) and unchanged and all(row["clean"] for row in rows)
    report = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "checker_sha256": sha(Path(__file__).read_bytes()),
              "status": "passed" if passed else "failed", "lean_version": version,
              "modules": rows, "sources_unchanged": unchanged,
              "total_audits": sum(row["audits"] for row in rows),
              "scope": "One actual history carries native support, finite-source bounds "
                       "and the retained contact profile. This does not derive a renewable "
                       "ChannelLaw, an ethical order or empirical realization."}
    (HERE / "integrated-continuation-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "modules": len(rows),
                      "audits": report["total_audits"]}), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
