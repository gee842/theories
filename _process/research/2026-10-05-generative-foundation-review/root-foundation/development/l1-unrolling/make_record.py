#!/usr/bin/env python3
"""Write the record what-an-extrapolation-given-nothing-fixes for L1: python3 -B make_record.py RECEIPT_ID

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/Unrolling.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.Unrolling'] == sha, 'receipt does not bind the current bytes'


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'Unrolled on its own proposals, an extrapolation that proposes the course\'s value at every step from '
              'some step on proposes the course at every step ahead; in every world a list holds, from the '
              'identification bound on, the extrapolation by elimination over the lasso candidates, given nothing, '
              'so proposes the value through the map at every step ahead, along orbits and along runs.',
        'zh': '在自身的提议上展开，自某步起每步都提议路程之值的外推，对前方每一步都提议路程；在每个由一个列表容纳的世界中，'
              '自辨识之界起，不被给予任何东西、对套索候选逐一排除的外推，由此对前方每一步提议经映射之值，沿轨道亦沿运行。',
        'declarations': d('Learning.extendBy', 'Learning.extendBy_of', 'Learning.unroll', 'Learning.ahead',
                          'Learning.unroll_prefix', 'Learning.ahead_accords', 'Learnable.ahead_fixes',
                          'LearnableRuns.ahead_fixes'),
    },
    {
        'en': 'A feature read off the future through the map is learned by the extrapolation given that reading, '
              'from the identification bound on, and from some step on where it is such a reading from some step on.',
        'zh': '从经映射之未来读出的特征，由被给予该读法的外推学得，自辨识之界起；在它自某步起才是这样的读法之处，自某步起。',
        'declarations': d('Learnable.ReadOff', 'Learnable.reading', 'Learnable.reading_rests',
                          'Learnable.reading_rests_from'),
    },
    {
        'en': 'In a world a list holds, a feature is learnable through the map exactly where some reading of futures, '
              'respecting values at each step, is the feature from some step on along every orbit (and along every '
              'run); returning configurations whose features agree from some step on have equal features.',
        'zh': '在由一个列表容纳的世界中，一个特征经映射可学，恰当某个对未来的读法（逐步尊重值）自某步起沿每条轨道（亦沿每次运行）'
              '就是该特征；特征自某步起一致的回返构形，其特征相等。',
        'declarations': d('Learnable.eq_of_returns', 'Learnable.readAt', 'Learnable.fromWorld',
                          'Learnable.fromWorld_respects', 'Learnable.reads_of_agree', 'Learnable.learnable_iff_reading',
                          'LearnableRuns.future_eq', 'LearnableRuns.learnable_iff_reading'),
    },
    {
        'en': 'Given nothing, no extrapolation rests in accord with every learnable feature: in a one-configuration '
              'world the features true and false are each learned given their reading, with the same prefixes.',
        'zh': '不被给予任何东西，没有外推与每个可学特征相合而静止：在只有一个构形的世界中，特征 true 与 false 各自在被给予其读法时被学得，'
              '而前缀相同。',
        'declarations': d('Learnable.given_nothing_not_every', 'LearnableRuns.given_nothing_not_every'),
    },
]

record = {
    'schema_version': 2,
    'id': 'what-an-extrapolation-given-nothing-fixes',
    'title': {
        'zh': '不被给予任何东西的外推所确定者',
        'en': 'What an extrapolation given nothing fixes',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': 'F11',
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'Given nothing, a prefix fixes the whole future through the map in every world a list holds; what a '
              'learnable feature adds to it is exactly a reading of that future, so no extrapolation given nothing '
              'learns every learnable feature.',
        'zh': '不被给予任何东西，在每个由一个列表容纳的世界中，一个前缀确定经映射的整个未来；一个可学特征对它所加的，恰是对那个未来的'
              '一个读法，所以没有不被给予任何东西的外推学得每个可学特征。',
    },
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. A list holding the orbit (or the world); values through the map compared decidably; a reading '
              'respecting values at each step (no function extensionality is assumed); for the exact theorem a '
              'fallback value of the feature, read nowhere along an orbit.',
        'zh': '不加公理。一个容纳轨道（或世界）的列表；经映射之值可判定地比较；一个逐步尊重值的读法（不假设函数外延性）；'
              '对精确定理，一个特征的备用值，沿任何轨道都不被读到。',
    }],
    'does_not_show': [
        {'en': 'An extrapolation that finds the reading: the reading of the first direction of the exact theorem is '
               'given the world, the law and the feature (fromWorld).',
         'zh': '找到读法的外推：精确定理第一方向的读法被给予世界、律与特征（fromWorld）。',
         'kind': 'scope'},
        {'en': 'Learning a feature from finitely many of its values; undetermined processes; rates beyond the stated '
               'bound.',
         'zh': '从特征的有限个值学习它；不确定的过程；超出所述之界的速率。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': SRC, 'detail': {
        'en': 'One configuration, one value through the map: the features true and false are each learnable, and no '
              'single extrapolation rests in accord with both (given_nothing_not_every).',
        'zh': '一个构形、经映射一个值：特征 true 与 false 各自可学，而没有单一外推与两者相合而静止（given_nothing_not_every）。',
    }}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 22 declarations of '
              'Becoming.Unrolling, 15 of them theorems, have empty axiom reports; the checker verifies core purity. '
              'Author self-review in study section 173; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.Unrolling 的 22 项声明（15 项定理）公理报告为空；'
              '检查器并核对核心纯净。作者自审见研究第 173 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Learning from finitely many values of the feature (part of a reading given); the enough of seeking under '
              'undetermined laws (board item S1); an independent review.',
        'zh': '从特征的有限个值学习（被给予读法的一部分）；不确定律下寻求之足够（看板项 S1）；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, Learning) named "a learner given nothing that rests on every '
              'learnable target, or a witness that none does". Ren, 18 October 2026: "Wait for N5\'s renames to land, '
              'then start the learning and seeking line on the renamed head." (provenance, not warrant). The witness '
              'answers the item; the exact theorem says what a learner given the world (fromLaw) is given beyond the '
              'prefix: a reading of the future through the map, which the prefix itself fixes.',
        'zh': '本章开放纲领（第 8.2 节，学习）列出“a learner given nothing that rests on every learnable target, or a '
              'witness that none does”。Ren，2026年10月18日：“Wait for N5\'s renames to land, then start the learning and '
              'seeking line on the renamed head.”（来历，不是根据）。见证回答此项；精确定理说出被给予世界的学习者（fromLaw）'
              '在前缀之外被给予的是什么：对经映射之未来的一个读法，而那个未来由前缀本身确定。',
    },
    'canonical_source': SRC,
    'aliases': ['what an extrapolation given nothing fixes', '不被给予任何东西的外推所确定者', 'unrolling', '展开',
                'learnable exactly where a reading of the future', '可学恰当是未来的读法',
                'given nothing, not every learnable feature', '不被给予任何东西，并非每个可学特征'],
    'dependencies': [],
    'related': [
        {'id': 'learnable-through-registration',
         'detail': {'en': 'There learnability is characterized with a learner given the world, the law and the target '
                          '(fromLaw); here what that learner is given beyond the prefix is exactly a reading of the '
                          'future, and given nothing no learner learns every learnable target.',
                    'zh': '那里以被给予世界、律与目标的学习者（fromLaw）刻画可学性；这里该学习者在前缀之外被给予的恰是对未来的读法，'
                          '而不被给予任何东西时没有学习者学得每个可学目标。'}},
        {'id': 'identification-where-bounded',
         'detail': {'en': 'The bound from which the extrapolation by elimination proposes the next value, and the '
                          'naming by a finite future of length 2N - 1, are taken from there.',
                    'zh': '逐一排除的外推自其起提议下一值之界，以及长度 2N − 1 的有限未来之命名，取自那里。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.Unrolling',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (L1), on Ren\'s "Wait for N5\'s renames to land, then start the learning and '
              'seeking line on the renamed head."; study section 173.',
        'zh': '2026年10月18日：新增（L1），按 Ren 的“Wait for N5\'s renames to land, then start the learning and seeking '
              'line on the renamed head.”；研究第 173 节。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/what-an-extrapolation-given-nothing-fixes.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
