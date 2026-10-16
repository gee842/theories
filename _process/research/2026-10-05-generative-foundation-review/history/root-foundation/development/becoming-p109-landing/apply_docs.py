#!/usr/bin/env python3
"""P109: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

The module bullet and the two table rows are read from docs.json. Each change asserts the text it
replaces, so a second run fails instead of applying twice.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
docs = json.loads((HERE / 'docs.json').read_text())


def once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)


def after_line(text, prefix, line):
    lines = text.split('\n')
    hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    lines.insert(hits[0] + 1, line)
    return '\n'.join(lines)


path = L / 'Becoming.lean'
t = path.read_text()
t = once(t, 'import Becoming.Readings\n', 'import Becoming.Readings\nimport Becoming.Coupling\n')
t = once(t, '\n\nThe core imports nothing else, every source declaration has an empty axiom report, and\n',
         '\n' + docs['bullet'] + '\nThe core imports nothing else, every source declaration has an empty axiom report, and\n')
path.write_text(t)

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Readings", "Becoming.Relevance", "Becoming"]',
         '"Becoming.Readings", "Becoming.Coupling", "Becoming.Relevance", "Becoming"]')
path.write_text(t)

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Readings`]', docs['readme_row'])
t = once(t, '）。L1–L3 不含伦理谓词', '；`Coupling` 导入 `Counterfactual` 与 `Readout`）。L1–L3 不含伦理谓词')
t = once(t, '). L1–L3 contain no ethical predicate', '; `Coupling` imports `Counterfactual` and `Readout`). L1–L3 contain no ethical predicate')
path.write_text(t)

t = CHAPTER.read_text()
t = after_line(t, '| L4 | [Becoming.Readings]', docs['chapter_row'])
t = once(t, '一个关系的起点：动作在展开之内形成的条件；',
         '一个关系的起点：动作在哪里形成已给出（`Becoming.Coupling`：部分的、其余的，或只是两者之关系的；无需从整体之外供给；'
         '一段进程的记录只在某个配置复现而动作不同之处固定动作是谁的）；')
t = once(t, 'One relational starting point: when a move is formed within the unfolding;',
         "One relational starting point: where a move is formed is given (`Becoming.Coupling`: the part's, the rest's, or "
         'only their relation\'s; no move needs supplying from outside the whole; the record of one course fixes whose move '
         'it is only where a configuration recurs with the move varied);')
t = once(t, '仍待 Ren：“行动不是展开之外的第二种原因”是否是 Ren 的读法；主张作为关系项的读法',
         '仍待 Ren：“行动不是展开之外的第二种原因”是否是 Ren 的读法，以及动作在哪里形成的读法（`Becoming.Coupling`：行与受是同一动作的'
         '两面，动作是谁的是关于未走之进程的主张）；主张作为关系项的读法')
t = once(t, "pending Ren: whether “an agent's choice is not a second kind of cause beside the unfolding” is Ren's reading; "
            'the reading of claims as relata',
         "pending Ren: whether “an agent's choice is not a second kind of cause beside the unfolding” is Ren's reading, and "
         'the readings of where a move is formed (`Becoming.Coupling`: acting and undergoing as one move read from its two '
         'sides, whose move it is as a claim about courses not taken); the reading of claims as relata')
CHAPTER.write_text(t)
print('root, checker, Lean README and chapter updated')
