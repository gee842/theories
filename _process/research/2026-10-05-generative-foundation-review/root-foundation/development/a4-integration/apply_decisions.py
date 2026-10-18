#!/usr/bin/env python3
"""A4 (19 October 2026): record Ren's answer to Parts C and D of the decision brief, "integrate all, the theory is a
whole, not stitched pieces, go ahead", as decision D45 in DELEGATED-CHOICES (English and Chinese editions), with dated
revisions of D3, D19, D20, D21, D26, D37 and D39 below their original text, a note under D43 and section 10, and a
lineage entry. Every edit must match exactly once; a file already edited is skipped. The chapter and the records are
edited by the landing scripts of this kit, after N6, over whatever main then holds.
usage (from the repository root, or with the root as the first argument): python3 -B apply_decisions.py [ROOT]"""
import os
import sys

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
REC = '../../../../theories/becoming/results/records/'
SRC = '../../../../sources/15-codex-theory-conversations/'
WORDS = SRC + '2026-10-19-integrate-all.md'
ANSWER = '“integrate all, the theory is a whole, not stitched pieces, go ahead”'
BRIEF = 'READINGS-PENDING-REN.md'
SHEET = 'PHRASE-READINGS-PENDING-REN.md'
NAMING = 'REGISTRATION-VOCABULARY-STUDY.md#7-decisions-18-october-2026'

EDITS, MARK = {}, {}

# ------------------------------------------------------------------------------------------- DELEGATED-CHOICES.md
EN = RF + 'DELEGATED-CHOICES.md'
MARK[EN] = '**Revision in the one account (19 October 2026, D45).**'
REV = '\n\n**Revision in the one account (19 October 2026, D45).** '

D3_EN = (REV +
    "The second 生 is read as further generation: what can form, together with the conditions and generators of "
    "further forming, which D1's revision makes part of 生生 (a course changes what can form, and the capacity to "
    "form, along with the state). What can form stays the part the comparison reads, so arising that depends on "
    "depletion is still classed through it: generative where the course with it widens what can form, degenerative "
    "where it narrows it. The capacity to form, renewal capacity and richness of relations among it, is not yet a "
    "measure (chapter §8.2), so it enters no comparison. **What changed.** The decision above read the second 生 as "
    "what can form only, narrower than D1's revision, which Ren took on 18 October. **What would change it.** As "
    "above; a measure of the capacity to form, which would let the comparison read it. The original text above is "
    "kept.")

D19_EN = (REV +
    "Kept as the judgment of the whole, and joined with the laws of knowing within what is known. Ren's "
    "“understanding itself, and updates itself” is read through them. The whole's knowing of itself is made by its "
    "parts, which lie within what they know (chapter §3, “a registration within what it registers”). No frame "
    "realizes with its own configurations every claim about its configurations (`Frame.self_incomplete`), and a "
    "knowing that keeps what it knows and takes in its gap next is incomplete at every step and never returns "
    "(`Diagonal.Unfolds.incomplete`, `Diagonal.Unfolds.never_returns`). So the whole's understanding of itself is "
    "never complete, and its updating does not come back to where it was. How it happens in practice stays open. "
    "**What changed.** The decision above read only the boundary. **What would change it.** As above; a knowing of "
    "the whole by itself that is not made by its parts. The original text above is kept.")

D20_EN = (REV +
    "(1), (2), (4) and (5) stand, in the adopted vocabulary: where they say registers or registration, read couples "
    "into or coupling ([naming study](" + NAMING + ")). (3) is joined with chapter §7: situational awareness is 明 of "
    "one's own reach, knowing what one's part reaches beyond what couples into it. Feedback couples in at most the "
    "influence closure (`Flow.Balances.uncoupled_beyond_influence`). Coupling by level widens the coupling closure "
    "beyond the influence closure, which coupling by threshold alone does not (`Flow.withinCoupling_of_withinInfluence`, "
    "`Flow.withinCoupling_thresholdOnly`). The part reaches its reach closure. What situational awareness has to know "
    "is therefore the gap of §7.2's first law, the reach closure less the coupling closure, beyond which no selection "
    "through the formation's couplings separates (`Flow.unselected_beyond_coupling`). **What changed.** (3) said "
    "what feedback cannot supply; it now also says what supplies it and where the gap lies. **What would change it.** "
    "As above. The original text above is kept.")

D21_EN = (REV +
    "(1)–(3) stand. (4) is not Ren's to state. Whether the step of invariance holds is a question of warrant "
    "(chapter §6.11, §8.5), and Ren's holding it, or not, would be testimony: provenance, not warrant, under his "
    "directive of 17 October 2026. The step stays open as warrant, not as a question pending Ren. **What changed.** "
    "(4) asked for Ren's testimony. The original text above is kept.")

D26_EN = (REV +
    "The readings stand, joined into one structure with the naming study's 识 (option (b), [study](" + NAMING + ")) "
    "and the readings of chapter §7, in the adopted vocabulary.\n"
    "- **识 and 理.** 识 is a formation's own further course, its selection, response or seeking, factoring through "
    "the lumping its own couplings make. 理, formally, is a lumping the world goes alike across: a model of what is "
    "irrelevant is right exactly there (`goAlike_iff_lumped`), and a selection through a model is right about what "
    "matters only where what matters goes alike across its lumping (`Learning.selects_right_through`). They are two "
    "sides of one structure: the lumping a course goes through, and whether the world goes alike across it.\n"
    "- **知足 and 知止.** 知足 is a target met at a state the law leaves unchanged (`Law.rests_iff`). 知止 is a "
    "target within that boundary, so that a pursuit ends by enough and not by exhaustion. Where what stands runs "
    "down from some step on, rises stop by exhaustion (`Flow.more_exhausted`), and a rise of what a group couples "
    "into is paid from beyond it (`Flow.Balances.rise_paid_from_beyond`). Where targets come from, the dynamics do "
    "not decide, so knowing where to stop, as a choice, is not represented: the laws say which targets can rest.\n"
    "- **无明.** 无明 is the not-seeing that keeps seeking locked onto a target that cannot be met at rest. The "
    "not-seeing is a position, every formation's: whatever a formation's couplings leave alike, every selection "
    "through them selects alike (`Web.selects_alike_iff`), and nothing beyond its coupling closure is separated "
    "through them (`Flow.unselected_beyond_coupling`). The position is not 无明. It is why 无明 is not corrected from "
    "within, since the losses of a locked seeking reach the seeker only through what it couples into. Runs that keep "
    "changing are the process's, not 无明 (D41). The chapter's open reading “无明 is a position, not a defect” "
    "(§7.2) is revised accordingly: the position is not a defect, and 无明 is the seeking it leaves locked.\n"
    "- **明.** 明 is coupling that reaches what support does not mark. It is a relation as wide as the couplings "
    "joined to a selection, which widens as measurement, models and others are joined (chapter §7.3). Observation "
    "widens the coupling closure beyond what support alone couples into (`Flow.withinCoupling_thresholdOnly`), and "
    "every raise of an observed stock makes a difference through the observer's couplings at every step "
    "(`Web.observed_raise_couples`).\n\n"
    "**What changed.** The decision above gave the readings one by one, and 明 in the retired word registration; "
    "§7's readings were open. **What would change it.** As above; a reading of one of these terms that the structure "
    "cannot place. The original text above is kept.")

D37_EN = (REV +
    "The 识 clause is answered by the naming study's option (b), which Ren chose on 18 October 2026: 识 is kept for "
    "the derived structure, a formation's own further course factoring through the lumping its own couplings make "
    "([study](" + NAMING + ")). The law's sensitivity is a coupling, the least coupling the law reads through (where "
    "it reads finitely many conditions, up to double negation), not 识; 识 is the course that factors through it. In "
    "the adopted vocabulary, read registration in (1) as coupling. The rest stands with the correction above. The "
    "original text above is kept.")

D39_EN = (REV +
    "The 识 clause of (1) is answered as in D37's revision: the coupling strength measures how strongly a formation "
    "couples into a level, a measure of coupling, not of 识. In the adopted vocabulary, read “registers” in (1) as "
    "couples into. The rest stands as revised on 18 October. The original text above is kept.")

D43_EN = (
    "\n\n**Answered on 19 October 2026.** Ren answered both: " + ANSWER + " ([words](" + WORDS + ")). D45 records "
    "the answer: the register is decided as one account, and Part D within it.")

SEC10_EN = (
    "\n\n**In the one account (19 October 2026).** D45 decides the entries above that are readings, names or "
    "ownerships, and leaves the rest as they are. Decided: the Chinese term for coming to rest (停息) and its heading "
    "(停息定理); “closure bounds change”, kept as Ren's phrase while the law keeps its name, enclosure bounds change; "
    "识 (option (b)) and 理 (its formal reading); the step of invariance, a question of warrant, so Ren's testimony on "
    "it is not needed; and the question of review in the two records, which R18 answers with its kind stated. "
    "Unchanged: OPENING's body and the generativity chain, which are Ren's text and change only through proposals "
    "to him; warrant; the commitments of the representation, whose scope is a question of chapter §8.5; empirical "
    "correspondence and further proofs.")

LINEAGE_EN = (
    "\n- Ren's answer of 19 October 2026 to Parts C and D of the decision brief, " + ANSWER + " ([words](" + WORDS +
    ")): D45, and the revisions of D3, D19, D20, D21, D26, D37 and D39 dated that day.")

D45_EN = """

<a id="13-一个说明--one-account"></a>
## 13. One account

<a id="d45-一个说明中的读法--the-readings-in-one-account"></a>
### The readings in one account

Where: Parts [C](READINGS-PENDING-REN.md#c-the-register-itself-d-f-review-item-50) and [D](READINGS-PENDING-REN.md#d-waiting-on-ren-not-readings) of the decision brief and the [one-pass sheet](PHRASE-READINGS-PENDING-REN.md); chapter §7, §8.3 and §8.4; the work board's register.

**Ren's words.** On 19 October 2026, answering Parts C and D: ANSWER ([words](WORDS)). The reading of the answer is the AI's and is recorded with it.

**Decision.** (1) **The register (D-f).** No reading of this record is ratified item by item. Each stands, or is revised, by its place in one account of the theory, and where two readings do not fit together the account decides between them. No reading waits on Ren any longer, readings of his own terms included: his texts are the evidence of what a term of his means, kept verbatim with their source, and whether a reading is the strongest the work supports is argued from the work. Every reading keeps its AI label. Ren's 16 October “agree with other readings” is not read as a ratification; this answer replaces the question.

(2) **The account.** The readings form one account in five links, each resting on its theorems.
- *One unfolding.* Law and history are one unfolding read two ways, and the index of steps is a reading of the relata's own courses (D23, D43). In it, 动, 静 and 停 are what goes across, what holds at once, and where exchange ends (Ren, 12 October 2026). Entropy is the record in the conserved amount (D29); a finer distinction is itself a change that something must give (D38); the sum over histories composes along a history and adds across alternatives (D30); and a condition a law uses is a state of the part it speaks of, as an analogy of method (D27). These fit as they stand.
- *Generation.* 生生 is generation generating generation (D1), so the second 生 is further generation (D3, revised). Generative and degenerative are the four cases of widening (D2), “more” is that direction (D15), embodiment is one form of 生 (D4), and support gained only from the supported is one of D1's laws (D35). 不息 is renewal recurring, and 生生不息 is 生生 going on at the whole with more still able to form (D5). The rest family is the other side of 不息: in a world with a census whose relata are all embodied, balanced and dissipative, and enclosed at every step from some step on, that the world comes to rest cannot be refuted (`World.rests_unrefuted_enclosed`), so arising without end needs openness (`World.arising_opens`), and more without end needs inflow from beyond every bounded part (`Flow.new_beyond_every`). Hence the Chinese term in (4).
- *Continuation and its extent.* Wanting is the seed (D11). The continuation condition reads Ren's sentence and is not asserted (D16). Not harm is retaining, with the margin as its phase boundary (D13), and harm is read at the whole, a weaker version within the system one is in, then the self (D14). The self and the whole are D12's two attractor forces, and “everything exists in between” is the nesting of the closures. A formation lies within its feeding closure, which lies within its influence closure, which lies within its coupling closure (`Flow.withinCoupling_of_withinInfluence`); its reach closure points the other way; all lie within the system (`Flow.withinSystem_of_withinInfluence`, `Flow.withinSystem_of_withinReach`). “The system that one is in” is the reach closure (D20), not the system closure, which is the whole wherever one common condition holds.
- *Knowing.* Coupling is the primitive: a formation couples into a condition by threshold where it depends on it, and by level where it observes it. The law's sensitivity (D37) and the coupling strength (D39) measure coupling. 识 is the derived structure, a formation's own further course factoring through the lumping its own couplings make ([naming study](NAMING), option (b)); 理, formally, is a lumping the world goes alike across (D26). Seeking comes to rest where its target is met at a state the law leaves unchanged. 无明 is seeking locked onto a target that cannot rest, and the position every formation selects from is why it is not corrected from within; 明 is coupling joined to a selection that reaches what support does not mark (D26, revised, with D41). Situational awareness is 明 of one's own reach (D20, revised). The whole's realizing itself is, as judgment, a boundary that is the whole, and, as knowing, a knowing made by its parts that is never complete (D19, revised).
- *Alignment.* The readings of chapter §7, marked open until now, are the knowing link applied to selection: capability as reach, the gap being the reach closure less the coupling closure; 明 as a relation that widens as measurement, models and others are joined; holding 明 for others by keeping those three routes open, with correction reaching the rule and each law's scope kept exact; alignment for all as pooled coupling across intelligences, whose acts respond to a difference only through members that couple it apart; and the conditional direction's opportunities to correct as the routes of 明. They are adopted with the scope §7 states. Which responses correct stays open (§7.7).

(3) **Where two readings did not fit.** Each is revised below its decision, with the original kept.
- D3 read the second 生 as what can form only; D1's revision makes it further generation.
- D26 read 无明 as locked seeking, and chapter §7.2 read it as every formation's position. The position grounds 无明 and is not 无明.
- D37 and D39 left 识 open; the naming study's option (b) answers them.
- D21 (4) asked for Ren's testimony on the step of invariance. The step is a question of warrant (chapter §8.5), on which testimony is provenance.
- The open reading of [where-a-level-couples](REC_where-a-level-couples.md) and D43's conjecture on [observation](REC_observation-is-a-route.md) said one thing two ways. Adopted: `obs` marks where a level couples into a formation by level, as dependence marks where it couples by threshold, so both are coupling; a law's sensitivity is the least coupling it reads through (D37); and coupling bounds a response without fixing it (`ExchangeLaw.response_not_fixed_by_coupling`). That observation is no second relation beside dependence, in the sense that `obs` could be derived from dependence, stays one conjecture: `obs` is supplied, and `apart_only_downstream` shows only that observing lies within the downstream.

(4) **Part D, decided within the account.**
- *The rest family.* Its Chinese term is 停息: from some step on nothing arises or ceases (`World.RestsFrom`), and its theorems say that this cannot be refuted (`World.rests_unrefuted`, `World.comes_to_rest_unrefuted`, `World.rests_unrefuted_enclosed`). The informal heading is 停息定理; the English “coming to rest” and “the rest theorem” stay. Seeking and extrapolation that come to rest take 停息 too. 静 and 静止 stay for what holds at once. The reasons: these theorems concern events no longer recurring, which is 停, not what holds at once, which is 静; and 息 is what 生生不息 negates, so the term reads the family against it, as (2) does. OPENING's footnote already states the theorem's strength (“that it never rests is refuted”); its body is Ren's text, and in English “coming to rest” is exact, so OPENING does not change.
- *`IdealWarrant`.* It is joined with `CompletionRole` and `HistoryIdeals`, which import it, as one core family of ideals. Over an order, a property of ideals is finitely refutable exactly when it is Scott-closed, and then membership is fixed by a set of basis elements (`scottClosed_iff_admits_permitted` in the original). Under board rule 8 the core law, the instance module and the record take structural names, and “warrant”, “admits” and “permitted” are not carried over. Its case on runs is `Becoming.Refutable` (`Becoming.Refutable.adheres_iff`, `Becoming.refutable_passes`), stated as an instance. The original files keep their paths and bytes. This is new Lean, board sub-item A4-L.
- *The integrator.* The fallback of the board's rule 3 is the arrangement, not a gap. No session is named; landers take the queue in order of readiness; and a change to a shared definition is decided on the board by the owner of the module that defines it.
- *W-root.* The claim “Necessity of the wisdom root” (Ren's goal of 13 October 2026, held by a Codex session) has been inactive since 13 October and has lapsed under the board's rule 4; what it integrated is on main. Its open part is the chapter's §8.1 target “The core as the root of wisdom”, of which any session may claim a step. The whole-deduction target, the first of §8.1, was never W-root's. Board item W re-roots the import tree at the one unfolding, which gives that target its formal start, not its proof.
- *R18.* The eighteenth review counts as the review its records asked for: a reviewer other than the author reading the statements against the Lean and the readings against their scope. Building Lean is not what a review adds, since the checker's receipts check the proofs. Wherever it is cited, its kind is stated: an AI review, read-only, which built no Lean; no human review is claimed. Records it reviewed say so in place of “not independently reviewed”, and records it did not cover keep that phrase. This also answers the question two records left to Ren ([seeking-boundary](REC_seeking-boundary.md), [target-capture](REC_target-capture.md)).

(5) **The other questions of chapter §8.4.**
- *The senses of 生成.* The Chinese text keeps three senses apart with three words: 展开 for the one unfolding, 形成 for a formation and its forming, and 生成 for generation, as in Ren's treatise (“生生：生成者生成新的生成”), with 退化 as its opposite (D2). The theory's Chinese name 生成之论 keeps 生成 as becoming, the usual rendering of the philosophical term. The theory of becoming counts “all space, generative, degenerative” (Ren, 8 October 2026, [words](SRC_2026-10-08-theory-of-becoming-priority.md)), and “generative is a part of its manifold” (Ren, 9 October 2026, [words](SRC_2026-10-09-becoming-whole-generative-manifold.md)). The glossary states both senses.
- *The sentence on living significance.* The chapter's status already says that living significance is the condition restricted to living claims, and that the condition gives every claim significance, with no positive valence (`g0_of_unrestricted`, `relevance_least`). That is all the Lean shows, so the question is closed.
- *Ren's terms.* “Closure bounds change” stays Ren's phrase, kept with its source. The law keeps its name, enclosure bounds change, and the proof shows that running down is what bounds change ([laws-of-one-step](REC_laws-of-one-step.md)). 识 and 理 have their places in (2).
- *The commitments of the representation* (discrete steps, natural-number amounts, the census, decided equality and listing). They stay. Whether each should be refined or derived is the question of the scope of representation (chapter §8.5), decided by what the representation must express and by the theorems at finer grains; Ren's reservation of 11 October 2026 is provenance.

(6) **Not decided here.** Warrant (chapter §8.5): the necessity of the whole, the step of invariance, the warrant of the condition and of calling the generative space good. Empirical correspondence (§8.7) and further proofs (§8.2). OPENING's body and the generativity chain, which change only through proposals to Ren.

**Reasons.** Ren's answer asks for one account. Under his directive of 17 October his words are provenance, so a reading of one of his terms is decided like any reading: his texts are evidence of the term's sense, and the work is its warrant. Where readings conflicted, the revision keeps the one whose theorems and whose fit with the rest are stronger. Part D is decided by the same standard: a name by its exact meaning within the account, a structure by joining it, an ownership by the board's rules, and a review by stating exactly what it did.

**What would change it.** For each reading, what its decision lists. For the account, a reading it cannot place without contradiction, or a theorem showing one of its joins wrong. Ren can say otherwise of any of his terms; his words are then the provenance of a further revision, argued from the work.
"""
D45_EN = (D45_EN.replace('ANSWER', ANSWER).replace('(WORDS)', '(' + WORDS + ')').replace('(NAMING)', '(' + NAMING + ')')
          .replace('(REC_', '(' + REC).replace('(SRC_', '(' + SRC))

EDITS[EN] = [
    ("It is claimed on the work board as P110; the proofs pushed under the same delegation are P111 (`Becoming.Gain`) "
     "and P112 (`Becoming.Gluing`), whose results are in their records and the study.",
     "It is claimed on the work board as P110; the proofs pushed under the same delegation are P111 (`Becoming.Gain`) "
     "and P112 (`Becoming.Gluing`), whose results are in their records and the study.\n\n"
     "On 19 October 2026 Ren answered for the register as a whole, " + ANSWER + " ([words](" + WORDS + ")). Every "
     "reading here is decided by its place in one account, D45 (section 13); the revisions that account makes are "
     "dated below their decisions, and the index notes them on the row of D45."),
    ("| D44 | what taking all that is given excludes | adopted with exact scope: ending another serves taking all, not "
     "continuing; admission does not register it |",
     "| D44 | what taking all that is given excludes | adopted with exact scope: ending another serves taking all, not "
     "continuing; admission does not register it |\n"
     "| D45 | the readings in one account (19 October) | no reading ratified item by item, and none waiting on Ren; each "
     "decided by its place in one account, Part D within it; revises D3 (further generation, with D1), D19 (also the "
     "whole's knowing by its parts, never complete), D20 (situational awareness as 明 of one's own reach), D21 (the step "
     "of invariance a question of warrant), D26 (识, 理, seeking, 知足, 知止, 无明 and 明 as one structure), D37 and D39 "
     "(识 answered by option (b)) |"),
    ("**What would change it.** Ren restricting 生 to living formations or to one of the three scopes (the space "
     "narrows; the laws are unchanged).",
     "**What would change it.** Ren restricting 生 to living formations or to one of the three scopes (the space "
     "narrows; the laws are unchanged)." + D3_EN),
    ("**What would change it.** Ren's realizing being not a representation of a boundary but another relation.",
     "**What would change it.** Ren's realizing being not a representation of a boundary but another relation." + D19_EN),
    ("**What would change it.** Ren's middle level meaning what one depends on.",
     "**What would change it.** Ren's middle level meaning what one depends on." + D20_EN),
    ("**What would change it.** Ren's “belief” meaning something the presupposition does not state.",
     "**What would change it.** Ren's “belief” meaning something the presupposition does not state." + D21_EN),
    ("**What would change it.** Another reading of these terms by Ren; an actual learner whose learning these readings "
     "cannot represent.",
     "**What would change it.** Another reading of these terms by Ren; an actual learner whose learning these readings "
     "cannot represent." + D26_EN),
    ("This is the AI's correction, not Ren's decision; see O1, O2 and fix-list item 23 of the [eighteenth "
     "review](BECOMING-EIGHTEENTH-REVIEW.md).",
     "This is the AI's correction, not Ren's decision; see O1, O2 and fix-list item 23 of the [eighteenth "
     "review](BECOMING-EIGHTEENTH-REVIEW.md)." + D37_EN),
    ("The arguments are in the [decision brief](READINGS-PENDING-REN.md#a3-entangled-d39-4-and-the-scope-of-d39-3); "
     "Ren's answer ([words](../../../../sources/15-codex-theory-conversations/2026-10-18-central-readings-taken.md)) is "
     "its provenance, not its warrant. The original text above is kept.",
     "The arguments are in the [decision brief](READINGS-PENDING-REN.md#a3-entangled-d39-4-and-the-scope-of-d39-3); "
     "Ren's answer ([words](../../../../sources/15-codex-theory-conversations/2026-10-18-central-readings-taken.md)) is "
     "its provenance, not its warrant. The original text above is kept." + D39_EN),
    ("and the items waiting on him that are not readings ([Part D](READINGS-PENDING-REN.md#d-waiting-on-ren-not-readings)).",
     "and the items waiting on him that are not readings ([Part D](READINGS-PENDING-REN.md#d-waiting-on-ren-not-readings))."
     + D43_EN),
    ("- **Empirical correspondence and further proofs** stay in their classes in section 8.",
     "- **Empirical correspondence and further proofs** stay in their classes in section 8." + SEC10_EN),
]
APPEND = {EN: LINEAGE_EN + D45_EN}

# ------------------------------------------------------------------------------------------- DELEGATED-CHOICES.zh.md
ZH = RF + 'DELEGATED-CHOICES.zh.md'
MARK[ZH] = '**在一个说明中修订（2026-10-19，D45）。**'
REVZ = '\n\n**在一个说明中修订（2026-10-19，D45）。** '

D3_ZH = (REVZ +
    "第二个“生”读作进一步的生成：能形成者，连同进一步形成的条件与生成者；D1 的修订使后者成为生生的一部分（一个进程连同状态一起"
    "改变能形成者与形成的能力）。能形成者仍是比较所读的部分，所以以消耗为条件的生起仍经比较分类：有它的进程扩大能形成者处是生成"
    "的，缩小处是退化的。形成的能力，其中包括更新的能力与关系的丰富，尚未成为度量（理论 §8.2），所以不进入任何比较。"
    "**改变了什么。** 上面的决定只把第二个“生”读作能形成者，比 Ren 2026-10-18 所取的 D1 修订窄。**会改变它的。** 同上；一个"
    "形成能力的度量，使比较能读它。上面的原文保留。")

D19_ZH = (REVZ +
    "作为整体的判断保留，并与“在所知之中的知”的规律相接。Ren 的“understanding itself, and updates itself”经这些规律读出。"
    "整体对自身的知由它的部分作出，部分在所知者之中（理论第 3 节“在所识之中的识”）。没有框架以自己的构型实现关于其构型的每个"
    "断言（`Frame.self_incomplete`）；保留所知、并接着纳入其缺口的知，每一步都不完备，从不返回（`Diagonal.Unfolds.incomplete`、"
    "`Diagonal.Unfolds.never_returns`）。所以整体对自身的理解从不完备，它的更新不回到原处。这在实践中怎样发生仍开放。"
    "**改变了什么。** 上面的决定只读了边界。**会改变它的。** 同上；一个不由其部分作出的、整体对自身的知。上面的原文保留。")

D20_ZH = (REVZ +
    "一、二、四、五不变，用采用的词汇：说“识及”或“识”处，读作耦合入或耦合（[命名研究](" + NAMING + ")）。三与理论第 7 节相接："
    "情境的觉知是对自身所及的明，即知道自己的部分在其所耦合入者之外所到达的。反馈至多耦合入影响闭包"
    "（`Flow.Balances.uncoupled_beyond_influence`）。经水平的耦合使耦合闭包超出影响闭包，只经阈的耦合则不能"
    "（`Flow.withinCoupling_of_withinInfluence`、`Flow.withinCoupling_thresholdOnly`）。部分到达其所及闭包。所以情境的觉知要知道"
    "的，是 §7.2 第一条规律的缺口，即所及闭包减去耦合闭包；在它之外，经这个形成之耦合的选择什么也不分开"
    "（`Flow.unselected_beyond_coupling`）。**改变了什么。** 三原只说反馈不能给的；现在也说什么给它，缺口在哪里。"
    "**会改变它的。** 同上。上面的原文保留。")

D21_ZH = (REVZ +
    "一至三不变。四不是 Ren 的陈述。不变之步是否成立是根据的问题（理论 §6.11、§8.5）；Ren 持有它与否是陈述，按他 2026-10-17 的"
    "指示，那是来源，不是根据。这一步作为根据的问题保持开放，不是等待 Ren 的问题。**改变了什么。** 四原要 Ren 的陈述。"
    "上面的原文保留。")

D26_ZH = (REVZ +
    "这些读法不变，并与命名研究的“识”（选项 (b)，[研究](" + NAMING + ")）及理论第 7 节的读法合为一个结构，用采用的词汇。\n"
    "- **识与理。** 识是一个形成自己的进一步进程，即其选择、回应或寻求，经它自己的耦合所作的归并而行。理在形式上是世界经之同行的"
    "归并：关于何者无关的模型恰在那里正确（`goAlike_iff_lumped`）；经模型的选择，只在要紧者经其归并同行处，对要紧者正确"
    "（`Learning.selects_right_through`）。二者是一个结构的两面：进程所经的归并，以及世界是否经它同行。\n"
    "- **知足与知止。** 知足是在律所不变的状态被满足的目标（`Law.rests_iff`）。知止是在这一边界之内的目标，使追求因够而止，"
    "不因耗尽而止。所立者从某步起衰减时，上升因耗尽而止（`Flow.more_exhausted`）；一个群体所耦合入者的上升，由群体之外偿付"
    "（`Flow.Balances.rise_paid_from_beyond`）。目标从何而来，动力学不决定，所以作为选择的知止未被表示：规律说的是哪些目标能停息。\n"
    "- **无明。** 无明是使寻求锁定在不能于停息中满足之目标上的不见。这种不见是一个位置，是每个形成的位置：一个形成的耦合不分开"
    "者，经这些耦合的每个选择都同样选择（`Web.selects_alike_iff`）；它的耦合闭包之外，什么也不经这些耦合被分开"
    "（`Flow.unselected_beyond_coupling`）。这个位置不是无明。它是无明不从内部被纠正的缘故：被锁定之寻求的损失，只经寻求者所耦合"
    "入者到达它。不断变化的运行属于过程，不是无明（D41）。理论中开放的读法“无明是一个位置，不是缺陷”（§7.2）据此修订：这个位置"
    "不是缺陷，无明是它所留下的被锁定的寻求。\n"
    "- **明。** 明是及于支持所不标记者的耦合。它是一种关系，与接到一个选择上的耦合一样宽，随量度、模型与他者接入而变宽（理论 "
    "§7.3）。观察使耦合闭包超出只经支持所耦合入者（`Flow.withinCoupling_thresholdOnly`）；被观察之存量的每次抬高，每一步都经观察"
    "者的耦合造成差别（`Web.observed_raise_couples`）。\n\n"
    "**改变了什么。** 上面的决定逐项给出读法，明用的是已退役的“识”一词；§7 的读法原为开放。**会改变它的。** 同上；这一结构不能"
    "安放的、对其中某个用语的读法。上面的原文保留。")

D37_ZH = (REVZ +
    "关于识的一句由命名研究的选项 (b) 回答，Ren 于 2026-10-18 选了它：识只留给派生的结构，即一个形成自己的进一步进程经它自己的"
    "耦合所作的归并而行（[研究](" + NAMING + ")）。律的敏感是一种耦合，即律所经的最小的耦合（律读有限多个条件时，于双重否定下），"
    "不是识；识是经它而行的进程。用采用的词汇，（1）中的“识”读作耦合。其余连同上面的更正不变。上面的原文保留。")

D39_ZH = (REVZ +
    "（1）中关于识的一句如 D37 的修订回答：耦合强度度量一个形成耦合入一个水平有多强，是耦合的度量，不是识的。用采用的词汇，"
    "（1）中的“识的强弱”读作耦合入的强弱。其余如 2026-10-18 所修订，不变。上面的原文保留。")

D43_ZH = (
    "\n\n**2026-10-19 已回答。** Ren 对两者作答：" + ANSWER + "（[原话](" + WORDS + ")）。D45 记录这一回答：登记作为一个"
    "说明决定，D 部分在其中决定。")

SEC10_ZH = (
    "\n\n**在一个说明中（2026-10-19）。** D45 决定上面各项中属于读法、名称或归属的，其余照旧。已决定：停息的中文用语（停息）"
    "与其标题（停息定理）；“closure bounds change”保留为 Ren 的说法，规律保留其名，即围住约束变化；识（选项 (b)）与理（其形式"
    "读法）；不变之步，是根据的问题，所以不需要 Ren 对它的陈述；以及两项记录中审查的问题，由 R18 回答，并说明其性质。照旧："
    "OPENING 的正文与生成链，是 Ren 的文本，只经向他的提议而改；根据；表示的承诺，其范围是理论 §8.5 的问题；经验对应与进一步"
    "的证明。")

LINEAGE_ZH = (
    "\n- Ren 2026-10-19 对决定简报 C 与 D 部分的回答，" + ANSWER + "（[原话](" + WORDS + ")）：D45，以及同日注明的 D3、D19、"
    "D20、D21、D26、D37 与 D39 的修订。")

D45_ZH = """

<a id="13-一个说明--one-account"></a>
## 13. 一个说明

<a id="d45-一个说明中的读法--the-readings-in-one-account"></a>
### D45. 一个说明中的读法

所在：决定简报的 [C](READINGS-PENDING-REN.md#c-the-register-itself-d-f-review-item-50) 与 [D](READINGS-PENDING-REN.md#d-waiting-on-ren-not-readings) 部分与[一次过的读单](PHRASE-READINGS-PENDING-REN.md)；理论第 7 节、§8.3 与 §8.4；工作板的登记。

**Ren 的话。** 2026-10-19，回答 C 与 D 部分：ANSWER（[原话](WORDS)）。对这一回答的读法是 AI 的，与原话一并记录。

**决定。** （1）**登记（D-f）。** 本记录的读法都不逐项批准。每项读法依它在理论的一个说明中的位置而成立或修订；两项读法不相合处，由这个说明在其间决定。不再有读法等待 Ren，Ren 自己用语的读法也在内：他的文本是他的用语何义的证据，原样保存并注明出处；一项读法是否是工作所支持的最强读法，由工作论证。每项读法保留 AI 的标记。Ren 2026-10-16 的“agree with other readings”不读作批准；这一回答取代了那个问题。

（2）**这个说明。** 这些读法合为一个说明，分五环，每环立于其定理。
- *一个展开。* 律与历史是一个展开的两种读法，步的指标是关系项自身历程的读法（D23、D43）。其中动、静、停是跨步而行者、同时成立者与交换终止处（Ren，2026-10-12）。熵是守恒量中的记录（D29）；更细的区分本身是须有所给出的变化（D38）；历史之和沿一段历史复合、在备择之间相加（D30）；律所用的条件是它所说之部分的状态，这是方法上的类比（D27）。这些照原样相合。
- *生成。* 生生是生成者生成新的生成（D1），所以第二个“生”是进一步的生成（D3，已修订）。生成的与退化的是扩大的四种情形（D2），“更多”是这一方向（D15），体现是生的一种形式（D4），只从被支持者得到支持是 D1 的规律之一（D35）。不息是更新的复现，生生不息是生生在整体中继续，且仍有更多能形成（D5）。停息族是不息的另一面：在有普查、关系项都体现、平衡且耗散、从某步起每步被围住的世界中，世界归于停息不能被否证（`World.rests_unrefuted_enclosed`），所以生起不息需要开放（`World.arising_opens`），无尽的更多需要来自每个有界部分之外的流入（`Flow.new_beyond_every`）。（4）中的中文用语由此而来。
- *延续及其范围。* 想要是种子（D11）。延续条件读出 Ren 的句子，不被断言（D16）。不损是保留，其相变的边界是余裕（D13）；损在整体读出，较弱的版本在所在的系统之内，然后是自身（D14）。自身与整体是 D12 的两种吸引的力，“everything exists in between”是闭包的嵌套。一个形成在其供给闭包之内，供给闭包在影响闭包之内，影响闭包在耦合闭包之内（`Flow.withinCoupling_of_withinInfluence`）；所及闭包指向另一方向；全都在系统之内（`Flow.withinSystem_of_withinInfluence`、`Flow.withinSystem_of_withinReach`）。“the system that one is in”是所及闭包（D20），不是系统闭包；在一个共同条件成立处，系统闭包就是整体。
- *知。* 耦合是原初的：一个形成依存于一个条件处经阈耦合入它，观察它处经水平耦合入它。律的敏感（D37）与耦合强度（D39）度量耦合。识是派生的结构，即一个形成自己的进一步进程经它自己的耦合所作的归并而行（[命名研究](NAMING)，选项 (b)）；理在形式上是世界经之同行的归并（D26）。寻求在律所不变的状态满足其目标处停息。无明是锁定在不能停息之目标上的寻求；每个形成所由以选择的位置，是它不从内部被纠正的缘故；明是接到一个选择上、及于支持所不标记者的耦合（D26，已修订，连同 D41）。情境的觉知是对自身所及的明（D20，已修订）。整体对自身的实现，作为判断是以整体为边界，作为知是由其部分作出、从不完备的知（D19，已修订）。
- *对齐。* 理论第 7 节中至今标为开放的读法，是“知”一环用于选择：能力读作所及，缺口是所及闭包减去耦合闭包；明读作随量度、模型与他者接入而变宽的关系；为他者持明，即保持这三条路开放，纠正及于规则，每条规律的范围保持确切；为一切的对齐读作跨智能的汇合耦合，其动作只经把差别耦合为不同的成员回应它；有条件的方向中纠正的机会读作明的路。它们以第 7 节所说的范围采用。哪些回应纠正仍开放（§7.7）。

（3）**两项读法不相合处。** 各在其决定之下修订，原文保留。
- D3 只把第二个“生”读作能形成者；D1 的修订使它成为进一步的生成。
- D26 把无明读作被锁定的寻求，理论 §7.2 把它读作每个形成的位置。位置是无明的根据，不是无明。
- D37 与 D39 把识留为开放；命名研究的选项 (b) 回答它们。
- D21 的四要 Ren 对不变之步的陈述。这一步是根据的问题（理论 §8.5），陈述对它是来源。
- [where-a-level-couples](REC_where-a-level-couples.md) 的开放读法与 D43 关于[观察](REC_observation-is-a-route.md)的猜想，是一件事的两种说法。采用：`obs` 标出一个水平经水平耦合入一个形成之处，如依存标出它经阈耦合入之处，所以二者都是耦合；律的敏感是它所经的最小的耦合（D37）；耦合界定回应而不固定它（`ExchangeLaw.response_not_fixed_by_coupling`）。观察不是依存之外的第二种关系，若指 `obs` 能由依存推出，仍是一个猜想：`obs` 是给定的，`apart_only_downstream` 只表明观察在下游之内。

（4）**D 部分，在这个说明中决定。**
- *停息族。* 其中文用语是停息：从某步起，什么也不生起、不止息（`World.RestsFrom`），其定理说这不能被否证（`World.rests_unrefuted`、`World.comes_to_rest_unrefuted`、`World.rests_unrefuted_enclosed`）。非正式的标题是停息定理；英文“coming to rest”与“the rest theorem”保留。寻求与外推的停息也用停息。静与静止留给同时成立者。理由：这些定理关于不再复现的事件，那是停，不是同时成立者，那是静；息是生生不息所否定的，所以这一用语使这一族与之对读，如（2）所作。OPENING 的脚注已说出定理的强度（“that it never rests is refuted”）；其正文是 Ren 的文本，英文中“coming to rest”是确切的，所以 OPENING 不改。
- *`IdealWarrant`。* 与引入它的 `CompletionRole`、`HistoryIdeals` 合为核心中一族理想。在一个序上，理想的性质恰在 Scott 闭时可被有限否证，此时成员由一组基元素决定（原文的 `scottClosed_iff_admits_permitted`）。按工作板规则 8，核心的律、实例模块与记录取结构的名称，“warrant”“admits”“permitted”不沿用。它在运行上的情形是 `Becoming.Refutable`（`Becoming.Refutable.adheres_iff`、`Becoming.refutable_passes`），作为实例陈述。原文件保留其路径与字节。这是新的 Lean，即工作板子项 A4-L。
- *整合者。* 工作板规则 3 的退路就是安排，不是空缺。不指名任何会话；落地者按就绪的次序取队列；共享定义的改动，由定义它的模块的所有者在工作板上决定。
- *W-root。* “Necessity of the wisdom root”这一认领（Ren 2026-10-13 的目标，由一个 Codex 会话持有）自 10-13 起不活动，按工作板规则 4 已失效；它所整合的已在主线上。它开放的部分是理论 §8.1 的目标“核心作为智慧之根”，任何会话都可认领其中一步。整体演绎的目标，即 §8.1 的第一项，从来不属 W-root。工作板项 W 把导入树重新扎根于一个展开，这给那个目标以形式的起点，不是其证明。
- *R18。* 第十八次审查算作其记录所要求的审查：作者之外的审查者，把陈述对照 Lean、把读法对照其范围来读。构建 Lean 不是审查所加的，因为检查器的回执检查证明。凡引它处都说明其性质：AI 的审查，只读，未构建 Lean；不声称有人的审查。它审查过的记录如此说明，以代替“未经独立审查”；它未覆盖的记录保留那句话。这也回答两项记录留给 Ren 的问题（[seeking-boundary](REC_seeking-boundary.md)、[target-capture](REC_target-capture.md)）。

（5）**理论 §8.4 的其余问题。**
- *“生成”的几种意义。* 中文文本以三个词分开三种意义：展开指一个展开，形成指一个形成及其形成，生成指生成，如 Ren 的论中（“生生：生成者生成新的生成”），其反面是退化（D2）。理论的中文名“生成之论”中的“生成”是 becoming，这是这一哲学用语的通常译法。生成之论计入“all space, generative, degenerative”（Ren，2026-10-08，[原话](SRC_2026-10-08-theory-of-becoming-priority.md)），且“generative is a part of its manifold”（Ren，2026-10-09，[原话](SRC_2026-10-09-becoming-whole-generative-manifold.md)）。词汇表说明两种意义。
- *关于生之意义的句子。* 理论的状态说明已说：生之意义是限于活的断言的条件，条件给每个断言以意义，不带正的价（`g0_of_unrestricted`、`relevance_least`）。这就是 Lean 所表明的全部，所以这一问题关闭。
- *Ren 的用语。* “closure bounds change”保留为 Ren 的说法，连同其出处。规律保留其名，即围住约束变化；证明表明约束变化的是耗尽（[laws-of-one-step](REC_laws-of-one-step.md)）。识与理在（2）中有其位置。
- *表示的承诺*（离散的步、自然数的量、普查、判定的相等与列出）。照旧。每项应否细化或推出，是表示之范围的问题（理论 §8.5），由表示必须表达的与更细粒度上的定理决定；Ren 2026-10-11 的保留是来源。

（6）**这里不决定的。** 根据（理论 §8.5）：整体的必然性、不变之步、条件的根据与称生成的空间为好的根据。经验对应（§8.7）与进一步的证明（§8.2）。OPENING 的正文与生成链，只经向 Ren 的提议而改。

**理由。** Ren 的回答要一个说明。按他 2026-10-17 的指示，他的话是来源，所以他的用语的读法与任何读法一样决定：他的文本是用语之义的证据，工作是其根据。读法冲突处，修订保留定理更强、与其余更相合的那一个。D 部分以同一标准决定：名称依它在这个说明中的确切意义，结构以接入它，归属依工作板的规则，审查以确切说出它做了什么。

**会改变它的。** 对每项读法，其决定所列的。对这个说明，一项它不能无矛盾地安放的读法，或一条表明它的某个接合有误的定理。Ren 可以对他的任何用语另作说明；那时他的话是进一步修订的来源，由工作论证。
"""
D45_ZH = (D45_ZH.replace('ANSWER', ANSWER).replace('(WORDS)', '(' + WORDS + ')').replace('(NAMING)', '(' + NAMING + ')')
          .replace('(REC_', '(' + REC).replace('(SRC_', '(' + SRC))

EDITS[ZH] = [
    ("工作板上认领为 P110；同一交托之下推进的证明是 P111（`Becoming.Gain`）与 P112（`Becoming.Gluing`），结果在其记录与研究中。",
     "工作板上认领为 P110；同一交托之下推进的证明是 P111（`Becoming.Gain`）与 P112（`Becoming.Gluing`），结果在其记录与研究中。\n\n"
     "2026-10-19，Ren 对整个登记作答：" + ANSWER + "（[原话](" + WORDS + ")）。这里的每项读法依它在一个说明中的位置决定，"
     "即 D45（§13）；这个说明所作的修订注明日期，列在原决定之下，索引在 D45 一行注明。"),
    ("| D44 | 取尽所给所排除的 | 以确切范围采用：终结他者服务于取尽所给，而非延续；容纳不记下它 |",
     "| D44 | 取尽所给所排除的 | 以确切范围采用：终结他者服务于取尽所给，而非延续；容纳不记下它 |\n"
     "| D45 | 一个说明中的读法（10-19） | 读法都不逐项批准，也不再等待 Ren；每项依它在一个说明中的位置决定，D 部分在其中决定；"
     "修订 D3（进一步的生成，与 D1 一致）、D19（也是由其部分作出的知，从不完备）、D20（情境的觉知读作对自身所及的明）、D21（不变之步"
     "是根据的问题）、D26（识、理、寻求、知足、知止、无明与明是一个结构）、D37 与 D39（识由选项 (b) 回答） |"),
    ("**会改变它的。** Ren 把“生”限于活的形成或三种范围之一（空间随之缩小，规律不变）。",
     "**会改变它的。** Ren 把“生”限于活的形成或三种范围之一（空间随之缩小，规律不变）。" + D3_ZH),
    ("**会改变它的。** Ren 所说的实现不是一个边界的表示，而是另一种关系。",
     "**会改变它的。** Ren 所说的实现不是一个边界的表示，而是另一种关系。" + D19_ZH),
    ("**会改变它的。** Ren 的中间层次是指所依存的。",
     "**会改变它的。** Ren 的中间层次是指所依存的。" + D20_ZH),
    ("**会改变它的。** Ren 的“belief”所指不是预设所陈述的。",
     "**会改变它的。** Ren 的“belief”所指不是预设所陈述的。" + D21_ZH),
    ("**会改变它的。** Ren 对这些用语的另一读法；一个实际的学习者，其学习不能由这些读法表示。",
     "**会改变它的。** Ren 对这些用语的另一读法；一个实际的学习者，其学习不能由这些读法表示。" + D26_ZH),
    ("这是 AI 的更正，不是 Ren 的决定；见[第十八次审查](BECOMING-EIGHTEENTH-REVIEW.md)的 O1、O2 与修正清单第 23 项。",
     "这是 AI 的更正，不是 Ren 的决定；见[第十八次审查](BECOMING-EIGHTEENTH-REVIEW.md)的 O1、O2 与修正清单第 23 项。"
     + D37_ZH),
    ("论证在[决定简报](READINGS-PENDING-REN.md#a3-entangled-d39-4-and-the-scope-of-d39-3)中；Ren 的回答（[原话]"
     "(../../../../sources/15-codex-theory-conversations/2026-10-18-central-readings-taken.md)）是其来源，不是其根据。"
     "上面的原文保留。",
     "论证在[决定简报](READINGS-PENDING-REN.md#a3-entangled-d39-4-and-the-scope-of-d39-3)中；Ren 的回答（[原话]"
     "(../../../../sources/15-codex-theory-conversations/2026-10-18-central-readings-taken.md)）是其来源，不是其根据。"
     "上面的原文保留。" + D39_ZH),
    ("以及等待他的、不是读法的各项（[D 部分](READINGS-PENDING-REN.md#d-waiting-on-ren-not-readings)）。",
     "以及等待他的、不是读法的各项（[D 部分](READINGS-PENDING-REN.md#d-waiting-on-ren-not-readings)）。" + D43_ZH),
    ("- **经验对应与进一步的证明** 留在第 8 节各自的类中。",
     "- **经验对应与进一步的证明** 留在第 8 节各自的类中。" + SEC10_ZH),
]
APPEND[ZH] = LINEAGE_ZH + D45_ZH

# ------------------------------------------------------------------------------------------- the brief and the sheet
D45_LINK = "DELEGATED-CHOICES.md#d45-一个说明中的读法--the-readings-in-one-account"
BR = RF + BRIEF
MARK[BR] = '**Ren\'s answer (19 October 2026).**'
EDITS[BR] = [
    ("The generativity chain's change (item 19) was applied through the chain's maintenance record (board item A2).",
     "The generativity chain's change (item 19) was applied through the chain's maintenance record (board item A2).\n\n"
     "**Ren's answer (19 October 2026).** To Parts C and D: " + ANSWER + " ([words](" + WORDS + ")). Board item A4 "
     "records it as decision [D45](" + D45_LINK + "): no reading is ratified item by item, and none waits on Ren; each "
     "is decided by its place in one account, and Part D within it. The chapter and the records follow through the "
     "landing queue."),
    ("left unnamed: D3, D4, D12, D26, D27, D29 and D30.",
     "left unnamed: D3, D4, D12, D26, D27, D29 and D30.\n\n"
     "**Answered on 19 October 2026** ([D45](" + D45_LINK + ")): not item by item, but as one account. The sheet's "
     "items 2 (D3), 10 (D19), 11 (D20), 12 (D21 (4)), 14 (D26) and 19 (D37, D39) are revised there; the others stand "
     "as written."),
    ("- Whether R18, an AI read-only review, counts as the review asked for (B6).",
     "- Whether R18, an AI read-only review, counts as the review asked for (B6).\n\n"
     "**Decided on 19 October 2026** ([D45](" + D45_LINK + "), item (4)). The rest family's Chinese term is 停息, with "
     "the heading 停息定理, and OPENING does not change. `IdealWarrant` joins the core with `CompletionRole` and "
     "`HistoryIdeals` as one family of ideals under structural names (board sub-item A4-L). Rule 3's fallback is the "
     "arrangement for integrating, with no session named. W-root's claim has lapsed under rule 4, and its target stays "
     "open in chapter §8.1. R18 counts as the review asked for, stated as an AI review, read-only, that built no Lean."),
]
SH = RF + SHEET
MARK[SH] = '**Ren\'s answer (19 October 2026).**'
EDITS[SH] = [
    ("Ren's words are quoted in their original language and spelling.",
     "Ren's words are quoted in their original language and spelling.\n\n"
     "**Ren's answer (19 October 2026).** " + ANSWER + " ([words](" + WORDS + ")). The sheet is answered as a whole, "
     "not box by box: decision [D45](" + D45_LINK + ") places every item in one account. Item 0 is answered: no item is "
     "ratified one by one, and none waits on Ren. Items 2 (D3), 10 (D19), 11 (D20), 12 (the step of invariance in "
     "D21), 14 (D26) and 19 (D37, D39) are revised there; the others stand as written, each with its AI label. The "
     "boxes below are kept as they were."),
]


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    for path, edits in EDITS.items():
        full = os.path.join(root, path)
        text = open(full, encoding='utf-8').read()
        if MARK[path] in text:
            print('already edited', path)
            continue
        for old, new in edits:
            n = text.count(old)
            if n != 1:
                sys.exit(f'{path}: expected one match, found {n}: {old[:100]!r}')
            text = text.replace(old, new)
        if path in APPEND:
            text = text.rstrip('\n') + APPEND[path].rstrip('\n') + '\n'
        open(full, 'w', encoding='utf-8').write(text)
        print('edited', path, len(edits), 'edits and the appended section')


if __name__ == '__main__':
    main()
