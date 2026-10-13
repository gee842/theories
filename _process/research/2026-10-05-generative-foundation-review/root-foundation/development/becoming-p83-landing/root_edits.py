#!/usr/bin/env python3
"""Add P83's module to the root module, the checker and the Lean README.

Usage: python3 -B root_edits.py ROOT core      (after copying the module, before the landing run)
       python3 -B root_edits.py ROOT readmes   (after both receipts pass)

`core` adds the import and docstring bullet of `Becoming.Identification` after those of
`Becoming.Description` in `Becoming.lean`, and the module with its scope sentence after Description's
in `CORE` and `SCOPE` of `check_becoming.py`. `readmes` adds the spine row and the import note to
`becoming/README.md`. The layer is Description's, read from its docstring bullet in `Becoming.lean`.
Every anchor must occur exactly once; rerunning on an edited checkout fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
STAGE = sys.argv[2]
assert STAGE in {'core', 'readmes'}, STAGE
B = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
root_text = (B / 'Becoming.lean').read_text()
found = re.findall(r'^\* `Becoming\.Description` \((L\d)\)', root_text, flags=re.M)
assert len(found) == 1, found
LAYER = found[0]
print('Description is', LAYER)


def edit(path, pairs):
    s = path.read_text()
    for anchor, new in pairs:
        assert s.count(anchor) == 1, (path.name, anchor[:80], s.count(anchor))
        s = s.replace(anchor, new)
    path.write_text(s)
    print('edited', path.relative_to(ROOT))


BULLET = f"""* `Becoming.Identification` ({LAYER}): identification, what a bounded record fixes (P83), with no
  premise beyond the bound on states. Two periods (Fine and Wilf): a course with period `p + 1`
  that comes back after `Q` steps at its first `p` steps does so at every step. Histories with at
  most `N` and `N'` states are fixed by their record before `N + N' - 1`, and for `N = 1` and
  `N = N'` no shorter record does. Where the bound is given induction is deduction: a lasso
  hypothesis within `N` unrefuted before `2N - 1` holds at every step; the learner that knows the
  bound is refuted nowhere and right from `2N - 1` on, and none can always speak sooner; the
  liar's rhythm is derived; a world answering that learner exceeds the bound. The learner that
  does not know the bound rests within it: a lasso hypothesis within `N` unrefuted for `2N - 1`
  steps is never refuted again, so the learner by refutation over the lasso hypotheses is right
  at every step from `N + (2N - 1) * tri N` on, a step its record does not show. In a world a
  list holds, naming configurations by their registered futures for `2N - 1` steps makes sense
  and carries the law, with no quotient. The readings are the AI's.
"""

SCOPE = (
    '    "Identification: a course with period p + 1 coming back after Q steps at its first p steps comes "\n'
    '    "back after Q steps at every step, and two lassos agreeing before (i + q + 1) + (i\' + q\') agree "\n'
    '    "everywhere; a history has at most N states exactly where it is a lasso within N, histories with "\n'
    '    "at most N and N\' states agreeing before N + N\' - 1 agree everywhere, records are equal exactly "\n'
    '    "where courses agree before their length, and for N = 1 and for N = N\' two such histories share "\n'
    '    "their record before N + N\' - 2 and differ there; on a history with at most N states a lasso "\n'
    '    "within N holding before 2N - 1 holds everywhere, the learner that knows N is refuted nowhere and "\n'
    '    "right from 2N - 1 on, no learner refuted nowhere claims at 2N - 2 on every such history, the "\n'
    '    "learner that knows two states is right about the denial from step 3, and the course answering "\n'
    '    "the learner that knows N has more than N states; on a history with at most N states a lasso "\n'
    '    "hypothesis (a, b) within N unrefuted for N + N - 1 steps from s >= a is unrefuted from s on, and the "\n'
    '    "learner by "\n'
    '    "refutation over the lasso hypotheses claims and is right at every step from N + (N + N - 1) * tri N "\n'
    '    "on, in a world a list of length N holds too; under a determined law on a list closed under "\n'
    '    "it, the same registered future is agreement for 2N - 1 steps, and naming by that finite future "\n'
    '    "makes sense, carries the law and decides likeness. "\n')

if STAGE == 'core':
    root = B / 'Becoming.lean'
    edit(root, [('import Becoming.Description\n', 'import Becoming.Description\nimport Becoming.Identification\n')])
    s = root.read_text()
    start = s.index('* `Becoming.Description` (')
    nxt = s.index('\n* `Becoming.', start) + 1
    root.write_text(s[:nxt] + BULLET + s[nxt:])
    checker = B / 'check_becoming.py'
    edit(checker, [('"Becoming.Description"', '"Becoming.Description", "Becoming.Identification"')])
    s = checker.read_text()
    start = s.index('    "Description: ')
    nxt = re.compile(r'\n    "[A-Z][A-Za-z]*: ').search(s, start + 1).start() + 1
    checker.write_text(s[:nxt] + SCOPE + s[nxt:])
    print('inserted the Identification bullet and scope sentence after Description')
else:
    ROW = (f'| {LAYER} | [`Becoming.Identification`](Becoming/Identification.lean) | 辨识（除了界不加前提，P83）：两个周期（Fine–Wilf，'
           '`period_extends`）；至多 N 与 N′ 个状态的历史由长 N + N′ − 1 的记录确定（`bounded_agree`），在 N = 1 与 N = N′ 时恰好'
           '（`record_short`、`record_short_twice`）；界给定时归纳即演绎（`bounded_induction`），知道界的学习者从 2N − 1 起每步都对，不能更早'
           '（`knowing_right`、`knowing_earliest`）；回答它的世界超出界（`answer_exceeds_bound`）；不知道界的学习者从 N + (2N − 1)·tri N 起每步都对'
           '（`learner_rests`、`held_learner_rests`）；以有限的所识的未来命名有意义，不用商'
           '（`Law.name_makesSense`） / identification: a bounded record fixes the course at an exact length; where the bound '
           'is given induction is deduction and the learner that knows it is right from 2N − 1 on, none sooner, the one that '
           'does not know it from N + (2N − 1)·tri N on; finite '
           'names for the split that makes sense |')
    readme = B / 'README.md'
    s = readme.read_text()
    for old, new in (('`Description` 导入 `Unfolding`、`Diagonal`、`Context`',
                      '`Identification` 导入 `Description`；`Description` 导入 `Unfolding`、`Diagonal`、`Context`'),
                     ('`Description` imports `Unfolding`, `Diagonal`, `Context`',
                      '`Identification` imports `Description`; `Description` imports `Unfolding`, `Diagonal`, `Context`')):
        assert s.count(old) == 1, (old, s.count(old))
        s = s.replace(old, new)
    at = s.index('[`Becoming.Description`]')
    j = s.index('\n', at) + 1
    s = s[:j] + ROW + '\n' + s[j:]
    readme.write_text(s)
    print('inserted the README row')
