#!/usr/bin/env python3
"""I4b-4: write the schema-2 record lifting-where-branching-is-finite (run from the repository root at landing).

usage: python3 -B make_record_lasting.py SECTION

Run after the core receipt holding the I4b-4 edits of Becoming.Lasting exists and the periphery checker
check_finite_branching_correspondence.py has passed against it. It binds Lasting.lean to the retained core receipt,
and FiniteBranchingCorrespondence.lean and FiniteBranching.lean to the retained instance receipt, which hashes
FiniteBranching after matching it to the completion package receipt (the package receipt's own format is not one the
research check reads; it stays a reference, as at the I4b-3 landing). The declarations listed in the laws are checked
against the new section of Lasting.lean and the instance module, and the statement, title, validation scope and next
delta against the research check's hard length caps.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/'
LASTING = BASE + 'lean/becoming/Becoming/Lasting.lean'
FORMAL = BASE + 'mathematical-abstraction/completion/formal/'
INSTANCE = FORMAL + 'FiniteBranchingCorrespondence.lean'
BRANCHING = FORMAL + 'FiniteBranching.lean'
PACKAGE = FORMAL + 'verification.json'
CORE_POINTER = BASE + 'lean/becoming/becoming-verification.json'
INSTANCE_POINTER = FORMAL + 'finite-branching-correspondence-verification.json'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-16-i4-decisions.md',
           'sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md']
REVIEWED = '2026-10-16T00:00:00+00:00'
SECTION = int(sys.argv[1])
# The new section of Lasting.lean starts here; what precedes it stays with the three market records.
MARKER = '/-! ## Lasting some course'
# The research check's hard caps (tools/research/style.py): (en, zh).
CAPS = {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260), 'next_delta': (400, 180)}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pair(zh, en):
    return {'zh': zh, 'en': en}


def declared(path, after=None):
    """The fully qualified declarations of a module, read from its namespaces; with `after`, only those following
    the line that starts with it."""
    names, spaces, on = [], [], after is None
    for line in (ROOT / path).read_text().splitlines():
        if not on and line.startswith(after):
            on = True
        m = re.match(r'^namespace (\S+)', line)
        if m:
            spaces.append(m.group(1))
            continue
        m = re.match(r'^end (\S+)', line)
        if m and spaces and spaces[-1] == m.group(1):
            spaces.pop()
            continue
        m = re.match(r'^(?:theorem|def|abbrev|structure|inductive|instance)\s+(\S+)', line)
        if m and on:
            names.append('.'.join(spaces + [m.group(1)]))
    assert on, after
    return names


def law(zh, en, names):
    return {'zh': zh, 'en': en, 'declarations': names}


def l(*names):
    return ['Becoming.Lasting.' + n for n in names]


def i(*names):
    return ['Becoming.FiniteBranchingCorrespondence.' + n for n in names]


LAWS = [
    law('某段 n 步的进程始于 s（Continues）；每个长度的进程都始于 s（Unbounded）；过程有限分支：每个配置的后继列出。n + 1 步的进程'
        '以 n 步的进程开始；有限分支处所达深度已定。',
        'Some course of n steps starts at s (Continues); courses of every length do (Unbounded); the process branches '
        'finitely where the successors of each configuration are listed. A course of n + 1 steps begins one of n, '
        'and where the process branches finitely the depth reached is decided.',
        l('Continues', 'Unbounded', 'FinitelyBranching', 'Continues.down', 'Continues.decided')),
    law('列表的成员满足已定递减族的每一步时，某成员处处满足，于双重否定下；所以有限分支处，无界配置不能没有无界后继。不用原则：'
        '目标是否证，故首个成员是否某处不满足可当作已定。',
        'Where each step of a decided decreasing family is met by some member of a list, some member meets every step, '
        'up to double negation; so where the process branches finitely, an unbounded configuration cannot fail to '
        'have an unbounded successor. No principle is used: the goal is a refutation.',
        l('list_throughout_not_not', 'Unbounded.successors', 'Unbounded.step_not_not')),
    law('给定 EitherThroughout，无界配置有无界后继，有限个起点中有每个长度进程者时其一无界（EitherThroughout.list 用于列出的后继'
        '或起点）。',
        'Given EitherThroughout, an unbounded configuration has an unbounded successor, and of finitely many starts '
        'among which courses of every length start, one is unbounded (EitherThroughout.list on the listed successors '
        'or starts).',
        l('Unbounded.step_of_either', 'unbounded_start_of_either')),
    law('留在一族之内的步的选取，从族的每个成员给出留在族内的运行。提升：有限分支处，EitherThroughout 与在有无界后继处对它的选取，'
        '使每个无界配置开始一个沿无界配置的运行。',
        'A selection of a step staying in a family gives a run from each member, staying in the family. Lifting: where '
        'the process branches finitely, EitherThroughout and a choice of an unbounded successor wherever one exists '
        'give every unbounded configuration a run along unbounded configurations.',
        l('along', 'runOf', 'runOf_start', 'runOf_within', 'lifting')),
    law('对每个有限分支过程都要求时，无界配置有无界后继恰是 EitherThroughout。见证：两个已定递减族每步有一个成立，使 Chains 两条链'
        '的分叉无界；无界后继是其族处处成立的链首。',
        'Asked of every finitely branching process, an unbounded configuration having an unbounded successor is '
        'exactly EitherThroughout. Witness: two decided decreasing families, one holding at each step, make the fork '
        'of the two chains of Chains unbounded; an unbounded successor is a chain start whose family holds throughout.',
        l('TwoChains.process', 'TwoChains.branching', 'TwoChains.chain_continues', 'TwoChains.chain_holds',
          'TwoChains.two_unbounded', 'TwoChains.side_of_unbounded', 'step_iff_either')),
    law('无有限分支时：根步到每个长度的臂，有每个长度的进程，而其后继都没有（长 n 的臂没有 n + 1 步的进程）。',
        'Without finite branching: a root stepping to an arm of every length has courses of every length, and none of '
        'its successors does (the arm of length n has no course of n + 1 steps).',
        l('Fan.Pos', 'Fan.Step', 'Fan.process', 'Fan.arm_continues', 'Fan.arm_bounded', 'Fan.root_unbounded',
          'Fan.no_unbounded_step')),
    law('实例（外围，自有检查器）：FiniteBranching 的关系即一个动作的过程，Reach 即 Continues，列出的子节点使其有限分支；经典推理给出 '
        'EitherThroughout，Lean 的选择选取无界后继，其五条提升定理由核心律给出。',
        'Instance (periphery, own checker): in FiniteBranching a relation is the process with one move, Reach is '
        'Continues and Unbounded is Unbounded, and listed children make the process finitely branching; classical '
        'reasoning gives EitherThroughout and Lean\'s choice selects an unbounded successor, so its five lifting '
        'theorems (finite_unbounded to labelled_lifting) follow from the core.',
        i('process', 'reach_iff_continues', 'unbounded_iff', 'finitelyBranching', 'either_classical',
          'finite_unbounded_by_core', 'unbounded_child_by_core', 'infinite_from_unbounded_by_core',
          'finite_initial_lifting_by_core', 'labelled_lifting_by_core')),
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
    assert receipt['source_sha256']['FiniteBranching.lean'] == sha(BRANCHING), 'package receipt predates FiniteBranching'


def record():
    new = declared(LASTING, MARKER)
    instance = declared(INSTANCE)
    listed = [d for x in LAWS for d in x['declarations']]
    assert sorted(listed) == sorted(new + instance), set(listed) ^ set(new + instance)
    core_receipt = passed(CORE_POINTER, 'Becoming.Lasting', LASTING)
    instance_receipt = passed(INSTANCE_POINTER, 'FiniteBranchingCorrespondence', INSTANCE)
    assert passed(INSTANCE_POINTER, 'FiniteBranching', BRANCHING) == instance_receipt
    package_passed()
    theorems = sum(1 for line in (ROOT / LASTING).read_text().splitlines() if line.startswith('theorem '))
    added = sum(1 for line in (ROOT / LASTING).read_text().split(MARKER, 1)[1].splitlines()
                if line.startswith('theorem '))
    bindings = [
        {'source': LASTING, 'receipt': core_receipt, 'sha256_pointer': '/source_sha256/Becoming.Lasting',
         'success_pointer': '/status', 'success_value': 'passed'},
        {'source': INSTANCE, 'receipt': instance_receipt,
         'sha256_pointer': '/source_sha256/FiniteBranchingCorrespondence',
         'success_pointer': '/status', 'success_value': 'passed'},
        # The instance receipt also hashes FiniteBranching, matched to the package receipt during the run.
        {'source': BRANCHING, 'receipt': instance_receipt, 'sha256_pointer': '/source_sha256/FiniteBranching',
         'success_pointer': '/status', 'success_value': 'passed'},
    ]
    r = {
        'schema_version': 2,
        'id': 'lifting-where-branching-is-finite',
        'title': pair('有限分支处的提升', 'Lifting where branching is finite'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F01',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '对每个有限分支的过程：所达深度已定；有每个长度进程的配置不能没有同样的后继；有之由 EitherThroughout 给出，对每个这样的过程'
            '要求时恰是此原则；选取给出运行。',
            'For every finitely branching process: the depth reached is decided; a configuration with courses of every '
            'length cannot fail to have a successor with them; it has one given EitherThroughout, exactly that '
            'principle asked of every such process; and a selection gives a run.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。过程任意；有限分支是假设（每个配置的后继列出）；EitherThroughout 是 step_of_either 与 lifting 的假设，'
            '对无界后继的选取是 lifting 的假设。',
            'No axiom. The process is arbitrary; finite branching is a hypothesis (the successors of each configuration '
            'listed); EitherThroughout is a hypothesis of step_of_either and lifting, and a choice of an unbounded '
            'successor one of lifting.')],
        'does_not_show': [
            {**pair('不用 EitherThroughout 时无界后继存在：对每个有限分支过程要求它恰是此原则。',
                    'An unbounded successor without EitherThroughout: asked of every finitely branching process it is '
                    'exactly that principle.'),
             'kind': 'non-implication', 'witness': 'Becoming.Lasting.step_iff_either'},
            {**pair('无有限分支时的提升：扇有每个长度的进程，其后继都没有。',
                    'Lifting without finite branching: the fan has courses of every length and none of its successors '
                    'does.'),
             'kind': 'non-implication', 'witness': 'Becoming.Lasting.Fan.no_unbounded_step'},
            {**pair('不经选取的运行：运行由在有无界后继处对它的选取造出，此处不由原则推出选取。',
                    'A run with no selection: the run is built from a choice of an unbounded successor wherever one '
                    'exists, which the principle does not give here.'), 'kind': 'scope'},
            {**pair('提升给出运行的存在，不给有效的选取或物理的无穷。',
                    'That lifting selects effectively or realizes a physical infinity: it gives a run\'s existence.'),
             'kind': 'scope'},
        ],
        'counterexamples': [],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查：Becoming.Lasting 共 {theorems} 项定理，新增 {len(new)} 项声明（{added} 项定理）公理报告'
            f'为空。外围实例 FiniteBranchingCorrespondence 由其检查器实查（Lean 4.30.0-rc2；四项对应公理报告为空，其余六项只用标准'
            f'公理），FiniteBranching 经实例回执绑定，其字节与完成包回执相合。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker: Becoming.Lasting has {theorems} theorems, and the '
            f'{len(new)} new declarations ({added} theorems) have empty axiom reports. The periphery instance '
            f'FiniteBranchingCorrespondence is checked by its own checker (Lean 4.30.0-rc2; four correspondences with '
            f'empty axiom reports, the other six with standard axioms only); FiniteBranching is bound through the '
            f'instance receipt, its bytes matching the completion package receipt. Author counterreview in study '
            f'section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '独立审查；不用选取时的运行（依赖选择的边界）；其余最近的缺口（Selection）。',
            'An independent review; a run without a selection (the boundary of dependent choice); the other closest gap '
            '(Selection).'),
        'correspondence': pair(
            'Ren 2026-10-16 对 I4 归类表选择“Closest gaps first”。归类表把 FiniteBranching 读作待接入的律：Becoming.Lasting 陈述了每个'
            '可容许进程都留下（Lasts、kernel_iff_lasts），未陈述某段进程延续。本结果陈述它，FiniteBranching 的提升是一个动作的过程的实例，'
            '其经典步分别是 EitherThroughout 与选取。读法（AI 的，待 Ren）：有每个长度的进程尚不是一段延续的进程；有限分支处二者之间所隔的，'
            '恰是在两支之间知道哪一支处处延续。',
            'Ren, 16 October 2026, chose “Closest gaps first” on the I4 classification table. The table read '
            'FiniteBranching as a join candidate: Becoming.Lasting stated that every admissible course stays (Lasts, '
            'kernel_iff_lasts), not that some course goes on. This result states it, with FiniteBranching\'s lifting '
            'as the instance of the process with one move; its classical steps are EitherThroughout and a selection. '
            'Readings (the AI\'s, pending Ren): courses of every length are not yet one course going on; where '
            'branching is finite, what lies between them is exactly knowing which of two branches goes on throughout.'),
        'canonical_source': LASTING,
        'aliases': ['Becoming.Lasting.lifting', 'Becoming.Lasting.step_iff_either', 'Becoming.Lasting.Unbounded',
                    'Becoming.Lasting.Unbounded.step_not_not', 'Becoming.Lasting.FinitelyBranching',
                    'lifting where branching is finite', '有限分支处的提升', 'König lifting', 'Kőnig lifting',
                    'lasting some course', '持续某段进程'],
        'dependencies': [{
            'id': 'tests-fix-likeness-where-determined', 'relation': 'formal-reuse',
            'detail': pair('复用 Becoming.Likeness 的 EitherThroughout、EitherThroughout.list、Decided.exists_listed、holds_below 与 '
                           'Chains（两条链及其列出的后继）。',
                           'Reuses Becoming.Likeness\'s EitherThroughout, EitherThroughout.list, Decided.exists_listed, '
                           'holds_below and Chains (the two chains and their listed outcomes).'),
            'interface': {'output': pair('EitherThroughout 及其列表形式；Chains 的过程与列出的后继。',
                                         'EitherThroughout and its list form; the process of Chains with its listed '
                                         'outcomes.'),
                          'input': pair('无界后继由列表形式给出；边界的见证是两条链的分叉。',
                                        'The unbounded successor comes from the list form; the boundary\'s witness is '
                                        'the fork of the two chains.'),
                          'conditions': pair('族已定且递减。', 'The families decided and decreasing.'),
                          'evidence': BASE + 'lean/becoming/Becoming/Likeness.lean'}}],
        'related': [{'id': 'market-supported-finite-transition', 'detail': pair(
            '其 kernel_iff_lasts 是对偶：无进程离开者恰是持续每个步数者，不需有限分支或原则。',
            'Its kernel_iff_lasts is the dual: what no course leaves is what lasts every horizon, with no finite branching '
            'or principle needed.')}],
        'references': [
            {'path': LASTING, 'role': 'proof', 'sha256': sha(LASTING), 'declarations': new},
            {'path': INSTANCE, 'role': 'proof', 'sha256': sha(INSTANCE), 'declarations': instance},
            {'path': BRANCHING, 'role': 'proof', 'sha256': sha(BRANCHING),
             'declarations': ['CompletionLifting.Reach', 'CompletionLifting.Unbounded',
                              'CompletionLifting.finite_unbounded', 'CompletionLifting.unbounded_child',
                              'CompletionLifting.infinite_from_unbounded', 'CompletionLifting.finite_initial_lifting',
                              'CompletionLifting.labelled_lifting']},
            {'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt)},
            {'path': instance_receipt, 'role': 'receipt', 'sha256': sha(instance_receipt)},
            {'path': PACKAGE, 'role': 'receipt', 'sha256': sha(PACKAGE)},
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': bindings,
        'history': [pair(
            f'2026-10-16：新增，整合 I4b 第四项（Ren 选择“Closest gaps first”）；研究 §{SECTION}。',
            f'16 October 2026: added, integration I4b item 4 (Ren chose “Closest gaps first”); study section {SECTION}.')],
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
