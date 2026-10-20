#!/usr/bin/env python3
"""CG2: the rest outruns the renewal, four theorems added to Becoming.Exclusion (Flow.rest_le_taken,
outrun_excess, outrun_below, outrun_ends, outrun_reading_alike; excess_of_takesAll now derived from
outrun_excess, rule 9). Updates the root doc bullet, the checker's scope text and the README row.
The module itself is edited in place on the branch. usage: python3 -B integrate.py (CG2_ROOT names the
checkout; each edit must match exactly once)"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['CG2_ROOT']).resolve() if os.environ.get('CG2_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


root = (PKG / 'Becoming.lean').read_text()
assert 'outrun' not in root, 'already integrated'
root = once(root, '''  The levels admit the second where it ends, so admission does not see the exclusion.
* `Becoming.Exhaustion` (L1)''', '''  The levels admit the second where it ends, so admission does not see the exclusion.
  Where a part (the rest) takes jointly more than is given, renewal ends whatever a member
  outside it takes, and with need one every reading after the end is alike under the
  member's acts: its restraint is invisible to such a reading.
* `Becoming.Exhaustion` (L1)''')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '''    "while the levels of the last two courses admit every member at every step. No ethical "
    "predicate occurs. "''', '''    "while the levels of the last two courses admit every member at every step; where a part takes "
    "jointly more than is given, the joint taking exceeds it whatever any other formation takes, so "
    "as many such steps as the level allows end every formation depending on the condition, and with "
    "need one two such flows agree on the condition from then on, however a member's act differs. "
    "No ethical predicate occurs. "''')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
rd = once(rd, "the levels of the last two courses admit every member at every step and each level path includes the other (`Excluding.admission_alike`) ([what-taking-all-excludes]",
          "the levels of the last two courses admit every member at every step and each level path includes the other (`Excluding.admission_alike`); where a part (the rest) takes jointly more than is given, the joint taking exceeds it whatever any other formation takes (`Flow.outrun_excess`, from `Flow.rest_le_taken`; `Flow.excess_of_takesAll` is its case), so `n` such steps from below `n + m` leave the level below `m` and end every dependent whatever a member outside the part takes (`Flow.outrun_below`, `Flow.outrun_ends`), and with need one every score reading the condition after the end scores two such flows alike, however the member's act differs (`Flow.outrun_reading_alike`) ([what-taking-all-excludes]")
(PKG / 'README.md').write_text(rd)
print('integrated')
