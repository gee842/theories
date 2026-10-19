#!/usr/bin/env python3
"""Write Y2's record place-relations-in-context and update Y1's record hexagrams-on-the-spine:
  python3 -B make_record.py CORE_RECEIPT STUDY_SECTION DECISION

The receipt is checked against the current bytes of Becoming/HexagramPlaces.lean and of every module the record binds,
every declaration of the module is listed in exactly one law, every declaration the record cites is in the receipt, and
the passage map is checked against the receipt (verify_mapping.py) before anything is written. Run after apply_text.py
(the study section, the decision and the canonical chapter in place) and before rendering."""
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT_DIR = HERE.parent
ROOT = HERE.parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/HexagramPlaces.lean'
KIT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
DCP = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CANON = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER = 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-the-changes-on-the-spine.md'
PROVENANCE = 'sources/zhouyi-yizhuan/PROVENANCE.json'
core_id, section, decision = sys.argv[1], sys.argv[2], sys.argv[3]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
GO = '“我要你把这个系统完全建立起来，要变成库的一部分，要确保它在spine上有明确的mapping”'
BOUND = ('HexagramPlaces', 'Hexagrams', 'Context', 'Learning', 'Mechanism', 'Recurrence', 'Frame')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
for name in BOUND:
    assert core['source_sha256'][f'Becoming.{name}'] == sha(f'{PKG}/Becoming/{name}.lean'), name
module = next(m for m in core['modules'] if m['module'] == 'Becoming.HexagramPlaces')
assert not any(module['axiom_dependencies'].values())
own = {d['name'] for d in module['declarations']}
audited = {d['name'] for m in core['modules'] for d in m['declarations']}
STUDY_TEXT = (ROOT / STUDY).read_text()
assert re.search(rf'^## {section}\. The relations of the places in the Changes \(Y2\)$', STUDY_TEXT, re.M), section
assert f'### {decision}. ' in (ROOT / DCP.replace('.md', '.zh.md')).read_text(), decision
check = subprocess.run([sys.executable, '-B', str(KIT_DIR / 'verify_mapping.py'), '--receipt', str(ROOT / core_receipt)],
                       capture_output=True, text=True)
assert check.returncode == 0, check.stdout + check.stderr
passages = json.loads((KIT_DIR / 'passages.json').read_text())['passages']
y2_passages = [p for p in passages if any(d.startswith('Becoming.Hexagram.') and d in own for d in p['declarations'])]


def h(*names):
    out = ['Becoming.Hexagram.' + n for n in names]
    missing = [n for n in out if n not in own]
    assert not missing, missing
    return out


def spine(*names):
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in audited]
    assert not missing, missing
    return out


laws = [
    {'en': 'A hexagram has three heights in each of two trigrams, each place being one height of one trigram, and two '
           'adjacent places meet at a seam; the places alternate in parity across every seam.',
     'zh': '一卦两个三画卦各有三个高度，每一位是一卦之一高度；相邻两位相接于一缝；六位奇偶在每一缝两侧相反。',
     'declarations': h('Height', 'Half', 'place', 'heightOf', 'Seam', 'below', 'above', 'Seam.next', 'Place.mirror',
                       'Height.mirror', 'Seam.mirror', 'odd', 'odd_above')},
    {'en': 'A line is in phase where its value is its place\'s parity (正); the two lines at one height are opposed where '
           'they differ (應); adjacent lines alternate, rise or fall across their seam (比, 承, 乘); the middle height is '
           'lines 2 and 5 (中). Rises and the bottom line count as many as falls and the top line.',
     'zh': '一爻之值合于其位之奇偶为正；同一高度两爻相异为应；相邻两爻相异为比，自下而上阴下阳上为承、阳下阴上为乘；'
           '中是二、五两位。承之数加初爻，等于乘之数加上爻。',
     'declarations': h('inPhase', 'opposed', 'alternates', 'rises', 'falls', 'middle', 'phaseCount', 'riseCount',
                       'fallCount', 'rises_falls_ends')},
    {'en': 'A relation read at each of its sites is a contextual reading of the configuration, gluing to one reading of '
           'the whole exactly where every site shows the same. The two trigrams read as contexts glue exactly where no '
           'height is opposed, so no frame of context-free claims fits the heights under any process, while the '
           'indexed frame fits.',
     'zh': '一关系在其各处所示，是对整卦的语境读法，恰当各处所示相同时粘合为对整卦的一个读法。上下两卦读作两个语境，'
           '恰当无一高度相应时粘合；所以任何过程之下没有去语境的框架合于诸高度，带索引的框架则合。',
     'declarations': h('atSites', 'atSites_glues_iff', 'atSites_glues_iff_constant', 'halves', 'halves_indexed',
                       'eq_iff_not_same', 'halves_agree_at', 'halves_glues_iff', 'halves_no_free_frame')},
    {'en': 'The phases glue exactly at 既濟 and 未濟, every line in phase or none; the oppositions where every height '
           'or none is opposed; the seams exactly at 乾, 坤, 既濟 and 未濟. So no frame of context-free claims fits '
           'the phases, the oppositions or the alternations under any process, while the indexed frame fits.',
     'zh': '各位之正恰在既濟、未濟（六爻皆正或皆不正）粘合；各高度之应在三处皆应或皆不应之处；各缝之比恰在乾、坤、既濟、未濟。'
           '所以任何过程之下，没有去语境的框架合于正、应或比，带索引的框架则合。',
     'declarations': h('jiJi_inPhase', 'weiJi_out_of_phase', 'inPhase_all_iff', 'inPhase_none_iff', 'phases_glue_iff',
                       'oppositions_glue_iff', 'alternates_all_iff', 'alternates_none_iff', 'seams_glue_iff',
                       'atSites_indexed', 'phases_no_free_frame', 'oppositions_no_free_frame', 'seams_no_free_frame')},
    {'en': 'The lines at a height are opposed exactly where both or neither are in phase; so both middle lines in phase '
           'give the middle opposed, and every line out of phase, or every line in phase, gives every height opposed. '
           'An unbroken and a broken middle line with an answer pick out the same configurations.',
     'zh': '同一高度两爻相应，恰当二者同正或同不正；所以两个中位皆正则中相应，六爻皆不正或皆正则三处皆应。'
           '居中之阳爻有应与居中之阴爻有应，所指是同一些构形。',
     'declarations': h('opposed_iff_phase', 'middle_phase_opposed', 'out_of_phase_opposed', 'in_phase_opposed',
                       'middleUnbrokenOpposed', 'middleBrokenOpposed', 'middleUnbrokenOpposed_eq',
                       'middleBrokenOpposed_eq')},
    {'en': 'The complement turns every phase, so the counts in phase of a configuration and its complement add to six, '
           'keeps every opposition and alternation, and exchanges rises and falls; turning over does the same at the '
           'mirrored site.',
     'zh': '错使每一爻之正翻转，故一卦与其错卦的当位之数相加为六；保持每一处应与比，交换承与乘；综在镜像之处作同样的事。',
     'declarations': h('same_not_left', 'same_not_not', 'line_complement', 'inPhase_complement', 'phaseCount_complement',
                       'opposed_complement', 'alternates_complement', 'rises_complement', 'line_reverse',
                       'inPhase_reverse', 'phaseCount_reverse', 'opposed_reverse', 'rises_reverse')},
    {'en': 'Changing the line at a place turns its phase and the opposition at its height and leaves every other place '
           'and height as it was; the count in phase moves by one.',
     'zh': '一爻之变翻转该位之正与其高度之应，其余各位、各高度不动；当位之数增或减一。',
     'declarations': h('line_flip_self', 'line_flip_other', 'inPhase_flip_self', 'inPhase_flip_other', 'phaseCount_flip',
                       'opposed_flip_self', 'opposed_flip_other')},
    {'en': 'Under the law of waxing and waning each line rises with its value, so its phase turns at every rise and is '
           'kept only where the top line enters at the bottom; the counts in phase before and after a step add to five '
           'or seven, so the count changes parity at every step, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4, 3, 4 from 乾, and is not '
           'a lumping the law goes alike across. Alternations, rises and falls travel with their lines.',
     'zh': '消息之律下每爻带着其值上升，每升一位其正即翻转，只在上爻入初位之处保持；一步前后的当位之数相加为五或七，'
           '所以当位之数每步改变奇偶，自乾为三、二、三、二、三、二、三、四、三、四、三、四，不是律所同行的归并。比、承、乘随其两爻而行。',
     'declarations': h('line_waxWane_above', 'same_not_right', 'inPhase_waxWane_above', 'inPhase_waxWane_bottom',
                       'phaseCount_waxWane', 'phaseCount_parity', 'phase_parity_along_run', 'phase_qian_orbit',
                       'phaseCount_not_lumped', 'phaseCount_not_goAlike', 'alternates_carried', 'rises_carried',
                       'falls_carried')},
    {'en': 'The oppositions of the three heights run under the law of waxing and waning on three cells, so they are a '
           'lumping the law goes alike across: three steps turn every opposition and six keep it; two patterns return '
           'at the second step, and the other six form one cycle of six steps through every height opposed and none. '
           'The doubled trigrams are three steps from opposition at every height.',
     'zh': '三个高度之应服从三格上的消息之律，所以是律所同行的归并：三步使每一处应翻转，六步复原；两种格局两步即返，'
           '其余六种成一个六步之环，经过三处皆应与三处皆不应。重卦三步之后三处皆应。',
     'declarations': h('opposition', 'waxWane3', 'opposition_waxWane', 'opposition_lumped', 'opposition_goAlike',
                       'opposed_three_steps', 'opposition_six', 'waxWane3_twice_iff', 'waxWane3_moves',
                       'opposition_cycle', 'opposition_two_iff', 'halves_glue_three')},
    {'en': 'Along every run of waxing and waning, each line\'s phase turns as it rises, the counts in phase at '
           'consecutive steps add to five or seven, and alternations travel with their lines; six steps on every phase '
           'is turned and, opposition being told by phase, every opposition kept; three steps on every opposition is '
           'turned; the pattern of oppositions changes at every step and, from every height opposed, goes round in six.',
     'zh': '沿消息之律的每一运行，每爻上升时其正翻转，相邻两步的当位之数相加为五或七，比随其两爻而行；'
           '六步之后每一爻之正翻转，而应由正而定，故每一处应保持；三步之后每一处应翻转；应之格局每步都变，'
           '自三处皆应六步一周。',
     'declarations': h('run_phase_rises', 'run_phase_enters', 'run_phaseCount', 'run_carried', 'run_six_turns',
                       'run_six_keeps', 'run_three_turns', 'run_doubled_three', 'run_opposition_moves',
                       'run_opposition_two_iff', 'opposition_orbit', 'map_agree', 'run_opposition_cycle')},
    {'en': 'Along every run of the change of one line, each step turns the phase of the line it changes and the '
           'opposition at its height and keeps every other; turned over, a run of waxing and waning is the run of '
           'the law backward from the turned-over configuration, on which every relation is mirrored; whatever a run '
           'of any process shows, opposition is told by phase.',
     'zh': '沿一爻之变的每一运行，每一步翻转所变之爻的正与其高度之应，其余不动；倒转消息之律的运行，即自倒转之卦逆行的运行，'
           '其上每一关系皆在镜像之处；任一过程的运行在任一步所示，应皆由正而定。',
     'declarations': h('changes_run_phase', 'changes_run_opposition', 'backward_run', 'backward_relations',
                       'shown_along_run')},
    {'en': 'The configurations the passage map cites are named by their number in the received order, and what the 彖 '
           'and the 象 say of their places holds of them: 未濟, 恒 and 咸 opposed at every height, 艮\'s trigrams '
           'gluing, the second line of 同人, the fourth of 小畜 and the fifth of 大有, the falls of 歸妹 and 夬.',
     'zh': '逐句对应所引之卦，以其在所传卦序中的序数命名；彖与象所说其爻位之关系在其上成立：未濟、恒、咸三处皆应，'
           '艮上下卦粘合，同人之二、小畜之四、大有之五，歸妹与夬之乘。',
     'declarations': h('nth', 'number', 'xu', 'xiaoXu', 'tongRen', 'daYou', 'xian', 'heng', 'guai', 'gen', 'guiMei',
                       'jiJi', 'weiJi', 'weiJi_opposed', 'heng_opposed', 'xian_opposed', 'gen_halves_glue',
                       'tongRen_second', 'xiaoXu_fourth', 'daYou_fifth', 'guiMei_falls', 'guai_falls')},
    {'en': 'Four censuses list the explicit statements of a kind in the 彖 and the 小象, found in the preserved pages by '
           'the script: 26 statements of 位 agree with the parity of their places, 9 of 中正 are middle and in phase, '
           '5 of 乘剛 are falls and 5 of 剛中而應 are the middle opposed; the two exceptions, 需\'s top line and 艮\'s '
           'fifth, are stated as they are.',
     'zh': '四项普查列出彖与小象中一类明言的全部，由检查脚本在所存之页中找出：言位者二十六处合于其位之奇偶，'
           '言中正者九处居中而当位，言乘刚者五处为乘，言剛中而應者五处为中相应；两处例外（需上六、艮六五）如其所是地写出。',
     'declarations': h('placeStatements', 'placesHold', 'placesHold_sound', 'placeStatements_agree', 'xu_top_inPhase',
                       'centreStatements', 'centresHold', 'centresHold_sound', 'centreStatements_agree',
                       'gen_fifth_out_of_phase', 'fallStatements', 'fallsHold', 'fallsHold_sound',
                       'fallStatements_agree', 'middleOppositionStatements', 'middleOppositionsHold',
                       'middleOppositionsHold_sound', 'middleOppositionStatements_agree')},
]
listed = [d for law in laws for d in law['declarations']]
assert len(listed) == len(set(listed)) and set(listed) == own, sorted(own ^ set(listed))
kinds = {k: sum(p['kind'] == k for p in y2_passages) for k in ('agreement', 'scope', 'divergence')}

record = {
    'schema_version': 2,
    'id': 'place-relations-in-context',
    'title': {'en': 'The relations of the places, read in context', 'zh': '爻位之关系，在位上读'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': json.loads((RECORDS / 'hexagrams-on-the-spine.json').read_text())['family'],
    'reviewed_at_utc': NOW,
    'statement': {
        'en': 'The relations of a hexagram\'s places, 正, 應, 比 and 中, are readings in context: they glue to a '
              'reading of the whole only where every site agrees, the trigrams exactly where no height is opposed. '
              'Along every run, opposition is told by phase; the oppositions carry waxing and waning, the phases '
              'do not.',
        'zh': '爻位之关系（正、应、比、中）是在位上成立的语境读法：只在各处所示相同时粘合为对整卦的读法，上下两卦恰在无一高度'
              '相应时粘合。沿每一运行，应由正而定；三处之应承载消息之律，当位之数不承载。'},
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom and no premise: the sites, relations, contextual readings and censuses are defined in the '
               'module; each spine law is used at its stated hypotheses (Contextual.fitsFree_iff with a height or a '
               'site as home; Learning.goAlike_iff_lumped at the oppositions and the count in phase); the laws along '
               'runs hold for every run of the named process, shown_along_run for every run of every process.',
         'zh': '不用公理、不加前提：各处、各关系、两种语境读法与普查都在模块中定义；脊柱的每条律按其所列假设使用'
               '（Contextual.fitsFree_iff 以每一高度或一处为所在；Learning.goAlike_iff_lumped 用于诸应与当位之数）；'
               '沿运行之律对所述过程的每一运行成立，shown_along_run 对六十四卦上任一过程的每一运行成立。'},
    ],
    'does_not_show': [
        {'en': 'What any passage says of the places beyond these relations; the passage map of the chapter states, '
               'passage by passage, agreement, exact scope or divergence, and its readings are the AI\'s.',
         'zh': '任何一段在这些关系之外关于爻位所说的；章节的逐句对应逐段写明相合、定域或相分，其读法是 AI 读法。',
         'kind': 'correspondence'},
        {'en': 'The ranks of the places (尊位, 貴賤); whether the bottom and top places have a place (初上无位); one line '
               'answered by all others (上下應之, 乘五剛); statements of place outside the four censuses; 王弼\'s '
               '《周易略例》, not preserved here.',
         'zh': '位的尊卑（尊位、贵贱），初上两位是否有位（初上无位），一爻为众爻所应（上下應之、乘五剛），以及四项普查之外'
               '关于位的言说（爻辞、大象、文言）；王弼《周易略例》未存于本库，未对照。',
         'kind': 'scope'},
        {'en': 'That being in phase, opposed, central or rising is good, fortunate or supports 生生; the module has no '
               'ethical predicate and no judgment of fortune.',
         'zh': '当位、相应、居中或承是善的、吉的或支持生生；模块没有伦理谓词，也没有吉凶判断。', 'kind': 'non-implication'},
    ],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {len(own)} declarations '
              f'of Becoming.HexagramPlaces, {module["theorems"]} of them theorems, have empty axiom reports; the checker '
              f'verifies core purity. The passage map ({len(passages)} passages, {len(y2_passages)} citing this module) '
              f'and the four censuses are checked by verify_mapping.py against the preserved Wikisource revisions and '
              f'the receipt\'s declaration list. Author self-review in study section {section}; not independently '
              f'reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.HexagramPlaces 的 {len(own)} 项声明'
              f'（{module["theorems"]} 项定理）公理报告为空；检查器并核对核心纯净。逐句对应（{len(passages)} 段，其中 '
              f'{len(y2_passages)} 段引本模块）与四项普查由 verify_mapping.py 对照保存的维基文库版本与回执的声明清单检查。'
              f'作者自审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': '王弼\'s reading that the bottom and top lines have no place, as a second relation on places 2 to 5, once '
              'the 《周易略例》 is preserved; the relation of one line to all the others (卦主); censuses of the line '
              'texts, the 大象 and the 文言; the nuclear law 互 and the cast of old and young lines on these sites (Y3); '
              'an independent review.',
        'zh': '王弼“初上无位”之读，作为二至五位上的另一关系，待《周易略例》存入本库；一爻与其余诸爻的关系（卦主）；'
              '爻辞、大象与文言的普查；互卦与之卦在这些位上的律（Y3）；独立审查。'},
    'correspondence': {
        'en': f'Continues hexagrams-on-the-spine (Y1), which listed the relations of the places as not done, on Ren\'s '
              f'request of 19 October 2026, {GO} (provenance, not warrant). The chapter on the 易传 maps '
              f'{len(y2_passages)} passages that cite this module: {kinds["agreement"]} agreements, {kinds["scope"]} '
              f'exact scopes and {kinds["divergence"]} divergences. Reading (the AI\'s, {decision}): 正 is a relation of a '
              f'line and its place, so a line\'s phase turns as it rises (六位時成); 應 is told by phase, so 未濟\'s '
              f'雖不當位，剛柔應也 is an entailment; 敵應 is where the two trigrams glue; the oppositions carry the law and '
              f'the count in phase does not; the text agrees with the relations in four censuses except at 需\'s top '
              f'line and 艮\'s fifth; the ranks of the places diverge.',
        'zh': f'接续 hexagrams-on-the-spine（Y1）所列未做的爻位之关系，按 Ren 2026年10月19日的要求 {GO}（来历，不是根据）。'
              f'论易传的一章中引本模块者 {len(y2_passages)} 段：相合 {kinds["agreement"]}、定域 {kinds["scope"]}、'
              f'相分 {kinds["divergence"]}。读法（AI 的，{decision}）：正是爻与位的关系，所以一爻上升时其正翻转（六位時成）；'
              f'应由正而定，未濟“雖不當位，剛柔應也”是蕴涵；敵應是上下两卦粘合之处；诸应承载律，当位之数不承载；'
              f'四项普查中经文与这些关系一致，只有需上六与艮六五两处例外；位的尊卑相分。'},
    'canonical_source': SRC,
    'aliases': ['the relations of the places', '爻位之关系', '應', '应', '比', '中', '正', '當位', '当位', '敵應', '承', '乘',
                '中正', '剛中而應', '六位時成', 'readings of the places in context',
                'Becoming.Hexagram.halves_glues_iff', 'Becoming.Hexagram.opposed_iff_phase',
                'Becoming.Hexagram.phaseCount_waxWane', 'Becoming.Hexagram.opposition_goAlike',
                'Becoming.Hexagram.placeStatements_agree'],
    'dependencies': [
        {'id': 'hexagrams-on-the-spine', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the configurations, the received order, complement, reverse, flip and waxWane of '
                          'Becoming.Hexagrams; the delta is the relations of the places read on them.',
                    'zh': '复用 Becoming.Hexagrams 的构形、所传卦序、错、综、一爻之变与消息之律；增量是在其上读出的爻位之关系。'},
         'interface': {'output': {'en': 'Six two-valued lines, the received order holding every configuration, and the '
                                        'laws of change on them.',
                                  'zh': '六爻二值、含全部构形的所传卦序，以及其上的变化之律。'},
                       'input': {'en': 'Hexagram, line, same, order, complement, reverse, flip, waxWane, rising.',
                                 'zh': 'Hexagram、line、same、order、complement、reverse、flip、waxWane、rising。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Hexagrams.lean'}},
        {'id': 'contextual-registration', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Contextual, Glues, indexed, indexed_fits, FitsFree and fitsFree_iff, reading the sites '
                          'of a relation and the two trigrams as contexts.',
                    'zh': '复用 Contextual、Glues、indexed、indexed_fits、FitsFree 与 fitsFree_iff，把一关系的各处与上下两卦读作语境。'},
         'interface': {'output': {'en': 'What contexts show glues exactly where they agree where they meet; a frame of '
                                        'context-free claims fits exactly where it glues everywhere; the indexed frame '
                                        'always fits.',
                                  'zh': '诸语境所示恰在相会处一致时粘合；去语境的框架恰在处处粘合时相合；带索引的框架总相合。'},
                       'input': {'en': 'atSites for each relation, halves for the trigrams, home the height itself.',
                                 'zh': '各关系的 atSites，两卦的 halves，所在即高度自身。'},
                       'conditions': {'en': 'Every context lies within its home (trivially, within is True).',
                                      'zh': '每一语境在其所在之内（within 恒真）。'},
                       'evidence': f'{PKG}/Becoming/Context.lean'}},
        {'id': 'generalization-through-lumping', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Learning.Lumped and Learning.goAlike_iff_lumped for the oppositions and the count in '
                          'phase under waxWane.',
                    'zh': '对 waxWane 下的诸应与当位之数复用 Learning.Lumped 与 Learning.goAlike_iff_lumped。'},
         'interface': {'output': {'en': 'A reading the law goes alike across exactly where it is a lumping.',
                                  'zh': '律在其上同行的读法，恰是归并。'},
                       'input': {'en': 'opposition and phaseCount under waxWane.',
                                 'zh': 'waxWane 下的 opposition 与 phaseCount。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Learning.lean'}},
    ],
    'related': [
        {'id': 'gluing-under-parity',
         'detail': {'en': 'Another case of contexts that glue or do not; here every reading is decided and the failure '
                          'to glue is located at the opposed heights.',
                    'zh': '语境粘合与否的另一例；这里每一读法可判定，不粘合之处落在相应的高度上。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted(own), 'sha256': sha(SRC)},
        {'path': core_receipt, 'role': 'receipt', 'declarations': [], 'sha256': sha(core_receipt)},
        {'path': f'{PKG}/Becoming/Hexagrams.lean', 'role': 'proof',
         'declarations': spine('Hexagram', 'Hexagram.line', 'Hexagram.same', 'Hexagram.order', 'Hexagram.complement',
                               'Hexagram.reverse', 'Hexagram.flip', 'Hexagram.waxWane', 'Hexagram.rising',
                               'Hexagram.changes', 'Hexagram.unwaxWane', 'Hexagram.reverse_wax',
                               'Hexagram.run_six_steps'),
         'sha256': sha(f'{PKG}/Becoming/Hexagrams.lean')},
        {'path': f'{PKG}/Becoming/Context.lean', 'role': 'proof',
         'declarations': spine('Contextual', 'Contextual.Glues', 'Contextual.indexed', 'Contextual.indexed_fits',
                               'Contextual.FitsFree', 'Contextual.fitsFree_iff'),
         'sha256': sha(f'{PKG}/Becoming/Context.lean')},
        {'path': f'{PKG}/Becoming/Learning.lean', 'role': 'proof',
         'declarations': spine('Learning.Lumped', 'Learning.goAlike_iff_lumped'),
         'sha256': sha(f'{PKG}/Becoming/Learning.lean')},
        {'path': f'{PKG}/Becoming/Mechanism.lean', 'role': 'proof', 'declarations': spine('GoAlike'),
         'sha256': sha(f'{PKG}/Becoming/Mechanism.lean')},
        {'path': f'{PKG}/Becoming/Recurrence.lean', 'role': 'proof',
         'declarations': spine('Law.orbit', 'Law.orbit_add', 'Law.run', 'Law.process'),
         'sha256': sha(f'{PKG}/Becoming/Recurrence.lean')},
        {'path': f'{PKG}/Becoming/Frame.lean', 'role': 'proof', 'declarations': spine('Frame', 'Run'),
         'sha256': sha(f'{PKG}/Becoming/Frame.lean')},
        {'path': CHAPTER, 'role': 'statement', 'declarations': [], 'sha256': sha(CHAPTER)},
        {'path': f'{KIT}/passages.json', 'role': 'integration', 'declarations': [], 'sha256': sha(f'{KIT}/passages.json')},
        {'path': f'{KIT}/verify_mapping.py', 'role': 'integration', 'declarations': [],
         'sha256': sha(f'{KIT}/verify_mapping.py')},
        {'path': STUDY, 'role': 'integration', 'declarations': [], 'sha256': sha(STUDY)},
        {'path': CANON, 'role': 'statement', 'declarations': [], 'sha256': sha(CANON)},
        {'path': PROVENANCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(PROVENANCE)},
        {'path': SOURCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(SOURCE)},
    ],
    'proof_bindings': [
        {'source': f'{PKG}/Becoming/{name}.lean', 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/Becoming.{name}',
         'success_pointer': '/status', 'success_value': 'passed'}
        for name in BOUND
    ],
    'history': [
        {'en': f'19 October 2026: added (Y2), continuing Y1 on Ren\'s {GO}; study section {section}, decision {decision}.',
         'zh': f'2026年10月19日：新增（Y2），接续 Y1，按 Ren 的 {GO}；研究第 {section} 节，决定 {decision}。'},
    ],
}
assert len(record['statement']['en']) <= 300 and len(record['statement']['zh']) <= 150, (
    len(record['statement']['en']), len(record['statement']['zh']))
(RECORDS / 'place-relations-in-context.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')

# Y1's record: the relations of the places are done; the references Y2 changed are re-pointed after reading the change.
y1_path = RECORDS / 'hexagrams-on-the-spine.json'
y1 = json.loads(y1_path.read_text())
scope = next(x for x in y1['does_not_show'] if x['kind'] == 'scope')
OLD_EN = ', and the relations of the places (應, 比, 中, 正).'
OLD_ZH = '，以及爻位之间的应、比、中、正。'
assert scope['en'].endswith(OLD_EN) and scope['zh'].endswith(OLD_ZH), scope
scope['en'] = scope['en'][:-len(OLD_EN)] + '; the relations of the places are in place-relations-in-context.'
scope['zh'] = scope['zh'][:-len(OLD_ZH)] + '；爻位之关系见 place-relations-in-context。'
NEXT_EN = 'The relations of the places (應, 比, 中, 正) as indexed readings in context; '
NEXT_ZH = '爻位的应、比、中、正作为带语境索引的读法；'
assert y1['next_delta']['en'].startswith(NEXT_EN) and y1['next_delta']['zh'].startswith(NEXT_ZH)
rest = y1['next_delta']['en'][len(NEXT_EN):]
y1['next_delta']['en'] = rest[0].upper() + rest[1:]
y1['next_delta']['zh'] = y1['next_delta']['zh'][len(NEXT_ZH):]
if not any(r['id'] == 'place-relations-in-context' for r in y1['related']):
    y1['related'].append({'id': 'place-relations-in-context',
                          'detail': {'en': 'The relations of the places (正, 應, 比, 中) read in context on these '
                                           'configurations, and their laws under the same changes.',
                                     'zh': '在这些构形上以语境读出的爻位之关系（正、应、比、中），及其在同样变化之下的律。'}})
changed = []
for ref in y1['references']:
    if ref['role'] in ('statement', 'integration') and ref['sha256'] != sha(ref['path']):
        ref['sha256'] = sha(ref['path'])
        changed.append(ref['path'].rsplit('/', 1)[-1])
y1['history'].append({
    'en': f'19 October 2026, Y2 (the relations of the places): the relations of the places, listed as not shown and '
          f'as the next delta, are now the record place-relations-in-context (study section {section}, decision '
          f'{decision}); {", ".join(changed)} re-pointed after reading the change (Y2 added its passages, its censuses '
          f'and their checks, its chapter text, its study section and its section 1 paragraph). The claim is unchanged.',
    'zh': f'2026年10月19日，Y2（爻位之关系）：原列为未示与下一步的爻位之关系，现为记录 place-relations-in-context'
          f'（研究第 {section} 节，决定 {decision}）；读过改动后，{"、".join(changed)} 重新指向。论断不变。'})
y1_path.write_text(json.dumps(y1, ensure_ascii=False, indent=2) + '\n')
print('written', len(own), 'declarations in', len(laws), 'laws;', len(y2_passages), 'of', len(passages),
      'passages cite the module; Y1 re-pointed:', changed)
