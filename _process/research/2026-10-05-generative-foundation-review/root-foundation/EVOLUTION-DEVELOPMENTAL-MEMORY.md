# Selected developmental relations: memory, interference and restoration

**Completed continuation, 8 October 2026.** [The theoretical study and counterreview](EVOLUTION-UPDATER-CONSEQUENCES.md) connects the consequence-to-updater replacement selected in §7 below: 36 additional checked theorems / 57 new audits, with this memory module unchanged. The next construction obligation concerns the available responsive rule and faithful success channel, not another generic memory or replacement gate.

8 October 2026. AI-authored theoretical derivation and author counterreview following Ren's “继续” and the [prospective protocol](EVOLUTION-DEVELOPMENTAL-MEMORY-PROTOCOL.md). **28 new Lean theorems / 44 new declaration audits pass.** The fresh build also checks the unchanged predecessor's 41 declarations; those are inherited results, not new achievements.

**中文结论：**在明确的非线性发育与选择模型中，逐项有利的关系更新可以形成从不完整线索重现两种格局的能力；继续偏向一种格局，会使另一种格局不能重现，即使此前的更新贡献全部保留。继续修改同一组关系又能恢复旧格局，无须清空历史。因此，**保留过去的改变、保有重现过去的能力、改善当前选择分数，是不同的关系性质。**这项条件性连接现已完成；下一连接是这些实际后果怎样参与更新规则自身的形成与修订。

## 1. The connection now established

The [preceding recovery](EVOLUTION-CONNECTIONISM-RECOVERY.md) derived a learning direction and sufficient recurrent conditions. A favorable local direction alone did not establish memory. This continuation connects, within one declared history:

**comparison of coefficient changes → retained selected relationships → development from incomplete cues → competing-pattern interference → further selected revision and restored recall.**

The pattern, developing profile and evaluating relation are differentiated roles within the modeled unfolding. A supplied schedule holds some relations fixed for analysis; it does not put an independent environment outside that unfolding. The model does not derive the formation of the schedule or evaluator. Nor are the pattern contributions separate stored objects: their decomposition records how the current matrix was formed, while recall depends on the relationships that actually operate together.

## 2. Primary comparison and exact model scope

Watson et al. already investigate evolutionary associative memory, incomplete/noisy cues and multiple selection patterns. Their reported nonlinear simulations are a substantive antecedent, not a result first proposed here. This round reads printed pp.1131–1133 of the preserved primary article in addition to the earlier model and analytical pages. [Watson et al., 2014, DOI 10.1111/evo.12337](https://www.richardawatson.com/_files/ugd/395d71_73b2fb6f638842949320c0dd26ccfd89.pdf). The [reading and provenance record](../../../../sources/evolutionary-selection/comparative-direction/README.md#developmental-memory-continuation) identifies the exact scope; no publication simulation or supplement is reproduced.

Use a finite real interaction matrix \(B\), profile \(p\), and binary selection pattern \(s_i\in\{-1,1\}\). Specialize the preceding developmental family to

\[
p_{t+1}=\tanh(Bp_t),\qquad W_s(p)=1+s^\top p.
\]

Here \(\tau=\delta=1\). The source's reported \(\delta=0.2,T=10\) run is **not** this specialization. Selection compares one developmental step starting from the fully adapted profile \(p_0=s\). Recall instead starts from a specified cue and follows any finite number of steps with the retained matrix. These horizons and initial conditions are explicit, different experimental roles under the same recurrence.

| Supplied relation | Its role and remaining explanatory obligation |
|---|---|
| Binary current pattern and initial profile \(g=s\) during selection | Represents adaptation to the current pattern; that adaptation is not derived here. |
| Both coefficient proposals \(+\eta,-\eta\), with \(\eta>0\) | Available variation and fixed step size; their origin and probabilities remain supplied. |
| Sequential sweep visiting each matrix entry once | Defines one complete learning episode, including self-interactions. Partial/random schedules and removing diagonal entries require separate proofs. |
| One-step score comparison and retention of the chosen matrix | Defines this deterministic selection/inheritance relation; no population fixation or reproductive interpretation follows automatically. |
| Order of current patterns and recall cues | Defines the history being tested; no endogenous context schedule or cue-generating mechanism is claimed. |
| Finite real network and tanh recurrence | Native laws of this local model; no biochemical formation or resource-cost model is supplied by these proofs. |

## 3. Deriving the retained update

For a proposal \(w\) at entry \((a,b)\), the exact nonlinear score difference is

\[
\Delta W_s=s_a\{\tanh((Bs)_a+w s_b)-\tanh((Bs)_a)\}.
\]

Strict monotonicity of tanh makes the positive proposal beneficial exactly when \(s_as_b>0\). The declared comparison chooses \(+\eta\) if it improves the score and \(-\eta\) otherwise. Under the stated binary-pattern assumptions the chosen proposal is always strictly beneficial and equals \(\eta s_as_b\). This holds for every current matrix, including matrices formed under earlier conflicting patterns. Theorems: `nonlinear_score_difference`, `positive_proposal_iff`, `selected_coefficient`, `selected_coordinate_gain`.

The sequential sweep therefore yields

\[
B' = B+\eta ss^\top.
\]

`accumulation_formula` proves the contribution of every visited coordinate; `learned_equals_store` derives the full outer-product update. `trained_equals_inherited` proves that iterating the actual comparisons from the zero matrix produces

\[
B_H=\sum_{s\in H}\eta ss^\top,
\]

with repeated patterns counted repeatedly. Formal lists place the newest episode first; the recursively evaluated older history occurs first in time. Thus the matrix used below is derived from the declared comparisons, rather than introduced as an unexplained memory matrix. The comparison law and proposal schedule themselves remain premises. Score improvement is relative to each episode's current pattern; it is not one global increasing objective across pattern changes.

## 4. What counts as recall, and when it persists

Define sign recall by \(s_i p_i>0\) for every coordinate. This distinguishes both patterns below, but does **not** assert exact recovery of amplitudes, asymptotic convergence, a unique fixed point, robust basin size or generalization to new combinations.

`history_field` derives

\[
(B_Hx)_i=\sum_{s\in H}\eta s_i\langle s,x\rangle.
\]

For a target contribution \(\eta ss^\top\) and remaining matrix \(R\), a sufficient one-step retrieval margin is

\[
|(Rx)_i|<\eta\langle s,x\rangle\quad\text{for every }i.
\]

`retrieval_margin` and `one_step_recall` show that this makes each next coordinate have the target sign. The bound is sufficient, not necessary: other contributions may support the target rather than oppose it.

Once the signs agree, `recall_preserved` proves preservation through every finite developmental step if

\[
s_i B_{ij}s_j\ge0\quad\text{for all }i,j,
\qquad B_{ii}>0\quad\text{for all }i.
\]

Negative interactions are allowed between coordinates whose target signs differ. The diagonal condition ensures a strictly positive contribution for each correctly signed coordinate. `enduring_recall` joins first-step retrieval to subsequent preservation. With equal positive contributions from any two binary patterns, `balanced_two_patterns_persist` proves preservation of each pattern's signs when development starts from that full pattern. This general theorem alone does not prove recovery from an incomplete cue; the following construction supplies that additional result.

## 5. One history: coexistence, loss and restoration

Let \(A=(1,1,1)\), \(C=(1,1,-1)\), and \(\eta=1\). Start at zero and perform the stated learning episodes. The outer products in this table are the derived retained matrices, not separate memory registers.

| Chronological episodes | Current matrix | Checked developmental result for every finite \(T\ge1\) |
|---|---|---|
| \(A,C\) | \(AA^\top+CC^\top\) | Cue \((1,0,1)\) recalls \(A\); cue \((1,0,-1)\) recalls \(C\). The missing second coordinate is reconstructed. |
| Then three more \(C\) episodes | \(AA^\top+4CC^\top\) | Even the complete old cue \(A\) develops with \(C\)'s signs, and therefore fails to recall \(A\). |
| Then four more \(A\) episodes | \(5AA^\top+4CC^\top\) | Cue \((1,0,1)\) again recalls \(A\). All earlier episode contributions remain in the sum. |

`common_history_realized` connects these matrices to the actual repeated comparisons. `both_recall`, `overwrite_changes_old_recall`, `old_recall_fails` and `old_recall_restored` establish the behaviors. Every coordinate update in this entire history satisfies the current-score improvement theorem; no matrix reset occurs between the stages.

One instructive relationship is \(B_{02}\). `balanced_relation_cancellation` checks its successive values **0, −3, +1**. Initially the two patterns' contributions cancel that interaction; subsequent selection recouples it negatively, and continued revision makes it positive. Coexistence is therefore realized by the formed organization of relations. It is not guaranteed by the mere presence of both patterns in the training record.

The restoration claim concerns the old pattern. It does not certify that every formerly accessible pattern remains retrievable after restoration, or that this particular repair is optimal.

There is also a genuine failure before any overwriting. With cue \((1,0,0)\) at the balanced stage, the third coordinate stays zero at every developmental step. `unresolved_coordinate` and `ambiguous_recall_fails` prove that neither full pattern is recalled. The two successful incomplete cues retain the distinguishing third sign; the failed cue does not. This is a failure of this matrix and recurrence, not a universal impossibility theorem for all cue-processing mechanisms.

## 6. The theoretical addition and author counterreview

The new connection makes historical retention and operative memory distinguishable within the same process. A past contribution can remain causally present yet become insufficient to reproduce its former effect because later relations change the combined field. Current improvement can therefore coexist with a loss of previously available developmental responses. Further selected change can restore one such response without removing the intervening history.

**Is the desired update hidden in a definition?** The selection operation is independently defined by a nonlinear score comparison. Its outer-product form and equivalence to the retained history are then proved. However, adapted initial signs, available proposals, their magnitude and complete coordinate access remain supplied. This is a real reduction of one model input, not a derivation of the entire learning mechanism from generativity alone.

**Is this full associative-memory theory?** No. The construction supplies partial-cue sign reconstruction and its persistence, alongside exact interference and restoration. Self-interactions are included, and a distinguishing cue is supplied. Capacity scaling, noisy-cue probabilities, attractor convergence, arbitrary sequences and the source's parameterized simulations remain outside the proof. The result also does not prove that tanh nonlinearity is necessary for these particular sign properties.

**Could a conventional connectionist account obtain the same result?** Yes. Correlation storage, cross-pattern interference and retrieval margins are established associative-memory ideas. Our contribution is this checked, source-mapped connection from the stipulated selected updates to positive and adverse developmental histories within the generative programme. It establishes neither algorithmic novelty nor broad superiority over evolutionary connectionism.

**Has the physical formation of the updater now been joined?** No. Existing [updater formation](../../../../theories/becoming/chapters/UPDATER-FORMATION.md), [inherited reconstruction](EVOLUTIONARY-ORGANIZATION-INTEGRATION.md) and [goal revision](../../../../theories/becoming/chapters/GOAL-FORMATION-AND-REVISION.md) retain their completed conditional scopes. Their histories cannot be spliced into this network merely because both use retained consequences; the operative variables, actual update access and causal interfaces must correspond.

**Does restored recall establish a good evolutionary direction?** Recall is an explicitly defined capacity, and \(W_s\) is a current comparison score. Neither is ethical authority. Whether a memory should be retained depends on its relationships and consequences under the completed G0/J practical commitments. No duty to preserve every historical pattern, universal favorable convergence or new ethical axiom is inferred. This causal result informs the wider alignment programme by showing exactly where locally successful updating can damage a previously realized capacity.

## 7. Completion and next connection

The selected task—derived retained update, partial-cue recall, interference and continued restoration in a common stated model—is complete. Do not reopen it as a generic missing-memory gate.

The next precise connection is **discrimination of the consequences of interference → formation or revision of the rule governing later updates**. Here the step size, selection horizon, proposal access and context schedule remain fixed. A continuation must explain how an actual consequence changes at least one of those relations, connect the change to subsequent recall, and preserve failures and tradeoffs. Existing updater-formation mechanisms are candidates to reuse after an explicit correspondence, not tasks to repeat from scratch. A freely supplied “protect memory” score would not explain that connection. Nor should preserving all memories be smuggled in as the ethical goal.

New empirical data are not a completion gate for this theoretical continuation. Population interpretation, biological applicability and comparative prediction retain their own separate requirements. The [broader theory's completion map](../../../../theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md#completion-requirements) remains unchanged.

## 8. Verification

The [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/DevelopmentalMemory.lean), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/check_developmental_memory.py) and [successful receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/developmental-memory-verification.json) bind the current result to a fresh temporary build. Lean 4.30.0-rc2 and Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa` are pinned. Source, compiler, checker, imports, manifest and logs are fingerprinted.

All 28 new theorems and 16 new definitions receive explicit dependency audits; the imported recovery module's 41 audits bring the rebuilt total to 85. Only standard `propext`, `Classical.choice` and `Quot.sound` logical dependencies occur. No added axiom, `sorry`, `admit`, unsafe proof shortcut or compiler warning is accepted. Failed development builds retain their diagnostic scope; the top-level receipt identifies the successful source-bound build. No independent-agent acceptance, new empirical validation or repository-wide audit is claimed. [Documentary checks](EVOLUTION-DEVELOPMENTAL-MEMORY-CHECKS.json) separately record links, source preservation and scoped integration.
