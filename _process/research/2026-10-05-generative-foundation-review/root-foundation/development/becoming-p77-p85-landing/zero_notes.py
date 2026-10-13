#!/usr/bin/env python3
"""Reconcile P77/P78/P79 with the zero-premise plan; retain the historical inventory.
Usage: python3 -B zero_notes.py W FIRST_SECTION
"""
from pathlib import Path
import sys

W, S = Path(sys.argv[1]).resolve(), int(sys.argv[2])
p = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/ZERO-PREMISE-PLAN.md'
s = p.read_text()
assert '**现状（P77–P79）。**' not in s
marker = '## 2. 零前提的重述 / Zero-premise restatements\n'
assert s.count(marker) == 1
note = f'''**表示的检验（P77、P78）。** 列出一次已重新奠定：列表恰在成员之间同一已定时能列出一次，否证形式的规律不需要它，按关系不可分辨地计数在每个世界都固定数目等价于排中律（`Becoming.Listing`，研究 §{S}）。这保留名字与关系的区别，不替 Ren 选择同一的读法。时间也不只检验粗化：停顿与去掉空步保留所名规律，给定足迹时，有交集交换的偏序恰刻画可通过交换无交集相邻步达到的次序（`Becoming.Order`，研究 §{S+1}）。足迹本身、最小足迹、正规形、重排中的普查及实际时间对应仍须分别处理。

**Tests of the representation (P77, P78).** Listing once is re-founded: a list can be listed once exactly where identity among its members is decided; refutation laws need no such premise, and fixing every list's number up to relational indiscernibility in every world is equivalent to excluded middle (`Becoming.Listing`, study §{S}). This preserves the distinction between names and relations and does not choose Ren's reading of identity. Time is tested beyond coarsening: stuttering and removing idle steps keep the named laws; for a supplied footprint, the partial order of joined exchanges characterizes the orders reached by commuting unjoined neighbouring exchanges (`Becoming.Order`, study §{S+1}). The footprint itself, the least footprint, normal forms, censuses along reorderings and actual time correspondence remain separate questions.

'''
s = s.replace(marker, note + marker)
marker2 = '**现状（P48）。**'
i = s.index(marker2)
note2 = f'''**现状（P77–P79）。** P77 的列出一次与 P78 的步序见上。P79 不重复 P48 的局部化：它证明所给一步样式的实现恰是它遵守所名条件的规律（`OneStep.every_iff`、`OneStep.laws`），补出所取非零须有取者、所给非零须有给者，精确刻画给者、容量与活动所加的规律，以及单一家族与逐步选家族上的接续（研究 §{S+2}）。这关闭所给样式的完备性问题，不是全部生成或全部规律的普遍完备性证明；活跃者计数、整段容量与活动仍开放。下面的旧清点、提议与历史现状按原范围保留。

**Status (P77–P79).** P77's listing once and P78's step order are stated above. P79 adds to P48's localization: realizing a specified one-step pattern is exactly obeying the laws of the named conditions (`OneStep.every_iff`, `OneStep.laws`). It supplies the missing nonzero-taking/taker and nonzero-giving/giver laws, characterizes exactly what givers, capacity and activity add, and the chaining on one family or continuity on families chosen step by step (study §{S+2}). This closes completeness for those patterns, not universal completeness for becoming or every law. Counts of active relata and capacity and activity over runs remain open. The earlier inventory, proposals and historical status below retain their original scope.

'''
s = s[:i] + note2 + s[i:]
p.write_text(s)
print('zero-premise plan: P77/P78 representation tests and P79 completeness reconciled')
