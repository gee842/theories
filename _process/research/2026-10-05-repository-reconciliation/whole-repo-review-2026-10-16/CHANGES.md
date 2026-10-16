# 3. What needs to change

[Review summary](README.md) · [Architecture](ARCHITECTURE.md) · [What is proved](PROVED.md) · [What needs to change](CHANGES.md) · [Restructure plan](RESTRUCTURE-PLAN.md)

> AI-authored section of the whole-repository review of 16–17 October 2026 (read-only, HEAD `0cfb9c567`; Claude Opus 5.5 reviewers with adversarial verification). Not Ren's text and not external review. Paths are repository-relative; counts are as measured by the reviewers at that HEAD.

**Abbreviations.**
- **chapter**: `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md`
- **L**: `experiments/integrated-correction/general-framework/generative-basis/lean`
- **B/**: `L/becoming/Becoming/`
- **RF**: `_process/research/2026-10-05-generative-foundation-review/root-foundation`
- **records/**: `theories/becoming/results/records/`
- **receipt**: the current core receipt `L/becoming/becoming-verification.json` (run 20261016T124157.989030Z)

Each item gives what is wrong, where, why (the evidence), the fix, and whether Ren must decide. "Partly" means the finding stands with the correction shown. Unverified minor findings are listed under "To check" at the end. No refuted findings were reported.

## Executive summary

1. **Critical. Revoke the leaked OpenRouter key today.** One live-format `sk-or-v1-` key is in 5 tracked files. It has been pushed to origin since 2026-09-25 (F1). Only Ren can revoke it. Redacting the files does not undo the leak.
2. **The Lean core is sound. Several prose claims say more than it proves.** Lean proves rest only as ¬¬∃. G0 follows by restricting a universal predicate. Several "draws in / opens" results are negations. "Rest at every resolution" is the fixed-unit theorem. "No Lean axiom" is cited on records whose periphery uses classical axioms. The Part I summary drops hypotheses. See (a).
3. **The 10-11 G0 fold and the 10-16 Part II fold have not reached most places.** About 25 places still call G0 or Unrestricted an asserted axiom: chapters, plans, Lean docstrings, records, goals, AGENTS.md and the generativity chain (B2).
4. **The canonical chapter lags P129/P130.** §9 counts are stale and P130 is missing. §8 stops at the 16th review and omits the readings pending Ren. Chinese and English contradict each other on who decided the 生/生生 readings. The English sections are summaries that drop citations.
5. **Navigation does not show what is proved.**
   - README features four pre-spine ethics records.
   - The first-priority "Next" is the 11 October redirect, which is already done.
   - GOALS gives no lifecycle state for its 15 scopes.
   - The directive register misses at least 19 recent Ren records.
   - The 2,208-file study folder and its 2.4 MB log have no index.
   - OPEN-QUESTIONS lists 4 items.
6. **Bloat.**
   - The 962 KB chapter states the theory three times.
   - The register table is rendered five times.
   - DEPENDENCIES.md is 555 KB.
   - About 4.8 MB of record history is rebind boilerplate.
   - The workboard is 276 KB.
   - Receipt run folders hold about 31.8k files (446 MB); counting all run-folder copies, they are 71% of all tracked files.
7. **Tooling.** CI is dead: billing failed, and a shallow checkout would fail anyway. `research-check` passes while four generated views are stale. The checker and registry resolve paths in ways that break under naive moves. **Fix the tools before moving anything.**
8. **Evidence at risk of loss.**
   - The fresh-run receipt exists only in `/private/tmp`.
   - A cited receipt exists only in the worktree `jolly-pike-140c94`.
   - Ren's own recordings exist only on local disk.
   - The guardian-anarchy repo exists only on this machine.
   - The disk is 91% full, with 88 worktrees.
9. **Provenance.**
   - About 10 governing Ren messages have no source record.
   - Several AI readings are labelled as Ren's.
   - Private third-party data (an illness, friends' transcripts) and ~35 unlicensed PDFs are pushed.
10. **For Ren:**
    - revoke the key; decide repository visibility and the data-inclusion policy;
    - wording of OPENING footnotes, AGENTS.md and GOALS;
    - which goals are closed, and the front-page result set;
    - whether D1–D39 are ratified, and whether 生成 should be split into separate terms;
    - billing, worktree and gc cleanup, and the restructure layout.

---

## (a) Correctness and overclaim

**A1 · major · confirmed — Rest is stated as "comes to rest"; Lean proves only that rest cannot be refuted.**
- Where:
  - chapter L77/L110 (item 4), L277/L281, L1177/L1275;
  - records `continued-change-needs-openness.json:14`, `space-and-its-parts.json:14`, `map-of-premises` (statement);
  - `B/Space.lean:66-70` docstring; `B/Premises.lean` header.
- Why:
  - `World.rests_unrefuted` (`Space.lean:337`), `comes_to_rest_unrefuted` (`Openness.lean:614`) and `rests_unrefuted_enclosed` (`Openness.lean:705`) all conclude `¬¬∃ N, RestsFrom N`. Naming the step needs LPO (`Counting.lean:1417 lpo_of_finite_ends`).
  - OPENING v6 already fixed this wording. The English convention exists only in the Chinese-only glossary row L1793.
- Fix: write "that it comes to rest cannot be refuted" in the English prose, records and docstrings. Add an English sentence to glossary L1793. Keep the theorem name and the Chinese term 静止定理, which are Ren's. Check whether the generativity chain quotes these headlines.
- Ren: no, for the AI text.

**A2 · major · confirmed — "G0 is a theorem" is presented with content Lean does not deliver.**
- Where:
  - chapter L30/32 (the one-sentence statement), L49/56, status table;
  - README L110-112 (headline "G0: …" stated outright);
  - OPENING `[^axiom]` L64 / README L68;
  - §6.15 bullet "Every use is discharged" (~L1027).
- Why:
  - `Unrestricted sig` (`Significance.lean:134`) is `∀ p t f, sig p t f`. `g0_of_unrestricted` and `relevance_least` are one-line unpackings (`Relevance.lean:90-131`); the module itself says "The step is immediate" (`Significance.lean:388-395`).
  - What follows is unvalenced significance of every claim, living or not. "Positive" and "further generation" are not represented (chapter L691 concedes this).
- Fix:
  - Add to the chapter's one-sentence statement (zh and en): "immediately: G0 is the axiom restricted to living claims; the condition gives significance to every claim, not a positive valence."
  - Make the README overview summary conditional ("Under G0, a condition, §6.15 …").
  - Retitle the §6.15 bullet "Every use is discharged (under the condition; by the definition of `Frame.relevance`)".
- Partly (foundation-1): the OPENING footnotes are Ren's text. Propose wording; do not edit.
- Ren: yes for OPENING and the README featured wording. Show Ren the chapter sentence, because the framing follows his fold.

**A3 · major · confirmed — §6.1 headline calls the Seed "S0".**
- Where: chapter L713/717.
- Why: `significant_iff` (`Metaethics.lean:192`) characterises G0 with `Seed` (`:152`, ∃ p c, living c ∧ sig p c). S0 is `SelfGood` (`:148`), a stronger premise. The premise card and the record keep the two apart.
- Fix: "a seed (some living claim significant from some standpoint; any position holding S0 with its own living content supplies one)", in both languages. Add the English counterpart of zh L715 ("the G0 ⇒ premises direction is nearly trivial").
- Ren: no.

**A4 · major · confirmed — Negations are glossed as positive existence ("draws in", "opens").**
- Where:
  - `B/Dissipation.lean` header L33-37 and L52-54, docstrings L576-579 and L672-675;
  - `Roles.generation_draws_in`;
  - chapter glossary L1731 (汲入);
  - record `no-finite-part-bears-taking` claims 3 and 5.
- Why: the conclusions are `¬ ∀ t, N ≤ t → Inward …` and `¬ ∀ t, T ≤ t → ClosedAt …` (`Dissipation.lean:445-452, 580-585`). The prose says "at arbitrarily late steps some formation gives …", which would be ∀N ∃t.
- Fix: use the exact form already used in `Continuation`: "it cannot be inward from any step on". Optionally add positive corollaries under named decidedness. Lean docstring edits go through the integrator's queue in a batched docs-only landing with a checker run. The same pattern is suspected in `Wholes.lean:127-190` and `Generation.lean:180-193` (To check).
- Ren: no.

**A5 · major · confirmed — "Rest at every resolution, with no premise added" is the fixed-unit theorem.**
- Where: the docstring and record summary of `World.rests_unrefuted_refinement_counted`; chapter L1177/L1275/L1578.
- Why: `Flow.refinement_gives_nothing` (`Resolution.lean:576-595`) shows dissipation plus enclosure force `split t * level t c = 0` from T on. The proof (L696-711) derives `unrefined` and calls `rests_unrefuted_enclosed`.
- Fix: "Counted as a giving, refinement is excluded by dissipation and enclosure wherever anything stands; rest then follows from the fixed-unit theorem." Lean statements stay as they are.
- Ren: no new decision; this states Ren's confirmed "case of 0" exactly.

**A6 · major · confirmed / partly — OPENING's physical premises are narrower than its prose.**
- Where:
  - OPENING ¶9 ("nothing comes from nothing … passes on without loss") and ¶13 ("nothing that goes on is closed");
  - `[^conditions]` L52-56;
  - chapter L1269 (novelty and forgetting laws).
- Why:
  - Confirmed: the rest theorems also need a census, embodiment and finite enclosure (`Openness.lean:705-707`). `fed_from_beyond` needs a finite distinct family with `Around` (`Continuation.lean:151-153`).
  - Partly: dissipation means at least one unit lost per uptake (`Dissipation.lean:224-232`). That is stronger than the statistical second law. `Passing.passes` (`Entropy.lean:1862`) is a finite, enclosed, lossless world that never rests.
  - Partly: the rest, novelty and forgetting laws are well-foundedness or pigeonhole on Nat. `laws-at-finer-units` shows rest fails at a refining unit.
  - The cited witness `Pair.own_not_joint` has no balancing web (`Continuation.lean:456-466`). `Exceeding.own_not_joint` is the balanced witness.
- Fix:
  - Propose to Ren: "wherever, as in ours, nothing comes from nothing, nothing passes on without loss, and what stands is what is active and can be counted". In `[^conditions]`, define dissipation as least loss per exchange in a closed family, and name `Passing` and the Resolution witnesses as caveats.
  - In the chapter: add the unit/discreteness dependence at L1269 and its zh line, and add a limitation line to the Novelty records.
- Ren: yes for OPENING; no for the chapter and records.

**A7 · major · confirmed / partly — "No Lean axiom" is claimed beyond its scope.**
- Where and why:
  - Confirmed: three records cite the standard boundary `no-ethical-premise`, which renders as "no Lean axiom": `every-origin-passes-the-gate.json:96`, `lifting-where-branching-is-finite.json:145`, `what-a-finite-history-refutes.json:127`. Their bound periphery receipts list propext, Quot.sound and Classical.choice. `standard-boundaries.json:9` sets a `cite_when` rule that `registry.validate` never checks.
  - Confirmed: `wisdom-root-part-one.json` L13/L17 says "hold axiom-free". It cites `LearningCorrespondence.responsive_learns`, `hebbian_activity_law_iff` and `updating_network_law_iff`, whose receipt lists Classical.choice.
  - Partly: README L102 says "It uses no Lean axiom" (hard-coded at `tools/research/navigation.py:220`). That is true of the core and bridge, not of featured periphery results (e.g. `PositiveGroundUncertainty`, 5 propext).
  - Partly: the chapter body §1–§5 cites periphery results with Classical.choice inside "Part I: Without axiom", without labelling them (L327, L346, L614, L673).
  - Unverified: "empty axiom reports" (AGENTS.md:35, OPENING:58, I5 REPORT) omits the 99 generated `*.mk.injEq` lemmas on propext in the core closure. No source declaration uses them.
- Fix:
  - Add a new boundary key, e.g. `no-ethical-premise-core-axiom-free`, for these records. Have the validator check `cite_when` against the receipts.
  - README: "Its core and bridge use no Lean axiom; some featured periphery results use Lean's standard axioms". Move this sentence into a configured Markdown file next to `readme_opening`.
  - Tag periphery citations in the chapter, and write "every source declaration" wherever empty reports are claimed.
- Ren: yes for OPENING:58 and AGENTS.md; no otherwise.

**A8 · major · confirmed — The `no-evaluation` boundary is used on records whose laws state significance or G0.**
- Where: `comparison-within-reach.json:179`, `levels-of-closure.json:183`, `life-as-condition-of-life.json:280`, `living-on-and-descent.json:193`.
- Why: their laws state `Web.Retains`, `Unrestricted`, `Mutualism.significant_iff` and `Valuation.significant_iff`. The boundary's definition says the record contains no ethical predicate.
- Fix: remove the key. Sweep other records that cite Retains, Adds, Unrestricted or `significant_iff`. Add a boundary such as "relates significance or the §6.15 condition to structure without asserting it".
- Ren: no.

**A9 · major · confirmed — `becoming-finite-horizon` makes a universal headline for a one-process result.**
- Where: `becoming-finite-horizon.json:14`.
- Why: `Renewable.finite_reading_includes_consumption` (`Horizon.lean:137`) is proved in the Renewable process. The record's own `does_not_show` says so.
- Fix: "In the renewable process, with or without feedback, no reading fixed by a finite prefix decides …". Keep the old text in `text_versions`.
- Ren: no.

**A10 · major · confirmed — Hypotheses are dropped in the Part I summary.**
- Where: chapter L1290-1297 (zh L1192-1199), and further:
  - item 4 L77/110: `rise_with_fall` without balance, `generation_opens` without `Distinct`;
  - `counting_*` (stated only for `Pointwise` properties);
  - L1236 `keep_pace` and L1304 `enclosure_bounds_change` (decidedness elided);
  - L1127 `unrestricted_iff_presupposed` (needs the whole admissible, not just covering);
  - L1324 `unrestricted_iff_g0` (needs every claim realised somewhere);
  - L1273 cites `World.contingent` where `World.independent` is meant.
- Why: the Lean statements of `most_difference_arrives` (`Propagation.lean:886`), `carried_le_polynomial` (`Loops.lean:1100`), `finite_horizon_iff_no_loop` (`Routes.lean:509`) and others require `every : ∀ c, c ∈ cs`, `Distinct`, stationary strengths, and bounded start and inflow. The §2 body and the records state these conditions.
- Fix: restore the conditions in both languages ("with every condition listed (each once)", "with the same formations and strengths at every step").
- Ren: no.

**A11 · major · partly — The premise card says every premise is named; it is not complete.**
- Where: chapter §0 L128-170.
- Why:
  - Confirmed: the eight World premises are missing (balance, dissipation, embodiment, census, bounded transmission, Acting, Taking, Dependent), as are the local conditions (finiteness, enclosure, listing, decidedness).
  - The Logic row says "Std", but the checker strips `import Std` and compiles the core from the prelude alone.
  - The Dynamics row still gives `Generative.Process` as "a local law supplied from outside", against the Ren-confirmed §1.
  - Partly: L169 "a definite global causal order is not assumed", while every World has one shared step index (L201 concedes this). Formations come from a fixed pre-given menu with threshold requirements.
  - Partly: FR is missing. Add one row for it. A pointer row for BC1, BC2, LC, LR, CP and NP is optional.
  - Partly: the §5 "established route" at L666 rests on EVALUATIVE-GROUNDING's repair premise. Name that condition in L666; do not put it on the card without review.
- Fix: add a "World premises" block with Lean names (`Space.lean:209-245`, `Premises.lean:141-147`, `Dissipation.lean:219-243`), a local-conditions block, and corrected Logic and Dynamics rows.
- Ren: no.

**A12 · major · partly — Definitional and near-definitional results are headlined as laws (pattern).**
- Where and why:
  - `worlds-are-runs`: 10 of 21 `Runs.lean` theorems are `rfl` or `Iff.rfl` (`Runs.lean:117-118, 159-161`). The record says it is not shown "by definition" (L101).
  - `World.unity` / `withRest_balanced`: balance is an accounting identity (`Imbalance.lean:68-75`). `Contextual.world_active` is `Iff.rfl`. Both establish that any sequence can be encoded, not a further fact about worlds.
  - "C is a law" on level paths: `Better := Widens`, so `paths_comparison_widens` holds by unfolding (`Significance.lean:431-445`). NONDUAL-METHOD:81 rejects moving content into definitions.
  - The first "law of every unfolding", `change_readings`, is `⟨.rfl×6⟩` (`Change.lean:542-548`). OPENING `[^law]` calls it "Proved".
  - §6.11 decomposition is the identity A ⇔ P ∧ (P → A) (`Boundaries.lean:393-431`).
  - `significance_undetermined` and `bounded_rival` toggle a free parameter. That shows non-entailment by the represented dynamics (NONDUAL-METHOD:90), not that "the axiom is needed" (docstring `Significance.lean:443-445`; chapter L684/692/1115).
- Partly: none of these is false. Each record or section needs a clause stating what is definitional and where the checked content is (e.g. `balanced_iff_exists_run`, `courseWorld_balanced_iff`).
- Fix:
  - Add a `definitional` tag or `does_not_show` scope item in records and module headers. Count restatement modules separately in totals (Courses, CourseWorlds, Readings, ParityReadings).
  - Rename the claim "C is a law" to "C's no-loss extension is exactly widening (definitional); that widening is better is the open warrant".
  - Reword "The axiom is needed" as "the represented dynamics contain no significance, so they do not entail it".
- Ren: yes for OPENING `[^law]` and for the argument in `[^axiom]`/`[^ethics]` that leans on the toggle; no elsewhere.

**A13 · major · partly — OPENING footnotes credit the axiom with what holds for every significance.**
- Where: OPENING `[^good-evil]` L72 / README L76 ("Proved under the one axiom"), `[^ethics]`.
- Why: `loses_iff_beyond_margin` and `adds_iff_within_margin` take any `sig` with no `Unrestricted` (`Significance.lean:328-345`). Only `free_rider_loses` and `unordered` use the axiom. Under the axiom every narrowing is a loss, so ordering mixed parts needs a measure that is still open (`Transfer.unordered`, `:511`). "A part enlarges itself …" has no formal counterpart.
- Fix: propose "For any significance, … ; under the axiom, for every continuation". Note that the enlargement reading is informal.
- Ren: yes.

**A14 · major · partly — 生生 is equated with the Lean `living` predicate in Chinese.**
- Where: `metaethical-core-characterization.json:13` (claim.zh, 7 uses); glossary L1693; zh title of `becoming-renewal-reading`.
- Why: the chapter itself says the `living` readings "do not include further generation; whether that is 生生 is a philosophical argument" (L141, L757).
- Fix: render `living` as 活的主张 / 活的内容 in the zh fields. Keep ids and aliases.
- Ren: show him, since 生生 is his central term.

**A15 · major · partly — The README-featured conditional assessment is called "independently reviewed".**
- Where: README L136; `conditional-foundation-assessment.json` overview.evidence; `chapters/START-HERE.md:7`.
- Why: the acceptance was by sub-agents of the same AI session. `FOUNDATION-ROOT-ACCEPTANCE.md:37` says these are "collaborating-AI internal reviews, not external peer review". The scope also predates the spine.
- Fix: correct overview.evidence (zh and en) and add `does_not_show` entries for internal review and pre-spine scope. The same qualifier is missing in EVALUATIVE-UPTAKE, -APPLICATION, EXPERIMENTAL-ACCESS and GENERATIVE-DEVELOPMENT (To check).
- Ren: no, but it changes the front page.

**A16 · major · partly — "Part I" modules import the Part II modules.**
- Where: `Loops`, `Observation` and `Onward` reach `Significance` and `Metaethics` through Testing → Feedback → Interdependence → Significance. 49 modules do so.
- Correction: none of them uses the axiom. This is a fact about import order, not a dependency on the axiom.
- Fix: now, say in the package README L131/133 that layers follow import order, not the Part I/Part II split. Later, factor the Significance-dependent part out of `Interdependence` (board claim plus a core run).
- Ren: no.

**A17 · minor · partly — Local overclaims.**
- `Frequency.lean:11-12, 26`; chapter L1297/L1648: "runaway is set by frequency, not strength" depends on Nat strengths ≥ 1. Add the qualifier to the doubling clause only.
- chapter L1495/1508: "a run from every configuration that can move is given". `Onward` gives this only within finitely many configurations or with a recognising test; in general it is equivalent to dependent choice.
- `Coupling.lean:49, 365-392`; chapter L1507: "no move needs supplying from outside the whole" is a re-encoding (a clock rest takes the moves as data).
- Learning header; chapter L572: "the uniformity of nature is no premise". It is a named local hypothesis (`Lumped`, held lists) of every positive theorem.
- chapter L62/67/95/100: "law (no premise)" covers local hypotheses. Write "no global premise; local conditions are written into each law".
- GLOSSARY.md:402, MAP.md:202, BOOKS.md:206: SSBX Lean claims stated as fact (0 sorry, 0 axioms). No such Lean is in the repository. COVERAGE.md:40 reports about 150 sorry.
- `chapter/RECIPIENT-CORRECTION`-style headline lemmas presented as "general theorems" (see To check).
- Ren: no.

**A18 · minor · partly — Integration is overstated.**
- Where: chapter §9 "All new formal results are stated on one spine".
- Why: THEOREM-CONNECTIVITY reports 1,019 of 7,214 theorems apart (792 on the extended base), 65 components, and every `families_reach_each_other` false. The families meet only by correspondence theorems. The chapter never cites this.
- Fix: add a §8 integration row with these counts and one qualifying sentence in §9.
- Ren: no.

**A19 · minor · partly — Empirical overclaim.**
- Where: generativity chain M20 (`GENERATIVITY-CHAIN.md:101`), "direct empirical support, completing the targeted operational evidence synthesis".
- Why: six published studies were selected after Ren's 10-08 remark. They are compatible exemplars, not tests that discriminate this theory from the alternatives.
- Fix: propose the qualifier "published experiments instantiate …" through the chain workflow.
- Ren: yes (curated view).

---

## (b) Stale or inconsistent canonical text

**B1 · major · confirmed — Chinese and English contradict each other on who decided the 生/生生 readings.**
- Where:
  - chapter item 11: zh L93 says the AI decided on Ren's 15 October delegation (D1); en L126 says "the readings … are Ren's";
  - §6.3: zh L748 ends "本章不替 Ren 作出" (the chapter does not decide for Ren); en L757 says the AI decided under D1.
- Why: `DELEGATED-CHOICES.md:53` records D1 as an AI decision. Each language is wrong in one place.
- Fix: en L126 → "decided by the AI on Ren's delegation of 15 October 2026 (生生 read as the generative space, D1)". zh L748 last sentence → the D1 decision.
- Related, the holding and conservation readings: zh L513 says they were adopted on the delegation; en L517 says they "await Ren". Reviewers disagree: one says align en to D5, the other says list them as awaiting Ren. Default: align en to zh, unless the integrator finds D5 does not cover them.
- Ren: only for the L517 scope question.

**B2 · major · confirmed / partly — The 11 October G0 fold and the 16 October Part II fold are not propagated.** The theory no longer asserts the axiom; it is the condition of §6.15. These places still assert or presuppose the old status:
- Chapter:
  - §6.8–6.12 are patched by a global reading rule (L698/700) instead of being edited ("Before Ren decides whether the axiom of Part II replaces G0", L1005/1025; L1003 heading; L872/887);
  - §6.7 "Center, one axiom" reads N_std as the one axiom (L828/849; also L89/122, L147 vs L143);
  - §6.15 bullet leads are unconditional (L1104/1122);
  - 94 "(Part I)/（第一部分）" tags and the "Part I: Without axiom" heading remain with no Part II (L171-175).
- Chapters:
  - `G0-WARRANT.md` L3/5/11/96 ("an adopted axiom"; listed as active in §11);
  - `ALIGNMENT-DIRECTION.md` L27/33;
  - `PRACTICAL-JUDGMENT.md` L19, and L67 (added 10-13: "Part II's axiom makes G0 hold");
  - `UNIFIED-ETHICAL-GROUNDING.md` L3-9;
  - `KNOWLEDGE.md` L188/254/264; `SHENGSHENG.md` L3/174; `THEORY-OF-BECOMING.md` L91;
  - `THE-THEORY-OF-EVOLUTION.md` L112; `WISDOM-AND-CONTEXT.md` L200.
- Plans: `RF/CONTINUATION-GROUNDING-PLAN.md` L3; `RF/BECOMING-UNIFICATION-PLAN.md` §10 L313/471 (23 inbound anchor links); `RF/PART-II-INVENTORY.md` §4 L161.
- Lean docstrings and README:
  - `Relevance.lean` header (missed by P129; 18 uses); `Metaethics.lean:52-53`; `Boundaries.lean:12-16, 145-147, 409`; `Bridge.lean:57-61, 419`; `Standpoints.lean:75-78`; `Response.lean:289`; `Significance.lean:106, 119`;
  - `Order.lean:155`, garbled by P129;
  - package README L89 "(Part II asserts it)".
- Records:
  - `one-axiom-yields-g0` L145, `significance-retained-within-margin` L23 and `whole-first-and-bounded-centers` L78 call it "Ren's axiom" with no P128 status;
  - the dependency conditions of 4 records still say "pending Ren" for readings delegated in D11–D21.
- Goals and AGENTS:
  - AGENTS.md:19 ("G0 公理路线已获明确授权", the G0 axiom route is authorized);
  - GOALS.md:75 (generative-alignment premise);
  - README:174 "complete at its explicit-axiom scope";
  - `theory-of-becoming.json` premises say "G0 is folded (Ren)" and drop the record of his conditional wording (register L65).
- Views: chain C17 L1713 contradicts C03 L459; `ARGUMENTS-M-Z.md:1770-1782` ("theorem of Part II's one axiom"); THEORY-MAP becoming status.
- Fix:
  - Rewrite AI-authored current text in conditional, past tense (chapter §6, PRACTICAL-JUDGMENT L67, records, Lean docstrings in one batched docs-only landing).
  - For historical chapters, prepend a dated, bilingual, AI-labelled scope note and leave the body unchanged.
  - Partly corrections: do not retitle the UNIFIED-ETHICAL-GROUNDING H2 (its anchor is linked); do not rewrite the 8 October sentences in KNOWLEDGE, Ren's 10-08 quote in G0-WARRANT, or row 6 of THE-THEORY-OF-EVOLUTION.
- Ren: yes for AGENTS.md, GOALS premises and the chain; no for AI text.

**B3 · major · confirmed — §9 counts and receipt citation are stale.**
- Where: chapter L1526-1676 and L1678/1680.
- Why:
  - The chapter cites 20261015T231055 (7,089 theorems, 9,753 audits, 126-module closure, 131 modules). The current receipt has 7,214 spine-plus-bridge (6,918 core), 9,912 audits, a 132-module closure and 137 spine modules.
  - 18–19 row counts differ from the current receipt; 13 were already wrong against the old one. Examples: Flow 77/97, Population 112/130, Identity 99/119, Dissipation 89/110, Likeness 137/156, Admission 38/46, Roles 136/145, Reserve 72/84, Standing 38/37.
  - Thresholds (L1646) and Observation (L1647) have no count cell. GenerativeCore shows "继承" (inherited) where the receipt has 23 foundation theorems. The table sums to 6,607 core against 6,918.
- Fix: generate the count column and the receipt sentence from the frozen receipt in `becoming-checks/`, not from the fresh-run summary (whose receipt is in /private/tmp). Keep the hand-written content column. `lean-index.json` holds no per-module counts, so the source has to be the receipt's `modules[].theorems`.
- Ren: no.

**B4 · major · confirmed — P130 is absent from the canonical chapter.**
- Where: chapter (0 mentions of `Becoming.Runs`, CourseWorlds, LearnableRuns, ParityReadings, FinerTraces, FormedLoops, `worlds-are-runs`, `two-act-worlds-carry-the-difference`); §8 row L1386.
- Fix:
  - Add six §9 rows with counts.
  - Add a §1/§8 paragraph with the limits: exact correspondence; World is still defined without Process; `families_reach_each_other` stays false.
  - Bind the two records.
- Partly: do not adopt "the one root is the run" (package README L124-129) as the theory's reading without Ren. Mark it in the README as the AI's reading.
- Ren: yes for the reading.

**B5 · major · confirmed / partly — §8 status apparatus is incomplete.**
- Where: chapter L1400, L1421-1450, L1512/1514.
- Why:
  - Reviews: the list stops at the 16th. Missing are the 15th (`BECOMING-R1-R2-REVIEW.md`), the 17th (`BECOMING-GENERAL-LAWS-REVIEW.md`), the P49 review, the 18th (`BECOMING-EIGHTEENTH-REVIEW.md`) and the release-readiness review. P128–P130 have had no review. `BECOMING-P49-REVIEW.md` calls itself the sixteenth, colliding with the P42–P43 review.
  - "What stays Ren's" omits the readings marked pending in the body: Onward L243/245, Tail L475/477, Remainder L487/489, Observation L503/505, Frequency L507/509, the P130 records, I4b-4 and `whole-first-and-bounded-centers`.
  - `Remainder.lean:76-95` is headed "pending Ren" but contains readings Ren took.
  - Partly: whether Ren's 10-16 "agree with other readings" ratifies D1–D39 is open (R18 D-f). D1, D5, D22 and D39(4) read his central terms 生生, 生生不息 and "entangled" (R18 D-a). Add this as a question; do not relabel, since the chapter already labels these as AI decisions.
  - The "Further proofs" list is mostly closed results (26 "is given" against 8 open clauses).
- Fix: generate a review ledger and a pending-Ren register. Build the register from non-history `correspondence` fields (82 records contain the string, many only in history), cross-checked against DELEGATED-CHOICES. Keep one clause of context per closed bullet.
- Ren: yes for the D1–D39 question.

**B6 · major · confirmed / partly — Records lag work that has landed.**
- `laws-of-one-step.json` L179/221/363 still lists finer units, coarser steps and continuous time as untested; Units, Sampling and Tower landed 10-12. `laws-at-finer-units.json:263` is the same.
- `subthreshold-registration.json` L176/352 says loops, gain and runaway are undefined; Runaway, Gain, Loops and Thresholds have landed.
- `recurrence-without-premise.json` L98/251 says the entropy instances are not given; `Becoming.Entropy`, landed 5cf28c742, gives them. Its validation says 40 modules in English and 75 in Chinese (To check).
- Partly: `own-count-misses-joint-excess` L169 and `support-from-the-supported` L176 ask for instances that RenewalBridge already gives.
- `theory-of-becoming-foundation` (the central open target) records no progress after P30. Correction: Ren keeps the status and target wording; add progress entries and edges with him.
- About 57 records have `validation_scope` prose that disagrees with their `proof_bindings`; 17 name no bound receipt. Fix: generate the current-receipt clause from the bindings and keep the old citations as history.
- 9 records corrected by R18 still say "not independently reviewed". Partly: R18 was an AI read-only review, so write "reviewed by R18 (AI, read-only)", not "independently". Ren decides whether it counts as the review asked for.
- 21 records cite proof files with no receipt binding. Partly: bind spine references only after confirming each declaration appears in the receipt's audits, not on a hash match.
- Fix for the root cause: render a "used by" list on record pages so hub records see their downstream work.
- Ren: only for the R18 question and the target framing.

**B7 · major · confirmed — Workboard and goals are stale.**
- Board (`_process/BECOMING-WORKBOARD.md`):
  - rows 41-45, 48, 50, 51 (P127–P118) say "handed to the integrator", and row 60 (P108) says "lands with batch 5", although all have landed (1a78f978, 83081fe1, 8effd116, ed704543, 17edc6d2, 09218b82, 8188bc30, 3b7f1c98, 6037767f);
  - row 51 says P118's readings are pending although Ren took them;
  - row 152 says Part II "awaits Ren" although P128 folded it; Target L26 still says "Part I first, then Part II";
  - I5 row 39 says "fresh run pending" (it passed, 0cfb9c56);
  - "Current continuation" L190-196 is the 13 October text, ending "not pushed";
  - no current integrator is named (row 81 is the 10-13 Codex handover);
  - the W-root owner has been inactive since 10-13 and the target is open.
- Goals: `theory-of-becoming.json` `next_step` is the 11 October redirect (4358d65d3), shown at README:146 and GOALS:204, and it has been carried out. `result_ids` lists 9 of 229 records; 192 records belong to no goal.
- Fix:
  - Board: add one clause to rule 4 letting the integrator append the landing commit to an owner's closed row, then update the cells. Name the integrator only on Ren's or the integrating session's confirmation. Ask Ren about the W-root ownership.
  - Goals: AGENTS.md limits goal edits to authorization changes, so either Ren approves a scope-text update or `render` takes "Next" from the target record's `next_delta`.
  - Reviewers disagree: board-1 needs no rule-4 change beyond that clause; nav-17 would amend rule 4 to move landed rows. Do the clause first and the move later.
- Ren: yes.

**B8 · major · confirmed — The required method page still calls the whole "generative".**
- Where: `chapters/NONDUAL-METHOD.md` L7, L9, L79. The closing L119 points to the historical GENERATIVE-GROUNDING and FOUNDATION-PREMISES; L111 is a 6 October "next join".
- Why: P36b (ba3b0e3b) recorded Ren's correction but deferred the body sweep. P36b is tracked nowhere on the board.
- Fix: rewrite with Ren's approval and keep a dated history copy. Record on the board that the chapter part of P36b is done and that the GOALS wording is open for Ren.
- Ren: yes.

**B9 · major · confirmed / partly — Chapters lag their records' spine restatements.**
- `MARKETS-AND-GENERATIVE-REGIMES.md` L178-200: the records now state Viability and Lasting laws with MarketInstances, and `cover_exact`. L190 still says the bound is "not claimed minimal".
- `BECOMING-FOUNDATION.md` L14, L66-82: the completion audit stops at P23–P30, yet the canonical item 11 cites it for "what remains open"; row 1 treats overlap as Ren's open choice against D2. Partly: keep the 10-09 table verbatim as dated history (3 records bind the file's sha) and add the current audit above it.
- `ALIGNMENT-THROUGH-CHANGE.md` L7/65 (partly): the abstract covers only §§1–5. Add a dated summary of §§6–14 and the spine forms.
- `THE-THEORY-OF-EVOLUTION.md` L3-29: 15 dated banners; the requirement table omits the descent and transmission records.
- Fix: dated "on the spine" notes, and bilingual banners where needed.
- Ren: no.

**B10 · major · confirmed / partly — The generativity chain is internally inconsistent and cannot be kept fresh.**
- Where: `theories/becoming/results/data/generativity-chain.json` and `GENERATIVITY-CHAIN.md`.
- Why:
  - C17 contradicts C03 on G0.
  - The 30 "Formal support" entries link 185 older Lean files and no spine module, apart from M15, M20, M21 and M24. Part I is absent.
  - Entries have become logs: M20 is 44,251 characters with 222 links, C14 25,148, M15 18,804. The page is 581 KB.
  - 30 of its 1,082 `reviewed_sources` are generated pages, so it is always "needs-review". R18 P8 found 8 landings that refreshed fingerprints with no recorded reading (6dbf6b79, 2f95dda3, 8188bc30, 841527bd, 3b7f1c98, 94fdd24e, 09218b82, ff4d5f17).
  - The M15 fix (4cc696ae) has no closing note in the record, and `updated` is still 2026-10-14.
- Fix:
  - Through `RF/GENERATIVITY-CHAIN-INDEX-RECORD.md`: revise M15 and C17, add one Part I and §6.15 entry, and move the dated accumulations verbatim into the record under dated headings.
  - Replace fingerprints of generated views with their editable inputs once the reading is recorded. Make `generative_chain.py` refuse `--record-review` on generated paths.
  - AGENTS.md calls the chain "Ren's"; its own text says it is AI-authored at Ren's request.
- Ren: yes.

**B11 · major · confirmed — The reading catalogue and theory map are stale and route readers to pre-spine chapters.**
- Where: `theories/becoming/results/README.md` L25-30, `data/arguments-m-z.json:1527`, `ARGUMENTS-M-Z.md:1770-1782`, `data/theory-map.json:3`, `tools/research/reading_catalogue.py:134, 148, 151`, `tools/research/lean_catalogue.py:41-48`, `navigation.py:275`.
- Why:
  - The entry for the canonical chapter fails its source-hash check, which blocks rendering.
  - Its text still says G0 is "a theorem of Part II's one axiom", and its Lean list names about 78 of 137 modules.
  - "What foundation has been established?" routes to generative-grounding, foundation-premises and theory. The Lean question routes to GENERATIVE-CORE-LEAN (6 October, 599 audits).
  - The "Updated: 2026-10-08" date is hard-coded, yet every generated page calls this the "Full reading catalogue".
- Fix: reread and then refresh. Route to the canonical chapter (§9 and `lean/becoming/README.md` first, historical chapters as secondary evidence). Relabel it "Pre-unification reading catalogue (2026-10-08)". Derive dates from the data.
- Ren: no.

**B12 · major · confirmed / partly — Chinese and English are not on a par in the canonical chapter.**
- Why:
  - English §1–§5, §6.1–§6.7 and §7 are summaries. The zh/en byte ratio falls to 0.16–0.49 in places (e.g. §7 L1337-1349 → L1351), and English drops Lean names, record links and links to Ren's sources.
  - Chinese-only content: the premise-card cells, all 43 rows of the §8 status table, the §9 content column (92 of 149 rows) and its header, the §10 meaning column (190 of 192 rows), the §11 role column, and blocks at L610-620, 663-674, 343-347 and 630-633.
  - §6.14 zh and en are different texts (L1079-1085). zh L715 (G0 ⇒ premises direction nearly trivial) and Ren's quote at L706 have no English.
  - Partly: English L531 drops "balance is assumed stepwise only on registered conditions" and the "heuristic, not a statement" caveat.
  - Partly: OPENING and NONDUAL-METHOD are English-only. That is not a defect; offer Ren a Chinese edition.
- Fix: fill the premise card, the §8 four targets and the §10 meaning column first. Add a warning-level parity check to `tools/research`. There is none now; 76 record field mismatches went uncaught, including the 40-vs-75 error in B6.
- Ren: only for OPENING.

**B13 · major · confirmed / partly — Term collisions across languages and glossaries.**
- `不息` → "unceasing generation" means the weak predicate `Unceasing` (L1719), while GLOSSARY.md:422 uses the same English for Ren's normative 生生不息. Rename the English to "unceasing arising" (L110 already says "arising without end"). Change `unceasing-generation-needs-renewal`'s title.en and keep the id and an alias.
- Partly: Chinese 生成 has three senses: the whole (生成之论), formation, and generative/generation (生成的空间). Put the split to Ren with the evidence.
- Two glossaries with no cross-links: GLOSSARY.md:3 claims to be "the canonical vocabulary of the corpus" (189 KB, no Becoming terms), while chapter §10 has 192 rows bound to Lean names. Only 1 headword (理) is shared, and senses diverge (理 "pattern" at :816 against Ren's 10-12 "modeling of laws" at L1836; 开/闭 at :297/302/360).
- Fix: keep GLOSSARY.md at its path. Add a scope header, a "Becoming spine terms" pointer and a sense crosswalk. Link both ways.
- Ren: yes for 生成 and for moving GLOSSARY.md.

**B14 · major · confirmed — Root corpus pages read as current.**
- Where: MAP.md, TIMELINE.md, BOOKS.md, GLOSSARY.md, `_process/THEORY-DIGEST.md`.
- Why:
  - MAP.md is linked from every generated page as "Broader theory map" (`navigation.py:275`). It is frozen at 10-04, and its row for `theories/becoming` describes the old SSBX folder (L142).
  - 14 pointers from these pages to OPEN-QUESTIONS sections now land on the generated register.
  - TIMELINE ends at 10-04 and its header contradicts its own sections. BOOKS is a superseded plan. THEORY-DIGEST names a slug that no longer exists.
- Fix (partly): point `navigation.py:275` at `theories/becoming/results/THEORY-MAP.md`. Add dated headers. Later, move to history with reading editions and keep root stubs and anchors.
- Ren: yes for moves.

**B15 · major · partly — Decidedness is called both a representation commitment and not one.**
- Where:
  - chapter L62/95/1133 say "not a commitment";
  - chapter L218 lists "decidability when counting" among the method commitments;
  - `Space.lean:1033-1035` (`law_decides` docstring) vs `:270-272`;
  - `Counting.lean:193-194`; `Significance.lean:119-120`; OPENING `[^law]`.
- Why: the counting laws quantify over `[∀ t x, Decidable (w.web.active t x)]`, which is global decidability for every relatum (`Counting.lean:229-235, 313-317, 524-527`).
- Fix: state the global decidability as a condition of these laws (not yet local) in the docstrings and the chapter's Counting summary (L1274 and zh). Drop it from the L218 list. Claim a board item for a local refinement.
- Ren: yes for OPENING.

**B16 · minor · confirmed — Local inconsistencies inside the chapter.**
- L251-253 lists as open what L271-273 proves (least footprint, census under reorderings).
- §6.9 L903/915 states a reading that L905/917 then withdraws.
- Partly: the §1 opening, L179/189, still treats `World` as the starting point, against L66 and L199.
- `ZERO-PREMISE-PLAN.md` L143/154 records the imbalance relatum as adopted, but L185/189 says "not adopted"; the header L7/9 says "pending Ren", and Sampling is still described as "uncommitted" (L140/151/215). Partly: do not move the file (56 inbound links and bindings); add a dated status note at the top.
- Ren: no.

---

## (c) Navigation and indexing

**C1 · major · confirmed — The front page does not show what is proved.**
- Where: `_process/research-config.json` `readme_featured_results`; README L106-150.
- Why: the four featured records (`positive-ground-open-futures`, `alignment-direction-g0-j`, `practical-judgment-g0-j`, `conditional-foundation-assessment`) are pre-unification ethics records. They are the only records with overviews. 138 records have spine canonical sources, but only 7 are in any goal.
- Fix: Ren chooses a headline set of Part I results. Each needs a bilingual overview, which is AI prose and requires his wording approval (`registry.py:158`). Show status (conditional, open, etc.) on each.
- Ren: yes.

**C2 · major · partly — GOALS has no lifecycle.**
- Where: GOALS.md, `_process/goals/*.json`, `navigation.py:77, 155`.
- Why:
  - The first priority is section 11 of 15 because goals are rendered in filename order. The 10-08 source says to display it first.
  - Nine authorized-session scopes from 10-07 to 10-09 have no state. The meta-attractor integration completed on 10-13; explicit-axiom-route is completed; generative-foundation is superseded.
  - 11 of the 47 Ren sources dated 10-11 to 10-16 are linked from goals; `2026-10-12-move-towards-100` is not.
  - The `generative-foundation` completion criterion still points to the historical GENERATIVE-GROUNDING.
- Fix: generalise `completed-route` into a status field with values (active, completed, dormant, superseded, `superseded_by`). Order by status. Closed scopes keep their record and anchor.
- Ren: yes. He confirms each closure; also whether the 良知 goal (LIANGZHI-EVOLUTION) stays active.

**C3 · major · confirmed — The directive register is incomplete and unstructured.**
- Where: `_process/RESEARCH-DIRECTIVES.md`.
- Why:
  - AGENTS.md:3 says every retained authorization is linked there. The register links 55 of the 264 records in `sources/15`; 35 records appear in no index at all.
  - 19 records dated 10-09 to 10-16 are absent, including `2026-10-15-situational-and-the-whole-core.md` (L27, Ren's "keep note, not follow blindly"), `2026-10-14-relation-first-refounding`, `2026-10-16-loop-formation-and-policies-go` and `2026-10-12-rest-family-strengths`. The 10-08 empirical directives are also missing ("Pursue full experimental validation", `2026-10-08-relations-across-scales.md:86`).
  - 61 paragraphs sit under one heading with no anchors and in mixed date order. Superseded entries (L65, L71) are not marked.
- Fix: generate a complete directive index over `sources/15` and `sources/16`. Classify each record first, then add only retained authorizations to the curated register and mark superseded entries. Partly: do not hand-add records without classifying them.
- Ren: yes for active/superseded status.

**C4 · major · confirmed / partly — The study and development folders have no index.**
- Where: `RF/README.md`; `RF/BECOMING-RENEWAL-READING.md`; `RF/development/`.
- Why:
  - `RF/README.md` (generated, 45 lines) lists no studies. RF has 2,208 flat top-level files (about 63 live).
  - The main log `BECOMING-RENEWAL-READING.md` (2,388,244 B, §1–§165, cited by records as "study §N") is linked from no top page. Its title describes only P3b and it has no table of contents.
    - About 30 headings carry no P-label, and sections are in landing order.
    - The English summary is a 545 KB block of unanchored bold paragraphs.
    - 24 sections still say "receipt pending" (L8206–L10162).
    - P89–P105 are absent from it.
  - `development/` has 197 entries and 1,274 files, no index, and kit READMEs that do not name their landing. Nine kits are referenced from nowhere.
  - `BECOMING-UNIFICATION-PLAN.md` ends at P88 with no pointer to the board.
- Fix: change `navigation.py` so it generates a family index and a live-file list. Generate a separate study index (headings, Result and Delta blocks, receipt column, Ren-status column). Add standalone `<a id="en-N">` lines, which do not count as drift; never rewrite headings or the title.
- Partly: AGENTS.md forbids hand-appending to the generated index, and the log must not move or be renamed (path, sha and § citations).
- Ren: no.

**C5 · major · confirmed — OPEN-QUESTIONS hides what is open.**
- Where: OPEN-QUESTIONS.md (`navigation.py:253-254` reuses the register header).
- Why: it shows 4 targets under the header "229 records". It omits the chapter's §8 open programme (L1353, about 12 groups), Ren's pending decisions, and at least 9 specified but unrun empirical designs (e.g. `REWARD-LEARNING-AND-RECIPIENT-CHOICE.md:68-72`, `EMPIRICAL-SCOPE.md:38-40, 77`, `RECIPIENT-CUE-GROUNDING.md:78`, `RECIPIENT-HARM-AND-ACTION.md:91`, BIOLOGICAL-JOINT-VALIDATION). Lines 40-233 are 64 historical anchor stubs.
- Fix: give the page its own header, link `#8-开放纲领--open-programme`, and register one open target `empirical-discriminators` (run `make research-find` first).
- Ren: whether the 10-08 "full experimental validation" directive is active.

**C6 · major · confirmed / partly — Chapter files do not say whether they are current.**
- Where: `theories/becoming/chapters/`.
- Why:
  - 30 of the 31 D–G, 25 of 28 H–M and all 27 S–Z chapters have no link to the canonical chapter. None carries a status banner.
  - Several call themselves current: `HUIGEN.md:3-5`, `LIANGZHI-EVOLUTION.md:3`, `START-HERE.md:116` ("Generative grounding … the current foundational goal").
  - §11 names 24 of 139 chapter files and defers the rest to the 10-08 catalogue.
  - §11 lists the frozen `THEORY-OF-BECOMING.md` and `THE-THEORY-OF-EVOLUTION.md` as active. It omits the live canonical sources SCIENTIFIC-PHILOSOPHY, ZERO-AXIOM-PRACTICAL-JUDGMENT and WISDOM-AND-CONTEXT, and labels PRACTICAL-JUDGMENT and PLURAL-SYSTEMS "historical" although they are canonical sources.
  - `chapters/verification/` is unmentioned.
  - Other study entry pages also claim "latest" or "primary" (`RF/../REVIEW.md:5, 13`; `support-and-shared-generativity/README.md:3, 9`).
- Fix:
  - Add a structured `status` field to `arguments-a-l.json`/`arguments-m-z.json`, rendered by `reading_catalogue.py`, and generate §11 from it.
  - Add bilingual banners only where a chapter's self-label misleads. Banners are additions; bodies, including Ren's quotes, stay byte-unchanged.
  - Refresh `source_sha256` only after rereading.
  - Add forward links where a "next step" was later done (e.g. PAID-PREIMPORT-EVIDENCE → RECIPIENT-REASON-REVISION).
  - Do not edit REVIEW.md (manifest-bound); add a new folder README instead.
- Ren: no.

**C7 · major · confirmed — Experiment and Lean entry pages never reach the spine.**
- Why:
  - None of the READMEs on the path IC → general-framework → generative-basis → `L/README.md` links `L/becoming/README.md`.
  - `experiments/README.md` L49 says experiments are "not part of the canonical theory corpus", and L73 calls IC "Earlier models". It holds 23 dated paragraphs, last edited 10-06.
  - `L/README.md` is a 6 October changelog that never links the package and lists OutcomeContinuation twice (L60, L65).
  - The deeper/ and inquiry-root/ READMEs omit 88 of 167 modules.
  - `universal-ethics` READMEs index 7 of 41 and 15 of 89 modules.
  - The `systems-complexity` README covers 14 of 28 modules, missing the three joined modules that records cite.
  - Market READMEs omit MarketInstances, VersionedTaskInstances and SharedStockInstances, which records bind.
  - `shared-renewal-capability` hides a 16-level nested line behind "Current v0.9".
  - The spine's own path names three superseded 5-October studies (IC-13).
- Fix: index READMEs with a lead pointer to the spine. Move dated paragraphs byte-for-byte to `HISTORY.md` files registered in the history manifest. Generate module tables from receipts. Do not move the spine without Ren's go and the freeze-aware tooling (E3).
- Ren: yes only for moving the path.

**C8 · major · confirmed — Module lists disagree with each other and with the checker.**
- Where: package README L12-133, `L/becoming/Becoming.lean`, chapter §9.
- Why:
  - The README layer table has 106 rows and misses 22 core modules (961 theorems: Assurance, Composition, ContinuingRevision, Copying, Countdown, CrossSituational, Gated, Granularity, Joining, Keeping, Lasting, Likeness, Postponement, Readout, ReferencePlan, Regrouping, RegroupingSelection, Retrodiction, Revision, Segmentation, TimedResponse, Viability).
  - The "Three rings" row names only `Becoming.Bridge`, of 8 BRIDGE modules (`check_becoming.py:82`). CompositionBridge appears in neither the README nor `Becoming.lean`.
  - The root docstring has 122 bullets for 128 imports.
  - "Each layer imports only those below it" is false: Assurance imports Joint and Lasting imports Likeness.
  - `Becoming.FallibleInquiry` sits in `Becoming/` but is periphery (own checker; 17 of 37 declarations on propext/Quot.sound) and is listed nowhere.
- Fix: generate the module, layer, ring and count columns from CORE/BRIDGE and the receipt, keeping the curated content cells. Mark FallibleInquiry as periphery in place; moving it risks the checker's stem resolution.
- Ren: no.

**C9 · major · confirmed — The Lean catalogue hides the pure core.**
- Where: `tools/research/lean_catalogue.py:176, 192-193`; `results/LEAN-INDEX.md`; `lean-declarations/ethics.md`.
- Why:
  - The "core" group holds 275 files: 138 spine, 95 deeper, 32 lean-root and 10 naturalism.
  - Its concept entry is the 10-06 GENERATIVE-CORE-LEAN chapter, and it shows no receipt figures.
  - All 144 universal-ethics modules, including neural calculus and kitchen transitions, are filed under "Normative grounding". Only 9 of the 24 records canonical there are F07.
  - Periphery declarations use namespace `Becoming`.
  - The index is stale by four rows after P130.
- Fix: group by the receipt's `core_modules`, `foundation_modules` and `bridge_modules`, with the rest as periphery; use §9 as the concept entry. Group the ethics catalogue by a checked-in mapping. Split MODULE-CLASSIFICATION's "Spine" column into core and periphery instances.
- Ren: only for any namespace change.

**C10 · major · confirmed / partly — Record navigation misfiles and omits results.**
- Family F07 ("Practical judgment under explicit axioms") holds 12 axiom-free structural records, e.g. `how-loops-form`, `observation-is-a-route`, `what-a-cut-loses`, `where-a-run-goes-on`. F01 holds 99 records. F22 is used by 12 records but is undefined.
  - Fix: add a Part I family to `session-results.json`, re-tag records in their JSON, and validate families against a list (`registry.py:461`).
- Becoming.Viability is owned by one record titled for a market application; Stock's general laws are restated in six application records.
  - Fix: split out a general-law record from the existing one; do not duplicate it.
- 15 records name the chapter as their "statement" source but the chapter never names them. Ten more spine records whose results the chapter states are never linked.
  - Fix: add the links, then add a warning-level check (partly: not a hard error).
- The I4b logical-strength results are absent from Part I and from the §8 logical-commitment paragraph L1460/1468: `origin_of_propositions_iff` (double-negation elimination), `refutable_passes_iff_markov`, `eitherThroughout_iff_llpoForDecided` (LLPO), option-model selection.
- Partly: "Part I stated whole" omits 37 core modules (1,406 theorems), and L1300 points to sections that do not contain them. Reword L1300 and generate the §9 catalogue; do not pad the summary.
- Partly: dependency edges encode shared definitions (about 32 of 285 a–l edges), so premises seem to propagate.
- Partly: strong periphery results have no record (`renewal_closure_theorem`, naturalism countermodels). Address this when the line is claimed.
- Ren: no.

**C11 · major · confirmed — `research-find` blind spots.**
- Where: `tools/research/research.py`; Makefile L10-11.
- Why:
  - Files over 2,000,000 B are skipped (`research.py:145`), so the main study log cannot be found.
  - `sources/` is excluded by default (L113-123), so Ren's directives cannot be found.
  - `development/` (landing reports, I5 summary) is excluded, while 103 frozen md/py files are searched.
  - Three different evidence classifiers disagree: `research.working`, `lean_catalogue.path_role` and the rename "preserved" list.
- Fix: one classifier in `tools/research/paths.py`; apply the size cap only to evidence paths; add a `directive-find` target (partly: keep the default scope).
- Ren: no.

**C12 · major · confirmed — The sources index is stale and broken.**
- Where: `sources/SOURCES.md`; source READMEs; group 20.
- Why:
  - SOURCES.md has 43 broken links to `../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/…` (L17, 238, 298, 348, 358, 406, 410, 420, 422, 454-506, 1971, 1999-2005, 2028, 2042). Each maps 1:1 to `theories/becoming/chapters/`.
  - 14 more broken links are in AI-authored source READMEs (21/, 22/LOCATIONS.md, 23/, 41/, evolutionary-selection).
  - SOURCES.md is a 369 KB layered log, last edited 10-09: the original header sits at L416, the stated total is 1,811 against 6,373 tracked files, and the developmental-attention and market-generativity groups are missing.
  - Group 20 (2,402 files, 341 MB of AI session output) has no README.
- Fix: remap the links and record them as a labelled link adaptation. Freeze the current SOURCES.md in history and generate a new index from a per-group registry (`sources/GROUPS.json`) plus `sources/README.md`. Add a README to group 20.
- Ren: no, except visibility (F2).

**C13 · major · partly — There is no empirical evidence index.**
- Why:
  - Chapter §8 "Empirical correspondence" (L1470) links no evidence.
  - `EMPIRICAL-SCOPE.md` (10-06 baseline) omits the 10-07 to 10-09 work (TCLab, Heald recovery, naming, ecology, kitchen).
  - Only 4 of 229 records are public-data assessments. Dickson (+10.07 pp) and DeCaro (+42.59 pp) are cited nowhere in `theories/`.
- Fix: generate `theories/becoming/results/EVIDENCE.md` from catalogue categories and assessment records. Migrate the analyses into assessment records, starting with gap-resolution. Link from §8.
- Ren: yes for the §8 link (canonical edit).

**C14 · major · confirmed / partly — Drafts and other top-level directories are unlocated.**
- `drafts/2026-10-02-iaseai-selecting-the-selectors/NOTES.md` presents v2, but the line ran to v7.3; whether anything was submitted is unrecorded.
- Partly: AGENTS.md L37 and BRIEF omit drafts/, output/, tmp/, worldbuilding/ and work/. Add them through the generator.
- The 14 frozen branch READMEs carry no status or pointer.
- Three "becoming claim N" citations dangle: drives:68 → 257, relational-self:77 → 296, zhishan:228 → 343. Retarget them to `_process/architecture/history/7ef46d1177ecd336/README.md` and its reading edition.
- Ren: yes for the submission status and which mission line is current.

**C15 · minor · partly — Start paths.**
- AGENTS.md:3 sends new agents to RESEARCH.md (a bare table) and BRIEF.md (boilerplate). Change the BRIEF generator; AGENTS.md edits are Ren's.
- The chain maintenance workflow is buried at L510 of 1,146 in `GENERATIVITY-CHAIN-INDEX-RECORD.md`. Link the anchor directly.
- "Eight parts" (README:104, `navigation.py:244`) now collides with Part I.
- The board's R18 row does not link `BECOMING-EIGHTEENTH-REVIEW.md`.
- Partly: 16 universal-grounding attempts have no joining ledger (`RF/WHOLE-*`, `YITI-REN-*`, etc.).
- Partly: the ALIGNMENT-COMPLETION seven requirements are an open target with no record. Run `research-find`, then create a target record or extend `alignment-direction-g0-j`.
- Partly: EXPLANATORY-NECESSITY's first-order/Cantor result (§§77-82) is linked from neither the chapter nor the records.
- Ren: yes for AGENTS.md.

---

## (d) Duplication and bloat

**D1 · major · confirmed — The canonical chapter is 962,442 B and states the theory three times.**
- Where: chapter.
- Why:
  - "The theory stated in full" is 71.8 KB. Items 3 and 4 are single paragraphs of 8.4–12.4 KB (L73, 77, 106, 110). 172 of its 196 identifiers are absent from the §1–§5 body.
  - "Part I stated whole" is 108 KB, with bullets up to 3,669 characters and material "kept as research notes" (L1177/1275).
  - §2 is 153 KB and has absorbed the propagation, loops and closing cluster (L479-509, 62 KB) and response/counterfactual (L467-477).
  - Lines 1–695 hold 88 ISO dates and 78 delegation formulas; §6 holds 47 more. Commit hashes, P-numbers and review counts are inline.
  - 104 records bind the whole-file sha, so every edit stales them; the P129 landing touched 299 files.
- Fix, as a staged board item owned by the integrator:
  - Keep a labelled frozen copy in the study.
  - Make one short status-labelled statement canonical at the same path, keeping anchors.
  - Generate the summary tables and the §9/§10 apparatus from records and the receipt.
  - Split parts into files with anchor stubs, and rebind records part by part after reading each change.
  - Partly: replace the repeated delegation formula with a compact tag ("[AI reading, D23]"); do not remove it, because AGENTS.md requires keeping Ren's words and AI elaboration apart.
- Ren: yes for retitling "Part I" and the opening's form.

**D2 · major · confirmed — Generated views duplicate each other.**
- Why:
  - The same 229-row table appears in RESULTS.md, RESEARCH.md, `theories/becoming/README.md` and `chapters/CLAIMS.md`, plus RESULT-REGISTER.md: about 350 KB, ungrouped.
  - `GOALS.md` and `results/ROADMAP.md` differ only in link base.
  - DEPENDENCIES.md is 555,205 B: 589 sections for 587 edges, with prose already rendered on record pages and no reverse index. It is linked from all 12 generated pages.
- Fix: keep the full table in RESULTS.md and make the others generated stubs. Render DEPENDENCIES as a compact table and add "Used by" to record pages.
- Partly: stubs keep every historical anchor and history-manifest entry. Check inbound links to RESULT-REGISTER first. Keep a stable `<a id>` per edge: 10 anchored inbound links exist, including from the chain.
- Ren: no.

**D3 · major · confirmed / partly — Record histories are mostly rebind boilerplate.**
- Why: the history field holds 6.5 MB of the 12.3 MB of record JSON (7,564 entries). About 5,365 entries (4.8 MB) only rebind or rehash with the claim unchanged; 1,052 come from chapter edits and 1,598 from the study-log hash. The rendered record pages total 11.0 MB.
- Fix: prefer render-side folding of pure re-points into a collapsed count. If entries move, snapshot first (`research.py snapshot`) and keep every entry that records a correction, review, Ren decision or narrowing. Going forward, write one reconciliation log per landing.
- Partly: do not split the study log to stop the churn. Scoped drift already absorbs appends, and a split would break path lookup and anchors.
- Ren: no.

**D4 · major · partly — The workboard is 276,352 B.**
- Why: 137 of 186 rows are landed. The item table runs P130→P89, then P42→P88. Rows of 3–6K characters carry scientific status, against the charter (L9). The 52 links to `#落地队列--landing-queue` land on struck-through 10-11 items.
- Fix: keep the path and headings. Move closed rows and the logs verbatim to a dated history page, leaving one-line stubs. Put the current queue first.
- Ren: yes, with the integrator, for the rule change.

**D5 · major · partly — Evidence run folders dominate the file count.**
- Why:
  - `L/becoming/becoming-checks` has 171 runs, 446 MB and 31,786 tracked files: 13,817 .lean copies (1,694 unique), 17,536 logs and 3,014 unique blobs in all.
  - `universal-ethics` has 345 runs; 271 (9,608 files, 156.7 MB) are unreferenced.
  - deeper/inquiry-root have 4,544 byte-identical files and 130 unreferenced runs. 23 of 35 periphery runs are unreferenced, as are 12 experiment run dirs.
  - 12,647 tracked files are empty. 71% of tracked files are run-folder copies.
- Correction: a move does not reduce the file count. Cited runs and the latest run per checker stay at their paths (E3). Any packing must keep each receipt verifiable through its `artifact_sha256` manifest, and history must stay under the Lean root in an ARCHIVE-matching folder.
- Fix: start with a sparse-checkout profile for worktrees and CI, which moves no data.
- Ren: yes for any packing.

**D6 · major · confirmed / partly — Chapters that accreted as session logs.**
- GENERATIVE-GROUNDING.md: 408,695 B; 74% dated status paragraphs, 181 of them before the first heading.
- UNIFIED-ETHICAL-GROUNDING.md: 411,836 B; one H2 of about 124 KB with 49 dated H3s.
- HUIGEN.md: 247 KB (§5 is 172 KB, 65 rounds). It has been replaced by the `wisdom-root` record, which cites CORE-CONSTRAINT-AND-WISDOM.
- ALIGNMENT-AND-GOVERNANCE.md: 106 KB, 57 dated paragraphs.
- ETHICAL-LEARNING.md: 215 KB, 88 rounds, §37 used twice, withdrawn §§67–74 inline. It is the canonical source of a record.
- PHILOSOPHICAL-ACCOUNT.md: the same two questions are closed at §10, §18, §22, §24 and §32.
- ZERO-AXIOM-PRACTICAL-JUDGMENT.md: 137 KB; §7 is still titled "Current blocked status".
- The mathematics line is spread over three overlapping status pages.
- Fix: keep paths and anchors (ETHICAL-LEARNING about 1,300 inbound anchor links, UNIFIED-ETHICAL-GROUNDING 2,544). Add a current head or banner and move dated preambles verbatim to linked history. Reread before refreshing `source_sha256` pins (GENERATIVE-GROUNDING has 15 or more). Move HUIGEN only through the rename mechanism with its consumers (`HUIGEN-CHECK.py`, the chain).
- Ren: yes for HUIGEN and the mathematics line.

**D7 · major · confirmed — `lean-index.json` churns on every landing.**
- Where: `theories/becoming/results/data/lean-index.json`.
- Why: 8,566,659 B, of which `contents_by_sha256` is 6.9 MB. 121 commits; one landing (4cc696aef) changed 225,678 lines.
- Fix: discover from `git ls-files`; drop the bodies of development attempts; mark the file `linguist-generated`; regenerate only at landings; update `session_map.py`.
- Ren: no.

**D8 · major · confirmed / partly — Landing kits duplicate each other.**
- Why:
  - 50 spent kits hold 48 spine-module copies, 40 of them byte-identical to the landing blobs.
  - Scripts are rewritten per landing: `apply_docs.py`×23, `make_records.py`×14, `repoint.py`×12, `update_records.py`×11.
  - About 800 files were added between 10-12 and 10-16.
  - 49 Becoming module copies outside the canonical directory pollute `git grep`.
  - 81 loose 10-06 snapshots sit at the top of development/. They are unique and linked from four chapters.
- Fix: a tested, spec-driven `tools/research/landing.py`. Kits stay byte-identical. Move them with a scripted rewrite: 12 records bind 7 kit files by sha, and 85 records link the readability migration tables from history prose. Exclude kit copies from search.
- Ren: no.

**D9 · major · partly — Module descriptions are maintained in five places.**
- Where: module headers; the `Becoming.lean` docstring (1,139 of 1,267 lines); the package README; chapter §9; `check_becoming.py` SCOPE (L88-1652, about 134 KB, copied into every receipt, 12.1 MB across runs). They have already diverged (README L89).
- Fix: fix README L89 now. Make module headers the source and generate the rest. Keep CORE in the checker, with an assert that it equals the root's imports.
- Ren: no.

**D10 · major · partly — Bulk that is not the theory.**
- `v6.2/planning` holds 300 multi-agent scratch files within 1,113 IASEAI files.
- worldbuilding has 159 MB of binaries, including a 15.6 MB zip whose members sit beside it.
- The publishing pipeline is split: builders in `tmp/pdfs`, PDFs in `output/pdf`, and the canvas source only as `output/pdf/generative-chiang-mai-2045.md`, against AGENTS' rule on exports.
- Fix: move whole folders with `git mv` and a manifest, no deduplication. Move builders to `drafts/<project>/build/` and the canvas source to a source location. Gitignore `tmp/` only after its tracked files have moved. Offer Ren LFS or a separate repo for the binaries.
- Ren: yes.

**D11 · minor · partly — Records and edit ledgers.**
- Records: F22 joining records share boilerplate `next_delta`; the carried-difference law is restated in three records without "special case of". Do not merge distinct claims.
- Edit ledgers (11.8 MB, 199 files): they look redundant with git, but 0 of 13 sampled `before_sha256` values exist in git. They are the only copy, so never replace them with git pointers.
- Ren: no.

---

## (e) Tooling and checking

**E1 · major · confirmed — CI gives no signal.**
- Where: `.github/workflows/research.yml:9`.
- Why: no run has started since 2026-10-15T16:38Z ("recent account payments have failed"). Before that, 18 runs failed at research-check: `actions/checkout@v4` defaults to depth 1, and `registry.reviewed_version` (`registry.py:46-80`) needs history, so a shallow clone reports drift for 248 bindings.
- Fix: `fetch-depth: 0` (or `filter: blob:none`), and report missing history as a warning.
- Ren: yes for billing.

**E2 · major · confirmed — `research-check` passes while four views are stale.**
- Why:
  - `lean_catalogue --check` reports 4 stale outputs. `reading_catalogue --check` reports a source-hash error. `generative_chain --check` says needs-review (36 modified sources). `session_map.render` differs from SESSION-RESULTS.md.
  - Most of these views have no top-line "generated" marker and are not in `generated-manifest.json`.
  - The manifest keeps an entry for the deleted page `selection-by-the-record-alone.md`.
  - `session_map --check` writes a tracked file.
  - Generator markers name legacy scripts (`registry.py:667, 700`).
- Fix: report these as named warnings, not errors (AGENTS.md: stale views must not block healthy records). Add markers and overwrite guards, prune the manifest, and make `--check` read-only.
- Ren: no.

**E3 · major · confirmed — Path assumptions make naive restructure moves break checks.**
- In `check_becoming.py`:
  - The foundation modules (`L/GenerativeCore.lean`, `L/inquiry-root/sufficiency/InquirySufficiency.lean`, `L/deeper/RelationalRenewal.lean`) are found by unique file stem across `L/`, skipping ARCHIVE-named directories (L1677-1688, assert L1709). There are 471 live copies of GenerativeCore.lean.
  - Inherited-module receipts are searched only under the Lean root (L1872-1891). 23 deeper modules are bound only by receipts inside run folders, and two modules by exactly one. 247 non-latest run folders are still cited.
  - The audit helpers are imported from the 7 October application checker `L/universal-ethics/generative-capacity/check.py` (L61-63), which 58 other checkers also use.
- In the research tools:
  - `reviewed_version` uses `git log --no-renames HEAD -- path`, so any `git mv` turns its pairs into drift.
  - `check_rename.py` hard-codes its receipt and reads only `moves[0][0]`.
  - Paths are hard-coded in `navigation.py:211, 273, 275`, `lean_catalogue` GROUPS L38-48, `reading_catalogue.py:194` and `session_map.py:23-29`. The chain uses a non-recursive glob, `root-foundation/*.md`.
  - 78 external scripts import tool internals, 86 set `parents[3]`, and 170 record history links are relative to `records/`.
- Moving the Lean tree as a whole touches 5,037 record path strings.
- Fix, as preconditions for any restructure:
  - No closure source under an ARCHIVE-matching directory, and no new duplicate stems.
  - Pin the FOUNDATION paths with the next core run.
  - Extract the audit helpers to `L/becoming/audit_support.py` and leave a shim.
  - Make `reviewed_version` follow a move manifest.
  - A generalised mover with per-batch receipts and tests.
  - History in same-depth sibling directories. Mirrored top-level history breaks every outward link; siblings break A 88 of 3,143, B 206 of 6,264, D 51 of 775.
  - Defer moving the Lean tree.
- Ren: yes for the plan.

**E4 · major · partly — Evidence that exists only in volatile places (act now).**
- Why:
  - The committed receipt is a cached run on 643c345c: 44 steps run, 659 reused, 270 reused origins outside the repository.
  - The fresh run on d21b311a (703 steps, 0 reused) is kept only as a summary whose `receipt` field points into `/private/tmp`. Its hash is truncated in `REPORT.md:89`, and the report omits the 99 core injEq constants.
  - The receipt cited by the entropy landing, `20261011T170859.998618Z` (385 files), exists only untracked in `.claude/worktrees/jolly-pike-140c94`.
  - `review-wt` (in /private/tmp) holds an untracked passed run `20261016T112106.917817Z`.
- Fix: copy all three, unchanged, into tracked evidence locations and record full sha256 values. No rerun is needed.
- Ren: no (this preserves data).

**E5 · major · confirmed / partly — Periphery receipts are stale against the current core and their own bytes.**
- Why:
  - 10 of 11 periphery instance receipts predate the current core. CorrectionInquiry: 67 of 113 closure modules changed, 23 core modules not in its closure. MachineInstances: 28 of 69 changed. LearningCorrespondence: 27 of 43 changed.
  - FallibleInquiry: 12 of 44 changed (it ran before P129).
  - The root build checker `L/check.py` now rejects at L160 after the I4c comment edits, while `L/README.md:70-72` still tells readers to run it.
  - The learning/, acquired-perspective/, naturalism and conditional/renewal receipts bind superseded bytes, and their READMEs do not say so.
  - 10 I4c-edited modules have no receipt for their current bytes. The edit also changed bytes pinned by 58–94 receipts per root file and by a preserved 5-September draft.
  - `StructuralInheritance.lean` (27 theorems) has never had a checker or receipt.
- Fix: one batched, cache-reusing periphery rerun, then rebind the records. Label stage receipts with the commits that changed their sources. Add an I4c byte-change manifest. Mark StructuralInheritance "unchecked".
- Ren: no.

**E6 · major · confirmed / partly — Historical checkers overwrite their own receipts.**
- Why: the root-foundation A–H slice has 147 such checkers, and in I–Z 114 of 118 write their CHECKS.json unconditionally. Six write `{"status":"checking"}` before asserting (ACQUIRED-BINDING, ACQUIRED-SEGMENTATION, COMPOSITIONAL-FORMATION, COMPOSITIONAL-TRANSMISSION, ENACTED-SCENE, EN…). They would now fail (e.g. `LIANGZHI-PRACTICAL-CHECK.py:46-48, 84`). `inquiry-root/check.py:99`, `chapters/verification/*` and experiment reproductions (shared-renewal, agentdojo) behave the same way.
- Fix: label them as point-in-time scripts bound to their commit. Never rerun one into its tracked receipt; restore any overwrite from git. Make new reproductions write to scratch.
- Ren: no.

**E7 · major · confirmed — The 10-09 rename broke frozen-input hashes.**
- Why:
  - `experiments/integrated-correction/selective-handoff/FREEZE.json` binds PROTOCOL.md at 7150bc30 (now c00a06f3), and `verify_results.py:205` now fails.
  - `FOUNDATION-ALTERNATIVE-ORIGINAL.md` was labelled "preserved byte for byte" and was rewritten.
  - The revisable-concern `context/MANIFEST.json` no longer matches.
  - Also affected: the cue and agentdojo freezes, EVALUATIVE-PLASTICITY, and `gap-resolution/MANIFEST.json` (10-11 rename). About 13 freeze-bound files in all.
- Fix: add a freeze-aware mode to `check_rename.py` that accepts the mapped `sha256_before → sha256_after`. Add one table in `_process/architecture/README.md` instead of per-experiment files. Restore original bytes only for files labelled byte-preserved, verifying `sha256_before`.
- Related: `agentdojo/independent-code-freeze.json` and the stochastic-prediction freeze were never committed in their frozen state, and only learned-claim-agents committed its freeze before its results. Say so once in the evidence index.
- Ren: no.

**E8 · major · confirmed — Git and disk hygiene.**
- Why:
  - 88 registered worktrees (54 in `.claude/worktrees`, 33 in /private/tmp, 1 in ~/.codex) use about 228 GB; 22 are prunable and 79 sit at commits already in main. The disk is 91% full (82 GiB free).
  - 142 local branches, 11 unmerged (8 with unique patch-ids).
  - About 1.9 GB of redundant packs and 344 MB of `tmp_obj`; auto-gc loops on warnings.
  - Only `gc.pruneExpire=never` is set, so reflog and worktree expiry still prune silently.
  - `.claude/worktrees/` is excluded only in `.git/info/exclude`, and the root `.gitignore` has 3 lines.
  - Codex refs pin a 185 MB non-LFS blob, so a mirror push would fail.
  - 789 paths exceed 260 bytes.
- Fix: report only until E4 is done. Then, with Ren's explicit go, use non-forced `git worktree remove`, set `gc.reflogExpire*` and `gc.worktreePruneExpire=never`, and expand the root `.gitignore`.
- Ren: yes.

**E9 · major · confirmed — Live tooling sits in dated study folders.**
- Why:
  - `rebind_batch.py` and `merge_records.py` (in `RF/development/becoming-general-laws-plan/integration/`, whose README says "not shared infrastructure (no tests)") ran in every landing up to today's notes-batch37.
  - `integration-i4a/table.py` generates MODULE-CLASSIFICATION.md.
  - Three divergent path classifiers exist: `SPINE-INTEGRATION.py:38-40`, `inventory.py:10` and `lean_catalogue.path_role`.
  - The landing kit and DECIDABILITY-INVENTORY generators, and the session-map tool data, also live in the study.
- Fix: promote these to `tools/research` with tests. Keep the originals with a pointer line.
- Ren: no.

**E10 · major · partly — Schema-1 backlog.**
- Why: 117 of 229 records are still schema 1 (54 of 106 in m–z). They produce 300 of 440 style warnings, including 66 process markers and 19 round-accretion warnings.
- Fix: migrate following `RESULT-WORKFLOW.md`, snapshot first, starting with the 19 round-accretion records.
- Ren: no.

**E11 · minor · partly — The other-studies verifier and Lean record bindings.**
- `2026-10-05-repository-reconciliation/verify_preservation.py` now fails with 60 errors while its saved receipt says passed. Keep the receipt and add a mapping layer in the new mover.
- Records with periphery receipts on an rc compiler or bound to pre-P129 spine bytes appear in To check.
- Ren: no.

---

## (f) Provenance and method

**F1 · critical · confirmed — A live-format OpenRouter API key is tracked and pushed.**
- Where:
  - `sources/14-claude-code-prompts/Users-ren-repos-context-runtime.md:7448`
  - `Users-ren-repos-ember.md:2679` and `:3006`
  - `Users-ren-repos-deepseek-harness.md:9557`
  - `_process/reading-notes/cb-03.md:945`
- Why: one distinct `sk-or-v1-` value has been on origin/main and all 9 `origin/claude/*` branches since b8591af (2026-09-25), so it is also in cloud and CI clones. No secret scan exists.
- Fix:
  1. Ren revokes the key at openrouter.ai. This is the only real remedy.
  2. Put a labelled redacted reading edition in HEAD and keep the originals in an untracked private store with their sha256.
  3. Do not rewrite history unless Ren decides to: about 362 cited commit hashes would change and every ref would need a force-push.
  4. Add a credential-pattern check to research-check.
- Also: an expired signed URL is kept in `sources/29-motor-learning-cost-2026-10-06/MANIFEST.json`.
- Ren: **yes, now.**

**F2 · major · partly — Private and third-party data is tracked and pushed.**
- Why:
  - Seven `sources/12-claude-ai-chats` files from 2026-03-21 to 03-24 concern a named third party's illness; one filename contains the name. Derived copies are in `_process/reading-notes/hb-02.md`, `_process/timeline-raw.tsv`, `_process/read-pass-1-plan.json` and `theories/memories-and-working-style/synthesis-all.md:37`.
  - Chats were selected by length and keyword, which pulled in mental-health, intimate, administrative and about 50 off-topic chats. `_ALL-719-INDEX.tsv` exposes all 719 titles.
  - `sources/14` is labelled "Ren's own long messages", but 517 of its 756 blocks (87.4% of characters) are harness task-notifications.
  - Friends' transcripts (97 files, a `friend_name` field) have no consent record.
  - 1,021 commits carry a corporate-domain author email.
  - Third-party field notes (Dali), server and mail infrastructure details, and Ren's email in 19 files (see To check).
- Fix: Ren sets an inclusion policy and decides on visibility (the remote is `github.com/yongxu/theories`). Selected files move to an untracked private store with their hashes, and index rows say "withheld". Add a dated correction note to the `sources/14` row (`SOURCES.md:442`). Add a `sharing_status` field per recording. Do not rewrite history.
- Ren: yes.

**F3 · major · partly — Ren's irreplaceable recordings are single local copies.**
- Why:
  - The 10-02 conversation (109.9 MB), the Soi Si Lom monologue (95.3 MB) and the airplane audio (7.9 MB) are gitignored. Meanwhile about 413 MB of re-downloadable CC0 Dryad MATs are committed as plain blobs.
  - The transcription pipelines exist only in ignored `tmp/friend-conversation-2026-10-02/` and `tmp/soi-si-lom-5-2/`, which the source README cites (L11).
- Fix: ask whether the originals exist elsewhere; if not, use LFS or a backed-up store keyed by the recorded sha256. Copy the pipeline scripts, without audio, into `sources/18-friend-conversations/<date>/pipeline/`.
- Ren: yes.

**F4 · major · confirmed — Governing Ren messages have no source records.**
- Why: about 10 messages exist only in transcripts or memory: the 10-14 general-laws plan, the open-issues plan ("please, do all"), P83c, P114, P121/P122, R18/P129/P130, and the 10-10 paper drop. 109 records quote them as "relayed by the integrating session" with no link. In addition:
  - Board row P121 quotes "let's finish both" with a link to a source that does not contain it, and the bullet parts are AI text Ren pasted back.
  - Board L36's "do a full review … fix all" joins two messages sent 18 minutes apart.
  - GOALS still lists the 10-08 wisdom-paper direction after the paper drop.
- Fix: write source records from the transcript's user messages (not from AI plans or memory), with session id and timestamps. Mark AI-recommended options Ren selected and AI-drafted replies he sent.
- Ren: confirm only; no decision needed.

**F5 · major · confirmed — Classical sources are credited only in Lean docstrings.**
- Why: the chapter has 0 occurrences of Gold, Bishop, Ishihara, Bridges, Abramsky, Arkhipov, Chebyshev and LLPO. §9 rows L1611, 1634, 1635, 1639 and 1641-1642 carry no credit, and neither does the package README.
- Fix: add a classical-sources cell to each §9 row (and to the generated catalogue), and add LLPO to §8 (L1468).
- Ren: no.

**F6 · major · partly — Ren's words and AI elaboration are blurred.**
- About 15 AI research write-ups (305 KB) and 2 conversation exports sit among the directive records in `sources/15`. Do not move them (about 900 inbound references); index each file by kind.
- `SOURCES.md:416` says "every file under sources/ is a copy". In fact 262 directive records were created in the repository, with 21 edit commits.
- The chapter says six times that Ren adopted the imbalance relatum (L73, 106, 1581, 1631, 1726, 1727), and `Imbalance.lean:34-37` says the same. The source records this as the AI's reading of "please, finish all".
- Goal premises present "G0 is folded (Ren)" and drop his conditional wording.
- Three I4b records say "which Ren took", resting on the AI's reading of the scope of "agree with other readings".
- `Continuation.lean:4-8` attributes an AI restatement to Ren. `Generation.lean:9` says "the author's reading" without saying whose.
- AGENTS.md:33 calls the chain "Ren's".
- Register summaries drop "(AI's recommended option)".
- Translations are put in quotation marks as Ren's words (register L53, chapter L578).
- The OPENING header says v5 although the text is v6; the byline understates how much the AI reworded.
- Fix: a kind index for `sources/15`, and consistent status tags ("adopted on Ren's go to a proposal that included it (AI's reading)").
- Ren: yes for AGENTS.md and the OPENING header and byline.

**F7 · major · confirmed — The I4a classification rubric is false for 8 inherited modules.**
- Where: `RF/development/integration-i4a/RUBRIC.md:36`.
- Why: it says inherited modules are on the spine run and read by the bridge. No bridge or Instances declaration names these eight (173 theorems): ContinuationConditions 18, ExplanatoryNecessity 17, ExplanatoryStructure 17, CorePredication 12, KnowledgeCorrespondence 20, CompositionalAcquisition 25, CompositionalFormation 37, CompositionalTransmission 27.
  - The table was generated on receipt 20261015T164401. CorrectionRelations is now an earlier version of Gluing's `Cycle.met_iff_even`.
  - Partly: the table cannot serve as a basis for moving files. Earlier versions stay in place (20 of 31 have outside importers).
- Fix: correct L36, add rows for the 27 transitively inherited modules, and rerun `table.py` on the current receipt.
- Ren: only for category changes.

**F8 · minor · partly — Method concerns.**
- Game studies model joint activity with separate maximizers, against the relation-first method in AGENTS.md. They rest on hand proofs and are listed as current (`experiments/README.md:64-75`; JOINT-FORMATION-MATH, FORMATION). Label them historical; do not rewrite them (they are hash-pinned).
- About 35 third-party PDFs and full texts have no rights record, and the repository has no LICENSE. Two imported datasets sit outside `sources/`; DeCaro's redistribution licence is unverified. Add a `rights_status` field. Ren chooses a LICENSE before any public release.
- Ren: yes for the licence.

---

## Reviewer disagreements to resolve

- The English L517 holding/conservation readings: align to the Chinese (D5), or list them as awaiting Ren? (B1)
- Workboard: add an integrator clause to rule 4 now, and move landed rows later (B7, D4)?
- Study log: split it, or index it in place? The evidence favours indexing in place (C4, D3).
- `FallibleInquiry`: list it as periphery in place, or move it beside its periphery sources? The checker's stem resolution favours keeping it in place (C8, E3).

---

## To check (unverified minor findings, not folded into the items above)

**(a)**
- `ch6-11` chapter L1124: "universal reason needs no neutrality premise", while A is a neutrality (`Relevance.lean:227-236`).
- `ch6-21` L1038: reason 3 lacks its support-gated scope, and "should" is the AI's verdict.
- `ch695-17` L71/104 vs L549: `share_rises` is a special case of the selection term, not the term itself.
- `ch695-18` L105: "the selection results are corollaries" goes beyond the record.
- `coreEH-6` `FallibleInquiry.lean:414-421`: the "common nonzero residual" witness compares a course with itself.
- `coreLO-8` `LossMatching.lean:215-219`: the docstring claims both directions; the theorem gives one.
- `coreLO-9` `LossMatching.lean:15`: "not conversely" has no witness.
- `coreRS-8` `RepairComparison.lean:345-354`: `fragile_b3_better_than_none` states the opposite of its name.
- `core-sw-6` `Tower.lean:4`: `Strict` is satisfied by the identity, so nothing encodes "ever finer".
- `core-sw-10` `Typicality.lean:24-38`: numeric corollaries that Lean does not state.
- `core-or-5` `Quantum.lean:474`: "quantum states" are nonzero integer vectors.
- `core-lean-A-5` `Admission.lean:63`: "four things a part does" is not a theorem.
- `core-il-8` `Identification.lean:~779`: "the liar's truth" headline.
- `core-il-17` `Interdependence.lean:76`: "selection between wholes" has no formal counterpart.
- `coreLO-10` `Novelty.lean:48`: "gain must come from beyond" is not proved there (that is `Gain`).
- `coreLO-11` `Mechanism.lean:61`: the global vs run-relative state law is not stated.
- `core-sw-11` `Thresholds.lean:157`: "Every law reads everything" needs `Nonanticipating`.
- `core-sw-14` chapter L529: the falsifiability gloss is not marked as a reading.
- `records-a-l-13` `contextual-registration.json:14`: "realised by qubits" is not formalised.
- `records-a-l-14` overreaching aliases ("general theory of loops", "only obstruction", "gain").
- `records-a-l-15` `continuous-time-as-tower` title.
- `records-a-l-16` the Σ⁰₂-LEM identification is cited, not proved.
- `records-mz-14` "returns" means revisiting in `returning-novelty-forgetting-on-levels`.
- `records-mz-20` the `protection-priority-excludes-uniform-aggregation` id overstates the result (it excludes Nat scores).
- `opening-15` `Pair` witness (see A6).
- `opening-16` `[^no-law]` labelled "Proved".
- `opening-17` `[^aligned]` incentives are not formalised (Ren's text).
- `oth-12` `relational-self-and-datong/README.md:73`: "the paper proves" an unreviewed hand proof with objection I2 open.
- `chapters-DEFG-13` EVOLUTIONARY-ORGANIZATION "complete explanation".
- `chapters-DEFG-14` "independently accepted" without the internal-review qualifier.
- `chapters-HM-9` MATHEMATICAL-TRUTH heading.
- `chapters-NR-13`, `experiments-11` elementary lemmas presented as "general theorems".
- `chapters-s-z-14` THEORY-OF-BECOMING endpoint-loss criterion is definitional.
- `empirical-claims-9` MEASURED-FEEDBACK L5 "physical correspondence established".
- `empirical-claims-11` THE-THEORY-OF-EVOLUTION L73 ratios without CIs (n=5).
- `rf-iz-18`, `IC-12`, `src2-13`: "theorem" or "proves" for hand arguments.
- `rf-iz-19` 无明 framing.
- `other-studies-17` OPTIMAL-FOUNDATION "proved optimality".
- `lean-periphery-13` `L/README.md:19`: "exact correspondences" is an iterate-trace lemma.
- `lean-dic-12` inquiry-root "necessity" title.
- `chtail-19` OPENING "explains good and evil" (Ren's text).

**(b)**
- `ch695-22` L247-273: telegraphic register and stray spacing.
- `ch6-14` §6.2 cites no countermodel declarations.
- `ch6-16` dated 13 October paragraph opening §6.13.
- `ch6-20` the Nagel 1970 attribution.
- `chtail-22` L1364: the scientific-inquiry row says only "open".
- `core-sw-3` Units header says need-in-unit is "not done".
- `core-sw-4` Testing readings say loops are undefined.
- `core-sw-17` Unfolding docstring keeps a superseded reading.
- `coreLO-12` review-round notes in Openness docstrings.
- `coreRS-10` Revision docstring contains a process instruction.
- `core-or-10` Regrouping, RegroupingSelection and ReferencePlan headers use plan numbers.
- `core-sw-13` TimedResponse header.
- `rf-iz-8` PART-II-INVENTORY has no outcome note and cites `finite_reading_credits_consumption`.
- `rf-iz-9` THEOREM-CONNECTIVITY §3 shows superseded figures.
- `rf-iz-10` MODULE-CLASSIFICATION header says "draft".
- `rf-iz-13` plans cite renamed declarations (`reform_reabsorbed`, `comes_to_rest`).
- `rfAH-8` chain record lacks an M15 closing entry.
- `rfAH-9` chapter L1518 cites the 10-09 instance table as current.
- `study-log-10/11/12/14` ZERO-PREMISE plan counts, sessions, the PART2 set in the inventory script, the plan census.
- `chapters-abc-9` ASSUMPTION-FREE-FOUNDATION has no forward pointer.
- `chapters-abc-11` cognition catalogue Lean list.
- `chapters-DEFG-10/12/16/18` ETHICAL-FOUNDATION, GENERATIVE-CORE-LEAN, DAO and FORMAL-CORE have no forward notes.
- `chapters-HM-10/11/13/14/17` spine pointers missing; catalogue "Next" questions dated 10-08.
- `chapters-NR-8/9/10/12` NONINSTRUMENTAL-CONCERN has two §9s; §7 omits Ren's "responsive transformation"; RELATIONS-ACROSS-SCALES drift; PRE-QIN write-back.
- `chapters-s-z-10/11/12/13/15/16` WISDOM-AND-CONTEXT Part II; VALUATION-DEVELOPMENT 103 vs 130 (and `experiments/README.md:3`); SCIENTIFIC-PHILOSOPHY numbering; ZERO-AXIOM §7 heading; mechanism chapters' "next connection" sections; catalogue undercount.
- `records-a-l-17/19` constitutive-binding cites three receipts it does not reference; `next_delta` written as status; `reviewed_at` lagging.
- `records-mz-15/18/19/21` `worlds-are-runs` credits the wrong owner; `rest-at-every-resolution` should be marked research notes (Ren); canonical sources not where the headline lives; `one-step-missing-laws`.
- `bilingual-10/14/15/16/17` 40 vs 75 modules; zh-only Ren quote; one-language blocks; titles that differ in strength (普遍实践权威 vs "warrant"); provenance links missing in English.
- `older-4/12/13/14/15/17` GLOSSARY meta-attractor; TIMELINE, BOOKS, THEORY-DIGEST, CRITIQUE-FINDINGS, COVERAGE.
- `oth-13/16/19` OPENING-V6 copy; two mission lines; THEORY-DIGEST.
- `development-10/11` board "not pushed"; P77 inventory points to the kit's Listing.lean.
- `ue-9/12` I4c notes say "on the spine" for a non-spine declaration; spine-instances record has an old binding.
- `lean-dic-9` inquiry-root "current verification".
- `lean-dic-10` ExplanatoryInfiniteBranches hides two unstated theorems.
- `IC-6` three instance receipts on rc2 and pre-P129 spine bytes.
- `IC-7/8` unbound comment edits; generative-basis MANIFEST.
- `empirical-claims-10/16` pre-review status strings; gap-resolution manifest drift.
- `other-studies-14` "Generative Existence" label.
- `crosswalk-15/16/17/18` Boundaries docstring; ambiguous `significant_iff`; Coupling not cited at L1312; bridge taxonomy.

**(c)**
- `nav-19` architecture README says "nine" goal records (now 15).
- `nav-23` history store has no INDEX.
- `older-16/19/20` CLOUD-HANDOFF dead links; reading-notes inputs; absolute path GLOSSARY:13.
- `chtail-18` lineage syntheses at the becoming root.
- `chapters-abc-13/14/15/16` PAID/GENERATIVE filenames; `chapters/verification/` placement; missing Lean cross-references; unregistered U1–U3 results.
- `chapters-DEFG-17` before-copies not in the manifest.
- `chapters-HM-16` JOINT-FORMATION-MATH unlinked evidence.
- `rf-iz-12/14/20/21/22` PATIENT-GROUND dead links; 88 unreferenced files; 5 pages awaiting chain discovery; the "Universal Metaethical Core" heading (Ren); pre-10-09 JSON paths unnoted.
- `study-log-9/13` five-to-seven-fold descriptions; the log is not the complete chronicle.
- `development-12/14/15` scattered rename maps; duplicate groups; absolute development paths.
- `other-studies-10/12/15` unified-theory has no README; path:line links; duplicate entry-file names.
- `IC-5/9` inquiry-correspondence has no README; two "endogenous continuation" studies.
- `lean-dic-11` period lower bound has no record.
- `lean-periphery-11/12/15/18` inventory keyed by filename; loose row relations; orphan illustration; second README in `learning/`.
- `experiments-9/14/15` pre-rename links in working docs; circular-construction orphan; AI syntheses in `sources/15`.
- `src0015-8/13/14/15/16`, `src2-11/12/17`: duplicated folder numbers; listing counts; unnamed memory dirs; accumulating records; off-topic chats; group READMEs; single attachments.
- `core-or-11` Ranking declarations live in Relevance.lean.
- `coreEH-10` the Feedback namespace lives in Horizon.lean.
- `core-sw-16` leaf modules; Standing belongs to the closed selection layer.
- `ue-13` review probes sit among live modules.
- `lean-dic-14` FallibleInquiry (see C8).

**(d)**
- Duplicated helper lemmas across core modules (`core-lean-A-7/8`, `coreA-6/7/11`, `coreEH-11`, `core-il-14`, `coreLO-3/4`, `core-or-8/9/12`, `coreRS-7`, `core-sw-9/15`). Fix: one low-layer helper module in a single checked batch.
- Long headers (`coreLO-13`).
- `records-mz-16/17` duplicated `next_delta`; alias lists duplicate declarations.
- `ue-10/11` byte-identical snapshots; three receipt layouts.
- `lean-periphery-17` root verification/ logs duplicated.
- `experiments-8/13` 1,868 snapshot links; large raw outputs (55.4 MB runs.jsonl).
- `health-13/14` 198 MB duplicate working-tree blobs; study log rewritten per landing.
- `oth-13/15` duplicate PDFs and snapshot copies.
- `other-studies-18` foundation-assessment README.
- `empirical-claims-14` Heald MATs in plain git.

**(e)**
- `checking-7` cache key omits pass criteria.
- `checking-8` the prelude-only strip uses an exact-text regex; no guard on `debug.skipKernelTC` or `unsafe`.
- `checking-10/11/12/13` pin README wording; absolute paths in receipts; scanner location; 6 failed runs without `artifact_sha256`.
- `lean-dic-13` receipt schemas lacking a status field hide valid receipts.
- `lean-dic-6` connected/ checkers fail.
- `tools-14/16/19/20/21/24` `session_map --check` writes; dead `write_views`; legacy markers; slow tests coupled to package paths; external imports of tools; README overclaims coverage.
- `results-13/17` hard-coded dates; Lean catalogue includes untracked files.
- `restructure-impact-10/11/13/15` `path_role` ignores "history"; becoming-checks relocation; concurrent branches; MAP.md tie.
- `health-7/8/9/10/11/12/15` gc config; Codex refs; .gitignore; tmp/ and output/; long paths; LFS pointer files; untracked catalogue inputs.
- `experiments-12` reproductions overwrite evidence.
- `rf-iz-15/16` session-map data location; `parents[n]` depths.

**(f)**
- `privacy-9/11/12/13/14/15` infrastructure details; street-level folder names; third-party field notes; personal email; no secret scan; duplicate PDF.
- `src2-8/9/10/14/15/16` friends' transcripts without consent; untracked pipelines; Ren requests only in session JSON; receipt reference load (63k); LFS pointers; analysis in source READMEs.
- `src0015-9/10/11/12` duplicate imports; no export hashes; an AI note formatted as a Ren blockquote (`2026-10-09-arising-ceasing-names.md:5`); a dead link inside Ren's quote (add an AI note after it).
- `ren-attr-8/9/12/13/15/16/17/18/19` (see F4/F6).
- `core-il-7/10`, `core-or-13` loose classical citations (Fine–Wilf, WKL⇔LLPO without its choice caveat, the subset construction).
- `coreEH-14` "the author's reading".
- `rf-iz-11/17` root MANIFEST README mismatch; Lean probes compiled only in a scratchpad.
- `other-studies-9/11/13/16` historical release checker; Ceroni files in a study; START-HERE arithmetic; RenewalLedger and market packages not bridged to the spine.
- `ch6-23` standpoints are a free index type (nondual method).
- `IC-10/14` imported originals in experiments/; a "paid" package title.
- `empirical-claims-13/15` datasets outside `sources/`; signed URL.
- `experiments-10` canonical sources of 7 general-law records point to market modules (integrator decides).
- `lean-periphery-14` market vocabulary in READMEs.
- `coreA-5`, `coreEH-8/9/15`, `core-il-11/15/16`, `coreLO-5`, `core-or-14`, `core-lean-A-6`, `chapters-s-z-7`: naming (CoursesBridge, Depletes, `agrees_iff_even`, `price`, `statesBelow_shift` homonym, `decide` binder, `section Governance`, the OneStep title, Reading/Readings/Readout, ContinuingRevision, the THEORY-OF-BECOMING.md vs THE-THEORY-OF-BECOMING.md collision). Renames need Ren under board rule 8.
