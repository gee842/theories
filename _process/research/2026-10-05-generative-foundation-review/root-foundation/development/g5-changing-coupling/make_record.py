#!/usr/bin/env python3
"""Write the record a-law-through-changing-coupling-along-one-run for G5: python3 -B make_record.py RECEIPT_ID SECTION

The receipt id names the checker run folder under becoming-checks/; the source hashes are read from that receipt and
checked against the files' current bytes before anything is written. SECTION is the study section number."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/LawThroughChangingCoupling.lean'
receipt_id, section = sys.argv[1], sys.argv[2]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
assert data['status'] == 'passed', data['status']
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/a-law-through-coupling-along-one-run.json').read_text())['family']
REN = "you have permission now, please see what else is there to do - keep pushing the frontier till finishing"


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'With dependences read off the configuration, two configurations are alike in what a formation couples into '
              'when the levels at each, through the dependence it has there, admit it alike and the conditions it observes '
              'stand alike. This is an equivalence, so some process going alike in it admits a run\'s steps before a step '
              'exactly where the occasions it couples alike, by the same move, lead to occasions it couples alike. Fixed '
              'conditions are the instance.',
        'zh': '依赖从配置读出时，两个配置在一个形成所耦合者上相同，当各自的水平经它在那里的依赖同样地容许它、且它所观察的条件水平相同。'
              '这是等价关系，所以某个在其上同去的过程容许一个运行在某步之前的各步，恰在它耦合相同的场合以相同的动作通向它耦合相同的场合之处。'
              '固定条件是其实例。',
        'declarations': d('Dependence.AdmitsAt', 'Dependence.AlikeAt', 'Dependence.alikeAt_equivalence',
                          'Dependence.conditions_alikeAt_iff', 'Run.law_through_dependence_iff'),
    },
    {
        'en': 'Along a run this is the relation between two steps each read through its own step\'s dependence. '
              'Web.AlikeThrough read at one step, between the levels standing at two steps, is the coupling with the '
              'dependence of that step held fixed; where the dependences at the two steps compared are that step\'s, it is '
              'the changing coupling.',
        'zh': '沿运行，这是两步各经本步依赖读出之间的关系。在某一步读出的 Web.AlikeThrough，在两步所立的水平之间，是把该步依赖固定的耦合；'
              '所比较两步的依赖就是该步的依赖之处，它就是改变的耦合。',
        'declarations': d('Web.AlikeAcross', 'Dependence.alikeAt_iff_alikeAcross', 'Dependence.fixedAt',
                          'Dependence.alikeThrough_iff_fixedAt', 'Web.admits_own_iff', 'Web.alikeAcross_iff_alikeThrough'),
    },
    {
        'en': 'Consistency reads a relation only on the run\'s configurations up to the step, so where a formation\'s '
              'dependences up to it are those of one step, the run is consistent under the changing coupling exactly where '
              'it is under the coupling fixed at that step.',
        'zh': '一致只读关系在运行到该步为止的配置上的部分，所以一个形成到该步为止的依赖都是某一步的依赖之处，运行在改变的耦合下一致，'
              '恰在它在固定于那一步的耦合下一致之处。',
        'declarations': d('Dependence.SameFor', 'Dependence.admitsAt_fixedAt_iff', 'Dependence.Unchanged',
                          'Run.consistentUnder_congr', 'Run.consistent_unchanged_iff'),
    },
    {
        'en': 'In Changing, one level rising by one each step, the process is determined. A dependence dissolving across '
              'the first step leaves the run consistent at every step under the changing coupling, and inconsistent at '
              'step 2 under the coupling fixed at the start. A dependence forming across the first step leaves the coupling '
              'fixed at the start consistent at every step, and the changing coupling inconsistent at step 3.',
        'zh': '在 Changing 中，一个水平每步升一，过程是确定的。在第一步消散的依赖使运行在改变的耦合下每步一致，而在开始时固定的耦合下于第 2 步不一致。'
              '在第一步形成的依赖使开始时固定的耦合每步一致，而改变的耦合于第 3 步不一致。',
        'declarations': d('Changing.process', 'Changing.run', 'Changing.determined', 'Changing.dissolving',
                          'Changing.forming', 'Changing.dissolves', 'Changing.forms',
                          'Changing.dissolving_not_admits_zero', 'Changing.dissolving_admits_succ',
                          'Changing.dissolving_consistent', 'Changing.dissolving_fixed_inconsistent',
                          'Changing.forming_admits_zero', 'Changing.forming_not_admits_one',
                          'Changing.forming_admits_three', 'Changing.forming_inconsistent',
                          'Changing.forming_fixed_consistent', 'Changing.forming_no_law',
                          'Changing.dissolving_fixed_no_law'),
    },
]

record = {
    'schema_version': 2,
    'id': 'a-law-through-changing-coupling-along-one-run',
    'title': {'zh': '沿一个运行经改变的耦合的规律', 'en': 'A law through coupling that changes along the run'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'Where what a formation depends on forms and dissolves along a run, the law at what it couples into on each '
              'occasion and the law at the coupling of one moment agree where nothing it depends on changes; otherwise '
              'neither gives the other.',
        'zh': '一个形成所依赖者沿运行形成与消散之处，它在每个场合所耦合者上的规律与某一时刻耦合上的规律，在它所依赖者无变之处一致；否则互不给出。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'Dependences are read off the configuration (Dependence of Becoming.Dependence); what a formation observes is '
               'fixed. For the criterion, the relation is the coupling, an equivalence. The witness is a one-level process. '
               'No axiom.',
         'zh': '依赖从配置读出（Becoming.Dependence 的 Dependence）；形成所观察者固定。对判据，关系是耦合，一个等价关系。见证是一个水平的过程。不加公理。'},
    ],
    'does_not_show': [
        {'en': 'Observation that changes along the run is not treated; what a formation observes is fixed, as in '
               'Becoming.Testing.',
         'zh': '沿运行改变的观察没有处理；形成所观察者固定，如 Becoming.Testing。',
         'kind': 'scope'},
        {'en': 'A dependence not read off the configuration (a Web whose requirements change with the step alone) is not '
               'treated here.',
         'zh': '不从配置读出的依赖（要求只随步改变的 Web）这里没有处理。',
         'kind': 'scope'},
        {'en': 'Which dependences an actual formation forms along an unfolding, or how many steps settle whether a law at '
               'its coupling holds.',
         'zh': '实际形成沿展开形成哪些依赖，或要多少步才定下其耦合上的规律是否成立。',
         'kind': 'correspondence'},
        {'en': 'The criterion is G4\'s applied to a new equivalence; what it adds is the relation through changing '
               'dependence, its bridges and the comparison with the fixed coupling.',
         'zh': '判据是把 G4 的判据用于新的等价关系；增量在于经改变依赖的关系、其桥接以及与固定耦合的比较。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': SRC, 'detail': {
        'en': 'Neither law gives the other where dependences change: Changing (dissolving_consistent with '
              'dissolving_fixed_inconsistent; forming_fixed_consistent with forming_inconsistent).',
        'zh': '依赖改变之处两种规律互不给出：Changing（dissolving_consistent 与 dissolving_fixed_inconsistent；'
              'forming_fixed_consistent 与 forming_inconsistent）。'}}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 24 theorems of '
              'Becoming.LawThroughChangingCoupling have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.LawThroughChangingCoupling 的 24 项定理公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {section} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Observation that changes along the run; how many steps settle whether a law at the coupling holds; an '
              'independent review.',
        'zh': '沿运行改变的观察；要多少步才定下耦合上的规律是否成立；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, Selection, causes and experiment) named "the criterion through '
              'coupling that changes along the run", which a-law-through-coupling-along-one-run left in does_not_show. '
              f'Ren, 18 October 2026: "{REN}"; 19 October: "continue" (provenance, not warrant); the AI chose the item. '
              'Reading (the AI\'s): a law at a formation\'s coupling along a course is a law at the coupling it has on each '
              'occasion; reading the course through the dependence of one moment can find a law its own coupling does not '
              'carry, or miss one it does.',
        'zh': '本章开放纲领（第 8.2 节，选择、原因与实验）列出“the criterion through coupling that changes along the run”，'
              'a-law-through-coupling-along-one-run 把它列在 does_not_show。'
              f'Ren，2026年10月18日：“{REN}”；10月19日：“continue”（来历，不是根据）；条目由 AI 选择。'
              '读法（AI 的）：沿进程在一个形成耦合上的规律，是在它每个场合所有耦合上的规律；经某一时刻的依赖读进程，可能找到它自己的耦合不承载的规律，'
              '也可能错过它承载的规律。',
    },
    'canonical_source': SRC,
    'aliases': ['law through changing coupling', '经改变的耦合的规律', 'forming and dissolving dependence',
                '形成与消散的依赖', 'coupling fixed at one step', '固定于一步的耦合'],
    'dependencies': [
        {'id': 'a-law-through-coupling-along-one-run', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Run.ConsistentUnder and Run.law_under_iff, the criterion up to an equivalence, and '
                          'Conditions.AlikeAt, the fixed coupling, which is the instance.',
                    'zh': '复用 Run.ConsistentUnder 与 Run.law_under_iff（到等价关系为止的判据），以及作为实例的固定耦合 Conditions.AlikeAt。'},
         'interface': {
             'output': {'en': 'The criterion along one run up to an equivalence, and coupling with fixed conditions.',
                        'zh': '沿一个运行到等价关系为止的判据，以及固定条件下的耦合。'},
             'input': {'en': 'The criterion the changing coupling is taken through, and the fixed coupling it is compared '
                             'with.',
                       'zh': '改变的耦合所经的判据，以及与之比较的固定耦合。'},
             'conditions': {'en': 'An equivalence.', 'zh': '一个等价关系。'},
             'evidence': f'{PKG}/Becoming/LawThroughCoupling.lean'}},
        {'id': 'testing-within-registration', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Web.AlikeThrough and thresholdOnly: Web.AlikeThrough at one step is the coupling with '
                          'that step\'s dependence fixed.',
                    'zh': '复用 Web.AlikeThrough 与 thresholdOnly：某一步的 Web.AlikeThrough 是把该步依赖固定的耦合。'},
         'interface': {
             'output': {'en': 'What registers alike in a formation at a step, under two level histories.',
                        'zh': '在两个水平历史之下，一个形成在某步耦合相同者。'},
             'input': {'en': 'The coupling of one step compared with the changing coupling.',
                       'zh': '与改变的耦合相比较的某一步的耦合。'},
             'conditions': {'en': 'None beyond the web.', 'zh': '网之外无。'},
             'evidence': f'{PKG}/Becoming/Testing.lean'}},
        {'id': 'becoming-dependence-dynamics', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Dependence, Web.Forms, Web.Dissolves and Dependence.along: dependences read off the '
                          'configuration, and a run read through them as a Web.',
                    'zh': '复用 Dependence、Web.Forms、Web.Dissolves 与 Dependence.along：从配置读出的依赖，以及经它们读作 Web 的运行。'},
         'interface': {
             'output': {'en': 'Dependences as an observable of the configuration, and their forming and dissolving.',
                        'zh': '作为配置可观察量的依赖，及其形成与消散。'},
             'input': {'en': 'The changing dependence the coupling is read through.', 'zh': '耦合所经的改变的依赖。'},
             'conditions': {'en': 'None beyond the run.', 'zh': '运行之外无。'},
             'evidence': f'{PKG}/Becoming/Dependence.lean'}},
        {'id': 'becoming-renewal-reading', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Conditions, the fixed conditions the dependence of one step is held as.',
                    'zh': '复用 Conditions，某一步的依赖所固定成的固定条件。'},
         'interface': {
             'output': {'en': 'Levels, requirements and needs read off configurations.', 'zh': '从配置读出的水平、要求与需要。'},
             'input': {'en': 'The conditions fixed at one step.', 'zh': '固定于一步的条件。'},
             'conditions': {'en': 'None.', 'zh': '无。'},
             'evidence': f'{PKG}/Becoming/Renewal.lean'}},
    ],
    'related': [
        {'id': 'subthreshold-registration',
         'detail': {'en': 'There a difference below a threshold is not registered; here which thresholds a formation has '
                          'changes along a run, and with it what it couples into.',
                    'zh': '那里阈值以下的差别不被识；这里形成有哪些阈值沿运行改变，它所耦合者也随之改变。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': f'{PKG}/Becoming/LawThroughCoupling.lean', 'role': 'proof',
         'declarations': d('Run.ConsistentUnder', 'Run.ConsistentUnder.earlier', 'Run.law_under_iff',
                           'Conditions.AlikeAt', 'Run.law_through_coupling_iff')},
        {'path': f'{PKG}/Becoming/Likeness.lean', 'role': 'proof', 'declarations': d('GoAlikeUnder')},
        {'path': f'{PKG}/Becoming/Testing.lean', 'role': 'proof', 'declarations': d('Web.AlikeThrough', 'thresholdOnly')},
        {'path': f'{PKG}/Becoming/Dependence.lean', 'role': 'proof',
         'declarations': d('Dependence', 'Conditions.dependence', 'Web.Forms', 'Web.Dissolves')},
        {'path': f'{PKG}/Becoming/Admission.lean', 'role': 'proof', 'declarations': d('Web.Admits')},
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
                       for m in ('LawThroughChangingCoupling', 'LawThroughCoupling', 'Likeness', 'Testing',
                                 'Dependence', 'Admission', 'World', 'Labelled', 'Renewal', 'Joint')],
    'history': [{
        'en': f'19 October 2026: added (G5), on Ren\'s standing go "{REN}" and "continue" (19 October); study section {section}.',
        'zh': f'2026年10月19日：新增（G5），按 Ren 的持续许可“{REN}”与“continue”（10月19日）；研究第 {section} 节。',
    }],
}
assert len(record['statement']['en']) <= 300, len(record['statement']['en'])
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
for b in record['proof_bindings']:
    key = b['sha256_pointer'].rsplit('/', 1)[-1]
    assert data['source_sha256'][key] == hashlib.sha256((ROOT / b['source']).read_bytes()).hexdigest(), key
out = ROOT / 'theories/becoming/results/records/a-law-through-changing-coupling-along-one-run.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
