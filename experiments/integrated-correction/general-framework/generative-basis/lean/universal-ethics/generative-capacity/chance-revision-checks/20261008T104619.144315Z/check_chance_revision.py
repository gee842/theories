#!/usr/bin/env python3
"""Kernel-check chance revision diagnostics; audit explicit declarations and retain evidence."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
import check as support

HERE = Path(__file__).resolve().parent
NAME = "ChanceRevision"
SOURCE = HERE / (NAME + ".lean")


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "chance-revision-checks" / stamp
    retained.mkdir(parents=True, exist_ok=False)
    content = SOURCE.read_bytes()
    helpers = {p.name: p.read_bytes() for p in (Path(__file__), HERE / "check.py")}
    (retained / SOURCE.name).write_bytes(content)
    for name, data in helpers.items():
        (retained / name).write_bytes(data)
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": support.TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "source_sha256": support.digest(content),
        "checker_sha256": {n: support.digest(b) for n, b in helpers.items()},
        "scope": "Two fair independent draws supply four uniform tickets. Keeping a settled first result and redrawing have the same full terminal joint law but differ in history fidelity. Conditional chance reset conflicts with fidelity. No mathematical declaration establishes initial fairness, ethical settlement authority or immunity from justified correction.",
    }
    try:
        registry = support.declarations(content.decode())
        assert re.findall(r"^import\s+(.+)$", support.code_only(content.decode()), re.M) == ["Std"]
        assert sum(d["kind"] == "theorem" for d in registry) == 7
        command = [str(Path.home() / ".elan/bin/lean"), "+" + support.TOOLCHAIN]
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = support.digest(binary.read_bytes())
        with tempfile.TemporaryDirectory(prefix="chance-revision-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": str(work)}
            (work / SOURCE.name).write_bytes(content)

            def run(args, log):
                result = subprocess.run(command + args, cwd=work, env=env, text=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=60)
                (retained / log).write_text(result.stdout)
                assert result.returncode == 0, result.stdout
                assert not re.search(r"\b(?:error|warning):", result.stdout), result.stdout
                return result.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            assert "version 4.29.1" in receipt["lean_version"]
            run(["-o", NAME + ".olean", SOURCE.name], "compile.log")
            audit = "import " + NAME + "\n" + "\n".join(
                "#print axioms " + item["name"] for item in registry) + "\n"
            (work / "Audit.lean").write_text(audit)
            (retained / "Audit.lean").write_text(audit)
            output = run(["Audit.lean"], "axioms.log")
            dependencies = {}
            for item in registry:
                name = item["name"]
                assert "'" + name + "' does not depend on any axioms" in output, (name, output)
                dependencies[name] = []
        assert SOURCE.read_bytes() == content
        assert all((HERE / n).read_bytes() == b for n, b in helpers.items())
        receipt.update(status="passed", kernel_checked=True, new_theorems=7,
                       declarations=registry, declaration_audits=len(registry),
                       axiom_dependencies=dependencies, source_unchanged_during_check=True)
        receipt["artifact_sha256"] = {
            p.name: support.digest(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()
        }
    except Exception as error:
        receipt.update(status="failed", error=str(error))
        raise
    finally:
        body = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
        (retained / "verification.json").write_text(body)
        (HERE / "chance-revision-verification.json").write_text(body)
    print(json.dumps({"status": receipt["status"], "new_theorems": 7,
                      "declaration_audits": receipt["declaration_audits"], "axioms": []}))


if __name__ == "__main__":
    main()
