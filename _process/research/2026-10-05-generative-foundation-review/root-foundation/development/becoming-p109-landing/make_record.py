#!/usr/bin/env python3
"""P109: write the schema-2 record where-a-move-is-formed into a checkout.

usage: python3 -B make_record.py ROOT

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then the record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Coupling.lean.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
LEAN = BASE + 'becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-no-two-realities.md',
           'sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md']
REVIEWED = '2026-10-15T00:00:00+00:00'
SECTION = 131


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


NONE = ('无。', 'None.')

LAWS = [
    law('部分与其余由在整体之内形成的一个动作耦合（同步积，动作从联合配置读出）：两方每一步取同一个动作，部分所做的就是其余所受的；'
        '耦合的整体就是积的 closedBy，动作读出而不读入；确定的律的耦合是确定的。',
        'A part and the rest are coupled by one move formed within the whole (the synchronized product, the move read off '
        'the joint configuration): both take one move at every step, what the part does being what the rest undergoes; '
        "the coupled whole is the product's closedBy, the move read off rather than read in; a coupling of determined "
        'laws is determined.',
        ['coupled', 'Run.part', 'Run.rest', 'Run.part_act_eq_rest_act', 'Run.toClosedBy', 'closedBy_formed',
         'Run.ofClosedBy', 'Run.ofClosedBy_toClosedBy', 'coupled_determined']),
    law('动作经配置的一个读法形成，当它随读法所归并者同行（Learning.Lumped）：在整体之内形成的动作经整体的配置形成，经一个读法形成者'
        '经每个至少同样区分的读法形成，经不区分任何东西的读法只形成处处相同的动作。',
        'A move is formed through a reading of the configuration where it goes alike across what the reading lumps '
        "(Learning.Lumped): a move formed within the whole is formed through the whole's configuration, one formed "
        'through a reading is formed through every reading telling apart at least as much, and through a reading telling '
        'nothing apart only a move that is the same everywhere is formed.',
        ['lumped_id', 'lumped_of_finer', 'lumped_const_iff']),
    law('动作是部分的恰当它是部分的策略，是其余的恰当它是其余的策略，两者都是恰当它处处相同，所以有所不同的动作至多由一方单独形成。',
        "The move is the part's exactly where it is a policy of the part, the rest's exactly where it is a policy of "
        'the rest, and both exactly where it is the same everywhere, so a move that differs anywhere is formed by at '
        'most one of them alone.',
        ['PartForms', 'RestForms', 'partForms_iff', 'restForms_iff', 'partForms_and_restForms_iff']),
    law('部分的律确定、动作是部分的时，部分承载自己的律，不论其余如何，部分的进程相同；律是函数时，每一方的进程都是以动作为输入的'
        '标准模型的轨迹，部分自己的动作在部分之内循环，又是其余的输入，整体按一个确定的律循环。',
        "Where the part's law is determined and the move is the part's, the part carries a law of its own and its course "
        "is the same whatever the rest; where the laws are functions, each side's course is the trajectory of the "
        "standard model with the move as input, the part's own move goes round within the part and is the rest's input, "
        'and the whole goes round by one determined law.',
        ['PartForms.goAlike', 'PartForms.parts_agree', 'Run.part_trajectory', 'Run.rest_trajectory', 'Run.part_orbit',
         'Run.rest_orbit', 'Run.rest_driven_by_part', 'wholeNext', 'Run.whole_orbit']),
    law('每个带标签过程的每个运行，无论动作如何，都是一个只有一个行动的整体中部分的进程，其余是一只钟，由它形成动作；进程的标准模型中，'
        '不读任何东西的律的动作只经阶段形成。',
        "Every run of a labelled process, whatever its moves, is the part's course in a whole of one action whose rest, a "
        "clock, forms the moves; in a course's standard model, the act of a law that reads nothing is formed through the "
        'stage alone.',
        ['clock', 'clock_determined', 'Run.withClock', 'Run.withClock_part', 'Run.withClock_restForms',
         'ExchangeLaw.ofMoves_lumped_stage']),
    law('律是函数时，由列表所持的整体、其余或部分形成的动作从某步起周期地重复，起点与周期之和不超过列表的长度；反之每个套索都由其位置'
        '组成的其余形成；所以从不进入循环的动作需要不被任何列表所持的形成者。',
        'Where the laws are functions, moves formed by a whole, a rest or a part held by a list repeat from some step '
        "with some period, start and period within the list's length; conversely every lasso is formed by a rest of its "
        'positions; so moves that never settle into a cycle need a former that no list holds.',
        ['Run.moves_lasso_of_rest_held', 'Run.moves_lasso_of_part_held', 'Run.moves_lasso_of_whole_held',
         'Run.whole_unheld_of_never_cycles', 'Run.rest_unheld_of_never_cycles', 'Run.part_unheld_of_never_cycles',
         'lassoRest', 'Run.withLasso', 'Run.withLasso_held', 'Run.withLasso_part']),
    law('沿一段进程，动作经配置形成，恰当某个在每个配置至多给一个动作的关系给出它们，不需判定；无物复现时每种读法都合，保留其历史的'
        '部分把每个动作读作自己的；部分复现而动作不同之处，其余在那里不同。',
        'Along a course the moves are formed through the configurations exactly where some relation giving at most one '
        'move at each configuration gives them, with no decision; where nothing recurs every reading fits, a part '
        'keeping its history reading every move as its own; where the part recurs with the move varied, the rest '
        'differs there.',
        ['lumped_of_new', 'not_lumped_of_varied', 'lumped_iff_singleValued', 'reading_le', 'rest_differs_of_varied',
         'Coupling.zero_add', 'Coupling.succ_add', 'Coupling.succ_sub_succ', 'Coupling.add_sub_left',
         'Run.keepHistory_formed']),
    law('在有限一段上、配置的相等可判定时，动作由配置的策略给出，恰当它们在同一配置处从不不同；动作的相等也可判定时，没有策略给出它们，'
        '恰当某个配置复现而动作不同。',
        'On a finite stretch with equality of configurations decided, the moves are given by a policy of the '
        'configuration exactly where they never differ at one configuration; with equality of moves decided too, no '
        'policy gives them exactly where a configuration recurs with the move varied.',
        ['policyUpto', 'policyUpto_agrees', 'lumped_upto_iff', 'throughout_or_fails', 'policyUpto_taken',
         'no_policy_upto_iff']),
    law("见证：同一段进程由部分的动作之律与其余的动作之律容许，两者只在进程不到之处不同；动作对其律不起作用的部分对其余封闭，而它的动作是"
        '其余的；部分不动而动作交替时，部分不形成动作；由两者是否不同形成的动作不由任一方单独形成。',
        "Witnesses: one course admitted by the part's law of the move and by the rest's, which differ only where it never "
        "goes; a part to whose law the move makes no difference, closed against the rest while its move is the rest's; a "
        'part standing still while the move alternates, which does not form it; a move formed by whether the two differ, '
        'formed by neither alone.',
        ['Coupling.alt', 'Coupling.ne_not', 'Coupling.alt_ne', 'TwoClocks.byPart', 'TwoClocks.byRest',
         'TwoClocks.together', 'TwoClocks.one_course_two_laws', 'TwoClocks.closed_not_own', 'Still.driven',
         'Parity.partCourse', 'Parity.restCourse', 'Parity.form', 'Parity.move', 'Parity.neither_alone']),
]


def record():
    coupling = LEAN + 'Coupling.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(coupling)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    theorems = sum(1 for line in (ROOT / coupling).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': 'where-a-move-is-formed',
        'title': pair('动作在哪里形成', 'Where a move is formed'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F01',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '在整体之内形成的一个动作耦合部分与其余：它是部分的恰当它是部分的策略，是其余的亦然，两者都是只在它处处相同时；'
            '每个运行都是一个整体中部分的进程，其余形成其动作；一段进程只在某个配置复现而动作不同之处固定动作是谁的。',
            "One move formed in a whole couples a part and the rest: it is the part's exactly where it is the part's "
            "policy, the rest's likewise, both only if constant; every run is a part's course whose moves a rest forms; a "
            'course fixes whose move it is only where a configuration recurs with the move varied.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。各律所写者写在定理中：部分的律确定（Determined），律是函数（每一步的后继由一个函数给出），配置在一个列表之内；'
            '配置与动作的相等可判定只用于有限一段上的策略与排除。',
            "No axiom. What each law needs is written into it: the part's law determined (Determined), the laws functions "
            "(each step's successor given by a function), the configurations within a list; decided equality of "
            'configurations and of moves only for the policy and the exclusion on a finite stretch.')],
        'does_not_show': [
            {**pair('哪种切分恰当，实际的动作是否是部分自己的：部分与其余是给定的（积的两个分量）。',
                    "Which cut of an actual unfolding into part and rest is apt, or that an actual move is the part's "
                    'own: the part and the rest are given (the two factors of the product).'), 'kind': 'scope'},
            {**pair('Run.withClock 以运行的动作为其余的数据：它说明任何动作都能读作在整体之内形成，不说明实际的展开有这样的其余，也不说明是哪一个。',
                    "Run.withClock takes the run's moves as the rest's data: it shows that every move can be read as "
                    'formed within a whole, not that an actual unfolding has such a rest, or which.'),
             'kind': 'non-implication', 'witness': 'Becoming.Run.withClock'},
            {**pair('一段进程不固定动作是谁的：同一段进程由部分的动作之律与其余的动作之律容许。',
                    "One course does not fix whose move it is: one course is admitted by the part's law of the move and "
                    "by the rest's."),
             'kind': 'non-implication', 'witness': 'Becoming.TwoClocks.one_course_two_laws'},
            {**pair('对其余封闭不推出动作是自己的。',
                    "Being closed against the rest does not imply that the move is one's own."),
             'kind': 'non-implication', 'witness': 'Becoming.TwoClocks.closed_not_own'},
            {**pair('律不确定时取哪个后继：耦合只形成动作，不形成后继。',
                    'Which successor a law that is not determined takes: the coupling forms the move, not the successor.'),
             'kind': 'scope'},
            {**pair('部分形成动作的多少（耦合的度量）；反事实之动作经部分自身的识读出（ExchangeLaw.Through 对部分之外的形成陈述）；连续时间。',
                    "How much of a move a part forms (a measure of coupling); the counterfactual's act read through the "
                    "part's own registration (ExchangeLaw.Through is stated for the formations outside the part); "
                    'continuous time.'), 'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': coupling,
             'detail': pair('Parity：动作是部分与其余是否不同；沿进程它不经部分的配置形成，也不经其余的配置形成，只经联合配置形成：'
                            '并非每个动作都是某一方的。',
                            'Parity: the move is whether the part and the rest differ; along the course it is formed '
                            "through neither the part's configurations nor the rest's, only through the joint "
                            "configuration: not every move is one side's.")}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Coupling 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Coupling, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '耦合的度量（部分形成动作的多少，与 Feedback 及到达相连）；反事实之动作经部分自身的识读出；非确定之律的后继由什么形成；连续时间；'
            '独立审查；Ren 对读法（行与受是同一动作的两面、动作是谁的是关于未走之进程的主张）的判断。',
            "A measure of coupling (how much of a move a part forms, with Feedback and reach); the counterfactual's act "
            "read through the part's own registration; what forms the successor of a law that is not determined; "
            "continuous time; an independent review; Ren's judgment on the readings (acting and undergoing as one move "
            'read from its two sides, whose move it is as a claim about courses not taken).'),
        'correspondence': pair(
            'Ren 2026-10-12 对律与历史是同一展开的两种读法：“yes, i do agree with your reading, there are no two realities”；'
            '2026-10-14 对从关系开始的重建：“please, finish all”。本结果回答 process-and-frame-as-readings 与 '
            'counterfactual-is-the-course 的 next_delta：动作何时在展开之内形成（总可如此读，其余形成它），何时是部分自己的（恰当它经部分'
            '的配置形成；一段进程只在配置复现而动作不同之处固定这一点）。读法（AI 的，待 Ren）：行与受是同一个动作的两面；输入是其余的配置，'
            '外来的标签是表示略去其形成的动作；动作是谁的是关于未走之进程的主张；识得越多，越多是自己的；封闭不是自己的；所做之事的新需要开放'
            '或增长。',
            'Ren, 12 October 2026, on law and history as one unfolding read two ways: “yes, i do agree with your reading, '
            'there are no two realities”; 14 October 2026, on the relation-first re-founding: “please, finish all”. This '
            'result answers the next_delta of process-and-frame-as-readings and counterfactual-is-the-course: when a move is '
            "formed within the unfolding (it can always be read so, its rest forming it) and when it is the part's own "
            "(exactly where it is formed through the part's configuration; one course fixes this only where a configuration "
            "recurs with the move varied). Readings (the AI's, pending Ren): acting and undergoing are one move read from "
            "its two sides; an input is the rest's configuration, and a label from outside is a move whose forming the "
            "representation leaves out; whose move it is, is a claim about courses not taken; reading more, more is one's "
            'own; closed is not own; novelty in what is done needs openness or growth.'),
        'canonical_source': coupling,
        'aliases': ['where a move is formed', '动作在哪里形成', 'whose move it is', '动作是谁的',
                    'acting and undergoing as one move', '行与受是同一动作的两面',
                    'no move from outside the whole', '无需从整体之外供给'],
        'dependencies': [
            dep('process-and-frame-as-readings',
                '复用 closedBy 与 Fork.label_couples：耦合的整体就是积的 closedBy，共享的动作是两方之间的关系。',
                "Reuses closedBy and Fork.label_couples: the coupled whole is the product's closedBy, and the shared move "
                'is the relation between the two sides.',
                ('closedBy：动作由配置的策略形成；共享的动作是部分之间的关系。',
                 "closedBy: a move formed by a policy of the configuration; a shared move as a relation between parts."),
                ('耦合的整体与积的 closedBy 是同一个运行的两种读法。',
                 "The coupled whole and the product's closedBy as two readings of one run."), NONE, 'Unfolding'),
            dep('counterfactual-is-the-course',
                '复用 ExchangeLaw.ofMoves、ExchangeLaw.policy 与 ExchangeLaw.stepBy：供给的动作在进程的标准模型中只经阶段形成。',
                "Reuses ExchangeLaw.ofMoves, ExchangeLaw.policy and ExchangeLaw.stepBy: supplied moves are formed through "
                "the stage alone in a course's standard model.",
                ('进程的标准模型；不读任何东西的律给出供给的动作。',
                 "A course's standard model; a law that reads nothing gives the supplied moves."),
                ('供给的动作如钟所形成的动作。', 'Supplied moves as the moves a clock forms.'), NONE, 'Counterfactual'),
            dep('causal-models-as-processes',
                '复用 trajectory：每一方的进程是以动作为输入的标准模型的轨迹。',
                "Reuses trajectory: each side's course is the trajectory of the standard model with the move as input.",
                ('标准模型的轨迹。', 'The trajectory of the standard model.'),
                ('自己的动作是其余的输入。', "An own move as the rest's input."),
                ('律是函数。', 'The laws are functions.'), 'Mechanism'),
            dep('projection-carrying-a-law',
                '复用 GoAlike、GoAlike.runs_agree 与 carries_law_iff：自己的动作封闭部分。',
                'Reuses GoAlike, GoAlike.runs_agree and carries_law_iff: an own move closes the part.',
                ('投影承载规律；同行的投影使运行一致。', 'A projection carrying a law; runs agreeing under it.'),
                ('部分承载自己的律，不论其余如何。', 'The part carrying a law of its own, whatever the rest.'),
                ("部分的律确定。", "The part's law determined."), 'Mechanism'),
            dep('recurrence-without-premise',
                '复用 Law.orbit：自己的动作在部分之内循环，整体按一个确定的律循环。',
                'Reuses Law.orbit: an own move goes round within the part, and the whole goes round by one determined law.',
                ('一个函数之律的轨道。', 'The orbit of a law that is a function.'),
                ('部分、其余与整体的进程作为轨道。', 'The courses of the part, the rest and the whole as orbits.'),
                ('律是函数。', 'The laws are functions.'), 'Recurrence'),
            dep('generalization-through-lumping',
                '复用 Learning.Lumped：经一个读法形成即随它所归并者同行。',
                'Reuses Learning.Lumped: formed through a reading is going alike across what it lumps.',
                ('归并：随读法所归并者同行。', 'Lumping: going alike across what a reading lumps.'),
                ('动作经部分、其余或配置形成。', 'A move formed through the part, the rest or the configurations.'),
                NONE, 'Learning'),
            dep('learning-by-refutation',
                '复用 Learning.Lasso、lasso_of_held、lassoNext、lasso_positions、upto 与 mem_upto：列表所持者形成套索，每个套索都如此形成。',
                'Reuses Learning.Lasso, lasso_of_held, lassoNext, lasso_positions, upto and mem_upto: what a list holds forms '
                'a lasso, and every lasso is so formed.',
                ('列表所持的轨道是套索；套索的位置。', 'An orbit held by a list is a lasso; the positions of a lasso.'),
                ('列表所持的形成者只形成套索。', 'A former held by a list forms only lassos.'),
                ('律是函数，配置在列表之内。', 'The laws are functions and the configurations within a list.'), 'Learning'),
            dep('control-coherence-loss',
                '复用 Readout.Reading、SingleValued、reading_single_iff、Decodes 与 lumped_of_decodes：记录所显示的动作之律。',
                'Reuses Readout.Reading, SingleValued, reading_single_iff, Decodes and lumped_of_decodes: the law of the '
                'move a record shows.',
                ('经约化的读出单值恰当它随约化同行；解码者。', 'A reading through a reduction is single-valued exactly where it goes alike; decoders.'),
                ('记录固定动作是谁的之处。', 'Where the record fixes whose move it is.'), NONE, 'Readout'),
            dep('experiment-needs-return',
                '复用 keepHistory 与 keepHistory_length：保留历史的部分把每个动作读作自己的。',
                'Reuses keepHistory and keepHistory_length: a part keeping its history reads every move as its own.',
                ('保留的历史及其长度。', 'The kept history and its length.'),
                ('历史的长度告诉步数，所以一个配置的策略给出每个动作。',
                 "The length of the history tells the step, so a policy of the configuration gives every move."),
                NONE, 'Experiment'),
        ],
        'related': [
            {'id': 'premises-read-off-the-exchange',
             'detail': pair('World.withRest 的对应：那里其余的交换从世界读出，这里其余对动作的形成从进程读出；如要求（ExchangeLaw.requirement_beyond_course），'
                            '动作是谁的属于律，一段进程不固定它。',
                            "The counterpart of World.withRest: there the rest's exchange is read off the world, here the "
                            "rest's forming of the move is read off the course; like requirement "
                            '(ExchangeLaw.requirement_beyond_course), whose move it is belongs to the law, which one course '
                            'does not fix.')},
            {'id': 'unity-of-readings',
             'detail': pair('算入其余，每个世界是交换之律的一次运行（World.unity）；算入形成动作的其余，每个带标签过程的运行是一个整体中部分的进程。',
                            'With the rest counted every world is one run of the law of exchange (World.unity); with the '
                            "rest that forms the moves counted, every run of a labelled process is a part's course in a whole.")},
        ],
        'references': [
            proof(coupling, actual),
            proof(BASE + 'GenerativeCore.lean', ['Generative.Process', 'Generative.productProcess']),
            proof(LEAN + 'Frame.lean', ['Becoming.Run']),
            proof(LEAN + 'Joint.lean', ['Becoming.Determined']),
            proof(LEAN + 'Recurrence.lean', ['Becoming.Law.orbit']),
            proof(LEAN + 'Mechanism.lean', ['Becoming.GoAlike', 'Becoming.GoAlike.runs_agree', 'Becoming.carries_law_iff',
                                            'Becoming.trajectory']),
            proof(LEAN + 'Experiment.lean', ['Becoming.keepHistory', 'Becoming.keepHistory_length']),
            proof(LEAN + 'Unfolding.lean', ['Becoming.closedBy', 'Becoming.Fork.label_couples']),
            proof(LEAN + 'Counterfactual.lean', ['Becoming.ExchangeLaw.ofMoves', 'Becoming.ExchangeLaw.policy',
                                                 'Becoming.ExchangeLaw.stepBy']),
            proof(LEAN + 'Learning.lean', ['Becoming.Learning.Lumped', 'Becoming.Learning.Lasso',
                                           'Becoming.Learning.lasso_of_held', 'Becoming.Learning.lassoNext',
                                           'Becoming.Learning.lasso_positions', 'Becoming.Learning.upto',
                                           'Becoming.Learning.mem_upto']),
            proof(LEAN + 'Readout.lean', ['Becoming.Readout.Reading', 'Becoming.Readout.SingleValued',
                                          'Becoming.Readout.reading_single_iff', 'Becoming.Readout.Decodes',
                                          'Becoming.Readout.lumped_of_decodes']),
            proof(LEAN + 'Reading.lean', ['Becoming.World.withRest', 'Becoming.ExchangeLaw.requirement_beyond_course']),
            proof(LEAN + 'Readings.lean', ['Becoming.World.unity']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-15：新增，回答 process-and-frame-as-readings 与 counterfactual-is-the-course 的 next_delta（P109）；研究 §{SECTION}。',
            f'15 October 2026: added, answering the next_delta of process-and-frame-as-readings and '
            f'counterfactual-is-the-course (P109); study section {SECTION}.')],
        'text_versions': [],
    }


def main():
    r = record()
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')


if __name__ == '__main__':
    main()
