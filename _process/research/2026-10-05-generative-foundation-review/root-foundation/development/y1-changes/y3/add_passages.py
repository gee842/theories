#!/usr/bin/env python3
"""Y3 (19 October 2026): add the passages on the hexagram laws of Becoming.HexagramLaws to the passage map, after Y2's
passages and before Y1's divergences (the passage 「天尊地卑」 first among them), and widen four of Y1's passages to the
new declarations (孔穎達's 「非覆即變」, 《繫辭下》's 窮則變, 《繫辭上》's 太極 and 剝's 消息); verify_mapping.py also reads
names of Becoming.HexagramLaws from its source before they are in a receipt, as it does for Y1's and Y2's modules,
and the chapter's passage table is reprinted from the map.
usage: python3 -B add_passages.py   (run once; it stops if any Y3 passage is already in passages.json)
The readings are AI readings (D47); verify_mapping.py checks every fragment and declaration."""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = HERE.parent / 'passages.json'
H = 'Becoming.Hexagram.'
M = H + 'MarkedLines.'


def hx(*names):
    return [H + n for n in names]


NEW = [
    {'id': 'zhongyao', 'source': 'yizhuan/xici-xia.json', 'locator': '《繫辭下》第七章',
     'fragments': ['若夫雜物撰德，辨是與非，則非其中爻不備'], 'kind': 'agreement',
     'declarations': hx('nuclear', 'inner', 'nuclear_inner', 'run_inner', 'nuclear_merges', 'nuclear_loses'),
     'reading': '中爻是第二至第五爻。互卦以二、三、四爻为下卦，三、四、五爻为上卦：互之所成恰由中爻定，起点中爻相同的'
                '两个历程自第一步起即为一个历程；初、上两爻一步即失，此律合并，永失一种可能。“辨是與非”是判断，不在律中：'
                '律所说的只是互卦所读之处，恰是中爻。'},
    {'id': 'xugua-shouwei', 'source': 'yizhuan/xugua.json', 'locator': '《序卦》首尾',
     'fragments': ['有天地，然後萬物生焉', '物不可窮也，故受之以未濟；終焉'], 'kind': 'agreement',
     'declarations': hx('process_returns_iff_ends', 'nuclear_rests_iff', 'nuclear_two_fixed_one_cycle',
                        'run_in_attractor', 'entry_counts', 'basin_counts'),
     'reading': '互之律下恰有四个构形复返：乾、坤不变，既濟、未濟相代；一切构形至迟第二步即入此四者，不再离开，'
                '依三、四两爻，十六归乾，十六归坤，三十二入既濟、未濟之相代。此四者恰是所传卦序首二卦与末二卦。'
                '序卦以天地始，以未濟终而说“物不可窮”：互之律下，既濟、未濟相代而不止，不是静止。'},
    {'id': 'cuozong', 'source': 'yizhuan/xici-shang.json', 'locator': '《繫辭上》第十章',
     'fragments': ['參伍以變，錯綜其數'], 'kind': 'scope',
     'declarations': hx('Symmetry', 'Symmetry.act', 'Symmetry.act_comp', 'Symmetry.comp_self',
                        'Symmetry.comp_comm', 'nuclear_act', 'nuclear_run_act', 'run_complement_apart',
                        'classOf_eq_iff', 'class_census', 'classes_goAlike', 'classes_not_goAlike_waxWane'),
     'reading': '经文的“錯綜”说的是数的交错综合；以“錯”名六爻皆变、以“綜”名倒转，是后世注家之用（明来知德）。脊柱所证的是'
                '后者：不变、錯、綜、錯而綜四者成一群，各为自身之逆，两两可交换；互之律与四者皆可交换，故四者各把互的每一'
                '历程送为互的历程，一卦与其錯卦的历程永不相遇；六十四卦分为二十类，八类各二卦，十二类各四卦，互同行于诸类'
                '之上，消息之律则否：倒转使它逆行。'},
    {'id': 'yongjiu', 'source': 'hexagrams/01.json', 'locator': '乾·用九、象',
     'fragments': ['用九：見羣龍无首，吉', '用九，天德不可為首也'], 'kind': 'scope',
     'declarations': hx('Marked', 'Marked.settle') + [M + n for n in (
         'settle', 'shown', 'onward', 'all_nines', 'settle_merges', 'run_settled', 'returns_iff', 'drawn',
         'shown_not_goAlike', 'onward_goAlike')],
     'reading': '用九读作六爻皆为老阳（九）之时（《左傳》昭公二十九年称此辞为“乾之坤”，未存于本库）：老爻变为其反而不再变，'
                '少爻不变，一步即定，此后历程静止；所示本卦乾，自第一步起历程所示为坤（之卦）。律对任一卦之老少皆成立，'
                '用九只是六爻皆变之一例。本卦不是此律所同行的归并：本卦相同，之卦可异；之卦则是。“見羣龍无首”“吉”是象与'
                '判断，不在律中。'},
    {'id': 'yongliu', 'source': 'hexagrams/02.json', 'locator': '坤·用六、象',
     'fragments': ['用六：利永貞', '用六永貞，以大終也'], 'kind': 'scope',
     'declarations': [M + n for n in ('all_sixes', 'run_settled', 'returns_iff', 'onward')],
     'reading': '用六读作六爻皆为老阴（六）：所示本卦坤，自第一步起历程所示为乾。《象》“以大終”读作终于阳（乾）；'
                '“利永貞”是判断，不在律中。'},
]

WIDEN = {
    'feifu': (hx('turn_fixed_iff', 'both_fixed_iff'),
              '倒转不变者八卦（乾坤、頤大過、坎離、中孚小過），恰是卦序以變相配者；倒转与六爻皆变所得相同者，恰是卦序中'
              '覆、變两者兼合之对（泰否、隨蠱、漸歸妹、既濟未濟）。'),
    'qiong-bian': ([M + 'run_settled', M + 'run_rests'],
                   '之卦之律下，老爻（九、六）一变即为少爻，此后不再变：在此律之内，“窮”读作老，变之后即久。'),
    'taiji': (hx('addOne', 'addOne_one_orbit', 'line_turns'),
              '加一之律依次经过全部六十四构形而后复返，只此一轨；第 k 爻每 2^(k−1) 步一变：逐层之分读作数位。'),
    'shang-xiaoxi': (hx('changesAround', 'changesAround_values', 'changesAround_counts', 'qian_not_reach_jiJi',
                        'starts_return', 'orbit_census'),
                     '消息之律分六十四构形为六轨：五轨十二步，一轨四步；承、乘之数加首尾相同之处，沿每一历程不变，为一、三'
                     '或五，分别在十二、四十、十二个构形上，故乾不能至既濟。'),
}

data = json.loads(MAP.read_text())
passages = data['passages']
ids = [p['id'] for p in passages]
assert not any(p['id'] in ids for p in NEW), 'Y3 passages already present'
at = ids.index('tianzun')
data['passages'] = passages[:at] + NEW + passages[at:]
for p in data['passages']:
    if p['id'] in WIDEN:
        names, sentence = WIDEN[p['id']]
        assert not set(names) & set(p['declarations']), p['id']
        p['declarations'] = p['declarations'] + names
        p['reading'] = p['reading'] + sentence
# The items named at the head of the map, whichever landed before (Y4's script writes the same form).
named = re.match(r'The passage map of (.+?):', data['about'])
items = sorted(set(re.findall(r'Y\d+', named.group(1))) | {'Y3'}, key=lambda y: int(y[1:]))
data['about'] = data['about'].replace(named.group(0), 'The passage map of ' + ', '.join(items[:-1]) + ' and ' + items[-1] + ':')
MAP.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('added', len(NEW), 'widened', len(WIDEN), 'passages', len(data['passages']))

# verify_mapping.py: names of Becoming.HexagramLaws checked against its source until they are in a receipt.
VERIFY = HERE.parent / 'verify_mapping.py'
v = VERIFY.read_text()
for old, new in (
        ('onto the spine (Y1, Y2). usage', 'onto the spine (Y1, Y2, Y3). usage'),
        ('names of Becoming.Hexagrams and\n     Becoming.HexagramPlaces not yet in that receipt',
         'names of Becoming.Hexagrams,\n     Becoming.HexagramPlaces and Becoming.HexagramLaws not yet in that receipt'),
        ("    from_source = lean_declarations(module) | lean_declarations(places)\n",
         "    laws = PKG / 'Becoming/HexagramLaws.lean'\n"
         "    if not laws.exists():\n"
         "        laws = HERE / 'y3/Becoming/HexagramLaws.lean'\n"
         "    from_source = lean_declarations(module) | lean_declarations(places) | lean_declarations(laws)\n")):
    assert v.count(old) == 1, old
    v = v.replace(old, new)
VERIFY.write_text(v)
print('verify_mapping.py reads Becoming.HexagramLaws')


# The chapter's passage table, reprinted from the map between its markers (verify_mapping.py --table).
table = subprocess.run([sys.executable, '-B', str(VERIFY), '--table'], capture_output=True, text=True, check=True).stdout
CHAPTER = HERE.parents[6] / 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
BEGIN, END = '<!-- passage-map:begin -->', '<!-- passage-map:end -->'
chapter = CHAPTER.read_text()
assert chapter.count(BEGIN) == 1 and chapter.count(END) == 1
start, stop = chapter.index(BEGIN) + len(BEGIN), chapter.index(END)
CHAPTER.write_text(chapter[:start] + '\n' + table.rstrip('\n') + '\n' + chapter[stop:])
print('chapter table reprinted')
