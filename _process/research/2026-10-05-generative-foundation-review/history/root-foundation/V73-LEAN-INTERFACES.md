# V7.3 and the available Lean interfaces

6 October 2026. AI-authored formal reuse audit for Ren's request to integrate the theory into the Lean generative model without adding assumptions or axioms. This records existing declarations, missing mathematics and one fresh library-dependency inspection. It does not claim that the six mechanisms have been proved from the root or that the no-assumptions requirement is met. The [mechanism audit](V73-MECHANISM-AUDIT.md) retains their full source scopes; the [assumption-elimination audit](ASSUMPTION-ELIMINATION-AUDIT.md) governs the stronger unresolved requirement.

## What is actually reusable

The current root [GenerativeCore.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean), importing `Std`, supplies an arbitrary action-labelled `Generative.Process`, its finite `Trace`, and exact statements about their declared meaning. These are structural interfaces. They do not assert that an actual selector is relative, a competence decays, a report is strategic, or an institution has authority.

The following distinction is essential: an existing theorem may require no new law when reused at its own conditional scope, but its application still needs the hypotheses in its type. No-custom-axiom compilation is also weaker than an empty `#print axioms` report. Neither establishes the physical or ethical interpretation of the definitions.

| V7.3 connection | Available Lean declarations and exact overlap | Still absent from Lean; restriction on reuse |
| --- | --- | --- |
| Common return → relative selection blindness | [MarketGenerativity.lean](../../../../experiments/market-generativity/formal/MarketGenerativity.lean): `MarketGenerativity.profits_difference` proves the exact rational identity that the declared two profit formulas differ by `gap fine q lobby cost`, independently of common price and levy. `shareStep` consumes that difference in the existing market law. | No general relative-selection invariance or Price-equation theorem was found. The market identity is an instance with supplied payoff definitions, not proof that every selector ignores common benefit. Its recorded proof has nonempty standard axiom dependencies. |
| Held evaluation → effective working objective | Existing learning/controller modules separate memory, observation and selection. These provide places where an actual changed objective could matter, not V7.3's continuation derivation. | No Lean derivation of common/relative discounted continuation returns, the working-weight formula, its nonlinear tail condition or the strategic extension was found. A rational algebraic rearrangement would not establish those returns or conditions. |
| Incoming influence → correction and capture | `MarketGenerativity.influenceStep`, `qualityStep`, `operatingStep`, `rectangle_one_step`, `rectangle_all_times`, `viable_guarded_step` and `safe_history_never_fails` formalize the existing paid discrete influence/liability/selection loop and conditional protected region. | No V7.3 continuous capture-network ODE, inbound row-sum certificate, core pruning or cascade theorem was found. The market law is a different, already supplied mechanism. `Generative.productProcess` synchronizes two constraints; it does not by itself construct the cross-coupled influence network. |
| Delegation → loss of independent competence | [Depletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean): `Generative.trace_reserve_bound`, `trace_length_bound` and `no_infinite_execution_under_depletion` constrain any declared natural reserve that strictly decreases on every event. | No V7.3 exponential disuse/recovery law, logarithmic lock time or competence-adjusted correction-rate theorem was found. Calling a natural reserve competence, or replacing the continuous mechanism with a new finite example, would not integrate that theorem. The strict-decrease premise must remain visible. |
| Communication → informative coordination | [ControllerRevision.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ControllerRevision.lean): `Generative.Learning.controlled_trace_commands`, `same_feedback_same_commands` and `same_feedback_excludes_incompatible_futures` establish an exact deterministic information interface for a supplied controller. | No uniform-quadratic cheap-talk equilibrium, relative-bias amplification or zero-sum payoff-equivalence proof was found. Equal-feedback results explain an informational obstruction; they do not explain incentive-induced suppression or faithful reporting. |
| Reform → survivable transition and maintained alternatives | `Generative.trace_append_iff` and `feasible_append_iff` retain actual successor conditions. [ResourceContinuation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean): `Generative.Conditional.support_trace_append`, `support_trace_bound` and `repeat_supported_cycle` retain supplied dated costs. Market declarations additionally include `reserve_accounting`, `reserve_preserves_floor`, `collar_recovers` and `failed_market_absorbing`. | No separatrix/dwell theorem, recruitable-alternative depth bound or S17 installation/booster/release certificate was found. The market's checked recovery collar is an existing scoped result, not S17. An actual closed accounted cycle allows finite repetitions; merely returning a projected label does not supply such a cycle. |

These searches covered the repository's active Lean sources, excluding preserved development/review copies when selecting reusable files. No active Lean declarations using real-analysis derivatives, infinite discounted sums, replicator dynamics, separatrices or cheap-talk equilibrium machinery were found. This is an inventory result, not a theorem that their formalization is impossible.

## Exact root interfaces that add no asserted mechanism

The following existing declarations can organize faithful integration without installing a new selected process:

- `Generative.trace_singleton_iff`: one-event traces coincide with the existing step relation.
- `Generative.trace_append_iff` and `feasible_append_iff`: composition uses the actual intermediate state.
- `Generative.projection_exact_iff` and `local_exact_iff_trace_exact`: local preservation/lifting and exact finite projected histories are equivalent. The equivalence does not assert that a proposed map satisfies either side.
- `Generative.feasible_difference_implies_projection_difference`: exact summaries must retain distinctions witnessed by different feasible futures, under the displayed exactness premise.
- `Generative.Learning.Refinement.closed_loop_local_exact` and `controlled_trace_exact`, in [ControlledRefinement.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ControlledRefinement.lean): supplied world exactness and compatible actual observations transport the same installed controller and inherited memory.
- `Generative.Conditional.trace_has_support_totals`: every actual trace has totals for the supplied edge valuations. Conservation or solvency does not follow until a separate `SustainLaw` is proved for that actual process.

These are useful because the proposed V7.3 integration must preserve state distinctions, observations, costs and continuation. Repackaging a mechanism's desired conclusion as a field of a structure or a preservation hypothesis would not discharge it. Reusing an existing conditional theorem is legitimate mathematics while remaining short of the no-assumptions foundation.

The existing tools use Lean `4.29.1`. The learning verifier assembles exact source bytes from root, conditional and learning directories into a temporary import path. Relevant module names are `GenerativeCore`, `ResourceContinuation`, `ControllerRevision` and `ControlledRefinement`; the marketplace file is the independent `MarketGenerativity` module importing only `Std`. The common toolchain does not establish a semantic equivalence between their laws.

## Fresh rational cancellation dependency check

A temporary scratch file imported `Std` and requested `#print axioms` for the existing rational algebra lemmas. The installed Lean `4.29.1` compiler returned:

| Declaration | Reported dependencies |
| --- | --- |
| `Rat.add_assoc` | `propext`, `Classical.choice`, `Quot.sound` |
| `Rat.add_comm` | `propext`, `Classical.choice`, `Quot.sound` |
| `Rat.add_neg_cancel` | `propext`, `Classical.choice`, `Quot.sound` |
| `Rat.sub_eq_add_neg` | `propext`, `Classical.choice`, `Quot.sound` |
| `Rat.sub_add_cancel` | `propext`, `Classical.choice`, `Quot.sound` |
| `Rat.add_sub_cancel` | `propext`, `Classical.choice`, `Quot.sound` |
| `Rat.ext` | none |

The scratch compile exited successfully. This inspected actual inherited proof dependencies; it did not change library or repository source. Invoking those lemmas directly instead of using `grind` or `omega` would still inherit their reported dependencies. `Rat.ext` alone supplies record extensionality, not the required rational arithmetic identities.

The historical [market verification output](../../../../experiments/market-generativity/formal/verification/MarketGenerativity.txt) likewise reports the three standard dependencies for `MarketGenerativity.profits_difference`, the market invariants and the recovery collar. In contrast, the historical [root output](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/verification/GenerativeCore.txt) records empty dependencies for its audited structural declarations, and the [controller output](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/verification/ControllerRevision.txt) records empty dependencies for the information-interface results above. Those existing mechanism checks were not rerun in this audit.

Therefore no `CommonReturn.lean` module was added through the tested library route: it would not satisfy the requested empty dependency report. This does not show that rational cancellation mathematically requires those axioms. A new constructive proof through rational normalization might remove them, but that proof has not been supplied or checked. Replacing rational payoffs with an integer illustration would avoid the requested domain and would not resolve this obligation.

The exact prospective algebraic target remains `(a+c)-(b+c)=a-b` over the existing `Rat` domain. A further exact characterization could relate equality of all pairwise differences to a common translation, using a designated index. Even a successful empty-axiom proof of those identities would establish only the algebraic core of V7.3's first mechanism. A selector's invariance must still be derived for its actual rule, rather than assumed or introduced by defining a new rule that has the desired property.

## Status

No new mechanism, payoff law, competence law, authority condition or ethical premise was installed. No six-mechanism Lean theorem or assumption-free generative model is claimed. The usable immediate contribution is exact structural integration of existing laws and histories, with their unresolved content still visible. The six V7.3 mechanisms retain their documented mathematical and empirical scopes until their actual missing mathematics and applications are separately discharged.
