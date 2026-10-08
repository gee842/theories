#!/usr/bin/env python3
"""Kernel-check judgment under warranted extension of its evaluative content.

Audits explicit top-level declarations, not generated projections/constructors.
No clinical, field, probability or normative-premise validation is performed.
"""
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
MODULES = ["PracticalJudgment", "ConcernExtension"]


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "concern-extension-checks" / stamp
    retained.mkdir(parents=True, exist_ok=False)
    sources = {n: (HERE / (n + ".lean")).read_bytes() for n in MODULES}
    helpers = {p.name: p.read_bytes() for p in [Path(__file__), HERE / "check.py"]}
    for name, data in helpers.items():
        (retained / name).write_bytes(data)
    for name, data in sources.items():
        (retained / (name + ".lean")).write_bytes(data)
    registry = {}
    for name, data in sources.items():
        source = data.decode()
        allowed = ["PracticalJudgment"] if name == "ConcernExtension" else ["Std"]
        assert re.findall(r"^import\s+(.+)$", support.code_only(source), re.M) == allowed
        # Validate the actual import above; reuse only the inherited declaration
        # scanner after substituting its accepted import token. Compile originals.
        registry[name] = support.declarations(source.replace("import PracticalJudgment", "import Std"))
    lean = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
    receipt = {
        "status": "checking", "utc": stamp,
        "scope": "Eight general extension results under the inherited J1/J2 comparator. Acquisition, meaning, ethical relevance and classification are substantive premises; 30 inherited theorems remain separately counted.",
        "retained_run": str(retained.relative_to(HERE)),
        "source_sha256": {n: support.digest(v) for n, v in sources.items()},
        "checker_sha256": {n: support.digest(v) for n, v in helpers.items()},
        "compiler_sha256": support.digest(lean.read_bytes()),
    }
    try:
        records = []
        with tempfile.TemporaryDirectory(prefix="concern-extension-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": str(work)}

            def run(args, log):
                result = subprocess.run([str(lean), *args], cwd=work, env=env,
                                        text=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, timeout=120)
                (retained / log).write_text(result.stdout)
                assert result.returncode == 0, result.stdout
                assert not re.search(r"\b(?:error|warning):", result.stdout), result.stdout
                return result.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            for name, data in sources.items():
                (work / (name + ".lean")).write_bytes(data)
            for name in MODULES:
                run(["-o", name + ".olean", name + ".lean"], name + ".log")
                for kind, directive in [("AxiomAudit", "#print axioms "), ("Signatures", "#check ")]:
                    audit = "import " + name + "\n" + "\n".join(
                        directive + item["name"] for item in registry[name]) + "\n"
                    filename = name + kind + ".lean"
                    (work / filename).write_text(audit)
                    (retained / filename).write_text(audit)
                    output = run([filename], name + kind + ".log")
                    if kind == "AxiomAudit":
                        dependencies = {}
                        for item in registry[name]:
                            full = item["name"]
                            if "'" + full + "' does not depend on any axioms" in output:
                                axioms = []
                            else:
                                found = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                                assert found, full
                                axioms = [a.strip() for a in found[1].split(",") if a.strip()]
                            assert set(axioms) <= support.STANDARD_AXIOMS, (full, axioms)
                            dependencies[full] = axioms
                records.append({"module": name,
                                "theorems": sum(x["kind"] == "theorem" for x in registry[name]),
                                "declarations": registry[name], "axiom_dependencies": dependencies,
                                "kernel_checked": True})
        assert all((HERE / (n + ".lean")).read_bytes() == v for n, v in sources.items())
        assert all((HERE / n).read_bytes() == v for n, v in helpers.items())
        receipt["source_unchanged_during_check"] = True
        receipt["modules"] = records
        receipt["status"] = "passed"
    except Exception as error:
        receipt["status"] = "failed"
        receipt["error"] = str(error)
        raise
    finally:
        receipt["artifact_sha256"] = {p.name: support.digest(p.read_bytes())
                                      for p in sorted(retained.iterdir()) if p.is_file()}
        serialized = json.dumps(receipt, indent=2) + "\n"
        (retained / "verification.json").write_text(serialized)
        (HERE / "concern-extension-verification.json").write_text(serialized)
    print(json.dumps({"status": receipt["status"], "modules": [
        {"module": r["module"], "theorems": r["theorems"], "audits": len(r["declarations"]),
         "axioms": sorted({a for deps in r["axiom_dependencies"].values() for a in deps})}
        for r in records]}, indent=2))


if __name__ == "__main__":
    main()
