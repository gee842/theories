#!/usr/bin/env python3
"""R37c: chapter section 9 (EN, ZH) from the passing receipt, the s9.py of development/r38-open-joins with
the old values read from the chapter rather than written in.
Usage (checkout root): python3 -B s9.py RECEIPT_ID BASE SECTION_ANCHOR

The receipt paragraph, the counts table, the core's module count, the L1 count and the cached steps follow
the run; SECTION_ANCHOR is the study section's anchor (for example
234-the-counted-corollaries-as-compositions-r37c)."""
import json
import re
import sys
from collections import Counter

RID, BASE, ANCHOR = sys.argv[1], sys.argv[2], sys.argv[3]
SECTION = ANCHOR.split('-', 1)[0]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
R = json.load(open(PKG + 'becoming-checks/' + RID + '/verification.json'))
assert R['status'] == 'passed' and R['source_unchanged_during_check']
mods, thms = Counter(), Counter()
for m in R['modules']:
    mods[m['layer']] += 1
    thms[m['layer']] += m['theorems']
spine_decls = sum(len(m['declarations']) for m in R['modules'] if m['spine'])
spine_thms = sum(m['theorems'] for m in R['modules'] if m['spine'])
closure = len(R['core_closure'])
closure_thms = sum(m['theorems'] for m in R['modules'] if m['module'] in R['core_closure'])
injeq = len(R.get('generated_axiom_dependencies', {}))
steps = R['lean_steps']
ran, reused = len(steps['ran']), len(steps['reused'])
L2 = int(re.search(r'L2, the ([0-9]+) modules whose source names the condition',
                    open('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md').read()).group(1))
L1 = mods['core'] - 1 - 3 - L2  # the root, L0 and L2 (layers37.py)
n = lambda x: f'{x:,}'
print(dict(mods), dict(thms), spine_decls, spine_thms, closure, closure_thms, injeq, ran, reused, L1)
STUDY = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#' + ANCHOR

CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
s = open(CH).read()


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:90]
    s = s.replace(old, new)


s, _n = re.subn(r"with the base and its layers: [0-9]+ modules counting the root `Becoming`.",
                f"with the base and its layers: {mods['core']} modules counting the root `Becoming`.", s)
assert _n == 1
s, _n = re.subn(r"L1, the other [0-9]+ of the core,", f"L1, the other {L1} of the core,", s)
assert _n == 1
i = s.index('**The current receipt** is run [`')
j = s.index('\n', i)
s = s[:i] + (f"**The current receipt** is run [`{RID}`](../../../{PKG}becoming-checks/{RID}/verification.json) (the [current pointer](../../../{PKG}becoming-verification.json)), "
             f"checked with Lean 4.29.1 on main {BASE[:9]} with R37c in the working tree ([study §{SECTION}]({STUDY})). "
             "It passed, the source unchanged during the check and the core with the ring compiled from the prelude.") + s[j:]
i = s.index('| Core modules (with the root `Becoming`, 0 theorems) |')
j = s.index('| Generated `injEq` lemmas on `propext` |', i)
j = s.index('\n', j)
s = s[:i] + f"""| Core modules (with the root `Becoming`, 0 theorems) | {mods['core']} modules, {n(thms['core'])} theorems |
| Instance modules | {mods['instance']} modules, {n(thms['instance'])} theorems |
| Application modules | {mods['application']} modules, {n(thms['application'])} theorems |
| Foundation modules | {mods['foundation']} modules, {thms['foundation']} theorems |
| Closure (core, ring and foundation) | {closure} modules, {n(closure_thms)} theorems |
| Spine (the core and the ring; no bridge since F3) | {n(spine_thms)} theorems |
| Audited spine declarations | {n(spine_decls)} |
| Inherited modules bound to passed receipts by hash | {mods['inherited'] or 3} (the foundation) |
| Superseded periphery modules (out of the run, bytes kept) | {len(R['superseded_modules'])} |
| Modules in the compile order | {len(R['compile_order'])} |
| Generated `injEq` lemmas on `propext` | {injeq} in the closure |""" + s[j:]
s, _n = re.subn(r"The run reused [0-9,]+ cached Lean steps from `~/.cache/becoming-lean` and ran [0-9]+;",
              f"The run reused {n(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran};", s)
assert _n == 1
open(CH, 'w').write(s)

ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
z = open(ZH).read()


def zrep(old, new):
    global z
    assert z.count(old) == 1, old[:60]
    z = z.replace(old, new)


z, _n = re.subn(r"L1 核心中 [0-9]+ 个", f"L1 核心中 {L1} 个", z)
assert _n == 1
i = z.index('**当前回执**是运行 [`')
j = z.index('\n', i)
z = z[:i] + f"**当前回执**是运行 [`{RID}`](../../../{PKG}becoming-checks/{RID}/verification.json)（[当前指针](../../../{PKG}becoming-verification.json)），以 Lean 4.29.1 检查（[研究第 {SECTION} 节]({STUDY})）。" + z[j:]
i = z.index('| 核心模块（含根 `Becoming`） |')
j = z.index('| 被取代的外围模块', i)
j = z.index('\n', j)
z = z[:i] + f"""| 核心模块（含根 `Becoming`） | {mods['core']} 个模块，{n(thms['core'])} 条定理 |
| 实例模块 | {mods['instance']} 个模块，{n(thms['instance'])} 条定理 |
| 应用模块 | {mods['application']} 个模块，{n(thms['application'])} 条定理 |
| 根基模块 | {mods['foundation']} 个模块，{thms['foundation']} 条定理 |
| 闭包（核心、环与根基） | {closure} 个模块，{n(closure_thms)} 条定理 |
| 审计的脊柱声明 | {n(spine_decls)} |
| 在 `propext` 上的生成的 `injEq` 引理 | 闭包中 {injeq} 条 |
| 被取代的外围模块（不在运行中，字节保留） | {len(R['superseded_modules'])} |""" + z[j:]
open(ZH, 'w').write(z)
