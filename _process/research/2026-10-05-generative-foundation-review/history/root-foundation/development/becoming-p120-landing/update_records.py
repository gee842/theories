#!/usr/bin/env python3
"""P120: the paired note in how-a-carried-difference-grows, whose next step what-a-cut-loses answers.

usage: python3 -B update_records.py ROOT

how-a-carried-difference-grows lists loops whose couplings come and go first in its next steps.
what-a-cut-loses answers it for exactness, for every schedule, and for growth in one direction: the
most difference that can arrive outgrows every polynomial only through a loop of the couplings that
go on. Whether it does so through every such loop, and how fast, are carried on in the new record's
next step. The change asserts the text it replaces, so a concurrent edit stops the script instead of
being overwritten. One paired history note. The scope item saying that the record's equivalences need
couplings at every step stays: it still holds of its theorems. Its correspondence, the readings Ren
decided on 16 October, is left as decided.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REC = ROOT / 'theories/becoming/results/records'
NEW = 'what-a-cut-loses'
OLD = 'how-a-carried-difference-grows'


def pair(zh, en):
    return {'zh': zh, 'en': en}


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80])
        field[lang] = field[lang].replace(old[lang], new[lang])


def main():
    path = REC / f'{OLD}.json'
    r = json.loads(path.read_text())
    replace(r['next_delta'], pair('时有时无的耦合上的回路；比强度之积', 'Loops whose couplings come and go; how fast'),
            pair('比强度之积', 'How fast'))
    assert all(x['id'] != NEW for x in r['related'])
    r['related'].append({'id': NEW, 'detail': pair(
        '对每个耦合时程回答其下一步首项“时有时无的耦合上的回路”：截断所失恰是更多次回应所携带的，恰在有按时间次序的更长的链处；时程安定时有限阶'
        '精确恰在上游没有继续着的耦合的回路；没有这样的回路时有多项式界。',
        'Answers the first item of its next step, loops whose couplings come and go, for every schedule: a cut loses '
        'exactly what more responses carry, exactly where a longer chain in time order arrives; once the schedule has '
        'settled, a finite order is exact exactly where no loop of the couplings that go on lies upstream; without '
        'such a loop the growth is polynomial.')})
    r['history'].append(pair(
        '2026-10-16 P120（截断所失，研究 §154）：回答下一步首项“时有时无的耦合上的回路”，就精确性而言对每个耦合时程，就增长而言在一个方向：'
        '能到达的最大差别快于每个多项式，只经由继续着的耦合的回路（carried_le_polynomial_from）；是否经由每个这样的回路、多快，由新记录的下一步'
        f'承接，所以删去此项；related 加 {NEW}。陈述与证明不变；does_not_show 仍对本记录的定理成立；correspondence 保持 Ren 所决定的读法。',
        '16 October 2026, P120 (what a cut loses, study section 154): answers the first item of the next step, loops '
        'whose couplings come and go, for exactness for every schedule of couplings, and for growth in one direction: '
        'the most difference that can arrive outgrows every polynomial only through a loop of the couplings that go '
        'on (carried_le_polynomial_from); whether through every such loop, and how fast, the new record\'s next step '
        f'carries on, so the item is removed; related adds {NEW}. Statement and proofs unchanged; does_not_show '
        'still holds of this record\'s theorems; correspondence keeps the readings Ren decided.'))
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('updated', OLD)


if __name__ == '__main__':
    main()
