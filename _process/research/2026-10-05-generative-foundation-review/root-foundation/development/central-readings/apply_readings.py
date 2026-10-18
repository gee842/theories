#!/usr/bin/env python3
"""A1 (18 October 2026): apply Ren's answer, "I take the revised readings of 生生, 生生不息 and "entangled". Record my
answer in sources, then apply them with Part B's recommendations, coordinating with N6.", to DELEGATED-CHOICES (English
and Chinese editions) and to the chapter (English and Chinese editions). D1, D5, D22 and D39 get dated revisions below
their original text; D43 records the readings of the brief's Part B. Every edit must match exactly once; a file already
edited is skipped. The board is edited by apply_board.py at landing, over whatever the board then holds.
usage (from the repository root): python3 -B apply_readings.py"""
import sys

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
CH = 'theories/becoming/chapters/'
REC = '../../../../theories/becoming/results/records/'
SRC = '../../../../sources/15-codex-theory-conversations/'
WORDS = SRC + '2026-10-18-central-readings-taken.md'
TREATISE = '../../../../sources/06-zhishan/shengsheng/生生不息论v1/生生不息论.md'
BRIEF = 'READINGS-PENDING-REN.md'
STUDY = 'BECOMING-RENEWAL-READING.md'
CREC = '../results/records/'
CWORDS = '../../../sources/15-codex-theory-conversations/2026-10-18-central-readings-taken.md'
CBRIEF = '../../../' + RF + BRIEF
ANSWER = ("“I take the revised readings of 生生, 生生不息 and \"entangled\". Record my answer in sources, then apply them "
          "with Part B's recommendations, coordinating with N6.”")
SEC7 = '\n\n<a id="7-从关系开始的重建--the-relation-first-re-founding"></a>'

EDITS, MARK = {}, {}

# ------------------------------------------------------------------------------------------- DELEGATED-CHOICES.md
EN = RF + 'DELEGATED-CHOICES.md'
MARK[EN] = '**Revision, taken by Ren (18 October 2026).**'

D1_EN = (
    "\n\n**Revision, taken by Ren (18 October 2026).** 生生 is read as generation generating generation: what forms "
    "preserves, restores, transmits or creates the conditions and generators of further forming, so a course changes "
    "what can form, and the capacity to form, along with the state. This is the definition in Ren's treatise 生生不息论 "
    "v1, under its heading “生生：生成者生成新的生成”: “这一次生成的结果，又保存、恢复、传递或创造了下一轮生成的条件与生成者。"
    "普通生成改变接下来的状态；生生还改变接下来能够形成哪些状态，以及世界能否继续发现新的形成方式” ([text](" + TREATISE + ")); "
    "Ren said the same on 10 October 2026: “it is about if the continuation of becoming continues itself”. The core "
    "states this structure in laws, not in one predicate: with nothing given from beyond, what can form is opened only "
    "by what the supported give (D35); where arising depletes finitely many conditions, unceasing generation needs "
    "renewal made within the unfolding (`Web.Unceasing.regeneration_recurs`); a whole whose parts pass persists only "
    "through the generation of its parts ([whole-persists-through-generation](" + REC + "whole-persists-through-generation.md)); "
    "a renewing formation does not consume (`Web.renewing_not_consuming`). The generative space is what can form now "
    "(the treatise: “在当下，生显为尚可成为的可能性空间”; D22). The direction of 生生, “more 生” and “more future, not "
    "less”, is compared by widening what can form (`Web.Widens`), with the four cases of D2; the treatise's "
    "“生生维护的不是选项数量” agrees, since widening is inclusion, not a count of options. The rest of the decision stands: "
    "the three scopes as scopes of what is counted, courses compared on possibilities, and 生生 as the object of the "
    "ethical direction rather than any new organization. The Lean predicate `living` does not read 生生: its readings "
    "do not include further generation. **What changed.** The decision above read 生生 as the generative space, the "
    "widening of what can form. A space and the widening of a space are different things, and widening compares, "
    "between two level paths, only one component of the treatise's (state, 可成为之域, 生成能力). Renewal capacity and "
    "richness of relations (Ren, 10 October 2026) stay measures not yet read (chapter §8.2). **What would change it.** "
    "Ren saying that 生生 names only the direction (then 生生 is the widening, and the generative space what is widened); "
    "a case that renews the conditions and generators of its own further forming which Ren judges not 生生; adopting "
    "renewal capacity or richness of relations as the measure of “more”, a premise beyond widening, since it orders "
    "mixed parts. The arguments are in the [decision brief](" + BRIEF + "#a1-生生-d1-and-the-generative-space-d22); Ren's "
    "answer ([words](" + WORDS + ")) is its provenance, not its warrant. The original text above is kept.")

D5_EN = (
    "\n\n**Revision, taken by Ren (18 October 2026).** 不息 keeps the reading above: arising recurs through renewal, so "
    "the source of generation does not dry up. This is the treatise's 不息, “不是永不消亡，而是不使生成之源枯竭”, and its "
    "不绝其源, with its five tests of true 不息 as necessary conditions ([text](" + TREATISE + ")). 生生不息 is read as "
    "生生 (D1) going on at the whole with more still able to form: not a return into copies of existing forms, which "
    "the treatise excludes (“不是现有形式的无限复制”). Complexity can keep rising, as Ren's answer of 7 October 2026 "
    "says (“复杂性/复杂结构的复杂度可以不断的上升”), though nothing requires it to rise; the treatise's true 不息 “不是数量的"
    "无限增加”, and Ren's “we can't compounding forever”, exclude reading it as growth. A whole that only returns has "
    "不息 but not 生生不息. A closed cycle whose total stays one, in which arising never ceases, is such a whole "
    "(`Recycle.closed_unceasing`); under the first law a finite whole whose rest gives nothing net stays within its "
    "stock (`Flow.whole_bounded_of_rest_idle`) and, with natural-number amounts, keeps revisiting configurations it "
    "has had (`Flow.whole_recurs_of_rest_idle`). P111 says what more needs, without redefining it: under the first "
    "law a family new at every step is given more than it takes, from the rest or across its boundary, at arbitrarily "
    "late steps, and so is every bounded family containing it (`Flow.new_beyond_every`): inflow from beyond, not "
    "growth. So a part fed from beyond, as the Earth is by the sun, can have 生生不息 while the inflow lasts; the whole "
    "can have it only if it is not a finite whole under the first law, and whether the actual whole is such a whole is "
    "empirical correspondence (chapter §8.7), not a reading. Scope: return is forced here by natural-number amounts, a "
    "commitment of the representation; with real amounts a bounded whole need not revisit a configuration exactly, and "
    "what replaces return there is open (chapter §8.5, the scope of representation). Succession and the level of the "
    "whole stand as decided above. **What changed.** The decision above counted return as 生生不息. **What would change "
    "it.** Ren counting return as 生生不息 (the decision above then stands); Ren requiring novelty at every step rather "
    "than more still able to form (the same theorem gives what that needs); reading 不塞其流 alone as the criterion, "
    "under which a closed cycle, whose flow is not blocked, would count. The arguments are in the [decision brief](" +
    BRIEF + "#a2-生生不息-d5); Ren's answer ([words](" + WORDS + ")) is its provenance, not its warrant. The original "
    "text above is kept.")

D22_EN = (
    "\n\n**Revision, taken by Ren (18 October 2026).** Kept, and folded into D1's revision with the types exact: the "
    "generative space is what can form now (the treatise: “在当下，生显为尚可成为的可能性空间”), and its widening reads "
    "“leads to more futures(flourishes/plurality)”. Ren's sentence of 11 October, ending “these are space where "
    "generatively happens”, names the region where something's continuation widens that space (chapter §6.13). "
    "Plurality stays an aspect not yet measured (D15). What changed: the space is no longer called 生生 itself; 生生 is "
    "the generation that generates generation (D1). The original text above is kept.")

D39_EN = (
    "\n\n**Revision, taken by Ren (18 October 2026).** (4) is revised. Ren's sentence has two clauses, and they are read "
    "by two structures already in the core. “Heavily coupled into it” is coupling strength, as in (1). “A highly "
    "entangled system” says that the couplings lie on loops through the whole, so that what an act's difference does "
    "comes back around and no finite order of responses fixes it: with every condition listed, where no loop lies "
    "upstream of a condition a finite order is exact there (`carriedWithin_exact_of_no_loop`), and where a loop that is "
    "fed, its couplings holding at every step, lies upstream, every order leaves something out "
    "(`carriedWithin_lt_of_loop`), both in `Becoming.Loops`. “Highly” is then the strengths along the loops and how "
    "often they act; whether a difference runs away depends on both, and a loop of recurring couplings need not run "
    "away (`Frequency.Sparse.polynomial`, P123). A chain of strong couplings with no loop is heavily coupled and not "
    "entangled. Identification with quantum entanglement stays declined: what the two share, that the whole does not "
    "separate into parts computed apart, is an analogy. (3) stands with the scope of the correction above: under a law "
    "that takes nothing, and so creates amounts, a held difference keeps arriving; under the first law it is not "
    "shown, and in a finite whole whose rest gives nothing net the levels stay within the stock "
    "(`Flow.whole_bounded_of_rest_idle`), so unbounded arrival needs amounts brought in from beyond, or created: the "
    "theory's form of Ren's “we can't compounding forever”. (1) and (2) stand. **What changed.** (4) above read "
    "“entangled” by strength alone, and (3) now has its scope. **What would change it.** Ren reading “a highly "
    "entangled system” as strength alone; a whole with tangled couplings that Ren judges not entangled. The arguments "
    "are in the [decision brief](" + BRIEF + "#a3-entangled-d39-4-and-the-scope-of-d39-3); Ren's answer ([words](" +
    WORDS + ")) is its provenance, not its warrant. The original text above is kept.")

D43_EN = (
    "\n\n<a id=\"d43-其余的待决读法--the-other-pending-readings\"></a>\n"
    "### The other pending readings, taken on 18 October 2026\n\n"
    "**Decision.** Taken by Ren on 18 October 2026 with Part B of the [decision brief](" + BRIEF +
    "#b-the-other-pending-readings), whose arguments they rest on; Ren's answer ([words](" + WORDS + ")) is their "
    "provenance, not their warrant. Each changes no theorem and adds no premise; the chapter labels them [AI reading, "
    "D43].\n"
    "- **The step index** (R1, [the-step-index-from-own-courses](" + REC + "the-step-index-from-own-courses.md)): "
    "kept. The shared index of steps is a reading of the relations, not their ground: two interleavings giving each "
    "relatum the same course reach the same configuration, so the index adds only an order no configuration reads. "
    "The likeness to the lack of a fact of order between events that cannot affect each other is an analogy only.\n"
    "- **Counted censuses** (R2 and R2b, [counting-where-the-counts-exist](" + REC +
    "counting-where-the-counts-exist.md)): kept. A count is a relation; the global decision is a condition only of "
    "`World.lpo_of_finite_ends`, whose subject it is.\n"
    "- **Only a loop makes a difference run away** (P118, the reading Ren took on 16 October; review item 44): narrowed. "
    "The necessity holds generally: where no loop lies upstream, a finite order is exact. The sufficiency, through "
    "every loop that couples at every step, holds for natural-number strengths, each positive one at least one, under "
    "the carrying law; with real strengths below one such a loop need not run away. That is damping, common in actual "
    "systems.\n"
    "- **What a cut loses** (P120, [what-a-cut-loses](" + REC + "what-a-cut-loses.md)): kept; its last clause is "
    "answered by P123: not through every loop of the couplings that go on, since one that recurs rarely stays "
    "polynomial (`Frequency.Sparse.polynomial`).\n"
    "- **How often couplings act** (P123, [how-often-couplings-act](" + REC + "how-often-couplings-act.md)): kept, "
    "with the natural-number scope in the reading itself: with strengths below one, frequent returns need not run "
    "away. The real-amount case, a spectral radius, is an open proof.\n"
    "- **Observation** (P125, [observation-is-a-route](" + REC + "observation-is-a-route.md); review item 45): weakened "
    "to what `apart_only_downstream` shows: observing lies within the downstream; a formation's exchange responds to "
    "a difference at a stock only through a level it reads that lies downstream of the stock. That observation is no "
    "second relation beside dependence goes beyond the theorem; it is kept as a conjecture, not a reading.\n"
    "- **The tail** (P126, [what-a-law-of-the-whole-and-no-part-takes](" + REC +
    "what-a-law-of-the-whole-and-no-part-takes.md)): kept as the review narrowed it: “a whole of this kind” takes only "
    "the weak rule, and “a related whole” the rule of the limited principle.\n"
    "- **Where a run goes on** (P127, [where-a-run-goes-on](" + REC + "where-a-run-goes-on.md)): kept: König's lemma in "
    "the finite case and dependent choice in general, both exact.\n"
    "- **Worlds are runs** (P130, first reading, [worlds-are-runs](" + REC + "worlds-are-runs.md)): revised in the "
    "light of R1. The run is the formal root of the package, not a ground beneath the world: a run is read step by "
    "step on a shared index of steps, and that index is itself a reading of the relata's own courses, a choice "
    "wherever exchanges share no relatum. The relational start is the relata's own courses, and a run is their reading "
    "with an interleaving chosen. “What a world adds to its run is nothing” stays.\n"
    "- **Two acts' worlds** (P130, second reading, [two-act-worlds-carry-the-difference](" + REC +
    "two-act-worlds-carry-the-difference.md)): kept: the counterfactual is the course the same law generates (P80), "
    "not a second reality.\n"
    "- **The joins** (U and U2, [study section 166](" + STUDY + "#166-every-spine-theorem-on-the-base-u) and [167](" +
    STUDY + "#167-the-unification-follow-through-u2)): their readings and the apart-by-design classification are kept; "
    "the checker requires a category and a reason for every apart root. The two trace laws flagged as possibly vacuous "
    "(`ProbeRunsInherited.empty_candidates_trace_fails` and the slow-query half of `slow_trace_misses_deadline`) are a "
    "check to do, not a reading: each needs a witness that it is not vacuous, or a label.\n"
    "- **Lifting where branching is finite** (I4b-4, [lifting-where-branching-is-finite](" + REC +
    "lifting-where-branching-is-finite.md)): kept as taken on 16 October, now confirmed.\n"
    "- **The whole first** ([whole-first-and-bounded-centers](" + REC + "whole-first-and-bounded-centers.md)): kept, "
    "as an order of how complete a judgment is, not as what life does (Ren: “not saying this is what life does”); the "
    "record now names the continuation condition, not “the axiom”, retired since P128.\n"
    "- **“The situation makes it true”** (review item 46): where it is cited, its formal part, the determination of the "
    "law whose moves are situations, holds by construction, since the situation names the configuration it leads to; "
    "the content is the count (`Situations.sum_finer`).\n"
    "- **Novelty and invariance** (review item 49, finding D-e): the P107 reading in [unity-of-readings](" + REC +
    "unity-of-readings.md) is kept only as an analogy: `Novelty`'s quantification over every family is not "
    "`BoundaryInvariant`, so it gives no support to the step of invariance, whose warrant stays open (chapter §8.5).\n"
    "- **The generativity chain** (review item 51): Ren took the proposal to add `Selection` (selection works through "
    "the selector's model), `Observation` (observing lies within the downstream) and `Parting` (where runs part, "
    "neither the record nor the law fixes the way) to its learning and wisdom links, each with its exact scope. The "
    "chain is Ren's curated argument, so the change goes through its [maintenance record]"
    "(GENERATIVITY-CHAIN-INDEX-RECORD.md).\n\n"
    "L1, S1 and S2 are D40-D42.\n"
    "**Reasons.** The brief's, item by item: a kept reading restates its theorems; a narrowed or weakened one is cut "
    "to what its theorem shows; P130's first reading is revised because R1 shows that the step index it relied on is "
    "itself a reading.\n"
    "**What would change it.** For each item, a theorem the reading misstates, or a better argument; for P125, a proof "
    "that observation is no second relation beside dependence; for P118 and P123, the real-amount case.\n"
    "**Not covered by Ren's answer**, and still his: whether his 16 October “agree with other readings” ratifies the "
    "register as a whole (review item 50, finding D-f; the brief's [Part C](" + BRIEF +
    "#c-the-register-itself-d-f-review-item-50) recommends no blanket ratification), and the items waiting on him "
    "that are not readings ([Part D](" + BRIEF + "#d-waiting-on-ren-not-readings)).")

EDITS[EN] = [
    ("D40-D42 are decided on Ren's words of 18 October 2026 (section 12).",
     "D40-D42 are decided on Ren's words of 18 October 2026 (section 12). D1, D5, D22 and D39 were revised and taken by "
     "Ren on 18 October 2026, and D43 records the other readings he took that day; each revision is dated below its "
     "decision, whose original text is kept."),
    ("\n*Index.**\n", "\n**Index.**\n"),
    ("| D1 | how 生生 is read | the generative space, widening what can form; the three scopes as scopes of what is "
     "counted |",
     "| D1 | how 生生 is read | revised and taken by Ren (18 October): generation generating generation; the generative "
     "space is what can form now, and widening compares the direction; the three scopes as scopes of what is counted |"),
    ("| D5 | succession, level of 生生不息 | through formed relations; the whole, unceasing as renewal recurring |",
     "| D5 | succession, level of 生生不息 | through formed relations; the whole; revised and taken by Ren (18 October): "
     "不息 as renewal recurring, 生生不息 with more still able to form, so return falls short |"),
    ("| D22 | the generative space | reads Ren's two sentences, the space of 生生 |",
     "| D22 | the generative space | reads Ren's two sentences; kept and taken by Ren (18 October), folded into D1: what "
     "can form now |"),
    ("| D39 | coupling strength and entanglement | adopted with exact scope, 识 itself Ren's; entanglement as the "
     "strength of coupling, not quantum entanglement |",
     "| D39 | coupling strength and entanglement | adopted with exact scope, 识 itself Ren's; revised and taken by Ren "
     "(18 October): strength for “heavily coupled into it”, loops for “a highly entangled system”, not quantum "
     "entanglement; (3) with the review's scope |"),
    ("| D42 | when the runs of a process settle | adopted with exact scope: not changing for ever is not settling; the "
     "analogy with D34 of form only; extended with S3 |",
     "| D42 | when the runs of a process settle | adopted with exact scope: not changing for ever is not settling; the "
     "analogy with D34 of form only; extended with S3 |\n"
     "| D43 | the other pending readings (18 October) | taken by Ren on the decision brief's recommendations: kept, "
     "narrowed, weakened or revised, item by item |"),
    ("Ren adopting a measure that orders mixed parts (“more futures” is a partial order, and parts that each exceed the "
     "other stay unranked).",
     "Ren adopting a measure that orders mixed parts (“more futures” is a partial order, and parts that each exceed the "
     "other stay unranked)." + D1_EN),
    ("with succession read only at the level of members, loss is not inherited with the tenure.",
     "with succession read only at the level of members, loss is not inherited with the tenure." + D5_EN),
    ("**Reasons.** Section 6.13; D1.\n**What would change it.** As for D1.",
     "**Reasons.** Section 6.13; D1.\n**What would change it.** As for D1." + D22_EN),
    ("see O3 and fix-list item 24 of the [eighteenth review](BECOMING-EIGHTEENTH-REVIEW.md).",
     "see O3 and fix-list item 24 of the [eighteenth review](BECOMING-EIGHTEENTH-REVIEW.md)." + D39_EN),
    (SEC7, D43_EN + SEC7),
    ("and as delegating their wording and scope: D40-D42.",
     "and as delegating their wording and scope: D40-D42.\n"
     "- Ren's answer of 18 October 2026, " + ANSWER + ", sent from a reply button the AI drafted, so the wording is "
     "the AI's and the choice Ren's ([words](" + WORDS + ")): D1, D5, D22 and D39 revised, and D43. The arguments are "
     "in the [decision brief](" + BRIEF + ")."),
]

# ---------------------------------------------------------------------------------------- DELEGATED-CHOICES.zh.md
ZH = RF + 'DELEGATED-CHOICES.zh.md'
MARK[ZH] = '**修订，由 Ren 取（2026-10-18）。**'

D1_ZH = (
    "\n\n**修订，由 Ren 取（2026-10-18）。** 生生读作生成者生成新的生成（generation generating generation）：所形成者保存、"
    "恢复、传递或创造进一步形成的条件与生成者，所以一个进程连同状态一起改变能形成者与形成的能力。这是 Ren 的《生生不息论》v1 "
    "在“生生：生成者生成新的生成”标题下的定义：“这一次生成的结果，又保存、恢复、传递或创造了下一轮生成的条件与生成者。普通生成"
    "改变接下来的状态；生生还改变接下来能够形成哪些状态，以及世界能否继续发现新的形成方式”（[原文](" + TREATISE + ")）；Ren "
    "2026-10-10 也说“it is about if the continuation of becoming continues itself”。核心以规律陈述这一结构，不以单一谓词："
    "不被给予来自外部的东西时，能形成者只由被支持者所给的打开（D35）；生起消耗有限多个条件时，不息的生成需要展开之内所造成的更新"
    "（`Web.Unceasing.regeneration_recurs`）；部分会消逝的整体只经由部分的生成而持续（[whole-persists-through-generation]("
    + REC + "whole-persists-through-generation.md)）；更新的形成不是消耗的（`Web.renewing_not_consuming`）。生成的空间是当下"
    "能形成者（论中：“在当下，生显为尚可成为的可能性空间”；D22）。生生的方向，“更多的生”与“more future, not less”，以能形成者"
    "的扩大比较（`Web.Widens`），带 D2 的四种情形；论中“生生维护的不是选项数量”与此一致：扩大是包含，不是选项的计数。决定的其余"
    "部分不变：三种范围作为所计者的范围，继续之间以可能性比较，生生是伦理方向的对象，而不是任何新组织。Lean 谓词 `living` 不读出"
    "生生：它的各读法不含进一步的生成。**改变了什么。** 上面的决定把生生读作生成的空间、能形成者的扩大。空间与空间的扩大是两回事，"
    "而扩大只在两条水平路径之间比较论中（状态，可成为之域，生成能力）的一个分量。更新能力与关系的丰富（Ren 2026-10-10）仍是尚未"
    "读出的度量（理论 §8.2）。**会改变它的。** Ren 说生生只指方向（那时生生是扩大，生成的空间是被扩大者）；一个更新自身进一步"
    "形成之条件与生成者、而 Ren 判为不是生生的情形；采用更新能力或关系的丰富作为“更多”的度量，那是扩大之外的前提，因为它给混合"
    "部分定序。论证在[决定简报](" + BRIEF + "#a1-生生-d1-and-the-generative-space-d22)中；Ren 的回答（[原话](" + WORDS +
    ")）是其来源，不是其根据。上面的原文保留。")

D5_ZH = (
    "\n\n**修订，由 Ren 取（2026-10-18）。** 不息保留上面的读法：生起经更新而复现，生成之源不枯竭。这是论中的不息，“不是永不"
    "消亡，而是不使生成之源枯竭”，与其“不绝其源”，论中真正之不息的五条检验作为必要条件（[原文](" + TREATISE + ")）。生生不息"
    "读作生生（D1）在整体上继续而仍有更多能形成：不是回返为已有形式的复制，论中排除这一点（“不是现有形式的无限复制”）。复杂性可以"
    "不断上升，如 Ren 2026-10-07 的回答所说（“复杂性/复杂结构的复杂度可以不断的上升”），但没有什么要求它上升；论中说真正的不息"
    "“不是数量的无限增加”，Ren 说“we can't compounding forever”，都排除把它读作增长。只回返的整体有不息而无生生不息。总量保持"
    "为一、生起永不止息的闭合循环就是这样的整体（`Recycle.closed_unceasing`）；在第一定律下，其余不净给出的有限整体留在其存量"
    "之内（`Flow.whole_bounded_of_rest_idle`），量为自然数时它反复回到曾有的构形（`Flow.whole_recurs_of_rest_idle`）。P111 "
    "说出“更多”需要什么，而不重新定义它：在第一定律下，每步都新的家族在任意晚的步得到多于它所取的，来自其余或跨过其边界，每个包含"
    "它的有界家族亦然（`Flow.new_beyond_every`）：是来自外部的流入，不是增长。所以一个由外部供给的部分，如地球之于太阳，在流入"
    "持续时可以有生生不息；整体只在不是第一定律下的有限整体时才能有；实际的整体是否是这样的整体，是经验对应（理论 §8.7），不是"
    "读法。范围：这里的回返由自然数的量迫使，那是表示的一项承诺；量为实数时，有界整体不必确切回到某个构形，那里代替回返的是什么"
    "是开放的（理论 §8.5，表示的范围）。接续与整体的层次如上决定。**改变了什么。** 上面的决定把回返算作生生不息。**会改变它的。** "
    "Ren 把回返算作生生不息（那时上面的决定成立）；Ren 要求每步都新，而不是仍有更多能形成（同一定理给出那需要什么）；单以“不塞"
    "其流”为判据，那时流没有被阻塞的闭合循环就会算作生生不息。论证在[决定简报](" + BRIEF + "#a2-生生不息-d5)中；Ren 的回答"
    "（[原话](" + WORDS + ")）是其来源，不是其根据。上面的原文保留。")

D22_ZH = (
    "\n\n**修订，由 Ren 取（2026-10-18）。** 保留，并入 D1 的修订，类型精确：生成的空间是当下能形成者（论中：“在当下，生显为"
    "尚可成为的可能性空间”），它的扩大读出“leads to more futures(flourishes/plurality)”。Ren 2026-10-11 那句以“these are "
    "space where generatively happens”结尾的话，指某物的延续在其中扩大这一空间的区域（理论 §6.13）。多元仍是尚未度量的方面"
    "（D15）。改变了什么：这一空间不再被称为生生本身；生生是生成者生成新的生成（D1）。上面的原文保留。")

D39_ZH = (
    "\n\n**修订，由 Ren 取（2026-10-18）。** （4）修订。Ren 的这句话有两个分句，由核心中已有的两种结构读出。“heavily coupled "
    "into it”是耦合强度，如（1）。“a highly entangled system”说耦合位于贯穿整体的回路上，所以一个动作的差别所做的会绕回来，"
    "没有有限的回应阶确定它：全部条件列出时，一个条件上游没有回路处，有限阶在那里精确（`carriedWithin_exact_of_no_loop`）；"
    "上游有被供给、且耦合每步成立的回路处，每一阶都有遗漏（`carriedWithin_lt_of_loop`），二者都在 `Becoming.Loops` 中。"
    "“highly”于是是回路上的强度与它们作用的频度；差别是否失控取决于两者，复现耦合的回路不必失控（`Frequency.Sparse.polynomial`，"
    "P123）。没有回路的强耦合之链是强耦合的，而不是纠缠的。等同于量子的纠缠仍不采用：二者共有的，即整体不能分为各自计算的部分，"
    "是类比。（3）以上面更正的范围保留：在什么也不取、因而创造量的律下，所持的差别不断到达；在第一定律下未表明，而在其余不净给出"
    "的有限整体中，水平留在存量之内（`Flow.whole_bounded_of_rest_idle`），所以无界的到达需要从外部带入的量，或被创造的量：这是"
    "理论对 Ren 的“we can't compounding forever”的形式。（1）与（2）不变。**改变了什么。** 上面的（4）只以强度读“entangled”；"
    "（3）现在有其范围。**会改变它的。** Ren 把“a highly entangled system”只读作强度；一个耦合交缠而 Ren 判为不纠缠的整体。论证"
    "在[决定简报](" + BRIEF + "#a3-entangled-d39-4-and-the-scope-of-d39-3)中；Ren 的回答（[原话](" + WORDS + ")）是其来源，"
    "不是其根据。上面的原文保留。")

D43_ZH = (
    "\n\n<a id=\"d43-其余的待决读法--the-other-pending-readings\"></a>\n"
    "### D43. 其余的待决读法（2026-10-18 取）\n\n"
    "所在：理论中标为 [AI reading, D43] 的读法；下列各记录的读法。\n\n"
    "**决定。** 由 Ren 2026-10-18 依[决定简报](" + BRIEF + "#b-the-other-pending-readings)的 B 部分取，各项依其论证；Ren 的"
    "回答（[原话](" + WORDS + ")）是其来源，不是其根据。每项不改动定理，也不加前提。\n"
    "- **步的指标**（R1，[the-step-index-from-own-courses](" + REC + "the-step-index-from-own-courses.md)）：保留。共同的步"
    "指标是关系的一种读法，不是关系的根基：给每个关系项同一进程的两种交错到达同一构形，所以指标只加上一个没有构形读出的次序。"
    "与彼此不能影响的事件之间没有次序的事实相似，只是类比。\n"
    "- **计数的普查**（R2 与 R2b，[counting-where-the-counts-exist](" + REC + "counting-where-the-counts-exist.md)）：保留。"
    "计数是一种关系；全局判定只是 `World.lpo_of_finite_ends` 的条件，而那正是它的主题。\n"
    "- **只有回路使差别失控**（P118，Ren 2026-10-16 所取的读法；审查第 44 项）：收窄。必要性一般成立：上游没有回路处，有限阶"
    "精确。充分性，即经由每个每步耦合的回路，在携带之律下、强度为自然数且每个正的强度至少为一时成立；实数强度小于一时，这样的回路"
    "不必失控。那是阻尼，在实际系统中常见。\n"
    "- **截断所失**（P120，[what-a-cut-loses](" + REC + "what-a-cut-loses.md)）：保留；其最后一句由 P123 回答：不必经由持续"
    "耦合的每个回路，稀少复现的回路保持多项式（`Frequency.Sparse.polynomial`）。\n"
    "- **耦合多常作用**（P123，[how-often-couplings-act](" + REC + "how-often-couplings-act.md)）：保留，把自然数的范围写入"
    "读法本身：强度小于一时，频繁的返回不必失控。实数量的情形（谱半径）是开放的证明。\n"
    "- **观察**（P125，[observation-is-a-route](" + REC + "observation-is-a-route.md)；审查第 45 项）：减弱为 "
    "`apart_only_downstream` 所表明的：观察在下游之内；一个形成的交换只经它所读、位于储量下游的水平回应储量上的差别。观察不是"
    "依赖之外的第二种关系，超出定理；作为猜想保留，不是读法。\n"
    "- **尾**（P126，[what-a-law-of-the-whole-and-no-part-takes](" + REC + "what-a-law-of-the-whole-and-no-part-takes.md)）："
    "以审查收窄后的形式保留：“这样的整体”只需要弱的规则，“一个相关的整体”需要有限全知原则的规则。\n"
    "- **运行在何处延续**（P127，[where-a-run-goes-on](" + REC + "where-a-run-goes-on.md)）：保留：有限情形是 König 引理，"
    "一般情形是依赖选择，二者都精确。\n"
    "- **世界是运行**（P130 第一读法，[worlds-are-runs](" + REC + "worlds-are-runs.md)）：按 R1 修订。运行是这一包的形式之根，"
    "不是世界之下的根基：运行在共同的步指标上逐步读出，而这一指标本身是关系项自身进程的一种读法，凡交换不共有关系项处是一种选择。"
    "关系的起点是关系项自身的进程，运行是选定一种交错的读法。“世界加于其运行的什么也没有”保留。\n"
    "- **两个动作的世界**（P130 第二读法，[two-act-worlds-carry-the-difference](" + REC +
    "two-act-worlds-carry-the-difference.md)）：保留：反事实是同一律所生成的进程（P80），不是第二个实在。\n"
    "- **接合**（U 与 U2，[研究 §166](" + STUDY + "#166-every-spine-theorem-on-the-base-u) 与 [§167](" + STUDY +
    "#167-the-unification-follow-through-u2)）：其读法与按设计分开的分类保留；检查器要求每个分开的根有类别与理由。被标为可能"
    "空洞的两条迹之律（`ProbeRunsInherited.empty_candidates_trace_fails` 与 `slow_trace_misses_deadline` 的慢查询一半）是要做"
    "的检查，不是读法：各需一个不空洞的见证，或一个标注。\n"
    "- **有限分支处的提升**（I4b-4，[lifting-where-branching-is-finite](" + REC + "lifting-where-branching-is-finite.md)）："
    "按 2026-10-16 所取保留，现予确认。\n"
    "- **整体优先**（[whole-first-and-bounded-centers](" + REC + "whole-first-and-bounded-centers.md)）：保留，读作判断有多"
    "完整的次序，不读作生命所做的（Ren：“not saying this is what life does”）；记录现在称延续条件，不称 P128 以来已退役的“公理”。\n"
    "- **“the situation makes it true”**（审查第 46 项）：被引用时，其形式部分，即以情境为移动之律的确定性，按构造成立，因为情境"
    "命名它所通向的构形；内容是计数（`Situations.sum_finer`）。\n"
    "- **新与不变**（审查第 49 项，所见 D-e）：[unity-of-readings](" + REC + "unity-of-readings.md) 中 P107 的读法只作为类比"
    "保留：`Novelty` 对每个家族的量化不是 `BoundaryInvariant`，所以不支持不变之步，其根据仍开放（理论 §8.5）。\n"
    "- **生成链**（审查第 51 项）：Ren 取了建议：把 `Selection`（选择经选择者的模型起作用）、`Observation`（观察在下游之内）与 "
    "`Parting`（运行分开处，记录与律都不固定去路）加入其学习与智慧的链接，各带确切范围。生成链是 Ren 所编的论证，所以改动经其"
    "[维护记录](GENERATIVITY-CHAIN-INDEX-RECORD.md)。\n\n"
    "L1、S1 与 S2 是 D40-D42。\n"
    "**理由。** 简报逐项所给：保留的读法复述其定理；收窄或减弱的读法截到其定理所表明的；P130 的第一读法因 R1 表明它所依的步指标"
    "本身是读法而修订。\n"
    "**会改变它的。** 对每一项，一条读法所误述的定理，或更好的论证；对 P125，观察不是依赖之外第二种关系的证明；对 P118 与 "
    "P123，实数量的情形。\n"
    "**不在 Ren 这一回答之内**、仍属 Ren 的：他 2026-10-16 的“agree with other readings”是否批准整个登记（审查第 50 项，所见 "
    "D-f；简报的 [C 部分](" + BRIEF + "#c-the-register-itself-d-f-review-item-50)建议不作整体批准），以及等待他的、不是读法的"
    "各项（[D 部分](" + BRIEF + "#d-waiting-on-ren-not-readings)）。")

EDITS[ZH] = [
    ("D40-D42 依 Ren 2026-10-18 的话决定（§12）。",
     "D40-D42 依 Ren 2026-10-18 的话决定（§12）。D1、D5、D22 与 D39 经修订，由 Ren 2026-10-18 取；D43 记录 Ren 同日所取的"
     "其余读法；各项修订注明日期，列在原决定之下，原文保留。"),
    ("\n**索引\n", "\n**索引。**\n"),
    ("| D1 | 生生的读法 | 生成的空间：能形成者的扩大；三种范围作为所计者的范围 |",
     "| D1 | 生生的读法 | 经修订由 Ren 取（10-18）：生成者生成新的生成；生成的空间是当下能形成者，扩大比较方向；三种范围作为"
     "所计者的范围 |"),
    ("| D5 | 接续与生生不息的层次 | 经已形成的关系；整体的层次，不息即更新的复现 |",
     "| D5 | 接续与生生不息的层次 | 经已形成的关系；整体的层次；经修订由 Ren 取（10-18）：不息即更新的复现，生生不息是仍有更多"
     "能形成，回返不足以是生生不息 |"),
    ("| D22 | 生成的空间 | 读出 Ren 的两句话，是生生的空间 |",
     "| D22 | 生成的空间 | 读出 Ren 的两句话；保留并由 Ren 取（10-18），并入 D1：当下能形成者 |"),
    ("| D39 | 耦合强度与纠缠 | 以确切范围采用，识本身属 Ren；纠缠读作耦合的强度，不等同于量子的纠缠 |",
     "| D39 | 耦合强度与纠缠 | 以确切范围采用，识本身属 Ren；经修订由 Ren 取（10-18）：“heavily coupled into it”读作强度，"
     "“a highly entangled system”读作回路，不等同于量子的纠缠；（3）带审查的范围 |"),
    ("| D42 | 过程的运行何时安定 | 以确切范围采用：不永远变化不是安定；与 D34 的相似只在形式上；以 S3 扩展 |",
     "| D42 | 过程的运行何时安定 | 以确切范围采用：不永远变化不是安定；与 D34 的相似只在形式上；以 S3 扩展 |\n"
     "| D43 | 其余的待决读法（10-18） | 由 Ren 依决定简报的建议取：逐项保留、收窄、减弱或修订 |"),
    ("Ren 采用一个给混合部分定序的度量（“更多的未来”是偏序，互相超出者不排序）。",
     "Ren 采用一个给混合部分定序的度量（“更多的未来”是偏序，互相超出者不排序）。" + D1_ZH),
    ("只在成员的层次上读接续时，损失不随任期继承。",
     "只在成员的层次上读接续时，损失不随任期继承。" + D5_ZH),
    ("**理由。** §6.13；D1。\n**会改变它的。** 同 D1。",
     "**理由。** §6.13；D1。\n**会改变它的。** 同 D1。" + D22_ZH),
    ("见[第十八次审查](BECOMING-EIGHTEENTH-REVIEW.md)的 O3 与修正清单第 24 项。",
     "见[第十八次审查](BECOMING-EIGHTEENTH-REVIEW.md)的 O3 与修正清单第 24 项。" + D39_ZH),
    (SEC7, D43_ZH + SEC7),
    ("读作对 AI 所解释的读法的总体同意，并交托其措辞与范围：D40-D42。",
     "读作对 AI 所解释的读法的总体同意，并交托其措辞与范围：D40-D42。\n"
     "- Ren 2026-10-18 的回答，" + ANSWER + "，由 AI 草拟的回复按钮发出，所以措辞是 AI 的，选择是 Ren 的（[原话](" + WORDS +
     ")）：D1、D5、D22 与 D39 的修订，以及 D43。论证在[决定简报](" + BRIEF + ")中。"),
]

# ------------------------------------------------------------------------------------- THE-THEORY-OF-BECOMING.md
CE = CH + 'THE-THEORY-OF-BECOMING.md'
MARK[CE] = 'generation generating generation'
LOOPS_LT = "`carriedWithin_lt_of_loop`"

S84_NEW = (
    "**Readings not yet adopted** [AI reading, open].\n"
    "- [where-a-level-couples](" + CREC + "where-a-level-couples.md): `obs` is not a second kind of relation beside the "
    "couplings and readings; it marks where a level can couple into a formation by level, as dependence marks where "
    "it can couple by threshold.\n"
    "- Kept as a conjecture, not a reading ([observation-is-a-route](" + CREC + "observation-is-a-route.md)): "
    "observation is no second relation beside dependence. `apart_only_downstream` shows only that observing lies "
    "within the downstream, the reading taken on 18 October 2026 (D43).\n\n"
    "Ren took the other readings this list held on 18 October 2026, as D43, together with the revised D1, D5, D22 and "
    "D39 ([words](" + CWORDS + ")).\n\n"
    "**The adopted readings as a whole.** Whether the readings of §8.3 stand as a whole (item 50 of the eighteenth "
    "review's fix list, finding D-f). Ren's \"agree with other readings\" of 16 October is provenance; it does not "
    "settle them. Ren took D1, D5, D22, D39 and D43 by name on 18 October, and D40-D42 rest on his words of that day. "
    "The [decision brief](" + CBRIEF + "#c-the-register-itself-d-f-review-item-50) recommends no blanket ratification: "
    "a reading of one of Ren's phrases needs his word on that phrase, and a reading of a theorem needs only argument.\n\n"
    "**The generativity chain** (item 51 of the eighteenth review's fix list). Ren took the proposal on 18 October 2026: "
    "`Selection`, `Observation` and `Parting` enter the learning and wisdom links, each with its exact scope (D43). The "
    "chain is Ren's curated argument and changes through its maintenance record; applying the proposal there is a "
    "separate step.\n\n"
    "**Questions from the whole-repository review of 16–17 October.**\n"
    "- Whether an independent review beyond the eighteenth, an AI review that built no Lean, is needed (§8.8).\n"
    "- The join of `IdealWarrant` under a structural name.\n"
    "- Who integrates, and who owns the open whole-deduction target (W-root).\n"
    "- Whether to split the three senses of 生成: the whole (生成之论), formation, and the generative (生成的空间).\n"
    "- Whether the chapter's sentence on living significance under the condition says all the Lean shows: "
    "immediately, living significance is the condition restricted to living claims, and the condition gives "
    "significance to every claim, not a positive valence.\n\n"
    "The review's question whether 生生 may be glossed by the Lean predicate `living` is answered by D1's revision: it "
    "may not, since the `living` readings do not include further generation.\n\n")

EDITS[CE] = [
    # the label legend
    ("**[AI reading, open]** marks a reading not yet adopted. The open readings are listed in section 8.4.",
     "**[AI reading, open]** marks a reading not yet adopted. The open readings are listed in section 8.4. Ren took D1, "
     "D5, D22, D39 and D43 on 18 October 2026 (section 8.3)."),
    # the theory stated in full, item 11
    ("The readings of 生 and 生生 are AI readings (生生 read as the generative space, D1); whether they are the right "
     "readings is open to argument (section 8.4).",
     "The readings of 生 and 生生 are AI readings, which Ren took on 18 October 2026 (生生 read as generation generating "
     "generation, its direction compared by widening, D1); a better argument still revises them (section 8.3)."),
    # premise card
    ("No comparison uses it; 生生 is read as the generative space [AI reading, D1]. Whether `living` is 生生 is a "
     "philosophical argument.",
     "No comparison uses it. 生生 is read as generation generating generation, its direction compared by widening what "
     "can form [AI reading, D1]; the `living` readings do not include further generation, so they do not read 生生."),
    # succession and 生生不息
    ("is read at the level of the whole, as arising that recurs through renewal [AI reading, D5].",
     "is read at the level of the whole: 不息 as arising that recurs through renewal, and 生生不息 as 生生 going on with "
     "more still able to form, so that a whole which only returns, copying forms it has had, has 不息 but not 生生不息 "
     "[AI reading, D5]."),
    # P127
    ("*Readings* [AI reading, open]. Within finitely many configurations, whatever goes on without end does so by "
     "coming round.",
     "*Readings* [AI reading, D43]. Within finitely many configurations, whatever goes on without end does so by "
     "coming round."),
    # R1
    ("*Reading* [AI reading, open]. The shared index of steps is a reading of the relations, not their ground.",
     "*Reading* [AI reading, D43]. The shared index of steps is a reading of the relations, not their ground."),
    # R2
    ("- *Counting where the counts exist.* A count is a relation, existing exactly where what it counts is decided",
     "- *Counting where the counts exist.* A count is a relation [AI reading, D43], existing exactly where what it "
     "counts is decided"),
    # P126
    ("*Readings* [AI reading, open]. What depends on the whole and on no part of it is given exactly where it can be "
     "decided",
     "*Readings* [AI reading, D43]. What depends on the whole and on no part of it is given exactly where it can be "
     "decided"),
    ("read as whether levels never vanish, the same whole takes only the weak rule, and read as whether they vanish "
     "eventually, the rule of the limited principle.",
     "read as whether levels never vanish, a whole of this kind takes only the weak rule, and read as whether they "
     "vanish eventually, a related whole, classically its complement but in the core another law, takes the rule of "
     "the limited principle."),
    # D39 (3) in Propagation
    ("a held difference keeps arriving, since levels hold what they are given.",
     "a held difference keeps arriving, since levels hold what they are given, under a law that takes nothing and so "
     "creates amounts (the carrying law); under the first law this is not shown, and in a finite whole whose rest gives "
     "nothing net the levels stay within the stock (`Flow.whole_bounded_of_rest_idle`)."),
    # P118
    ("so the most difference that can arrive grows faster than every polynomial only through a loop, and through every "
     "loop that couples at every step, couplings that hold only at some steps being open here.",
     "so the most difference that can arrive grows faster than every polynomial only through a loop, and, with "
     "natural-number strengths, each positive one at least one, through every loop that couples at every step "
     "(narrowed and taken on 18 October 2026, D43: with real strengths below one such a loop need not run away, which "
     "is damping), couplings that hold only at some steps being open here."),
    # P120
    ("*Readings* [AI reading, open]. Ren asked on 12 October 2026 “how how accurate can we do that uh what is the "
     "limitation do we have losses” ([source](../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-"
     "100.md)), and on 16 October took",
     "*Readings* [AI reading, D43]. Ren asked on 12 October 2026 “how how accurate can we do that uh what is the "
     "limitation do we have losses” ([source](../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-"
     "100.md)), and on 16 October took"),
    ("only through a loop of the couplings that go on; whether through every such loop is not derived here.",
     "only through a loop of the couplings that go on, and not through every such loop: one that recurs rarely stays "
     "polynomial (`Frequency.Sparse.polynomial`, under “How often couplings act” below)."),
    # P125
    ("*Readings* [AI reading, open]. Observation is not a second relation beside dependence but standing at the end of "
     "a route of readings from what is observed; a formation comes to observe by a reading that closes a route.",
     "*Readings* [AI reading, D43]. Observing lies within the downstream: a formation's exchange responds to a "
     "difference at a stock only through a level it reads that lies downstream of the stock, so a formation observes "
     "only at the end of a route of readings from what is observed, the route of length zero being direct observation; "
     "a formation comes to observe by a reading that closes a route. That observation is no second relation beside "
     "dependence goes beyond the theorem, which shows only that it does not go beyond dependence; it is kept as a "
     "conjecture (§8.4)."),
    # P123
    ("*Readings* [AI reading, open]. Ren asked on 12 October 2026 “how how accurate can we do that uh what is the "
     "limitation do we have losses” ([source](../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-"
     "100.md)); how fast a difference runs away is set by how often couplings act: frequent returns make it run away and "
     "rare coupling steps keep it polynomial",
     "*Readings* [AI reading, D43]. Ren asked on 12 October 2026 “how how accurate can we do that uh what is the "
     "limitation do we have losses” ([source](../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-"
     "100.md)); how fast a difference runs away is set by how often couplings act: with natural-number strengths, each "
     "positive one at least one, frequent returns make it run away (with strengths below one they need not), and rare "
     "coupling steps keep it polynomial"),
    # the situation makes it true
    ("the core states what every situation obeys, and the situation makes the actual change true; a chance",
     "the core states what every situation obeys, and the situation makes the actual change true; its formal part, the "
     "determination of the law whose moves are situations, holds by construction, since the situation names the "
     "configuration it leads to, and the content is the count (`Situations.sum_finer`; D43); a chance"),
    # D1 at §6
    ("A reading [AI reading, D1, D10]: 生生 reads as the generative space (section 6.13), and comparison uses no reading "
     "of `living`;",
     "A reading [AI reading, D1, D10]: 生生 reads as generation generating generation, its direction compared by "
     "widening the generative space (section 6.13), and comparison uses no reading of `living`;"),
    # the whole first
    ("not as a description of what life does.",
     "not as a description of what life does [AI reading, D43]."),
    # entangled
    ("The coupling strengths measure it (`Becoming.Propagation`): how entangled a whole is reads as how strongly its "
     "exchanges are coupled to each other's levels, and the carried amount as how far and how fast an act's difference "
     "can grow in it. This reading is not identified with quantum entanglement [AI reading, D39].",
     "The coupling strengths measure it (`Becoming.Propagation`). Ren's sentence goes on: “everyone country, every "
     "person, is heavily coupled into it”. Its two clauses are read by two structures: “heavily coupled into it” by "
     "the coupling strengths, and “a highly entangled system” by couplings that lie on loops through the whole, so that "
     "what an act's difference does comes back around and no finite order of responses fixes it "
     "(`carriedWithin_exact_of_no_loop`, " + LOOPS_LT + "); how highly is the strengths along the loops and how often "
     "they act, and the carried amount reads as how far and how fast an act's difference can grow in it. This reading "
     "is not identified with quantum entanglement [AI reading, D39]."),
    # §8.2 row of worlds as runs
    ("That \"the one root is the run\" is the AI's reading; the theory does not adopt it (§8.4).",
     "Read so, the run is the formal root of the package, not a ground beneath the world: its index of steps is a "
     "reading of the relata's own courses, which are the relational start (§8.3, D43)."),
    # §8.3
    ("numbered D1–D39. The readings change no theorem and add no premise to any law, and a better argument revises "
     "them.",
     "numbered D1–D43. Ren took D1, D5, D22 and D39, revised, and the readings of D43 on 18 October 2026 ([words](" +
     CWORDS + ")); his taking them is their provenance, not their warrant. The readings change no theorem and add no "
     "premise to any law, and a better argument revises them."),
    ("- 生生 is read as the generative space, the widening of what can form. The three scopes of 7 October 2026 are "
     "scopes of what is counted. Living significance and C share this reading, and courses are compared on "
     "possibilities (D1, D22).",
     "- 生生 is read as generation generating generation: what forms preserves, restores, transmits or creates the "
     "conditions and generators of further forming, so a course changes what can form, and the capacity to form, along "
     "with the state. The generative space is what can form now, and the direction of 生生 is compared by widening it. "
     "The three scopes of 7 October 2026 are scopes of what is counted. Living significance and C share this reading, "
     "and courses are compared on possibilities (D1, D22, revised on 18 October 2026)."),
    ("- Succession is read through the formed relations of continuation. 生生不息 is read at the level of the whole, as "
     "arising that recurs through renewal: in a bounded whole whose rest is idle it is return, and endless novelty "
     "needs gain from beyond every bounded part (D5; `Becoming.Gain`).",
     "- Succession is read through the formed relations of continuation. 生生不息 is read at the level of the whole: "
     "不息 as arising that recurs through renewal, and 生生不息 as 生生 going on with more still able to form. In a "
     "bounded whole whose rest is idle 不息 is return, which falls short of 生生不息; under the first law, more without "
     "end needs inflow from beyond every bounded part, not growth (`Flow.new_beyond_every`). Return is forced by "
     "natural-number amounts, a commitment of the representation (D5, revised on 18 October 2026; `Becoming.Gain`)."),
    ("How entangled a whole is reads as how strongly its exchanges are coupled to each other's levels; this is not "
     "quantum entanglement (D39).",
     "In Ren's sentence, “heavily coupled into it” reads as coupling strength, and “a highly entangled system” as "
     "couplings that lie on loops through the whole, how highly being the strengths along the loops and how often they "
     "act; this is not quantum entanglement. A held difference keeps arriving under laws that create amounts, and under "
     "the first law this is not shown (D39, revised on 18 October 2026)."),
    ("- Names: the AI's working names are adopted where the statement has their exact meaning, and 生起／止息 is "
     "adopted as the Chinese for arising and ceasing (D36).\n",
     "- Names: the AI's working names are adopted where the statement has their exact meaning, and 生起／止息 is "
     "adopted as the Chinese for arising and ceasing (D36).\n"
     "- What an extrapolation given nothing fixes, the boundary of enough under undetermined laws and when the runs of "
     "a process settle are read with exact scope: in worlds a list holds a prefix fixes the future through the map, "
     "and a reading is a function, not a model held; enough is a relation of the process with the target, and failing "
     "to rest because runs keep changing is not 无明; not changing for ever is not settling (D40-D42, on Ren's words "
     "of 18 October 2026).\n"
     "- Taken by Ren on 18 October 2026 with the decision brief's recommendations (D43): the step index is a reading of "
     "the relations, not their ground (R1); a count is a relation (R2); only a loop makes a difference run away, and "
     "every loop that couples at every step does so only with natural-number strengths, since a damped loop need not "
     "(P118, narrowed); a cut loses what longer routes carry, and a loop of recurring couplings need not run away "
     "(P120, P123); observing lies within the downstream (P125, weakened; that observation is no second relation "
     "beside dependence is a conjecture); the tail's strengths, for a whole of this kind and a related whole (P126); "
     "going on by coming round, and dependent choice in general (P127); the run is the formal root of the package, not "
     "a ground beneath the world, since its index of steps is a reading of the relata's own courses (P130, revised "
     "after R1); the counterfactual is the course the same law generates (P130); the joins' readings (U, U2); lifting "
     "where branching is finite (I4b-4); the whole first, as an order of how complete a judgment is. The likeness of "
     "`Novelty`'s quantification to `BoundaryInvariant` is an analogy only.\n"),
    ("which situation happens is not a count (`Becoming.Situations`). They read Ren's words of 16 October 2026",
     "which situation happens is not a count (`Becoming.Situations`; the determination of the law whose moves are "
     "situations holds by construction, and the content is the count, `Situations.sum_finer`, D43). They read Ren's "
     "words of 16 October 2026"),
    # glossary and crosswalk
    ("| 生生 (generativity) | Ren's term: the arising within the whole and its going on generating further; the object "
     "of the ethical direction. It is not the Lean predicate `living`: the `living` readings do not include further "
     "generation, and whether they are 生生 is a philosophical argument. | none; `living` is narrower |",
     "| 生生 (generativity) | Ren's term: the arising within the whole and its going on generating further, generation "
     "generating generation: what forms preserves, restores, transmits or creates the conditions and generators of "
     "further forming (D1, taken by Ren on 18 October 2026); the object of the ethical direction. Its direction is "
     "compared by widening what can form now, the generative space. It is not the Lean predicate `living`, whose "
     "readings do not include further generation. | none; `living` is narrower; the direction: `Web.Widens` |"),
    ("the generative space is where a part widens what can form (§6.13).",
     "the generative space is what can form now, and where a part widens it is the region Ren's sentence of 11 October "
     "names (§6.13; D22, revised on 18 October 2026)."),
    ("This chapter's 生生 is the object of the ethical direction, and its formal `Unceasing` (\"unceasing arising\") is "
     "much weaker: some formation arises at arbitrarily late steps.",
     "This chapter's 生生 is the object of the ethical direction. The chapter reads 不息 as arising that recurs through "
     "renewal and 生生不息 as 生生 going on at the whole with more still able to form, so return into copies of "
     "existing forms falls short (D5, taken by Ren on 18 October 2026). The formal `Unceasing` (\"unceasing arising\") "
     "is much weaker: some formation arises at arbitrarily late steps."),
]
SPANS = {CE: ("**Readings not yet adopted** [AI reading, open].\n", "**Normative warrant** is not a choice of reading.",
              S84_NEW, 9)}

# ---------------------------------------------------------------------------------- THE-THEORY-OF-BECOMING.zh.md
CZ = CH + 'THE-THEORY-OF-BECOMING.zh.md'
MARK[CZ] = '生成者生成新的生成'
DC = '../../../' + RF + 'DELEGATED-CHOICES.md'

EDITS[CZ] = [
    ("包括生成的空间：部分在其中扩大能形成者，把“更好”读作扩大，C 是规律（§6.13）。",
     "包括生成的空间：当下能形成者，部分在其中扩大它之处是生成发生的区域，把“更好”读作扩大，C 是规律（§6.13）。"),
    ("“生”与“生生”的读法依 Ren 2026-10-15 的交托由 AI 决定（生生读作生成的空间，[D1](" + DC + ")）；",
     "“生”与“生生”的读法是 AI 的读法，Ren 2026-10-18 取（生生读作生成者生成新的生成，其方向以扩大比较，[D1](" + DC + ")）；"),
    ("比较不用它，生生读作生成的空间（AI 依 Ren 2026-10-15 的交托决定，[D1](" + DC + ")）；是否即生生，是哲学论证",
     "比较不用它；生生读作生成者生成新的生成，其方向以能形成者的扩大比较（AI 的读法，Ren 2026-10-18 取，[D1](" + DC +
     ")）；`living` 的读法不含进一步的生成，所以不读出生生"),
    ("生成的空间是部分在其中扩大能形成者之处（§6.13）",
     "生成的空间是当下能形成者，部分在其中扩大它之处是 Ren 2026-10-11 那句话所说的区域（§6.13；D22，2026-10-18 修订）"),
    ("接续经延续的已形成关系读，“生生不息”读在整体的层次，即经更新而复现的生起（AI 依 Ren 2026-10-15 的交托决定，[D5](" + DC +
     ")）。",
     "接续经延续的已形成关系读，“生生不息”读在整体的层次：不息是经更新而复现的生起，生生不息是生生继续而仍有更多能形成，只回返、"
     "复制已有形式的整体有不息而无生生不息（AI 的读法，经修订由 Ren 2026-10-18 取，[D5](" + DC + ")）。"),
    ("读法（AI 的，待 Ren）：有限多配置之内", "读法（AI 的，Ren 2026-10-18 取，D43）：有限多配置之内"),
    ("读法（AI 的，待 Ren）：依存于整体而不依存于其任何部分者", "读法（AI 的，Ren 2026-10-18 取，D43）：依存于整体而不依存于其任何部分者"),
    ("读作水平永不消失，同一个整体只需要弱的规则，读作终将消失则需要有限全知原则的规则。",
     "读作水平永不消失，这样的整体只需要弱的规则；读作终将消失，一个相关的整体（经典地是它的补，在核心中是另一个律）需要有限全知"
     "原则的规则。"),
    ("所持的差别不断到达，因为水平持有所给的。",
     "所持的差别不断到达，因为水平持有所给的；这在什么也不取、因而创造量的律（携带之律）下表明，在第一定律下未表明：其余不净给出"
     "的有限整体中，水平留在存量之内（`Flow.whole_bounded_of_rest_idle`）。"),
    ("所以能到达的最大差别快于每个多项式，只经由回路，且经由每个每步耦合的回路；只在某些步成立的耦合在这里开放。",
     "所以能到达的最大差别快于每个多项式，只经由回路，且在强度为自然数、每个正的强度至少为一时，经由每个每步耦合的回路（2026-10-18 "
     "收窄并取，D43：实数强度小于一时，这样的回路不必失控，即阻尼）；只在某些步成立的耦合在这里开放。"),
    ("读法（AI 的，待 Ren）：Ren 2026-10-12 问“how how accurate can we do that uh what is the limitation do we have "
     "losses”（[来源](../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)），2026-10-16 把",
     "读法（AI 的，Ren 2026-10-18 取，D43）：Ren 2026-10-12 问“how how accurate can we do that uh what is the limitation "
     "do we have losses”（[来源](../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)），"
     "2026-10-16 把"),
    ("是否经由每个这样的回路这里不推出。",
     "不必经由每个这样的回路：稀少复现的回路保持多项式（`Frequency.Sparse.polynomial`，见下文“耦合多常作用”）。"),
    ("读法（AI 的，待 Ren）：观察不是依赖之外的第二种关系，而是站在从所观察者出发的所读路线的末端；一个形成开始观察，是一次读"
     "闭合一条路线。",
     "读法（AI 的，经减弱由 Ren 2026-10-18 取，D43）：观察在下游之内：一个形成的交换只经它所读、位于储量下游的水平回应储量上的"
     "差别，所以一个形成只在从所观察者出发的所读路线的末端观察，长度为零的路线是直接观察；一个形成开始观察，是一次读闭合一条路线。"
     "观察不是依赖之外的第二种关系，超出定理，定理只表明观察不越出依赖；作为猜想保留。"),
    ("读法（AI 的，待 Ren）：Ren 2026-10-12 问回路“how how accurate",
     "读法（AI 的，Ren 2026-10-18 取，D43）：Ren 2026-10-12 问回路“how how accurate"),
    ("失控多快由耦合多常作用定：返回频繁则失控，",
     "失控多快由耦合多常作用定：强度为自然数、每个正的强度至少为一时，返回频繁则失控（强度小于一时不必），"),
    ("耦合强度度量它（`Becoming.Propagation`）：一个整体有多纠缠，读作其交换与彼此的水平耦合有多强，所携带的量读作一个动作的"
     "差别在其中能多远、多快地增长（读法是 AI 的，依 Ren 2026-10-15 的交托采用，不等同于量子的纠缠，D39）。",
     "耦合强度度量它（`Becoming.Propagation`）。Ren 的这句话接着说“everyone country, every person, is heavily coupled "
     "into it”，两个分句由两种结构读出：“heavily coupled into it”读作耦合强度，“a highly entangled system”读作耦合位于贯穿"
     "整体的回路上，所以一个动作的差别所做的会绕回来，没有有限的回应阶确定它（`carriedWithin_exact_of_no_loop`、"
     "`carriedWithin_lt_of_loop`）；多“highly”是回路上的强度与它们作用的频度，所携带的量读作一个动作的差别在其中能多远、多快"
     "地增长（读法是 AI 的，经修订由 Ren 2026-10-18 取，不等同于量子的纠缠，D39）。"),
    ("中，编号 D1–D39。它们不改动任何定理",
     "中，编号 D1–D43；D1、D5、D22 与 D39 经修订，D43 的各项读法，由 Ren 2026-10-18 取（[原话](" + CWORDS + ")），"
     "这是其来源，不是其根据。它们不改动任何定理"),
    ("- 生生读作生成的空间，即能形成者的扩大；Ren 2026-10-07 的三种范围是所计者的范围；G0 与 C 共用这一读法，继续之间以可能性"
     "比较（D1、D22）。",
     "- 生生读作生成者生成新的生成：所形成者保存、恢复、传递或创造进一步形成的条件与生成者，所以一个进程连同状态一起改变能形成者"
     "与形成的能力；生成的空间是当下能形成者，生生的方向以其扩大比较；Ren 2026-10-07 的三种范围是所计者的范围；G0 与 C 共用这一"
     "读法，继续之间以可能性比较（D1、D22，2026-10-18 修订）。"),
    ("- 接续经延续的已形成关系读；生生不息读在整体的层次，即经更新而复现的生起：在其余闲置的有界整体中它是回返，无尽的新需要来自"
     "每个有界部分之外的增益（D5；`Becoming.Gain`）。",
     "- 接续经延续的已形成关系读；生生不息读在整体的层次：不息是经更新而复现的生起，生生不息是生生继续而仍有更多能形成；在其余闲置"
     "的有界整体中不息是回返，回返不足以是生生不息；在第一定律下，无尽的更多需要来自每个有界部分之外的流入，不是增长"
     "（`Flow.new_beyond_every`）；回返由自然数的量迫使，那是表示的一项承诺（D5，2026-10-18 修订；`Becoming.Gain`）。"),
    ("一个整体有多纠缠读作其交换与彼此水平耦合有多强，不等同于量子的纠缠（D39）。",
     "Ren 的句子中，“heavily coupled into it”读作耦合强度，“a highly entangled system”读作耦合位于贯穿整体的回路上，多"
     "“highly”是回路上的强度与其作用的频度；不等同于量子的纠缠；所持的差别不断到达，在创造量的律下成立，在第一定律下未表明（D39，"
     "2026-10-18 修订）。"),
    ("- 名称：AI 拟定的工作名称在陈述有其确切意义处采用，生起／止息作为中文采用（D36）。\n",
     "- 名称：AI 拟定的工作名称在陈述有其确切意义处采用，生起／止息作为中文采用（D36）。\n"
     "- 不被给予任何东西的外推所确定者、不确定之律下够的边界与过程的运行何时安定，以确切范围读：在由列表容纳的世界中，前缀确定经映射"
     "的未来，读法是函数，不是被持有的模型；够是过程与目标的关系，因运行不断变化而不能静止不是无明；不永远变化不是安定（D40-D42，"
     "依 Ren 2026-10-18 的话）。\n"
     "- Ren 2026-10-18 依决定简报的建议所取的读法（D43）：步的指标是关系的一种读法，不是其根基（R1）；计数是一种关系（R2）；只有"
     "回路使差别失控，而每个每步耦合的回路只在强度为自然数时如此，受阻尼的回路不必（P118，收窄）；截断失去更长路线所携带的，复现"
     "耦合的回路不必失控（P120、P123）；观察在下游之内（P125，减弱；观察不是依赖之外的第二种关系是猜想）；尾的强度，对这样的整体"
     "与相关的整体（P126）；靠回转而延续，一般情形是依赖选择（P127）；运行是这一包的形式之根，不是世界之下的根基，因为其步指标是"
     "关系项自身进程的读法（P130，按 R1 修订）；反事实是同一律生成的进程（P130）；接合的读法（U、U2）；有限分支处的提升（I4b-4）；"
     "整体优先，读作判断有多完整的次序。`Novelty` 的量化与 `BoundaryInvariant` 的相似只是类比。\n"),
    ("自然数权重计数情境，哪个情境发生不是计数（`Becoming.Situations`）。",
     "自然数权重计数情境，哪个情境发生不是计数（`Becoming.Situations`；以情境为移动之律的确定性按构造成立，内容是计数，"
     "`Situations.sum_finer`，D43）。"),
    ("| 生生 | 生生 (generativity) | 整体中的生及其继续生成；伦理方向的对象 | `living` |",
     "| 生生 | 生生 (generativity) | 整体中的生及其继续生成，即生成者生成新的生成：所形成者保存、恢复、传递或创造进一步形成的条件与"
     "生成者（D1，Ren 2026-10-18 取）；伦理方向的对象；其方向以当下能形成者的扩大比较 | 无；`living` 更窄；方向：`Web.Widens` |"),
]


def main():
    for path, edits in EDITS.items():
        text = open(path, encoding='utf-8').read()
        if MARK[path] in text:
            print('already edited', path)
            continue
        for old, new in edits:
            n = text.count(old)
            if n != 1:
                sys.exit(f'{path}: expected one match, found {n}: {old[:100]!r}')
            text = text.replace(old, new)
        if path in SPANS:
            start, end, new, items = SPANS[path]
            if text.count(start) != 1 or text.count(end) != 1:
                sys.exit(f'{path}: span markers not unique')
            i, j = text.index(start), text.index(end)
            old_span = text[i:j]
            if old_span.count('\n- [') != items:
                sys.exit(f'{path}: span holds {old_span.count(chr(10) + "- [")} listed records, expected {items}')
            text = text[:i] + new + text[j:]
        open(path, 'w', encoding='utf-8').write(text)
        print('edited', path, len(edits), 'edits')


if __name__ == '__main__':
    main()
