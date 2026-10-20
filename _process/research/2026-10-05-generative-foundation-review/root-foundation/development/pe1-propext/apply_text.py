#!/usr/bin/env python3
"""PE1's chapter text: a paragraph in section 9 after "The checker." on why the core excludes propext and why the
periphery may use it, a pointer in section 0's proof-language row, and the same paragraph, shorter, in the Chinese
edition's section 9. usage: python3 -B apply_text.py   (from the checkout root; each edit must match exactly once)"""
from pathlib import Path

EN = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
ZH = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md')
MOD = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/PropositionIdentity.lean'
REC = '../results/records/proposition-identity.md'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:80], text.count(old))
    return text.replace(old, new)


PARA = (
    f'**Why the core excludes `propext`, and why the periphery may use it** ([`Becoming.PropositionIdentity`]({MOD}), '
    f'no axiom; [record]({REC})). From the relational start a proposition is read through its relations of derivation, '
    'what derives it and what it derives, and `propext` (`(a ↔ b) → a = b`) says that a proposition is nothing beyond '
    'them. The module states this exactly. `propext`, as a proposition, holds exactly where every reading of '
    'propositions is lumped by interderivability (`Learning.Lumped`, read through the two ends of an interderivation; '
    '`extensional_iff_lumped`), and exactly where the reading that reads a proposition by name, the identity, is '
    '(`byName_lumped_iff`); a reading built from relations (atoms, the connectives, quantifiers over any type) '
    'respects interderivability already, with `↔` rather than `=` (`Formula.eval_congr`). The identification forgets '
    'no witness: any two witnesses of `a ↔ b` are equal (`iff_witness_unique`), while `Bool` has two different '
    'self-inverse maps (`two_equivalences`), so identifying types along an equivalence would lose which one. So '
    '`propext` is an exact lumping of outcomes. What it does not keep is the course: transport along any equation of '
    'propositions with a constant motive keeps the value (`transport_const`), but a value transported along `propext` '
    'does not reduce. `#reduce` stops at the transport, and neither `rfl` nor `decide` proves the value it provably '
    'has; this is a kernel observation with Lean 4.29.1, kept with the record, not a theorem. The core\'s runs, '
    'censuses and witnesses are checked by computation (`rfl` and `decide` on them), so the core states `↔` wherever a '
    'result would need `=` between propositions and keeps its empty report; the periphery, whose results concern '
    'outcomes and carry their own receipts, may use `propext` as the exact lumping it is. That every reading of a '
    'proposition is relational is `propext` itself: here it is a hypothesis (`Extensional`), never a conclusion.\n\n')
ANCHOR = '**The current receipt** is run '

ROW_OLD = ('no excluded middle, choice, propositional or function extensionality is assumed. ')
ROW_NEW = ('no excluded middle, choice, propositional or function extensionality is assumed. What identifying '
           'interderivable propositions (`propext`) keeps and loses, and why the core states `↔` where a result would '
           'need `=`, is stated in §9 (`Becoming.PropositionIdentity`). ')

ZH_PARA = (
    f'**核心为何不用 `propext`，外围为何可以用**（[`Becoming.PropositionIdentity`]({MOD})，不用公理；[记录]({REC})）。'
    '从关系的起点，一个命题经其推导关系被读：什么推出它，它推出什么；`propext`（`(a ↔ b) → a = b`）说命题不外乎这些关系。'
    '模块确切陈述：作为命题的 `propext` 恰在命题的每个读法都按可互推归并之处成立（`Learning.Lumped`，经一个互推的两端读；'
    '`extensional_iff_lumped`），也恰在按名读命题的读法（恒等）如此之处（`byName_lumped_iff`）；由关系构成的读法'
    '（原子、联结词、对任何类型的量词）本已尊重可互推，给出 `↔` 而非 `=`（`Formula.eval_congr`）。这一等同不丢失见证：'
    '`a ↔ b` 的任两个见证相等（`iff_witness_unique`），而 `Bool` 有两个不同的自逆映射（`two_equivalences`），所以沿等价等同类型会丢失是哪一个。'
    '所以 `propext` 是对结果的确切归并。它不保留的是进程：沿命题之间任一等式、以常值动机输运保值（`transport_const`），'
    '但沿 `propext` 输运的值不再归约：`#reduce` 停在输运处，`rfl` 与 `decide` 都证不出它可证的值；这是 Lean 4.29.1 内核的观察，随记录保存，不是定理。'
    '核心的运行、计数与见证以计算检查（对它们用 `rfl` 与 `decide`），所以核心在结果需要命题之间的 `=` 之处陈述 `↔`，保持空的公理报告；'
    '外围的结果关乎结果并各有回执，可以把 `propext` 当作它所是的确切归并来用。命题的每个读法都是关系的，这就是 `propext` 本身：在此它是假设（`Extensional`），从不是结论。\n\n')
ZH_ANCHOR = ('所有新的形式结果陈述在一条脊柱上；它不能表达某结果之处就扩展它，而不另建模型，既有模块经实例或等价定理相连。'
             '核心的要求（§0 A 组）由[合并的检查器]')

en = EN.read_text()
assert 'Why the core excludes `propext`' not in en, 'already applied'
en = once(en, ANCHOR, PARA + ANCHOR)
en = once(en, ROW_OLD, ROW_NEW)
EN.write_text(en)

zh = ZH.read_text()
i = zh.index(ZH_ANCHOR)
j = zh.index('\n\n', i) + 2
assert zh.count(ZH_ANCHOR) == 1
zh = zh[:j] + ZH_PARA + zh[j:]
ZH.write_text(zh)
print('applied')
