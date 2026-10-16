<a id="p47-独立审查登记与检验--independent-review-of-p47-registration-and-testing"></a>
# Independent review of P47: registration and testing

> Some passages exist only in the [Chinese edition](BECOMING-P49-REVIEW.zh.md): sections “Independent review of P47: registration and testing”; “摘要”; “F4（乙，中等）所及闭包的传递性在“其余交换不变”的比较中不起作用；已检查回应性版本 / The closure's transitivity is idle in the fixed-rest comparison; a responsive version is checked”.

Object:

本审查只在 `review/` 下建文件。没有修改仓库文件，没有运行 make 目标或仓库检查器，没有改变 git 状态。只做了只读的 `git status`、`git diff`、`git show`。
Only files under `review/` were created. No repository file was edited, no make target or repository checker was run, and git state was not changed. Only read-only `git status`, `git diff` and `git show` were used.

Classification, as in earlier reviews:
- a relation omitted by the representation;
- an unresolved inference or an overclaim;
- a genuine counterexample under the stated conditions.

---

<a id="摘要"></a>

## English summary

**Formal status.**
- Lean 4.29.1 (`f72c35b3`). A copy of the module recompiles with no error and no warning.
- An audit of every constant gives empty axiom reports: 127 constants, 0 with axioms (`Audit.lean`, `Audit.out.txt`).
- Every theorem proves its own statement. The problems are in the prose, the readings, the names and the scope of one hypothesis, not in the proofs.
- All 192 probe constants are free of axioms (`ProbeAudit.lean`, `ProbeAudit.out.txt`). They use no classical reasoning and no `propext`, so each proposed theorem can enter the pure core. `ProbeNames.lean` deliberately shows that `nomatch` proofs of numeral disequalities bring in `propext`.

**Verdicts.**

| Question | Verdict |
|---|---|
| 1. Correctness and correspondence | **Accept the Lean.** Every theorem proves what its own statement says. **Narrow the prose** at the points in §7. Two kinds of problem stand out: four readings say more than any theorem, and two citations point to the wrong theorem. |
| 2. Threshold blindness | **The three theorems: accept as stated.**<br>**`RespondsThrough`: accept as a disclosed hypothesis.** Reject its name, and its omission from the readings and the README. It excludes other formations responding to the stock, and renewal that depends on the level. Under such responses a richer web can end `g` first (A7, 丙 against the unqualified reading).<br>**Idle hypotheses.** The `requires` and `need` hypotheses do no work (A0).<br>**Sharper forms are checked.** No `DecidableEq`, several stocks, the break located as a divergence, and an exact one-step characterization (A1–A4, A8).<br>**"Drawn on only after a break": accurate under the hypothesis, as a necessary condition.** "Drawn on" means "changed". The break that matters is a divergence of support, not the poorer web's failure (A4, A6). `Gated.surplus_waits` is nontrivial. |
| 3. Reach blindness | **Accept.** The registration closure contains the influence closure, and equals it under `supportOnly`.<br>**Transitivity.** The closure's transitivity is idle in the fixed-rest comparison. A responsive version is checked (B1), and it contains both P47 theorems as instances (B3, B4).<br>**`Prey`: correct.** Its first conjunct rests on an omitted relation: the prey does not bear on itself, and the predator is active with zero standing (F2, 甲). It illustrates the decision on own standing; it does not support it. |
| 4. Refutation | **Accept `Refutes` as the record-alone notion.** **Reject the horizon conclusions drawn from it:** over all histories, every tail claim is trivially unrefuted (C2).<br>**Add `RefutesWithin`.** Refutation relative to a class of admissible histories is refutation of the class and the claim together (C6).<br>**How the stated results fare:**<ul><li>`not_of_alike`, `later` and `widen` are unchanged.</li><li>`not_meets` needs the actual history inside the class (C1).</li><li>`unrefuted_beyond_registration` holds for every class containing the withheld levels, and only for those (C7).</li><li>The clearer half of `tested_by_dweller` holds for every class containing the cleared history.</li></ul>**What a model adds.** A complete model makes registration idle (C8). A wrong model refutes truths (C4). Registration refutes the model (C4b). |
| 5. `tested_by_dweller`, `finite_reading_withholds_renewal` | **`tested_by_dweller`: accept.** It is correct, nonvacuous and accurately described. It is near-definitional: a claim about the dweller's admission is tested by that admission. Pooled testing (C5) is the more informative relational statement.<br>**`withholds_renewal`: accept as a corollary, not a new result.** From `credits_consumption` alone, ¬(sound ∧ complete) and the ¬¬-witness both follow (E). The delta is the constructive witness. The header of `Becoming.Horizon` already states the dichotomy in prose. |
| 6. Own standing | **Accept the parametric `obs`.** **Reject counting own standing as registered by default.** Prefer registration through `Web.SelfBearing`, with `ownStanding` an observation premise (a self-gauge) (F3; §6). |
| 7. Readings | **Mixed** (§4):<ul><li>three blindnesses: supported in scope, not exhaustive;</li><li>runaway: overreach;</li><li>measurement: supported (A8);</li><li>models cross the horizon: plausible and unproved in the module, checked here with its costs (C3, C4, C4b);</li><li>others' registration widens the closure: mis-cited; it holds only through pooling or a new relation (C5, B5);</li><li>falsifiability: three parts supported, "corrected by the unfolding" unformalized, "no finite record tests whole-run claims" overreach;</li><li>理: plausible, read as a model answerable to registration, not as a register.</li></ul> |
| 8. Names | **Rename** `RespondsThrough`, `AlikeUpTo`, `threshold_blind`, `surplus_*`, `Gated`, `Ended` and `admits_iff_supported`. **Retire** the root-level `one_ne_two` and `two_ne_three`. **Fix** the Chinese 计入 in the README row. No Lean name clashes with `Bridge.lean` or elsewhere in the core (§5). |
| 9. Missing statements | **Most important: B1, reach blindness where the members respond.** Next: the exact threshold theorems (A1–A4, A8), refutation relative to a model (C1–C8), and the bridge to `Becoming.Inquiry` (D). All are checked and axiom-free (§3). |

**Top findings, in order.**
1. F1 (乙, major): the horizon reading overreaches.
2. F2 (甲/丙, major): threshold blindness rests on `RespondsThrough`, which is missing from the readings.
3. F3 (乙, major): own standing should register through self-bearing, not as a default gauge; the `Prey` witness rests on an omission.
4. F4 (乙, moderate): the closure's transitivity is idle in the fixed-rest comparison; B1 is checked.
5. F5 (乙, moderate): the threshold theorem can be sharpened; the break is a divergence.
6. F6 (乙, moderate): `Refutes` covers claims about one history; claims about what an act does are counterfactual and need a model.
7. F7 (provenance, moderate): Ren's acceptance is not preserved in a source file.
8. F8–F13 (minor): mis-citations, the horizon dual as a corollary, reuse of P42, near-definitional witnesses, the inquiry bridge, names.

---

<a id="0-范围与方法--scope-and-method"></a>
## 0. Scope and method

I read the module in full. I also read:
- the parts of `Becoming.Feedback` it uses: closures, `support_agrees`, `agrees_of_quiet`, `admits_unreached`, `unregistered_beyond_influence`, and the `Clearing` and `Margin` witnesses;
- `Becoming.Horizon` in full;
- `Becoming.Inquiry` in full;
- the one-kind parts of `Becoming.Roles` (`Embodied`, `SelfBearing`) and `Becoming.Reserve` (`carries_of_own`, held conditions);
- the definitions of `Web`, `Flow`, `Balances`, `withhold` and `WithheldLevels`;
- the plan, Ren's source record, `AGENTS.md`, `NONDUAL-METHOD.md`, the P42–P43 review (at c9c219e3) for format, and the worktree diff (README row, `Becoming.lean`, `check_becoming.py`).

Probes are run with
`cd review && LEAN_PATH=<build> ~/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean <Probe>.lean`.
For the combined audit, the probe files were compiled with `-o` into `review/olean/`, which holds copies of the probes and their `.olean` files. Nothing was written to the build directory.

<a id="1-形式复核--formal-recheck"></a>
## 1. Formal recheck

- **Identical sources.** Every `Becoming/*.lean` in the scratch build is byte-identical to the worktree. `Testing.lean` has the sha256 above.
- **Recompilation.** `TestingCopy.lean` (the same bytes) compiles against the build with no output.
- **Module audit.** `Audit.lean` applies `Lean.collectAxioms` to every constant whose module is `Becoming.Testing`, generated auxiliaries included: 127 constants, 0 with axioms.
- **Probe audit.** `ProbeAudit.lean` does the same for the four probe modules:

  | Probe module | Constants | With axioms |
  |---|---|---|
  | `ProbeThreshold` | 67 | 0 |
  | `ProbeReach` | 37 | 0 |
  | `ProbeTesting` | 62 | 0 |
  | `ProbeStanding` | 26 | 0 |

- **`ProbeNames.lean`.**
  - `fun h => nomatch h` proves `(1 : Nat) ≠ 2` but depends on `propext`; `by decide` is free of axioms. So the long proofs of `one_ne_two` and `two_ne_three` are justified by the purity rule.
  - Core Lean 4.29.1 has neither `one_ne_two` nor `Nat.one_ne_two`, so there is no clash in the core closure.
  - The file intentionally contains two failing `#check` lines that record the absence.
- **Unused hypotheses.** The hypotheses `requires` and `need` of `threshold_blind`, `surplus_untouched` and `surplus_after_break` are passed only to the recursive call. The linter does not flag them; they are idle (A0).

---

<a id="2-发现--findings"></a>
## 2. Findings

<a id="f1乙重大视界读法关于整个运行的主张只在延续开放时不被有限记录判定--the-horizon-reading-whole-run-claims-are-undecided-by-a-finite-record-only-where-the-continuation-is-open"></a>
### The horizon reading: whole-run claims are undecided by a finite record only where the continuation is open

**English.**
- **Location.**
  - Header lines 57–59: "every finite test of renewal errs on one side".
  - Readings, lines 70–72: "claims about the whole run are not tested by any finite record".
  - Docstring of `Renewable.finite_reading_withholds_renewal` (line 682).
  - The README row ("every finite test of renewal errs on one side (horizon ...)").
- **Problem.**
  - **Scope.** The result is `Renewable.prefix_does_not_decide`, about one process whose prefix does not fix the actions to come. `Becoming.Horizon` itself says that what no prefix decides there "is the action still to be taken".
  - **For `Refutes` the claim is trivial.** `Refutes` quantifies over every level history. A claim met by some history agreeing with the record up to `t` is unrefuted at `t` (`unrefuted_of_extension`). So for every finite record, both "the stock comes to zero" and its rival "it stays positive after `t`" are unrefuted, by any formation and under any observation (C2 `tail_untested`).
  - **Relative to a model it is false.** Take a model that fixes the exchange: `Model L` is the set of histories balancing a flow `L`. A formation observing a stock refutes, at step 0, every false claim that the stock comes to zero (C3 `model_refutes_tail`).
  - **The costs.**
    - Refutation within a model is refutation of the model and the claim together (C6 `refutesWithin_iff_conjunction`), the Duhem–Quine structure.
    - A wrong model refutes a true claim (C4 `Stationary.model_error`).
    - Registration refutes the model itself: within the stationary model, the gauging formation's belief becomes empty at step 1 (C4b `Stationary.model_refuted`).
  - **As a universal statement, "every finite test of renewal errs" is false** where the model is right and the continuation is fixed.
- **Fix.**
  - Restate as: "Where the continuation is open, as in `Renewable`, no reading decided by a finite prefix coincides with the whole-run classification (`no_exact_finite_reading`). A model of the continuation makes whole-run claims refutable by a finite record, but only relative to the model; such a refutation is a refutation of the model and the claim together, and the model is itself refuted where no history it admits is registered alike."
  - Add `RefutesWithin` and C3–C6 to the module.
- **Probes.** `ProbeTesting.lean`: `tail_untested`, `model_refutes_tail`, `Stationary.model_error`, `Stationary.model_refuted`, `refutesWithin_iff_conjunction`, `Becoming.Renewable.no_exact_finite_reading`. All are free of axioms.

<a id="f2甲丙重大阈下不见取决于-respondsthrough读法和-readme-没有写出它--threshold-blindness-rests-on-respondsthrough-which-the-readings-and-readme-omit"></a>
### Threshold blindness rests on `RespondsThrough`, which the readings and README omit

**English.**
- **Location.**
  - The definition `Flow.RespondsThrough` (lines 205–210).
  - The Readings at lines 62–66.
  - The README row ("a stock depended on and not observed registers only at the break, so the surplus of a richer stock is drawn on only after the poorer one fails to support").
- **What the definition says.** Wherever `g` has registered alike up to `t`, the *totals*, over every formation taking part, taken from and given to each condition `g` registers are equal in the two flows across step `t`. It is a closed-loop hypothesis on the whole exchange around `g`, not a description of `g`'s responses.
- **What it excludes.**
  - **Other formations responding to the stock directly.** An open-access fishery is an example: a richer stock draws more boats.
  - **Renewal that depends on the level.** Logistic regrowth gives more where the stock is higher.
- **Witness (A7 `Attracting.richer_breaks_first`).**
  - A taker takes two units when the stock stands at three, so the richer web (3) ends the dependent at step 1.
  - At step 1 the poorer web (2) still supports it.
  - The dependent registers alike at step 0 and differently at step 1, where the poorer supports and the richer does not.
  - `RespondsThrough` fails, so the module's theorem does not apply. This is not a counterexample to the theorem.
  - It is a counterexample (丙) to the unqualified readings, and to the README's statement, which drops the hypothesis.
- **Fix.**
  - Rename `RespondsThrough` (§5, e.g. `ExchangeFollows`) and reword its docstring: "the exchange on what `g` registers follows `g`'s registration".
  - In every reading and in the README, add "where the exchange on what `g` registers follows its registration".
  - Preserve `Attracting` as the counterexample that marks the scope: where others respond to the stock itself, a larger stock can end `g` sooner.
- **Probe.** `ProbeThreshold.lean`: `Attracting.richer_breaks_first`, free of axioms.

<a id="f3乙重大自身水平应经依存于自身登记而非默认为完全的量度prey-依赖一个省略--own-standing-should-register-through-self-bearing-not-as-a-default-gauge-prey-rests-on-an-omission"></a>
### Own standing should register through self-bearing, not as a default gauge; `Prey` rests on an omission

**English.**
- **Location.**
  - `ownStanding` (lines 100–105).
  - The header at lines 17–18 and 35–38.
  - `Prey` (lines 528–651).
  - The README row.
- **Problem.**
  - **The spine already has the structural relation.** `Web.SelfBearing x` in `Becoming.Roles`: while active, `x` requires its own standing at a positive need. Under it, own standing registers through support like any other condition.
  - **`Prey`'s "beyond the influence closure" rests on an omission.** In `Prey` the prey does not bear on itself (`Prey_omits`).
    - It is supported and active at every step, with and without the bite. The difference `ownStanding` registers makes no difference to the prey in the representation.
    - The predator is active with zero standing, so it is not embodied.
    - The first conjunct of `registers_taking`, "beyond the influence closure", holds only because of this omitted relation.
  - **With self-bearing the picture changes** (`SelfPrey.threshold_on_oneself`):
    - the predator lies within the influence closure (`SelfPrey.within_influence`);
    - a bite of one from a standing of two is below the threshold and registers alike under `supportOnly`, while under `ownStanding` it registers;
    - a bite of two registers through support.
  - **Under `ownStanding`, self-depletion has no threshold blindness.** A formation whose reserve is its own standing is a full gauge of it: in `Gauged`, where F = C = Unit, `ownStanding` is exactly the stock observation (`Gauged_own`). Self-depletion that goes unregistered until collapse cannot then be expressed. The same reserve represented as a held condition (`Reserve`'s `hold f`) is threshold-blind. The verdict depends on the carving.
- **Fix.**
  - Keep `obs` parametric.
  - Make the default one-kind reading "own standing registers through self-bearing": `supportOnly`, with `SelfBearing` where it holds.
  - Present `ownStanding` as one observation premise, a gauge of one's own standing that is formed (nociception, proprioception), not given.
  - Replace or supplement `Prey` with `SelfPrey`, whose contrast is the informative one: threshold versus gauge on oneself.
  - Add to "What is not derived": "that a formation gauges its own standing".
- **Probes.** `ProbeStanding.lean`: `Gauged_own`, `Prey_omits`, `SelfPrey.within_influence`, `SelfPrey.threshold_on_oneself`. All are free of axioms.

<a id="f4乙中等所及闭包的传递性在其余交换不变的比较中不起作用已检查回应性版本--the-closures-transitivity-is-idle-in-the-fixed-rest-comparison-a-responsive-version-is-checked"></a>
### The closure's transitivity is idle in the fixed-rest comparison; a responsive version is checked

**English.**
- **Location.**
  - `Flow.Balances.unregistered_beyond_registration` (lines 234–246).
  - The header at lines 26–35.
- **Problem.**
  - **Only direct exchange matters in the fixed-rest comparison.** There, `g`'s registration depends only on whether part members exchange directly with what `g` registers (`admits_unreached`, `agrees_of_quiet`). The closure only makes the statement uniform over a region.
  - **A transitive link does nothing.** A part member can lie within `f`'s registration closure, through a chain, and still change nothing `f` registers. The P42 review made the same point for the influence closure (its F2).
  - **When the closure does work.** It does work only where the formations inside it respond to what they register, a comparison the module does not state.
- **Checked statement (B1 `Flow.Balances.alike_within_closed`).** Take two balanced flows with the same formations taking part, and a region closed in both flows under `RegisteredFrom`. Suppose:
  - the levels start alike on everything any member registers;
  - each member's take and give on what the members register depend only on its own registration.

  Then every member registers alike at every step, whatever differs elsewhere:
  - formations beyond the region act differently;
  - members act on conditions no member registers;
  - unregistered levels differ.

  B2 states it for `f`'s registration closure drawn through both flows.
- **Instances.**
  - P47's fixed-rest theorem is an instance: the second flow is `L.withhold part` (B3 `withheld_instance`).
  - `Clearing.alike_for_clearer` is an instance (B4 `ClearingResponsive.alike_for_clearer_responsive`). The clearer's own clearing is an act on a condition that nothing in its closure registers. Reach blindness and "acting on what one does not register" are one statement.
- **Fix.**
  - Make B1 the module's reach-blindness theorem.
  - Keep the fixed-rest form as its corollary.
  - Read the closure as the scope of registration where the members respond.
- **Probe.** `ProbeReach.lean`, all 37 constants free of axioms.

<a id="f5乙中等阈值定理可以更精确断裂是分岔--the-threshold-theorem-sharpens-the-break-is-a-divergence"></a>
### The threshold theorem sharpens: the break is a divergence

- **Idle hypotheses (A0 `threshold_blind_no_webs`).** The module's theorem holds for every second web. The proof applies it to the second web with the first web's `requires` and `need` substituted: the conclusion mentions only `W.level`, `W'.level` and `W.Admits`. The agreement is needed only to read `W.Admits (W'.level t) t g` as `W'.Supported t g` (`Web.admits_iff_supported`).
- **Differences kept (A1 `alike_keeps_difference`).** While `g` registers alike, exchange that follows registration keeps every difference on a registered condition exactly as it was at the start: `W'.level t e + W.level 0 e = W.level t e + W'.level 0 e`. A1 needs no start hypothesis and no `DecidableEq`.
- **Several stocks (A2 `alike_while_poorer_supported`).** Suppose the second web is at least as rich on every registered condition at the start and alike on every observed one. Then `g` registers alike at every step before which the poorer web supported it. A2 needs no `DecidableEq`.
- **The first difference (A3 `alike_iff_richer_only`).** At a step where the invariants hold, registering alike is exactly this: if the richer levels admit `g`, the poorer web supports it. So the first step at which registration differs is the first at which the richer web supports `g` and the poorer does not.
- **The break is a divergence (A4 `changed_after_divergence`).** A registered difference changes only after a step at which the richer web admitted `g` and the poorer did not support it (constructively, ¬∀). The poorer web's failure is necessary for a change but not sufficient. In A6 (`JointFailure.untouched_after_joint_failure`) both webs fail at step 1 because a second requirement is gone, and the stock difference stays one at every step.
- **A corollary (A5 `threshold_blind_of_general`).** The module's theorem follows from A1 and A2. `DecidableEq` is used only to turn `stock` and `start` into the ≥ hypothesis.
- **Exact one-step characterization (A8).**
  - `Exact.registers_threshold_only`: let every other registered condition be alike at `s`. An unobserved condition then registers only whether it meets the need: under both histories or under neither, `g` registers alike, whatever the two levels.
  - `Exact.observed_registers_level`: an observed condition registers every difference in its level.

  This is the exact sense in which observing a condition removes its threshold blindness, which question 9 asked for.
- **Wording.**
  - "The surplus is drawn on" (lines 49–52, 319, 335) is `W'.level t c ≠ W.level t c + d`. It covers changes in either direction; say "the difference changes".
  - `surplus_after_break` gives ¬∀ (not ∃) because `Supported` is not decidable. Say so, or state the decidable case.
  - Section heading at line 258: "support registers a stock only at the break". Better: "support registers a stock only where it changes admission (A8), so a difference persists until the webs' support diverges (A4)".
- **Fix.**
  - Drop the `requires` and `need` hypotheses, or state that they serve only the reading.
  - Replace the theorem by A1, A2 and A4 with A8, and keep `threshold_blind` as the corollary A5.
- **Probe.** `ProbeThreshold.lean`, all 67 constants free of axioms.

<a id="f6乙中等refutes-检验的是关于一条历史的主张我的行动造成什么是反事实的--refutes-tests-claims-about-one-history-what-an-act-does-is-counterfactual"></a>
### `Refutes` tests claims about one history; what an act does is counterfactual

**English.**
- **Location.** The Falsifiability reading (lines 70–72), and the plan's T3 ("the claim that the clearing ends the dweller").
- **What a claim is.** A claim of `Refutes` is a predicate on one level history. The module correctly tests "the dweller is ended" (`Ended`), a claim about the state. "My clearing ends the dweller" compares two histories, with and without the act. No single record registers it.
- **What this does to the readings.** Correction "by the unfolding" of what one's own act does, the case runaway avoidance and situational awareness need, is therefore not covered. By C7 (`beyond_needs_model`), a formation within the closure that refutes a claim about a part beyond it refutes it only relative to a model the withheld levels do not meet, that is, a model of the part's exchange. The clearer can refute "the dweller is admitted at the third step" without registering anything about the habitat only through a complete model (C8 `ClearingModel.model_idles_registration`), and then registration does no work.
- **Fix.**
  - Keep `Ended` as worded; do not restore the plan's causal wording.
  - Add to "What is not derived": "claims about what an act does, which compare two histories, are tested only relative to a model of the history without it".
  - Mark intervention, varying one's own act and registering the difference, as the open route.
- **Probes.** `ProbeTesting.lean`: `beyond_needs_model`, `ClearingModel.model_idles_registration`.

<a id="f7出处中等ren-接受没有来源记录--rens-acceptance-is-not-in-a-preserved-source"></a>
### Ren's acceptance is not in a preserved source

- **Location.** Header line 61 ("Readings (the AI's, which Ren accepted on 11 October 2026)") and the README row ("accepted by Ren on 11 October 2026").
- **What the sources contain.**
  - `sources/15-codex-theory-conversations/2026-10-11-wisdom-from-registration.md` holds Ren's question and "Try again", and nothing else from Ren.
  - The plan (§5) still lists the readings, 理 and own standing as "Choices for Ren", pending.
  - No source file records the acceptance, or that Ren asked the AI to decide on own standing.
- **Fix.** Before the module or README says "accepted by Ren", preserve Ren's words with date and provenance under `sources/15-codex-theory-conversations/`. AGENTS.md requires distinguishing Ren's words from AI elaboration, and preserving provenance. Until then, write "pending Ren". Record the own-standing choice as the AI's decision at Ren's request, citing the record.

<a id="f8乙次要引错的定理--mis-citations"></a>
### Mis-citations

- **Lines 53–56.** "while no response through support alone can (`Gauged.draws_surplus`)". The general impossibility is `surplus_untouched` (contrapositive). `Gauged.draws_surplus` shows only that this pair does not respond through support.
  - Its `RespondsThrough ... stock` holds **vacuously**: observing the stock, the formation registers the webs apart at step 0, so the hypothesis "alike up to t" never holds.
  - So the docstring at line 412, "Observing the stock, the two flows respond to it only through what it registers", should say: "Observing the stock, the formation registers the webs apart at the first step, so responding through registration constrains nothing".
- **Lines 67–69.** "another formation's registration and new exchanges widen the closure (`Clearing.tested_by_dweller`, `Refutes.widen`)".
  - `tested_by_dweller` shows another formation testing what the clearer cannot; it does not widen the clearer's closure.
  - `Refutes.widen` is about observation, not exchange.
  - Cite B5 `withinRegistration_mono_obs` and `withinRegistration_mono_flow`: the closure grows with observation and with exchange.
  - Cite C5 `ClearingPooled.pooled`: a pair tests what neither member can.
  - Note that pooling presupposes a relation between the two (communication), which the representation does not have. Where it is represented, it is an exchange or an observation, and it widens the closure by B5.
- **Lines 502–505.** `Gated.surplus_waits`: "registers the richer stock as the poorer up to the third step". At the third step (index 2) they differ. Say "before the third step".

<a id="f9乙次要视界对偶是推论--the-horizon-dual-is-a-corollary"></a>
### The horizon dual is a corollary

- **What follows from `finite_reading_credits_consumption` alone.**
  - A sound reading does not credit every renewing run (E `sound_not_complete`).
  - The witness of the dual holds up to double negation: apply the theorem to the doubly negated reading (E `withholds_not_not`).
  - No reading decided by a prefix is exactly the whole-run classification (E `no_exact_finite_reading`). This is the constructive content of "errs on one side": "on at least one side".
- **The delta.** `finite_reading_withholds_renewal` adds the constructive witness ∃, by the same two-line proof from `prefix_does_not_decide`.
- **Already in prose.** The header of `Becoming.Horizon` states the dichotomy: "either withholds credit from a run that the whole-run reading classifies as renewing, or credits one it classifies as consuming".
- **Fix.** Under AGENTS.md this is a corollary of the existing horizon result, not an independent result. Record it there, with this delta. Consider stating `no_exact_finite_reading` as the headline.

<a id="f10次要对-p42-的复用--reuse-of-p42"></a>
### Reuse of P42

- **The delta of `unregistered_beyond_registration`.** It extends `unregistered_beyond_influence` with observed levels, through `agrees_of_quiet`. Under `supportOnly` it reduces to the P42 theorem (`withinRegistration_supportOnly`).
- **Record.** It should be recorded as an extension of the P42 record, with the reused IDs and the delta (observation), not as an independent result. B1 (F4) is the substantive delta, if it is adopted.

<a id="f11次要tested_by_dweller-近乎定义--tested_by_dweller-is-near-definitional"></a>
### `tested_by_dweller` is near-definitional

- **The relation is correct.** The claim `Ended` is a claim about the dweller's admission, and the dweller's registration is its admission. So "the dweller refutes that it is ended" is close to definitional. "The clearer never refutes it" follows because the clearer registers nothing about the habitat.
- **A more informative witness.** C5 `ClearingPooled.pooled`: in the spared world, at the third step, neither the clearer nor the dweller refutes "the dweller or the clearer is not admitted", and the pair does. That is testing that needs two positions.
- **Fix.** Optionally add C5 beside `tested_by_dweller`.

<a id="f12次要缺少到-becominginquiry-的桥--no-bridge-to-becominginquiry"></a>
### No bridge to `Becoming.Inquiry`

The plan's T1 asked for this bridge. D gives it at the level of a judgment:
- **Belief.** A formation's belief at `t` is the set of histories it registers alike with the actual up to `t`.
- **Refutation.** It is disjointness from the belief (`belief_refutes_iff`).
- **Judgment.** A judgment from the registration is a `CommonResponse` of `judgeProcess` over the belief (`belief_judge_iff`, via `commonResponse_judge_iff`).
- **Narrowing.** Later steps and more observation narrow the belief and keep every common response (`belief_judge_later`, `belief_judge_widen`, via `commonResponse_antitone`).
- **Beyond the closure.** A judgment from within the registration closure must be admissible both with and without a part beyond it (`belief_judge_beyond`).

The multi-step `Scope` bridge, with a policy whose sensing factors through registration, remains open.

<a id="f13次要名字--names"></a>
### Names

See §5. In order of importance:
- `RespondsThrough` misdescribes the hypothesis (F2).
- `surplus_*` is economic vocabulary.
- `threshold_blind` and "blindness" are metaphors where "subthreshold" is the scientific term.
- `AlikeUpTo` is too generic in `Web`.
- `Gated` reuses the spine's "gated" (gated renewal, the support-gated law) for a different relation.
- `Ended` is specific to the dweller.
- `admits_iff_supported` mirrors `Web.supported_iff_admits` (`Becoming.Admission`) with a different statement.
- `one_ne_two` and `two_ne_three` are generic arithmetic at the `Becoming` root.
- The README's Chinese 计入 for "registers" has an accounting sense. The recent commits removed "accounting" from the core (eef040d3, 968e1ef4). The plan's 登记 has an administrative sense.

---

<a id="3-建议的更强定理--proposed-stronger-theorems-all-checked"></a>
## 3. Proposed stronger theorems (all checked)

| Id | Declaration | File | Statement in brief | Axioms |
|---|---|---|---|---|
| A0 | `Flow.threshold_blind_no_webs` | `ProbeThreshold.lean` | `threshold_blind` without the second web's `requires`/`need` | none |
| A1 | `Flow.alike_keeps_difference` | `ProbeThreshold.lean` | While alike, exchange following registration keeps each registered difference; no start hypothesis, no `DecidableEq` | none |
| A2 | `Flow.alike_while_poorer_supported` | `ProbeThreshold.lean` | Richer (≥) on registered conditions and alike on observed ones at the start ⇒ alike while the poorer supports; several stocks, no `DecidableEq` | none |
| A3 | `Flow.alike_iff_richer_only` | `ProbeThreshold.lean` | Under the invariants: alike ⇔ (richer admits ⇒ poorer supports) | none |
| A4 | `Flow.changed_after_divergence` | `ProbeThreshold.lean` | A registered difference changes only after a divergence (richer admits, poorer not) | none |
| A5 | `Flow.threshold_blind_of_general` | `ProbeThreshold.lean` | The module's theorem from A1 + A2 | none |
| A6 | `JointFailure.untouched_after_joint_failure` | `ProbeThreshold.lean` | Both webs fail; the difference stays one forever | none |
| A7 | `Attracting.richer_breaks_first` | `ProbeThreshold.lean` | A taker responding to the stock: the richer web ends `g` first; `RespondsThrough` fails | none |
| A8 | `Exact.registers_threshold_only`, `Exact.observed_registers_level` | `ProbeThreshold.lean` | Unobserved: only the threshold registers; observed: the level registers | none |
| B1 | `Flow.Balances.alike_within_closed` | `ProbeReach.lean` | Reach blindness where the members respond through their own registration | none |
| B2 | `Flow.Balances.alike_within_registration` | `ProbeReach.lean` | B1 for `f`'s registration closure through both flows | none |
| B3 | `Flow.withheld_instance` | `ProbeReach.lean` | P47's fixed-rest theorem as an instance of B1 | none |
| B4 | `ClearingResponsive.alike_for_clearer_responsive` | `ProbeReach.lean` | `alike_for_clearer` as an instance of B1 | none |
| B5 | `Flow.withinRegistration_mono_obs`, `_mono_flow` | `ProbeReach.lean` | The closure grows with observation and with exchange | none |
| C1 | `RefutesWithin`, `refutes_iff_within_all`, `.narrow`, `.not_meets` | `ProbeTesting.lean` | Refutation relative to a model; soundness needs the actual history in the model | none |
| C2 | `tail_untested` | `ProbeTesting.lean` | Over all histories, a whole-run claim and its rival are both unrefuted by every finite record | none |
| C3 | `model_refutes_tail` | `ProbeTesting.lean` | Relative to a model of the exchange, observing a stock refutes at step 0 every false claim that it comes to zero | none |
| C4 | `Stationary.model_error` | `ProbeTesting.lean` | A wrong model refutes a true claim | none |
| C4b | `Stationary.model_refuted` | `ProbeTesting.lean` | Registration refutes the model (empty belief) | none |
| C5 | `RefutesBy.of_member`, `ClearingPooled.pooled` | `ProbeTesting.lean` | Pooled testing: the pair refutes what neither member does | none |
| C6 | `refutesWithin_iff_conjunction` | `ProbeTesting.lean` | Model-relative refutation is refutation of model ∧ claim | none |
| C7 | `beyond_needs_model` | `ProbeTesting.lean` | Beyond the registration closure, refutation rests on a model the withheld levels do not meet | none |
| C8 | `ClearingModel.model_idles_registration` | `ProbeTesting.lean` | A complete model refutes without registration | none |
| D | `belief_refutes_iff`, `belief_judge_iff`, `belief_judge_later`, `belief_judge_widen`, `belief_judge_beyond` | `ProbeTesting.lean` | The bridge to `Becoming.Inquiry` | none |
| E | `Renewable.sound_not_complete`, `withholds_not_not`, `no_exact_finite_reading` | `ProbeTesting.lean` | What `credits_consumption` already gives | none |
| F1 | `Gauged_own` | `ProbeStanding.lean` | In `Gauged`, `ownStanding` is the stock gauge | none |
| F2 | `Prey_omits` | `ProbeStanding.lean` | The prey is unaffected by what it registers; not self-bearing; the predator is not embodied | none |
| F3 | `SelfPrey.within_influence`, `SelfPrey.threshold_on_oneself` | `ProbeStanding.lean` | Self-bearing: the predator lies within influence; the bite registers by threshold, not by gauge | none |

**Suggested integration order.**
1. B1, with B3 and B4 as corollaries, replacing the reach section's central theorem.
2. A1, A2, A4 and A8, with A5 as the old statement.
3. `RefutesWithin` with C2, C3, C4/C4b, C6 and C7, rewriting the horizon and falsifiability readings.
4. F3 (`SelfPrey`) beside or instead of `Prey`.
5. D, if the module may import `Becoming.Inquiry`; it is in the pure core, so this keeps purity. Otherwise D goes into a small bridge module.

---

<a id="4-读法评估--the-readings-question-7"></a>
## 4. The readings (question 7)

| Reading (module header / plan) | Assessment |
|---|---|
| Three blindnesses of feedback: threshold, horizon, reach | **Supported in scope; not exhaustive.**<ul><li>Threshold holds where exchange follows registration (F2).</li><li>Horizon holds where the continuation is open (F1).</li><li>Reach is fixed-rest in the module, responsive in B1.</li></ul>Other blindnesses already on the spine are not mentioned:<ul><li>net exchange (`agrees_iff_even`);</li><li>support as one joint bit, which does not say which requirement failed (A8 with several requirements);</li><li>timing (`Late`).</li></ul>The horizon one is a theorem about runs of a process, not about `Web`/`Flow` registration; the module does not connect them (F1, C2, C3). |
| A runaway is a loop inside a blindness: its gains register, its losses do not until the break | **Overreach.**<ul><li>No loop, runaway or gain is defined.</li><li>"Gains register" has no counterpart: draws do not register (only support does), and activity is supplied.</li><li>Under responses to the stock, losses can register sooner in the richer world (A7).</li><li>Holds as a heuristic within the hypothesis of F2.</li></ul> |
| Measurement registers a level below the threshold (`Gauged`) | **Supported**, exactly by A8. `Gauged`'s `RespondsThrough` is vacuous (F8), and measurement is supplied (`obs`), not formed. |
| A model of where the run goes crosses the horizon | **Plausible; unproved in the module; checked here with its costs.**<ul><li>C3: a model makes whole-run claims refutable.</li><li>C6: the refutation is of model ∧ claim.</li><li>C4: a wrong model refutes truths.</li><li>C4b: registration refutes the model.</li><li>C7: beyond the closure only a model can judge.</li></ul> |
| Others' registration and new exchanges widen the closure | **Mis-cited (F8).**<ul><li>True of new exchanges and observation (B5).</li><li>Others' registration tests what one cannot (C5, `tested_by_dweller`), but it reaches one only through a relation the representation must contain. When it does, that relation is an exchange or observation, so this reading reduces to B5.</li></ul> |
| Falsifiability: a claim and its rivals must differ in what can register | **Supported:** `Refutes.not_of_alike`, the necessary condition. |
| …the condition of being corrected by the unfolding | **Unformalized.** Nothing revises a claim; "correction" needs an updating organization. Causal claims are not covered (F6). |
| …relational | **Supported** (`tested_by_dweller`; more strongly C5). |
| …moves with what is registered | **Supported** (`Refutes.widen`, `Refutes.later`; B5). |
| …claims about the whole run are not tested by any finite record | **Overreach (F1).** True only where the continuation is open, or trivially for `Refutes` (C2); false relative to a model (C3). |
| 理 is the model that registers what 心's feedback cannot (plan §2a) | **Plausible; reword.**<ul><li>A model does not register. It narrows the admissible histories, so that the same registration decides more (C3, C7).</li><li>It can mislead (C4), and registration corrects it (C4b).</li><li>So 理 regulating 心 is a loop in which 理 is itself answerable to registration, not a second register.</li><li>The formation of such a model is not derived (module's own "not derived").</li></ul> |
| Plan (b): reasoning over the same registration makes no new distinction; updating keeps what was robust | **Supported**, now in the module's terms by D: the belief is fixed by registration (`belief_refutes_iff`), and common responses survive narrowing (`belief_judge_later`, `_widen`). "Learning is a change of organization through what registers" is not formalized. |
| Plan (e): no better guardian; only distributed registration covers reach | **Partly supported.** Pooling tests what no single member can (C5). "Only" is not proved. |

---

<a id="5-名字--names-question-8"></a>
## 5. Names (question 8)

Ren's criteria (`2026-10-10-structural-names`, `zero-axiom-part-and-names`): formal, scientific and systems words; not social or financial; no limited-scope or dualist word where a structural one exists.

**Lean name clashes.** No name of the module occurs in `Bridge.lean` or in any other core module (grep over `Becoming/*.lean`). `section Gated` in `Becoming.Continuation` creates no namespace, so `Becoming.Gated` does not clash, but the concept is reused (below). `Becoming.one_ne_two` does not clash in core Lean 4.29.1 (`ProbeNames`).

| Name | Assessment | Proposal |
|---|---|---|
| `RegistersAlike` | Acceptable. "Register" is measurement vocabulary (an instrument registers). It means "makes the same difference to `g` at `t`". | Keep. In Chinese, avoid 计入 and 登记; use 对 g 不可辨 or 在 g 中显现相同. |
| `AlikeUpTo` | Too generic in the `Web` namespace (alike in what?). | `RegistersAlikeUpTo`, or the observability term `IndistinguishableUpTo`. |
| `Refutes` | Acceptable as Popper's term. For formations without inquiry (the dweller), read it as "the registration excludes the claim". | Keep, and say so in the docstring. Optionally `Excludes` in the core, with "refutes" in prose. |
| `Registers` | Imprecise. For a dependence, `g` registers only the joint support bit, not `c`'s level (A8). | Keep and fix the docstring ("enters what registers in `g`: through support's threshold if depended on, its level if observed"), or `EntersRegistration`. |
| `RegisteredFrom` | Parallel to `AffectedBy`; fine. | Keep. |
| `WithinRegistration` | Parallel to `WithinInfluence`; fine. | Keep. |
| `RespondsThrough` | **Misleading.** It is a hypothesis on the totals of all formations' exchange on `g`'s registered conditions, not on `g`'s responses (F2). | `ExchangeFollows` or `FollowsRegistration`, with the docstring "the exchange on what `g` registers follows `g`'s registration". |
| `supportOnly` | Fine. It names the resulting registration. | Keep. |
| `ownStanding` | Fine as a name. It should be presented as one observation, a gauge of oneself (F3). | Keep, or `selfGauge`. |
| `threshold_blind` | "Blind" is a sensory metaphor; "subthreshold" is the scientific term (as in subthreshold stimuli). | `subthreshold_alike`. Chinese 阈下. |
| `surplus_untouched`, `surplus_after_break` | "Surplus" is economic vocabulary. "Reserve" is taken (`Becoming.Reserve`, a technical sense), and so are "margin" (`Margin`) and "excess" (joint excess). | `difference_kept` and `difference_changes_after_divergence` (A1, A4). |
| `Gauged` | Good. | Keep. |
| `Gated` | Reuses "gated" from gated renewal (`Continuation`, `section Gated`) and the support-gated law (`Horizon`, `Feedback.law`) for a different relation: drawing while supported. | `Thresholded` or `SupportDrawn`. |
| `Prey` | Ecological; fine. Revise the witness (F3). | Keep, plus `SelfPrey`. |
| `Ended` | Specific to the dweller and to step 2. | `DwellerEnded`. |
| `one_ne_two`, `two_ne_three` | Generic arithmetic exported at the root of `Becoming`. | Make them `private`, or use `by decide` in place (axiom-free, `ProbeNames`); avoid `nomatch` (it brings in `propext`). |
| `Web.admits_iff_supported` | Mirrors `Web.supported_iff_admits` (`Becoming.Admission`, one web) with a different statement (two agreeing webs). | `Web.admits_iff_supported_of_agree`. |

---

<a id="6-自身水平的决定--the-decision-on-own-standing-question-6"></a>
## 6. The decision on own standing (question 6)

**For counting own standing as registered (the module's choice).**
- **One relatum.** In the one-kind reading, formation `g` and condition `g` are one relatum (`Becoming.Roles`). A change in `g`'s standing is a change in `g`. Denying that it registers in `g` could look like splitting the formation into an observer and its body.
- **Being taken from.** It is the most direct relation one undergoes. A representation in which a prey registers being eaten only through its food would be odd.
- **Harmless formally.** `obs` is a parameter, and every theorem holds for every `obs`.

**Against it, and for registration through self-bearing.**
1. **The module's own principle.** Through dependence, registration is a threshold, one support bit (A8). `ownStanding` gives the formation an exact, full gauge of its own level, which no other relation gets. That is privileged, transparent self-access.
   - The nondual method lists observer/world and knowing/acting among the pairs whose relation must be reconstructed. It warns against beginning "with a neutral object plus an external meaning-giver". Knowing "occurs within this unfolding".
   - An exact self-gauge by default supplies a knower rather than explaining one.
   - Registering one's own standing through what one needs of oneself treats the formation's relation to itself like its relation to any condition. That is the more nondual choice.
2. **The spine already has the relation.** `Web.SelfBearing`: depending on one's own standing at a positive need. Roles itself says embodiment and self-bearing are "readings under the identification", which the representation supplies as a correspondence premise. `ownStanding` is a further reading of the same kind, not a consequence of the identification.
3. **`Prey` shows the decision, not its warrant.** The predator lies beyond the influence closure only because the prey does not bear on itself (F2). In the representation the registered difference affects nothing the prey does or undergoes. The predator is active with zero standing.
4. **Self-depletion.** Under `ownStanding`, blindness to the depletion of what is carved as one's own standing cannot be expressed (F1 `Gauged_own`). Yet unnoticed self-depletion until collapse is a central runaway, as in overwork, addiction or a body's slow loss. The same reserve carved as a held condition (`Reserve`'s `hold f`) is threshold-blind. The verdict depends on the carving.
5. **The module's own list.** It says "What is not derived: that a formation observes anything beyond its support". Own standing is beyond support, so making it observed by default contradicts the list.

**Recommendation.**
- Keep `obs` parametric and `supportOnly` as the base.
- In the one-kind reading, register own standing through `SelfBearing`, so that it registers as a threshold.
- Treat `ownStanding` as a formed observation premise, a gauge of oneself, beside `Gauged`'s stock gauge.
- `SelfPrey` (F3) then gives the informative contrast: a bite registers through support only if it brings the standing below the self-need, and a gauge of oneself registers any bite.
- This is a representation choice, as the plan says. It does not change any theorem.

---

<a id="7-修正清单按严重程度-corrections-in-order-of-severity"></a>
## 7. Corrections, in order of severity

1. **Horizon and falsifiability readings (F1).**
   - Restate both readings with the open-continuation scope.
   - Add `RefutesWithin` and C3, C4/C4b, C6 and C7.
   - Change "every finite test errs on one side" to "no finite reading is exact" (`no_exact_finite_reading`).
2. **`RespondsThrough` (F2).**
   - Rename it and fix its docstring.
   - Add its scope to the readings and the README row.
   - Preserve `Attracting`.
3. **Own standing (F3).**
   - Use registration through self-bearing as the default.
   - Present `ownStanding` as an observation premise.
   - Add `SelfPrey`.
   - Record what `Prey` omits.
4. **Reach (F4).** Adopt B1 as the reach-blindness theorem, with B3 and B4.
5. **Threshold (F5).**
   - Drop the idle `requires` and `need`.
   - Adopt A1, A2, A4 and A8.
   - Say "difference changes" and "divergence".
   - Fix the section heading at line 258.
6. **Counterfactual claims (F6).** Add to "What is not derived"; keep `Ended` as worded.
7. **Provenance (F7).** Preserve Ren's acceptance in `sources/`, or write "pending Ren".
8. **Citations (F8).**
   - Lines 53–56: cite `surplus_untouched`.
   - Line 412: `Gauged`'s vacuity.
   - Lines 67–69: cite B5 and C5, not `tested_by_dweller` and `widen`.
   - Lines 502–505: "before the third step".
9. **Records (F9, F10).**
   - Record the horizon dual as a corollary of the horizon record.
   - Record `unregistered_beyond_registration` as an extension of P42's record.
10. **Witnesses and the bridge (F11, F12).** Optionally add C5 and D.
11. **Names (F13, §5).**

---

<a id="8-探针文件--probe-files"></a>
## 8. Probe files

All files are in `scratchpad/p47/review/`.

| File | Content | Result |
|---|---|---|
| `Audit.lean`, `Audit.out.txt` | Axiom audit of every constant of `Becoming.Testing` | 127 constants, 0 with axioms |
| `TestingCopy.lean` | Byte copy of the module (same sha256), recompiled | Clean |
| `ProbeThreshold.lean`, `.out.txt` | A0–A8 | 67 constants, 0 with axioms |
| `ProbeReach.lean`, `.out.txt` | B1–B5 | 37 constants, 0 with axioms |
| `ProbeTesting.lean`, `.out.txt` | C1–C8, D, E (imports `Becoming.Inquiry`) | 62 constants, 0 with axioms |
| `ProbeStanding.lean`, `.out.txt` | F1–F3 | 26 constants, 0 with axioms |
| `ProbeNames.lean`, `.out.txt` | Numeral witnesses; core names | `nomatch` forms depend on `propext`; `by decide` has no axioms; 2 intentional `#check` errors record that core has no `one_ne_two` and no `Nat.one_ne_two` |
| `ProbeAudit.lean`, `.out.txt` | Combined audit of the four probe modules | 192 constants, 0 with axioms |
| `olean/` | Copies of the probes compiled with `-o`, for the combined audit | Build artifacts only |

The probe `.lean` files' sha256:

| File | sha256 |
|---|---|
| `ProbeThreshold.lean` | `b9e9b8c2ce2399e71262ceb577a15ca6cb33b1256b150148a31f601abd3bc6cf` |
| `ProbeReach.lean` | `7f8da9f1b915e39986554ff36d06e81e175fd896a1c0ff1e6d084b74f69cadf4` |
| `ProbeTesting.lean` | `2ad175f9b7faa3b10da43090cf8a520cae38e2684867dadd0b4fee730968ed2a` |
| `ProbeStanding.lean` | `0a3ea312c715e501ecac5ba5b9c88d9339fff11ed0aca712d6e8f20a6b0a824a` |
| `ProbeNames.lean` | `b0aa6640026484a13a8962d40d76b3257841c76b7a4f09fa85df3b7b282b4cac` |
