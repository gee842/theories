#!/usr/bin/env python3
"""Write EV4's record and note it in the record it continues (selection-term-over-generations):
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.SelectionLevels (a short
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
MOD = 'SelectionLevels'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. Selection within groups and among them (EV4)'
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


RID = 'selection-within-and-among-groups'
S = 'SelectionLevels.'
laws = [
    ('A family listed group by group has as its totals, weighted total and number of members the sums of the groups\'; '
     'with k groups of m members each it has k times m members.',
     '逐组列出的族，其总量、加权总量与成员数是各组的之和；k 个组各有 m 个成员时，族有 k 乘 m 个成员。',
     [S + 'whole_total', S + 'whole_weighted', S + 'whole_length', S + 'total_eq_of_mem', S + 'whole_length_of_equal']),
    ('With no premise beyond groups of equal size: the whole\'s concordance, with k times the groups\' own discordance and '
     'the discordance among groups read by their totals, is the whole\'s discordance with k times the groups\' own '
     'concordance and the concordance among groups. Divided through, the whole\'s covariance of weight and amount is the '
     'mean of the groups\' covariances with the covariance of their means.',
     '除各组大小相等外不加前提：整体的一致度，加上 k 倍各组自身的不一致度与以组总量读的组间不一致度，等于整体的不一致度加上 k 倍各组自身的一致度与组间一致度。除尽后，整体的协方差等于各组协方差的均值加组均值的协方差。',
     [S + 'levels', S + 'lhs_shape', S + 'rhs_shape']),
    ('So the whole selects for the amount exactly where the two levels together do, and nothing exactly where they '
     'balance. Selected against within the groups, an amount is selected for in the whole only where selection among the '
     'groups goes for it; selected against among them, only where selection within goes for it.',
     '故整体恰在两层合起来选择某量时选择它，恰在两层相抵时不选择。在组内被逆向选择之量，只在组间选择偏向它时才在整体中被选择；在组间被逆向选择之量，只在组内选择偏向它时。',
     [S + 'rises_iff', S + 'none_iff', S + 'among_for_of_rises', S + 'within_for_of_rises']),
    ('Where every group is uniform in amount nothing is selected within them and the whole\'s selection is selection among '
     'groups alone; where the groups\' totals are alike nothing is selected among them and the whole\'s selection is k times '
     'selection within.',
     '每组在该量上均匀之处，组内无选择，整体的选择只是组间选择；各组总量相同之处，组间无选择，整体的选择是 k 倍组内选择。',
     [S + 'within_none_of_uniform', S + 'levels_of_uniform', S + 'among_none_of_alike', S + 'levels_of_alike']),
    ('Over listed generations with exact transmission, a generation listed as groups of equal size raises its mean amount '
     'across the step exactly where, read by offspring number, the two levels together select for the amount; selected '
     'against within the groups, its mean rises only where selection among them goes for it.',
     '在传递精确的列出世代中，列为等大小之组的一代，其平均量跨一步恰在以后代数读的两层合起来选择该量时上升；在组内被逆向选择时，其均值只在组间选择偏向它时上升。',
     [S + 'rises_exact_iff_levels', S + 'among_for_of_raises']),
    ('Witnesses: two groups of two, the amount one at a member holding back. It leaves fewer offspring than its groupmate, '
     'so selection within goes against it; where the other group leaves none, selection among groups goes for it and the '
     'whole selects for it; where the other group leaves three each, both levels go against it and so does the whole.',
     '见证：两个两人组，保留者处该量为一。它留下的后代少于同组者，故组内选择逆向于它；另一组无后代时，组间选择偏向它，整体选择它；另一组每人留下三个时，两层皆逆向于它，整体亦然。',
     [S + 'equal', S + 'AmongWins.among_wins', S + 'WithinWins.within_wins']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))

TERM_DEP = dep('selection-term-over-generations', 'formal-reuse',
               'Reuses Becoming.SelectionTerm\'s covariation (applied to the whole, to each group and to the groups read by '
               'their totals), its balance lemmas, uniform-amount laws, listed generations and exact transmission '
               '(Generations.raises_exact_iff).',
               '复用 Becoming.SelectionTerm 的协变（用于整体、各组与以总量读的组）、其平衡引理、均匀量之律、列出的世代与精确传递（Generations.raises_exact_iff）。',
               'The selection term proper of any finite family, and its course over generations.',
               '任意有限族的真正选择项，及其在世代中的进程。',
               'The selection term divided by level: within groups and among them.', '按层划分的选择项：组内与组间。',
               'Groups of equal size; exact transmission where named.', '各组大小相等；所列处传递精确。',
               src('SelectionTerm'))

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'Selection within groups and among them', 'zh': '组内选择与组间选择'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'For a family listed as groups of equal size, the selection term proper divides exactly into selection '
              'within the groups and selection among them; an amount selected against within every group is selected for '
              'in the whole only where selection among groups goes for it.',
        'zh': '对列为等大小之组的族，真正的选择项恰好分为组内选择与组间选择；在各组内被逆向选择之量，只在组间选择偏向它时才在整体中被选择。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. Any finite family listed as groups, natural-number weights and amounts; groups of equal size for '
              'the division and what follows from it. Over generations: discrete generations listed as offspring of the '
              'last, one generation listed as such groups, exact transmission where named.',
        'zh': '不加公理。任意列为组的有限族、自然数权重与量；划分及其推论需各组大小相等。世代：离散的世代，每一代列为上一代的后代，其中一代列为这样的组，所列处传递精确。'}],
    'does_not_show': [
        {'en': 'Groups of unequal size: there the division weights each group\'s own term by the whole\'s size over the '
               'group\'s, which is not stated.',
         'zh': '大小不等的组：此时划分以整体规模比组规模来加权各组自身的项，未陈述。', 'kind': 'scope'},
        {'en': 'What the groups are, why their members\' offspring numbers differ, or how groups form, persist or mix: '
               'which level wins is read off the counts, not explained. No base reading (groups as lineages within their '
               'own families) is given.',
         'zh': '组是什么、其成员的后代数为何不同、组如何形成、持续或混合：哪一层胜出是从计数读出的，不是解释。未给出流上的读法（组为各自族内的世系）。',
         'kind': 'scope'},
        {'en': 'Transmission that is not exact: the generational form is stated with exact transmission only.',
         'zh': '不精确的传递：世代形式只在传递精确时陈述。', 'kind': 'scope'},
        {'en': 'That selection among groups ought to win, or that holding back is better: the division is an identity of '
               'counts; ranking goes through the comparison C, not through it.',
         'zh': '组间选择应当胜出，或保留更好：划分是计数的恒等式；排序经由比较 C，不经由它。', 'kind': 'non-implication'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Selection within the groups against an amount does not decide the whole: with the same groups and the same '
              'within-group counts the whole selects for it (AmongWins.among_wins) or against it (WithinWins.within_wins), '
              'according to selection among the groups.',
        'zh': '组内对某量的逆向选择不决定整体：同样的组、同样的组内计数，整体选择它（AmongWins.among_wins）或逆向于它（WithinWins.within_wins），取决于组间选择。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Built and reviewed in one session, with no separate reviewer; author review in study section {N}; not '
              'independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'Groups of unequal size; groups read on the base as lineages within their own families, with what each draws '
              'from a shared condition (DrawnBeyond); transmission that is not exact; an independent review.',
        'zh': '大小不等的组；在流上把组读作各自族内的世系，连同各自从共同条件所取之量（DrawnBeyond）；不精确的传递；独立审查。'},
    'correspondence': {
        'en': 'The multilevel form of Price\'s equation (Price 1972; Hamilton 1975), the law of total covariance: with '
              'equal group sizes, Cov(w, z) = E_g[Cov_g(w, z)] + Cov_g(E[w], E[z]). levels is this with denominators '
              'cleared over ordered pairs (the whole\'s pairs number (km)^2, a group\'s m^2, the groups\' k^2). Readings '
              '(the AI\'s): where selection within each group goes against what keeps a shared condition, the whole keeps '
              'it only through selection among groups.',
        'zh': 'Price 方程的多层形式（Price 1972；Hamilton 1975），即总协方差律：组大小相等时，Cov(w, z) = E_g[Cov_g(w, z)] + Cov_g(E[w], E[z])。levels 是它在有序对上消去分母的形式（整体的对数为 (km)^2，一组为 m^2，组间为 k^2）。读法（AI 的）：在每组内的选择逆向于维持共同条件之物处，整体只经由组间选择维持它。'},
    'canonical_source': src(MOD),
    'aliases': ['selection within groups and among them', '组内选择与组间选择', 'multilevel Price equation',
                'multilevel selection', 'law of total covariance', 'Becoming.SelectionLevels.levels',
                'Becoming.SelectionLevels.among_for_of_rises', 'Becoming.SelectionLevels.rises_exact_iff_levels'],
    'dependencies': [TERM_DEP],
    'related': [
        {'id': 'selection-term-over-generations', 'detail': {
            'en': 'The selection term proper divided by level.', 'zh': '按层划分的真正选择项。'}},
        {'id': 'evolution-on-descent', 'detail': {
            'en': 'Selection over generations read where a generation is listed as groups.',
            'zh': '一代列为组时所读的世代选择。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('SelectionTerm'), 'role': 'proof', 'sha256': sha(src('SelectionTerm'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (EV4), the multilevel form of the selection term; study section {N}.',
        'zh': f'2026年10月20日：新增（EV4），选择项的多层形式；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID)

# The record it continues.
p = RECORDS / 'selection-term-over-generations.json'
d = json.loads(p.read_text())
d['related'].append({'id': RID, 'detail': {
    'en': 'The selection term divided into selection within groups and among them, for groups of equal size.',
    'zh': '对等大小之组，选择项分为组内选择与组间选择。'}})
for r in d['references']:
    if r['path'] == CHAPTER:
        r['sha256'] = sha(CHAPTER)
d['history'].append({
    'en': f'20 October 2026, EV4: the multilevel form of the selection term is stated in Becoming.SelectionLevels (record '
          f'{RID}, study section {N}). The claim is unchanged.',
    'zh': f'2026年10月20日，EV4：选择项的多层形式陈述于 Becoming.SelectionLevels（记录 {RID}，研究第 {N} 节）。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
