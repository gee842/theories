#!/usr/bin/env python3
"""R33: the chapter's sentences on the receipt, the counts, the layers and the connectivity (English and
Chinese editions), after R32's chapter_text.py.

Each replacement is exact and occurs once (a rerun skips one already applied). The receipt facts are read
from the receipt given, the layer counts from layers.py (with the joined modules gone) and the
connectivity numbers from THEOREM-CONNECTIVITY.json, so the text says what they say.
usage: python3 -B chapter_text.py RECEIPT_ID MAIN_COMMIT"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r32-folds'))
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import fold  # noqa: E402
import layers  # noqa: E402

layers.GONE += ['Becoming.' + x for x, _ in fold.FOLDS]
layers.GONE += ['Becoming.LawThroughCoupling', 'Becoming.LawThroughChangingCoupling']
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
ETHICS = {'Becoming.Metaethics', 'Becoming.Significance'}
REACH = sum(1 for m in lcore if clo[m] & ETHICS)
assert (L2, L2_NAMING, REACH) == (19, 16, 18), (L2, L2_NAMING, REACH)

f = lambda n: f'{n:,}'
LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RFL = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RFL + 'BECOMING-RENEWAL-READING.md#224-joins-r33'
STUDY32 = RFL + 'BECOMING-RENEWAL-READING.md#223-forwarders-copies-and-reading-modules-r32'
C11 = RFL + 'THEOREM-CONNECTIVITY.md#11-r32-the-measure-stops-rewarding-restatement'
WHAT_EN = ('joins. The criterion along one run through a projection, through what a formation couples into and through '
           'coupling that changes is one law under an equivalence in `Becoming.LawAlongRun`, the other two modules '
           'joined into it with their names; learning through a map is tracking in the limit, identification where '
           'the feature is invariant; a loop link\'s factor is apart from a coupling strength and the self-loop\'s '
           'return map is the carried amount; the tolerance law is a web\'s run; and an interleaving builds a `World`')
WHAT_ZH = ('并合：沿一个运行经投影、经形成所耦合者与经改变的耦合的判据，在 `Becoming.LawAlongRun` 中是等价关系之下的一条规律，另两个模块以原名并入；'
           '经映射的学习是极限中的跟随，特征不变时即辨识；回路环节的倍率与耦合强度分开，自环的回返映射就是所携带的量；容忍律是网的运行；交错构造 `World`')

OLD_RUN = ("That run reused 441 cached Lean steps from `~/.cache/becoming-lean` and ran 687; R32's earlier run, "
           "`20261019T225814.056669Z`, passed with the same counts before the docs followed the removals (study §223).")
EN = [
    (f"In the [theorem-level measurement]({C11}) on R32's tree (20 October 2026), 473 of the 11,330 spine theorems stand "
     "apart from both base families (195 of 7,698 on 17 October, after the join modules of board item U), and each of the "
     "342 roots among them stands apart for a stated reason: a fact about one constructed model (205), a support lemma "
     "(83), a general structure (33), a restatement (9), a statement of logical strength alone (10) or a calibration (2). "
     "Since R32 the measure counts no named one-line restatement as a connection, and it reports apart the 172 statements "
     "that reach the base only through a law of their own module.",
     f"In the [theorem-level measurement]({C11}) on R33's tree (20 October 2026), {APART} of the {f(SPINE)} spine theorems "
     f"stand apart from both base families (195 of 7,698 on 17 October, after the join modules of board item U), and each "
     f"of the {ROOTS} roots among them stands apart for a stated reason: a fact about one constructed model "
     f"({CAT['model-witness']}), a support lemma ({CAT['support']}), a general structure ({CAT['general-structure']}), a "
     f"restatement ({CAT['restates']}), a statement of logical strength alone ({CAT['logical-strength']}) or a calibration "
     f"({CAT['calibration']}). Since R32 the measure counts no named one-line restatement as a connection, and it reports "
     f"apart the {G3} statements that reach the base only through a law of their own module."),
    ("In the theorem-connectivity measure on R32's tree the World family reaches the Process family",
     "In the theorem-connectivity measure on R33's tree the World family reaches the Process family"),
    ("850 statements use both, and 473 of the 11,330 spine theorems stand apart from both.",
     f"{BOTH} statements use both, and {APART} of the {f(SPINE)} spine theorems stand apart from both."),
    ("finds 473 of the 11,330 spine theorems apart from both base families at the last rerun (on R32's tree, under the "
     "measure that since R32 counts no named restatement as a connection,",
     f"finds {APART} of the {f(SPINE)} spine theorems apart from both base families at the last rerun (on R33's tree, under "
     "the measure that since R32 counts no named restatement as a connection,"),
    ("279 modules counting the root `Becoming`, and 282 in the core closure with the foundation.",
     f"{len(core)} modules counting the root `Becoming`, and {len(core) + len(found)} in the core closure with the foundation."),
    ("- L1 holds the other 256:", f"- L1 holds the other {L1}:"),
    (re.compile(r"It was checked with Lean 4\.29\.1 on main ad2efa757 with R32 in the working tree: forwarders, copies and "
                r"reading modules\..*?\(\[study §223\]\([^)]*\)\)\. It passed\. Its counts:", re.S),
     f"It was checked with Lean 4.29.1 on main {MAIN} with R33 in the working tree: {WHAT_EN}. Every kept declaration has "
     f"the type it had, three under the names of R33's rename table ([study §224]({STUDY})). It passed. Its counts:"),
    (re.compile(r"is run `20261019T231053\.882924Z`, frozen in \[`becoming-checks/20261019T231053\.882924Z/`\]\([^)]*\)\."),
     f"is run `{RID}`, frozen in [`becoming-checks/{RID}/`]({LINK}becoming-checks/{RID}/verification.json)."),
    ("| Core modules (with the root `Becoming`, 0 theorems) | 279 modules, 11,330 theorems |",
     f"| Core modules (with the root `Becoming`, 0 theorems) | {len(core)} modules, {f(T_CORE)} theorems |"),
    ("| Foundation modules | 3 modules, 74 theorems |", f"| Foundation modules | 3 modules, {T_FOUND} theorems |"),
    ("| Core closure | 282 modules, 11,404 theorems |",
     f"| Core closure | {len(core) + len(found)} modules, {f(T_CORE + T_FOUND)} theorems |"),
    ("| Spine (the core; no bridge since the F3 sweep) | 11,330 theorems |",
     f"| Spine (the core; no bridge since the F3 sweep) | {f(T_CORE)} theorems |"),
    ("| Audited spine declarations | 15,621 |", f"| Audited spine declarations | {f(DECL)} |"),
    ("| Modules in the compile order | 282 |", f"| Modules in the compile order | {len(r['compile_order'])} |"),
    (OLD_RUN, f"That run reused {f(REUSED)} cached Lean steps from `~/.cache/becoming-lean` and ran {f(RAN)}."),
]
ZH = [
    (f"在 R32 树（2026-10-20）上的[定理层面的连通度量]({C11})中，脊柱 11,330 条定理里有 473 条与两个基底族都散立，其中 342 个根各有说明的理由；"
     "自 R32 起度量不把具名的一行重述算作连接，并把只经由本模块之律到达基底的 172 条陈述另行报告；",
     f"在 R33 树（2026-10-20）上的[定理层面的连通度量]({C11})中，脊柱 {f(SPINE)} 条定理里有 {APART} 条与两个基底族都散立，其中 {ROOTS} "
     f"个根各有说明的理由；自 R32 起度量不把具名的一行重述算作连接，并把只经由本模块之律到达基底的 {G3} 条陈述另行报告；"),
    ("在 R32 树上的定理层面连通度量中，世界一族到达过程一族", "在 R33 树上的定理层面连通度量中，世界一族到达过程一族"),
    ("850 条陈述同时用到两族，脊柱的 11,330 条定理中 473 条与两族都散立。",
     f"{BOTH} 条陈述同时用到两族，脊柱的 {f(SPINE)} 条定理中 {APART} 条与两族都散立。"),
    ("共 19 个；其余 256 个为 L1。", f"共 {L2} 个；其余 {L1} 个为 L1。"),
    ("下表的层与定理数随 R32 更新；", "下表的层与定理数随 R33 更新；"),
    (re.compile(r"的\[当前回执 `20261019T231053\.882924Z`\]\([^)]*\)（Lean 4\.29\.1，main ad2efa757 加 R32：.*?\[研究 §223\]\([^)]*\)）："
                r"核心 279 个模块（含根模块 `Becoming`），11,330 项定理；连同三个基础模块，核心闭包 282 个模块、11,404 项定理；审计的脊柱声明 15,621 项", re.S),
     f"的[当前回执 `{RID}`]({LINK}becoming-checks/{RID}/verification.json)（Lean 4.29.1，main {MAIN} 加 R33：{WHAT_ZH}；"
     f"每个保留的声明类型不变，三个以 R33 改名表的名称，[研究 §224]({STUDY})）：核心 {len(core)} 个模块（含根模块 `Becoming`），{f(T_CORE)} 项定理；"
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
