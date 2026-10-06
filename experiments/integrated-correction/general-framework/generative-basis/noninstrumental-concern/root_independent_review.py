#!/usr/bin/env python3
"""Independent finite scope checks and a separate frozen-source Lean build.

This checks a proposed logical decomposition, not the truth of an ethical
ground. It never rewrites the earlier 66-declaration verification receipt.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import permutations
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
BASIS = HERE.parent
TOOLCHAIN = "leanprover/lean4:v4.29.1"


def digest(data):
    return sha256(data).hexdigest()


def finite_checks():
    """Evaluate definitions directly over every 3 x 3 binary interpretation."""
    counts = dict(interpretations=0, universal=0, anchors=0,
                  locality=0, anchors_and_locality=0,
                  anchors_without_locality=0, locality_without_anchors=0)
    for opportunity in range(1 << 9):
        for reason in range(1 << 9):
            rows = [(opportunity >> (3 * e)) & 7 for e in range(3)]
            positive = [(reason >> (3 * e)) & 7 for e in range(3)]
            universal = all((r & h) == h for h, r in zip(rows, positive))
            anchors = all(not h or bool(h & r) for h, r in zip(rows, positive))
            locality = all(not (h & r) or (h & r) == h
                           for h, r in zip(rows, positive))
            assert universal == (anchors and locality)
            counts["interpretations"] += 1
            for key, value in (("universal", universal), ("anchors", anchors),
                               ("locality", locality),
                               ("anchors_and_locality", anchors and locality),
                               ("anchors_without_locality", anchors and not locality),
                               ("locality_without_anchors", locality and not anchors)):
                counts[key] += int(value)

    # History is transformed along with labels: neither primitive ownership
    # nor a special preferred name is present in this relation.
    history = {(0, 0), (1, 1)}
    covariance_checks = 0
    for permutation in permutations(range(2)):
        moved_history = {(permutation[a], permutation[e]) for a, e in history}
        for a in range(2):
            for e in range(2):
                assert ((a, e) in history) == (
                    (permutation[a], permutation[e]) in moved_history)
                covariance_checks += 1
    assert all(any((a, e) in history for a in range(2)) for e in range(2))
    assert (0, 0) in history and (1, 0) not in history

    # A patient event can have an independent eligible actor without having
    # any actor in its own continuity. Patient and actor domains differ here.
    inactive_patient_events = {"never-agent-patient"}
    eligible = {("independent-helper", "never-agent-patient")}
    linked_reason = set()
    no_self_seed = all(not any((a, e) in linked_reason for a, _ in eligible)
                       for e in inactive_patient_events)
    assert no_self_seed and eligible

    # Without an eligible actor, UniversalC2 is vacuously true; unconditional
    # event coverage is false. Coverage must be restricted by opportunity.
    empty_opportunity = set()
    vacuous_universal = all(pair in linked_reason for pair in empty_opportunity)
    unconditional_anchor = any(pair in linked_reason for pair in empty_opportunity)
    assert vacuous_universal and not unconditional_anchor
    return dict(**counts, bad_events=3, candidate_execution_positions=3,
                varied_predicates="all opportunity and reason matrices; Bad fixed true",
                history_covariance_comparisons=covariance_checks,
                history_anchor_without_executor_closure=True,
                never_agent_without_reason_seed=True,
                empty_opportunity_requires_qualified_coverage=True)


def execute(command, cwd, env):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    sources = [BASIS / "lean/GenerativeCore.lean",
               BASIS / "lean/conditional/ResourceContinuation.lean",
               HERE / "PatientConcern.lean", HERE / "GroundingContract.lean",
               HERE / "RootGrounding.lean"]
    frozen = {p: p.read_bytes() for p in sources}
    prior = (HERE / "verification.json").read_bytes()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    version = execute(["lean", "+" + TOOLCHAIN, "--version"], HERE, env)
    assert version.returncode == 0 and "version 4.29.1," in version.stdout
    logs = HERE / "root-independent-logs"
    logs.mkdir(exist_ok=True)
    modules = []
    allowed = {"propext", "Quot.sound", "Classical.choice"}
    with tempfile.TemporaryDirectory(prefix="concern-root-independent-") as name:
        build = Path(name)
        for path, data in frozen.items():
            assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", data.decode())
            assert not re.search(r"^\s*(axiom|constant)\s", data.decode(), re.M)
            (build / path.name).write_bytes(data)
        build_env = dict(env, LEAN_PATH=str(build))
        for path in sources:
            result = execute(["lean", "+" + TOOLCHAIN, "-o",
                              path.stem + ".olean", path.name], build, build_env)
            log = logs / (path.stem + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout)
            expected = len(re.findall(r"^#print axioms ", frozen[path].decode(), re.M))
            axiom_set = {x.strip() for _, xs in audits for x in xs.split(",") if x.strip()}
            clean = (result.returncode == 0 and "warning:" not in result.stdout
                     and "sorryAx" not in result.stdout and len(audits) == expected
                     and expected > 0 and axiom_set <= allowed)
            modules.append(dict(module=path.stem,
                                source=str(path.relative_to(BASIS)),
                                source_sha256=digest(frozen[path]),
                                dependency_audits=len(audits),
                                axioms=sorted(axiom_set), clean=clean,
                                log=str(log.relative_to(HERE)),
                                log_sha256=digest(log.read_bytes())))
            if not clean:
                print(result.stdout)
                raise RuntimeError("Independent Lean build failed: " + path.name)
    counts = finite_checks()
    unchanged = all(p.read_bytes() == data for p, data in frozen.items())
    old_receipt_unchanged = (HERE / "verification.json").read_bytes() == prior
    assert unchanged and old_receipt_unchanged
    record = dict(status="passed", checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  independent_frozen_temporary_build=True,
                  toolchain=TOOLCHAIN, lean_version=version.stdout.strip(),
                  sources_unchanged=unchanged,
                  prior_66_receipt_unchanged=old_receipt_unchanged,
                  prior_66_receipt_sha256=digest(prior),
                  checker_sha256=digest(Path(__file__).read_bytes()),
                  modules=modules, finite_checks=counts,
                  scope="Independent proof-source compilation and finite checking of reason coverage versus executor closure. No proof of experiential realization, moral ground, universality of C2, or an assumption-free foundation.")
    (HERE / "root-independent-review.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(dict(status=record["status"], finite_checks=counts,
                         new_audits=modules[-1]["dependency_audits"]), indent=2))


if __name__ == "__main__":
    main()
