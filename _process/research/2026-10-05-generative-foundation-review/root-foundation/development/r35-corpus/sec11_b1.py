#!/usr/bin/env python3
"""R35 batch B1, after the move: chapter section 11 (EN, ZH) and the section 3 citation say where the moved chapters
now stand. usage (from the checkout root): python3 -B sec11_b1.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
EN = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
RC = 'receipt `_process/architecture/moves/R35-B1-chapters.json`'

EN_ROWS = {
    '| Foundation study | [G0-WARRANT](../history/G0-WARRANT.md) |':
        f'| Moved to history | [G0-WARRANT](../history/G0-WARRANT.md) | Written on 9 October 2026, when living significance was an adopted axiom; it is now a condition (§6.15), so the framing is historical. What each kind of support contributes is stated in §8.5. Moved unchanged to `../history/` with its Chinese edition by R35 (20 October 2026; {RC}). |',
    '| Statement source | [PHILOSOPHICAL-ACCOUNT](../history/PHILOSOPHICAL-ACCOUNT.md) |':
        f'| Moved to history | [PHILOSOPHICAL-ACCOUNT](../history/PHILOSOPHICAL-ACCOUNT.md) | The synthesis of knowing and wisdom of 8 October 2026, a restatement of the whole outside this chapter; §3 cites it as that synthesis. Moved unchanged by R35 ({RC}). |',
    '| Statement source | [PLURAL-SYSTEMS-AND-CORRECTION](../history/PLURAL-SYSTEMS-AND-CORRECTION.md) |':
        f'| Moved to history | [PLURAL-SYSTEMS-AND-CORRECTION](../history/PLURAL-SYSTEMS-AND-CORRECTION.md) | Its section 15, responsive transformation (9 October 2026), is stated in §4; the rest records models of correction superseded since. Moved unchanged with its Chinese edition by R35 ({RC}). |',
    '| Mathematics | [MATHEMATICAL-ROOT-FRONTIER](../history/MATHEMATICAL-ROOT-FRONTIER.md) |':
        f'| Moved to history | [MATHEMATICAL-ROOT-FRONTIER](../history/MATHEMATICAL-ROOT-FRONTIER.md) | Status page of 16 October 2026 of the mathematics line kept outside the spine, superseded by §8 and §9. Moved unchanged by R35 ({RC}). |',
    '| Historical, pinned | [ALIGNMENT-COMPLETION](../history/ALIGNMENT-COMPLETION.md) |':
        f'| Moved to history | [ALIGNMENT-COMPLETION](../history/ALIGNMENT-COMPLETION.md) | Historical (6 October 2026). The frozen check script that names its old path is evidence of 9 October and reaches it through the move receipt. Moved unchanged by R35 ({RC}). |',
    '| Historical, pinned | [FORMAL-CORE](../history/FORMAL-CORE.md) |':
        f'| Moved to history | [FORMAL-CORE](../history/FORMAL-CORE.md) | Historical (5 October 2026); moved unchanged by R35, as ALIGNMENT-COMPLETION. |',
    '| Historical, pinned | [FORMAL-SPECIFICATION](../history/FORMAL-SPECIFICATION.md) |':
        f'| Moved to history | [FORMAL-SPECIFICATION](../history/FORMAL-SPECIFICATION.md) | Historical (5 October 2026); moved unchanged by R35, as ALIGNMENT-COMPLETION. |',
}
ZH_ROWS = {
    '| 根基研究 | [生命意义的根据](../history/G0-WARRANT.md) |':
        '| 已移入历史 | [生命意义的根据](../history/G0-WARRANT.md) | 写于 2026-10-09，当时生命意义是一条采用的公理；它现在是条件（§6.15），所以其框架是历史的。每种支持各承担什么，已写入“哲学根据”。R35（2026-10-20）连同其中文版原样移入 `../history/` |',
}


def rows(path, table):
    text = path.read_text()
    lines = text.split('\n')
    for i, line in enumerate(lines):
        for head, new in table.items():
            if line.startswith(head):
                lines[i] = new
                table = {k: v for k, v in table.items() if k != head}
                break
    assert not table, list(table)
    return '\n'.join(lines)


en = rows(EN, dict(EN_ROWS))
old = '[The philosophical account](../history/PHILOSOPHICAL-ACCOUNT.md) joins them with common inquiry and practical wisdom.'
assert en.count(old) == 1
en = en.replace(old, 'The philosophical account of 8 October 2026 ([history](../history/PHILOSOPHICAL-ACCOUNT.md)) joins them with common inquiry and practical wisdom.')
EN.write_text(en)
zh = rows(ZH, dict(ZH_ROWS))
old = '[哲学说明](../history/PHILOSOPHICAL-ACCOUNT.md)把它们与共同探究和实践智慧合在一起。'
assert zh.count(old) == 1
zh = zh.replace(old, '2026 年 10 月 8 日的哲学说明（[历史](../history/PHILOSOPHICAL-ACCOUNT.md)）把它们与共同探究和实践智慧合在一起。')
ZH.write_text(zh)
print('ok')
