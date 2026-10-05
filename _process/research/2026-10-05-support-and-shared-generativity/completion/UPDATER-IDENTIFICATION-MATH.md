# What identifies an operative updater change?

6 October 2026. AI-authored mathematical and identification proposal for the retrospective motor-learning study. This note was scoped before inspecting the workbook's response values or the producer's analysis. It distinguishes empirical estimands from conditional equality proofs; it adds no Lean theorem count. The governing connection is **consequences and their costs → changed learning behavior → warranted evidence about an operative learning mechanism**.

The [existing diagnostic contract](../../2026-10-05-generative-foundation-review/root-foundation/ROUTE-DIAGNOSTICS-MATH.md) identifies three recipient-update classes within four declared route recipes, using actual input, completed writing, bounded memory and stable binding. The [paid revision construction](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/LEARNING-ROUTE-REVISION.md) then intervenes on a physically represented route while preserving the actual record. This note asks which analogous causal claims can be supported by an external experiment. It does not assume that a behavioral learning-rate estimate already measures that route variable.

## 1. The empirical source and three distinct estimands

Sedaghat-Nejad and Shadmehr's [PNAS article](https://www.pnas.org/doi/10.1073/pnas.2101717118) manipulates the opportunity cost of correcting a saccade: correction consumes viewing time in a motion-discrimination task. Its within-participant switch at trial 951 exchanges the coherence association for both target sides; their costs change in opposite directions. A control removes competition for viewing time. Error-clamp and recovery conditions constrain retention explanations. The fitted state-space description separates retention from error sensitivity. These are manipulations and model-based measurements of behavior; the experiment does not replace an identified physical updater component. The companion evidence audit determines what the [OSF H24J8](https://osf.io/h24j8/) binned source curves can actually reproduce.

Let \(C\) denote the manipulated task condition, rather than an independently measured metabolic bill. Let \(Y\) denote a declared subsequent response and \(H\) the relevant pre-intervention history. Distinguish:

1. **Effect of the task manipulation.** A contrast such as
   \[
   \mathbb E[Y^{do(C=c_1)}-Y^{do(C=c_0)}\mid H]
   \]
   concerns the imposed condition's total effect. The experimental assignment, counterbalancing, carryover and measurement assumptions determine whether a particular paired contrast identifies it. A retrospective comparison of binned endpoints is a paired behavioral contrast unless those design assumptions justify the stronger causal interpretation. Merely observing the same participant twice does not provide independent state resets.
2. **Effective error sensitivity within a specified model.** For example,
   \[
   x_{n+1}=a x_n+b(C_n)e_n+\epsilon_n,
   \quad y_n=x_n+\eta_n,\quad e_n=d_n-y_n.
   \tag{1}
   \]
   Here \(d_n\) is the imposed displacement, avoiding use of \(r\) for both perturbation and mechanism. A fitted difference in \(b\) is conditional on the observation model, latent-memory dimension, retention law, noise assumptions, error exposure and trial ordering. A paired asymptote difference alone does not estimate \(b\): even in a noiseless constant-displacement model the fixed point depends on both \(a\) and \(b\). A nonsignificant retention contrast is not an equality proof.
3. **Causal change of an operative retained updater.** This means that a physically specified, retained component or organization \(R\), reached by the same continuing subject/carrier, changes the update kernel under matched memory, delivered evidence and writing opportunities. An intervention identifying that causal role must isolate it from concurrent changes in input encoding, write availability and action readout. Architectural replacement is stronger still: it requires evidence about altered organization/material and its persistence, not merely a fitted gain.

The retrospective analysis can test a declared contrast in the public curves. It cannot silently promote that contrast to estimand 3, re-fit unobserved trial histories from bins, or count a model parameter as measured hardware. The selected source is useful evidence about cost-sensitive learning even if that stronger promotion fails.

## 2. A fixed law can represent a revisable operative updater

Write a mechanistic model as

\[
q_{n+1}=U(r_n,q_n,u_n,W_n),\qquad
r_{n+1}=V(r_n,q_n,u_n,C_n),
\tag{2}
\]

where \(q\) is acquired memory, \(r\) retained updater state, \(u\) evidence delivered at a specified boundary, and \(W\) a writable opportunity. The combined state \(s=(q,r)\) obeys the single fixed law

\[
s_{n+1}=F(s_n,u_n,W_n,C_n)
 :=\big(U(r,q,u,W),V(r,q,u,C)\big).
\tag{3}
\]

**Equality claim.** With the same initial \((q,r)\), inputs and coupled noise, (2) and (3) have identical states and outputs at every finite step. Induction proves this: their successor expressions are the same. Thus behavioral evidence cannot distinguish a changing operative updater from its exact fixed augmented-state realization. The two descriptions are not competing empirical mechanisms when their physical interfaces coincide.

This is an application of the [causal-root representation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-CORE-LEAN.md), not a new impossibility discovery. Nor does it refute operative revision. The repository's successfully changed route also evolves under one fixed law. The meaningful question is which retained organization has what causal role, how it was changed and maintained, and which observation or intervention distinguishes alternatives. “The fundamental transition rule itself changed” is not an additional identification criterion.

A finite selector choosing between two permanently available gains can similarly realize a two-gain update description. A demonstrated change in which gain is operative does not by itself demonstrate construction of a previously absent program, a changed molecular rule, or novel architecture.

## 3. Exact input-encoding counterexample

Assume a nonzero constant \(\beta\) and any function \(b(c)\). Compare two structural descriptions:

\[
\begin{array}{ll}
\mathsf{Gain}:& u_n=e_n,\quad x_{n+1}=a x_n+b(C_n)u_n+\epsilon_n;\\[2mm]
\mathsf{Input}:& u_n=\dfrac{b(C_n)}{\beta}e_n,\quad
x_{n+1}=a x_n+\beta u_n+\epsilon_n.
\end{array}
\tag{4}
\]

The second updater's coefficients remain fixed. The condition changes the evidence reaching it. These models have exactly equal \(x\) trajectories and observed \(y\) under the same initial memory, externally imposed displacements and coupled process/measurement noise, including closed-loop \(e_n=d_n-y_n\). They also agree under externally clamped error words. Substitution gives the same successor at each step, so induction gives pathwise equality. If \(0\le b(c)\le\beta\), the input multiplier can be interpreted as attenuation rather than arbitrary amplification.

This is a constructive identification failure for the interface observing \((C,d,e,y)\) but not the delivered internal \(u\). Equal external geometric error does not establish equal encoded teaching input. Independent input calibration or an intervention delivering matched signals downstream of that encoding would distinguish these particular descriptions. That new intervention tests the circuit at its named entry; placing it downstream of the component under investigation would bypass that component and change the question.

The countermodel is not a claim that sensory attenuation explains the selected experiment. Its function is logical: a condition-dependent input path remains an alternative unless independently excluded. A control equalizing task difficulty or removing time competition can rule out specific alternatives without establishing that every remaining cost effect acts inside a retained update mechanism. Equation (4) can depend on the time-competition condition itself, so removing that competition need not distinguish its two descriptions.

## 4. Writing opportunities and latent memory are separate alternatives

### Writing gate

Let an otherwise fixed updater have a binary completion gate:

\[
X_{n+1}=aX_n+\beta W_n e_n,\quad
\Pr(W_n=1\mid C_n=c,X_n,e_n)=p(c).
\tag{5}
\]

Then

\[
\mathbb E[X_{n+1}\mid X_n,e_n,C_n=c]
 =aX_n+\beta p(c)e_n.
\tag{6}
\]

Changing available write time or the probability of successful updating changes the effective conditional-mean gain while the admitted update rule stays fixed. A continuously available fraction \(W=b(c)/\beta\) gives exact pathwise equality with (1) in the noiseless case; a binary gate gives the conditional-mean equality in (6), **not generally equality of the full distribution**. Its conditional variance includes \(\beta^2p(c)(1-p(c))e_n^2\). Raw trial distributions or an independently observed write/processing-opportunity variable can therefore distinguish versions that binned means cannot.

Write completion is not a benign covariate if the manipulated mechanism can affect it. Restricting analysis to observed completed writes can select different histories across arms. A matched assay must either provision and intervene on a common admissible write opportunity independently, or preserve noncompletion as an outcome and estimate an intention-to-assay effect. The formal route diagnostic's completed-write premise cannot be inferred from unchanged behavior.

### Hidden memory composition

Even matching the current observable response need not match acquired memory. Let fixed fast and slow states obey \(x_f'=a_f x_f+b_f e\), \(x_s'=a_s x_s+b_s e\), with observable \(y=x_f+x_s\). The states \((0,0)\) and \((1,-1)\) both have \(y=0\), yet under \(e=0\) their next outputs differ by \(a_f-a_s\). No updater coefficient has changed. Recovery/retention experiments help constrain such hidden-memory alternatives; they do not automatically prove equality of all relevant latent states or architectural revision.

These examples explain why cost, latent sensitivity, delivered input, available writing and retained mechanism must be kept as separate variables. They are alternatives to overidentification, not simultaneous findings about the source participants.

## 5. An intervention-preserving criterion

Specify an assay before its outcome. Its interface includes:

- a memory-setting/measurement procedure \(Q\), with its costs and demonstrated adequacy;
- direct delivered evidence \(u\) at a named physical boundary and recipient/context binding;
- a writable opportunity \(W=1\), common funding/lifetime support, and explicit noncompletion outcomes;
- interventions \(I_0,I_1\) on independently specified retained updater states or components;
- a post-write memory read and a later common action/readout probe.

Let \(K_i(\cdot\mid q,u,W=1,z)\) be the interventional distribution of the acquired-memory read after \(I_i\), where \(z\) retains resource, context and other causal conditions required by the assay. Require:

1. **Relevance and retention:** the interventions actually establish distinguishable retained component states, verified at the assay's time scale. An external cost instruction is not automatically such an intervention.
2. **Matching and common support:** the two arms have the same relevant \(q,u,W,z\), or an identified randomized design estimates a declared standardized contrast over their common support. Matched observed endpoints alone are insufficient when memory is latent.
3. **Exclusion and fidelity:** apart from the specified updater path, \(I_i\) does not directly change the acquired record, input encoder, input exposure, write opportunity, target context, resources or measurement/readout. Verify what can be verified; state the remainder as assumptions. A treatment that changes several of these has a broader total-effect estimand.
4. **Operative consequence:** for at least one admissible assay,
   \[
   K_0(\cdot\mid q,u,1,z)\ne K_1(\cdot\mid q,u,1,z).
   \tag{7}
   \]
   To call the changed memory operational in later action, also test its subsequent read/use. A common paid memory clamp, exchange or rescue that removes/restores the action contrast can help identify mediation; an unused changed register is not enough.

Under the declared causal law and these premises, (7) identifies a causal role of the intervened retained organization in updating at that interface. It identifies a task-relative operative class, not a unique anatomical explanation. Within the existing recipient assay, CLOSED and FROZEN remain equivalent unless input-presence measurements or different interventions enlarge the interface. Failure to find a contrast under finitely many probes is not universal equivalence.

A practical stronger assay would measure the putative component before and after learning, test retained differences after common cost conditions are restored, and perturb/rescue that component while preserving the delivered-error and write interfaces. Persistence after restoring common conditions rules out a purely instantaneous cost lookup, but can still reflect retained contextual memory. Physical perturbation plus exclusion is what narrows that ambiguity. If the component is inaccessible, report a history-dependent change in an effective update kernel under the specified assays, not a demonstrated material replacement.

## 6. Invariance is relative to preserved interventions

Let two state descriptions be related by a map \(\phi\) that preserves the assay's preparation, interventions \(I_i\), delivered-input/write labels and observation/readout. In a stochastic formulation require transition-kernel pushforward commutation for every admitted assay event, not merely equality of possible paths. Induction then gives equality of the pushed-forward finite assay laws. If the post-write observation is faithfully preserved, the contrast (7) is unchanged.

This is the appropriate representation-invariant claim. It is stronger than merely renaming a fitted coordinate “updater,” and weaker than demanding an absolute decomposition of nature into unique memory and mechanism variables. An arbitrary encoding that erases the intervention target or changes the observation cannot be used to argue that the identified contrast has disappeared. Conversely, preserving uncontrolled state paths alone does not preserve the assay. The existing [controlled-refinement account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONTROLLED-REFINEMENT.md) makes the corresponding observation/controller distinction; its Lean scope does not already supply this stochastic pushforward theorem.

## 7. Bounded empirical claims and the next test

For the selected binned-data reanalysis, the warranted hierarchy is:

| Available evidence | Defensible claim, conditional on its design/model | Claim still unsupported |
|---|---|---|
| Paired curves under changed task conditions | Reproduced paired behavioral contrast; an experimental total-effect interpretation needs the assignment/carryover assumptions | A located retained updater changed |
| Identified state-space fit with adequate error/retention information | A changed effective sensitivity parameter within that model | Unique location in input encoding, write gate or hardware |
| Persistence under common conditions, with matched direct inputs/opportunities | A retained history-dependent functional difference | Unique physical mechanism or formation of new architecture |
| Selective retained-component intervention/rescue plus matching and exclusion | Causal contribution of that component to the operative update class | Origin of the component recipe, universal beneficial selection or ethical significance |

A null paired contrast would challenge the proposed empirical connection in these public curves. A reproduced contrast with unresolved input/gate alternatives supports cost-sensitive adaptation while narrowing the proposed architectural interpretation. A selective component intervention that changes subsequent learning under matched conditions would advance the stronger mechanism claim. A direct effect on readout or input that survives the proposed exclusions would instead require revising that attribution.

The [standalone countermodel check](../../../../experiments/motor-learning-cost/identification_check.py) uses exact rational synthetic inputs, imports no workbook or producer analysis, and records its own limited scope. It checks algebraic examples and guard/exclusion witnesses, not the source data or the neuroscience model fit. This note does not claim that the observer, calibration, funding relation or replacement machinery has thereby been formed. Those remain further parts of the generative derivation.
