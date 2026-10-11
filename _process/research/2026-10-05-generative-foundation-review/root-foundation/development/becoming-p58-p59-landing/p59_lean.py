#!/usr/bin/env python3
"""P59 Lean: imbalance counted as a relatum, proved equivalent first. python3 -B p59_lean.py ROOT

Adds the core module `Becoming.Imbalance` (imports `Becoming.Locality` and `Becoming.Resolution`;
no existing module changes) and registers it in the root module and the checker, after
`Becoming.Units` where that module exists and after `Becoming.Resolution` otherwise. Every edit is
an exact replacement that must match once."""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
HERE = Path(__file__).resolve().parent
LB = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
B = LB / 'Becoming'


def ws(old):
    return re.compile(r'\s+'.join(re.escape(w) for w in old.split()))


def sub_once(s, old, new, where):
    pat = ws(old)
    found = pat.findall(s)
    assert len(found) == 1, (where, len(found), old[:90])
    return pat.sub(lambda _: new, s, count=1)


def insert_before(s, anchor, text, where):
    m = list(ws(anchor).finditer(s))
    assert len(m) == 1, (where, len(m), anchor[:90])
    return s[:m[0].start()] + text + s[m[0].start():]


shutil.copyfile(HERE / 'Imbalance.lean', B / 'Imbalance.lean')

p = LB / 'Becoming.lean'
s = p.read_text()
after = 'Becoming.Units' if re.search(r'^import Becoming\.Units$', s, re.M) else 'Becoming.Resolution'
s = re.sub(rf'^import {re.escape(after)}$', f'import {after}\nimport Becoming.Imbalance', s, count=1,
           flags=re.M)
assert s.count('import Becoming.Imbalance') == 1
s = insert_before(s, '* `Becoming.Continuation` (L3):', '''* `Becoming.Imbalance` (L3): imbalance counted as a relatum, proved equivalent first (Ren,
  11 October 2026: "please"; adoption is Ren's). Wherever the flow does not balance, the
  difference is counted as the exchange of one more relatum, never active and requiring
  nothing; then every flow balances, the flow balances on a family across a step exactly where
  that relatum is idle there, and on a family across a step the activity premises hold of the
  extended flow exactly where they hold of the flow and it balances there. Nothing is adopted:
  the laws of the core keep balance as a local condition. The readings are the AI's, pending
  Ren.
''', 'root bullet')
p.write_text(s)

p = LB / 'check_becoming.py'
s = p.read_text()
s = sub_once(s, f'"{after}",', f'"{after}", "Becoming.Imbalance",', 'checker CORE')
s = insert_before(s, '"Continuation: across a step', '''"Imbalance: across a step a condition's level changes by what the flow gives and takes "
    "exactly where the flow balances there; counting the difference as the exchange of one "
    "more relatum, never active and requiring nothing, every flow balances, the flow balances "
    "on a family across a step exactly where that relatum neither gives nor takes on its "
    "members there, and the two representations are equivalent step by step: on a family "
    "across a step, only active relata giving, and only active relata taking and only what "
    "they draw on, hold of the extended flow exactly where they hold of the flow and it "
    "balances there; nothing is adopted. "
    ''', 'scope Imbalance')
p.write_text(s)
print('P59 Lean patch applied to', ROOT, 'after', after)
