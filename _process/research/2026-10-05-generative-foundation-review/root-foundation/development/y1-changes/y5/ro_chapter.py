#!/usr/bin/env python3
"""Y5 (19 October 2026): bring RO's chapter on the Chinese sources up to Y5. The passage tables are reprinted from
RO's passages.json (after ro_fixes.py); §5.1's paragraph on the arrangements says what is now proved; §8's row of the
hexagram world's supplements says the gap is closed and states what Y5 proved, correcting the claim it quoted; §11's
first item counts six gaps left. usage: python3 -B ro_chapter.py [CHECKOUT_ROOT] (each edit must match once)."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[6]
KIT = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources'
CHAPTER = ROOT / 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
sys.path.insert(0, str(KIT))
import verify_ro as V  # noqa: E402

LEAN = ('../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
        'HexagramSequences.lean')
RECORD = '[hexagram-arrangements-and-laws](../results/records/hexagram-arrangements-and-laws.md)'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


text = CHAPTER.read_text()
passages = json.loads((KIT / 'passages.json').read_text())['passages']
for t in V.TRADITIONS:
    if any(p['tradition'] == t for p in passages):
        start = text.index(V.begin(t)) + len(V.begin(t))
        text = text[:start] + '\n' + V.table(passages, t) + '\n' + text[text.index(V.end(t)):]

text = once(text, '''- **排列与估值之处不是。** [序卦在对与对之间](#p-xugua-between-pairs)给出的理由（物不可以终否，故受之以同人）是加在一个清单上的读法，不是构形所承载的承续之律：所传卦序不是任何三格局部规则的运行（最多 63 步中 9 步相合），也不是任何“置换诸位再加掩码”之律的运行（最好的是倒转，28 步，恰是对内的倒转）。这一点由脚本计算，尚未写成 Lean（§8）。''',
            f'''- **排列与估值之处不是。** [序卦在对与对之间](#p-xugua-between-pairs)给出的理由（物不可以终否，故受之以同人）是加在一个清单上的读法，不是构形所承载的承续之律。所传卦序是一个律的运行，但运行它的律除未济一处外都相同，是一张表：每一爻皆读每一爻，不与倒转、全变或二者交换，所以没有三格局部规则、也没有任何“置换诸位再加掩码”之律运行它（[`Becoming.HexagramSequences`]({LEAN})，Y5，§8）；脚本另算的部分相合（三格局部规则最多 63 步中 9 步，置换加掩码之律最好的是倒转，28 步，恰是对内的倒转）不变。[杂卦](#p-zagua-pairs)保留同样的三十二对，丢掉对与对之间的次序；[帝出乎震](#p-shuogua-di-chu-zhen)之八站同样不与全变、倒转或轮转交换。''')

text = once(text, '''| 卦序“不是任何律的轨道”只在易传章 §8 中说明，未证 | 所传卦序不是任何三格局部规则、也不是任何置换加掩码之律的运行；卦变为两爻互换，保阳爻之数，是两半之间交换律的一步；阳爻之数的奇偶是律所同行的归并；杂卦是同一 32 对的置换；消息之律无静止 |''',
            f'''| 已由 Y5 补上（[`Becoming.HexagramSequences`]({LEAN})，记录 {RECORD}）；原引易传章 §8“卦序不是任何律的轨道”之说不确 | 所证：运行所传卦序之律除未济一处外都相同，恰其一不合并、成六十四步之一轨；每一这样的律每一爻皆读每一爻，不与倒转、全变或二者交换，所以没有三格局部规则、没有置换加掩码之律运行它；卦变为两爻互换，保阳爻之数，是两卦之间交换律的一步，读为世界则平衡；阳爻之数的奇偶是消息之律与一爻之变所同行的归并，三爻之奇偶恰分阳卦阴卦；杂卦是同一 32 对的另一次序；消息之律与一爻之变的运行无静止；八站与交亦各写成 |''')

text = once(text, '- §8 的七项缺口，各待认领与写成 Lean。',
            '- §8 的前六项缺口，各待写成 Lean（已认领者见工作板）；第七项（卦的世界的补充）已由 Y5 写成。')
CHAPTER.write_text(text)
print('RO chapter updated')
