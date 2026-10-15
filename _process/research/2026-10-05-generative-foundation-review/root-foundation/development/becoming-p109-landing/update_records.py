#!/usr/bin/env python3
"""P109: paired notes in the two records whose next step where-a-move-is-formed answers.

usage: python3 -B update_records.py ROOT

Each change asserts the text it replaces, so a concurrent edit stops the script instead of being
overwritten. One paired history note per record; the landing's reconciliation of hashed documents
extends that note rather than adding a second one.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REC = ROOT / 'theories/becoming/results/records'
NOTE = {'zh': '2026-10-15 P109（动作在哪里形成，研究 §131）：', 'en': '15 October 2026, P109 (where a move is formed, study section 131): '}


def load(ident):
    return json.loads((REC / f'{ident}.json').read_text())


def save(r):
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80])
        field[lang] = field[lang].replace(old[lang], new[lang])


def relate(r, zh, en):
    assert all(x['id'] != 'where-a-move-is-formed' for x in r['related'])
    r['related'].append({'id': 'where-a-move-is-formed', 'detail': {'zh': zh, 'en': en}})


def note(r, zh, en):
    r['history'].append({'zh': NOTE['zh'] + zh, 'en': NOTE['en'] + en})


def process_and_frame():
    r = load('process-and-frame-as-readings')
    replace(r['next_delta'],
            {'zh': '动作在展开之内形成的条件（何时一个动作是某个形成的，而不是外来的）；',
             'en': "when a move is formed within the unfolding (when it is a formation's, not supplied from outside); "},
            {'zh': '', 'en': ''})
    relate(r,
           '推进其下一步：动作总可读作在整体之内形成（Run.withClock：其余形成它），恰当它经部分的配置形成时是部分自己的（PartForms）；'
           '耦合的整体就是积的 closedBy（Run.toClosedBy、Run.ofClosedBy）；一段进程只在配置复现而动作不同之处固定动作是谁的。',
           'Advances its next step: a move can always be read as formed within a whole (Run.withClock: its rest forms '
           "it), and is the part's own exactly where it is formed through the part's configuration (PartForms); the "
           "coupled whole is the product's closedBy (Run.toClosedBy, Run.ofClosedBy); one course fixes whose move it is "
           'only where a configuration recurs with the move varied.')
    note(r,
         '下一步中“动作在展开之内形成的条件”由 where-a-move-is-formed 回答，删去；related 加 where-a-move-is-formed。陈述与证明不变；'
         '本记录的限制（动作在展开之内形成与否不由本记录的定理推出）仍对其自身的定理成立。',
         "in the next step, “when a move is formed within the unfolding” is answered by where-a-move-is-formed and "
         'removed; related adds where-a-move-is-formed. Statement and proofs unchanged; the limitation that this '
         "record's theorems do not derive whether a move is formed within the unfolding still holds of them.")
    save(r)


def counterfactual():
    r = load('counterfactual-is-the-course')
    replace(r['next_delta'],
            {'zh': '何时一个动作是部分自己的；', 'en': "when a move is the part's own; "},
            {'zh': '', 'en': ''})
    relate(r,
           '推进其下一步：动作是部分自己的，恰当它经部分的配置形成；进程的标准模型中，不读任何东西的律的动作只经阶段形成，'
           '如钟所形成者（ExchangeLaw.ofMoves_lumped_stage）。',
           "Advances its next step: a move is the part's own exactly where it is formed through the part's "
           "configuration; in a course's standard model, the act of a law that reads nothing is formed through the stage "
           'alone, as a clock forms moves (ExchangeLaw.ofMoves_lumped_stage).')
    note(r,
         '下一步中“何时一个动作是部分自己的”由 where-a-move-is-formed 回答，删去；related 加 where-a-move-is-formed。陈述与证明不变。',
         "in the next step, “when a move is the part's own” is answered by where-a-move-is-formed and removed; related "
         'adds where-a-move-is-formed. Statement and proofs unchanged.')
    save(r)


def main():
    process_and_frame()
    counterfactual()
    print('updated process-and-frame-as-readings and counterfactual-is-the-course')


if __name__ == '__main__':
    main()
