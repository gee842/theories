# Memory correction: observation and intervention scope

6 October 2026. Independent AI-authored mathematical/source review supporting **retained correction → diagnosis and warranted correction after handover**. This reviews a specific inference, not the existence of memory poisoning or the integrity of reported experiments. No model calls, raw-data reanalysis or scientific computation were performed.

## Source claim and reading scope

Ahad et al.'s *The Misattribution Gap*, v1, defines logs containing retrieved contexts, agent outputs, composed outputs and classifier verdicts. Appendix A replaces a poisoned entry with innocuous equal-norm filler, matches a violation rate, and concludes identical log distributions and impossibility of model-layer auditing. I inspected Theorem 1, sections 3.1–3.3 and Appendix A. The proof as written does not establish that conclusion. [Primary text, Appendix A](https://arxiv.org/html/2605.22842v1#A1).

The following examples and proofs are this review's constructions. They are not reconstructions of the paper's experimental systems or new empirical observations.

## 1. Equal norm does not preserve retrieval

For cosine top-one retrieval, take query \(q=(1,0)\), candidate \(m=(1,0)\), replacement \(f=(0,1)\), and another document \(b=(1/\sqrt2,1/\sqrt2)\). All have unit norm. Their similarities to the query are respectively \(1,0,1/\sqrt2\). Replacing \(m\) with \(f\) changes the retrieved document from \(m\) to \(b\). The same example works for dot-product ranking. No ties or estimation are involved.

A rank-preservation premise would need the relevant similarity ordering, not just norms. Even identical embedding vectors would not establish identical observable document text if the representation is noninjective. Conversely, this counterexample does not assert what any particular text embedder assigns to particular strings. It refutes a purported implication from equal norm alone.

## 2. A verdict is a projection of a record

Let two deterministic logs have identical outputs and safe verdicts but retrieved-text fields \(R=m\) and \(R=f\), where the strings differ. The event \(E=\{R=m\}\) has probabilities one and zero. Their full-log laws therefore differ. A classifier that maps both strings to “safe” makes its own verdict uninformative; it does not erase a differing field from the log.

This perfectly distinguishes the two **specified** worlds. It is not a general poison detector: an observer may not know which text is malicious, what its authority is, or whether it caused the output. Observable difference, known provenance, causal attribution and normative validity are distinct. If “clean” instead permits the same text with a different unobserved history or authorization, identical textual logs may be possible—but that is a different construction requiring its own assumptions.

## 3. Matching an outcome rate does not match the joint law

Consider two sessions whose violation indicators are \((V_1,V_2)\). Process P chooses \((0,0)\) or \((1,1)\), each with probability one half. Process Q chooses \((0,1)\) or \((1,0)\), each with probability one half. Each process has violation probability one half in each session and expected total one. Nevertheless,

\[
P(V_1=V_2)=1,\qquad Q(V_1=V_2)=0.
\]

Thus the two-session records are perfectly distinguishable even if every other observed field is constant. Marginal agreement cannot establish agreement of temporal dependence, output contents or cross-agent dependence.

There is also a quantifier distinction. If, for every realized trace \(\ell\), one can choose a model \(Q_\ell\) that reproduces it, that does not exhibit one fixed model Q reproducing P's whole probability law. Even identical supports leave room for very different likelihoods. A construction chosen after seeing the trace can establish an explanation compatible with that trace without establishing statistical indistinguishability.

## 4. The valid weaker result

Fix an observation map g and two hypotheses with the **same entire observed-record law** \(g_*P=g_*Q\). Then every possibly randomized diagnostic using only that record has the same output distribution under both hypotheses. Proof: the diagnostic applies the same conditional output kernel to the same input measure. With equal prior probabilities, its binary classification accuracy is one half. This is a standard conditional identification result, already used at a different empirical scope in the [recipient-cue account](../../../../theories/becoming/history/RECIPIENT-CUE-GROUNDING.md); it is not a new theorem claimed for this programme.

A sufficient sequential premise is equality of every next-observation kernel conditional on the **full observed past**, with the same initial law. Multiplying those kernels yields equal finite joint laws. A sufficiently unrestricted simulator can be defined using those kernels. Its existence does not show that a particular post-training procedure, fixed LLM architecture or memory replacement realizes it.

For an **active** auditor, include its permitted actions in the contract. Equality must hold for next-observation kernels conditional on each reachable observation/action history under every allowed audit policy. Then induction also covers adaptive experiments. Equality of passive session logs alone says nothing conclusive about additional activation measurements, changed queries, memory interventions or retraining outcomes. An indistinguishable pair rules out uniform identification over a class containing that pair; it does not establish that every pair in the class is indistinguishable.

## 5. A correction test that can change the account

Freeze the observation map, target failure, available interventions and attribution claim before interpreting a succession experiment. Preserve the actual retained payload and provenance/access history. Compare selective memory replacement while holding the controller fixed with selective controller replacement while holding relevant memory fixed, where the implementation supports those interventions. Include fresh and stale evidence, legitimate similarly formatted records and affected cases not used to construct the correction. A measured intervention difference can identify contribution under its stated controls; it need not identify a unique cause.

Deleting a document can change context length, ranking and which other documents appear. Holding rank and length fixed still need not hold semantics fixed. Accordingly, distinguish the total effect of removing an entry from the direct effect of a content component under a controlled replacement. Joint memory–controller dependence is also possible: a failure can require both rather than belonging exclusively to one layer. A stochastic resampling difference or loss of necessary benign context is not automatically evidence of malicious causal origin.

For a claimed corrective successor, measure whether the changed action persists on relevant new cases and whether justified distinctions survive. A smaller violation count caused by refusing every task is different from selective correction. A replacement model operating through the same compromised shared store is a legitimate test of that shared-support vulnerability, but not evidence that an acquired correction was transmitted to it. Factual diagnosis does not by itself supply patient welfare, authority or normative warrant.

**Scoped verdict:** do not use the audited proof to claim universal immunity to model-layer diagnosis or equality of full logs. Retain the weaker observation-relative identification limit and evaluate memory risk through its actual evidence. The substantive contribution is a corrected diagnostic obligation for empirical succession tests, not another mandatory monitor, a new formal construction or a rejection of the paper's reported attacks. The [cross-domain identification](CROSS-DOMAIN-IDENTIFICATION.md), [composition audit](EVALUATIVE-COMPOSITION-AUDIT.md) and [alignment completion contract](../../../../theories/becoming/chapters/ALIGNMENT-COMPLETION.md) retain the broader open goal.

## Final canonical and metric review — 6 October 2026

Accepted the [canonical account](../../../../theories/becoming/history/MEMORY-CORRECTION-AND-SUCCESSION.md), SHA-256 `0346e1df420a09e6055338b5b16e74836acdc8af93fb5fb4cabfd81ff1e47142`, and [metric audit](MEMORY-CORRECTION-METRICS.md), SHA-256 `a4675370b749aceda3d7c8dd2e8f862ae4d92f8d8bca0ec888310466f74693a6`, at their stated source and inference scopes. This acceptance follows independent primary-text inspection and manual algebraic review, not model execution or numerical replication.

The canonical rational competitor `(4/5, 3/5)` has unit norm and score `4/5` against `(1, 0)`, so its rank counterexample is exact. Its two-session laws share the specified marginals and differ on the equality event. In the constructed `H = M × U` system at `M = U = 1`, setting either input to zero prevents the event. Both are causal contributors under those stipulated interventions; neither intervention establishes exclusive responsibility. This does not estimate contributions in a learned system.

The metric identity uses one fixed valid matched cohort and a positive clean-success denominator. The corrected text makes an empty conditional denominator undefined, separates terminal success from target coverage, and distinguishes the authored ratios from a release's displayed scores. The common-clean subset remains a restricted descriptive comparison. Unknown polluted outcomes after observed clean failure are not reclassified as observed failures. The separate Execute/Forget branches allow different later-action continuations; a later trace **or a justified bridge law** can supply the missing connection.

I also inspected the preserved full CoMemBench tree and pinned README in [source 34](../../../../sources/34-memory-correction-2026-10-06/README.md). The narrow claim about available artifacts is supported; the source audit does not turn inaccessible or unlocated outputs into evidence of universal absence. Whole-package hash verification is a separate preservation check.

The final opening concerns establishing warranted correction through succession. It does not require every successful policy to preserve explicit reason text, or impose a universal comparison apparatus. Actual handoff, supported applicability and consequential use remain distinct observations. The conclusion-only alternative, shared-support confounds, active-intervention qualification and separate ethical grounds prevent a favorable task result from being promoted into complete alignment. No substantive blocker remains; the constructive succession work and the larger foundation remain open at their own scopes.
