#!/usr/bin/env python3
"""P120: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

The module bullet, the table rows, the paragraphs, the summaries and the glossary rows are read from
docs.json (written by make_docs_json.py). Each change asserts the text it replaces, so a second run
fails instead of applying twice. New lines go after Loops': the root's import and module bullet, the
core list, the checker's scope entry, the Lean README's L4 row and within-layer imports, and the
chapter's L4 row, so modules landing before this one leave the anchors in place.

Chapter edits: §2, the paragraph "How a carried difference grows" no longer lists couplings that come
and go as not derived and points to `Becoming.Remainder`, and a paragraph "What a cut loses" follows
it; "Part I stated whole", one item after how a carried difference grows; §8, the status row of the
response as the dynamics give (the loops on couplings that come and go leave the open items; whether
every schedule settles, and whether every loop of recurring couplings makes the most difference that
can arrive run away, join them) and the further proofs under feedback and reach (couplings that come
and go are given); §9, one L4 row; the glossary, three rows after "loop (of couplings)".
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
GROWS = '../results/records/how-a-carried-difference-grows.md'
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
t = once(t, '\nimport Becoming.Loops\n', '\nimport Becoming.Loops\nimport Becoming.Remainder\n')
last = ('  step, a finite order is exact, and the most difference that can arrive is bounded by a\n'
        '  polynomial, exactly where no loop lies upstream.\n')
t = once(t, last, last + docs['bullet'] + '\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Loops", ', '"Becoming.Loops", "Becoming.Remainder", ')
t = once(t, '    "a polynomial exactly where no loop lies upstream. "\n',
         '    "a polynomial exactly where no loop lies upstream. "\n' + docs['scope'])
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Loops`]', docs['readme_row'])
t = once(t, '；`Loops` 导入 `Propagation`）', '；`Loops` 导入 `Propagation`；`Remainder` 导入 `Loops`）')
t = once(t, '; `Loops` imports `Propagation`)', '; `Loops` imports `Propagation`; `Remainder` imports `Loops`)')
out[path] = t

t = CHAPTER.read_text()
# §2: the paragraph on how a carried difference grows no longer lists couplings that come and go as not derived
t = once(t, '强度本身、时有时无的耦合、比强度之积更细的失控速度、无穷多条件、连续时间与实数的量都不推出。',
         '强度本身、比强度之积更细的失控速度、无穷多条件、连续时间与实数的量都不推出；时有时无的耦合见 `Becoming.Remainder`。')
t = once(t, 'The strengths themselves, couplings that come and go, how fast a runaway is beyond the product of the '
            'strengths, infinitely many conditions, continuous time and real amounts are not derived.',
         'The strengths themselves, how fast a runaway is beyond the product of the strengths, infinitely many '
         'conditions, continuous time and real amounts are not derived; couplings that come and go are treated in '
         '`Becoming.Remainder`.')
# §2: a paragraph after it
t = after_line(t, '**How a carried difference grows (Part I).**', '', docs['paragraph_zh'], '', docs['paragraph_en'])
# Part I stated whole
t = after_line(t, '- **所携带的差别怎样增长。**', docs['whole_zh'])
t = after_line(t, '- **How a carried difference grows.**', docs['whole_en'])
# §8 status row of the response as the dynamics give; the row's last clause is left as it stands
t = once(t, f'（[how-a-carried-difference-grows]({GROWS})）。开放：律本身；反例之存在的确切强度；时有时无的耦合上的回路',
         f'（[how-a-carried-difference-grows]({GROWS})）' + docs['status_zh'] + '。' + docs['open_zh'])
# §8 further proofs under feedback and reach
t = once(t, '；时有时无的耦合上的回路，比强度之积更细的失控速度。', docs['further_zh'])
t = once(t, '; loops whose couplings come and go, and how fast a runaway is beyond the product of the strengths.',
         docs['further_en'])
# §9: one L4 row after Loops'
t = after_line(t, '| L4 | [Becoming.Loops]', docs['chapter_row'])
# glossary
t = after_line(t, '| 回路（耦合的） | loop (of couplings) |', *docs['glossary'])
out[CHAPTER] = t
for path, text in out.items():
    path.write_text(text)
print('root, checker, Lean README and chapter updated')
