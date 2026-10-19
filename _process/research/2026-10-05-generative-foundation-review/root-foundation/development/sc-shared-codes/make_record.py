#!/usr/bin/env python3
"""Write SC's record: python3 -B make_record.py CORE_RECEIPT   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of the module (a short name must match
exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE_CHAPTER = 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
PASSAGES = ('_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources/'
            'passages.json')
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'SharedCodes'
RID = 'a-code-formed-between-formations'
core_id = sys.argv[1]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
section = re.search(r'^## (\d+)\. A code formed between formations \(SC\)$', (ROOT / STUDY).read_text(), re.M)
assert section, 'study section missing'
N = section.group(1)
decision = re.search(r'^\| D(\d+) \| a code formed between formations', (ROOT / STUDY).parent.joinpath(
    'DELEGATED-CHOICES.md').read_text(), re.M)
assert decision, 'decision missing'
D = decision.group(1)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


m = next(m for m in core['modules'] if m['module'] == f'Becoming.{MOD}')
assert core['source_sha256'][f'Becoming.{MOD}'] == sha(src(MOD)), 'receipt does not bind the module'
assert not any(m['axiom_dependencies'].values())
FULL = [d['name'] for d in m['declarations']]
n_decl, n_thm = len(FULL), m['theorems']


def resolve(names):
    out = []
    for n in names:
        hits = [f for f in FULL if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (n, hits)
        out.append(hits[0])
    return out


def dep(rid, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': 'formal-reuse', 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


STATEMENT = {
    'en': 'Codes changed only by hearing keep agreement exactly through closed hearings; the start and the order fix the '
          'form reached; reading across holds where codes agree; no law privileging neither form nor formation settles a '
          'symmetric disagreement; imposed and written-back codes stay.',
    'zh': '只经听取而变的编码，恰经封闭的听取保持相合；所成之形由起点与次序固定；编码相合处可互读；既不特许形式也不特许形成者的律不能解决对称的'
          '分歧；强加的与写回的编码保持。'}
assert len(STATEMENT['en']) <= 300, len(STATEMENT['en'])

LAWS = [
    ('Hearing is a process of the spine, a stretch of its run an order of hearings, and every start and sequence of '
     'hearings has its run; hearing makes no form, and a step changes a form exactly at its hearer, at the sense heard, '
     'where the rule takes the form and the speaker\'s form differs.',
     '听取是脊柱的一个过程，其运行的一段是一个听取次序，每个起点与听取序列都有其运行；听取不造新形，一步恰在其听者、所听之义、规则取形且说者之形'
     '不同处改变一形。',
     ['process', 'step_at', 'window_runBy', 'state_hearings', 'hearingRun', 'run_held', 'run_changes_iff']),
    ('A group agreeing at a sense keeps agreeing through every hearing closed for it, exactly unless a member hears the '
     'sense, the rule takes the form and the speaker\'s form is not the group\'s; along runs so closed no member\'s form '
     'changes, and agreement of all is a rest under every rule.',
     '在某义上相合的一组经每个对它封闭的听取保持相合，恰除非某成员听此义、规则取形且说者之形不是该组之形；沿如此封闭的运行，无成员之形改变；'
     '全体相合在每条规则下都是静止。',
     ['agreement_kept', 'kept_iff', 'run_kept_iff', 'run_kept', 'run_agreement_kept', 'pair_kept', 'all_agree_rest']),
    ('Under hearings that take the form heard, each formation holds the start\'s form of its origin; where two forms '
     'differ, every run with given hearings agrees from every start exactly where they give all formations one origin; '
     'the forms that can become shared are exactly the forms in use.',
     '在取所听之形的听取下，每个形成持有起点处其来源之形；两形不同时，有给定听取的每个运行恰在这些听取给所有形成同一来源时从每个起点相合；可成为'
     '共有者恰是在用之形。',
     ['run_origin', 'run_origin_window', 'agrees_every_start_iff', 'run_agrees_every_start_iff', 'shared_iff_in_use',
      'run_shared_iff_in_use', 'TwoFormations.order_decides']),
    ('Under a pointer law every start agrees at a step exactly where the pointer\'s paths have met; being joined through '
     'couplings is not enough: on the path a – c – b with each following the least-indexed of itself and its couplings, '
     'a and b never agree.',
     '在指针律下，每个起点恰在指针之路已相遇的那一步相合；经耦合相连并不够：在路 a – c – b 上，各取其自身与所耦合者中编号最小者，a 与 b 永不'
     '相合。',
     ['follow', 'follow_state', 'follow_agrees_iff', 'Path.never_agree']),
    ('A formation whose code tells senses apart reads another\'s form for a sense as that sense, and only it, exactly '
     'where their codes agree there, and otherwise as another sense; a hearing keeps the hearer telling senses apart '
     'exactly where the form taken is not one it gives another sense, so agreement sense by sense can merge senses.',
     '编码分别诸义的形成，恰在两编码于某义相合处把对方此义之形读作此义且只读作此义，否则读作另一义；一次听取恰在所取之形不是听者给另一义之形时，'
     '保持听者分别诸义，所以逐义的相合可以合并诸义。',
     ['self_reads_iff', 'reads_iff', 'reads_other', 'run_reads_iff', 'run_reads_kept', 'keeps_apart_iff',
      'run_keeps_apart_iff', 'TwoFormations.homonym']),
    ('No form is privileged: runs through one order from starts differing by a renaming differ by it at every step, '
     'tell apart the same senses, and a renamed description carries a law exactly where the description does.',
     '不特许任何形式：经同一次序、起点相差一个改名的运行每步都相差此改名，分别同样的义；改名后的描述恰在原描述承载规律处承载规律。',
     ['hearBy_keeps_renaming', 'run_renamed', 'reached_differ_iff', 'run_renamed_tells_apart_iff', 'renamed_goAlike_iff',
      'renamed_carries_iff']),
    ('Agreement needs a broken symmetry: a law keeping an exchange of formations and a renaming of forms keeps a '
     'symmetric start symmetric, so formations it exchanges never agree where the renaming moves every form; a centre, '
     'a preferred form and an order of hearing each break one symmetry and bring agreement.',
     '相合需要打破对称：保持形成之交换与形式之改名的律使对称的起点保持对称，所以在改名移动每个形之处，它所交换的形成永不相合；中心、偏好之形与'
     '听取次序各打破一个对称而带来相合。',
     ['Law.KeepsRelation.run', 'Law.Commutes.keepsRelation', 'keeps_both', 'symmetric_kept', 'agrees_only_fixed',
      'never_agrees', 'never_agrees_of_both', 'pair_agrees_only_fixed', 'pair_never_agrees',
      'TwoFormations.crossing_never_agrees', 'TwoFormations.three_agree', 'TwoFormations.centre_breaks_exchange',
      'TwoFormations.preferred_breaks_renaming', 'TwoFormations.ordered_breaks_exchange']),
    ('An imposed code makes all agree and read each other where it tells senses apart; each formation loses what its '
     'code told apart and the imposed code merges, its source nothing; along every later run of hearing this stays, and '
     'a merged distinction comes back only from a form kept outside.',
     '强加的编码使所有人相合，并在它分别诸义处互读；每个形成失去其编码所分而强加编码所合并者，其来源一无所失；沿此后每个听取运行这些保持，'
     '被合并的分别只从外面保留的形式回来。',
     ['impose_agrees', 'impose_reads', 'impose_loses_iff', 'source_loses_nothing', 'held_stays', 'run_imposed_stays',
      'run_from_imposition', 'outside_needed', 'outside_returns']),
    ('A resolution written back into the records later generations read rests from the next generation on, merges the '
     'histories resolving alike, so no later reading recovers them, and under omission rests away from the target; '
     'kept records bar a different resolution, and where records are only added a resolution is lost but never '
     'replaced.',
     '写回后代所读记录的判定自下一代起静止，合并判定相同的历史，所以后来的读法读不回它们；遗漏之下静止于所指之外；保留的记录阻止不同的判定；'
     '记录只增补处，判定可失去而不被替换。',
     ['resolve', 'generation', 'WritesExactly', 'written_rests', 'every_generation_resolves', 'resolved_alike_merged',
      'generation_merges', 'no_reading_recovers', 'covered_rest', 'omitted_rest', 'kept_bars', 'kept_rests', 'adding',
      'added_never_replaced', 'Gloss.taken_up_locks', 'Gloss.uptake_loses']),
]

COUNTER = [
    {'path': src(MOD), 'detail': {
        'en': 'The proposed coupling form refuted (Path.never_agree): on the path a – c – b, every two formations joined '
              'through couplings and each adopting at once the code of the least-indexed of itself and its couplings, '
              'a and b each point to themselves and never agree, so agreement under that law is not equivalent to every '
              'coupling closure being the whole.',
        'zh': '原拟耦合形式之反例（Path.never_agree）：在路 a – c – b 上，任两形成经耦合相连，各即刻取其自身与所耦合者中编号最小者之码，a 与 b '
              '各指向自身，永不相合；所以该律之下的相合不等价于每个耦合闭包为全体。'}},
    {'path': src(MOD), 'detail': {
        'en': 'A symmetric law never agrees (TwoFormations.crossing_never_agrees): two formations each taking the other\'s '
              'form at once exchange their forms forever.',
        'zh': '对称的律永不相合（TwoFormations.crossing_never_agrees）：两个形成各即刻取对方之形，永远互换其形。'}},
    {'path': src(MOD), 'detail': {
        'en': 'Agreement can cost distinctions (TwoFormations.homonym): two codes each telling two senses apart, one '
              'hearing the other at one sense, leave the hearer one form for both.',
        'zh': '相合可以付出分别（TwoFormations.homonym）：两个各分别两义的编码，一方在一义上听另一方，使听者对两义只有一形。'}},
]
resolve(['Path.never_agree', 'TwoFormations.crossing_never_agrees', 'TwoFormations.homonym'])

BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']

DEPS = [
    dep('what-a-commuting-law-keeps-apart',
        'Uses Law.Commutes and its run laws: Law.Commutes.keepsRelation is the relational form of keeps_fixed, and '
        'pair_agrees_only_fixed reads it on two formations.',
        '使用 Law.Commutes 及其运行之律：Law.Commutes.keepsRelation 是 keeps_fixed 的关系形式，pair_agrees_only_fixed 在两个形成上读之。',
        'A law commuting with a map keeps the relation of a configuration to its image along its runs.',
        '与一映射交换的律沿其运行保持构形与其像的关系。',
        'From a pair the joint exchange fixes, the two formations agree only on a form the renaming fixes.',
        '从联合交换所固定的一对出发，两个形成只在改名所固定的形上相合。',
        'The law commutes with exchanging the two formations together with the forms.',
        '律与同时交换两个形成及其形相交换。', src('Commuting')),
    dep('projection-carrying-a-law',
        'Uses carries_law_iff: renamed_carries_iff states that a renamed description carries a law exactly where the '
        'description does.',
        '使用 carries_law_iff：renamed_carries_iff 说改名后的描述恰在原描述承载规律处承载规律。',
        'A projection carries a determined law exactly where configurations alike under it go alike.',
        '一个投影恰在其下相同的构形同样变化时承载确定的规律。',
        'Renaming forms by a map telling them apart keeps which descriptions carry a law.',
        '以分别诸形的映射改名，保持哪些描述承载规律。',
        'The renaming tells forms apart.', '改名分别诸形。', src('Mechanism')),
    dep('recurrence-without-premise',
        'Uses Law.orbit, Law.run, Law.Merges and Law.merged_stays for the pointer law and the generations of records.',
        '对指针律与记录的代际使用 Law.orbit、Law.run、Law.Merges 与 Law.merged_stays。',
        'What a law merges stays merged along its runs.', '律所合并者沿其运行保持合并。',
        'Two histories of records resolving alike are one from the next generation on, and no later reading recovers '
        'them.',
        '判定相同的两段记录史自下一代起合一，后来的读法读不回它们。',
        'Each generation writes a record offering exactly what it resolved.', '每一代写下恰提供其所判定者的记录。',
        src('Recurrence')),
]

RELATED = [
    {'id': 'chinese-sources-on-the-spine',
     'detail': {'en': 'Closes the second of its seven gaps (a code formed between formations); four passages of its map '
                      'are re-pointed to these laws.',
                'zh': '补上其七项缺口中的第二项（在形成之间形成的编码）；其逐句对应中的四段改指向这些律。'}},
    {'id': 'what-finitely-many-labels-fix',
     'detail': {'en': 'A code read off finitely many labels of a given feature: supplied to one side, where here the code '
                      'forms between formations.',
                'zh': '从给定特征的有限多个标签读出编码：编码给予一方；此处编码在形成之间形成。'}},
    {'id': 'historical-source-binding',
     'detail': {'en': 'Dated controls separate rival histories; here records kept from before are what bar a reading '
                      'written back (kept_bars).',
                'zh': '有日期的对照分开对手的历史；此处是此前保留的记录阻止写回的读法（kept_bars）。'}},
]

record = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'A code formed between formations', 'zh': '在形成之间形成的编码'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': STATEMENT,
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(names)} for en, zh, names in LAWS],
    'hypotheses': [
        {'en': 'No axiom. The codes, the hearings and the rule of adoption are given; every other premise is named where '
               'it is used: hearings closed for a group; hearings that take the form heard; two forms that differ; a list '
               'of every formation; a rule reading codes alike after a renaming; a law keeping an exchange and a renaming; '
               'a renaming moving every form at the sense; records written to offer exactly what was resolved; decided '
               'equality of formations and senses where an order is stepped back through.',
         'zh': '不加公理。编码、听取与采纳规则是给定的；其余每个前提都在用到之处具名：对一组封闭的听取；取所听之形的听取；两个不同的形；列出每个'
               '形成的列表；在改名后同样读编码的规则；保持一个交换与一个改名的律；在该义上移动每个形的改名；写下恰提供所判定者的记录；在回溯次序之处'
               '形成与义的相等可判定。'}],
    'does_not_show': [
        {'en': 'Which orders actual exchange takes, with probabilities over orders, and how long agreement takes: the voter '
               'model\'s and the naming game\'s expectations are not stated.',
         'zh': '实际交换取哪些次序、次序上的概率，以及相合需要多久：投票者模型与命名博弈的期望未陈述。', 'kind': 'scope'},
        {'en': 'Codes holding several forms for a sense, rules reading more than the two codes, adoption of whole codes, '
               'and an exact step bound for a pointer law on finite sets.',
         'zh': '一义多形的编码、读两个编码之外内容的规则、整码采纳，以及有限集上指针律的确切步数界。', 'kind': 'scope'},
        {'en': 'That actual conventions, scripts or the theory\'s own terms form by hearing in this way, or whether a '
               'shared, imposed or kept code supports or damages 生生.',
         'zh': '实际的约定、文字或理论自己的术语以这种听取方式形成，或共有的、强加的、保留的编码支持还是损害生生。',
         'kind': 'non-implication'}],
    'counterexamples': COUNTER,
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author review in study section {N}; readings D{D}; not independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者审查见研究第 {N} 节；读法 D{D}；未经人的独立审查。'},
    'next_delta': {
        'en': 'Probabilities over orders and the time agreement takes; codes with several forms for a sense; adoption of '
              'whole codes; the step bound of a pointer law on finite sets; an independent review.',
        'zh': '次序上的概率与相合所需的时间；一义多形的编码；整码采纳；有限集上指针律的步数界；独立审查。'},
    'correspondence': {
        'en': 'RO\'s chapter on the Chinese sources found the spine lacking a law of a code formed between formations '
              '(荀子 正名: 名无固宜，约定俗成谓之宜; 同则同之，异则异之), of an imposed code (說文叙: 书同文) and of a reading '
              'written back (說文: 止戈为武). Hearing by adoption is the voter model and the naming game, the codes those of '
              'Lewis signalling systems, the symmetry law equivariance (Curie\'s principle). The readings onto the texts '
              f'are the AI\'s (D{D}).',
        'zh': 'RO 关于中国思想诸传统的一章发现，脊柱缺在形成之间形成的编码之律（荀子正名：名无固宜，约定俗成谓之宜；同则同之，异则异之）、强加的'
              '编码之律（说文叙：书同文）与写回的读法之律（说文：止戈为武）。以采纳而听取即投票者模型与命名博弈，编码即 Lewis 信号系统之编码，'
              f'对称之律即等变性（居里原理）。对原典的读法是 AI 的（D{D}）。'},
    'canonical_source': src(MOD),
    'aliases': [
        'a code formed between formations', 'shared codes', '约定俗成', '在形成之间形成的编码', 'agreement needs a broken symmetry',
        'Becoming.SharedCodes.kept_iff', 'Becoming.SharedCodes.run_agrees_every_start_iff',
        'Becoming.SharedCodes.never_agrees_of_both', 'Becoming.SharedCodes.run_from_imposition',
        'Becoming.SharedCodes.written_rests', 'Becoming.SharedCodes.Path.never_agree'],
    'dependencies': DEPS,
    'related': RELATED,
}
cited = {src(MOD)}
extra = []
for d in DEPS:
    e = d['interface']['evidence']
    if e not in cited:
        cited.add(e)
        extra.append(e)
for extra_source in (src('CrossSituational'),):
    if extra_source not in cited:
        cited.add(extra_source)
        extra.append(extra_source)
record['references'] = (
    [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(FULL), 'sha256': sha(src(MOD))}]
    + [{'path': p, 'role': 'proof', 'sha256': sha(p)} for p in extra]
    + [{'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
       {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
       {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
       {'path': SOURCE_CHAPTER, 'role': 'provenance', 'sha256': sha(SOURCE_CHAPTER)},
       {'path': PASSAGES, 'role': 'provenance', 'sha256': sha(PASSAGES)}])
record['proof_bindings'] = [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                             'success_pointer': '/status', 'success_value': 'passed'}]
record['history'] = [{
    'en': f'19 October 2026: added (SC), the second gap of RO\'s chapter on the Chinese sources; study section {N}, '
          f'readings D{D}.',
    'zh': f'2026年10月19日：新增（SC），即 RO 关于中国思想诸传统一章的第二项缺口；研究第 {N} 节，读法 D{D}。'}]
path = RECORDS / f'{RID}.json'
assert not path.exists(), 'record exists'
path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('written', RID, n_thm, n_decl)
