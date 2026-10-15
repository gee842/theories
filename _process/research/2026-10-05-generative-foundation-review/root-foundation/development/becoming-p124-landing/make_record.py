#!/usr/bin/env python3
"""P124: write the schema-2 record loops-within-what-a-law-reads and the paired notes it answers.

usage: python3 -B make_record.py ROOT [SECTION]

References are hashed from ROOT (run after apply_docs.py, so the study and chapter hashes are those
of the applied texts). The receipt reference and the proof bindings are added at landing, so until
then the record names "receipt bound at landing". The declarations listed in the laws are checked
against Becoming/Thresholds.lean, and the reused ones against their modules.

Paired notes: how-a-carried-difference-grows and how-loops-form drop "joining the formation of loops
and Becoming.Runaway's policies within one law" from their next step (how-loops-form also drops
"Ren's judgment on the readings", which Ren gave on 16 October) and relate the new record;
runaway-distance-unregistered's first next-step item, connecting its policies to loops, becomes how a
formation comes to observe a stock, and it relates the new record. Each change asserts the text it
replaces; nothing is written unless every change applies. One history note per record.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTION = int(sys.argv[2]) if len(sys.argv) > 2 else 157
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-16-loop-formation-and-policies-go.md'
REVIEWED = '2026-10-16T00:00:00+00:00'
ID = 'loops-within-what-a-law-reads'


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
    law('一个律读一个时程：对部分之外的每个形成，在所标条件上至该步一致的历史下律给得相同。未读的水平耦合强度为零，所以限于所读的强度'
        '是律的强度。每个读已立者的律读全部；经识而读的律读每个覆盖其识的时程，其进程是经识的策略。',
        'A law reads a schedule when, for each formation outside the part, it gives alike under histories agreeing up to '
        'the step on the conditions marked. An unread level is coupled with strength zero, so the strengths restricted to '
        'what is read are strengths of the law. Every law of what has stood reads everything; a law reading through a '
        'registration reads every schedule covering it, and its courses are policies through registration.',
        ['ExchangeLaw.ReadsAt', 'restrictReads', 'ExchangeLaw.ReadsAt.respondsWithin_unread',
         'ExchangeLaw.ReadsAt.restrict', 'ExchangeLaw.Nonanticipating.readsAt_all', 'ExchangeLaw.Through.readsAt',
         'ExchangeLaw.Through.policyThrough']),
    law('回路在所读之内：限于所读的强度的每个耦合读其水平；汲取回应它所降低的水平只在它读之处；无人读的水平下游只有它自己，没有回路经过它；'
        '回路在一步形成只经过在那一步读其所给之处下游一个水平的形成。',
        'Loops lie within what is read: every coupling of the restricted strengths reads its level; a draw responds to the '
        'level it lowers only where it reads it; downstream of a level nothing reads lies only itself, and no loop passes '
        'through it; a loop forms at a step only through a formation reading there a level downstream of where it gives.',
        ['Thresholds.cond_pos', 'Thresholds.pos_cond', 'couplesAt_reads', 'couplesAt_of_reads', 'couples_reads',
         'self_coupling_reads', 'upstream_unread', 'not_onLoop_unread', 'onLoop_succ_reads']),
    law('无人读者不被带到任何处：对每个读一个时程的律，两个平衡的进程在场的形成相同、部分动作相同、其余遵从律，起始只在一个储量上不同时，'
        '在部分之外无人读这个储量之前，别处都相同，储量之差保持。',
        'What nothing reads is carried nowhere: for every law reading a schedule, two balanced courses with the same '
        'formations present, the part acting alike and the rest following the law, apart at the start only in a stock, '
        'are alike everywhere else, the stock\'s gap held, until something outside the part reads the stock.',
        ['Thresholds.raise_step', 'Thresholds.same_step', 'held_while', 'unread_carried_nowhere']),
    law('断裂：律只在储量低于阈值时才读它，是说储量立于阈值时它只读储量立着；经识而读、部分之外无人观察储量、阈值不低于各自所需者的律都是'
        '这样。对每个这样的律，储量抬高多少，到断裂为止别处都相同、储量高出所抬高者：断裂还有多远不被带到任何处。',
        'The break: a law reads a stock only below a threshold when, while the stock stands at the threshold, it reads only '
        'that it stands; every law reading through a registration in which no formation outside the part observes the '
        'stock, with the threshold at least each need of it, is such a law. For every such law, however much the stock is '
        'raised, up to the break everything else is alike and the stock stands higher by the raise: the distance to the '
        'break is carried nowhere.',
        ['ExchangeLaw.ReadsBelow', 'break_carried_nowhere', 'Thresholds.le_of_not_lt', 'ExchangeLaw.Through.readsBelow']),
    law('断裂之前律就是其立律（储量低于阈值之处读作立于阈值）；立律不读储量，对储量的耦合强度为零，没有经过储量的回路，储量下游只有它自己：'
        '经过储量的回路在断裂处形成。储量在条件中由给出的标记标出，不判定条件。',
        'Before the break the law is its standing law, reading the stock as standing at its threshold wherever it stands '
        'below it; the standing law does not read the stock, is coupled to it with strength zero and has no loop through '
        'it, only the stock lying downstream of it: the loop through the stock forms at the break. The stock is '
        'marked among the conditions by a marking given with it, so no decision on conditions is used.',
        ['standAt', 'offStock', 'ExchangeLaw.standing', 'standAt_stock', 'standAt_unmarked', 'standAt_of_stands',
         'offStock_stock', 'offStock_other', 'ExchangeLaw.ReadsBelow.standing_readsAt',
         'ExchangeLaw.ReadsBelow.standing_unread', 'ExchangeLaw.ReadsBelow.standing_no_loop',
         'ExchangeLaw.Nonanticipating.standing_alike', 'Flow.follows_standing_before']),
    law('汲取的见证：一个形成在储量立于 N + 1 时每步从储量汲取一个单位给产物，只在低于 N + 1 时读储量。它的每个强度都把储量耦合到自身，'
        '一圈的回路，而断裂之前它给得如其立律，对储量强度为零；一步上一个进程的储量低于阈值、抬高者的立着，那一步抬高者多给产物一。',
        'The draw witness: a formation draws one unit from a stock and gives it to a product at each step while the stock '
        'stands at N + 1, reading the stock only below N + 1. Every strengths of it couple the stock into itself, a loop of '
        'one, while before the break it gives as its standing law, with strength zero from the stock; at a step where one '
        'course\'s stock stands below the threshold and a raised one\'s at it, the raised course gives one more to the '
        'product across that step.',
        ['Thresholds.Draw.law', 'Thresholds.Draw.nonanticipating', 'Thresholds.Draw.reads',
         'Thresholds.Draw.strength_pos', 'Thresholds.Draw.onLoop', 'Thresholds.Draw.only', 'Thresholds.Draw.forms_at_break',
         'Thresholds.Draw.diverges_at_break']),
]

REUSED = [
    ('Counterfactual', ['Becoming.ExchangeLaw', 'Becoming.ExchangeLaw.GivesAlike', 'Becoming.ExchangeLaw.Nonanticipating',
                        'Becoming.ExchangeLaw.Through', 'Becoming.Flow.Follows', 'Becoming.Flow.ActsAlike',
                        'Becoming.Flow.totals_alike_of_each']),
    ('Propagation', ['Becoming.ExchangeLaw.RespondsWithin', 'Becoming.ExchangeLaw.exchangeGap',
                     'Becoming.ExchangeLaw.exchangeGap_of_alike', 'Becoming.gap', 'Becoming.gap_add_self']),
    ('Loops', ['Becoming.Couples', 'Becoming.Coupled', 'Becoming.OnLoop', 'Becoming.Upstream', 'Becoming.Loops.beq_self',
               'Becoming.Loops.ble_succ_self']),
    ('Remainder', ['Becoming.CouplesAt', 'Becoming.couples_iff_couplesAt']),
    ('Closing', ['Becoming.strengthsBefore', 'Becoming.onLoop_succ_iff', 'Becoming.Closing.ble_false_of_lt']),
    ('Runaway', ['Becoming.Flow.PolicyThrough']),
    ('Testing', ['Becoming.Web.Registers', 'Becoming.Web.RegistersAlikeUpTo']),
    ('Flow', ['Becoming.Flow', 'Becoming.Flow.Balances', 'Becoming.Flow.taken', 'Becoming.Flow.given']),
    ('Dependence', ['Becoming.Web', 'Becoming.add_right_cancel']),
    ('Admission', ['Becoming.Web.Admits']),
    ('Feedback', ['Becoming.Web.DependsOn']),
    ('Recurrence', ['Becoming.le_succ_cases']),
    ('Generation', ['Becoming.total']),
]


def record():
    path = LEAN + 'Thresholds.lean'
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
        'title': pair('回路在律所读之内，经过储量的回路在断裂处形成',
                      'Loops lie within what a law reads, and the loop through a stock forms at its break'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '未读的水平耦合强度为零，所以回路在律所读之内，在读增长之处形成；对每个只在储量低于阈值时才读它的律，储量的抬高到断裂为止不被带到'
            '任何处，断裂之前没有经过储量的回路：经过储量的回路在断裂处形成。',
            'An unread level is coupled with strength zero, so loops lie within what a law reads and form where reading '
            'grows; for every law reading a stock only below a threshold, a raise is carried nowhere up to the break, with '
            'no loop through the stock before it: that loop forms at the break.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。各定理所写者写在定理中：律所读的时程（ReadsAt）或只在储量低于阈值时才读它（ReadsBelow）；强度 k 是给出的界；'
            '两个进程平衡、在场的形成相同、部分动作相同、其余遵从律，起始只在储量上不同；立律与断裂之前的一致要求律读已立者。',
            'No axiom. What each theorem needs is written into it: the schedule a law reads (ReadsAt) or its reading a stock '
            'only below a threshold (ReadsBelow); the strengths k as supplied bounds; two balanced courses with the same '
            'formations present, the part acting alike and the rest following the law, apart at the start only in the '
            'stock; the agreement with the standing law before the break needs the law to read what has stood.')],
        'does_not_show': [
            {**pair('一个形成怎样开始观察它所依赖的储量；律读什么、阈值在哪里。',
                    'How a formation comes to observe a stock it depends on; which schedule a law reads and where its '
                    'threshold lies.'), 'kind': 'scope'},
            {**pair('只在高于阈值时才读或其他形状的读：抬高可能改变读，未陈述。',
                    'Reading only above a threshold, or in other shapes: a raise may change the reading, not stated.'),
             'kind': 'scope'},
            {**pair('与 Becoming.Runaway 的“其余固定”比较强弱：那里其余任意而固定，这里其余遵从律而不必固定，两者都不蕴含另一个。',
                    'A comparison with the rest fixed in Becoming.Runaway: there the rest is arbitrary but fixed, here it '
                    'follows the law without being fixed, and neither implies the other.'), 'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': path,
             'detail': pair('汲取的见证：律的每个强度都把储量耦合到自身，强度之界看不出回路只在断裂处闭合；断裂之前的动力学是没有这个回路的立律。',
                            'The draw witness: every strengths of the law couple the stock into itself, so a bound on '
                            'strengths does not show that the loop closes only at the break; before the break the '
                            'dynamics are those of the standing law, which has no such loop.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Thresholds 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Thresholds, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '一个形成怎样开始观察它所依赖的储量；只在高于阈值时或其他形状的读；断裂之后实际的失控（回应的下界）；独立审查；Ren 对读法的判断。',
            'How a formation comes to observe a stock it depends on; reading only above a threshold, or in other shapes; the '
            'actual runaway after the break (lower bounds on responses); an independent review; Ren\'s judgment on the '
            'readings.'),
        'correspondence': pair(
            'Ren 2026-10-16 取的 P118 第三项读法与 P122 留下“一个形成的汲取开始回应其汲取所降低的水平，那里与 Becoming.Runaway 相遇”；'
            'AI 问是否开始把回路的形成与 Runaway 的策略接起来，Ren 答“please”。本结果在一个律中接起来。读法（AI 的，待 Ren）：失控的断裂就是'
            '回路形成之处，Becoming.Runaway 的不识与 Becoming.Closing 的形成是同一件事的两面；能识距离者是断裂之前对储量水平的读，它使'
            '回路更早形成。',
            'P118\'s third reading as Ren took it on 16 October 2026, and P122, left open “where a formation\'s drawing comes '
            'to respond to the level its drawing lowers, where this meets Becoming.Runaway”; asked whether to start joining '
            'loop formation with Runaway\'s policies, Ren wrote “please”. This result joins them within one law. Readings '
            '(the AI\'s, pending Ren): a runaway\'s break is where a loop forms, the blindness of Becoming.Runaway and the '
            'formation of Becoming.Closing being one event seen from two sides; what registers the distance is a reading of '
            'the stock\'s level before the break, which forms the loop earlier.'),
        'canonical_source': path,
        'aliases': ['loops within what a law reads', '回路在律所读之内', 'what a law reads', '律所读', 'reading bounds coupling',
                    '读限制耦合', 'the break', '断裂', 'standing law', '立律', 'stock read only below a threshold',
                    '只在低于阈值时才读的储量', 'distance to the break carried nowhere', '断裂还有多远不被带到任何处',
                    'draw witness', '汲取的见证'],
        'dependencies': [
            dep('counterfactual-is-the-course',
                '复用 ExchangeLaw、GivesAlike、Nonanticipating、Through、Follows、ActsAlike 与 totals_alike_of_each：律、读与两个进程的比较。',
                'Reuses ExchangeLaw, GivesAlike, Nonanticipating, Through, Follows, ActsAlike and totals_alike_of_each: the '
                'law, its reading and the comparison of two courses.',
                ('交换之律；经识而读；进程遵从律。', 'Laws of exchange; reading through registration; courses following a law.'),
                ('读一个时程的律；只在低于阈值时读储量的律；两个进程的保持。',
                 'Laws reading a schedule; laws reading a stock only below a threshold; holding across two courses.'),
                ('无。', 'None.'), 'Counterfactual'),
            dep('how-much-difference-arrives',
                '复用 RespondsWithin、exchangeGap 与 gap：耦合强度。',
                'Reuses RespondsWithin, exchangeGap and gap: coupling strength.',
                ('耦合强度。', 'Coupling strengths.'),
                ('未读的水平强度为零；限于所读的强度；见证的强度为正。',
                 'Strength zero on unread levels; restricted strengths; positive strength in the witness.'),
                ('无。', 'None.'), 'Propagation'),
            dep('how-a-carried-difference-grows',
                '复用 Couples、Coupled、OnLoop 与 Upstream：回路在所读之内。',
                'Reuses Couples, Coupled, OnLoop and Upstream: loops lie within what is read.',
                ('耦合、链、回路、上游。', 'Couplings, chains, loops, upstream.'),
                ('每个耦合读其水平；没有回路经过无人读的水平。',
                 'Every coupling reads its level; no loop passes through a level nothing reads.'),
                ('无。', 'None.'), 'Loops'),
            dep('how-loops-form',
                '复用 strengthsBefore 与 onLoop_succ_iff：回路在读增长之处形成。',
                'Reuses strengthsBefore and onLoop_succ_iff: loops form where reading grows.',
                ('到某步形成的回路；回路由闭合而形成。', 'Loops formed by a step; a loop forms by closing.'),
                ('回路在一步形成只经过在那一步读的形成。', 'A loop forms at a step only through a formation reading there.'),
                ('无。', 'None.'), 'Closing'),
            dep('runaway-distance-unregistered',
                '复用 Flow.PolicyThrough：经识而读之律的进程是经识的策略；断裂不被识对整个律成立。',
                'Reuses Flow.PolicyThrough: the courses of a law reading through registration are policies through it; '
                'the break unregistered holds for whole laws.',
                ('经识的策略；断裂之前储量抬高不被识。', 'Policies through registration; a raise unregistered before the break.'),
                ('对每个只在低于阈值时读储量的律，抬高到断裂为止不被带到任何处。',
                 'For every law reading a stock only below a threshold, a raise carried nowhere up to the break.'),
                ('其余遵从律（不是其余固定）。', 'The rest following the law (not the rest fixed).'), 'Runaway'),
        ],
        'related': [
            {'id': 'what-a-cut-loses',
             'detail': pair('复用 CouplesAt：在某步作用的耦合。', 'Reuses CouplesAt: couplings acting at a step.')},
            {'id': 'every-origin-passes-the-gate',
             'detail': pair('那里识与检验之门；这里识限制耦合，回路在所读之内。',
                            'There the gate of registration and testing; here registration bounds coupling, and loops lie '
                            'within what is read.')},
        ],
        'references': [proof(path, actual)] + [proof(LEAN + m + '.lean', names) for m, names in REUSED] + [
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
            {'path': SOURCE, 'role': 'provenance', 'sha256': sha(SOURCE)},
        ],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，按 Ren 同日“please”（P124）：在一个律中把回路的形成与 Becoming.Runaway 的策略接起来；研究 §{SECTION}。',
            f'16 October 2026: added, on Ren\'s “please” of the same day (P124): joining loop formation and '
            f'Becoming.Runaway\'s policies within one law; study section {SECTION}.')],
        'text_versions': [],
    }


NOTE = pair(f'2026-10-16 P124（回路在律所读之内，与断裂，研究 §{SECTION}）：',
            f'16 October 2026, P124 (loops within what a law reads, and the break, study section {SECTION}): ')
KEEP = pair('陈述与证明不变。', 'Statement and proofs unchanged.')
RELATED = pair('在一个律中：回路在所读之内，在读增长之处形成；只在储量低于阈值时才读它的律，断裂之前没有经过储量的回路，回路在断裂处形成。',
               'Within one law: loops lie within what is read and form where reading grows; for a law reading a stock only '
               'below a threshold there is no loop through the stock before the break, and the loop forms at the break.')


def load(ident):
    return json.loads((REC / f'{ident}.json').read_text())


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80], field[lang].count(old[lang]))
        field[lang] = field[lang].replace(old[lang], new[lang])


def relate(r):
    assert all(x['id'] != ID for x in r['related']), r['id']
    r['related'].append({'id': ID, 'detail': RELATED})


def history(r, zh, en):
    r['history'].append({'zh': NOTE['zh'] + zh + KEEP['zh'], 'en': NOTE['en'] + en + ' ' + KEEP['en']})


def paired():
    out = []
    r = load('how-a-carried-difference-grows')
    replace(r['next_delta'], pair('在一个律中把回路的形成与 Becoming.Runaway 的策略连起来；',
                                  "joining the formation of loops and Becoming.Runaway's policies within one law; "),
            pair('', ''))
    relate(r)
    history(r, f'下一步中“在一个律中把回路的形成与 Becoming.Runaway 的策略连起来”由 {ID} 回答，去掉；related 加 {ID}。',
            f"in the next step, “joining the formation of loops and Becoming.Runaway's policies within one law” is "
            f'answered by {ID} and dropped; related adds {ID}.')
    out.append(r)

    r = load('how-loops-form')
    replace(r['next_delta'], pair('把形成与 Becoming.Runaway 的策略在一个律中连起来；独立审查；Ren 对读法的判断。',
                                  "joining formation and Becoming.Runaway's policies within one law; an independent review; "
                                  "Ren's judgment on the readings."),
            pair('独立审查。', 'an independent review.'))
    old = pair('两者在一个律中的连接未陈述。', 'Joining the two within one law is not stated.')
    new = pair(f'两者在一个律中的连接见 {ID}。', f'Joining the two within one law: {ID}.')
    hits = [x for x in r['related'] if x['id'] == 'runaway-distance-unregistered']
    assert len(hits) == 1
    replace(hits[0]['detail'], old, new)
    relate(r)
    history(r, f'下一步中“把形成与 Becoming.Runaway 的策略在一个律中连起来”由 {ID} 回答，“Ren 对读法的判断”已于 2026-10-16 给出'
               f'（2026-10-16-routes-closing-readings），都去掉；related 中与 runaway-distance-unregistered 的连接指向 {ID}，并加 {ID}。',
            f"in the next step, “joining formation and Becoming.Runaway's policies within one law” is answered by {ID} and "
            "“Ren's judgment on the readings” was given on 16 October (2026-10-16-routes-closing-readings), so both are "
            f'dropped; in related the joining with runaway-distance-unregistered points to {ID}, and {ID} is added.')
    out.append(r)

    r = load('runaway-distance-unregistered')
    replace(r['next_delta'],
            pair('把这里的策略与回路相连：形成的汲取回应其自身汲取所降低的水平时，汲取与水平组成一个回路（具有给定耦合强度时，回路的一般定义与绕回路的失控由 '
                 'how-a-carried-difference-grows 给出，回路的形成由 how-loops-form 给出）；',
                 "Connect the policies here to loops: where a formation's draw responds to a level its own draw lowers, draw and "
                 'level form a loop (for laws with given coupling strengths, a loop in general and the runaway around it are '
                 'given by how-a-carried-difference-grows, and how a loop forms by how-loops-form);'),
            pair(f'一个形成怎样开始观察它所依赖的储量（这里的策略与回路的连接由 {ID} 给出：只在储量低于阈值时才读它的律，断裂之前没有经过'
                 '储量的回路，回路在断裂处形成）；',
                 'How a formation comes to observe a stock it depends on (the connection of the policies here to loops is '
                 f'given by {ID}: for a law reading a stock only below a threshold there is no loop through the stock before '
                 'the break, and the loop forms at the break);'))
    relate(r)
    history(r, f'下一步的第一项“把这里的策略与回路相连”由 {ID} 回答，改为一个形成怎样开始观察它所依赖的储量；related 加 {ID}。',
            f'the first item of the next step, connecting the policies here to loops, is answered by {ID} and becomes how a '
            f'formation comes to observe a stock it depends on; related adds {ID}.')
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
