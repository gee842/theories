#!/usr/bin/env python3
"""P113: the paired note in counterfactual-is-the-course, whose next step sensitivity-is-the-least-registration answers.

usage: python3 -B update_records.py ROOT

The change asserts the text it replaces, so a concurrent edit stops the script instead of being
overwritten. One paired history note; the landing's reconciliation of hashed documents extends that
note rather than adding a second one. The scope item "Whether sensitivity remains the least
registration with infinitely many conditions is not stated, and no counterexample is given" stays:
it still holds of this record's own theorems.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REC = ROOT / 'theories/becoming/results/records'
NOTE = {'zh': '2026-10-15 P113（任意多条件下最小的识，研究 §137）：',
        'en': '15 October 2026, P113 (the least registration with any number of conditions, study section 137): '}
NEW = 'sensitivity-is-the-least-registration'


def load(ident):
    return json.loads((REC / f'{ident}.json').read_text())


def save(r):
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80])
        field[lang] = field[lang].replace(old[lang], new[lang])


def counterfactual():
    r = load('counterfactual-is-the-course')
    replace(r['next_delta'],
            {'zh': '条件无穷多时敏感是否仍是最小的识（或反例）；',
             'en': 'Whether sensitivity remains the least registration with infinitely many conditions, or a '
                   'counterexample; the responsive reach'},
            {'zh': '', 'en': 'The responsive reach'})
    assert all(x['id'] != NEW for x in r['related'])
    r['related'].append({'id': NEW, 'detail': {
        'zh': '回答其下一步：凡律在每个历史下读有限多个条件，无论条件多少，敏感都是最小的识'
              '（ExchangeLaw.ReadsFinitely.least_registration），条件有限的情形（ExchangeLaw.Nonanticipating.through_sensitive）'
              '是其实例；条件无穷多时这一条件不能去掉（tailLaw_no_least_registration，给定消失之判定），条件编号时每个反例都给出弱有限'
              '全知原则（wlpo_of_not_through_sensitive）。',
        'en': 'Answers its next step: wherever the law reads finitely many conditions under each history, sensitivity is '
              'the least registration with any number of conditions (ExchangeLaw.ReadsFinitely.least_registration), the '
              'finite case (ExchangeLaw.Nonanticipating.through_sensitive) being its instance; with infinitely many '
              'conditions this cannot be dropped (tailLaw_no_least_registration, given the decision of vanishing), and '
              'with numbered conditions every counterexample gives the weak limited principle of omniscience '
              '(wlpo_of_not_through_sensitive).'}})
    r['history'].append({
        'zh': NOTE['zh'] + f'下一步中“条件无穷多时敏感是否仍是最小的识（或反例）”由 {NEW} 回答，删去；related 加 {NEW}。陈述与证明不变；'
              'does_not_show 中“条件无穷多时……不陈述，也不给反例”仍对本记录的定理成立。',
        'en': NOTE['en'] + 'in the next step, “whether sensitivity remains the least registration with infinitely many '
              f'conditions, or a counterexample” is answered by {NEW} and removed; related adds {NEW}. Statement and '
              'proofs unchanged; the scope item that this is not stated and no counterexample is given still holds of '
              "this record's theorems."})
    save(r)


def main():
    counterfactual()
    print('updated counterfactual-is-the-course')


if __name__ == '__main__':
    main()
