#!/usr/bin/env python3
"""I4b-1: write the schema-2 record every-origin-passes-the-gate (run from the repository root at landing).

usage: python3 -B make_record.py SECTION

Run after the core receipt holding the I4b edits of Becoming.Gated exists and the periphery checker
check_living_organization_correspondence.py has passed against it. It binds Gated.lean to the retained core receipt
(becoming-checks/<utc>/verification.json, the one becoming-verification.json names) and
LivingOrganizationCorrespondence.lean to the retained copy of the instance receipt, after checking that both passed for
the current bytes. The declarations listed in the laws are checked against the new section of Gated.lean and the
instance module.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
GATED = BASE + 'becoming/Becoming/Gated.lean'
INSTANCE = BASE + 'universal-ethics/LivingOrganizationCorrespondence.lean'
LIVING = BASE + 'universal-ethics/LivingOrganization.lean'
CORE_POINTER = BASE + 'becoming/becoming-verification.json'
INSTANCE_POINTER = BASE + 'universal-ethics/living-organization-correspondence-verification.json'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-16-i4-decisions.md',
           'sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md']
REVIEWED = '2026-10-16T00:00:00+00:00'
SECTION = int(sys.argv[1])
# The declarations the I4b section adds to Becoming.Gated; the earlier four theorems and KeptBy stay with
# organizational-rule-inheritance.
EARLIER = {'Becoming.Gated.KeptBy', 'Becoming.Gated.kept_along', 'Becoming.Gated.kept_along_iff',
           'Becoming.Gated.change_passes_gate', 'Becoming.Gated.change_located'}


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


def g(*names):
    return ['Becoming.Gated.' + n for n in names]


def i(*names):
    return ['Becoming.LivingOrganizationCorrespondence.' + n for n in names]


LAWS = [
    law('门是动作上的已定标记。非门控步保持性质 p，是说步前成立则步后成立；反映 p，是说步后成立则步前成立。保持一个量恰是保持它的'
        '每个值，也恰是反映它的每个值；性质沿每段非门控进程被保持（被反映），恰当每个非门控步保持（反映）它。',
        'A gate is a decided mark on moves. The ungated steps preserve a property p where it holding before a step gives '
        'it after, and reflect p where it holding after gives it before. Keeping a quantity is preserving every value of '
        'it, and equally reflecting every value; a property is preserved (reflected) along every ungated course exactly '
        'when every ungated step preserves (reflects) it.',
        g('PreservedBy', 'ReflectedBy', 'keptBy_iff_preserved', 'keptBy_iff_reflected', 'preserved_along',
          'preserved_along_iff', 'reflected_along')),
    law('离开经过门：非门控步保持 p 时，从 p 成立处到 p 不成立处的进程含门控动作；保持量的旧律是其 p 为“q 等于起点之值”的情形。',
        'Leaving passes the gate: where the ungated steps preserve p, a course from where p holds to where it fails '
        'contains a gated move; the earlier law for a kept quantity is its case p := (q equals its starting value).',
        g('leaving_passes_gate')),
    law('每个起源都经过门：非门控步反映 p 时，终于 p 成立处的进程或始于 p 成立处，或分为前段、一个之后 p 成立的门控步与其余。'
        '不判定 p：门本身已定。',
        'Every origin passes the gate: where the ungated steps reflect p, a course ending where p holds started where '
        'it held, or splits into a prefix, a gated step after which p holds, and the rest. Nothing about p is decided: '
        'the gate itself is.',
        g('origin')),
    law('门是命题而非已定时，起源之律在每个门都成立或不成立处成立；对每个过程都要求时，它恰是双重否定消去（见证：一步从假到真，'
        '在真处 p 成立，门为 Q）。',
        'With the gate a proposition rather than decided, the origin law holds wherever every gate holds or fails; asked '
        'of every process it is exactly double-negation elimination (witness: one move from false to true, p holding at '
        'true, the gate Q).',
        g('origin_of_decides', 'origin_of_propositions_iff')),
    law('实例（外围，自有检查器）：在 LivingOrganization 中，以进入池的配方为门，其他步反映池的出现，所以 trace_pool_origin 由 '
        'origin 给出，并多给出进入步之后池即出现；凡准入配方都闭合时，没有门，reflected_along 使空池保持为空。',
        'Instance (periphery, own checker): in LivingOrganization, with the recipes entering the pool as the gate, every '
        'other step reflects pool presence, so trace_pool_origin follows from origin, which adds that the pool is present '
        'right after the entry step; where every admitted recipe is closed there is no gate, and reflected_along keeps an '
        'empty pool empty.',
        i('entryDecidable', 'entryGate', 'presence_reflected', 'trace_pool_origin_by_core', 'entry_then_present',
          'empty_pool_preserved_by_core')),
]


def passed(pointer, module, source):
    # The top-level receipt is overwritten by the next run; bind its retained copy.
    top = json.loads((ROOT / pointer).read_text())
    if 'retained_run' in top:
        path = str(Path(pointer).parent / top['retained_run'] / 'verification.json')
    else:
        path = BASE + f'becoming/becoming-checks/{top["utc"]}/verification.json'
    receipt = json.loads((ROOT / path).read_text())
    assert receipt['status'] == 'passed', path
    assert receipt['source_sha256'][module] == sha(source), ('receipt predates the source', path, source)
    return path


def record():
    new = [n for n in declared(GATED) if n not in EARLIER]
    instance = declared(INSTANCE)
    listed = [d for l in LAWS for d in l['declarations']]
    assert sorted(listed) == sorted(new + instance), set(listed) ^ set(new + instance)
    core_receipt = passed(CORE_POINTER, 'Becoming.Gated', GATED)
    instance_receipt = passed(INSTANCE_POINTER, 'LivingOrganizationCorrespondence', INSTANCE)
    theorems = sum(1 for line in (ROOT / GATED).read_text().splitlines() if line.startswith('theorem '))
    bindings = [
        {'source': GATED, 'receipt': core_receipt, 'sha256_pointer': '/source_sha256/Becoming.Gated',
         'success_pointer': '/status', 'success_value': 'passed'},
        {'source': INSTANCE, 'receipt': instance_receipt,
         'sha256_pointer': '/source_sha256/LivingOrganizationCorrespondence',
         'success_pointer': '/status', 'success_value': 'passed'},
    ]
    return {
        'schema_version': 2,
        'id': 'every-origin-passes-the-gate',
        'title': pair('每个起源都经过门', 'Every origin passes the gate'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F10',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '对每个过程与动作上的已定之门：非门控步反映的性质，终于其成立处的进程或始于其成立处，或经一个之后它成立的门控步，不判定该性质；'
            '离开非门控步保持的性质经过门。门是命题时这一律恰是双重否定消去。',
            'For every process and decided gate: where ungated steps reflect a property, a course ending where it holds '
            'started there or passes a gated step after which it holds, the property undecided; leaving a preserved '
            'property passes the gate. With a propositional gate this is double-negation elimination.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。门是动作到布尔值的映射（已定）；性质 p 是任意命题，不判定。以命题为门的形式把每个门成立或不成立写作假设。',
            'No axiom. The gate maps moves to Booleans (decided); the property p is any proposition and is not decided. '
            "The form with a propositional gate takes each gate's holding or failing as a hypothesis.")],
        'does_not_show': [
            {**pair('门控动作改变任何东西：门只定位改变或起源能从哪里进入。',
                    'That a gated move changes anything: the gate only locates where change or origin can enter.'),
             'kind': 'scope'},
            {**pair('不判定 p 时，起源之律给出第一个使 p 成立的门控步（之前 p 不成立）：它给出一个之后 p 成立的门控步。',
                    'Without deciding p, the first gated step at which p comes to hold (failing before it): the law gives a '
                    'gated step after which p holds.'), 'kind': 'scope'},
            {**pair('以命题为门而不判定时的起源之律：对每个过程要求它恰是双重否定消去。',
                    'The origin law with a propositional gate and no decision: asked of every process it is exactly '
                    'double-negation elimination.'),
             'kind': 'non-implication', 'witness': 'Becoming.Gated.origin_of_propositions_iff'},
            {**pair('LivingOrganization 的配方、准入反应与所选的池对应任何实际化学：闭合是所准入配方的已查性质，不是一切化学的定律。',
                    "That LivingOrganization's recipes, admitted reactions and selected pool correspond to any actual "
                    'chemistry: closure is a checked property of the admitted recipes, not a law of all chemistry.'),
             'kind': 'scope'},
        ],
        'counterexamples': [],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查：Becoming.Gated 共 {theorems} 项定理，新增 {len(new)} 项声明公理报告为空；'
            f'外围实例 LivingOrganizationCorrespondence 由其检查器实查（标准公理）。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker: Becoming.Gated has {theorems} theorems, and the '
            f'{len(new)} new declarations have empty axiom reports; the periphery instance LivingOrganizationCorrespondence '
            f'is checked by its own checker (standard axioms). Author counterreview in study section {SECTION}; not '
            f'independently reviewed.'),
        'next_delta': pair(
            '独立审查；判定 p 时的第一个起源步；其余最近的缺口（Horizon、Lasting、Selection，I4b）。',
            'An independent review; the first origin step where p is decided; the other closest gaps (Horizon, Lasting, '
            'Selection, I4b).'),
        'correspondence': pair(
            'Ren 2026-10-16 对 I4 归类表选择“Closest gaps first”。归类表把 LivingOrganization 读作待接入的律：Becoming.Gated 要求未经门的步'
            '双向保持，单向的轨迹律未陈述。本结果陈述它，并把 Gated 的旧律作为其情形。读法（AI 的，待 Ren）：门定位起源能从哪里进入；'
            '反映即“后有则前有”，一个组织的池或早已在，或经一次进入而在。',
            'Ren, 16 October 2026, chose “Closest gaps first” on the I4 classification table. The table read LivingOrganization '
            'as a join candidate: Becoming.Gated asked for keeping in both directions, and the one-directional trace law was '
            'unstated. This result states it, with the earlier Gated law as its case. Readings (the AI\'s, pending Ren): the '
            'gate locates where an origin can enter; reflecting is "present after only if present before", and an '
            "organization's pool was either there already or came in through an entry."),
        'canonical_source': GATED,
        'aliases': ['Becoming.Gated.origin', 'Becoming.Gated.leaving_passes_gate',
                    'Becoming.Gated.origin_of_propositions_iff', 'every origin passes the gate', '每个起源都经过门',
                    'leaving passes the gate', '离开经过门'],
        'dependencies': [{
            'id': 'organizational-rule-inheritance', 'relation': 'formal-reuse',
            'detail': pair('复用 Becoming.Gated 的 KeptBy：保持一个量恰是保持（反映）它的每个值，change_passes_gate 是 leaving_passes_gate '
                           '的情形。',
                           'Reuses Becoming.Gated.KeptBy: keeping a quantity is preserving (reflecting) every value of it, '
                           'and change_passes_gate is a case of leaving_passes_gate.'),
            'interface': {'output': pair('非门控步保持的量（KeptBy）；改变经过门。',
                                         'A quantity the ungated steps keep (KeptBy); change passes the gate.'),
                          'input': pair('保持读作保持或反映每个值。', 'Keeping read as preserving or reflecting every value.'),
                          'conditions': pair('无。', 'None.'), 'evidence': GATED}}],
        'related': [],
        'references': [
            {'path': GATED, 'role': 'proof', 'sha256': sha(GATED), 'declarations': new},
            {'path': INSTANCE, 'role': 'proof', 'sha256': sha(INSTANCE), 'declarations': instance},
            {'path': LIVING, 'role': 'integration', 'sha256': sha(LIVING),
             'declarations': ['Generative.LivingOrganization.trace_pool_origin',
                              'Generative.LivingOrganization.empty_pool_preserved',
                              'Generative.LivingOrganization.step_pool_origin',
                              'Generative.LivingOrganization.closed_step_preserves_absence']},
            {'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt)},
            {'path': instance_receipt, 'role': 'receipt', 'sha256': sha(instance_receipt)},
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': bindings,
        'history': [pair(
            f'2026-10-16：新增，整合 I4b 第一项（Ren 选择“Closest gaps first”）；研究 §{SECTION}。',
            f'16 October 2026: added, integration I4b item 1 (Ren chose “Closest gaps first”); study section {SECTION}.')],
        'text_versions': [],
    }


def main():
    r = record()
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), '+', len(r['references'][1]['declarations']),
          'declarations')


if __name__ == '__main__':
    main()
