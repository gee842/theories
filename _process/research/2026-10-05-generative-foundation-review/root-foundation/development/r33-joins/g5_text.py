#!/usr/bin/env python3
"""R33 (G5): apply the bridge to LearnableRuns and LimitVerification's vocabulary, then the prose pass
("predicts" for an extrapolation that "rests in accord") on the four learning-through-a-map modules,
rewrapping only the comment lines the pass lengthened. Run once on main's files (orig/ keeps them)."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B = HERE.parents[5] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
ORIG = HERE / 'orig'


def run(*args):
    subprocess.run([sys.executable, *map(str, args)], check=True)


lr = B / 'LearnableRuns.lean'
lr.write_text((ORIG / 'LearnableRuns.lean').read_text())
run(HERE / 'edit_learnableruns.py', lr)
s = lr.read_text()
for old, new in [
    ('Limit.Identifies g fun r => some (val (r.state 0)) := fun g =>',
     'Limit.Identifies g fun r => some (val (r.state 0)) := fun _ =>'),
    ('  fun ⟨g, fixed, identifies⟩ =>\n    match', '  fun ⟨_, fixed, identifies⟩ =>\n    match'),
    ('      Limit.Tracks (guess reg pred) fun k r => some (val (r.state k)) :=',
     '      Limit.Tracks (guess (next := next) reg pred) fun k r => some (val (r.state k)) :='),
]:
    assert s.count(old) == 1, old
    s = s.replace(old, new)
lr.write_text(s)
for name in ['Learnable', 'Unrolling', 'Labels']:
    (B / f'{name}.lean').write_text((ORIG / f'{name}.lean').read_text())
run(HERE / 'rests_prose.py', *[B / f'{n}.lean' for n in ['Learnable', 'Unrolling', 'Labels', 'LearnableRuns']])
for name in ['Learnable', 'Unrolling', 'Labels', 'LearnableRuns']:
    run(HERE / 'rewrap.py', ORIG / f'{name}.lean', B / f'{name}.lean')
