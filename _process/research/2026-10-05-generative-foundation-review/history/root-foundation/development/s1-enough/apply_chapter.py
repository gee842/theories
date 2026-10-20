#!/usr/bin/env python3
"""Apply S1's chapter edits: python3 -B apply_chapter.py. Each edit must match exactly once."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Enough.lean'
REC = '../results/records/the-boundary-of-enough-under-undetermined-laws.md'

EDITS = [
    ('the boundary of enough under undetermined laws; ',
     'when the runs of a process settle, the part of assured enough that does not mention the target (possible and '
     'assured enough under undetermined laws: `Becoming.Enough`); '),
    ('[seeking-boundary](../results/records/seeking-boundary.md), [target-capture](../results/records/target-capture.md), '
     '[runaway-distance-unregistered]',
     f'[seeking-boundary](../results/records/seeking-boundary.md), [the-boundary-of-enough-under-undetermined-laws]({REC}), '
     '[target-capture](../results/records/target-capture.md), [runaway-distance-unregistered]'),
]

BULLET_AFTER = '- *The boundary of enough.* Under a determined law,'
BULLETS = [
    f'- *Enough under undetermined laws* ([Becoming.Enough]({LEAN}), [the-boundary-of-enough-under-undetermined-laws]({REC})). '
    'Under an undetermined law a configuration has many runs, and enough parts in two. Some run from a configuration '
    'comes to rest with its target met exactly where a configuration reachable from it meets the target and has a step '
    'that stays (`Enough.possibly_rests_iff`). Every run from it does exactly where every reachable configuration with a '
    'step that stays meets the target and every run from it settles (`Enough.assured_iff`); the second part is of the '
    'process alone. Every configuration being able to stay and meeting the target is not enough: with two '
    'configurations and every step allowed, the alternating run never settles (`Enough.Free.stays_meet_not_assured`). '
    'Under a determined law the two are one and are the boundary above (`Enough.law_possibly_iff`, '
    '`Enough.law_possibly_iff_assured`).',
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
