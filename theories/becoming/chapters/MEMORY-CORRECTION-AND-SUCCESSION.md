# What must survive a correction

6 October 2026. AI-authored research on **warranted correction → retained evidence → changed successor action**, supporting the existing [alignment and governance goal](ALIGNMENT-COMPLETION.md). The initial source and mathematical audit below made no model calls. A subsequent fixed pilot now adds actual outputs from 24 fresh AI contexts: both instruction variants selectively reused inherited corrections correctly, with no observed benefit from the added boundary reminder. These responses do not establish the entire correction-to-execution chain.

**To establish warranted correction through succession, we need to trace how the correction changes the successor's justified action.** The [institutional study](EVIDENCE-AND-INSTITUTIONAL-CORRECTION.md) distinguished a corrected case from revision of its shared rationale. Across an AI handoff, we must additionally distinguish a stored correction, its delivery to a successor, its justified interpretation and its actual use. Receiving a trusted message can support action; it does not alone demonstrate the ability to detect when that message has become inapplicable.

## The existing positive result and the missing contrast

The repository already has an [actual founder/successor experiment](../../../sources/20-codex-theory-sessions-2026-10-05/sin/outputs/experiment-report.md), independently checked in the [evidence audit](../../../_process/research/2026-10-05-revisable-concern/settlement/evidence/report.md). Timely feedback enabled a corrective packet whose availability improved successor performance in a supplied rule family. That is evidence for a bounded transmission mechanism. It does not establish selective revision of an inherited false or stale packet, newly acquired concern for another being, or justification of the task's objective.

The new discriminating question is joint: **does a successor retain a grounded correction where it applies, and revise or suspend inherited content when accessible evidence defeats it?** A conclusion-only message with matched substantive information helps distinguish evidence-sensitive assessment from ordinary message transmission. Where that comparison cannot be constructed fairly, its limitation must remain explicit; a whole factorial design is not required for every narrower claim.

The successor must have evidence capable of distinguishing the tested conditions. Secretly changing the correct answer while withholding all distinguishing information would test an impossible demand. Nor should an unavailable record be labeled a false proposition. The [external-information argument](ALIGNMENT-AND-GOVERNANCE.md) applies here without requiring constant live contact: retained evidence can be informative, and its applicability must be supported at the time of use.

## What the new benchmark sources do and do not establish

The [source audit][evidence] records versioned primary materials and the inspected public releases. It distinguishes papers' descriptions, available schemas, reported aggregates and actual per-run records. A schema for evidence is not evidence that the corresponding event occurred.

**CoMemBench.** Its isolation score conditions on successful clean target nodes; its handoff score conditions on verified predecessors. Neither is whole-workflow success. The inspected pinned release supplies task-side artifacts, not model-execution traces. [Paper, section 4 and Appendix F](https://arxiv.org/html/2609.32192v2); [public release](https://huggingface.co/datasets/anonymous-submission-333/anonymous-submission).

Our [metric audit][metrics] gives the exact consequence. On one fixed cohort of valid matched pairs, let `c` be the fraction with clean target success and `r` the isolation score among those successes. When `c > 0`, the fraction succeeding at that target in both runs is `c × r`; with no clean successes, `r` is undefined. In an authored arithmetic example, one system has conditional ratio `r = 1` by succeeding cleanly on only two of ten pairs, while another has `r = 0.8` and succeeds jointly on eight. These are mathematical ratios, not published benchmark scores. This does not make the conditional metric wrong. It makes the population and question indispensable. A terminal workflow rate cannot replace `c`, and common-clean comparisons must remain restricted comparisons. Missing execution evidence is separate from an observed failure.

**MemSecBench.** Execute and Forget independently start from the same post-Write snapshot. Forget assesses repaired and preserved memory semantics; the paper explicitly distinguishes this from subsequent retrieval or task use. [Paper, lifecycle protocol and Appendix E.4](https://arxiv.org/html/2607.27080v1).

Consequently, these observations can establish what happened when a poisoned state was executed and what state a repair produced, without establishing what execution from the repaired state would do. In notation, observing `E(M_W)` and `F(M_W) = M_F` does not observe `E(M_F)`. Two continuations can agree on every measured checkpoint and differ at that unmeasured operation. A follow-on action trace or a justified bridge law is needed for the stronger claim. This is our nonidentification argument, not a claim that the benchmark promised the missing endpoint or that its repair measurements lack value.

## A published impossibility argument needs a narrower observation boundary

The *Misattribution Gap* paper's Appendix A attempts to establish indistinguishability between memory poisoning and altered model behavior. Its construction changes retrieved text while its stated logs include retrieved contexts, and uses matching violation rates to assert identical observable laws. The [independent mathematical review][review] finds that this proof does not establish its advertised scope. [Primary paper, Appendix A](https://arxiv.org/html/2605.22842v1).

Three explicit counterexamples explain the limit:

1. Equal embedding norms do not preserve retrieval rank. Against query `(1, 0)`, replacing `(1, 0)` with `(0, 1)` preserves norm but moves its score below a competing unit vector `(4/5, 3/5)`.
2. Equal classifier verdicts do not make full logs equal. A log that retains the retrieved text can distinguish two different texts even when both receive the same classifier label. Distinguishing those records is not the same as identifying which document is malicious; that needs further grounds.
3. Equal error marginals do not imply equal history laws. A process producing `00` or `11` with equal probability and one producing `01` or `10` with equal probability each have error probability `1/2` at both times. Whether the two observations agree distinguishes the processes perfectly.

The valid weaker statement is important: if two mechanisms induce the same probability law for a **specified available observation**, no test restricted to that observation can distinguish them better than the information in its prior. To extend that result to active inspection, retraining or interventions, equivalence must hold for the permitted experiments too. It cannot be inferred from matching one behavior rate or a classifier's judgment. This is a standard identification constraint, not a new universal impossibility theorem.

The critique leaves memory-mediated failures possible and does not reproduce or refute the paper's experimental results. It also does not provide a ready poison detector. It prevents us from borrowing an unsupported impossibility claim as a foundation for alignment or governance.

## Selective reuse in actual fresh contexts

The [completed pilot](../../../experiments/integrated-correction/selective-handoff/README.md) reuses four actual corrective packets from the earlier founder experiment. Their text is unchanged. Each new context receives one packet, a constructed later episode and a current audit. That audit either confirms the inherited correction, defeats it, or comes from another setting and leaves the target unresolved. Both instruction variants receive exactly the same substantive information and the same finite candidate family; one adds a reminder to check scope and revise selectively.

| Current evidence | Ordinary instruction | Added boundary reminder |
|---|---:|---:|
| Confirms the correction | 4/4 complete contexts | 4/4 |
| Defeats the correction | 4/4 | 4/4 |
| Concerns another setting | 4/4 | 4/4 |

All 24 fresh contexts returned all eight warranted outputs: 160 definite routes and 32 required expressions of uncertainty. Each donor fixture passed all three situations in both arms. In the unrelated-setting condition, uncertainty was selective: four answers were unresolved and four remained determined under either candidate rule. The response patterns are incompatible with always copying the packet, always using the base rule, or always abstaining.

The interpretation is deliberately bounded. Ordinary finite-candidate elimination also solves every case, and the added reminder produced no gain in any of the 12 paired situations. This is a ceiling result in a small selected task set, not statistical equivalence or evidence of a distinctive new inference mechanism. Because the packet is present in every arm, its separate causal contribution is not estimated.

The [frozen protocol](../../../experiments/integrated-correction/selective-handoff/PROTOCOL.md) supplied the complete two-rule family, exact audits, episode boundaries and the norm of answering only what all compatible rules support. Fresh contexts were requested with no conversation history; this does not certify independent learned models or filesystem isolation. The saved response texts are copies from actual completions. Local runtime metadata corroborates the 24 calls, but its protected message bodies do not independently verify plaintext prompts or outputs. Prior service and successor cases can overlap the new tests; novelty beyond the current calibration and old founder baseline is not claimed.

This result closes the absence of direct fresh-context evidence for **selective assessment of these inherited corrections**. It does not observe a successor choosing and performing new evidence gathering, repairing its own persistent memory and later executing an external task from that repaired state. Those are distinct parts of the existing connection, not claims that can be inferred from a perfect answer score. No new donor learning, value acquisition, recipient benefit or ethical justification was measured. The [result review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/SELECTIVE-HANDOFF-RESULTS-REVIEW.md) records the final scope and provenance.

## Diagnosis and correction concern the interacting system

Our further causal example shows why finding an external cause does not by itself exonerate every internal mechanism. Let an undesirable event occur exactly when an invalid memory directive `M = 1` meets a susceptible decision rule `U = 1`, so `H = M × U`. Removing the directive prevents the event; changing the decision rule also prevents it. An intervention on memory identifies a causal contribution in this construction. It does not prove that memory is the unique relevant cause or that no improvement to interpretation is possible.

Ren's clarification about external integration makes this broader observation boundary natural. The supported object of assessment is the process that actually produces action: inherited evidence, retrieval, interpretation, authority, tools and consequences, with their interactions. The weights alone or the archive alone may omit relevant causes. The appropriate boundary depends on the claim and available interventions; merely expanding it cannot guarantee a correct diagnosis.

For a concrete successor claim, therefore, preserve the actual donor acquisition and handoff, distinguish controller replacement from another call in one context, and trace the successor's use on new relevant cases. Record both valid retention and warranted revision, including abstention, loss of access and unimplemented decisions. A corrected archive, a positive conditional score and a plausible explanation are separate evidence, not interchangeable certificates of that whole history.

The task's benefit, affected person's standing and legitimate authority remain independently warranted premises. A task-defined answer or security label cannot supply those by itself. The [evaluative application](EVALUATIVE-APPLICATION.md) and [ethical foundation](ETHICAL-FOUNDATION.md) retain their positive arguments and scoped requirements.

The source audit closes a specific interpretive question: the inspected benchmark endpoints and the reviewed impossibility proof do **not** establish corrected action through succession. It supplies counterexamples and a discriminating test for that existing obligation. The actual constructive succession work remains separate; no new apparatus or completion condition has been added. The [five foundation conditions](GENERATIVE-GROUNDING.md#completion-of-the-unified-foundation) and the full alignment goal remain unchanged.

[evidence]: ../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MEMORY-CORRECTION-EVIDENCE.md
[metrics]: ../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MEMORY-CORRECTION-METRICS.md
[review]: ../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MEMORY-CORRECTION-REVIEW.md
