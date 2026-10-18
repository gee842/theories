#!/usr/bin/env python3
"""Write the record a-law-through-a-projection-along-one-run for G3: python3 -B make_record.py RECEIPT_ID SECTION

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written. SECTION is the study section number."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean'
PKG = f'{LEAN}/becoming'
SRC = f'{PKG}/Becoming/LawAlongRun.lean'
CORE = f'{LEAN}/GenerativeCore.lean'
receipt_id, section = sys.argv[1], sys.argv[2]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.LawAlongRun'] == sha, 'receipt does not bind the current bytes'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/projection-carrying-a-law.json').read_text())['family']
REN = 'please see what else is there to do - keep pushing the frontier till finishing'


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'Some determined process on a description admits a run\'s steps before a step, read through the projection, '
              'exactly where any two of them from configurations alike under it, by the same move, reach configurations '
              'alike under it. The witness is the record read through the projection: it admits those steps, every '
              'process admitting them admits its steps, and it is determined exactly where they are consistent.',
        'zh': '某个描述上的确定过程容许一个运行在某步之前经投影读出的各步，恰在其中任两步从经投影相同的配置、以相同的动作，到达经投影相同的配置之处。'
              '见证是经投影读出的记录：它容许这些步，容许它们的每个过程都容许它的步，并恰在它们一致处是确定的。',
        'declarations': d('Run.ConsistentThrough', 'Run.recordThrough', 'Run.stepsThrough_record', 'Run.record_least',
                          'Run.record_determined_iff', 'Run.law_through_iff'),
    },
    {
        'en': 'Consistency up to a step holds at every earlier step, so where no determined process on the description '
              'admits the steps before a step, none admits them before any later one. Through the identity at every '
              'step the criterion is Becoming.Unfolding\'s consistency of a history, of which exists_law_iff is the law.',
        'zh': '到某步为止的一致在每个更早的步都成立，所以在没有描述上的确定过程容许某步之前各步之处，也没有一个容许任何更晚步之前的各步。'
              '经恒等投影、在每一步，这判据就是 Becoming.Unfolding 中历史的一致，exists_law_iff 是其规律。',
        'declarations': d('Run.ConsistentThrough.earlier', 'Run.no_law_later', 'Run.consistent_id_iff'),
    },
    {
        'en': 'Where configurations alike under the projection go alike, every run is consistent through it at every '
              'step; the converse fails: a run staying at one configuration of a process allowing every step is '
              'consistent through the identity, and the process does not go alike. Switching\'s missing state law '
              'follows from the criterion along its run.',
        'zh': '经投影相同的配置同去之处，每个运行在每一步经它一致；反之不然：在允许每一步的过程中停在一个配置的运行经恒等一致，而过程不同去。'
              'Switching 缺少状态规律，可沿其运行由判据推出。',
        'declarations': d('Run.consistent_of_goAlike', 'Constant.process', 'Constant.run', 'Constant.consistent',
                          'Constant.not_goAlike', 'Switching.inconsistent', 'Switching.no_state_law_of_criterion'),
    },
    {
        'en': 'The image of a process through a projection represents every finite path exactly, in the sense of '
              'GenerativeCore\'s projection_exact_iff, exactly where configurations alike under it match each other\'s '
              'steps up to it; some determined process on the description admits every step read through it and lifts '
              'each of its steps from every configuration of the fibre exactly where configurations alike go alike and '
              'match. Going alike does not give matching (Stuck); Coarse is exact through its first bit.',
        'zh': '过程经投影的像恰在经它相同的配置能在投影意义上相互匹配对方的步之处，按 GenerativeCore 的 projection_exact_iff 精确表示每条有限路径；'
              '某个描述上的确定过程容许经它读出的每一步，并从纤维中每个配置提升它的每一步，恰在相同的配置同去且匹配之处。'
              '同去不给出匹配（Stuck）；Coarse 经其第一位是精确的。',
        'declarations': d('MatchesThrough', 'image_exact_iff', 'exact_law_iff', 'Stuck.process', 'Stuck.goAlike_not_matches',
                          'Coarse.matching', 'Coarse.exact_law'),
    },
]

record = {
    'schema_version': 2,
    'id': 'a-law-through-a-projection-along-one-run',
    'title': {'zh': '沿一个运行经投影的规律', 'en': 'A law through a projection along one run'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'A determined law on a description admits a run\'s steps up to a step exactly where steps alike under it, '
              'by the same move, end alike; the record is the least candidate and failure persists. The image is exact '
              'on finite paths exactly where alike configurations match steps.',
        'zh': '描述上的确定规律容许一个运行到某步为止的各步，恰在经它相同、动作相同的步终于相同之处；记录是最小候选，失败持续。像在有限路径上精确，恰在相同的配置相互匹配步之处。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'None beyond the run, the projection and the step before which its steps are read; the witnesses are '
               'two-configuration processes. No axiom.',
         'zh': '运行、投影以及读到哪一步之外无；见证是两个配置的过程。不加公理。'},
    ],
    'does_not_show': [
        {'en': 'Which projection an actual unfolding carries a law through, or that any formation forms or uses one.',
         'zh': '实际展开经哪个投影承载规律，或任何形成形成或使用一个投影。',
         'kind': 'correspondence'},
        {'en': 'The instance with Becoming.Testing\'s registration (Web.AlikeThroughUpTo) as the projection is not stated.',
         'zh': '以 Becoming.Testing 的识（Web.AlikeThroughUpTo）为投影的实例没有陈述。',
         'kind': 'scope'},
        {'en': 'A law means a determined process; undetermined and random laws along a run are not treated.',
         'zh': '规律指确定的过程；沿运行的不确定与随机规律没有处理。',
         'kind': 'scope'},
        {'en': 'The criterion along one run is near-definitional: what it adds is the least candidate, the persistence '
               'of failure, the identity instance and the separation from the process\'s law.',
         'zh': '沿一个运行的判据近于定义：增量在于最小候选、失败的持续、恒等实例以及与过程规律的分离。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': SRC, 'detail': {
        'en': 'A run consistent where the process has no law: Constant (Constant.consistent, Constant.not_goAlike). Going '
              'alike without exactness: Stuck (Stuck.goAlike_not_matches).',
        'zh': '运行一致而过程无规律：Constant（Constant.consistent、Constant.not_goAlike）。同去而不精确：Stuck（Stuck.goAlike_not_matches）。'}}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 17 theorems of '
              'Becoming.LawAlongRun have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.LawAlongRun 的 17 项定理公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {section} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'The instance with Becoming.Testing\'s registration (Web.AlikeThroughUpTo) as the projection; how many steps of a run settle whether a '
              'law through a finite description holds (with Becoming.Recurrence); an independent review.',
        'zh': '以 Becoming.Testing 的识（Web.AlikeThroughUpTo）为投影的实例；一个运行要多少步才定下经有限描述的规律是否成立（与 Becoming.Recurrence 一起）；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, Selection, causes and experiment) named "a constructive '
              'criterion along one run for a projection carrying a law" and "the bridge to GenerativeCore\'s exact '
              'projection"; projection-carrying-a-law left both in does_not_show. Becoming.Unfolding had the case through '
              'the identity over the whole history (Consistent, exists_law_iff); here any projection, up to any step, '
              'with the identity case as an instance. '
              f'Ren, 18 October 2026: "{REN}" (provenance, not warrant). Reading (the AI\'s): a run is evidence of a law '
              'at a description exactly as far as its own steps agree; what it never visits it does not test; a law at a '
              'description is not yet a faithful model of finite paths, which needs every configuration of a class to '
              'be able to do what any of them did.',
        'zh': '本章开放纲领（第 8.2 节，选择、原因与实验）列出“a constructive criterion along one run for a projection carrying a law”与'
              '“the bridge to GenerativeCore\'s exact projection”；projection-carrying-a-law 把两者列在 does_not_show。Becoming.Unfolding '
              '有经恒等、对整个历史的情形（Consistent、exists_law_iff）；这里是任何投影、到任何一步，恒等情形是实例。'
              f'Ren，2026年10月18日：“{REN}”（来历，不是根据）。读法（AI 的）：一个运行在多大程度上自身各步一致，就在多大程度上是描述上规律的证据；'
              '它未到过的，它不检验；描述上的规律还不是有限路径的忠实模型，后者要求一类中每个配置都能做其中任一个做过的。',
    },
    'canonical_source': SRC,
    'aliases': ['criterion along one run', '沿一个运行的判据', 'law through a projection', '经投影的规律',
                'exact projection', '精确投影', 'matching steps', '匹配步'],
    'dependencies': [
        {'id': 'projection-carrying-a-law', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Image, factors_image, GoAlike, image_determined_iff, carries_law_iff, goAlike_const and '
                          'the witnesses Coarse and Switching; the delta is the criterion along one run and exactness.',
                    'zh': '复用 Image、factors_image、GoAlike、image_determined_iff、carries_law_iff、goAlike_const 以及见证 Coarse 与 '
                          'Switching；增量是沿一个运行的判据与精确性。'},
         'interface': {
             'output': {'en': 'A projection carrying a law over every configuration; the image as least candidate.',
                        'zh': '投影在一切配置上承载规律；像作为最小候选。'},
             'input': {'en': 'The law of the process through a projection, against which one run\'s criterion is set, and '
                             'the image whose exactness is characterized.',
                       'zh': '过程经投影的规律，与之对照一个运行的判据；以及其精确性被刻画的像。'},
             'conditions': {'en': 'None beyond the process and the projection.', 'zh': '过程与投影之外无。'},
             'evidence': f'{PKG}/Becoming/Mechanism.lean'}},
        {'id': 'experiment-needs-return', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Run.StepsThrough and FactorsThrough.',
                    'zh': '复用 Run.StepsThrough 与 FactorsThrough。'},
         'interface': {
             'output': {'en': 'A run\'s steps before a step admitted by a process read through a projection.',
                        'zh': '一个过程经投影容许一个运行在某步之前的各步。'},
             'input': {'en': 'What the criterion along one run characterizes.', 'zh': '沿一个运行的判据所刻画者。'},
             'conditions': {'en': 'None beyond the run.', 'zh': '运行之外无。'},
             'evidence': f'{PKG}/Becoming/Experiment.lean'}},
        {'id': 'process-and-frame-as-readings', 'relation': 'formal-reuse',
         'detail': {'en': 'Run.consistent_id_iff states Becoming.Unfolding\'s Consistent as the criterion through the '
                          'identity at every step, so exists_law_iff is its instance.',
                    'zh': 'Run.consistent_id_iff 把 Becoming.Unfolding 的 Consistent 陈述为经恒等、在每一步的判据，所以 exists_law_iff 是其实例。'},
         'interface': {
             'output': {'en': 'A history\'s consistency and the determined law it shows.',
                        'zh': '历史的一致及其所显示的确定规律。'},
             'input': {'en': 'The identity instance of the criterion.', 'zh': '判据的恒等实例。'},
             'conditions': {'en': 'None beyond the run.', 'zh': '运行之外无。'},
             'evidence': f'{PKG}/Becoming/Unfolding.lean'}},
        {'id': 'finite-trace-transport', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses GenerativeCore\'s Trace and projection_exact_iff (exact representation of finite paths).',
                    'zh': '复用 GenerativeCore 的 Trace 与 projection_exact_iff（有限路径的精确表示）。'},
         'interface': {
             'output': {'en': 'Finite traces and the exact projection of finite paths.',
                        'zh': '有限迹与有限路径的精确投影。'},
             'input': {'en': 'The exactness that MatchesThrough characterizes for the image.',
                       'zh': 'MatchesThrough 为像所刻画的精确性。'},
             'conditions': {'en': 'None beyond the process and the projection.', 'zh': '过程与投影之外无。'},
             'evidence': CORE}},
    ],
    'related': [
        {'id': 'experiment-needs-return',
         'detail': {'en': 'There the record fixes a move\'s outcome only where taken; here the record read through a '
                          'description is the least candidate law, a law exactly where it is consistent.',
                    'zh': '那里记录只在动作被取处固定其结果；这里经描述读出的记录是最小的候选规律，恰在一致处是规律。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': f'{PKG}/Becoming/Mechanism.lean', 'role': 'proof',
         'declarations': d('Image', 'factors_image', 'GoAlike', 'image_determined_iff', 'carries_law_iff',
                           'goAlike_const', 'Coarse.process', 'Coarse.goAlike', 'Switching.run')},
        {'path': f'{PKG}/Becoming/Experiment.lean', 'role': 'proof',
         'declarations': d('Run.StepsThrough', 'FactorsThrough')},
        {'path': f'{PKG}/Becoming/Unfolding.lean', 'role': 'proof',
         'declarations': d('Consistent', 'exists_law_iff')},
        {'path': CORE, 'role': 'proof',
         'declarations': ['Generative.Trace', 'Generative.projection_exact_iff']},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md',
         'role': 'provenance'},
    ],
    'proof_bindings': [{'source': f'{PKG}/Becoming/{m}.lean', 'receipt': receipt,
                        'sha256_pointer': f'/source_sha256/Becoming.{m}', 'success_pointer': '/status',
                        'success_value': 'passed'} for m in ('LawAlongRun', 'Mechanism', 'Experiment', 'Unfolding')]
                      + [{'source': CORE, 'receipt': receipt, 'sha256_pointer': '/source_sha256/GenerativeCore',
                          'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'18 October 2026: added (G3), on Ren\'s "{REN}"; study section {section}.',
        'zh': f'2026年10月18日：新增（G3），按 Ren 的“{REN}”；研究第 {section} 节。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
for b in record['proof_bindings']:
    key = b['sha256_pointer'].rsplit('/', 1)[-1]
    assert data['source_sha256'][key] == hashlib.sha256((ROOT / b['source']).read_bytes()).hexdigest(), key
out = ROOT / 'theories/becoming/results/records/a-law-through-a-projection-along-one-run.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
