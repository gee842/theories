#!/usr/bin/env python3
"""Apply R2's chapter edits: python3 -B apply_chapter.py. Each edit must match exactly once."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/CensusCounts.lean'
REC = '../results/records/counting-where-the-counts-exist.md'

EDITS = [
    ('One exception is not yet localized: the counting laws of `Becoming.Counting` quantify over worlds whose '
     'activity is globally decidable (section 0).',
     'The counting laws of `Becoming.Counting` quantify over worlds whose activity is globally decidable; restated '
     'over counted censuses (`Becoming.CensusCounts`), the laws under the premises, each selection, enclosure and '
     'finite worlds take no decision procedure and hold for every property of the counts. Only the laws where the '
     'premises bind still take one (section 0).'),
    ('the laws of counting worlds with decided activity are of two kinds: the tally alone, or the tally plus nothing '
     'arising at a step at which nothing is active (`World.counting_under`).',
     'the laws of counting worlds with decided activity are of two kinds: the tally alone, or the tally plus nothing '
     'arising at a step at which nothing is active (`World.counting_under`); over counted censuses the same holds '
     'with no decided activity and for every property of the counts (`World.counting_under_counted`).'),
    ('since the core does not assume function extensionality. | `Pointwise` | condition of the counting laws |',
     'since the core does not assume function extensionality. Over counted censuses no such condition is needed: '
     'counts taken as relations are unique where they exist (`Counts.unique`, `Becoming.CensusCounts`). | '
     '`Pointwise` | condition of the decided counting laws |'),
    ('which is global decidability of activity: a condition of those laws, not yet localized.',
     'which is global decidability of activity. Over counted censuses (`Becoming.CensusCounts`) the laws under the '
     'premises, each selection, enclosure and finite worlds take none: a ceasing or coming count across a step '
     'exists exactly where the listed relata\'s being listed at the other end is weakly decided '
     '(`World.ceasings_exist_iff_listed`). The laws where the premises bind (`World.binding_counting` and its '
     'family) still take it.'),
    ('(`World.counting_under`), with the activity of every relatum decided, a global condition of these laws.',
     '(`World.counting_under`), with the activity of every relatum decided; over counted censuses the same laws '
     'hold with no decision procedure and for every property of the counts (`World.counting_under_counted`).'),
    ('the counting laws (`World.enclosure_bounds_change`, `World.counting_under` and their family) still take '
     'decidability of activity for every relatum and step, `[∀ t x, Decidable (w.web.active t x)]`, and '
     '`World.counting_under` holds for pointwise properties only; a local refinement is open.',
     'the counting laws (`World.enclosure_bounds_change`, `World.counting_under` and their family) take '
     'decidability of activity for every relatum and step, `[∀ t x, Decidable (w.web.active t x)]`, and '
     '`World.counting_under` holds for pointwise properties only. Over counted censuses '
     f'([Becoming.CensusCounts]({LEAN})) the laws under the premises, each selection, enclosure and finite worlds '
     'need neither (`World.counting_under_counted`, `World.enclosure_bounds_change_counted`, '
     '`World.finite_counting_counted`); open there: the laws where the premises bind (`World.binding_counting` '
     'and its family), whose forward steps need counted forms.'),
    ('[counting-under-enclosure](../results/records/counting-under-enclosure.md), '
     '[ceasing-needs-arising](../results/records/ceasing-needs-arising.md)',
     '[counting-under-enclosure](../results/records/counting-under-enclosure.md), '
     f'[counting-where-the-counts-exist]({REC}), '
     '[ceasing-needs-arising](../results/records/ceasing-needs-arising.md)'),
    ('One exception is still global: the counting laws (`World.enclosure_bounds_change`, `World.counting_under` and '
     'their family) take decidability of activity at every step and for every relatum (§8.2).',
     'The counting laws (`World.enclosure_bounds_change`, `World.counting_under` and their family) take '
     'decidability of activity at every step and for every relatum. Over counted censuses '
     '(`Becoming.CensusCounts`) the laws under the premises, each selection, enclosure and finite worlds take '
     'none, and only the laws where the premises bind still take it (§8.2).'),
]

BULLET_AFTER = '- *Premises carve proper parts.*'
BULLET = (
    f'- *Counting where the counts exist.* A count is a relation, existing exactly where what it counts is decided '
    f'([Becoming.CensusCounts]({LEAN}), [counting-where-the-counts-exist]({REC})). Across a step a ceasing count '
    f'exists exactly where, for each relatum listed before the step, whether it is listed after the step is weakly '
    f'decided; a coming count likewise (`World.ceasings_exist_iff_listed`, `World.comings_exist_iff_listed`). '
    f'Wherever the counts of a census exist they are a tally with no decidedness. Under each selection of the '
    f'premises, under enclosure and in finite worlds, the laws of counting hold of them for every property of the '
    f'counts (`World.counting_under_counted`, `World.enclosure_bounds_change_counted`, '
    f'`World.finite_counting_counted`). Where a procedure decides activity, its marks are these counts '
    f'(`World.countsOf_decided`), so the decided laws follow. The laws where every selected premise binds '
    f'(`World.binding_counting` and its family) are not restated and still take the procedure.'
)

text = C.read_text()
for old, new in EDITS:
    assert text.count(old) == 1, ('edit does not match once', old[:80], text.count(old))
    text = text.replace(old, new)
lines = text.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith(BULLET_AFTER)]
assert len(idx) == 1, idx
assert BULLET not in text
lines.insert(idx[0] + 1, BULLET)
C.write_text('\n'.join(lines))
print('applied', len(EDITS), 'edits and one bullet')
