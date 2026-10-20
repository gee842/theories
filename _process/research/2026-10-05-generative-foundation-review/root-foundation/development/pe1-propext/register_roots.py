#!/usr/bin/env python3
"""Register PE1's apart roots in THEOREM-CONNECTIVITY-APART.json (Becoming.PropositionIdentity is about the proof
language, not about a process or a world, so every root stands apart by design). usage: python3 -B register_roots.py
(from the checkout root; refuses an entry that exists)"""
import json
from pathlib import Path

P = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json')
M = 'Becoming.PropositionIdentity'
N = M + '.'
LEAF = 'PE1: about the proof language (what identifying interderivable propositions keeps and loses), not a law of the unfolding; '
ROOTS = {
    N + 'extensional_iff_lumped': ('logical-strength', LEAF + 'propositional extensionality, a logical principle like those '
                                   'the category names, stated exactly as the lumping of every reading of propositions by interderivability'),
    N + 'lumped_of_byName': ('logical-strength', LEAF + 'where the reading by name is lumped by interderivability, '
                             'propositional extensionality holds and every reading is lumped'),
    N + 'Formula.read_congr': ('general-structure', LEAF + 'every reading through a formula built from relations, on any '
                               'type of atoms and quantifiers, respects interderivability'),
    N + 'iff_witness_unique': ('support', LEAF + 'proof irrelevance of Prop: any two witnesses of an iff are equal by rfl'),
    N + 'derivation_unique': ('support', LEAF + 'proof irrelevance of Prop: any two derivations of b from a are equal by rfl'),
    N + 'two_equivalences': ('model-witness', LEAF + 'two different self-inverse maps on Bool, showing that an equivalence of '
                             'types carries content where a witness of iff does not'),
    N + 'transport_const': ('support', LEAF + 'transport along an equation of propositions with a constant motive keeps the value'),
    N + 'transport_refl': ('support', LEAF + 'transport along rfl is the identity by computation'),
}
d = json.loads(P.read_text())
for k, (cat, reason) in ROOTS.items():
    assert k not in d['roots'], k
    assert cat in d['categories'], cat
    d['roots'][k] = {'module': M, 'category': cat, 'reason': reason}
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('registered', len(ROOTS))
