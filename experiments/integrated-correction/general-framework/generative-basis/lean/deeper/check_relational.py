#!/usr/bin/env python3
"""Build RelationalDynamics with its import closure and require empty axiom audits.

Uses `lean +<toolchain>` when elan is installed, otherwise the `lean` on PATH,
and requires Lean 4.29.1 either way. No axiom is allowed, including propext,
Quot.sound and Classical.choice.
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

ROOT = Path(__file__).resolve().parent
MODULES = ["GenerativeCore", "DynamicUnderdetermination", "RelationalDynamics"]
SOURCES = {name: (ROOT.parent if name == "GenerativeCore" else ROOT) /
           (name + ".lean") for name in MODULES}
NEW = {"RelationalDynamics"}
ALLOWED_AXIOMS = set()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=300)


def main():
    toolchain = (ROOT / "lean-toolchain").read_text().strip()
    lean = ["lean", "+" + toolchain] if shutil.which("elan") else ["lean"]
    version = run(lean + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout, version.stdout
    prefix = run(lean + ["--print-prefix"], ROOT)
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin" / "lean"
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
    results = []
    output_dir = ROOT / "verification"
    output_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="relational-dynamics-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in MODULES:
            result = run([str(compiler), "-o", name + ".olean", name + ".lean"], build, env)
            if name in NEW:
                (output_dir / (name + ".txt")).write_text(result.stdout)
            result.check_returncode()
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout)
            used = {a.strip() for _, axioms in audits for a in axioms.split(",") if a.strip()}
            if name in NEW:
                assert audits, name
                assert used <= ALLOWED_AXIOMS, (name, sorted(used))
            results.append({"module": name, "sha256": digest(frozen[name]),
                            "audits": len(audits), "axioms": sorted(used)})
    receipt = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "lean_version": version.stdout.strip(),
        "compiler_sha256": digest(compiler.read_bytes()),
        "allowed_axioms": sorted(ALLOWED_AXIOMS),
        "modules": results,
    }
    (ROOT / "relational-dynamics-verification.json").write_text(
        json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
