#!/usr/bin/env python3
"""A4 (19 October 2026): the chapter, English and Chinese, after decision D45 ("integrate all, the theory is a whole,
not stitched pieces, go ahead"). The readings are decided as one account: §7's open readings are adopted, §8.3 gains
the revisions of D3, D19, D20, D21, D37 and D39 and the item D45, §8.4 keeps only what is not a reading, §8.8 states
what R18 is, and the glossary gains 明 and 识 and the decided term for coming to rest.

The Chinese edition takes the same decisions where it carries the passages, and two sweeps:
- 静止 -> 停息 for the rest family (D45 (4)), outside link targets, anchors and code spans; the edition uses 静止 only
  in the sense of 停 (events no longer recurring), never in the sense of 静;
- bare 生成 meaning becoming -> 生成／变化, as the title and the glossary write it (D45 (5)).

The blocks are written against the text N6 leaves (N6 rewrites some of the same lines), so this lands after N6.
Each old string must match exactly once (the 生成 sentence that occurs twice, exactly twice); the Chinese old strings
are matched after the sweep. If a file already carries the kit's mark it is left alone.
usage (from the repository root): python3 -B apply_chapter.py [ROOT]"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
EN = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
MARK = {EN: '[AI reading, D45]', ZH: '（AI 的，D45）'}
SRC = '../../../sources/15-codex-theory-conversations/'
RF = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
REC = '../results/records/'

# ------------------------------------------------------------------------------------------------ English
EN_BLOCKS = [
    # legend
    ("**[AI reading, open]** marks a reading not yet adopted. The open readings are listed in section 8.4. Ren took D1, "
     "D5, D22, D39 and D43 on 18 October 2026 (section 8.3).",
     "**[AI reading, open]** marks a reading not yet decided, listed in section 8.4. Ren took D1, D5, D22, D39 and D43 "
     "on 18 October 2026, and on 19 October answered the register as a whole: each reading is decided by its place in "
     "one account, and none waits on him (D45, section 8.3)."),
    # section 2, observation as a route
    ("That observation is no second relation beside dependence goes beyond the theorem, which shows only that it does "
     "not go beyond dependence; it is kept as a conjecture (§8.4).",
     "That observation is no second relation beside dependence, in the sense that `obs` could be derived from "
     "dependence, goes beyond the theorem, which shows only that it does not go beyond dependence; it is kept as a "
     "conjecture (§8.4). In the sense that both are coupling, it holds (“Where a level couples into a formation”, "
     "below)."),
    # section 2, where a level couples into a formation
    ("*Reading* [AI reading, open]. `obs` is not a second kind of relation beside the couplings and readings: it marks "
     "where a level can couple into a formation by level, as dependence marks where it can couple by threshold; what "
     "can couple in bounds what responds, and a law's responses are its couplings. This answers, for the level branch, "
     "the question that [observation-is-a-route](" + REC + "observation-is-a-route.md) leaves open.",
     "*Reading* [AI reading, D45]. `obs` is not a second kind of relation beside the couplings and readings: it marks "
     "where a level can couple into a formation by level, as dependence marks where it can couple by threshold, so both "
     "are coupling; what can couple in bounds what responds without fixing it "
     "(`ExchangeLaw.response_not_fixed_by_coupling`), and a law's responses are its couplings. That is the sense in "
     "which observation is no second relation. The stronger sense, that `obs` could be derived from dependence, is the "
     "conjecture [observation-is-a-route](" + REC + "observation-is-a-route.md) keeps (§8.4): `obs` is supplied."),
    # section 3, the boundary condition for 无明
    ("*Readings* [AI reading, D26]. 无明 is the not-seeing that keeps seeking locked onto a target that cannot be met at "
     "rest. 明 (míng, “seeing, clarity”) is coupling that reaches what support does not mark. Knowing enough and knowing "
     "where to stop (知足, 知止) are targets within the boundary of enough.",
     "*Readings* [AI reading, D26, D45]. 无明 is the not-seeing that keeps seeking locked onto a target that cannot be "
     "met at rest. The position every formation selects from grounds it and is not it: the position is why the losses "
     "locked seeking makes beyond what couples into it do not reach it through its own feedback (§7.2). 明 (míng, "
     "“seeing, clarity”) is coupling that reaches what support does not mark. Knowing enough (知足) is a target met at a state the law leaves unchanged (`Law.rests_iff`), and "
     "knowing where to stop (知止) is a target within that boundary, so that a pursuit ends by enough and not by "
     "exhaustion (`Flow.more_exhausted`). Where targets come from the dynamics do not decide; the laws say which "
     "targets can rest."),
    # section 7.2, readings
    ("*Readings* [AI reading, open].\n\n- **无明 is a position, not a defect.** Every formation, human or AI, selects "
     "through its own couplings. These laws say what that position does not see: what lies beyond its coupling closure, "
     "its own act's difference there, where what it raises is drawn from, how far off its break is, what a finite "
     "history leaves open, what its untaken acts would have done, and whether its target can rest. Runs that keep "
     "changing are a feature of the process, not of the target, and are not 无明 (D41).",
     "*Readings* [AI reading, D45].\n\n- **The position is not a defect; 无明 is the seeking it leaves locked.** Every "
     "formation, human or AI, selects through its own couplings. These laws say what that position does not see: what "
     "lies beyond its coupling closure, its own act's difference there, where what it raises is drawn from, how far off "
     "its break is, what a finite history leaves open, what its untaken acts would have done, and whether its target "
     "can rest. The position is not 无明: 无明 is seeking locked onto a target that cannot rest, and the position is why "
     "the losses that seeking makes beyond what couples into it do not reach it through its own feedback (§7.3, D26). "
     "Runs that keep changing are a feature of the process, not of the target, and are not 无明 (D41)."),
    # section 7.3, the reading
    ("*Reading* [AI reading, D26]. 无明 is the not-seeing that keeps seeking locked onto a target that cannot be met at "
     "rest. 明 (míng, “seeing, clarity”) is coupling that reaches what support does not mark; D26 words it with "
     "“registration”, which the naming study replaced by coupling.",
     "*Reading* [AI reading, D26, D45]. 无明 is the not-seeing that keeps seeking locked onto a target that cannot be "
     "met at rest. 明 (míng, “seeing, clarity”) is coupling that reaches what support does not mark."),
    # section 7.3, readings
    ("*Readings* [AI reading, open].\n\n- **明 is a relation, not a state.** It is as wide as the couplings joined to a "
     "selection, and it widens as measurement, models and others are joined. The three routes have one structure: each "
     "joins to a selection a coupling that reaches where the selector's own does not.",
     "*Readings* [AI reading, D45].\n\n- **明 is a relation, not a state.** It is as wide as the couplings joined to a "
     "selection, and it widens as measurement, models and others are joined. The three routes have one structure: each "
     "joins to a selection a coupling that reaches where the selector's own does not.\n"
     "- **识, 理 and 明 are one structure.** 识 is a formation's own further course, its selection, response or "
     "seeking, factoring through the lumping its own couplings make. 理, formally, is a lumping the world goes alike "
     "across (`goAlike_iff_lumped`), and a selection through a model is right about what matters only where what "
     "matters goes alike across the model's lumping (`Learning.selects_right_through`). 明 widens the couplings a "
     "course goes through; whether the world goes alike across what they lump is the question of 理.\n"
     "- **Situational awareness is 明 of one's own reach.** Feedback couples in at most the influence closure "
     "(`Flow.Balances.uncoupled_beyond_influence`). The coupling closure holds the influence closure and is that "
     "closure where only support couples in, so only observation can widen it "
     "(`Flow.withinCoupling_of_withinInfluence`, `Flow.withinCoupling_thresholdOnly`, `Flow.withinCoupling_mono_obs`). "
     "A part reaches its reach closure. What situational awareness has to know is therefore the gap of law 1, the "
     "reach closure less the coupling closure (D20)."),
    # section 7.4
    ("*Reading* [AI reading, open]. Alignment, so read,",
     "*Reading* [AI reading, D45]. Alignment, so read,"),
    # section 7.5
    ("**Where the two parts meet** [AI reading, open].",
     "**Where the two parts meet** [AI reading, D45]."),
    # section 7.7
    ("The readings marked open in §7.2–§7.5 are the AI's.",
     "The readings of §7.2–§7.5 are the AI's. They were open until 19 October 2026, when the readings were decided as "
     "one account, and are adopted with the scope this section states (D45)."),
    # section 8, introduction
    ("The open readings are in §8.4. The formal statement being complete",
     "Since 19 October 2026 no reading is open (§8.4, D45). The formal statement being complete"),
    # section 8.2, origins, refutation and the remaining joins
    ("the order form of `IdealWarrant` on partial orders (the general mathematical line, kept outside the spine for "
     "now); the join of `IdealWarrant` under a structural name (§8.4).",
     "the join of `IdealWarrant` with `CompletionRole` and `HistoryIdeals` as one core family of ideals under "
     "structural names, decided on 19 October 2026 (D45; new Lean, board item A4-L): over a partial order, a property "
     "of ideals is finitely refutable exactly when it is Scott-closed, and `Becoming.Refutable` is its case on runs."),
    # section 8.3, introduction
    ("numbered D1–D43. Ren took D1, D5, D22 and D39, revised, and the readings of D43 on 18 October 2026 ([words](" + SRC
     + "2026-10-18-central-readings-taken.md)); his taking them is their provenance, not their warrant. The readings "
     "change no theorem and add no premise to any law, and a better argument revises them. Whether they stand as a "
     "whole is open (§8.4).",
     "numbered D1–D45. Ren took D1, D5, D22 and D39, revised, and the readings of D43 on 18 October 2026 ([words](" + SRC
     + "2026-10-18-central-readings-taken.md)). On 19 October he answered the register as a whole, “integrate all, the "
     "theory is a whole, not stitched pieces, go ahead” ([words](" + SRC + "2026-10-19-integrate-all.md)): the readings "
     "stand as one account, each decided by its place in it, and where two did not fit together the account decided "
     "between them (D45, the last item below). His words are their provenance, not their warrant. The readings change "
     "no theorem and add no premise to any law, and a better argument revises them."),
    # section 8.3, D3
    ("- The second 生 is what can form, active or not. Arising that depends on depletion is classed through the "
     "comparison. Embodied relata are 生, and generation is not restricted to embodiment (D3, D4).",
     "- The second 生 is further generation: what can form, active or not, with the conditions and generators of "
     "further forming, as D1 reads 生生. What can form is the part the comparison reads, so arising that depends on "
     "depletion is classed through it; the capacity to form is not yet a measure (§8.2). Embodied relata are 生, and "
     "generation is not restricted to embodiment (D3, revised on 19 October 2026; D4)."),
    # section 8.3, D16-D20
    ("The whole realizing itself reads as a represented boundary that is the whole. \"Situational awareness\" reads as a "
     "center knowing what its part reaches beyond its feedback (D16–D20).",
     "The whole realizing itself reads, as judgment, as a represented boundary that is the whole, and, as knowing, as a "
     "knowing made by its parts that is never complete (`Frame.self_incomplete`, `Diagonal.Unfolds.incomplete`). "
     "\"Situational awareness\" reads as 明 of one's own reach: knowing what one's part reaches beyond what couples into "
     "it, the gap of §7.2's first law (D16–D20; D19 and D20 revised on 19 October 2026)."),
    # section 8.3, D37
    ("in the exact sense of tail events, without probability (D37).",
     "in the exact sense of tail events, without probability (D37; its 识 clause answered on 19 October 2026 by option "
     "(b) of the naming study)."),
    # section 8.3, D39
    ("and under the first law this is not shown (D39, revised on 18 October 2026).",
     "and under the first law this is not shown (D39, revised on 18 October 2026; its 识 clause answered on 19 October "
     "2026: the strength measures coupling, not 识)."),
    # section 8.3, D21
    ("- The presupposition reads Ren's \"belief\". The admissible drawings of a self include the whole. The order of "
     "levels reads as three readings of the presupposition (D21).",
     "- The presupposition reads Ren's \"belief\". The admissible drawings of a self include the whole. The order of "
     "levels reads as three readings of the presupposition. Whether the step of invariance holds is a question of "
     "warrant (§6.11, §8.5), on which Ren's testimony would be provenance (D21, revised on 19 October 2026)."),
    # section 8.3, D45
    ("The likeness of `Novelty`'s quantification to `BoundaryInvariant` is an analogy only.\n\n"
     "**Identification and situations.**",
     "The likeness of `Novelty`'s quantification to `BoundaryInvariant` is an analogy only.\n"
     "- One account (D45, on Ren's answer of 19 October 2026). The readings form one account in five links, each "
     "resting on its theorems: one unfolding, generation, continuation and its extent, knowing, and alignment. In the "
     "knowing link coupling is the primitive, by threshold where a formation depends on a condition and by level where "
     "it observes it, and the law's sensitivity (D37) and the coupling strength (D39) measure coupling. 识 is a "
     "formation's own further course factoring through the lumping its own couplings make, and 理, formally, a lumping "
     "the world goes alike across. 知足 is a target met at a state the law leaves unchanged, and 知止 a target within "
     "that boundary, so that a pursuit ends by enough and not by exhaustion. 无明 is seeking locked onto a target that "
     "cannot rest; the position every formation selects from is neither a defect nor 无明, and it is why the losses of "
     "that seeking beyond what couples into it do not reach it through its own feedback. 明 is coupling joined to a selection that reaches what support does not mark (D26, "
     "revised). §7's readings, open until then, are the knowing link applied to selection, adopted with §7's scope. "
     "`obs` and dependence are both coupling, by level and by threshold; that `obs` could be derived from dependence "
     "stays a conjecture (§8.4).\n\n"
     "**Identification and situations.**"),
    # section 8.4, up to the generativity chain
    ("The readings and choices below are open. Each is decided by argument, as the readings of §8.3 are; where the "
     "readings are the AI's, the records state them in full. Who said a word is provenance; it does not settle a "
     "reading.\n\n"
     "**Ren's texts and terms.** OPENING's body is Ren's text, and Ren's terms keep Ren's wording: the Chinese term for "
     "coming to rest (归于静止 or 停) and the heading \"the rest theorem\" (静止定理); \"closure bounds change\"; 识 and 理 "
     "as Ren reads them. These change only with Ren; what they are read to mean is open to argument like any "
     "reading.\n\n"
     "**Provenance.** Whether a reading is Ren's own, and whether Ren holds the step of invariance (§6.11), are "
     "questions of provenance, answered from Ren's words. Neither decides whether the step holds, which is a question "
     "of warrant (§8.5).\n\n"
     "**The commitments of the representation.** Discrete steps, natural-number amounts, the census where infinitely "
     "many stand, and decided equality and listing are commitments of the representation (class b; Ren reserved them "
     "on 11 October 2026: \"(b) belongs to the representation, which needs my decision\"). Whether each should stay a "
     "commitment, be refined or be derived is open, and is decided by what the representation must express (§8.5, the "
     "scope of representation) and by the theorems at finer grains (`Becoming.Units`, `Becoming.Resolution`).\n\n"
     "**Readings not yet adopted** [AI reading, open].\n"
     "- [where-a-level-couples](" + REC + "where-a-level-couples.md): `obs` is not a second kind of relation beside the "
     "couplings and readings; it marks where a level can couple into a formation by level, as dependence marks where it "
     "can couple by threshold; what can couple in bounds what responds, and a law's responses are its couplings.\n"
     "- Kept as a conjecture, not a reading ([observation-is-a-route](" + REC + "observation-is-a-route.md)): "
     "observation is no second relation beside dependence. `apart_only_downstream` shows only that observing lies "
     "within the downstream, the reading taken on 18 October 2026 (D43).\n"
     "- §7.2–§7.5: 无明 read as the position of every formation in alignment; capability read as reach, the gap being "
     "reach less coupling; 明 read as a relation that widens as measurement, models and others are joined; holding 明 "
     "for others (measurement, models others can check, pools that include those an act reaches), with correction "
     "reaching the rule and each law's scope kept exact; alignment for all as pooled coupling across intelligences, "
     "whose acts respond to a difference only through members that couple it apart, with correction and escalation "
     "read as one loop through another's coupling and response; the conditional direction's opportunities to correct "
     "read as the routes of 明 ([source](" + SRC + "2026-10-18-the-light-and-alignment-for-all.md)).\n\n"
     "Ren took the other readings this list held on 18 October 2026, as D43, together with the revised D1, D5, D22 and "
     "D39 ([words](" + SRC + "2026-10-18-central-readings-taken.md)).\n\n"
     "**The adopted readings as a whole.** Whether the readings of §8.3 stand as a whole (item 50 of the eighteenth "
     "review's fix list, finding D-f). Ren's \"agree with other readings\" of 16 October is provenance; it does not "
     "settle them. Ren took D1, D5, D22, D39 and D43 by name on 18 October, and D40-D42 rest on his words of that day. "
     "The [decision brief](" + RF + "READINGS-PENDING-REN.md#c-the-register-itself-d-f-review-item-50) recommends no "
     "blanket ratification: a reading of one of Ren's phrases needs his word on that phrase, and a reading of a theorem "
     "needs only argument.",
     "No reading is open since 19 October 2026. Ren answered the register as a whole, “integrate all, the theory is a "
     "whole, not stitched pieces, go ahead” ([words](" + SRC + "2026-10-19-integrate-all.md)), and each reading is "
     "decided by its place in one account (§8.3, D45). A reading added later is decided the same way, by argument and "
     "by how it fits the rest; who said a word is provenance and does not settle it. What this section keeps is not a "
     "choice of reading.\n\n"
     "**Ren's texts and terms.** OPENING's body is Ren's text, and the generativity chain is his curated argument; they "
     "change only through proposals to him. His terms keep his wording where they are quoted, with their source, and "
     "are read like any reading (D45). The Chinese term for coming to rest is 停息, with the heading 停息定理 (the rest "
     "theorem): these theorems say that events stop recurring, which is 停, not what holds at once, which is 静, and 息 "
     "is what 生生不息 negates. \"Closure bounds change\" stays Ren's phrase, and the law keeps its name, enclosure "
     "bounds change. 识 and 理 have their places in the account (§8.3).\n\n"
     "**Provenance.** Whether a reading is Ren's own is a question of provenance, answered from Ren's words. Whether "
     "the step of invariance holds (§6.11) is a question of warrant (§8.5), on which Ren's testimony would be "
     "provenance (D21).\n\n"
     "**The commitments of the representation.** Discrete steps, natural-number amounts, the census where infinitely "
     "many stand, and decided equality and listing are commitments of the representation (class b; Ren reserved them "
     "on 11 October 2026: \"(b) belongs to the representation, which needs my decision\"). They stay. Whether each "
     "should stay a commitment, be refined or be derived is the question of the scope of representation (§8.5), "
     "decided by what the representation must express and by the theorems at finer grains (`Becoming.Units`, "
     "`Becoming.Resolution`); Ren's reservation is provenance (D45).\n\n"
     "**A conjecture, not a reading** ([observation-is-a-route](" + REC + "observation-is-a-route.md), "
     "[where-a-level-couples](" + REC + "where-a-level-couples.md)). That observation is no second relation beside "
     "dependence, in the sense that `obs` could be derived from dependence. `obs` is supplied, and "
     "`apart_only_downstream` shows only that observing lies within the downstream (D43). What is adopted is the "
     "weaker sense: `obs` marks where a level couples into a formation by level, as dependence marks where it couples "
     "by threshold, so both are coupling; a law's sensitivity is the least coupling it reads through (D37); and "
     "coupling bounds a response without fixing it (`ExchangeLaw.response_not_fixed_by_coupling`; D45).\n\n"
     "**The readings as a whole**, decided on 19 October 2026 (D45; item 50 of the eighteenth review's fix list, "
     "finding D-f). No reading is ratified item by item; each stands, or is revised, by its place in one account, and "
     "Ren's answer replaces the question whether his \"agree with other readings\" of 16 October ratified them ([brief, "
     "Part C](" + RF + "READINGS-PENDING-REN.md#c-the-register-itself-d-f-review-item-50)). The readings this list "
     "held are decided: where a level couples, as above; §7.2–§7.5, adopted with §7's scope; and the rest, taken by Ren "
     "on 18 October 2026 as D43 with the revised D1, D5, D22 and D39 ([words](" + SRC
     + "2026-10-18-central-readings-taken.md))."),
    # section 8.4, the review's questions
    ("**Questions from the whole-repository review of 16–17 October.**\n"
     "- Whether an independent review beyond the eighteenth, an AI review that built no Lean, is needed (§8.8).\n"
     "- The join of `IdealWarrant` under a structural name.\n"
     "- Who integrates, and who owns the open whole-deduction target (W-root).\n"
     "- Whether to split the three senses of 生成: the whole (生成之论), formation, and the generative (生成的空间).\n"
     "- Whether the chapter's sentence on living significance under the condition says all the Lean shows: "
     "immediately, living significance is the condition restricted to living claims, and the condition gives "
     "significance to every claim, not a positive valence.",
     "**Questions from the whole-repository review of 16–17 October**, decided on 19 October 2026 (D45).\n"
     "- R18 counts as the review its records asked for. Wherever it is cited its kind is stated: an AI review, "
     "read-only, which built no Lean (§8.8).\n"
     "- `IdealWarrant` is joined with `CompletionRole` and `HistoryIdeals` as one core family of ideals under "
     "structural names; this is new Lean, open in §8.2 until it lands (board item A4-L).\n"
     "- No integrator is named: the board's fallback stands, in which landers take the queue in order of readiness. "
     "W-root's claim lapsed; its open part is the §8.1 target on the root of wisdom, and the whole-deduction target was "
     "never W-root's.\n"
     "- The three senses of 生成 are kept apart in the Chinese edition by three words: 展开 for the one unfolding, 形成 "
     "for a formation and its forming, and 生成 for generation; becoming is 生成／变化, as in the edition's title "
     "(glossary, “Becoming”).\n"
     "- The sentence on living significance under the condition says what the Lean shows: living significance is the "
     "condition restricted to living claims, and the condition gives every claim significance, with no positive "
     "valence (`g0_of_unrestricted`, `relevance_least`)."),
    # section 8.8, the R18 row
    ("items 44–51 are open questions (§8.4); handled in study §163 |",
     "items 44–49 and 51 were answered on 18 October 2026 (D43, with the revisions of D1, D5, D22 and D39) and item 50 "
     "on 19 October (D45); handled in study §163 |"),
    # section 8.8, not yet reviewed
    ("- Because the eighteenth review was an AI review that built no Lean, records it corrected say \"reviewed by R18 "
     "(AI, read-only)\". Whether a further independent review is needed is open (§8.4).",
     "- The eighteenth review counts as the review its records asked for: a reviewer other than the author reading the "
     "statements against the Lean and the readings against their scope, while the checker's receipts check the proofs "
     "(D45). Wherever it is cited its kind is stated: an AI review, read-only, which built no Lean; no human review is "
     "claimed. Records it reviewed say \"reviewed by R18 (AI, read-only)\" in place of \"not independently reviewed\"; "
     "records it did not cover keep that phrase."),
    # glossary
    ("| Becoming (生成／变化) | The whole unfolding made up of the forming, holding, transforming, degrading and "
     "dissolving of relations. | — |",
     "| Becoming (生成／变化) | The whole unfolding made up of the forming, holding, transforming, degrading and "
     "dissolving of relations. The Chinese edition writes becoming as 生成／变化 and keeps bare 生成 for generation, the "
     "opposite of degeneration (退化, D2); the one unfolding is 展开, and a formation and its forming are 形成 (D45). "
     "| — |"),
    ("| coming to rest (归于静止) | From some step on,",
     "| coming to rest (停息) | From some step on,"),
    ("The Chinese term and the title 静止定理 (the rest theorem) are Ren's. The rest theorem:",
     "The Chinese term is 停息, and the title 停息定理 (the rest theorem): the theorems say that events stop recurring, "
     "which is 停, not what holds at once, which is 静 (D45). The rest theorem:"),
    ("| enough (够) | A goal is met at a state the unfolding leaves unchanged. Under a determined law, seeking rests "
     "exactly where it reaches such a state. | `Law.rests_iff`, `Law.fixed_rests` |",
     "| enough (够) | A goal is met at a state the unfolding leaves unchanged. Under a determined law, seeking rests "
     "exactly where it reaches such a state. Knowing enough (知足) is such a goal, and knowing where to stop (知止) a "
     "goal within this boundary, so that a pursuit ends by enough and not by exhaustion (AI readings, D26, D45). "
     "| `Law.rests_iff`, `Law.fixed_rests` |"),
    ("| 无明 (not-seeing) | An AI reading: the not-seeing that locks seeking onto a goal that cannot be met at rest. Its "
     "boundary is enough. | `Becoming.Seeking` |",
     "| 无明 (not-seeing) | An AI reading: the not-seeing that locks seeking onto a goal that cannot be met at rest. Its "
     "boundary is enough. The position every formation selects from grounds it and is not it (§7.2, D45). "
     "| `Becoming.Seeking`, `Flow.unselected_beyond_coupling` |\n"
     "| 明 (seeing, clarity) | An AI reading: coupling joined to a selection that reaches what support does not mark. A "
     "relation, not a state: as wide as the couplings joined to a selection, it widens as measurement, models and "
     "others are joined (§7.3, D26, D45). | `Web.observed_raise_couples`, `Web.selects_alike_all_iff` |\n"
     "| 识 (shí) | Ren's word, kept for a derived structure (option (b) of the naming study): a formation's own further "
     "course, its selection, response or seeking, factoring through the lumping its own couplings make. It is not a "
     "relation beside coupling; the law's sensitivity and the coupling strength measure coupling, not 识 (D37, D39, "
     "D45). | `Web.SelectsThrough`, `Web.selects_alike_iff` |"),
    # glossary, retired labels
    ("| folding (of G0, of Part II) | the restatement of an axiom as a condition (dated note in §6.15) | — |",
     "| folding (of G0, of Part II) | the restatement of an axiom as a condition (dated note in §6.15) | — |\n"
     "| 归于静止, 静止定理 (Chinese terms for coming to rest and the rest theorem) | 停息, 停息定理 (D45, 19 October "
     "2026) | — |"),
]

# ------------------------------------------------------------------------------------------------ Chinese
# Old strings are given as the text stands before the sweep; they are swept before matching. New strings are final.
ZH_BLOCKS = [
    # section 2, observation as a route
    ("观察不是依赖之外的第二种关系，超出定理，定理只表明观察不越出依赖；作为猜想保留。",
     "观察不是依存之外的第二种关系，若指 `obs` 可由依存推出，就超出定理，定理只表明观察不越出依存；这作为猜想保留（§8）。"
     "若指两者都是耦合，经水平与经阈，它成立（D45）。"),
    # section 3, the boundary condition for 无明
    ("读法（AI 的，依 Ren 2026-10-15 的交托采用）：无明是使寻求锁定在不能于静止中满足之目标上的不见；明是及于支持所不标记者的"
     "耦合；知足、知止是够的边界之内的目标；",
     "读法（AI 的，D26、D45）：无明是使寻求锁定在不能于停息中满足之目标上的不见；每个形成作选择所在的位置是它的根据，却不是它："
     "位置是被锁定的寻求在其所耦合入者之外造成的损失不经其自身的反馈到达它的缘由（§7.2）；明是及于支持所不标记者的耦合；知足是在律所不变的状态被满足的目标"
     "（`Law.rests_iff`），知止是这一边界之内的目标，使追逐因够而止，不因耗尽而止（`Flow.more_exhausted`）；目标从何而来，"
     "动力学不决定，规律说的是哪些目标能停息；"),
    # section 7.2, readings
    ("读法（AI 的，开放）：\n\n- **无明是一个位置，不是缺陷。** 每个形成，人或 AI，都经自己的耦合选择。这些规律说出这个位置所"
     "不见的：耦合闭包之外的，自身动作在那里的差别，所抬高者从何处汲取，断裂还有多远，有限历史所留下的开放，未取之动作本会造成"
     "什么，以及目标能否静止。不断变化的运行是过程的特征，不是目标的，不是无明（D41）。",
     "读法（AI 的，D45）：\n\n- **位置不是缺陷；无明是它所留下的被锁定的寻求。** 每个形成，人或 AI，都经自己的耦合选择。这些"
     "规律说出这个位置所不见的：耦合闭包之外的，自身动作在那里的差别，所抬高者从何处汲取，断裂还有多远，有限历史所留下的开放，"
     "未取之动作本会造成什么，以及目标能否停息。位置不是无明：无明是锁定在不能停息之目标上的寻求，位置是这一寻求"
     "在其所耦合入者之外造成的损失不经其自身的反馈到达它的缘由（§7.3，D26）。不断变化的运行是过程的特征，不是目标的，不是无明（D41）。"),
    # section 7.3, the reading
    ("读法（AI 的，D26）：无明是使寻求锁定在不能于静止中满足之目标上的不见。明是及于支持所不标记者的耦合；D26 以“识”表述，"
     "命名研究把它改为耦合。",
     "读法（AI 的，D26、D45）：无明是使寻求锁定在不能于停息中满足之目标上的不见。明是及于支持所不标记者的耦合。"),
    # section 7.3, readings
    ("读法（AI 的，开放）：\n\n- **明是关系，不是状态。** 它与接到选择上的耦合一样宽，随量度、模型与他者的接入而扩展。三条路有"
     "同一结构：各把一个及于选择者自身耦合所不及之处的耦合，接到选择上。",
     "读法（AI 的，D45）：\n\n- **明是关系，不是状态。** 它与接到选择上的耦合一样宽，随量度、模型与他者的接入而扩展。三条路有"
     "同一结构：各把一个及于选择者自身耦合所不及之处的耦合，接到选择上。\n"
     "- **识、理与明是同一结构。** 识是一个形成自身的进一步历程，即它的选择、回应或寻求，经其自身耦合所成之归并而行。理在形式上"
     "是世界经它同去的归并（`goAlike_iff_lumped`）；经模型的选择，只在要紧者经模型的归并同去之处，对要紧者是对的"
     "（`Learning.selects_right_through`）。明扩展一个历程所经的耦合；世界是否经它们所归并者同去，是理的问题。\n"
     "- **情境的觉知是对自身所及的明。** 反馈至多耦合入影响闭包（`Flow.Balances.uncoupled_beyond_influence`）。耦合闭包含影响"
     "闭包，只经支持耦合入时就是影响闭包，所以只有观察能使它变宽（`Flow.withinCoupling_of_withinInfluence`、"
     "`Flow.withinCoupling_thresholdOnly`、`Flow.withinCoupling_mono_obs`）。部分到达其所及闭包。所以情境的觉知要知道的，是"
     "规律 1 的缺口，即所及闭包减去耦合闭包（D20）。"),
    # section 7.4
    ("读法（AI 的，开放）：如此读，对齐",
     "读法（AI 的，D45）：如此读，对齐"),
    # section 7.5
    ("**两部分在何处相接**（AI 的读法，开放）。",
     "**两部分在何处相接**（AI 的读法，D45）。"),
    # section 7.7
    ("§7.2–§7.5 中标为开放的读法是 AI 的。",
     "§7.2–§7.5 的读法是 AI 的；它们开放到 2026-10-19，那时诸读法作为一个说明被决定，以本节所说的范围采用（D45）。"),
    # section 8, introduction
    ("其后，每个开放项归入四类之一：属于 Ren 的、哲学根据、经验对应、进一步的证明。先前列为 Ren 的选择的读法与名称，Ren "
     "2026-10-15 交 AI 以其最好的判断决定（[原话](" + SRC + "2026-10-15-delegated-choices.md)），决定连同理由与会改变它们的"
     "东西在[决定记录](" + RF + "DELEGATED-CHOICES.md)中；仍属 Ren 的在下面列出。",
     "其后，每个开放项归入四类之一：开放的读法、哲学根据、经验对应、进一步的证明；2026-10-19 起没有开放的读法（D45）。先前列为 "
     "Ren 的选择的读法与名称，Ren 2026-10-15 交 AI 以其最好的判断决定（[原话](" + SRC + "2026-10-15-delegated-choices.md)）；"
     "2026-10-19 Ren 对整个登记作答，每个读法由它在一个说明中的位置决定，不再有读法等待 Ren，他自己用语的读法也一样。决定连同"
     "理由与会改变它们的东西在[决定记录](" + RF + "DELEGATED-CHOICES.md)中；Ren 的文本与来源在下面列出。"),
    # section 8, the readings: introduction
    ("中，编号 D1–D43；D1、D5、D22 与 D39 经修订，D43 的各项读法，由 Ren 2026-10-18 取（[原话](" + SRC
     + "2026-10-18-central-readings-taken.md)），这是其来源，不是其根据。",
     "中，编号 D1–D45；D1、D5、D22 与 D39 经修订，D43 的各项读法，由 Ren 2026-10-18 取（[原话](" + SRC
     + "2026-10-18-central-readings-taken.md)）；2026-10-19 Ren 对整个登记作答（[原话](" + SRC
     + "2026-10-19-integrate-all.md)），诸读法作为一个说明成立，每项由它在其中的位置决定，两项不合处由这个说明在其间决定"
     "（D45，下面最后一项）。他的话是其来源，不是其根据。"),
    # D3
    ("- 第二个“生”是能形成者，活跃与否；以消耗为条件的生起经比较归类；体现的关系项是“生”，生成不限于体现（D3、D4）。",
     "- 第二个“生”是进一步的生成：能形成者（活跃与否），连同进一步形成的条件与生成者，如 D1 对生生的读法；能形成者是比较所读的"
     "部分，所以以消耗为条件的生起经比较归类；形成的能力尚不是度量（§8“进一步的证明”）；体现的关系项是“生”，生成不限于体现"
     "（D3，2026-10-19 修订；D4）。"),
    # D16-D20
    ("整体对自身的实现读作以整体为所表示的边界；“situational awareness”读作中心知道其部分在反馈之外所到达的（D16–D20）。",
     "整体对自身的实现，作为判断读作以整体为所表示的边界，作为认识读作由其部分作出、永不完整的认识（`Frame.self_incomplete`、"
     "`Diagonal.Unfolds.incomplete`）；“situational awareness”读作对自身所及的明：知道其部分所及超出耦合入它者之处，即 §7.2 "
     "规律 1 的缺口（D16–D20；D19、D20 于 2026-10-19 修订）。"),
    # D37
    ("取尾事件（不带概率）的确切意义（D37）。",
     "取尾事件（不带概率）的确切意义（D37；其关于识的一句 2026-10-19 依命名研究的选项 (b) 作答）。"),
    # D39
    ("在第一定律下未表明（D39，2026-10-18 修订）。",
     "在第一定律下未表明（D39，2026-10-18 修订；其关于识的一句 2026-10-19 作答：强度度量耦合，不度量识）。"),
    # D21
    ("- 预设读出 Ren 的“belief”；自身的可容许划法包括整体；层级的次序读作预设的三种读法（D21）。",
     "- 预设读出 Ren 的“belief”；自身的可容许划法包括整体；层级的次序读作预设的三种读法；不变之步是否成立是根据问题（§6.11；"
     "§8“哲学根据”），Ren 对它的陈述会是来源，不是根据（D21，2026-10-19 修订）。"),
    # D45, the conjecture, and what stays Ren's
    ("`Novelty` 的量化与 `BoundaryInvariant` 的相似只是类比。\n\n"
     "**尚未采用的读法**（AI 的，开放）。\n\n"
     "- [where-a-level-couples](" + REC + "where-a-level-couples.md)：`obs` 不是耦合与读之外的第二种关系：它标出水平能经水平"
     "耦合入形成之处，如依存标出能经阈耦合之处；所能耦合入者界定所回应者，律的回应即其耦合。\n"
     "- 作为猜想保留，不是读法（[observation-is-a-route](" + REC + "observation-is-a-route.md)）：观察不是依赖之外的第二种"
     "关系。`apart_only_downstream` 只表明观察在下游之内，这是 2026-10-18 所取的读法（D43）。\n"
     "- 第 7.2–7.5 节：无明读作对齐中每个形成的位置；能力读作所及，缺口是所及减去耦合；明读作关系，随量度、模型与他者的接入而"
     "扩展；为他者持明（量度、他者能检查的模型、包含动作所及者的组），纠正须及于规则，各规律的范围保持精确；为一切的对齐读作跨"
     "智能的合起来的耦合，其动作只经把差别耦合得有别的成员回应它，纠正与升级读作同一种经他者耦合与回应的回路；有条件之方向中纠正"
     "的机会读作明之路（[来源](" + SRC + "2026-10-18-the-light-and-alignment-for-all.md)）。\n\n"
     "**仍属于 Ren 的**\n\n"
     "- Ren 自己的文本与用语：OPENING 及其脚注；静止的中文用语（归于静止或停）与“静止定理”这一标题；Ren 命名的“closure bounds "
     "change”；“识”与“理”作为 Ren 的读法。\n"
     "- Ren 的陈述：Ren 是否持有不变之步，以及任何“某读法是否是 Ren 的读法”。\n"
     "- Ren 保留的表示决定（2026-10-11：“(b) belongs to the representation, which needs my decision”）：离散的步、自然数的"
     "量、无穷多立着者处的普查、判定的相等与列出。\n",
     "`Novelty` 的量化与 `BoundaryInvariant` 的相似只是类比。\n"
     "- 一个说明（D45，依 Ren 2026-10-19 的回答）：诸读法构成一个说明，分五环，各以其定理为据：一个展开、生成、延续及其范围、"
     "知、对齐。在知这一环中，耦合是原初的：形成依存于一个条件处经阈耦合入它，观察它处经水平耦合入它；律的敏感（D37）与耦合强度"
     "（D39）度量耦合。识是一个形成自身的进一步历程经其自身耦合所成之归并而行，理在形式上是世界经它同去的归并。知足是在律所不变的"
     "状态被满足的目标，知止是这一边界之内的目标，使追逐因够而止，不因耗尽而止。无明是锁定在不能停息之目标上的寻求；每个形成作选择"
     "所在的位置既不是缺陷也不是无明，是这一寻求在其所耦合入者之外造成的损失不经其自身的反馈到达它的缘由。明是接到选择上、及于支持所不标记者的耦合（D26，修订）。§7 的"
     "读法此前开放，是知这一环用于选择，以 §7 所说的范围采用。`obs` 与依存都是耦合，经水平与经阈；`obs` 可由依存推出，仍是猜想"
     "（见下）。\n\n"
     "**一个猜想，不是读法**（[observation-is-a-route](" + REC + "observation-is-a-route.md)、[where-a-level-couples]("
     + REC + "where-a-level-couples.md)）：观察不是依存之外的第二种关系，即 `obs` 可由依存推出。`obs` 是给出的，"
     "`apart_only_downstream` 只表明观察在下游之内（D43）。所采用的是较弱的意义：`obs` 标出水平经水平耦合入形成之处，如依存"
     "标出经阈耦合之处，所以两者都是耦合；律的敏感是它所经的最小的耦合（D37）；耦合界定回应而不确定它"
     "（`ExchangeLaw.response_not_fixed_by_coupling`；D45）。\n\n"
     "**Ren 的文本与来源**\n\n"
     "- Ren 自己的文本：OPENING 的正文是 Ren 的文本，生成性之链是他所编的论证，两者只经向他的提议而改变；OPENING 的脚注是 AI "
     "写的。他的用语在引用处保留原文与来源，其读法与任何读法一样由论证决定（D45）：停的一族的中文用语是“停息”，非正式标题是"
     "“停息定理”，因为这些定理说的是发生不再复现，即停，不是同时成立者，即静，而息正是生生不息所否定的；“closure bounds "
     "change”保留为 Ren 的说法，规律保留其名（`World.enclosure_bounds_change`）；识与理在一个说明中有其位置（上面 D45 一项）。\n"
     "- 来源：某读法是否是 Ren 自己的，是来源问题，由他的原话回答；不变之步是否成立是根据问题，Ren 对它的陈述会是证言，即来源，"
     "不是根据（D21，2026-10-19 修订）。\n"
     "- 表示的承诺：离散的步、自然数的量、无穷多立着者处的普查、判定的相等与列出保持为承诺；每一项应保持、细化还是推出，是表示的"
     "范围问题（下面的哲学根据），由表示须表达什么与更细粒度上的定理（`Becoming.Units`、`Becoming.Resolution`）决定；Ren "
     "2026-10-11 的保留（“(b) belongs to the representation, which needs my decision”）是来源（D45）。\n"),
    # section 8, review
    ("；延续的奠基（§6.7）已由[独立审查](" + RF + "CONTINUATION-GROUNDING-REVIEW.md)检查，十三项更正已处理。审查检查已有结果，"
     "不是一类开放内容。",
     "；延续的奠基（§6.7）已由[独立审查](" + RF + "CONTINUATION-GROUNDING-REVIEW.md)检查，十三项更正已处理；第十八次审查（"
     "[R18](" + RF + "BECOMING-EIGHTEENTH-REVIEW.md)）是 AI 的审查，只读，未构建 Lean，它算作其记录所要求的审查，凡引用处都"
     "说明其性质，不声称有人的审查（D45）。审查检查已有结果，不是一类开放内容。"),
    # glossary
    ("| 生成／变化 | Becoming | 关系的形成、维持、转化、退化与消解构成的整体展开 | — |",
     "| 生成／变化 | Becoming | 关系的形成、维持、转化、退化与消解构成的整体展开；本版以“生成／变化”写 becoming，单说“生成”指"
     "生成（generation），与退化相对（D2）；同一展开说“展开”，一个形成及其形成说“形成”（D45） | — |"),
    ("| 归于静止 | coming to rest |",
     "| 停息 | coming to rest |"),
    ("（中文术语与“静止定理”这一标题由 Ren 定）",
     "（中文术语是“停息”，标题是“停息定理”：这些定理说的是发生不再复现，即停，不是同时成立者，即静，D45）"),
    ("| 够 | enough | 目标在一个展开所不变的状态被满足；在确定的律之下，寻求恰在到达这样的状态时静止 | `Law.rests_iff`、"
     "`Law.fixed_rests` |",
     "| 够 | enough | 目标在一个展开所不变的状态被满足；在确定的律之下，寻求恰在到达这样的状态时停息；知足是这样的目标，知止是"
     "这一边界之内的目标，使追逐因够而止，不因耗尽而止（AI 的读法，D26，D45） | `Law.rests_iff`、`Law.fixed_rests` |"),
    ("| 无明 | 无明 (not-seeing) | AI 的读法（依 Ren 2026-10-15 的交托采用）：使寻求锁定在不能于静止中满足之目标上的不见；"
     "其边界是够 | `Becoming.Seeking` |",
     "| 无明 | 无明 (not-seeing) | AI 的读法：使寻求锁定在不能于停息中满足之目标上的不见；其边界是够；每个形成作选择所在的位置"
     "是它的根据，却不是它（§7.2，D45） | `Becoming.Seeking`、`Flow.unselected_beyond_coupling` |\n"
     "| 明 | 明 (seeing, clarity) | AI 的读法：接到选择上、及于支持所不标记者的耦合；是关系，不是状态，与接到选择上的耦合一样宽，"
     "随量度、模型与他者的接入而扩展（§7.3，D26，D45） | `Web.observed_raise_couples`、`Web.selects_alike_all_iff` |\n"
     "| 识 | 识 (shí) | Ren 的用语，保留给一个导出的结构（命名研究的选项 (b)）：一个形成自身的进一步历程（选择、回应或寻求）"
     "经其自身耦合所成之归并而行；不是耦合之外的关系，律的敏感与耦合强度度量耦合，不度量识（D37，D39，D45） | "
     "`Web.SelectsThrough`、`Web.selects_alike_iff` |"),
    # bare 生成 meaning becoming
    ("它不先假定生成是好的。", "它不先假定生成／变化是好的。"),
    ("\n- 生成是好的；\n", "\n- 生成／变化是好的；\n"),
    ("\n## 1. 生成：同一展开\n", "\n## 1. 生成／变化：同一展开\n"),
    ("每个生成是否都能像脊柱那样表示", "每个生成／变化是否都能像脊柱那样表示"),
]
TWICE = [("每个生成是否都能这样表示", "每个生成／变化是否都能这样表示")]

# Restatements by items that may land before this kit and that edit text inside its old strings: M4 (where two courses
# rejoin) and N7 (the reading pass on "correction"; Ren, 19 October 2026: "correct? this is a dualist word, are we
# drifting off?"). An old string may match with any of them applied, and exactly one variant must match once.
PEER = {
    EN: [
        ("with correction and escalation read as one loop through another's coupling and response; ",
         "with a response that closes a difference and one that widens it read as one loop through another's coupling "
         "and response, the course without the act as a comparison rather than a standard; "),
        ("with correction reaching the rule and each law's scope kept exact;",
         "with a lasting change reaching the rule and each law's scope kept exact;"),
        ("the conditional direction's opportunities to correct read as the routes of 明",
         "the conditional direction's opportunities to revise read as the routes of 明"),
    ],
    ZH: [
        ("纠正与升级读作同一种经他者耦合与回应的回路；",
         "闭合差别的回应与扩大差别的回应读作同一种经他者耦合与回应的回路，无动作的进程是比较而非标准；"),
        ("纠正须及于规则，各规律的范围保持精确", "持久的改变须及于规则，各规律的范围保持精确"),
        ("有条件之方向中纠正的机会读作明之路", "有条件之方向中修订的机会读作明之路"),
    ],
}

# link targets, explicit anchors and code spans keep their bytes
PROTECT = re.compile(r'\]\([^)\n]*\)|<a id="[^"\n]*"></a>|`[^`\n]*`')


def sweep(text):
    out, last = [], 0
    for m in PROTECT.finditer(text):
        out.append(text[last:m.start()].replace('静止', '停息'))
        out.append(m.group(0))
        last = m.end()
    out.append(text[last:].replace('静止', '停息'))
    return ''.join(out)


def variants(path, old):
    subs = [pair for pair in PEER[path] if pair[0] in old]
    out = []
    for mask in range(2 ** len(subs)):
        v = old
        for i, (a, b) in enumerate(subs):
            if mask >> i & 1:
                v = v.replace(a, b)
        out.append(v)
    return out


def apply(path, text, blocks, transform=lambda s: s, twice=()):
    for old, new in blocks:
        hits = [v for v in variants(path, transform(old)) if text.count(v)]
        if len(hits) != 1 or text.count(hits[0]) != 1:
            sys.exit(f'{path}: expected one match, found {[text.count(v) for v in hits]}: {transform(old)[:120]!r}')
        text = text.replace(hits[0], new)
    for old, new in twice:
        old = transform(old)
        n = text.count(old)
        if n != 2:
            sys.exit(f'{path}: expected two matches, found {n}: {old[:120]!r}')
        text = text.replace(old, new)
    return text


def main():
    en = (ROOT / EN).read_text(encoding='utf-8')
    if MARK[EN] in en:
        print('already edited', EN)
    else:
        en = apply(EN, en, EN_BLOCKS)
        (ROOT / EN).write_text(en, encoding='utf-8')
        print('edited', EN, '| [AI reading, open] left:', en.count('[AI reading, open]'))
    zh = (ROOT / ZH).read_text(encoding='utf-8')
    if MARK[ZH] in zh:
        print('already edited', ZH)
        return
    before = zh.count('静止')
    zh = sweep(zh)
    swept = before - zh.count('静止')
    zh = apply(ZH, zh, ZH_BLOCKS, sweep, TWICE)
    (ROOT / ZH).write_text(zh, encoding='utf-8')
    left = [m.start() for m in re.finditer('静止', zh)]
    print('edited', ZH, f'| 静止 -> 停息: {swept}; 静止 left: {len(left)} (in link targets);',
          'AI 的，开放 left:', zh.count('AI 的，开放'), '| 开放） left:', zh.count('读法，开放'))


if __name__ == '__main__':
    main()
