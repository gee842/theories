#!/usr/bin/env python3
"""P113: the root module, the checker's core list, the Lean README and the theory chapter.

usage: python3 -B apply_docs.py W

The module bullet, the two table rows and the two glossary rows are read from docs.json. Each
change asserts the text it replaces, so a second run fails instead of applying twice.

Chapter edits: the §9 row; in §8 the further proof "Feedback and reach" (the question is answered)
and the Ren's-choices item for §6.10 (the readings); the status row and the paragraph of the response
as the dynamics give, which named the question as not derived (the paragraph also still named when
a move is the part's own, which P109 answered; both now point to the module that answers them); the
summary in "Part I stated whole"; the logical commitment (a third place where a principle of
omniscience bounds what the core can state); the glossary row "sensitive" and a row "reads finitely
many conditions".
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
t = once(t, 'import Becoming.Coupling\n', 'import Becoming.Coupling\nimport Becoming.Sensitivity\n')
t = once(t, '\n\nThe core imports nothing else, every source declaration has an empty axiom report, and\n',
         '\n' + docs['bullet'] + '\nThe core imports nothing else, every source declaration has an empty axiom report, and\n')
path.write_text(t)

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Coupling", "Becoming.Relevance", "Becoming"]',
         '"Becoming.Coupling", "Becoming.Sensitivity", "Becoming.Relevance", "Becoming"]')
path.write_text(t)

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Coupling`]', docs['readme_row'])
t = once(t, '；`Coupling` 导入 `Counterfactual` 与 `Readout`）。',
         '；`Coupling` 导入 `Counterfactual` 与 `Readout`；`Sensitivity` 导入 `Counterfactual`）。')
t = once(t, '; `Coupling` imports `Counterfactual` and `Readout`).',
         '; `Coupling` imports `Counterfactual` and `Readout`; `Sensitivity` imports `Counterfactual`).')
path.write_text(t)

t = CHAPTER.read_text()
# §9: one L4 row after Becoming.Coupling
t = after_line(t, '| L4 | [Becoming.Coupling]', docs['chapter_row'])
# §8, further proofs: the question is answered
t = once(t,
         '- 反馈与所及：条件无穷多时，律的敏感是否仍是它所经的最小的识（回应由动力学给出的比较已陈述，`Becoming.Counterfactual`；'
         '经识回应时的限定，`Becoming.Response`）；',
         '- 反馈与所及：凡律在每个历史下读有限多个条件，条件任意多时它的敏感仍是它所经的最小的识已给出（`Becoming.Sensitivity`；'
         '条件无穷多时这一条件不能去掉：给定水平是否终将消失的判定，尾之律是反例，而条件以自然数编号时每个反例都给出弱有限全知原则；'
         '回应由动力学给出的比较已陈述，`Becoming.Counterfactual`；经识回应时的限定，`Becoming.Response`）；'
         '反例之存在的确切强度（在弱有限全知原则与消失之判定之间）；')
t = once(t,
         "- Feedback and reach: whether, with infinitely many conditions, a law's sensitivity is still the least registration it "
         'reads through (the comparison in which others respond as the dynamics give is stated, `Becoming.Counterfactual`; the '
         'confinement where the rest responds through registration, `Becoming.Response`); ',
         "- Feedback and reach: that, with any number of conditions, a law's sensitivity is still the least registration it reads "
         'through is given wherever the law reads finitely many conditions under each history (`Becoming.Sensitivity`; with '
         'infinitely many conditions this cannot be dropped: given a decision of whether levels vanish eventually, the tail law is '
         'a counterexample, and with the conditions numbered every counterexample gives the weak limited principle of omniscience; '
         'the comparison in which others respond as the dynamics give is stated, `Becoming.Counterfactual`; the confinement where '
         'the rest responds through registration, `Becoming.Response`); the exact strength of the existence of a counterexample, '
         'between the weak limited principle of omniscience and the decision of vanishing; ')
# §8, Ren's choices: the readings of §6.10 gain the least registration and the tail
t = once(t, '；“situational awareness”是否读作中心知道部分在其反馈之外所到达的。',
         '；“situational awareness”是否读作中心知道部分在其反馈之外所到达的；条件任意多时，识是否读作律的敏感（凡律在每个历史下读'
         '有限多个条件，`Becoming.Sensitivity`），依存于整体而不依存于其任何部分者是否读作尾（读法是 AI 的）。')
t = once(t, '; whether “situational awareness” reads as a center knowing what its part reaches beyond its feedback.',
         '; whether “situational awareness” reads as a center knowing what its part reaches beyond its feedback; with any number '
         "of conditions, whether registration reads as the law's sensitivity (wherever the law reads finitely many conditions "
         'under each history, `Becoming.Sensitivity`), and whether what depends on the whole and on no part of it reads as a tail '
         "(the readings are the AI's).")
# the paragraph of the response as the dynamics give: what it did not derive is now answered elsewhere
t = once(t, '律本身、它读已立者、进程可行，以及条件无穷多时敏感是否仍是最小的识，都不推出，何时一个动作是部分自己的也不推出。',
         '律本身、它读已立者、进程可行，都不推出。条件无穷多时敏感是否仍是最小的识，由 `Becoming.Sensitivity` 回答：凡律在每个历史下读'
         '有限多个条件，敏感都是最小的识；这一条件不能去掉：给定水平是否终将消失的判定，尾之律是反例，而条件以自然数编号时每个反例都'
         '给出弱有限全知原则。何时一个动作是部分自己的，由 `Becoming.Coupling` 回答：恰当它经部分的配置形成。')
t = once(t,
         'The law itself, that it reads what has stood, feasibility, and whether sensitivity is still the least registration with '
         "infinitely many conditions, are not derived, nor when a move is the part's own.",
         'The law itself, that it reads what has stood, and feasibility are not derived. Whether sensitivity is still the least '
         'registration with infinitely many conditions is answered in `Becoming.Sensitivity`: it is wherever the law reads finitely '
         'many conditions under each history; that condition cannot be dropped, for given a decision of whether levels vanish '
         'eventually the tail law is a counterexample, and with the conditions numbered every counterexample gives the weak limited '
         "principle of omniscience. When a move is the part's own is answered in `Becoming.Coupling`: exactly where it is formed "
         "through the part's configuration.")
# Part I stated whole
t = once(t, '条件有限时这个识就是律的敏感（`ExchangeLaw.Nonanticipating.through_sensitive`）',
         '律在每个历史下读有限多个条件时，无论条件多少，这个识就是律的敏感（`ExchangeLaw.ReadsFinitely.through_sensitive`；'
         '条件有限时每个读已立者的律都如此，`ExchangeLaw.Nonanticipating.through_sensitive`）')
t = once(t,
         "and with finitely many conditions that registration is the law's sensitivity "
         '(`ExchangeLaw.Nonanticipating.through_sensitive`)',
         'and wherever the law reads finitely many conditions under each history, with any number of conditions, that registration '
         "is the law's sensitivity (`ExchangeLaw.ReadsFinitely.through_sensitive`; with finitely many conditions every law of what "
         'has stood does, `ExchangeLaw.Nonanticipating.through_sensitive`)')
# §8 status row
t = once(t,
         '，条件有限时这个识就是律的敏感，比较不另给第二个流与回应（[counterfactual-is-the-course](../results/records/'
         'counterfactual-is-the-course.md)、[comparison-where-the-rest-responds](../results/records/'
         'comparison-where-the-rest-responds.md)）。开放：律本身；条件无穷多时敏感是否仍是最小的识；差别到达多少；读法待 Ren |',
         '，律在每个历史下读有限多个条件时，无论条件多少，这个识就是律的敏感，比较不另给第二个流与回应；条件无穷多时这一条件不能去掉，'
         '条件以自然数编号时每个反例都给出弱有限全知原则（[counterfactual-is-the-course](../results/records/'
         'counterfactual-is-the-course.md)、[comparison-where-the-rest-responds](../results/records/'
         'comparison-where-the-rest-responds.md)、[sensitivity-is-the-least-registration](../results/records/'
         'sensitivity-is-the-least-registration.md)）。开放：律本身；反例之存在的确切强度；差别到达多少；读法待 Ren |')
# the logical commitment
t = once(t, '所以核心陈述较弱的形式：不在任意晚的步活跃，曾经成立的不是无界多。',
         '所以核心陈述较弱的形式：不在任意晚的步活跃，曾经成立的不是无界多。最小的识亦然（`Becoming.Sensitivity`）：条件以自然数编号时，'
         '读已立者的律若在两个于其所敏感者上相同的历史下给出不同，就给出弱有限全知原则（`WLPO`：每个布尔序列处处为假或否；有限全知原则'
         '给出它，它没有构造性证明；`wlpo_of_not_through_sensitive`），所以核心对在每个历史下读有限多个条件的律陈述它。')
t = once(t, 'So the core states the weaker forms: not active at arbitrarily late steps, and not unboundedly many ever holding.',
         'So the core states the weaker forms: not active at arbitrarily late steps, and not unboundedly many ever holding. '
         'Likewise the least registration (`Becoming.Sensitivity`): with the conditions numbered by the natural numbers, a law of '
         'what has stood that gives differently under two histories agreeing on what it is sensitive to gives the weak limited '
         'principle of omniscience (`WLPO`: every Boolean sequence is false throughout or not; the limited principle gives it, and '
         'it has no constructive proof; `wlpo_of_not_through_sensitive`), so the core states it for laws reading finitely many '
         'conditions under each history.')
# glossary
t = once(t,
         '| 敏感 | sensitive | 形成的交换对一个条件敏感：某步只改变该条件的水平就改变它所交换的；条件有限时，读已立者的律经其敏感而读，'
         '它所经的每个识（连同所依存的）都不漏掉其敏感者 | `ExchangeLaw.Sensitive`、`ExchangeLaw.Nonanticipating.through_sensitive`、'
         '`ExchangeLaw.Through.registers_of_sensitive` |',
         docs['glossary_sensitive'] + '\n' + docs['glossary_reads'])
CHAPTER.write_text(t)
print('root, checker, Lean README and chapter updated')
