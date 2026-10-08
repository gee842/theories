#!/usr/bin/env python3
"""Finite extensional controls for CorrectionRelations; not an AI experiment.
The cycle oracle enumerates joint assignments rather than using parity.
The Lean induction, not these finite cases, justifies arbitrary finite size.
"""
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent
BITS = (False, True)
PAIRS = tuple(product(BITS, repeat=2))
RELATIONS = tuple(frozenset(pair for i, pair in enumerate(PAIRS) if mask & (1 << i))
                  for mask in range(16))
CONTEXTS = tuple(frozenset(b for i, b in enumerate(BITS) if mask & (1 << i))
                 for mask in range(4))

def boundary(r):
    return {b for _, b in r}

def fits(r, context):
    return any(b in context for _, b in r)

def compose(r, s):
    return frozenset((a, c) for a, c in PAIRS
                     if any((a, b) in r and (b, c) in s for b in BITS))

def propagate(signs, root):
    value = root
    for sign in signs:
        value = value != sign
    return value

def cycle_assignments(signs, root):
    if not signs:
        return [()]
    matches = []
    for rest in product(BITS, repeat=len(signs) - 1):
        nodes = (root,) + rest
        if all(nodes[(i + 1) % len(nodes)] == (nodes[i] != sign)
               for i, sign in enumerate(signs)):
            matches.append(nodes)
    return matches

context_pairs = 0
for r, s in product(RELATIONS, repeat=2):
    refinement = all(not fits(r, c) or fits(s, c) for c in CONTEXTS)
    equivalent = all(fits(r, c) == fits(s, c) for c in CONTEXTS)
    assert refinement == (boundary(r) <= boundary(s))
    assert equivalent == (boundary(r) == boundary(s))
    context_pairs += 1

composition_triples = 0
for r, s, t in product(RELATIONS, repeat=3):
    direct = frozenset((a, d) for a, d in PAIRS
                      if any((a, b) in r and (b, c) in s and (c, d) in t
                             for b, c in PAIRS))
    assert compose(compose(r, s), t) == direct == compose(r, compose(s, t))
    composition_triples += 1

cycle_records = []
assignment_checks = 0
for n in range(8):
    for signs in product(BITS, repeat=n):
        probe = propagate(signs, False)
        for root in BITS:
            assignments = cycle_assignments(signs, root)
            assignment_checks += 1 if n == 0 else 2 ** (n - 1)
            assert bool(assignments) == (not probe)
            assert len(assignments) == int(not probe)
            corrected = cycle_assignments(signs + (probe,), root)
            assert len(corrected) == 1
            cycle_records.append({'signs': list(signs), 'root': root,
                                  'solutions': len(assignments), 'probe': probe,
                                  'corrected_solutions': len(corrected)})
assert not cycle_assignments((True, propagate((False,), False)), False)

revision_records = []
for n in range(2, 8):
    for old in product(BITS, repeat=n):
        old_probe = propagate(old, False)
        for index in range(n - 1):
            half = old[:index] + (not old[index],) + old[index + 1:]
            current = half[:index + 1] + (not half[index + 1],) + half[index + 2:]
            assert propagate(current, False) == old_probe
            assert propagate(half, False) != old_probe
            for root in BITS:
                assert len(cycle_assignments(current + (old_probe,), root)) == 1
                assert not cycle_assignments(half + (old_probe,), root)
            revision_records.append({'old': list(old), 'index': index,
                                     'current': list(current), 'probe': old_probe})

realization = []
for switched, requested in product(BITS, repeat=2):
    def works(mode, command):
        output = (command != mode) if switched else command
        return output == requested
    assert all(any(works(mode, c) for c in BITS) for mode in BITS)
    uniform = [c for c in BITS if all(works(mode, c) for mode in BITS)]
    observed = [policy for policy in product(BITS, repeat=2)
                if all(works(mode, policy[int(mode)]) for mode in BITS)]
    assert len(uniform) == (0 if switched else 1)
    assert len(observed) == 1
    realization.append({'switched': switched, 'requested': requested,
                        'uniform_solutions': uniform, 'observed_solutions': observed})

def sha(data):
    return hashlib.sha256(data).hexdigest()

record = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'status': 'passed',
          'source_sha256': {'CorrectionRelations.lean': sha((HERE / 'CorrectionRelations.lean').read_bytes())},
          'runner_sha256': sha(Path(__file__).read_bytes()),
          'context_relation_pairs': context_pairs,
          'context_predicates_per_pair': len(CONTEXTS),
          'composition_relation_triples': composition_triples,
          'cycle_length_range': [0, 7], 'cycle_root_records': len(cycle_records),
          'original_joint_assignments_checked': assignment_checks,
          'cycle_records': cycle_records, 'realization_records': realization,
          'paired_revision_cases': len(revision_records), 'revision_records': revision_records,
          'scope': 'Extensional Boolean checks and brute-force witnesses; not empirical AI, '
                   'not proof of arbitrary finite size, not physical implementability.'}
(HERE / 'correction-relations-model-checks.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({k: v for k, v in record.items() if k not in {'cycle_records', 'realization_records', 'revision_records'}}))
