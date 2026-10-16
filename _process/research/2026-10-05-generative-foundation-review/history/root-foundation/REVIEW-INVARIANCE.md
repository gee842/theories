# Adversarial review: invariant root and joint information–execution theorem

Internal specialist-style review, 5 October 2026. Reviewed `ROOT-FOUNDATION.md` and `INFORMATION-AND-RENEWAL.md`, with the theorem premises in `TURNOVER-AND-CLOSURE.md` consulted for consistency. This is an AI-assisted mathematical and claim-scope audit. It is not independent human peer review, empirical validation, or a certification of novelty.

## Verdict

**No blocking mathematical error identified.** The exact joint feasibility result, its control-independent deadline, and the stated numerical witness are correct under the declared continuous-time operating model. The root synthesis preserves the necessary distinctions between conditional universality, faithful-description invariance, a physical hypothesis of widespread renewal, propositional truth, and normative justification.

The documents can be integrated in their present form. Two optional wording clarifications below would improve resistance to misreading but do not change a theorem or its proof.

## 1. Exact joint feasibility theorem: passed

With positive rates and the supplied laws

\[
\dot c=\alpha u(1-c)-\delta c,\qquad
\dot b=s(1-u)-q,
\]

the claimed effort bounds are obtained directly from the two boundary derivatives. When their interval is nonempty, constant effort in that interval keeps the reliability floor forward invariant and prevents the execution reserve from decreasing. This establishes sufficiency from every specified safe initial state, including zero reserve under the explicitly stipulated continuous-flow service semantics.

For necessity, independently differentiating the certificate gives

\[
\frac{d}{dt}\left[\frac bs+
\frac1\alpha\log\frac{1-c_*}{1-c}\right]
=1-\frac qs-\frac{\delta c}{\alpha(1-c)}.
\]

The effort variable cancels exactly. The last ratio is increasing in \(c\), so on \(c\ge c_*\) the derivative is bounded above by \(u_{\rm execution}-u_{\rm information}\). This argument works almost everywhere for measurable bounded controls and can be integrated along every absolutely continuous solution. Randomization or adaptation does not evade it because each realized allocation satisfies the same bound. No optimization over an assumed family of stationary controllers is being mistaken for optimization over all controllers.

The certificate is nonnegative on the safe region and finite at the stated initial states. The finite deadline therefore follows. A trajectory can remain safe at the exact deadline and fail only upon continuing beyond it; the worked witness states this correctly. Excluding an initially perfect channel avoids a singular certificate, and applying the proof after any positive time closes that apparent loophole because positive decay makes the channel imperfect immediately.

The attained minimum error tolerance follows algebraically from solving the effort inequality. It is a model-specific feasibility threshold. The document correctly does not infer a universal physical energy-per-truth constant from it.

The generalized repair law supplies only an obstruction unless a suitable invariant region and feasible policy are separately established. Section 5 explicitly makes that distinction.

## 2. Information bound and selection example: passed

The minimum binary average error is \((1-\operatorname{TV})/2\); the derivation has the correct factor of two. The erasure-channel specialization has total variation \(c\), yielding error \((1-c)/2\). A fair answer on erasure gives equal error in the two circumstances. The lower bound on average error therefore also establishes optimal maximum error for this symmetric channel. The note does not incorrectly generalize that equality to arbitrary asymmetric channels.

Past observations cannot help in this example because the current circumstance is declared fresh and independent of the earlier record. The text also avoids the false inference that computational effort can never help: it distinguishes implementing a decoder from supplying distinctions absent from its actual input.

For the selected-maintenance example, the two boundary equilibria and their eigenvalues are correct. The interior equilibrium has the stated Jacobian and determinant \(-1/6\), establishing a saddle. The two rectangular invariant regions follow from the direction of the vector field on their threshold boundaries. Within their interiors the sign of the selection derivative supplies the claimed monotonic movement toward the corresponding boundary practice. The text restricts its basin claims and explicitly notes that growing \(b\) prevents the subsystem equilibria from being full-state fixed points.

An independent exact-fraction check reproduced the feasible interval \([2/3,3/4]\), minimum error \(1/11\), all three table rows, the strict-tolerance reliability \(24/29\), required effort \(4/5\), sharp five-unit horizon, and saddle determinant. These checks corroborate the displayed arithmetic; they are constructed mathematical verification, not observations of a real institution or organism.

## 3. Root synthesis and causal scope: passed

R1 preserves policy realizability and required consequences in both directions. It does not grant hidden states or the evaluator's extra observations to the controller. Its full finite statement in the invariance companion supplies the appropriate kernel-and-interface construction. The root correctly distinguishes the attainable outcome set from the complete mapping of labeled interventions to consequences; its action-swap witness prevents an overclaim of causal identity from all-task outcome feasibility alone.

R2 is a valid topological lifetime induction. The maximum predecessor deadline is conservative for multiple jointly required parents, which is appropriate for a necessity result. All initial instances were created no later than zero, all later instances require a live parent, and later external organizational entry is excluded. Those premises prevent an untracked durable record, spontaneous establishment, or later import from being silently treated as an internal renewal event. The type-cycle conclusion concerns repeated types along forward event ancestry, not backward causation.

R3 correctly needs productive vulnerability. Nonnegative balances imply that unbounded loss requires unbounded provision. Finite branching then supplies an unbounded internal predecessor when external provision is finite. Productive vulnerability is what allows the argument to continue through that predecessor. Without that premise, an undegrading supplier is an explicit counterexample, and the documents acknowledge it. The resulting graph concerns cumulative recurrent contribution, not simultaneous operation, positive average rate, bounded renewal gaps, or a stable equilibrium.

Combining these results with the information theorem is logically conditional: the actual information and execution supports must satisfy the graph or lifetime premises. The synthesis states those shared application assumptions rather than claiming that the scalar reliability equation by itself identifies a finite closed support network.

## 4. Truth, normativity, and scientific positioning: passed with continuing limitations

The root distinguishes factual correspondence, evidence, executable response, and normative legitimacy. It does not identify a self-maintaining error regime with truth merely because the regime is stable. Nor does it infer that reproducing any institution is morally desirable. Acceptance requirements and legitimate amendments remain separately supplied and assessed.

Description invariance is correctly distinguished from a quantity conserved through physical time. Extending a horizon can expose modeled exhaustion; rescaling time cannot create a causal feedback path. The final universality statement is appropriately restricted to the stated mathematical class.

The documents credit statistical decision theory, biological constraint closure, graph-cycle methods, and especially Kolchinsky–Wolpert and Sowinski et al. for information–viability connections. They describe the present contribution as an integration and explicit derivation within this project, with originality against the full literature unestablished. This is the defensible status. A new universal law, universally valid physical loop, or foundational account of every meaning of reason would require further argument and evidence.

## 5. Optional clarifications

1. **Conditional accuracy versus aggregate accuracy.** To make the strength of the requirement maximally explicit, section 2 or 3 of the information note could say: “The error guarantee applies to the channel available at every service time, conditional on the pre-observation history and current reliability; it is not merely an average across times.” The present equations already impose the stronger pointwise reliability floor. Aggregate accuracy could permit trading temporary inaccuracy against later high accuracy and would define a different feasibility problem.
2. **Batched service would change the boundary semantics.** An optional application sentence could say: “A discrete task requiring a minimum batch of reserve before execution needs that reserve floor and jump expenditure in place of the continuous expenditure law.” The current model explicitly defines executable service through nonnegative continuous reserve, so this is an implementation boundary rather than an error.

No author changes are required by this review to sustain the stated propositions. Empirical tests still need independently measured observation laws, decay and renewal rates, operative support graphs, resource constraints, and interventions. The review certifies none of those inputs.
