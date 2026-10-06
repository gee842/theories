#!/usr/bin/env python3
"""Fresh build of the native-port continuation module from frozen source bytes.

Inherited modules must keep the source hashes recorded by their own receipts.
New declarations may use only Lean's standard propext and Quot.sound.
Uses `lean +<toolchain>` through elan when available, else `lean` on PATH;
either way the reported version must be 4.29.1.
"""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
LEAN = ROOT.parents[1]
SOURCES = {
    "GenerativeCore": LEAN / "GenerativeCore.lean",
    "Depletion": LEAN / "Depletion.lean",
    "NativePacketProcess": LEAN / "inquiry-root/sufficiency/NativePacketProcess.lean",
    "ResourceContinuation": LEAN / "conditional/ResourceContinuation.lean",
    "NativePortContinuation": ROOT / "NativePortContinuation.lean",
}
INHERITED_SHA256 = {
    "GenerativeCore": "e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8",
    "Depletion": "324021e3f315d7f06f2ae28624aa4468f1029a77347a6f3952c5313c2641aa3e",
    "NativePacketProcess": "da9d06d9f0fca5cb1252105dccb473246ad66dbdb81a63b048d63b12c9da5d7b",
}
NEW = "NativePortContinuation"
ALLOWED_AXIOMS = {"propext", "Quot.sound"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600)


def compiler():
    toolchain = (ROOT / "lean-toolchain").read_text().strip()
    for prefix in (["lean", "+" + toolchain], ["lean"]):
        try:
            version = run(prefix + ["--version"], ROOT)
        except FileNotFoundError:
            continue
        if version.returncode == 0 and "version 4.29.1," in version.stdout:
            where = run(prefix + ["--print-prefix"], ROOT)
            return toolchain, version.stdout.strip(), Path(where.stdout.strip()) / "bin" / "lean"
    raise SystemExit("Lean 4.29.1 not found")


def main():
    toolchain, version, lean = compiler()
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    for name, wanted in INHERITED_SHA256.items():
        assert digest(frozen[name]) == wanted, name
    text = frozen[NEW].decode()
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text)
    assert not re.search(r"^\s*(axiom|constant)\s", text, re.M)
    declared = re.findall(r"^(?:theorem|def)\s+(\w+)", text, re.M)
    requested = re.findall(r"^#print axioms (\S+)", text, re.M)
    theorems = re.findall(r"^theorem\s+(\w+)", text, re.M)
    assert set(theorems) <= set(requested), set(theorems) - set(requested)
    results = []
    out = ROOT / "verification"
    out.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="native-port-continuation-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in SOURCES:
            result = run([str(lean), "-o", name + ".olean", name + ".lean"], build, env)
            log = out / (name + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout.replace("\n ", " "))
            axioms = sorted({a.strip() for _, group in audits for a in group.split(",") if a.strip()})
            clean = (result.returncode == 0 and "warning:" not in result.stdout
                     and "sorryAx" not in result.stdout)
            if name == NEW:
                names = [a.rsplit(".", 1)[-1] for a, _ in audits]
                clean = clean and names == requested and set(axioms) <= ALLOWED_AXIOMS
            results.append({
                "module": name, "source": os.path.relpath(SOURCES[name], ROOT),
                "source_sha256": digest(frozen[name]), "exit_code": result.returncode,
                "audits": len(audits), "axioms": axioms,
                "empty_axiom_audits": sum(not g.strip() for _, g in audits),
                "clean": clean, "log": "verification/" + log.name,
                "log_sha256": digest(log.read_bytes()),
            })
            if not clean:
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
    passed = unchanged and len(results) == len(SOURCES) and all(r["clean"] for r in results)
    new = results[-1] if results and results[-1]["module"] == NEW else {}
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "lean_version": version,
        "toolchain": toolchain, "compiler_sha256": digest(lean.read_bytes()),
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "fresh_temporary_build": True, "source_unchanged_during_check": unchanged,
        "allowed_standard_axioms_for_new_module": sorted(ALLOWED_AXIOMS),
        "new_module_audits": new.get("audits"), "new_module_empty_audits": new.get("empty_axiom_audits"),
        "new_declarations": declared, "modules": results,
        "scope": "The reconstructed native port conserves held + enacted relative to arrived on "
                 "every call, belongs to the conditional account-law class U1 with equality, "
                 "inherits the U2 history bound and arrival-window theorem, and with only its own "
                 "source strictly lowers a potential on every completed call, so it has no "
                 "infinite execution. No inherited source is changed. This is a statement about "
                 "the Lean reconstruction, not physical identification or a derivation of the "
                 "port's gate, cycle or tariff.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "new_module_audits": record["new_module_audits"],
                      "new_module_empty_audits": record["new_module_empty_audits"]}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
