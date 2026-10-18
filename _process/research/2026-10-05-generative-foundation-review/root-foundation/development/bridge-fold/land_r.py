#!/usr/bin/env python3
"""F3R (18 October 2026): register F3R's new core modules. Idempotent; rerun after a rebase.

usage (from the checkout root): python3 -B land_r.py [MODULE ...]   (default: every module below)

Adds each module to `CORE` in `check_becoming.py` after its anchor, imports it in `Becoming.lean`
and lists it in that file's module notes, the package README's layer table and import notes, and
the chapter reference's table. Touches no existing core module, bridge or join file, and neither
the `BRIDGE` nor the `PERIPHERY_JOINS` list.
"""
import pathlib
import re
import sys

PKG = pathlib.Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming')
REF = pathlib.Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE.md')

# module: (layer, CORE / docstring / reference anchor, README anchor, theorems, text)
MODULES = {
    'Integers': ('L2', 'Assurance', 'Quantum', 37,
                 'constructive ring laws on `Int` (no premise): integers read as difference pairs of natural '
                 'numbers, with the commutativity, associativity, negation, cancellation and multiplication laws the '
                 'dephasing model uses, every one with an empty axiom report'),
    'AssurancePlans': ('L2', 'Assurance', 'Quantum', 23,
                       'plans on determined, open and shut processes (no premise): under a determined process a trace '
                       'has one end, so some end meeting a goal is every end (`Trace.determined_end`, '
                       '`every_end_of_some_end`); with every move open some end is not every end, and with none every '
                       'claim about ends is vacuous (`Open.some_not_every`, `Shut.no_end`); an itinerary of responses '
                       'that keeps a band completes from every configuration in it (`completes_itinerary`); in the '
                       'regulation model opposite moves keep the band and merge nothing (`Regulation.kept_along`), and '
                       'in the three-route model each adequate reading merges outcomes another tells apart, so no '
                       'coarsest adequate description exists (`Routes.no_coarsest_adequate`)'),
    'SupportRecovery': ('L3', 'RenewalFlow', 'RenewalFlow', 9,
                        'recovery in the support-gated family (no premise): with both formations unsupported the level '
                        'stays (`absorbs`); a window of supported net repair raises the level by at least its length '
                        '(`window_progress`); two pulses with the same later inputs recover or end for good, and the '
                        'recovered history is neither renewing nor consuming in the whole-time classification '
                        '(`same_later_inputs`, `supported_pulse_recovers`, `unsupported_pulse_ends`, `recovered_neither`)'),
    'ActiveReading': ('L4', 'Ranking', 'Ranking', 14,
                      'the reading of every active event beside the whole-run reading (no premise): the whole-run '
                      'reading withholds a consumer\'s events, and living significance on it credits exactly the active '
                      'events of non-consuming formations (`g0_wholeRun_iff`); under the reading of every active event an '
                      'overdrawing formation leaves the two courses unranked, so C admits a comparison preferring the '
                      'course with it (`overdraw_unranked`, `overdraw_admits_occurrence`), while sharing still extends '
                      'winning by consumption (`contest_readings`)'),
    'StrictTransport': ('L4', 'LossMatching', 'LossMatching', 19,
                        'strict transport along a supplied comparison (the comparison is a hypothesis): a strict anchor '
                        'is carried by weak steps on its side, through compatible relations, along runs that lose or '
                        'gain no claim, and by faithful redescription, and a supplied link makes it a reason '
                        '(`reason_of_strict_above`); a cutoff order prefers repair exactly below its cutoff, so '
                        'compatible cutoffs disagree, and the finishing-first rival supplies no cutoff '
                        '(`cutoffs_disagree`, `continuation_first_no_cutoff`)'),
    'MatchedCourses': ('L4', 'StrictTransport', 'StrictTransport', 33,
                       'comparison anchors for courses from one start that each secure the claims of some positions '
                       '(reading the claims as complete comparable basic losses is the premise `BasicAlike` or '
                       '`BaseApart`, and sufficiency of matching, `Frame.SufficientMatching`, is a hypothesis): support '
                       'returns while missed claims stay lost (`recovery_retains_loss`); counts of losses decide strict '
                       'matches (`matches_iff`, `lost_counts`), which give the two anchors and their order under '
                       'sufficiency (`conditional_outer_order`); where every claim rests on a base, the course losing '
                       'it matches nothing (`fragile_b3_matches_nothing`)'),
    'Dephasing': ('L4', 'Readout', 'Coupling', 63,
                  'the control–target dephasing model on integer amplitudes (no premise): dephasing keeps the '
                  'diagonal and the mass and merges a prepared and a coherent state, so no decoder reads the response '
                  'through the diagonal record and no uniform map restores it (`no_diagonal_response_decoder`, '
                  '`no_uniform_dephase_inverse`, through `Readout`); recording into a branch reduces to dephasing and '
                  'joint reversal restores the control; read as a law of change, dephasing settles, merges, is not '
                  'lossless, and its runs meet (`settles`, `not_lossless`, `runs_meet`)'),
    'ProjectedLaws': ('L4', 'Dephasing', 'Dephasing', 28,
                      'projected laws of a deterministic law (no premise): a reduced law commutes with the law exactly '
                      'when the law factors through the projection, exactly when merged configurations go alike, and '
                      'then along every word (`commuting_iff_factors`, `fibre_iff_goAlike`, `commuting_iff_traces`); '
                      'with the same cells, crossed wiring leaves one cell no law of its own '
                      '(`no_autonomous_left_law`), and in the device model formation and recurrence share one history '
                      'that parts alone cannot keep (`parts_only_cannot_preserve_futures`)'),
    'JointPhase': ('L4', 'ProjectedLaws', 'ProjectedLaws', 23,
                   'joint phase on two registers (no premise): the interaction keeps both local states and the basis '
                   'masses while it changes the cross term, so the relation is told apart only through the joint '
                   '(`same_interaction_distinguishes_relation`); no update of the local pair carries the law '
                   '(`no_local_pair_update`, `local_pair_carries_no_law`); a summary retaining the control is exact '
                   'along every finite word and omits the other relations (`every_finite_word_exact`, '
                   '`summary_omits_other_relations`)'),
    'ActivationCapacity': ('L4', 'Bundles', 'Bundles', 7,
                           'effective capacity in the activation law (no premise): a configuration realizes both claims '
                           'exactly when both are active (`joint_iff`); the joint content is realizable within one move '
                           'from the coupled configuration and not from the initial one, so a preparation step changes '
                           'the current capacity (`preparation_changes_capacity`); after the release no number of moves '
                           'realizes it (`released_not_joint`, `release_loses_joint`), and the prepared configuration can '
                           'still end one-sided (`prepared_can_end_one_sided`)'),
}
IMPORT_NOTES = {
    '; within L3,': '; `AssurancePlans` imports `Assurance`',
    '; within L4,': '; `SupportRecovery` imports `RenewalFlow`',
    '). L1–L3 contain': ('; `ActiveReading` imports `Ranking`; `MatchedCourses` imports `LossMatching` and '
                         '`StrictTransport`; `Dephasing` imports `Readout`; `ProjectedLaws` imports `Readout`; '
                         '`JointPhase` imports `Dephasing` and `ProjectedLaws`'),
    '; `Narrowing` imports': '; `ActivationCapacity` imports `Bundles` and `Recurrence`',
}


def after_entry(lines, start, is_entry):
    """Index just past the entry starting at `start` (its continuation lines included)."""
    i = start + 1
    while i < len(lines) and not is_entry(lines[i]) and lines[i].startswith('  '):
        i += 1
    return i


def main(selected):
    checker = PKG / 'check_becoming.py'
    src = checker.read_text()
    core = re.search(r'^CORE = \[(.*?)\]', src, re.S | re.M)
    body = core.group(1)
    for m in selected:
        name = f'"Becoming.{m}"'
        if name in body:
            continue
        anchor = f'"Becoming.{MODULES[m][1]}"'
        assert anchor in body, anchor
        body = body.replace(anchor, f'{anchor}, {name}', 1)
    src = src[:core.start(1)] + body + src[core.end(1):]
    checker.write_text(src)

    root = PKG / 'Becoming.lean'
    lines = root.read_text().split('\n')
    for m in selected:
        layer, anchor, _, _, text = MODULES[m]
        if f'import Becoming.{m}' not in lines:
            i = lines.index(f'import Becoming.{anchor}')
            lines.insert(i + 1, f'import Becoming.{m}')
        if not any(l.startswith(f'* `Becoming.{m}` (') for l in lines):
            i = next(k for k, l in enumerate(lines) if l.startswith(f'* `Becoming.{anchor}` ('))
            j = after_entry(lines, i, lambda l: l.startswith('* `'))
            words, out, cur = f'* `Becoming.{m}` ({layer}): {text}.'.split(' '), [], ''
            for w in words:
                if cur and len(cur) + 1 + len(w) > 98:
                    out.append(cur)
                    cur = '  ' + w
                else:
                    cur = f'{cur} {w}' if cur else w
            out.append(cur)
            lines[j:j] = out
    root.write_text('\n'.join(lines))

    readme = PKG / 'README.md'
    lines = readme.read_text().split('\n')
    for m in selected:
        layer, _, anchor, _, text = MODULES[m]
        if any(l.startswith(f'| {layer} | [`Becoming.{m}`]') for l in lines):
            continue
        i = next(k for k, l in enumerate(lines) if re.match(rf'^\| L\d \| \[`Becoming\.{anchor}`\]', l))
        lines.insert(i + 1, f'| {layer} | [`Becoming.{m}`](Becoming/{m}.lean) | {text} |')
    text = '\n'.join(lines)
    for at, note in IMPORT_NOTES.items():
        if note not in text:
            assert text.count(at) == 1, at
            text = text.replace(at, note + at, 1)
    readme.write_text(text)

    lines = REF.read_text().split('\n')
    for m in selected:
        layer, anchor, _, count, text = MODULES[m]
        if any(f'[Becoming.{m}](' in l for l in lines):
            continue
        i = next(k for k, l in enumerate(lines) if re.match(rf'^\| L\d \| \[Becoming\.{anchor}\]\(', l))
        link = f'../../../{PKG}/Becoming/{m}.lean'
        lines.insert(i + 1, f'| {layer} | [Becoming.{m}]({link}) | {text[0].upper() + text[1:]}. | {count} |')
    REF.write_text('\n'.join(lines))


if __name__ == '__main__':
    main(sys.argv[1:] or list(MODULES))
