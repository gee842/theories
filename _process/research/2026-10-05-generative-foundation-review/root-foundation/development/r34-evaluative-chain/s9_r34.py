#!/usr/bin/env python3
"""R34: the chapter's sentences on the receipt, the counts, the layers and the connectivity (English and
Chinese editions), after R33's chapter_text.py. The receipt facts are read from the receipt given, the layers
from layers34.py and the connectivity from THEOREM-CONNECTIVITY.json, and asserted against the text written.
Each replacement occurs once.
usage: python3 -B s9_r34.py RECEIPT_ID MAIN_COMMIT"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('layers34', HERE / 'layers34.py')
l34 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(l34)
layers = l34.layers
ROOT = HERE.parents[5]
CH = ROOT / 'theories/becoming/chapters'
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
RID, MAIN = sys.argv[1], sys.argv[2]
r = json.load(open(PKG / 'becoming-checks' / RID / 'verification.json'))
assert r['status'] == 'passed'
core = [m for m in r['modules'] if m.get('layer') == 'core']
found = [m for m in r['modules'] if m.get('layer') == 'foundation']


def thm(m):
    t = m.get('theorems')
    return len(t) if isinstance(t, list) else (t or 0)


T_CORE, T_FOUND = sum(thm(m) for m in core), sum(thm(m) for m in found)
DECL = sum(len(m.get('declarations', [])) for m in core)
RAN, REUSED = len(r['lean_steps']['ran']), len(r['lean_steps'].get('reused', []))
conn = json.load(open(RF / 'THEOREM-CONNECTIVITY.json'))
assert conn['core_receipt_at_commit'] == RID
APART, SPINE, ROOTS, CAT = conn['apart'], conn['spine_theorems'], conn['apart_roots'], conn['apart_roots_by_category']
BOTH = conn['classes']['statement on both families']
G3 = conn['classes']['statement on the base only through a law of its own module']
assert SPINE == T_CORE
lcore, mods, clo, layer, direct = layers.layers()
L1 = sum(1 for m in lcore if layer[m] == 1)
L2 = sum(1 for m in lcore if layer[m] == 2)
REACH = sum(1 for m in lcore if clo[m] & {'Becoming.Metaethics', 'Becoming.Significance'})
assert (L2, len(direct), REACH, L1) == (16, 16, 15, 258), (L2, len(direct), REACH, L1)
assert (len(core), T_CORE, DECL, APART, BOTH, ROOTS, G3) == (278, 11401, 15713, 476, 876, 340, 176), \
    (len(core), T_CORE, DECL, APART, BOTH, ROOTS, G3)

f = lambda n: f'{n:,}'
LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RFL = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RFL + 'BECOMING-RENEWAL-READING.md#225-one-evaluative-chain-r34'
WHAT_EN = ("one evaluative chain. Over the run, a part whose draws fall on renewed conditions does not narrow and a "
           "consumed dependence makes a part that opens nothing narrow, with the stepwise class and the consuming class "
           "alone as boundaries (`Becoming.Retaining`); on level paths the condition, significance and C read one object, "
           "admission; standpoints as formations, with `own` a closure, leave `sig` the only supplied evaluative "
           "parameter; the direction is a core schema on a web's moves (`Becoming.Direction`); and `Ranking`, "
           "`Relevance` and `ActiveReading` read their worlds as webs. Every kept declaration has the type it had or is a "
           "restatement listed in the study, and two are removed as the same statement as a kept one")
WHAT_ZH = ("一条评价之链：在整段上，汲取都落在被更新之条件上的部分不缩小，被消耗的依存使不打开什么的部分缩小，以逐步的类与单是消耗的类为界（`Becoming.Retaining`）；"
           "在水平路径上条件、意义与 C 读同一个对象，即接纳；以形成为立场、以闭包为 `own`，`sig` 是唯一给出的评价参数；方向是网之动作上的核心模式"
           "（`Becoming.Direction`）；`Ranking`、`Relevance` 与 `ActiveReading` 把世界读作网。每个保留的声明类型不变，或是研究中列出的重述，两个因与保留者陈述相同而删去")

EN = [
    ("on R33's tree (20 October 2026), 479 of the 11,381 spine theorems stand apart",
     f"on R34's tree (20 October 2026), {APART} of the {f(SPINE)} spine theorems stand apart"),
    ("and each of the 342 roots among them stands apart for a stated reason: a fact about one constructed model (205), a support lemma (82),",
     f"and each of the {ROOTS} roots among them stands apart for a stated reason: a fact about one constructed model ({CAT['model-witness']}), a support lemma ({CAT['support']}),"),
    ("In the theorem-connectivity measure on R33's tree the World family reaches the Process family",
     "In the theorem-connectivity measure on R34's tree the World family reaches the Process family"),
    ("859 statements use both, and 479 of the 11,381 spine theorems stand apart from both.",
     f"{BOTH} statements use both, and {APART} of the {f(SPINE)} spine theorems stand apart from both."),
    ("finds 479 of the 11,381 spine theorems apart from both base families at the last rerun (on R33's tree,",
     f"finds {APART} of the {f(SPINE)} spine theorems apart from both base families at the last rerun (on R34's tree,"),
    ("277 modules counting the root `Becoming`, and 280 in the core closure with the foundation.",
     f"{len(core)} modules counting the root `Becoming`, and {len(core) + len(found)} in the core closure with the foundation."),
    ("- L2 holds the 16 modules whose source names the continuation condition of §6.15 or a valuation (`Unrestricted`, `Valuation`), from `Becoming.Metaethics` and `Becoming.Significance` on, and the 3 modules that import one of them without naming either (`ActiveReading`, `Ranking`, `ScoreRepresentation`): 19 modules.",
     f"- L2 holds the {L2} modules whose source names the continuation condition of §6.15 or a valuation (`Unrestricted`, `Valuation`), from `Becoming.Metaethics` and `Becoming.Significance` on. No module imports one of them without naming either: `ActiveReading`, `Ranking` and `ScoreRepresentation` did until R34, which read their worlds as webs and state living significance beside `Extension` ([study §225]({STUDY}))."),
    ("- L1 holds the other 254:", f"- L1 holds the other {L1}:"),
    ("Eighteen core modules reach `Significance` or `Metaethics` through their imports: 138 did before R31",
     "Fifteen core modules reach `Significance` or `Metaethics` through their imports, 18 before R34: 138 did before R31"),
    ("is run `20261019T235844.485705Z`, frozen in [`becoming-checks/20261019T235844.485705Z/`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/20261019T235844.485705Z/verification.json).",
     f"is run `{RID}`, frozen in [`becoming-checks/{RID}/`]({LINK}becoming-checks/{RID}/verification.json)."),
    ("| Core modules (with the root `Becoming`, 0 theorems) | 277 modules, 11,381 theorems |",
     f"| Core modules (with the root `Becoming`, 0 theorems) | {len(core)} modules, {f(T_CORE)} theorems |"),
    ("| Core closure | 280 modules, 11,455 theorems |",
     f"| Core closure | {len(core) + len(found)} modules, {f(T_CORE + T_FOUND)} theorems |"),
    ("| Spine (the core; no bridge since the F3 sweep) | 11,381 theorems |",
     f"| Spine (the core; no bridge since the F3 sweep) | {f(T_CORE)} theorems |"),
    ("| Audited spine declarations | 15,687 |", f"| Audited spine declarations | {f(DECL)} |"),
    ("| Modules in the compile order | 280 |", f"| Modules in the compile order | {len(r['compile_order'])} |"),
    ("That run reused 1,036 cached Lean steps from `~/.cache/becoming-lean` and ran 84.",
     f"That run reused {f(REUSED)} cached Lean steps from `~/.cache/becoming-lean` and ran {f(RAN)}."),
]
ZH = [
    ("在 R33 树（2026-10-20）上的[定理层面的连通度量]", "在 R34 树（2026-10-20）上的[定理层面的连通度量]"),
    ("中，脊柱 11,381 条定理里有 479 条与两个基底族都散立，其中 342 个根各有说明的理由；",
     f"中，脊柱 {f(SPINE)} 条定理里有 {APART} 条与两个基底族都散立，其中 {ROOTS} 个根各有说明的理由；"),
    ("在 R33 树上的定理层面连通度量中，世界一族到达过程一族", "在 R34 树上的定理层面连通度量中，世界一族到达过程一族"),
    ("859 条陈述同时用到两族，脊柱的 11,381 条定理中 479 条与两族都散立。",
     f"{BOTH} 条陈述同时用到两族，脊柱的 {f(SPINE)} 条定理中 {APART} 条与两族都散立。"),
    ("的 16 个模块，以及导入它们而不说出两者的 3 个模块（`ActiveReading`、`Ranking`、`ScoreRepresentation`），共 19 个；其余 254 个为 L1。",
     f"的 {L2} 个模块；没有模块导入它们而不说出两者（`ActiveReading`、`Ranking` 与 `ScoreRepresentation` 到 R34 为止如此，R34 把它们的世界读作网，并把生命意义陈述在 `Extension` 旁，[研究 §225]({STUDY})）；其余 {L1} 个为 L1。"),
    ("通过导入到达 `Significance` 或 `Metaethics` 的核心模块现为 18 个：",
     f"通过导入到达 `Significance` 或 `Metaethics` 的核心模块现为 {REACH} 个，R34 之前为 18 个；"),
    ("下表的层与定理数随 R33 更新；", "下表的层与定理数随 R34 更新；"),
    ("：核心 277 个模块（含根模块 `Becoming`），11,381 项定理；连同三个基础模块，核心闭包 280 个模块、11,455 项定理；审计的脊柱声明 15,687 项",
     f"：核心 {len(core)} 个模块（含根模块 `Becoming`），{f(T_CORE)} 项定理；连同三个基础模块，核心闭包 {len(core) + len(found)} 个模块、{f(T_CORE + T_FOUND)} 项定理；审计的脊柱声明 {f(DECL)} 项"),
]


def run(path, subs):
    text = path.read_text()
    for old, new in subs:
        n = text.count(old)
        assert n == 1, (path.name, old[:80], n)
        text = text.replace(old, new)
    path.write_text(text)
    print(path.name, len(subs))


en = CH / 'THE-THEORY-OF-BECOMING.md'
text = en.read_text()
start = text.index("It was checked with Lean 4.29.1 on main 7950e8798 with R33 in the working tree: joins.")
end = text.index("It passed. Its counts:", start)
text = text[:start] + (f"It was checked with Lean 4.29.1 on main {MAIN} with R34 in the working tree: {WHAT_EN} "
                       f"([study §225]({STUDY})). ") + text[end:]
en.write_text(text)
run(en, EN)
zh = CH / 'THE-THEORY-OF-BECOMING.zh.md'
text = zh.read_text()
head = "的[当前回执 `20261019T235844.485705Z`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/20261019T235844.485705Z/verification.json)（Lean 4.29.1，main 7950e8798 加 R33："
start = text.index(head)
end = text.index("）：核心 277 个模块", start)
assert text.count(head) == 1
text = text[:start] + (f"的[当前回执 `{RID}`]({LINK}becoming-checks/{RID}/verification.json)（Lean 4.29.1，main {MAIN} 加 R34："
                       f"{WHAT_ZH}，[研究 §225]({STUDY})") + text[end:]
zh.write_text(text)
run(zh, ZH)
