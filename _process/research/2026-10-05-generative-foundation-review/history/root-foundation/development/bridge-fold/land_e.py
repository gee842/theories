#!/usr/bin/env python3
"""F3E (18 October 2026): register F3E's new core modules. Idempotent; rerun after a rebase.

usage (from the checkout root): python3 -B land_e.py [MODULE ...]   (default: every module below)

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
# The README's layer table lists no `Likeness`, `Composition`, `Joining` or `Granularity`, so its rows
# follow `Histories` in order; the other lists follow the module each builds on.
MODULES = {
    'HistoryLanguages': ('L3', 'Granularity', 'Histories', 37,
                         'languages of histories (no premise): a prefix-closed language of words is realized exactly by '
                         'the law of its histories (`realizes_feasible`); continuation profiles, letterwise stability '
                         'and the obstruction that locates a changed profile; the bounded language, the latch and the '
                         'gate'),
    'Coverage': ('L3', 'HistoryLanguages', 'HistoryLanguages', 23,
                 'a placement course and the global cover it builds (no premise): a course of placements covers '
                 'a board exactly where its tiles and the rest make up the board up to order, with no event order; '
                 'where allowed tiles join opposite colours the balance is kept, so the board with two opposite '
                 'corners removed has no cover (`mutilated_no_cover`), and balance does not determine coverability '
                 '(`balance_does_not_determine_coverability`)'),
    'Presentations': ('L3', 'Coverage', 'Coverage', 36,
                      'exact and reduced presentations (no premise; extensionality of predicates named where used): '
                      'presentations exact for the same answers share one kernel and one alignment; a relation '
                      'descends to codes exactly where it is saturated; the canonical presentation by all predicates; '
                      'a frame\'s branching tests as questions'),
    'Carriers': ('L3', 'Presentations', 'Presentations', 46,
                 'one carrier, several laws (no premise): `static`, `toggle` and their kin share carrier and feasible '
                 'words; symmetry does not fix the law, and relational identity reads `static` and `toggle` as one '
                 'recurrence; feasible words do not fix endpoints (`word_feasibility_does_not_determine_endpoints`)'),
    'BranchingCorrespondence': ('L3', 'Carriers', 'Carriers', 10,
                                'branching tests match the configurations of two frames (excluded middle named): '
                                'configurations passing the same tests match successors and are bisimilar, reachable '
                                'configurations correspond one to one and steps are carried exactly '
                                '(`SameBranchingTests.correspondence_of_em`); every bisimulation agrees with the tests'),
    'JointCorrespondence': ('L3', 'BranchingCorrespondence', 'BranchingCorrespondence', 9,
                            'what a joint frame reaches by steps and parts (stability of the tests named): joint tests '
                            'carry pairs and steps exactly and match reachable configurations one to one; codes '
                            'reading the joint tests lift the parts, the plans and exclusive support'),
    'ListFootprints': ('L3', 'JointCorrespondence', 'JointCorrespondence', 9,
                       'lists as footprints (no premise): a plan is realized exactly where what its leaves draw on is '
                       'supported, so reassociating or reordering a plan keeps whether it is realized '
                       '(`realizes_iff_of_perm`)'),
    'Fragments': ('L3', 'ListFootprints', 'ListFootprints', 23,
                  'fragments of a process joined end to start (no premise): joining is functional and associative '
                  'with idle units; probes by the fragments that stay recover the ends and the joining and miss the '
                  'course between (`probes_miss_course`)'),
    'LocalUnits': ('L3', 'Fragments', 'Fragments', 45,
                   'units of a joining (no premise): unique under associativity, shared by what joins, carried by '
                   'correspondences; chain completion is that a common unit suffices; on traced fragments the units '
                   'are the fragments that stay, and the process that moves at most once has units but is not chain '
                   'complete'),
    'JoiningContexts': ('L3', 'LocalUnits', 'LocalUnits', 23,
                        'contexts of a joining as courses of its frame (no premise): agreeing on contexts is passing '
                        'the same tests (`ContextSame.iff_sameTests`) and, for a functional joining, the largest '
                        'compatible relation (`contextSame_iff_compatible`)'),
    'JoiningCodes': ('L3', 'JoiningContexts', 'JoiningContexts', 11,
                     'codes read against contexts and branching tests (excluded middle named where used): the joining '
                     'of codes, its domain and functionality; a test asked after a context; a presentation exact and '
                     'reduced for the tests lifts a joining with listed outcomes (`FiniteOutcomes.lifts_of_exact`)'),
    'JoiningRoles': ('L3', 'JoiningCodes', 'JoiningCodes', 23,
                     'roles and retained references by branching tests (excluded middle and function extensionality '
                     'named where used): units give every role; the traced fragments of the process that moves once '
                     'collapse through roles and stay apart through retained references (`Fragment.once_codes_apart`)'),
    'Grains': ('L3', 'JoiningRoles', 'JoiningRoles', 6,
               'what remained of reading at two grains (no premise; the decision of two tests named where used): '
               'renaming into single-move blocks and reading finer returns the test (`BranchingTest.finer_rename`); '
               'either of two decided tests; histories of recipes are finer courses; configurations with no step and '
               'the same claims are alike (`Alike.of_stuck`)'),
}
IMPORT_NOTES = {
    '; within L4,': ('; `HistoryLanguages` imports `Histories`; `Presentations` and `JointCorrespondence` import '
                     '`Composition`; `Carriers` imports `Unfolding`; `BranchingCorrespondence` and `Grains` import '
                     '`Granularity`, and `BranchingCorrespondence`, `JointCorrespondence` and `Fragments` import '
                     '`Presentations`; `ListFootprints` imports `Composition`, `Coverage`, `Joining` and `Weighted`; '
                     '`Fragments` imports `Joining`; `LocalUnits` imports `Fragments`, `JoiningContexts` imports '
                     '`LocalUnits`, `JoiningCodes` imports `JoiningContexts` and `BranchingCorrespondence`, and '
                     '`JoiningRoles` imports `JoiningCodes`'),
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
