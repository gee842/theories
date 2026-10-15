#!/usr/bin/env python3
"""P127: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

The module bullet, the scope entry, the table rows, the paragraphs, the clauses and the glossary
rows are read from docs.json (written by make_docs_json.py). Each change asserts the text it
replaces, so a second run fails instead of applying twice. `Becoming.Onward` extends
`Becoming.Parting`, so its lines go after Parting's: the root's import and module bullet, the core
list, the Lean README's L4 row and within-layer imports, and the chapter's L4 row. The checker's
scope entry goes after Tail's, the last of the entries.

Chapter edits: §1, the paragraph pair on when the course branches says, in place of "not derived: a
run from every configuration that can move (a choice)", where a run goes on, and a paragraph pair
"Where a run goes on" follows it; "Part I stated whole", one item after the item on returning where
the course branches; §8, the status row of when the course branches gains the result; §8, the
further proofs under when the course branches give the run; §9, one L4 row; the glossary, two rows
after "run".
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
LIKE = '../results/records/determinacy-up-to-likeness.md'
docs = json.loads((HERE / 'docs.json').read_text())
out = {}


def once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)


def after_line(text, prefix, *new):
    lines = text.split('\n')
    hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    lines[hits[0] + 1:hits[0] + 1] = list(new)
    return '\n'.join(lines)


path = L / 'Becoming.lean'
t = path.read_text()
t = once(t, '\nimport Becoming.Parting\n', '\nimport Becoming.Parting\nimport Becoming.Onward\n')
last = '  decidability (`Lasting.Continues`).\n'
t = once(t, last, last + docs['bullet'] + '\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Parting", ', '"Becoming.Parting", "Becoming.Onward", ')
last = '    "which gives that rule and LPO. "\n'
t = once(t, last, last + docs['scope'])
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Parting`]', docs['readme_row'])
t = once(t, '；`Parting` 导入 `Distinguishing` 与 `Lasting`；',
         '；`Parting` 导入 `Distinguishing` 与 `Lasting`；`Onward` 导入 `Parting`；')
t = once(t, '; `Parting` imports `Distinguishing` and `Lasting`; ',
         '; `Parting` imports `Distinguishing` and `Lasting`; `Onward` imports `Parting`; ')
out[path] = t

t = CHAPTER.read_text()
# §1: when the course branches says where a run goes on
t = once(t, '读法是 AI 的，依 Ren 2026-10-15 的交托采用。不推出：从每个能动的配置出发的运行（选择）；在界内被吸入；分支路径上的度量。',
         '读法是 AI 的，依 Ren 2026-10-15 的交托采用。' + docs['branch_zh'] + '不推出：在界内被吸入；分支路径上的度量。')
t = once(t, 'Not derived: a run from every configuration that can move (a choice); being drawn in within a bound; a measure '
            'on branching courses.',
         docs['branch_en'] + 'Not derived: being drawn in within a bound; a measure on branching courses.')
# §1: a paragraph pair after the paragraphs on when the course branches
t = after_line(t, '**When the course branches (Part I).**', '', docs['paragraph_zh'], '', docs['paragraph_en'])
# Part I stated whole
t = after_line(t, '- 每个过程必然吸入的恰是不返回者，可能被吸入是在某一路径中失去自身；', docs['whole_zh'])
t = after_line(t, '- Every process necessarily draws exactly what does not return, and possibly drawn is losing oneself',
               docs['whole_en'])
# §8 status row of when the course branches
t = once(t, f'（[determinacy-up-to-likeness]({LIKE})）；读法依 Ren 2026-10-15 的交托采用；在界内被吸入与分支路径上的度量开放 |',
         f'（[determinacy-up-to-likeness]({LIKE})）' + docs['status_zh']
         + '；读法依 Ren 2026-10-15 的交托采用；在界内被吸入与分支路径上的度量开放 |')
# §8 further proofs under when the course branches
t = once(t, '从每个能动的配置出发的运行是否需要选择之外的条件；', docs['further_zh'])
t = once(t, 'whether a run from every configuration that can move needs more than a choice; ', docs['further_en'])
# §9: one L4 row after Parting's
t = after_line(t, '| L4 | [Becoming.Parting]', docs['chapter_row'])
# glossary
t = after_line(t, '| 运行 | run | 无穷的实际执行 | `Run` |', *docs['glossary'])
out[CHAPTER] = t
for path, text in out.items():
    path.write_text(text)
print('root, checker, Lean README and chapter updated')
