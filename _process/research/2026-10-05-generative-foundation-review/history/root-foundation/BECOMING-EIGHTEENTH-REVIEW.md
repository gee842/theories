<a id="第十八次独立审查p107p127-与-i4b--eighteenth-independent-review-p107p127-and-i4b"></a>
# Eighteenth independent review: P107–P127 and I4b

> Some passages exist only in the [Chinese edition](BECOMING-EIGHTEENTH-REVIEW.zh.md): sections “Eighteenth independent review: P107–P127 and I4b”; “摘要”; “Errors”; “Overstatements”; “Presentation (true, but misleading or thin as stated)”.

Object:
- Study：`BECOMING-RENEWAL-READING.md` §125 与 §137–§161。
  - P107 `Novelty`、`Reading`、`Readings`；
  - P111 `Gain`；P112 `Gluing`；P113 `Sensitivity`；
  - P114 `Courses`、`CoursesBridge`；P115 `Propagation`；
  - P118 `Loops`；P120 `Remainder`；P121 `Routes`；P122 `Closing`；
  - P123 `Frequency`；P124 `Thresholds`；P125 `Observation`；P126 `Tail`；P127 `Onward`；
  - I4b-1 `Gated`；I4b-2 `Selection`；I4b-3 `Horizon`；I4b-4 `Lasting`。

The review ran in its own git worktree, on branch `r18-review`. As the task required:
- no `check_becoming.py` or `lake` build was run;
- no record, chapter, OPENING, README, GOALS or generated file was edited;
- the work board was not edited.

Lean was only read, with small Python scripts that extract statements and docstrings. Mathematics marked "reviewer's argument" is not Lean-checked.

Severity, as in the seventeenth review:

"Thin" means true and honestly stated, but close to a definition or a known small fact. It is not an error.

---

<a id="摘要"></a>

| 严重度 |
|---|
| error |
| overstatement |
| understatement |
| presentation |
| credit |
| confirmed |

## English summary

**Formal state.**
- No false Lean theorem was found, and every "exactly" checked is a genuine iff.
- The constructive calibrations are right:
  - WLPO and LPO in `Sensitivity` and `Tail`, with rule and Prop forms kept apart;
  - `RecursOrStops` in `Frequency`;
  - dependent choice in `Onward`;
  - double-negation elimination in `Gated`;
  - Markov's principle in `Horizon`.
- Every theorem with a ¬¬ conclusion carries the ¬¬ in Lean. The problems are in the prose: two records drop it.

**The problems are in the words, not the theorems.** There are four kinds.

1. **Three errors.**
   - The `what-a-finite-history-refutes` statement says that a reading with an adhering run outside it is "neither refutable nor verifiable". The Lean gives "not refutable" only, and eventual occurrence is a counterexample: it is verifiable in the process of all sequences.
   - The `Horizon` module doc says recurrence and eventual occurrence "are neither".
   - In `every-origin-passes-the-gate`, the zh of does_not_show 1 inverts the en.
2. **A constructive overstatement.** `Sensitivity` says that "with infinitely many conditions the condition cannot be dropped", and D37 says the reading "does not apply". But the counterexample `tailLaw` needs a decision of vanishing, which gives LPO, and any counterexample gives WLPO. In the core the condition is neither refuted nor shown droppable.
3. **The bound is attained by a law that is not gainless.** The supremum in `Propagation` is attained by `ExchangeLaw.carrying`. That law takes nothing and gives, so it breaks the first law (`Flow.Gainless`). "A held difference keeps arriving" and "every loop at least doubles" rest on this law and on natural strengths of at least one. Neither the records nor the reading Ren took say so.
4. **Necessity stated as identity.** Three places claim more than is proved, or claim what holds by construction:
   - `Observation`'s headline "Registering is being downstream";
   - the `Thresholds` statement "with no loop through the stock before it";
   - the formal half of "the situation makes it true" in `Situations`.

**Sound but thin.** These are not wrong:
- `Readings.Contextual.world_active` is `Iff.rfl`.
- The first conjunct of `World.unity` holds for every `World`.
- `Gain.rise_netGiver` is an accounting identity.
- `Closing.onLoop_iff_formed` is nearly definitional.
- `Situations.finerLaw_determined` is true by construction.
- `Parting.world_right_iff` gives the learner the whole world.
- The tying premises of `Reading.readOff` hold by construction.

**Credits.** Several standard sources are missing:
- Gold and Moore in `Parting`;
- Mermin, Abramsky et al. and Arkhipov in `Gluing`;
- Bishop, Bridges–Richman and Ishihara in `Sensitivity`;
- Akama–Berardi–Hayashi–Kohlenbach in `Tail` and `Frequency`;
- König in `Onward`;
- Alpern–Schneider and Kelly in `Horizon`;
- Goguen–Meseguer in `Observation`;
- LLPO and weak König in `Lasting`.

**Generativity chain.** Since the whole-chain review of 14 October (`e667f358`), 33 landings have refreshed 78 fingerprints in `generativity-chain.json` with "chain review recorded" in their messages. The index record has no entry after that date, and no chain entry mentions any module under review (P8).

<a id="0-范围与方法--scope-and-method"></a>
## 0. Scope and method

For each item the seven checks of the task were applied:
1. record against Lean;
2. satisfiable hypotheses, and no vacuous, `rfl` or by-construction headline;
3. classical credit;
4. honest scope: ¬¬ forms, decision oracles, rule vs Prop, finite vs general;
5. integration with the shared base;
6. readings against theorems;
7. zh/en equivalence.

Lean statements and docstrings were read for all modules in scope. All 21 records bound to them were read field by field (statement, laws, hypotheses, does_not_show, counterexamples, correspondence), in both languages. The study sections, the release-readiness review, `DELEGATED-CHOICES.md` (D1–D5, D22, D23, D37 and D39 in full, the rest by index) and its source were read. Proofs were read where a headline looked definitional.

Findings already made by the release-readiness review are not counted again. These are the re-definitions `Courses.anyChange` = `Parting.free` and `Parting.after` = `Run.onward`, the two roots, and the stale connectivity measure. The board has given them to P129 and P130.

Paths:
- *core* = `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`
- *rec* = `theories/becoming/results/records/`
- *study* = `BECOMING-RENEWAL-READING.md`

Lean line numbers are at `ce808d6a`.

<a id="1-发现表--findings-table"></a>
## 1. Findings table

### Errors

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| E1 | rec what-a-finite-history-refutes, statement en and zh | The statement says a reading with an adhering run outside it is "neither refutable nor verifiable". The Lean gives "not refutable" only. Non-verifiability needs a run inside that adheres to the complement. Eventual occurrence is a counterexample: the all-false run adheres to it from outside, yet it is verifiable (open). | error | `not_refutable_of_adheres` concludes `¬ Refutable L` from an adhering run outside `L`; `not_verifiable_of_adheres` needs `Adheres (¬ L ·) r` with `L r`. Law 2 of the same record states both halves correctly. | en: "a reading with an adhering run outside it is not refutable, and one with a run inside adhering to its complement is not verifiable"; zh likewise: "其外有附着运行的读法不可否证，其内有附着于补集的运行的读法不可证实". |
| E2 | `Horizon` module doc, *core* `Horizon.lean` l. 48–51 | "recurrence and eventual occurrence are neither" follows "not refutable … and dually not verifiable", so it reads as neither refutable nor verifiable. Both cited theorems are `_not_refutable`, and eventual occurrence is verifiable. | error | `Sequences.recurs_not_refutable` and `Sequences.eventually_not_refutable`. The record's law 2 correctly adds that never-occurring is not verifiable (`never_not_verifiable`). | "recurrence and eventual occurrence are not refutable (…), and never occurring is not verifiable (`Sequences.never_not_verifiable`)". |
| E3 | rec every-origin-passes-the-gate, does_not_show 1, zh | The en lists what is not shown: without deciding p, the first gated step at which p comes to hold. The zh says the origin law gives that first step, which inverts the en. | error | Compare the en: "Without deciding p, the first gated step at which p comes to hold (failing before it): the law gives a gated step after which p holds." `origin` gives some gated step, not the first. | zh: "不判定 p 时，第一个使 p 成立的门控步（之前 p 不成立）：律只给出一个之后 p 成立的门控步。" |

### Overstatements

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| O1 | `Sensitivity` module doc (*core* `Sensitivity.lean` l. 45); rec sensitivity-is-the-least-registration, statement zh and counterexample 0; D37 (1) | The doc says the condition "cannot be dropped"; counterexample 0 says that without it the least registration fails; D37 says the reading "does not apply". But `tailLaw` takes the vanishing decision `decides` as a parameter, and `lpo_of_vanish_decided` shows that decision gives LPO. Conversely, any counterexample gives WLPO (`wlpo_of_not_through_sensitive`). So in the core the condition is neither refuted nor shown droppable. It sits between WLPO and LPO. | overstatement | `tailLaw (decides : ∀ α, Decidable (VanishFrom α))`, l. 301; `tailLaw_no_least_registration` l. 357; `lpo_of_vanish_decided` l. 553; `wlpo_of_not_through_sensitive` l. 528. `Tail` (P126) states this calibration exactly; `Sensitivity` and D37 predate it and were not revised. | Doc: "With infinitely many conditions the condition cannot be dropped given a decision of vanishing (which gives LPO), and any law that drops it gives WLPO." Record: same in statement zh and counterexample 0. D37 (1): "with infinitely many conditions the reading is not shown to apply: given a decision of vanishing, the tail law has no least registration." |
| O2 | rec sensitivity-is-the-least-registration, statement en/zh and law 1 | `least_registration` concludes `¬ ¬ W.Registers obs h c`. The statement and law 1 say "the least registration" with no double negation. | overstatement | `ExchangeLaw.ReadsFinitely.least_registration`, l. 181. | Add "up to double negation" (zh "于双重否定下"), or state it for stable `Registers`. |
| O3 | `Propagation`; rec how-much-difference-arrives (does_not_show 2, counterexample 1, readings); D39 (3) | `most_difference_arrives` holds over all laws, and the supremum is attained by `ExchangeLaw.carrying`. That law takes nothing (`fun _ _ _ _ => 0`) and gives the strengths times the sum of all past levels, so it breaks `Flow.Gainless` as soon as it gives anything. The non-implication "bounded input does not imply bounded arrival … levels hold what they are given" and the reading "a held difference keeps arriving" (adopted in D39 (3)) rest on a law that creates amounts. Whether the bound is tight for gainless laws is not stated, and the record never mentions gainlessness. | overstatement | *core* `Propagation.lean` l. 641–648: "nothing is taken". `Flow.Gainless`: `total cs (L.give t f) ≤ total cs (L.take t f)` for closed families. | Record: say that the attaining law is not gainless, and that the bound is shown attained over all laws, not over gainless ones. D39 (3): add the same scope. Optional (S): state the gainless case, either tightness or a sharper bound that uses the stock. |
| O4 | `Loops`, `Frequency`; rec how-a-carried-difference-grows, how-often-couplings-act (statements, readings); Ren's taken P118 reading | "Each return at least doubles" and "whatever the strengths" hold only because strengths are natural numbers, a positive strength is at least one, and the carrying law does not dissipate (see also O3). With strengths below one (real amounts), the Neumann series converges for spectral radius below one, and frequent returns need not run away. `Frequency`'s does_not_show 3 concedes this, but the statements and readings are general. On 16 October 2026 Ren took "only a loop makes a difference run away … through every loop". Its sufficiency half, that every loop coupling at every step runs away, is an artefact of ℕ, and Ren should be told. | overstatement | `carried_doubles_return`, `SelfLoop.carried_eq` (D·(1 + M)^a); *rec* how-often-couplings-act does_not_show 3 ("a positive strength may be below one"). | Statements: add "with natural-number strengths, each positive one at least one" (zh "强度为自然数，正的强度至少为一"). Readings: say that the sufficiency half is the natural-number case. (P): ask Ren whether the taken reading stands with this scope. |
| O5 | `Observation` headline (*core* `Observation.lean` l. 12, 30, 274, 353); rec observation-is-a-route (title, statement, readings) | The headline claims identity. `apart_only_downstream` proves necessity only: what is not downstream stands alike. The converse, that what is downstream differs, fails, as does_not_show 0 concedes. The reading "observation is not a second kind of relation beside dependence" goes beyond the theorem: it shows observation does not exceed dependence, not that it is dependence. | overstatement | `apart_only_downstream` l. 285: `∀ t e, ¬ Upstream … c e → …alike`. | Headline: "Registering lies within the downstream" (zh "所识不出下游"). Statement: "a formation can register a difference only where it is downstream". (P): the reading. |
| O6 | rec loops-within-what-a-law-reads, statement en/zh | The statement says there is "no loop through the stock before it: that loop forms at the break". But the law's own strengths couple the stock to itself from the start, as counterexample 0 says. The loop-free law is the standing law, and the law acts as it before the break (`follows_standing_before`). What forms at the break is the loop that acts in the dynamics, not a loop of the strengths. | overstatement | `ReadsBelow.standing_no_loop`, `Flow.follows_standing_before`, `Draw.onLoop` (every strengths of the draw put the stock on a loop). | "Before the break the law acts as its standing law, which has no loop through the stock; the loop that acts forms at the break." Same in zh. |
| O7 | `Horizon` docstring of `Refutable.adheres_least` (l. 316) | "The least refutable reading": the theorem says only that every refutable reading containing K holds, up to double negation, at every run adhering to K. It does not show that `Adheres K` is itself refutable, so "least" is not shown. | overstatement | Statement at l. 317–320. | Docstring: "Refutable supersets hold where the subset is adhered to." Optional (S): prove `Refutable (Adheres K)` (closure is closed), which would earn "least". |
| O8 | `Gated` module doc, *core* `Gated.lean` l. 24 | "The law holds exactly where each gate is decided (`origin_of_decides`)". `origin_of_decides` proves sufficiency only. | overstatement | `origin_of_decides (decides : ∀ a, gate a ∨ ¬ gate a)` l. 181. | "the law holds where each gate is decided". |
| O9 | rec every-origin-passes-the-gate, statement en/zh | "With a propositional gate this is double-negation elimination" drops "asked of every process". For one process the law is not DNE. | overstatement | `origin_of_propositions_iff`; does_not_show 2 of the same record states it correctly. | Add "asked of every process" (zh "对每个过程都要求时"). |
| O10 | rec what-a-law-of-the-whole-and-no-part-takes (readings); `Tail` | The reading "the same whole … takes only the weak rule" treats `neverIndicator` and `vanishIndicator` as one whole. They coincide only classically. In the core they are two different laws. | overstatement | `Tail` docstrings; the two indicators read different properties (never 1 vs vanishing from some point). | Reading: "a whole of the same kind" or "a related whole". (P) if Ren has taken it. |
| O11 | rec orders-as-a-sum-over-histories, statement en/zh; rec how-loops-form statement | "A finite horizon is exact exactly where no loop lies upstream" drops its conditions: every condition listed, and formations and strengths the same at every step. "Before it forms growth is polynomial" in `how-loops-form` likewise drops "every condition listed". The laws have the conditions; the statements do not. | overstatement (minor) | Laws 5 and hypotheses of both records. | Add "with every condition listed and the law stationary" (zh "条件全部列出、律每步相同时"). |

### Understatements

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| U1 | `Lasting.EitherThroughout` (*core* `Likeness.lean` l. 1251); rec lifting-where-branching-is-finite | `EitherThroughout` 是：对两个判定的、向下封闭的序列 α、β，若每处 α 或 β，则 α 处处或 β 处处。审查者的论证（未经 Lean 检查）：它等价于 LLPO。<br>正方向：给一个至多有一个 1 的序列 s，令 α k 为“k 以内偶位都为 0”，β k 为“k 以内奇位都为 0”。两者判定、向下封闭，每处其一成立。<br>反方向：令偶位 2k 标 α 第一次不成立之处，奇位 2k + 1 标 β 第一次不成立之处。向下封闭与“每处其一”保证至多一个 1，LLPO 即给出结论。<br>所以“课程每个长度与一个课程继续之间恰是 EitherThroughout”可以读作“恰是 LLPO”，与弱 König 引理的标定相合。<br>`EitherThroughout` says: for decided, downward-closed α and β with α or β at every step, α holds throughout or β does. Reviewer's argument, not Lean-checked: it is equivalent to LLPO.<br>Forward: given s with at most one 1, let α k be "no 1 at even positions ≤ k" and β k "no 1 at odd positions ≤ k". Both are decided and downward closed, and one holds at each k.<br>Converse: mark at position 2k the first failure of α and at 2k + 1 the first failure of β. Downward closure and "one at each step" give at most one 1, and LLPO gives the conclusion.<br>So "between courses of every length and one course going on lies exactly `EitherThroughout`" can read "exactly LLPO", in line with the weak König lemma calibration. | understatement | Definition l. 1251. Weak König ⇔ LLPO: Ishihara 1990; Bridges–Richman 1987. | (S): prove `EitherThroughout ↔ LLPO` in the core, with LLPO stated for Boolean sequences with at most one `true`. Then (R): name it in the record. |
| U2 | rec what-a-law-of-the-whole-and-no-part-takes, does_not_show 1 | "Whether WLPO gives LPO" is left open. As Props it is known unprovable: WLPO is strictly weaker than LPO (Akama–Berardi–Hayashi–Kohlenbach 2004). That the core cannot prove it is known, not open. | understatement | Record text. | Cite the result, scoped to Props over intuitionistic arithmetic; keep the rule form open if it is meant. |
| U3 | rec how-often-couplings-act (law 6, does_not_show 0) | `RecursOrStops` is excluded middle at level Σ⁰₂ (Σ⁰₂-LEM), strictly stronger than LPO (= Σ⁰₁-LEM). The record says it "gives" LPO, which is true but undersells it: every schedule settling is exactly Σ⁰₂-LEM. The correspondence field says "excluded middle in Σ⁰₂ form", but the statement and does_not_show do not. | understatement | `RecursOrStops : ∀ R : Nat → Nat → Bool, (∀ n, ∃ m, R n m = true) ∨ ∃ n, ∀ m, R n m = false`. | Statement and does_not_show 0: "exactly Σ⁰₂ excluded middle, which gives LPO" (zh "恰是 Σ⁰₂ 排中，给出有限全知原则"). |

### Presentation (true, but misleading or thin as stated)

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| P1 | `Reading`; rec premises-read-off-the-exchange | `readOff` defines the requirement as responding below need, so "activity needs support" follows in one line (`supported_of_responds`), and `reading_glue` "with no premise" unfolds the definition. The record concedes that balance holds by construction (does_not_show 3), but not that support does too. | presentation | `readOff := ⟨level, L.Exchanging, requires, need, fun t f c => 0 < L.take t f c⟩`; `supported_of_responds := Nat.ge_of_not_lt fun below => responds l (fun _ _ _ => rfl) below exchanges`. | Add to does_not_show: "under `readWeb`, activity needs support by the definition of the requirement". |
| P2 | `Readings`; rec unity-of-readings | `Contextual.world_active` is `Iff.rfl`. The first conjunct of `World.unity` holds for every `World`: with the rest counted, every sequence of levels is a run of `exchange`, so it excludes nothing. The statement "counting the rest, every world is one run of exchange" does not say so. | presentation (thin) | `w.withRest.exchangeRun World.withRest_balanced`. | Statement: add "which every sequence of levels is, the rest counted". |
| P3 | `Gain`; rec where-novelty-gain-comes-from, law 0 | "Every rise is given" (`rise_netGiver`) is an accounting identity: the rest is defined as the residual in `withImbalance`. Law 0 does not mark it as holding by construction. | presentation | Definition of `withImbalance`. | Law 0: "by the definition of the rest as the residual". |
| P4 | `Situations`; rec weights-count-situations; the reading Ren took | In `finerLaw` the situation in the move names the target configuration, so `finerLaw_determined` holds by construction. The reading "a branching law is a determined law with the situation forgotten", or "the situation makes it true", is formally the small fact that putting the outcome into the move determines it. The substance is `sum_finer`, the counting. | presentation (thin) | *core* `Situations.lean` l. 101–102. | Record: say that determination holds by construction and that the content is the count (`sum_finer`). (P): Ren should know this when the reading is cited. |
| P5 | `Parting`; rec identification-where-runs-part | `world_right_iff` and `some_right_iff` give the learner the whole world (P, moves, all, reg, s). The converse is the near-tautological indistinguishability argument, which the record honestly calls known. | presentation (thin) | Statements. | None needed beyond credit (K9). |
| P6 | `Closing`; rec how-loops-form | `onLoop_iff_formed` is nearly definitional, since couplings are defined as acting at some step. `onLoop_succ_iff` is the graph fact that an added edge closes a cycle. | presentation (thin) | Statements. | None. |
| P7 | rec typicality-by-counting | "0.88^n" and "pq/((p+q)²ε²n)" are arithmetic in the prose, not Lean statements. | presentation (minor) | Record text against `Typicality` statements. | Mark them as arithmetic from the stated bounds, or bind them to theorems. |
| P8 | GENERATIVITY-CHAIN (`theories/becoming/results/data/generativity-chain.json`, `GENERATIVITY-CHAIN-INDEX-RECORD.md`) | Since the whole-chain review of 14 October (`e667f358`), 33 landings refreshed 78 fingerprints in `reviewed_sources`, their messages saying "chain review recorded". The index record has no entry after that date. No entry's content changed apart from one added review source, and no entry mentions a module under review. Each changed source may have been read and the entries left right, but that is not recorded. AGENTS.md requires reading and reconciling a change before a hash is refreshed. Whether the chain's learning and wisdom links should take in `Parting`, `Observation` and `Selection` ("memory is not wisdom") is Ren's to decide. | presentation (process) | `git diff e667f3587 HEAD -- theories/becoming/results/data/generativity-chain.json`: only hash lines and one review path change. `git log` of the index record: last commit `e667f358`. | (R): add one index-record entry listing the refreshed sources and what was checked; if they were not read, restore "pending" for them. (P): whether these modules enter the chain. |
| P9 | rec where-a-run-goes-on, law 0 zh | The zh "从运行的每个配置开始每个长度的路径" lacks its verb (有). "运行的每个配置可从其起点得到" does not match the en "each is had from its start": the en means each course, the zh each configuration. | presentation (zh/en) | Record text. | zh: "从运行的每个配置开始，有每个长度的路径，每条都从其起点得到；……". |

### Credit

| id | module / record | missing credit | where to add |
|---|---|---|---|
| K1 | `Gluing`; rec gluing-under-parity | `global_or_contradicts` is Gaussian elimination over GF(2) (the Fredholm alternative for linear systems). The all-vs-nothing parity proofs are Mermin 1990 (PRL 65), and Mermin–Peres. The cohomological/parity criterion is Abramsky, Barbosa, Kishida, Lal and Mansfield 2015 ("Contextuality, cohomology and paradox", CSL), and the parity games are Arkhipov 2012. CHSH is already credited. | module doc; record correspondence |
| K2 | `Sensitivity`; rec sensitivity-is-the-least-registration | LPO is from Bishop 1967, and WLPO from Bridges–Richman 1987. A discontinuous function giving WLPO is a standard result of constructive reverse mathematics (Ishihara). That every function reading finitely many conditions is continuous ties to Brouwer's continuity principle, which D37 already names. | module doc; record correspondence |
| K3 | `Tail` | Name the sources rather than "standard": Bishop and Bridges–Richman for LPO/WLPO; Akama–Berardi–Hayashi–Kohlenbach 2004 for the separation (U2). Kolmogorov's tail events are already in D37. | module doc; record |
| K4 | `Frequency` | Σ⁰₂-LEM and its place above LPO: Akama–Berardi–Hayashi–Kohlenbach 2004 (U3). The discrete Grönwall bound is already named in the record. | module doc; record |
| K5 | `Onward`; rec where-a-run-goes-on | `fan_no_run` is the failure of König's lemma for infinitely branching trees (König 1927), and the finite case is König's lemma. Dependent choice is named. | module doc; record correspondence |
| K6 | `Horizon`; rec what-a-finite-history-refutes | Refutable = closed and verifiable = open in the prefix topology, with adherence as closure: safety and liveness, Alpern–Schneider 1985 ("Defining liveness", IPL 21); also Kelly 1996 (*The Logic of Reliable Inquiry*) for refutation and verification in the limit. | module doc; record correspondence |
| K7 | `Observation`; rec observation-is-a-route | Noninterference (Goguen–Meseguer 1982) and the dependency-graph reading of information flow. | module doc; record correspondence |
| K8 | `Lasting`; rec lifting-where-branching-is-finite | Weak König's lemma ⇔ LLPO (Ishihara 1990; Bridges–Richman 1987), which bears on `EitherThroughout` (U1). | module doc; record |
| K9 | `Parting`; rec identification-where-runs-part | `free_never_right` is a diagonal argument in the style of Gold 1967 ("Language identification in the limit"). The parting and distinguishing tests go back to Moore 1956 ("Gedanken-experiments on sequential machines"). `Learnable` credits Gold; `Parting` does not. | module doc; record correspondence |
| K10 | `Typicality` | The record credits Chebyshev and Bernoulli, and the Lean names Chernoff and the law of large numbers. Name Chebyshev in the Lean where the variance bound is used. | Lean docstring |
| K11 | `Selection`; rec selection-through-a-model-of-the-options | Equivariance under swaps of options is the neutrality condition of May 1952, and the tie case is the Buridan symmetry argument. | module doc; record correspondence (minor) |
| K12 | `Routes`; rec orders-as-a-sum-over-histories | The sum over routes of a linear recurrence is the walk-sum (path-sum) expansion of the Neumann series. `Remainder` names Neumann, Dyson and Peano–Baker; `Routes` names only the Feynman analogy. | module doc; record correspondence (minor) |

### Confirmed

| id | module / record | finding | severity |
|---|---|---|---|
| C1 | `Novelty`; rec returning-novelty-forgetting-on-levels | `returns_of_bounded` concludes `¬¬ W.Revisits cs T`, and this is disclosed. `rests_of_loses` has the form `¬ ∀ N, ∃ t, N ≤ t ∧ W.Changes cs t`. The argument is pigeonhole. Sound. | confirmed |
| C2 | `Gluing` | `global_or_contradicts` is exact under `[DecidableEq C]` and distinct claims, and `noGlobal_iff` under listed contexts. Both are in the hypotheses. | confirmed |
| C3 | `Tail` | The rule forms (`Nonempty (∀ s, Decidable …)`) and the Prop forms are kept apart. Counterexample ⇔ WLPO as a rule and vanishing decision ⇔ LPO as a rule are exact. | confirmed |
| C4 | `Courses`, `CoursesBridge` | Instances only, honestly described. On `anyChange` the retrodiction and fallible-witness instances are on the base only trivially, since every sequence is a run (thin; the duplicate is P129's). | confirmed (thin) |
| C5 | `Propagation` | `most_difference_arrives` is an exact iff over all laws, and the Lipschitz/Grönwall comparison is credited. The scope issue is O3. | confirmed |
| C6 | `Remainder` | Neumann, Dyson and Peano–Baker are credited. Settled schedules are written in as hypotheses. "Only through a loop" comes from a contrapositive, which is a ¬¬ form (minor). Does_not_show 0, "every schedule settles … classically true", is right. | confirmed |
| C7 | `Routes` | `routeSum_eq_carriedWithin` and `carried_eq_courses` are exact, and the counting weights are honestly said not to cancel. | confirmed |
| C8 | `Thresholds` | `break_carried_nowhere` and `unread_carried_nowhere` are exact. The Runaway join is stated within one law, and its scope against `Runaway` is in does_not_show 2. The statement issue is O6. | confirmed |
| C9 | `Frequency` | The rate bounds, `Sparse.polynomial` (a recurring loop need not run away) and `settled_every_iff` are exact. `polynomial_iff` needs `1 ≤ M` and `1 ≤ D`, and both are in the theorem. | confirmed |
| C10 | `Onward` | Finite ⇒ a run is a course into a return, with no selection. Asked of every process, a run is exactly dependent choice, which is a definition (`DependentSelection`). Exact. | confirmed |
| C11 | `Gated` | `origin` uses no decision of p, and `origin_of_propositions_iff` ↔ DNE is right. | confirmed |
| C12 | `Selection` | `selected_alike_iff` and `singled_iff_untied` are sound. Ren approved the reading "memory gives distinctions, not their relevance" on 16 October 2026. | confirmed |
| C13 | `Horizon` | `refutable_passes` and Markov's principle are exact, the record's law 2 is right, and the ¬¬ forms are in place. The errors are E1, E2 and O7. | confirmed |
| C14 | `Typicality`, `Situations` (`sum_finer`) | The counting laws are exact. Laplace and Boltzmann are credited in `Situations`. | confirmed |

### Readings and the delegation (P110)

| id | item | finding | class |
|---|---|---|---|
| D-a | D1, D5, D22 | The delegation's scope excluded "Ren's own texts and terms" (source l. 27), but its examples are only OPENING and its footnote, the Chinese rest term and the informal rest heading. D1 fixes how 生生 is read ("generative space, widening what can form"). D5 reads 生生不息 at the level of the whole, and in a bounded whole with the rest idle as return rather than endless novelty. D22 reads Ren's "generative space" and "flourishes/plurality". These are Ren's central terms, so the decisions are within the letter of the delegation but against its spirit. | (P) |
| D-b | D37 (1) | It repeats O1's overstatement: "with infinitely many conditions the reading does not apply". | (R) in DELEGATED-CHOICES |
| D-c | D39 (3) | It adopts "a held difference keeps arriving" on the strength of a witness that is not gainless (O3). | (R) and (P) |
| D-d | D39 (4) | It reads Ren's OPENING word "entangled" as coupling strength. It is carefully scoped ("OPENING stays Ren's") and declines quantum entanglement, but it still decides how Ren's word is read. | (P) |
| D-e | P107 reading in `unity-of-readings` | "Under the invariance the laws meet" treats `Novelty`'s universal quantification over families as if it were `BoundaryInvariant`. That is an analogy, and it bears on the invariance step of Part II. | (P) |
| D-f | All D-items | Whether Ren's "agree with other readings" ratifies all of D1–D39 is still open, as the release-readiness review noted. | (P) |

<a id="2-各模块结论--verdict-per-module"></a>
## 2. Verdict per module

| module | verdict |
|---|---|
| `Novelty` | Sound. |
| `Reading` | Sound but thin: the tying premises hold by construction (P1). |
| `Readings` | Sound but thin: `world_active` is `Iff.rfl` and the unity conjunct is trivial (P2); one reading is an analogy (D-a…f). |
| `Gain` | Sound; law 0 is an identity (P3). |
| `Gluing` | Sound and exact; credit is missing (K1). |
| `Sensitivity` | Sound Lean, with an overstated constructive scope in the prose (O1, O2) and missing credit (K2). |
| `Tail` | Sound and exact; one reading is classical (O10), one open item is known (U2), and credit is missing (K3). |
| `Courses`, `CoursesBridge` | Sound but thin (C4). |
| `Propagation` | Sound Lean; the attaining law is not gainless, and the records and readings never say so (O3). |
| `Loops` | Sound Lean; "every loop doubles" is the natural-number, non-dissipating case (O4). |
| `Remainder` | Sound. |
| `Routes` | Sound; minor credit (K12). |
| `Closing` | Sound but thin (P6); the statement omits a condition (O11). |
| `Thresholds` | Sound; the statement overstates (O6). |
| `Frequency` | Sound; the ℕ scope (O4) and Σ⁰₂ (U3) should be stated. |
| `Observation` | Sound Lean; the headline overstates (O5). |
| `Onward` | Sound and exact; König credit is missing (K5), and the zh of law 0 is garbled (P9). |
| `Parting` | Sound but thin (P5); Gold and Moore credit is missing (K9). |
| `Typicality` | Sound; the prose arithmetic is unbound (P7). |
| `Situations` | Sound; determination holds by construction, and the content is the count (P4). |
| `Gated` | Sound Lean; record errors (E3, O9) and a doc overstatement (O8). |
| `Selection` | Sound. |
| `Horizon` | Sound Lean; a record error (E1), a doc error (E2) and the "least" docstring (O7). |
| `Lasting` | Sound; `EitherThroughout` is likely LLPO, to be proved (U1). |

<a id="3-一元关系方法--the-nondual-method"></a>
## 3. The nondual method

No module under review introduces a separate entity that the shared base lacks, except the coupling-array dialect already given to P130. Two readings speak of observation and situations as if they were relations beside the unfolding, and then deny it:
- O5 ("observation is not a second kind of relation") claims more than the theorem shows.
- P4 ("the situation makes it true") rests on a construction in which the situation contains the outcome.

Both are matters of what the theorem shows, not of a dualist premise.

<a id="4-未能检查--what-could-not-be-checked"></a>
## 4. What could not be checked

- No Lean was built. U1's equivalence and the optional (S) items are unproved.
- The connectivity measure was not re-run; it is stale by the release-readiness review.
- D6–D21, D24–D36 and D38 were read by index only.
- The proofs of `Gluing`, `Remainder` and `Routes` were read at the statement level.

---

<a id="fix-list--修正清单"></a>
## Fix list

(L) Lean docstring or credit, exact file and text. (R) Record field. (S) A new or changed theorem. (P) Ren's decision.

**(L) Lean docstrings and credits** (*core* = `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`)
1. E2, *core* `Horizon.lean` l. 50–51. Replace "recurrence and eventual occurrence are neither (`Sequences.recurs_not_refutable`, `Sequences.eventually_not_refutable`)" with "recurrence and eventual occurrence are not refutable (`Sequences.recurs_not_refutable`, `Sequences.eventually_not_refutable`), and never occurring is not verifiable (`Sequences.never_not_verifiable`)".
2. O7, *core* `Horizon.lean` l. 316. Replace the docstring "**The least refutable reading.**" with "**Refutable supersets hold where the subset is adhered to.**".
3. O8, *core* `Gated.lean` l. 24. Replace "the law holds exactly where each gate is decided" with "the law holds where each gate is decided".
4. O1, *core* `Sensitivity.lean` l. 45. Replace "With infinitely many conditions the condition cannot be dropped." with "With infinitely many conditions the condition cannot be dropped given a decision of vanishing, which gives LPO (`lpo_of_vanish_decided`); any law that drops it gives WLPO (`wlpo_of_not_through_sensitive`)."
5. O5, *core* `Observation.lean` l. 12, 30, 274 and 353. Replace "observing is being downstream", "**Registering is being downstream.**", "## Registering is being downstream" and "**Observation is a route.**" with "observing lies within the downstream", "**Registering lies within the downstream.**", "## Registering lies within the downstream" and "**Observation goes only by a route.**".
6. O3, *core* `Propagation.lean` l. 641. Add to the `ExchangeLaw.carrying` docstring: "It takes nothing, so it is not gainless; the bound is attained over all laws, not shown over gainless ones."
7. O4, *core* `Loops.lean` and `Frequency.lean` module docs. Add: "Strengths are natural numbers, so a positive strength is at least one; with strengths below one the doubling does not follow."
8. K1, `Gluing.lean` module doc. Credit Gaussian elimination over GF(2) (the Fredholm alternative), Mermin 1990, Abramsky–Barbosa–Kishida–Lal–Mansfield 2015 and Arkhipov 2012.
9. K2, `Sensitivity.lean` module doc. Credit Bishop 1967 (LPO), Bridges–Richman 1987 (WLPO) and Ishihara (a discontinuous function gives WLPO).
10. K3, `Tail.lean` module doc. Credit the same, plus Akama–Berardi–Hayashi–Kohlenbach 2004.
11. U3/K4, `Frequency.lean`, the docstring of `RecursOrStops`. Add: "This is excluded middle at level Σ⁰₂ of the arithmetical hierarchy (Akama–Berardi–Hayashi–Kohlenbach 2004), strictly stronger than LPO."
12. K5, `Onward.lean`, the docstring of `fan_no_run` and the module doc. Credit König 1927, and say this is the failure of König's lemma without finite branching.
13. K6, `Horizon.lean` module doc. Credit Alpern–Schneider 1985 (safety = closed, liveness = dense) and Kelly 1996.
14. K7, `Observation.lean` module doc. Credit noninterference (Goguen–Meseguer 1982).
15. K8, `Lasting.lean` and `Likeness.lean` l. 1251. Credit weak König ⇔ LLPO (Ishihara 1990; Bridges–Richman 1987).
16. K9, `Parting.lean` module doc. Credit Gold 1967 for `free_never_right` and Moore 1956 for distinguishing experiments.
17. K10, `Typicality.lean`. Name Chebyshev where the variance bound is used.
18. K11 and K12, `Selection.lean` and `Routes.lean` module docs. Credit May 1952 (neutrality), and the walk-sum expansion of the Neumann series.

**(R) Record fields** (*rec* = `theories/becoming/results/records/`)
19. E1, *rec* what-a-finite-history-refutes, statement en and zh. Say "not refutable", and add "one with a run inside adhering to its complement is not verifiable". Replace zh "既不可否证也不可证实" accordingly.
21. O9, *rec* every-origin-passes-the-gate, statement en/zh. Add "asked of every process" (zh "对每个过程都要求时").
22. O1 and O2, *rec* sensitivity-is-the-least-registration:
    - statement en/zh and law 1: add "up to double negation" (zh "于双重否定下");
    - statement zh and counterexample 0: replace "cannot be dropped" with "cannot be dropped given a decision of vanishing (LPO); dropping it gives WLPO";
    - bring zh and en to the same length and content;
    - add credit K2.
23. O1, `DELEGATED-CHOICES.md` D37 (1), zh and en. Replace "With infinitely many conditions the reading does not apply: the registrations the tail law reads through have no least one" with "With infinitely many conditions the reading is not shown to apply: given a decision of vanishing (which gives LPO), the tail law has no least registration, and any such law gives WLPO". (This is a study file, not a record; the owner of P110 should edit it.)
24. O3, *rec* how-much-difference-arrives, does_not_show 2, counterexample 1 and readings. Say the attaining law takes nothing and is not gainless, and that the bound is shown attained over all laws. Apply the same to D39 (3).
25. O4, *rec* how-a-carried-difference-grows and how-often-couplings-act, statements en/zh. Add "with natural-number strengths, each positive one at least one". In the readings, mark the sufficiency half as that case.
26. O5, *rec* observation-is-a-route, title, statement and readings. Use "lies within the downstream" (zh "不出下游"), and say "can register only where downstream".
27. O6, *rec* loops-within-what-a-law-reads, statement en/zh. Use "before the break the law acts as its standing law, which has no loop through the stock; the loop that acts forms at the break".
28. O10, *rec* what-a-law-of-the-whole-and-no-part-takes, readings. Replace "the same whole" with "a whole of the same kind", or justify the identification classically.
29. U2 and K3, same record, does_not_show 1. Cite Akama–Berardi–Hayashi–Kohlenbach 2004: as Props, WLPO does not give LPO.
30. U3 and K4, *rec* how-often-couplings-act, statement and does_not_show 0. Use "exactly Σ⁰₂ excluded middle, which gives LPO".
31. O11, *rec* orders-as-a-sum-over-histories and how-loops-form, statements. Add "every condition listed" and, for orders, "the law stationary".
32. P1, *rec* premises-read-off-the-exchange, does_not_show. Add "activity needs support by the definition of the requirement under `readWeb`".
33. P2, *rec* unity-of-readings, statement en/zh. Add that, the rest counted, every sequence of levels is a run of `exchange`.
34. P3, *rec* where-novelty-gain-comes-from, law 0. Add "by the definition of the rest as the residual".
35. P4, *rec* weights-count-situations, correspondence. Say that determination of `finerLaw` holds by construction and that the content is `sum_finer`.
36. P7, *rec* typicality-by-counting. Mark "0.88^n" and "pq/((p+q)²ε²n)" as arithmetic from the theorems' bounds, or bind them.
37. P8, `GENERATIVITY-CHAIN-INDEX-RECORD.md`. Add an entry for the 78 fingerprints refreshed since `e667f358`, stating what was read. Where nothing was read, restore those sources to pending. This is a chain maintenance record, not a generated file; the integrator should edit it.
39. K1, K5, K6, K7, K8, K9 and K11. Add the same credits to the correspondence fields of gluing-under-parity, where-a-run-goes-on, what-a-finite-history-refutes, observation-is-a-route, lifting-where-branching-is-finite, identification-where-runs-part and selection-through-a-model-of-the-options.
40. U1 (after item 41 lands), *rec* lifting-where-branching-is-finite. Name `EitherThroughout` as LLPO. Also add to the reading that `lifting` needs selection as well (does_not_show 2 already has it).

**(S) Statement problems needing a new or changed theorem**
41. U1. Prove `EitherThroughout ↔ LLPO` in the core, with LLPO for Boolean sequences with at most one `true`. The reviewer's argument is in the table above.
42. O3 (optional). State the gainless case of `most_difference_arrives`: either tightness over gainless laws, or a bound that uses the stock.
43. O7 (optional). Prove `Refutable (Adheres K)`, so that "least refutable reading" is earned; otherwise keep the docstring of item 2.

**(P) Ren's decisions**
44. O4. Does the P118 reading Ren took, "only a loop makes a difference run away … through every loop", stand, given that its sufficiency half holds only for natural-number strengths and laws that create amounts?
45. O5. The reading "observation is not a second kind of relation beside dependence": keep, weaken to "does not go beyond dependence", or drop.
46. P4. When "the situation makes it true" is cited, should it say that its formal part holds by construction?
47. D-a. D1, D5 and D22 read Ren's own terms 生生, 生生不息 and "generative space". Ratify, revise or take back.
48. D-c and D-d. D39 (3), "a held difference keeps arriving", needs a scope (O3). D39 (4) reads Ren's word "entangled" as coupling strength.
49. D-e. The analogy between `Novelty`'s universal quantification and `BoundaryInvariant`, as it bears on Part II's invariance step.
50. D-f. Whether "agree with other readings" ratifies D1–D39 as a whole.
51. P8. Whether `Parting`, `Observation` and `Selection` should enter the generativity chain's learning and wisdom links.

*This is an AI review (Opus 5.5), not Ren's words. No Lean was built and no checker was run. It proves no new claim and is not independent acceptance of any result.*
