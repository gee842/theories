#!/usr/bin/env python3
"""Independent review: immutable receipt bindings and isolated Lean recompilation."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
BASE = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"
DOC = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-DIRECTION.md"
INTEGRATION = HERE.parents[1] / "ALIGNMENT-DIRECTION-INTEGRATION.md"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    receipt_bytes = (BASE / "alignment-direction-verification.json").read_bytes()
    r = json.loads(receipt_bytes)
    assert r["status"] == "passed"
    frozen = BASE / r["retained_run"]
    assert receipt_bytes == (frozen / "verification.json").read_bytes()
    for name, sha in r["artifact_sha256"].items():
        assert digest((frozen / name).read_bytes()) == sha, name
    for name, sha in r["checker_sha256"].items():
        assert digest((BASE / name).read_bytes()) == sha, name
    sources = {name: (BASE / (name + ".lean")).read_bytes() for name in r["source_sha256"]}
    for name, data in sources.items():
        assert digest(data) == r["source_sha256"][name]
        assert data == (frozen / (name + ".lean")).read_bytes()
    binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
    assert digest(binary.read_bytes()) == r["lean_binary_sha256"]
    docs = {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in [DOC, INTEGRATION]}
    counts = {}
    with tempfile.TemporaryDirectory(prefix="alignment-direction-independent-review-") as folder:
        work = Path(folder)
        for name, data in sources.items():
            (work / (name + ".lean")).write_bytes(data)

        def run(args, log):
            p = subprocess.run([str(binary)] + args, cwd=work,
                               env={**os.environ, "LEAN_PATH": str(work)},
                               text=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, timeout=120)
            (HERE / log).write_text(p.stdout)
            assert p.returncode == 0, p.stdout
            assert not re.search(r"\b(?:error|warning):", p.stdout), p.stdout
            return p.stdout

        version = run(["--version"], "version.log").strip()
        assert version == r["lean_version"]
        for name, data in sources.items():
            source = data.decode()
            # These manually inspected sources have no nested block comments,
            # strings, generated structures or nested declaration namespaces.
            clean = re.sub(r"/-.*?-/", "", source, flags=re.S)
            clean = re.sub(r"--[^\n]*", "", clean)
            assert not re.search(r"\b(?:sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|debug\.skipKernelTC", clean)
            assert re.findall(r"^namespace (\w+)$", clean, re.M) == [name]
            imports = re.findall(r"^import (\w+)$", clean, re.M)
            assert imports == (["Std"] if name == "PracticalJudgment" else ["PracticalJudgment"])
            declarations = [{"kind": kind, "name": name + "." + short}
                            for kind, short in re.findall(r"^(def|theorem) (\w+)\b", clean, re.M)]
            record = next(m for m in r["modules"] if m["module"] == name)
            assert declarations == record["declarations"]
            assert sum(d["kind"] == "theorem" for d in declarations) == record["theorems"]
            run(["-o", name + ".olean", name + ".lean"], name + ".log")
            audit = "import " + name + "\n" + "\n".join("#print axioms " + d["name"] for d in declarations) + "\n"
            (work / (name + "Audit.lean")).write_text(audit)
            output = run([name + "Audit.lean"], name + "AxiomAudit.log")
            assert output == (frozen / (name + "AxiomAudit.log")).read_text()
            for d in declarations:
                full = d["name"]
                if "'" + full + "' does not depend on any axioms" in output:
                    dependencies = []
                else:
                    match = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                    assert match, full
                    dependencies = [a.strip() for a in match[1].split(",") if a.strip()]
                assert dependencies == record["axiom_dependencies"][full]
                assert set(dependencies) <= {"propext", "Quot.sound", "Classical.choice"}
            signatures = "import " + name + "\n" + "\n".join("#check " + d["name"] for d in declarations if d["kind"] == "theorem") + "\n"
            (work / (name + "Signatures.lean")).write_text(signatures)
            signatures_output = run([name + "Signatures.lean"], name + "Signatures.log")
            assert signatures_output == (frozen / (name + "Signatures.log")).read_text()
            counts[name] = {"theorems": record["theorems"], "explicit_declarations": len(declarations)}
    assert receipt_bytes == (BASE / "alignment-direction-verification.json").read_bytes()
    for name, data in sources.items():
        assert data == (BASE / (name + ".lean")).read_bytes()
    for path, sha in docs.items():
        assert digest((ROOT / path).read_bytes()) == sha
    result = {
        "status": "passed_independent_source_binding_and_isolated_recompilation",
        "utc": datetime.now(timezone.utc).isoformat(),
        "author_retained_run": r["retained_run"],
        "author_receipt_sha256": digest(receipt_bytes),
        "author_retained_artifacts_verified": len(r["artifact_sha256"]),
        "source_sha256": r["source_sha256"],
        "document_sha256": docs,
        "lean_version": version,
        "lean_binary_sha256": r["lean_binary_sha256"],
        "counts": counts,
        "independent_logs_match_author": True,
        "scope": "Independent exact-source compilation, signature/dependency comparison and receipt consistency. Does not establish philosophical warrant or actual-world correspondence.",
        "review_script_sha256": digest(Path(__file__).read_bytes()),
        "review_log_sha256": {p.name: digest(p.read_bytes()) for p in sorted(HERE.glob("*.log"))},
    }
    (HERE / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
