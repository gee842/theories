#!/usr/bin/env python3
"""P126: the paired note in sensitivity-is-the-least-registration.

usage: python3 -B update_records.py ROOT [SECTION]

sensitivity-is-the-least-registration lists first in its next step the exact strength of a
counterexample's existence, between the weak limited principle and the decision of vanishing. The
new record answers it: with the conditions numbered, a counterexample exists exactly where a rule
decides, of every Boolean sequence, whether it is false throughout, and the decision of vanishing is
exactly the limited principle as a rule. So the item leaves next_delta, and related adds the new
record. One paired history note. Statement, proofs and does_not_show are unchanged: the scope items
still hold of the record's theorems. The change asserts the text it replaces, so a concurrent edit
stops the script instead of being overwritten.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
N = int(sys.argv[2]) if len(sys.argv) > 2 else 160
REC = ROOT / 'theories/becoming/results/records'
NEW = 'what-a-law-of-the-whole-and-no-part-takes'


def pair(zh, en):
    return {'zh': zh, 'en': en}


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80])
        field[lang] = field[lang].replace(old[lang], new[lang])


def sensitivity():
    path = REC / 'sensitivity-is-the-least-registration.json'
    r = json.loads(path.read_text())
    replace(r['next_delta'],
            pair('反例之存在的确切强度（在弱有限全知原则与消失之判定之间）；条件不编号时',
                 'The exact strength of a counterexample\'s existence (between the weak limited principle and the '
                 'decision of vanishing); what a counterexample gives'),
            pair('条件不编号时', 'What a counterexample gives'))
    assert all(x['id'] != NEW for x in r['related'])
    r['related'].append({'id': NEW, 'detail': pair(
        '回答其下一步首项：条件编号时，反例恰在一个规则判定每个布尔序列是否处处为假之处存在（弱有限全知原则作为规则），由只由规则造出的'
        '永不消失之律达到；尾之律所取的消失之判定恰是有限全知原则作为规则。',
        'Answers the first item of its next step: with the conditions numbered, a counterexample exists exactly '
        'where a rule decides, of every Boolean sequence, whether it is false throughout (the weak limited principle '
        'as a rule), attained by the law of levels that never vanish, built from the rule alone; the decision of '
        'vanishing the tail law takes is exactly the limited principle as a rule.')})
    r['history'].append(pair(
        f'2026-10-16 P126（整体而无部分之律所需，研究 §{N}）：下一步首项“反例之存在的确切强度”由 {NEW} 回答：条件以自然数编号时，反例'
        '恰在一个规则判定每个布尔序列是否处处为假之处存在（弱有限全知原则作为规则），消失之判定恰是有限全知原则作为规则；所以删去此项；'
        f'related 加 {NEW}。陈述与证明不变；does_not_show 仍对本记录的定理成立；correspondence 中的读法仍按其所注。',
        f'16 October 2026, P126 (what a law of the whole and no part takes, study section {N}): the first item of the '
        f'next step, the exact strength of a counterexample\'s existence, is answered by {NEW}: with the conditions '
        'numbered by the natural numbers, a counterexample exists exactly where a rule decides, of every Boolean '
        'sequence, whether it is false throughout (the weak limited principle of omniscience as a rule), and the '
        'decision of vanishing is exactly the limited principle as a rule; so the item is removed; related adds '
        f'{NEW}. Statement and proofs unchanged; does_not_show still holds of this record\'s theorems; the readings in '
        'correspondence stay as marked there.'))
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('updated sensitivity-is-the-least-registration')


if __name__ == '__main__':
    sensitivity()
