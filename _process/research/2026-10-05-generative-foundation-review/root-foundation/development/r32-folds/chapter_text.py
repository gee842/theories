#!/usr/bin/env python3
"""R32: the chapter's sentences on the receipt, the counts, the layers and the connectivity (English and
Chinese editions), after R31's chapter_text.py.

Each replacement is exact and occurs once (a rerun skips one already applied). The receipt facts are read
from the receipt given, the layer counts from layers.py (with the folded modules gone) and the
connectivity numbers from THEOREM-CONNECTIVITY.json, so the text says what they say.
usage: python3 -B chapter_text.py RECEIPT_ID MAIN_COMMIT"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import fold  # noqa: E402
import layers  # noqa: E402

layers.GONE += ['Becoming.' + x for x, _ in fold.FOLDS]
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
assert conn['core_receipt_at_commit'] == RID, conn['core_receipt_at_commit']
APART = conn['apart']
SPINE = conn['spine_theorems']
assert SPINE == T_CORE, (SPINE, T_CORE)
ROOTS = conn['apart_roots']
CAT = conn['apart_roots_by_category']
BOTH = conn['classes']['statement on both families']
G3 = conn['classes']['statement on the base only through a law of its own module']
lcore, mods, clo, layer, direct = layers.layers()
L1 = sum(1 for m in lcore if layer[m] == 1)
L2 = sum(1 for m in lcore if layer[m] == 2)
L2_NAMING = len(direct)
L2_IMPORTING = sorted(m[9:] for m in lcore if layer[m] == 2 and m not in direct)
ETHICS = {'Becoming.Metaethics', 'Becoming.Significance'}
REACH = sum(1 for m in lcore if clo[m] & ETHICS)
assert (L2, L2_NAMING, REACH) == (19, 16, 18), (L2, L2_NAMING, REACH)

f = lambda n: f'{n:,}'
LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RFL = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RFL + 'BECOMING-RENEWAL-READING.md#223-forwarders-copies-and-reading-modules-r32'
STUDY31 = RFL + 'BECOMING-RENEWAL-READING.md#222-layers-and-one-prelude-r31'
C10 = RFL + 'THEOREM-CONNECTIVITY.md#10-reruns-on-each-landing-17-19-october-2026'
C11 = RFL + 'THEOREM-CONNECTIVITY.md#11-r32-the-measure-stops-rewarding-restatement'
WHAT_EN = ('forwarders, copies and reading modules. 173 pure forwarders, theorems whose whole proof applies another law to '
           'their own binders, were removed, and their uses point to the law; 61 copies of a statement stated elsewhere were '
           'removed, twelve of them by stating the statement once in `Becoming.Prelude`; and 26 reading and small modules '
           'were folded into the module they read as its final section, their declarations and names unchanged')
WHAT_ZH = ('转发、副本与读取模块：删去 173 个纯转发（整个证明只把另一条律应用于自己的约束变量的定理），用处改指该律；删去 61 个在别处已有陈述的副本，'
           '其中十二条改为在 `Becoming.Prelude` 中只陈述一次；26 个读取模块与小模块作为末节折入其所读模块，声明与名称不变')
L2_EN = ', '.join(f'`{m}`' for m in L2_IMPORTING)
L2_ZH = '、'.join(f'`{m}`' for m in L2_IMPORTING)

EN = [
    (f"In the [theorem-level measurement]({C10}) on R28's tree (20 October 2026), 485 of the 11,684 spine theorems stand apart "
     "from both base families (195 of 7,698 on 17 October, after the join modules of board item U), and each of the 345 roots "
     "among them stands apart for a stated reason: a fact about one constructed model (205), a support lemma (85), a general "
     "structure (31), a restatement (12), a statement of logical strength alone (10) or a calibration (2).",
     f"In the [theorem-level measurement]({C11}) on R32's tree (20 October 2026), {APART} of the {f(SPINE)} spine theorems stand "
     f"apart from both base families (195 of 7,698 on 17 October, after the join modules of board item U), and each of the "
     f"{ROOTS} roots among them stands apart for a stated reason: a fact about one constructed model ({CAT['model-witness']}), "
     f"a support lemma ({CAT['support']}), a general structure ({CAT['general-structure']}), a restatement ({CAT['restates']}), "
     f"a statement of logical strength alone ({CAT['logical-strength']}) or a calibration ({CAT['calibration']}). Since R32 the "
     f"measure counts no named one-line restatement as a connection, and it reports apart the {G3} statements that reach the "
     "base only through a law of their own module."),
    ("In the theorem-connectivity measure on R28's tree the World family now reaches the Process family",
     "In the theorem-connectivity measure on R32's tree the World family reaches the Process family"),
    ("870 statements use both, and 485 of the 11,684 spine theorems stand apart from both.",
     f"{BOTH} statements use both, and {APART} of the {f(SPINE)} spine theorems stand apart from both."),
    (f"finds 481 of the 11,566 spine theorems apart from both base families at the last rerun (on R31's tree; the reruns are "
     f"logged in [its §10]({C10}))",
     f"finds {APART} of the {f(SPINE)} spine theorems apart from both base families at the last rerun (on R32's tree, under the "
     f"measure that since R32 counts no named restatement as a connection, [its §11]({C11}); the earlier reruns are logged in "
     f"[its §10]({C10}))"),
    ("305 modules counting the root `Becoming`, and 308 in the core closure with the foundation.",
     f"{len(core)} modules counting the root `Becoming`, and {len(core) + len(found)} in the core closure with the foundation."),
    ("and the 4 modules that import one of them without naming either (`ActiveReading`, `BoundaryWorlds`, `Ranking`, "
     "`ScoreRepresentation`): 21 modules.",
     f"and the {len(L2_IMPORTING)} modules that import one of them without naming either ({L2_EN}): {L2} modules."),
    ("- L2 holds the 17 modules whose source names", f"- L2 holds the {L2_NAMING} modules whose source names"),
    ("- L1 holds the other 280:", f"- L1 holds the other {L1}:"),
    (f"Twenty core modules reach `Significance` or `Metaethics` through their imports, 138 before ([study §222]({STUDY31})).",
     f"Eighteen core modules reach `Significance` or `Metaethics` through their imports: 138 did before R31 ([study §222]({STUDY31})), "
     f"and 20 before R32 folded `BoundaryFlows` and `BoundaryWorlds` into `Boundaries` ([study §223]({STUDY}))."),
    (re.compile(r"It was checked with Lean 4\.29\.1 on main 5c55b36f4 with R31 in the working tree: layers and one prelude\..*?"
                r"\(\[study §222\]\([^)]*\)\)\. It passed\. Its counts:", re.S),
     f"It was checked with Lean 4.29.1 on main {MAIN} with R32 in the working tree: {WHAT_EN}. Every kept declaration has the "
     f"type it had ([study §223]({STUDY})). It passed. Its counts:"),
    (re.compile(r"is run `20261019T213206\.644158Z`, frozen in \[`becoming-checks/20261019T213206\.644158Z/`\]\([^)]*\)\."),
     f"is run `{RID}`, frozen in [`becoming-checks/{RID}/`]({LINK}becoming-checks/{RID}/verification.json)."),
    ("| Core modules (with the root `Becoming`, 0 theorems) | 305 modules, 11,566 theorems |",
     f"| Core modules (with the root `Becoming`, 0 theorems) | {len(core)} modules, {f(T_CORE)} theorems |"),
    ("| Foundation modules | 3 modules, 74 theorems |", f"| Foundation modules | 3 modules, {T_FOUND} theorems |"),
    ("| Core closure | 308 modules, 11,640 theorems |",
     f"| Core closure | {len(core) + len(found)} modules, {f(T_CORE + T_FOUND)} theorems |"),
    ("| Spine (the core; no bridge since the F3 sweep) | 11,566 theorems |",
     f"| Spine (the core; no bridge since the F3 sweep) | {f(T_CORE)} theorems |"),
    ("| Audited spine declarations | 15,857 |", f"| Audited spine declarations | {f(DECL)} |"),
    ("| Modules in the compile order | 308 |", f"| Modules in the compile order | {len(r['compile_order'])} |"),
    ("| Generated `injEq` lemmas on `propext` | 188 in the core closure |",
     f"| Generated `injEq` lemmas on `propext` | {GEN} in the core closure |"),
    ("- That run reused 1,225 cached Lean steps from `~/.cache/becoming-lean` and ran 7; R31's earlier runs on the way ran the "
     "rest (study §222).",
     f"- That run reused {f(REUSED)} cached Lean steps from `~/.cache/becoming-lean` and ran {f(RAN)}."),
]
ZH = [
    (f"在 R28 树（2026-10-20）上的[定理层面的连通度量]({C10})中，脊柱 11,684 条定理里有 485 条与两个基底族都散立，其中 345 个根各有说明的理由；",
     f"在 R32 树（2026-10-20）上的[定理层面的连通度量]({C11})中，脊柱 {f(SPINE)} 条定理里有 {APART} 条与两个基底族都散立，其中 {ROOTS} "
     f"个根各有说明的理由；自 R32 起度量不把具名的一行重述算作连接，并把只经由本模块之律到达基底的 {G3} 条陈述另行报告；"),
    ("在 R28 树上的定理层面连通度量中，世界一族现在到达过程一族", "在 R32 树上的定理层面连通度量中，世界一族到达过程一族"),
    ("870 条陈述同时用到两族，脊柱的 11,684 条定理中 485 条与两族都散立。",
     f"{BOTH} 条陈述同时用到两族，脊柱的 {f(SPINE)} 条定理中 {APART} 条与两族都散立。"),
    ("的 17 个模块，以及导入它们而不说出两者的 4 个模块（`ActiveReading`、`BoundaryWorlds`、`Ranking`、`ScoreRepresentation`），共 21 个；其余 280 个为 L1。",
     f"的 {L2_NAMING} 个模块，以及导入它们而不说出两者的 {len(L2_IMPORTING)} 个模块（{L2_ZH}），共 {L2} 个；其余 {L1} 个为 L1。"),
    (f"现为 20 个，R31 之前为 138 个（[研究 §222]({STUDY31})）。下表的层与定理数随 R31 更新；",
     f"现为 18 个：R31 之前为 138 个（[研究 §222]({STUDY31})），R32 把 `BoundaryFlows` 与 `BoundaryWorlds` 折入 `Boundaries` 之前为 20 个"
     f"（[研究 §223]({STUDY})）。下表的层与定理数随 R32 更新；"),
    (re.compile(r"的\[当前回执 `20261019T213206\.644158Z`\]\([^)]*\)（Lean 4\.29\.1，main 5c55b36f4 加 R31：.*?\[研究 §222\]\([^)]*\)）："
                r"核心 305 个模块（含根模块 `Becoming`），11,566 项定理；连同三个基础模块，核心闭包 308 个模块、11,640 项定理；审计的脊柱声明 15,857 项", re.S),
     f"的[当前回执 `{RID}`]({LINK}becoming-checks/{RID}/verification.json)（Lean 4.29.1，main {MAIN} 加 R32：{WHAT_ZH}；"
     f"每个保留的声明类型不变，[研究 §223]({STUDY})）：核心 {len(core)} 个模块（含根模块 `Becoming`），{f(T_CORE)} 项定理；"
     f"连同三个基础模块，核心闭包 {len(core) + len(found)} 个模块、{f(T_CORE + T_FOUND)} 项定理；审计的脊柱声明 {f(DECL)} 项"),
]

for path, subs in ((CH / 'THE-THEORY-OF-BECOMING.md', EN), (CH / 'THE-THEORY-OF-BECOMING.zh.md', ZH)):
    text = path.read_text()
    for old, new in subs:
        if isinstance(old, str):
            n = text.count(old)
            if n == 0 and new in text:
                continue
            assert n == 1, (path.name, old[:80], n)
            text = text.replace(old, new)
        else:
            hits = old.findall(text)
            if not hits and new in text:
                continue
            assert len(hits) == 1, (path.name, old.pattern[:80], len(hits))
            text = old.sub(lambda m: new, text, count=1)
    path.write_text(text)
    print(path.name, 'done')
print('core', len(core), T_CORE, 'decl', DECL, 'ran', RAN, 'reused', REUSED, 'apart', APART, 'roots', ROOTS, 'L1', L1, 'L2', L2)
