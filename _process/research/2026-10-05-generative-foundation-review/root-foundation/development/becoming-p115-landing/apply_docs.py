#!/usr/bin/env python3
"""P115: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

The module bullet, the table rows, the paragraphs, the summaries and the glossary rows are read from
docs.json (written by make_docs_json.py). Each change asserts the text it replaces, so a second run
fails instead of applying twice. New lines go at the end of the root's imports, the core list, the
Lean README's L4 rows and within-layer imports and the chapter's L4 rows, so modules landing
before this one (such as P116's) leave the anchors in place. The checker's scope text gains an
entry after Counterfactual's.

Chapter edits: §2, the paragraph of the comparison where the rest responds (its "not derived" now
points to `Becoming.Propagation` for how much difference arrives) and a paragraph "How much
difference arrives" after that of the response as the dynamics give; §6.10, the sentence that a
common condition does not measure coupling gains what measures it; "Part I stated whole", one item
after the response as the dynamics give; §8, the status row of the response as the dynamics give
and the further proofs under feedback and reach (how much difference arrives and a measure of
coupling are given; a general theory of loops stays open); §9, one L4 row; the glossary, rows
"coupling strength" and "carried amount".
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = Path(sys.argv[1]).resolve()
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECORD = '../results/records/how-much-difference-arrives.md'
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


def after_last(text, prefix, *new):
    lines = text.split('\n')
    hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert hits, prefix
    lines[hits[-1] + 1:hits[-1] + 1] = list(new)
    return '\n'.join(lines)


SCOPE = (
    '    "Propagation: in two balanced flows the difference of a condition\'s levels changes across a "\n'
    '    "step by exactly the difference given less the difference taken, so its gap is at most its gap "\n'
    '    "before with the gaps of every exchange with it; an exchange is coupled to a level with strength "\n'
    '    "at most k where, under two histories differing in that level only, it differs by at most k "\n'
    '    "times that level\'s gap; for a law of what has stood strength zero is insensitivity, strengths "\n'
    '    "add up over levels changed one at a time and bound a part\'s share of a move, and a law giving "\n'
    '    "the square of a level has no finite strength; where the rest follows such a law every gap is "\n'
    '    "at most the carried amount, the course of the carrying law from the starting gaps and the "\n'
    '    "part\'s gaps, which has those strengths and attains it, so the carried amount is the most "\n'
    '    "difference that can arrive; it is positive exactly along a route in time of positive "\n'
    '    "strengths, a route of TimedResponse\'s spread where the strengths are registered, and where no "\n'
    '    "route reaches the levels agree; carried amounts add and grow with the gaps and strengths; a "\n'
    '    "unit relayed at twice its level arrives as 2t by step t + 1, and a loop of strength one gives "\n'
    '    "2^t. "\n')


def after_containing(text, part, *new):
    lines = text.split('\n')
    hits = [i for i, l in enumerate(lines) if part in l]
    assert len(hits) == 1, (part, len(hits))
    lines[hits[0] + 1:hits[0] + 1] = list(new)
    return '\n'.join(lines)


path = L / 'Becoming.lean'
t = path.read_text()
t = once(t, '\n\n/-!\n# The Theory of Becoming: the formal core',
         '\nimport Becoming.Propagation\n\n/-!\n# The Theory of Becoming: the formal core')
t = once(t, '\n\nThe core imports nothing else, every source declaration has an empty axiom report, and\n',
         '\n' + docs['bullet'] + '\n\nThe core imports nothing else, every source declaration has an empty axiom report, and\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Relevance", "Becoming"]', '"Becoming.Propagation", "Becoming.Relevance", "Becoming"]')
t = once(t, '    "closed process is the course. "\n    "Selection: ',
         '    "closed process is the course. "\n' + SCOPE + '    "Selection: ')
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_last(t, '| L4 | [`Becoming.', docs['readme_row'])
t = once(t, '）。L1–L3 不含伦理谓词', '；`Propagation` 导入 `Counterfactual` 与 `TimedResponse`）。L1–L3 不含伦理谓词')
t = once(t, '). L1–L3 contain no ethical predicate',
         '; `Propagation` imports `Counterfactual` and `TimedResponse`). L1–L3 contain no ethical predicate')
out[path] = t

t = CHAPTER.read_text()
# §2: the comparison where the rest responds no longer leaves how much difference arrives underived
t = once(t, '形成只经其识回应、怎样回应、差别到达多少，都不推出。',
         '形成只经其识回应、怎样回应，都不推出；差别到达多少，在其余遵从具有给定耦合强度之律处由 `Becoming.Propagation` 回答。')
t = once(t, 'That formations respond only through their registration, how they respond and how much difference arrives are '
            'not derived.',
         'That formations respond only through their registration and how they respond are not derived; how much difference '
         'arrives is answered in `Becoming.Propagation` where the rest follows a law with given coupling strengths.')
# §2: a paragraph after that of the response as the dynamics give
t = after_containing(t, "exactly where it is formed through the part's configuration.",
                     '', docs['paragraph_zh'], '', docs['paragraph_en'])
# §6.10: what measures coupling
t = once(t, '那个条件是一个共同条件，不度量耦合。',
         '那个条件是一个共同条件，不度量耦合。耦合强度度量它（`Becoming.Propagation`）：一个整体有多纠缠，读作其交换与彼此的水平耦合'
         '有多强，所携带的量读作一个动作的差别在其中能多远、多快地增长（读法是 AI 的）。')
t = once(t, 'That condition is one common condition; it does not measure coupling.',
         'That condition is one common condition; it does not measure coupling. The coupling strengths measure it '
         '(`Becoming.Propagation`): how entangled a whole is reads as how strongly its exchanges are coupled to each other\'s '
         'levels, and the carried amount as how far and how fast an act\'s difference can grow in it (the reading is the '
         'AI\'s).')
# Part I stated whole
t = after_line(t, '- **回应由动力学给出。**', docs['whole_zh'])
t = after_line(t, '- **The response as the dynamics give.**', docs['whole_en'])
# §8 status row of the response as the dynamics give
t = once(t,
         '、[sensitivity-is-the-least-registration](../results/records/sensitivity-is-the-least-registration.md)）。'
         '开放：律本身；反例之存在的确切强度；差别到达多少；读法待 Ren |',
         '、[sensitivity-is-the-least-registration](../results/records/sensitivity-is-the-least-registration.md)）；'
         '差别到达多少至多是耦合强度所携带的量，所携带的量恰好达到，是能到达的最大差别，恰沿正强度的时间路线为正'
         f'（[how-much-difference-arrives]({RECORD})）。开放：律本身；反例之存在的确切强度；回路的一般理论；读法待 Ren |')
# §8 further proofs under feedback and reach
t = once(t,
         '；中心怎样表示其所及闭包；按步、按时间先后的影响闭包与所及闭包（比较已按时间先后，`Flow.ReachesBefore`）；耦合的度量。',
         '；差别到达多少与耦合的度量已给出（`Becoming.Propagation`：耦合强度度量敏感，强度为零恰是不敏感；所携带的量是能到达的最大差别，'
         '恰好达到，恰沿正强度的时间路线为正）；中心怎样表示其所及闭包；按步、按时间先后的影响闭包与所及闭包（比较已按时间先后，'
         '`Flow.ReachesBefore`；差别的时间路线，`carried_pos_iff`）；回路的一般理论（绕回路的强度与失控，`Becoming.Propagation` 只给见证）。')
t = once(t,
         '; how a center represents its reach closure; influence and reach closures step by step and in temporal order (the '
         'comparison is already ordered in time, `Flow.ReachesBefore`); a measure of coupling.',
         '; how much difference arrives and a measure of coupling are given (`Becoming.Propagation`: the coupling strengths '
         'measure sensitivity, strength zero being insensitivity; the carried amount is the most difference that can arrive, '
         'attained, and positive exactly along a route in time of positive strengths); how a center represents its reach '
         'closure; influence and reach closures step by step and in temporal order (the comparison is already ordered in '
         'time, `Flow.ReachesBefore`; a difference\'s routes in time, `carried_pos_iff`); a general theory of loops (the '
         'strength around a loop and its runaway, of which `Becoming.Propagation` gives witnesses only).')
# §9: one L4 row after the last
t = after_last(t, '| L4 | [Becoming.', docs['chapter_row'])
# glossary
t = after_line(t, '| 读有限多个条件 | reads finitely many conditions |', docs['glossary_strength'], docs['glossary_carried'])
out[CHAPTER] = t
for path, text in out.items():
    path.write_text(text)
print('root, checker, Lean README and chapter updated')
