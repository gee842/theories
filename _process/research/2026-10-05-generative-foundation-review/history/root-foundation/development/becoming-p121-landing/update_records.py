#!/usr/bin/env python3
"""P121 and P122: paired notes in the records whose next steps the two new records answer.

usage: python3 -B update_records.py ROOT [P121_SECTION P122_SECTION]

how-a-carried-difference-grows (P118, with P120's edits) lists "how loops form, where a draw meets
Becoming.Runaway's policies" and "joining the orders to the sum over histories" in its next step, and
its third reading, taken by Ren, waits for a loop-formation theorem. losses-of-the-sum-over-histories
(P82) gains the join as related. runaway-distance-unregistered (P55) asks to connect its policies to
loops where a draw responds to a level it lowers. Each change asserts the text it replaces, so a
concurrent edit stops the script, and nothing is written unless every change applies. Ren's readings
as recorded are not rewritten: a dated sentence after them says what now exists. One paired history
note per record.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTIONS = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (155, 156)
REC = ROOT / 'theories/becoming/results/records'
ROUTES, CLOSING = 'orders-as-a-sum-over-histories', 'how-loops-form'


def pair(zh, en):
    return {'zh': zh, 'en': en}


NOTE = pair(f'2026-10-16 P121 与 P122（携带差别的阶作为历史之和、回路怎样在展开中形成，研究 §{SECTIONS[0]}、§{SECTIONS[1]}）：',
            f'16 October 2026, P121 and P122 (the orders of a carried difference as a sum over histories, how loops form '
            f'within the unfolding, study sections {SECTIONS[0]} and {SECTIONS[1]}): ')
KEEP = pair('陈述与证明不变。', 'Statement and proofs unchanged.')


def load(ident):
    return json.loads((REC / f'{ident}.json').read_text())


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80], field[lang].count(old[lang]))
        field[lang] = field[lang].replace(old[lang], new[lang])


def relate(r, ident, detail):
    assert all(x['id'] != ident for x in r['related']), (r['id'], ident)
    r['related'].append({'id': ident, 'detail': detail})


def history(r, zh, en):
    r['history'].append({'zh': NOTE['zh'] + zh + KEEP['zh'], 'en': NOTE['en'] + en + ' ' + KEEP['en']})


def carried():
    r = load('how-a-carried-difference-grows')
    replace(r['next_delta'],
            pair('回路怎样在展开中形成（汲取与 Becoming.Runaway 的策略相遇处）；把各阶与历史之和连起来；',
                 "how loops form, where a draw meets Becoming.Runaway's policies; joining the orders to the sum over "
                 'histories; '),
            pair('在一个律中把回路的形成与 Becoming.Runaway 的策略连起来；',
                 "joining the formation of loops and Becoming.Runaway's policies within one law; "))
    after = pair('暂取此形式，待有回路形成之定理时可修订。',
                 'taken for now and open to revision once a loop-formation theorem exists.')
    replace(r['correspondence'], after,
            pair(after['zh'] + f'（2026-10-16 之后：两者由 {ROUTES} 接合，各阶是沿时间往回的路线之和；回路形成的定理是 {CLOSING}，'
                 '回路由闭合而形成；第三项读法待 Ren 再议。）',
                 after['en'] + f' (After 16 October: the two are joined by {ROUTES}, the orders being sums over routes back '
                 f'in time; the loop-formation theorem is {CLOSING}, a loop forming by closing; the third reading awaits '
                 "Ren's revision.)"))
    relate(r, ROUTES, pair('各阶是历史之和：沿时间往回的路线之和在视界 j + 1 上就是 j 阶，截断就是视界。',
                           'The orders are a sum over histories: the sum over routes back in time at horizon j + 1 is '
                           'order j, and a cut is a truncation.'))
    relate(r, CLOSING, pair('回路怎样在展开中形成：经过在形成之步作用、闭合一条链的耦合；形成之前增长至多是多项式。',
                            'How loops form within the unfolding: through a coupling acting at the step of formation that '
                            'closes a chain; before formation growth is at most polynomial.'))
    history(r, '下一步中“回路怎样在展开中形成”与“把各阶与历史之和连起来”由新记录回答，改为在一个律中把形成与 Becoming.Runaway 的策略'
               f'连起来；correspondence 在 Ren 的读法之后加一句注明已有者，读法本身不改；related 加 {ROUTES} 与 {CLOSING}。',
            "in the next step, “how loops form, where a draw meets Becoming.Runaway's policies” and “joining the orders "
            'to the sum over histories” are answered by the new records and become joining formation and '
            "Becoming.Runaway's policies within one law; correspondence gains one sentence after Ren's readings saying "
            f'what now exists, the readings themselves unchanged; related adds {ROUTES} and {CLOSING}.')
    return r


def losses():
    r = load('losses-of-the-sum-over-histories')
    relate(r, ROUTES, pair('所携带的差别是计数权重的历史之和：Becoming.Loops 的 j 阶就是视界 j + 1；每个历史之和按阶展开，j 阶到视界 j 精确。',
                           'The carried difference is a sum over histories of counting weights: order j of '
                           'Becoming.Loops is horizon j + 1; every sum over histories expands by order, exact up to '
                           'horizon j.'))
    history(r, f'related 加 {ROUTES}：两个积分接合。', f'related adds {ROUTES}: the two integrations joined.')
    return r


def runaway():
    r = load('runaway-distance-unregistered')
    old = pair('（具有给定耦合强度时，回路的一般定义与绕回路的失控由 how-a-carried-difference-grows 给出）；',
               '(for laws with given coupling strengths, a loop in general and the runaway around it are given by '
               'how-a-carried-difference-grows);')
    replace(r['next_delta'], old,
            pair(f'（具有给定耦合强度时，回路的一般定义与绕回路的失控由 how-a-carried-difference-grows 给出，回路的形成由 {CLOSING} 给出）；',
                 '(for laws with given coupling strengths, a loop in general and the runaway around it are given by '
                 f'how-a-carried-difference-grows, and how a loop forms by {CLOSING});'))
    relate(r, CLOSING, pair('这里失控的断裂在其前不被识；那里使之失控的回路的形成也不被它所携带的量识，能识它的是识耦合本身者。',
                            "Here a runaway's break is not registered before it; there the formation of the loop that "
                            'runs away is not registered by the amounts it carries either: what registers it is what '
                            'registers the couplings themselves.'))
    history(r, f'下一步的回路一项注明回路的形成由 {CLOSING} 给出，与策略的连接仍是下一步；related 加 {CLOSING}。',
            f'the loop item of the next step notes that how a loop forms is given by {CLOSING}, connecting it to the '
            f'policies staying a next step; related adds {CLOSING}.')
    return r


def main():
    out = [carried(), losses(), runaway()]
    for r in out:
        (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('updated', ', '.join(r['id'] for r in out))


if __name__ == '__main__':
    main()
