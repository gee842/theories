#!/usr/bin/env python3
"""Apply S2's chapter edits: python3 -B apply_chapter.py. Each edit must match exactly once."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Settling.lean'
REC = '../results/records/when-the-runs-of-a-process-settle.md'

EDITS = [
    ('when the runs of a process settle, the part of assured enough that does not mention the target (possible and '
     'assured enough under undetermined laws: `Becoming.Enough`); ',
     'whether, with the limited principle of omniscience, no reachable change that can be undone gives settling '
     '(possible and assured enough under undetermined laws: `Becoming.Enough`; in a world a list holds, some run keeps '
     'changing exactly where a reachable change can be undone, while every run settling needs `LPO` already for two '
     'configurations: `Becoming.Settling`); '),
    ('[the-boundary-of-enough-under-undetermined-laws](../results/records/the-boundary-of-enough-under-undetermined-laws.md), '
     '[target-capture](../results/records/target-capture.md), [runaway-distance-unregistered]',
     '[the-boundary-of-enough-under-undetermined-laws](../results/records/the-boundary-of-enough-under-undetermined-laws.md), '
     f'[when-the-runs-of-a-process-settle]({REC}), '
     '[target-capture](../results/records/target-capture.md), [runaway-distance-unregistered]'),
]

BULLET_AFTER = '- *Enough under undetermined laws*'
BULLETS = [
    f'- *When the runs settle* ([Becoming.Settling]({LEAN}), [when-the-runs-of-a-process-settle]({REC})). A run that '
    'changes within a loop, between two visits of one configuration, gives a run from the same configuration that goes '
    'round the loop and keeps changing (`Settling.recurs_of_loop`). Along a run a list holds, change that recurs is a '
    'change within a loop (`Settling.loop_of_recurs`). So in a world a list holds, some run from a configuration keeps '
    'changing exactly where a configuration reachable from it has a step to another configuration from which it can be '
    'reached again (`Settling.keeps_changing_iff`), and where assured enough holds there is no such step '
    '(`Settling.assured_no_undoable`). That no run keeps changing does not give a step from which each run is settled: '
    'with two configurations and no way back from the second, no run keeps changing, and every run settling is the '
    'limited principle of omniscience (`Settling.OneWay.never_keeps_changing`, `Settling.OneWay.lpo_of_settles`), '
    'which the core does not assume.',
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
