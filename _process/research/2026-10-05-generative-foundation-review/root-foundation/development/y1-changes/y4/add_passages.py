#!/usr/bin/env python3
"""Y4 (19 October 2026): add the passages of 王弼's 《周易略例》 and of the new censuses (the 彖's whole
statements of place, 上下應, the 爻辭's 中 and 位, the 大象's 中, the 小象's 中) to the passage map, after
the passage 「二與四同功而異位」 and before the divergences of Y2, and revise five passages of Y2 to the
relations of Becoming.HexagramSites.
usage: python3 -B add_passages.py   (run once; it stops if any Y4 passage is already in passages.json)
The readings are AI readings (D47, D49); verify_mapping.py checks every fragment and declaration.
Only 明彖 marks 王弼's text in the stored edition; in the other pages 王弼's paragraphs and 邢璹's notes
alternate, and every fragment below is from a paragraph of 王弼's."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = HERE.parent / 'passages.json'
H = 'Becoming.Hexagram.'


def hx(*names):
    return [H + n for n in names]


NEW = [
    {'id': 'jian-dangwei', 'source': 'hexagrams/39.json', 'locator': '蹇·彖',
     'fragments': ['當位貞吉，以正邦也'], 'kind': 'agreement',
     'declarations': hx('tuanWholeStatements', 'tuanWhole_between', 'tuanWhole_six', 'allHold_iff', 'jian3',
                        'holdsPlace'),
     'reading': '彖言整卦之位者五处（蹇“當位”、漸“進得位”、歸妹“位不當”、既濟“剛柔正而位當”、未濟“不當位”），'
                '检查脚本在所存六十四页中逐一找出。以二至五位读，五处皆合；以六位之奇偶读，只既濟、未濟两处合：'
                '蹇、漸初爻不当位，漸上爻亦然。中间四爻皆当位者恰是既濟、蹇、漸、家人四卦，彖于四卦皆言位或正。'
                '“貞吉”“正邦”是判断，不在律中。'},
    {'id': 'guimei-weibudang', 'source': 'hexagrams/54.json', 'locator': '歸妹·彖',
     'fragments': ['征凶，位不當也'], 'kind': 'agreement',
     'declarations': hx('noneHold_iff', 'tuanWhole_between', 'tuanWhole_six', 'holdsPlace'),
     'reading': '歸妹中间四爻皆不当位；中间四爻皆不当位者恰是未濟、歸妹、解、睽四卦。其初九、上六依六位之奇偶反而当位，'
                '所以此句只在初上无位之读下对整卦成立。“征凶”是判断，不在律中。'},
    {'id': 'bi-shangxiaying', 'source': 'hexagrams/08.json', 'locator': '比·彖',
     'fragments': ['不寧方來，上下應也'], 'kind': 'agreement',
     'declarations': hx('answeredStatements', 'answeredStatements_sole', 'sole', 'sole_answered', 'sole_unique'),
     'reading': '彖言“上下應”者三处（比、小畜、大有），检查脚本逐一找出：每处所说之爻都是卦中唯一之阳爻或阴爻'
                '（比九五、小畜六四、大有六五），与其余五爻皆相异，其余五爻亦各与之相应。这是一爻与其余诸爻之关系，'
                '比对应之位宽；有此一爻之卦恰十二，其爻唯一。'},
    {'id': 'cui-youwei', 'source': 'hexagrams/45.json', 'locator': '萃·九五',
     'fragments': ['萃有位，无咎'], 'kind': 'agreement',
     'declarations': hx('lineTextPlace', 'lineTextPlace_holds', 'holdsPlace', 'middle'),
     'reading': '爻辭明言位者只此一处，检查脚本在所存六十四页之爻辭中找出：九五居中，阳居奇位，当位，在初上之间而有定位。'
                '“无咎”是判断，不在律中。'},
    {'id': 'tai-zhongxing', 'source': 'hexagrams/11.json', 'locator': '泰·九二',
     'fragments': ['得尚于中行'], 'kind': 'scope',
     'declarations': hx('lineTextMiddle', 'middleCourseLines', 'lineTextMiddle_places', 'betweenEnds', 'middle'),
     'reading': '爻辭言“中”者十一爻，检查脚本逐一找出：皆在二至五位，初上无一；其中居中者五（師九二、泰九二、家人六二、'
                '夬九五、豐六二）。言“中行”者五爻（泰九二、復六四、益六三、益六四、夬九五），居中者只泰九二、夬九五：'
                '爻辭之“中”多是中间，不都是居中之位。'},
    {'id': 'xu-yanzaizhong', 'source': 'hexagrams/05.json', 'locator': '需·九二·象',
     'fragments': ['需于沙，衍在中也'], 'kind': 'scope',
     'declarations': hx('middle', 'betweenEnds'),
     'reading': '小象言“中”者五十一爻，检查脚本逐一找出：四十七爻居中（二、五位）；其余四处不是居中之读：泰六四“中心”、'
                '復六四“中行”、震上六“中未得”、豐九四“日中”。需九二居中。'},
    {'id': 'shi-daxiang', 'source': 'hexagrams/07.json', 'locator': '師·象',
     'fragments': ['地中有水，師'], 'kind': 'scope',
     'declarations': hx('halves', 'middle'),
     'reading': '大象言“中”者八处（師、謙、隨、復、大畜、明夷、升、革），检查脚本逐一找出：每处都是下卦之象在上卦之象之中，'
                '是上下两体之关系，不是居中之位；言“位”者二处（鼎“正位凝命”、艮“思不出其位”），是君子之位，不是爻位。'
                '大象不言爻位之关系。'},
    {'id': 'lueli-bianwei-top', 'source': 'lueli/bianwei.json', 'locator': '王弼《周易略例·辯位》',
     'fragments': ['唯《乾》上九《文言》雲：「貴而無位」，《需》上六雲：「雖不當位」。若以上為陰位邪？'
                   '則《需》上六不得雲不當位也。若以上陽位邪？則《乾》上九不得雲貴而無位也'],
     'kind': 'agreement',
     'declarations': hx('top_no_parity', 'qian_top', 'xu_top_no_place', 'fixedPhase', 'holdsPlace'),
     'reading': '王弼之两难：乾上九为阳，需上六为阴，文言与小象皆说其不在位；给上位任一奇偶，二者必有一个当位，'
                '没有一个奇偶使二者都不当位。以初上无位读之，二者皆不在位。所存本“云”作“雲”，照录。'},
    {'id': 'lueli-bianwei-noplace', 'source': 'lueli/bianwei.json', 'locator': '王弼《周易略例·辯位》',
     'fragments': ['《象》無初上得位失位之文，又《系辭》但論三五、二四同功異位，亦不及初上',
                   '初上無陰陽定位，亦以明矣'],
     'kind': 'agreement',
     'declarations': hx('betweenEnds', 'fixedPhase', 'fixedPhase_end', 'holdsPlace_iff', 'holdsPlace_ends',
                        'placeStatements_between', 'placeStatements_hold', 'statements_fix_parity',
                        'centre_fixes_parity'),
     'reading': '第二个关系：二至五位依奇偶有定位，初、上无定位，在两端之爻不在位。小象明言位者二十六处在三、四、五位，'
                '无一在初；需上六一处在上。以此读之，二十七处与文言乾上九“貴而无位”皆相合，没有例外。'
                '二至五位之奇偶亦由所言之位定出：小象之言定三、四、五位，中正之言定二位，与奇偶相合。'},
    {'id': 'lueli-bianwei-zhongshi', 'source': 'lueli/bianwei.json', 'locator': '王弼《周易略例·辯位》',
     'fragments': ['然事不可無終始，卦不可無六爻，初上雖無陰陽本位，是終始之地也',
                   '卦以六爻為成，則不得不謂之六位時成也'],
     'kind': 'agreement',
     'declarations': hx('fixedPhase_waxWane_enters', 'changes_run_ends', 'sole_top_passes', 'sole_six',
                        'sole_waxWane_none', 'run_between_six'),
     'reading': '初、上无定位，却是一爻进入与离开之处：消息之律下，新爻自初位入，升至二位才取得定位之正；'
                '一爻在初或上变动，二至五位之定位皆不变，只改变其旁之应与比。一爻对其余五爻之独应不能延续一步，六步后复回；'
                '在上之独爻升出，留下六爻皆同之卦，两步后自初位复入：终始之地。'},
    {'id': 'lueli-shibian-xiang', 'source': 'lueli/minggua-shibian-tongyao.json',
     'locator': '王弼《周易略例·明卦適變通爻》',
     'fragments': ['夫應者，同誌之象也；位者，爻所處之象也；承乘者，逆順之象也；遠近者，險易之象也；'
                   '內外者，出處之象也；初上者，始終之象也'],
     'kind': 'scope',
     'declarations': hx('opposed', 'holdsPlace', 'rises', 'falls', 'halves', 'betweenEnds', 'answers',
                        'sole_top_passes'),
     'reading': '六种关系在律中各有其结构：應是同一高度两爻相异；位是二至五位上爻与奇偶相合；承乘是缝之起落；'
                '內外是上下两体；初上是无定位之两端，一爻自此入、自此出。遠近只是两位之距，律中两爻之关系不依距离。'
                '“同志”“逆順”“險易”“出處”是读法，不在律中。'},
    {'id': 'lueli-tongbian-yingbi', 'source': 'lueli/mingyao-tongbian.json', 'locator': '王弼《周易略例·明爻通變》',
     'fragments': ['近不必比，遠不必乖。同聲相應，高下不必均也'], 'kind': 'agreement',
     'declarations': hx('answers', 'answers_symm', 'opposed_answers', 'alternates_answers', 'opposed'),
     'reading': '两爻之相应只依其值相异，不依其距：对应之位（相距三）之应与相邻之比，是同一关系在不同两位上的读法，'
                '近者不必相应，远者可以相应。邢璹注以初四、二五、三上为“同聲相應”：在两体中同一高度，'
                '高下在不同之体。'},
    {'id': 'lueli-mingtuan-zhu', 'source': 'lueli/mingtuan.json', 'locator': '王弼《周易略例·明彖》',
     'fragments': ['一卦五陽而一陰，則一陰為之主矣。五陰而一陽，則一陽為之主矣',
                   '故陰爻雖賤，而為一卦之主者，處其至少之地也'],
     'kind': 'agreement',
     'declarations': hx('sole', 'sole_count', 'soleAny_count', 'sole_unique', 'sole_iff_flip', 'sole_places',
                        'sole_any_phase'),
     'reading': '一爻与其余五爻皆相异，恰在五阳一阴或五阴一阳之卦；此爻唯一，十二卦即纯卦之一爻变，六位各二。'
                '十二之中，在二至五位而当位者四，不当位者四，在初上者四：此关系不依位与正。“主”在此读作其余诸爻皆与之相应之爻；'
                '“賤”是等级，不在律中。'},
    {'id': 'lueli-xia-yiti', 'source': 'lueli/lueli-xia.json', 'locator': '王弼《周易略例·略例下》',
     'fragments': ['凡《彖》者，通論一卦之體者也。一卦之體，必由一爻為主。則指明一爻之美，以統一卦之義，大有之類是也。'
                   '卦體不由乎一爻，則全以二體之義明之，豐卦之類是也'],
     'kind': 'scope',
     'declarations': hx('daYou_answered', 'feng_no_sole', 'soleAny_count', 'none_sole', 'halves'),
     'reading': '大有六五与其余五爻皆相异；豐无此爻，彖以上下两体读之。律中有独应之爻者只十二卦，其余五十二卦没有：'
                '“必由一爻為主”在此十二卦成立；王弼于他卦所举之主（居中、得位、有应之爻）是其他关系。'
                '“美”“統”不在律中。'},
    {'id': 'lueli-lv', 'source': 'lueli/lueli-xia.json', 'locator': '王弼《周易略例·略例下》',
     'fragments': ['故《履》卦六三，為為兌之主，以應於《乾》。成卦之體，在斯一爻'], 'kind': 'agreement',
     'declarations': hx('lv_sole', 'sole', 'answeredStatements_sole'),
     'reading': '履六三是卦中唯一之阴爻，与其余五爻皆相异；彖“說而應乎乾”读作此爻与上体乾之三爻皆相应。'
                '所存本作“為為兌之主”，衍一“為”字，照录。'},
    {'id': 'lueli-mingxiang', 'source': 'lueli/mingxiang.json', 'locator': '王弼《周易略例·明象》',
     'fragments': ['得意在忘象，得象在忘言', '義茍在健，何必馬乎？類茍在順，何必牛乎？'], 'kind': 'scope',
     'declarations': ['Becoming.Learning.goAlike_iff_lumped']
     + hx('pairs_goAlike', 'yang_not_goAlike', 'betweenPhases_not_goAlike'),
     'reading': '意读作一个读法所能跟随者：一个读法可以只记其值而忘其构形，恰当律沿此读法同行（可归并）。一卦与其错之对是这样的读法；'
                '阳爻之数不是，二至五位之定位之正亦不是，后者须看初位所入之爻。“得意忘象”在律中只对同行之读法成立；'
                '马、牛之类的象不在模块之中。'},
    {'id': 'lueli-bianwei-rank', 'source': 'lueli/bianwei.json', 'locator': '王弼《周易略例·辯位》',
     'fragments': ['夫位者，列貴賤之地，待才用之宅也', '位有尊卑，爻有陰陽'], 'kind': 'divergence',
     'declarations': hx('holdsPlace', 'atSites_glues_iff') + ['Becoming.Contextual.indexed_fits',
                                                              'Becoming.Web.significance_undetermined'],
     'reading': '王弼以位为贵贱之列、才用之宅，位有尊卑。模块中的位是语境之索引，爻与位之关系（定位、当位）不带等级与判断，'
                '律亦不决定意义；理论不采贵贱尊卑之读（与《繫辭》“貴賤”“天尊地卑”之相分同）。'},
    {'id': 'lueli-mingtuan-zhizhong', 'source': 'lueli/mingtuan.json', 'locator': '王弼《周易略例·明彖》',
     'fragments': ['夫眾不能治眾，治眾者，至寡者也', '故眾之所以得咸存者，主必致一也'], 'kind': 'divergence',
     'declarations': hx('answers_symm', 'sole_answered', 'sole_unique', 'answers_shown_along_run'),
     'reading': '律中一爻与其余五爻之关系是对称的：它与五爻皆相异，五爻亦各与它相异；关系中没有“治”之方向，'
                '也没有一个律使众爻之存依赖于此一爻。“治眾”“主必致一”是统治之读，理论不采；理论读关系本身。'},
    {'id': 'lueli-guale-yinwei', 'source': 'lueli/guale.json', 'locator': '王弼《周易略例·卦略》（履、大過）',
     'fragments': ['陽處陰位，謙也。故此一卦，皆以陽處陰為美也', '故陽爻皆以居陰位為美'], 'kind': 'divergence',
     'declarations': hx('inPhase', 'holdsPlace') + ['Becoming.Web.significance_undetermined'],
     'reading': '小象多以不当位为失，王弼于履、大過、大壯则以阳居阴位为美：同一关系（阳爻不当位）在不同之卦得相反之判断。'
                '律中只有关系，判断不由关系定；理论不采“美”之判断。'},
]

REVISE = {
    'xiaoxu-shangxia': ('agreement', hx('sole', 'xiaoXu_answered', 'answeredStatements_sole'),
                        '六四为阴而当位；以对应之位论，只初九与之相应。“上下應之”读作一个阴爻与其余五个阳爻皆相异：'
                        '小畜六四是卦中唯一之阴爻，其余五爻皆与之相应。'),
    'dayou-zunwei': ('divergence', hx('sole', 'daYou_answered'),
                     '六五居中而不当位，以对应之位论只与九二相应；“上下應之”是六五与其余五个阳爻皆相异，在律中。'
                     '“尊位”是位的等级，理论不采（与《繫辭》“貴賤”之相分同），所以仍为相分。'),
    'guai-chengwugang': ('agreement', hx('guai_iff', 'guai_sole', 'sole_broken_seams'),
                         '以相邻之位论，上六只乘九五一刚，诸位之间只此一处落；“乘五剛”读作上六与其下五个阳爻皆相异：'
                         '上爻为阴而与其余五爻皆相异者恰是夬，此阴爻之下是唯一之落。'),
    'lv-weibudang': ('agreement', hx('placeStatements_between', 'placeStatements_hold', 'holdsPlace'),
                     '小象明言位者二十七处（位不當、不當位、未當位、未得位；位正當、位當、當位），检查脚本在所存六十四页中逐一找出：'
                     '二十六处在三、四、五位，与其爻是否当位相合；需上六一处在上位。以初上无位之读，二十七处与《文言》乾上九'
                     '“貴而无位”皆相合，没有例外。“凶”是判断，不在律中。'),
    'xu-shangliu': ('agreement', hx('xu_top_no_place', 'top_no_parity', 'holdsPlace', 'fixedPhase'),
                    '上六阴居偶位，依六位之奇偶是当位，象却说不当位。王弼《周易略例·辯位》以此句与乾上九“貴而无位”为初、上'
                    '无定位之证。模块有两个关系：依六位之奇偶，此处相分；依初上无位之读，上六无定位而不在位，象之言相合。'),
}

data = json.loads(MAP.read_text())
passages = data['passages']
ids = {p['id'] for p in passages}
assert not ids & {p['id'] for p in NEW}, 'Y4 passages already present'
assert set(REVISE) <= ids, 'a passage to revise is missing'
at = next(i for i, p in enumerate(passages) if p['id'] == 'tonggong-yiwei') + 1
passages[at:at] = NEW
for p in passages:
    if p['id'] in REVISE:
        kind, more, reading = REVISE[p['id']]
        p['kind'] = kind
        p['declarations'] += [d for d in more if d not in p['declarations']]
        p['reading'] = reading
about = data['about'].replace('(and two commentaries)', '(and three commentaries)')
named = re.match(r'The passage map of (.+?):', about)
items = re.findall(r'Y\d+', named.group(1)) + ['Y4']
data['about'] = about.replace(named.group(0), 'The passage map of ' + ', '.join(items[:-1]) + ' and Y4:')
MAP.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('added', len(NEW), 'passages; revised', len(REVISE), '; now', len(passages))
