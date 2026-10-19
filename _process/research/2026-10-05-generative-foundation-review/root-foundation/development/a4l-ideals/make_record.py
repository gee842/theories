#!/usr/bin/env python3
"""Write the record a-history-read-off-its-finite-stretches for A4-L:
python3 -B make_record.py CORE_RECEIPT SECTION CORRESPONDENCE_RECEIPT

CORE_RECEIPT names the core checker's run folder under becoming-checks/, CORRESPONDENCE_RECEIPT the correspondence
checker's under ideals-correspondence-checks/; SECTION is the study section number. Every declaration the record names
is checked against its file, the source hashes against both receipts, and the aliases against every other record's,
before anything is written."""
import datetime
import glob
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
FORMAL = 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal'
sys.path.insert(0, str(ROOT / PKG))
sys.dont_write_bytecode = True
import check_becoming as cb  # noqa: E402

core_id, section, corr_id = sys.argv[1], sys.argv[2], sys.argv[3]
CORE_RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
CORR_RECEIPT = f'{FORMAL}/ideals-correspondence-checks/{corr_id}/verification.json'
PACKAGE_RECEIPT = f'{FORMAL}/verification.json'
core = json.loads((ROOT / CORE_RECEIPT).read_text())
corr = json.loads((ROOT / CORR_RECEIPT).read_text())
assert core['status'] == 'passed' and corr['status'] == 'passed', (core['status'], corr['status'])
IDEALS, HISTORY = f'{PKG}/Becoming/Ideals.lean', f'{PKG}/Becoming/HistoryIdeals.lean'
HORIZON, LANGUAGES, CHANGE = (f'{PKG}/Becoming/Horizon.lean', f'{PKG}/Becoming/HistoryLanguages.lean',
                              f'{PKG}/Becoming/Change.lean')
CORR = f'{FORMAL}/IdealsCorrespondence.lean'
REN = 'integrate all, the theory is a whole, not stitched pieces, go ahead'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/what-a-finite-history-refutes.json').read_text())['family']


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'An ideal of a preorder of stretches is a nonempty set of stretches, closed downward, in which any two are '
              'extended by a third; ideals are ordered by inclusion, and two holding the same stretches are the same '
              'history (antisymmetry is not used). A principal ideal is a finite history. For a process, a stretch is a '
              'run with a horizon, one extending another where its horizon is later and the two runs agree up to the '
              'earlier; a run is the ideal of the stretches it passes through, two runs\' ideals lie one below the other '
              'exactly where the runs agree at every horizon, and no run\'s ideal is a finite history.',
        'zh': '片段预序的理想是非空、向下封闭、任两个片段都被第三个延伸的片段集；理想按包含排序，所含片段相同的两个是同一历史（不用反对称性）。'
              '主理想是有限历史。对一个过程，片段是一个运行连同一界，一个片段延伸另一个，当其界更晚且两运行到较早之界一致；'
              '运行是它所经片段的理想，两运行的理想一个在另一个之下恰在两运行于每一界都一致之处，且没有运行的理想是有限历史。',
        'declarations': d('Ideals.Preorder', 'Ideals.Ideal', 'Ideals.Ideal.LE', 'Ideals.Ideal.Same', 'Ideals.idealOrder',
                          'Ideals.principal', 'Ideals.principal_le_iff', 'Ideals.principal_le_principal_iff',
                          'stretchOrder', 'Run.stretches', 'Run.stretches_le_iff', 'Run.stretches_not_principal'),
    },
    {
        'en': 'A reading of points is refutable where every point outside it has a stretch that no point of the reading '
              'passes through, and a point adheres to it where each of its stretches is a stretch of a point of the '
              'reading. A refutable reading holds, up to double negation, at every adhering point; a refutable superset '
              'so holds at every point adhering to the subset; where the reading is stable adhering is holding; and a '
              'point adhering while outside shows the reading is not refutable. For runs these are refutability and '
              'adherence at the runs\' ideals, so the laws of Becoming.Horizon on what a finite history refutes follow '
              'from them as their case of runs.',
        'zh': '点的读法可否证：其外每个点都有一个片段，读法内没有点经过它；点附着于读法：它的每个片段都是读法内某点的片段。'
              '可否证的读法在每个附着点上于双重否定下成立；可否证的超集在附着于子集的点上亦然；读法稳定时附着即成立；附着而在外的点显示读法不可否证。'
              '对运行，这就是在运行的理想上的可否证与附着，所以 Becoming.Horizon 关于有限历史所否证者的律作为其运行情形由此推出。',
        'declarations': d('Ideals.RefutableBy', 'Ideals.AdheresBy', 'Ideals.RefutableBy.not_not',
                          'Ideals.RefutableBy.adheres_least', 'Ideals.RefutableBy.adheres_iff',
                          'Ideals.not_refutableBy_of_adheres', 'Ideals.refutableBy_adheres_iff',
                          'refutable_iff_refutableBy', 'adheres_iff_adheresBy', 'Stretches.not_not',
                          'Stretches.adheres_least', 'Stretches.adheres_iff', 'Stretches.not_refutable_of_adheres',
                          'Stretches.refutable_adheres_iff'),
    },
    {
        'en': 'A class of ideals is closed where it is closed downward and under directed unions. It is closed exactly '
              'where it is the class of the ideals within a lower set of stretches; that set is unique and is the '
              'class\'s content, the stretches of its ideals. On runs, a reading holding every run adhering to it is the '
              'reading of the runs whose stretches lie in the content of its runs: it is made of tests, one for each '
              'stretch, read as propositions. A run lies in a closed class exactly where each of its stretches is a '
              'stretch of a history of the class.',
        'zh': '理想的类是闭的：它向下封闭且对有向并封闭。它闭恰在它是落在某个片段下集之内的理想之类之处；该集唯一，就是类的内容，即其理想的片段。'
              '在运行上，在每个附着于它的运行上成立的读法，是片段都落在其运行之内容中的运行的读法：它由测试构成，每个片段一个，读作命题。'
              '运行在闭类中，恰在它的每个片段都是类中某历史的片段之处。',
        'declarations': d('Ideals.Closed', 'Ideals.Lower', 'Ideals.Within', 'Ideals.Content',
                          'Ideals.closed_iff_within_principal', 'Ideals.closed_iff_lower', 'Ideals.lower_unique',
                          'Ideals.lower_iff_content', 'Ideals.content_lower', 'closed_iff_within_lower',
                          'Stretches.closed_runs'),
    },
    {
        'en': 'The hull of a class, the ideals each of whose stretches is a stretch of an ideal of the class, is its least '
              'closed superclass: closed, holding the class, unique, adding no stretch, and joint, any two stretches of '
              'an ideal of the hull being extended by one stretch of one ideal of the class. On runs, a run adheres to a '
              'reading exactly where its ideal lies in the hull of the reading\'s runs, that is, in every closed class of '
              'histories holding them, with no double negation.',
        'zh': '类的包，即每个片段都是类中某理想之片段的理想，是它最小的闭超类：闭、含该类、唯一、不添片段，且联合：包中理想的任两个片段被类中某一理想的某一片段延伸。'
              '在运行上，运行附着于读法，恰在它的理想落在读法之运行的包中之处，即落在每个含这些运行的历史闭类中，没有双重否定。',
        'declarations': d('Ideals.Hull', 'Ideals.hull_contains', 'Ideals.hull_closed', 'Ideals.hull_least',
                          'Ideals.hull_content', 'Ideals.hull_unique', 'Ideals.hull_joint', 'runClass',
                          'adheres_iff_hull', 'Stretches.adheres_iff_closed', 'Stretches.adherence_unique',
                          'Stretches.adheres_content', 'Stretches.adheres_joint'),
    },
    {
        'en': 'A refutable class is closed up to double negation, and a closed class is refutable where a history known '
              'not to lie within it shows a stretch outside. Asked of every order and class each step is exactly '
              'double-negation elimination, and asked of every process too, with witnesses on the process of (): not '
              'being refuted by any finite stretch is not belonging, and a history known not to lie within a closed '
              'class does not thereby show the stretch at which it leaves. A refutable class of histories is refutable '
              'at runs, and asked of every process a refutable reading holds at every run adhering to it exactly under '
              'double-negation elimination.',
        'zh': '可否证的类于双重否定下是闭的；闭类可否证，在已知不在其内的历史显示一个外面的片段之处。对每个序与类要求时，每一步恰是双重否定消去；'
              '对每个过程要求时亦然，见证在 () 的过程上：未被任何有限片段否证并不就是属于；已知不在闭类之内的历史并不因此显示它离开的片段。'
              '可否证的历史类在运行上可否证；对每个过程要求时，可否证读法在每个附着运行上成立恰是双重否定消去。',
        'declarations': d('Ideals.Refutable', 'Ideals.Refutable.closed', 'Ideals.Closed.refutable_iff',
                          'Ideals.within_refutable_iff', 'Ideals.refutable_closed_iff', 'Ideals.closed_refutable_iff',
                          'Stretches.refutable_of_class', 'Stretches.within_refutable', 'Stretches.unitCut',
                          'Stretches.refutable_closed_iff', 'Stretches.closed_refutable_iff', 'refutable_holds_iff'),
    },
    {
        'en': 'The ideals avoiding a set of stretches form a closed class, the only closed class holding exactly the '
              'finite histories that avoid the set, and refutable where every ideal failing to avoid it holds a stretch '
              'of it; on runs, a run adhering to the runs that avoid the set avoids it. These are the safety classes.',
        'zh': '避开一个片段集的理想构成闭类，是恰含避开该集之有限历史的唯一闭类；在每个不避开它的理想都含其一个片段之处可否证；'
              '在运行上，附着于避开该集之运行的运行也避开它。这些是安全性的类。',
        'declarations': d('Ideals.Avoids', 'Ideals.avoids_iff_within', 'Ideals.avoids_closed', 'Ideals.avoids_unique',
                          'Ideals.avoids_refutable_of_found', 'Stretches.avoids_adheres', 'Stretches.avoids_runs',
                          'Stretches.avoids_refutable'),
    },
    {
        'en': 'A lower set of stretches, with the order it inherits, has as its ideals exactly the ideals within it, by '
              'lifting and restricting, the order kept; on runs, the histories of the set\'s order are the process\'s '
              'histories within it, and two runs within it are ordered there exactly where they agree at every horizon.',
        'zh': '片段的下集连同所继承的序，其理想恰是落在其内的理想，经提升与限制，序不变；在运行上，该集之序的历史就是过程落在其内的历史，'
              '落在其内的两个运行在那里有序，恰在它们于每一界一致之处。',
        'declarations': d('Ideals.Preorder.restrict', 'Ideals.Ideal.restrict', 'Ideals.Ideal.lift', 'Ideals.lift_within',
                          'Ideals.lift_restrict', 'Ideals.restrict_lift', 'Ideals.lift_le_iff',
                          'Stretches.inherited_histories', 'Stretches.within_order_iff'),
    },
    {
        'en': 'The ideals are directed-complete; the compact ones are exactly the finite histories; a monotone map of '
              'stretches into a directed-complete order extends to a continuous map of ideals, unique up to the '
              'target\'s equivalence; a compact basis that generates fixes its completion up to an equivalence the basis '
              'fixes; and the readings "lies above this stretch" tell ideals apart. On runs: no run is compact, a '
              'continuous reading of the histories is fixed at every run by its values on finite histories, finite '
              'stretches tell runs apart, the finite histories are a compact basis, and the histories are the '
              'completion of the stretches.',
        'zh': '理想是有向完备的；紧的恰是有限历史；片段到有向完备序的单调映射延拓为理想的连续映射，在目标的等价下唯一；生成的紧基在基所固定的等价下固定其完备化；'
              '读法“在此片段之上”区分理想。在运行上：没有运行是紧的；历史的连续读法在每个运行上由其在有限历史上的值固定；有限片段区分运行；'
              '有限历史是紧基；历史是片段的完备化。',
        'declarations': d('Ideals.DirectedComplete', 'Ideals.idealComplete', 'Ideals.Compact',
                          'Ideals.compact_iff_principal', 'Ideals.Monotone', 'Ideals.Continuous', 'Ideals.extend',
                          'Ideals.unique_continuous_extension', 'Ideals.CompactBasis', 'Ideals.OrderEquivalence',
                          'Ideals.principal_basis', 'Ideals.unique_basis_representation', 'Ideals.above',
                          'Ideals.extend_above_iff', 'Ideals.above_readings_separate', 'Stretches.run_not_compact',
                          'Stretches.run_reading_unique', 'Stretches.runs_told_apart', 'Stretches.finite_basis',
                          'Stretches.histories_representation'),
    },
    {
        'en': 'A history settles where one of its stretches reaches the latest horizon among them, and goes on where it '
              'has stretches beyond every horizon. One that settles is a finite history; one that goes on, with a '
              'stretch beyond each horizon picked, is the history of the run read off the picks. So, for every process, '
              'a history that settles, or goes on with its stretches picked, is a finite history or a run; a finite '
              'history settles and a run\'s history goes on. Telling, of every history of the process of () cut at a '
              'Boolean sequence\'s first true, whether it settles or goes on is exactly the limited principle of '
              'omniscience: telling whether a history ends is deciding whether it changes again.',
        'zh': '历史止定：它的某个片段达到其中最晚之界；历史继续：它有超出每一界的片段。止定的是有限历史；继续的，挑出超出每一界的片段，就是由所挑者读出之运行的历史。'
              '所以对每个过程，止定的、或挑出片段而继续的历史，是有限历史或运行；有限历史止定，运行的历史继续。'
              '对 () 的过程中在布尔序列第一个真处截断的每个历史，判定它止定还是继续，恰是有限全知原则：判定历史是否终结，就是判定它是否还会变化。',
        'declarations': d('Stretches.Settles', 'Stretches.GoesOn', 'Stretches.settles_principal', 'Stretches.pickedRun',
                          'Stretches.goesOn_run', 'Stretches.classification', 'Stretches.principal_settles',
                          'Stretches.run_goesOn', 'Stretches.cut', 'Stretches.cut_decided_iff_lpo', 'HistoryIdeals.cut',
                          'HistoryIdeals.cut_decided_iff_lpo'),
    },
    {
        'en': 'Words are ordered by prefix; a sequence is the ideal of its initial words. A history, finite or '
              'infinite, has an ideal below another\'s exactly where it is a prefix of it, and the same words make the '
              'same history; an ideal of words that settles, or goes on with its words picked, is a history. For the '
              'process of all sequences the runs\' histories are these, in order, sameness and prefix-closed languages. '
              'A prefix-closed language is a lower set of words, so its histories form a closed class; the finite '
              'histories with the infinite histories of a property are not refutable where some sequence lies outside '
              'it, recurrence among them.',
        'zh': '词按前缀排序；序列是其初始词的理想。有限或无限的历史，其理想在另一个之下，恰在它是另一个的前缀之处；同样的词构成同一历史；'
              '止定的、或挑出词而继续的词理想是历史。对所有序列构成的过程，运行的历史就是这些，在序、相同与前缀封闭语言上皆然。'
              '前缀封闭语言是词的下集，所以其历史构成闭类；有限历史连同某性质的无限历史，在有序列落在该性质之外处不可否证，复现是其一例。',
        'declarations': d('HistoryIdeals.prefixOrder', 'HistoryIdeals.traceIdeal', 'HistoryIdeals.History',
                          'HistoryIdeals.historyIdeal', 'HistoryIdeals.history_le_iff',
                          'HistoryIdeals.historyIdeal_same_iff', 'HistoryIdeals.classification',
                          'HistoryIdeals.sequence_stretch_iff', 'Stretches.sequences_le_iff',
                          'Stretches.sequences_same_iff', 'Stretches.sequences_within_iff',
                          'HistoryIdeals.prefixClosed_iff_lower', 'HistoryIdeals.history_within_iff',
                          'HistoryIdeals.FiniteOr', 'HistoryIdeals.finiteOr_not_refutable',
                          'HistoryIdeals.finiteOr_recurs_not_refutable'),
    },
    {
        'en': 'Instance (periphery, own checker): the completion package\'s IdealWarrant, CompletionRole and '
              'HistoryIdeals read as instances, a poset\'s order the core\'s order of stretches and its ideals, classes, '
              'content and hull the core\'s. W1\'s lower bases, W2\'s least hull and W2a\'s prohibitions follow with '
              'empty axiom reports; W1\'s equivalence of finite refutability and Scott closure, A2, A2a, A3 and A4 '
              'follow with the classical and extensionality steps each needs named.',
        'zh': '实例（外围，自有检查器）：完成包的 IdealWarrant、CompletionRole 与 HistoryIdeals 读作实例，偏序的序是核心的片段序，其理想、类、内容与包是核心的。'
              'W1 的下基、W2 的最小包与 W2a 的禁止由此推出，公理报告为空；W1 中有限可否证与 Scott 闭的等价、A2、A2a、A3 与 A4，连同各自所需的经典与外延步骤而推出。',
        'declarations': d('IdealsCorrespondence.toCore', 'IdealsCorrespondence.finiteRefutable_iff_refutable',
                          'IdealsCorrespondence.scottClosed_iff_closed', 'IdealsCorrespondence.scottHull_iff_hull',
                          'IdealsCorrespondence.scottClosed_iff_lower_basis_by_core',
                          'IdealsCorrespondence.hull_least_by_core',
                          'IdealsCorrespondence.respects_iff_admits_avoiding_by_core',
                          'IdealsCorrespondence.finiteRefutable_iff_scottClosed_by_core',
                          'IdealsCorrespondence.unique_continuous_extension_by_core',
                          'IdealsCorrespondence.positive_reading_membership_by_core',
                          'IdealsCorrespondence.unique_basis_representation_by_core',
                          'IdealsCorrespondence.ideal_classification_by_core',
                          'IdealsCorrespondence.history_order_iff_by_core'),
    },
]


def module_names(path):
    return {x['name'] for x in cb.declarations((ROOT / path).read_bytes())}


core_names = module_names(IDEALS) | module_names(HISTORY)
corr_names = module_names(CORR)
named = [x for law in laws for x in law['declarations']]
missing = [x for x in named if x not in core_names | corr_names]
assert not missing, missing
ideals_decls = sorted(x for x in named if x in module_names(IDEALS))
history_decls = sorted(x for x in named if x in module_names(HISTORY))
corr_decls = sorted(x for x in named if x in corr_names)

horizon = d('Run.AgreeUpTo', 'Refutable', 'Adheres', 'Refutable.not_not', 'Refutable.adheres_least',
            'Refutable.adheres_iff', 'not_refutable_of_adheres', 'refutable_adheres_iff', 'Adheres.adheres',
            'Sequences.process', 'Sequences.agree_iff', 'Markov', 'refutable_passes_iff_markov')
languages = d('HistoryLanguages.PrefixClosed')
change = d('LPO')

record = {
    'schema_version': 2,
    'id': 'a-history-read-off-its-finite-stretches',
    'title': {'zh': '从有限片段读出的历史', 'en': 'A history read off its finite stretches'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'For every process, its histories are the ideals of the order of its finite stretches. Adhering is the '
              'least closed class; refutable and closed classes pass into each other up to a step that, asked of every '
              'process, is exactly double-negation elimination.',
        'zh': '对每个过程，其历史是其有限片段之序的理想。附着是最小的闭类；可否证类与闭类互相转换，差一步，而对每个过程要求时这一步恰是双重否定消去。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom. The order is any preorder (antisymmetry is not used, so the same history is two-way '
               'inclusion); the process and the readings are arbitrary. The classification takes the decision of '
               'settling and the picked stretches as data. Double-negation elimination is the hypothesis of one '
               'direction of refutable_closed_iff, closed_refutable_iff and refutable_holds_iff, and the limited '
               'principle of omniscience of one direction of cut_decided_iff_lpo. The instance module uses Lean\'s '
               'standard axioms where its declarations name them.',
         'zh': '不加公理。序是任意预序（不用反对称性，所以同一历史是双向包含）；过程与读法任意。分类把止定的判定与所挑片段作为数据。'
               '双重否定消去是 refutable_closed_iff、closed_refutable_iff 与 refutable_holds_iff 一个方向的假设，有限全知原则是 '
               'cut_decided_iff_lpo 一个方向的假设。实例模块在其声明注明处用 Lean 的标准公理。'},
    ],
    'does_not_show': [
        {'en': 'Which readings of an actual unfolding are refutable or closed: that depends on the process they are read '
               'on; the laws say what each gives.',
         'zh': '实际展开的哪些读法可否证或闭：这取决于读它们的过程；本律说各自给出什么。',
         'kind': 'scope'},
        {'en': 'That every refutable class is closed, or every closed class refutable, without a decision: asked of every '
               'process each is exactly double-negation elimination.',
         'zh': '不经判定，每个可否证类都闭、或每个闭类都可否证：对每个过程要求时，每一个恰是双重否定消去。',
         'kind': 'non-implication', 'witness': 'Becoming.Stretches.refutable_closed_iff'},
        {'en': 'That every history settles or goes on: asked of the cut histories of the process of () it is exactly the '
               'limited principle of omniscience.',
         'zh': '每个历史止定或继续：对 () 的过程的截断历史要求时，恰是有限全知原则。',
         'kind': 'non-implication', 'witness': 'Becoming.Stretches.cut_decided_iff_lpo'},
        {'en': 'Boolean tests from the propositional tests a closed reading is made of: that needs each stretch\'s test '
               'decided (compare refutable_passes_iff_markov).',
         'zh': '由闭读法所含的命题测试得到布尔测试：这需要判定每个片段的测试（参见 refutable_passes_iff_markov）。',
         'kind': 'scope'},
        {'en': 'What a finite stretch verifies, the open classes of histories, is not stated on this order.',
         'zh': '有限片段所证实者，即历史的开类，未在此序上陈述。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': HISTORY, 'detail': {
        'en': 'On the process of (), the histories passing through the stretch at horizon 1, or all where a proposition '
              'holds, are refutable once it is not refuted, and closed only if it holds (refutable_closed_iff); the '
              'histories within the stretches at horizon 0 are closed, and the history reaching horizon 1 where the '
              'proposition holds shows no refuting stretch unless it holds (unitCut, closed_refutable_iff). The finite '
              'histories with the infinite histories of a property are not refutable (finiteOr_not_refutable).',
        'zh': '在 () 的过程上，经过界 1 处片段的历史，或命题成立时的所有历史，在命题未被否证时可否证，但只有命题成立时才闭（refutable_closed_iff）；'
              '落在界 0 片段之内的历史是闭的，而命题成立时到达界 1 的历史，除非命题成立，不显示否证片段（unitCut、closed_refutable_iff）。'
              '有限历史连同某性质的无限历史不可否证（finiteOr_not_refutable）。'}}],
    'standard_boundaries': ['no-ethical-premise-core-axiom-free', 'no-evaluation', 'discrete-steps',
                            'formal-not-empirical', 'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': 'Machine-checked by the consolidated Lean 4.29.1 checker (receipt CORE_ID): Becoming.Ideals has {I} '
              'theorems and Becoming.HistoryIdeals {H}, every declaration with an empty axiom report; the checker '
              'verifies core purity. The periphery instance IdealsCorrespondence is checked by its own checker (Lean '
              '4.30.0-rc2, receipt CORR_ID): {C} theorems, {E} of its {D} declarations with empty axiom reports and the '
              'rest with standard axioms only; the four package modules match the completion package receipt. Author '
              'self-review in study section SECTION; not independently reviewed.',
        'zh': 'Lean 4.29.1 合并检查器实查（回执 CORE_ID）：Becoming.Ideals 有 {I} 项定理，Becoming.HistoryIdeals 有 {H} 项，'
              '每个声明公理报告为空；检查器并核对核心纯净。外围实例 IdealsCorrespondence 由其检查器实查'
              '（Lean 4.30.0-rc2，回执 CORR_ID）：{C} 项定理，{D} 个声明中 {E} 个公理报告为空，其余只用标准公理；'
              '四个包模块与完成包回执一致。作者自审见研究第 SECTION 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'What a finite stretch verifies (the open classes) on the order of stretches; an independent review.',
        'zh': '有限片段所证实者（开类）在片段之序上；独立审查。',
    },
    'correspondence': {
        'en': 'Decision D45 (4) of 19 October 2026 joined IdealWarrant with CompletionRole and HistoryIdeals as one core '
              f'family under structural names (board item A4-L). Ren, 19 October 2026: “{REN}” (provenance, not '
              'warrant); his “(a)” of 16 October had kept IdealWarrant outside the spine (study section 153). The '
              'ideals of the order of finite stretches are the ideal completion of domain theory (Abramsky and Jung '
              '1994); on runs the closed classes are the safety properties of Alpern and Schneider (1985), and '
              'refutation from finite data is that of Kelly (1996), as what-a-finite-history-refutes notes. '
              'Classically finite refutability and Scott closure coincide (IdealWarrant\'s W1); constructively each '
              'direction is a step that, asked of every order and class, is exactly double-negation elimination. '
              'Readings (the AI\'s): not being refuted by any finite stretch is not belonging; a history known not to '
              'lie within a closed class does not thereby show the stretch at which it leaves; telling whether a '
              'history ends is deciding whether it changes again.',
        'zh': '2026年10月19日的决定 D45 (4) 把 IdealWarrant 与 CompletionRole、HistoryIdeals 合为结构命名下的一个核心族（工作板条目 A4-L）。'
              f'Ren，2026年10月19日：“{REN}”（来历，不是根据）；他10月16日的“(a)”曾把 IdealWarrant 留在脊柱外（研究第153节）。'
              '有限片段之序的理想就是域论的理想完备化（Abramsky 与 Jung 1994）；在运行上，闭类是 Alpern 与 Schneider（1985）的安全性质，'
              '由有限数据否证是 Kelly（1996）的否证，如 what-a-finite-history-refutes 所注。经典地，有限可否证与 Scott 闭一致（IdealWarrant 的 W1）；'
              '构造地，每个方向差一步，对每个序与类要求时恰是双重否定消去。读法（AI 的）：未被任何有限片段否证并不就是属于；'
              '已知不在闭类之内的历史并不因此显示它离开的片段；判定历史是否终结，就是判定它是否还会变化。',
    },
    'canonical_source': IDEALS,
    'aliases': ['a history read off its finite stretches', '从有限片段读出的历史', 'ideals of finite stretches',
                '有限片段的理想', 'closed classes of histories', '历史的闭类', 'Becoming.Stretches.classification',
                'Becoming.Stretches.refutable_closed_iff', 'Becoming.Stretches.cut_decided_iff_lpo'],
    'dependencies': [
        {'id': 'what-a-finite-history-refutes', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Becoming.Horizon\'s Run.AgreeUpTo, Refutable and Adheres: the order of stretches is '
                          'agreement up to the earlier horizon, and Horizon\'s laws are derived here as the case of runs.',
                    'zh': '复用 Becoming.Horizon 的 Run.AgreeUpTo、Refutable 与 Adheres：片段之序是到较早之界的一致，Horizon 的律在此作为运行情形推出。'},
         'interface': {
             'output': {'en': 'Agreement up to a horizon, and refutability and adherence of readings of runs.',
                        'zh': '到一界的一致，以及运行读法的可否证与附着。'},
             'input': {'en': 'The order of stretches, and the readings of runs the laws of ideals are read on.',
                       'zh': '片段之序，以及理想之律所读的运行读法。'},
             'conditions': {'en': 'None.', 'zh': '无。'},
             'evidence': HORIZON}},
    ],
    'related': [
        {'id': 'becoming-finite-horizon',
         'detail': {'en': 'There no finite prefix decides the whole-run classification in Renewable; here what a finite '
                          'stretch refutes in every process, as the closed classes of its histories.',
                    'zh': '那里在 Renewable 中没有有限前缀决定整段分类；这里是每个过程中有限片段所否证者，即其历史的闭类。'}},
    ],
    'references': [
        {'path': IDEALS, 'role': 'proof', 'declarations': ideals_decls},
        {'path': HISTORY, 'role': 'proof', 'declarations': history_decls},
        {'path': HORIZON, 'role': 'proof', 'declarations': horizon},
        {'path': LANGUAGES, 'role': 'proof', 'declarations': languages},
        {'path': CHANGE, 'role': 'proof', 'declarations': change},
        {'path': CORR, 'role': 'proof', 'declarations': corr_decls},
        {'path': f'{FORMAL}/IdealWarrant.lean', 'role': 'proof'},
        {'path': f'{FORMAL}/CompletionRole.lean', 'role': 'proof'},
        {'path': f'{FORMAL}/HistoryIdeals.lean', 'role': 'proof'},
        {'path': CORE_RECEIPT, 'role': 'receipt'},
        {'path': CORR_RECEIPT, 'role': 'receipt'},
        {'path': PACKAGE_RECEIPT, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-19-integrate-all.md', 'role': 'provenance'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md',
         'role': 'provenance'},
    ],
    'proof_bindings': [{'source': f'{PKG}/Becoming/{m}.lean', 'receipt': CORE_RECEIPT,
                        'sha256_pointer': f'/source_sha256/Becoming.{m}', 'success_pointer': '/status',
                        'success_value': 'passed'}
                       for m in ('Ideals', 'HistoryIdeals', 'Horizon', 'HistoryLanguages', 'Change')]
                      + [{'source': f'{FORMAL}/{m}.lean', 'receipt': CORR_RECEIPT,
                          'sha256_pointer': f'/source_sha256/{m}', 'success_pointer': '/status',
                          'success_value': 'passed'}
                         for m in ('IdealsCorrespondence', 'IdealWarrant', 'CompletionRole', 'HistoryIdeals')],
    'history': [{
        'en': f'19 October 2026: added (A4-L), on decision D45 (4) and Ren\'s “{REN}” (19 October); study section '
              f'{section}.',
        'zh': f'2026年10月19日：新增（A4-L），依决定 D45 (4) 与 Ren 的“{REN}”（10月19日）；研究第 {section} 节。',
    }],
}

# The counts in the validation scope come from the two receipts.
mods = {m['module']: m for m in core['modules']}
target = next(m for m in corr['modules'] if m['module'] == 'IdealsCorrespondence')
counts = {'I': int(mods['Becoming.Ideals']['theorems']), 'H': int(mods['Becoming.HistoryIdeals']['theorems']),
          'C': int(target['theorems']), 'D': len(target['declarations']),
          'E': sum(1 for x in target['declarations'] if not target['axiom_dependencies'].get(x['name']))}
assert not any(mods[m]['axiom_dependencies'].get(x['name']) for m in ('Becoming.Ideals', 'Becoming.HistoryIdeals')
               for x in mods[m]['declarations']), 'core axiom report not empty'
for lang in ('en', 'zh'):
    text = record['validation_scope'][lang].replace('CORE_ID', core_id).replace('CORR_ID', corr_id)
    text = text.replace('SECTION', section)
    for key, value in counts.items():
        text = text.replace('{' + key + '}', str(value))
    assert '{' not in text, text
    record['validation_scope'][lang] = text
assert len(record['statement']['en']) <= 300, len(record['statement']['en'])

for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
by_path = {ref['path']: ref for ref in record['references']}
for b in record['proof_bindings']:
    receipt = core if b['receipt'] == CORE_RECEIPT else corr
    key = b['sha256_pointer'].rsplit('/', 1)[-1]
    assert receipt['source_sha256'][key] == by_path[b['source']]['sha256'], key

taken = {}
for f in glob.glob(str(ROOT / 'theories/becoming/results/records/*.json')):
    other = json.loads(Path(f).read_text())
    if other.get('id') == record['id']:
        continue
    for alias in [other.get('id')] + other.get('aliases', []):
        if isinstance(alias, str):
            taken[alias.casefold()] = other.get('id')
clash = {a: taken[a.casefold()] for a in [record['id']] + record['aliases'] if a.casefold() in taken}
assert not clash, clash

out = ROOT / 'theories/becoming/results/records/a-history-read-off-its-finite-stretches.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out, counts)
