"""Compile the structural core and record the exact source and axiom report."""

from pathlib import Path
import hashlib
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone


def main() -> int:
    root = Path(__file__).resolve().parent
    source = root / "GenerativeCore.lean"
    lean = shutil.which("lean")
    if lean is None:
        print("Lean is not on PATH; install the toolchain in lean-toolchain.")
        return 1

    version = subprocess.run(
        [lean, "--version"], cwd=root, capture_output=True, text=True
    )
    if version.returncode != 0:
        print(version.stdout + version.stderr)
        return version.returncode

    result = subprocess.run(
        [lean, source.name], cwd=root, capture_output=True, text=True
    )
    contents = source.read_text(encoding="utf-8")
    names = re.findall(r"^theorem\s+(\w+)", contents, flags=re.MULTILINE)
    output = result.stdout + result.stderr
    missing = [
        name for name in names
        if f"'GenerativeCore.{name}' " not in output
    ]
    forbidden = bool(re.search(r"^\s*(?:axiom|sorry)\b", contents, re.MULTILINE))
    passed = (
        result.returncode == 0
        and not missing
        and "sorryAx" not in output
        and not forbidden
        and "version 4.29.1," in version.stdout
    )
    report = "\n".join([
        "Generative foundations — structural proof verification",
        f"Checked at: {datetime.now(timezone.utc).isoformat()}",
        f"Toolchain: {version.stdout.strip()}",
        f"Source SHA256: {hashlib.sha256(source.read_bytes()).hexdigest()}",
        f"Compile return code: {result.returncode}",
        f"Theorem declarations: {len(names)}",
        f"Missing axiom reports: {missing}",
        f"Result: {'PASS' if passed else 'FAIL'}",
        "",
        output.rstrip(),
        "",
        "Scope: structural statements in the declared mathematical models.",
        "This check does not prove moral premises or empirical adequacy.",
        "",
    ])
    (root / "verification.txt").write_text(report, encoding="utf-8")
    print(report)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
