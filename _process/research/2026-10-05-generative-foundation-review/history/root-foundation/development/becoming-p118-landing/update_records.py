#!/usr/bin/env python3
"""P118: the paired notes in the three records whose next step how-a-carried-difference-grows answers.

usage: python3 -B update_records.py ROOT

how-much-difference-arrives listed a general theory of loops first in its next steps;
comparison-where-the-rest-responds and runaway-distance-unregistered asked to define a loop in
general and state a runaway as a theorem. Each change asserts the text it replaces, so a concurrent
edit stops the script instead of being overwritten, and nothing is written unless every change
applies. The anchors stop before the punctuation that follows them, so the script applies whether or
not P110's decisions (on branch p110-frontier) have removed the items after them. One paired history
note per record; the landing's reconciliation of hashed documents extends that note rather than
adding a second one. Scope items saying that these records' own
theorems give only witnesses, or define no loop, stay: they still hold of those theorems.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REC = ROOT / 'theories/becoming/results/records'
NEW = 'how-a-carried-difference-grows'
NOTE = {'zh': '2026-10-16 P118（所携带的差别怎样增长，研究 §152）：',
        'en': '16 October 2026, P118 (how a carried difference grows, study section 152): '}
KEEP = {'zh': '陈述与证明不变；does_not_show 仍对本记录的定理成立。',
        'en': "Statement and proofs unchanged; does_not_show still holds of this record's theorems."}


def load(ident):
    return json.loads((REC / f'{ident}.json').read_text())


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80])
        field[lang] = field[lang].replace(old[lang], new[lang])


def pair(zh, en):
    return {'zh': zh, 'en': en}


def note(r, old, related, zh, en, also=None):
    replace(r['next_delta'], *old)
    if also:
        also(r)
    assert all(x['id'] != NEW for x in r['related'])
    r['related'].append({'id': NEW, 'detail': related})
    r['history'].append({'zh': NOTE['zh'] + zh + f'related 加 {NEW}。' + KEEP['zh'],
                         'en': NOTE['en'] + en + f' related adds {NEW}. ' + KEEP['en']})


def comparison_still_open(r):
    """how-much-difference-arrives said of comparison-where-the-rest-responds that loops stay open."""
    hits = [x for x in r['related'] if x['id'] == 'comparison-where-the-rest-responds']
    assert len(hits) == 1
    replace(hits[0]['detail'], pair('回路的一般理论仍开放。', 'a general theory of loops stays open.'),
            pair(f'回路的一般理论见 {NEW}。', f'a general theory of loops is given in {NEW}.'))


CHANGES = {
    'how-much-difference-arrives': (
        (pair('回路的一般理论（绕回路的强度与失控）；最小的强度', 'A general theory of loops (the strength around a loop and its '
              'runaway); a least strength'),
         pair('最小的强度', 'A least strength')),
        pair('回答其下一步首项：所携带的量按阶展开；上游没有回路处有限阶精确、增长至多是多项式，截断所漏有界且由自环达到；回路每绕一圈至少'
             '乘以一加其强度之积（carried_runaway）；形成与强度每步相同时，能到达的最大差别有多项式界，恰在上游没有回路处'
             '（gap_polynomial_iff_no_loop）。本记录的链与自环是这条规律的两端。',
             'Answers the first item of its next step: the carried amount expands by order; where no loop lies upstream a '
             'finite order is exact and the growth at most polynomial, a cut missing at most a bound a self-loop attains; '
             'a loop multiplies what reaches it every time around by at least one plus the product of its strengths '
             '(carried_runaway); with the same formations and strengths at every step, the most difference that can '
             'arrive is polynomially bounded exactly where no loop lies upstream (gap_polynomial_iff_no_loop). This '
             "record's chain and self-loop are the two ends of that law."),
        '下一步首项“回路的一般理论（绕回路的强度与失控）”由新记录回答，删去；related 中关于 comparison-where-the-rest-responds 的“回路的'
        '一般理论仍开放”改为指向新记录；',
        'in the next step, the first item, “a general theory of loops (the strength around a loop and its runaway)”, is '
        'answered by the new record and removed; in related, “a general theory of loops stays open” of '
        'comparison-where-the-rest-responds now points to the new record;',
        comparison_still_open),
    'comparison-where-the-rest-responds': (
        (pair('回路的一般定义，以及在其中陈述绕回路的强度与失控（how-much-difference-arrives 只给见证）',
              'Define a loop in general and state the strength around it and its runaway (how-much-difference-arrives '
              'gives witnesses only)'),
         pair(f'没有有限耦合强度之律上的回路（具有给定强度时由 {NEW} 回答）',
              f'Loops under laws with no finite coupling strength (answered by {NEW} where the strengths are given)')),
        pair('回答其下一步中回路的一项，在其余遵从具有给定耦合强度之律处：回路是经正强度的耦合回到出发条件的链（OnLoop），绕回路的强度是'
             '一加回路上强度之积，到达回路者每圈至少乘以它（carried_runaway），形成与强度每步相同时有多项式界恰在上游没有回路处。',
             'Answers the item on loops in its next step, where the rest follows a law with given coupling strengths: a '
             'loop is a chain of couplings of positive strength back to where it started (OnLoop), the strength around '
             'it is one plus the product of its strengths, by which what reaches it is multiplied every time around '
             '(carried_runaway), and with the same formations and strengths at every step a polynomial bound holds '
             'exactly where no loop lies upstream.'),
        '下一步中“回路的一般定义，以及在其中陈述绕回路的强度与失控”在具有给定耦合强度之律上由新记录回答，收窄为没有有限强度之律上的回路；',
        'in the next step, “define a loop in general and state the strength around it and its runaway” is answered by '
        'the new record for laws with given coupling strengths, and narrowed to loops under laws with no finite '
        'strength;'),
    'runaway-distance-unregistered': (
        (pair('一般地定义回路（水平影响取用、取用又影响水平的闭合；Becoming.Response 的 Loop 是一个见证：部分的动作改变另一形成所识，'
              '另一形成回应，差别回到部分的支持）并把失控本身陈述为定理；',
              'Define a loop in general (levels affecting taking, and taking the levels; the Loop of Becoming.Response is '
              "one witness, in which a part's act changes what another formation registers, the other responds, and the "
              "difference returns to the part's support) and state a runaway itself as a theorem;"),
         pair(f'把这里的策略与回路相连：形成的汲取回应其自身汲取所降低的水平时，汲取与水平组成一个回路（具有给定耦合强度时，回路的一般'
              f'定义与绕回路的失控由 {NEW} 给出）；',
              "Connect the policies here to loops: where a formation's draw responds to a level its own draw lowers, draw "
              'and level form a loop (for laws with given coupling strengths, a loop in general and the runaway around '
              f'it are given by {NEW});')),
        pair('回答其下一步中“一般地定义回路并把失控陈述为定理”，在具有给定耦合强度的交换律上：回路是经正强度的耦合回到出发条件的链，到达'
             '回路者每圈至少乘以一加其强度之积（carried_runaway）；所失控的是能到达的最大差别，由携带之律达到。这里的失控是保持支持的策略，'
             '两者的连接仍是下一步。',
             'Answers the item of its next step asking to define a loop in general and state a runaway as a theorem, for '
             'laws of exchange with given coupling strengths: a loop is a chain of couplings of positive strength back to '
             'where it started, and what reaches it is multiplied every time around by at least one plus the product of '
             'its strengths (carried_runaway); what runs away is the most difference that can arrive, attained by the '
             'carrying law. The runaway here is a policy keeping support, and connecting the two stays a next step.'),
        '下一步中“一般地定义回路并把失控本身陈述为定理”在具有给定耦合强度的交换律上由新记录回答，改为把这里的策略与回路相连；',
        'in the next step, “define a loop in general and state a runaway itself as a theorem” is answered by the new '
        'record for laws of exchange with given coupling strengths, and becomes connecting the policies here to '
        'loops;'),
}


def main():
    out = []
    for ident, change in CHANGES.items():
        r = load(ident)
        note(r, *change)
        out.append(r)
    for r in out:
        (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('updated', ', '.join(r['id'] for r in out))


if __name__ == '__main__':
    main()
