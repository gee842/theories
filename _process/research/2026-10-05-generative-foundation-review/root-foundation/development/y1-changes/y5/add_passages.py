#!/usr/bin/env python3
"""Y5 (19 October 2026): add to the passage map of the 易传 chapter the two passages of the 彖 that read an exchange
of two lines and that RO's map does not hold, 恒's 剛上而柔下 and 咸's 柔上而剛下, after the passage 「參伍以變，錯綜其數」
(cuozong); the map's description names Y5. The other passages of the 傳's arrangements (the 序卦 within and between
pairs, the 雜卦, the 彖 of 損益, 泰否 and 既濟未濟, 繫辭下's 陽卦奇 and 說卦 ch. 3 and ch. 5) are in RO's map, quoted
from the atlas's preserved texts, and ro_passages.py adds Y5's declarations to them; verify_mapping.py checks the
module's 雜卦 sequence against the preserved 雜卦 and its stations against 說卦 ch. 5.
usage: python3 -B add_passages.py   (run once; it stops if any Y5 passage is already in passages.json)
The readings are AI readings (D47, D49); verify_mapping.py checks every fragment and declaration."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = HERE.parent / 'passages.json'
H = 'Becoming.Hexagram.'


def hx(*names):
    return [H + n for n in names]


AFTER_CUOZONG = [
    {'id': 'heng-gangshang', 'source': 'hexagrams/32.json', 'locator': '恒·彖',
     'fragments': ['剛上而柔下'],
     'kind': 'agreement',
     'declarations': hx('swap', 'yang_swap', 'across', 'passing', 'passUp', 'across_exchange', 'exchanges',
                        'named_exchanges', 'exchangesRun', 'exchangeWorld_balances', 'exchangeWorld_rise_fall')
                     + ['Becoming.World.balances_iff_exchange'],
     'reading': '恒是泰之初、四两爻相易：初九之刚上至四，六四之柔下至初，一阳爻自下卦入上卦。两爻相易保持阳爻之数；'
                '下卦与上卦之间的相易是两卦之间交换之律的一步，其所移即一阳上行、下行或无；一切相易之历程读为世界皆平衡，'
                '一卦之数每一升皆有所给，每一降皆有所取。損是泰之三、上两爻相易，同为一阳上行（損下益上），'
                '其彖见[中国思想章](CHINESE-SOURCES-AND-BECOMING.md#p-tuan-sun-yi)。'},
    {'id': 'xian-roushang', 'source': 'hexagrams/31.json', 'locator': '咸·彖',
     'fragments': ['柔上而剛下'],
     'kind': 'agreement',
     'declarations': hx('named_exchanges', 'passDown', 'three_iff', 'three_census', 'exchanges_keep',
                        'exchanges_run_total', 'exchanges_from_tai_pi'),
     'reading': '咸是否之三、上两爻相易：六三之柔上至上，上九之刚下至三，一阳爻自上卦入下卦；益是否之初、四两爻相易，'
                '同为一阳下行（損上益下）。三阳三阴之卦二十，恰是泰、否与由之下卦一爻、上卦一爻相易所得之十八卦，两两不同；'
                '自泰或否起，一切相易之历程不出此二十卦，两卦之数之和恒为三。彖于哪一卦取哪一种易，是读法，不在律中。'},
]

AFTER_DADE = []

data = json.loads(MAP.read_text())
ids = [p['id'] for p in data['passages']]
new_ids = [p['id'] for p in AFTER_CUOZONG + AFTER_DADE]
assert not set(new_ids) & set(ids), set(new_ids) & set(ids)
out = []
for p in data['passages']:
    out.append(p)
    if p['id'] == 'cuozong':
        out.extend(AFTER_CUOZONG)
    if p['id'] == 'dade':
        out.extend(AFTER_DADE)
assert len(out) == len(ids) + len(new_ids)
data['passages'] = out
old_about = 'The passage map of Y1, Y2, Y3 and Y4:'
assert data['about'].count(old_about) == 1
data['about'] = data['about'].replace(old_about, 'The passage map of Y1, Y2, Y3, Y4 and Y5:')
MAP.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('added', len(new_ids), 'passages;', len(out), 'in all')
