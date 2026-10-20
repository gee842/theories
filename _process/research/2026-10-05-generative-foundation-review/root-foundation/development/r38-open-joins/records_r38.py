#!/usr/bin/env python3
"""R38 (20 October 2026): extend R33's records of G6 and G10 with what R38 proves (run once, after the
checker run; the hash-only re-points of other records go through tools/research/repoint.py).

usage (from the checkout root): python3 -B records_r38.py RECEIPT_ID

* whether-a-loop-closes-a-difference (G6): one turn around a cycle of exact links stated exactly, the
  excess over the return map's course, the exact premise of equality, the ring on which the bound is
  strict (a counterexample to equality for two or more conditions), and Rejoining's gap as a return map
  where the courses' exchanges respond to it, with the witness's counterexample across the act; a
  dependency on where-two-courses-rejoin.
* the-world-an-interleaving-builds (G10): the own count and the standing after own exchanges, the index
  map with its laws, the matching of each relatum's exchanges and the readings the same for every
  interleaving; the open part restated (one renumbering of the steps and Reordering's footprint), and
  what the relation gives the necessity target and the premise card's shared index.
Each record gets a history note; the proof binding of the changed Lean file is rebound to the receipt."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
B = LEAN + 'becoming/Becoming/'
RID = sys.argv[1]
RECEIPT = LEAN + f'becoming/becoming-checks/{RID}/verification.json'
receipt = json.loads((ROOT / RECEIPT).read_text())
assert receipt['status'] == 'passed'
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
STUDY_SECTION = sys.argv[2] if len(sys.argv) > 2 else '233'


def h(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def load(i):
    return json.loads((REC / f'{i}.json').read_text())


def save(d):
    (REC / f"{d['id']}.json").write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('wrote', d['id'])


def t(en, zh):
    return {'en': en, 'zh': zh}


def rebind(d, src, module):
    assert receipt['source_sha256'][module] == h(src), module
    for b in d['proof_bindings']:
        if b['source'] == src:
            b['receipt'] = RECEIPT
    for r in d['references']:
        if r['path'] == src:
            r['sha256'] = h(src)
    if not any(r['path'] == RECEIPT for r in d['references']):
        d['references'].append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})


def add_decls(d, src, names):
    for r in d['references']:
        if r['path'] == src:
            for x in names:
                if x not in r['declarations']:
                    r['declarations'].append(x)
            return
    raise KeyError(src)


# ---------------------------------------------------------------- G6
LR = B + 'LoopReturn.lean'
P = 'Becoming.LoopReturn.'
d = load('whether-a-loop-closes-a-difference')
d['statement'] = t(  # the statement's length limits (300 en, 150 zh): rewritten whole
    'A loop closes a difference only through a link giving back less than it received; with whole-number factors it '
    'closes at once, keeps it or runs away. Around a cycle of exact links one turn is the return map\'s course plus what '
    'the cycle held, strictly more for two or more conditions.',
    '回路只经给回少于所受的环节闭合差别；整数倍率下立即闭合、保持或失控。绕精确环节之回路，一圈是回返映射的进程加回路所持者，'
    '两个或更多条件时严格更多。')
cycle = [P + x for x in ('GivesExactly', 'heldAlong', 'link_rearranged', 'carried_along_exact', 'carried_around_exact',
                         'carried_around_excess', 'around_course_iff')]
ring = [P + x for x in ('RingGives', 'ring_even', 'product_const', 'one_add_pow_lt', 'Ring.pred', 'Ring.conditions',
                        'Ring.strengths', 'Ring.amount', 'Ring.cycle', 'Ring.cycle_start', 'Ring.cycle_back',
                        'Ring.pred_cycle', 'Ring.pred_mem', 'Ring.cycle_mem', 'Ring.total_at', 'Ring.gives',
                        'Ring.coupled', 'Ring.givesExactly', 'Ring.amount_eq', 'Ring.exceeds_course',
                        'Ring.bound_strict')]
rejoin = [P + x for x in ('gap_add_right', 'RespondsByReturn', 'gap_succ', 'responds_iff', 'gap_course', 'gap_scaling',
                          'replenishing_responds', 'replenishing_course', 'replenishing_no_return')]
d['laws'] += [
    {'en': 'Around a cycle of m + 1 links each giving exactly its strength (at every step and from any levels the '
           'formations present give into the next condition exactly w i times the current level of the one before, and '
           'nothing else), the carried amount at the loop one turn after t is the product of the strengths times the '
           'carried amount at t, with what the loop held at t + m and the last strength times what the intermediate '
           'conditions held as the turn passed them, carried on by the strengths after them; so it is the return map\'s '
           'course after one turn with what the loop gained over the turn\'s first m steps and that carried-on amount, '
           'and equal to the course exactly where both are nothing. carried_along_exact states carried_along\'s bound '
           'with what it leaves out.',
     'zh': '绕 m + 1 个环节、每个恰按其强度给出的回路（每一步、对任何水平，在场的形成给下一个条件的恰是 w i 乘前一条件的当前水平，'
           '此外无他），t 之后一圈回路所携带的量，是诸强度之积乘 t 时的携带量，加上回路在 t + m 所持，再加最后一个强度乘中间条件在这一圈'
           '经过时所持、由其后强度继续传下者；所以它是回返映射一圈后的进程，加上回路在这一圈前 m 步所增与那继续传下的量，二者皆无时恰等于'
           '该进程。carried_along_exact 陈述 carried_along 之界及其所略。',
     'declarations': cycle},
    {'en': 'On a ring of m + 2 conditions, each receiving exactly w times the current level of the one before, every '
           'condition starting at D, each condition grows as a self-loop of strength w would, (1 + w) ^ t * D; since '
           '1 + w ^ (m + 2) < (1 + w) ^ (m + 2) for a positive w, carried_around_course\'s bound holds on this ring\'s '
           'cycle (it is coupled with strength w at every step) and is strict from a positive D: equality to the '
           'return map\'s course fails around every cycle of two or more conditions, and holds for one '
           '(selfLoop_carried).',
     'zh': '在 m + 2 个条件的环上，每个条件恰收到前一条件当前水平的 w 倍，各条件都从 D 开始，则每个条件都像强度 w 的自回路那样增长，'
           '为 (1 + w) ^ t * D；因正的 w 有 1 + w ^ (m + 2) < (1 + w) ^ (m + 2)，carried_around_course 之界在此环的回路上成立'
           '（每一步都以强度 w 耦合），且自正的 D 起为严格：绕两个或更多条件的每个回路，与回返映射进程的相等都不成立；一个条件时成立'
           '（selfLoop_carried）。',
     'declarations': ring},
    {'en': 'A difference at one condition of Rejoining as a return map: where two flows balance on c and, from step s, '
           'each course\'s level of c with what it gives c and what the other takes stand at f of the gap before '
           '(RespondsByReturn, exactly the gap\'s step, responds_iff), the gap at s + n is f\'s course after n turns, '
           'one turn a step; for a response linear in the gap (a loop of multiplying links) it is the product of the '
           'factors to the n times the gap at s, so whole_factors applies. In Rejoining\'s witness the responder '
           'responds by taking one off from the act on; from the start, across the act, the gap 0, 1, 0, 0 is the '
           'course of no map.',
     'zh': '把 Rejoining 在一个条件上的差别读作回返映射：两流在 c 上平衡，且自第 s 步起每条进程的 c 之水平加其给 c 者与另一条所取者，'
           '与另一条相应之和的差距为此前差距的 f（RespondsByReturn，恰为差距的一步，responds_iff），则 s + n 时的差距是 f 的 n 圈进程，'
           '一步一圈；对差距为线性的回应（相乘环节的回路），它是倍率之积的 n 次方乘 s 时的差距，故 whole_factors 适用。在 Rejoining 的'
           '见证中，自该行动起回应者以减一回应；自起点、跨过该行动，差距 0、1、0、0 不是任何映射的进程。',
     'declarations': rejoin},
]
d['hypotheses'].append(t(
    'For the exact turn: each link of the cycle is the only giving into the condition it gives to, at exactly its '
    'strength, read off the current level (GivesExactly; the ring meets it). For Rejoining\'s gap: the two flows balance '
    'on the condition at every step and their exchanges respond to the gap by a map from step s (RespondsByReturn), '
    'which is taken as given, not derived from a law of exchange.',
    '精确一圈：回路的每个环节是给其所给条件的唯一给予，恰按其强度、读当前水平（GivesExactly；环满足之）。Rejoining 的差距：'
    '两流在该条件上每一步平衡，且自第 s 步起其交换按某映射回应差距（RespondsByReturn），此为所设，非由交换律推出。'))
d['does_not_show'] = [
    t('A loop of Rejoining where the difference is many numbers: the reading is of the gap at one condition, and that '
      'the exchanges respond to it by a map is a premise.',
      '差别为多个数时 Rejoining 的回路：此读法读的是一个条件上的差距，且交换按映射回应它是前提。') | {'kind': 'scope'},
    d['does_not_show'][1],
    t('The carried amount around a cycle exactly where links read more than the current level of the one before, or '
      'other formations give into the cycle: there the exact turn does not apply and the bound is what holds.',
      '环节所读不止前一条件的当前水平、或另有形成给入回路时，绕回路所携带的量的精确值：那里精确一圈不适用，所成立的是界。')
    | {'kind': 'scope'},
]
d['counterexamples'] = [
    {'path': LR, 'detail': t(
        'LoopReturn.Ring.bound_strict: on the ring of m + 2 conditions with a positive strength, every condition '
        'starting at the same positive amount, the carried amount one turn on is strictly above the return map\'s '
        'course; equality to the course fails for every cycle of two or more conditions.',
        'LoopReturn.Ring.bound_strict：在正强度、各条件自相同的正量出发的 m + 2 个条件之环上，一圈后的携带量严格高于回返映射的进程；'
        '对两个或更多条件的每个回路，与进程的相等都不成立。')},
    {'path': LR, 'detail': t(
        'LoopReturn.replenishing_no_return: without the premise that the exchanges respond to the gap, the gap at one '
        'condition need not be the course of any map (Rejoining\'s witness, across the act: 0, 1, 0, 0).',
        'LoopReturn.replenishing_no_return：没有交换回应差距这一前提，一个条件上的差距不必是任何映射的进程（Rejoining 的见证，'
        '跨过该行动：0、1、0、0）。')},
]
d['next_delta'] = t(
    'Real factors, where a multiplication below one closes gradually; a law of exchange whose response is a map of the '
    'gap, derived rather than supplied; the difference at many conditions as a return map on their levels; an '
    'independent review.',
    '实数倍率，其中小于一的乘法逐步闭合；回应为差距之映射的交换律，由推导而非所设；把多个条件上的差别读作其水平上的回返映射；独立审查。')
if not any(x['id'] == 'where-two-courses-rejoin' for x in d['dependencies']):
    d['dependencies'].append({
        'id': 'where-two-courses-rejoin', 'relation': 'formal-reuse',
        'detail': t('Reuses Rejoining\'s balanced flows, its witness Replenishing (flow, web, balances) and its reading of '
                    'the difference at one condition.',
                    '复用 Rejoining 的平衡流、其见证 Replenishing（流、网、平衡）及其对一个条件上差别的读法。'),
        'interface': {'output': t('Two balanced flows and the difference at a condition; the witness in which a responder '
                                  'gives back what an act took.',
                                  '两个平衡流及一个条件上的差别；回应者给回行动所取的见证。'),
                      'input': t('The gap at one condition as a return map\'s course, and the countermodel across the act.',
                                 '一个条件上的差距作为回返映射的进程，及跨过该行动的反模型。'),
                      'conditions': t('The flows balance on the condition; the exchanges respond to the gap by a map.',
                                      '两流在该条件上平衡；交换按映射回应差距。'),
                      'evidence': B + 'Rejoining.lean'}})
rebind(d, LR, 'Becoming.LoopReturn')
add_decls(d, LR, cycle + ring + rejoin)
if not any(r['path'] == B + 'Rejoining.lean' for r in d['references']):
    d['references'].append({'path': B + 'Rejoining.lean', 'role': 'proof', 'sha256': h(B + 'Rejoining.lean'),
                            'declarations': ['Becoming.Replenishing.flow', 'Becoming.Replenishing.web',
                                             'Becoming.Replenishing.balances']})
d['aliases'] += [x for x in ('exact turn around a cycle', '回路一圈的精确值', P + 'around_course_iff',
                             P + 'Ring.bound_strict', P + 'gap_course') if x not in d['aliases']]
d['reviewed_at_utc'] = NOW
d['history'].append(t(
    f'20 October 2026, R38 (the open parts of R33\'s G6): three laws added (the exact turn around a cycle of exact '
    f'links and its excess over the return map\'s course, with the exact premise of equality; the ring on which the '
    f'bound is strict, the counterexample to equality for two or more conditions; Rejoining\'s gap at one condition as '
    f'a return map where the exchanges respond to it, with the witness\'s counterexample across the act), the premises '
    f'they take, two counterexamples, a dependency on where-two-courses-rejoin; the two open items of R33 replaced by '
    f'what stays open. Proof binding (LoopReturn.lean) rebound to core receipt {RID}. Study section {STUDY_SECTION}.',
    f'2026年10月20日，R38（R33 之 G6 的开放部分）：新增三条规律（精确环节之回路的精确一圈及其超出回返映射进程者，附相等的确切前提；'
    f'界为严格的环，即两个或更多条件时相等的反例；Rejoining 在一个条件上的差距在交换回应它之处作为回返映射，附跨过行动的见证反例）、'
    f'其所取前提、两个反例、对 where-two-courses-rejoin 的依赖；R33 的两项开放项换为仍开放者。证明绑定（LoopReturn.lean）'
    f'改到核心回执 {RID}。研究第 {STUDY_SECTION} 节。'))
save(d)

# ---------------------------------------------------------------- G10
IL = B + 'Interleavings.lean'
Q = 'Becoming.Interleavings.LocalLaw.'
Q0 = 'Becoming.Interleavings.'
d = load('the-world-an-interleaving-builds')
d['statement'] = t(  # the statement's length limits (300 en, 150 zh): rewritten whole
    'From a local law and a list of exchanges a World of the spine is built whose steps balance. For any two '
    'interleavings of the same own courses an index map for each relatum matches its standings step by step, so what '
    'is read through its own steps is the same for every interleaving.',
    '由局部律与交换之列构造出脊柱的一个世界，其各步平衡。对同一自身进程的任意两个交错，每个关系项的索引映射逐步相配其所立，'
    '所以经其自身各步读出者对每个交错都相同。')
own = [Q + x for x in ('ownCount', 'standingAfter', 'ownCount_true', 'ownCount_false', 'ownCount_zero', 'runUpTo_own',
                       'standingAfter_of_interleavings', 'runUpTo_of_own', 'world_own', 'world_of_own')] + \
      [Q + 'afterOwn', Q + 'afterOwn_zero']
index = [Q + x for x in ('ownCount_le', 'firstAt', 'firstAt_true', 'firstAt_false', 'ownCount_firstAt', 'firstAt_least',
                         'indexMap', 'length_of_interleavings', 'ownCount_index', 'runUpTo_index', 'world_index',
                         'exchangeAt_lt', 'exchangeAt_own', 'firstAt_succ_step', 'index_matches')]
reads = [Q + 'world_reads_alike']
d['laws'] += [
    {'en': 'A relatum\'s standing at step t of a list is its standing after the own exchanges the first t exchanges hold '
           '(ownCount, standingAfter). So in two interleavings of the same courses, with the relata listed, a relatum '
           'stands alike at any two steps, one in each world, at which it has taken equally many of its own exchanges.',
     'zh': '关系项在一列的第 t 步所立，是它在前 t 个交换所含的自身交换之后所立（ownCount、standingAfter）。所以关系项列出时，'
           '在同一进程的两个交错中，关系项在任意两步（各在一个世界）所立相同，只要到那时它已取同样多的自身交换。',
     'declarations': own},
    {'en': 'The index map for a relatum sends a step of one list to the least step of the other at which the relatum has '
           'taken as many of its own exchanges (firstAt is that least step; ownCount_index); a relatum stands at step t '
           'of one world where it stands at the mapped step of the other. Where it takes an exchange at step t of one '
           'list, the map sends t + 1 to the step after the one at which it takes the same exchange in the other.',
     'zh': '关系项的索引映射把一列的一步送到另一列中该关系项已取同样多自身交换的最早一步（firstAt 即那最早一步；ownCount_index）；'
           '关系项在一个世界第 t 步所立，等于它在另一世界映射所给那一步所立。它在一列第 t 步取一个交换处，映射把 t + 1 送到它在另一列'
           '取同一交换那一步之后一步。',
     'declarations': index},
    {'en': 'What is read through a relatum\'s own steps is the same for every interleaving: for every property of a '
           'standing, a relatum has it at some step of one world exactly where at some step of the other, and at every '
           'step of one exactly where at every step of the other.',
     'zh': '经关系项自身各步读出者，对每个交错都相同：对所立的每个性质，关系项在一个世界某步具有它，恰当它在另一世界某步具有它；'
           '在一个世界每步具有，恰当在另一世界每步具有。',
     'declarations': reads},
]
d['hypotheses'] = [t(
    'No axiom. A local law on whole-number standings for the world (the laws of own steps hold for any states); the '
    'relata listed, once where balance is stated; relata told apart for the move. The courses are finite lists.',
    '不加公理。世界取整数所立上的局部律（关于自身各步的规律对任何状态成立）；关系项列出，陈述平衡处恰列一次；为动区分关系项。'
    '进程是有限列。')]
d['does_not_show'] = [
    t('One renumbering of all the steps carrying one interleaving\'s world to the other\'s: the index maps are one for '
      'each relatum, and a relation reading two relata at one step of the shared index (which stand together at a '
      'step) is not shown the same for every interleaving.',
      '把一个交错之世界带到另一个之世界的、所有步的单一重编号：索引映射是每个关系项各一个，读共同指标同一步上两个关系项的关系'
      '（哪些在同一步共同所立）未证对每个交错相同。') | {'kind': 'scope'},
    t('The correspondence with the footprint of Becoming.Reordering (Footprinted, Reindexes, converse): there a relatum '
      'a step does not touch is unmoved across it, activity included, while this world marks a relatum active exactly '
      'at the steps whose exchange touches it, so the footprint of the exchanges does not contain them; and Reindexes '
      'needs each exchange\'s occurrence matched in the two lists, which needs the maps of the relata an exchange '
      'touches to agree.',
      '与 Becoming.Reordering 之足迹（Footprinted、Reindexes、converse）的对应：那里一步不触及的关系项跨此步不动，活跃也包括在内，'
      '而此世界恰在其交换触及关系项之步标其为活跃，所以交换的足迹不包含它们；且 Reindexes 需要每个交换在两列中的出现相配，这需要'
      '一个交换所触及诸关系项的映射彼此一致。') | {'kind': 'correspondence'},
    d['does_not_show'][2],
]
d['next_delta'] = t(
    'One renumbering of the steps matching each exchange\'s occurrence across the relata it touches; then the '
    'correspondence with Becoming.Reordering through a footprint containing the world\'s activity; courses without '
    'end; an independent review.',
    '与每个交换所触及诸关系项相配其出现的单一步重编号；然后经包含世界之活跃的足迹与 Becoming.Reordering 对应；无尽的进程；独立审查。')
d['correspondence'] = t(
    d['correspondence']['en'] + ' With the index map (R38), what the world says of each relatum, read through its own '
    'steps, is the same for every interleaving: the premise card\'s one shared index (§0, block A) commits, for what is '
    'read per relatum, to no more than a choice among interleavings, which moves where on the index a standing falls '
    'and not which standings a relatum passes through or in what order. For the necessity target (the deductive '
    'necessity of the whole, item 1 of §8.1, and the representation criterion K4) this makes the shared index a reading '
    'wherever a law is read through each relatum\'s own steps; a law that reads several relata at one step of the index '
    'is still read on a chosen interleaving, which is what one renumbering of the steps would settle.',
    d['correspondence']['zh'] + '有了索引映射（R38），世界关于每个关系项所说者，经其自身各步读出，对每个交错都相同：前提卡上唯一'
    '的共同指标（§0，A 区）对按关系项读出者而言，只承诺在诸交错中作一选择，这选择移动的是所立落在指标的何处，而非关系项经过哪些所立'
    '或按何次序。对必然性目标（整体的演绎必然性，§8.1 第 1 项，及表示判据 K4），这使共同指标在每条经各关系项自身各步读出的规律处'
    '成为一个读法；在指标同一步读几个关系项的规律仍在所选的交错上读出，这正是单一步重编号将解决者。')
rebind(d, IL, 'Becoming.Interleavings')
add_decls(d, IL, own + index + reads)
d['aliases'] += [x for x in ('index map', '索引映射', Q + 'world_index', Q + 'world_reads_alike') if x not in d['aliases']]
d['reviewed_at_utc'] = NOW
d['history'].append(t(
    f'20 October 2026, R38 (the open part of R33\'s G10): three laws added (the standing at a step as the standing '
    f'after own exchanges, so equal own counts stand alike across interleavings; the index map, its exactness and its '
    f'matching of each relatum\'s exchanges; the readings through own steps the same for every interleaving), the '
    f'general step-by-step relation thus proved directly rather than by composing adjacent swaps; the open part '
    f'restated as one renumbering of the steps and the correspondence with Reordering\'s footprint, with its blocker; '
    f'what the relation gives the necessity target and the premise card added to the correspondence. Proof binding '
    f'(Interleavings.lean) rebound to core receipt {RID}. Study section {STUDY_SECTION}.',
    f'2026年10月20日，R38（R33 之 G10 的开放部分）：新增三条规律（某步所立即自身交换之后所立，故自身计数相等者在各交错间所立相同；'
    f'索引映射、其精确性及其对每个关系项之交换的相配；经自身各步的读法对每个交错相同），一般的逐步关系由此直接证明，而非由相邻对调'
    f'合成；开放部分改述为单一步重编号及与 Reordering 足迹的对应，附其阻碍；对应部分加入此关系给必然性目标与前提卡者。证明绑定'
    f'（Interleavings.lean）改到核心回执 {RID}。研究第 {STUDY_SECTION} 节。'))
save(d)
