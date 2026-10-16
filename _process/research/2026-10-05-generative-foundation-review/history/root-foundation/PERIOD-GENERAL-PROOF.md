# Completing the arbitrary-period inquiry bound

7 October 2026. AI-authored formal continuation of [the written period argument](PERIOD-LOWER-BOUND-ARGUMENT.md) and [its independent review](PERIOD-REDUCTION-REVIEW.md). This study addresses recognition and conditional resource selection inside the supplied native inquiry process. It does not supply ethical warrant, explain the entire native law without premises, or replace the first-priority normative-grounding programme.

**Verification status: completed.** The original-game correspondence and arbitrary-period conclusions below passed a fresh Lean 4.29.1 build of **21 modules**, with **796 new and 1,183 total axiom audits, all empty**, and no warnings or errors. The three generated Lean files were also reproduced byte for byte from the four saved witness inputs. The [source-bound receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/period-general-proof-verification.json) and [immutable run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/period-general-proof-runs/20261007T120131.192982Z/verification.json) preserve the exact checked sources, compiler identity, logs, hashes and generator replay. This closes the earlier missing Lean correspondence within the stated inquiry model.

## Exact target

The positive cycle carrier has arbitrary size. Its binary output pattern, primitive advance and read operations, full initial uncertainty over phase and a fixed reading inversion, and worst-case command budget are those already defined by `PhasePeriodSelection.knowsWithin`. A policy may stop early, read repeatedly, skip intermediate readings, and use different branches after each observation. The two requested output values may have different policies. This is the reset-free advance/read repertoire with a fixed unknown inversion; protocols adding reset or probe commands, randomized control, or expected-cost success criteria are outside this game. The output pattern need not have length equal to the carrier for the inquiry results; the cost corollary uses the original matching-length representation.

The checked statements are:

- `PeriodGeneralProof.no_six_commands`: no positive carrier admits both requested-value guarantees within six commands.
- `PeriodGeneralProof.bothValues_at_least_seven`: every such guarantee has a worst-case budget of at least seven.
- `PeriodGeneralProof.seven_has_one_triple`: a seven-command guarantee covers every cyclic seven-bit window by **one** native or complemented native factor triple.
- `PeriodGeneralProof.seven_repeatsEveryThree`: the original `repeatsEveryThree` predicate holds, including carrier divisibility by three.
- `PeriodCostSelection.nonrepeating_needs_eight`: every other carrier/output pattern requires at least eight commands if it admits any both-value guarantee.
- `PeriodCostSelection.three_phase_least_guaranteed_draw_unbounded`: remove the former period-eight upper bound from the original guaranteed-draw comparison, preserving its other premises.

These concern worst-case guarantees. A favorable realized branch can finish earlier. Cycles with no successful guarantee are not assigned a finite command minimum.

## Closing the original-game correspondence

The existing `PeriodStrategySemantics.knows_iff_policy` connects the exact original Boolean search with existence of a bounded stop/advance/read policy, for every belief, including the empty belief. This is the starting theorem, rather than an informal reading of the search code.

`PeriodFirstRead` handles the actual full unknown-start belief. A winning policy for each target yields a bounded reachable phase bearing that target. The other target therefore supplies the opposite-output witness needed to rule out stopping before any informative reading. Before the first reading, advance permutes all possible phases while retaining inversion, so those leading advances can be removed. The proof chooses the zero branch of the first read: for every phase, inversion equal to its actual output makes the first observed bit zero. That one residual policy therefore succeeds at every phase under its corresponding inversion. No symmetry between the zero and one branches is assumed.

The proof is constructive and permits any number of initial advances within the bounded policy. Its induction first obtains a strictly shorter successful residual, then extends its available budget by adding unused allowance. Extending allowance does not add a command. This keeps the distinction between worst-case bound and realized execution explicit.

`PeriodCycleWindows.window` encodes the seven actual outputs reached by zero through six applications of the native advance operation. It wraps around any short carrier as often as needed. `PeriodPolicyCover.local_is_original` proves that normalized local-word evaluation is exactly original policy evaluation at the walked phase with inversion equal to the starting output. The invariant `budget + position < 7` ensures that every needed coordinate exists.

`PeriodPolicyCover.policy_covered` is induction over **every** policy constructor. Each policy's successful words are contained in one member of a checked finite covering family at its budget, position and requested target. Stop, advance, both independent read branches and early stopping are covered. `winning_residual_covered` then supplies a single such member covering every actual cyclic window.

## Why the finite witness tables suffice

The earlier written argument proposed exact maximal-language enumeration. This proof route needs less: **certified coverage**. A finite family may include extra words or extra candidates, provided each policy has a dominating member. The lower bound remains sound because any actual successful cycle must still be contained in one of those members.

`generate_period_cover.py` selects family members and witnesses using ordinary Python arithmetic. Those choices are untrusted. `PeriodCoverRules` checks every stop, advance and read dominance witness pointwise on all 128 words, including the selected parent's index bound. The generic policy induction uses only these checked rules. It does not assume that the generator was implemented correctly, that the families are exactly maximal, that every family member is realizable by a policy, or that generic arithmetic mask operations preserve set semantics. The two target families are independently checked against their respective stop semantics and common relative-reading branches; no unproved complement correspondence is needed.

The residual root families contain 44 candidates at budget five and 201 at budget six for each target. These finite families cover bounded local policy behavior through the proved coverage induction; they do not enumerate or bound cycle periods.

`PeriodPrunedCover` checks concrete deletion routes. At each route step, all 128 words are checked: membership in the old mask together with an allowed successor and predecessor implies membership in the next mask. Actual cyclic next and previous windows provide those witnesses for every positive carrier, so every actual window survives each checked step. At route endpoints, finite checks certify the chosen covering candidate. The proof allows multiple components and needs no equality with a strongly connected component computation.

After root pruning, four candidates suffice for each six-command target and ten for each seven-command target. Joint routes preserve coverage by the intersection of the independently chosen target candidates. Every six-command joint route ends in the empty mask, contradicting the existence of the phase-zero window. Every seven-command route ends in the empty mask or one of the two native factor triples. Hence every actual window is contained in one common triple; the proof does not replace that disjunction by unrestricted membership in their union.

## Periodicity and the selection consequence

`PeriodWindowPeriodicity` derives the periodicity conclusion from the concrete common triple. Finite checked facts identify its deterministic three-state successor orbit. A general modular-walk proof shows that walking the carrier length returns to the starting phase. Returning in that three-state orbit forces carrier length divisible by three. This is stronger than merely noticing equality of coordinates zero and three, which alone would not justify the divisibility statement. The resulting three-step equality and divisibility give the original Boolean `repeatsEveryThree` predicate.

The draw comparison assumes **3 ≤ pattern.length** and given native configurations with the specified live-cell counts, the same other retained cells and the same workspace. It removes only the former upper bound of eight. The supplied retained-cycle representation remains `1 + 2n`, with the same native draw schedule. Each requested value may have its own policy, and every both-value guarantee in this advance/read game has a worst-case requirement of at least seven commands; the existing native three-phase information-game strategy attains seven. Every larger carrier retains strictly more cycle cells, giving greater per-command draw under those premises. The product comparison is therefore strict for larger carriers. It compares guaranteed inquiry budgets times supplied per-command draws; availability, execution capacity and acquisition of those represented configurations remain separate requirements. It does not select the native pattern by average known-phase waiting time: the earlier period-five counterexample for that measure remains valid.

The [independent composition review](PERIOD-GENERAL-PROOF-REVIEW.md) checks the first-read, local-policy and original-game composition modules against exact source hashes. It confirms the quantifier order, fixed inversion, initial phase permutation, early-stop handling and positive-carrier boundary. Its author supplied the separate pruning component; that boundary of independence is recorded explicitly.

## Premises and foundational scope

All differentiation here is internal to one specified process: output phase, recorded reading, inversion, command and retained configuration are coordinates and operations in that model. The proof does not assume a fundamentally separate observer or environment. It proves a conditional limitation on recognition and material realization within the supplied command and representation laws. It neither derives those laws from an unsupplied foundation nor turns efficient realization into a justified ethical objective.

The composed checked theorem removes the need to enumerate longer carriers for this inquiry bound. Further changes to commands, uncertainty, observation reliability, criterion of success or retained representation would define a different comparison requiring its own proof. The precise contribution to the governing programme is a universal-in-carrier-size implementation constraint, while normative warrant and the stronger no-assumptions account keep their independent scope.

## Source and receipt

All new source modules and witness generators are in the existing [inquiry-root sufficiency directory](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/). The [fresh checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_period_general_proof.py) compiles the complete import closure with Lean 4.29.1, captures every axiom audit and raw log, snapshots all sources and witness generators, verifies hashes after compilation, and rejects warnings, errors or any nonempty audited dependency. The successful [run directory](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/period-general-proof-runs/20261007T120131.192982Z/) contains all 21 source snapshots, their raw compiler outputs, all four witness inputs, the successful generator-replay log and the full audit map. Earlier receipts remain unchanged as records of their narrower results.
