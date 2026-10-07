#!/usr/bin/env python3
"""Fresh build of ContactFormation, FormationClosure, AcquiredContact, PortValuation and ValuationInCore over the unchanged 32-module process-law closure.

Portable: uses `lean` from PATH (or $LEAN) and checks its version against the
pinned toolchain. Sources are copied into a temporary directory; no local
.olean is reused. Every #print axioms report must be empty, with no warnings,
proof placeholders or axiom declarations. The receipt is written next to this
script as contact-formation-verification.json.
"""
from datetime import datetime, timezone
import hashlib, json, os, re, shutil, subprocess, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = CORE.parents[4]
CLOSURE = HERE / "process-law-verification.json"
NEW = ["ContactFormation", "FormationClosure", "AcquiredContact", "PortValuation", "ValuationInCore",
       "RevisingPort", "RelationalCut", "PortAlignment"]
# Imported from the valuation-development package, built in the same closure.
VALUATION = ["AxiomFree", "ValuationDevelopment", "ClosedLoopValuation"]
# Imported only for their definitions; their own audits belong to their packages.
ALIGNMENT = ["RemainingDependency", "InquiryRelevance", "InquiryWarrant"]
SUPPORT = set(VALUATION + ALIGNMENT)
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    lean = os.environ.get("LEAN") or shutil.which("lean")
    assert lean, "lean not found on PATH"
    pinned = (CORE / "lean-toolchain").read_text().strip().rsplit(":v", 1)[-1]
    version = subprocess.run([lean, "--version"], capture_output=True, text=True).stdout.strip()
    assert f"version {pinned}," in version, (pinned, version)
    closure = json.loads(CLOSURE.read_bytes())
    assert closure["status"] == "passed"
    modules = [(row["module"], REPO / row["source"]) for row in closure["modules"]]
    for name, path in modules:
        recorded = next(r for r in closure["modules"] if r["module"] == name)["source_sha256"]
        assert sha(path.read_bytes()) == recorded, f"{name} changed since the process-law receipt"
    valuation_dir = REPO / "experiments/valuation-development/lean"
    modules += [(name, HERE / (name + ".lean")) for name in NEW[:3]]
    modules += [(name, valuation_dir / (name + ".lean")) for name in VALUATION]
    alignment_dir = (CORE.parent / "mathematical-abstraction/acquisition/feedback/"
                     "remaining-dependency/formal")
    modules += [(name, HERE / (name + ".lean")) for name in NEW[3:7]]
    modules += [(name, alignment_dir / (name + ".lean")) for name in ALIGNMENT]
    modules += [(name, HERE / (name + ".lean")) for name in NEW[7:]]
    rows, passed = [], True
    with tempfile.TemporaryDirectory(prefix="contact-formation-") as temporary:
        build = Path(temporary)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name, path in modules:
            data = path.read_bytes()
            built = data
            if name in SUPPORT:
                built = re.sub(rb"(?m)^#print axioms .*$", b"", data)
            (build / (name + ".lean")).write_bytes(built)
            text = re.sub(r"/-.*?-/|--[^\n]*", "", data.decode(), flags=re.S)
            placeholders = re.findall(r"\b(sorry|admit|native_decide)\b", text)
            declared = re.findall(r"^\s*(?:axiom|opaque|constant)\s+\S+", text, re.M)
            result = subprocess.run([lean, "-o", name + ".olean", name + ".lean"], cwd=build,
                                    env=env, capture_output=True, text=True, timeout=600)
            output = result.stdout + result.stderr
            audits = AUDIT.findall(output)
            nonempty = {n: a for n, a in audits if a.strip()}
            clean = (result.returncode == 0 and (name in SUPPORT or "warning" not in output)
                     and not placeholders
                     and not declared and not nonempty)
            rows.append({"module": name, "source": str(path.relative_to(REPO)),
                         "source_sha256": sha(data), "exit_code": result.returncode,
                         "audits": len(audits), "nonempty_audits": nonempty, "clean": clean})
            print(json.dumps({"module": name, "clean": clean, "audits": len(audits)}), flush=True)
            if not clean:
                print(output)
                passed = False
                break
    new_rows = [r for r in rows if r["module"] in NEW]
    passed = (passed and len(rows) == len(modules) and len(new_rows) == len(NEW)
              and all(r["audits"] > 0 for r in new_rows))
    record = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "passed" if passed else "failed", "lean_version": version,
              "modules": rows, "total_audits": sum(r["audits"] for r in rows),
              "new_module_audits": {r["module"]: r["audits"] for r in new_rows},
              "scope": "ContactFormation, FormationClosure, AcquiredContact, ValuationDevelopment, ClosedLoopValuation, PortValuation and ValuationInCore over the unchanged 32-module process-law closure. Empty axiom reports do not establish an assumption-free foundation; the salvage rate, formation and salvage tariffs and the contact-opening rule are supplied, and the inquiry schedule and its reading are described rather than built as a further mechanism."}
    (HERE / "contact-formation-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(rows), "audits": record["total_audits"]}))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
