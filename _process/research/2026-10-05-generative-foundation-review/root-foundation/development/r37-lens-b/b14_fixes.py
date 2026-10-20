#!/usr/bin/env python3
"""R37 B14, after b14_witnesses.py: the exact edits the first scratch build asked for.

* A constructor named in full (`Member.first`) does not unfold the abbreviation `Member`, so the
  modules naming one write `Witnesses.Member.first`; `.first` with an expected type is unchanged.
* `Exceeding.Alone.flow`, the renewer with one taker, is `Witnesses.relay` too."""
import re
from pathlib import Path

B = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
for mod in ('Exhaustion', 'RelativePosition'):
    p = B / f'{mod}.lean'
    s = p.read_text()
    s2 = re.sub(r'(?<![.\w])Member\.(renewer|first|second)\b', r'Witnesses.Member.\1', s)
    assert s2 != s
    p.write_text(s2)
p = B / 'Continuation.lean'
s = p.read_text()
old = '''def flow : Flow Exceeding.Member Unit where
  present _ := [.renewer, .first]
  take _ f _ := match f with
    | .renewer => 0
    | .first => 2
    | .second => 0
  give _ f _ := match f with
    | .renewer => 2
    | .first => 0
    | .second => 0'''
assert s.count(old) == 1
p.write_text(s.replace(old, 'def flow : Flow Exceeding.Member Unit := Witnesses.relay (fun _ => [.renewer, .first]) 2 2 0'))
