#!/usr/bin/env python3
"""Write the record what-finitely-many-labels-fix for L2: python3 -B make_record.py RECEIPT_ID

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/Labels.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.Labels'] == sha, 'receipt does not bind the current bytes'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/what-an-extrapolation-given-nothing-fixes.json').read_text())['family']
SECTION = int(re.search(r'^## (\d+)\. What finitely many labels fix \(L2\)$', (ROOT / '_process/research/2026-10-05-'
                        'generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md').read_text(), re.M).group(1))
WORDS = ('"alright, generally agree, please make your own pareto frontier decisions, and push the frontier - words are '
         'important, but i think you are capable"')


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'A table of labelled names: a name is a finite future through the map, latest first, and a label a value '
              'of the feature; the extrapolation given a table unrolls the extrapolation by elimination over the lasso '
              'candidates and proposes the label of the first entry whose name the proposed future begins with.',
        'zh': '带标签的名字之表：名字是有限的经映射的未来（最近的在前），标签是特征的一个值；被给予表的外推展开套索候选上的逐除外推，'
              '提出所提议之未来以其名字开头的第一个条目的标签。',
        'declarations': d('Learning.prefix_map', 'Identification.firstFit_mem', 'Identification.firstFit_map',
                          'Learnable.Begins', 'Learnable.decBegins', 'Learnable.byTable',
                          'Learnable.entryOf', 'Learnable.tableOf', 'Learnable.length_map', 'Learnable.mem_map_of',
                          'Learnable.tableOf_length', 'Learnable.entryOf_name_length', 'Learnable.tableOf_names',
                          'Learnable.begins_entryOf'),
    },
    {
        'en': 'In a world a list of N holds, where configurations with the same future through the map have features '
              'agreeing from some step on, the extrapolation given the table of the N configurations as many steps on '
              'as the list is long, each named by its first N - 1 values through the map and labelled with its '
              'feature, rests in accord with the feature along every orbit and every run, from the bound of the '
              'extrapolation given nothing on; so a feature is learnable exactly where the extrapolation given some '
              'table of at most N labelled names of N - 1 values learns it.',
        'zh': '在由 N 个构形的列表容纳的世界中，经映射未来相同的构形其特征自某步起一致之处，被给予世界之表（列表长度那么多步之后的 N '
              '个构形，各以其经映射的前 N - 1 个值命名、以其特征为标签）的外推，自不被给予任何东西的外推之界起，沿每条轨道与每次运行'
              '与特征相合而静止；所以一个特征可学，恰当被给予某个至多 N 个、各 N - 1 个值的带标签名字之表的外推学得它。',
        'declarations': d('Learnable.table_rests', 'Learnable.learnable_iff_table', 'LearnableRuns.table_rests',
                          'LearnableRuns.learnable_iff_table'),
    },
    {
        'en': 'Every value the feature takes from the step an extrapolation given a table rests on is a label of an entry '
              'of the table; where the law leaves every configuration unchanged, every value the feature takes is.',
        'zh': '自被给予表的外推静止之步起，特征所取的每个值都是表中某条目的标签；律使每个构形不变之处，特征所取的每个值都是。',
        'declarations': d('Learnable.label_of_rests', 'Learnable.labels_of_still', 'LearnableRuns.labels_of_still'),
    },
    {
        'en': 'Where the map also carries the feature, every feature is learned by the extrapolation given nothing in a '
              'world a list holds, from the bound on, along every orbit and every run, and unrolled it proposes the '
              'feature at every step ahead: the labels before the bound fix every later one.',
        'zh': '映射也带着特征之处，在由一个列表容纳的世界中，每个特征都由不被给予任何东西的外推自界起、沿每条轨道与每次运行学得；展开后它提出此后每一步的特征：'
              '界之前的标签确定此后的每一个。',
        'declarations': d('Learnable.rests_with_labels', 'Learnable.ahead_with_labels', 'LearnableRuns.rests_with_labels',
                          'LearnableRuns.ahead_with_labels'),
    },
]

record = {
    'schema_version': 2,
    'id': 'what-finitely-many-labels-fix',
    'title': {
        'zh': '有限多个标签所确定者',
        'en': 'What finitely many labels fix',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'In a world a list of N holds, a feature is learnable through the map exactly where an extrapolation given '
              'at most N labelled names of N - 1 values learns it; its labels include every value the feature takes once '
              'it rests; where the map carries the feature, labels before a bound fix every later one.',
        'zh': '在由 N 个构形的列表容纳的世界中，一个特征经映射可学，恰当被给予至多 N 个、各 N - 1 个值的带标签名字的外推学得它；'
              '其标签含特征在它静止后所取的每个值；映射带着特征之处，界之前的标签确定此后的每一个。',
    },
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. A determined law; a list holding the world (or the orbit, for the labels along the course); '
              'values through the map compared decidably, and the feature\'s values too where the map carries it.',
        'zh': '不加公理。一个确定之律；一个容纳世界（或就沿进程的标签而言，轨道）的列表；经映射的值可判定地比较，映射带着特征之处其值亦然。',
    }],
    'does_not_show': [
        {'en': 'An extrapolation that finds the table: the table of the world is built from the world, the law and the '
               'feature, as fromWorld is.',
         'zh': '找到这张表的外推：世界之表由世界、律与特征构成，如 fromWorld。',
         'kind': 'scope'},
        {'en': 'That names of fewer than N - 1 values, or fewer than N entries, fail in some world of N configurations '
               '(for telling configurations apart N - 1 is exact, Law.sameFuture_classes_exact; for the extrapolation '
               'given a table it is not stated); undetermined processes; probabilistic or approximate learning.',
         'zh': '少于 N - 1 个值的名字或少于 N 个条目在某个 N 构形的世界中失败（就区分构形而言 N - 1 是精确的，Law.sameFuture_classes_exact；'
               '就被给予表的外推而言未陈述）；不确定的过程；概率的或近似的学习。',
         'kind': 'scope'},
    ],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 25 declarations of '
              'Becoming.Labels, 20 of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {SECTION}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.Labels 的 25 项声明（20 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {SECTION} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Whether N - 1 values and N entries are needed for the extrapolation given a table; a table found rather '
              'than given; undetermined processes; an independent review.',
        'zh': '被给予表的外推是否需要 N - 1 个值与 N 个条目；找到而不是被给予的表；不确定的过程；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, Learning) named "learning a target from finitely many of its '
              'values, given part of a reading of the future rather than the whole". Ren, 18 October 2026: ' + WORDS +
              ' (provenance, not warrant); the AI chose the item. A table of labelled names is the finite part of the '
              'reading that suffices; the labels along the course are feedback the map carries.',
        'zh': '本章开放纲领（第 8.2 节，学习）列出“learning a target from finitely many of its values, given part of a reading '
              'of the future rather than the whole”。Ren，2026年10月18日：' + WORDS + '（来历，不是根据）；此项由 AI 选定。带标签'
              '名字之表是读法中足够的有限部分；沿进程的标签是映射所带的反馈。',
    },
    'canonical_source': SRC,
    'aliases': ['what finitely many labels fix', '有限多个标签所确定者', 'table of labelled names', '带标签名字之表',
                'learnable from finitely many labels', '从有限多个标签可学', 'labels along the course', '沿进程的标签'],
    'dependencies': [],
    'related': [
        {'id': 'what-an-extrapolation-given-nothing-fixes',
         'detail': {'en': 'There a learnable feature is a reading of the future, a function on whole futures; here a '
                          'finite part of it, at most N labelled names of N - 1 values, suffices.',
                    'zh': '那里可学特征是对未来的读法，即整个未来上的函数；这里其有限部分（至多 N 个、各 N - 1 个值的带标签名字）就足够。'}},
        {'id': 'learnable-through-registration',
         'detail': {'en': 'There learnability is characterized with an extrapolation built from the law (fromLaw); here '
                          'the extrapolation given a finite table learns every learnable feature, and where the map '
                          'carries the feature along the course every feature is learned given nothing.',
                    'zh': '那里以依律所建之外推（fromLaw）刻画可学性；这里被给予有限之表的外推学得每个可学特征，'
                          '映射沿进程带着特征之处，每个特征都不被给予任何东西而学得。'}},
        {'id': 'identification-where-bounded',
         'detail': {'en': 'Moore\'s bound N - 1 (Law.sameFuture_iff_within) gives the length of the names.',
                    'zh': 'Moore 之界 N - 1（Law.sameFuture_iff_within）给出名字的长度。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.Labels',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (L2), on Ren\'s ' + WORDS + f', the AI choosing the item; study section {SECTION}; '
              'the reading is D40 of DELEGATED-CHOICES, extended with L2.',
        'zh': '2026年10月18日：新增（L2），按 Ren 的' + WORDS + f'，此项由 AI 选定；研究第 {SECTION} 节；读法是 DELEGATED-CHOICES '
              '的 D40，以 L2 扩展。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/what-finitely-many-labels-fix.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
