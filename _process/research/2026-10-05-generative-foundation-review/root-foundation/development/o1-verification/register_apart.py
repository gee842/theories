#!/usr/bin/env python3
"""Register O1's apart roots in THEOREM-CONNECTIVITY-APART.json (each with module, category and reason), keeping the
file's order and format. usage: python3 -B register_apart.py  (run from the checkout root)"""
import json
from pathlib import Path
P = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json')
M = 'Becoming.Verification'
NEW = {
    'Becoming.Ideals.Open.interior_iff': ('support', 'An open class is its own interior: `VerifiableBy.interior_iff` with `Open.verifiable`, a one-line unpacking; at runs, a verifiable reading holds exactly its verified runs (`verifiable_iff_verified`).'),
    'Becoming.Ideals.hull_not_interior_compl': ('restates', 'The hull meets no ideal of the interior of the complement, `AdheresBy.not_interior_compl` read on classes; its case of runs is `Adheres.not_verified_compl`, stated on the base.'),
    'Becoming.Ideals.interior_iff_meets': ('support', 'The interior is the class meeting the stretches only ideals of the class hold: the two definitions unpacked (`Iff.rfl`); at runs it is `Stretches.verifyingClass_iff`.'),
    'Becoming.Ideals.interior_largest': ('support', 'The interior holds every open subclass: `interiorBy_largest` with `Open.verifiable`, a one-line corollary; at runs it is `verified_largest`.'),
    'Becoming.Ideals.interior_open': ('support', 'The interior is open: `interiorBy_verifiable` with `verifiable_open`, a one-line corollary; at runs, being verified is verifiable (`verified_verifiable`).'),
    'Becoming.Ideals.interior_sub': ('support', 'The interior lies within the class: `InteriorBy.holds` read on classes, a one-line unpacking; at runs it is `Verified.holds`.'),
    'Becoming.Ideals.verifiable_compl_refutable_iff': ('calibration', 'Asked of every order and class, the step from a verifiable class to a refutable complement is exactly double-negation elimination (two-element chain): a history only known not to lie outside a verifiable class does not thereby show the stretch that verifies it. On runs the same step gives Markov\'s principle (`verifiable_compl_refutable_markov`).'),
}
d = json.loads(P.read_text())
for k, (cat, reason) in NEW.items():
    assert k not in d['roots'], k
    assert cat in d['categories'], cat
    d['roots'][k] = {'module': M, 'category': cat, 'reason': reason}
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('registered', len(NEW))
