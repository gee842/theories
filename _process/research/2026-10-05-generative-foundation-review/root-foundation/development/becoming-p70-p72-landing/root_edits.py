#!/usr/bin/env python3
"""Add P70–P72's modules (with P72q's) to the root module, the checker and the Lean README.

Usage: python3 -B root_edits.py ROOT core      (after copying the modules, before the landing run)
       python3 -B root_edits.py ROOT readmes   (after both receipts pass)

`core` adds the imports and docstring bullets of `Becoming.Diagonal`, `Becoming.Context`,
`Becoming.Quantum` (L2) and `Becoming.Description` to `Becoming.lean`, and the modules with their
scope sentences to `CORE` and `SCOPE` in `check_becoming.py`. `readmes` adds the spine rows and the
import notes to `becoming/README.md`. Whether `Becoming.Description` imports `Becoming.Learning`
(P73 landed first and lean/learning_patch.py was applied) is read from the copied module: then it
is L4 and goes after Learning, otherwise L3 after P69's Unfolding. Every anchor must occur exactly
once; rerunning on an edited checkout fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
STAGE = sys.argv[2]
assert STAGE in {'core', 'readmes'}, STAGE
B = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEARNING = 'import Becoming.Learning' in (B / 'Becoming/Description.lean').read_text()
LAYER = 'L4' if LEARNING else 'L3'
AFTER = 'Learning' if LEARNING else 'Unfolding'
print('Description imports Learning:', LEARNING)


def edit(path, pairs):
    s = path.read_text()
    for anchor, new in pairs:
        assert s.count(anchor) == 1, (path.name, anchor[:80], s.count(anchor))
        s = s.replace(anchor, new)
    path.write_text(s)
    print('edited', path.relative_to(ROOT))


BULLETS_L2 = """* `Becoming.Diagonal` (L2): a registration within what it registers (P71), with no premise. A
  family indexed by what it reads misses the gap of any map moving every value (Lawvere's
  diagonal); no family of claims is complete, and no frame realizes with its own configurations
  every claim about them; for values compared by equality, a registration within what it
  registers is complete exactly where nothing differs, and a complete one has fixed points.
  Completing is an unfolding, incomplete at every step, its gaps pairwise different, never
  returning and held by no finite stock, and one exists; revision by a map moving every value
  never rests, and the two-valued denial returns every two steps. The readings are the AI's.
* `Becoming.Context` (L2): contextual registration (P72), with no premise. Registrations in
  contexts glue exactly where contexts agree where they meet; a frame of context-free claims fits
  exactly where they glue at every configuration, and the frame indexed by context always fits,
  so context-free claims are a commitment of the representation; with local possibilities and no
  context-free reading no configuration respecting them glues, and where some context allows
  something they are the parts of no whole. Specker's three boxes and the Mermin–Peres square are
  witnesses. The readings are the AI's.
* `Becoming.Quantum` (L2): the quantum realization of the Mermin–Peres square (P72q, written and
  checked by the owner of P64–P68). The nine two-qubit observables as integer matrices square to
  the identity, commute along each line, and multiply to minus the identity along the third
  column and to the identity along every other line; the values a nonzero vector shows jointly on
  a line are a possibility of the line, and every possibility is shown, so no context-free
  assignment is shown jointly on every line.
"""

BULLET_DESCRIPTION = f"""* `Becoming.Description` ({LAYER}): what a description keeps and loses (P70), with no premise.
  Describing the parts separately gives back the whole exactly where it is rectangular, the lost
  relation reappearing as surplus; three parts can be related as a whole while every two are free,
  and on Specker's pairs the pairs do not give the parity back; a relation forms only by joint
  action, lasts under laws moving each part by itself and merging nothing that occurs, and ends
  only by loss or joint action. Under a determined law the coarsest split keeping what is
  registered and carrying a law makes sense; what is registered now makes sense exactly where it
  carries a law, and a part alone exactly where the rest makes no difference to its next value, a
  controller's rule included; position and velocity are a pair. States are read off a registered
  history: beyond the succession of steps every registered history is a determined law, with
  finitely many states exactly where its registration repeats from some moment on.""" + (
    """ The same
  law as `Learning.goAlike_iff_lumped` is its instance here, and finitely many states is P73's
  lasso.""" if LEARNING else '') + """ The readings are the AI's; Ren asked for the pair to be dug
  deeper and agreed with the reply that followed.
"""

SCOPE_L2 = (
    '    "Diagonal: a family of registrations indexed by what it reads says no gap of a map moving every "\n'
    '    "value, and one saying every reading gives every map a value alike with its image; a claim is "\n'
    '    "never alike with its negation, so no family of claims says every reading and no frame realizes "\n'
    '    "every pattern of claims about its own configurations; with equality of values decidable, "\n'
    '    "completeness is exactly all values being equal; a registration keeping what it says and next "\n'
    '    "saying its gap is incomplete at every step, says no later gap earlier, has no two gaps alike "\n'
    '    "where likeness is transitive, never returns, and holds its gaps in no finite stock where "\n'
    '    "likeness is symmetric and transitive, and such an unfolding exists on Bool; revision by a map "\n'
    '    "moving every value never rests, and the two-valued denial returns every two steps. "\n'
    '    "Context: registrations in contexts glue at a configuration exactly where any two contexts "\n'
    '    "registering a claim agree, each claim having a context; a frame of context-free claims fits "\n'
    '    "exactly where they glue at every configuration, while the frame indexed by context always fits; "\n'
    '    "where possibilities are local and admit no context-free reading no respecting configuration "\n'
    '    "glues, and no frame of context-free claims fits a world with one respecting configuration; a "\n'
    '    "whole lies within what its restrictions glue to, restrictions are local, and possibilities with "\n'
    '    "no context-free reading, where some context allows something, are the restrictions of no whole; "\n'
    '    "Specker\'s three boxes and the Mermin-Peres square admit no context-free reading, no context "\n'
    '    "forcing a claim. "\n'
    '    "Quantum: the nine two-qubit observables of the Mermin-Peres square, as integer matrices, each "\n'
    '    "square to the identity, commute along each line and anticommute off it, and multiply along a "\n'
    '    "line to minus the identity in the third column and to the identity otherwise; the values a "\n'
    '    "nonzero vector shows jointly on a line have the line\'s parity and are a possibility of the "\n'
    '    "line, every possibility is shown by an explicit vector, and no assignment to the nine cells is "\n'
    '    "shown jointly on every line. "\n')

SCOPE_DESCRIPTION = (
    '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n'
    '    "is rectangular, and two parts that always go alike can go apart; three parts can be related "\n'
    '    "while every two are free, and on Specker\'s pairs every reading is allowed by every pair while "\n'
    '    "the pairs do not give the whole back; a law moving each part by itself keeps a whole "\n'
    '    "rectangular, copying relates, a relation lasts under laws merging nothing that occurs and ends "\n'
    '    "by forgetting or by a coupling acting again; under a determined law read through a "\n'
    '    "registration, a split keeping what is registered and going alike relates configurations by a "\n'
    '    "bisimulation and the coarsest one makes sense, what is registered now makes sense exactly where "\n'
    '    "it goes alike with the law, a registered part alone exactly where the rest makes no difference "\n'
    '    "to its next value, and for a rule changing with it exactly where the rule makes none; "\n'
    '    "registering position under motion the pair makes sense and neither alone; moments of a "\n'
    '    "registered sequence are one state where all registered after them is alike, which is likeness "\n'
    '    "under the law of moments, and there are finitely many states exactly where two moments are one "\n'
    '    "state, by a pigeonhole up to a relation with no decision; a returning configuration has finitely "\n'
    '    "many states under every registration, and the two-valued denial has exactly two"\n' + (
    '    "; going alike under a determined law is Learning\'s lumping, and a lasso is two moments being "\n'
    '    "one state, so finitely many states is a lasso"\n' if LEARNING else '') +
    '    ". "\n')

if STAGE == 'core':
    root = B / 'Becoming.lean'
    edit(root, [
        ('import Becoming.Recurrence\n', 'import Becoming.Recurrence\nimport Becoming.Diagonal\nimport Becoming.Context\n'
                                         'import Becoming.Quantum\n'),
        (f'import Becoming.{AFTER}\n', f'import Becoming.{AFTER}\nimport Becoming.Description\n'),
        ('* `Becoming.Renewal` (L3)', BULLETS_L2 + '* `Becoming.Renewal` (L3)'),
    ])
    # The Description bullet goes after its predecessor's bullet, before the next bullet.
    s = root.read_text()
    start = s.index(f'* `Becoming.{AFTER}` (')
    nxt = s.index('\n* `Becoming.', start) + 1
    root.write_text(s[:nxt] + BULLET_DESCRIPTION + s[nxt:])
    checker = B / 'check_becoming.py'
    edit(checker, [
        ('"Becoming.Recurrence", ', '"Becoming.Recurrence", "Becoming.Diagonal", "Becoming.Context", "Becoming.Quantum", '),
        (f'"Becoming.{AFTER}"', f'"Becoming.{AFTER}", "Becoming.Description"'),
        ('    "Renewal: a run read through observables', SCOPE_L2 + '    "Renewal: a run read through observables'),
    ])
    s = checker.read_text()
    start = s.index(f'    "{AFTER}: ')
    nxt = re.compile(r'\n    "[A-Z][A-Za-z]*: ').search(s, start + 1).start() + 1
    checker.write_text(s[:nxt] + SCOPE_DESCRIPTION + s[nxt:])
    print('inserted the Description bullet and scope sentence after', AFTER)
else:
    ROWS_L2 = '\n'.join([
        '| L2 | [`Becoming.Diagonal`](Becoming/Diagonal.lean) | 在所识之中的识（不加前提，P71）：以所读者为索引的族漏掉移动每个值之映射的缺口（Lawvere 的对角线，'
        '`gap_unsaid`），主张族从不完备，框架不以自己的配置实现每种关于配置的主张（`Frame.self_incomplete`）；以相等比较的值，完备恰在没有差别处'
        '（`complete_iff_alike`）；补全的展开每一步不完备，从不返回，没有有限储存持有（`Unfolds.never_returns`、`Unfolds.unheld`）；修正从不静止，'
        '二值的否定每两步返回 / a registration within what it registers: a family indexed by what it reads misses the gap '
        'of any map moving every value; completeness exactly where nothing differs; completing is an unfolding that never '
        'returns and is held by no finite stock; the liar as a rhythm |',
        '| L2 | [`Becoming.Context`](Becoming/Context.lean) | 语境中的识（不加前提，P72）：诸识粘合恰当语境在相交处一致（`Contextual.glues_iff_agree`），'
        '不依语境的主张的框架恰在处处粘合时合，以语境为索引的框架总合（`Contextual.fitsFree_iff`、`Contextual.indexed_fits`）；没有不依语境的读法、'
        '某个语境允许某物的可能性不是任何整体的部分（`no_whole`）；Specker 的三个盒子与 Mermin–Peres 方阵 / contextual registration: a '
        'frame of context-free claims fits exactly where the registrations glue, the indexed frame always; possibilities '
        'with no context-free reading are the parts of no whole; Specker\'s boxes and the Mermin–Peres square |',
        '| L2 | [`Becoming.Quantum`](Becoming/Quantum.lean) | Mermin–Peres 方阵的量子实现（P72q，由 P64–P68 的所有者写成）：两个量子比特上九个可观测量'
        '作为整数矩阵，平方为 I，每条线两两对易，线的乘积在第三列为 −I（`line_product`）；态在一条线上共同显示的值是该线的一个可能，每个可能都被显示，'
        '所以没有不依语境的值（`no_context_free_values`） / the quantum realization of the square: nine two-qubit observables, '
        'their line products, and no context-free values |',
    ])
    ROW_DESCRIPTION = (
        f'| {LAYER} | [`Becoming.Description`](Becoming/Description.lean) | 描述保留什么、失去什么（不加前提，P70）：分离恰在整体为矩形处给回整体，'
        '失去的是关系（`separation_faithful_iff`）；关系只由共同作用形成，在各自不合并的律下持续，只由失去或共同作用结束（`relation_persists`）；'
        '确定的律下保留所识并承载规律的最粗切分有意义（`Law.makesSense_of_law`），部分单独有意义恰当其余对它的下一值不造成差别'
        '（`Law.part_makesSense_iff_step`）；状态从所识的历史读出，状态有限恰当所识从某一刻起重复（`finitely_many_states_iff`'
        + ('、`finitely_many_states_iff_lasso`' if LEARNING else '') +
        '） / what a description keeps and loses: separation loses exactly the relation; a relation forms, lasts and ends '
        'in the joint law; the split that makes sense; states read off a registered history, finitely many exactly where '
        'it repeats from some moment on |')
    readme = B / 'README.md'
    imports_zh = '`Description` 导入 `Unfolding`、`Diagonal`、`Context`' + (' 与 `Learning`' if LEARNING else '')
    imports_en = '`Description` imports `Unfolding`, `Diagonal`, `Context`' + (' and `Learning`' if LEARNING else '')
    edit(readme, [
        ('每层只导入它下面的层（L3 内：', '每层只导入它下面的层（L2 内：`Becoming.Diagonal` 导入 `Becoming.Recurrence`，`Context` 导入 '
                                  '`Becoming.Frame`，`Quantum` 导入 `Context`；L3 内：'),
        ('Each layer imports only those below it (within L3, ',
         'Each layer imports only those below it (within L2, `Becoming.Diagonal` imports `Becoming.Recurrence`, `Context` '
         'imports `Becoming.Frame` and `Quantum` imports `Context`; within L3, '),
        *([('`Learning` 导入 `Mechanism` 与 `Selection`；', '`Learning` 导入 `Mechanism` 与 `Selection`；' + imports_zh + '；'),
           ('`Learning` imports `Mechanism` and `Selection`;', '`Learning` imports `Mechanism` and `Selection`; ' + imports_en + ';')]
          if LEARNING else
          [('。L4 内：', '；' + imports_zh + '。L4 内：'), ('; within L4, ', '; ' + imports_en + '; within L4, ')]),
    ])
    s = readme.read_text()
    at = s.index('| L2 | [`Becoming.Recurrence`]')
    j = s.index('\n', at) + 1
    s = s[:j] + ROWS_L2 + '\n' + s[j:]
    at = s.index(f'[`Becoming.{AFTER}`]')
    j = s.index('\n', at) + 1
    s = s[:j] + ROW_DESCRIPTION + '\n' + s[j:]
    readme.write_text(s)
    print('inserted the README rows')
