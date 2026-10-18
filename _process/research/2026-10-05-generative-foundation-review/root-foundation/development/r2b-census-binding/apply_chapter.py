#!/usr/bin/env python3
"""Apply R2b's chapter edits: python3 -B apply_chapter.py. Each edit must match exactly once."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
LEAN2 = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/CensusBinding.lean'
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/CensusCounts.lean'

EDITS = [
    ('restated over counted censuses (`Becoming.CensusCounts`), the laws under the premises, each selection, enclosure '
     'and finite worlds take no decision procedure and hold for every property of the counts. Only the laws where the '
     'premises bind still take one (section 0).',
     'restated over counted censuses (`Becoming.CensusCounts`, `Becoming.CensusBinding`), every law of that family, '
     'under the premises, each selection, where the selected premises bind, under enclosure and in finite worlds, '
     'takes no decision procedure and holds for every property of the counts (section 0).'),
    ('The laws where the premises bind (`World.binding_counting` and its family) still take it.',
     'Over counted censuses the laws where the premises bind take none either (`Becoming.CensusBinding`).'),
    ('The laws where every selected premise binds (`World.binding_counting` and its family) are not restated and '
     'still take the procedure.',
     f'The laws where the selected premises bind hold of them too, with what binding adds: something active, something '
     f'arising, and both at one step, each where the selection gives it (`World.binding_counting_under_counted` and '
     f'its finite and enclosed forms, [Becoming.CensusBinding]({LEAN2})).'),
    (f'Over counted censuses ([Becoming.CensusCounts]({LEAN})) the laws under the premises, each selection, enclosure '
     'and finite worlds need neither (`World.counting_under_counted`, `World.enclosure_bounds_change_counted`, '
     '`World.finite_counting_counted`); open there: the laws where the premises bind (`World.binding_counting` and '
     'its family), whose forward steps need counted forms.',
     f'Over counted censuses ([Becoming.CensusCounts]({LEAN}), [Becoming.CensusBinding]({LEAN2})) every law of this '
     'family needs neither (`World.counting_under_counted`, `World.enclosure_bounds_change_counted`, '
     '`World.binding_counting_under_counted`), so the exception is resolved by counted forms; the decided statements '
     'stay. Open there: using the counted statements where the decided ones are used; the laws read on dependence, '
     'which take a decision of dependence rather than of activity.'),
    ('take none, and only the laws where the premises bind still take it (§8.2).',
     'take none, and over counted censuses the laws where the premises bind take none either '
     '(`Becoming.CensusBinding`, §8.2).'),
]

text = C.read_text()
for old, new in EDITS:
    assert text.count(old) == 1, ('edit does not match once', old[:80], text.count(old))
    text = text.replace(old, new)
C.write_text(text)
print('applied', len(EDITS), 'edits')
