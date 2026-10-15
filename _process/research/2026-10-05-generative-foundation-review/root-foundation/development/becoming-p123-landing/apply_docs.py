#!/usr/bin/env python3
"""P123: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

The module bullet, the table rows, the paragraphs, the summaries and the glossary rows are read from
docs.json (written by make_docs_json.py). Each change asserts the text it replaces, so a second run
fails instead of applying twice. New lines go after those of `Becoming.Thresholds` (P124), the module
landed just before this one: the root's import and module bullet, the core list, the checker's scope
entry, the Lean README's L4 row and within-layer imports, and the chapter's L4 row.

Chapter edits: §2, the paragraph "What a cut loses" gains a dated parenthetical saying which three of
the items it lists as not derived `Becoming.Frequency` answers (P120's readings, pending Ren, are left
as they stand), and a paragraph pair "How often couplings act" follows the paragraphs on loops within
what a law reads; "Part I stated whole", one item after loops within what a law reads; §8, the status
row of the response as the dynamics give (whether every schedule settles, and whether every loop of
recurring couplings makes the most difference that can arrive run away, leave the open items; how fast
a runaway of given strengths is joins them) and the further proofs under feedback and reach (how often
couplings act is given, after loops within what a law reads; how a formation comes to observe a stock
it depends on is left as it stands); §9, one L4 row; the glossary, three rows after "break (of a stock
read only below a threshold)".
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CUT = '../results/records/what-a-cut-loses.md'
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
t = once(t, '\nimport Becoming.Thresholds\n', '\nimport Becoming.Thresholds\nimport Becoming.Frequency\n')
last = '  stock, so the loop through the stock forms at the break, unforeseen.\n'
t = once(t, last, last + docs['bullet'] + '\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Thresholds", ', '"Becoming.Thresholds", "Becoming.Frequency", ')
last = '    "the break. "\n'
t = once(t, last, last + docs['scope'])
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Thresholds`]', docs['readme_row'])
t = once(t, '；`Thresholds` 导入 `Closing` 与 `Runaway`）', '；`Thresholds` 导入 `Closing` 与 `Runaway`；`Frequency` 导入 `Closing`）')
t = once(t, '; `Thresholds` imports `Closing` and `Runaway`)',
         '; `Thresholds` imports `Closing` and `Runaway`; `Frequency` imports `Closing`)')
out[path] = t

t = CHAPTER.read_text()
# §2: the paragraph on what a cut loses notes the three items Becoming.Frequency answers
t = once(t, f'连续时间与实数的量也不推出。见 [what-a-cut-loses]({CUT})。',
         f'连续时间与实数的量也不推出{docs["cut_zh"]}。见 [what-a-cut-loses]({CUT})。')
t = once(t, f'continuous time and real amounts. See [what-a-cut-loses]({CUT}).',
         f'continuous time and real amounts{docs["cut_en"]}. See [what-a-cut-loses]({CUT}).')
# §2: a paragraph pair after the paragraphs on loops within what a law reads
t = after_line(t, '**Loops within what a law reads, and the break (Part I).**', '', docs['paragraph_zh'], '',
               docs['paragraph_en'])
# Part I stated whole
t = after_line(t, '- **回路在律所读之内，与断裂。**', docs['whole_zh'])
t = after_line(t, '- **Loops within what a law reads, and the break.**', docs['whole_en'])
# §8 status row of the response as the dynamics give
t = once(t, f'（[what-a-cut-loses]({CUT})）。开放：律本身；反例之存在的确切强度；每个耦合时程是否终将安定；复现耦合的回路是否都使能到达'
            '的最大差别失控。',
         f'（[what-a-cut-loses]({CUT})）' + docs['status_zh'] + '。' + docs['open_zh'] + '。')
# §8 further proofs under feedback and reach
t = once(t, '断裂之前没有经过储量的回路）；', '断裂之前没有经过储量的回路）；' + docs['further_zh'])
t = once(t, '；每个时程是否终将安定，复现耦合的回路是否都使之失控，比强度之积更细的失控速度。', docs['further_tail_zh'])
t = once(t, 'with no loop through the stock before it); ',
         'with no loop through the stock before it); ' + docs['further_en'])
t = once(t, '; whether every schedule settles, whether every loop of recurring couplings makes a difference run away, '
            'and how fast a runaway is beyond the product of the strengths.', docs['further_tail_en'])
# §9: one L4 row after Thresholds'
t = after_line(t, '| L4 | [Becoming.Thresholds]', docs['chapter_row'])
# glossary
t = after_line(t, '| 断裂（只在低于阈值时才读的储量的） | break (of a stock read only below a threshold) |',
               *docs['glossary'])
out[CHAPTER] = t
for path, text in out.items():
    path.write_text(text)
print('root, checker, Lean README and chapter updated')
