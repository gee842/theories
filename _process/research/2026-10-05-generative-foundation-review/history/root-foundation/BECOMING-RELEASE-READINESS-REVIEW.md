# 生成之论：发布准备度全面审查 / Release-readiness review of the Theory of Becoming

2026-10-16 · on `main` 1a78f978 · six independent reviewers (Opus 5.5, read-only) plus one checker run by the lead · AI review, not Ren's words.

## 摘要 / Summary

**中文。** 证明在形式上是可靠的：核心与桥接没有 `sorry`、没有公理、没有 `native_decide` 或元编程；检查器在 1a78f978 上通过（核心公理为空，审计 9,753 条声明）。构造性逻辑的标定（排中律、LPO、WLPO、依赖选择）陈述正确。但多数单个定理是经典结果在本理论词汇中的重述；真正独特的是“纯前导、无选择、无命题外延”的形式化与“排中律／WLPO／LPO／依赖选择恰在何处进入”的前提地图。“统一、完整、封闭、零公理”的目标尚未达到：零前提多是把前提移入定理假设；脊柱有两个根（Process 与 World）并出现第三套方言（耦合数组 / `ExchangeLaw`）；第二部分仍有一条公理且其根据未给出。公开文字有若干超出定理的说法（含一处不存在的定理名）。建议：现在不整体发布；先做一次不需新证明的“打包”（修正文字、可复现构建、独立复核近期落地项、重跑连通度），然后发布一个限定范围的子集。

**English.** The proofs are formally sound: no `sorry`, axioms, `native_decide` or metaprogramming in core and bridge; the checker passes on 1a78f978 (empty core axiom report, 9,753 declaration audits). The constructive calibrations (EM, LPO, WLPO, dependent choice) are stated correctly. Most individual theorems, however, are classical results restated in the theory's vocabulary; what is distinctive is the prelude-only, choice-free, propext-free formalization and the exact map of where EM / WLPO / LPO / DC enter. The goal of "one unified, complete, enclosed, zero-axiom theory" is not yet met: zero-premise mostly relocates premises into theorem hypotheses; the spine has two roots (Process and World) and a third dialect (coupling arrays / `ExchangeLaw`); Part II keeps one axiom whose warrant is open. Public prose overclaims in several places, including one theorem name that does not exist. Recommendation: do not release everything now; do a packaging pass that needs no new proofs (prose fixes, reproducible build, independent review of recent landings, re-run connectivity), then release a scoped subset.

## 1. Soundness — sound, with caveats

Checker run by the lead in a detached scratch worktree at 1a78f978: `status: passed`, `core_axioms: []`, 123 core + 8 bridge modules, 9,753 declaration audits, 98 generated `injEq` constants on `propext` (no source declaration uses them), 78 inherited periphery modules using `propext`/`Quot.sound`/`Classical.choice` as designed. 1 Lean step ran, 677 were reused from `~/.cache/becoming-lean`.

| Finding | Severity |
|---|---|
| Core + bridge: zero `sorry`/`admit`/`axiom`/`native_decide`/`unsafe`/`implemented_by`/`extern`/`opaque`/`partial`/`macro`/`elab`/`set_option`; ~150 `decide` on finite goals, kernel-checked. Periphery (431 files): zero `sorry`/`axiom`/`native_decide`; `set_option` only resource/lint. | none |
| Checker enforces import closure (local files only, so no Mathlib/`Lean` meta in spine), core purity, per-declaration `#print axioms`, environment-wide `collectAxioms` for the core, prelude-only compile with warnings fatal. `step_key` hashes toolchain, binary, source and imported keys recursively: a stale pass cannot be reused for changed inputs. | none |
| **C1** Receipt is cache-dominated; the cache is outside the repo and unauthenticated. Not reproducible by an outsider without `BECOMING_FRESH=1`. | minor (provenance) |
| **C2** Declaration scanner is a column-0 regex (misses unnamed `instance :`, modifiers, indented decls). Core is backed by the environment audit; the bridge is not. | minor |
| **C3** `inherited_receipts` is a substring test over any passing JSON — records history, does not replace checking (inherited modules are compiled anyway). | minor |
| **C4** `Becoming.FallibleInquiry` receipt (10-13) no longer matches 24 modules it imports. | minor (periphery) |
| **V1–V5** Sound but thin: Unfolding base equivalences by `Iff.rfl`; `change_readings` six `.rfl`; ~86 `rfl` theorems and ~180 trivial proofs counted in totals; "least registration" only under `¬¬`; G0 from near-universal premises (`Neutral`). No sampled headline has unsatisfiable hypotheses or hypotheses containing the conclusion. | minor (substance) |
| LPO/WLPO defined standardly as `Prop`s, never assumed; Tail "rule" = `Nonempty (∀ s, Decidable …)` (stronger than WLPO), both directions proved; `RecursOrStops ⇒ LPO` and `⇔` settling not overstated; `runs_iff_selection` is DC at `Type 0`, both directions. | correct |

## 2. Claims against proofs

No false theorem was found. Over-reading is in prose:

1. **Dangling citation.** README.md:60 and OPENING.md:56 cite `World.rests_enclosed`; the theorem is `World.rests_unrefuted_enclosed` (Openness.lean:703), concluding `¬¬ ∃ N, RestsFrom N` under `Counted`, `Embodied`, `Balanced`, `Dissipative`, enclosure.
2. **"Universal invariants… in every universe… None of this needs an axiom."** Three senses are merged: no Lean axiom (true for core and bridge); premises as hypotheses ("Y iff Z", true); necessity of the whole (open, `theory-of-becoming-foundation`). The premise-free laws the opening leads with are definitional (`change_readings`), counting (`keep_pace`) or tautological (`Shown.run`); the README's own `[^no-law]` concedes they exclude nothing beyond the representation.
3. **"Arising and ceasing are one change"** — `Web.change_readings` (Change.lean:536) is `⟨.rfl ×6⟩`: a definition read three ways, not a law.
4. **G0 "folded".** `Unrestricted sig` (Significance.lean:130) is `∀ p t f, sig p t f`; the axiom is strictly stronger than G0 and makes significance constant. The record says so; README and OPENING do not. README.md:102 (hardcoded at `tools/research/navigation.py:220`) still says the Core "adopts one explicit axiom, G0"; GENERATIVITY-CHAIN C03 likewise.
5. **"The axiom is needed"** (`Web.significance_undetermined`) compares constant `True`/`False` valuations: it shows `sig` is a free parameter, not that the dynamics fail.
6. **"C is a law, not a premise"** (§6.13) holds by construction once `Better := Widens`.
7. **"Explains good and evil… basis of all ethics."** Under `Unrestricted` every closing loses, including predation, apoptosis, ending a cancer; discrimination needs a measure that is not proved. `loses_iff_beyond_margin` holds for every `sig`: credit the arithmetic, not the axiom. The "Open" status sits only in a footnote.
8. **Tail / Sensitivity "cannot be dropped"** is shown relative to a decision oracle; Bishop is not credited.
9. **Dissipation = the second law** is a modelling correspondence (integer unit lost per take), not established.
10. **"Every declaration has an empty axiom report"** is true of core and bridge; the ethics/alignment results the README features partly live in the classical periphery.
11. **Learnable / Unfolding readings**: the converse learner is handed the world and the target; the "shown" law is the history's own steps.

Exact and well-scoped: `World.law_iff_em`, `lossless_iff_returns`, Moore bounds (`sameTests_iff_within`, exactness), `run_iff_returning`, `runs_iff_selection`, Gluing parity law, Typicality concentration, the alignment record (G0 + J1–J4, honestly scoped).

## 3. Novelty

| Result | Class |
|---|---|
| Recurrence (lossless ⇔ returns in finite worlds) | known (finite permutation / pigeonhole), good formalization (no decidable equality, no choice) |
| Distinguishing N−1, N+N′−1, exact | Moore 1956 (credited), constructive refinement |
| Identification, two periods | Fine–Wilf (credited) |
| 2N−1 learner, least-bound learner | Gold 1967 identification in the limit — **not credited** |
| Refutation learner (N³−N)/4 | plausibly new, narrow (depends on enumeration order) |
| `learnable_iff` | observability characterization, near-tautological converse |
| Sensitivity/Tail WLPO/LPO; `law_iff_em` | Bishop/Ishihara/Bridges–Richman reverse constructive math — **not credited**; clean calibrations |
| Onward | lasso/pigeonhole; DC by definition |
| Loops/Remainder/Frequency/Routes | truncated Neumann/path-sum expansions; nilpotent ⇔ acyclic |
| Gluing + Quantum | Mermin/Peres (credited); Abramsky et al. 2015, Arkhipov 2012 not credited |
| Entropy, Flow laws | accounting identities; substance is in the modelling |
| Typicality/Situations | Chebyshev/Chernoff/Bernoulli — not credited |
| Metaethics/Significance (G0) | formally immediate; contribution is the premise audit and `bounded_rival` |

**Distinctive contribution:** (i) ~7,100 theorems in one choice-free, propext-free, prelude-only Lean spine; (ii) the exact premise map — where EM, WLPO, LPO and DC enter; (iii) a premise-transparent staging of the step from dynamics to ethics, with the egoist rival shown consistent (`bounded_rival`) and the axiom decomposed into presupposition + invariance step. That honest boundary is more valuable to philosophers and alignment researchers than any claim of having derived ethics.

## 4. Integration

- One `Process`, `Run`, `Frame`, `World`: no re-built base types.
- **Two roots plus a third dialect.** Process/Frame/Run and Web/Flow/World are linked by correspondence theorems (`Frame.world`, `World.exchangeRun`, `Run.toWithMove`, `ExchangeLaw.world`), not definitions. P110–P127 (Propagation … Onward, Loops, Remainder, Closing, Frequency, Gluing on `ParitySystem`) are stated on σ arrays / `ExchangeLaw` and mostly touch neither base.
- Import graph: DAG of depth 26; 73 of 131 modules import exactly one spine module; 38 modules imported by none, including older ones (Substitution, Wholes, Standing, Tower, Units, Transmission, Succession, Persistence, Listing, OneStep, OrderNormal, Relevance, Quantum).
- **Connectivity measure is stale**: THEOREM-CONNECTIVITY at 108e278e (946 of 6,089 apart; 124 meeting statements); P114's 971 → 799 was never re-run into the JSON; 18 modules added since. Quantum 37/37 and Learnable 17/17 apart (the latter partly a choice of base).
- Re-definitions: `CrossSituational.Distinct` = `Becoming.Distinct`; `Parting.after` = `Run.onward`; `Courses.anyChange` = `Parting.free`. Homonyms: `Returns` ×4, `Recurs`, `RunsDown`, `Registers`, `Alike`; `Ranking.Course` clashes with "course".
- Periphery: 567 modules / ~10.8k theorems; 20 import Becoming; 95 have no import link either way.
- Theories: none of the 16 non-Becoming theories cites a Becoming Lean name; meta-attractor alone has formal content connected (MarketInstances).
- Records: 227 records cite 7,245 Lean names; all but two resolve (`Distinct` ambiguous, `OneStep.Witness` a namespace). `learning-by-refutation` is kind theorem with no declarations.

## 5. Theory state

**Met:** zero Lean axioms in the core; one spine with shared base definitions; the zero-premise redirect executed (every premise use localized, laws as "Y iff Z"); logical strengths calibrated; P58/P59, 无明 plan, I4 table decided and landed.

**Not met:** necessity of the whole without substantive axioms (open); "enclosed" (about a dozen open groups in chapter §8); representation commitments (discrete steps, ℕ amounts, shared index, decided equality, listing) are themselves premises; the rest theorem rests on ℕ well-foundedness and is restored under refinement only by counting refinement as giving; Part II's axiom warrant (the invariance step) is unargued; the base is still typed carriers with relations as functions (`Process S A`, `Frame.realized`, `Web F C`, `Flow` take/give) — P69 removes the configuration/move split, the carrier/relation split remains; evaluation (`Valuation Pos C`) is an added layer.

**Review lag:** the seventeenth review (10-14) is the last independent one; about 20 landings since (P107–P127, I4b) are unreviewed; `one-axiom-yields-g0` is still `recorded-checked`.

**Strongest objections:** (O1) the no-premise laws are combinatorics of a chosen representation — conceded in labels, not in the opening; (O2) the ethics step is a choice, and under `Unrestricted` it does not separate good from evil without a further measure; (O3) meanings (生生 as generative space, 识 as registration, 理 as lumping) are mostly AI-decided under delegation, ratified with "I don't have context"; (O4) unity is mostly co-location, not inferential dependence; (O5) `¬¬` forms behind plain prose.

## 6. Codebase health

- `make research-check`: exit 0, 227 records, 0 errors, 0 drift, 0 broken links; 422 style warnings. `make research-test`: 101 passed.
- **CI is not running**: 54 of the last 60 GitHub Actions runs failed because jobs never started (account billing / spending limit). Last success 2026-10-15 16:32Z.
- Reproducibility: `lean/becoming/` has no `lean-toolchain` or lakefile; `check_becoming.py` hardcodes `~/.elan` paths; the Mathlib periphery depends on `~/repos/生生不息` (not in the repo) and toolchain v4.30.0-rc2, different from the core's v4.29.1; no "verify it yourself" instructions; the checker writes a run folder into the repo each run.
- Size: `.git` 5.6 GB (+344 MB `tmp_obj_*`); 69,881 tracked files, 47,192 of them in 759 retained check-run folders; `becoming-checks/` 169 runs, 435 MB; `.claude/worktrees` 156 GB in 51 worktrees; 130 branches (119 merged); 22 prunable worktree entries; 57 committed `.pyc`.
- Release hygiene: no LICENSE; third-party datasets and PDFs; private sources (`sources/12-claude-ai-chats`, `13-claude-memories`, `18-friend-conversations` audio); `/Users/ren` in 1,292 tracked files.
- Docs: README → OPENING → chapter is a good entry; MAP.md is September-era and English-only; OPENING has no Chinese edition; the premise card's cells are Chinese-only and list "Lean 4.29.1 内核与 Std" though the core uses only the prelude; one garbled zh clause in `where-a-run-goes-on`.

## 7. Verdict and path to release

**Are the proofs sound?** Yes, at the level checked: kernel-checked, axiom-free core and bridge, correct constructive statements. To make that claim to outsiders, one fresh run (`BECOMING_FRESH=1`) and an environment audit for the bridge are needed.

**Are they integrated?** Partly. Shared base types, but two roots joined by correspondence, a newer third dialect, a stale connectivity measure, and other theories connected in prose only.

**Ready to release?** Not as a whole. A scoped subset is credible after packaging; no new proofs are required for it.

### Before any release (no new proofs)

1. Fix public prose: the dangling `World.rests_enclosed`; the three senses of "zero axiom"; `change_readings` as definition; `Unrestricted` stronger than G0 (README:102 via `navigation.py:220`, GENERATIVITY-CHAIN C03); `significance_undetermined`; §6.13 C; "good and evil" into main text with its open status; `¬¬` forms; Learnable/Unfolding readings; scope of "every declaration". OPENING wording is Ren's to approve.
2. Credit Gold, Bishop/Ishihara/Bridges–Richman, Abramsky et al., Arkhipov, Chebyshev/Bernoulli, path-sum literature.
3. Independent review (the eighteenth) of P107–P127 and I4b; move `one-axiom-yields-g0` to reviewed or keep it marked.
4. Reproducible build: `lean-toolchain` + minimal lakefile in `lean/becoming/`; `elan which lean` or `LEAN` env; a read-only / `--out` checker mode; "verify it yourself" section; one `BECOMING_FRESH=1` run; extend the environment audit to the bridge.
5. Restore CI (billing) and confirm green on head.
6. Re-run THEOREM-CONNECTIVITY on head with `ExchangeLaw`, `orbit`/`next`, `Weights` either added to the base or shown instances of it.
7. LICENSE; decide what is private (sources 12, 13, 18; `/Users/ren` paths); decide on a public mirror versus the 5.6 GB history.

### Release 1 — constructive library (after the above)

About 20 headline theorems in one file in plain vocabulary with classical sources named: Recurrence (`lossless_iff_returns`, `returns_iff_keeps`, `rise_not_lossless`, `withHistory_never_returns`); Distinguishing/Identification (`sameTests_iff_within`, `Law.sameTests_iff_below_across`, exactness, `period_extends`, `bounded_agree`, `withBound_exact`, `rest_earliest`, `leastBound_exact`, `learner_rest_cubic`); `learnable_iff`; calibrations (`World.law_iff_em`, `not_through_sensitive_iff_rule`, `vanishDecision_iff_lpoRule`, `run_iff_returning`, `fan_no_run`, `runs_iff_selection`); Gluing (`global_or_contradicts`, `noGlobal_iff`) with the Mermin–Peres realization; `SelfLoop.polynomial_iff`; `carried_eq_courses`. A peripheral Mathlib bridge (`Lossless ↔ Function.Injective`, `Returns ↔ IsPeriodicPt`, list-holds ↔ `Finite`) and a short technical note with related work.

### Release 2 — later

Flow/World conditional laws, Entropy, and the G0 premise audit as a modelling-and-premise monograph: "these inferences are checked; these premises are open", headlined by `bounded_rival` and the presupposition + invariance decomposition. After the G0 derivation has an independent review, the README is aligned with its footnotes, and the two-root structure is reduced or plainly stated.

### Integration work (theory, not packaging)

One root (define `Frame`/`Run` as readings of `World` or name one base all families instantiate); a Courses-style instance module for the coupling-array frontier on `ExchangeLaw.world`; instances for Gluing, Typicality, Routes, Situations, Quantum, Retrodiction; remove the three re-definitions and disambiguate the homonyms; a manifest marking the 95 unlinked periphery modules historical or connecting them; bind `learning-by-refutation` to declarations.

## 8. Decisions that are Ren's

- Readings marked pending Ren: P120 Remainder, P123 Frequency, P125 Observation, P126 Tail, P127 Onward, I4b-4, `whole-first-and-bounded-centers`.
- Chapter §8 reserved items: OPENING and its footnote; 归于静止 vs 停 and "the rest theorem"; the name "closure bounds change" (running down, not closure, bounds change); 识 = sensitivity?; 理; **whether Ren holds the invariance step** (the crux of Part II); the representation decisions.
- Whether "agree with other readings" (10-16) ratifies all of D1–D39.
- Generativity-chain entries F30, M25, M20, C14, M15, M24, M26 and the C01 link.
- OPENING length, Chinese edition, attribution line.
- When Part I counts as enclosed enough to begin Part II proper; whether to attempt the no-axiom ethical step.
- Release scope, licensing, private material, and history weight.

## Provenance

Reviewers: Lean soundness; claims vs proofs; integration; codebase health; theory state and method; novelty and release readiness. All read-only, no Lean rebuilds. The lead ran `check_becoming.py` once (cache reuse) in a detached worktree at 1a78f978 and spot-checked the dangling citation, `change_readings`, `Unrestricted`, README:102 / `navigation.py:220` and the CI failures. This review is an evidence artifact, not an independent result.
