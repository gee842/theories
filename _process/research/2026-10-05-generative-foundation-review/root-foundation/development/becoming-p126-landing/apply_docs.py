#!/usr/bin/env python3
"""P126: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

The module bullet, the scope entry, the table rows, the paragraphs, the summaries and the glossary
rows are read from docs.json (written by make_docs_json.py). Each change asserts the text it
replaces, so a second run fails instead of applying twice. `Becoming.Tail` extends
`Becoming.Sensitivity`, so its lines go after Sensitivity's: the root's import and module bullet,
the core list, the Lean README's L4 row and within-layer imports, and the chapter's L4 row. The
checker's scope entry goes after Frequency's, the last of the entries (Sensitivity has none).

Chapter edits: §2, the paragraph pair on the response as the dynamics give says, after its
sentence on `Becoming.Sensitivity`, where a counterexample exists, and a paragraph pair "What a law
of the whole and no part takes" follows it; "Part I stated whole", one item after the response as
the dynamics give; §8, the status row of the response as the dynamics give gains the result after
its clause on the least registration, and the exact strength leaves its open items; §8, the
further proofs under feedback and reach give the exact strength; §9, one L4 row; the glossary, two
rows after "reads finitely many conditions".
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SENS = '../results/records/sensitivity-is-the-least-registration.md'
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
t = once(t, '\nimport Becoming.Sensitivity\n', '\nimport Becoming.Sensitivity\nimport Becoming.Tail\n')
last = '  registration gives the weak limited principle of omniscience.\n'
t = once(t, last, last + docs['bullet'] + '\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Sensitivity", ', '"Becoming.Sensitivity", "Becoming.Tail", ')
last = '    "LPO; the loops of Loops and Closing are instances. "\n'
t = once(t, last, last + docs['scope'])
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Sensitivity`]', docs['readme_row'])
t = once(t, '；`Sensitivity` 导入 `Counterfactual`；', '；`Sensitivity` 导入 `Counterfactual`；`Tail` 导入 `Sensitivity`；')
t = once(t, '; `Sensitivity` imports `Counterfactual`; ',
         '; `Sensitivity` imports `Counterfactual`; `Tail` imports `Sensitivity`; ')
out[path] = t

t = CHAPTER.read_text()
# §2: the response as the dynamics give says where a counterexample exists
t = once(t, '而条件以自然数编号时每个反例都给出弱有限全知原则。何时一个动作是部分自己的',
         '而条件以自然数编号时每个反例都给出弱有限全知原则' + docs['response_zh'] + '。何时一个动作是部分自己的')
t = once(t, 'and with the conditions numbered every counterexample gives the weak limited principle of omniscience. '
            'When a move is the part\'s own',
         'and with the conditions numbered every counterexample gives the weak limited principle of omniscience'
         + docs['response_en'] + '. When a move is the part\'s own')
# §2: a paragraph pair after the paragraphs on the response as the dynamics give
t = after_line(t, '**The response as the dynamics give (Part I).**', '', docs['paragraph_zh'], '',
               docs['paragraph_en'])
# Part I stated whole
t = after_line(t, '- **回应由动力学给出。**', docs['whole_zh'])
t = after_line(t, '- **The response as the dynamics give.**', docs['whole_en'])
# §8 status row of the response as the dynamics give
t = once(t, f'[sensitivity-is-the-least-registration]({SENS})）；差别到达多少至多是耦合强度所携带的量',
         f'[sensitivity-is-the-least-registration]({SENS})）' + docs['status_zh'] + '；差别到达多少至多是耦合强度所携带的量')
t = once(t, '。开放：律本身；反例之存在的确切强度；给定强度的失控速度（谱半径）。', '。开放：律本身；给定强度的失控速度（谱半径）。')
# §8 further proofs under feedback and reach
t = once(t, '反例之存在的确切强度（在弱有限全知原则与消失之判定之间）；', docs['further_zh'])
t = once(t, 'the exact strength of the existence of a counterexample, between the weak limited principle of '
            'omniscience and the decision of vanishing; ', docs['further_en'])
# §9: one L4 row after Sensitivity's
t = after_line(t, '| L4 | [Becoming.Sensitivity]', docs['chapter_row'])
# glossary
t = after_line(t, '| 读有限多个条件 | reads finitely many conditions |', *docs['glossary'])
out[CHAPTER] = t
for path, text in out.items():
    path.write_text(text)
print('root, checker, Lean README and chapter updated')
