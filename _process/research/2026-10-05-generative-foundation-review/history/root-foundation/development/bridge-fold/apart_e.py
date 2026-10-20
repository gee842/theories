#!/usr/bin/env python3
"""F3E (19 October 2026): register the apart roots of F3E's core modules. Idempotent.

usage (from the checkout root): python3 -B apart_e.py

Adds an entry (module, category, reason) to THEOREM-CONNECTIVITY-APART.json for each root below that has
none; entries already present are left as they are. Then run `THEOREM-CONNECTIVITY.py --check`.
"""
import json
import pathlib

APART = pathlib.Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/'
                     'THEOREM-CONNECTIVITY-APART.json')
GS, MW, SU = 'general-structure', 'model-witness', 'support'


def by(origin):
    return f' ({origin}, ported by F3E)'


PRES = 'a law of every presentation of any type of things by codes answering any type of questions'
JOIN = 'a law of every joining (a ternary relation) on any type of fragments'
ROOTS = {
    'BranchingTest.finer_rename': ('Becoming.Grains', GS, 'a law of every renaming of branching tests into blocks '
                                   'of single moves, on any type of moves and claims: read back at the finer grain '
                                   'the renamed test is the test itself, an equality of tests with no frame'
                                   + by('ExplanatoryGranularity')),
    'Carriers.identity_bool_bijection': ('Becoming.Carriers', SU, 'a statement using only the prelude: the '
                                         'identity on `Bool` is one to one and onto' + by('DynamicSymmetry')),
    'Carriers.negation_bool_bijection': ('Becoming.Carriers', SU, 'a statement using only the prelude: negation on '
                                         '`Bool` is one to one and onto' + by('DynamicSymmetry')),
    'Coverage.balance_does_not_determine_coverability': (
        'Becoming.Coverage', MW, 'a fact about two constructed boards: the separated pair balances like the empty '
        'board, which is covered, and has no cover' + by('ExplanatoryStructure')),
    'HistoryLanguages.same_future_extends': ('Becoming.HistoryLanguages', GS, 'a law of every language of words on '
                                             'any alphabet: histories with one continuation profile keep one profile '
                                             'after a common extension' + by('ContinuationConditions')),
    'Joining.Occurrence.ofTuple_at': ('Becoming.JoiningRoles', SU, 'a one-line unpacking of `Occurrence.ofTuple`: '
                                      'each role is filled by the fragment the tuple gives it'
                                      + by('ExplanatoryJoiningRefinement')),
    'Joining.chainComplete_iff_commonUnit_suffices': ('Becoming.LocalUnits', GS, JOIN + ': under associativity, '
                                                      'functionality and units, chain completion is that a common '
                                                      'unit suffices for joining' + by('ExplanatoryLocalUnits')),
    'Joining.leftUnit_transport': ('Becoming.LocalUnits', GS, JOIN + ': a one-to-one correspondence carrying a '
                                   'joining carries its left units' + by('ExplanatoryLocalUnits')),
    'Joining.rightUnit_transport': ('Becoming.LocalUnits', GS, JOIN + ': a one-to-one correspondence carrying a '
                                    'joining carries its right units' + by('ExplanatoryLocalUnits')),
    'Joining.units_agree': ('Becoming.LocalUnits', GS, JOIN + ': under associativity any two assignments of units '
                            'agree' + by('ExplanatoryLocalUnits')),
    'ListFootprints.realizes_iff_of_perm': ('Becoming.ListFootprints', GS, 'a law of every plan over lists of any '
                                            'type of resources: plans drawing on reorderings of one list are '
                                            'realized at the same lists' + by('ExplanatoryFootprints')),
    'ListFootprints.realizes_reassociate': ('Becoming.ListFootprints', GS, 'a law of every plan over lists of any '
                                            'type of resources: reassociating a plan keeps where it is realized'
                                            + by('ExplanatoryFootprints')),
    'Midway.exists_phase': ('Becoming.Grains', SU, 'a one-line unpacking of the witness\'s configuration type: '
                            'something exists among its six configurations exactly where one of them is it'
                            + by('ExplanatoryGranularityBoundary')),
    'Presentations.all_predicates_force_injective': ('Becoming.Presentations', GS, PRES + ': a presentation exact '
                                                     'for all predicates gives distinct things distinct codes'
                                                     + by('ExplanatoryUniqueness')),
    'Presentations.all_predicates_relation_recoverable': ('Becoming.Presentations', GS, PRES + ': under a '
                                                          'presentation exact for all predicates every relation '
                                                          'is read exactly through the codes'
                                                          + by('ExplanatoryUniversality')),
    'Presentations.all_predicates_unique_correspondence': ('Becoming.Presentations', GS, PRES + ': two '
                                                           'presentations exact for all predicates match their used '
                                                           'codes one to one' + by('ExplanatoryUniversality')),
    'Presentations.canonical_exact': ('Becoming.Presentations', SU, 'a one-line unpacking of `canonical`: the '
                                      'presentation of each thing by its answers reads every answer exactly'
                                      + by('ExplanatoryUniversality')),
    'Presentations.canonical_factor': ('Becoming.Presentations', GS, PRES + ', with extensionality of predicates a '
                                       'named hypothesis: every exact presentation factors through the canonical '
                                       'one' + by('ExplanatoryUniversality')),
    'Presentations.first_summary_cannot_answer_both': ('Becoming.Presentations', MW, 'a fact about one constructed '
                                                       'presentation of pairs of bits: with both bits asked, no '
                                                       'reading of the first bit is exact' + by('ExplanatoryUniqueness')),
    'Presentations.full_exact': ('Becoming.Presentations', MW, 'a fact about one constructed presentation of pairs '
                                 'of bits: the pair as code reads the first bit exactly' + by('ExplanatoryUniqueness')),
    'Presentations.full_not_reduced': ('Becoming.Presentations', MW, 'a fact about one constructed presentation of '
                                       'pairs of bits: the pair as code is not reduced for the first bit'
                                       + by('ExplanatoryUniqueness')),
    'Presentations.lift_exact_iff_saturated': ('Becoming.Presentations', GS, PRES + ': the image of a relation is '
                                               'its exact reading through an exact reduced presentation exactly '
                                               'where the relation is saturated' + by('ExplanatoryUniversality')),
    'Presentations.relation_descends_iff_saturated': ('Becoming.Presentations', GS, PRES + ': a relation descends '
                                                      'to an exact reduced presentation exactly where it is '
                                                      'saturated' + by('ExplanatoryUniversality')),
    'Presentations.relational_reading_unique_on_used': ('Becoming.Presentations', GS, PRES + ': exact readings of '
                                                        'one relation agree on used codes'
                                                        + by('ExplanatoryUniversality')),
    'Presentations.separating_relation_blocks_descent': ('Becoming.Presentations', GS, PRES + ': one pair of '
                                                         'triples answering alike on which the relation differs '
                                                         'blocks every exact reading' + by('ExplanatoryUniversality')),
    'Presentations.short_exact': ('Becoming.Presentations', MW, 'a fact about one constructed presentation of '
                                  'pairs of bits: the first bit as code reads it exactly' + by('ExplanatoryUniqueness')),
    'Presentations.short_reduced': ('Becoming.Presentations', MW, 'a fact about one constructed presentation of '
                                    'pairs of bits: the first bit as code is reduced' + by('ExplanatoryUniqueness')),
}

d = json.loads(APART.read_text())
for name, (module, category, reason) in ROOTS.items():
    d['roots'].setdefault('Becoming.' + name, {'module': module, 'category': category, 'reason': reason})
APART.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print(len(ROOTS), 'entries')
