#!/usr/bin/env python3
"""Write Y4's record fixed-places-and-sole-lines and update the records of Y1 and Y2:
  python3 -B make_record.py CORE_RECEIPT STUDY_SECTION DECISION

The receipt is checked against the current bytes of Becoming/HexagramSites.lean and of every module the record binds,
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
SRC = f'{PKG}/Becoming/HexagramSites.lean'
KIT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
DCP = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CANON = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER = 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-the-changes-on-the-spine.md'
PROVENANCE = 'sources/zhouyi-yizhuan/PROVENANCE.json'
LUELI = ('bianwei', 'mingtuan', 'lueli-xia', 'minggua-shibian-tongyao', 'mingyao-tongbian', 'guale', 'mingxiang')
core_id, section, decision = sys.argv[1], sys.argv[2], sys.argv[3]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
GO = '“我要你把这个系统完全建立起来，要变成库的一部分，要确保它在spine上有明确的mapping”'
BOUND = ('HexagramSites', 'HexagramPlaces', 'Hexagrams', 'Context', 'Learning', 'Mechanism', 'Recurrence', 'Frame')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
for name in BOUND:
    assert core['source_sha256'][f'Becoming.{name}'] == sha(f'{PKG}/Becoming/{name}.lean'), name
module = next(m for m in core['modules'] if m['module'] == 'Becoming.HexagramSites')
assert not any(module['axiom_dependencies'].values())
own = {d['name'] for d in module['declarations']}
audited = {d['name'] for m in core['modules'] for d in m['declarations']}
STUDY_TEXT = (ROOT / STUDY).read_text()
assert re.search(rf'^## {section}\. 王弼\'s readings of the places on the spine \(Y4\)$', STUDY_TEXT, re.M), section
assert f'### {decision}. ' in (ROOT / DCP.replace('.md', '.zh.md')).read_text(), decision
check = subprocess.run([sys.executable, '-B', str(KIT_DIR / 'verify_mapping.py'), '--receipt', str(ROOT / core_receipt)],
                       capture_output=True, text=True)
assert check.returncode == 0, check.stdout + check.stderr
passages = json.loads((KIT_DIR / 'passages.json').read_text())['passages']
y4_passages = [p for p in passages if any(d.startswith('Becoming.Hexagram.') and d in own for d in p['declarations'])]


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
    {'en': 'The second relation of phase: lines 2 to 5 have the phase of their place\'s parity and the bottom and top '
           'lines have none (初上无位); a line holds its place where it is in phase between the ends. It is the phase '
           'of inPhase between the ends and says nothing at them.',
     'zh': '第二个关系：二至五位依其奇偶有定位之正，初、上两位没有（初上无位）；一爻在位，恰当它在两端之间而当位。'
           '它在两端之间即 inPhase 之正，在两端不说。',
     'declarations': h('betweenEnds', 'Between', 'Between.place', 'fixedPhase', 'holdsPlace', 'fixedPhase_between',
                       'fixedPhase_end', 'holdsPlace_iff', 'holdsPlace_inPhase', 'holdsPlace_ends')},
    {'en': '王弼\'s dilemma: of two lines that differ at a place, every parity of the place puts one in phase, so no '
           'parity of the top place leaves both 需\'s top line and 乾\'s out of phase, as the 小象 and the 文言 say. '
           'The 小象\'s statements of place fix the parity of places 3, 4 and 5, and the statements of 中正 that of '
           'place 2.',
     'zh': '王弼之两难：一位上两爻相异，此位任一奇偶必使其一当位；所以上位没有一个奇偶使需上六与乾上九都不当位，'
           '如小象与文言所说。小象言位之句定三、四、五位之奇偶，言中正之句定二位之奇偶。',
     'declarations': h('qian', 'same_comm', 'one_in_phase_of_parity', 'top_no_parity', 'parityOf',
                       'parity_of_statement', 'statements_fix_parity', 'centre_fixes_parity')},
    {'en': 'The 26 statements of place of the 小象 all stand between the ends, and with 乾\'s top line (貴而无位) and '
           '需\'s (雖不當位) all 28 hold under the second relation, with no exception.',
     'zh': '小象言位之二十六处皆在两端之间；连同乾上九（貴而无位）与需上六（雖不當位），二十八处在第二个关系下皆成立，没有例外。',
     'declarations': h('all_sound', 'all_complete', 'all_congr', 'placeStatements_between', 'topStatements',
                       'placeStatements_hold', 'xu_top_no_place', 'qian_top')},
    {'en': 'The 彖\'s nine statements of the place of one line all agree; its five statements of the place of the whole '
           '(蹇, 漸, 歸妹, 既濟, 未濟) all hold between the ends, and only two under the six places. The configurations '
           'with every line between the ends in phase are exactly 既濟, 蹇, 漸 and 家人, and with none exactly 未濟, '
           '歸妹, 解 and 睽.',
     'zh': '彖言一爻之位者九处皆合；言整卦之位者五处（蹇、漸、歸妹、既濟、未濟）以二至五位读皆成立，以六位读只成立两处。'
           '中间四爻皆当位者恰是既濟、蹇、漸、家人，皆不当位者恰是未濟、歸妹、解、睽。',
     'declarations': h('tuanPlaceStatements', 'tuanPlaceStatements_agree', 'allHold', 'noneHold', 'wholeBetween',
                       'wholeSix', 'tuanWholeStatements', 'tuanWhole_between', 'jian3', 'jian4', 'jiaRen', 'kui', 'xie',
                       'tuanWhole_six', 'allHold_iff', 'noneHold_iff')},
    {'en': 'The phases between the ends read at their four places glue to a reading of the whole exactly where all four '
           'or none are in phase, so no frame of context-free claims fits them under any process.',
     'zh': '二至五位之正读作四处的语境读法，恰在四爻皆当位或皆不当位之处粘合为对整卦的读法；所以任何过程之下没有去语境的框架与之相合。',
     'declarations': h('betweenPhase', 'allHold_sites', 'not_true_eq', 'noneHold_sites', 'between_glues_iff',
                       'between_no_free_frame')},
    {'en': 'Configurations alike in the phases between the ends have the same lines there, so the falls, rises and '
           'alternations of the three inner seams and the opposition of the middle height are told by those phases; '
           'changing the bottom or top line keeps them and turns the opposition and alternation beside it.',
     'zh': '二至五位之正相同的两卦，其间诸爻相同；所以中间三缝之乘、承、比与中之高度之应皆由这些正而定；初、上之爻变，'
           '诸正不动，其旁之应与比翻转。',
     'declarations': h('SameBetween', 'sameBetween_phase', 'falls_iff_phase', 'rises_iff_phase', 'alternates_iff_phase',
                       'opposed_mid_told', 'inner_seams_told', 'sameBetween_flip_end', 'alternates_flip_bottom',
                       'alternates_flip_top', 'ends_not_told')},
    {'en': 'The complement turns every phase between the ends, turning over takes the places between the ends to each '
           'other and turns their phases, and changing a line between the ends turns its phase; the counts holding '
           'their place of a configuration and its complement add to four.',
     'zh': '错使二至五位每一正翻转，综使其间诸位互换并翻转其正，其间一爻之变翻转该位之正；一卦与其错卦在位之爻数相加为四。',
     'declarations': h('fixedPhase_complement', 'fixedPhase_reverse', 'fixedPhase_flip_self', 'placedCount',
                       'placedCount_complement')},
    {'en': 'Under waxing and waning the line entering place 2 takes the phase opposite to its phase at the bottom, and '
           'each phase between the ends turns as its line rises; the counts holding their place before and after a '
           'step, with the bottom line\'s phase, add to four and the fifth line\'s phase; a line rising from 2 to 5 '
           'holds its place at exactly two of them. The phases between the ends are not a lumping the law goes alike '
           'across.',
     'zh': '消息之律下，入二位之爻取其在初位之正之反，二至五位之正随爻上升而翻转；一步前后在位之爻数相加，再加初爻之正，'
           '等于四加五位之正；一爻自二升至五，恰在其中两位在位。二至五位之正不是律所同行的归并。',
     'declarations': h('fixedPhase_waxWane_enters', 'fixedPhase_waxWane_rises', 'placedCount_waxWane', 'betweenPhases',
                       'betweenPhases_not_lumped', 'betweenPhases_not_goAlike', 'course_between')},
    {'en': 'Two lines answer where their values differ, at any two places: symmetric, never of a line with itself, kept '
           'by the complement; opposition at a height and alternation at a seam are this relation at their pairs.',
     'zh': '两爻相应，是其值相异，在任何两位：对称，一爻不与自身相应，错保持之；一高度之应与一缝之比都是这一关系在其两位上。',
     'declarations': h('answers', 'answers_symm', 'answers_self', 'opposed_answers', 'alternates_answers',
                       'answers_complement')},
    {'en': 'A sole line answers every other line: it is the line alone of its kind, in a configuration with one '
           'unbroken or one broken line, and it is unique; the twelve such configurations are the uniform ones with '
           'one line changed, kept by the complement and by turning over.',
     'zh': '独应之爻与其余五爻皆相应：它是一卦中唯一之阳爻或阴爻，其爻唯一；有此一爻之十二卦，即纯卦之一爻变，错、综保持之。',
     'declarations': h('others', 'mem_others', 'not_mem_others_self', 'sole', 'sole_answered', 'sole_of_answered',
                       'or_left_true', 'or_right_true', 'or_false_split', 'sole_count', 'soleAny', 'soleAny_count',
                       'sole_any', 'none_sole', 'sole_unique', 'uniform', 'sole_iff_flip', 'sole_flip',
                       'sole_complement', 'sole_reverse')},
    {'en': 'A sole line does not depend on place or phase: of the twelve, four hold their place between the ends, four '
           'are out of phase there and four are at the ends. Its configuration is opposed at its height only, as 節 '
           'is with no sole line; below a sole broken line is a fall and above it a rise, and no other seam rises or '
           'falls; a sole broken line at the top is exactly 夬.',
     'zh': '独应不依位与正：十二卦中，在二至五位当位者四，不当位者四，在两端者四。其卦只在其爻之高度相应，节亦只一处相应而无独应；'
           '独阴之下为乘、之上为承，其余之缝无起落；上爻为独阴者恰是夬。',
     'declarations': h('sole_any_phase', 'soleList', 'sole_places', 'heightMark', 'sole_opposition', 'jie',
                       'jie_one_opposed', 'bottomMark', 'topMark', 'sole_broken_seams', 'sole_unbroken_seams',
                       'guai_iff', 'guai_sole')},
    {'en': 'Under waxing and waning no configuration with a sole line has one a step later; six steps on the sole line '
           'is back at its place; a sole line at the top passes out, leaving every line alike, and two steps on a sole '
           'line stands at the bottom.',
     'zh': '消息之律下，有独应之卦一步之后没有独应；六步之后独爻在原位复回；上位之独爻升出，留下纯卦，两步之后独爻在初位。',
     'declarations': h('soleAny_waxWane', 'and_false_of_true', 'sole_waxWane_none', 'sole_six', 'sole_top_passes')},
    {'en': 'Censuses of the text: the three 彖 statements of 上下應 (比, 小畜, 大有) are sole lines, as is 履\'s third '
           'line, and 豐 has none; the eleven line texts of 中 all stand between the ends, five in the middle, and of '
           'the five of 中行 two; the one line text of 位 (萃有位) holds its place.',
     'zh': '经文之普查：彖言“上下應”三处（比、小畜、大有）皆为独应之爻，履六三亦然，豐无；爻辭言“中”十一爻皆在两端之间，'
           '五爻居中，言“中行”五爻居中者二；爻辭言位一处（萃有位）在位。',
     'declarations': h('answeredStatements', 'answeredStatements_sole', 'lv', 'feng', 'lv_sole', 'feng_no_sole',
                       'xiaoXu_answered', 'daYou_answered', 'lineTextMiddle', 'middleCourseLines',
                       'lineTextMiddle_places', 'lineTextPlace', 'lineTextPlace_holds')},
    {'en': 'Along every run of waxing and waning the phases between the ends rise with their lines and are all turned '
           'six steps on, and the line from the bottom holds its place at two of its next four places; a sole line '
           'never lasts a step, is back six steps on, and passes from the top to the bottom in two; turned over, the '
           'run of the law backward mirrors both relations.',
     'zh': '沿消息之律的每一运行，二至五位之正随爻上升，六步后皆翻转，自初位而上之爻在其后四位中恰两处在位；独应不延续一步，'
           '六步复回，在上者两步后至初；倒转之运行在镜像之处。',
     'declarations': h('run_between_rises', 'run_placedCount', 'run_course_between', 'run_between_six',
                       'backward_between', 'backward_sole', 'run_sole')},
    {'en': 'Along every run of the change of one line, a step at an end keeps every phase between the ends and turns '
           'the opposition and alternation beside it, a step between them turns its phase, changing a sole line '
           'gives a uniform configuration and changing a line of a uniform one gives a sole line; whatever a run of '
           'any process shows, the laws of both relations hold.',
     'zh': '沿一爻之变的每一运行，一步在两端，二至五位之正不动，其旁之应与比翻转；在其间，翻转该位之正；变独爻得纯卦，'
           '纯卦变一爻得独应。任一过程的运行在任一步所示，两种关系之律皆成立。',
     'declarations': h('changes_run_between', 'changes_run_ends', 'changes_run_sole', 'between_shown_along_runs',
                       'between_glue_along_run', 'sole_shown_along_run', 'answers_shown_along_run')},
]
listed = [d for law in laws for d in law['declarations']]
assert len(listed) == len(set(listed)) and set(listed) == own, sorted(own ^ set(listed))
kinds = {k: sum(p['kind'] == k for p in y4_passages) for k in ('agreement', 'scope', 'divergence')}

record = {
    'schema_version': 2,
    'id': 'fixed-places-and-sole-lines',
    'title': {'en': 'Fixed places between the ends, and the line answered by all others',
              'zh': '初上无位与独应之爻'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': json.loads((RECORDS / 'place-relations-in-context.json').read_text())['family'],
    'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Read with no fixed place at the bottom and top, every statement of place in the 彖 and the 小象 holds; '
              'no parity of the top place can. A line answered by all others is unique, rests on no place or phase, '
              'never lasts a step of waxing and waning, and leaves at the top to enter at the bottom.',
        'zh': '以初上无位读之，彖与小象言位之句皆成立，上位任一奇偶都不能如此。独应之爻唯一，不依位与正，'
              '在消息之律下不延续一步，自上位出、自初位入。'},
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom and no premise: the places between the ends, the second relation, the answer of two lines, the '
               'sole line and the censuses are defined in the module; each spine law is used at its stated hypotheses '
               '(Contextual.fitsFree_iff with a place between the ends as home; Learning.goAlike_iff_lumped at the '
               'phases between the ends); the laws along runs hold for every run of the named process, and the '
               'shown-along-run laws for every run of every process on the configurations.',
         'zh': '不用公理、不加前提：两端之间之位、第二个关系、两爻之应、独应之爻与普查都在模块中定义；脊柱的每条律按其所列假设使用'
               '（Contextual.fitsFree_iff 以两端之间一位为所在；Learning.goAlike_iff_lumped 用于二至五位之正）；'
               '沿运行之律对所述过程的每一运行成立，所示之律对六十四卦上任一过程的每一运行成立。'},
    ],
    'does_not_show': [
        {'en': 'What any passage says beyond these relations; the chapter\'s passage map states, passage by passage, '
               'agreement, exact scope or divergence, and its readings are the AI\'s. 王弼\'s text is quoted from the '
               'edition\'s paragraphs of his, not from 邢璹\'s notes, which the edition does not mark except in 明彖.',
         'zh': '任何一段在这些关系之外所说的；章节的逐句对应逐段写明相合、定域或相分，其读法是 AI 读法。王弼之文引自此版中王弼之段，'
               '不引邢璹之注；此版除明彖外未标出两者。',
         'kind': 'correspondence'},
        {'en': 'The ranks of the places (貴賤, 尊卑); the ruling of the many by the one (治眾), the sole line\'s relation '
               'being symmetric; the other rulers 王弼 names (a middle line, a line in place, a line answered at its '
               'height); 時 read with 位; 王弼\'s line-by-line commentary (周易注), not preserved here; the 文言\'s '
               'statements of place and 中.',
         'zh': '位的贵贱尊卑；“治眾”（独应是对称的关系）；王弼所举的其他之主（居中、得位、有应之爻）；时与位合读；'
               '王弼《周易注》未存于本库；文言中言位、言中之处。',
         'kind': 'scope'},
        {'en': 'That holding a place, answering or being alone of a kind is good, fortunate, beautiful or supports 生生; '
               'the module has no ethical predicate and no judgment.',
         'zh': '在位、相应或独一是善的、吉的、美的或支持生生；模块没有伦理谓词，也没有判断。', 'kind': 'non-implication'},
    ],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {len(own)} declarations '
              f'of Becoming.HexagramSites, {module["theorems"]} of them theorems, have empty axiom reports; the checker '
              f'verifies core purity. The passage map ({len(passages)} passages, {len(y4_passages)} citing this module) '
              f'and the censuses are checked by verify_mapping.py against the preserved Wikisource revisions, the '
              f'receipt\'s declaration list and the module\'s lists; each census was mutated to confirm that the check '
              f'fails. Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.HexagramSites 的 {len(own)} 项声明'
              f'（{module["theorems"]} 项定理）公理报告为空；检查器并核对核心纯净。逐句对应（{len(passages)} 段，其中 '
              f'{len(y4_passages)} 段引本模块）与各项普查由 verify_mapping.py 对照保存的维基文库版本、回执的声明清单与模块的清单检查；'
              f'每项普查都以变异检验过。作者自审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': 'The other rulers 王弼 names (a middle line, a line in place, a line answered at its height) as relations '
              'of their own; 時 with 位 (明卦適變通爻); 王弼\'s 周易注 preserved and compared line by line; the 文言\'s '
              'statements of place; an independent review.',
        'zh': '王弼所举的其他之主（居中、得位、有应之爻）作为各自的关系；时与位合读（明卦適變通爻）；存入王弼《周易注》并逐爻对照；'
              '文言中言位之处；独立审查。'},
    'correspondence': {
        'en': f'Continues place-relations-in-context (Y2), which listed 初上无位, the line answered by all others and '
              f'王弼\'s 《周易略例》 as not done, on Ren\'s request of 19 October 2026, {GO} (provenance, not warrant). '
              f'The chapter on the 易传 maps {len(y4_passages)} passages that cite this module: {kinds["agreement"]} '
              f'agreements, {kinds["scope"]} exact scopes and {kinds["divergence"]} divergences. Reading (the AI\'s, '
              f'{decision}): the 彖 and the 象 speak of place by the second relation, and 王弼\'s argument for it is '
              f'a law of their statements; 需\'s top line moves from divergence to agreement under it while the '
              f'parity of six places stays as stated; 上下應之, 乘五剛 and 成卦之體，在斯一爻 read one line against '
              f'all the others; 王弼\'s 主 is taken as that relation and his 治眾, 貴賤 and 美 diverge.',
        'zh': f'接续 place-relations-in-context（Y2）所列未做的初上无位、一爻为众爻所应与王弼《周易略例》，按 Ren 2026年10月19日的要求'
              f' {GO}（来历，不是根据）。论易传的一章中引本模块者 {len(y4_passages)} 段：相合 {kinds["agreement"]}、'
              f'定域 {kinds["scope"]}、相分 {kinds["divergence"]}。读法（AI 的，{decision}）：彖与象言位用的是第二个关系，'
              f'王弼为之所立之论是其言之律；需上六在其下由相分变为相合，六位之奇偶如其所述保留；上下應之、乘五剛与“成卦之體，在斯一爻”'
              f'读一爻与其余诸爻；王弼之“主”只取此关系，其“治眾”“貴賤”“美”相分。'},
    'canonical_source': SRC,
    'aliases': ['初上无位', '初上無位', '初上无阴阳定位', '辯位', '卦主', '一爻为主', '独应', '上下應之', '上下應', '乘五剛',
                '周易略例', '王弼', 'the sole line', 'places between the ends', 'second relation of phase',
                'Becoming.Hexagram.top_no_parity', 'Becoming.Hexagram.holdsPlace', 'Becoming.Hexagram.sole_unique',
                'Becoming.Hexagram.sole_top_passes', 'Becoming.Hexagram.placeStatements_hold'],
    'dependencies': [
        {'id': 'place-relations-in-context', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the places, heights, seams, the relations inPhase, opposed, alternates, rises and falls, '
                          'atSites and the census of the 小象\'s statements of place; the delta is the second relation '
                          'and the answer of two lines at any pair.',
                    'zh': '复用 Becoming.HexagramPlaces 的位、高度、缝，正、应、比、承、乘诸关系，atSites 与小象言位之普查；'
                          '增量是第二个关系与任何两位之应。'},
         'interface': {'output': {'en': 'The relations of the places at their sites, their laws under the changes, and the '
                                        'statements of place of the 小象 as a checked list.',
                                  'zh': '在其所在之处的爻位之关系、其在诸变化下的律，以及作为已检查清单的小象言位之句。'},
                       'input': {'en': 'place, heightOf, below, above, odd, inPhase, opposed, alternates, rises, falls, '
                                       'middle, atSites, number, placeStatements, centreStatements.',
                                 'zh': 'place、heightOf、below、above、odd、inPhase、opposed、alternates、rises、falls、'
                                       'middle、atSites、number、placeStatements、centreStatements。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/HexagramPlaces.lean'}},
        {'id': 'hexagrams-on-the-spine', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the configurations, the received order, complement, reverse, flip, changes, waxWane '
                          'and unwaxWane of Becoming.Hexagrams.',
                    'zh': '复用 Becoming.Hexagrams 的构形、所传卦序、错、综、一爻之变、消息之律及其逆行。'},
         'interface': {'output': {'en': 'Six two-valued lines and the laws of change on them.',
                                  'zh': '六爻二值与其上的变化之律。'},
                       'input': {'en': 'Hexagram, line, same, yang, complement, reverse, flip, changes, waxWane, '
                                       'unwaxWane, rising, allBroken, six_steps, run_six_steps.',
                                 'zh': 'Hexagram、line、same、yang、complement、reverse、flip、changes、waxWane、'
                                       'unwaxWane、rising、allBroken、six_steps、run_six_steps。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Hexagrams.lean'}},
        {'id': 'contextual-registration', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Contextual, Glues, FitsFree and fitsFree_iff, reading the four places between the ends '
                          'as contexts.',
                    'zh': '复用 Contextual、Glues、FitsFree 与 fitsFree_iff，把两端之间的四位读作语境。'},
         'interface': {'output': {'en': 'A frame of context-free claims fits exactly where what the contexts show glues '
                                        'everywhere.',
                                  'zh': '去语境的框架恰在诸语境所示处处粘合时相合。'},
                       'input': {'en': 'atSites betweenPhase, home a place between the ends.',
                                 'zh': 'atSites betweenPhase，所在为两端之间一位。'},
                       'conditions': {'en': 'Every context lies within its home (trivially).',
                                      'zh': '每一语境在其所在之内（平凡成立）。'},
                       'evidence': f'{PKG}/Becoming/Context.lean'}},
        {'id': 'generalization-through-lumping', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Learning.Lumped and Learning.goAlike_iff_lumped for the phases between the ends under '
                          'waxWane.',
                    'zh': '对 waxWane 下二至五位之正复用 Learning.Lumped 与 Learning.goAlike_iff_lumped。'},
         'interface': {'output': {'en': 'A reading the law goes alike across exactly where it is a lumping.',
                                  'zh': '律在其上同行的读法，恰是归并。'},
                       'input': {'en': 'betweenPhases under waxWane.', 'zh': 'waxWane 下的 betweenPhases。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Learning.lean'}},
    ],
    'related': [],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted(own), 'sha256': sha(SRC)},
        {'path': core_receipt, 'role': 'receipt', 'declarations': [], 'sha256': sha(core_receipt)},
        {'path': f'{PKG}/Becoming/HexagramPlaces.lean', 'role': 'proof',
         'declarations': spine('Hexagram.place', 'Hexagram.heightOf', 'Hexagram.below', 'Hexagram.above',
                               'Hexagram.odd', 'Hexagram.inPhase', 'Hexagram.opposed', 'Hexagram.alternates',
                               'Hexagram.rises', 'Hexagram.falls', 'Hexagram.middle', 'Hexagram.atSites',
                               'Hexagram.atSites_glues_iff_constant', 'Hexagram.number', 'Hexagram.opposition',
                               'Hexagram.opposed_iff_phase', 'Hexagram.inPhase_waxWane_above',
                               'Hexagram.placeStatements', 'Hexagram.centreStatements', 'Hexagram.phases_glue_iff',
                               'Hexagram.backward_run'),
         'sha256': sha(f'{PKG}/Becoming/HexagramPlaces.lean')},
        {'path': f'{PKG}/Becoming/Hexagrams.lean', 'role': 'proof',
         'declarations': spine('Hexagram', 'Hexagram.line', 'Hexagram.same', 'Hexagram.yang', 'Hexagram.complement',
                               'Hexagram.reverse', 'Hexagram.flip', 'Hexagram.changes', 'Hexagram.waxWane',
                               'Hexagram.unwaxWane', 'Hexagram.rising', 'Hexagram.allBroken', 'Hexagram.six_steps',
                               'Hexagram.run_six_steps'),
         'sha256': sha(f'{PKG}/Becoming/Hexagrams.lean')},
        {'path': f'{PKG}/Becoming/Context.lean', 'role': 'proof',
         'declarations': spine('Contextual', 'Contextual.Glues', 'Contextual.FitsFree', 'Contextual.fitsFree_iff'),
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
    ] + [
        {'path': f'sources/zhouyi-yizhuan/lueli/{page}.json', 'role': 'provenance', 'declarations': [],
         'sha256': sha(f'sources/zhouyi-yizhuan/lueli/{page}.json')} for page in LUELI
    ] + [
        {'path': SOURCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(SOURCE)},
    ],
    'proof_bindings': [
        {'source': f'{PKG}/Becoming/{name}.lean', 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/Becoming.{name}',
         'success_pointer': '/status', 'success_value': 'passed'}
        for name in BOUND
    ],
    'history': [
        {'en': f'19 October 2026: added (Y4), continuing Y2 on Ren\'s {GO}; study section {section}, decision {decision}.',
         'zh': f'2026年10月19日：新增（Y4），接续 Y2，按 Ren 的 {GO}；研究第 {section} 节，决定 {decision}。'},
    ],
}
assert len(record['statement']['en']) <= 300 and len(record['statement']['zh']) <= 150, (
    len(record['statement']['en']), len(record['statement']['zh']))
(RECORDS / 'fixed-places-and-sole-lines.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')


def repoint(rec, note_en, note_zh):
    """Re-point the statement, integration and provenance references Y4 changed, after reading the change."""
    changed = []
    for ref in rec['references']:
        if ref['role'] in ('statement', 'integration', 'provenance') and ref['sha256'] != sha(ref['path']):
            ref['sha256'] = sha(ref['path'])
            changed.append(ref['path'].rsplit('/', 1)[-1])
    rec['history'].append({'en': note_en.format(', '.join(changed) or 'no reference'),
                           'zh': note_zh.format('、'.join(changed) or '无引用')})
    return changed


# Y2's record: 初上无位, the line answered by all others and the 《周易略例》 are done.
y2_path = RECORDS / 'place-relations-in-context.json'
y2 = json.loads(y2_path.read_text())
scope = next(x for x in y2['does_not_show'] if x['kind'] == 'scope')
OLD_EN = ('The ranks of the places (尊位, 貴賤); whether the bottom and top places have a place (初上无位); one line '
          'answered by all others (上下應之, 乘五剛); statements of place outside the four censuses; 王弼\'s '
          '《周易略例》, not preserved here.')
OLD_ZH = ('位的尊卑（尊位、贵贱），初上两位是否有位（初上无位），一爻为众爻所应（上下應之、乘五剛），以及四项普查之外'
          '关于位的言说（爻辞、大象、文言）；王弼《周易略例》未存于本库，未对照。')
assert scope['en'].startswith(OLD_EN) and scope['zh'].startswith(OLD_ZH), scope
# Keep what later items added after Y2's text (Y2b: the censuses of the sixty-four by each count).
rest_en, rest_zh = scope['en'][len(OLD_EN):], scope['zh'][len(OLD_ZH):]
scope['en'] = ('The ranks of the places (尊位, 貴賤); the reading with no fixed place at the bottom and top (初上无位), '
               'the line answered by all others (上下應之, 乘五剛), the censuses of the line texts and the 大象, and '
               '王弼\'s 《周易略例》 are in fixed-places-and-sole-lines; the 文言\'s statements of place.') + rest_en
scope['zh'] = ('位的尊卑（尊位、贵贱）；初上无位之读、一爻为众爻所应（上下應之、乘五剛）、爻辭与大象之普查与王弼《周易略例》，'
               '见 fixed-places-and-sole-lines；文言中关于位的言说。') + rest_zh
NEXT_EN = ('王弼\'s reading that the bottom and top lines have no place, as a second relation on places 2 to 5, once '
           'the 《周易略例》 is preserved; the relation of one line to all the others (卦主); censuses of the line '
           'texts, the 大象 and the 文言; ')
NEXT_ZH = ('王弼“初上无位”之读，作为二至五位上的另一关系，待《周易略例》存入本库；一爻与其余诸爻的关系（卦主）；'
           '爻辞、大象与文言的普查；')
assert y2['next_delta']['en'].startswith(NEXT_EN) and y2['next_delta']['zh'].startswith(NEXT_ZH), y2['next_delta']
y2['next_delta']['en'] = 'A census of the 文言; ' + y2['next_delta']['en'][len(NEXT_EN):]
y2['next_delta']['zh'] = '文言的普查；' + y2['next_delta']['zh'][len(NEXT_ZH):]
if not any(r['id'] == 'fixed-places-and-sole-lines' for r in y2['related']):
    y2['related'].append({'id': 'fixed-places-and-sole-lines',
                          'detail': {'en': '王弼\'s second relation of phase on places 2 to 5 beside inPhase, under which '
                                           '需\'s top line agrees, and the line answered by all others.',
                                     'zh': '王弼在二至五位上的第二个关系，在 inPhase 之旁，需上六在其下相合；以及独应之爻。'}})
y2_changed = repoint(
    y2,
    f'19 October 2026, Y4 (王弼\'s readings of the places): 初上无位, the line answered by all others and the '
    f'《周易略例》, listed as not shown and as the next delta, are now the record fixed-places-and-sole-lines (study '
    f'section {section}, decision {decision}); the passages on 小畜, 大有, 夬, 履六三 and 需上六 cite it, 需上六 now '
    f'an agreement under the second relation while xu_top_inPhase stands; {{}} re-pointed after reading the change '
    f'(Y4 added its passages, censuses, chapter text, study section, canonical paragraph and preserved pages). The '
    f'claim is unchanged.',
    f'2026年10月19日，Y4（王弼之读）：原列为未示与下一步的初上无位、一爻为众爻所应与《周易略例》，现为记录 '
    f'fixed-places-and-sole-lines（研究第 {section} 节，决定 {decision}）；小畜、大有、夬、履六三与需上六各段引之，'
    f'需上六在第二个关系下改为相合，xu_top_inPhase 仍成立；读过改动后，{{}} 重新指向。论断不变。')
y2_path.write_text(json.dumps(y2, ensure_ascii=False, indent=2) + '\n')

# Y1's record: only the references Y4 changed.
y1_path = RECORDS / 'hexagrams-on-the-spine.json'
y1 = json.loads(y1_path.read_text())
y1_changed = repoint(
    y1,
    f'19 October 2026, Y4 (王弼\'s readings of the places, record fixed-places-and-sole-lines, study section '
    f'{section}): {{}} re-pointed after reading the change (Y4 added its passages, censuses, chapter text, study '
    f'section, canonical paragraph and the preserved pages of the 《周易略例》). The claim is unchanged.',
    f'2026年10月19日，Y4（王弼之读，记录 fixed-places-and-sole-lines，研究第 {section} 节）：读过改动后，{{}} 重新指向。论断不变。')
y1_path.write_text(json.dumps(y1, ensure_ascii=False, indent=2) + '\n')
print('written', len(own), 'declarations in', len(laws), 'laws;', len(y4_passages), 'of', len(passages),
      'passages cite the module; Y2 re-pointed:', y2_changed, '; Y1 re-pointed:', y1_changed)
