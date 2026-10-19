#!/usr/bin/env python3
"""Y5 (19 October 2026): add the passages of the 傳's arrangements to the passage map of the 易传 chapter: the 序卦
between pairs and its 剝窮上反下, the 彖 of 損, 益, 恒, 咸, 泰, 否 and 既濟, 繫辭下's 陽卦奇，陰卦偶 and 說卦 ch. 3 and
ch. 5. The agreements and exact scopes go after the passage 「參伍以變，錯綜其數」 (cuozong), the divergence of 說卦
ch. 5 after 「天地之大德曰生」 (dade), before the divergence of 大衍; the map's description names Y5.
The 雜卦 is not among the preserved Wikisource pages of the 易传 chapter; its passages are in RO's map, quoted from the
atlas's preserved text, and verify_mapping.py checks the module's 雜卦 sequence against that text.
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
    {'id': 'xugua-xiangshou', 'source': 'yizhuan/xugua.json', 'locator': '《序卦》',
     'fragments': ['履而泰，然後安，故受之以泰；泰者通也', '物不可以終通，故受之以否',
                   '物不可以終否，故受之以同人'],
     'kind': 'scope',
     'declarations': hx('RunsOrder', 'orderNext', 'orderNext_runsOrder', 'runsOrder_agrees',
                        'runsOrder_lossless_iff', 'orderNext_one_orbit', 'runsOrder_reads',
                        'runsOrder_blind_not_lumped', 'ringRule_not_runsOrder', 'twistedRule_not_runsOrder',
                        'waxWane_not_runsOrder', 'runsOrder_not_commutes', 'rearrange_not_runsOrder',
                        'runsOrder_not_lumped'),
     'reading': '序卦以事理说每一卦之所受。所传卦序是一个律的运行：取每卦至其后一卦、未濟至乾之律（orderNext）；'
                '运行此序之律除未濟一处外皆与之相同，其中恰此一律不合并，自乾六十四步首次复返，历经全部构形。'
                '但运行此序之律，每一爻皆读每一爻：改任一爻，后一卦之任一爻在某一构形上随之而变；'
                '所以没有三格之环律（直读或扭转，消息之律在其中）运行此序；每对之内是錯、綜或二者之一步，'
                '与其交换之律下一步即返，所以运行此序之律不与錯、綜或二者交换，重排爻位加掩码之律皆与錯交换，'
                '无一运行此序；它也不同行于对或阳爻数之奇偶。卦序是一张表，不是一个只读部分构形或保持对称之律；'
                '序卦所给的是言中之理，不在律中。本章 §8 此前说“卦序本身不是任何律的轨道”，不确，今改。'},
    {'id': 'xugua-bo-fu', 'source': 'yizhuan/xugua.json', 'locator': '《序卦》',
     'fragments': ['物不可以終盡，剝窮上反下，故受之以復'],
     'kind': 'agreement',
     'declarations': hx('bo', 'fu', 'bo_fu', 'ringRule', 'twistedRule', 'waxWane_twisted'),
     'reading': '剝窮上反下：各爻上升一位、上爻不变而入初位，是直读之环上的移位，一步即由剝至復，与倒转剝所得相同。'
                '消息之律是扭转之环：上爻入初时变其刚柔，由剝一步至坤，再一步至復。序卦此句所说之移是直环之移，'
                '不是消息之一步。“物不可以終盡”是一般之断言，脊柱只在此一步上检查。'},
    {'id': 'sun-xiashang', 'source': 'hexagrams/41.json', 'locator': '損·彖',
     'fragments': ['損下益上，其道上行'],
     'kind': 'agreement',
     'declarations': hx('swap', 'yang_swap', 'across', 'passing', 'passUp', 'across_exchange', 'exchanges',
                        'named_exchanges', 'exchangesRun', 'exchangeWorld', 'exchangeWorld_balances',
                        'exchangeWorld_rise_fall') + ['Becoming.World.balances_iff_exchange'],
     'reading': '損是泰之三、上两爻相易：一阳爻自下卦入上卦，下卦之阳数减一，上卦增一，阳爻总数不变。'
                '两爻相易保持阳爻之数；下卦与上卦之间的相易，是二者之间交换之律的一步，其所移即一阳上行、下行或无。'
                '一切相易之历程读为世界皆平衡：一卦之数每一升皆有所给，每一降皆有所取。“其道上行”在此是阳爻自下而上。'},
    {'id': 'yi-shangxia', 'source': 'hexagrams/42.json', 'locator': '益·彖',
     'fragments': ['損上益下，民說无疆'],
     'kind': 'agreement',
     'declarations': hx('named_exchanges', 'passDown', 'across_exchange', 'exchanges_keep', 'exchanges_run_total'),
     'reading': '益是否之初、四两爻相易：一阳爻自上卦入下卦，上卦之数减一，下卦增一。沿一切相易之历程，'
                '两卦之数之和恒为起点之阳爻数。“民說无疆”是判断，不在律中。'},
    {'id': 'heng-gangshang', 'source': 'hexagrams/32.json', 'locator': '恒·彖',
     'fragments': ['剛上而柔下'],
     'kind': 'agreement',
     'declarations': hx('named_exchanges', 'across', 'passing'),
     'reading': '恒是泰之初、四两爻相易：初九之刚上至四，六四之柔下至初，一阳上行。'},
    {'id': 'xian-roushang', 'source': 'hexagrams/31.json', 'locator': '咸·彖',
     'fragments': ['柔上而剛下'],
     'kind': 'agreement',
     'declarations': hx('named_exchanges', 'three_iff', 'three_census', 'exchanges_from_tai_pi'),
     'reading': '咸是否之三、上两爻相易：六三之柔上至上，上九之刚下至三，一阳下行。三阳三阴之卦二十，'
                '恰是泰、否与由之下卦一爻、上卦一爻相易所得之十八卦，两两不同；自泰或否起，一切相易之历程不出此二十卦。'
                '彖于哪一卦取哪一种易，是读法，不在律中。'},
    {'id': 'tai-jiao', 'source': 'hexagrams/11.json', 'locator': '泰·彖',
     'fragments': ['則是天地交而萬物通也'],
     'kind': 'scope',
     'declarations': hx('meets', 'meets_tai_pi', 'pi_of_tai', 'kept_alike', 'tai_pi_runs')
                     + ['Becoming.Law.Commutes.iterate'],
     'reading': '交：同一高度下卦之爻为阳、上卦之爻为阴（天在下而地在上）。泰三个高度皆交，否皆不交。'
                '否是泰之錯，也是泰之綜，所以凡为錯所保持之读法，应、比、对、阳爻数之奇偶，'
                '在自泰与自否之消息历程上每一步都相同；交不为錯所保持，在两值之间读出一个方向，才把泰否分开。'
                '“萬物通”是判断，不在律中。'},
    {'id': 'pi-bujiao', 'source': 'hexagrams/12.json', 'locator': '否·彖',
     'fragments': ['則是天地不交而萬物不通也'],
     'kind': 'scope',
     'declarations': hx('meets', 'meets_tai_pi', 'tai_pi_runs'),
     'reading': '否三个高度皆不交；其余为錯所保持之读法皆与泰相同（见泰·彖）。“萬物不通”是判断，不在律中。'},
    {'id': 'jiji-zhongzhi', 'source': 'hexagrams/63.json', 'locator': '既濟·彖',
     'fragments': ['終止則亂，其道窮也'],
     'kind': 'agreement',
     'declarations': hx('waxWane_moves', 'run_never_rests', 'never_comes_to_rest', 'changes_run_never_rests',
                        'six_steps', 'complement_moves'),
     'reading': '消息之律下没有不动之卦：六步即为其錯，而錯移动每一构形；所以消息之运行在任何一步都不止，'
                '也不会自某步起止，既濟亦然；一爻之变的每一步都移动构形。“則亂”是判断，不在律中；'
                '律所示的是：在这两个律下，止不是可到达的状态。'},
    {'id': 'yanggua-qi', 'source': 'yizhuan/xici-xia.json', 'locator': '《繫辭下》第三章',
     'fragments': ['陽卦多陰，陰卦多陽，其故何也？陽卦奇，陰卦偶'],
     'kind': 'agreement',
     'declarations': hx('count3', 'strokes3', 'odd3_iff', 'trigramOf', 'halfYang_trigram', 'trigramOdd',
                        'trigramOdd_flip', 'changes_run_trigram', 'yangOdd', 'yangOdd_lumped', 'yangOdd_goAlike',
                        'yangOdd_goAlike_changes', 'run_yangOdd', 'changes_run_yangOdd'),
     'reading': '三爻之阳爻数为奇者，恰是乾与震、坎、艮（坤变一爻）；为偶者，恰是坤与巽、離、兌（乾变一爻）。'
                '以笔画计，阴爻二画，画数与阳爻数之和为六，奇偶相同。“多陰”只合震、坎、艮，乾亦奇而不多陰。'
                '一爻之变使其所在之卦由阳卦为阴卦或反之，另一卦之类不变。六爻阳爻数之奇偶是消息之律与一爻之变皆通行之归并，'
                '阳爻数本身不是。“其德行”以下君子小人之说是判断，不在律中。'},
    {'id': 'shuogua-dingwei', 'source': 'yizhuan/shuogua.json', 'locator': '《說卦》第三章',
     'fragments': ['天地定位，山澤通氣，雷風相薄，水火不相射'],
     'kind': 'agreement',
     'declarations': hx('Trigram.complement3', 'Trigram.opposite_stations'),
     'reading': '第三章四对：乾坤、艮兌、震巽、坎離，每对皆为錯（三爻皆变）。'},
]

AFTER_DADE = [
    {'id': 'shuogua-dichu', 'source': 'yizhuan/shuogua.json', 'locator': '《說卦》第五章',
     'fragments': ['帝出乎震，齊乎巽，相見乎離，致役乎坤，說言乎兌，戰乎乾，勞乎坎，成言乎艮'],
     'kind': 'divergence',
     'declarations': hx('Trigram.stations', 'Trigram.stations_not_commutes', 'Trigram.ringRule3_rotate',
                        'Trigram.stations_not_rules', 'Trigram.opposite_stations'),
     'reading': '八站之序：运行此序之律不与錯、綜、錯而綜或三爻之轮转交换，所以没有三格环律（直读或扭转）运行此序。'
                '环上相对之四对，只有離坎为錯，而第三章之四对皆为錯。此序依时令与方位而排，是指派，不是爻之关系之律；'
                '脊柱不断言其指派。传文自解“帝”为万物之出，不读为一个意志之主。'},
]

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
