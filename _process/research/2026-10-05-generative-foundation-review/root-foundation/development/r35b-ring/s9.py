#!/usr/bin/env python3
"""R35b: chapter section 9 (EN, ZH) from the passing receipt. Usage (checkout root): python3 -B s9.py RECEIPT_ID BASE"""
import json
import sys
from collections import Counter

RID, BASE = sys.argv[1], sys.argv[2]
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
ring_m = mods['instance'] + mods['application']
ring_t = thms['instance'] + thms['application']
n = lambda x: f'{x:,}'
print(dict(mods), dict(thms), spine_decls, spine_thms, closure, closure_thms, injeq, ran, reused)

CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
s = open(CH).read()


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:90]
    s = s.replace(old, new)


rep("- *Core*: the foundation modules `GenerativeCore`, `InquirySufficiency` and `RelationalRenewal`, with the base and its layers: 278 modules counting the root `Becoming`, 281 in the closure with the foundation.",
    f"- *Core*: the foundation modules `GenerativeCore`, `InquirySufficiency` and `RelationalRenewal`, with the base and its layers: {mods['core']} modules counting the root `Becoming`.\n"
    f"- *Instances and applications* (R35b, 20 October 2026): the instances read general laws of the core on one named carrier, the Changes (`Becoming.Hexagrams`, `HexagramPlaces`, `HexagramCommuting`, `HexagramLaws`, `HexagramSites`, `HexagramSequences`) and `Becoming.PlaceTransitionNets`, {mods['instance']} modules; the applications are leaves no core module imports (`Becoming.Dispatch`, `GuardHorizon`, `ResponseLearning`, `Coverage`, `SeedReach`, `ScopedReach`), {mods['application']} modules. They are held to the core's conditions (the closure of the core and the ring is {closure} modules with the foundation, compiled from the prelude, every axiom report empty) and lie outside the core by direction: no core module but the root imports one of them, and no instance imports an application (`INSTANCES`, `APPLICATIONS` and `ring_direction` in the checker). The split of `Becoming.Commuting`'s instance section into `Becoming.HexagramCommuting` made the Changes' chain importer-free; no file moved.")
rep("the instance modules and the Python experiments; it may use any tool",
    "the periphery's instance modules and the Python experiments; it may use any tool")
rep("L1, the other 258.", "L1, the other 246 of the core, and the 13 modules of the instance and applications ring, all L1.")
i = s.index('**The current receipt** is run [`20261020T005554.047169Z`]')
j = s.index('\n', i)
s = s[:i] + (f"**The current receipt** is run [`{RID}`](../../../{PKG}becoming-checks/{RID}/verification.json) (the [current pointer](../../../{PKG}becoming-verification.json)), "
             f"checked with Lean 4.29.1 on main {BASE[:9]} with R35b in the working tree ([study §228](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#228-the-instance-and-applications-ring-r35b)). "
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
rep("The run reused 1,117 cached Lean steps from `~/.cache/becoming-lean` and ran 7;",
    f"The run reused {n(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran};")
open(CH, 'w').write(s)

ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
z = open(ZH).read()


def zrep(old, new):
    global z
    assert z.count(old) == 1, old[:60]
    z = z.replace(old, new)


zrep("三层由各模块的源码与导入经", f"核心之外是实例与应用环（R35b）：实例在一个具名载体上读核心的一般规律（《周易》诸模块与 `Becoming.PlaceTransitionNets`，{mods['instance']} 个模块），应用是核心无一导入的叶子（`Becoming.Dispatch` 等 {mods['application']} 个模块）；二者受核心同样的条件约束（只用前导编译，公理报告为空），按方向在核心之外：除根 `Becoming` 外没有核心模块导入它们，没有实例导入应用（检查器的 `INSTANCES`、`APPLICATIONS` 与 `ring_direction`）。`Becoming.Commuting` 的实例一节分出为 `Becoming.HexagramCommuting`，没有文件移动。三层由各模块的源码与导入经")
zrep("L1 258 个", "L1 核心中 246 个，另有实例与应用环的 13 个模块，皆为 L1")
i = z.index('**当前回执**是运行 [`20261020T005554.047169Z`]')
j = z.index('\n', i)
z = z[:i] + f"**当前回执**是运行 [`{RID}`](../../../{PKG}becoming-checks/{RID}/verification.json)（[当前指针](../../../{PKG}becoming-verification.json)），以 Lean 4.29.1 检查（[研究第 228 节](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#228-the-instance-and-applications-ring-r35b)）。" + z[j:]
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
