# Structural inspection with fallible witnesses

8 October 2026. AI-authored continuation of [Ren's instruction](../../../../sources/15-codex-theory-conversations/2026-10-08-finish-alignment-fruits.md#continuation-through-fallible-inspection). Current theory: [alignment through change §10](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-THROUGH-CHANGE.md#10-fallible-witnesses-and-contested-control--见证可能失实时的共同控制辨认).

**Completed connection:** jointly interpret a structural claim and its possible witness failures, retain every compatible causal description, then use their common consequences in actual correction. No particular witness must be infallible. The new package has **24 checked Lean theorems / 41 declaration audits and 18,684 matched finite records**. Actual candidate coverage, the admitted joint-failure range and correctness of received reports outside it remain substantive premises.

## 1. The precise premise being weakened

The [previous result](EVIDENCE-QUALIFIED-CORRECTION-INTEGRATION.md) connects unresolved causal hypotheses to a conservative command certificate. Its inspection returns a supplied faithful structural answer. The present extension permits false or absent structural reports from several positions, including positions implicated in the very control structure being investigated. It asks when their conflicting reports support a narrower command-failure envelope.

[General model revision](MODEL-REVISION-INTEGRATION.md), [source reliance](SOURCE-RELIANCE-INTEGRATION.md), [route acquisition](ACQUIRED-CORRECTION-INTEGRATION.md) and [reviewer reconfiguration](CORRECTION-RECONFIGURATION-INTEGRATION.md) are already completed conditional results. They are reused, not reopened. The new inference is **contested structural reports → joint factual/fault explanations → retained command envelope → funded correction**. This is a specific implementation requirement for the existing G0/J account of ends and selection rules. It is not an additional derivation of that normative ground.

Under the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md), a witness is a reporting role formed within the same organizational relations it describes. A root cause can affect both command review and structural testimony. A diagnostic role and a command-approving role are distinguished by their actual capabilities and permissions; neither is outside the process. The model records these overlaps and the cost of collecting reports. It omits the development of the reporting abilities, identity infrastructure and embodied sensing relations. Their omission is not evidence that such relations are fundamentally separate or impossible to explain.

## 2. Joint interpretation prevents a specific circular inference

Let a hypothesis `h` supply a Boolean answer `A(h)` and an envelope `F(h)` of possible faulty witness sets. A registered report is true, false or missing. Retain `h` exactly when some `B` in `F(h)` can explain the transcript: every received report outside `B` agrees with `A(h)`. Missing reports impose no constraint. Disagreement is allowed inside `B`; it does not cause automatic deletion of the hypothesis.

This is consistency-based diagnosis, not majority voting or a posterior probability. The function is named `posterior` only for the resulting list after inspection. It assigns no probability, prior weight or preferred hypothesis. It searches for at least one admissible joint explanation for each candidate. It does not choose a candidate first and then use that candidate's favored witnesses to certify its choice.

`joint_refinement_preserves_actual` proves retention when the actual hypothesis was included, at least one admitted witness fault set contains all dishonest received reports, and reports outside it are missing or correct. Actual faults may be a subset of that admitted set; no exact fault identification is required. `joint_refinement_subset` proves that filtering does not introduce new hypotheses. All-missing reports retain every candidate with a nonempty envelope. An empty envelope supplies no explanation, so such a candidate is removed.

`refined_pool_remains_sound` then imports the preceding command certificate theorem. The actual hypothesis remains in the pool, so its covered command-failure sets remain constraints on certification. Inspection and command envelopes may differ; each has its own coverage and response premises. `jointly_inspected_completion` combines retention with the previous completion theorem. The post-inspection installation must still have a current request, faithful and responsive surviving command reviewers, a separated pooled envelope and enough work and time. The protected mandate check remains in force.

The completion theorem is a composition of existing execution guarantees with the new retention proof, not a new command implementation. It takes the installation after inspection costs have been paid. The executable `inspect`/`run` construction separately performs that payment, stores the actual received transcript, updates candidates and invokes the existing guarded command procedure. The example connects the two operations by actual state changes.

## 3. Exact scope of distinguishability

Consider two **opposite Boolean answers**, with witness-fault envelopes `Fa` and `Fb`. Lean proves the following equivalence for a fixed registered roster and complete transcripts:

> No complete transcript is compatible with both answers if and only if every pair `a ∈ Fa`, `b ∈ Fb` leaves a registered witness outside `a ∪ b`.

The witness outside both faults would have to report both opposite answers, which is impossible. Conversely, if an admitted pair covers the whole roster, the construction `ambiguousReports` gives a single complete transcript compatible with both answers: report the second answer inside `a` and the first answer outside it. This is an exhibited ambiguity under the specified report laws, not freely toggling an unrelated truth predicate.

For partial transcripts, the relevant common witness must have supplied a report. `received_common_survivor_forces_same_answer` states that directly. `responsive_survivors_exclude_opposite` allows faulty witnesses to withhold: if all actual surviving witnesses respond correctly, and each alternative fault set leaves a common survivor, an opposite answer is excluded. Thus complete reporting by faulty witnesses is unnecessary for this sufficient guarantee. Complete transcripts are the scope of the exact equivalence, not an execution precondition.

This is static factual discrimination at one collector. It does not prove distributed agreement, resistance to equivocation across different collectors, asynchronous termination, or the completeness of the hypothesis vocabulary. The condition uses pairs of candidate fault sets. It is not a replacement for the three-set conditions in Byzantine quorum protocols with stronger consistency requirements.

## 4. A conflict that additional names cannot resolve

Reuse the three command arrangements from the previous study. Four registered review positions have root supports `0,0,2,3` (left sharing), `0,0,3,2` (left sharing with the other supports swapped), or `0,1,2,2` (right sharing). Inspection asks whether cause 0 reaches reviewer 1. The answers are true, true and false. Each description admits any one of its listed root causes failing. Witnesses initially share those same causal dependencies.

The received transcript `false,false,true,true` is ambiguous. Left sharing explains the first two reports as compromised together; right sharing explains the last two that way. A more dangerous shortcut also passes: the left hypothesis's own certificate accepts true from positions 2 and 3, while the right hypothesis's own certificate accepts false from positions 0 and 1. Both locally certify the answer used to justify their own trust arrangement. `conflicting_models_each_certify_themselves` checks these two certificates and shows that joint interpretation correctly retains all three hypotheses.

Now add a fifth **diagnostic-only** position with distinct root support 4. It is allowed to fail alone; no witness is guaranteed individually reliable. The transcript `false,false,true,true,true` retains the two left-sharing descriptions and excludes right sharing. The pooled command envelope is now available. A different transcript `true,true,true,true,false` reaches the same structural conclusion even though the fifth report is false. The theorem therefore does not merely rename a trusted oracle.

The physical distinction matters. A fifth position sharing position 2's support leaves the original ambiguity intact: its report can be compromised together with the right pair. If the distinctly supported fifth report is absent, the four remaining reports also retain all three candidates. These counterexamples concern this transcript and failure range; four witnesses can resolve other transcripts.

The fifth position reports structural evidence but has no command-approval role in this example. Its omission from the command roster is an explicit scope condition. If a feasible fifth position could instead be authorized directly to review the command, expanding that roster might make structural diagnosis unnecessary. No superiority or minimal-cost claim over that alternative is made.

## 5. Paid execution and failures

Inspection charges one work unit and represented time slot for each of the four or five registered reports, including missing ones. A slot stands for bounded collection/timeout; this is not a proof of network response time. The recorded transcript contains `(position, optional answer)` pairs. The command then charges its existing eight collection units and three execution units when funded and certified.

With actual left sharing, cause 0 failed, and the five-report transcript above, sixteen units and sixteen steps suffice: five for inspection, eight for command evidence, three to complete shutdown. Two structural witnesses lie; the two command reviewers outside their shared cause support the actual correction. The remaining two structural descriptions are not forced into a unique answer about unrelated supports. The final state is stopped, completed and advanced to serial 1.

With only fifteen units, inspection still succeeds and two hypotheses remain, but command collection leaves two units, insufficient for the three execution operations. Thirteen spent units remain recorded. Without the fifth witness, the same four-report conflict leaves all three models; twelve units are spent inspecting and collecting command evidence, and correction remains uncertified. Denied inspection performs neither collection nor command execution.

The root range is a real condition. Under actual right sharing, the unadmitted joint failure `{2,4}` can compromise positions 2, 3 and 4. Those positions can produce the same five-report transcript that eliminates the actual right-sharing model. The wrong inference is retained as `uncovered_correlated_witness_failure_can_delete_actual`. The protected direct mandate guard still applies; this theorem shows failed diagnosis, not a demonstrated unauthorized-command bypass.

The simulation distinguishes arbitrary diagnostic reports from command response behavior. Diagnostic faults can lie or withhold. The concrete command simulator makes exposed command reviewers withhold, while the imported generic certificate theorem has its broader conditional scope. Root 4 affects only diagnostic support; it lies outside the preceding command module's named root bounds. Those finite cases are executions under the explicit formula law, not an assertion that the generic command `Covered` premise holds for every raw root list in the grid. The joint failure is likewise intentionally outside the guarantee.

## 6. Alignment argument and author counterreview

The practical conclusion is that the evaluative organization can be examined without granting one inspector unconditional epistemic authority. What matters is the relation between possible causes, possible false reports and a distinction sufficient for the required response. Retaining unresolved explanations protects correction from evidence that merely fits its favored controller.

Under G0/J, this supports a responsibility to scrutinize relevant control relations when losses and feasible alternatives make that scrutiny warranted. It does not make every test obligatory, every trustworthy witness entitled to command, or every technically possible shutdown good. Permission, burdens on affected lives, current obligations and the legitimacy of the supplied mandate retain their prior substantive evaluation. Technical separation of supports can help implement a justified decision; it does not generate its ethical justification.

| Counterreview | Resolution or retained condition |
|---|---|
| Has infallibility simply moved upward? | No particular witness is infallible, but joint-failure coverage and the behavior of survivors remain assumed. The result weakens a single faithful-read premise; it does not eliminate all correspondence assumptions. |
| Can the preferred model choose which evidence counts? | It can explain reports under its own fault possibilities, but cannot win merely by passing its own certificate. Every compatible alternative remains in the command envelope. |
| Does a duplicate witness add support? | Only if its causal support changes distinguishability. The checked shared-support fifth witness fails. |
| Is the fifth secretly an oracle? | Its own-failure transcript is checked. The original four witnesses can collectively correct its false answer under the admitted cause range. |
| Is silence a false answer? | No. Missing reports do not contradict a candidate. Silence can block discrimination without proving it false. |
| Is the diagnosis a truth guarantee outside the candidate set? | No. Omitted hypotheses or joint causes can defeat it; the new counterexample retains actual-model deletion. |
| Are hidden identities exposed directly to the decision rule? | The filter reads only candidate predictions, fault envelopes and the transcript. The simulator uses actual causal structure only to generate physical responses. |
| Does this solve changing control? | The arrangement is stable through this modeled inspection/use interval. Unrecorded change and recorder/monitor compromise remain outside the guarantee. |
| Does this improve on ordinary diagnosis theory? | No superiority claim. Conventional consistency-based diagnosis and adversarial error models can reproduce the construction. |

This is author counterreview, not independent-agent acceptance or measured deployment evidence. It preserves the informative failure rather than requiring all constructed cases to favor the theory.

## 7. Primary-source comparison

Sources inspected on 8 October 2026; no originals were imported or altered.

**Reiter (1987), [A Theory of Diagnosis from First Principles](https://www.cs.ru.nl/~peterl/teaching/KeR/reiter.pdf).** The abstract, introduction and opening problem formulation were inspected. Reiter treats diagnoses as explanations involving abnormal components and allows competing diagnoses, with further measurements used to distinguish them. This supplies substantial prior art for jointly treating reports and possible faults. Our finite Boolean filter is narrower and has no claim to replace his general algorithm. It additionally connects the retained structural possibilities to this repository's existing command envelope; novelty of that connection is not established by this comparison.

**Cachin and Tackmann (2019), [Asymmetric Distributed Trust](https://drops.dagstuhl.de/storage/00lipics/lipics-vol153-opodis2019/LIPIcs.OPODIS.2019.7/LIPIcs.OPODIS.2019.7.pdf).** The abstract and sections 3–4 through the coverage-based classification of processes were inspected. Their fail-prone models make trust assumptions explicit and distinguish guarantees when actual faults are covered. Their Q3/B3 conditions serve Byzantine quorum consistency and availability; our two-set condition serves a single factual transcript. They do not prove the same task, and our condition is no improvement on theirs. Their guarantees also clarify why sincere behavior does not compensate for incorrect assumptions about joint compromise.

The conventional rival is a fixed, permitted collector using consistency-based diagnosis over admitted adversarial fault sets, followed by conservative validation and protected execution. It accounts for the formal results. The generative account contributes the wider interpretation of inquiry, support, responsibility and changing selection relations under the explicit normative commitments; this local construction does not prove its exclusive necessity.

## 8. Verification and completion

[Proof module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FallibleInspection.lean), [finite runner](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FallibleInspectionCases.lean), [reproducible checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_fallible_inspection.py), [proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/fallible-inspection-verification.json).

Lean 4.29.1 compiled fresh frozen copies of six inherited modules and both new modules. The proof module contains 24 new theorems and 41 audited explicit declarations. Twenty-two audits have no axioms; seven use `propext`, ten use `propext`/`Quot.sound`, and two additionally use `Classical.choice`. Inherited declarations and generated projections are not recounted. The retained build has no warnings. The scanner rejects placeholders, custom axioms, unsafe code, native proof shortcuts, implementation substitution and kernel bypass. The generic statements and their dependency audits are retained alongside the frozen source and compiler hash.

A separately expressed Python reference matches 2,592 transcript refinements and certificate comparisons, 7,560 costed executions, 6,804 executions enumerating all report assignments on the small diagnostic rosters, and 1,728 paired-fault transcript records: **18,684** in total. The arbitrary-assignment cases overwrite healthy positions with their lawful reports, so many assignments induce the same physical transcript. These are matched records, not 18,684 independent scenarios or empirical trials. The same author wrote both implementations; kernel proofs carry the general mathematical claims.

**Closed locally:** factual inspection need not depend on a designated infallible witness. Joint interpretation preserves actual covered possibilities, gives an exact complete-transcript distinction criterion and can narrow control uncertainty enough for paid correction. Missing evidence, duplicate supports, self-certifying rival models, exhaustion and uncovered joint compromise remain explicit.

**Next unresolved connection:** how actual reporting and recording relations continue to warrant the candidate and joint-cause bounds as organization changes. The strongest immediate need is correspondence for those bounds and for the recorder/monitor, not another generic filter or quorum theorem. Earlier source revision and reconfiguration supply completed conditional components; they must be connected to the same actual history before claiming this stronger result. Normative legitimacy and arbitrary adversarial coverage remain distinct questions.

[Owned index changes](FALLIBLE-INSPECTION-INDEX-EDITS.json) and [documentary checks](FALLIBLE-INSPECTION-CHECKS.json) bind this result to M25/F30 without certifying unrelated concurrent studies.

**中文结论。** 结构检查不必依赖某个绝对可信者：把事实候选与见证失陷范围共同解释，保留所有相容说明，再以其共同范围认证实际纠正。对相反答案，完整记录可辨认当且仅当任意两候选失陷集合不能覆盖全部见证；缺报必须按实际收到的共同幸存见证判断。第五见证只有真实支承不同才可能解除本例歧义，而且它本身也允许失实。新增24项定理／41项审计与18,684项记录匹配通过；真实范围覆盖、非失陷报告的忠实、记录与执行支承及权限正当性仍明示。没有把技术辨认等同伦理根据，也没有重开已完成的一般修订机制。
