#!/usr/bin/env python3
"""I4b-3: write the schema-2 record what-a-finite-history-refutes (run from the repository root at landing).

usage: python3 -B make_record_horizon.py SECTION

Run after the core receipt holding the I4b-3 edits of Becoming.Horizon exists and the periphery checker
check_prefix_safety_correspondence.py has passed against it. It binds Horizon.lean to the retained core receipt,
PrefixSafetyCorrespondence.lean to the retained copy of the instance receipt, and PrefixSafety.lean to the completion
package receipt, after checking that each passed for the current bytes. The declarations listed in the laws are
checked against the new section of Horizon.lean and the instance module, and the statement, title, validation scope
and next delta against the research check's hard length caps.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/'
HORIZON = BASE + 'lean/becoming/Becoming/Horizon.lean'
FORMAL = BASE + 'mathematical-abstraction/completion/formal/'
INSTANCE = FORMAL + 'PrefixSafetyCorrespondence.lean'
PREFIX = FORMAL + 'PrefixSafety.lean'
PACKAGE = FORMAL + 'verification.json'
CORE_POINTER = BASE + 'lean/becoming/becoming-verification.json'
INSTANCE_POINTER = FORMAL + 'prefix-safety-correspondence-verification.json'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-16-i4-decisions.md',
           'sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md']
REVIEWED = '2026-10-16T00:00:00+00:00'
SECTION = int(sys.argv[1])
# Horizon's declarations before I4b-3; they stay with becoming-finite-horizon and no-finite-part-bears-taking.
EARLIER = {'Becoming.Run.cons', 'Becoming.Run.AgreeUpTo', 'Becoming.Renewable.prefix_does_not_decide',
           'Becoming.Renewable.finite_reading_includes_consumption', 'Becoming.Renewable.whole_run_includes_overdraw',
           'Becoming.Renewable.amount_reading', 'Becoming.Renewable.cycle_reading_not_finite', 'Becoming.Feedback.law',
           'Becoming.Feedback.stopping', 'Becoming.Feedback.continuing', 'Becoming.Feedback.step_two',
           'Becoming.Feedback.step_one', 'Becoming.Feedback.descending', 'Becoming.Feedback.at_horizon',
           'Becoming.Feedback.after_horizon', 'Becoming.Feedback.supported', 'Becoming.Feedback.prefix_does_not_decide'}
# The research check's hard caps (tools/research/style.py): (en, zh).
CAPS = {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260), 'next_delta': (400, 180)}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pair(zh, en):
    return {'zh': zh, 'en': en}


def declared(path):
    """The fully qualified declarations of a module, read from its namespaces."""
    names, spaces = [], []
    for line in (ROOT / path).read_text().splitlines():
        m = re.match(r'^namespace (\S+)', line)
        if m:
            spaces.append(m.group(1))
            continue
        m = re.match(r'^end (\S+)', line)
        if m and spaces and spaces[-1] == m.group(1):
            spaces.pop()
            continue
        m = re.match(r'^(?:theorem|def|abbrev|structure|inductive|instance)\s+(\S+)', line)
        if m:
            names.append('.'.join(spaces + [m.group(1)]))
    return names


def law(zh, en, names):
    return {'zh': zh, 'en': en, 'declarations': names}


def h(*names):
    return ['Becoming.' + n for n in names]


def i(*names):
    return ['Becoming.PrefixSafetyCorrespondence.' + n for n in names]


LAWS = [
    law('两个运行到一界一致，是自反、对称、传递的，界缩小仍一致。读法可否证：其外每个运行有一界，界内与它一致的运行都在读法之外；'
        '可证实对偶。运行附着于读法：每一界内它都与读法内某运行一致。读法内的运行附着于它，附着随读法扩大，附着于附着者即附着。',
        'Agreement of two runs up to a horizon is reflexive, symmetric and transitive, and holds at every smaller horizon. '
        'A reading is refutable where every run outside it has a horizon within which every agreeing run is outside; '
        'verifiable dually. A run adheres to a reading where at every horizon it agrees with a run inside. Runs inside '
        'adhere, adherence grows with the reading, and adhering to the adherent is adhering.',
        h('Run.AgreeUpTo.refl', 'Run.AgreeUpTo.symm', 'Run.AgreeUpTo.trans', 'Run.AgreeUpTo.mono', 'Refutable',
          'Verifiable', 'Adheres', 'Adheres.of', 'Adheres.mono', 'Adheres.adheres')),
    law('可否证的读法在每个附着于它的运行上于双重否定下成立；可否证的超集在附着于子集的运行上亦然；读法稳定（双重否定下成立即成立）时，'
        '附着即成立。',
        'A refutable reading holds, up to double negation, at every run adhering to it, and a refutable superset so holds '
        'at every run adhering to the subset; where the reading is stable (holding up to double negation is holding), '
        'adhering is holding.',
        h('Refutable.not_not', 'Refutable.adheres_least', 'Refutable.adheres_iff')),
    law('运行附着于读法而在其外，读法不可否证；附着于补集而在其内，读法不可证实。在所有序列构成的过程中，把序列在一界后接成常值，'
        '界内一致不变，故复现与终于发生皆不可否证，从不发生不可证实。',
        'A run adhering to a reading while outside it shows the reading is not refutable, and one adhering to the '
        'complement while inside shows it is not verifiable. In the process whose runs are all sequences, splicing a '
        'constant after a horizon keeps agreement within it, so recurrence and eventual occurrence are not refutable '
        'and never occurring is not verifiable.',
        h('not_refutable_of_adheres', 'not_verifiable_of_adheres', 'Sequences.process', 'Sequences.run',
          'Sequences.agree_iff', 'Sequences.splice', 'Sequences.splice_agree', 'Sequences.splice_after',
          'Sequences.Recurs', 'Sequences.Eventually', 'Sequences.recurs_not_refutable',
          'Sequences.eventually_not_refutable', 'Sequences.never_not_verifiable')),
    law('由测试构成的读法：第 n 个测试是布尔值，由到第 n + 1 步的历史决定，读法即没有测试失败；它在每个附着于它的运行上成立。'
        '给定 Markov 原则（不全为假的布尔序列有真项），它可否证；布尔序列的每个有限前缀或全假或已见真项。',
        'A reading made of tests: the test at n is Boolean and fixed by the history through step n + 1, and the reading '
        'is that no test fails; it holds at every run adhering to it. Given Markov\'s principle (a Boolean sequence not '
        'all false has a true term) it is refutable; every finite prefix of a Boolean sequence is all false or shows a '
        'true term.',
        h('Passes', 'ByPrefixes', 'adheres_passes', 'Markov', 'refutable_passes', 'false_below_or_true')),
    law('对每个过程都要求时，由测试构成的读法可否证恰是 Markov 原则（见证：所有布尔序列的过程，第 n 个测试读第 n 项）。',
        'Asked of every process, refutability of every reading made of tests is exactly Markov\'s principle (witness: '
        'the process of all Boolean sequences, the test at n reading term n).',
        h('refutable_passes_iff_markov')),
    law('实例（外围，自有检查器）：PrefixSafety 的迹是所有序列过程的运行，同前缀即到界一致，有限可否证即可否证，前缀闭包即附着；'
        '其经典定理由核心律加经典推理给出：闭包内即成立、闭包最小、复现与终止事件不可有限否证、前缀测试性质可有限否证。',
        'Instance (periphery, own checker): PrefixSafety\'s traces are the runs of the process of all sequences, a shared '
        'prefix is agreement up to a horizon, finite refutability is refutability and the prefix closure is adherence; '
        'its classical theorems follow from the core laws with classical reasoning: holding within the closure, the '
        'least closure, recurrence and termination not finitely refutable, prefix tests refutable.',
        i('samePrefix_iff_agree', 'finiteRefutable_iff_refutable', 'prefixClosure_iff_adheres',
          'holds_of_prefixClosure_by_core', 'prefixClosure_least_by_core', 'recurrence_not_finiteRefutable_by_core',
          'terminationEvent_not_finiteRefutable_by_core', 'markov_classical', 'boundary_closed_by_core')),
]


def passed(pointer, module, source):
    # The top-level receipt is overwritten by the next run; bind its retained copy.
    top = json.loads((ROOT / pointer).read_text())
    if 'retained_run' in top:
        path = str(Path(pointer).parent / top['retained_run'] / 'verification.json')
    else:
        path = BASE + f'lean/becoming/becoming-checks/{top["utc"]}/verification.json'
    receipt = json.loads((ROOT / path).read_text())
    assert receipt['status'] == 'passed', path
    assert receipt['source_sha256'][module] == sha(source), ('receipt predates the source', path, source)
    return path


def package_passed():
    # The completion package's check.py writes its receipt only after every compile and audit passed.
    receipt = json.loads((ROOT / PACKAGE).read_text())
    assert receipt['fresh_build'] is True and receipt['custom_axioms'] == [] and receipt['proof_holes'] is False
    assert receipt['source_sha256']['PrefixSafety.lean'] == sha(PREFIX), 'package receipt predates PrefixSafety.lean'


def record():
    new = [n for n in declared(HORIZON) if n not in EARLIER]
    assert EARLIER <= set(declared(HORIZON)), EARLIER - set(declared(HORIZON))
    instance = declared(INSTANCE)
    listed = [d for l in LAWS for d in l['declarations']]
    assert sorted(listed) == sorted(new + instance), set(listed) ^ set(new + instance)
    core_receipt = passed(CORE_POINTER, 'Becoming.Horizon', HORIZON)
    instance_receipt = passed(INSTANCE_POINTER, 'PrefixSafetyCorrespondence', INSTANCE)
    assert passed(INSTANCE_POINTER, 'PrefixSafety', PREFIX) == instance_receipt
    package_passed()
    theorems = sum(1 for line in (ROOT / HORIZON).read_text().splitlines() if line.startswith('theorem '))
    bindings = [
        {'source': HORIZON, 'receipt': core_receipt, 'sha256_pointer': '/source_sha256/Becoming.Horizon',
         'success_pointer': '/status', 'success_value': 'passed'},
        {'source': INSTANCE, 'receipt': instance_receipt,
         'sha256_pointer': '/source_sha256/PrefixSafetyCorrespondence',
         'success_pointer': '/status', 'success_value': 'passed'},
        # The instance receipt also hashes PrefixSafety, matched to the package receipt, whose own format
        # (`modules` a count) the research check's receipt reader does not take; the package receipt stays a
        # reference (integrator, landing I4b-3).
        {'source': PREFIX, 'receipt': instance_receipt, 'sha256_pointer': '/source_sha256/PrefixSafety',
         'success_pointer': '/status', 'success_value': 'passed'},
    ]
    r = {
        'schema_version': 2,
        'id': 'what-a-finite-history-refutes',
        'title': pair('有限历史所否证者', 'What a finite history refutes'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F01',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '对每个过程：有限历史可否证的读法，在每个附着于它的运行上于双重否定下成立；其外有附着运行的读法既不可否证也不可证实；'
            '由前缀测试构成的读法皆可否证，恰是 Markov 原则。',
            'For every process: a reading that finite histories refute holds, up to double negation, at every run '
            'adhering to it; a reading with an adhering run outside it is neither refutable nor verifiable; and '
            'refutability of every reading made of prefix tests is exactly Markov\'s principle.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。过程、读法与运行任意；测试是布尔值（已定），由到其步的历史决定（ByPrefixes）；Markov 原则是 refutable_passes '
            '的假设，稳定是 Refutable.adheres_iff 的假设。',
            'No axiom. The process, reading and run are arbitrary; tests are Boolean (decided) and fixed by the history '
            'through their step (ByPrefixes); Markov\'s principle is a hypothesis of refutable_passes, and stability one '
            'of Refutable.adheres_iff.')],
        'does_not_show': [
            {**pair('哪些实际读法可否证：这取决于读它的过程；本律说可否证给出什么。',
                    'Which actual readings are refutable: that depends on the process they are read on; the law says '
                    'what refutability gives.'), 'kind': 'scope'},
            {**pair('不用 Markov 原则时，由测试构成的读法可否证：对每个过程要求它恰是 Markov 原则。',
                    'Refutability of readings made of tests without Markov\'s principle: asked of every process it is '
                    'exactly Markov\'s principle.'),
             'kind': 'non-implication', 'witness': 'Becoming.refutable_passes_iff_markov'},
            {**pair('可否证的读法在附着处径直成立：这需要读法稳定，外围实例以经典推理供给。',
                    'That a refutable reading holds outright at an adhering run: that needs the reading stable, which '
                    'the periphery instance supplies by classical reasoning.'), 'kind': 'scope'},
            {**pair('PrefixSafety 的迹是实际历史的模型：迹是自然数上的函数。',
                    'That PrefixSafety\'s traces model an actual history: traces are functions on the natural numbers.'),
             'kind': 'scope'},
        ],
        'counterexamples': [],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查：Becoming.Horizon 共 {theorems} 项定理，新增 {len(new)} 项声明公理报告为空。外围实例 '
            f'PrefixSafetyCorrespondence 由其检查器实查（Lean 4.30.0-rc2；五项对应公理报告为空，其余四项只用标准公理），'
            f'PrefixSafety 与完成包回执一致。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker: Becoming.Horizon has {theorems} theorems, and the '
            f'{len(new)} new declarations have empty axiom reports. The periphery instance PrefixSafetyCorrespondence is '
            f'checked by its own checker (Lean 4.30.0-rc2; five correspondences with empty axiom reports, the other four '
            f'with standard axioms only), PrefixSafety matching the completion package receipt. Author counterreview in '
            f'study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '独立审查；IdealWarrant 在偏序上的形式（一般数学线，暂留脊柱外）；其余最近的缺口（Lasting、Selection）。',
            'An independent review; IdealWarrant\'s order form on posets (the general mathematical line, outside the '
            'spine for now); the other closest gaps (Lasting, Selection).'),
        'correspondence': pair(
            'Ren 2026-10-16 对 I4 归类表选择“Closest gaps first”。归类表把 PrefixSafety 读作待接入的律：Becoming.Horizon 陈述了有限前缀'
            '不决定什么，未陈述有限历史否证什么。本结果对每个过程陈述它，PrefixSafety 的前缀拓扑是所有序列过程的实例，其经典定理成为核心律'
            '加双重否定与 Markov 原则。IdealWarrant 在偏序上推广它，属 Ren 暂留脊柱外的一般数学线。读法（AI 的，待 Ren）：有限记录能显示'
            '的，是运行在可否证读法之外；运行在其内只是未被否证；由测试否证，须在只知并非全部通过时找到失败的测试。',
            'Ren, 16 October 2026, chose “Closest gaps first” on the I4 classification table. The table read PrefixSafety '
            'as a join candidate: Becoming.Horizon stated what no finite prefix decides, not what a finite history '
            'refutes. This result states it for every process, with PrefixSafety\'s prefix topology as the instance of '
            'the process of all sequences; its classical theorems become the core laws with double negation and '
            'Markov\'s principle. IdealWarrant generalizes it to posets and belongs to the general mathematical line '
            'Ren left outside the spine for now. Readings (the AI\'s, pending Ren): what a finite record can show is '
            'that a run lies outside a refutable reading; that a run lies inside is only not refuted; and refuting by '
            'tests means finding a failed test where it is only known that not all pass.'),
        'canonical_source': HORIZON,
        'aliases': ['Becoming.Refutable', 'Becoming.Adheres', 'Becoming.refutable_passes_iff_markov',
                    'Becoming.Refutable.not_not', 'what a finite history refutes', '有限历史所否证者',
                    'finite refutability', '有限可否证', 'adherence', '附着'],
        'dependencies': [{
            'id': 'becoming-finite-horizon', 'relation': 'formal-reuse',
            'detail': pair('复用 Becoming.Horizon 的 Run.AgreeUpTo：有限视界说没有有限前缀决定整段分类，本结果说有限前缀能否证什么。',
                           'Reuses Becoming.Horizon\'s Run.AgreeUpTo: the finite horizon shows that no finite prefix '
                           'decides the whole-run classification; this result says what a finite prefix can refute.'),
            'interface': {'output': pair('到一界一致（Run.AgreeUpTo）。', 'Agreement up to a horizon (Run.AgreeUpTo).'),
                          'input': pair('读法的可否证与附着都以它定义。',
                                        'Refutability and adherence of a reading are defined by it.'),
                          'conditions': pair('无。', 'None.'), 'evidence': HORIZON}}],
        'related': [],
        'references': [
            {'path': HORIZON, 'role': 'proof', 'sha256': sha(HORIZON), 'declarations': new},
            {'path': INSTANCE, 'role': 'proof', 'sha256': sha(INSTANCE), 'declarations': instance},
            {'path': PREFIX, 'role': 'proof', 'sha256': sha(PREFIX),
             'declarations': ['CompletionWarrant.PrefixSafety.FiniteRefutable',
                              'CompletionWarrant.PrefixSafety.PrefixClosure',
                              'CompletionWarrant.PrefixSafety.finiteRefutable_iff_prefixClosure',
                              'CompletionWarrant.PrefixSafety.prefixClosure_least',
                              'CompletionWarrant.PrefixSafety.boundary_closed',
                              'CompletionWarrant.PrefixSafety.recurrence_not_finiteRefutable',
                              'CompletionWarrant.PrefixSafety.terminationEvent_not_finiteRefutable']},
            {'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt)},
            {'path': instance_receipt, 'role': 'receipt', 'sha256': sha(instance_receipt)},
            {'path': PACKAGE, 'role': 'receipt', 'sha256': sha(PACKAGE)},
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': bindings,
        'history': [pair(
            f'2026-10-16：新增，整合 I4b 第三项（Ren 选择“Closest gaps first”）；研究 §{SECTION}。',
            f'16 October 2026: added, integration I4b item 3 (Ren chose “Closest gaps first”); study section {SECTION}.')],
        'text_versions': [],
    }
    for key, (en, zh) in CAPS.items():
        assert len(r[key]['en']) <= en and len(r[key]['zh']) <= zh, (key, len(r[key]['en']), len(r[key]['zh']))
    return r


def main():
    r = record()
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), '+', len(r['references'][1]['declarations']),
          'declarations; statement', len(r['statement']['en']), '/', len(r['statement']['zh']), 'chars')


if __name__ == '__main__':
    main()
