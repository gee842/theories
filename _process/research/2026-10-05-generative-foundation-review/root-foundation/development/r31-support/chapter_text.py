#!/usr/bin/env python3
"""R31: the chapter's §9 sentences on layers, receipt and counts (English and Chinese editions).

Each replacement occurs exactly once (a rerun skips one already applied). The receipt facts are read
from the receipt given and the connectivity numbers from THEOREM-CONNECTIVITY.json, so the text says
what they say. usage: python3 -B chapter_text.py RECEIPT_ID MAIN_COMMIT"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
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


T_CORE = sum(thm(m) for m in core)
T_FOUND = sum(thm(m) for m in found)
DECL = sum(len(m.get('declarations', [])) for m in core)
steps = r['lean_steps']
RAN = len(steps['ran'])
REUSED = len(steps.get('reused', []))
GEN = len(r.get('generated_axiom_dependencies', {}))
conn = json.load(open(RF / 'THEOREM-CONNECTIVITY.json'))
APART = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
SPINE = conn['spine_theorems']
assert conn['core_receipt_at_commit'] == RID, conn['core_receipt_at_commit']
assert SPINE == T_CORE, (SPINE, T_CORE)
LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
STUDY = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#222-layers-and-one-prelude-r31'
f = lambda n: f'{n:,}'

EN = [
    (re.compile(r"finds 485 of the 11,684 spine theorems apart from both base families at the last rerun \(on R28's tree;"),
     f"finds {f(APART)} of the {f(SPINE)} spine theorems apart from both base families at the last rerun (on R31's tree;"),
    (re.compile(r"\*\*The current receipt\.\*\* .*? It passed\. Its counts:", re.S),
     f"**The current receipt.** The [current receipt]({LINK}becoming-verification.json) is run `{RID}`, frozen in "
     f"[`becoming-checks/{RID}/`]({LINK}becoming-checks/{RID}/verification.json). It was checked with Lean 4.29.1 on main "
     f"{MAIN} with R31 in the working tree: layers and one prelude. The conditional theorems moved into companion modules "
     "after `Becoming.Significance`, the law-level notions into `Becoming.Laws`, and the lemmas on numbers, truth values, "
     "lists and options into `Becoming.Prelude`, each stated once: 111 copies were removed and their uses point to the kept "
     "name, and `Becoming.Order` was split into `Stuttering`, `Reordering` and `IdleRemoval`. Every kept declaration has the "
     f"type it had ([study §222]({STUDY})). It passed. Its counts:"),
    (re.compile(r"\| Core modules \(with the root `Becoming`, 0 theorems\) \| [\d,]+ modules, [\d,]+ theorems \|"),
     f"| Core modules (with the root `Becoming`, 0 theorems) | {len(core)} modules, {f(T_CORE)} theorems |"),
    (re.compile(r"\| Foundation modules \| 3 modules, [\d,]+ theorems \|"), f"| Foundation modules | 3 modules, {T_FOUND} theorems |"),
    (re.compile(r"\| Core closure \| [\d,]+ modules, [\d,]+ theorems \|"),
     f"| Core closure | {len(core) + len(found)} modules, {f(T_CORE + T_FOUND)} theorems |"),
    (re.compile(r"\| Spine \(the core; no bridge since the F3 sweep\) \| [\d,]+ theorems \|"),
     f"| Spine (the core; no bridge since the F3 sweep) | {f(T_CORE)} theorems |"),
    (re.compile(r"\| Audited spine declarations \| [\d,]+ \|"), f"| Audited spine declarations | {f(DECL)} |"),
    (re.compile(r"\| Modules in the compile order \| [\d,]+ \|"), f"| Modules in the compile order | {len(r['compile_order'])} |"),
    (re.compile(r"\| Generated `injEq` lemmas on `propext` \| [\d,]+ in the core closure \|"),
     f"| Generated `injEq` lemmas on `propext` | {GEN} in the core closure |"),
    (re.compile(r"- That run reused [\d,]+ cached Lean steps from `~/.cache/becoming-lean` and ran [\d,]+ \([^)]*\)\."),
     f"- That run reused {f(REUSED)} cached Lean steps from `~/.cache/becoming-lean` and ran {f(RAN)}."),
]
ZH = [
    (re.compile(r"核心（`Becoming.World`，L0 及其两个基础模块，加 L1–L4；一个基底是运行，导入树从基础与 `Becoming.Frame` 开始，"),
     "核心（基础之上的 L0：`Becoming.Prelude`、`Becoming.Frame` 与 `Becoming.World`，加 L1 与 L2；一个基底是运行，导入树从基础与只导入 "
     "`Init` 的 `Becoming.Prelude` 开始，`Becoming.Frame` 导入它与 `GenerativeCore`，"),
    (re.compile(r"`import Becoming` 导入全部四层，"), "`import Becoming` 导入全部三层，"),
    (re.compile(r"(\n\| 层 \| 模块 \| 内容 \| 定理 \|)"),
     "\n各层是每个模块的源码与导入的可检查性质，由 [`layers.py`](../../../_process/research/2026-10-05-generative-foundation-review/"
     "root-foundation/development/r31-support/layers.py) 计算：L0 是基底 `Becoming.World`、`Becoming.Frame` 与 `Becoming.Prelude`；"
     "L2 是源码说出 §6.15 的延续条件或赋值（`Unrestricted`、`Valuation`）的 17 个模块，以及导入它们而不说出两者的 4 个模块"
     "（`ActiveReading`、`BoundaryWorlds`、`Ranking`、`ScoreRepresentation`），共 21 个；其余 280 个为 L1。没有模块导入更高层的模块，"
     "脚本检查这一点；所以不用条件的定理与条件分开：通过导入到达 `Significance` 或 `Metaethics` 的核心模块现为 20 个，R31 之前为 138 个"
     f"（[研究 §222]({STUDY})）。下表的层与定理数随 R31 更新；生成的模块表见[包说明]({LINK}README.zh.md)。\n\\1"),
    (re.compile(r"的\[当前回执 `[0-9TZ.]+`\]\([^)]*\)（Lean 4\.29\.1，main [0-9a-f]+ 加 R30：.*?\[研究 §221\]\([^)]*\)）："
                r"核心 [\d,]+ 个模块（含根模块 `Becoming`），[\d,]+ 项定理；连同三个基础模块，核心闭包 [\d,]+ 个模块、[\d,]+ 项定理；"
                r"审计的脊柱声明 [\d,]+ 项", re.S),
     f"的[当前回执 `{RID}`]({LINK}becoming-checks/{RID}/verification.json)（Lean 4.29.1，main {MAIN} 加 R31：层与一个前导；"
     "条件定理移入 `Becoming.Significance` 之后的伴随模块，律层概念移入 `Becoming.Laws`，关于数、真值、列表与选项的引理移入 "
     "`Becoming.Prelude`，每条只陈述一次：删去 111 个副本，用处改指保留的名称；`Becoming.Order` 拆为 `Stuttering`、`Reordering` 与 "
     f"`IdleRemoval`；每个保留的声明类型不变，[研究 §222]({STUDY})）：核心 {len(core)} 个模块（含根模块 `Becoming`），{f(T_CORE)} 项定理；"
     f"连同三个基础模块，核心闭包 {len(core) + len(found)} 个模块、{f(T_CORE + T_FOUND)} 项定理；审计的脊柱声明 {f(DECL)} 项"),
]

for path, subs in ((CH / 'THE-THEORY-OF-BECOMING.md', EN), (CH / 'THE-THEORY-OF-BECOMING.zh.md', ZH)):
    text = path.read_text()
    for pat, new in subs:
        hits = pat.findall(text)
        if len(hits) == 0 and (new.replace('\\1', '') in text):
            continue
        assert len(hits) == 1, (path.name, pat.pattern[:70], len(hits))
        text = pat.sub(lambda m: m.expand(new) if '\\1' in new else new, text, count=1)
    path.write_text(text)
    print(path.name, 'done')
print('core', len(core), T_CORE, 'decl', DECL, 'ran', RAN, 'reused', REUSED, 'apart', APART)
