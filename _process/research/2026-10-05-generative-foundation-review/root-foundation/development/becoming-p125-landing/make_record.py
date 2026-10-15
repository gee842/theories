#!/usr/bin/env python3
"""P125: write the schema-2 record observation-is-a-route, the paired notes it answers, and the
follow-up for Ren's agreement with P124's readings in loops-within-what-a-law-reads.

usage: python3 -B make_record.py ROOT [SECTION]

References are hashed from ROOT (run after apply_docs.py, so the study and chapter hashes are those
of the applied texts). The receipt reference and the proof bindings of the new record are added at
landing, so until then it names "receipt bound at landing". The declarations listed in the laws are
checked against Becoming/Observation.lean, and the reused ones against their modules.

Paired notes:
- loops-within-what-a-law-reads: its readings marked agreed by Ren (16 October, "agree in general",
  source 2026-10-16-thresholds-readings-and-measure-question, added as provenance); the declaration
  Thresholds.le_of_not_lt renamed Thresholds.le_of_not_not, and the Thresholds proof reference rehashed
  for that rename and the header's readings note (the receipt binding is renewed at landing); its next
  step drops how a formation comes to observe a stock (answered by observation-is-a-route) and Ren's
  judgment on the readings (given); related adds the new record.
- runaway-distance-unregistered: its next step's first item, how a formation comes to observe a stock,
  is answered and dropped; related adds the new record.
Each change asserts the text it replaces; nothing is written unless every change applies. One history
note per change.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTION = int(sys.argv[2]) if len(sys.argv) > 2 else 159
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-16-thresholds-approach-approved.md'
AGREED = 'sources/15-codex-theory-conversations/2026-10-16-thresholds-readings-and-measure-question.md'
REVIEWED = '2026-10-16T00:00:00+00:00'
ID = 'observation-is-a-route'
P124 = 'loops-within-what-a-law-reads'


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


LAWS = [
    law('差别只往下游去：起始之差只在一个储量上为正、部分不给差时，在一步被传到的条件都在储量的下游，按到那一步形成的耦合；所以所携带的量，'
        '能到达的最多的差，在不在下游之处为零。链可接，形成的路线保持形成。',
        'A difference goes only downstream: where the starting gap is positive at one stock alone and the part gives no '
        'gap, a gap conveyed to a condition at a step lies downstream of the stock by the couplings formed by that step; so '
        'the carried amount, the most difference that can arrive, is zero wherever not downstream. Chains join, and a '
        'route formed stays formed.',
        ['Upstream.single', 'Upstream.trans', 'Upstream.snoc', 'Upstream.before_mono', 'conveyed_upstream',
         'carried_zero_off_downstream']),
    law('路线由闭合而形成：到 T + 1 形成的路线是到 T 形成的路线，与经过一个在第 T 步作用的耦合者。',
        'A route forms by closing: the routes formed by step T + 1 are those formed by T and those through a coupling '
        'acting at step T.',
        ['upstream_succ_iff', 'route_forms_by_closing']),
    law('读入每个条件：形成与一个条件的交换只由时程为那个条件所标的水平决定。读一个时程的律是对所有条件读得一样的特例，经识而读的律也是；'
        '未读入的水平耦合强度为零，所以限于所读的强度是律的强度，其路线是所读的路线。',
        'Reading into each condition: what a formation exchanges with a condition is fixed by the levels the schedule marks '
        'for that condition. A law reading a schedule is the case reading alike for every condition, and so is a law '
        'reading through a registration; a level unread into a condition is coupled into it with strength zero, so the '
        'strengths restricted to what is read are strengths of the law, and their routes are routes of reading.',
        ['ExchangeLaw.ReadsInto', 'readCouplings', 'restrictInto', 'ExchangeLaw.ReadsAt.readsInto',
         'ExchangeLaw.Through.readsInto', 'ExchangeLaw.ReadsInto.respondsWithin_unread', 'ExchangeLaw.ReadsInto.restrict',
         'couplesAt_readCouplings', 'upstream_readCouplings']),
    law('所识即在下游：对每个读入每个条件一个时程、所读水平列出的律，两个平衡的进程在场的形成相同、部分动作相同、其余遵从律，起始只在一个'
        '储量上不同时，在每一步凡不在储量下游（按到那一步形成的所读路线）的条件都相同；所以一个形成所读入的水平都不在下游时它的交换相同，'
        '经识而读的律所识者都不在下游时也是。所观察的储量是长度为零的路线。',
        'Registering is being downstream: for every law reading into each condition a schedule of listed levels, two '
        'balanced courses with the same formations present, the part acting alike and the rest following the law, apart '
        'at the start only in a stock, are alike at each step at every condition not downstream of the stock by the '
        'readings formed by then; so a formation whose readings into a condition all lie off the downstream exchanges '
        'alike, and so does one reading through registration whose registrations all lie off it. The stock observed is '
        'the route of length zero.',
        ['apart_only_downstream', 'exchange_alike_off_downstream', 'ExchangeLaw.Through.alike_off_downstream']),
    law('量度的见证：一个形成从第 T 步起把储量的水平加到记录上，在记录显示至少 N 时从储量汲取。T 之前储量下游只有它自己，没有经过它的'
        '回路；在第 T 步从储量到记录的路线与储量 → 记录 → 汲取的回路形成；只在储量上不同的两个进程，记录到 T 为止相同，跨过第 T 步差出'
        '抬高，汲取回应记录。',
        'The measurement witness: from step T a formation adds the stock\'s level to a record, and draws from the stock '
        'while the record shows at least N. Before T only the stock lies downstream of it and no loop passes through it; '
        'at T the route stock → record and the loop stock → record → draw form; in two courses apart only on the stock '
        'the record is alike up to T and differs by the raise across the step from T, and the draw responds to the '
        'record.',
        ['Observation.Measure.law', 'Observation.Measure.reads', 'Observation.Measure.readsInto',
         'Observation.Measure.listed', 'Observation.Measure.no_coupling_from_stock',
         'Observation.Measure.downstream_before', 'Observation.Measure.no_loop_before', 'Observation.Measure.route_at',
         'Observation.Measure.record_into_stock', 'Observation.Measure.loop_at', 'Observation.Measure.registers_after',
         'Observation.Measure.draw_responds']),
]

REUSED = [
    ('Propagation', ['Becoming.Conveyed', 'Becoming.carried', 'Becoming.carried_pos_iff',
                     'Becoming.ExchangeLaw.RespondsWithin', 'Becoming.ExchangeLaw.exchangeGap', 'Becoming.gap',
                     'Becoming.gap_eq_zero_iff']),
    ('Loops', ['Becoming.Couples', 'Becoming.Coupled', 'Becoming.OnLoop', 'Becoming.Upstream', 'Becoming.Loops.beq_self']),
    ('Remainder', ['Becoming.CouplesAt']),
    ('Closing', ['Becoming.strengthsBefore', 'Becoming.couples_before_iff', 'Becoming.couples_before_mono',
                 'Becoming.couples_before_of_couplesAt', 'Becoming.Upstream.lift', 'Becoming.Upstream.refl',
                 'Becoming.Closing.join', 'Becoming.Closing.join_below', 'Becoming.Closing.join_from',
                 'Becoming.Coupled.append', 'Becoming.Coupled.one', 'Becoming.Closing.split', 'Becoming.onLoop_of_closing',
                 'Becoming.Closing.ble_false_of_lt']),
    ('Thresholds', ['Becoming.ExchangeLaw.ReadsAt', 'Becoming.ExchangeLaw.Through.readsAt', 'Becoming.held_while',
                    'Becoming.Thresholds.same_step', 'Becoming.Thresholds.cond_pos', 'Becoming.Thresholds.pos_cond']),
    ('Counterfactual', ['Becoming.ExchangeLaw', 'Becoming.ExchangeLaw.Through', 'Becoming.Flow.Follows',
                        'Becoming.Flow.ActsAlike']),
    ('Testing', ['Becoming.Web.Registers']),
    ('Flow', ['Becoming.Flow', 'Becoming.Flow.Balances', 'Becoming.Flow.taken', 'Becoming.Flow.given',
              'Becoming.eq_zero_of_not_pos']),
    ('Population', ['Becoming.total_congr_on']),
    ('Dependence', ['Becoming.Web']),
    ('Recurrence', ['Becoming.le_succ_cases', 'Becoming.gap_of_lt']),
    ('Generation', ['Becoming.total']),
]


def record():
    path = LEAN + 'Observation.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(path)
    assert sorted(listed) == sorted(actual), set(listed) ^ set(actual)
    assert len(set(listed)) == len(listed)
    for module, names in REUSED:
        missing = set(names) - set(declared(LEAN + module + '.lean'))
        assert not missing, (module, missing)
    theorems = sum(1 for line in (ROOT / path).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': ID,
        'title': pair('观察是从所观察者出发的路线：差别只往下游去',
                      'Observation is a route from what is observed: a difference goes only downstream'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '一个储量之差只往它的下游去；对每个读入每个条件的律，只在储量上不同的进程在不在其下游之处都相同，所以一个形成只经它所读的、在储量'
            '下游的水平识储量，所观察者是长度为零的路线；路线由闭合而形成。',
            "A stock's difference goes only downstream; for every law reading into each condition, courses apart only in the "
            'stock are alike wherever not downstream of it, so a formation registers it only through a level it reads '
            'downstream, observing it being the route of length zero; a route forms by closing.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。各定理所写者写在定理中：律读入每个条件的时程（ReadsInto），所读的水平列出；起始之差只在储量上，部分不给差（对所携带'
            '的量）；两个进程平衡、在场的形成相同、部分动作相同、其余遵从律，起始只在储量上不同（对进程）。不判定条件，不需条件有限。',
            'No axiom. What each theorem needs is written into it: the schedule a law reads into each condition (ReadsInto), '
            'the levels read being listed; the starting gap at the stock alone and none from the part (for the carried '
            'amount); two balanced courses with the same formations present, the part acting alike and the rest following '
            'the law, apart at the start only in the stock (for the courses). No decision on conditions, and no finiteness '
            'of conditions, is used.')],
        'does_not_show': [
            {**pair('在下游者必不同：一个形成可以读而不回应；见证给出实际不同的一例。',
                    'That what lies downstream differs: a formation may read without responding; the witness gives one case '
                    'where it does.'), 'kind': 'scope'},
            {**pair('律读什么、量度何时开始、记录是否及时被读；带误差的量度。',
                    'Which schedule a law reads, when a measurement starts and whether the record is read in time; '
                    'measurement with error.'), 'kind': 'scope'},
            {**pair('以强度陈述进程：由强度界多处不同的历史之差要逐处换历史，需判定条件；这里进程的定理用读的时程。',
                    'Statements on courses by strengths: bounding a difference of histories apart in many places by '
                    'strengths changes them one place at a time and needs a decision on conditions; the theorems on courses '
                    'here use the schedule read.'), 'kind': 'scope'},
        ],
        'counterexamples': [],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Observation 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Observation, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '带误差的量度；他者之识作为路线；在下游者何时必不同（回应的下界）；独立审查；Ren 对读法的判断。',
            'Measurement with error; another\'s registration as a route; when what lies downstream must differ (lower bounds '
            'on responses); an independent review; Ren\'s judgment on the readings.'),
        'correspondence': pair(
            'P124 留下“一个形成怎样开始观察它所依赖的储量”；Ren 对 P124 的做法答“approve your approach, please continue”。本结果回答：'
            '观察是站在从所观察者出发的所读路线的末端。读法（AI 的，待 Ren）：观察不是依赖之外的第二种关系，直接观察是长度为零的路线，量度、'
            '模型或他者之识是更长的路线；一个形成开始观察，是一次读闭合一条路线；P124 第二项读法中断裂之前对储量水平的读就是这样一条路线。',
            'P124 left open how a formation comes to observe a stock it depends on; Ren answered P124\'s approach with '
            '“approve your approach, please continue”. This result answers: to observe is to stand at the end of a route of '
            'readings from what is observed. Readings (the AI\'s, pending Ren): observation is not a second relation beside '
            'dependence, direct observation being the route of length zero and a measurement, a model or another\'s '
            'registration a longer route; a formation comes to observe by a reading that closes a route; the reading of the '
            'stock\'s level before the break in P124\'s second reading is such a route.'),
        'canonical_source': path,
        'aliases': ['observation is a route', '观察是路线', 'a difference goes only downstream', '差别只往下游去',
                    'registering is being downstream', '所识即在下游', 'reading into each condition', '读入每个条件',
                    'apart only downstream', '只在下游不同', 'a route forms by closing', '路线由闭合而形成',
                    'measurement witness', '量度的见证'],
        'dependencies': [
            dep('how-much-difference-arrives',
                '复用 Conveyed、carried 与 carried_pos_iff：差被传到之处；RespondsWithin 与 exchangeGap：耦合强度。',
                'Reuses Conveyed, carried and carried_pos_iff: where a gap is conveyed; RespondsWithin and exchangeGap: '
                'coupling strength.',
                ('差被传到之处；所携带的量；耦合强度。', 'Where a gap is conveyed; the carried amount; coupling strengths.'),
                ('差只往下游去；所携带的量在别处为零；未读入的水平强度为零。',
                 'A gap goes only downstream; the carried amount zero elsewhere; strength zero on levels unread.'),
                ('起始之差只在储量上，部分不给差。', 'The starting gap at the stock alone, none from the part.'),
                'Propagation'),
            dep('how-a-carried-difference-grows',
                '复用 Couples、Coupled、OnLoop 与 Upstream：下游即路线。',
                'Reuses Couples, Coupled, OnLoop and Upstream: downstream is a route.',
                ('耦合、链、回路、上游。', 'Couplings, chains, loops, upstream.'),
                ('差所到之处在下游；所识者在下游。', 'Where a difference arrives lies downstream; what is registered lies downstream.'),
                ('无。', 'None.'), 'Loops'),
            dep('how-loops-form',
                '复用 strengthsBefore、couples_before_*、Closing.split 与 onLoop_of_closing：路线由闭合而形成。',
                'Reuses strengthsBefore, couples_before_*, Closing.split and onLoop_of_closing: a route forms by closing.',
                ('到某步形成的耦合；链的分裂；闭合的回路。', 'Couplings formed by a step; splitting a chain; closing a loop.'),
                ('路线由闭合而形成；量度见证中的回路。', 'A route forms by closing; the loop in the measurement witness.'),
                ('无。', 'None.'), 'Closing'),
            dep(P124,
                '复用 ReadsAt、Through.readsAt、held_while 与 same_step：读一个时程是读入每个条件的特例；见证的进程。',
                'Reuses ReadsAt, Through.readsAt, held_while and same_step: reading a schedule is the case of reading '
                'into each condition alike; the witness courses.',
                ('读一个时程的律；保持直到读。', 'Laws reading a schedule; holding until read.'),
                ('读入每个条件；经识而读者的所识在下游。',
                 'Reading into each condition; what a law reading through registration registers lies downstream.'),
                ('无。', 'None.'), 'Thresholds'),
            dep('counterfactual-is-the-course',
                '复用 ExchangeLaw、Through、Follows 与 ActsAlike：律与两个进程的比较。',
                'Reuses ExchangeLaw, Through, Follows and ActsAlike: the law and the comparison of two courses.',
                ('交换之律；经识而读；进程遵从律。', 'Laws of exchange; reading through registration; courses following a law.'),
                ('只在下游不同。', 'Apart only downstream.'),
                ('无。', 'None.'), 'Counterfactual'),
        ],
        'related': [
            {'id': 'runaway-distance-unregistered',
             'detail': pair('那里观察 obs 是给出的；这里观察是从所观察者出发的所读路线，直接观察是长度为零的路线。',
                            'There observation, obs, is given; here it is a route of readings from what is observed, direct '
                            'observation being the route of length zero.')},
            {'id': 'what-a-cut-loses',
             'detail': pair('复用 CouplesAt：在某步作用的耦合。', 'Reuses CouplesAt: couplings acting at a step.')},
        ],
        'references': [proof(path, actual)] + [proof(LEAN + m + '.lean', names) for m, names in REUSED] + [
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
            {'path': SOURCE, 'role': 'provenance', 'sha256': sha(SOURCE)},
        ],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，按 Ren 同日“approve your approach, please continue”（P125）：一个形成怎样开始观察它所依赖的储量；'
            f'研究 §{SECTION}。',
            f'16 October 2026: added, on Ren\'s “approve your approach, please continue” of the same day (P125): how a '
            f'formation comes to observe a stock it depends on; study section {SECTION}.')],
        'text_versions': [],
    }


NOTE = pair(f'2026-10-16 P125（观察是从所观察者出发的路线，研究 §{SECTION}）：',
            f'16 October 2026, P125 (observation as a route from what is observed, study section {SECTION}): ')
KEEP = pair('陈述与证明不变。', 'Statement and proofs unchanged.')
RELATED = pair('观察是从所观察者出发的所读路线：差别只往下游去，形成只经它所读的、在储量下游的水平识储量；路线由闭合而形成。',
               'Observation is a route of readings from what is observed: a difference goes only downstream, and a formation '
               'registers a stock only through a level it reads downstream of it; a route forms by closing.')


def load(ident):
    return json.loads((REC / f'{ident}.json').read_text())


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80], field[lang].count(old[lang]))
        field[lang] = field[lang].replace(old[lang], new[lang])


def relate(r):
    assert all(x['id'] != ID for x in r['related']), r['id']
    r['related'].append({'id': ID, 'detail': RELATED})


def history(r, zh, en, keep=True):
    r['history'].append({'zh': NOTE['zh'] + zh + (KEEP['zh'] if keep else ''),
                         'en': NOTE['en'] + en + (' ' + KEEP['en'] if keep else '')})


def paired():
    out = []
    r = load(P124)
    replace(r['correspondence'], pair('读法（AI 的，待 Ren）：', "Readings (the AI's, pending Ren): "),
            pair('读法（AI 的，Ren 2026-10-16 同意：“agree in general”）：',
                 "Readings (the AI's, agreed by Ren on 16 October 2026: “agree in general”): "))
    replace(r['next_delta'],
            pair('一个形成怎样开始观察它所依赖的储量；只在高于阈值时', 'How a formation comes to observe a stock it depends on; reading only above'),
            pair('只在高于阈值时', 'Reading only above'))
    replace(r['next_delta'], pair('；独立审查；Ren 对读法的判断。', "; an independent review; Ren's judgment on the readings."),
            pair('；独立审查。', '; an independent review.'))
    thresholds = LEAN + 'Thresholds.lean'
    hits = [x for x in r['references'] if x['role'] == 'proof' and x['path'] == thresholds]
    assert len(hits) == 1
    names = hits[0]['declarations']
    assert names.count('Becoming.Thresholds.le_of_not_lt') == 1
    names[names.index('Becoming.Thresholds.le_of_not_lt')] = 'Becoming.Thresholds.le_of_not_not'
    assert sorted(names) == sorted(declared(thresholds)), set(names) ^ set(declared(thresholds))
    hits[0]['sha256'] = sha(thresholds)
    laws = [l for l in r['laws'] if 'Becoming.Thresholds.le_of_not_lt' in l['declarations']]
    assert len(laws) == 1
    laws[0]['declarations'] = ['Becoming.Thresholds.le_of_not_not' if d == 'Becoming.Thresholds.le_of_not_lt' else d
                               for d in laws[0]['declarations']]
    for ref in r['references']:
        if ref['role'] in ('integration', 'statement'):
            ref['sha256'] = sha(ref['path'])
    assert all(x['path'] != AGREED for x in r['references'])
    r['references'].append({'path': AGREED, 'role': 'provenance', 'sha256': sha(AGREED)})
    relate(r)
    r['history'].append(pair(
        '2026-10-16：Ren 对两项读法与改名答“agree in general”（2026-10-16-thresholds-readings-and-measure-question，加作出处）：'
        '读法标为 Ren 同意；Thresholds.le_of_not_lt 改名为 Thresholds.le_of_not_not（前提是 ¬¬ a ≤ b，新名字恰说所证者），'
        '陈述与证明不变；Thresholds.lean 的模块说明随之改，其证明引用重新取哈希，回执绑定于落地时更新；next_delta 去掉“Ren 对读法的判断”。',
        '16 October 2026: Ren answered the two readings and the renaming with “agree in general” '
        '(2026-10-16-thresholds-readings-and-measure-question, added as provenance): the readings are marked agreed by '
        'Ren; Thresholds.le_of_not_lt is renamed Thresholds.le_of_not_not (its premise is ¬¬ a ≤ b, and the new name '
        'states exactly what it proves), statement and proof unchanged; the Thresholds.lean header changes with it, its '
        'proof reference is rehashed and the receipt binding renewed at landing; next_delta drops “Ren\'s judgment on the '
        'readings”.'))
    history(r, f'下一步中“一个形成怎样开始观察它所依赖的储量”由 {ID} 回答，去掉；related 加 {ID}。',
            f'in the next step, how a formation comes to observe a stock it depends on is answered by {ID} and dropped; '
            f'related adds {ID}.')
    out.append(r)

    r = load('runaway-distance-unregistered')
    replace(r['next_delta'],
            pair('一个形成怎样开始观察它所依赖的储量（这里的策略与回路的连接由 loops-within-what-a-law-reads 给出：只在储量低于阈值时才读它的律，'
                 '断裂之前没有经过储量的回路，回路在断裂处形成）；他者',
                 'How a formation comes to observe a stock it depends on (the connection of the policies here to loops is '
                 'given by loops-within-what-a-law-reads: for a law reading a stock only below a threshold there is no loop '
                 'through the stock before the break, and the loop forms at the break); the policy form'),
            pair('他者', 'The policy form'))
    relate(r)
    history(r, f'下一步的第一项“一个形成怎样开始观察它所依赖的储量”由 {ID} 回答（这里给出的 obs 是从所观察者出发的路线，直接观察是长度为零'
               f'的路线），去掉；related 加 {ID}。',
            f'the first item of the next step, how a formation comes to observe a stock it depends on, is answered by {ID} '
            f'(the obs given here is a route from what is observed, direct observation being the route of length zero) and '
            f'dropped; related adds {ID}.')
    out.append(r)
    return out


def main():
    new = record()
    out = paired()
    for r in [new] + out:
        (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', new['id'], len(new['references'][0]['declarations']), 'declarations; updated',
          ', '.join(r['id'] for r in out))


if __name__ == '__main__':
    main()
