#!/usr/bin/env python3
"""A1 (18 October 2026): the readings Ren took on 18 October in the records' live fields. Labels "pending Ren" become
"taken by Ren on 18 October 2026" with the decision (DELEGATED-CHOICES D1, D5, D22, D39 or D43); readings narrowed,
weakened or revised are restated as taken; "an argued judgment on the readings" leaves next_delta where the brief gave
it. Each edit must match exactly once within its field; each record changed gets one history note. A record already
carrying the note is skipped. usage (from the repository root): python3 -B apply_records.py"""
import json, sys

R = 'theories/becoming/results/records/'
NOTE = '18 October 2026, A1'
T_EN = 'taken by Ren on 18 October 2026, DELEGATED-CHOICES D43'
T_ZH = 'Ren 2026-10-18 取，DELEGATED-CHOICES D43'

# record: [(field path, old, new)]
E = {}
H = {}

E['how-a-carried-difference-grows'] = [
    (('correspondence', 'en'),
     "only through a loop, and through every loop that couples at every step (the AI's note: this sufficiency half holds "
     "because strengths are natural numbers, each positive one at least one, and the carrying law takes nothing; with "
     "strengths below one it need not hold), couplings at only some steps being open;",
     "only through a loop, and, with natural-number strengths, each positive one at least one, under the carrying law, "
     "through every loop that couples at every step (narrowed by the AI and " + T_EN + ": with real strengths below one "
     "such a loop need not run away, which is damping), couplings at only some steps being open;"),
    (('correspondence', 'zh'),
     "只经由回路，且经由每个每步耦合的回路（AI 的注：这一充分的一半成立，是因为强度为自然数、正的强度至少为一，且携带之律什么也不取；"
     "强度小于一时不必成立），只在某些步成立的耦合开放；",
     "只经由回路，且在携带之律下、强度为自然数且每个正的强度至少为一时，经由每个每步耦合的回路（AI 收窄，" + T_ZH + "：实数强度"
     "小于一时，这样的回路不必失控，即阻尼），只在某些步成立的耦合开放；"),
]
H['how-a-carried-difference-grows'] = (
    "the reading Ren took on 16 October, that only a loop makes a difference run away and through every loop that "
    "couples at every step, is narrowed as Ren took it on 18 October (DELEGATED-CHOICES D43, review item 44): the "
    "sufficiency half holds for natural-number strengths under the carrying law, and the AI's note on it becomes part of "
    "the reading. Before: \"only through a loop, and through every loop that couples at every step (the AI's note: this "
    "sufficiency half holds because strengths are natural numbers, each positive one at least one, and the carrying law "
    "takes nothing; with strengths below one it need not hold)\"",
    "Ren 10月16日所取的读法（只有回路使差别失控，且经由每个每步耦合的回路）按 Ren 10月18日所取收窄（DELEGATED-CHOICES D43，审查"
    "第 44 项）：充分的一半在携带之律下、强度为自然数时成立，AI 的注成为读法的一部分；原文见英文")

E['what-a-cut-loses'] = [
    (('correspondence', 'en'), "Readings (the AI's, pending Ren):", "Readings (the AI's, " + T_EN + "):"),
    (('correspondence', 'en'),
     "The most difference that can arrive outgrows every polynomial only through a loop of the couplings that go on; "
     "whether through every such loop is not derived.",
     "The most difference that can arrive outgrows every polynomial only through a loop of the couplings that go on, and "
     "not through every such loop, since one that recurs rarely stays polynomial (Frequency.Sparse.polynomial, "
     "how-often-couplings-act)."),
    (('correspondence', 'zh'), "读法（AI 的，待 Ren）：", "读法（AI 的，" + T_ZH + "）："),
    (('correspondence', 'zh'), "是否经由每个这样的回路不推出。",
     "不必经由每个这样的回路：稀少复现的回路保持多项式（Frequency.Sparse.polynomial，how-often-couplings-act）。"),
    (('next_delta', 'en'), "; an independent review; an argued judgment on the readings.", "; an independent review."),
    (('next_delta', 'zh'), "；独立审查；对读法的论证判断。", "；独立审查。"),
]
H['what-a-cut-loses'] = (
    "the readings taken by Ren (DELEGATED-CHOICES D43); their last clause, \"whether through every such loop is not "
    "derived\", is answered by how-often-couplings-act: not through every such loop. The judgment on the readings leaves "
    "the next step",
    "读法由 Ren 取（DELEGATED-CHOICES D43）；最后一句“是否经由每个这样的回路不推出”由 how-often-couplings-act 回答：不必经由每个"
    "这样的回路。对读法的判断移出下一步")

E['how-often-couplings-act'] = [
    (('correspondence', 'en'), "Readings (the AI's, pending Ren):", "Readings (the AI's, " + T_EN + "):"),
    (('correspondence', 'zh'), "读法（AI 的，待 Ren）：", "读法（AI 的，" + T_ZH + "）："),
    (('next_delta', 'en'), "; an independent review; a judgment on the readings.", "; an independent review."),
    (('next_delta', 'zh'), "；独立审查；对读法的判断。", "；独立审查。"),
]
H['how-often-couplings-act'] = (
    "the readings taken by Ren with the natural-number scope already in them (DELEGATED-CHOICES D43); the judgment on "
    "the readings leaves the next step",
    "读法由 Ren 取，自然数的范围已在读法之中（DELEGATED-CHOICES D43）；对读法的判断移出下一步")

E['observation-is-a-route'] = [
    (('correspondence', 'en'),
     "Readings (the AI's, pending Ren): observation is not a second relation beside dependence (the AI's note: the "
     "theorem shows only that observation does not go beyond dependence, not that it is dependence), direct observation "
     "being the route of length zero",
     "Readings (the AI's, weakened to what apart_only_downstream shows and " + T_EN + "): observing lies within the "
     "downstream: a formation's exchange responds to a difference at a stock only through a level it reads that lies "
     "downstream of the stock, direct observation being the route of length zero"),
    (('correspondence', 'en'),
     "the reading of the stock's level before the break in P124's second reading is such a route.",
     "the reading of the stock's level before the break in P124's second reading is such a route. That observation is "
     "not a second relation beside dependence goes beyond the theorem, which shows only that observation does not go "
     "beyond dependence, not that it is dependence; it is kept as a conjecture, not a reading."),
    (('correspondence', 'zh'),
     "读法（AI 的，待 Ren）：观察不是依赖之外的第二种关系（AI 的注：定理只表明观察不越出依赖，未表明观察就是依赖），直接观察是长度"
     "为零的路线",
     "读法（AI 的，减弱为 apart_only_downstream 所表明的，" + T_ZH + "）：观察在下游之内：一个形成的交换只经它所读、位于储量下游"
     "的水平回应储量上的差别，直接观察是长度为零的路线"),
    (('correspondence', 'zh'),
     "P124 第二项读法中断裂之前对储量水平的读就是这样一条路线。",
     "P124 第二项读法中断裂之前对储量水平的读就是这样一条路线。观察不是依赖之外的第二种关系，超出定理：定理只表明观察不越出依赖，"
     "未表明观察就是依赖；它作为猜想保留，不是读法。"),
    (('next_delta', 'en'), "; an independent review; an argued judgment on the readings.",
     "; the conjecture that observation is not a second relation beside dependence; an independent review."),
    (('next_delta', 'zh'), "；独立审查；对读法的论证判断。", "；观察不是依赖之外第二种关系这一猜想；独立审查。"),
]
H['observation-is-a-route'] = (
    "the reading weakened to what apart_only_downstream shows and taken by Ren (DELEGATED-CHOICES D43, review item 45): "
    "observing lies within the downstream. \"Observation is not a second relation beside dependence\", which went "
    "beyond the theorem, is kept as a conjecture and enters the next step",
    "读法减弱为 apart_only_downstream 所表明的，由 Ren 取（DELEGATED-CHOICES D43，审查第 45 项）：观察在下游之内。“观察不是依赖"
    "之外的第二种关系”超出定理，作为猜想保留，进入下一步")

E['worlds-are-runs'] = [
    (('correspondence', 'en'),
     "Readings (the AI's, pending Ren): the root is the run because every other reading is one; a run is the unfolding "
     "read step by step, what it is at each step and how it goes on, and a world is the same unfolding read as relata "
     "of one kind exchanging; the identification is exact, so the two are one reading of one unfolding, not two things "
     "joined, and the run is no ground beneath the world.",
     "Readings (the AI's, the first revised in the light of R1 and " + T_EN + "): the run is the formal root of the "
     "package, not a ground beneath the world: a run is the unfolding read step by step on a shared index of steps, "
     "what it is at each step and how it goes on, and that index is itself a reading of the relata's own courses, a "
     "choice wherever exchanges share no relatum (the-step-index-from-own-courses); the relational start is the "
     "relata's own courses, and a run is their reading with an interleaving chosen. A world is the same unfolding read "
     "as relata of one kind exchanging; the identification is exact, so the two are one reading of one unfolding, not "
     "two things joined."),
    (('correspondence', 'zh'),
     "读法（AI 的，待 Ren）：根是运行，因为其他每个读法都是运行；运行是逐步读的展开，每步是什么、怎样继续，世界是同一展开读作同类"
     "关系项的交换；同一化恰好，所以二者是一个展开的一个读法，不是两物相连，运行也不是世界之下的根基。",
     "读法（AI 的，第一项按 R1 修订，" + T_ZH + "）：运行是这一包的形式之根，不是世界之下的根基：运行是在共同的步指标上逐步读的"
     "展开，每步是什么、怎样继续，而这一指标本身是关系项自身进程的一种读法，凡交换不共有关系项处是一种选择"
     "（the-step-index-from-own-courses）；关系的起点是关系项自身的进程，运行是选定一种交错的读法。世界是同一展开读作同类关系项的"
     "交换；同一化恰好，所以二者是一个展开的一个读法，不是两物相连。"),
    (('next_delta', 'en'), "; an independent review; an argued judgment on the readings and on a definitional root.",
     "; an independent review; an argued judgment on a definitional root."),
    (('next_delta', 'zh'), "；独立审查；对读法与定义上的根的论证判断。", "；独立审查；对定义上的根的论证判断。"),
]
H['worlds-are-runs'] = (
    "the first reading revised in the light of R1 and taken by Ren (DELEGATED-CHOICES D43): the run is the formal root "
    "of the package, its index of steps a reading of the relata's own courses. Before: \"the root is the run because "
    "every other reading is one; a run is the unfolding read step by step, what it is at each step and how it goes on, "
    "and a world is the same unfolding read as relata of one kind exchanging; the identification is exact, so the two "
    "are one reading of one unfolding, not two things joined, and the run is no ground beneath the world.\"",
    "第一项读法按 R1 修订，由 Ren 取（DELEGATED-CHOICES D43）：运行是这一包的形式之根，其步指标是关系项自身进程的一种读法；"
    "原文见英文")

E['two-act-worlds-carry-the-difference'] = [
    (('correspondence', 'en'), "Readings (the AI's, pending Ren):", "Readings (the AI's, " + T_EN + "):"),
    (('correspondence', 'zh'), "读法（AI 的，待 Ren）：", "读法（AI 的，" + T_ZH + "）："),
    (('next_delta', 'en'), "; an independent review; an argued judgment on the readings.", "; an independent review."),
    (('next_delta', 'zh'), "；独立审查；对读法的论证判断。", "；独立审查。"),
]
H['two-act-worlds-carry-the-difference'] = ("the readings taken by Ren (DELEGATED-CHOICES D43)",
                                            "读法由 Ren 取（DELEGATED-CHOICES D43）")

E['the-step-index-from-own-courses'] = [
    (('correspondence', 'en'), "Reading (the AI's, pending Ren):", "Reading (the AI's, " + T_EN + "):"),
    (('correspondence', 'zh'), "读法（AI 的，待 Ren）：", "读法（AI 的，" + T_ZH + "）："),
    (('next_delta', 'en'), "; an independent review; an argued judgment on the reading.", "; an independent review."),
    (('next_delta', 'zh'), "；独立审查；对读法的论证判断。", "；独立审查。"),
]
H['the-step-index-from-own-courses'] = ("the reading taken by Ren (DELEGATED-CHOICES D43)",
                                        "读法由 Ren 取（DELEGATED-CHOICES D43）")

E['counting-where-the-counts-exist'] = [
    (('correspondence', 'en'), "counts are relations, as Becoming.Decidedness reads them,",
     "counts are relations, as Becoming.Decidedness reads them (the AI's reading, " + T_EN + "),"),
    (('correspondence', 'zh'), "计数是关系，如 Becoming.Decidedness 所读，",
     "计数是关系，如 Becoming.Decidedness 所读（AI 的读法，" + T_ZH + "），"),
]
H['counting-where-the-counts-exist'] = ("the reading that a count is a relation taken by Ren (DELEGATED-CHOICES D43)",
                                        "计数是关系这一读法由 Ren 取（DELEGATED-CHOICES D43）")

E['what-a-law-of-the-whole-and-no-part-takes'] = [
    (('correspondence', 'en'), "Readings (the AI's, pending Ren):", "Readings (the AI's, " + T_EN + "):"),
    (('correspondence', 'zh'), "读法（AI 的，待 Ren）：", "读法（AI 的，" + T_ZH + "）："),
    (('next_delta', 'en'), "; an independent review; an argued judgment on the readings.", "; an independent review."),
    (('next_delta', 'zh'), "；独立审查；对读法的论证判断。", "；独立审查。"),
]
H['what-a-law-of-the-whole-and-no-part-takes'] = (
    "the readings, as the eighteenth review narrowed them, taken by Ren (DELEGATED-CHOICES D43)",
    "读法按第十八次审查的收窄由 Ren 取（DELEGATED-CHOICES D43）")

E['where-a-run-goes-on'] = [
    (('correspondence', 'en'), "Readings (the AI's, pending Ren):", "Readings (the AI's, " + T_EN + "):"),
    (('correspondence', 'zh'), "读法（AI 的，待 Ren）：", "读法（AI 的，" + T_ZH + "）："),
    (('next_delta', 'en'), "; an independent review; an argued judgment on the readings.", "; an independent review."),
    (('next_delta', 'zh'), "；独立审查；对读法的论证判断。", "；独立审查。"),
]
H['where-a-run-goes-on'] = ("the readings taken by Ren (DELEGATED-CHOICES D43)", "读法由 Ren 取（DELEGATED-CHOICES D43）")

E['lifting-where-branching-is-finite'] = [
    (('correspondence', 'en'), "Readings (the AI's, which Ren took on 16 October 2026):",
     "Readings (the AI's, which Ren took on 16 October 2026 and confirmed on 18 October 2026, DELEGATED-CHOICES D43):"),
    (('correspondence', 'zh'), "读法（AI 的，Ren 2026-10-16 已取）：",
     "读法（AI 的，Ren 2026-10-16 已取，2026-10-18 确认，DELEGATED-CHOICES D43）："),
]
H['lifting-where-branching-is-finite'] = (
    "the readings, marked taken by Ren's 16 October \"agree with other readings\", confirmed by Ren (DELEGATED-CHOICES "
    "D43)",
    "读法曾标为由 Ren 10月16日的“agree with other readings”所取，现由 Ren 确认（DELEGATED-CHOICES D43）")

W = 'whole-first-and-bounded-centers'
E[W] = [
    (('hypotheses', 0, 'en'),
     "The axiom: Unrestricted sig, that from every standpoint",
     "The continuation condition: Unrestricted sig, that from every standpoint"),
    (('hypotheses', 0, 'en'),
     "reading it as Ren's axiom is the AI's reading, adopted on Ren's delegation.",
     "reading it as the condition Ren stated, which Ren then called an axiom, is the AI's reading, adopted on Ren's "
     "delegation."),
    (('hypotheses', 0, 'zh'), "公理：Unrestricted sig，", "延续条件：Unrestricted sig，"),
    (('hypotheses', 0, 'zh'), "把它读作 Ren 的公理是 AI 的读法，依 Ren 的交托采用。",
     "把它读作 Ren 所陈述的条件（Ren 当时称之为公理）是 AI 的读法，依 Ren 的交托采用。"),
    (('validation_scope', 'en'), "no Lean axiom is used, the axiom Unrestricted being a hypothesis of the theorems.",
     "no Lean axiom is used, the continuation condition Unrestricted being a hypothesis of the theorems."),
    (('validation_scope', 'zh'), "不用 Lean 公理，公理 Unrestricted 是定理的假设。",
     "不用 Lean 公理，延续条件 Unrestricted 是定理的假设。"),
    (('correspondence', 'en'), "Ren's axiom is “for anything,",
     "Ren's statement of the continuation condition, which Ren then called an axiom, is “for anything,"),
    (('correspondence', 'zh'), "Ren 的公理是“for anything,", "Ren 对延续条件的表述（Ren 当时称之为公理）是“for anything,"),
    (('correspondence', 'en'), "The author's reading (an AI argument, adopted on Ren's delegation): Retains.within",
     "The author's reading (an AI argument, adopted on Ren's delegation and " + T_EN + "): Retains.within"),
    (('correspondence', 'zh'), "作者的读法（AI 论证，依 Ren 的交托采用）：Retains.within",
     "作者的读法（AI 论证，依 Ren 的交托采用，" + T_ZH + "）：Retains.within"),
    (('dependencies', 0, 'interface', 'input', 'en'), "under the axiom the dweller is lost from every standpoint.",
     "under the continuation condition the dweller is lost from every standpoint."),
    (('dependencies', 0, 'interface', 'input', 'zh'), "公理之下从每个立场失去栖居者。", "延续条件之下从每个立场失去栖居者。"),
    (('dependencies', 2, 'detail', 'en'), "Reuses the axiom Unrestricted", "Reuses the continuation condition Unrestricted"),
    (('dependencies', 2, 'detail', 'zh'), "复用公理 Unrestricted", "复用延续条件 Unrestricted"),
    (('dependencies', 2, 'interface', 'output', 'en'), "The axiom and its rival.", "The continuation condition and its rival."),
    (('dependencies', 2, 'interface', 'output', 'zh'), "公理与它的对手。", "延续条件与它的对手。"),
    (('dependencies', 3, 'detail', 'en'), "and under the axiom they do not disagree.",
     "and under the continuation condition they do not disagree."),
    (('dependencies', 3, 'detail', 'zh'), "公理之下不分歧。", "延续条件之下不分歧。"),
    (('dependencies', 3, 'interface', 'input', 'en'), "supplied as the axiom is.",
     "supplied as the continuation condition is."),
    (('dependencies', 3, 'interface', 'input', 'zh'), "与公理一样被给出。", "与延续条件一样被给出。"),
    (('dependencies', 3, 'interface', 'conditions', 'en'), "The reading pending Ren.",
     "The reading " + T_EN + "."),
    (('dependencies', 3, 'interface', 'conditions', 'zh'), "读法待 Ren。", "读法由 " + T_ZH + "。"),
    (('related', 2, 'detail', 'en'),
     "Without the axiom, the verdict bounded by the feeding closure is the axiom's where the closure is the whole;",
     "Without the continuation condition, the verdict bounded by the feeding closure is the condition's where the "
     "closure is the whole;"),
    (('related', 2, 'detail', 'zh'), "不用公理时，以供给闭包为界的判断在闭包是整体时就是公理的判断；",
     "不用延续条件时，以供给闭包为界的判断在闭包是整体时就是延续条件的判断；"),
]
H[W] = (
    "the reading of Ren's order of levels taken by Ren (DELEGATED-CHOICES D43), and the live fields name the "
    "continuation condition where they said \"the axiom\", a label retired since P128; Ren's quoted words, which say "
    "\"axiom\", are unchanged",
    "Ren 的层级次序的读法由 Ren 取（DELEGATED-CHOICES D43）；活字段中原称“公理”之处改称延续条件（P128 以来“公理”已退役）；所引 "
    "Ren 原话中的“axiom”不变")

E['unity-of-readings'] = [
    (('correspondence', 'en'), "the self “can not justify itself”.",
     "the self “can not justify itself”. That last reading is an analogy only (" + T_EN + ", review finding D-e): "
     "Novelty's quantification over every family is not BoundaryInvariant, so it gives no support to the step of "
     "invariance, whose warrant stays open."),
    (('correspondence', 'zh'), "没有它自身“can not justify itself”。",
     "没有它自身“can not justify itself”。最后这一读法只是类比（" + T_ZH + "，审查所见 D-e）：Novelty 对每个家族的量化不是 "
     "BoundaryInvariant，所以不支持不变之步，其根据仍开放。"),
]
H['unity-of-readings'] = (
    "the reading \"under the invariance the laws meet\" kept as an analogy only, as Ren took it (DELEGATED-CHOICES D43, "
    "review finding D-e)",
    "“在规律所满足的不变之下”这一读法只作为类比保留，由 Ren 取（DELEGATED-CHOICES D43，审查所见 D-e）")

E['how-much-difference-arrives'] = [
    (('correspondence', 'en'),
     "in Ren's “highly entangled system”, entanglement reads as how strongly exchanges are coupled to each other's "
     "levels, not as quantum entanglement.",
     "in Ren's sentence, “heavily coupled into it” reads as coupling strength and “a highly entangled system” as "
     "couplings that lie on loops through the whole, how highly being the strengths along the loops and how often they "
     "act, not as quantum entanglement (revised and taken by Ren on 18 October 2026, DELEGATED-CHOICES D39)."),
    (('correspondence', 'zh'),
     "Ren 的“highly entangled system”中，纠缠读作交换与彼此水平耦合的强度，不等同于量子的纠缠。",
     "Ren 的句子中，“heavily coupled into it”读作耦合强度，“a highly entangled system”读作耦合位于贯穿整体的回路上，多“highly”"
     "是回路上的强度与其作用的频度，不等同于量子的纠缠（经修订由 Ren 2026-10-18 取，DELEGATED-CHOICES D39）。"),
]
H['how-much-difference-arrives'] = (
    "the reading of \"entangled\" revised as Ren took it (DELEGATED-CHOICES D39): strength for \"heavily coupled into "
    "it\", loops for \"a highly entangled system\". Before: \"in Ren's “highly entangled system”, entanglement reads as "
    "how strongly exchanges are coupled to each other's levels, not as quantum entanglement.\"",
    "“entangled”的读法按 Ren 所取修订（DELEGATED-CHOICES D39）：“heavily coupled into it”读作强度，“a highly entangled "
    "system”读作回路；原文见英文")

E['comparison-by-widening'] = [
    (('correspondence', 'en'), "the generative space is where a part widens what can form.",
     "what can form now is the generative space, and where a part widens it is the region Ren's sentence names (D22, "
     "revised and taken by Ren on 18 October 2026)."),
    (('correspondence', 'en'),
     "plurality an aspect not yet measured, and widening is the space of 生生 (D22).",
     "plurality an aspect not yet measured; widening compares the direction of 生生, which is generation generating "
     "generation (D1 and D22, revised and taken by Ren on 18 October 2026)."),
    (('correspondence', 'zh'), "生成的空间读作部分在其中扩大能形成者之处。",
     "当下能形成者是生成的空间，部分在其中扩大它之处是 Ren 那句话所说的区域（D22，经修订由 Ren 2026-10-18 取）。"),
    (('correspondence', 'zh'), "多样性是尚未度量的一面，扩大就是生生的空间（D22）。",
     "多样性是尚未度量的一面；扩大比较生生的方向，生生是生成者生成新的生成（D1 与 D22，经修订由 Ren 2026-10-18 取）。"),
]
H['comparison-by-widening'] = (
    "the readings of the generative space and of 生生 revised as Ren took them (DELEGATED-CHOICES D1, D22): what can "
    "form now is the generative space, and widening compares the direction of 生生. Before: \"the generative space is "
    "where a part widens what can form\" and \"widening is the space of 生生 (D22)\"",
    "生成的空间与生生的读法按 Ren 所取修订（DELEGATED-CHOICES D1、D22）：当下能形成者是生成的空间，扩大比较生生的方向；原文见英文")

E['identity-across-steps'] = [
    (('correspondence', 'en'),
     "On Ren's delegation 生生不息 is read at the level of the whole, as arising that recurs through renewal, lineages "
     "and members being levels within it at which continuation is read (DELEGATED-CHOICES D5);",
     "On Ren's delegation 生生不息 is read at the level of the whole, lineages and members being levels within it at "
     "which continuation is read: 不息 as arising that recurs through renewal, and 生生不息 as 生生 going on with more "
     "still able to form, so return falls short (DELEGATED-CHOICES D5, revised and taken by Ren on 18 October 2026);"),
    (('correspondence', 'zh'),
     "依 Ren 的交托，“生生不息”读在整体的层次，即经更新而复现的生起，谱系与成员是其中读延续的层次（DELEGATED-CHOICES D5）；",
     "依 Ren 的交托，“生生不息”读在整体的层次，谱系与成员是其中读延续的层次：不息是经更新而复现的生起，生生不息是生生继续而仍有"
     "更多能形成，回返不足以是生生不息（DELEGATED-CHOICES D5，经修订由 Ren 2026-10-18 取）；"),
]
H['identity-across-steps'] = (
    "the reading of 生生不息 revised as Ren took it (DELEGATED-CHOICES D5): 不息 is arising that recurs through renewal, "
    "and 生生不息 needs more still able to form, so return falls short. Before: \"as arising that recurs through renewal\"",
    "生生不息的读法按 Ren 所取修订（DELEGATED-CHOICES D5）：不息是经更新而复现的生起，生生不息需要仍有更多能形成，回返不足以是"
    "生生不息；原文见英文")

E['ranking-under-readings'] = [
    (('correspondence', 'en'), "On Ren's delegation 生生 reads as the generative space (DELEGATED-CHOICES D1).",
     "生生 reads as generation generating generation, its direction compared by widening what can form "
     "(DELEGATED-CHOICES D1, revised and taken by Ren on 18 October 2026)."),
    (('correspondence', 'zh'), "依 Ren 的交托，生生读作生成的空间（DELEGATED-CHOICES D1）。",
     "生生读作生成者生成新的生成，其方向以能形成者的扩大比较（DELEGATED-CHOICES D1，经修订由 Ren 2026-10-18 取）。"),
]
H['ranking-under-readings'] = (
    "the reading of 生生 revised as Ren took it (DELEGATED-CHOICES D1). Before: \"On Ren's delegation 生生 reads as the "
    "generative space\"",
    "生生的读法按 Ren 所取修订（DELEGATED-CHOICES D1）；原文见英文")

E['becoming-stepwise-reading'] = [
    (('correspondence', 'en'),
     "on Ren's delegation 生生 is read as the generative space, and comparison uses no reading of living (integration "
     "note §8.5; DELEGATED-CHOICES D1).",
     "生生 is read as generation generating generation, its direction compared by widening what can form, and comparison "
     "uses no reading of living (integration note §8.5; DELEGATED-CHOICES D1, revised and taken by Ren on 18 October "
     "2026)."),
    (('correspondence', 'zh'),
     "依 Ren 的交托，生生读作生成的空间，比较不用 living 的读法（整合文档 §8.5；DELEGATED-CHOICES D1）。",
     "生生读作生成者生成新的生成，其方向以能形成者的扩大比较，比较不用 living 的读法（整合文档 §8.5；DELEGATED-CHOICES D1，经修订"
     "由 Ren 2026-10-18 取）。"),
]
H['becoming-stepwise-reading'] = (
    "the reading of 生生 revised as Ren took it (DELEGATED-CHOICES D1); the review counterexample that records the "
    "earlier reading is kept as it was. Before: \"on Ren's delegation 生生 is read as the generative space\"",
    "生生的读法按 Ren 所取修订（DELEGATED-CHOICES D1）；记录早先读法的审查反例保持原样；原文见英文")

E['where-novelty-gain-comes-from'] = [
    (('correspondence', 'en'),
     "生生不息 reads at the level of the whole, where in a bounded whole with the rest idle it is return, not endless "
     "novelty;",
     "生生不息 reads at the level of the whole: 不息 as arising that recurs through renewal, which in a bounded whole with "
     "the rest idle is return, and 生生不息 as 生生 going on with more still able to form, which return falls short of "
     "and which under the first law needs inflow from beyond every bounded part (D5, revised and taken by Ren on 18 "
     "October 2026);"),
    (('correspondence', 'zh'),
     "生生不息读在整体的层次，在其余闲置的有界整体中它是回返，不是无尽的新；",
     "生生不息读在整体的层次：不息是经更新而复现的生起，在其余闲置的有界整体中是回返；生生不息是生生继续而仍有更多能形成，回返不足"
     "以是它，在第一定律下它需要来自每个有界部分之外的流入（D5，经修订由 Ren 2026-10-18 取）；"),
]
H['where-novelty-gain-comes-from'] = (
    "the reading of 生生不息 revised as Ren took it (DELEGATED-CHOICES D5). Before: \"生生不息 reads at the level of the "
    "whole, where in a bounded whole with the rest idle it is return, not endless novelty\"",
    "生生不息的读法按 Ren 所取修订（DELEGATED-CHOICES D5）；原文见英文")


def get(d, path):
    for k in path[:-1]:
        d = d[k]
    return d, path[-1]


def main():
    for rid, edits in E.items():
        f = R + rid + '.json'
        d = json.load(open(f, encoding='utf-8'))
        if any(h.get('en', '').startswith(NOTE + ' (Ren') for h in d.get('history', [])):
            print('already edited', rid)
            continue
        for path, old, new in edits:
            parent, key = get(d, path)
            n = parent[key].count(old)
            if n != 1:
                sys.exit(f'{rid} {path}: expected one match, found {n}: {old[:90]!r}')
            parent[key] = parent[key].replace(old, new)
        en, zh = H[rid]
        d['history'].append({
            'en': f"{NOTE} (Ren 18 October: {ANSWER_EN}): {en}. The claim is unchanged.",
            'zh': f"2026年10月18日，A1（Ren 10月18日的回答）：{zh}。论断不变。"})
        open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        print('edited', rid, len(edits))


ANSWER_EN = ('"I take the revised readings of 生生, 生生不息 and \\"entangled\\". Record my answer in sources, then apply '
             'them with Part B\'s recommendations, coordinating with N6."')

if __name__ == '__main__':
    main()
