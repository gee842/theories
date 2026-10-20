#!/usr/bin/env python3
"""Write EV5's record and note it in the record it continues (selection-within-and-among-groups):
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.GroupEnding (a short
name must match exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
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
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'GroupEnding'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. Selection among groups by ending, through conditions of their own (EV5)'
assert re.search('^' + re.escape(HEAD) + '$', (ROOT / STUDY).read_text(), re.M)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


def decls(mod):
    m = next(m for m in core['modules'] if m['module'] == f'Becoming.{mod}')
    assert core['source_sha256'][f'Becoming.{mod}'] == sha(src(mod)), ('receipt does not bind', mod)
    return m


def resolve(mod, names):
    full = [d['name'] for d in decls(mod)['declarations']]
    out = []
    for n in names:
        hits = [f for f in full if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (mod, n, hits)
        out.append(hits[0])
    return out


m = decls(MOD)
assert not any(m['axiom_dependencies'].values())
n_decl, n_thm = len(m['declarations']), sum(1 for d in m['declarations'] if d.get('kind') == 'theorem')

BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


RID = 'selection-among-groups-by-ending'
LV = 'selection-within-and-among-groups'
S = 'GroupEnding.'
F = 'GroupEnding.Flow.'
laws = [
    ('Where every group with less of an amount than another leaves no offspring, nothing is discordant among the groups; '
     'so the whole selects for the amount exactly where k times the within-group discordance is below k times the '
     'within-group concordance with the concordance among groups.',
     '每个某量少于另一组的组都不留后代时，组间无不一致；故整体恰在 k 倍组内不一致度低于 k 倍组内一致度加组间一致度时选择该量。',
     [S + 'Ended', S + 'excess_pos_of_lt', S + 'among_not_against', S + 'rises_iff_ended']),
    ('With groups uniform in the amount as well, the whole never selects against it, and selects for it wherever a group '
     'with more of it leaves offspring beside one with less.',
     '各组在该量上也均匀时，整体从不逆向于它；凡有某量较多且留下后代的组与较少的组并存，整体就选择它。',
     [S + 'not_against_of_ended', S + 'pairs_pos', S + 'rises_of_ended']),
    ('Where only active formations give, a formation not active at a step leaves no descendant across it; a member '
     'depending, at a need of at least m, on a condition whose gated renewal ran into joint excess leaves none from then '
     'on.',
     '只有活跃的形成给予时，在某一步不活跃的形成不跨该步留下后代；以至少 m 的需要依存于其门控更新遭遇共同过度之条件的成员，此后不留后代。',
     [F + 'inactive_childless', F + 'excess_childless']),
    ('Over generations of descent a member not active has offspring number nothing, a group of such members leaves no '
     'offspring, and where the groups with less of the amount are such groups, those groups leave nothing.',
     '在世系世代中，不活跃的成员后代数为零，由这样的成员组成的组不留后代；某量较少的组皆为这样的组时，它们不留任何后代。',
     [F + 'offspring_zero', F + 'group_childless', S + 'mem_whole', F + 'ended_of_inactive']),
    ('With exact transmission and groups uniform in the amount, where the groups with less of it are not active and a '
     'group with more of it leaves offspring beside one with less, the mean amount rises across the step.',
     '传递精确且各组在该量上均匀时，若某量较少的组不活跃，且有某量较多、留下后代的组与较少的组并存，则平均量跨该步上升。',
     [F + 'raises_of_inactive']),
    ('Where every member of a generation is not active, as where every group depends on one condition that ran into joint '
     'excess, the next generation is empty: one shared condition leaves no group to select among.',
     '一代的每个成员都不活跃时，例如每个组都依存于同一个遭遇共同过度的条件，下一代为空：一个共同条件不留下可供组间选择的组。',
     [F + 'all_end']),
    ('Witnesses: the keeping group and a group whose condition ended. With the member holding back leaving one offspring '
     'and its groupmate two, selection among groups outweighs selection within and the whole selects for holding back; '
     'with the groupmate leaving five, selection within outweighs and the whole goes against it.',
     '见证：保持之组与条件已终止之组。保留者留下一个后代、同组者两个时，组间选择胜过组内选择，整体选择保留；同组者留下五个时，组内选择胜出，整体逆向于保留。',
     [S + 'keepingFirst', S + 'keeps', S + 'uniform', S + 'equal', S + 'Outweighed.outweighed',
      S + 'Outweighed.keeping_rises', S + 'Outweighs.outweighs']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))

LV_DEP = dep(LV, 'formal-reuse',
             'Reuses Becoming.SelectionLevels\' division of the selection term (levels, rises_iff, levels_of_uniform) and '
             'the family listed by groups (whole).',
             '复用 Becoming.SelectionLevels 对选择项的划分（levels、rises_iff、levels_of_uniform）与逐组列出的族（whole）。',
             'The selection term divided into within-group and among-group parts.', '分为组内与组间两部分的选择项。',
             'The among-group part fixed by ending.', '由终止所定的组间部分。',
             'Groups of equal size.', '各组大小相等。', src('SelectionLevels'))
GATE_DEP = dep('own-count-misses-joint-excess', 'formal-reuse',
               'Reuses Becoming.Continuation\'s Flow.joint_excess_ends: joint excess ends gated renewal and every '
               'formation depending on the condition at such a need.',
               '复用 Becoming.Continuation 的 Flow.joint_excess_ends：共同过度终止门控更新，以及以这样的需要依存于该条件的每个形成。',
               'Members depending on a condition that ran into joint excess are not active from then on.',
               '依存于遭遇共同过度之条件的成员此后不活跃。',
               'Such members leave no descendants, and their group no offspring.', '这样的成员不留后代，其组不留后代。',
               'Balance, only active formations giving, activity needing support, the gate.', '平衡、只有活跃的形成给予、活动需要支持、门控。',
               src('Continuation'))

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'Selection among groups by ending', 'zh': '经由终止的组间选择'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Where groups with less of an amount leave no offspring, nothing is selected against it among groups; on the '
              'base, a group whose own condition ran into joint excess leaves none. One condition shared by every group '
              'ends every group, so it supplies no selection among them.',
        'zh': '某量较少的组不留后代时，组间无逆向于它的选择；在流上，自身条件遭遇共同过度的组不留后代。每个组共享的一个条件终止每个组，故不提供组间选择。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. Groups of equal size for the division. On the base: only active formations give, activity needs '
              'support, balance at the condition, the gate (whatever gives to it depends on it at a need of at least m), '
              'n steps of joint excess from a level below n + m, members depending on the condition at such a need. Over '
              'generations: descent, the generation listed as the groups, groups uniform in the amount and exact '
              'transmission where named.',
        'zh': '不加公理。划分需各组大小相等。流上：只有活跃的形成给予、活动需要支持、该条件处的平衡、门控（给予它的都以至少 m 的需要依存于它）、自低于 n + m 的水平起 n 步共同过度、成员以这样的需要依存于该条件。世代：世系、该代列为这些组、所列处各组在该量上均匀且传递精确。'}],
    'does_not_show': [
        {'en': 'Which group\'s condition runs into joint excess, or why: it is a hypothesis wherever it enters, as is that '
               'members depend on their own group\'s condition.',
         'zh': '哪个组的条件遭遇共同过度，或为什么：凡出现处都是假设；成员依存于本组条件亦然。', 'kind': 'scope'},
        {'en': 'Mixed groups and inexact transmission: there selection within the surviving groups enters and can outweigh '
               '(Outweighs); mixing between groups and groups whose conditions are coupled are not stated.',
         'zh': '混合的组与不精确的传递：此时幸存组内的选择进入并可能胜出（Outweighs）；组间混合与条件相互耦合的组未陈述。', 'kind': 'scope'},
        {'en': 'How groups form, or that keeping a condition is better: ending is read in the counts; ranking goes through '
               'the comparison C.',
         'zh': '组如何形成，或维持条件更好：终止在计数中读出；排序经由比较 C。', 'kind': 'non-implication'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Ending among groups does not decide the whole: with the other group ended, a groupmate leaving five against '
              'one holding back leaving one makes the whole select against holding back (Outweighs.outweighs).',
        'zh': '组间的终止不决定整体：另一组已终止时，同组者留下五个、保留者留下一个，使整体逆向于保留（Outweighs.outweighs）。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Built and reviewed in one session, with no separate reviewer; author review in study section {N}; not '
              'independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'Groups whose conditions are coupled (a neighbour reseeding); mixing between groups; how groups form; an '
              'independent review.',
        'zh': '条件相互耦合的组（邻居补种）；组间混合；组如何形成；独立审查。'},
    'correspondence': {
        'en': 'Group selection by differential extinction (Wright 1945; Levins 1970 on metapopulation extinction; Wilson '
              'and Sober 1994): groups whose members overuse a resource of their own go extinct, while within each group '
              'selection may favour overuse. Here extinction is the gated ending of the group\'s own condition, and the '
              'shared-condition corollary is the tragedy of the commons read with descent (Hardin 1968). Readings (the '
              'AI\'s): a condition of one\'s own is what lets ending select among groups; a commons shared by all ends all.',
        'zh': '经由差异性灭绝的组选择（Wright 1945；Levins 1970 论集合种群灭绝；Wilson 与 Sober 1994）：成员过度使用自身资源的组灭绝，而各组内的选择可能偏向过度使用。此处灭绝即组自身条件的门控终止；共同条件的推论即连同世系读出的公地悲剧（Hardin 1968）。读法（AI 的）：自身的条件使终止能在组间选择；所有人共享的公地终止所有人。'},
    'canonical_source': src(MOD),
    'aliases': ['selection among groups by ending', '经由终止的组间选择', 'group selection by extinction',
                'Becoming.GroupEnding.rises_iff_ended', 'Becoming.GroupEnding.Flow.excess_childless',
                'Becoming.GroupEnding.Flow.raises_of_inactive', 'Becoming.GroupEnding.Flow.all_end'],
    'dependencies': [LV_DEP, GATE_DEP],
    'related': [
        {'id': LV, 'detail': {'en': 'Its among-group part fixed by ending on the base.', 'zh': '其组间部分由流上的终止所定。'}},
        {'id': 'what-bounds-offspring-numbers', 'detail': {
            'en': 'Lineages ending within closed families, read here for groups on conditions of their own.',
            'zh': '在封闭族内终止的世系，此处对依存于自身条件的组读出。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('SelectionLevels'), 'role': 'proof', 'sha256': sha(src('SelectionLevels'))},
                   {'path': src('Continuation'), 'role': 'proof', 'sha256': sha(src('Continuation'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (EV5), selection among groups fixed by ending on the base; study section {N}.',
        'zh': f'2026年10月20日：新增（EV5），由流上的终止所定的组间选择；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID)

p = RECORDS / f'{LV}.json'
d = json.loads(p.read_text())
d['related'].append({'id': RID, 'detail': {
    'en': 'The among-group part fixed by ending: groups whose own condition ran into joint excess leave no offspring.',
    'zh': '由终止所定的组间部分：自身条件遭遇共同过度的组不留后代。'}})
for r in d['references']:
    if r['path'] == CHAPTER:
        r['sha256'] = sha(CHAPTER)
d['history'].append({
    'en': f'20 October 2026, EV5: the base reading of groups, by ending, is stated in Becoming.GroupEnding (record {RID}, '
          f'study section {N}). The claim is unchanged.',
    'zh': f'2026年10月20日，EV5：组在流上的读法（经由终止）陈述于 Becoming.GroupEnding（记录 {RID}，研究第 {N} 节）。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
