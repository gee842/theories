#!/usr/bin/env python3
"""P126: write docs.json, the texts apply_docs.py places.

usage: python3 -B make_docs_json.py

The root module bullet and the checker's scope entry are wrapped here at 100 columns, as the files
they go into are; the other texts are single lines of Markdown.
"""
import json
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
RECORD = '../results/records/what-a-law-of-the-whole-and-no-part-takes.md'
SENSITIVITY = '../results/records/sensitivity-is-the-least-registration.md'

BULLET = (
    '`Becoming.Tail` (L4): what a law of the whole and no part takes, with no premise beyond what each '
    'statement names. A number read off levels that no single condition changes is set by the tail alone; the '
    'law exchanging it reads what has stood and is insensitive to every condition, and where the number '
    'differs it has no least registration. With the conditions numbered, such a number, a law insensitive at '
    'a step to every condition that still differs there, and a counterexample to the least registration each '
    'exist exactly where a rule decides, of every Boolean sequence, whether it is false throughout: the weak '
    'limited principle of omniscience as a rule. The decision of vanishing is exactly the limited principle '
    'as a rule, so the tail law takes the limited principle where a counterexample needs only the weak '
    'rule, which the indicator of never vanishing takes.')

SCOPE = (
    'Tail: a number read off levels that no single condition changes is one that levels agreeing from some '
    'condition on give alike, and the law exchanging it reads what has stood, is insensitive to every '
    'condition and, where the number differs, does not read through what it is sensitive to and has no least '
    'registration; the tail law of Sensitivity is the instance of the indicator of vanishing; with the '
    'conditions numbered, such a number, a law insensitive at a step to every condition that still differs '
    'there, and a counterexample to the least registration each exist exactly where a rule decides of every '
    'Boolean sequence whether it is false throughout, the law of levels that never vanish being built from '
    'the rule; the decision of vanishing is exactly a rule deciding whether a sequence has a true, which '
    'gives that rule and LPO.')

README_ROW = (
    '| L4 | [`Becoming.Tail`](Becoming/Tail.lean) | 整体而无部分之律所需（除了各定理所写者不加前提）：没有一个条件改变的数'
    '（`ChangedByNoCondition`）恰是只由尾所定者（`ChangedByNoCondition.eq_of_agree_from`、'
    '`ChangedByNoCondition.of_agree_from`）；交换它的整体之律（`wholeLaw`）读已立者、不敏感于任何条件（`wholeLaw_nonanticipating`、'
    '`wholeLaw_insensitive`、`wholeLaw_not_sensitive`），经从任一条件起的各条件而读（`wholeLaw_through_from`），这个数有差别时不经'
    '其敏感而读、不读有限多个条件、它所经的识没有最小的（`wholeLaw_not_through_sensitive`、`wholeLaw_not_readsFinitely`、'
    '`wholeLaw_no_least_registration`），尾之律是消失之指示的实例（`tailLaw_eq_wholeLaw`）；比较两个数判定混合所沿的序列，所以'
    '反例给出规则（`mixedDecision`、`insensitiveDiffersDecision`、`notThroughSensitiveDecision`），规则给出 `WLPO`'
    '（`WLPO.of_rule`）；规则两次判定水平是否永不消失（`vanishesFrom`、`neverIndicator`、`vanishesFrom_never_iff`），永不消失之律是'
    '只由规则造出的反例（`neverLaw`、`neverLaw_nonanticipating`、`neverLaw_insensitive`、`neverLaw_differs`），其指示与消失之指示'
    '之和为 1（`neverIndicator_add_vanishIndicator`）；这样的数、在某步不敏感于每个条件而仍有差别的律、最小的识的反例，各恰在规则'
    '存在处存在（`changedByNoCondition_iff_rule`、`insensitive_differs_iff_rule`、`not_through_sensitive_iff_rule`）；消失之判定'
    '恰是有限全知原则作为规则（`lpoRuleOfVanishDecision`、`raisedFrom`、`vanishDecisionOfLPORule`、'
    '`vanishDecision_iff_lpoRule`），它给出弱的规则与 `LPO`（`wlpoRuleOfLPORule`、`LPO.of_rule`）；读法是 AI 的，待 Ren / what '
    'a law of the whole and no part takes (no premise beyond what each theorem names): a number no single '
    'condition changes (`ChangedByNoCondition`) is exactly one the tail alone sets '
    '(`ChangedByNoCondition.eq_of_agree_from`, `ChangedByNoCondition.of_agree_from`); the law of the whole '
    'exchanging it (`wholeLaw`) reads what has stood and is insensitive to every condition '
    '(`wholeLaw_nonanticipating`, `wholeLaw_insensitive`, `wholeLaw_not_sensitive`), reads through the conditions '
    'from any one on (`wholeLaw_through_from`), and where the number differs does not read through what it is '
    'sensitive to, nor finitely many conditions, and has no least registration (`wholeLaw_not_through_sensitive`, '
    '`wholeLaw_not_readsFinitely`, `wholeLaw_no_least_registration`), the tail law being the instance of the '
    'indicator of vanishing (`tailLaw_eq_wholeLaw`); comparing two numbers decides the sequence a mix runs '
    'along, so a counterexample gives a rule (`mixedDecision`, `insensitiveDiffersDecision`, '
    '`notThroughSensitiveDecision`), and the rule gives `WLPO` (`WLPO.of_rule`); the rule decides twice whether '
    'levels never vanish (`vanishesFrom`, `neverIndicator`, `vanishesFrom_never_iff`), and the law of levels '
    'that never vanish is a counterexample built from the rule alone (`neverLaw`, `neverLaw_nonanticipating`, '
    '`neverLaw_insensitive`, `neverLaw_differs`), its indicator and that of vanishing summing to 1 '
    '(`neverIndicator_add_vanishIndicator`); such a number, a law insensitive at a step to every condition that '
    'still differs there, and a counterexample to the least registration each exist exactly where the rule does '
    '(`changedByNoCondition_iff_rule`, `insensitive_differs_iff_rule`, `not_through_sensitive_iff_rule`); the '
    'decision of vanishing is exactly the limited principle of omniscience as a rule '
    '(`lpoRuleOfVanishDecision`, `raisedFrom`, `vanishDecisionOfLPORule`, `vanishDecision_iff_lpoRule`), which '
    'gives the weak rule and `LPO` (`wlpoRuleOfLPORule`, `LPO.of_rule`); the readings are the AI\'s, pending '
    'Ren |')

CHAPTER_ROW = (
    f'| L4 | [Becoming.Tail]({LEAN}Tail.lean) | 整体而无部分之律所需（除了各定理所写者不加前提）：没有一个条件改变的数只由尾所定，'
    '交换它的律读已立者、不敏感于任何条件，这个数有差别时它所经的识没有最小的，尾之律是一例；条件以自然数编号时，这样的数、在某步不敏感'
    '于每个条件而仍有差别的律、最小的识的反例，各恰在一个规则判定每个布尔序列是否处处为假之处存在，即弱有限全知原则作为规则；永不消失'
    '之律由这个规则造出；消失之判定恰是有限全知原则作为规则。/ What a law of the whole and no part takes, with no premise '
    'beyond what each theorem names: a number no single condition changes is set by the tail alone, and the law '
    'exchanging it reads what has stood and is insensitive to every condition, with no least registration where '
    'the number differs, the tail law being one; with the conditions numbered, such a number, a law insensitive '
    'at a step to every condition that still differs there, and a counterexample to the least registration each '
    'exist exactly where a rule decides, of every Boolean sequence, whether it is false throughout, the weak '
    'limited principle of omniscience as a rule; the law of levels that never vanish is built from that rule; '
    'the decision of vanishing is exactly the limited principle as a rule. | 39 |')

RESPONSE_ZH = '；反例恰在一个规则判定每个布尔序列是否处处为假之处存在（`Becoming.Tail`）'
RESPONSE_EN = ('; a counterexample exists exactly where a rule decides, of every Boolean sequence, whether it is '
               'false throughout (`Becoming.Tail`)')

PARAGRAPH_ZH = (
    f'**整体而无部分之律所需（第一部分）。** `Becoming.Sensitivity` 留下反例之存在的确切强度，在弱有限全知原则与消失之判定之间'
    f'（[Becoming.Tail]({LEAN}Tail.lean)）。从水平读出的数，只在一个条件上不同的水平给出相同者，说没有一个条件改变它'
    '（`ChangedByNoCondition`）；这恰是从某个条件起相同的水平给出相同者，其下的条件一次换一个'
    '（`ChangedByNoCondition.eq_of_agree_from`、`ChangedByNoCondition.of_agree_from`）：没有部分改变的，只由尾所定。交换这样一个数'
    '的整体之律（`wholeLaw`）读已立者，在每步不敏感于每个条件，经从任一条件起的各条件而读；这个数有差别时，它不经其敏感而读，不读有限'
    '多个条件，它所经的识没有最小的（`wholeLaw_not_through_sensitive`、`wholeLaw_not_readsFinitely`、'
    '`wholeLaw_no_least_registration`）；尾之律是消失之指示的实例（`tailLaw_eq_wholeLaw`）。`Becoming.Sensitivity` 沿一个布尔序列'
    '混合两段历史，再比较两个数；比较数是判定的，所以每个反例给出的不只是弱有限全知原则，而是一个规则，对每个布尔序列判定它是否处处为假'
    '（`mixedDecision`、`insensitiveDiffersDecision`、`notThroughSensitiveDecision`；规则给出 `WLPO`，`WLPO.of_rule`）。反过来，给定'
    '这样的规则，水平从第 N 个条件起是否消失可判定（`vanishesFrom`），水平是否从哪个条件起都不消失由规则再判定一次（`neverIndicator`、'
    '`vanishesFrom_never_iff`）；这个指示不被任何条件改变，在全为 0 与全为 1 的水平之间不同，给定消失之判定时与消失之指示之和为 1'
    '（`neverIndicator_add_vanishIndicator`）；它的律是一个只由规则造出的反例（`neverLaw`）。所以不被任何条件改变而仍有差别的数、'
    '在某步不敏感于每个条件而仍有差别的律、最小的识的反例，各恰在这样的规则存在之处存在（`changedByNoCondition_iff_rule`、'
    '`insensitive_differs_iff_rule`、`not_through_sensitive_iff_rule`）。消失之判定恰是有限全知原则作为规则：它判定每个布尔序列是否'
    '有真者，这样的规则也分两次判定消失（`lpoRuleOfVanishDecision`、`vanishDecisionOfLPORule`、`vanishDecision_iff_lpoRule`），并'
    '给出弱的规则与 `LPO`（`wlpoRuleOfLPORule`、`LPO.of_rule`）；尾之律取有限全知原则作为规则，反例只需要弱的。读法（AI 的，待 Ren）：依存于整体而'
    '不依存于其任何部分者，恰在能对每个无尽的是非记录判定它是否全是否之处给出；条件编号时，最小的识恰在这一全知处不成立，不需要更多，'
    '核心不假定它；读作水平永不消失，同一个整体只需要弱的规则，读作终将消失则需要有限全知原则的规则。命题 `WLPO` 是否给出规则（从关系'
    '选出函数，核心不假定）、弱的规则是否给出有限全知原则、条件不以自然数编号时反例给出什么，都不推出。见 '
    f'[what-a-law-of-the-whole-and-no-part-takes]({RECORD})。')

PARAGRAPH_EN = (
    '**What a law of the whole and no part takes (Part I).** `Becoming.Sensitivity` leaves open the exact '
    'strength of the existence of a counterexample, between the weak limited principle of omniscience and the '
    f'decision of vanishing ([Becoming.Tail]({LEAN}Tail.lean)). A number read off levels is changed by no '
    'condition where levels differing at one condition only give it alike (`ChangedByNoCondition`); exactly '
    'then levels agreeing from some condition on give it alike, the conditions below being changed one at a '
    'time (`ChangedByNoCondition.eq_of_agree_from`, `ChangedByNoCondition.of_agree_from`): what no part '
    'changes, only the tail sets. The law of the whole exchanging such a number (`wholeLaw`) reads what has '
    'stood, is insensitive at every step to every condition and reads through the conditions from any one on; '
    'where the number differs, it does not read through what it is sensitive to, nor finitely many conditions, '
    'and the registrations it reads through have no least one (`wholeLaw_not_through_sensitive`, '
    '`wholeLaw_not_readsFinitely`, `wholeLaw_no_least_registration`); the tail law is the instance of the '
    'indicator of vanishing (`tailLaw_eq_wholeLaw`). `Becoming.Sensitivity` mixes two histories along a '
    'Boolean sequence and then compares two numbers; comparing numbers is decided, so every counterexample '
    'gives not only the weak limited principle of omniscience but a rule deciding, of every Boolean sequence, '
    'whether it is false throughout (`mixedDecision`, `insensitiveDiffersDecision`, '
    '`notThroughSensitiveDecision`; the rule gives `WLPO`, `WLPO.of_rule`). Conversely, given such a rule, '
    'whether levels vanish from condition N on is decided (`vanishesFrom`), and whether they vanish from no '
    'condition on is decided by the rule again (`neverIndicator`, `vanishesFrom_never_iff`); this indicator is '
    'changed by no condition, tells levels all 0 from levels all 1, and with the decision of vanishing given '
    'sums with the indicator of vanishing to 1 (`neverIndicator_add_vanishIndicator`); its law is a '
    'counterexample built from the rule alone (`neverLaw`). So a number changed by no condition that still '
    'differs, a law insensitive at a step to every condition that still differs there, and a counterexample to '
    'the least registration each exist exactly where such a rule does (`changedByNoCondition_iff_rule`, '
    '`insensitive_differs_iff_rule`, `not_through_sensitive_iff_rule`). The decision of vanishing is exactly '
    'the limited principle of omniscience as a rule: it decides of every Boolean sequence whether it has a '
    'true, and such a rule decides vanishing in two passes (`lpoRuleOfVanishDecision`, '
    '`vanishDecisionOfLPORule`, `vanishDecision_iff_lpoRule`), giving the weak rule and `LPO` '
    '(`wlpoRuleOfLPORule`, `LPO.of_rule`); so the tail law takes the limited principle as a rule, where a '
    'counterexample needs only the weak one. Readings '
    '(the AI\'s, pending Ren): what depends on the whole and on no part of it is given exactly where it can be '
    'decided, of every unending record of yes and no, whether it says no throughout; with the conditions '
    'numbered, the least registration fails exactly at this omniscience and needs no more of it, and the core '
    'does not assume it; read as whether levels never vanish, the same whole takes only the weak rule, and read '
    'as whether they vanish eventually, the rule of the limited principle. Whether the proposition `WLPO` gives '
    'a rule (choosing a function from a relation, which the core does not assume), whether the weak rule gives '
    'the limited principle, and what a counterexample gives where the conditions are not numbered by the '
    f'natural numbers are not derived. See [what-a-law-of-the-whole-and-no-part-takes]({RECORD}).')

WHOLE_ZH = (
    '- **整体而无部分之律所需。** 条件以自然数编号时，从水平读出的、没有一个条件改变而仍有差别的数，在某步不敏感于每个条件而仍有差别的'
    '律，与最小的识的反例，各恰在一个规则判定每个布尔序列是否处处为假之处存在（`changedByNoCondition_iff_rule`、'
    '`insensitive_differs_iff_rule`、`not_through_sensitive_iff_rule`）；消失之判定恰是有限全知原则作为规则'
    '（`vanishDecision_iff_lpoRule`）。')
WHOLE_EN = (
    '- **What a law of the whole and no part takes.** With the conditions numbered by the natural numbers, a '
    'number read off levels that no condition changes and that still differs, a law insensitive at a step to '
    'every condition that still differs there, and a counterexample to the least registration each exist '
    'exactly where a rule decides, of every Boolean sequence, whether it is `false` throughout '
    '(`changedByNoCondition_iff_rule`, `insensitive_differs_iff_rule`, `not_through_sensitive_iff_rule`); the '
    'decision of vanishing is exactly the limited principle of omniscience as a rule '
    '(`vanishDecision_iff_lpoRule`).')

STATUS_ZH = (
    '；反例恰在一个规则判定每个布尔序列是否处处为假之处存在，即弱有限全知原则作为规则，消失之判定恰是有限全知原则作为规则'
    f'（[what-a-law-of-the-whole-and-no-part-takes]({RECORD})）')

FURTHER_ZH = (
    '反例之存在的确切强度已给出（`Becoming.Tail`：反例恰在一个规则判定每个布尔序列是否处处为假之处存在，即弱有限全知原则作为规则；'
    '消失之判定恰是有限全知原则作为规则）；')
FURTHER_EN = (
    'the exact strength of the existence of a counterexample is given (`Becoming.Tail`: a counterexample exists '
    'exactly where a rule decides, of every Boolean sequence, whether it is false throughout, the weak limited '
    'principle of omniscience as a rule; the decision of vanishing is exactly the limited principle as a '
    'rule); ')

GLOSSARY = [
    '| 没有一个条件改变（整体而无部分） | changed by no condition (a whole and no part) | 从水平读出的数，只在一个条件上不同的水平'
    '给出相同者；恰是从某个条件起相同的水平给出相同者，只由尾所定；交换它的律不敏感于任何条件，这个数有差别时没有最小的识 | '
    '`ChangedByNoCondition`、`ChangedByNoCondition.eq_of_agree_from`、`wholeLaw`、`wholeLaw_no_least_registration` |',
    '| 规则（判定处处为假的） | rule (deciding false throughout) | 对每个布尔序列判定它是否处处为假：弱有限全知原则作为规则，给出 '
    '`WLPO`；整体而无部分者、最小的识的反例，各恰在它存在处存在；判定是否有真者的规则恰是消失之判定 | '
    '`changedByNoCondition_iff_rule`、`not_through_sensitive_iff_rule`、`WLPO.of_rule`、`vanishDecision_iff_lpoRule` |',
]


def bullet(text):
    return '\n'.join(textwrap.wrap(text, width=100, initial_indent='* ', subsequent_indent='  ',
                                   break_on_hyphens=False, break_long_words=False))


def scope(text):
    """Lines `    "..."`, each at most 100 columns, each piece ending in a space."""
    words, lines, cur = text.split(' '), [], ''
    for w in words:
        nxt = (cur + ' ' + w) if cur else w
        if len(nxt) + 1 > 93:
            lines.append(cur + ' ')
            cur = w
        else:
            cur = nxt
    lines.append(cur + ' ')
    out = ''.join(f'    "{line}"\n' for line in lines)
    assert all(len(line) <= 100 for line in out.splitlines())
    return out


docs = {
    'bullet': bullet(BULLET), 'scope': scope(SCOPE), 'readme_row': README_ROW, 'chapter_row': CHAPTER_ROW,
    'response_zh': RESPONSE_ZH, 'response_en': RESPONSE_EN, 'paragraph_zh': PARAGRAPH_ZH,
    'paragraph_en': PARAGRAPH_EN, 'whole_zh': WHOLE_ZH, 'whole_en': WHOLE_EN, 'status_zh': STATUS_ZH,
    'further_zh': FURTHER_ZH, 'further_en': FURTHER_EN, 'glossary': GLOSSARY,
}
assert all(len(line) <= 100 for line in docs['bullet'].splitlines())
(HERE / 'docs.json').write_text(json.dumps(docs, ensure_ascii=False, indent=2) + '\n')
print('wrote docs.json:', ', '.join(docs))
