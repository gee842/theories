#!/usr/bin/env python3
"""P121 and P122: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

Runs on a tree where P120's texts are in place (its apply_docs.py), as the new entries go after
Remainder's. The module bullets, the scope entries, the table rows, the paragraphs, the summaries and
the glossary rows are read from docs.json (written by make_docs_json.py). Each change asserts the
text it replaces, so a second run fails instead of applying twice.

Chapter edits: §2, the paragraphs "The orders of a carried difference as a sum over histories" and
"How loops form within the unfolding" after "What a cut loses"; in "How a carried difference grows",
Ren's readings as decided on 16 October stay as they are, and one dated clause after each of the two
readings P121 and P122 answer says what now exists (the third reading awaits Ren's revision);
"Part I stated whole", two items after what a cut loses; §8, the further proofs under feedback and
reach (the orders as a sum over histories and how loops form are given; joining the formation of
loops with Becoming.Runaway's policies is open); §9, two L4 rows after Remainder's; the glossary, two
rows after "settled (schedule of couplings)".
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
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
t = once(t, '\nimport Becoming.Remainder\n', '\nimport Becoming.Remainder\nimport Becoming.Routes\nimport Becoming.Closing\n')
last = ('  where no loop of the couplings that go on lies upstream, with no listing of every condition, and\n'
        '  the most difference that can arrive grows faster than every polynomial only through such a loop.\n')
t = once(t, last, last + docs['bullet_routes'] + '\n' + docs['bullet_closing'] + '\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Remainder", ', '"Becoming.Remainder", "Becoming.Routes", "Becoming.Closing", ')
t = once(t, '    "polynomial; the results of Loops on exactness follow as instances. "\n',
         '    "polynomial; the results of Loops on exactness follow as instances. "\n'
         + docs['scope_routes'] + docs['scope_closing'])
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Remainder`]', docs['readme_routes'], docs['readme_closing'])
t = once(t, '；`Remainder` 导入 `Loops`）', '；`Remainder` 导入 `Loops`；`Routes` 导入 `Weighted` 与 `Loops`；`Closing` 导入 `Remainder`）')
t = once(t, '; `Remainder` imports `Loops`)',
         '; `Remainder` imports `Loops`; `Routes` imports `Weighted` and `Loops`; `Closing` imports `Remainder`)')
out[path] = t

t = CHAPTER.read_text()
# §2: Ren's readings in "How a carried difference grows" stay; a dated clause after each answered one
t = once(t, '`Loops.binom` 数回应的时间次序；两者尚未连起来。',
         '`Loops.binom` 数回应的时间次序；两者尚未连起来（2026-10-16 之后由 `Becoming.Routes` 接合：各阶是沿时间往回的路线之和，'
         '截断就是视界）。')
t = once(t, '`Loops.binom` counting their time orderings; the two are not yet joined.',
         '`Loops.binom` counting their time orderings; the two are not yet joined (after 16 October they are joined by '
         '`Becoming.Routes`: the orders are sums over routes back in time, and a cut is a truncation).')
t = once(t, '例如一个形成的汲取开始回应其汲取所降低的水平，那里与 `Becoming.Runaway` 相遇。',
         '例如一个形成的汲取开始回应其汲取所降低的水平，那里与 `Becoming.Runaway` 相遇（2026-10-16 之后，回路形成的定理是 '
         '`Becoming.Closing`：回路由闭合一条链的耦合而形成；这一读法待 Ren 再议）。')
t = once(t, "for example where a formation's drawing comes to respond to the level its drawing lowers, where this "
            'meets `Becoming.Runaway`.',
         "for example where a formation's drawing comes to respond to the level its drawing lowers, where this "
         'meets `Becoming.Runaway` (after 16 October the loop-formation theorem is `Becoming.Closing`: a loop forms '
         "through a coupling that closes a chain; this reading awaits Ren's revision).")
# §2: two paragraphs after "What a cut loses"
t = after_line(t, '**What a cut loses, for every schedule of couplings (Part I).**', '',
               docs['paragraph_routes_zh'], '', docs['paragraph_routes_en'], '',
               docs['paragraph_closing_zh'], '', docs['paragraph_closing_en'])
# Part I stated whole
t = after_line(t, '- **截断所失。**', docs['whole_routes_zh'], docs['whole_closing_zh'])
t = after_line(t, '- **What a cut loses.**', docs['whole_routes_en'], docs['whole_closing_en'])
# §8 further proofs under feedback and reach
t = once(t, '快于每个多项式只经由持续耦合的回路）；每个时程是否终将安定，',
         '快于每个多项式只经由持续耦合的回路）；各阶作为历史之和已给出（`Becoming.Routes`：沿时间往回的路线之和在视界 j + 1 上就是 '
         'j 阶，截断就是视界）；回路怎样形成已给出（`Becoming.Closing`：回路由闭合在形成之步作用的耦合而形成；形成之前增长至多是'
         '多项式，且不由至今的量显示；强度从进程读出时，回路的形成从展开读出）；在一个律中把回路的形成与 `Becoming.Runaway` 的策略'
         '连起来；每个时程是否终将安定，')
t = once(t, 'growth faster than every polynomial only through such a loop); whether every schedule settles, ',
         'growth faster than every polynomial only through such a loop); the orders as a sum over histories are given '
         '(`Becoming.Routes`: the sum over routes back in time at horizon j + 1 is order j, and a cut is a '
         'truncation); how loops form is given (`Becoming.Closing`: a loop forms through a coupling acting at the '
         'step of formation that closes a chain; before it forms growth is at most polynomial and is not shown by '
         'the amounts so far; with strengths read off the course, the formation of loops is read off the '
         "unfolding); joining the formation of loops and `Becoming.Runaway`'s policies within one law; whether "
         'every schedule settles, ')
# §9: two L4 rows after Remainder's
t = after_line(t, '| L4 | [Becoming.Remainder]', docs['chapter_row_routes'], docs['chapter_row_closing'])
# glossary
t = after_line(t, '| 安定（耦合时程的） |', docs['glossary_route'], docs['glossary_closing'])
out[CHAPTER] = t
for path, text in out.items():
    path.write_text(text)
print('root, checker, Lean README and chapter updated')
