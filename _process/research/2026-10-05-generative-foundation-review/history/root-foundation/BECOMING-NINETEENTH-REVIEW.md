<a id="nineteenth-review--第十九次审查"></a>
# Nineteenth review: what was checked after the eighteenth and never reviewed

An AI review, read-only. It built no Lean, ran no checker and changed no record, chapter, OPENING, README, GOALS, generated page or Lean file. It changed only this file, its row on the work board (item R20) and its row in chapter §8.8. Lean was read through a small script that prints each declaration's docstring and statement; proofs were read only where a finding needed them. Mathematics marked "reviewer's argument" is not Lean-checked.

**Object** (chapter §8.8, "Not yet reviewed", and the landings since 18 October 2026):
- the restatement of the continuation condition as the conditional §6.15, and the Lean docstrings that followed it (P128, P129);
- `Becoming.Runs` and the five P130 modules after it: `CourseWorlds`, `LearnableRuns`, `ParityReadings`, `FinerTraces`, `FormedLoops`;
- sections never reviewed: §6.8 (what the condition yields), §6.9 (route (b)), §6.12 (the audit of uses), the externalist defence of A and the ground of the neutralities;
- W1 (the re-root at `Becoming.World`), the F2 and F3 ports and the F3 sweep, A4-L (`Becoming.Ideals`, `Becoming.HistoryIdeals`), K1–K3 (`Becoming.Cuts`), Y1 (`Becoming.Hexagrams` and the 易传 chapter), V (`Withholding`, `Widening`, `Pace`, `Passing`, `JointKeeping`);
- R19's wording changes, `e96ab8fc6..f0a887a61` (canonical chapter, kept chapters, Chinese edition).

**Base.** main at `b88c2d972` (V landed; core receipt `20261019T064004.300228Z`). Line numbers are at that commit.

**Paths.** *core* = `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`; *ch* = `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md`; *zh* = its Chinese edition; *rec* = `theories/becoming/results/records/`; *DC* = `DELEGATED-CHOICES.md` in this folder.

**Severity,** as in the seventeenth and eighteenth reviews: *error* (the prose says what the Lean contradicts, or cites what is not there), *overstatement* (the prose claims more than the Lean states: a dropped hypothesis, quantifier or ¬¬), *naming*, *label* (a reading without its AI label or with a stale status), *presentation* (true, but stale, thin or misleading as placed), *confirmed*.

---

<a id="summary--摘要"></a>
## Summary

**Formal state.** No false Lean theorem was found in what was read. Every "exactly" checked is a genuine `↔`. The constructive calibrations read are right: `refutable_holds_iff`, `Stretches.refutable_closed_iff` and `closed_refutable_iff` (double-negation elimination), `Stretches.cut_decided_iff_lpo` (LPO), and the port grades that name excluded middle, choice or a section as hypotheses. The V modules state their witnesses' exactness with explicit second witnesses (`closes_within_exact`, `whole_fixed_exact`, `dissolving`, `Line.passes_out_exact`, `Ring.givesFirst_restores_exact`).

**The problems are again in the words.** Five kinds:

1. **Five errors.**
   - The glossary entry *significance* still reads "Positive significance from a standpoint" (ch:1642, zh:1367; and `Metaethics.lean:152`, the docstring of `Valuation.Seed`). R19 removed the positive gloss everywhere else; in the Lean `sig` is a bare `Prop`.
   - §6.1 still says "The object of living significance is 生生 … life in the whole and its continuing generation" (ch:786, zh:450). D1's revision says "the Lean predicate `living` does not read 生生", and §6.12 (ch:1031) says that reading was withdrawn. R19's commit `ec24028e2` reports the change made; this sentence was missed.
   - The V constraint table (ch:712) says "Every return of a loop with whole-number strengths at least doubles what arrives (`runaway_of_returns`)". The same table, two rows up, cites `Widening.whole_strengths`: with product 1 a loop of whole-number strengths keeps the difference at every turn. The doubling (`carried_doubles_return`) is of the carried amount, the most difference that can arrive, attained by `ExchangeLaw.carrying`, which is not gainless (eighteenth review, finding 3). Of an actual loop the sentence is false.
   - §6.12 (ch:1025) cites `inventory_g0_of_unrestricted`, "the bridge states this for the periphery's interface". The bridge left the core in the F3 sweep, and the declaration is in no live Lean file (the port map sends it to `g0_of_unrestricted`).
   - The decision register still describes the retired structure as current. D16(3): "where Part II asserts the axiom it is a theorem"; D18: "the one axiom is Part II's assertion"; D21: "what Part II's assertion adds"; D13: "retaining adds no premise under the axiom". Its standard 1 (§0) reads "Ren's words first … the decision follows them". §6.15 says the theory asserts no condition, and D45 and AGENTS.md say Ren's words are provenance. The register is live and is where every [AI reading, Dn] label points.
2. **Overstatements.** The worst is a dropped double negation: `Web.begins_within` (Passing) is `¬ ∀ j < d, ∀ a, ¬ Arises (S + j) a`, while ch:723 and the record `a-pattern-lasts-through-passing` (law 1) say "has a carrier beginning within every `d` steps". Two more places drop conditions:
   - the 易传 mapping reads 生生之謂易 as "生生 … needs openness and inflow from beyond" (ch:278; YI-ZHUAN rows and §5) and grades it *exact scope*, without the census, embodiment, balance and dissipation that `World.arising_opens` needs, or the dissipation, enclosure and the ¬¬ of `Web.generation_fed_from_beyond`;
   - R19's new reason "the dynamics … do not single out a center (`Clearing.center_not_derived`)" (ch:897, repeated at ch:923) generalizes from one witness.
3. **Naming.** V's module names collide with existing namespaces. `Becoming.Widening` also holds `Relevance`'s witness (`Widening.bare_forces_reason`), and "widening" is the core's word for the generative space (`Web.Widens`, D1), not for a growing difference. The module `Becoming.Passing` shares its name with `Entropy`'s namespace `Becoming.Passing`, whose `Passing.passes` the chapter cites in "The theory stated whole". `Becoming.Switching` now holds three unrelated witnesses.
4. **Labels.** Nine Lean module docs still say "Readings (the AI's, pending Ren)", which no reading has been since D45. Several readings in §6.8, §6.9, §6.12 and V's framings carry no D-number.
5. **Presentation.** Counts are stale (§9 against the V receipt; the Chinese §9 still names eight bridge modules). One instance the chapter cites (`PreparationCorrespondence`) lies outside the core and outside `experiments/`. §9's "the import tree starts there" leaves out the three foundation roots. "The core states the content of every periphery module" omits the 72 theorems it states with a classical principle as hypothesis.

**What has no object.** The chapter has no externalist defence of A and no argued ground of the neutralities to review. What it has is the label "an externalist articulation premise" (ch:161), the countermodels of §6.2 and the open item of §8.5. §8.8 lists them as unreviewed; they are open targets.

**Sound.** The §6.15 equivalences, the margin laws, route (b), the decomposition, A4-L, K1–K3, Y1's laws, `Becoming.Runs` and the V laws say what their Lean says, apart from the findings below.

---

<a id="1-findings--发现"></a>
## 1. Findings

Ranked by severity, then by reach. "Fix" is what an integrating session would change; this review changed none of it.

### Errors

| id | where | finding | Lean | fix |
|---|---|---|---|---|
| E1 | ch:1642; zh:1367; core `Metaethics.lean:152` | Glossary *significance* = "Positive significance from a standpoint"; `Valuation.Seed`'s docstring "Some living claim has positive significance". | `Valuation.sig : Pos → C → Prop` (no valence); `relevance_least`; §6.15 "not a positive valence" | Glossary: "Significance from a standpoint: whether, from a standpoint, a claim (or a formation's continuation at a step) has significance; it carries no valence." Same in zh. The docstring goes with R19's open docstring item (needs a checker run). |
| E2 | ch:786; zh:450 | §6.1: "The object of living significance is 生生 (… life in the whole and its continuing generation …)". Contradicts D1's revision and §6.12 (ch:1031). | `G0 M living positive`; `living : Q → Prop` with no further generation (premise card D) | "Living significance concerns realized living content; 生生, life in the whole and its continuing generation, is the object of the ethical direction, compared by widening (D1). The `living` readings do not include further generation." |
| E3 | ch:712 (V table, row 6) | "Every return of a loop with whole-number strengths at least doubles what arrives (`runaway_of_returns`)." False of actual loops: in the same table `whole_strengths` keeps the difference at product 1. | `carried_doubles_return`, `runaway_of_returns` (Frequency.lean:430, 464) state it of `carried`; `Widening.whole_strengths` (Widening.lean:484) | "Every return at least doubles the carried amount, the most difference that can arrive at a condition (`carried_doubles_return`); returns often enough make it outgrow every polynomial (`runaway_of_returns`). The bound is attained by the carrying law, which is not gainless. An actual loop of whole-number strengths keeps the difference at product 1 and runs away at product 2 or more (`Widening.whole_strengths`)." |
| E4 | ch:1025 | §6.12 cites `inventory_g0_of_unrestricted` and "the bridge". No bridge since the F3 sweep; the name is in no live Lean file. | port map `development/bridge-fold/f3j/map_s1.py:114` → `g0_of_unrestricted`; `PositiveGround` (core) | Cite the core statement of the inventory case (`positive_ground_by_bound_of_unrestricted` and `g0_of_unrestricted`, after checking which `PositiveGround`/`Handoff` theorem states the interface), and drop "the bridge". |
| E5 | DC §0 standard 1; D13 "Reasons"; D16(3); D18 "Decision" and "Reasons"; D21 | The register describes "Part II's assertion" and "the one axiom" as current, and its first standard makes Ren's words decide. | `Unrestricted` is a hypothesis everywhere (33 theorems by statement scan); §6.15 | Restate D16(3) and D18 in current terms (the condition of §6.15, not asserted), D13 "under the condition", and D21's "what the condition adds"; replace standard 1 by D45's rule (Ren's words are the evidence of what a term of his means; a reading stands by its place in one account). Keep the old text as dated history. |

### Overstatements

| id | where | finding | Lean | fix |
|---|---|---|---|---|
| O1 | ch:723; rec `a-pattern-lasts-through-passing` law 1 | "has a carrier beginning within every `d` steps". The Lean is the negation of "no carrier begins across `d` consecutive steps", ¬¬∃, with activity undecided. | `Web.begins_within` (Passing.lean:113) | "no `d` consecutive steps pass without a carrier beginning (`Web.begins_within`, in double-negation form)". `ByPassing.passes_within` does give ∃ under the passing premise; say so beside it. |
| O2 | ch:278; YI-ZHUAN-AND-BECOMING.md rows `p-shengsheng` (l. 69) and §5 (l. 109); D47(2) | 生生之謂易 graded *exact scope*: "生生 … needs openness and inflow from beyond". The conditions of the cited laws are missing. | `World.arising_opens` (Openness.lean:722: census, embodiment, balance, dissipation); `Web.generation_fed_from_beyond` (Continuation.lean:401: balance, dissipation, a finite family without repetition, enclosed around from some step; conclusion ¬∀¬) | Name the conditions: "in a counted, embodied, balanced and dissipative world, arising without end excludes enclosure from any step on, and a dissipative family enclosed around cannot from some step on be fed from nothing beyond". Same in zh and in D47. |
| O3 | ch:897 (R19 wording), ch:923 | "centers and their boundaries are formed within the dynamics, which do not single out a center (`Clearing.center_not_derived`)". The theorem is one witness: significance closed along feeding, with self-significance everywhere, fails standpoint neutrality and living significance. It shows that a center derived along dependence does not give the condition, not that the dynamics single out no center. | `Clearing.center_not_derived` (Standpoints.lean:435) | "along dependence the center is not derived (`Clearing.center_not_derived`)", as ch:84 already says; keep "the dynamics do not single out a center" only as a reading [AI reading, D11/D43]. |
| O4 | ch:697; rec `conditions-kept-together` law 4; core JointKeeping.lean module doc and docstring at 402 | "no course leaves the guard … from any configuration". The theorem states `Kernel` at one configuration, `withinRenewal.state 0`. | `Renewable.kept_part_not_renewal` | Say "from this configuration", or add the one-line `∀ s, Kernel …` (the focal formation is active at every configuration). |
| O5 | ch:1463; ch:226 | "It imports nothing, so the import tree starts there" (`Becoming.World`). The three foundation modules are roots too: `Becoming.Frame` imports `GenerativeCore` and `Becoming.Renewal` imports `RelationalRenewal`, neither through `World`. "Root" is also given to the run (ch:1278, ch:1311; Runs.lean module doc, "the one root is the run"). | imports of World.lean (none), Frame.lean:1, Renewal.lean:1 | "The base `Becoming.World` imports nothing; with the three foundation modules it is a root of the import tree (W2, queued, moves …)". Use one word for the import root and another for "every reading is a run". |
| O6 | ch:1455 | "the core states the content of every periphery module that was in the checker's run". The port files grade 72 theorems *same* only with a principle named as hypothesis: excluded middle (52), extensionality (9), stability (6), section (3), choice (1), decision (1). | `development/bridge-fold/port-*.md` | add "… with the excluded middle, choice, extensionality, stability or sections their periphery proofs used taken as hypotheses (72 theorems)". |
| O7 | ch:845 | "D follows from A and from the significance of living significance". The theorem has no living-significance hypothesis; it reads "positive" as unindexed significance. | `positioned_articulation_of_articulates` (Metaethics.lean:236) | "D follows from A, with positive content read as significance from every standpoint". |
| O8 | ch:473; Cuts.lean module doc and docstring at 102 | "its ends staying within each other's closure". For a directed `added` the Lean asks only that the target lie within the source's closure. | `Cuts.closure_unchanged_iff_bypassed` | "each removed link's target stays within its source's closure under what remains"; "each other's" holds for links read both ways (`link_cut_unchanged_iff`). |

### Naming

| id | where | finding | fix |
|---|---|---|---|
| N1 | core `Widening.lean` (namespace at 91), `Relevance.lean:247` | Module `Becoming.Widening` and `Relevance`'s witness share the namespace `Becoming.Widening`. The core's "widening" is the generative space (`Web.Widens`, D1, §6.13); the module states whether a loop closes, keeps or widens a *difference*, and its headline case is closing. The name states the opposite case of its own headline and reuses the theory's most loaded word. | A structural name for the law, such as `Becoming.ReturnMaps` or `Becoming.LoopReturn`; rename the `Relevance` witness `BareSignificance`. A rename after landing needs a name that states a wrong meaning (AGENTS.md, naming); this one does, on both counts. |
| N2 | core `Passing.lean`; `Entropy.lean:1692` | Module `Becoming.Passing` (patterns passed across carriers) and `Entropy`'s namespace `Becoming.Passing` (a unit carried back and forth; `Passing.passes`, cited in "The theory stated whole", II) share one name for two different things. | Rename the `Entropy` witness `Shuttle` or similar, or the module `Becoming.PatternPassing`. |
| N3 | core `LawAlongRun.lean:206`, `Mechanism.lean:385`, `Pace.lean:274`; `LawAlongRun.lean:238`, `Mechanism.lean:357` | `Becoming.Switching` holds three unrelated witnesses (V added the third); `Becoming.Coarse` holds two. One notion, one name (P129) is not met. | Qualify each by its module (`Pace.Switching`, …), the way `Withholding.Ring` is. |

### Labels and status

| id | where | finding | fix |
|---|---|---|---|
| L1 | core `Interleavings.lean:33`, `Remainder.lean:76`, `Onward.lean:48`, `Runs.lean:54`, `Frequency.lean:68`, `Observation.lean:53`, `CourseWorlds.lean:61`, `Propagation.lean:68`, `Tail.lean:59` | "Readings (the AI's, pending Ren)". Since D45 no reading waits on Ren. | "Readings (the AI's, Dn)" with the decision that took each; goes with the next checker run that touches these files. |
| L2 | ch:936 ("Reading Ren's words", §6.8); ch:955 ("Reading.", §6.9); ch:957 ("[AI reading]" without a number); ch:1033 ("Courses are compared on possibilities, a reading adopted") | Readings with no D-number. AGENTS.md: every reading keeps its AI label. | [AI reading, D16]; [AI reading, D17, D18, D19]; [AI reading, D20]; [AI reading, D1]. |
| L3 | ch:697–700 (V's five framings) | Readings sit in the framing bullets, outside the block labelled [AI reading, D48]: "A society that oppression or extraction keeps going for centuries is this case", "So `Viability = …` is a heuristic", "That is the whole truth of 'any factor at zero …'", "Term limits, audits, courts and antitrust are, so read, couplings". D48(1) covers them, but the chapter does not say so. | Label the five framings [AI reading, D48], or move these sentences into the readings block. |

### Presentation

| id | where | finding | fix |
|---|---|---|---|
| P1 | ch:1455, ch:1458 | §9: "264 modules … 267 in the core closure", "466 of the 9,895 spine theorems apart". The V receipt (§8.2) has 269 and 272 modules and 10,174 theorems. | Refresh from the receipt and the last connectivity rerun. |
| P2 | zh:1244 | The Chinese §9 cites receipt `20261015T231055.702986Z`, 126 core-closure modules and "八个桥接模块". The zh banner says its framing matched the English on 19 October. | Regenerate the zh receipt paragraph from the English. |
| P3 | ch:473 | `PreparationCorrespondence.bond_cut_separates` and `reinforced_cut_unchanged` are cited like spine theorems. They are an instance with standard axioms and its own receipt (`20261019T052332.277017Z`), and the file lives in `_process/research/…/development/k1-cuts/`, not in `experiments/` (REPOSITORY-LAYOUT: executable research in `experiments/`). | Say "(periphery instance, standard axioms)"; move the file under `experiments/` with `research.py move`. |
| P4 | ch:1092 | "At least 26 theorems … take `Unrestricted` as a hypothesis", "Twenty more … state the condition in their conclusion". A statement scan of the core finds 33 and 24. "At least" keeps it true; the counts are of 17 October. | Recount at landing, or drop the numbers and cite the inventory. |
| P5 | ch:717, 719, 726 | V wording a little stronger than the Lean: "more waiting is less giving" (`waitsAll_more_waiting`, `answers_more_waiting` are monotone: never more giving); "restores every formation from the third step on, from every start, and no earlier" (exactness is from one start, `oneWithheld`); "a closing loop merges two differences" (`closing_merges` needs `f 0 = 0`). | "more waiting never gives more"; "and, from the one withholding, no earlier"; "a return map keeping no difference that closes merges two". |
| P6 | ch:933 | "the levels without it admit every formation at every step" cites `Clearing.free_rider_loses`, which states admission of the clearer only. | Cite `Clearing.admitted_all_without` (Significance.lean:462). |
| P7 | ch:788 | §6.1's characterization omits that `Valuation.significant_iff` needs a standpoint `p₀`; §5 (ch:754) includes it. | "On a connected whole with some standpoint and some living claim". |
| P8 | ch:473 | `Flow.system_unchanged_without_iff` and `Flow.withinSystem_two_takers_iff` take `[DecidableEq C]`; the chapter does not say so (the module doc does). | "with equality of conditions decided". |
| P9 | core `CourseWorlds.lean` module doc | "the counterfactual worlds of P80b attain the most difference that can arrive": attained by the carrying law, which is not gainless; the doc does not say so (§8.2 lists "tightness over gainless laws" as open). | One clause, as in E3. |
| P10 | 11 docstrings ("positively relevant", "positive significance": `ScoreRepresentation`, `Metaethics`, `PositiveGround`, `ActiveReading`, `ProfileReach`, `Handoff`, `Becoming.lean`) | R19's open item, carried here so the fix list is whole. | With L1, in one checker run. |
| P11 | ch:1446–1447 (§8.8) | "the externalist defence of A and the ground of the neutralities" are listed as unreviewed, but no such argued text exists; "the structure of the former conditional part" is history. | §8.8: list them as open targets (§8.5), not as unreviewed sections. |

### Confirmed

Read against their Lean and found to say what it says (apart from the findings above):
- **§6.15.** The equivalences `Web.widens_iff_retains_adds`, `Web.keeps_iff_retains` and `Web.mixed_iff_adds` hold under the condition. So do `retains_iff_includes`, `adds_iff_exceeds` and `retains_agree`; `Valuation.premises_of_unrestricted` with its stepwise, relational and run readings; `relevance_least` and `g0_of_unrestricted`; `Web.Retains.within`; `Flow.within_closure_iff_retains`; `universal_reason_of_unrestricted` (A remains, as a `Neutral` hypothesis); `Ranking.possible_extends_iff`. The statement of `unrestricted_iff_g0` (with `somewhere`) and of `Web.unrestricted_iff_paths_g0` is exact. In the decomposition, `unrestricted_iff_presupposed_along`, `unrestricted_iff_presupposed` (whole admissible), `unrestricted_of_presupposed` (covering), `boundaryInvariant_iff_conditional`, `boundaryInvariant_iff_all` and `Clearing.without_invariance` all match; the chapter's "locates the step and does not lower the condition" is right, since `boundaryInvariant_iff_all` makes the step, given the presupposition, the condition at that standpoint. `Web.significance_undetermined` (with an event that lives) is stated with its scope.
- **§6.8.** The margin laws (`Balances.retains_iff_within_margin`, `loses_iff_beyond_margin`, `adds_iff_within_margin`) take no condition, as said; `Preemption.not_undermining_yet_loses`, `Transfer.unordered`, `Restoring.Inflow.retains_adds`, `Web.Retains.not_added`, `Retains.of_fewer`, `retains_bounded_iff`, `AdmitsWithin.narrow`, `Clearing.centers_disagree` and `bounded_rival`.
- **§6.9.** `Flow.beyond_gives_nothing`, `Clearing.dependenceRegion_iff` (the region is exactly the feeding closure), `Balances.consumption_ends_with_feeders` (bound by the level at `T`), `Overshoot.ends_through_feeder`, `Clearing.closure_supported`, `bounded_whole`, `retains_bounded_iff_includes` and `retains_bounded_iff_retains` (with the covering hypothesis named), `Clearing.within_closure_yet_loses`, `Clearing.levels`, `Clearing.reach_middle` and `Trophic.mediates`. "Route (b) reaches the whole only where the whole is one feeding closure" is what the Lean shows.
- **§6.12.** `articulates_total`, `Widening.bare_forces_reason` (forced reading of A on living content), and the ranking theorems named.
- **V.** `Withholding`: closed forms, absorption, passing out, return around loops and the ring witnesses, with no premise on `α`, as the module says. `Widening`: `never_closes_of_no_less`, `closing_needs_less` (the link is found), `closes_within` with exactness, `sub_const_closes`/`open`, `cut_closes`/`cut_reopened`, `settles_within`, `runs_away`, `whole_strengths`, `nothing_between` and `gradual_needs_another_link`. `Pace`: `pace_law` (`L ≥ 2N − 1`, two values given), `dissolving`, `held_fixed`, `whole_fixed` and its exactness, and `rule_until_reading` with `Copying.rule_parts`. `Passing`: everything under the passing premise. `JointKeeping`: `kernel_and_iff`, `kernel_allOf_iff`, `ChoicePoint.each_not_joint` and `no_rule_decides_joint` (for decisions shown to exist), with `no_respecting_rule_decides_joint`.
- **Y1.** `order_paired`, `changes_merges`/`changes_keeps`, `waxWane_lossless`/`returns`, `fourth_step` (4 is the least return: reviewer's argument from `state 2 ≠ sui`), `every_returns_iff` for every law of hexagrams, `pairs_goAlike`/`yang_not_goAlike`, `arising_recurs`/`ceasing_recurs`, `revisits_within_order` and `kept_history_unlisted`. 一陰一陽 against `World.law_iff_em` is right in the 易传 chapter (finite worlds); ch:278 drops "finite" (fold into O2's fix). 窮則變 against `consumed_ends_when_fixed`/`consumed_continues_transformed` is right.
- **K1–K3.** `within_link_iff`, `attached_link_separates`, `joined_cut_unchanged_iff`, `Flow.GrownBy` (a hypothesis on the list, as said), `GrownBy.condition_needed`, `every_condition_needed` and `cut_unchanged_iff`.
- **A4-L.** `adheres_iff_closed`, `closed_iff_within_lower`, `Stretches.not_not`, `refutable_holds_iff`, `Stretches.refutable_closed_iff`/`closed_refutable_iff`, `Stretches.classification` (with the decision as hypothesis), the two `cut_decided_iff_lpo` (runs and words), `histories_representation` and `run_reading_unique`. The `IdealsCorrespondence` path exists.
- **`Becoming.Runs` and P130.** The identifications `World.run_world`, `Run.world_*`, `World.balanced_iff_run`/`law`/`exists_run`, `World.restRun_web`, `ExchangeLaw.courseWorld_balanced_iff` (with `Nonanticipating`) and `carriedWorld_balanced` are as the record `worlds-are-runs` says. `LearnableRuns`, `ParityReadings`, `FinerTraces` and `FormedLoops` state what their module docs say; `FinerTraces` says honestly that the counts are of the enumeration.
- **W1, F2/F3.** `Becoming.World` imports nothing. Every port file grades each theorem *same* or *step* with a stated core counterpart, and none is open. The checker strips the foundation's `import Std` and compiles from the prelude (`check_becoming.py:12`, 2567–2627), as §9 says. The chapter's `Passing.passes` (II) is `Entropy`'s and matches its sentence.
- **R19.** The new reasons citing `Frame.self_incomplete`, `Contextual.fitsFree_iff`, `World.withRest` and `goAlike_iff_lumped` say what those declarations state. Every Lean link in the chapter resolves.

---

<a id="2-verdict-per-item--各项结论"></a>
## 2. Verdict per item

| item | verdict |
|---|---|
| §6.15 and its docstrings | Sound; E4 (one dangling bridge citation, in §6.12), P4 (counts). The P129 docstrings use current terms; the "positive" docstrings remain (P10). |
| §6.8 | Sound; O3 (from R19), P6, L2. |
| §6.9 | Sound; L2. |
| §6.12 | E4; L2. |
| Externalist defence of A, ground of the neutralities | No argued text to review (P11). The countermodels of §6.2 that show A and each neutrality needed were read and match their Lean. |
| `Becoming.Runs` + P130 | Sound; L1, O5 ("root"), P9. |
| W1 | Sound as an import change; O5. |
| F2/F3 ports and sweep | Graded per theorem; O6. Individual grades were sampled, not rechecked. |
| A4-L | Sound. |
| K1–K3 | Sound; O8, P3, P8. |
| Y1 | Laws sound; O2 in the 易传 reading of 生生之謂易. |
| V | Laws sound; E3, O1, O4, N1–N3, L3, P5. |
| R19 wording | E1 and E2 are places R19 meant to change and missed; O3 is wording R19 introduced; P2 (zh). |
| Decision register | E5. |

<a id="3-the-nondual-method--一元关系方法"></a>
## 3. The nondual method

The texts read keep to it. A collective is stated as "a region of formed relations, not a unit with an interest of its own" (V), and joint keeping is put as pooled couplings, not as opposed interests. The condition is read as boundary neutrality, not as a center at every point. Two places lean the other way in wording only:
- O3 states as a fact of the dynamics what one witness shows of one construction;
- E5's standard 1 makes one participant's words decide a reading, which the method's own rule (D45) has replaced.

<a id="4-what-could-not-be-checked--未能检查"></a>
## 4. What could not be checked

- No Lean was built and no receipt rerun. The receipts were not re-hashed; the 19 October whole-repository review did that for K2.
- Proofs were read only for O1, O4, E3 and the ChoicePoint law.
- Of the 44 passages of the 易传 map, the four the chapter names were checked, not all 44.
- Of about 1,800 port grade rows, the "named" grades were counted and about thirty rows were sampled.
- U and U2 (the join modules of 17 October) landed after the eighteenth review and are not in §8.8's list or in this one's object. They remain unreviewed.
- The Chinese edition was spot-checked only (E1, E2, P2).
- Records were read only where a finding needed them: `a-pattern-lasts-through-passing`, `conditions-kept-together`, `worlds-are-runs`.

<a id="fix-list--修正清单"></a>
## Fix list

For an integrating session. Docs-only items need no checker run; Lean docstring items go together in one.

**Docs only**
1. E1: the glossary entry *significance*, en and zh.
2. E2: §6.1's "object" sentence, en and zh.
3. E3: V table row 6.
4. E4: §6.12's inventory sentence, citing the core statement.
5. E5: D13, D16(3), D18, D21 and §0 standard 1 in DC (and DC.zh), with dated notes.
6. O1: ch:723 and the record `a-pattern-lasts-through-passing` (law 1 and summary).
7. O2: ch:278, the 易传 chapter's row `p-shengsheng` and §5, and D47(2).
8. O3: ch:897 and ch:923.
9. O4: ch:697 and the record `conditions-kept-together` (law 4).
10. O5: ch:226, ch:1463; one word for the import root.
11. O6: ch:1455.
12. O7: ch:845.
13. O8: ch:473.
14. L2: the labels at ch:936, 955, 957 and 1033.
15. L3: the five V framings.
16. P1 and P2: refresh the §9 counts and the zh receipt paragraph.
17. P3: mark the `PreparationCorrespondence` citation and move the file under `experiments/`.
18. P4–P8, P11.

**With the next checker run (Lean docstrings and names)**

19. L1: nine module docs, "pending Ren" → their D-numbers.
20. P10 and E1's `Valuation.Seed` docstring: the "positive" docstrings.
21. O4 and O8: JointKeeping's and Cuts' docstrings.
22. P9: CourseWorlds' module doc.
23. N1–N3: names. These need a rename table and record rebinding, so decide them on the board first (board rule 3: the module owner decides).
