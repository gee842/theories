#!/usr/bin/env python3
"""Period-independent local-language certificates and their pinned Lean checks.

This enumerates bounded strategies over local words, never cycle periods. The
mathematical correspondence to the original knowsWithin game is recorded in
PERIOD-LOWER-BOUND-ARGUMENT.md; it is not silently counted as a Lean theorem.
"""
from __future__ import annotations

import ast
from datetime import datetime, timezone
from functools import lru_cache
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
N = 7
FULL = (1 << (1 << N)) - 1
BITS = [sum(1 << word for word in range(1 << N) if word >> p & 1) for p in range(N)]
OBSERVATIONS = [mask ^ BITS[0] for mask in BITS]
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def maximal(items):
    """Different ordering/implementation from Lean: descending cardinality."""
    retained = []
    for item in sorted(set(items), key=lambda x: (-x.bit_count(), x)):
        if not any(item & existing == item for existing in retained):
            retained.append(item)
    return tuple(retained)


@lru_cache(None)
def languages(budget, position):
    """All strategy acceptance sets up to maximal-language domination."""
    candidates = [BITS[position]]  # Stop immediately.
    if budget:
        candidates.extend(languages(budget - 1, position + 1))  # Advance.
        previous = languages(budget - 1, position)
        low = maximal(mask & (FULL ^ OBSERVATIONS[position]) for mask in previous)
        high = maximal(mask & OBSERVATIONS[position] for mask in previous)
        candidates.extend(left | right for left in low for right in high)  # Read.
    return maximal(candidates)


def flip_words(mask):
    return sum(1 << (127 - word) for word in range(128) if mask >> word & 1)


def trim_once(mask):
    return sum(1 << word for word in range(128) if mask >> word & 1 and
               (mask >> (word >> 1) & 1 or mask >> ((word >> 1) | 64) & 1) and
               (mask >> ((word << 1) & 127) & 1 or mask >> (((word << 1) & 127) | 1) & 1))


def trim(mask, count=128):
    for _ in range(count):
        revised = trim_once(mask)
        if revised == mask:
            return mask
        mask = revised
    return mask


def certificate(budget):
    raw = languages(budget, 0)
    recurrent = maximal(trim(mask) for mask in raw)
    joint = maximal(trim(high & flip_words(low)) for high in recurrent for low in recurrent)
    return dict(residual_budget=budget, language_count=len(raw), pruned_count=len(recurrent),
                joint_count=len(joint), languages_hex=[hex(x) for x in raw],
                pruned_hex=[hex(x) for x in recurrent], joint_hex=[hex(x) for x in joint],
                joint_words=[[format(word, "07b")[::-1] for word in range(128) if mask >> word & 1]
                             for mask in joint])


def closure():
    index = {p.stem: p for root in (CORE, CORE / "inquiry-root", HERE) for p in root.glob("*.lean")}
    order = []
    def visit(name):
        if name in order or name.split(".")[0] in ("Init", "Std", "Lean"):
            return
        for imported in re.findall(r"^import\s+(\S+)", index[name].read_text(), re.M):
            visit(imported)
        order.append(name)
    visit("PeriodLocalCertificate")
    if "PeriodStrategySemantics" in index:
        visit("PeriodStrategySemantics")
    return [(name, index[name]) for name in order]


def main():
    six, seven = certificate(5), certificate(6)
    assert (six["language_count"], six["pruned_count"], six["joint_hex"]) == (44, 4, ["0x0"])
    native = sum(1 << word for word in (18, 36, 73))
    assert (seven["language_count"], seven["pruned_count"], set(seven["joint_hex"])) == (201, 10, {hex(native), hex(flip_words(native))})
    report = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), window_bits=N,
                  six_commands=six, seven_commands=seven,
                  dp_counts={f"{d},{p}": len(languages(d, p)) for d in range(7) for p in range(7-d)},
                  checker_sha256=sha(Path(__file__).read_bytes()),
                  scope="Worst-case six/seven-command local-language kernel certificates, original-game bounded-policy semantics, and generic pruning preservation. The written first-read/window/mask reduction is not a completed composed Lean correspondence theorem. Favorable realized branches can stop earlier.")
    lean = shutil.which("lean")
    assert lean
    prefix = [lean, "+leanprover/lean4:v4.29.1"] if shutil.which("elan") else [lean]
    version = subprocess.run(prefix + ["--version"], capture_output=True, text=True, check=True).stdout.strip()
    assert "4.29.1" in version
    compiler_prefix = subprocess.run(prefix + ["--print-prefix"], capture_output=True, text=True, check=True).stdout.strip()
    compiler = Path(compiler_prefix) / "bin" / "lean"
    report.update(version=version, compiler=str(compiler), compiler_sha256=sha(compiler.read_bytes()))
    receipt = HERE / "period-general-runs" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    (receipt / "sources").mkdir(parents=True)
    report["receipt"] = str(receipt.relative_to(REPO))
    (receipt / Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    (receipt / "lean-toolchain").write_text("leanprover/lean4:v4.29.1\n")
    # Save portable exact masks even if a later compilation fails.
    (receipt / "local-languages.json").write_text(json.dumps(report, indent=2) + "\n")
    (HERE / "period-general-languages.json").write_text(json.dumps(report, indent=2) + "\n")
    harness = """import PeriodLocalCertificate
open Generative.InquirySufficiency.PeriodLocalCertificate
#eval languages 5 0
#eval sixRecurrent
#eval sixJoint
#eval languages 6 0
#eval recurrentLanguages
#eval jointLanguages
"""
    (receipt / "Correspondence.lean").write_text(harness)
    modules, audits, own_audits = [], {}, {}
    with tempfile.TemporaryDirectory(prefix="period-general-") as temporary:
        build = Path(temporary)
        env = {**os.environ, "LEAN_PATH": str(build)}
        for name, source in closure():
            raw = source.read_bytes()
            (build / (name + ".lean")).write_bytes(raw)
            (receipt / "sources" / (name + ".lean")).write_bytes(raw)
            if name in ("PeriodLocalCertificate", "PeriodWindowPruning", "PeriodStrategySemantics"):
                assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", raw.decode())
                assert not re.search(r"^\s*(axiom|constant)\s", raw.decode(), re.M)
            run = subprocess.run(prefix + ["-o", name + ".olean", name + ".lean"], cwd=build,
                                 env=env, capture_output=True, text=True, timeout=1200)
            output = run.stdout + run.stderr
            (receipt / (name + ".log")).write_text(output)
            modules.append(dict(module=name, source=str(source.relative_to(REPO)), source_sha256=sha(raw), exit_code=run.returncode))
            assert run.returncode == 0 and not re.search(r"\b(error|warning)\b", output), output[-4000:]
            parsed = {n: [a.strip() for a in ax.split(",") if a.strip()] for n, ax in AUDIT.findall(output)}
            audits.update(parsed)
            if name in ("PeriodLocalCertificate", "PeriodWindowPruning", "PeriodStrategySemantics"):
                own_audits.update(parsed)
                expected = re.findall(r"^#print axioms (\S+)", raw.decode(), re.M)
                assert sorted(parsed) == sorted(expected)
        assert all(not axioms for axioms in audits.values()), {n:a for n,a in audits.items() if a}
        (build / "Correspondence.lean").write_text(harness)
        run = subprocess.run(prefix + ["Correspondence.lean"], cwd=build, env=env,
                             capture_output=True, text=True, timeout=600)
        (receipt / "Correspondence.log").write_text(run.stdout + run.stderr)
        assert run.returncode == 0
        actual = [set(ast.literal_eval(block)) for block in re.findall(r"\[[^\]]*\]", run.stdout, re.S)]
        expected = [set(int(x, 16) for x in cert[key]) for cert in (six, seven)
                    for key in ("languages_hex", "pruned_hex", "joint_hex")]
        assert actual == expected
    assert all(sha((REPO / row["source"]).read_bytes()) == row["source_sha256"] for row in modules)
    report.update(status="passed", modules=modules, new_audits=len(own_audits), total_audits=len(audits), all_audits_empty=True,
                  exact_mask_sets_matched=6)
    (receipt / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    (HERE / "period-general-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("status", "receipt", "new_audits", "total_audits", "exact_mask_sets_matched")}, indent=2))


if __name__ == "__main__":
    main()
