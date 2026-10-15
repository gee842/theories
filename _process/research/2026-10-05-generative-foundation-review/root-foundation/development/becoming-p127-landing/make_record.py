#!/usr/bin/env python3
"""P127: write the schema-2 record where-a-run-goes-on into a checkout.

usage: python3 -B make_record.py ROOT [SECTION]

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then the record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Onward.lean, and the reused ones against their modules.
The lengths of the public texts are printed against the lint's caps. SECTION is the study section
(161 unless given).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTION = int(sys.argv[2]) if len(sys.argv) > 2 else 161
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
LEAN = BASE + 'becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md',
           'sources/15-codex-theory-conversations/2026-10-11-zero-premise-laws.md']
REVIEWED = '2026-10-16T00:00:00+00:00'


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pair(zh, en):
    return {'zh': zh, 'en': en}


def proof(path, names):
    return {'path': path, 'role': 'proof', 'sha256': sha(path), 'declarations': names}


def law(zh, en, names):
    return {'zh': zh, 'en': en, 'declarations': ['Becoming.' + n for n in names]}


def dep(ident, zh, en, out, inp, cond, module):
    return {'id': ident, 'relation': 'formal-reuse', 'detail': pair(zh, en),
            'interface': {'output': pair(*out), 'input': pair(*inp), 'conditions': pair(*cond),
                          'evidence': LEAN + module + '.lean'}}


def declared(path):
    """The fully qualified declarations of a core module, read from its namespaces."""
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
        m = re.match(r'^(?:theorem|def|abbrev|structure|inductive)\s+(\S+)', line)
        if m:
            names.append('.'.join(spaces + [m.group(1)]))
    return names


O = 'Onward.'
K = 'KeepsMoving'

LAWS = [
    law('从运行的每个配置开始每个长度的路径，运行的每个配置可从其起点得到；从路径通向之处的运行前接路径即得运行，从路径通向返回者之处'
        '运行绕返回而行。',
        'From each configuration of a run courses of every length start, and each is had from its start; a run from '
        'where a course leads, preceded by the course, is a run, and from where a course leads to a return a run goes '
        'round the return.',
        [O + n for n in ['continues_of_run', 'unbounded_of_run', 'reach_of_run', 'run_of_trace', 'run_of_reach',
                         'run_of_returning']]),
    law('有限多配置之内，与列表一样长的路径重复一个配置而通向返回者；所以运行恰在这样的路径开始处、每个长度的路径都开始处、路径通向'
        '返回者处开始，不需判定也不需选取；后继列出时运行是否开始已定。',
        'Within finitely many configurations a course as long as the list repeats one and leads to a return; so a run '
        'starts exactly where such a course, courses of every length, or a course to a return start, with no decision '
        'and no selection; with successors listed, whether one starts is decided.',
        [O + n for n in ['reach_along', 'returning_of_continues', 'run_of_continues', 'run_iff_continues',
                         'run_iff_unbounded', 'run_iff_returning', 'run_decided']]),
    law('分支无穷时，每个长度的路径不给出运行：扇的根有每个长度的路径，没有运行。',
        'Where branching is infinite, courses of every length give no run: the root of the fan has courses of every '
        'length and no run.',
        [O + 'fan_no_run']),
    law('一族保持运动，指从每个成员有一步通向成员；族内的步构成过程，其运行是留在族中的运行。有限多配置之内，运行从每个成员开始并'
        '留在族中。',
        'A family keeps moving where from each member some step leads to a member; the steps within it form a process '
        'whose runs are the runs staying in the family. Within finitely many configurations a run starts at each '
        'member and stays in the family.',
        [O + n for n in [K, 'within', 'ofWithin', 'ofWithin_within', K + '.continues', K + '.run']]),
    law('不合并、有限多配置之内，不给定运行：配置恰在与列表一样长的路径从它开始处返回，保持运动的族的每个成员都返回；族中跨步不下降'
        '的量每步不变，上升需要合并；每个长度的路径都开始而不返回者需要开放。',
        'Merging nothing within finitely many configurations, with no run given: a configuration returns exactly where '
        'a course as long as the list starts there, and each member of a family that keeps moving returns; a quantity '
        'never falling across a step within the family keeps its value, a rise needing a merge; a configuration with '
        'courses of every length that never returns needs openness.',
        [O + n for n in ['lossless_returns_iff', K + '.returns', 'lossless_no_rise', 'rise_needs_merge',
                         'lossless_unlisted']]),
    law('测试在枚举的移动中认出留在族中的一步时（有这样的一步时某个移动通过），搜索经可达性逐个测试直到通过，每步这样取，运行作为'
        '数据造出，从成员开始并留在族中，不经选取；步与族已定、步的移动被枚举时，逐个测试就是这样的测试。',
        'Where a test recognizes among enumerated moves a step staying in the family (some move passing wherever there '
        'is such a step), search through accessibility tests each until one passes; taking each step so builds a run '
        'as data, from the member and staying in the family, with no selection; where steps and the family are '
        'decided and the steps\' moves enumerated, testing each move is such a test.',
        [O + n for n in ['Later', 'searchFrom', 'acc_below', 'search', 'Finds', 'searchedStep', 'searchedRun',
                         'searchedRun_start', 'searchedRun_within', 'decidedTest', 'decidedTest_finds']]),
    law('对每个过程要求从每个保持运动的族的每个成员出发都有留在族中的运行，恰是依赖选择：全的关系从每个起点有沿它的序列。',
        'A run staying in the family from every member of every family that keeps moving, asked of every process, is '
        'exactly dependent choice: a total relation has a sequence along it from every start.',
        [O + n for n in ['DependentSelection', 'moveOf', 'moveOf_eq', 'runs_iff_selection']]),
]

BRANCHING = ['Becoming.Branching.Returns', 'Becoming.Branching.Lossless', 'Becoming.Branching.Returns.run',
             'Becoming.Branching.Lossless.returns', 'Becoming.Branching.Lossless.no_rise']
LASTING = ['Becoming.Lasting.Continues', 'Becoming.Lasting.Continues.decided', 'Becoming.Lasting.Unbounded',
           'Becoming.Lasting.FinitelyBranching', 'Becoming.Lasting.runOf', 'Becoming.Lasting.runOf_within',
           'Becoming.Lasting.Fan.process', 'Becoming.Lasting.Fan.no_unbounded_step']
PARTING = ['Becoming.Parting.path_of_continues', 'Becoming.Parting.and_both', 'Becoming.Parting.and_of']
RECURRENCE = ['Becoming.revisits_within', 'Becoming.gap_of_lt']
FRAME = ['Becoming.Run', 'Becoming.Reach', 'Becoming.Reach.refl', 'Becoming.Reach.of_step', 'Becoming.Reach.trans',
         'Becoming.Run.reach']
HORIZON = ['Becoming.Run.cons']
DECIDEDNESS = ['Becoming.Decided']

CAPS = {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260), 'next_delta': (400, 180),
        'correspondence': (1200, 500), 'laws': (420, 190), 'hypotheses': (420, 190), 'does_not_show': (240, 110)}


def record():
    onward = LEAN + 'Onward.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(onward)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    assert len(set(listed)) == len(listed)
    reused = [(LEAN + 'Branching.lean', BRANCHING), (LEAN + 'Lasting.lean', LASTING), (LEAN + 'Parting.lean', PARTING),
              (LEAN + 'Recurrence.lean', RECURRENCE), (LEAN + 'Frame.lean', FRAME), (LEAN + 'Horizon.lean', HORIZON),
              (LEAN + 'Decidedness.lean', DECIDEDNESS)]
    for path, names in reused:
        missing = set(names) - set(declared(path))
        assert not missing, (path, missing)
        assert len(set(names)) == len(names), path
    theorems = sum(1 for line in (ROOT / onward).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': 'where-a-run-goes-on',
        'title': pair('运行在何处延续', 'Where a run goes on'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '有限多配置之内，运行恰是通向返回的路径，由路径本身给出；沿运行的定律对每个能继续运动的配置成立；测试认出移动处运行经搜索'
            '造出；对每个过程要求运行，恰是依赖选择。',
            'Within finitely many configurations a run is exactly a course into a return, given by the course itself, '
            'and the laws along runs hold wherever the process can keep moving; a search over recognized moves builds '
            'one; asked of every process, a run is dependent choice.'),
        'laws': LAWS,
        'hypotheses': [
            pair('不加公理。列出全部配置的列表、后继的列表、测试与枚举、步与族的判定在用到处作为假设写入，不假定；依赖选择作为命题陈述，'
                 '不假定。',
                 'No axiom. A list holding every configuration, the listed successors, a test with an enumeration, and '
                 'decisions of the steps and the family are written in as hypotheses where used, never assumed; '
                 'dependent choice is stated as a proposition, never assumed.')],
        'does_not_show': [
            {**pair('核心是否给出依赖选择：那是关于理论的陈述，需要核心之外的模型。',
                    'Whether the core gives dependent choice: a statement about the theory, needing a model outside '
                    'it.'),
             'kind': 'scope'},
            {**pair('每个长度的路径给出运行，不限于有限多配置：扇的根有每个长度的路径，没有运行。',
                    'That courses of every length give a run beyond finitely many configurations: the root of the fan '
                    'has courses of every length and no run.'),
             'kind': 'non-implication', 'witness': 'Becoming.Onward.fan_no_run'},
            {**pair('有限分支而不搜索时沿无界配置的运行（Lasting 经 EitherThroughout 与选取给出）；不列出配置时沿运行的定律。',
                    'Runs along unbounded configurations where branching is finite and nothing is searched (given in '
                    'Lasting through EitherThroughout and a selection); the laws along runs where nothing lists the '
                    'configurations.'),
             'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': LEAN + 'Lasting.lean',
             'detail': pair('扇（Lasting.Fan）：根有每个长度的路径而没有运行（Onward.fan_no_run）：有限多配置之外，每个长度的路径不给出'
                            '运行。',
                            'The fan (Lasting.Fan): the root has courses of every length and no run (Onward.fan_no_run): '
                            'beyond finitely many configurations, courses of every length give no run.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Onward 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Onward, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '不列出配置时沿运行的定律（例如以测试与枚举陈述）；在界内被吸入；独立审查；Ren 对读法的判断。',
            'The laws along runs where nothing lists the configurations (for instance through a test and an '
            'enumeration); being drawn in within a bound; an independent review; Ren\'s judgment on the readings.'),
        'correspondence': pair(
            'Ren 2026-10-12 的目标：“move towards 100%, you can spawn a few agents for help, pick the \"What would move '
            'it most next\" first, and don\'t stop until we are 100%”。本结果回答 returning-where-the-course-branches 的 '
            'next_delta 与 lifting-where-branching-is-finite 的 next_delta 第二项。读法（AI 的，待 Ren）：有限多配置之内，无尽地进行者'
            '靠回转而进行，路径本身显出它在何处返回，不需选取，延续从展开读出；配置不受界时，无尽的进行在能搜索移动处给出，对每个过程要求'
            '每个能继续运动的配置都开始一个运行，恰是依赖选择。依赖选择是标准名，核心名 DependentSelection 沿 Lasting 的“选取”；选取是每步'
            '取一个延续的函数，不是一个选取者。',
            'Ren, 12 October 2026, the goal: “move towards 100%, you can spawn a few agents for help, pick the \"What '
            'would move it most next\" first, and don\'t stop until we are 100%”. This result answers the next_delta of '
            'returning-where-the-course-branches and the second item of the next_delta of '
            'lifting-where-branching-is-finite. Readings (the AI\'s, pending Ren): within finitely many configurations, '
            'whatever goes on without end does so by coming round; the course itself shows where it returns, nothing is '
            'selected, and going on is read off the unfolding; where the configurations are not bounded, going on '
            'without end is given where the moves can be searched, and asked of every process, that every '
            'configuration that can keep moving starts a run is exactly dependent choice. Dependent choice is the standard '
            'name; the core name DependentSelection follows Lasting\'s selection, a function taking a continuation at '
            'each step, not a selector.'),
        'canonical_source': onward,
        'aliases': ['where a run goes on', '运行在何处延续', 'a run is a course into a return', '运行是通向返回的路径',
                    'keeps moving', '保持运动', 'run without a selection', '不用选取时的运行', 'dependent choice',
                    '依赖选择', 'searched run', '搜索的运行'],
        'dependencies': [
            dep('returning-where-the-course-branches',
                '复用返回（Returns）、不合并（Lossless）、返回者的运行（Returns.run）与沿运行的定律（Lossless.returns、'
                'Lossless.no_rise）：本结果给出运行，使这些定律不给定运行而成立。',
                'Reuses returning (Returns), merging nothing (Lossless), the run of what returns (Returns.run) and the '
                'laws along runs (Lossless.returns, Lossless.no_rise): this result supplies the run, so the laws hold '
                'with no run given.',
                ('返回；不合并；返回者绕返回而行的运行；不合并时沿运行返回、不上升。',
                 'Returning; merging nothing; a run going round a return; returning and no rise along runs where '
                 'nothing merges.'),
                ('运行恰是通向返回的路径；沿运行的定律不给定运行。',
                 'A run as a course into a return; the laws along runs with no run given.'),
                ('列出全部配置的列表。', 'A list holding every configuration.'),
                'Branching'),
            dep('lifting-where-branching-is-finite',
                '复用路径（Continues）与其深度之判定、无界（Unbounded）、有限分支、选取给出运行（runOf）与扇（Fan）。',
                'Reuses courses (Continues) and the decision of their depth, unboundedness (Unbounded), finite '
                'branching, a selection giving a run (runOf) and the fan (Fan).',
                ('n 步的路径；后继列出时其深度已定；选取给出运行；扇的根无界而无无界后继。',
                 'Courses of n steps; their depth decided where successors are listed; a selection giving a run; the '
                 'fan\'s root unbounded with no unbounded successor.'),
                ('运行与路径的当且仅当；运行是否开始已定；搜索的运行；扇没有运行。',
                 'The equivalences of runs and courses; whether a run starts, decided; the searched run; the fan has no '
                 'run.'),
                ('无。', 'None.'),
                'Lasting'),
            dep('identification-where-runs-part',
                '复用路径按位置（path_of_continues）与布尔的合取（and_both、and_of）。',
                'Reuses courses by position (path_of_continues) and Boolean conjunction (and_both, and_of).',
                ('n 步的路径按位置列出。', 'A course of n steps listed by position.'),
                ('与列表一样长的路径通向返回者。', 'A course as long as the list leading to a return.'),
                ('无。', 'None.'),
                'Parting'),
            dep('recurrence-without-premise',
                '复用列表中的重复（revisits_within）与间隔（gap_of_lt）：与列表一样长的路径重复一个配置。',
                'Reuses repetition within a list (revisits_within) and gaps (gap_of_lt): a course as long as the list '
                'repeats a configuration.',
                ('列表持有的序列在列表长度之内重复。', 'A sequence a list holds repeats within the list\'s length.'),
                ('路径重复一个配置，被重复者返回。', 'A course repeats a configuration, which returns.'),
                ('无。', 'None.'),
                'Recurrence'),
        ],
        'related': [
            {'id': 'returning-where-the-course-branches',
             'detail': pair('回答其下一步：沿运行的定律对每个能继续运动的配置成立，不给定运行，有限即可，不需可判定。',
                            'Answers its next step: the laws along runs hold for every configuration that can keep '
                            'moving, with no run given; finiteness suffices, with no decidability.')},
            {'id': 'lifting-where-branching-is-finite',
             'detail': pair('回答其下一步“不用选取时的运行”：有限多配置之内不需选取，测试认出移动处经搜索，一般地恰是依赖选择。',
                            'Answers its next step, a run without a selection: within finitely many configurations none '
                            'is needed, where a test recognizes the moves a run is built by search, and in general it is '
                            'exactly dependent choice.')},
            {'id': 'what-a-law-of-the-whole-and-no-part-takes',
             'detail': pair('同样确定一个推理原则的确切位置：那里反例恰是弱有限全知原则作为规则；这里运行恰是依赖选择。',
                            'Likewise fixes the exact place of a principle of reasoning: there a counterexample is '
                            'exactly the weak limited principle as a rule; here a run is exactly dependent choice.')},
        ],
        'references': [
            proof(onward, actual),
            proof(LEAN + 'Branching.lean', BRANCHING),
            proof(LEAN + 'Lasting.lean', LASTING),
            proof(LEAN + 'Parting.lean', PARTING),
            proof(LEAN + 'Recurrence.lean', RECURRENCE),
            proof(LEAN + 'Frame.lean', FRAME),
            proof(LEAN + 'Horizon.lean', HORIZON),
            proof(LEAN + 'Decidedness.lean', DECIDEDNESS),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，回答 returning-where-the-course-branches 的 next_delta 与 lifting-where-branching-is-finite 的'
            f' next_delta 第二项（P127）；研究 §{SECTION}。',
            f'16 October 2026: added, answering the next_delta of returning-where-the-course-branches and the second '
            f'item of the next_delta of lifting-where-branching-is-finite (P127); study section {SECTION}.')],
        'text_versions': [],
    }


def lengths(r):
    over = []
    for key in ('title', 'statement', 'validation_scope', 'next_delta', 'correspondence'):
        for lang, cap in zip(('en', 'zh'), CAPS[key]):
            n = len(r[key][lang])
            if n > cap:
                over.append((key, lang, n, cap))
    for key in ('laws', 'hypotheses', 'does_not_show'):
        for i, item in enumerate(r[key]):
            for lang, cap in zip(('en', 'zh'), CAPS[key]):
                n = len(item[lang])
                if n > cap:
                    over.append((f'{key}[{i}]', lang, n, cap))
    return over


def main():
    r = record()
    path = REC / f'{r["id"]}.json'
    assert not path.exists(), 'the record is already there'
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')
    for o in lengths(r):
        print('over cap:', *o)


if __name__ == '__main__':
    main()
