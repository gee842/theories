#!/usr/bin/env python3
"""R46 (20 October 2026): extend the record the-world-an-interleaving-builds with what R46 proves (run once, after
the checker run; the hash-only re-points of other records go through tools/research/repoint.py).

usage (from the checkout root): python3 -B records_r46.py RECEIPT_ID STUDY_SECTION

Three laws (one renumbering of all the steps; agreement through it; the correspondence with Becoming.Reordering),
the premise they add, three counterexamples (Pair.apart_differs, Pair.touch_not_contains, Pair.idle_unmatched),
the open parts replaced by what stays open, the correspondence's last sentence rewritten for what the renumbering
gives the necessity target and section 0's shared index, a dependency on order-of-exchanges-is-the-invariant, a
history note, and the proof binding of Interleavings.lean rebound to the receipt."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
B = LEAN + 'becoming/Becoming/'
RID, SECTION = sys.argv[1], sys.argv[2]
RECEIPT = LEAN + f'becoming/becoming-checks/{RID}/verification.json'
receipt = json.loads((ROOT / RECEIPT).read_text())
assert receipt['status'] == 'passed'
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def h(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def t(en, zh):
    return {'en': en, 'zh': zh}


IL = B + 'Interleavings.lean'
RO = B + 'Reordering.lean'
Q = 'Becoming.Interleavings.LocalLaw.'
P = 'Becoming.Interleavings.Pair.'
path = REC / 'the-world-an-interleaving-builds.json'
d = json.loads(path.read_text())
assert not any('R46' in x['en'] for x in d['history']), 'already applied'

d['statement'] = t(
    'From a local law and a list of exchanges a World of the spine is built whose steps balance. Two interleavings of '
    'the same courses, every exchange touching a relatum, are carried one to the other by one renumbering of the '
    'steps, under which what is read at a step on what its exchange touches agrees.',
    '由局部律与交换之列构造出脊柱的一个世界，其各步平衡。同一进程的两个交错，每个交换都触及某关系项时，由所有步的一个重编号'
    '彼此相带，经此在一步上就其交换所触及者读出的一切都相同。')
assert len(d['statement']['en']) <= 300 and len(d['statement']['zh']) <= 150, (len(d['statement']['en']),
                                                                               len(d['statement']['zh']))

law2 = d['laws'][1]
assert law2['en'].startswith('The world of a local law on whole-number standings')
law2['en'] = law2['en'].replace('is active where the exchange at t touches it,',
                                'is active where the exchange at t touches it (decided: touchAt),')
law2['zh'] = law2['zh'].replace('被第 t 个交换触及处为活跃，', '被第 t 个交换触及处为活跃（已判定：touchAt），')
for x in (Q + 'touchAt', Q + 'world_active_iff', Q + 'touchAt_some', Q + 'touchAt_none', Q + 'touchAt_iff'):
    if x not in law2['declarations']:
        law2['declarations'].append(x)

one = [Q + x for x in ('exchangeAt_mem', 'exchangeAt_append_lt', 'exchangeAt_append', 'exchangeAt_beyond',
                       'exchangeAt_none', 'exchangeAt_some', 'length_insert', 'ownCount_append_le', 'ownCount_append',
                       'ownCount_untouched', 'ownCount_mono', 'step_of_ownCount', 'firstAt_after',
                       'occurrence_matches', 'Touching', 'Touching.tail', 'Touching.remove', 'length_of_courses',
                       'touches_of_touchedIn', 'renumber', 'renumber_none', 'renumber_lead', 'renumber_spec',
                       'renumber_exchange', 'renumber_count', 'renumber_index', 'renumber_renumber',
                       'renumber_beyond', 'renumber_lt', 'renumber_reindexes')]
agree = [Q + x for x in ('touchAt_renumber', 'runUpTo_untouched', 'runUpTo_renumber', 'reads_renumber',
                         'change_renumber', 'world_renumber_active', 'world_renumber_level', 'world_renumber_reads',
                         'fall_of_change', 'rise_of_change', 'world_renumber_flow')]
order = [Q + x for x in ('footprinted', 'touchAround', 'bool_or_false_left', 'bool_or_false_right',
                         'bool_or_of_left', 'bool_or_of_right', 'untouched_unmoved', 'touch_contains_iff',
                         'around_contains', 'around_joined', 'keeps_consecutive', 'around_keeps_identity',
                         'renumber_keeps', 'world_renumber_correspondence')]
witness = [P + x for x in ('touches', 'act', 'keeps', 'reads', 'law', 'start', 'apart_differs',
                           'touch_not_contains', 'idle_unmatched')]
d['laws'] += [
    {'en': 'Where every exchange of two interleavings of the same courses touches some relatum (Touching), with the '
           'relata listed, the lists have one length, and where one has an exchange at step t the other has the same '
           'exchange at exactly one step at which every relatum it touches has taken as many of its own exchanges: the '
           'k-th taking of an exchange in one is the k-th in the other at every relatum it touches. The renumbering '
           'sends t there (read off the first listed relatum the exchange touches; every relatum it touches gives the '
           'same step), and for each such relatum its index map sends t + 1 to the step after. It is undone by the '
           'renumbering the other way at every step, sends the steps below the length among themselves and fixes '
           'every step from the length on, so the two renumberings Reindex the steps (Becoming.Reordering).',
     'zh': '同一进程的两个交错，每个交换都触及某个关系项（Touching）、关系项列出时，两列等长；一列在第 t 步有一个交换处，另一列恰在'
           '一步有同一交换，在那一步它所触及的每个关系项已取同样多的自身交换：一个交换在一列中的第 k 次取用，在它所触及的每个关系项'
           '处就是在另一列中的第 k 次。重编号把 t 送到那里（按该交换所触及的第一个所列关系项读出；它所触及的每个关系项给出同一步），'
           '对每个这样的关系项，其索引映射把 t + 1 送到那之后一步。反向的重编号在每一步都把它还原，它把长度以下的步彼此对应，从长度起'
           '每一步不动，所以两个重编号对诸步构成 Reindexes（Becoming.Reordering）。',
     'declarations': one},
    {'en': 'Through the renumbering the worlds agree: a relatum is active at step t of one exactly where it is active at '
           'the renumbered step of the other, for every relatum at every step; the step takes the same exchange (the '
           'same relata present, each taking and giving the same: Flow.SameExchange); and every relatum the exchange '
           'touches stands alike before it and after it. So every relation read at one step on the relata its exchange '
           'touches, however many, holds at step t of one world exactly where at the renumbered step of the other; '
           'this holds for any states, not only whole-number standings.',
     'zh': '经由重编号，两个世界相同：对每个关系项在每一步，它在一个世界第 t 步活跃，恰当它在另一世界重编号所给之步活跃；该步取同一'
           '交换（在场的关系项相同，各取各给相同：Flow.SameExchange）；该交换所触及的每个关系项在其前后所立都相同。所以在一步就其交换'
           '所触及诸关系项读出的每个关系，不论读几个，在一个世界第 t 步成立恰当在另一世界重编号所给之步成立；这对任何状态成立，不只是'
           '整数所立。',
     'declarations': agree},
    {'en': 'The correspondence with Becoming.Reordering: the renumbering keeps the order of exchanges sharing a relatum '
           '(Keeps, for the footprint of the touches, in which two exchanges are joined exactly where they touch a '
           'relatum in common), and that footprint moves with it. It contains the exchanges exactly where no relatum is '
           'touched at a step after one not touching it, the world\'s activity being taking part in the exchange across '
           'a step. The footprint around each step, what the exchange at it or at the next touches, contains them, '
           'activity included, but joins every two consecutive exchanges, so the only renumbering of the steps keeping '
           'its order fixes every step: Reordering\'s commutations relate the world of an interleaving to no other '
           'interleaving\'s world, and the relation between them is the renumbering. On the worlds, '
           'world_renumber_correspondence gathers the premises of Reordering\'s converse the renumbering meets: the '
           'reindexing (fixing every step from the length on), the kept order, the same exchange at the renumbered '
           'step and the moved footprint.',
     'zh': '与 Becoming.Reordering 的对应：重编号保持共享关系项之交换的次序（对触及的足迹为 Keeps；在其中两个交换恰在共同触及某关系项'
           '时相连），且该足迹随重编号移动。它恰在没有关系项在一个不触及它的步之后被触及时包含诸交换，因为世界的活跃是参与跨该步的交换。'
           '每步周围的足迹（该步或下一步的交换所触及者）包含它们，活跃也在内，但连起每两个相邻的交换，所以保持其次序的步之重编号只有使'
           '每一步不动者：Reordering 的交换不把一个交错的世界关联到任何别的交错的世界，二者之间的关系是这个重编号。在世界上，'
           'world_renumber_correspondence 汇集重编号所满足的 Reordering 之 converse 的前提：重编（从长度起每一步不动）、所保持的'
           '次序、重编号之步取同一交换、随之移动的足迹。',
     'declarations': order},
]
d['hypotheses'] = [
    d['hypotheses'][0],
    t('For the renumbering: every exchange of both lists touches some relatum (Touching), and the relata are listed. '
      'Without the first an exchange touching no relatum has no match (Pair.idle_unmatched).',
      '重编号：两列的每个交换都触及某个关系项（Touching），关系项列出。没有前者，不触及任何关系项的交换无可相配'
      '（Pair.idle_unmatched）。'),
]
d['does_not_show'] = [
    t('A relation read at one step on relata the step\'s exchange does not touch: what stands together there is the '
      'chosen interleaving\'s, and no renumbering carries it (Pair.apart_differs).',
      '在一步就该步交换不触及的关系项读出的关系：那里谁与谁共同所立属于所选的交错，没有重编号能带过去（Pair.apart_differs）。')
    | {'kind': 'scope'},
    t('A reading of activity as a relatum\'s state between steps, under which Reordering\'s commutations could relate '
      'two interleavings\' worlds; here activity is taking part in the exchange across a step, so the touch footprint '
      'contains the exchanges only in the case touch_contains_iff states and the footprint around each step orders '
      'every two consecutive steps.',
      '把活跃读作关系项在两步之间的状态的读法，在其下 Reordering 的交换可以关联两个交错的世界；此处活跃是参与跨一步的交换，所以触及'
      '的足迹只在 touch_contains_iff 所述情形包含诸交换，而每步周围的足迹给每两个相邻的步定序。') | {'kind': 'correspondence'},
    t('Courses without end; footprints that read relata they do not change; exchanges touching no relatum.',
      '无尽的进程；读而不改关系项的足迹；不触及任何关系项的交换。') | {'kind': 'scope'},
]
d['counterexamples'] = [
    {'path': IL, 'detail': t(
        'Interleavings.Pair.apart_differs: [0, 1] and [1, 0] interleave the same courses of two relata no exchange '
        'connects, and the renumbering exchanges their steps; at step 1 of the first world one relatum stands below '
        'the other, and at no step of the second does. A relation read at one step on relata the step\'s exchange '
        'does not touch is not the same for every interleaving.',
        'Interleavings.Pair.apart_differs：[0, 1] 与 [1, 0] 交错两个无交换相连之关系项的同一进程，重编号对调其两步；在第一个世界第 1 '
        '步一个关系项低于另一个，在第二个世界没有一步如此。在一步就该步交换不触及的关系项读出的关系并非对每个交错都相同。')},
    {'path': IL, 'detail': t(
        'Interleavings.Pair.touch_not_contains: in the world of [0, 1] the footprint of the touches does not contain '
        'the exchanges: the relatum true is untouched at step 0 and touched at step 1, so its activity changes across '
        'a step not touching it.',
        'Interleavings.Pair.touch_not_contains：在 [0, 1] 的世界中，触及的足迹不包含诸交换：关系项 true 在第 0 步不被触及、在第 1 '
        '步被触及，所以其活跃跨一个不触及它的步而改变。')},
    {'path': IL, 'detail': t(
        'Interleavings.Pair.idle_unmatched: [2] and [] give every relatum the same own course, while [2] has at step '
        '0 an exchange touching no relatum that [] has at no step: without Touching there is no renumbering of the '
        'steps matching the exchanges.',
        'Interleavings.Pair.idle_unmatched：[2] 与 [] 给每个关系项同一自身进程，而 [2] 在第 0 步有一个不触及任何关系项的交换，[] 在'
        '任何一步都没有：没有 Touching 就没有使交换相配的步之重编号。')},
]
d['next_delta'] = t(
    'Courses without end; activity read as a relatum\'s state between steps, under which Reordering\'s commutations '
    'could relate interleavings\' worlds; an independent review.',
    '无尽的进程；把活跃读作关系项在两步之间的状态，在其下 Reordering 的交换可以关联诸交错的世界；独立审查。')
old_en = ('a law that reads several relata at one step of the index is still read on a chosen interleaving, which is '
          'what one renumbering of the steps would settle.')
old_zh = '在指标同一步读几个关系项的规律仍在所选的交错上读出，这正是单一步重编号将解决者。'
assert d['correspondence']['en'].endswith(old_en) and d['correspondence']['zh'].endswith(old_zh)
d['correspondence'] = t(
    d['correspondence']['en'][:-len(old_en)] +
    'With one renumbering of all the steps (R46), the same holds of every law read at one step on the relata that '
    'step\'s exchange touches, however many: the shared index is a reading for it as well. What remains a commitment of '
    'the representation is exactly which relata that no exchange at a step relates stand together there, and '
    'Pair.apart_differs shows that this is not carried by any renumbering: it is the choice of interleaving itself, not '
    'a gap in the proof. For the necessity target this narrows the index\'s part of item 1 of §8.1 and of K4 to laws '
    'reading, at one step, relata no exchange there relates; and since Reordering\'s commutations relate no two '
    'interleavings\' worlds (activity being taking part in the exchange across a step), the renumbering, not a '
    'commutation, is the relation between them.',
    d['correspondence']['zh'][:-len(old_zh)] +
    '有了所有步的一个重编号（R46），在一步就该步交换所触及诸关系项读出的每条规律，不论读几个，也是如此：共同指标对它也是一个读法。'
    '仍为表示之承诺者，恰是在一步上没有交换相关联的关系项谁与谁在那里共同所立，而 Pair.apart_differs 表明没有重编号能带过它：这就是'
    '交错的选择本身，不是证明的缺口。对必然性目标，这把 §8.1 第 1 项与 K4 中关于指标的部分收窄为在一步读该处无交换相关联之关系项的'
    '规律；又因 Reordering 的交换不关联任何两个交错的世界（活跃是参与跨一步的交换），二者之间的关系是这个重编号，而非交换。')

# the proof binding and references
for b in d['proof_bindings']:
    if b['source'] == IL:
        b['receipt'] = RECEIPT
assert receipt['source_sha256']['Becoming.Interleavings'] == h(IL)
for r in d['references']:
    if r['path'] == IL:
        r['sha256'] = h(IL)
        for x in law2['declarations'] + one + agree + order + witness:
            if x not in r['declarations']:
                r['declarations'].append(x)
if not any(r['path'] == RECEIPT for r in d['references']):
    d['references'].append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
reo = ['Becoming.Reindexes', 'Becoming.Footprinted', 'Becoming.Footprinted.Contains', 'Becoming.Footprinted.Joined',
       'Becoming.Footprinted.Keeps', 'Becoming.Flow.SameExchange', 'Becoming.Web.Unmoved']
if not any(r['path'] == RO for r in d['references']):
    d['references'].append({'path': RO, 'role': 'proof', 'sha256': h(RO), 'declarations': reo})
if not any(x['id'] == 'order-of-exchanges-is-the-invariant' for x in d['dependencies']):
    d['dependencies'].append({
        'id': 'order-of-exchanges-is-the-invariant', 'relation': 'formal-reuse',
        'detail': t('Reuses Reordering\'s Footprinted, Contains, Joined, Keeps, Reindexes and Flow.SameExchange: the '
                    'renumbering is stated in its terms, and its footprints are read on the world an interleaving '
                    'builds.',
                    '复用 Reordering 的 Footprinted、Contains、Joined、Keeps、Reindexes 与 Flow.SameExchange：重编号以其'
                    '术语陈述，其足迹在交错所构造的世界上读出。'),
        'interface': {'output': t('Footprints, the order of joined exchanges, renumberings of a stretch of steps.',
                                  '足迹、相连交换的次序、一段步的重编号。'),
                      'input': t('The renumbering as a Reindexes keeping the order of the touch footprint; which '
                                 'footprints contain the interleaving world\'s exchanges.',
                                 '重编号作为保持触及足迹之次序的 Reindexes；哪些足迹包含交错之世界的交换。'),
                      'conditions': t('Every exchange touches a relatum; the relata listed.',
                                      '每个交换都触及某个关系项；关系项列出。'),
                      'evidence': RO}})
for x in ('one renumbering of the steps', '步的单一重编号', Q + 'renumber_reindexes', Q + 'world_renumber_reads',
          Q + 'around_keeps_identity', P + 'apart_differs'):
    if x not in d['aliases']:
        d['aliases'].append(x)
d['validation_scope'] = t(
    f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {RID}): the cited declarations of '
    'Becoming.Interleavings have empty axiom reports; the checker verifies core purity. Author self-review in study '
    f'sections 224, 233 and {SECTION}; not independently reviewed.',
    f'Lean 4.29.1 合并检查器实查（回执 {RID}）：所引 Becoming.Interleavings 的声明公理报告为空；检查器并核对核心纯净。作者自审见研究'
    f'第 224、233 与 {SECTION} 节；未经独立审查。')
d['reviewed_at_utc'] = NOW
d['history'].append(t(
    f'20 October 2026, R46 (the open part R38 left): three laws added (one renumbering of all the steps, matching each '
    f'taking of an exchange at every relatum it touches, each such relatum\'s index map one step back, a Reindexes of '
    f'the steps; activity, the exchange and the standings of what it touches agreeing through it, so every relation '
    f'read at one step on those relata agrees; the correspondence with Reordering: the touch footprint\'s order kept, '
    f'its containment exactly characterized, and the footprint around each step containing the exchanges but leaving '
    f'only the identity renumbering), the premise Touching, three counterexamples, a dependency on '
    f'order-of-exchanges-is-the-invariant; the world\'s activity restated as the decided touch (touchAt), equivalent '
    f'to the earlier form (world_active_iff); the open parts replaced by what stays open; the correspondence\'s last '
    f'sentence rewritten. Proof binding (Interleavings.lean) rebound to core receipt {RID}. Study section {SECTION}.',
    f'2026年10月20日，R46（R38 所留的开放部分）：新增三条规律（所有步的一个重编号，在交换所触及的每个关系项处相配其每次取用，'
    f'对每个这样的关系项是其索引映射退后一步，对诸步构成 Reindexes；经由它活跃、交换与其所触及者的所立相同，故在一步就这些关系项'
    f'读出的每个关系相同；与 Reordering 的对应：保持触及足迹的次序，其包含关系被确切刻画，每步周围的足迹包含诸交换却只留下恒等'
    f'重编号），前提 Touching，三个反例，对 order-of-exchanges-is-the-invariant 的依赖；世界的活跃改述为已判定的触及（touchAt），'
    f'与先前形式等价（world_active_iff）；开放部分换为仍开放者；对应部分末句改写。证明绑定（Interleavings.lean）改到核心回执 '
    f'{RID}。研究第 {SECTION} 节。'))
path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('wrote', d['id'])
