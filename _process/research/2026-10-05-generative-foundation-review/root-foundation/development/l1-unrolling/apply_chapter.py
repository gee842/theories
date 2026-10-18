#!/usr/bin/env python3
"""Apply L1's chapter edits: python3 -B apply_chapter.py. Each edit must match exactly once."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Unrolling.lean'
REC = '../results/records/what-an-extrapolation-given-nothing-fixes.md'

EDITS = [
    ('a learner given nothing that rests on every learnable target, or a witness that none does; ',
     'learning a target from finitely many of its values, given part of a reading of the future rather than the '
     'whole (given nothing, no learner rests on every learnable target; a target is learnable exactly where it is, '
     'from some step on, a reading of the future through the map, which the prefix fixes given nothing: '
     '`Becoming.Unrolling`); '),
    ('[learnable-through-registration](../results/records/learnable-through-registration.md) |',
     '[learnable-through-registration](../results/records/learnable-through-registration.md), '
     f'[what-an-extrapolation-given-nothing-fixes]({REC}) |'),
]

BULLET_AFTER = '- Targets that go alike across the registration (`Lumped`) are always learnable'
BULLETS = [
    f'- *Given nothing, the future is fixed* ([Becoming.Unrolling]({LEAN}), [what-an-extrapolation-given-nothing-fixes]({REC})). '
    'Unroll the lasso learner given nothing (the extrapolation by elimination over the lasso candidates) on its own '
    'proposals, putting each proposed value at the front of the prefix. In every world a list holds, from the '
    'identification bound on, it then proposes the value through the map at every step ahead (`Learnable.ahead_fixes`). '
    'Over every course no prefix fixes the next value (`Learning.no_prefix_fixes_next`); here a list holds the world.',
    '- *Learnable exactly where a reading of the future.* A target is learnable exactly where some reading of '
    'futures, respecting values at each step, is the target from some step on along every orbit '
    '(`Learnable.learnable_iff_reading`). The reading on the necessity side is given the world, the law and the '
    'target (`Learnable.fromWorld`): a configuration as many steps on as the list is long returns, and returning '
    'configurations whose targets agree from some step on have equal targets (`Learnable.eq_of_returns`). On the '
    'sufficiency side the learner given only the reading learns the target (`Learnable.reading_rests_from`). So what '
    '`fromLaw` is given beyond the prefix is exactly a reading of the future through the map.',
    '- *Given nothing, not every learnable target.* No learner given nothing rests on every learnable target: in a '
    'one-configuration world the targets `true` and `false` are each learnable, with the same prefixes '
    '(`Learnable.given_nothing_not_every`). The witness is elementary; the content is what the prefix does fix. The '
    'same three hold along the runs of the law (`LearnableRuns.ahead_fixes`, `LearnableRuns.learnable_iff_reading`, '
    '`LearnableRuns.given_nothing_not_every`).',
]

text = C.read_text()
for old, new in EDITS:
    assert text.count(old) == 1, ('edit does not match once', old[:80], text.count(old))
    text = text.replace(old, new)
lines = text.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith(BULLET_AFTER)]
assert len(idx) == 1, idx
for b in BULLETS:
    assert b not in text
lines[idx[0] + 1:idx[0] + 1] = BULLETS
C.write_text('\n'.join(lines))
print('applied', len(EDITS), 'edits and', len(BULLETS), 'bullets')
