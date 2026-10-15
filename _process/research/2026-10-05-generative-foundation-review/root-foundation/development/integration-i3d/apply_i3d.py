#!/usr/bin/env python3
"""Integration I3d landing kit: python3 -B apply_i3d.py SECTION

Run from the repository root after the core receipt holding the I3d edits of Becoming.Readout, Becoming.Copying,
Becoming.Stock, Becoming.Feedback and Becoming.Bridge exists and the four periphery checkers
(check_preparation_correspondence.py, check_judging_correspondence.py, check_renewing_correspondence.py,
check_substitution_correspondence.py) have passed against it. It
* checks that the retained core receipt and the retained copies of the four periphery receipts passed for the
  current bytes of every module the records bind;
* edits the six records: material-preparation-output, growth-constrained-fragmentation,
  risk-certificate-outcome-distinction, binding-preserving-substitution, renewing-consuming-formation and
  alignment-direction-g0-j (core, bridge and instance references with their declarations, bindings of each to its
  retained receipt, aliases, dependencies and history; claims, statements and validation scope are left as they
  are, the evidence going in the history entry as in I3a to I3c);
* measures with SPINE-INTEGRATION.py and inserts study section SECTION (s134_zh.md before the English
  summary, s134_en.md at the end), filling receipts and measure.
Then run `make research-render` and `make research-check`.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
KIT = Path(__file__).resolve().parent
STUDY_DIR = KIT.parents[1]
STUDY = STUDY_DIR / 'BECOMING-RENEWAL-READING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
B = LEAN + 'becoming/Becoming/'
CORE_RECEIPT = LEAN + 'becoming/becoming-verification.json'
UE = LEAN + 'universal-ethics/'
GC = UE + 'generative-capacity/'
DP = LEAN + 'deeper/'


def instance(folder, target, stem):
    return (folder + target + '.lean', folder + stem + '-verification.json', folder + 'check_' + stem.replace('-', '_') + '.py',
            target, folder + stem + '-checks/')


INSTANCES = {
    'preparation': instance(UE, 'PreparationCorrespondence', 'preparation-correspondence'),
    'judging': instance(DP, 'JudgingCorrespondence', 'judging-correspondence'),
    'renewing': instance(GC, 'RenewingCorrespondence', 'renewing-correspondence'),
    'substitution': instance(DP, 'SubstitutionCorrespondence', 'substitution-correspondence'),
}
# The core and bridge modules the records bind to the retained core receipt.
CORE_MODULES = {'Readout', 'Copying', 'Stock', 'Feedback', 'Bridge'}
I3 = '2026-10-15，整合 I3d（Ren：“a lot proofs are probably not integrated”）：'
I3_EN = '15 October 2026, integration I3d (Ren: “a lot proofs are probably not integrated”): '
RUN = {}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def declared(path, full):
    """Every named declaration occurs in the file as a definition or theorem."""
    text = (ROOT / path).read_text()
    for name in full:
        short = name.split('.')[-1]
        assert re.search(r'^\s*(?:theorem|def|inductive|structure|abbrev)\s+(?:\S+\.)?' + re.escape(short) + r'\b',
                         text, re.M), (path, name)
    return full


def passed_for(receipt, pointer_module, source):
    r = json.loads((ROOT / receipt).read_text())
    assert r['status'] == 'passed', receipt
    assert r['source_sha256'][pointer_module] == sha(source), ('receipt predates the source', receipt, source)
    return r


def receipts():
    """The retained copies of the landed core receipt and of the three periphery receipts, each passed for the
    current bytes of what the records bind."""
    core = json.loads((ROOT / CORE_RECEIPT).read_text())
    RUN['core'] = LEAN + 'becoming/becoming-checks/' + core['utc'] + '/verification.json'
    for module in CORE_MODULES:
        passed_for(RUN['core'], 'Becoming.' + module, B + module + '.lean')
    out = {'core': core['utc']}
    for key, (source, receipt, _, target, folder) in INSTANCES.items():
        top = passed_for(receipt, target, source)
        RUN[key] = folder + top['utc'] + '/verification.json'
        assert sha(RUN[key]) == sha(receipt), ('retained copy differs from the receipt', RUN[key])
        out[key] = top['utc']
    return out


def ref(path, role, decls=()):
    return {'path': path, 'role': role, 'sha256': sha(path), 'declarations': declared(path, list(decls)) if decls else []}


def core_refs(modules):
    """Core module sources with their declarations, the retained core receipt, and a binding of each."""
    refs = [ref(B + module + '.lean', 'proof', decls) for module, decls in modules]
    bindings = [{'source': B + module + '.lean', 'receipt': RUN['core'], 'sha256_pointer': '/source_sha256/Becoming.' + module,
                 'success_pointer': '/status', 'success_value': 'passed'} for module, _ in modules]
    return refs + [ref(RUN['core'], 'receipt')], bindings


def instance_refs(key, decls):
    source, _, checker, target, _ = INSTANCES[key]
    refs = [ref(source, 'proof', decls), ref(RUN[key], 'receipt'), ref(checker, 'provenance')]
    return refs, [{'source': source, 'receipt': RUN[key], 'sha256_pointer': '/source_sha256/' + target,
                   'success_pointer': '/status', 'success_value': 'passed'}]


def joined(*parts):
    refs, bindings = [], []
    for r, b in parts:
        refs += r
        bindings += b
    return refs, bindings


R = 'Becoming.Readout.'
P = 'Becoming.PreparationCorrespondence.'
J = 'Becoming.JudgingCorrespondence.'
N = 'Becoming.RenewingCorrespondence.'
U = 'Becoming.SubstitutionCorrespondence.'
K = 'Becoming.Stock.'


def evidence(utc, key, zh_axioms, en_axioms):
    return (f'外围实例模块由其检查器以 Lean 4.30.0-rc2 与 Mathlib 实查（回执 {utc[key]}），{zh_axioms}；'
            f'所实例化的核心律由核心运行审计（回执 {utc["core"]}，公理报告为空）。',
            f'The periphery instance module is checked by its own checker with Lean 4.30.0-rc2 and Mathlib (receipt '
            f'{utc[key]}), {en_axioms}; the core laws it instantiates are audited by the core run (receipt {utc["core"]}, '
            'empty axiom reports).')


def changes(utc):
    prep_ax = ('只用标准公理：unit、use_unit 与 adjacent 等不提及外围构造的声明公理报告为空，置换的对应用库的 Classical.choice',
               'standard axioms only: unit, use_unit, adjacent and the other declarations that mention no periphery '
               'construction have empty axiom reports, and the permutation correspondence uses the library’s '
               'Classical.choice')
    return {
        'risk-certificate-outcome-distinction': {
            'parts': joined(
                core_refs([('Readout', [R + n for n in ['LumpedOn', 'Judges', 'lumpedOn_of_judges', 'firstJudge',
                                                        'firstJudge_judges', 'judges_iff_lumpedOn', 'no_judge_of_merged']])]),
                instance_refs('judging', [J + n for n in ['realizations', 'endpoint', 'certificate', 'mem_realizations',
                                                          'judges_iff', 'endpoint_judge_iff',
                                                          'no_endpoint_only_prior_certificate_by_core']])),
            'aliases': [R + 'judges_iff_lumpedOn', R + 'no_judge_of_merged'],
            'evidence': evidence(utc, 'judging', '只用标准公理（propext、Quot.sound），realizations 的公理报告为空',
                                 'standard axioms only (propext, Quot.sound), realizations with an empty report'),
            'zh': I3 + '在脊柱上陈述（Becoming.Readout 的列出之族的判断，新增，不加前提）。只读约化值的判者对列出之族的每个成员给出观测，恰当观测在约化所合并的成员间一致（judges_iff_lumpedOn）；判者以每个约化值的第一个列出成员作答（firstJudge），不用选择；故约化合并两个观测所分开的成员时没有这样的判者（no_judge_of_merged）。外围实例 JudgingCorrespondence：每律与其每个模式是容许的实现，所列诸律的实现是一个列出的族，所到终点是其约化，律是否以三分之一为路线 0 之风险的界是观测；外围的判者陈述即核心的 Judges（judges_iff），故只看终点的判者分类证书恰当到达同一终点的实现带同一证书（endpoint_judge_iff）；均匀律与偏倚律的模式 1 到达同一终点而界一成立一不成立，故 no_endpoint_only_prior_certificate 由 no_judge_of_merged 给出（no_endpoint_only_prior_certificate_by_core）。所给的事件律、等权与三分之一界保持原范围。',
            'en': I3_EN + 'stated on the spine (the new law of Becoming.Readout for judging a listed family, no premise). A judge reading only the reduced value gives the observable at every member of a listed family exactly where the observable goes alike across the members the reduction merges (judges_iff_lumpedOn); the judge answers with the first listed member of each reduced value (firstJudge), so no choice is used, and no judge exists where the reduction merges two members the observable tells apart (no_judge_of_merged). Periphery instance JudgingCorrespondence: each law with each of its modes is an admitted realization, the realizations of the listed laws are a listed family, the endpoint reached is its reduction and whether the law bounds the risk of route 0 by one third is the observable; the periphery’s judge statement is the core’s Judges (judges_iff), so a judge of the endpoint classifies the certificate exactly where realizations reaching one endpoint carry one certificate (endpoint_judge_iff), and since mode 1 of the uniform and of the biased law reach one endpoint while the bound holds of the first only, no_endpoint_only_prior_certificate follows from no_judge_of_merged (no_endpoint_only_prior_certificate_by_core). The supplied event laws, equal weights and the one-third bound keep their scope.',
        },
        'growth-constrained-fragmentation': {
            'parts': joined(
                core_refs([('Feedback', ['Becoming.ClosedUnder', 'Becoming.WithinClosure', 'Becoming.closure_iff_certified',
                                         'Becoming.not_within_of_closed'])]),
                instance_refs('preparation', [P + n for n in ['adjacent', 'connected_of_adjacent', 'connected_iff_within',
                                                              'component_is_closure', 'certificate_exact_split_by_core',
                                                              'cut_separates', 'returns_differ',
                                                              'no_parent_summary_predictor_by_core']])),
            'aliases': ['Becoming.closure_iff_certified', 'Becoming.not_within_of_closed'],
            'dependencies': [{'id': 'risk-certificate-outcome-distinction', 'relation': 'formal-reuse', 'detail': {
                'zh': '复用 Becoming.Readout.no_judge_of_merged：组成相同的两个生长图切割回报不同，故亲代摘要的任何函数都不同时给出二者（PreparationCorrespondence.no_parent_summary_predictor_by_core）。',
                'en': 'Reuses Becoming.Readout.no_judge_of_merged: the two grown graphs have the same parent summary and different mean cut returns, so no function of the summary gives both (PreparationCorrespondence.no_parent_summary_predictor_by_core).'}}],
            'evidence': evidence(utc, 'preparation', *prep_ax),
            'zh': I3 + '在脊柱上陈述（Becoming.Feedback 的闭包证书，新增，不加前提）。一个区域恰是一个形成在关系下的闭包，当且仅当它含该形成、对关系封闭且在闭包之内（closure_iff_certified），在有限情形可由有限计算核查；含一形成而不含另一形成的封闭区域分开二者的闭包（not_within_of_closed）。外围实例 PreparationCorrespondence：由键相连即在对称读取的键之下的闭包内（connected_iff_within）；含根且对每条余下之键封闭的分量即该闭包（component_is_closure），故 certificate_exact_split 由核心律给出（certificate_exact_split_by_core），证书确认的切割分开两端（cut_separates）；组成相同的两个生长图切割回报不同（returns_differ），由 Readout.no_judge_of_merged，亲代摘要的任何函数都不同时给出二者（no_parent_summary_predictor_by_core）。生长史、采样与局部生产律保持原范围。',
            'en': I3_EN + 'stated on the spine (the new closure certificate of Becoming.Feedback, no premise). A region is a formation’s closure under a relation exactly where it holds the formation, is closed under the relation and lies within the closure (closure_iff_certified), which a finite computation can check in the finite case; a closed region holding one formation and not another separates their closures (not_within_of_closed). Periphery instance PreparationCorrespondence: being connected by the bonds is lying within the closure under the bonds read symmetrically (connected_iff_within); a component holding its root and closed on every remaining bond is that closure (component_is_closure), so certificate_exact_split follows from the core law (certificate_exact_split_by_core), and a certified cut leaves its two ends apart (cut_separates); the two grown graphs of matched composition have different mean cut returns (returns_differ), so by Readout.no_judge_of_merged no function of the parent summary gives both (no_parent_summary_predictor_by_core). Growth histories, sampling and the local production law keep their scope.',
        },
        'material-preparation-output': {
            'parts': joined(
                core_refs([('Copying', ['Becoming.Copying.countOf_removeAll', 'Becoming.Copying.nil_iff_countOf_zero',
                                        'Becoming.Copying.empties_iff'])]),
                instance_refs('preparation', [P + n for n in ['unit', 'use_unit', 'countOf_eq_count', 'mem_iff_countOf_pos',
                                                              'erase_eq_remove', 'route_some_iff', 'preparation_empties_iff',
                                                              'preparation_leaves']])),
            'aliases': ['Becoming.Copying.empties_iff'],
            # recurrent-chain-assembly, on which inherited-structural-copying depends, depends on this record, so the
            # shared copying law enters as a related link, not a dependency.
            'related': [{'id': 'inherited-structural-copying', 'detail': {
                'zh': '同用 Becoming.Copying 的逐记号复制（steps、use、countOf）：准备即每次接合汲取一单位的复制（PreparationCorrespondence.route_some_iff），池用尽的条件即 Copying.empties_iff。',
                'en': 'Uses the same token-by-token copying of Becoming.Copying (steps, use, countOf): preparation is copying with a unit draw per attachment (PreparationCorrespondence.route_some_iff), and emptying the pool is Copying.empties_iff.'}}],
            'evidence': evidence(utc, 'preparation', *prep_ax),
            'zh': I3 + '在脊柱上陈述（Becoming.Copying 的池用尽之律，新增，不加前提）。自池逐记号复制一词，池最后为空恰当池中每个记号恰如词中所用、且空闲支持覆盖各次接合的汲取（empties_iff；countOf_removeAll：移去之后每个记号的计数即原计数减去词中的计数）。外围实例 PreparationCorrespondence：route 完成、池中余 rest、支持余 left，恰当以每次接合汲取一单位的复制如此（route_some_iff）；故准备完成且池用尽，恰当池是配方的排列且配方不长于支持，所余支持为支持减去配方长度（preparation_empties_iff、preparation_leaves），即本记录的论断。所给配方、局部生产律与存量保持原范围。',
            'en': I3_EN + 'stated on the spine (the new law of Becoming.Copying for emptying the pool, no premise). Copying a word token by token from a pool leaves the pool empty exactly where the pool holds each token exactly as often as the word uses it and the free support covers the draws of the attachments (empties_iff; countOf_removeAll: after removal each token’s count is its count less the word’s). Periphery instance PreparationCorrespondence: route completes with rest left in the pool and left support free exactly when copying with a unit draw per attachment does (route_some_iff); so preparation completes with an empty residual pool exactly when the pool is a permutation of the recipe and the recipe is no longer than the support, the support left being the support less the recipe’s length (preparation_empties_iff, preparation_leaves), which is this record’s claim. The supplied recipe, production law and stocks keep their scope.',
        },
        'renewing-consuming-formation': {
            'parts': joined(
                core_refs([('Stock', [K + n for n in ['FallsBy', 'trace_falls', 'falls_iff', 'trace_exhausts', 'zero_of_add_le',
                                                      'exhausted_within', 'draws_nothing_from_empty']])]),
                instance_refs('renewing', [N + n for n in ['beyond', 'formedOf', 'remaining_falls', 'forms_while_held', 'moves',
                                                           'path_trace', 'total_moves', 'beyond_current_bounded_by_core',
                                                           'beyond_current_ceases_by_core', 'shared_formation_ends_by_core']])),
            'aliases': [K + 'trace_falls', K + 'exhausted_within'],
            'evidence': evidence(utc, 'renewing', '只用标准公理（propext、Quot.sound），beyond、formedOf 与 moves 的公理报告为空',
                                 'standard axioms only (propext, Quot.sound), beyond, formedOf and moves with empty reports'),
            'zh': I3 + '在脊柱上陈述（Becoming.Stock 的所汲取而不补充的水平，新增，不加前提）。每步之后所存加所汲取不超过之前所存时（FallsBy），沿任何历程终存加汲取总和不超过初存（trace_falls，每步如此恰当每历程如此，falls_iff）；正水平上每步都有所汲取时，与初存一样长的历程止于零（exhausted_within），零处的步不汲取（draws_nothing_from_empty）。外围实例 RenewingCorrespondence：超出当前更新率的步是一个过程的步（beyond），每步之后所余之界（所持条件加三角形更新界，外围的 budget）至少减去所形成者（remaining_falls），为正处总有所形成（forms_while_held），两者都来自外围的 beyond_step；超出当前更新率之历程的前 n 步是其轨迹（path_trace），汲取即所形成的总和（total_moves）。故整个展开的形成以该界为限（beyond_current_bounded_by_core），自等于该界之时起不再形成（beyond_current_ceases_by_core），分给任何部分（含共享形成）的份额随之终止（shared_formation_ends_by_core）。无恢复的磨损律保持原范围。',
            'en': I3_EN + 'stated on the spine (the new laws of Becoming.Stock for a level drawn on and not replenished, no premise). Where what stands after each step plus what it draws is at most what stood before (FallsBy), what stands at the end of every course plus everything drawn along it is at most what stood at its start (trace_falls; each step so exactly when every course so, falls_iff); where moreover every step from a positive level draws something, every course as long as the starting level ends at nothing (exhausted_within), and a step from nothing draws nothing (draws_nothing_from_empty). Periphery instance RenewingCorrespondence: steps beyond the current renewal rate are the moves of one process (beyond); across each the remaining bound (held conditions plus the triangular renewal bound, the periphery’s budget) falls by at least what forms (remaining_falls), and something forms wherever it is positive (forms_while_held), both from the periphery’s beyond_step; the first n steps of a course beyond the current rate are its trace (path_trace), drawing in all what formed (total_moves). So the whole unfolding’s formation is within that bound (beyond_current_bounded_by_core), nothing forms from the time equal to it (beyond_current_ceases_by_core), and every share of it, shared formation included, ends with it (shared_formation_ends_by_core). The no-recovery wear law keeps its scope.',
        },
        'binding-preserving-substitution': {
            'parts': joined(
                core_refs([('Readout', [R + n for n in ['ThroughParts', 'ReadsDirectly', 'agree_iff_parts',
                                                        'supplied_agree_iff_parts']])]),
                instance_refs('substitution', [U + n for n in ['part', 'read', 'use', 'through', 'direct', 'supplied',
                                                               'supplies', 'all_terms_agree_iff_positions_by_core']])),
            'aliases': [R + 'agree_iff_parts', R + 'supplied_agree_iff_parts'],
            'evidence': evidence(utc, 'substitution', '只用 Quot.sound（函数外延，与外围的代入引理相同），part、read、use、direct 与 supplied 的公理报告为空',
                                 'Quot.sound only (function extensionality, as in the periphery’s substitution lemma), part, read, use, direct and supplied with empty reports'),
            'zh': I3 + '在脊柱上陈述（Becoming.Readout 的经由部分的读取，新增，不加前提）。一族读取只经部分读取（ThroughParts）、每部分都被某读取直接读出（ReadsDirectly）时，两构型在每个读取下一致恰当在每部分一致（agree_iff_parts）；故替换的每个读取都是自它供给之构型的读取时，替换在每个读取下与原物一致，恰当所供给的构型在每部分与原物一致（supplied_agree_iff_parts）。外围实例 SubstitutionCorrespondence：对一个语境的赋值是以位置为部分的构型，消费者以求值读它；求值只经位置读取（through，用函数外延），位置的直接使用读出该位置（direct）；外围的代入引理 extract_substitute 说替换后每个消费者的读取即它对生产者所供给之赋值的读取（supplies）。故全部消费者在代入前后求值相同，恰当每个替换项给出其原位置的根据（all_terms_agree_iff_positions_by_core）。核心给出判据；代入引理仍是外围对其语言的定理，语言与绑定的解释保持原范围。',
            'en': I3_EN + 'stated on the spine (the new law of Becoming.Readout for readings through parts, no premise). Where every reading of a family reads only through the parts (ThroughParts) and each part is read directly by some reading (ReadsDirectly), two configurations agree under every reading exactly where they agree at every part (agree_iff_parts); so where each reading of a replacement is the reading of the configuration it supplies, the replacement agrees with the original under every reading exactly where the supplied configuration agrees with it at every part (supplied_agree_iff_parts). Periphery instance SubstitutionCorrespondence: an assignment to a context is a configuration whose parts are its positions, and a consumer reads it by evaluation; evaluation reads only through the positions (through, with function extensionality) and the direct use of a position reads that position (direct); the periphery’s substitution lemma extract_substitute makes each consumer’s reading after replacement its reading of the assignment the producers supply (supplies). So every consumer evaluates alike before and after replacement exactly where each replacement term supplies the ground at its original position (all_terms_agree_iff_positions_by_core). The core supplies the criterion; the substitution lemma remains the periphery’s theorem about its language, and the language and the interpretation of binding keep their scope.',
        },
        'alignment-direction-g0-j': {
            'parts': core_refs([('Bridge', ['Becoming.BetterAt', 'Becoming.Judgment.frame', 'Becoming.Judgment.protecting',
                                            'Becoming.Judgment.gaining', 'Becoming.Judgment.better_iff_betterAt',
                                            'Becoming.Judgment.frontier_iff', 'Becoming.alignment_better_iff_betterAt',
                                            'Becoming.alignment_frontier_iff'])]),
            'aliases': ['Becoming.alignment_better_iff_betterAt', 'Becoming.alignment_frontier_iff'],
            'evidence': (f'桥接由核心运行编译与审计（回执 {utc["core"]}），新增声明的公理报告为空；AlignmentDirection 与 PracticalJudgment 作为继承模块随运行编译，其既有回执不变。',
                         f'The bridge is compiled and audited by the core run (receipt {utc["core"]}), the new declarations with empty axiom reports; AlignmentDirection and PracticalJudgment compile in the run as inherited modules, their earlier receipt unchanged.'),
            'zh': I3 + '在脊柱上陈述（桥接中的确切实例）。每个保护优先的比较 PracticalJudgment.Better 都是其选项框架上的 BetterAt：选项是无步之框架的配置，左边实现所保护的论断、右边实现所得，以前者为 basic、后者为 living（Judgment.frame、Judgment.better_iff_betterAt），前沿亦同（Judgment.frontier_iff）。故 AlignmentDirection 对计划的比较与合格计划的前沿就是脊柱上 BetterAt 的比较与前沿（alignment_better_iff_betterAt、alignment_frontier_iff），转移优于扩张与扩张被排除出前沿是脊柱上比较的陈述。论断、Ren 的话与 G0 的折叠不变：BetterAt 陈述 J1/J2，即核心之外的公开承诺，这里不用也不断言 G0。需求覆盖（Covered）在脊柱上没有确切的对应（Becoming.Wholes 的 Web.Covered 不以需求为指标），故 covered_transfer_with_old_model_stopped 与 promised_successor_without_delivery_fails 留在外围。',
            'en': I3_EN + 'stated on the spine (an exact instance in the bridge). Every protection-first comparison PracticalJudgment.Better is BetterAt on the frame of its options: the options are the configurations of a frame with no moves realizing the protected claims on the left and the gains on the right, the former read as basic and the latter as living (Judgment.frame, Judgment.better_iff_betterAt), with the same frontier (Judgment.frontier_iff). So AlignmentDirection’s comparison of plans and its frontier of eligible plans are the comparison and frontier of the spine’s BetterAt (alignment_better_iff_betterAt, alignment_frontier_iff), and transfer over expansion and the exclusion of expansion from the frontier are statements of the spine’s comparison. The claims, Ren’s words and the fold of G0 are unchanged: BetterAt states J1/J2, disclosed commitments outside the core, and G0 is neither used nor asserted here. Demand-indexed coverage (Covered) has no exact counterpart on the spine (Becoming.Wholes’ Web.Covered is not indexed by demand), so covered_transfer_with_old_model_stopped and promised_successor_without_delivery_fails stay in the periphery.',
        },
    }


def apply_records(utc):
    """Records keep their validation scope (schema-1 records may not grow it); the evidence of this integration goes
    in the history entry, as in I3a and I3b."""
    for rid, change in changes(utc).items():
        path = RECORDS / (rid + '.json')
        d = json.loads(path.read_text())
        have = {r['path'] for r in d['references']}
        refs, bindings = change['parts']
        for r in refs:
            if r['path'] in have:  # one reference per path, its declarations merged
                old = next(x for x in d['references'] if x['path'] == r['path'])
                assert old['sha256'] == r['sha256'], (rid, r['path'])
                old['declarations'] = old.get('declarations', []) + [n for n in r['declarations'] if n not in old.get('declarations', [])]
                continue
            d['references'].append(r)
            have.add(r['path'])
        for b in bindings:
            if b not in d['proof_bindings']:
                d['proof_bindings'].append(b)
        for alias in change['aliases']:
            assert alias not in d['aliases'], (rid, alias)
            d['aliases'].append(alias)
        for edge in change.get('dependencies', []):
            assert edge['id'] not in {e['id'] for e in d['dependencies']}, (rid, edge['id'])
            d['dependencies'].append(edge)
        for link in change.get('related', []):
            assert link['id'] not in {e['id'] for e in d.get('related', [])}, (rid, link['id'])
            d.setdefault('related', []).append(link)
        if 'counterexample' in change:
            d['counterexamples'].append(change['counterexample'])
        if 'laws' in change:
            d['laws'].extend(change['laws'])
        zh, en = change['evidence']
        d['history'].append({'zh': change['zh'] + zh, 'en': change['en'] + ' ' + en})
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        print(rid, len(refs), 'references,', len(change['aliases']), 'aliases')


def measure():
    out = subprocess.run([sys.executable, '-B', str(STUDY_DIR / 'SPINE-INTEGRATION.py')], capture_output=True,
                         text=True, check=True).stdout
    return json.loads(out)


def insert_study(section, utc, before, m):
    records, was = m['records'], before['records']
    stated, outside = records.get('stated on the spine', 0), records.get('outside the spine run', 0)
    stated0, outside0 = was.get('stated on the spine', 0), was.get('outside the spine run', 0)
    fill = {'{CORE}': utc['core'], '{PREP}': utc['preparation'], '{JUDG}': utc['judging'],
            '{RENEW}': utc['renewing'], '{SUBST}': utc['substitution'], '{STATED}': f'{stated0} → {stated}', '{OUTSIDE}': f'{outside0} → {outside}',
            '{NOLEAN}': str(records.get('no Lean proof', 0)),
            '{CITING}': f'{before["records_citing_a_spine_proof"]} → {m["records_citing_a_spine_proof"]}',
            '{STATED_SHORT}': f'from {stated0} to {stated}', '{OUTSIDE_SHORT}': f'from {outside0} to {outside}'}
    zh, en = (KIT / 's134_zh.md').read_text(), (KIT / 's134_en.md').read_text()
    for key, value in fill.items():
        zh, en = zh.replace(key, value), en.replace(key, value)
    zh = zh.replace('## 134.', f'## {section}.', 1)
    en = en.replace('section 134', f'section {section}', 1)
    assert not re.search(r'\{[A-Z_]+\}', zh + en), 'unfilled placeholder'
    text = STUDY.read_text()
    assert f'\n## {section}. ' not in text, 'section number taken'
    anchor = '\n## English summary\n'
    assert text.count(anchor) == 1
    text = text.replace(anchor, '\n' + zh.rstrip('\n') + '\n' + anchor)
    text = text.rstrip('\n') + '\n\n' + en.rstrip('\n') + '\n'
    STUDY.write_text(text)


def main():
    section = int(sys.argv[1])
    utc = receipts()
    before = measure()
    apply_records(utc)
    m = measure()
    print(json.dumps({k: m[k] for k in ('records', 'records_citing_a_spine_proof', 'records_outside_the_spine_run')},
                     ensure_ascii=False))
    insert_study(section, utc, before, m)


if __name__ == '__main__':
    main()
