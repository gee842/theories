#!/usr/bin/env python3
"""A4-L: register the apart roots of `Becoming.Ideals` and `Becoming.HistoryIdeals` in THEOREM-CONNECTIVITY-APART.json.

Every other theorem of the two modules reaches the base: the laws of ideals are read on the histories of a process in
`Becoming.Stretches` (HistoryIdeals). What stays apart is support (equivalence laws, the empty class, unpacked
definitions, two laws of directed suprema) and four laws whose case on the base is stated elsewhere: the hull's
idempotence, whose case of runs is Horizon's `Adheres.adheres`, and the classification of the ideals of words, whose
process form is `Stretches.classification`. Each entry must be new; entries are appended, as the register keeps them. usage (from the repository root):
python3 -B register_apart.py"""
import json
from pathlib import Path

REGISTER = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json')
I, H = 'Becoming.Ideals', 'Becoming.HistoryIdeals'
ENTRIES = {
    'Becoming.Ideals.Closed.hull_iff': (I, 'support',
        'A closed class is its own hull: `hull_least` with `hull_contains`, a one-line unpacking; at runs, a reading '
        'holding every run adhering to it holds exactly those runs, and adhering itself is the least closed class '
        '(`Stretches.adheres_iff_closed`).'),
    'Becoming.Ideals.Ideal.Same.trans': (I, 'support',
        'Transitivity of holding the same stretches, a one-line lemma of the module\'s own definitions.'),
    'Becoming.Ideals.Preorder.Equiv.refl': (I, 'support',
        'Reflexivity of an order\'s equivalence (each element below itself both ways), a one-line lemma of the '
        'module\'s own definitions.'),
    'Becoming.Ideals.avoids_principal_iff': (I, 'support',
        'A finite history avoids `F` exactly where no element of `F` lies below its stretch: the definition of '
        '`Avoids` unpacked (`Iff.rfl`).'),
    'Becoming.Ideals.content_false': (I, 'support',
        'The empty class has no content: a one-line unpacking of `Content`.'),
    'Becoming.Ideals.false_closed': (I, 'support',
        'The empty class is closed: a one-line unpacking of `Closed` (a directed set of ideals is nonempty).'),
    'Becoming.Ideals.false_refutable': (I, 'support',
        'The empty class is refuted at any stretch of any ideal: a one-line unpacking of `Refutable`.'),
    'Becoming.Ideals.within_false': (I, 'support',
        'No ideal lies within the empty set of stretches, since an ideal has a stretch: a one-line unpacking.'),
    'Becoming.Ideals.restrict_false_none': (I, 'support',
        'The empty set\'s order has no ideal: a one-line unpacking of `Ideal.nonempty`.'),
    'Becoming.Ideals.hull_hull': (I, 'restates',
        'The hull\'s idempotence, `AdheresBy.adheres` read on the hull; its case of runs is Horizon\'s '
        '`Adheres.adheres` (a run adhering to the runs that adhere to a reading adheres to it), already on the base.'),
    'Becoming.Ideals.hull_iff_within_content': (I, 'support',
        'The hull is the class within the content: the two definitions unpacked (`Iff.rfl`); at runs it is '
        '`adheres_iff_adheresBy`.'),
    'Becoming.Ideals.idealOrder_equiv_iff': (I, 'support',
        'Equivalence in the order of ideals is holding the same stretches: a one-line unpacking of `idealOrder`.'),
    'Becoming.Ideals.lower_unique_of_two': (I, 'support',
        'Two lower sets giving one class are the same set: `lower_unique` applied twice, a one-line corollary.'),
    'Becoming.Ideals.sup_congr': (I, 'support',
        'Directed suprema of two sets holding the same elements are equivalent: the fields of `DirectedComplete` '
        'unpacked; the histories of a process are such an order (`idealComplete`).'),
    'Becoming.Ideals.sup_mono': (I, 'support',
        'A directed supremum lies below that of a larger directed set: the fields of `DirectedComplete` unpacked.'),
    'Becoming.HistoryIdeals.classification': (H, 'restates',
        'The case of words of `Stretches.classification`, which states for the histories of every process that one '
        'settling, or going on with a stretch beyond each horizon picked, is a finite history or the history of a run; '
        'on the process of all sequences its stretches and the words are one order read two ways '
        '(`HistoryIdeals.sequence_stretch_iff`, `Stretches.sequences_le_iff`).'),
    'Becoming.HistoryIdeals.principal_settles': (H, 'restates',
        'The case of words of `Stretches.principal_settles` (a finite history settles), stated on the base for every '
        'process.'),
    'Becoming.HistoryIdeals.trace_goesOn': (H, 'restates',
        'The case of words of `Stretches.run_goesOn` (a run\'s history goes on), stated on the base for every '
        'process.'),
}

data = json.loads(REGISTER.read_text(encoding='utf-8'))
for name, (module, category, reason) in ENTRIES.items():
    assert name not in data['roots'], ('already registered', name)
    assert category in data['categories'], category
    data['roots'][name] = {'module': module, 'category': category, 'reason': reason}
REGISTER.write_text(json.dumps(data, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('registered', len(ENTRIES), 'apart roots')
