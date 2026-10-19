#!/usr/bin/env python3
"""Y2 (19 October 2026): add the passages on the relations of the places to the passage map, after the passage
「天下之動，貞夫一者也」 and before Y1's divergences, and widen two of Y1's passages to the new declarations.
usage: python3 -B add_passages.py   (run once; it stops if any Y2 passage is already in passages.json)
The readings are AI readings (D47, D49); verify_mapping.py checks every fragment and declaration."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = HERE.parent / 'passages.json'
H = 'Becoming.Hexagram.'


def hx(*names):
    return [H + n for n in names]


NEW = [
    {'id': 'dieyong-gangrou', 'source': 'yizhuan/shuogua.json', 'locator': '《說卦》第二章',
     'fragments': ['分陰分陽，迭用柔剛，故易六位而成章'], 'kind': 'agreement',
     'declarations': hx('odd', 'odd_above', 'inPhase', 'inPhase_all_iff', 'alternates_all_iff'),
     'reading': '六位奇偶相间：每一相邻两位，奇偶相反。一爻之值与其位之奇偶相合为正；六爻皆正恰是既濟，'
                '每一相邻两爻皆相异恰是既濟与未濟。'},
    {'id': 'zhengwei', 'source': 'hexagrams/63.json', 'locator': '既濟·彖',
     'fragments': ['剛柔正而位當也'], 'kind': 'agreement',
     'declarations': hx('inPhase', 'jiJi_inPhase', 'inPhase_all_iff', 'atSites', 'phases_glue_iff'),
     'reading': '正是一爻与其位的关系，在位上成立。各位之正读作一个带语境的读法，它粘合为对整卦的一个读法，'
                '恰在六爻皆正（既濟）或皆不正（未濟）之处；彖于既濟说整卦“剛柔正而位當”，正在其一。'},
    {'id': 'weiji-ying', 'source': 'hexagrams/64.json', 'locator': '未濟·彖',
     'fragments': ['雖不當位，剛柔應也'], 'kind': 'scope',
     'declarations': hx('weiJi_out_of_phase', 'weiJi_opposed', 'opposed_iff_phase', 'out_of_phase_opposed'),
     'reading': '同一高度的两位奇偶相反，所以两爻相应，恰当二者同正或同不正；六爻皆不当位，三对便皆相应。'
                '“雖”把两者读作相反，律中则是前者蕴涵后者。'},
    {'id': 'heng-jieying', 'source': 'hexagrams/32.json', 'locator': '恒·彖',
     'fragments': ['剛柔皆應'], 'kind': 'agreement',
     'declarations': hx('opposed', 'heng_opposed', 'oppositions_glue_iff'),
     'reading': '恒三个高度皆相应，下卦是上卦之错；各高度之应在此粘合为对整卦的一个读法。'},
    {'id': 'xian-ganying', 'source': 'hexagrams/31.json', 'locator': '咸·彖',
     'fragments': ['二氣感應以相與'], 'kind': 'agreement',
     'declarations': hx('xian_opposed', 'oppositions_glue_iff', 'halves_glues_iff'),
     'reading': '咸三个高度皆相应：以上下两卦为两个语境，每一高度两卦所示皆相异。“相與”在此读作经由相异而相应，'
                '不读作两卦合一。'},
    {'id': 'gen-diying', 'source': 'hexagrams/52.json', 'locator': '艮·彖',
     'fragments': ['上下敵應，不相與也'], 'kind': 'agreement',
     'declarations': hx('halves', 'halves_glues_iff', 'gen_halves_glue', 'halves_no_free_frame', 'halves_indexed')
     + ['Becoming.Contextual.indexed_fits'],
     'reading': '敵應：每一高度两爻相同，上下两卦作为语境处处所示一致而粘合，没有一处相应，故“不相與”。'
                '相应之处，一个高度之爻在两卦中是两个主张；没有去语境的读法合于所有构形，带语境索引的读法则合。'},
    {'id': 'gangzhong-erying', 'source': 'hexagrams/07.json', 'locator': '師·彖',
     'fragments': ['剛中而應'], 'kind': 'agreement',
     'declarations': hx('middleUnbrokenOpposed', 'middleUnbrokenOpposed_eq', 'middleBrokenOpposed_eq',
                        'middleOppositionStatements', 'middleOppositionStatements_agree'),
     'reading': '彖言“剛中而應”者五卦：師、臨、无妄、萃、升；检查脚本在所存六十四页中找出全部五处，每卦居中之阳爻皆有应。'
                '剛中而應恰是中之高度相应，与“柔中而應”所指相同：一个关系，从其两端读。'},
    {'id': 'tongren-dezhong', 'source': 'hexagrams/13.json', 'locator': '同人·彖',
     'fragments': ['柔得位得中，而應乎乾'], 'kind': 'agreement',
     'declarations': hx('tongRen_second', 'inPhase', 'middle', 'opposed'),
     'reading': '六二为阴，当位，居中，其高度与上卦乾之九五相应。'},
    {'id': 'xiaoxu-shangxia', 'source': 'hexagrams/09.json', 'locator': '小畜·彖',
     'fragments': ['柔得位而上下應之'], 'kind': 'scope',
     'declarations': hx('xiaoXu_fourth', 'opposed'),
     'reading': '六四为阴而当位；以对应之位论，只初九与之相应，中、上两个高度不相应。“上下應之”读的是一个阴爻与其余五个阳爻的关系，'
                '不是对应之位，此关系不在模块之中。'},
    {'id': 'dayou-zunwei', 'source': 'hexagrams/14.json', 'locator': '大有·彖',
     'fragments': ['柔得尊位，大中而上下應之'], 'kind': 'divergence',
     'declarations': hx('daYou_fifth', 'middle', 'inPhase', 'opposed'),
     'reading': '六五居中而不当位，只中之高度与九二相应。“尊位”是位的等级，理论不采（与《繫辭》“貴賤”之相分同）；'
                '“上下應之”与小畜同，不是对应之位。'},
    {'id': 'guimei-chenggang', 'source': 'hexagrams/54.json', 'locator': '歸妹·彖',
     'fragments': ['柔乘剛也'], 'kind': 'agreement',
     'declarations': hx('falls', 'guiMei_falls', 'rises_falls_ends'),
     'reading': '六三在九二之上，六五在九四之上，两处柔乘刚。自下而上，阳之起（承）与落（乘）次数之差由首尾两爻定：'
                '承之数加初爻，等于乘之数加上爻。'},
    {'id': 'guai-chengwugang', 'source': 'hexagrams/43.json', 'locator': '夬·彖',
     'fragments': ['柔乘五剛也'], 'kind': 'scope',
     'declarations': hx('guai_falls', 'falls'),
     'reading': '以相邻之位论，上六只乘九五一刚，诸位之间只此一处落；“乘五剛”读的是一阴在五阳之上的整体，比相邻关系宽。'},
    {'id': 'lv-weibudang', 'source': 'hexagrams/10.json', 'locator': '履·六三·象',
     'fragments': ['咥人之凶，位不當也'], 'kind': 'agreement',
     'declarations': hx('placeStatements', 'placeStatements_agree', 'inPhase', 'xu_top_inPhase'),
     'reading': '小象明言位者二十七处（位不當、不當位、未當位、未得位；位正當、位當、當位），检查脚本在所存六十四页中逐一找出：'
                '二十六处与其爻是否当位相合，皆在三、四、五位；只有需上六一处相分（见下）。“凶”是判断，不在律中。'},
    {'id': 'xu-shangliu', 'source': 'hexagrams/05.json', 'locator': '需·上六·象',
     'fragments': ['雖不當位，未大失也'], 'kind': 'divergence',
     'declarations': hx('xu_top_inPhase', 'inPhase'),
     'reading': '上六阴居偶位，依奇偶是当位，象却说不当位。王弼《周易略例·辯位》以此句为初、上两位无定位之证'
                '（该文未存于本库，未核对）。模块对六位一律以奇偶定正，不采“初上无位”之读，所以此处相分。'},
    {'id': 'xu-zhongzheng', 'source': 'hexagrams/05.json', 'locator': '需·九五·象',
     'fragments': ['酒食，貞吉，以中正也'], 'kind': 'agreement',
     'declarations': hx('centreStatements', 'centreStatements_agree', 'middle', 'inPhase', 'gen_fifth_out_of_phase'),
     'reading': '小象言“中正”“正中”者十处，检查脚本逐一找出：九处是居中而当位之爻；只有艮六五一处相分（见下）。'},
    {'id': 'gen-zhongzheng', 'source': 'hexagrams/52.json', 'locator': '艮·六五·象',
     'fragments': ['艮其輔，以中正也'], 'kind': 'divergence',
     'declarations': hx('gen_fifth_out_of_phase', 'middle', 'inPhase'),
     'reading': '六五居中，阴居奇位，依奇偶不当位，象却说中正：此处的“正”读作因得中而正，不是位之奇偶。'
                '模块不以中代正，所以相分。'},
    {'id': 'tun-chenggang', 'source': 'hexagrams/03.json', 'locator': '屯·六二·象',
     'fragments': ['六二之難，乘剛也'], 'kind': 'agreement',
     'declarations': hx('fallStatements', 'fallStatements_agree', 'falls'),
     'reading': '小象言“乘剛”者五处（屯六二、豫六五、噬嗑六二、困六三、震六二），检查脚本逐一找出：每处都是阴爻在阳爻之上，'
                '即其下之缝为落。'},
    {'id': 'liuwei-shicheng', 'source': 'hexagrams/01.json', 'locator': '乾·彖',
     'fragments': ['大明終始，六位時成'], 'kind': 'scope',
     'declarations': hx('line_waxWane_above', 'inPhase_waxWane_above', 'phaseCount_parity', 'phase_qian_orbit'),
     'reading': '消息之律下，每爻逐步升经六位，其值不变，其正每升一位即翻转：一爻所示依其所处之位与时。'
                '当位之数每步改变奇偶，自乾十二步为三、二、三、二、三、二、三、四、三、四、三、四。“大明”之读不在律中。'},
    {'id': 'tonggong-yiwei', 'source': 'yizhuan/xici-xia.json', 'locator': '《繫辭下》第八章',
     'fragments': ['二與四同功而異位，其善不同：二多譽，四多懼，近也'], 'kind': 'scope',
     'declarations': hx('odd', 'heightOf', 'middle', 'Seam'),
     'reading': '二、四同为偶位（同功）；二居下卦之中，四居上卦之下（異位）。“多譽”“多懼”是判断，'
                '“近”指四近于五，皆不在模块之中。'},
    {'id': 'wen-budang', 'source': 'yizhuan/xici-xia.json', 'locator': '《繫辭下》第八章',
     'fragments': ['道有變動，故曰爻；爻有等，故曰物；物相雜，故曰文；文不當，故吉凶生焉'], 'kind': 'divergence',
     'declarations': hx('inPhase', 'atSites_glues_iff') + ['Becoming.Web.significance_undetermined'],
     'reading': '爻与位相当与否，是带位之索引的关系（正）。“爻有等”是等级；“文不當，故吉凶生焉”把不当读作吉凶之源。'
                '律中的关系不带判断，动力学不决定意义。'},
]

WIDEN = {
    'liuyao-xiangza': (hx('halves_indexed', 'atSites_glues_iff', 'inPhase_waxWane_above'),
                       '一爻之义随其位与时：带语境索引的框架合于所示的一切；各语境所示能粘合，恰当它们在相接处一致。'
                       '爻位之间的关系（正、应、比、中）都在位上成立：同一爻沿消息之律升一位，其正即翻转。'),
    'guijian': (hx('odd', 'middle'),
                '位有别，是语境之索引：三、五同为奇位（同功），五居中而三不居中（異位）；位无等级。'),
}

data = json.loads(MAP.read_text())
passages = data['passages']
ids = {p['id'] for p in passages}
assert not ids & {p['id'] for p in NEW}, 'Y2 passages already present'
at = next(i for i, p in enumerate(passages) if p['id'] == 'zhen-fu-yi') + 1
passages[at:at] = NEW
for p in passages:
    if p['id'] in WIDEN:
        more, reading = WIDEN[p['id']]
        p['declarations'] += [d for d in more if d not in p['declarations']]
        p['reading'] = reading
data['about'] = data['about'].replace("Y1's passage map:", "The passage map of Y1 and Y2:")
MAP.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('added', len(NEW), 'passages; widened', len(WIDEN), '; now', len(passages))
