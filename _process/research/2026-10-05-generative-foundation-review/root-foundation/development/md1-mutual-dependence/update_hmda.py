#!/usr/bin/env python3
"""MD1: the record how-much-difference-arrives states D39's reading of "entangled" in its correspondence; bring it to
the revision of 19 October (mutual dependence) and note it in the history. python3 -B update_hmda.py"""
import json
P = 'theories/becoming/results/records/how-much-difference-arrives.json'
d = json.load(open(P))
E_OLD = ('“a highly entangled system” as couplings that lie on loops through the whole, how highly being the strengths '
         'along the loops and how often they act, not as quantum entanglement (revised and taken by Ren on 18 October '
         '2026, DELEGATED-CHOICES D39).')
E_NEW = ('“a highly entangled system” as mutual dependence, every influence closure the whole, under which every link of '
         'affecting lies on a loop through the whole, how highly being the strengths along the loops and how often they '
         'act, not as quantum entanglement (revised and taken by Ren on 18 October 2026, and revised to mutual dependence '
         'on 19 October 2026, DELEGATED-CHOICES D39; record mutual-dependence-and-its-pace).')
Z_OLD = ('“a highly entangled system”读作耦合位于贯穿整体的回路上，多“highly”是回路上的强度与其作用的频度，不等同于量子的纠缠'
         '（经修订由 Ren 2026-10-18 取，DELEGATED-CHOICES D39）。')
Z_NEW = ('“a highly entangled system”读作相互依存，即每个影响闭包都是整体，在它之下每一影响之链都位于贯穿整体的回路上，'
         '多“highly”是回路上的强度与其作用的频度，不等同于量子的纠缠（经修订由 Ren 2026-10-18 取，2026-10-19 修订为相互依存，'
         'DELEGATED-CHOICES D39；记录 mutual-dependence-and-its-pace）。')
for lang, old, new in [('en', E_OLD, E_NEW), ('zh', Z_OLD, Z_NEW)]:
    assert d['correspondence'][lang].count(old) == 1, lang
    d['correspondence'][lang] = d['correspondence'][lang].replace(old, new)
d['history'].append({
    'en': '19 October 2026, MD1 (mutual dependence and the pace it gives): the correspondence reads "a highly entangled '
          'system" as mutual dependence, D39 as revised that day; the coupling strength and the laws of this record are '
          'unchanged.',
    'zh': '2026年10月19日，MD1（相互依存及其给出的步速）：对应部分把“a highly entangled system”读作相互依存，即 D39 当日的修订；'
          '耦合强度与本记录的规律不变。'})
open(P, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated how-much-difference-arrives')
