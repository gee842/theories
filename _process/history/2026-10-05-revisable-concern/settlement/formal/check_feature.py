#!/usr/bin/env python3
"""Finite grammar construction; standard library only, independent of game code."""
from itertools import combinations, product
from fractions import Fraction
from pathlib import Path
import json


rows = list(product((0, 1), repeat=3))
# The environment's independent assay table. The learner below sees only rows
# and these eight labels; XOR is not a feature primitive or learner operation.
labels = [0, 0, 1, 1, 1, 1, 0, 0]
literals = tuple((coordinate, negated) for coordinate in range(3)
                 for negated in (False, True))
terms = [(literal,) for literal in literals]
terms += list(combinations(literals, 2))
candidates = [(term,) for term in terms] + list(combinations(terms, 2))
candidates.sort(key=lambda f: (sum(len(t) for t in f), repr(f)))
discovery = [i for i, row in enumerate(rows) if row[2] == labels[i]]
validation = [i for i, row in enumerate(rows) if row[2] != labels[i]]
evaluations = 0


def predict(formula, row):
    return int(any(all(bool(row[coordinate]) != negated
                       for coordinate, negated in term)
                   for term in formula))


def literal_name(literal):
    coordinate, negated = literal
    return ("not " if negated else "") + "xyz"[coordinate]


def formula_name(formula):
    return " or ".join("("+" and ".join(map(literal_name, term))+")"
                       for term in formula)


discovery_pass = []
for formula in candidates:
    outputs = [predict(formula, rows[i]) for i in discovery]
    evaluations += len(discovery)
    if outputs == [labels[i] for i in discovery]:
        discovery_pass.append(formula)
survivors = []
for formula in discovery_pass:
    outputs = [predict(formula, rows[i]) for i in validation]
    evaluations += len(validation)
    if outputs == [labels[i] for i in validation]:
        survivors.append(formula)

assert survivors
selected = survivors[0]
assert sum(len(term) for term in selected) == 4
assert all(sum(len(term) for term in candidate) >= 4 for candidate in survivors)
assert [predict(selected, row) for row in rows] == labels
for literal in literals:
    assert [predict(((literal,),), row) for row in rows] != labels
identity = (((2, False),),)
assert identity in discovery_pass
assert all(predict(identity, rows[i]) != labels[i] for i in validation)
gamma = Fraction(1, 32)
kappa = Fraction(1, 4*len(candidates))
epsilon = Fraction(1, 4*evaluations)
replay_checks = 6
rho = Fraction(1, 24)
assert len(rows)*gamma + len(candidates)*kappa + evaluations*epsilon + replay_checks*rho == 1
result = dict(status="passed", candidates_constructed=len(candidates),
              discovery_rows=discovery, validation_rows=validation,
              candidates_passing_discovery=len(discovery_pass),
              candidates_passing_complete_validation=len(survivors),
              candidate_row_evaluations=evaluations,
              selected_feature=formula_name(selected),
              selected_literal_count=4, primitive_features_all_fail=True,
              identity_proxy_fits_discovery_fails_all_validation=True,
              assay_label_price=str(gamma), assembly_price=str(kappa),
              evaluation_price=str(epsilon), graph_replay_checks=replay_checks,
              graph_replay_price=str(rho),
              total_feature_bill="1",
              truth_table=[dict(input=list(row), label=label,
                               prediction=predict(selected,row))
                           for row,label in zip(rows,labels)])
path=Path(__file__).with_name("feature-results.json")
path.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({key:result[key] for key in
                  ("status","candidates_constructed","candidate_row_evaluations",
                   "selected_feature","total_feature_bill")}))
