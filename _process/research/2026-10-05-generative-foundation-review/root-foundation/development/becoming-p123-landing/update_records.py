#!/usr/bin/env python3
"""P123: the paired notes in what-a-cut-loses and how-a-carried-difference-grows.

usage: python3 -B update_records.py ROOT [SECTION]

what-a-cut-loses lists first in its next step whether every schedule settles (with the exact
strength of that claim) and whether every loop of recurring couplings makes the most difference that
can arrive run away, and how fast. how-often-couplings-act answers both: every schedule settling is
exactly the dichotomy RecursOrStops, which gives the limited principle of omniscience; such a loop
need not run away, runs away where its returns are frequent, and the rate counts the steps at which
couplings act. The spectral radius of given strengths stays. The same note records that the item
"joining what a cut loses to the losses of the sum over histories" is answered by
orders-as-a-sum-over-histories (P121: a cut at order j is a truncation of the sum over histories at
horizon j + 1), which the landing of P121 left in place, and the related entry saying the two are not
yet joined now says so.

how-a-carried-difference-grows lists first how fast a runaway is beyond the product of the strengths;
the new record gives the rate by the steps at which couplings act, attained by a self-loop, and the
item becomes how fast a runaway of given strengths is beyond that. Its correspondence, the readings
Ren decided on 16 October, is left as decided; the open case named there, couplings at only some
steps, is answered by the new record, which related now names.

Each change asserts the text it replaces, so a concurrent edit stops the script instead of being
overwritten. One paired history note in each. Statements, proofs and does_not_show are unchanged:
the scope items still hold of each record's theorems.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
N = int(sys.argv[2]) if len(sys.argv) > 2 else 158
REC = ROOT / 'theories/becoming/results/records'
NEW = 'how-often-couplings-act'
ROUTES = 'orders-as-a-sum-over-histories'


def pair(zh, en):
    return {'zh': zh, 'en': en}


def replace(field, old, new):
    for lang in ('zh', 'en'):
        assert field[lang].count(old[lang]) == 1, (lang, old[lang][:80])
        field[lang] = field[lang].replace(old[lang], new[lang])


def load(name):
    path = REC / f'{name}.json'
    return path, json.loads(path.read_text())


def cut():
    path, r = load('what-a-cut-loses')
    replace(r['next_delta'],
            pair('每个耦合时程是否终将安定（其确切强度）；复现耦合的回路是否都使最大差别失控、多快（谱半径）；实数的量、连续时间与无穷多条件；'
                 '把截断所失与历史之和的损失连起来；',
                 'Whether every schedule settles, and the exact strength of that claim; whether every loop of recurring '
                 'couplings makes the most difference that can arrive run away, and how fast (a spectral radius); real '
                 'amounts, continuous time and infinitely many conditions; joining what a cut loses to the losses of the '
                 'sum over histories; '),
            pair('给定强度的失控多快（谱半径）；实数的量、连续时间与无穷多条件；',
                 'How fast a runaway of given strengths is (a spectral radius); real amounts, continuous time and '
                 'infinitely many conditions; '))
    losses = [x for x in r['related'] if x['id'] == 'losses-of-the-sum-over-histories']
    assert len(losses) == 1
    replace(losses[0]['detail'], pair('两者尚未连起来。', 'The two are not yet joined.'),
            pair(f'{ROUTES} 把两者连起来：j 阶截断是历史之和在视界 j + 1 上的截断。',
                 f'{ROUTES} joins the two: a cut at order j is a truncation of the sum over histories at horizon '
                 'j + 1.'))
    assert all(x['id'] not in (NEW, ROUTES) for x in r['related'])
    r['related'].append({'id': ROUTES, 'detail': pair(
        '截断就是视界：j 阶截断是沿时间往回的路线之和在视界 j + 1 上的截断，所以截断所失就是历史之和的截断所弃者。',
        'A cut is a horizon: a cut at order j is the truncation at horizon j + 1 of the sum over routes back in time, '
        'so what a cut loses is what that truncation of the sum over histories drops.')})
    r['related'].append({'id': NEW, 'detail': pair(
        '回答其下一步的前两项：每个时程都安定恰是二分 RecursOrStops，给出有限全知原则；复现耦合的回路不一定失控，返回频繁时失控，失控的速度'
        '按耦合作用之步计。',
        'Answers the first two items of its next step: every schedule settling is exactly the dichotomy '
        'RecursOrStops, which gives the limited principle of omniscience; a loop of recurring couplings need not run '
        'away, runs away where its returns are frequent, and the rate counts the steps at which couplings act.')})
    r['history'].append(pair(
        f'2026-10-16 P123（耦合多常作用，研究 §{N}）：回答下一步前两项，每个时程都安定恰是二分 RecursOrStops（给出有限全知原则，'
        '核心不假定），复现耦合的回路不一定失控（稀疏的自环），返回频繁时失控，速度按耦合作用之步计，由自环达到；所以删去这两项，给定强度的'
        f'谱半径留下；related 加 {NEW}。同时：“把截断所失与历史之和的损失连起来”已由 {ROUTES} 回答（P121：j 阶截断是视界 j + 1 上的截断），'
        f'P121 落地时留下了此项，所以删去；related 中“两者尚未连起来”改为由 {ROUTES} 连起来，并加 {ROUTES}。陈述与证明不变；does_not_show '
        '仍对本记录的定理成立；correspondence 中的读法仍是 AI 的、待 Ren。',
        f'16 October 2026, P123 (how often couplings act, study section {N}): answers the first two items of the next '
        'step: every schedule settling is exactly the dichotomy RecursOrStops (which gives the limited principle of '
        'omniscience and which the core does not assume), and a loop of recurring couplings need not run away (the '
        'sparse self-loop), runs away where its returns are frequent, the rate counting the steps at which couplings '
        f'act and attained by a self-loop; so both items are removed and the spectral radius of given strengths stays; '
        f'related adds {NEW}. Also: “joining what a cut loses to the losses of the sum over histories” is answered by '
        f'{ROUTES} (P121: a cut at order j is a truncation at horizon j + 1), which the landing of P121 left in place, '
        f'so it is removed; in related, “the two are not yet joined” becomes joined by {ROUTES}, and {ROUTES} is '
        'added. Statement and proofs unchanged; does_not_show still holds of this record\'s theorems; the readings in '
        'correspondence stay the AI\'s, pending Ren.'))
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('updated what-a-cut-loses')


def grows():
    path, r = load('how-a-carried-difference-grows')
    replace(r['next_delta'],
            pair('比强度之积更细的失控速度（谱半径）；',
                 'How fast a runaway is beyond the product of the strengths (a spectral radius); '),
            pair('给定强度的、比强度之积与耦合作用之步数更细的失控速度（谱半径）；',
                 'How fast a runaway of given strengths is beyond the product of the strengths and the count of steps '
                 'at which couplings act (a spectral radius); '))
    assert all(x['id'] != NEW for x in r['related'])
    r['related'].append({'id': NEW, 'detail': pair(
        '几何之界只在耦合作用之步计数仍成立且由自环达到；Ren 认为对的读法“只有回路使差别失控”中只在某些步成立的耦合，两个方向都已关闭：'
        '只有继续着的耦合的回路能使之失控，这样的回路不一定失控，返回频繁时失控。',
        'The geometric bound holds counting only the steps at which couplings act and is attained by a self-loop; in '
        'the reading Ren called right, “only a loop makes a difference run away”, couplings at only some steps are '
        'closed both ways: only a loop of the couplings that go on can make it run away, such a loop need not, and it '
        'does where its returns are frequent.')})
    r['history'].append(pair(
        f'2026-10-16 P123（耦合多常作用，研究 §{N}）：下一步首项“比强度之积更细的失控速度”部分回答：能到达的最大差别至多是起始之差乘以'
        '一加强度的有耦合作用之步数次幂，由自环达到；每次返回至少使之加倍；所以此项改为给定强度的、比这更细的速度（谱半径）。Ren 2026-10-16'
        f' 所定读法中开放的只在某些步成立的耦合，由 {NEW} 两个方向回答；related 加 {NEW}。陈述与证明不变；does_not_show 仍对本记录的定理'
        '成立；correspondence 保持 Ren 所决定的读法。',
        f'16 October 2026, P123 (how often couplings act, study section {N}): the first item of the next step, how fast '
        'a runaway is beyond the product of the strengths, is answered in part: the most difference that can arrive '
        'is at most the starting gap times one plus the strength to the number of steps at which couplings act, '
        'attained by a self-loop, and every return at least doubles it; so the item becomes how fast a runaway of '
        'given strengths is beyond that (a spectral radius). The case left open in the readings Ren decided on 16 '
        f'October, couplings at only some steps, is answered both ways by {NEW}; related adds {NEW}. Statement and '
        'proofs unchanged; does_not_show still holds of this record\'s theorems; correspondence keeps the readings Ren '
        'decided.'))
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('updated how-a-carried-difference-grows')


if __name__ == '__main__':
    cut()
    grows()
