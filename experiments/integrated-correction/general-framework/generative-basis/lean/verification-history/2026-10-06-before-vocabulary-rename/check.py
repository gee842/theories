#!/usr/bin/env python3
"""Check that the 6 October 2026 vocabulary rename changed names only.

Builds the current sources of every module whose identifiers changed, together
with their full import closures (41 modules), in a fresh temporary directory.
Each audited declaration must report exactly the axioms recorded for the same
declaration before the rename (before-audits.json, built from the preserved
sources here), under the declared renames. Builds must have no warnings.
SupportedRevision needs Mathlib and is outside this check; its change is four
identifier substitutions recorded in the preserved source diff.
"""
from datetime import datetime, timezone
import hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[6]
SEARCH = ["experiments/integrated-correction/general-framework/generative-basis",
          "experiments/shared-renewal-capability/regulation/retention/formation/formal",
          "experiments/valuation-development/lean"]
ROOTS = ["GenerativeDerivedProcessLawModel", "RenewalExamples", "SupportNecessity",
         "NativePortContinuation", "PatientConcern", "ControllerRevision", "FormationSupport",
         # Modules that reached main while the rename was in progress, renamed on merge.
         "PortValuation", "PhaseCycleDerivation"]
SKIP = re.compile(r"/(runs?|sources|verification[^/]*|legacy-replays|[^/]*-checks|[^/]*-runs|"
                  r"snapshots?|adaptive-verification|[^/]*-development)(/|$)")


def lean():
    for prefix in (["lean", "+leanprover/lean4:v4.29.1"], ["lean"]):
        try:
            out = subprocess.run(prefix + ["--version"], capture_output=True, text=True)
        except FileNotFoundError:
            continue
        if out.returncode == 0 and "version 4.29.1," in out.stdout:
            where = subprocess.run(prefix + ["--print-prefix"], capture_output=True, text=True)
            return out.stdout.strip(), Path(where.stdout.strip()) / "bin" / "lean"
    raise SystemExit("Lean 4.29.1 not found")


def index():
    mods = {}
    for base in SEARCH:
        for root, _, files in os.walk(REPO / base):
            if SKIP.search(root[len(str(REPO / base)):]):
                continue
            for f in files:
                if f.endswith(".lean"):
                    mods.setdefault(f[:-5], []).append(Path(root) / f)
    return mods


def closure(mods):
    order, seen = [], set()

    def visit(m):
        if m in seen or m.split(".")[0] in ("Std", "Init", "Lean"):
            return
        seen.add(m)
        paths = mods[m]
        assert len(paths) == 1, (m, paths)
        for i in re.findall(r"^import (\S+)", paths[0].read_text(), re.M):
            visit(i)
        order.append((m, paths[0]))
    for r in ROOTS:
        visit(r)
    return order


def build(order, compiler):
    """Compile modules in order in a fresh directory; yield (module, path, result, output, audits)."""
    with tempfile.TemporaryDirectory(prefix="vocabulary-rename-") as tmp:
        for m, p in order:
            shutil.copy(p, Path(tmp) / (m + ".lean"))
        env = dict(os.environ, LEAN_PATH=tmp)
        for m, p in order:
            r = subprocess.run([str(compiler), "-o", m + ".olean", m + ".lean"], cwd=tmp, env=env,
                               capture_output=True, text=True)
            out = (r.stdout + r.stderr).replace("\n ", " ")
            audits = {a: sorted(x.strip() for x in g.split(",") if x.strip()) for a, g in re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", out)}
            yield m, p, r, out, audits
            if r.returncode:
                print(out[:4000])
                return


def record_before():
    """Rebuild before-audits.json from the preserved pre-rename sources."""
    _, compiler = lean()
    order = []
    for m, p in closure(index()):
        kept = HERE / "sources" / p.relative_to(REPO / "experiments")
        order.append((m, kept if kept.exists() else p))
    before = {}
    for m, p, r, out, audits in build(order, compiler):
        assert r.returncode == 0 and "warning:" not in out, m
        before[m] = {"source": str(p.relative_to(REPO)), "audits": audits}
    assert len(before) == len(order)
    (HERE / "before-audits.json").write_text(json.dumps(before, indent=1) + "\n")
    print(json.dumps({"before_modules": len(before), "audits": sum(len(v["audits"]) for v in before.values())}))


def main():
    if sys.argv[1:] == ["--record-before"]:
        return record_before()
    version, compiler = lean()
    before = json.loads((HERE / "before-audits.json").read_text())
    renames = json.loads((HERE / "renames.json").read_text())["declaration_renames_by_module"]
    order = closure(index())
    assert [m for m, _ in order] == list(before), "module closure changed"
    rows, mismatches = [], []
    for m, p, r, out, audits in build(order, compiler):
        mp = renames.get(m, {})

        def ren(q):
            parts = q.split(".")
            parts[-1] = mp.get(parts[-1], parts[-1])
            return ".".join(parts)
        expected = {ren(k): v for k, v in before[m]["audits"].items()}
        ok = r.returncode == 0 and "warning:" not in out and expected == audits
        if not ok:
            mismatches.append(m)
        rows.append({"module": m, "source": str(p.relative_to(REPO)),
                     "source_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                     "audits": len(audits), "renamed": sum(ren(k) != k for k in before[m]["audits"]),
                     "matches_before_under_renames": ok})
    passed = not mismatches and len(rows) == len(order)
    receipt = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
               "status": "passed" if passed else "failed", "lean_version": version,
               "compiler_sha256": hashlib.sha256(compiler.read_bytes()).hexdigest(),
               "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "modules": len(rows), "audits": sum(r["audits"] for r in rows),
               "renamed_declarations": sum(r["renamed"] for r in rows),
               "mismatches": mismatches, "rows": rows,
               "scope": "Every audited declaration in the checked closure reports the same axioms as "
                        "before the vocabulary rename, under the declared renames. This certifies a "
                        "renaming, not a new result."}
    (HERE / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in ("status", "modules", "audits", "renamed_declarations", "mismatches")}))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
