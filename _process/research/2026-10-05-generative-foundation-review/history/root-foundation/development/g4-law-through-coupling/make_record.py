#!/usr/bin/env python3
"""Write the record a-law-through-coupling-along-one-run for G4: python3 -B make_record.py RECEIPT_ID SECTION

The receipt id names the checker run folder under becoming-checks/; the source hashes are read from that receipt and
checked against the files' current bytes before anything is written. SECTION is the study section number."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/LawThroughCoupling.lean'
receipt_id, section = sys.argv[1], sys.argv[2]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
assert data['status'] == 'passed', data['status']
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/a-law-through-a-projection-along-one-run.json').read_text())['family']
REN = ("Yes: claim G4 on the board — the criterion along one run with Becoming.Testing's registration as the "
       "projection — and prove it in scratch while the queue runs.")


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'Where a relation is an equivalence, some process going alike under it admits a run\'s steps before a step '
              'exactly where any two of them from related configurations, by the same move, reach related configurations. '
              'The witness is the record read under the relation; the forward direction needs no equivalence.',
        'zh': '关系是等价关系时，某个在它之下同去的过程容许一个运行在某步之前的各步，恰在其中任两步从相关的配置、以相同的动作，到达相关的配置之处。'
              '见证是在该关系下读出的记录；正方向不需要等价。',
        'declarations': d('Run.ConsistentUnder', 'Run.recordUnder', 'Run.recordUnder_steps', 'Run.recordUnder_goAlike',
                          'Run.law_under_iff'),
    },
    {
        'en': 'Consistency up to a step holds at every earlier step, so once no such process admits the steps it admits '
              'none later; a process going alike under the relation makes every run consistent; through equal '
              'projections the criterion is the one along one run through a projection.',
        'zh': '到某步为止的一致在每个更早的步都成立，所以一旦没有这样的过程容许那些步，以后也没有；在该关系下同去的过程使每个运行一致；'
              '经相等的投影，这判据就是沿一个运行经投影的判据。',
        'declarations': d('Run.ConsistentUnder.earlier', 'Run.no_law_under_later', 'Run.consistentUnder_of_goAlikeUnder',
                          'Run.consistentUnder_eq_iff'),
    },
    {
        'en': 'With fixed conditions, two configurations are alike in what a formation couples into when their levels '
              'admit it alike and the conditions it observes stand alike; this is an equivalence, exactly Web.AlikeThrough '
              'on the runs read through the conditions, between two runs at a step and between two steps of one run. So '
              'some process going alike in what the formation couples into admits a run\'s steps exactly where the '
              'occasions it couples alike, by the same move, lead to occasions it couples alike.',
        'zh': '在固定条件下，两个配置在一个形成所耦合者上相同，当它们的水平同样地容许它、且它所观察的条件水平相同；这是等价关系，恰是经条件读出的运行上的 '
              'Web.AlikeThrough，无论是两个运行在同一步之间，还是一个运行的两步之间。所以某个在该形成所耦合者上同去的过程容许一个运行的各步，'
              '恰在它耦合相同的场合以相同的动作通向它耦合相同的场合之处。',
        'declarations': d('Conditions.AdmitsAt', 'Conditions.AlikeAt', 'Conditions.alikeAt_equivalence',
                          'Conditions.alikeThrough_iff', 'Conditions.alikeAt_iff_alikeThrough',
                          'Run.law_through_coupling_iff'),
    },
    {
        'en': 'In Unseen the process is determined, and a formation depending on one level and observing nothing couples '
              'the run\'s first two steps alike while by the same move they lead to configurations it couples apart: the '
              'level it does not couple into decides, and no law holds at its coupling along the run. Observing that '
              'level, the run is consistent at every step.',
        'zh': '在 Unseen 中过程是确定的，一个依于一个水平而不观察任何东西的形成把运行的前两步耦合为相同，而以相同的动作它们通向它耦合为不同的配置：'
              '它不耦合的水平起决定作用，沿该运行在其耦合上没有规律。观察那个水平，运行在每一步都一致。',
        'declarations': d('Unseen.process', 'Unseen.level', 'Unseen.conditions', 'Unseen.state', 'Unseen.run',
                          'Unseen.determined', 'Unseen.admits', 'Unseen.not_admits_zero', 'Unseen.inconsistent',
                          'Unseen.no_law', 'Unseen.observing', 'Unseen.first_apart', 'Unseen.consistent_observing'),
    },
]

record = {
    'schema_version': 2,
    'id': 'a-law-through-coupling-along-one-run',
    'title': {'zh': '沿一个运行经耦合的规律', 'en': 'A law through what a formation couples into, along one run'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'What a formation couples into carries a law along one run exactly where the occasions it couples alike, '
              'by the same move, lead to occasions it couples alike; an uncoupled level can break this law in a '
              'determined process.',
        'zh': '形成所耦合者沿一个运行承载规律，恰在它耦合相同的场合以相同的动作通向它耦合相同的场合之处；在确定的过程中一个未耦合的水平可以打破这规律。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'For the backward direction, the relation is an equivalence; for coupling, the conditions are fixed '
               '(Conditions of Becoming.Renewal). The witness is a two-level process. No axiom.',
         'zh': '对反方向，关系是等价关系；对耦合，条件是固定的（Becoming.Renewal 的 Conditions）。见证是两个水平的过程。不加公理。'},
    ],
    'does_not_show': [
        {'en': 'Coupling that changes along the run (Dependence rather than fixed Conditions), where the relation need not '
               'be an equivalence, is not treated.',
         'zh': '沿运行改变的耦合（Dependence 而非固定的 Conditions），其关系不必是等价关系，没有处理。',
         'kind': 'scope'},
        {'en': 'The up-to form over histories (Web.AlikeThroughUpTo) relates two histories and is not the relation here.',
         'zh': '对历史的到某步为止的形式（Web.AlikeThroughUpTo）关联两个历史，不是这里的关系。',
         'kind': 'scope'},
        {'en': "Which formation's coupling carries a law along an actual unfolding, or how many steps settle it.",
         'zh': '实际展开中哪个形成的耦合承载规律，或要多少步才定下。',
         'kind': 'correspondence'},
        {'en': 'The criterion is near-definitional; what it adds is the relation form, the bridge to coupling and the '
               'witness.',
         'zh': '判据近于定义；增量在于关系形式、到耦合的桥接与见证。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': SRC, 'detail': {
        'en': 'A determined process with no law at a formation\'s coupling along a run: Unseen (Unseen.determined, '
              'Unseen.no_law).',
        'zh': '确定的过程而沿运行在形成的耦合上无规律：Unseen（Unseen.determined、Unseen.no_law）。'}}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 18 theorems of '
              'Becoming.LawThroughCoupling have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.LawThroughCoupling 的 18 项定理公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {section} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Coupling that changes along the run; how many steps settle whether a law at a finite coupling holds; an '
              'independent review.',
        'zh': '沿运行改变的耦合；要多少步才定下有限耦合上的规律是否成立；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, Selection, causes and experiment) named "the instance of the '
              'criterion along one run with Becoming.Testing\'s registration as the projection"; '
              'a-law-through-a-projection-along-one-run left it in does_not_show. Registration is now called coupling '
              '(Web.AlikeThrough); it is a relation, and an equality of what is coupled would need propext, so the '
              'criterion is stated up to a relation. '
              f'Ren, 18 October 2026: "{REN}" (provenance, not warrant). Reading (the AI\'s): a formation\'s own course is '
              'evidence of a law at its coupling exactly as far as it agrees with itself; where what it does not couple '
              'into decides its next coupling, it meets no law at its coupling, only a record.',
        'zh': '本章开放纲领（第 8.2 节，选择、原因与实验）列出“the instance of the criterion along one run with Becoming.Testing\'s '
              'registration as the projection”；a-law-through-a-projection-along-one-run 把它列在 does_not_show。识现称耦合'
              '（Web.AlikeThrough）；它是关系，所耦合者的相等需要 propext，所以判据到关系为止陈述。'
              f'Ren，2026年10月18日：“{REN}”（来历，不是根据）。读法（AI 的）：一个形成自己的进程在多大程度上与自身一致，就在多大程度上是其耦合上规律的证据；'
              '它不耦合者决定其下一步耦合之处，它在其耦合上遇不到规律，只有记录。',
    },
    'canonical_source': SRC,
    'aliases': ['law through coupling', '经耦合的规律', 'criterion up to a relation', '到关系为止的判据',
                'law through registration', '经识的规律', 'uncoupled level decides', '未耦合的水平决定'],
    'dependencies': [
        {'id': 'a-law-through-a-projection-along-one-run', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Run.ConsistentThrough: the criterion through a projection is the instance with equal '
                          'projections (Run.consistentUnder_eq_iff).',
                    'zh': '复用 Run.ConsistentThrough：经投影的判据是以相等投影的实例（Run.consistentUnder_eq_iff）。'},
         'interface': {
             'output': {'en': 'The criterion along one run through a projection.', 'zh': '沿一个运行经投影的判据。'},
             'input': {'en': 'The instance with equal projections.', 'zh': '以相等投影的实例。'},
             'conditions': {'en': 'None beyond the run.', 'zh': '运行之外无。'},
             'evidence': f'{PKG}/Becoming/LawAlongRun.lean'}},
        {'id': 'determinacy-up-to-likeness', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses GoAlikeUnder (through the identity) as the law up to a relation.',
                    'zh': '复用 GoAlikeUnder（经恒等）作为到关系为止的规律。'},
         'interface': {
             'output': {'en': 'A process going alike under a relation on descriptions.', 'zh': '在描述上的关系之下同去的过程。'},
             'input': {'en': 'What the criterion up to a relation characterizes.', 'zh': '到关系为止的判据所刻画者。'},
             'conditions': {'en': 'None beyond the process and the relation.', 'zh': '过程与关系之外无。'},
             'evidence': f'{PKG}/Becoming/Likeness.lean'}},
        {'id': 'testing-within-registration', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Web.AlikeThrough and thresholdOnly: coupling at a configuration is Web.AlikeThrough on '
                          'the runs read through fixed conditions.',
                    'zh': '复用 Web.AlikeThrough 与 thresholdOnly：配置上的耦合是经固定条件读出的运行上的 Web.AlikeThrough。'},
         'interface': {
             'output': {'en': 'What registers alike in a formation at a step, under two level histories.',
                        'zh': '在两个水平历史之下，一个形成在某步耦合相同者。'},
             'input': {'en': 'The relation the criterion is taken through.', 'zh': '判据所经的关系。'},
             'conditions': {'en': 'Fixed conditions.', 'zh': '固定条件。'},
             'evidence': f'{PKG}/Becoming/Testing.lean'}},
        {'id': 'becoming-dependence-dynamics', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Conditions.dependence and Dependence.along, which read a run through fixed conditions as '
                          'a Web.',
                    'zh': '复用 Conditions.dependence 与 Dependence.along，它们把运行经固定条件读作 Web。'},
         'interface': {
             'output': {'en': 'A run read through its dependences.', 'zh': '经其依赖读出的运行。'},
             'input': {'en': 'The webs on which coupling is compared.', 'zh': '比较耦合所在的网。'},
             'conditions': {'en': 'None beyond the run.', 'zh': '运行之外无。'},
             'evidence': f'{PKG}/Becoming/Dependence.lean'}},
        {'id': 'becoming-renewal-reading', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Conditions, the fixed conditions of configurations.', 'zh': '复用 Conditions，配置的固定条件。'},
         'interface': {
             'output': {'en': 'Levels, requirements and needs read off configurations.', 'zh': '从配置读出的水平、要求与需要。'},
             'input': {'en': 'The conditions coupling is stated on.', 'zh': '陈述耦合所依的条件。'},
             'conditions': {'en': 'None.', 'zh': '无。'},
             'evidence': f'{PKG}/Becoming/Renewal.lean'}},
    ],
    'related': [
        {'id': 'subthreshold-registration',
         'detail': {'en': 'There a difference below a threshold is not registered; here a level outside what a formation '
                          'couples into decides its next coupling along a run.',
                    'zh': '那里阈值以下的差别不被识；这里形成所耦合者之外的水平沿运行决定其下一步的耦合。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': f'{PKG}/Becoming/LawAlongRun.lean', 'role': 'proof', 'declarations': d('Run.ConsistentThrough')},
        {'path': f'{PKG}/Becoming/Likeness.lean', 'role': 'proof', 'declarations': d('GoAlikeUnder')},
        {'path': f'{PKG}/Becoming/Testing.lean', 'role': 'proof', 'declarations': d('Web.AlikeThrough', 'thresholdOnly')},
        {'path': f'{PKG}/Becoming/Dependence.lean', 'role': 'proof', 'declarations': d('Conditions.dependence')},
        {'path': f'{PKG}/Becoming/World.lean', 'role': 'proof', 'declarations': d('Web')},
        {'path': f'{PKG}/Becoming/Labelled.lean', 'role': 'proof', 'declarations': d('Dependence.along')},
        {'path': f'{PKG}/Becoming/Renewal.lean', 'role': 'proof', 'declarations': d('Conditions')},
        {'path': f'{PKG}/Becoming/Joint.lean', 'role': 'proof', 'declarations': d('Determined')},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md',
         'role': 'provenance'},
    ],
    'proof_bindings': [{'source': f'{PKG}/Becoming/{m}.lean', 'receipt': receipt,
                        'sha256_pointer': f'/source_sha256/Becoming.{m}', 'success_pointer': '/status',
                        'success_value': 'passed'}
                       for m in ('LawThroughCoupling', 'LawAlongRun', 'Likeness', 'Testing', 'Dependence', 'World',
                                 'Labelled', 'Renewal', 'Joint')],
    'history': [{
        'en': f'18 October 2026: added (G4), on Ren\'s "{REN}"; study section {section}.',
        'zh': f'2026年10月18日：新增（G4），按 Ren 的“{REN}”；研究第 {section} 节。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
for b in record['proof_bindings']:
    key = b['sha256_pointer'].rsplit('/', 1)[-1]
    assert data['source_sha256'][key] == hashlib.sha256((ROOT / b['source']).read_bytes()).hexdigest(), key
out = ROOT / 'theories/becoming/results/records/a-law-through-coupling-along-one-run.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
