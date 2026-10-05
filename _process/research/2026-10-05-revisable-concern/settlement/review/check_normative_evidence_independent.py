#!/usr/bin/env python3
"""Read-only independent reconstruction; prints results and rewrites no inputs."""

from collections import defaultdict
from itertools import product
from pathlib import Path
import hashlib
import json


def main():
    here = Path(__file__).resolve().parent
    repo = next(p for p in here.parents if (p / "AGENTS.md").exists()
                and (p / "RESEARCH.md").exists())
    settlement = here.parent
    n = 4
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    relations = []
    for bits in range(1 << len(pairs)):
        relation = {(i, i) for i in range(n)} | {
            pair for index, pair in enumerate(pairs) if bits >> index & 1
        }
        closure = set(relation)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (i, k) in closure and (k, j) in closure:
                        closure.add((i, j))
        if closure == relation:
            relations.append(relation)
    witnesses = 0
    for left, right in product(relations, repeat=2):
        common = left & right
        strict = {(a, b) for a, b in common if (b, a) not in common}
        remainder = {a for a in range(n)
                     if not any((b, a) in strict for b in range(n))}
        assert remainder
        for a, b in strict:
            assert a != b
            for c in range(n):
                if (b, c) in strict:
                    assert (a, c) in strict
        for b in set(range(n)) - remainder:
            assert any((a, b) in strict for a in remainder)
            witnesses += 1

    audit = json.loads((settlement / "evidence/existing-evidence-audit.json").read_text())
    assert all(hashlib.sha256((repo / path).read_bytes()).hexdigest() == digest
               for path, digest in audit["hashes"].items())
    source = repo / "sources/20-codex-theory-sessions-2026-10-05/sin/work/package-reproduction/live"
    assignments = json.loads((source / "assignments.json").read_text())
    seats = {(row["id"], row["replica"]): row["B"]
             for row in json.loads((source / "successor-assignments.json").read_text())}
    scores = defaultdict(lambda: [0, 0])
    for path in sorted((source / "lineages").glob("*/private.json")):
        case = json.loads(path.read_text())
        truth = case["truth"]
        labels = [row[0] if truth is None else row[0] ^ int(
            row[truth[0]] == truth[2] and row[truth[1]] == truth[3])
            for row in case["test"]]
        for replica in ("r0", "r1"):
            answers = json.loads((path.parent / (replica + "-response.json")).read_text())["answers"]
            assert len(answers) == len(labels)
            key = (case["stratum"], assignments[case["id"]], seats[(case["id"], replica)])
            scores[key][0] += sum(type(value) is int and value in (0, 1)
                                  and value == label for value, label in zip(answers, labels))
            scores[key][1] += len(labels)

    protocol = json.loads((settlement / "evidence/protocol.json").read_text())
    assert len(protocol["comparisons"]) == 6
    assert abs(protocol["analysis"]["alpha_each_two_sided"] * 6 - 0.05) < 1e-15
    assert abs(protocol["analysis"]["alpha_each_tail"] * 12 - 0.05) < 1e-15
    result = {
        "status": "passed",
        "four_action_preorders": len(relations),
        "ordered_two_model_profiles": len(relations) ** 2,
        "maximal_dominating_witnesses": witnesses,
        "source_hashes_matched": len(audit["hashes"]),
        "successor_answers_rescored": sum(value[1] for value in scores.values()),
        "rescored_cells": [{"stratum": key[0], "timely_feedback": key[1],
                            "access": key[2], "correct": value[0], "total": value[1]}
                           for key, value in sorted(scores.items())],
        "protocol_version": protocol["version"],
        "protocol_comparisons": len(protocol["comparisons"]),
        "family_alpha_arithmetic": "passed",
        "new_empirical_observations": 0,
        "scope": "Proof corroboration, saved-file integrity and rescoring, and protocol alpha arithmetic; no normative, empirical-prevalence, or interval-coverage validation."
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
