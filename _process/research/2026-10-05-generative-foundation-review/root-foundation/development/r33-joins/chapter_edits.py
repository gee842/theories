#!/usr/bin/env python3
"""R33: the chapter's paragraphs on the joins (English edition; the Chinese edition's two sentences on
LoopReturn and Tolerance). Section 9 (receipt, counts, layers, connectivity) is chapter_text.py's.

* G4: the three bullets on a law along one run become one, the law and its three readings.
* G5: learning through a map is tracking in the limit (the Limit paragraph); "rests" in the learning
  sense says "predicts".
* G6: the section 4 table rows and the LoopReturn paragraph keep factor and coupling strength apart and
  cite the join.
* G7: the Tolerance paragraph states the tolerance law as a web's run.
* G10: the Interleavings paragraph states the world an interleaving builds.
Each replacement is exact and occurs once. Run once."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CH = ROOT / 'theories/becoming/chapters'
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
STUDY = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
S224 = STUDY + '#224-joins-r33'


def edit(path, pairs):
    s = path.read_text()
    for old, new in pairs:
        assert s.count(old) == 1, (path.name, old[:90], s.count(old))
        s = s.replace(old, new, 1)
    path.write_text(s)
    print(path.name, len(pairs), 'edits')


EN = CH / 'THE-THEORY-OF-BECOMING.md'
s = EN.read_text()
i = s.index('- *Along one run, and exactly* ([Becoming.LawAlongRun]')
j = s.index('\n', s.index('- *Through coupling that changes* ([Becoming.LawThroughChangingCoupling]', i))
G4_OLD = s[i:j]
G4_NEW = (
    f"- *Along one run, under a relation* ([Becoming.LawAlongRun]({LEAN}LawAlongRun.lean), "
    "[a-law-through-a-projection-along-one-run](../results/records/a-law-through-a-projection-along-one-run.md)). "
    "One law: under an equivalence, some process going alike under it admits a run's steps up to a step exactly where "
    "any two of them alike under it, by the same move, end alike (`Run.law_under_iff`). The record read under it is "
    "the witness, and once the criterion fails it fails from then on (`Run.no_law_under_later`). Its three readings "
    "are corollaries. *Through a projection*, the relation of equal images: the record read through π is the least "
    "candidate (`Run.law_through_iff`, `Run.record_least`), and through the identity at every step it is the law a "
    "history shows (`Run.consistent_id_iff`, `exists_law_iff`). *Through coupling that changes*: with dependences "
    "read off the configuration (`Dependence`), what a formation couples into on each occasion, through the "
    "dependence it then has, is an equivalence (`Dependence.alikeAt_equivalence`, `Run.law_through_dependence_iff`), "
    "and `Web.AlikeThrough` read at one step is that coupling with the step's dependence held fixed "
    "(`Dependence.alikeThrough_iff_fixedAt`). *Through fixed conditions*, the instance whose dependences do not "
    "change: what a formation couples into is exactly `Web.AlikeThrough` on the runs read through the conditions "
    "(`Conditions.alikeThrough_iff`, `Run.law_through_coupling_iff`, `Dependence.conditions_alikeAt_iff`), and where "
    "a formation's dependences up to a step are that step's the two criteria agree (`Run.consistent_unchanged_iff`). "
    "A run can be consistent where the process does not go alike (`Constant`). A level the formation does not couple "
    "into can decide what it next couples into, however determined the process is, and then no law holds at its "
    "coupling along the run (`Unseen.no_law`); coupling into that level restores it (`Unseen.consistent_observing`). "
    "Where dependences form or dissolve, neither the fixed nor the changing criterion gives the other: a dissolving "
    "dependence carries a law the coupling fixed at the start lacks, and a forming one breaks a law it has "
    "(`Changing.dissolving_consistent`, `Changing.dissolving_fixed_inconsistent`, `Changing.forming_fixed_consistent`, "
    "`Changing.forming_inconsistent`). A law at a description is not yet an exact model of finite paths: the image is "
    "exact in the sense of `Generative.projection_exact_iff` exactly where configurations alike match each other's "
    "steps up to π (`image_exact_iff`, `exact_law_iff`), and going alike does not give it (`Stuck`). Study: "
    f"[section 181]({STUDY}#181-a-law-through-a-projection-along-one-run-g3), "
    f"[section 185]({STUDY}#185-a-law-through-what-a-formation-couples-into-along-one-run-g4), "
    f"[section 187]({STUDY}#187-a-law-through-coupling-that-changes-along-the-run-g5), [section 224]({S224}).")

edit(EN, [
    (G4_OLD, G4_NEW),
    # G5
    ("Identification in the limit verifies and refutes each hypothesis in the limit (`Limit.identifies_verifies`, "
     "`Limit.identifies_refutes`); `Learnable.Predicts` is such identification along an orbit through a map.",
     "Identification in the limit verifies and refutes each hypothesis in the limit (`Limit.identifies_verifies`, "
     "`Limit.identifies_refutes`). It is the case of a constant target of tracking in the limit, a guess that from some "
     "horizon on is the target's value at the horizon (`Limit.Tracks`, `Limit.identifies_iff_tracks`), and learning "
     "through a map is tracking: an extrapolation predicts a feature along every run exactly where its guess, fixed "
     "by the record through the map, tracks the feature (`LearnableRuns.predicts_iff_tracks`), and in a world a list "
     "holds a feature is learnable exactly where some guess so fixed tracks it (`LearnableRuns.learnable_iff_tracks`). "
     "Where the law leaves the feature unchanged this is identifying it in the limit "
     "(`LearnableRuns.learnable_iff_identifies`); without that premise it is not: a feature the law changes can be "
     "learnable while its value at the start is identified by no guess so fixed "
     "(`LearnableRuns.Merge.learnable_not_identifies`)."),
    ("and rests on the feature from step T when it proposes the feature's value at every step from T on",
     "and predicts the feature from step T when it proposes the feature's value at every step from T on"),
    ("- An extrapolation resting on both has features that agree from some step on (`agree_of_predicts_both`). Where "
     "the features differ at arbitrarily late steps, no extrapolation rests on both,",
     "- An extrapolation predicting both has features that agree from some step on (`agree_of_predicts_both`). Where "
     "the features differ at arbitrarily late steps, no extrapolation predicts both,"),
    ("In every world a list holds, it rests from `Becoming.Identification`'s bound on (`predicts_through`).",
     "In every world a list holds, it predicts the feature from `Becoming.Identification`'s bound on (`predicts_through`)."),
    ("some extrapolation reading through the map rests at every configuration exactly where",
     "some extrapolation reading through the map predicts the feature at every configuration exactly where"),
    ("No extrapolation given nothing rests on every learnable feature: in a one-configuration world",
     "No extrapolation given nothing predicts every learnable feature: in a one-configuration world"),
    ("This table of the world rests in accord with every learnable feature from the bound",
     "This table of the world predicts every learnable feature from the bound"),
    ("Every value the feature takes once it rests is a label (`Learnable.label_of_predicts`).",
     "Every value the feature takes from the step from which the extrapolation given a table predicts it is a label "
     "(`Learnable.label_of_predicts`)."),
    ("The witness that no extrapolation given nothing rests on every learnable feature is elementary;",
     "The witness that no extrapolation given nothing predicts every learnable feature is elementary;"),
    # G6
    ("| 5. Bounded conflict | A loop closes a difference only through a link that gives back less than it received "
     "(`Becoming.LoopReturn`, below). | Real strengths are open. |",
     "| 5. Bounded conflict | A loop closes a difference only through a link that gives back less than it received "
     "(`Becoming.LoopReturn`, below); a link's factor, what it multiplies the returning difference by, is not a coupling "
     "strength: on a condition coupled to itself with strength `M` the factor is `1 + M` (`LoopReturn.selfLoop_carried`). "
     "| Real factors are open. |"),
    ("the bound is attained by the carrying law, which is not gainless, and an actual loop of whole-number strengths "
     "keeps the difference at product 1 and runs away at product 2 or more (`LoopReturn.whole_strengths`);",
     "the bound is attained by the carrying law, which is not gainless. Read on a loop's return map, a condition coupled "
     "to itself with strength `M` multiplies the carried difference by `1 + M` each step, which is the carried amount "
     "and its gap exactly (`LoopReturn.selfLoop_carried`, `LoopReturn.selfLoop_gap`), and around a cycle of several "
     "conditions the course multiplying by one plus the product of the strengths stays at or below the carried amount "
     "(`LoopReturn.carried_around_course`); a loop of whole-number factors keeps the difference at factor 1 and runs "
     "away at factor 2 or more (`LoopReturn.whole_factors`), so on a self-coupled condition every positive whole "
     "strength carries a positive difference past every bound;"),
    ("The speed of a runaway with real strengths is open;", "The speed of a runaway with real factors is open;"),
    ("With whole-number strengths there is nothing between: a loop closes at the first turn, keeps the difference at "
     "every turn, or runs away (`whole_strengths`, `nothing_between`). Closing gradually needs a link that is not a "
     "multiplication (`gradual_needs_another_link`).",
     "With whole-number factors there is nothing between: a loop closes at the first turn, keeps the difference at "
     "every turn, or runs away (`whole_factors`, `nothing_between`). Closing gradually needs a link that is not a "
     "multiplication (`gradual_needs_another_link`). A link's factor is what it multiplies by; a strength is a coupling "
     "strength of `Becoming.Propagation`, and around a cycle the product of the coupling strengths (`Loops.product`). "
     "The two meet on `Becoming.Loops`' carried amount: a condition holding what it has and coupled to itself with "
     "strength `M` multiplies its difference by `1 + M` each turn, so the course of that return map is the carried "
     "amount and its gap against the quiet course (`geomBound_eq_course`, `selfLoop_carried`, `selfLoop_gap`, through "
     "`carried_attained`); around a cycle of several conditions, the intermediate conditions holding and still giving, "
     "the return map by one plus the product of the coupling strengths stays at or below the carried amount after "
     f"each turn (`carried_around_course`), and the equality is not shown. Study: [section 224]({S224})."),
    # G7
    ("and is available exactly where the envelopes are separated (`certified_available_iff`, `certified_blocked`).",
     "and is available exactly where the envelopes are separated (`certified_available_iff`, `certified_blocked`). "
     "On a web the tolerance law is a run. Let each condition depend only on itself and need `k a` units, and let it be "
     "given one unit by each upstream formation supported the step before; then support is the run of the tolerating "
     "law with tolerance the number upstream less `k a`, where `k a` is at most that number (`web_tolerating`, and "
     "`web_activity_tolerating` where activity is support); a web is built to these terms (`giftWeb`, "
     "`giftWeb_tolerating`). With `k a` all upstream it is `Becoming.Withholding`'s law without memory "
     f"(`web_answers`). Study: [section 224]({S224})."),
    # G10
    ("- The own courses fix the interleaving exactly where every exchange touches a relatum and every two exchanges are "
     "the same or share one (`unique_iff`, `traced_unique_iff`).\n",
     "- The own courses fix the interleaving exactly where every exchange touches a relatum and every two exchanges are "
     "the same or share one (`unique_iff`, `traced_unique_iff`).\n"
     "- *The world an interleaving builds.* From a local law on whole-number standings, the relata listed, a list of "
     "exchanges and a start, `LocalLaw.world` is a `World` of the spine: at step `t` each relatum stands where the first "
     "`t` exchanges leave it (`world_level`), is active where the exchange at `t` touches it, and takes from itself or "
     "gives to itself what the step changes, so with every relatum listed once each step balances (`world_balances`). "
     "Two interleavings of the same own courses give every relatum the same course of standings, its standing after "
     "each of its own exchanges in order (`standings_of_courses`, `standings_of_interleavings`), and the same standing "
     "from both lengths on (`world_final`). Taking two adjacent exchanges that share no relatum in either order leaves "
     "the world alike at every step but the one between them (`world_swap`); at that step a relatum either of them "
     "touches stands, in one world, where it stands one step later or earlier in the other, and one neither touches "
     "stands alike (`world_swap_between`). For two interleavings differing by more than one such exchange, a relation "
     f"between their worlds step by step is not stated. Record: [the-world-an-interleaving-builds](../results/records/"
     f"the-world-an-interleaving-builds.md). Study: [section 224]({S224}).\n"),
])

ZH = CH / 'THE-THEORY-OF-BECOMING.zh.md'
edit(ZH, [
    ("整数强度下回路要么第一圈闭合，要么保持，要么失控，中间没有（`whole_strengths`）。",
     "整数倍率下回路要么第一圈闭合，要么保持，要么失控，中间没有（`whole_factors`）；环节的倍率不是耦合强度：自身以强度 `M` "
     "耦合的条件每圈把差乘以 `1 + M`，正是 `Becoming.Loops` 所携带的量及其差（`selfLoop_carried`、`selfLoop_gap`），绕几个条件的回路，"
     "以一加强度之积为倍率的进程不超过所携带的量（`carried_around_course`）。"),
    ("并恰在包络分隔处可用（`certified_kept`、`certified_available_iff`）。",
     "并恰在包络分隔处可用（`certified_kept`、`certified_available_iff`）。在网上容忍律是一个运行：每个条件只依赖自身、需要 `k a` "
     "个单位、由上一步每个受支持的上游形成各给一个单位时，支持就是容忍数为上游数减 `k a` 的容忍律之运行（`web_tolerating`）；"
     "`k a` 取全部上游时即 `Becoming.Withholding` 无记忆之律（`web_answers`）。"),
])
