#!/usr/bin/env python3
"""P127: the paired notes in returning-where-the-course-branches and lifting-where-branching-is-finite.

usage: python3 -B update_records.py ROOT [SECTION]

returning-where-the-course-branches has one next step: state the laws along runs for every
configuration that can move without a choice. The new record answers it, for finitely many
configurations with no decision, so the next step becomes the open item its limitations name,
being drawn in within a bound. lifting-where-branching-is-finite lists a run without a selection
(the boundary of dependent choice) after an independent review; the new record answers it, so the
item leaves. Both gain the new record under related and one history note. Statements, proofs,
hypotheses, limitations and does_not_show are unchanged: they still hold of each record's own
theorems. Each change asserts the text it replaces, so a concurrent edit stops the script instead
of being overwritten.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
N = int(sys.argv[2]) if len(sys.argv) > 2 else 161
REC = ROOT / 'theories/becoming/results/records'
NEW = 'where-a-run-goes-on'


def pair(zh, en):
    return {'zh': zh, 'en': en}


def note(r, detail):
    assert all(x['id'] != NEW for x in r['related'])
    r['related'].append({'id': NEW, 'detail': detail})


def returning():
    path = REC / 'returning-where-the-course-branches.json'
    r = json.loads(path.read_text())
    assert r['next_delta'] == pair(
        '对每个能动的配置不加选择地陈述沿运行的定律（例如对有限的、可判定的过程）。',
        'State the laws along runs for every configuration that can move without a choice (for instance for finite, '
        'decidable processes).'), r['next_delta']
    r['next_delta'] = pair('在界内被吸入（见 limitations）。', 'Being drawn in within a bound (see limitations).')
    note(r, pair(
        '回答其下一步：有限多配置之内运行恰是通向返回的路径，不需判定也不需选取；沿运行的定律对每个能继续运动的配置成立，不给定运行'
        '（lossless_returns_iff、lossless_no_rise、lossless_unlisted）；对每个过程要求运行恰是依赖选择。',
        'Answers its next step: within finitely many configurations a run is a course into a return, with no decision '
        'and no selection; the laws along runs hold for every configuration that can keep moving, with no run given '
        '(lossless_returns_iff, lossless_no_rise, lossless_unlisted); asked of every process, a run is exactly '
        'dependent choice.'))
    r['history'].append(pair(
        f'2026-10-16 P127（运行在何处延续，研究 §{N}）：下一步“对每个能动的配置不加选择地陈述沿运行的定律”由 {NEW} 回答：有限多配置'
        '之内运行恰是通向返回的路径，不需判定也不需选取，沿运行的定律对每个能继续运动的配置成立，不给定运行；所以下一步改为 limitations '
        f'所列的在界内被吸入；related 加 {NEW}。陈述、证明、hypotheses 与 limitations 不变：仍对本记录的定理成立。',
        f'16 October 2026, P127 (where a run goes on, study section {N}): the next step, stating the laws along runs for '
        f'every configuration that can move without a choice, is answered by {NEW}: within finitely many configurations a '
        'run is a course into a return, with no decision and no selection, and the laws along runs hold for every '
        'configuration that can keep moving with no run given; so the next step becomes being drawn in within a bound, '
        f'listed under limitations; related adds {NEW}. Statement, proofs, hypotheses and limitations unchanged: they '
        'still hold of this record\'s theorems.'))
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('updated returning-where-the-course-branches')


def lifting():
    path = REC / 'lifting-where-branching-is-finite.json'
    r = json.loads(path.read_text())
    assert r['next_delta'] == pair('独立审查；不用选取时的运行（依赖选择的边界）。',
                                   'An independent review; a run without a selection (the boundary of dependent '
                                   'choice).'), r['next_delta']
    r['next_delta'] = pair('独立审查。', 'An independent review.')
    note(r, pair(
        '回答其下一步“不用选取时的运行”：有限多配置之内，每个长度的路径都开始处有运行，不需选取也不需 EitherThroughout；测试认出'
        '移动处运行经搜索造出；对每个过程要求从每个保持运动的族的每个成员出发的运行，恰是依赖选择。',
        'Answers its next step, a run without a selection: within finitely many configurations a run starts wherever '
        'courses of every length do, with no selection and no EitherThroughout; where a test recognizes the moves a run '
        'is built by search; asked of every process, a run from every member of every family that keeps moving is '
        'exactly dependent choice.'))
    r['history'].append(pair(
        f'2026-10-16 P127（运行在何处延续，研究 §{N}）：下一步“不用选取时的运行（依赖选择的边界）”由 {NEW} 回答：有限多配置之内不需'
        '选取，测试认出移动处经搜索，对每个过程要求它恰是依赖选择；所以删去此项，下一步只余独立审查；related 加 '
        f'{NEW}。陈述、证明与 does_not_show 不变：仍对本记录的定理成立。',
        f'16 October 2026, P127 (where a run goes on, study section {N}): the next step, a run without a selection (the '
        f'boundary of dependent choice), is answered by {NEW}: within finitely many configurations no selection is '
        'needed, where a test recognizes the moves a run is built by search, and asked of every process it is exactly '
        f'dependent choice; so the item is removed, leaving an independent review; related adds {NEW}. Statement, '
        'proofs and does_not_show unchanged: they still hold of this record\'s theorems.'))
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('updated lifting-where-branching-is-finite')


if __name__ == '__main__':
    returning()
    lifting()
