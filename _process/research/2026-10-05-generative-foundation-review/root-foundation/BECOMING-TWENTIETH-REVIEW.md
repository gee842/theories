<a id="twentieth-review--第二十次审查"></a>
# Twentieth review: the theory as one whole — completion, unification, coherence, elegance, redundancy

20 October 2026. An AI review, read-only. It built no Lean, ran no checker and changed no record, chapter, OPENING, README, GOALS, generated page or Lean file. It added only this file, its folder [`twentieth-review/`](twentieth-review/) and its row on the work board (item R24). Seven lens reviews were run in parallel, each with the same [brief](twentieth-review/BRIEF.md), and each lens report is kept in full:

| Lens | Report | Question |
|---|---|---|
| A | [foundations](twentieth-review/A-FOUNDATIONS.md) | Is there one base? Parallel notions, layers, shared definitions |
| B | [Lean redundancy](twentieth-review/B-LEAN-REDUNDANCY.md) | Duplicate statements and definitions, restatement layers, witnesses, sizes |
| C | [chapter](twentieth-review/C-CHAPTER.md) | Is the canonical chapter one argument? Repetition, §6, density |
| D | [completion](twentieth-review/D-COMPLETION.md) | What "complete" means, coverage, the open programme, modelling choices, the ethics |
| E | [corpus](twentieth-review/E-CORPUS.md) | Live documents, glossaries, records, the study, leftovers |
| F | [vocabulary](twentieth-review/F-VOCABULARY.md) | One notion, one name; nondual vocabulary; the ethics as one account |
| G | [frontier](twentieth-review/G-FRONTIER.md) | Do the modules landed 18–19 October join the theory or stand beside it? |

This file is the synthesis. It groups the lens findings into eight themes, says which claims were re-checked against the source, and gives one ordered programme. Finding IDs (A1, B7, …) point into the lens reports, where each has its evidence, proposal and cost.

**Base.** main at `121ff8042` (W2 landed), with R21 (`80d2b6d74`) and R22 (`05f075f77`) landing during the review; both changed docstrings, docs and names only, and the connectivity measure on R22's tree is unchanged (495 apart of 11,647). Line numbers in the lens reports are of `121ff8042` and may shift by a few. The lens reports use the module names before R22: `Becoming.Widening` is now `Becoming.LoopReturn`, and `Becoming.Passing` is now `Becoming.PatternPassing`.

**Difference from the nineteenth review.** The nineteenth compared prose with Lean sentence by sentence; R21 and R22 applied its fixes. This review is one level up: whether the theory is one theory. Sentence-level errors appear here only where they matter for the whole, and none of the nineteenth's findings is repeated.

**Re-checked in the source by the synthesis** (beyond the lenses' own checks): `structure Web` (World.lean:35) has exactly the fields of `Dependence Nat F C` (Dependence.lean:165); `World.run_world` is `rfl` (Runs.lean:120); `Interdependence` imports `Significance` and holds 5 `Unrestricted` hypotheses, `Feedback` 8, while `Testing`, `Selection`, `Learning` and `Hexagrams` hold none; `Image` (Mechanism.lean:89) and `Readout.image` (Readout.lean:129) have the same body; `falls_not_recurring` (Renewal.lean:58) and `whole_falls_not_recurring` (LeastLoss.lean:421) have the same statement; `Web.paths_comparison_widens` (ValuationFrames.lean) holds for every `living`, and its own docstring says the ranking is supplied by the reading of "better"; `rising_recurs` (Change.lean:302) sums falls of at least one; the `Becoming.Generation` header reads "generation" as arising; §7.5's record is `alignment-direction-g0-j`; the chapter is 738,669 bytes, about 99,000 words, with about 2,300 distinct backticked names.

---

<a id="summary--摘要"></a>
## Summary

**The verdict.** The theory has, in substance, the shape of one elegant theory. In presentation and in its formal architecture it is not yet one. Its best parts are already unifying: law and history as two readings of one unfolding, recurrence (lossless ⇔ returns), five of the eight World premises as readings of one exchange and three as states of the law, the margin law and widening with no axiom, the decomposition of the condition, the selection line and §4's constraint table. But the last two days of work, about 4,300 core theorems and 50 records, added mostly beside the old rather than under it, and the presentation records the order of the work rather than the order of the argument.

Eight themes, in order of what they cost the whole:

1. **Two bases, not one** (major; A1, A2, A3, B7, G1, D4). The process family (`Process`/`Trace`/`Run`) and the world family (`World`/`Web`/`Flow`) are defined independently and meet only through 163 correspondence statements; the measure's `families_reach_each_other` is false in every direction. Yet the identification is already definitional in one direction (a `World` is a run of the law it shows, by `rfl`), and the world-side record `Web F C` is field for field `Dependence Nat F C`. About 55 companion modules (`…Runs`, `…Worlds`, `…Webs`, `…Traces`, `…Frames`; ≈11k lines) exist only to carry laws across the gap. The README names the relation in the opposite direction ("the process enters as a reading of the World"), and the prose names three different roots. Making one base by definition is also the formal content of the necessity target that §8.1 itself names.
2. **Generalizations land beside, not below** (major; G2, B1, B9). Each generalization lands as a new leaf plus a theorem "the old law is a case of this", while the old proof stays: Ideals beside Horizon, LeastLoss beside the rest family, CensusCounts beside Counting, SelectionPool beside Selection, the `Law.*` vocabulary beside `Branching.*`. No module that existed before 17 October imports any of the 47 new-result modules. The theory grows where it should compress.
3. **The ethics is one account written as five rounds** (major; F4, F5, F6, D2, D3, D8, C3). Underneath there are two premises: a scope premise (the continuation condition, which is the self's presupposition plus the step of invariance) and an order premise (C: widening is better). The text, and AGENTS.md, say "what ranks lies in C and in the step of invariance"; by the chapter's own result the condition orders nothing, so the step of invariance fixes whose losses count, not the order. The evaluative object `living` plays no part in any ranking (`paths_comparison_widens` holds for every `living`), and the one theorem relating undermining to widening is a divergence (`not_undermining_yet_loses`). Standpoints are a separate supplied type. §6 has fifteen subsections ordered by the dates of the rounds, with the no-axiom part (§6.13) after the conditional part.
4. **One notion, several names; one name, several notions** (major; B2, F1, F3, F9, A10, B13, G9). `Returns` has four definitions, rest and settling seven for at least four notions, `Lossless` and `Merges` three each; "generation" names arising in 31 declarations and a module, against the theory's own rule; the Lean `Unfolding` is a legacy static record, not the one unfolding; `G0`, `positive`, `SelfGood` are live. In the prose, "whole", "condition", "reading", "law" and "selection" each carry three to eight senses, and the headline claims are stated in them. About ten namespace collisions remain beyond the nineteenth review's three.
5. **"Complete" has no checkable meaning** (major; D1, D4, D10, D11). Of "unified, complete, enclosed, zero-axiom" only zero-axiom is checked. "Enclosed" is defined nowhere. "Complete" points to four criteria of 9 October, never audited since, one of which names a "Ren's choice" class that D45 abolished; item 11 and "What this completeness is" still claim it. Three of the five §8.1 targets restate target 1 or §8.5.
6. **Modelling choices do work under "no premise"** (moderate; D5, D6). `rising_recurs`, the §2 principle `falls_not_recurring` and "joint excess cannot outlast what was held" are facts about natural-number amounts, headlined as laws of every unfolding; the chapter's own `Halving` refutes the first two over dense amounts. The generative space counts only formations of a type given in advance, so the 生生 it is meant to compare (generators of further forming) can exceed what it registers.
7. **The chapter is a register, not an argument** (major; C1, C2, C4, C5, E1, G14). 99,000 words, about 2,300 distinct Lean names (1,698 used once), 59% of lines carrying Lean names; the theory stated five or six times (status, "stated in full", §0, "stated whole", §9, glossary, OPENING's footnotes); the foundation ("the whole and its parts") at the end of §1, after six hexagram paragraphs; about 29% of the bytes process history or duplication, including a 17.8 kB connectivity log in one §8.2 cell. The chapter grew 47% in two days.
8. **The corpus outweighs the theory** (moderate; E2, E3, E4, E8, E10, E14). Generated views 9.0 MB and record pages 6.7 MB against 3.2 MB of English chapters; 84% of record history entries are rebind and repoint notes; no record is ever marked superseded, and 53 still bind proofs to retired periphery modules; about 25 of the study's 135 top-level entries are live; 34 worktrees hold 121 GB, 26 of them at heads already on main.

**Statement-level redundancy is low** (B): about 4% of theorems (450–500 of 11,678) could go with no statement lost. The waste is in definitions, modules and placement, not in duplicated mathematics. That makes the consolidation below mostly mechanical.

**The two moves that would most advance the theory as a whole** (argued in D §2c and A §3): **(i)** one base by definition (theme 1), restating the spine's laws over the law of exchange; **(ii)** one evaluative chain (theme 3): join what can form, its significance and its order, so that a single line runs from the unfolding through the condition and C to the alignment direction, which today ends in a 7 October periphery module whose premise is still named "G0" (D7).

---

<a id="1-two-bases--两个基底"></a>
## 1. Two bases, not one

**What is the case** (A1, A2, verified). `Becoming.World` imports nothing; `Becoming.Frame` imports only the foundation `GenerativeCore`. Neither family is defined from the other. The exact relation is asymmetric: World → Run is definitional (`World.run_world`, `Run.world_webAt`, `Run.world_move`, `World.web_along`, all `rfl`), so a `World` is the curried form of a history of snapshots and exchanges; Run → World is lossy (`Frame.world` keeps activity and drops levels and flows). The five-field standing record exists five times (`RelationalRenewal.Unfolding`, `Conditions`, `Dependence`, `Web`, `WebAt`) and the exchange record twice (`Flow`, `Exchange`).

**What the documents say.** README and `Becoming.lean`: the base is `World`, and the process "enters as a reading of it". World.lean's own doc: `World` "is not the starting point". Runs.lean: "the one root is the run". Chapter §1: `World` is "the reading where the readings glue". The study leaves "whether one is defined from the other" waiting for Ren, which since D45 no one owns.

**What it costs.** The W2 rule (no module free of the labelled process imports the frame) is right under two bases, and it produces the companion layer (A3, B7: 53–59 modules, ≈11k lines, 181 one-line theorems; `PresentationFrames` says of itself "none is a further result"). The frontier deepened the split: 30 new-result modules speak only the process vocabulary, 17 only the world vocabulary, 10 of their 2,287 theorems both (G1). The collective line is cut down the middle: Withholding, Tolerance, LoopReturn (the former `Widening`, renamed by R22), Pace, RuleCapture and SharedCodes run on private configuration types wrapped in `Law.run`, with no `Web`/`Flow`/`World` symbol at all, while Selection, Regulation, PatternPassing (the former `Passing`) and MutualDependence run on flows and webs (G3, G7). The connectivity measure counts the first group as "on the base", so "apart = 0" there overstates integration.

**The unified form** (A §3, G1, judgment argued in A). One root, the run (a history with its moves; the law read off it by `Shown`), because that direction is already exact and `rfl` and because it is what "law read off the unfolding" says; one indexed standing record `Dependence S F C` with `Web F C := Dependence Nat F C`; one exchange record; `World` as a history of snapshot and exchange, its balance "the history lies within `exchangeAt`" (already `World.balanced_iff_law`). Then a World law is a run law by instance, the 163-statement meeting zone becomes most of the spine, and the companion modules fold back. The stronger form, which is the formal part of the necessity target (§8.1 row 1, D4), follows: the spine's laws stated over every law of exchange (`ExchangeLaw.worldRun` already sends a law to a run; `ExchangePremises` already reads five premises off the exchange and shows three to be states of the law). Interleavings, which derives the step index from the relata's own courses, should then construct the `World` (G10), so that "one shared index" leaves the premise card as a reading.

**Feasibility not yet checked.** That `abbrev Web := Dependence Nat …` keeps `w.web.level` and the `Web.*` dot lemmas working, and that the `World` redefinition breaks no proof, are inferences from the `rfl` identities; a scratch build settles them before any claim.

---

<a id="2-generalizations-beside--概括落在旁边"></a>
## 2. Generalizations land beside, not below

**What is the case** (G2, B1, B9, verified for the pairs named). LeastLoss proves six spine rest laws "again from the least-loss law, their statements unchanged" (`whole_falls_not_recurring` = `falls_not_recurring`, …). HistoryIdeals adds "Horizon's `Refutable.not_not` is the case of runs of `Ideals.RefutableBy.not_not`" beside Horizon's own proof. CensusCounts "states the same laws with neither" decidability, and Counting keeps its own proofs. SelectionPool re-derives Selection's case "with its own hypotheses". `Law.Lossless/Merges/Returns/Reachable/KeepsPossibilities` (for `next : S → S`) restate `Branching.*` at `Law.process next`, joined by ten `law_*_iff` bridges. In all, about 93 strict duplicate groups and 279 pure forwarders (B9, B10).

**Why it matters for elegance.** A theory is unified when the general law is the reason for the special one. Here the general law is a second reason beside the first, so every generalization raises the count of theorems and records and leaves the reader two paths to one fact. The apart register already labels 16 roots "restates".

**The unified form.** Invert where the general module is pure and low: `Ideals` imports nothing, so Horizon imports it and derives its refutation laws; `Amounts` moves below `Flow`/`World` and the rest family is proved once as its whole-number instance; the decided counting laws become corollaries of the counted ones (counts exist where decided); `Law.*` become abbreviations at `Law.process`, the bridges `Iff.rfl`. **A board rule** would turn this into the default: *a module that generalizes an existing law lands below it and proves it, or proves it as a corollary; it does not land beside it* (G §4, recommendation 7). The current claim R23 (`Becoming.ListingRefutations`, `_listing` corollaries with no `Distinct`) is a case in point: under the rule its laws would become the proofs of the existing ones rather than a new module beside them; its owner decides.

---

<a id="3-the-ethics-as-one-account--伦理作为一个说明"></a>
## 3. The ethics: one account written as five rounds

**The structure underneath** (F §2c, verified against the definitions). With no premise: an order on what can form (`Web.Includes` ⊂ `Widens`, `Keeps`, `Mixed`, narrows), the margin law and "whole first". A free parameter `sig`, which the dynamics leave undetermined (`Web.significance_undetermined`). One **scope premise**: the continuation condition `Unrestricted sig`, which is exactly the self's presupposition plus the step of invariance (`unrestricted_iff_presupposed_along`); under it retaining and adding are including and exceeding, and widening is retaining and adding (`Web.widens_iff_retains_adds`). One **order premise**: C, read as "widening is better" (`Comparison` with `Better := Widens`; `paths_comparison_widens` is definitional and says so). Living significance, the seed and the neutralities are corollaries under the scope premise and characterizations of rival boundaries without it. A, L and J1–J4 are the practical premises.

**Where the text blurs it.**
- *Scope and order conflated* (F5). The status block, §6.15 and AGENTS.md say "what ranks lies in C's calling widening better **and in the step of invariance**"; §6.13 and §8.5 say the content of "calling the generative space good" **is** the step of invariance. But the condition, which the step of invariance completes, "by itself orders nothing" (chapter, verified). The step of invariance decides whose losses count; only C orders. And "C follows from the condition" (premise card E, §6.8) holds only by reading "better" as retaining and adding, which places the ranking weight in the gloss of a word, against AGENTS.md's "hide no weight … in a definition".
- *Which condition the ethics rests on* (D8). "Conditional on the continuation condition" names the premise that does the least ranking work; the ranking rests on C and its open warrant. Every summary of the ethics (chapter target 2, README note, AGENTS.md) should name both premises.
- *Live contradictions of D1's revision* (F6): §8.3's first bullet ("living significance and C share this reading" of 生生), target 2 ("through living significance"), §7.5 ("one evaluation … by living significance").
- *Order of presentation* (F4, C3): §6.1–§6.15 follow the rounds (G0, wanting, the one axiom, the fold), six anchors still carry `g0`/`p39`–`p44`, "follows immediately, by instantiation" is said about 13 times, and the clean no-axiom part (§6.13) comes after the conditional part.

**Where the formal account is incomplete.**
- *The evaluative object and the order never meet* (D2, F13). `living` (active and not undermining) enters no ranking; no theorem relates `Widens` to renewing, consuming, undermining or arising, and the one that relates undermining to narrowing is a counterexample: a living event that narrows (`not_undermining_yet_loses`). D2's reading "generative at the level of formations = renewing" has no theorem behind it.
- *Evaluation does not differentiate within the unfolding* (D3, F7). Standpoints are a separate type `Pos`, regions `own` and significance `sig` are supplied (Metaethics.lean says so), and the coupling laws of §7 read a supplied, step-independent `obs`. "How a center forms" is open in four places of §8.
- *The direction is off the spine* (D7). §7.5's claim is bound to a 7 October periphery module of ten theorems over four plans, carrying `propext`, whose stated premise is "G0".

**The unified form.** Present the ethics in logical order in five sections (C3, F4): significance undetermined; the order of what can form, with no premise; how far it reaches, with no premise; the scope premise and what it yields (living significance once, as a corollary, with its characterization and rivals); the order premise C with A, L, J and what stays open. Say "instantiation" once. Then, as Lean work: either prove under named premises how a part's run class relates to its widening (with `not_undermining_yet_loses` as the boundary witness) or restate living significance over admission, so that the condition, significance and C read one object (D2); state the core laws with `Pos := F` and `own` as a closure, leaving `sig` the only supplied evaluative parameter, which the condition fills (D3); and state the direction as a core theorem on a world's moves (`FrontierWorlds`), under C read as widening and J1–J4, keeping the periphery module as an instance (D7).

---

<a id="4-names--命名"></a>
## 4. One notion, one name

**Lean** (B2, F3, F9, A10, B13, G9). The notions with several definitions: `Returns` (a configuration had again; a level met again; a coupling chain closing), `Settles`/`Rests`/`RestsFrom` (no arising or ceasing; a state fixed with its target met; a prediction right from some step; a pause), `Lossless` (injective steps; no amount lost), `Merges`, `Keeps` (7), `Closed` (5), "history" (4 definitions), "course" (7). Names that state a wrong meaning: the `generation_*` family and `Becoming.Generation` (arising), `Unfolding` (a static-dependence record), `Becoming.Coupling` (where a move is formed, not couples-into), `G0`, `positive`, `SecuresPositiveGround`, `SelfGood` (×2), `DependentSelection` (a choice principle), `free_rider_loses`. Eleven namespaces hold unrelated witnesses (`Crossing`, `Cycle`, `Loop`, `Copying`, `Settling`, `Parting`, `Fork`, `Circulation`, `Halving`). Lens B also counts a third `Coarse` in Branching; on reading, it reopens Mechanism's witness, as R22 decided, so that item is withdrawn.

**Prose** (F1, F2, F8, F10, F14). "Whole" is the space of worlds, the formations of one world and the theory's content; the necessity target and the ethics use it at different levels. "Condition" is the relatum role, the continuation condition, a law's local hypotheses and a status. "Reading" has eight senses, including the label "[AI reading]". "Law" is both a dynamics and a theorem. The 202-row glossary has no row for unfolding, relatum, formation, condition-as-role, level, support, standpoint, `living`, coupling (D45's primitive), generation, loss, law, history or pool. Standpoint/center/position/evaluator are one notion with four names. Contest vocabulary ("winning by consumption", "the free rider", "rules the winners write", "the patient's side") fails D54's own relational test. 停息 and 静 conflict between D45(4) and D49(4).

**The unified form.** A core vocabulary of about 36 terms, each with one definition, one Lean anchor and its Chinese term (F §2f), the glossary split into that vocabulary and an index of formal terms, and one statement-preserving rename table for the Lean (N5's precedent: 175 declarations in one checker run; here about 160). The renames meet AGENTS.md's bar: each name states a wrong meaning or collides. Prevalence of social or financial names in the Lean is low (≈0.8% of declaration names), so this is a cleanup, not a re-founding. Record IDs with retired labels (20) keep stable redirects (E4, F17).

---

<a id="5-completion--完整"></a>
## 5. What "complete" means

Today only zero-axiom has a check. D1 proposes a criterion a script can run, offered here as the AI's proposal (the wording of the targets stays a goal scope):

| | Criterion | Checkable by |
|---|---|---|
| K1 | **Coverage**: one row per phase (generation, maintenance, transformation, degeneration, dissolution), per differentiation (actor, patient, knowing, evaluation, capacity, responsibility) and per domain (life, evolution, learning, collective, significance, alignment), each naming its central core declarations and status | a `COVERAGE.json` the checker reads |
| K2 | **Unity**: every central declaration in the main component and stated on one base; `families_reach_each_other` true | the connectivity measure |
| K3 | **Premises**: each premise of a central law has witnesses meeting and failing it | as `World.contingent` |
| K4 | **Representation**: each central law tagged with the modelling choices it uses (ℕ amounts, discrete steps, fixed type, decidedness, …); each ℕ-tagged law has a dense-amount form or a counterexample, as LeastLoss has | a record field |
| K5 | **Enclosure**: the free parameters of central laws (`sig`, `Pos`/`own`, `obs`, naming, the rest relatum) listed; "enclosed" = only named conditions are supplied | statement scan |
| K6 | **Ethics chain**: one core chain from the evaluation row to the conclusions §7.5 uses, every normative hypothesis named | the checker |
| K7 | **Open register**: each open item in exactly one class, not done, not duplicated | `research-check` |

The coverage matrix (D §2b) finds: the five phases, actor, knowing, learning and collective dynamics proved on the spine; patient and evolution partly; evaluation's formation, capacity, responsibility, life and the alignment direction in prose or open. The open programme (§8) is about 6,400 words with duplicates (center formation ×3, the definitional join ×2, real amounts ×3) and stale rows (the Seeking row answered by RuleCapture; a header dated 17 October). D9 ranks about twelve items as significant; the rest belong to records' `next_delta`.

---

<a id="6-modelling-choices--建模选择"></a>
## 6. Modelling choices doing work under "no premise"

The pure core's empty axiom reports are real; the assumptions lie in the representation, as AGENTS.md says. The chapter discloses this for the rest family (with `Amounts.rests` and `Halving` as the model to follow), feeding from beyond and runaway, but not for three statements headlined as laws of every unfolding or as a principle: `rising_recurs` ("finitely many conditions that keep falling keep rising"), `falls_not_recurring` (§2's headline), and `Flow.excess_bounded` ("joint excess cannot outlast what was held") (D5). Each sums falls of at least one unit. The fix is the one LeastLoss already made: state the ℕ case as the instance of the well-founded or least-loss form, and tag each central law with the choices it uses (K4). Separately, `Widens` counts admissions of members of a fixed type `F`, so a course that creates a new kind of formation or requirement widens nothing; the theory's reading of 生生 as creating "generators of further forming" exceeds it. `Flow.GrownBy` (Cuts) is a structure that could carry widening over a grown world (D6).

---

<a id="7-the-chapter--正文"></a>
## 7. The chapter: a register, not an argument

C maps the section dependencies. §1–§3 cite study sections far more than earlier chapter sections; §5 depends forward on §6.12; §6.7 holds dynamics laws that need no condition; the coupling and response line that §3, §4 and §7 rest on sits in the middle of §2; §7.1–§7.4 re-cite §3 (§7.2: 29 of 29 names already earlier). Ten central results are identified (C §2.5); three of them (the margin law and widening, joint excess ending the renewers, growth exponential iff a loop is upstream) are not in front. "The deepest part" puts the calibrations of the logic at the summit, against AGENTS.md's rule that a calibration of the logic alone is a lemma of the law that needs it (C2a). "The theory stated whole" still quotes the 17 October measure (195 of 7,698 apart; now 495 of 11,647) and covers none of the frontier of §2–§4.

**The unified form** (C2, C5): a preface of one page (one sentence; four kinds of standing; where the ethics lies); §0 as the only home of the representation and the premises; the body said once, in the order: one unfolding → premises carve parts → organization → coupling and response → knowing → seeking and selection → significance without condition → the condition → alignment → open; one closing theorem map that replaces both "stated in full" and "stated whole"; a glossary of definitions only; process history (receipts, dates, "is now / until the F3 sweep", narrations of what Ren asked) moved to records and history. Estimated at about a third of the present length with no result lost. It is best written **after** themes 1–4 settle the structure it presents, so it is written once (programme step 5). The Chinese edition lags structurally (old §8, a dangling §8.6 reference, catalogue inline; C6). OPENING's footnotes are AI-written and restate the chapter a sixth time; they may point to the theorem map. Its body, Ren's voice, links to retired anchors that must stay as aliases (flag only).

---

<a id="8-corpus-and-frontier--文档与前沿"></a>
## 8. The corpus, the records and the frontier

**Corpus** (E). The whole is stated outside the chapter again by MAP, README, BECOMING-FOUNDATION, PHILOSOPHICAL-ACCOUNT and MATHEMATICAL-CORE. Four catalogues describe the same ~297 modules (Lean README, REFERENCE's module table, LEAN-INDEX, LEAN-DECLARATIONS), and the layer tables disagree with the import graph (A5: five upward edges; 273 and 200 of 296 modules covered). ARGUMENTS ×2, SESSION-RESULTS and THEORY-MAP are 8 October snapshots rendered as live pages (G0 62 times). About fourteen chapters are superseded or cited by no record (E14). Six chapters cover the Chinese tradition (E15). Seven unmaintained Chinese editions use G0, one titled as if G0 were an adopted axiom (E5).

**Records** (E3, E7, E8). 84% of 11,541 history entries are rebind, repoint or receipt notes (RESULT-WORKFLOW asks for one note per round). Law families are split by landing (counting and census across ≥ 11 records; settling ⇔ LPO three times; two one-step records with contradictory titles). Supersession is never used: 0 of 279 records are superseded, 53 bind proofs to retired periphery modules, and one record's canonical source is the retired bridge.

**The study and the tree** (E10, E12). About 25 of 135 top-level study entries are live; executed plans, answered briefs, superseded reviews and 64 landed-item kits stay beside them; the study log is 1.4 MB and rehashed by 213 records at every landing. 34 worktrees use 121 GB: 26 at heads already on main, 8 with commits not on main that need a `refs/salvage/…` ref before cleanup.

**The frontier** (G). Since 17 October: 121 core modules (4,317 theorems), of which 67 ports, 7 base re-readings and 47 new results; records 229 → 279; the chapter +47%; apart theorems 180 → 495, 376 of them in modules added since 17 October. The infrastructure converged (no bridge, re-rooting, base re-readings, ExchangePremises, Cuts, `Commuting`); the theory expanded at the leaves. Specific parallel carriers: one criterion in three modules (LawAlongRun, LawThroughCoupling, LawThroughChangingCoupling; G4), two theories of learning in the limit (Learnable/Unrolling/Labels vs LimitVerification; G5), two loop theories (LoopReturn, the former `Widening`, vs Loops/Rejoining; G6), collective formations on private types (G7), two counting families (G8). The 周易 line (511 theorems, 22% of the new results) is a good instance that produced a reusable law (`Commuting`), but its text-formalization modules (Places, Sites) belong in an instance ring, and in the Y1 map 33 of 52 "agreements" cite only the passage's own encoding (G11, G12). About twenty ported modules have no record and no chapter sentence (G13).

The new ZH claim (the 中华 edition, 5,673 judgments) extends this line. Under G11–G12 it would gain from two things settled first: the instance ring, and the split of "agreement" into agreement with a general law and the text's structure formalized. Its owner decides.

---

<a id="what-is-sound--应保留的"></a>
## What is sound and should be kept

- **The method and the discipline**: one relational unfolding first; the pure core (empty axiom reports, prelude only); standing labels (law, theorem under premises, condition, reading); honest scope ("a weaker model omitting a relation is not a refutation"); every reading labelled.
- **The strongest results**, which a reader-first chapter should lead with: one change read three ways; law and history as two readings (`Shown`, `exists_law_iff`, `Histories`); recurrence (lossless ⇔ returns; kept history needs openness); premises carve parts, with five premises read off one exchange and three as states of the law; rest under least loss with its exact premises (LeastLoss with `Halving`); the margin law and widening with no axiom; `Web.significance_undetermined`; the decomposition of the condition and "it orders nothing"; selection through couplings, the gap and pooled coupling; growth exponential iff a loop is upstream; the calibrations stated with what they say about the unfolding.
- **Integration done right**, the pattern for everything above: the selection line (SelectionGap derives the rest's response; PoolResponse derives SelectionPool's premise); ExchangePremises; Cuts (examples made one law); `EdgeClosure.Closure` through `Reach` with its equivalence; `Dependence.conditions_alikeAt_iff`; §4's constraint table ("none is an axiom").
- **The instruments**: the theorem-connectivity measure and the apart register with a category for every root (it is what exposed theme 1; K2 needs only a target); `research.py move` with manifests; the generated-page discipline; the chapters README generated from §11; N5's table-driven renaming with no aliases.
- **Statement-level economy**: about 4% removable statements in a 166k-line core grown by many sessions; exactness witnesses kept; each calibration a single theorem.

---

<a id="programme--推进次序"></a>
## Programme: one order of work

Each step names the findings it closes. Docs-only steps need no checker run; Lean steps go through the queue, one checker run each. Steps 1 and 2 can run in parallel; step 3 needs step 2's names; step 4 needs step 3; step 5 waits for step 4 so that the chapter is rewritten once.

| Step | Content | Findings | Cost |
|---|---|---|---|
| **0. Rule** | Board rule 9: a generalization lands below the law it generalizes and proves it; it does not land beside it. A new module either is imported by an existing one or states why it is a leaf (an instance, a tool). | G2, G §4 | board text |
| **1. Docs now** | (a) Ethics wording: scope vs order in the chapter's status block, §6.13, §6.15, §8.5 and AGENTS.md; "C follows from the condition" restated as `widens_iff_retains_adds`; F6's three contradictions; D8's "both premises" in every summary. (b) The exact base relation in README, `Becoming.lean`'s header, World.lean's doc and §1/§9 (two presentations, `rfl` one way, lossy the other; one word for the root). (c) ℕ tags on `rising_recurs`, `falls_not_recurring`, `excess_bounded`; the fixed-type limit of `Widens`. (d) §8 rewritten as about twelve ranked items; the connectivity log moved to THEOREM-CONNECTIVITY.md; "stated whole"'s measure updated. (e) K1–K7 proposed; item 11's claim qualified until they run; target 1's formal part restated as the base step (proposal: the wording of a target is a goal scope). | F4–F6, D8, A1 (docs), D5, D6, D9, C4, G14, D1, D4, D11, D14 | 1–2 sessions |
| **2. Corpus and records** | Moves to history (≈14 chapters with editions, REFERENCE's verbatim parts, four snapshot pages, ≈40 uncited study files, executed plans and answered briefs, superseded reviews, 64 landed kits); record history compacted to substantive notes; supersession used; 53 proof bindings re-roled as provenance; record families; one module table generated from the import graph; merged worktrees and `.build` removed (salvage refs first for the 8 unmerged). | E1–E18, A5, C6 | 4–6 days of docs and tooling; no Lean |
| **3. Names and support, one checker run** | One rename table: B2's notions, F3 (`generation_*` → `arising_*`, module `Becoming.Arising`), F9 (`G0`, `positive`, `SelfGood`, `Unfolding` ported to `Web`, `Coupling`, `DependentSelection`, the three `RestsFrom`), B13's namespaces (less the withdrawn `Coarse`), A10, G9. One `Becoming.Prelude` (A9, B12). The 13 conditional theorems moved out of Interdependence/Feedback so that about 100 modules leave the ethics' import closure (A4). `Determined` and the law constructors in one law module (A7). `Image` deleted (B3). | B2, B3, B12, B13, F3, F9, A4, A7, A9, A10, G9 | 2 sessions, mechanical |
| **4. One base** | Scratch build first. One indexed standing record and `abbrev Web` (A2); `World` as a history (A1); `Law.*` as abbreviations at `Law.process` (B1, A6); inversions: Ideals → Horizon, Amounts → rest family, counted → decided counting, SelectionPool → Selection (G2); companion modules folded back (A3, B7); the connectivity measure counting recorded instances and the class "on the base only through a law defined in the same module" (B8, G3); target: `families_reach_each_other` true. Then the folds G4–G8 and Interleavings constructing the `World` (G10). | A1–A3, A6, B1, B7–B11, B14, G1–G8, G10 | 6–8 sessions, mostly mechanical, with fresh checker runs |
| **5. One evaluative chain** | The relation of run class to widening, or living significance restated over admission (D2, F13); `Pos := F`, `own` as a closure (D3, F7); the direction as a core theorem on a world's moves (D7); widening over a grown world (D6). | D2, D3, D6, D7, F7, F13 | moderate proof work |
| **6. The chapter, once** | The reader-first chapter (C5) on the settled structure: preface, §0, body once in argument order, one theorem map, glossary of ≈36 core terms plus an index (F2), §6 in five sections (C3); the Chinese edition brought to the same structure; OPENING's footnotes pointed at the theorem map. | C1–C6, E1, F1, F2, F4 | 2–3 sessions |

Throughout: the instance ring for the 周易 text modules, the PT nets and the ports with no argument role (G11, G13), and the split "agreement" grade (G12), before the ZH line grows further.

---

<a id="what-could-not-be-checked--未能检查"></a>
## What could not be checked

- No Lean was built and no checker or measure rerun. The feasibility of the definitional refactors (step 4), of the joins G5–G7 and G10, and of the D2 link are inferences; each needs a scratch build before any claim. That the ℕ-dependent statements fail over dense amounts is argued from their proofs and from `Halving`, not checked as a countermodel for each.
- Duplicate counts come from normalized statement text (B, A); about twenty pairs were read, and the group counts are upper bounds for "same statement". Whether a name to be deleted is cited by records, the chapter or OPENING was not checked: `make research-find` on each name first.
- The co-occurrence scan behind D2 is textual; a bridge through an intermediate definition could be missed.
- The 47 frontier modules were read at header and grep level; the 400 kB Chinese-sources chapter and the 易传 chapter were sampled; the Chinese editions were checked for structure only.
- Whether the 8 unmerged worktree heads hold anything not relanded under another commit was tested by ancestry only.
- Every lens and this synthesis are AI work, read-only, of one day. §8.9's objection "every review is by AI" applies to this one too.
