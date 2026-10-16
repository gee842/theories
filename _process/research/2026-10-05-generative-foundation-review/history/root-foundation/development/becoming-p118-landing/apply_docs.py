#!/usr/bin/env python3
"""P118: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

The module bullet, the table rows, the paragraphs, the summaries and the glossary rows are read from
docs.json (written by make_docs_json.py). Each change asserts the text it replaces, so a second run
fails instead of applying twice. New lines go after Propagation's: the root's import and module
bullet, the core list, the checker's scope entry, the Lean README's L4 row and within-layer imports,
and the chapter's L4 row, so modules landing before this one leave the anchors in place.

Chapter edits: §2, Propagation's paragraph no longer lists a general theory of loops as not derived
and points to `Becoming.Loops`, and a paragraph "How a carried difference grows" follows it; "Part I
stated whole", one item after how much difference arrives; §8, the status row of the response as
the dynamics give (a general theory of loops leaves the open items, loops whose couplings come and
go join them) and the further proofs under feedback and reach (a general theory of loops is given);
§9, one L4 row; the glossary, rows "order (of the carried amount)" and "loop (of couplings)" after
"carried amount".
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
HOW_MUCH = '../results/records/how-much-difference-arrives.md'
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
t = once(t, '\nimport Becoming.Propagation\n', '\nimport Becoming.Propagation\nimport Becoming.Loops\n')
t = once(t, '  bound through a chain, and a loop of strength one doubles it every step.\n',
         '  bound through a chain, and a loop of strength one doubles it every step.\n' + docs['bullet'] + '\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Propagation", ', '"Becoming.Propagation", "Becoming.Loops", ')
t = once(t, '    "2^t. "\n', '    "2^t. "\n' + docs['scope'])
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Propagation`]', docs['readme_row'])
t = once(t, '；`Propagation` 导入 `Counterfactual` 与 `TimedResponse`）',
         '；`Propagation` 导入 `Counterfactual` 与 `TimedResponse`；`Loops` 导入 `Propagation`）')
t = once(t, '; `Propagation` imports `Counterfactual` and `TimedResponse`)',
         '; `Propagation` imports `Counterfactual` and `TimedResponse`; `Loops` imports `Propagation`)')
out[path] = t

t = CHAPTER.read_text()
# §2: Propagation's paragraph no longer lists a general theory of loops as not derived
t = once(t, '强度本身是给出的界，不陈述最小的强度；回路的一般理论、无穷多条件、连续时间与实数的量都不推出。',
         '强度本身是给出的界，不陈述最小的强度；无穷多条件、连续时间与实数的量都不推出；回路的一般理论见 `Becoming.Loops`。')
t = once(t, 'The strengths themselves are supplied bounds, and no least strength is stated; a general theory of loops, '
            'infinitely many conditions, continuous time and real amounts are not derived.',
         'The strengths themselves are supplied bounds, and no least strength is stated; infinitely many conditions, '
         'continuous time and real amounts are not derived; a general theory of loops is given in `Becoming.Loops`.')
# §2: a paragraph after Propagation's
t = after_line(t, '**How much difference arrives (Part I).**', '', docs['paragraph_zh'], '', docs['paragraph_en'])
# Part I stated whole
t = after_line(t, '- **差别到达多少。**', docs['whole_zh'])
t = after_line(t, '- **How much difference arrives.**', docs['whole_en'])
# §8 status row of the response as the dynamics give; the row's last clause, on its readings, is left as it stands
t = once(t, f'（[how-much-difference-arrives]({HOW_MUCH})）。开放：律本身；反例之存在的确切强度；回路的一般理论',
         f'（[how-much-difference-arrives]({HOW_MUCH})）' + docs['status_zh']
         + '。开放：律本身；反例之存在的确切强度；时有时无的耦合上的回路')
# §8 further proofs under feedback and reach
t = once(t, '；回路的一般理论（绕回路的强度与失控，`Becoming.Propagation` 只给见证）。', docs['further_zh'])
t = once(t, '; a general theory of loops (the strength around a loop and its runaway, of which `Becoming.Propagation` gives '
            'witnesses only).', docs['further_en'])
# §9: one L4 row after Propagation's
t = after_line(t, '| L4 | [Becoming.Propagation]', docs['chapter_row'])
# glossary
t = after_line(t, '| 所携带的量 | carried amount |', docs['glossary_order'], docs['glossary_loop'])
out[CHAPTER] = t
for path, text in out.items():
    path.write_text(text)
print('root, checker, Lean README and chapter updated')
