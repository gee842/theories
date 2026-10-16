#!/usr/bin/env python3
"""P107 landing edits that need the core run (run with the checkout root as argument).

usage: land_p107_docs.py ROOT CORE_RECEIPT PREV_UTC (receipt relative to ROOT; PREV_UTC the receipt the chapter names now)
1. The chapter's §9 totals move to the run (theorems, declaration audits, core closure, package, bridge and
   inherited modules), matched by pattern on the receipt the chapter names now.
2. The reading entry the-theory-of-becoming is reconciled with the chapter after reading its changes:
   the re-founding is added to the argument, the imbalance choice in the next steps becomes Ren's
   adoption, the three modules join its Lean list, and only then its source hash is refreshed.
Every replacement asserts the text it replaces.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
CORE = sys.argv[2]
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
READING = ROOT / 'theories/becoming/results/data/arguments-m-z.json'


def sub1(s, old, new):
    assert s.count(old) == 1, (s.count(old), old[:90])
    return s.replace(old, new)


NUM_ZH = {3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九', 10: '十'}
NUM_EN = {3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
RUN_LINK = r'\.\./\.\./\.\./experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/'
ZH_RE = re.compile(r'\[冻结回执 `(?P<utc>\d{8}T\d{6}\.\d{6}Z)`\]\(' + RUN_LINK + r'(?P=utc)/verification\.json\)覆盖 '
                   r'(?P<th>\d+) 项定理、(?P<au>\d+) 项声明审计，源声明的公理报告全部为空；核心闭包共 (?P<cl>\d+) 个模块'
                   r'（包 (?P<pk>\d+) 个模块，含根模块与(?P<br>[一二三四五六七八九十]+)个桥接模块）；(?P<inh>\d+) 个继承模块')
EN_RE = re.compile(r'The consolidated checker and its receipt `(?P<utc>\d{8}T\d{6}\.\d{6}Z)` cover (?P<th>\d+) theorems and '
                   r'(?P<au>\d+) declaration audits, all source declarations with empty axiom reports; the core closure has '
                   r'(?P<cl>\d+) modules \(the package (?P<pk>\d+), with the root and the (?P<br>[a-z]+) bridge modules\)\. '
                   r'The current bytes of (?P<inh>\d+) inherited modules')


def chapter(prev, utc, theorems, audits, closure, package, bridges, inherited):
    """The §9 totals move from the receipt the chapter names (which must be PREV) to the landed run."""
    p = ROOT / CH
    s = p.read_text()
    out = []
    for rx, words, fmt in (
            (ZH_RE, NUM_ZH, lambda: (f'[冻结回执 `{utc}`](../../../experiments/integrated-correction/general-framework/'
                                     f'generative-basis/lean/becoming/becoming-checks/{utc}/verification.json)覆盖 {theorems} '
                                     f'项定理、{audits} 项声明审计，源声明的公理报告全部为空；核心闭包共 {closure} 个模块（包 '
                                     f'{package} 个模块，含根模块与{NUM_ZH[bridges]}个桥接模块）；{inherited} 个继承模块')),
            (EN_RE, NUM_EN, lambda: (f'The consolidated checker and its receipt `{utc}` cover {theorems} theorems and {audits} '
                                     'declaration audits, all source declarations with empty axiom reports; the core closure '
                                     f'has {closure} modules (the package {package}, with the root and the {NUM_EN[bridges]} '
                                     f'bridge modules). The current bytes of {inherited} inherited modules'))):
        found = list(rx.finditer(s))
        assert len(found) == 1, (rx.pattern[:40], len(found))
        m = found[0]
        assert m['utc'] == prev, (m['utc'], prev)
        out.append({k: m[k] for k in ('utc', 'th', 'au', 'cl', 'pk', 'br', 'inh')})
        s = s[:m.start()] + fmt() + s[m.end():]
    assert [out[0][k] for k in ('th', 'au', 'cl', 'pk', 'inh')] == [out[1][k] for k in ('th', 'au', 'cl', 'pk', 'inh')], out
    p.write_text(s)
    return out[1]


ARG_ZH = ('10月14日的从关系开始的重建（Ren：“why do we need "World"?”，随后“please, finish all”）只用水平陈述规律，每条写入部分的'
          '一个状态：存量在界内的家族回返，每步都新的家族超出每个界，在界内而交换不止的家族与有限的整体不承载其历史，每次变化都下降时'
          '变化不无尽复现；Entropy 在第一律之下的形式是其情形。它从交换读出 World 的前提：活跃即交换，汲取即所取，整体的其余算作关系项'
          '（Ren 采用），于是每个世界都平衡，其平衡恰是其余从不活跃；交换之律下把要求读作回应，活动需要支持，四个联结前提都由读法成立；'
          '要求是律的反事实，没有历程固定它。八个前提的独立性度量 World 分别选取的字段的自由，不度量生成的偶然。统一由一个形式陈述：'
          '一个运行在语境中的诸读法总是一个世界（量子的识亦然）；不依语境的描述恰在它们粘合处存在；平衡是所立与交换两种变化读法的粘合；'
          '算入其余时每个世界都是交换之律的一次运行；在同样的不变标准下，意义在某个边界内成立只能因为对一切成立（重述 Becoming.Boundaries）。')
ARG_EN = (' The relation-first re-founding of 14 October (Ren: “why do we need "World"?”, then “please, finish all”) states laws '
          'on the levels alone, each with one state of the part written into it: a family whose stock stays within a bound '
          'returns, one new at every step exceeds every bound, a bounded family exchanged with without end and a finite whole '
          'do not carry their history, and with loss at each change, change does not recur without end; Entropy\'s forms under '
          'the first law are their cases. It reads World\'s premises off the exchange: activity is exchanging and drawing is '
          'taking, and the rest of the whole is counted as a relatum (adopted by Ren), so every world balances and its balance '
          'is the rest never active; under a law of exchange, with requirement read as response, activity needs support, so '
          'all four tying premises hold by reading, and requirement is a counterfactual of the law that no course fixes. The '
          'independence of the eight premises measures the freedom of World\'s separately chosen fields, not contingency in '
          'becoming. One shape states unity: the readings in context of a run always make one world, quantum registrations '
          'included; a context-free description exists exactly where they glue; balance is the gluing of the standing\'s and '
          'the exchange\'s readings of change; with the rest counted every world is one run of the law of exchange; and under '
          'the same standard of invariance significance holds within some boundary only by holding for everything (restating '
          'Becoming.Boundaries).')
NEXT_ZH_OLD = '可判定性（P58）与不平衡关系项（P59）留给 Ren 的选择：“too dualist”是否读作强加于生成的是或否之分；是否采用把不平衡算作关系项的表示。'
NEXT_ZH_NEW = ('可判定性（P58）留给 Ren 的选择：“too dualist”是否读作强加于生成的是或否之分；不平衡关系项（P59）已由 Ren 2026-10-14 采用，'
               '即在每个世界中算入整体的其余（Becoming.Reading）。重建的读法仍待 Ren 判断：必然的规律不需要必然的条件（如曲率是区域的状态），'
               '新是来自部分之外的增益，第二部分的公理归于预设。')
NEXT_EN_OLD = ('Decidedness (P58) and the imbalance relatum (P59) leave Ren\'s choices: whether “too dualist” reads as the yes/no '
               'split imposed on becoming; whether to adopt the representation counting an imbalance as a relatum.')
NEXT_EN_NEW = ('Decidedness (P58) leaves Ren\'s choice whether “too dualist” reads as the yes/no split imposed on becoming; the '
               'imbalance relatum (P59) Ren adopted on 14 October 2026, as the rest of the whole counted in every world '
               '(Becoming.Reading). The re-founding\'s readings remain Ren\'s to judge: a necessary law needing no necessary '
               'condition (as curvature is a state of a region), novelty as gain from beyond the part, and the axiom of Part II '
               'coming to the presupposition.')


def reading():
    d = json.loads(READING.read_text())
    e = [x for x in d if x.get('id') == 'the-theory-of-becoming']
    assert len(e) == 1
    e = e[0]
    assert ARG_EN.strip() not in e['argument_en']
    e['argument_zh'] = e['argument_zh'] + ARG_ZH
    e['argument_en'] = e['argument_en'] + ARG_EN
    e['next_zh'] = sub1(e['next_zh'], NEXT_ZH_OLD, NEXT_ZH_NEW)
    e['next_en'] = sub1(e['next_en'], NEXT_EN_OLD, NEXT_EN_NEW)
    for m in ('Novelty', 'Reading', 'Readings'):
        path = LEAN + m + '.lean'
        assert path not in e['lean']
        e['lean'].append(path)
    e['source_sha256'] = hashlib.sha256((ROOT / CH).read_bytes()).hexdigest()
    READING.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    PREV = sys.argv[3]
    run = json.loads((ROOT / CORE).read_text())
    assert run['status'] == 'passed'
    utc = CORE.split('/')[-2]
    spine = [m for m in run['modules'] if m['spine']]
    theorems = sum(m['theorems'] for m in spine)
    audits = sum(len(m['declarations']) for m in spine)
    closure, package = len(run['core_closure']), len(run['spine_modules'])
    assert package == len(spine), (package, len(spine))
    bridges, inherited = len(run['bridge_modules']), len(run['inherited_receipts'])
    old = chapter(PREV, utc, theorems, audits, closure, package, bridges, inherited)
    reading()
    print('chapter totals', old, '->', dict(utc=utc, th=theorems, au=audits, cl=closure, pk=package, br=bridges,
                                              inh=inherited), '; reading entry reconciled and rehashed')
