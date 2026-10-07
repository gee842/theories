#!/usr/bin/env python3
"""Fresh, source-bound Lean verification of direct material regeneration.

Snapshots the entire repository import closure before compiling, audits every
new declaration, and retains source hashes and raw output. The second target
is the separately authored reachability/formed-capability distinction.
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
TARGETS = ["PortDirectRenewal", "GenerativePossibility"]
ALLOWED_AXIOMS = {"propext", "Quot.sound"}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def closure():
    ordered, seen = [], set()

    def visit(name):
        if name in seen or name.split(".")[0] in {"Init", "Std", "Lean"}:
            return
        candidates = [root / (name.replace(".", "/") + ".lean") for root in ROOTS
                      if (root / (name.replace(".", "/") + ".lean")).is_file()]
        assert len(candidates) == 1, (name, candidates)
        path = candidates[0]
        data = path.read_bytes()
        seen.add(name)
        for line in re.findall(r"^\s*import (.+)$", data.decode(), re.M):
            for dependency in line.split("--", 1)[0].split():
                visit(dependency)
        ordered.append((name, path, data))

    for target in TARGETS:
        visit(target)
    return ordered


def main():
    lean = os.environ.get("LEAN") or shutil.which("lean")
    assert lean, "lean not found"
    version = subprocess.check_output([lean, "--version"], text=True).strip()
    assert "version 4.29.1," in version, version
    sources = closure()
    checker = Path(__file__).read_bytes()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    run = HERE / "port-direct-renewal-runs" / run_id
    snapshot = run / "sources"
    snapshot.mkdir(parents=True)
    (run / Path(__file__).name).write_bytes(checker)
    (run / "lean-toolchain").write_text("leanprover/lean4:v4.29.1\n")
    for name, _, data in sources:
        target = snapshot / (name.replace(".", "/") + ".lean")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    rows, passed = [], True
    with tempfile.TemporaryDirectory(prefix="port-direct-renewal-") as tmp:
        build = Path(tmp)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name, path, data in sources:
            relative = name.replace(".", "/")
            target = build / (relative + ".lean")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            source = re.sub(r"/-.*?-/|--[^\n]*", "", data.decode(), flags=re.S)
            forbidden = re.findall(r"\b(?:sorry|admit|native_decide)\b|^\s*(?:axiom|opaque|constant)\s+\S+",
                                   source, re.M)
            result = subprocess.run([lean, "-o", relative + ".olean", relative + ".lean"],
                                    cwd=build, env=env, capture_output=True, text=True, timeout=600)
            output = result.stdout + result.stderr
            audits = AUDIT.findall(output)
            dependencies = {n: [item.strip() for item in a.split(",") if item.strip()]
                            for n, a in audits}
            nonempty = {n: a for n, a in dependencies.items() if a}
            forbidden_axioms = {n: a for n, a in dependencies.items() if set(a) - ALLOWED_AXIOMS}
            declarations = re.findall(
                r"^\s*(?:(?:noncomputable|private|protected)\s+)*(?:def|theorem|lemma|structure|inductive|abbrev)\s+([\w.]+)",
                source, re.M)
            audited = {n.rsplit(".", 1)[-1] for n, _ in audits}
            missing = [n for n in declarations if n.rsplit(".", 1)[-1] not in audited] if name in TARGETS else []
            requested = re.findall(r"^\s*#print axioms (\S+)", source, re.M)
            requested_present = all(any(n == req or n.endswith("." + req) for n, _ in audits)
                                    for req in requested)
            clean = (result.returncode == 0 and not forbidden and not forbidden_axioms and not missing
                     and requested_present and len(audits) == len(requested))
            if name in TARGETS:
                clean = clean and "warning" not in output and bool(audits)
            rows.append({"module": name, "source": str(path.relative_to(REPO)),
                         "source_sha256": sha(data), "exit_code": result.returncode,
                         "audits": len(audits), "nonempty_audits": nonempty,
                         "forbidden_axioms": forbidden_axioms, "forbidden_source": forbidden,
                         "unaudited_new_declarations": missing, "clean": clean,
                         "compiler_output": output})
            print(json.dumps({"module": name, "clean": clean, "audits": len(audits)}), flush=True)
            if not clean:
                print(output)
                passed = False
                break
    changed = [str(path.relative_to(REPO)) for _, path, data in sources if path.read_bytes() != data]
    if Path(__file__).read_bytes() != checker:
        changed.append(str(Path(__file__).relative_to(REPO)))
    passed = passed and len(rows) == len(sources) and not changed
    record = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "passed" if passed else "failed", "lean_version": version,
              "compiler_sha256": sha(Path(lean).resolve().read_bytes()),
              "targets": TARGETS, "snapshot": str(run.relative_to(REPO)),
              "source_changed_during_run": changed, "modules": rows,
              "total_audits": sum(r["audits"] for r in rows),
              "new_declarations": sum(r["audits"] for r in rows if r["module"] in TARGETS),
              "standard_axioms_allowed": sorted(ALLOWED_AXIOMS), "checker_sha256": sha(checker),
              "scope": "Actual finite source-consuming regeneration of spare formation material; "
                       "held balance includes inquiry, recovery and optional initial formation. "
                       "Global reachability and actual formed capability remain distinct. "
                       "No new-organization, indefinite-renewal, diversity-growth or ethical theorem is claimed."}
    (HERE / "port-direct-renewal-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(rows), "audits": record["total_audits"]}))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
