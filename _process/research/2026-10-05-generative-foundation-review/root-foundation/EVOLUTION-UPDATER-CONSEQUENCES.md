# From interference to replacement of the updating rule

**Selected construction correspondence completed, 8 October 2026.** [The derivation and counterreview](EVOLUTION-CALIBRATED-UPDATER.md) adds 30 checked theorems / 59 new audits. The rule and success-access inputs identified below are now recovered from acquired local readings and formed connections under explicit reference, transfer, component and extra-support premises. This predecessor’s 36 theorems / 57 audits and original support account remain unchanged; the new account declares its additional construction reserve.

8 October 2026. AI-authored theoretical derivation and author counterreview following Ren's “继续” and the [prospective protocol](EVOLUTION-UPDATER-CONSEQUENCES-PROTOCOL.md). **36 new Lean theorems / 57 new explicit declaration audits pass.** The two unchanged predecessor modules contribute 85 separately rebuilt audits (142 total).

**中文结论：**在同一保留历史中，持续追加的更新规则会反复造成“偏向常见格局—损坏另一格局—再次修复”；按实际反应决定是否继续更新的可用规则，则能在这个范围内避免再次破坏。实际反应能否获得支持，进一步决定更新器能否维持及何时允许重建。这里接通的是**更新关系 → 后续反应 → 支持与失效 → 更新规则的替换 → 改变后续更新**。替代规则的来源、可靠辨别及支持法则仍有明示前提；不是从“损坏存在”直接推出必然自我改进。

## 1. What this continuation must explain

The [preceding memory result](EVOLUTION-DEVELOPMENTAL-MEMORY.md) distinguished historical contribution, operative recall and improvement in the current selection score. It left the update rule fixed. This study follows a consequence of that rule into its continued operation or replacement. The performance difference is calculated from the actual tanh network, not entered as a table of updater fitness or an additional reward for preserving a privileged old pattern.

The developing relationships, supplied task profiles, task responses and updater support are local roles within one modeled unfolding. The complete relation matters: a response can affect updater persistence only through an actual return/maintenance link. The model states that link. It does not turn task success into an ethical judgment, or put the tasks in a fundamentally independent external realm.

## 2. The same network, two available updating rules

Retain the earlier profiles \(A=(1,1,1)\), \(C=(1,1,-1)\), full-decay tanh development and selected unit-size coefficient updates. Write

\[
B(a,b)=aAA^\top+bCC^\top.
\]

At each presented task \(s\in\{A,C\}\), first read the response \(p=\tanh(Bs)\). The task succeeds exactly when \(s_i p_i>0\) at every coordinate. Only then perform any update. The full task profile is supplied as both the starting profile and the target signal. **This round uses a one-step readout of full profiles**, not the preceding partial-cue theorem's arbitrary finite developmental horizon. The reduction is explicit; the earlier longer-horizon results remain unchanged.

The two available rules are:

- **Continual:** perform the preceding selected update after every task, whether the readout succeeded or failed.
- **Responsive:** perform that same update only after a failed readout; otherwise preserve the current matrix.

Whenever either rule performs an update, it invokes the preceding `learn` operation: the sequence of coefficient proposals selected by the specified nonlinear score comparison. `learned_first` and `learned_second` derive its exact action as \((a,b)\mapsto(a+1,b)\) or \((a,b+1)\). The earlier theorem still establishes strict current-score gain for each selected coordinate change. The responsive rule changes **whether those changes are admitted**, not their formula.

The responsive rule's availability and faithful success signal are premises. Its definition does not inspect a list of protected old patterns, future tasks or the desired outcome of the comparison. It does inspect every component of the current response against the current task signal. That informational access and its implementation must be accounted for when moving beyond this formal comparison.

## 3. The performance difference is derived

`first_field`, `second_field` and the strict monotonicity of tanh yield the exact conditions

\[
\begin{aligned}
A\text{ succeeds}&\iff 3a+b>0\;\land\;3a-b>0,\\
C\text{ succeeds}&\iff a+3b>0\;\land\;3b-a>0.
\end{aligned}
\]

These are theorems about the actual response, not independent success labels. `predecessor_networks` identifies the preceding balanced matrix with \(B(1,1)\) and its overwritten matrix with \(B(1,4)\).

Present the repeated cycle \(C,C,C,A\). Starting from \(B(n+1,3n+1)\), continual updating succeeds on the first three tasks. Before the last task its matrix is \(B(n+1,3n+4)\); the distinguishing \(A\) field equals \(-1\), so that task fails. Its ensuing update produces \(B(n+2,3n+4)\). Thus `continual_cycle` proves, for every natural \(n\), exactly **three successes per four-task cycle** and the actual retained next matrix. `repeated_continual_cycles` proves the joined finite history from \(B(1,1)\): after \(n\) cycles the matrix is \(B(n+1,3n+1)\) and the success count is \(3n\).

The first cycle ends at \(B(2,4)\). Both task responses succeed there. `responsive_stable` proves a general conditional result: whenever both responses succeed, any finite sequence of these two tasks under the responsive rule preserves the matrix and succeeds on every task. Therefore from the **same** post-cycle state \(B(2,4)\), responsive updating obtains four successes on the next cycle, while continual updating again obtains three and changes the matrix to \(B(3,7)\).

`routes_differ_after_failure` checks that this is an operative rule difference: on the next \(C\) task, continual updating changes the matrix whereas responsive updating does not. The latter's maintenance cannot be credited merely to a new updater label.

There is also an explicit repair result. If the responsive rule encounters the overwritten \(B(1,4)\) on task \(A\), it performs the selected update and reaches \(B(2,4)\), after which the stability theorem applies. This is `repaired_by_responsive`. In the replacement history below, however, **the old rule's final update has already made that local repair**. The new rule prevents its repeated destruction. We do not substitute the separate repair theorem for what actually occurs in the joined witness.

## 4. Actual returns enter maintenance and replacement

The support interface is deliberately explicit. Each four-task cycle requires four remaining source opportunities. A successful readout transfers one unit into the current stock; a failed readout leaves that unit unavailable and records it as waste. A live updater requires four stock units to renew at the cycle's end. If insufficient stock remains, the updater expires while the matrix and all remaining stock persist. An available proposal may then be installed for two stock units. Installation changes the updater and stock, never the network matrix.

This is a supplied coarse support law. It represents costly construction and performance-dependent maintenance; it is not derived chemistry. The return criterion requires the whole current sign response, whereas the earlier coefficient-selection score was the real-valued \(1+s^\top p\). We explicitly add this threshold-dependent return relation. A score improvement and successful completion can differ; silently treating them as the same fitness would invalidate the explanation.

The joined witness starts with the already developed \(B(1,1)\), an installed continual updater, zero stock and twelve source opportunities. Earlier formation of that starting network and updater is outside this suffix's support account.

| Event completed | Network | Operative updater | Stock | Source left | Spent | Waste |
|---|---|---|---:|---:|---:|---:|
| Declared entrance | \(B(1,1)\) | Continual | 0 | 12 | 0 | 0 |
| First actual cycle | \(B(2,4)\) | Expired | 3 | 8 | 0 | 1 |
| Responsive proposal constructed | \(B(2,4)\) | Responsive | 1 | 8 | 2 | 1 |
| Next actual cycle and renewal | \(B(2,4)\) | Responsive | 1 | 4 | 6 | 1 |
| Another cycle and renewal | \(B(2,4)\) | Responsive | 1 | 0 | 10 | 1 |

`complete_replacement_history` verifies this exact sequence. The old rule really caused the changing matrices and failed readout; its actual returns are insufficient for renewal. The new rule is installed from retained stock, governs subsequent updates and obtains enough actual return to renew twice. The twelve initial units are accounted for throughout. `cycle_conserves`, `installation_conserves` and `finite_history_conserves` prove the account for all finite event lists under this law. `final_account_and_exhaustion` proves that the final state cannot execute another cycle without additional source. This is finite realized renewal, not indefinite free replenishment.

The proposal is **not selected by an omniscient observer**. The construction event supplies an available candidate. Its later success determines renewal. The proof does not assign a probability to which proposal appears. If the same old continual type is proposed instead at the identical retired state, `old_proposal_fails_again` follows it through two cycles to another expiration, with network \(B(4,10)\), stock 3, source 0, spent 6 and waste 3. This adverse path preserves the dependence on available variation and actual proposal occurrence.

## 5. What is reused, what is still supplied

The existing [updater-formation construction](../../../../theories/becoming/history/UPDATER-FORMATION.md) already gives formed constituents, construction costs, resource-dependent turnover and subsequent use of a changed updater. It is a completed result, not a missing generic gate.

| Reused explanatory role | Present realization and composition boundary |
|---|---|
| A rule changes later reconstruction/learning | `update` governs whether the selected matrix update occurs; the two rules provably differ on the same input state. |
| Actual success sustains the rule that governed activity | Native tanh task responses determine transferred support, which enters the renewal condition. No updater-fitness table is supplied. |
| Failure permits a different constructed rule | Insufficient stock expires the old rule; an affordable proposal installs a replacement while preserving the matrix. |
| Continuing state and finite provision survive turnover | One support account includes actual success, loss, construction and renewal. Source exhaustion blocks further cycles. |
| Physical origin of the mechanisms | **Not composed here:** the earlier material slots, reactions and adapter differ from this real-valued network and packet law. No chemical or toolchain correspondence is claimed. |

Still supplied are the two-rule repertoire, accurate current-task comparison, fully specified task profiles and their cycle, ideal real arithmetic/tanh law, access to all coefficients, unit proposal magnitude, faithful matrix retention, support transfer, construction/renewal costs and the initially installed state. The current derivation removes an independently stipulated updater-performance table: its entries now follow from native development and actual task order. It does not remove all those remaining inputs.

## 6. Limits and author counterreview

**Does responsive updating always have greater return?** No. On the unchanged sequence \(C,C,C,C\), `unchanged_context_no_return_gain` proves four successes for both rules. The switching pattern matters. Under the stated cycle and common post-failure matrix, the raw return difference is one unit; `extra_cost_threshold` gives the exact comparison when different total costs are charged: the responsive net return is larger precisely when its excess cost is less than one unit. This cost comparison is a stated extension, not a cost already measured in the witness.

**Does the gate create its own reliable signal?** No. `false_success_blocks_repair` retains an explicit adverse case: reporting success at \(B(1,4)\) on \(A\) suppresses repair although the actual response fails. The main result requires a faithful comparator. A useful continuation must explain that access or derive the candidate updater's construction, rather than label its signal intrinsically meaningful.

**Is this spontaneous invention of a learning rule?** No. The candidate repertoire is supplied and includes a familiar response-sensitive alternative. We explain consequence-dependent replacement and renewal within this repertoire, including an unsuccessful proposal. We do not establish the evolution of the repertoire, mutation probabilities, hereditary spread through a population or open-ended invention.

**Is a single current task's response enough to protect every old capacity?** No. The invariant applies to the two stated tasks and one-step full-profile responses. Different profiles, noisy feedback, amplitude precision, other developmental horizons or a third task require new analysis. Suppressing updates after current success could preserve an inadequate representation in a richer domain. The earlier partial-cue and ambiguous-cue results remain at their original scope.

**Does the model evade the ethical issue by renaming success?** The task criterion and support law are declared causal premises. Support to this organization does not establish whole generative goodness. G0/J and the completed practical account keep their independent justificatory work within the same relational theory. The present result supplies a causal implementation condition for alignment: consequences must actually reach the maintenance or replacement of the updating relation. It proves neither ethical recognition nor inevitable alignment.

## 7. Comparison, completion and next connection

Learning-rule evolution is established comparative ground. Chalmers's *The Evolution of Learning* evolves encoded weight-changing procedures using task performance; its encoding restricts local variables and permitted forms, and the reported experiments include a delta-rule result. It studies a population and a broader candidate space than this two-rule turnover witness. [Author-hosted primary paper, §§2.1–2.2.6 and the inspected opening of §3.1](https://consc.net/papers/evolution.pdf). Bengio and colleagues likewise describe optimization over parameterized local learning rules, while distinguishing the search procedure's plausibility from that of the resulting rule. [Authors' 1992 announcement and abstract](https://mailman.srv.cs.cmu.edu/pipermail/connectionists/1992-January/014054.html). These sources receive credit; neither study is reproduced here. The [scoped reading record](../../../../sources/evolutionary-selection/comparative-direction/README.md#updater-consequences-continuation) records exactly what was inspected.

The contribution within our programme is the **checked common history from inherited developmental interference to an actually operative replacement rule, through explicit finite support**, with repeated failure and a different unsuccessful proposal preserved. Ordinary connectionist and control accounts can express the same mechanism. No field-wide novelty or broad superiority follows from giving it a generative interpretation.

The selected consequence-dependent replacement connection is complete at this stated scope. Its next unresolved input is more precise than generic “self-improvement”: **how an available response-sensitive updating relation and its reliable success access are constructed from local relations, while preserving the response and support correspondence established here**. Existing formation and acquired-evidence results can be reused only through a justified interface. The current two-rule palette and faithful comparator cannot be presented as their already-derived consequence. This is an additional derivation, not a prerequisite to crediting the completed replacement result. Empirical calibration remains separate from this theoretical continuation.

## 8. Proof and documentary verification

The [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/UpdaterConsequences.lean), [fresh-build checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/check_updater_consequences.py) and [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/updater-consequences-verification.json) identify the final checked claims. All 36 new theorems and 21 other explicit declarations pass, with standard logical dependencies disclosed. The two predecessor modules are rebuilt and their 85 audits counted separately (142 total). Lean 4.30.0-rc2 and Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa` remain pinned.

The checker binds source, compiler, imports, manifest and logs; it audits explicit declarations and rejects proof holes, added axioms, unsafe shortcuts and compiler warnings. Standard logical dependencies are disclosed. Syntax/proof-development failures retain their diagnostic records and are not scientific counterexamples. No independent-agent acceptance, empirical experiment or repository-wide audit is claimed. [Documentary checks](EVOLUTION-UPDATER-CONSEQUENCES-CHECKS.json) separately verify scoped links, source bindings and integration.
