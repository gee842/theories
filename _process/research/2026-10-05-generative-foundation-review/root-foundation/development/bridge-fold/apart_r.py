#!/usr/bin/env python3
"""F3R (19 October 2026): register the apart roots of F3R's core modules. Idempotent.

usage (from the checkout root): python3 -B apart_r.py

Adds an entry (module, category, reason) to THEOREM-CONNECTIVITY-APART.json for each root below
that has none; entries already present are left as they are. Then run
`THEOREM-CONNECTIVITY.py --check`.
"""
import json
import pathlib

APART = pathlib.Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/'
                     'THEOREM-CONNECTIVITY-APART.json')
B = 'Becoming.'
ROUTES = ('a fact about the four routes and the cutoff or finishing-first order on them, one constructed model '
          'of the weak rules (GenerativeLossComparison, ported by F3R)')
ROOTS = {
    'ActiveReading.absent_included': ('support', 'a one-line unpacking: `Ranking.absent_sustains` with '
                                      '`absent_not_consuming`, the course without the focal formation read by the '
                                      'whole-run reading (RenewalComparison.absent_grounds, ported by F3R)'),
    'Dephasing.no_uniform_dephase_inverse': ('model-witness', 'a fact about the constructed dephasing map on 2x2 '
                                             'integer matrices (OperativeCoherence, ported by F3R); its law is '
                                             '`Readout.no_restore`, through which it is proved'),
    'Dephasing.retained_response_exact': ('model-witness', 'a fact about the constructed control-target model: the '
                                          'retained branch decodes the response exactly (OperativeCoherence, ported '
                                          'by F3R)'),
    'Integers.add_right_cancel': ('support', 'an arithmetic lemma on `Int` using only the prelude, constructive '
                                  '(Becoming.Integers, F3R)'),
    'MatchedCourses.b2_correspondence_involutive': ('model-witness', 'a fact about one constructed course model: '
                                                    'the b2 loss correspondence is its own inverse (RepairComparison, '
                                                    'ported by F3R)'),
    'MatchedCourses.separated_same_position': ('model-witness', 'a fact about one constructed course model: two '
                                               'claims of one position are separated in time (RepairComparison, '
                                               'ported by F3R)'),
    'MatchedCourses.support_between': ('model-witness', 'a fact about one constructed course model: support is '
                                       'available between the claims of a position (RepairComparison, ported by F3R)'),
    'MatchedCourses.support_restored': ('model-witness', 'a fact about one constructed course model: support is '
                                        'back at the final state of every course (RepairComparison, ported by F3R)'),
    'ProjectedLaws.cross_routing_two_steps': ('model-witness', 'a computation in the constructed two-cell wiring '
                                              'model (SystemsOrganization, ported by F3R)'),
    'ProjectedLaws.no_autonomous_left_law': ('model-witness', 'a counterexample in the constructed two-cell wiring '
                                             'model: crossed routing leaves one cell no law of its own; its law is '
                                             '`Mechanism.carries_law_iff` (SystemsOrganization, ported by F3R)'),
    'ProjectedLaws.self_routing_fixed': ('model-witness', 'a computation in the constructed two-cell wiring model '
                                         '(SystemsOrganization, ported by F3R)'),
    'StrictTransport.anchor_licenses_no_longer_repair': ('model-witness', ROUTES),
    'StrictTransport.continuation_first_above_every': ('model-witness', ROUTES),
    'StrictTransport.continuation_first_no_cutoff': ('model-witness', ROUTES),
    'StrictTransport.continuation_first_prefers_shorter': ('model-witness', ROUTES),
    'StrictTransport.continuation_first_transitive': ('model-witness', ROUTES),
    'StrictTransport.cutoff_transitive': ('model-witness', ROUTES),
    'StrictTransport.cutoffs_disagree': ('model-witness', ROUTES),
    'StrictTransport.shorter_interruption_no_worse': ('model-witness', ROUTES),
    'StrictTransport.strict_iff_of_faithful': ('general-structure', 'a law of every supplied comparison on any type '
                                               'and every faithful redescription of it; the base supplies no reading '
                                               'of the comparison (GenerativeLossComparison, ported by F3R)'),
    'SupportRecovery.same_later_inputs': ('model-witness', 'a fact about the two constructed pulse histories: they '
                                          'draw and contribute the same after the first step (RenewalRecovery, '
                                          'ported by F3R)'),
}


def main():
    d = json.loads(APART.read_text())
    added = 0
    for name, (category, reason) in ROOTS.items():
        full = B + name
        if full in d['roots']:
            continue
        assert category in d['categories'], category
        d['roots'][full] = {'module': B + name.split('.')[0], 'category': category, 'reason': reason}
        added += 1
    APART.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
    print(added, 'entries added')


if __name__ == '__main__':
    main()
