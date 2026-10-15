#!/usr/bin/env python3
"""I4b-1: the documents naming Becoming.Gated (run from the repository root after copying the module in).

* the theory chapter's §9 row for Becoming.Gated: what it states and its theorem count;
* the module bullet in Becoming.lean.
Each edit asserts the text it replaces, so a second run fails."""
import re
from pathlib import Path

LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
GATED = Path(LEAN + 'becoming/Becoming/Gated.lean')
theorems = sum(1 for line in GATED.read_text().splitlines() if re.match(r'^theorem ', line))

chapter = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
s = chapter.read_text()
old = ('只有一类动作能改变的东西（不加前提）：量沿每段非门控进程保持，恰当每个非门控步保持它；改变它的进程经过门，且在一个本身改变它的门控步上。'
       '/ What only a class of moves can change: kept along every ungated course exactly when kept by every ungated step; '
       'change is located at a gated step. | 4 |')
new = ('只有一类动作能改变的东西（不加前提）：量沿每段非门控进程保持，恰当每个非门控步保持它；改变它的进程经过门，且在一个本身改变它的门控步上。'
       '单向亦然：非门控步保持的性质，离开它的进程经过门；非门控步反映的性质，成立处的进程或始于它成立处，或在一个门控步之后它成立（不判定该性质）；'
       '门是命题而非已定时，这一律恰是双重否定消去。'
       '/ What only a class of moves can change: kept along every ungated course exactly when kept by every ungated step; '
       'change is located at a gated step. One direction suffices: a course leaving a property the ungated steps preserve '
       'passes the gate, and a course ending where a property the ungated steps reflect holds started where it held or '
       'has a gated step after which it holds, with nothing about the property decided; with the gate a proposition '
       f'rather than decided, this law is exactly double-negation elimination. | {theorems} |')
assert s.count(old) == 1, 'chapter row changed'
chapter.write_text(s.replace(old, new))

package = Path(LEAN + 'becoming/Becoming.lean')
s = package.read_text()
old = """* `Becoming.Gated` (L2): what only a class of moves can change, with no premise. A quantity kept
  by every ungated step is kept along every ungated course, and conversely; a course that
  changes it passes the gate, at a gated step that itself changes it.
"""
new = """* `Becoming.Gated` (L2): what only a class of moves can change, with no premise. A quantity kept
  by every ungated step is kept along every ungated course, and conversely; a course that
  changes it passes the gate, at a gated step that itself changes it. One direction suffices: a
  course leaving a property the ungated steps preserve passes the gate, and a course ending where
  a property the ungated steps reflect holds started where it held or has a gated step after
  which it holds, nothing about the property decided. With the gate a proposition, the origin
  law is exactly double-negation elimination.
"""
assert s.count(old) == 1, 'package bullet changed'
package.write_text(s.replace(old, new))
print('chapter row (', theorems, 'theorems) and package bullet')
