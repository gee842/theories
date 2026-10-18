#!/usr/bin/env python3
"""F3Q, the inquiry and composition family (18 October 2026): per-theorem verdicts.

usage (from the checkout root): python3 -B port_q.py        writes port-q.md beside this file

The data below is the one place the verdicts live; `rebind_q.py` reads it to rebind the records.
Each row: periphery theorem, the step-0 audit's grade (or F3Q's own grade where the audit did not
cover the module), the grade against the core after the port, the core counterpart, how it holds.
The joins whose periphery import is in the family are listed the same way, per theorem.
"""
import pathlib

HERE = pathlib.Path(__file__).parent

# module -> dict(path, audited, kind ('periphery' or 'join'), rows, note)
# row: (theorem, before, after, counterpart, how)
FAMILY = {}
JOINS = {}


def mod(name, path, audited, rows, note='', join=False):
    (JOINS if join else FAMILY)[name] = dict(path=path, audited=audited, rows=rows, note=note)


def ported(module, pairs, before='none', how='stated on the core, constructive'):
    """Rows for theorems stated in a new core module, by (old, new) name pairs."""
    out = []
    for pair in pairs:
        old, new = pair[0], pair[1]
        grade = pair[2] if len(pair) > 2 else 'same'
        note = pair[3] if len(pair) > 3 else how
        out.append((old, before if isinstance(before, str) else before.get(old, 'none'), grade,
                    f'Becoming.{module}.{new}', note))
    return out


SECTION = 'same (section named)'
SECTION_HOW = ('the periphery decoder used `Classical.choose`; the core takes a section of the map over the '
               'domain (`SectionWithin`) as a hypothesis, which is the datum a decoder needs, so no choice is used')

# --- sub-chain 1: general laws ------------------------------------------------------------------
mod('KnowledgeCorrespondence', 'inquiry-root/KnowledgeCorrespondence.lean', False, ported('PartialReadout', [
    ('exact_is_sound', 'ExactWithin.sound'),
    ('exact_requires_resolution', 'ExactWithin.lumped'),
    ('resolution_admits_decoder', 'ExactWithin.ofSection', SECTION, SECTION_HOW),
    ('exact_possible_iff_resolves', 'exact_exists_iff', SECTION, SECTION_HOW),
    ('conflicting_fibre_forces_abstention', 'SoundWithin.silent'),
    ('sound_restricts_domain', 'SoundWithin.mono'),
    ('refinement_preserves_resolution', 'LumpedWithin.finer'),
    ('preserved_record_preserves_exactness', 'ExactWithin.retained'),
    ('calibrated_pair_exact', 'paired_exact'),
    ('raw_signal_not_resolving', 'signal_not_lumped'),
    ('no_exact_raw_decoder', 'signal_no_exact'),
    ('every_sound_raw_decoder_abstains', 'signal_sound_silent'),
    ('direct_exact_on_normal', 'direct_exact_unreversed'),
    ('direct_fails_on_expanded_domain', 'direct_not_sound'),
    ('lucky_actual_correct', 'direct_right_once'),
    ('parity_record_exact', 'parity_exact'),
    ('double_reversal_exact', 'negated_exact'),
    ('true_content_trivially_safe', 'safe_of_holds'),
    ('abstention_sound', 'silent_sound'),
    ('abstention_not_exact', 'silent_not_exact'),
]), note=('`Becoming.Readout` states the whole-domain, never-silent case (`Readout.Decodes`, '
          '`Learning.Lumped`); `PartialReadout.exactWithin_univ_iff` and `lumpedWithin_univ_iff` join the two. '
          'The general laws take any feature type where the periphery took `Bool`. Names: evidence is the map, the '
          'target the feature, resolution lumping within the domain, abstention silence (naming study §7).'))

mod('GenerativeClosure', 'inquiry-root/GenerativeClosure.lean', False, ported('Derivation', [
    ('derivation_sound', 'Derives.sound'),
    ('all_closed_descendants_necessary', 'closed_throughout'),
    ('all_relative_descendants_necessary', 'relative_throughout'),
    ('entire_closure_necessary_iff_basis', 'closure_throughout_iff'),
    ('local_justification_discharges_context', 'discharged_throughout'),
    ('no_counterexample_to_closed_descendant', 'no_countermodel'),
    ('countermodel_excludes_derivation', 'countermodel_excludes'),
    ('derived_lemma_extension_preserves_necessity', 'lemma_throughout'),
    ('extra_claim_derives_with_one_local_premise', 'claim_under_itself'),
    ('extra_claim_not_necessary', 'claim_not_throughout'),
    ('extra_claim_not_closed_derivable', 'claim_not_closed'),
    ('one_local_premise_becomes_an_implication', 'claim_implies_itself'),
]), note=('The core had no derivation calculus. `Becoming.Derivation.Derives` is the same calculus on the core’s '
          'claims (`S → Prop`); `Necessary inquiry p` is `Throughout D p`, `addDerived` is `withLemma`.'))

mod('JointInterpretation', 'inquiry-root/JointInterpretation.lean', True, ported('Derivation', [
    ('package_derivable', 'conjunction_derives'),
    ('package_iff_list', 'conjunction_iff'),
    ('package_iff_basis', 'conjunction_iff_basis'),
    ('basis_iff_relative_closure', 'basis_iff_relative'),
    ('common_basis_iff_common_closure', 'common_basis_iff_common_closure'),
    ('pointwise_closure_iff_common', 'pointwise_iff_common'),
    ('pointwise_closure_gives_common_relative', 'pointwise_common_relative'),
    ('separate_basis_rows_fit', 'rows_each_met'),
    ('separate_rows_have_no_common_interpretation', 'rows_not_together'),
    ('separate_rows_do_not_cover_full_closure', 'rows_not_pointwise'),
]), note='`package` is `conjunction`, `incompatibleRows` is `rows`.')

# --- sub-chain 1: joins -------------------------------------------------------------------------
J = 'becoming/Becoming/'
mod('Becoming.DerivationScopeProcesses', J + 'DerivationScopeProcesses.lean', False, ported('Derivation', [
    ('relative_on_scope', 'Scope.relative'),
    ('discharged_on_scope', 'Scope.discharged'),
    ('lemma_extension_on_scope', 'Scope.lemma_closed'),
    ('countermodel_on_scope', 'Scope.countermodel'),
], before='step'), join=True)
mod('Becoming.Bridge', J + 'Bridge.lean', False, ported('Derivation', [
    ('derivation_sound_on_scope', 'Scope.closed'),
    ('closure_over_scope_iff_basis', 'Scope.closure_iff'),
    ('sound_goal_closure', 'Scope.goal_closure'),
    ('common_on_scope_iff', 'Scope.common_iff'),
], before='step'), join=True, note='Only the section "Derivation over the scope of an inquiry" reads this family.')
mod('Becoming.ReachableFrames', J + 'ReachableFrames.lean', False, ported('Derivation', [
    ('common_relative_on_scope', 'Scope.common_relative'),
], before='step'), join=True,
    note=('Only `common_relative_on_scope` reads this family (`JointInterpretation`); `carries_compose`, '
          '`complement_closed_no_extension` and `required_through_summary` read family J’s modules.'))
mod('Becoming.ExactRecordRuns', J + 'ExactRecordRuns.lean', False, ported('PartialReadout', [
    ('exact_sound', 'Runs.exact_sound'),
    ('exact_resolves', 'Runs.exact_lumped'),
    ('sound_abstains', 'Runs.sound_silent'),
    ('sound_within', 'Runs.sound_mono'),
    ('finer_resolves', 'Runs.finer_lumped'),
    ('kept_exact', 'Runs.retained_exact'),
    ('abstaining_sound', 'Runs.silent_sound'),
    ('abstaining_not_exact', 'Runs.silent_not_exact'),
    ('exact_iff_restsFrom', 'Runs.exact_iff_restsFrom'),
], before='step'), join=True, note='`recordBefore` is `Runs.prefixBefore`, `valueAt` is `Runs.featureAt`.')
mod('Becoming.ExactRecordRunsInherited', J + 'ExactRecordRunsInherited.lean', False, ported('PartialReadout', [
    ('exact_possible_iff', 'Runs.exact_exists_iff', SECTION, SECTION_HOW),
], before='step'), join=True)

NEW = [
    ('Becoming.PartialReadout', 'Becoming.Readout, Becoming.LearnableRuns', 1,
     'sound and exact partial readings of a feature through a map on a domain; silence; the channel model; '
     'readings of the prefix along runs'),
    ('Becoming.Derivation', 'Becoming.Inquiry', 1,
     'premise-tracked derivation from a basis: soundness, closure throughout a domain, one configuration for a '
     'finitely based closure, readings on the scope of an inquiry'),
]


def counts(rows):
    s = sum(r[2].startswith('same') for r in rows)
    t = sum(r[2] == 'step' for r in rows)
    return s, t, len(rows) - s - t


def render():
    out = ['# F3Q: per-theorem verdicts of the inquiry and composition family', '',
           '18 October 2026. Board row F3Q of [the port program](PORT-PROGRAM.md); format of the step-0 '
           '[restatement audit](RESTATEMENT-AUDIT.md#2-grades-and-verdicts). Generated by `port_q.py` from its data; '
           'edit the data, not this file.', '',
           '"Before" is the step-0 audit\'s grade where it covered the module, and F3Q\'s own grade against the core '
           'otherwise; "after" is the grade against the core with the new core modules. *Same (section named)* is '
           'the analogue of the audit\'s *same (excluded middle named)*: the periphery proof chose a representative '
           'classically, and the core theorem takes the section as a hypothesis. A module is **ported** when every '
           'theorem is same or step after. Every new core module compiles from the prelude with an empty axiom '
           'report.', '',
           '## New core modules', '', '| Module | Builds on | Sub-chain | Content |', '|---|---|--:|---|']
    out += [f'| `{m}` | {b} | {n} | {c} |' for m, b, n, c in NEW]
    out += ['', '## Summary', '', '| Module | Theorems | same | step | open | Verdict |', '|---|--:|--:|--:|--:|---|']
    for name, d in FAMILY.items():
        s, t, o = counts(d['rows'])
        out.append(f'| [{name}](#{name.lower()}) | {len(d["rows"])} | {s} | {t} | {o} | '
                   + ('ported' if o == 0 else 'partly ported') + ' |')
    total = [r for d in FAMILY.values() for r in d['rows']]
    s, t, o = counts(total)
    out.append(f'| **All {len(FAMILY)}** | **{len(total)}** | **{s}** | **{t}** | **{o}** | |')
    out += ['', 'Joins and bridge sections whose periphery import is in the family:', '',
            '| Join | Theorems read | same | step | open |', '|---|--:|--:|--:|--:|']
    for name, d in JOINS.items():
        s, t, o = counts(d['rows'])
        out.append(f'| [`{name}`](#{name.lower().replace(".", "")}) | {len(d["rows"])} | {s} | {t} | {o} |')

    def table(name, d, heading):
        out.extend(['', f'### {heading}', '',
                    f'Source: `{d["path"]}`. ' + ('Before: the step-0 audit.' if d['audited'] else 'Before: graded by F3Q.')
                    + (' ' + d['note'] if d['note'] else ''), '',
                    '| Theorem | Before | After | Core counterpart | How |', '|---|---|---|---|---|'])
        out.extend(f'| `{a}` | {b} | {c} | `{e}` | {f} |' for a, b, c, e, f in d['rows'])

    out += ['', '## Periphery modules']
    for name, d in FAMILY.items():
        table(name, d, name)
    out += ['', '## Joins and bridge sections', '',
            'A join or bridge declaration leaves the package when the modules it reads retire (the sweep, F3); its '
            'content is in the core first. "Before" is the join\'s own grade: a join states its periphery theorem '
            'through a core law, by logic.']
    for name, d in JOINS.items():
        table(name, d, f'`{name}`')
    out += ['', '## Overlaps', '',
            '- `Becoming.ReachableFrames` and `Becoming.ReachableFramesInherited` also read family J '
            '(`JointContinuationClassification`, `AlignmentDirection`); F3Q states only `common_relative_on_scope`.',
            '- `Becoming.Bridge` and `Becoming.Instances` read every family; F3Q states only the declarations listed '
            'above.', '']
    (HERE / 'port-q.md').write_text('\n'.join(out))


if __name__ == '__main__':
    render()
