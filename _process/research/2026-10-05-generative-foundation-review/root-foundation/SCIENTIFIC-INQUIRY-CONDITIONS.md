# Generative conditions of scientific inquiry

6 October 2026. AI-authored mechanism and proof study of Ren's conjecture that a philosophy claiming scientific adequacy must be coherent with the generative foundation. The named connection is **formed, evidence-responsive learning → warranted, revisable scientific inquiry**. This study follows the [governing objective](../../../../theories/becoming/history/GENERATIVE-GROUNDING.md) and its [premise ledger](../../../../theories/becoming/history/FOUNDATION-PREMISES.md). It supplies conditional arguments and an interface for the current recipient/reason studies; it does not establish a uniquely necessary philosophy, a sufficient definition of knowledge, or completion of the foundation.

## 1. The strongest claim presently supportable

A philosophy that makes a definite claim about reliable empirical inquiry must accommodate the conditions needed for that claim. Those conditions include sufficient accessible distinctions for the question asked; a rule that can actually use them; warranted restrictions on the relation between evidence and target; and, when continued inquiry is claimed, the continuation of the relevant supports. The generative programme gives one connected way to explain these conditions and their production or destruction.

The mathematics below establishes **conditional necessity**, not the exclusive ownership of those conditions by our theory. A rival can satisfy them with a different ontology, vocabulary or implementation. A rival can also reject a premise or narrow its claim. A contradiction matters when the rival claims an achievement while denying a condition demonstrably required for that same achievement under the same admitted circumstances.

For example, saying that an inquiry can reliably distinguish two hypotheses while every accessible experiment has exactly the same consequences under both is a substantive inconsistency. Saying that a philosophy must agree with every current generative hypothesis is unsupported. The proof applies to the common operational constraint; additional claims concerning the formation of particular sensors, ethical significance or universal favorable development carry further obligations.

The target also needs qualification. The results concern empirical discrimination and its use. They are not an argument that every mathematical or logical truth requires a fresh environmental observation, that every scientific claim must predict a binary label, or that every sound belief must be acquired by the individual who holds it. Testimony, inherited records and preinstalled models can carry relevant information; their history belongs in the explanation when its origin is at issue.

## 2. One continuing inquiry, without an analyst's oracle

Let the unresolved alternatives be \(\theta\in\{0,1\}\). They may describe different target conditions, response laws or factual claims. At stage \(t\), the inquirer has an accessible history \(h_t\), chooses an admissible experiment \(a_t\) using a common policy \(\pi_t(a\mid h_t)\), and receives \(y_{t+1}\) under a supplied observation law

\[
K_{\theta,t}(y\mid h_t,a_t).
\tag{1}
\]

The history must include all information actually available to that policy: prior records, inherited memory, accessible stock changes, unsuccessful actions, timing and messages. An action that is unaffordable or forbidden is not automatically an available experiment. Any accessible indication of affordability or permission must itself be included. No hidden true target, evaluator's score, discarded laboratory trace or future outcome is added to the inquirer's state merely because an analyst can inspect it.

The policy is the same rule across unresolved alternatives. Giving it a different hidden-world-dependent initialization or a correct label would supply information that the inquiry purportedly has to obtain. That can be a legitimate different model, but it cannot prove discovery from the original interface. Stochastic controllers are permitted; their randomization has no extra target information beyond the accessible history unless explicitly supplied.

The finite alphabet presentation makes the proofs transparent. It is a local mathematical input, not a metaphysical claim that reality is finite. A horizon \(T\) is fixed for the initial results. Early stopping can be represented by a terminal action and padding symbols. No asymptotic conclusion follows without an actual indefinitely supported protocol.

## 3. Accessible distinction is necessary for reliable distinction

### Proposition I1 — Interactive indistinguishability

Suppose initial accessible information has the same distribution under both alternatives. Suppose also that admissible actions agree and

\[
K_{0,t}(\cdot\mid h,a)=K_{1,t}(\cdot\mid h,a)
\tag{2}
\]

for every relevant stage, common reachable history and available action. Then every finite adaptive inquiry has the same accessible transcript law under both alternatives. Any binary final decision has worst-case error at least \(1/2\).

**Proof.** Initial histories have the same law. If \(h_t\) has the same law, applying the same policy kernel gives the same joint law of \((h_t,a_t)\). Equation (2) then gives the same joint law of \((h_t,a_t,y_{t+1})\), hence the same next-history law. Induction reaches \(T\). Apply the common final decision kernel. If its probability of answering one is \(p\), the errors are \(p\) under alternative zero and \(1-p\) under alternative one. Their sum is one, so their maximum is at least one half. ∎

This is an elementary statistical indistinguishability argument, not a new law discovered by the generative theory. Its integration matters: adaptive experimentation, further reasoning and revision of the decision rule cannot recover a distinction absent from **every** accessible experiment. If an intervention changes the observation law, the premise fails and learning can become possible. If the transcript included less information than the inquirer actually has, the conclusion was applied to the wrong interface.

An abstention option changes the service claim. Under equal transcript laws, let the common probability of committing to zero or one be \(c\). The sum of the two erroneous-commitment probabilities is \(c\), so the equal-prior erroneous-commitment probability is \(c/2\). Conditional on a commitment and \(c>0\), equal-prior error is one half. Always answering “unknown” avoids false assertions while providing no discrimination. Soundness, coverage and timely completion must therefore be reported separately.

### Proposition I2 — The exact finite reliability bound

For an actual common inquiry policy \(\pi\), let \(P_0^\pi,P_1^\pi\) be the finite laws of its complete accessible transcript. Write

\[
\operatorname{TV}(P,Q)=\frac12\sum_h|P(h)-Q(h)|.
\]

The smallest equal-prior average error among every decoder of that transcript is

\[
e_*^\pi=\frac{1-\operatorname{TV}(P_0^\pi,P_1^\pi)}2.
\tag{3}
\]

**Proof.** If \(r(h)\) is the probability of answering one, average error is \(\frac12\sum_h[P_0^\pi(h)r(h)+P_1^\pi(h)(1-r(h))]\). Each summand is affine in \(r(h)\), so its minimum selects the more likely alternative and contributes \(\frac12\min(P_0^\pi(h),P_1^\pi(h))\). Summing and using \(\min(p,q)=(p+q-|p-q|)/2\) yields (3). ∎

This repeats the standard identity already proved in [Information and renewal, E1](INFORMATION-AND-RENEWAL.md); the new use is to apply it to the complete adaptive transcript rather than one isolated observation. No new theorem of statistical priority is claimed. An error requirement \(e\le\varepsilon<1/2\) requires \(\operatorname{TV}\ge1-2\varepsilon\). A worst-case error guarantee implies this average-error requirement; the converse need not hold for an asymmetric experiment. Equal weighting is the stated testing benchmark, not a claim that all rational priors must be equal. With a strongly unequal prior, always guessing the more common alternative can have small prior-weighted error without discriminating the alternatives. That is a different guarantee.

If \(\Pi\) is the actual affordable and available policy family, assume \(\Pi\ne\varnothing\) and define

\[
D^*=\sup_{\pi\in\Pi}\operatorname{TV}(P_0^\pi,P_1^\pi).
\tag{4}
\]

The family may include a no-inquiry or abstention policy when new tests are unaffordable. If no policy is implementable at all, the claimed operational capability already fails and (4) is not needed. When \(D^*<1-2\varepsilon\), the claimed reliability is impossible for that interface. A supremum equal to or above the threshold does not by itself install an affordable decoder or attain the supremum. Thus the bound gives a precise obligation, not a free construction.

For any common postprocessing kernel \(L\),

\[
\operatorname{TV}(P_0L,P_1L)\le\operatorname{TV}(P_0,P_1),
\tag{5}
\]

because expanding each processed difference and applying the triangle inequality gives \(\sum_z|\sum_h(P_0(h)-P_1(h))L(z\mid h)|\le\sum_h|P_0(h)-P_1(h)|\sum_zL(z\mid h)\). Compression or reinterpretation can make useful distinctions easier to exploit; it cannot increase statistical distinguishability beyond the complete input. A new observation or a better experiment is not mere postprocessing and can increase it.

## 4. Information, accurate output and warranted inference are different

Equation (3) proves that an optimal decoder exists when the channel laws are supplied. It does not prove that the inquirer knows those laws, can identify their interpretation, can implement that decoder, or can justify using it in a changed context. A persistent correct guess in one actual world is likewise different from a reliable method across the declared unresolved alternatives.

A minimal operational certificate can be defined without solving the whole philosophical analysis of knowledge. For a finite transcript \(h\), let

\[
\mathcal M(h)=\{m\in\mathcal M:P_m(h)>0\}
\tag{6}
\]

be the admitted models compatible with that transcript. The class includes the target **and** the relevant sensor, sampling and context laws. Suppose the same certificate rule issues claim \(\varphi\) from \(h\).

### Proposition I3 — Exact certificate scope

The certificate is zero-error sound on every admitted finite positive-probability transcript if and only if every issued \(\varphi\) holds in every model in \(\mathcal M(h)\).

**Proof.** If some compatible model falsifies \(\varphi\), the misleading transcript has positive probability in that model, so issuing \(\varphi\) is not zero-error sound. Conversely, if all compatible models satisfy the claim, issuance on any realized positive-probability transcript is correct. For a randomized rule, apply the condition to each claim issued with positive probability. ∎

If an actually received finite transcript yields \(\mathcal M(h)=\varnothing\), it signals a failure of the admitted model/interface account. The theorem covers positive-probability transcripts in the admitted class and supplies no warrant for arbitrary claims from an off-model observation. An implemented procedure must flag the mismatch rather than convert vacuous entailment into an empirical certificate.

This is a finite-support semantic entailment criterion. It does not establish that the admitted class is complete, that its restrictions are independently warranted, or that exact certificates are the only legitimate scientific inference. With noise, overlapping supports often prohibit exact identification while allowing useful controlled error. Risk bounds then require their own model, sampling law and lifetime accounting. The repository's [noisy transfer-evidence study](../../2026-10-05-concern-theory/TRANSFER-EVIDENCE-MATH.md) supplies such a conditional construction; successors cannot restart its error allowance or count copied evidence as new samples.

Scientific warrant extends beyond having written a model in which a certificate is true. Its application requires reasons for accepting the relevant law class, provenance connecting retained records to the intended question, attention to defeaters and a suitable account of inferential reliability. These are research obligations, not consequences of writing “warranted” into the output type. The note establishes a constraint on those obligations, not a complete epistemology or a deductive escape from all uncertainty.

The distinction between faithful transmission and semantic warrant is also consonant with Shannon's scope: his [1948 original paper, introduction](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) separates the engineering problem of reproducing selected messages from questions of their meaning. The present inference is ours: a correctly copied bit still needs an identified question and a justified observation law before it supports a factual conclusion. Shannon's communication theorem is not being cited as a theorem of truth or ethical justification.

## 5. A correction mechanism cannot universally certify its own channel

Consider a stable binary target \(\theta\), actions \(a\in\{0,1\}\), and actual benefit

\[
R=\mathbf1\{a=\theta\}.
\]

Only the report \(Y=R\mathbin{\mathrm{xor}}b\) is accessible, where \(b\) is an unknown fixed sensor inversion. Compare two admitted worlds:

| World | Productive target | Sensor | Report for action 0 | Report for action 1 |
|---|---|---|---|---|
| \(m_0\) | \(\theta=0\) | faithful, \(b=0\) | 1 | 0 |
| \(m_1\) | \(\theta=1\) | inverted, \(b=1\) | 1 | 0 |

Assume initial records, action costs and every other accessible consequence agree. The actual recipient benefits differ, but the inquiry has no independent observation of that benefit or its consequences. Equation (2) holds for every action and history. By I1, no adaptive controller, social vote, repeated reading or internal revision can identify which target is actually helped with uniform error below one half. A hundred instruments that copy the same corrupted source do not change the accessible law.

An independent recipient-stock measurement, an identified calibration intervention or another observation with different laws would break this particular equivalence. Statistical independence of every evidence source is not universally necessary; what is necessary for this discrimination is some accessible information that actually distinguishes the admitted alternatives. A known initial orientation could also do so, but then the task includes that inherited information.

This counterexample does not show that calibration is impossible. It shows that **unrestricted simultaneous error of target interpretation and every available checking channel cannot be defeated by checking alone**. A calibration claim always has a domain of errors it can detect and a remaining boundary of assumptions. The generative theory should explain how trustworthy interfaces arise, are cross-checked and renewed under specified conditions; it cannot replace that work with an infallible “correction” operator.

## 6. Repeated inquiry requires its supports under explicit loss assumptions

A single successful observation does not require perpetual renewal. A durable record need not be rewritten merely because time passes. Inheritance can be distributed across instruments, archives and institutions; it need not reside in one organism. These are genuine scope limits on any proposed universal memory or renewal principle.

For a simple conditional budget argument, suppose each completed inquiry consumes at least \(c>0\) units of a named accounted support; initial stock is \(B_0<\infty\); cumulative provision by time \(t\) is \(P(t)\); and other losses are nonnegative. Nonnegative remaining stock gives

\[
cN(t)\le B_0+P(t),
\tag{7}
\]

where \(N(t)\) counts completed inquiries. Consequently, unbounded completed inquiry requires unbounded cumulative provision. If \(P(t)\le P_{\max}<\infty\), then \(N(t)\le\lfloor(B_0+P_{\max})/c\rfloor\). This is a balance argument, not a universal minimum energy per true belief. Without the positive lower cost, a sequence of costs \(2^{-n}\) has finite total; without loss or a finite stock, the stated obstruction need not apply.

The stronger [root support theorems](ROOT-FOUNDATION.md) identify when finite vulnerable support types require recurrent external provision or internal renewal ancestry. They also retain durable-support and open-boundary exceptions. [Information and renewal](INFORMATION-AND-RENEWAL.md) separately gives an exact conditional tradeoff between maintaining a discriminating channel and executing responses. Its continuous-readiness requirement must not be transferred to inquiries demanded only at known sparse times; the preserved scheduling counterexample shows why.

The substantive necessity is task-relative: a repeatedly claimed capability must retain or reconstruct the conditions actually required at its demand times. It does not establish that a practice preserves truth because it persists, that success selects the best inquiry institutions, or that science must autonomously reproduce every material component inside a closed boundary. Which supports form, which are externally provided and which fail remain empirical and causal questions.

## 7. What this contributes to the actual recipient and reason projects

The [recipient identification study](../../2026-10-05-concern-theory/RECIPIENT-IDENTIFICATION-INTEGRATION.md) implements a concrete instance of I3. It observes \(C=V\mathbf1\{A=Z\}\) without direct access to the opportunity \(V\) or target \(Z\). Under its stable-target, no-false-positive law, \(C=1\) entails \(A=Z\). A zero does not. Finite all-zero histories have positive probability under both orientations when outages are possible. Paid accurate recording of those zeros cannot remove that ambiguity.

This is a valuable scientific-philosophy discriminator: a method can deliver the same amount of recipient support as a comparator while producing fewer false qualifications. Behavioral success alone does not identify the quality or provenance of the inference. Conversely, an unknown certificate does not mean help is impossible; it means the declared evidence does not justify the stronger identification.

The [recording-fidelity construction](../../2026-10-05-concern-theory/RECORDING-FIDELITY-INTEGRATION.md) establishes another distinct interface. Complete paid recording preserves its stipulated sample law; repeated outcome-selective omission can defeat the reused confidence formula. Selecting a positive witness is nevertheless sound for an implication guaranteed by a no-false-positive law. The difference concerns the inference target and assumptions, not a universal demand to store every event forever.

The current [record-to-reason construction](../../../../theories/becoming/history/RECORDED-REASONS.md) is a separate producer under active validation when this note was written. It proposes paid reading, context checks, rooted reconstruction and successor replay. Its crucial semantic interface is of the form

\[
\text{observed positive}\Rightarrow F(c,e),\qquad
F(c,e)\Rightarrow(R(c,\mathrm{src}(e))\Rightarrow R(c,\mathrm{dst}(e))).
\tag{8}
\]

The first implication is a calibrated factual assay. The second is a relevance or reason-transfer premise; the initial root reason has its own grounds. Paying for the reader and proving its graph closure cannot make arbitrary versions of either implication sound. Removing an edge after an adverse assay need not remove a conclusion that retains another valid root path. Missing observation, negative evidence, stale context and blocked action must stay distinct.

In particular, the identification branch's ambiguous zero cannot be supplied as the reason branch's sound negative assay. A compatible join must either preserve unknown status or construct a further discriminator. A retained positive is context-bound; target change may invalidate its use without corrupting the original record. The present study supplies these epistemic interface requirements, not another learner, another invented ethical reward or a duplicate formal package.

## 8. A nontrivial meaning of compatibility

Compatibility cannot mean merely that any philosophy can be renamed as a transition graph. Such representation is too permissive to decide the conjecture. For a concrete disputed claim, fix:

1. the target question, admitted alternatives and demanded reliability/coverage;
2. the actual observation and intervention interface, with resource and time restrictions when relevant;
3. what a proposed translation preserves: initial information, named actions, observations, claim meanings and feasible policies;
4. a consequence on which the two accounts can agree or disagree under that same interpretation.

The [faithful-description result](ROOT-FOUNDATION.md#1-the-invariant-is-what-the-system-can-actually-accomplish) shows why such translations preserve attainable response profiles. They cannot add a hidden true label, erase a cost, reassign a recipient or swap an intervention's meaning to manufacture agreement. A rival that predicts below-bound error under I1 or I2 contradicts the shared operational assumptions. A rival that identifies a previously omitted sensor changes the interface and may expose a mistake in our application. A rival that respects the constraints but supplies a simpler mechanism is a scientific competitor, even if it never uses the word generativity.

The philosophical burden is therefore asymmetric only where a necessity result has actually been established. Necessary conditions rule out incompatible achievement claims. They do not rank every compatible philosophy, prove the sufficiency of our account, or authorize excluding criticism of its supplied laws. Our own formulations face the same constraints.

## 9. Premises, status and the next result that would change the account

| Result or obligation | What remains supplied | What is established here |
|---|---|---|
| Interactive discrimination | Model class, complete accessible interface, common initialization/policy, finite horizon | Equal interaction laws force equal transcripts and the stated error obstruction |
| Finite reliability | Transcript laws, target semantics, error criterion | Exact decoder bound; limited information cannot be repaired by postprocessing alone |
| Exact certificate | Admitted law class and factual meaning | Issuance requires entailment across compatible positive-probability models for zero-error soundness |
| Sensor correction | Available calibration interventions and admitted error class | Jointly misleading target/sensor alternatives can defeat every available check |
| Continued inquiry | Positive support demand, accounts, horizon, actual loss/renewal laws | Stated balance and inherited support theorems constrain repeatability |
| Warranted reasons | Calibration, relevance, rooted grounds, context validity | The needed input types are distinguished; their general formation and justification remain open |

The proof steps above are elementary hand arguments, with standard statistical identities inherited explicitly. They have not been claimed as new Lean theorems or independently completed external review. No empirical data were collected and no existing scientific checks were rerun merely to create this exposition. Shannon's original introduction was inspected online on 6 October 2026; the mathematical and implementation claims rely on the displayed arguments and linked repository results, each at its own recorded validation scope.

The next constructive connection is **qualified recipient evidence → retained context and provenance → paid reason revision and successor replay**, with uncertainty and evidence identity preserved. The parallel implementation should supply actual messages and states satisfying (8), expose its remaining calibration/relevance premises and show the failure paths when those premises change.

A discriminating extension would admit both target drift and sensor inversion, then construct and pay for a calibration intervention that separates them. The theorem should state exactly which error pairs remain indistinguishable and when the mechanism must report unknown. A claim of reliable identification while both worlds in Section 5 remain observationally equivalent would fail. A discovered additional material channel would revise the interface. An independently supported realization across materially different domains would strengthen the proposed generative explanation, while an exact conventional realization would establish shared mechanism rather than exclusive theoretical ownership.

The supported research conjecture is thus: **any adequate account of empirical inquiry must respect the causal and informational conditions of the inquiry it claims to explain; the generative foundation aims to derive the formation, maintenance and revision of those conditions within one account.** Establishing that our proposed minimal principles exhaust those conditions, or uniquely characterize scientific philosophy, remains a further task.


## 10. Fallible inquiry and the foundational inference

8 October 2026. This continues [Ren's explicit completion request](../../../../sources/15-codex-theory-conversations/2026-10-08-knowledge-content-continuation.md#finish-the-necessary-foundation-of-scientific-inquiry). Begin with activity forming differences, retaining some effects and thereby changing later activity. Evidence acquisition, calibration, interpretation and judgment are differentiated relations in that history. The alternatives below are alternative specifications of that activity, not independently existing observer and world substances.

The original §§3–4 already supplied statistical bounds by hand. The exact correspondence, acquired interpretation and completed model-revision studies remain completed under their hypotheses. This continuation supplies an actual Lean check of a finite weighted, fallible component and its adaptive interface. It does not count established statistical mathematics as a new discovery. Concurrent joining-refinement work is left to its own study; its unintegrated files are not imported as accepted premises here.

```text
Result: finite-fallible-inquiry-necessity (migration of the inquiry-conditions
  claim with new formal evidence and an adaptive cross-representation connection).
Reuse: this study I1/I2 and abstention analysis; KnowledgeCorrespondence exact
  resolution; InquiryAdequacy's separation of identifying and responding;
  scientific compatibility's achievement-versus-necessary-condition test.
Delta: actual checked error/coverage bounds without perfect-answer assumptions;
  direct finite marginal-law and paired-scenario versions; common-processing
  contraction; adaptive blindness across different internal state types.
Premises: intended binary contrast; complete available information; actual finite
  natural-weight laws (equal positive totals for probability comparisons); a
  common response rule; supplied correspondence of steps and readouts.
Evidence: ScientificInquiryNecessity.lean and immutable successful receipt;
  primary statistical source comparison and author counterreview below.
Boundary: no independent empirical warrant of those laws, general knowledge
  analysis, universal ontology, entire-theory necessity or G0 derivation.
Integration: adaptive relation preservation supplies equality of readouts;
  equality supplies the coverage/error obstruction. The coupling bound also
  quantifies permitted departures. No finite-branching or perfect-answer
  premise from the joining theorem is silently imported.
```

### 10.1 A criterion independent of allegiance to the theory

Specify what the inquiry claims to achieve before asking whether our core is necessary. A binary contrast asks which of two materially or explanatorily relevant alternatives holds. A response may assert either answer or suspend. Its declared service consists of coverage and error on those alternatives. These requirements can be supplied by the scientific question, an experimental protocol or a critic; they contain no occurrence of G0, generativity, monism or acceptance of this theory.

This does not reduce every scientific activity to binary testing. It applies whenever an achievement claim includes such a contrast, including an implication of a richer estimate or prediction. A research programme can be scientifically legitimate while failing to resolve it. A mathematical proof can proceed from premises without a new experiment. The obligation is on an account that asserts the corresponding empirical achievement.

### 10.2 Exact checked content for imperfect inquiry

Let `tally w f xs` sum natural weights times the specified event count. `wrong` counts a false committed answer; `committed` counts an answer rather than suspension. The list and weights are a finite law table. They are not a finite sample presumed to certify its generating law. The following formulas are the integer statements checked by Lean.

For paired scenarios with complete evidence `e0`, `e1` and a common reader, let C be commitment weight under alternative 0, E0 and E1 the false-answer weights, and D the weight of unequal evidence. Then:

**C ≤ E0 + E1 + D.**

The pointwise reason is exhaustive: with the same accessible evidence and shared reader randomization, a committed answer is the same in both cases, so it is wrong in one of them. Unequal evidence accounts for the remaining cases. `fallible_inquiry_bound` sums this statement. `error_budgets_require_difference` yields C ≤ b0 + b1 + D from declared error budgets. Coverage 100 and each error at most 10 therefore require D at least 80; the named arithmetic corollary is checked. D depends on the chosen valid pairing, so a loose pairing yields a loose bound. It is not silently identified with total variation.

A direct marginal-law version removes the need to choose that pairing. For evidence values e with weights p0(e), p1(e), define Δ as the sum of `p0(e) - p1(e)` with natural subtraction. `distributional_coverage_bound` proves **C ≤ E0 + E1 + Δ**. When the two tables each have the same positive total N, dividing all counts by N gives the usual directional-variation bound; under equal mass the normalized Δ is total variation. The Lean statement is the natural-weight version, not a newly checked measure-theoretic theorem for arbitrary real laws.

`likelihood_attains_overlap` checks the false-answer weight of the likelihood reader as the sum of `min(p0(e), p1(e))`; `overlap_plus_excess` checks that this overlap plus Δ equals the total p0 weight. These supply the existing full-coverage testing identity at the finite rational-law interface. They do not acquire the true laws or install the reader. `sharp_fallible_witness` gives five equal-weight cases, four distinguishing and one indistinguishable, attaining C=5, E0=0, E1=1, D=4. It is a constructed law, not empirical data.

`blind_coverage_bound` proves C=E0+E1 when paired answers coincide. `abstention_is_not_discrimination` preserves zero coverage and zero errors for universal suspension. Correctly refusing an answer can be warranted; it cannot be reported as successful discrimination. A favorable prior can also reward a constant answer without resolving both alternatives. No universal equal prior is imposed on rational choice.

`common_processing_cannot_add_difference` checks contraction of paired differences under common subsequent processing. It concerns processing the same complete input, including shared randomization. A new observation, inherited information omitted from the initial description, or a change in the actual intervention law changes the premise. More computation can make an already present distinction usable; the theorem does not deny that achievement.

### 10.3 Adaptive activity and different internal descriptions

The argument need not require identical internal state spaces. In `run_preserves_relation`, one description uses S, another T; a relation R links corresponding situations. If the initial situations satisfy R and every paired step preserves it, the completed finite runs satisfy R. A step may include the policy's choice, a changed instrument, retention and a revision of the policy itself when those activities are represented in the state. A finite stopping rule can be represented by an absorbing finished state. This representation is an application obligation, not a claim that all actual inquiry has already been encoded.

R is a witness proposed by the account under test, not a definition of scientific adequacy. If related situations also give the same final answers, `adaptive_blindness_bound` connects this dynamic witness to the exact commitment/error identity. `adaptive_service_excludes_blindness` proves that such an account is incompatible with coverage greater than the sum of its two error budgets. The proof works across different internal partitions and vocabularies without a state bijection or common fragment set. It establishes an obstruction to erasing a relevant contrast; it does not recover the whole common joining structure between arbitrary representations.

Producer and consumer are joined explicitly: `run_preserves_relation` → same final readout → `adaptive_blindness_bound` → `adaptive_service_excludes_blindness`. Preserving a relation and matching readouts remain supplied premises. This does not claim to discover a matching relation for every proposed pair of theories.

### 10.4 What follows philosophically

There is now a defensible necessity argument with an independently stated achievement:

1. Fix the actual question, alternative conditions, complete access, coverage and claimed error tolerance.
2. Audit whether a proposed account preserves the relationships capable of carrying the required distinction into a usable answer.
3. Where that account entails the checked blindness or inadequate-separation condition, the claimed achievement is excluded at this interface.
4. Therefore, an adequate account of that achievement cannot also erase or deny those relationships. Its language and internal divisions can differ.

The conclusion is a general conditional constraint on empirical inquiry, with a finite weighted formal component. It is stronger than saying that science can be redescribed in generative vocabulary: it excludes definite achievement claims under definite conditions. It is also narrower than a proof that the whole ontology is mandatory. Information-theoretic success does not by itself settle consciousness, reference, explanatory depth or the authority of practical reasons.

The generative account gives the constraint a connected explanatory task: explain how relevant differences form, become accessible, persist or are reconstructed, and enter revised judgment within the same unfolding. Existing acquired-interpretation and revision mechanisms supply conditional examples. They are not counted again or treated as an empirical census. To explain continued scientific practice, its actual material and institutional supports must also be connected; the earlier support results require their own loss and demand premises. No perpetual renewal duty follows from one isolated correct answer.

### 10.5 Primary assessment and substantive counterreview

The statistical foundation is established prior mathematics. [Aldous and Fill, §12.1.1](https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch12.S1.html) state the coupling inequality and require correct marginal laws; their §12.1.2 stresses both construction and analysis of the coupling. The present finite paired bound uses that style of reasoning, with abstention exposed. [Yu 1997, Lemma 1](https://web.stanford.edu/class/stats300a/REFS/yu1997assouad.pdf) relates separation of target values and distributional overlap to estimation limits. These sources support the statistical mechanism, not our philosophical universality. Reading limits are recorded in the [source dossier](../history/root-foundation/SCIENTIFIC-PHILOSOPHY-SOURCES.md#fallible-inquiry-necessity-source-check).

| Counterreview | Assessment |
|---|---|
| Is generativity built into adequacy? | No core-allegiance predicate occurs in the formal criterion. The scientific target and law correspondence remain substantive supplied inputs. Calling every actual process generative would add no further proof. |
| Does ordinary fallibility defeat necessity? | No. Nonzero error and abstention occur in the bound. A weaker achievement has weaker requirements. |
| Do two worlds recreate dualism? | The pair compares alternative descriptions/conditions within the inquiry task. It posits no independently existing subject/object substances. A coupling is an analytical device, not simultaneous physical execution of both alternatives. |
| Does a complete record require complete reality? | No. Complete means every input actually used at this interface. Omitted inherited knowledge or timing invalidates an application; irrelevant detail need not be retained. |
| Can a model be scientifically useful while omitting the mechanism? | Yes. A useful predictor need not explain how its evidence was produced. The obligation applies to what the account claims to explain, and omission is distinct from denying a necessary relationship. |
| Can a correct answer be luck? | Yes. An actual true output alone supplies neither the two-case guarantee nor knowledge. Calibration, relevance and competent uptake retain their earlier obligations. |
| Does this refute an equally successful instrumentalist or static account? | No. Either can preserve the tested relationships. Representation plurality is compatible with shared necessary constraints. |
| Does the familiar statistical theorem prove the whole theory? | No. The contribution is formal verification and a connected necessity argument. Known mathematics gives no automatic warrant for monism, G0 or exclusivity. |
| Can finite testing establish every actual law used here? | No. The proof checks consequences of law tables; actual calibration and transfer remain fallible empirical questions. |
| Is the remaining universality gap an impossibility theorem? | No. Neither this study nor the concurrent representation work proves the generative proposal impossible. |

### 10.6 Completion judgment and the exact remaining inference

**Completed here:** a checked finite fallible constraint and its adaptive cross-representation composition; a substantive argument that any adequate explanation of the specified empirical achievement must respect it. This closes the need to rely on infallible, perfectly complete answers for that necessity argument. The argument admits ignorance, inherited knowledge, different internal articulations and correction.

**Still open:** demonstrating that the full proposed relational core, with a justified mapping from each of its commitments, is indispensable across the intended range of scientific inquiry. The current theorem establishes necessary access and use constraints; it does not identify those constraints with every claim of the theory. A proof of this broader target would need the additional mapping and scope argument, not merely another compilation or a definition of science that accepts the core.

The next substantive connection is to specify which further core commitment, beyond information carried into warranted response, is claimed necessary for a named scientific achievement; then derive its necessity or retain an adequate rival that dispenses with it. This targets the actual missing inference. The historical blanket “next construction” in §9 does not reopen the completed acquired-interpretation and model-revision studies.

**中文结论。** 本轮把可错求知的必要约束接入实际 Lean 检查：允许错误、保留不作答，低错误且有覆盖的辨别仍须有足够可用区别。不同内部状态和分节可以通过明示关系进入同一限制；不要求现实本体相同或完整模型同构。已完成的是这项条件必要性及其哲学对应，不是把整个理论、所有科学范围或 G0 的必要性宣布已证。关系产生、保留、使用和修订的统一说明仍有正面根据；其完整范围须另作论证。

Formal evidence: [source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/ScientificInquiryNecessity.lean), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/check_scientific_inquiry_necessity.py), [latest receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/scientific-inquiry-necessity-verification.json). The canonical result binds the immutable successful snapshot, not only the latest pointer. Compiler dependencies and counts are recorded there; absence of custom postulates is not absence of model premises. This is author verification, not independent-agent review or empirical confirmation.


### 10.7 Map the result to the actual core before claiming completion

The [current root](../../../../theories/becoming/history/DEEPER-GENERATIVE-ROOT.md#1-the-positive-candidate) and [premise ledger](../../../../theories/becoming/history/FOUNDATION-PREMISES.md#1-the-common-claim) begin with activity forming and changing the conditions of further activity, including observation, modeling and evaluation. Their explanatory commitment is richer than the assertion that an output bit differs. The correspondence can now be stated commitment by commitment:

| Core relationship | Independently specified achievement | Present warrant |
|---|---|---|
| Consequential differentiation becomes accessible | Discriminate opposed targets with coverage exceeding combined error budgets | The finite law-table and coupling bounds establish the required separation under the supplied law correspondence. |
| Continuing effects enter later activity | A later judgment uses information acquired earlier | Common-processing contraction excludes manufacture from a wholly erased complete input. External records or reacquisition can preserve the needed route; individual permanent memory is not required. |
| A formed organization actually uses distinctions | Realize the declared judgment rather than merely store informative data | The proof audits a reader/run when supplied. Existing acquisition mechanisms provide conditional realizations; the universal formation of all such capacities is not proved by this bound. |
| Models and inquiries occur within the reality explained | Explain production, use and correction of scientific accounts themselves | The connected account includes these activities and exposes their dependencies. This is an affirmative methodological argument, not a deduction that every entity has one uniquely specified generative constitution. |
| Conditions remain available under continuing demand | Continue an inquiry that consumes or loses its supports | Earlier support laws apply with their stated demand, loss and boundary assumptions. A fixed finite observation does not require perpetual renewal. |
| Relevant failures can change judgment or method | Correct a specified error across an admitted disturbance class | Completed revision mechanisms show realizations. The noise/target correspondence and relevant error class must remain warranted; a successfully calibrated isolated measurement need not revise itself. |

This mapping identifies both positive necessity and real limits. It prevents silently treating the most demanding account of indefinitely sustained, self-correcting science as a requirement on every isolated scientific achievement. It also prevents weakening the whole root to “some information exists” and then announcing that the original foundation has been proved.

The remaining obstacle is therefore substantive: warrant the intended scope and the additional formation/immanence commitments as necessary explanatory requirements. It is not a demand that empirical assumptions become logically infallible, that every physical law be derived, or that the completed G0 route be reopened. Conversely, merely placing those commitments in the definition of adequate science would bypass the user's conjecture. The partial theorem is finished; the full target remains a live philosophical inference with explicit content.

## 11. Necessity correspondence on the unified Becoming spine

13 October 2026. Ren reviewed the substantially advanced repository and then directed this session: “认可 请完成”. This continues the same full target; it does not replace it with the completion of this section. Work-board item P90. The argument and counterreview here are AI-authored. No independent review, new mathematical result or empirical experiment is claimed.

```text
Result: scientific-inquiry-foundation (existing open target).
Reuse: finite-fallible-inquiry-necessity; testing-within-registration;
  experiment-needs-return; learning-by-refutation;
  generalization-through-lumping; identification-where-bounded;
  process-and-frame-as-readings; tests-fix-likeness-where-determined;
  contextual-registration; the compatibility audit in ScientificCompatibility.
Delta: map these accepted outputs to the independent necessity obligation;
  distinguish necessity of a conditional law from actuality of its antecedent;
  apply the native structural reconstruction result and its native counterexample;
  resolve which formation/immanence claims are warranted and which remain supplied.
Premises / correspondence: actual task, complete access at the selected interface,
  admissible alternatives, intended readings and claim correspondence; branching
  conditions or state bounds only where the cited theorem uses them.
Evidence: the existing source-bound Lean receipts, inspected declarations,
  affirmative argument, author counterreview and primary-source comparison below.
Boundary: no proof of the full core's science-wide indispensability; no proof that
  such a foundation is impossible. The target's completion criterion is unchanged.
Integration: accepted spine results now supply the specific consumers in §11.2;
  this is interpretive reuse, not a new Lean adapter or independent result count.
```

### 11.1 Start with the inquiry as a relation within the unfolding

An experimental preparation changes what can happen next. Some of the resulting differences participate in a later record, comparison or response. Further encounters can change that arrangement or its interpretation. The instrument, investigated phenomenon, record and inquirer name differentiated relationships within this unfolding; they are not four independently given substances that a fifth relation connects. Where the preparation destroys a possibility or the record loses a difference, that loss is real and belongs to the explanation.

The independent achievements are correspondingly specific: distinguishing declared alternatives at a given error tolerance; preserving a result for later use; predicting an untried case; diagnosing a failure of a model; explaining which interventions leave which continuations possible. A scientifically adequate account of one achievement need not answer all the other questions. A general account of inquiry that undertakes all of them cannot exempt its own instruments, representations and revisions from the relationships on which its explanations rely.

That last sentence is a philosophical explanatory obligation. It does not derive a unique constitution of all reality. Nor does a supplied local law thereby lie outside reality: the problem is whether the explanation has established that law and its bearing on the achievement, not whether every upstream relation has been derived before any local explanation is allowed.

### 11.2 What each completed result now supplies

| Independent achievement | Accepted producer → necessity consumer | What remains supplied or excluded |
|---|---|---|
| Discriminate opposed empirical alternatives with stated coverage and errors | [finite-fallible-inquiry-necessity](../../../../theories/becoming/results/records/finite-fallible-inquiry-necessity.md): the finite bound requires enough distinction to reach the answer. | The finite law table, complete input boundary and application to the target. This does not require perfect knowledge or any particular mental architecture. |
| Refute or judge a claim through what a formation registers | [testing-within-registration](../../../../theories/becoming/results/records/testing-within-registration.md): `Web.Refutes.not_of_alike`, `Web.refutesWithin_iff_conjunction`, `Web.belief_judge_iff` connect registration, model-relative refutation and the shared inquiry interface. | Which relations actually register, what a record is about and which model is warranted. The `obs` relation is supplied; its existence is not derived merely by naming observation. |
| Transfer a learned response to an untried case | [generalization-through-lumping](../../../../theories/becoming/results/records/generalization-through-lumping.md): `Learning.lumped_right_iff` and `transfer_right_iff` locate correctness in the world's agreement across the model's grouping. | The grouping and actual agreement. A correct training fit alone does not establish them. |
| Infer an entire registered course from a finite record | [identification-where-bounded](../../../../theories/becoming/results/records/identification-where-bounded.md): `Identification.bounded_agree` and `bounded_induction` establish what a stated state bound permits. | Determined courses and the state bound. The bound is a restriction on admissible alternatives, not something every finite record itself certifies. P73's `no_record_fixes_next_finite` allows different, unbounded-in-size finite realizations. |
| Account for which courses and endpoint claims are possible | [tests-fix-likeness-where-determined](../../../../theories/becoming/results/records/tests-fix-likeness-where-determined.md): `alike_iff_sameTests` recovers relational likeness from the complete specified tests where both frames are determined up to likeness. | The complete question family, matched meanings of moves/claims, and the branching condition. It concerns possibility tests, not frequencies, arbitrary physical observability or a finite experimental sample. |
| Represent the inquiry and its claims in the same unfolding | [process-and-frame-as-readings](../../../../theories/becoming/results/records/process-and-frame-as-readings.md): `Shown.run`, `Frame.world_active`, `Frame.novel_iff_arises` and `World.balances_iff_exchange` connect histories, claims and worlds. | This establishes explicit representations and equivalences at their stated scope. It does not select the actual law, derive the formation of each move or give an arbitrary claim-world the material support law of an actual instrument. |
| Preserve the circumstances in which a value registers | [contextual-registration](../../../../theories/becoming/results/records/contextual-registration.md): `Contextual.indexed_fits` preserves context; `fitsFree_iff` and `no_free_frame` show when dropping it fails. | Contextuality is a reason to preserve a relationship, not to declare all scientific descriptions incompatible with the core. Indexing preserves a supplied contextual description; it does not independently establish every physical correspondence. |
| Continue inquiry under actual consumption and loss | The accepted Becoming support and renewal laws supply their conditional necessities, as already used in §§6 and 10.7. | The relevant balance, loss, embodiment and boundary conditions. No universal positive cost, perpetual inquiry or unconditional ethical obligation is inferred. |

The rows have different consumers. The statistical row constrains usable access, the learning row constrains transfer, and the reconstruction row constrains an explanatory structure. They must not be accumulated as though every success presupposed every row. Conversely, their connection within the spine is substantive progress: it is no longer accurate to describe the scientific account as just an external statistical inequality with no relation to the theory's own registration or dynamics.

### 11.3 The strongest completed structural route, and its exact failure case

The native result `Becoming.alike_iff_sameTests` is stronger than the statement that the same terminology can describe two accounts. `SameTests` asks whether each finite course of moves is possible and whether each declared claim can be realized at its end. The two frames may have different configuration types. Where both are determined up to relational likeness, agreement on this whole question family forces a bisimulation: realized claims and subsequent moves match in both directions. `Alike.sameTests` supplies the converse. These are existing, checked theorems in [Histories.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Histories.lean), not a new proof in this note.

**Application argument:** if an independently specified scientific explanatory task really includes that entire question family, and the two descriptions meet the stated correspondence and branching conditions, an equally adequate rival must preserve that relational content. This establishes a precise route to a necessary structural foundation without requiring the rival's state names or philosophical allegiance. It does not require a uniquely named ontology. The application remains conditional on the scientific task actually having this scope.

The same file contains a decisive check on broadening the inference. `Choosing.late` permits both continuations after the first move; `Choosing.early` settles which continuation remains at that move. `Choosing.sameTests` proves that the possible move courses agree, while `Choosing.not_alike` proves that the branching structures do not. This is a change in an actual transition relationship of the shared core, not a freely toggled verdict in a weaker external model. Its declared claim type is empty: the example isolates course availability and must not be advertised as an empirically calibrated model or equality of every possible observation and probability law.

Consequently, course-possibility success alone does not license full structural reconstruction in the branching case. A richer question about alternatives remaining together can distinguish the two. The existing finite-branching modal result and its spine bridge address such richer tests at their own scope. The extra question must be independently warranted; calling it “scientific” because it reveals our preferred structure would be circular.

This counterexample defeats that broadening of this reconstruction route. It does **not** refute the full theory: both frames are already represented within it, and the theory itself explains their difference. It does not show that all scientifically useful rivals can contradict the core, either.

### 11.4 Necessity of a law does not make its condition universal

The current Part I contains universal statements with their local conditions inside them. A law constraining a balanced, dissipative unfolding does not assert that every unfolding is balanced and dissipative. A scientific description outside that condition is not thereby a counterexample to the law. This corrects an overly strong possible reading of “every core commitment must be necessary for every science”: it would demand the antecedents of all conditional laws even though the theory does not demand them.

There are three different obligations:

1. **Derivation:** does the stated result follow in the formal representation, with its hypotheses intact? The existing Lean checks answer this for their declarations. Empty axiom reports do not erase binders, definitions or representation commitments.
2. **Correspondence:** does the described inquiry instantiate that representation and those hypotheses in the respects used? A frame can preserve contextual claims without making all quantities natural-number stocks; the stronger material World readings need their own correspondence. Do not transfer a limitation of one layer to every layer, or a representation success in one layer to every other layer.
3. **Indispensability:** does the independently declared achievement require the content at issue, even under another adequate description? The reconstruction theorem answers a substantial instance under its conditions; the other rows answer different instances.

A proof of the first obligation can constrain a scientific application once the second is justified. The third makes the stronger foundational claim. Formal validity alone supplies neither all actual correspondences nor the indispensability of the complete representation. Equally, failing to infer an unconditional antecedent does not undermine a valid conditional foundation.

The target here is compatibility and necessary relational content, not exclusive authorship, unique vocabulary or mandatory belief in every explanatory interpretation. Requiring those stronger properties would inflate Ren's conjecture and manufacture an unnecessary obstacle. The unresolved obstacle after removing them is still real: independently justify the scope over which the full proposed content is indispensable.

### 11.5 Formation and immanence: discharge the right obligation

The earlier §10.7 left “formed use” and “inquiry within reality” broad. Their obligations can now be separated more precisely.

**Actual use.** A claim that a recorded distinction contributed to a judgment incurs an implementation obligation: identify its participation in the actual response. Purely stored but unused information does not explain that response. `belief_judge_iff` gives an exact interface, and the acquisition and model-revision studies already give conditional implementations. This does not establish that every scientist learns that interface in the same way or that every isolated correct answer is acquired knowledge.

**Formation.** Explaining an existing capacity and explaining its historical formation are different scientific achievements within the same reality. An account explicitly undertaking the latter must explain the relevant changes in organization. Requiring every scientifically legitimate local prediction to derive its instrument's whole genealogy would be an unsupported strengthening. The universal target therefore cannot be completed by silently adding that stronger explanatory demand to every scientific act.

**Immanence.** A comprehensive explanation of inquiry must account for evidence production and uptake as activities with consequences, rather than treating an unexplained semantic verdict as the mechanism of its own formation. The spine supplies ways of doing so without a primitive knower/world partition. The further thesis that these representations exhaust the necessary constitution of any possible inquiry remains a philosophical and correspondence obligation. It is not established by the fact that an observer and its claim tokens can be placed inside a model.

Thus the actual-use obligation has a definite necessity argument; historical formation has a definite task-relative obligation; full constitutive immanence has positive explanatory support but no completed science-wide deduction here. This neither reinstalls separate realities nor dismisses the real relations a richer model has supplied.

### 11.6 Counterreview of the completed correspondence

| Challenge to this argument | Result of author counterreview |
|---|---|
| “Necessary for a complete explanatory task” was silently replaced by “necessary for every scientific act”. | Rejected. The task and question family must be stated before importing the relevant row. A calibrated single measurement is not required to be an indefinitely self-revising institution. |
| Every actual finite record satisfies the complete-test hypothesis. | Rejected. `SameTests` quantifies over all finite move courses and declared claims, not only the observations performed. P83 gives a distinct, bounded positive result. |
| The branching example refutes the theory or universal compatibility. | Rejected. It refutes reconstruction from the narrower test family without the branching condition. The full account preserves and explains the omitted relationship. |
| The formal core assumes context-free physical values and therefore fails on contextual registrations. | Too strong. `Contextual.indexed_fits` already preserves contextual readings; `no_free_frame` pinpoints the failure of removing context. Universality beyond the represented contexts is still not proved. |
| Zero extra axioms establishes that all reality must have the chosen representation. | Rejected. The kernel checks derivation. Representation adequacy is a different claim. |
| A rival that withholds the ontology contradicts it. | Rejected. Withholding assent is not denial. Establish an actual incompatible commitment before using a rival against compatibility. |
| The remaining issue is ethics, so adding G0 would finish science's foundation. | Rejected. The scientific target remains incomplete within Part I even with ethical necessity set aside. The authorized ethical route is not reopened. |
| The remaining gap proves that no necessary scientific foundation is possible. | Rejected. The existing exact cases are positive evidence. No impossibility result about the full target has been established. |

### 11.7 Primary-source comparison and reading scope

Van Fraassen's *Constructive Empiricism Now* treats instruments as arrangements producing observable effects and distinguishes acceptance from belief in a whole theory. Re-read scope: pp. 154–155 and 164–167. This supports taking an empiricist rival seriously without construing withheld ontological assent as denial of the inquiry's relations. It does not prove that rival adequate. [Author-hosted paper](https://www.princeton.edu/~fraassen/articles/pdfs/CE_Now.pdf).

Norton's *A Material Theory of Induction* argues that domain facts warrant induction, rather than a universally sufficient inference schema. Checked scope: the 2003 abstract and the author's research summary; the full-paper fetch was unreliable and is not reported as a complete reading. The comparison suggests testing actual local correspondence alongside a general constraint; it does not establish that Becoming supplies or cannot supply that correspondence. [Institutional abstract](https://eprints-prod-01.library.pitt.edu/2740/) · [author's summary](https://sites.pitt.edu/~jdnorton/homepage/research/ind_material.html).

Accessed 13 October 2026. Both are primary philosophical comparisons, not experimental evidence or borrowed proofs of this programme. The assessment of their bearing is ours.

### 11.8 Endpoint and the remaining proof obligation

**Completed in this continuation:** the correspondence audit on the unified spine, the exact structural necessity application with its conditions, the test against the native branching counterexample, and the separation of conditional-law necessity, actual correspondence and whole-core indispensability. These are integration and philosophical assessment of existing results; they are not additional independent mathematical discoveries. The earlier mechanisms, statistical results and their boundaries remain intact.

**Not completed:** the original target that the full proposed core is indispensable across the intended scientific scope. This is no longer adequately described as “we need another local learning theorem”. The missing work is to justify the coverage of the scientific question family and the remaining constitutive/representation commitments. The present record cannot honestly be changed to completed.

The next test that could change this judgment is precise: select a disputed full-core commitment; state an actual scientific explanatory undertaking independently of it; establish that every adequate description of that undertaking preserves the commitment, using an explicit correspondence or a reconstruction result whose question scope is independently justified. Alternatively, retain an adequate same-task rival that genuinely denies it. A missing representation in a thin rival is not yet that denial, and a further successful model is not yet the universal necessity proof. These are acceptance conditions, not a newly invented requirement for a uniquely named ontology.

**中文对应。** 从同一展开中形成的准备、作用、记录和回应开始，认识者与被认识者是其中分化的关系位置。科学成就须按它实际声称做到了什么来检验。已证明的结果现已给出一组实质对应：可错辨别需要可用区别；检验经由所识，模型相对的否证涉及模型与主张一起；推广正确需要世界在被归并之处确实同去；有界且确定的历程可以由有限记录确定；在双方都“在相同之下确定”时，完整的既定检验族固定关系结构。最后一项允许内部状态和语言不同，是正面的结构必要性结果，其数学证明已由共同核心完成。

但完整检验族不是已经做过的有限实验。共同核心自己的 `Choosing` 例子表明，在该例声明的范围内，所有可行的动作序列相同，后续选择是否仍同时开放却不同。这否定从较窄检验直接恢复完整分支结构的推论，不否定理论；理论本身保存了那项关系。语境性也不能被当作整个核心的反例：核心已有带语境的表示，并准确指出去掉语境何时失效。

本轮另一项修正是：科学必须尊重已成立的条件规律，不意味着每个科学对象都必须满足每条规律的前件。须分别完成推导、实际对应和不可缺少性三项工作。零公理检查完成的是相应推导；局部实际对应和结构必要性已有很多正面结果。完整核心在整个所声明科学范围内不可缺少，仍未获得独立证明。形成与内在性的根据也被分清：实际使用某区别必须有使它参与回应的关系；解释能力如何形成须交代其形成；要求每个局部科学结论都解释整段形成史则过强。把这些都纳入同一现实是本理论的正面解释方向，尚非完整科学普遍性已证。

因此，本轮完成对应与反审，不把原来的完整目标缩小后宣布完成，也不宣布它不可能。下一项实质证据必须补上所声明科学问题范围与完整核心承诺之间的必要性连接；再增加局部定理的数量本身不完成这一连接。

## 12. From fallible discrimination to the unfolding's operative relations

13 October 2026, P92. **Exact delta:** connect the already checked finite error/coverage bound to the shared spine's actual exchanges, registration and common-law response. This extends `finite-fallible-inquiry-necessity`; it is not a second independent statistical discovery. It reuses `comparison-where-the-rest-responds` and `counterfactual-is-the-course`, rather than constructing another model of inquiry.

### 12.1 The disputed commitment and independently stated task

The commitment tested is that reliable discrimination must be enabled by relationships in the unfolding that produces the response. Start with activity that changes a condition, its registration by a differentiated formation, and a response through that registration. The investigated activity and reader are roles within these relationships. Comparing two courses is an analytical comparison of possible unfoldings, not the postulation of two independent substances.

State the achievement without requiring acceptance of Becoming: on a finite weighted family of paired alternatives, the same answering procedure must attain a specified commitment coverage while keeping its errors against the false and true target alternatives within specified budgets. Abstention is permitted. A lucky correct answer in one alternative is not this achievement. The original statistical theorem already constrains it.

The new question is whether the necessary distinction may be left wholly disconnected from the relationships through which the reader responds. The result below rules that out **where the native mechanism and pairing correspond to the inquiry**. It does not assume that every inquiry everywhere has this representation.

### 12.2 Premises and formal connection

Use existing `Flow`, `Web`, `WithinResponse`, `RegistersAlikeUpTo`, `ExchangeLaw.Through` and `Flow.Follows`. The adapter's premises are all visible in its signatures:

1. The paired flows balance their condition levels and have the same formations present at each step.
2. Outside the varying part's responsive reach, initially registered condition levels agree. This permits previously formed common records; it does not permit differently informative initial records to be silently ignored.
3. Outside the varying part, both courses follow one supplied exchange law, which reads only the respective formation's registration. Existing `ExchangeLaw.Through.responds` derives the pair's response condition from that law.
4. The same answering rule factors through the reader's complete registration up to its answer time. The interface must include relevant retained records, preparation, randomization and other actual access. This factoring condition is an implementation obligation, not an assumption that answers are true.
5. Finite natural weights pair the alternatives. A probability reading needs the original result's actual-law and equal-positive-total correspondence. The quantitative reach indicator has an explicit decision of reach; the qualitative impossibility and exact blind identity require none.

`Flow.alike_beyond_response` produces equality of registered histories outside the responsive reach. `answer_alike_beyond_response` consumes that equality to obtain equality of answers. `answer_alike_beyond_law` discharges the separate response premise using the shared law. The original `fallible_inquiry_bound` and `tally_mono` then give the quantitative connection. No inference from “wants good reasons” to the content of those reasons occurs.

Write **C** for left-side commitment weight, **E₀** and **E₁** for the two error weights, and **R** for the weight of paired comparisons whose varying part is within responsive reach of the reader. The checked result is:

**C ≤ E₀ + E₁ + R.**

`error_budgets_require_reach` substitutes independently specified coverage and error budgets. If every comparison is beyond reach, `beyond_reach_coverage_eq_errors` gives the stronger exact statement **C = E₀ + E₁**. Abstention reduces coverage along with error; it cannot satisfy a positive discrimination service by avoiding all answers.

A precise distinction matters: native `WithinResponse` is a structural closure through exchanges occurring in either whole course. It is an upper bound on where differences can arrive. It does **not** prove a time-ordered transmission path by the answer time, nor that any difference travels along every available path. The theorem establishes necessity of this operative relational connectivity, not a complete identification of the actual causal message chain. `different_answers_not_beyond` states the constructive conclusion as double negation of reach; obtaining the positive finite indicator uses the explicit decision.

### 12.3 Native witnesses and counterreview

The checked `Witness` uses two formations and one shared condition within the existing `Web`/`Flow`. The varying formation either gives to that condition or does not; a distinct reader observes it. The courses start alike, balance, and the reader's exchange follows the same zero-exchange law. At step one the same readout correctly distinguishes the alternatives. This demonstrates that the mechanism conditions and successful discrimination can coexist.

A second checked rule ignores the available signal and always answers false. It still factors through the same registration and errs on the true alternative. Reach is therefore no guarantee that evidence is used well; connectivity, discrimination and knowledge remain different claims.

| Objection | Resolution and retained boundary |
|---|---|
| “Identical evidence means identical answers” was assumed and renamed a result. | Factoring through complete registration is explicit. Equality of that registration is derived from balance, initial agreement and the common law outside responsive reach. The statistical bound is reused, not relabelled as a discovery. |
| An unconnected reader can already possess the answer. | Differing informative initial records fail the stated common-start condition. Their provenance or the earlier interval must be accounted for in that application. The theorem does not erase memory. |
| Forecasting would require a future event to signal backwards. | No. The differing part is a specified source in the compared courses, not necessarily the future event named by the prediction. Common causes, initial evidence and model correspondence must be represented correctly. |
| Reach is enough to know. | Refuted by the checked ignored-signal witness. The structural closure also need not respect transmission order by the answer time. |
| A different vocabulary avoids the restriction. | A rival with corresponding courses and actual readout interfaces inherits the bound. Proving such correspondence for every adequate scientific representation is still the larger obligation, not a premise that all rivals accept Becoming. |
| A supplied law is external to the unfolding. | No. Supplying a local law limits what this theorem explains or derives; it does not place that law outside reality. Its actual warrant remains to be established. |
| This completes the full universal foundation. | No. This closes the connection from the existing fallible achievement to native relational connectivity in the stated class. It does not make discrete natural-valued balance, stable presence, initial pairing or the full constitutive account universally necessary. |

This is an author counterreview and a formal check, not an independent philosophical review or new empirical evidence.

### 12.4 Evidence, completion and bearing on the foundation

[Formal adapter](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/FallibleInquiry.lean) · [retained check](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/fallible-inquiry-checks/20261013T110231.056199Z/verification.json) · [canonical result](../../../../theories/becoming/results/records/finite-fallible-inquiry-necessity.md).

Lean 4.29.1 checked **13 theorems / 17 source declarations** in the adapter: **11 empty axiom reports and 6 using only `propext` and `Quot.sound`**. The 38 inherited modules are separately source-bound to prior passed evidence. The adapter is peripheral: nothing in the pure core imports it, and its standard dependencies do not alter or enlarge the core's zero-axiom claim. The original 18-theorem statistical receipt remains intact. New theorem counts measure formal work, not independent discoveries.

**Local completion:** the required distinction is now connected formally to the actual relationship structure of the existing spine, with the response condition derived from one common law and with successful and unsuccessful native witnesses. It is no longer merely a bare-input statistical constraint.

**Bearing on Ren's conjecture:** a philosophical account that affirms this independently stated discrimination achievement, accepts a faithful application of these mechanism conditions, yet denies even the necessary connectivity is inconsistent. It cannot rescue that same achievement simply by changing terminology. This supports the relational core at a definite point. To infer that *the entire proposed core is necessary for every scientific philosophy*, the scientific scope and remaining constitutive commitments still require the wider correspondence/necessity argument in §11. This continuation has neither completed that inference nor proved it impossible.

**中文对应。** 本轮补上的不是另一份范围清单，而是一条实编连接：在同一展开中，部分活动改变条件，条件进入另一个形成的所识，回应经由所识而形成。若两条比较历程满足明确的平衡、共同起点、同一响应律和完整读数条件，则“作答覆盖 ≤ 两类错误 + 回应关系可达的权重”；全部不可达时，覆盖恰等于两类错误之和。共同响应由同一规律推出，不再另给两个流恰好同回应的假定。原有有限统计定理、脊柱的回应闭包和同律结果均直接复用。

具体例子已核验：活动者给予共享条件、另一形成读取它，可以正确辨别；相同可达关系下忽略信号，仍会答错。这里的可达是两条完整历程中实际交换关系的结构闭包，尚非截至作答时刻的逐时传递路径。初始记录若已不同，不能套用共同起点；预测也不要求未来事件倒传信号。定理限制了充分对应到该机制的科学说明，未把这种表示的全部承诺证明为整个科学的普遍必要条件。因此，这一局部必要性连接完成，原来的全理论目标保持开放。

## 13. Test the premise: what is necessary for success, and what is necessary for a description?

13 October 2026, P94. [Ren's correction and continuation](../../../../sources/15-codex-theory-conversations/2026-10-13-scientific-foundation-as-testable-hypothesis.md) changes this session's objective from securing a predetermined positive answer to testing a revisable hypothesis. The candidate remains that the full proposed core supplies necessary scientific foundations. The admissible research outcomes now explicitly include necessity of the full core, necessity of only a proper part, and revision of a commitment. None has been established globally by this change of research direction. Work continues in this conversation; Ren explicitly declined automatic scheduling.

### 13.1 A concrete premise test, with the same unfolding and task

**Reused records:** `finite-fallible-inquiry-necessity`, `comparison-where-the-rest-responds`, `counterfactual-is-the-course` and `imbalance-as-relatum`. **Delta:** test the role of balance in §12, preserve the very same native readout task while reducing its exchange description, and prove a strictly more permissive sufficient condition for the beyond-reach blindness result. The existing `Flow`, `Web`, `Flow.withImbalance`, `Web.withRefinement` and closed-region theorem are used throughout. No separate theory or alternative world model is introduced.

Begin with the native witness's actual pattern: one formation gives to a shared condition, a distinct reader registers the changed level, and its answer distinguishes the two courses. This is one differentiated relational arrangement. The level histories, original varying formation, readout and target labels stay fixed throughout the test.

Now describe **both** histories with the zero-exchange `flow false`, omitting the giving in the true alternative. Four facts are checked:

- The same readout still answers the two target alternatives correctly (`omitted_exchange_keeps_task`).
- The reduced exchange description has no exchange and no path from the original varying formation to the distinct reader (`omitted_exchange_none`, `omitted_exchange_no_reach`).
- It no longer balances the rising history (`omitted_exchange_unbalanced`).
- The reader's rest-law still holds (`omitted_exchange_follows`); the omission was not compensated by changing that law.

Thus the numerical reach bound would fail if its balance premise were simply removed. Equally, the output achievement alone does not require the *description* to have already represented every relevant exchange. This is a boundary between success at an answer task and completeness of an exchange explanation. It does not establish that the world lacks the omitted relationship, that an incomplete explanation is adequate for a complete mechanistic task, or that the full theory has a counterexample. The original complete witness explicitly supplies the omitted relationship.

### 13.2 Does accounting for the residual remove all the conditions?

Apply the core's existing `Flow.withImbalance` to the reduced descriptions. It retains the levels and gives/takes the previously unaccounted change through the added relatum `none`; `counted_residual_balances` is an instance of the already proved balancing theorem, not a rediscovery.

The two courses' residual exchanges differ immediately: zero versus one at their first step (`counted_residual_differs`). If the residual is left outside the varying part, it registers alike at the common initial history but exchanges differently, so the response premise fails (`counted_residual_not_response`). If the residual is included among the differences, it reaches the reader (`counted_residual_reaches`).

**Balance by representation therefore does not automatically discharge the whole explanatory obligation.** The difference has been retained in another relation. Its response, origin or status among the varying conditions must still be explained or supplied. The added accounting term is not by itself empirical discovery of a new agent, and a locally supplied law is not thereby external to reality.

### 13.3 Positive result: common unaccounted change is enough for blindness

The countertest also suggests a positive generalization. Absolute balance says the description's unaccounted change vanishes in each course. The blindness proof only needs a weaker sufficient condition here: **the residual take and give agree between the compared courses**, even when nonzero.

The checked proof uses the existing balancing extension. Original formations keep exactly their registration; the added accounting relatum registers nothing. Include it with the original region outside responsive reach. `closed_with_imbalance` proves that an originally closed region remains closed in this extension. Common residual exchange makes the added relatum respond alike. The inherited `Flow.alike_within_closed` then applies.

The main result, `alike_with_common_imbalance`, retains:

1. The same formations present in the two original flows.
2. Matching initial levels on conditions registered outside the original responsive reach.
3. Original formations outside the varying part respond alike when their past registrations agree.
4. The added residual's take and give agree in the two courses at every step and condition.

**Conclusion:** every original formation beyond the original responsive reach registers alike at every time. `answer_alike_with_common_imbalance` carries this to any common answer rule through its complete past registration. There is no absolute-balance hypothesis and no decision of reach.

`common_imbalance_of_balanced` proves that the former balanced case is included: both residuals are zero. `common_nonzero_imbalance` provides a checked case with common nonzero residual and failure of original balance. This witnesses the genuine weakening of that premise. It is a controlled comparison of an existing history, not a new empirical example of a successful scientific institution.

This new result is **a weaker sufficient mechanism condition for blindness**, not a proof of the weakest possible condition. Equality of every residual at every condition may itself be stronger than needed for a particular reader or time. The unchanged finite statistical theorem can consume the resulting answer equality; this round does not claim a newly formalized quantitative bound under the weaker condition. The original quantitative native theorem retains its exact original balance hypotheses and historical receipt.

### 13.4 What changed in the foundation assessment?

| Candidate inference | Result of the test |
|---|---|
| A correct discriminating readout proves its exchange description is complete. | Rejected by the omission witness: the readout and answers stay fixed while balance fails. |
| The §12 structural-reach bound needs no balance or replacement condition. | Rejected: the omitted-exchange witness would have positive coverage, zero errors and zero represented reach. |
| A formally balanced encoding automatically explains every source of distinction. | Rejected: the added residual either violates the unchanged response premise or enters the varying part's reach. |
| Absolute balance in each original description is indispensable to the beyond-reach blindness result. | Too strong. Common residual exchange suffices; absolute balance is its zero-residual special case. |
| Therefore the complete relational theory is unnecessary or false. | Not established. The full native account preserves precisely the relationship the reduced description omits. |
| Therefore the complete relational theory is scientifically necessary. | Also not established. The checked implication requires correspondence of the represented histories, target, readout and mechanism conditions to an independently stated scientific task. |

The warranted positive conclusion is sharper than “relations matter”: within the represented task, one must not treat an uncontrolled difference in an omitted process as though it could supply no information, and shared background change need not be fully cancelled to establish blindness. The theorems distinguish which differences can enter a response; they do not turn every supplied balance convention into an unconditional foundation of science.

**Philosophical discipline.** This session does not identify being scientific with every current proposition being true. Research status, correctness, success at a specified task, explanatory completeness and foundational necessity require different arguments. Nor does scientific activity's depending on a relationship require a scientist to possess or accept our complete theory of it. These distinctions guide the assessment; they are not additional mathematical theorems established by this example.

### 13.5 Evidence and next discriminating question

The peripheral adapter adds **15 theorems and 2 definitions** to P92: the module now has **28 theorems / 34 source declarations**. Its source-declaration reports contain **20 empty lists and 14 using only `propext` and `Quot.sound`**. The pure core does not import it. The original P92 source snapshot and 13-theorem receipt remain preserved; the 42 inherited modules are separately bound to prior passed evidence. The new source and retained check are linked from the [same canonical result](../../../../theories/becoming/results/records/finite-fallible-inquiry-necessity.md). This is formal testing and author counterreview; no new empirical data or independent philosophical acceptance is asserted.

The selected next question is **how to warrant the complete actual reading interface and the relevant mechanism law independently of success in the observations already collected**. The core's finite sensitivity and bounded-identification results are available inputs; they must be reused with their hypotheses, not reopened as missing constructions. An interface called “complete” by definition is not enough, and a successful finite readout alone does not establish the law's untested scope. Work on changing registration already owned by P93 is not duplicated here. This question concerns correspondence and the scope of a claim, rather than another reformulation of the full-core necessity hypothesis.

**中文对应。** 本轮实际检验了上一轮的一个前提，而没有先要求结果支持整个理论。保留同一活动、水平历程和读数程序，只在描述中漏写造成变化的给予，读数仍然可以正确，所给交换说明却不再平衡。把未写出的差额算作已有核心中的另一个关系项，平衡恢复；但差异没有消失：新项若留在变化部分之外，就破坏“相同所识给出相同响应”的条件；若把它列入变化来源，它便重新到达读者。此例不否定完整账户中的真实关系。

更进一步，已证明原来的绝对平衡可以在不可辨别结论中放宽：两条比较历程中未计入的给予和取得相同即可，并不要求它们各自为零。旧平衡情形是其特例，还有共同非零差额的见证。这里得到的是一个更弱的充分机制条件，尚非科学活动的最终最小必要条件。成果修正了“哪些条件不可取消”的判断，而没有把成功预测、完整机制说明和整个理论的普遍必要性混成同一件事。下一步核查完整输入与所用规律怎样获得独立根据；全理论必要性作为可修正假说继续保留。

## 14. Warrant the relevant restrictions without requiring complete device knowledge

13 October 2026, P97. Begin with the actual continuation from preparation through interaction and recording to comparison and further action. Calibration and criticism are further differentiations of that same activity. The object, instrument and judging formation name roles in these relations; they are not introduced as independently existing substances. An unknown relationship can still operate, and a supplied local law can describe relationships within reality.

**Exact delta:** §13 left the independent warrant of the reading interface and response law as the next question. The [primary-source comparison](SCIENTIFIC-INQUIRY-EVIDENCE.md#6-warrant-without-exhaustive-device-knowledge) now tests whether this requires exhaustive knowledge of an actual device. It supports a narrower burden: warrant the restrictions used by the specific inference, while leaving other details open where they do not undermine it. This is a philosophical correspondence and source assessment, not a new mathematical proof, physical experiment or completed empirical instantiation of `Flow`.

### 14.1. Reuse the completed results without adding an epistemic oracle

| Producer and reused result ID | Exact output and conditions | Consumer in this inquiry | What the producer does not supply |
|---|---|---|---|
| `counterfactual-is-the-course`: `ExchangeLaw.Nonanticipating.through_sensitive` | For a supplied nonanticipating law, a list covering all condition values and decidable equality on conditions, the law reads through its sensitivity relation | A complete formal interface for the declared law; no need for a parallel observation model | Discovery of the actual law, an experimentally certified inventory of all conditions, or a computable assay of its sensitivity |
| Same result: `ExchangeLaw.Through.registers_of_sensitive` | Outside the varying part, a law reading through registration cannot be sensitive to a condition whose registration is denied: the constructive output is double negation | A precise consistency demand between the proposed law and interface | An unconditional positive observation certificate, empirical sensitivity detection, or proof that the chosen law is actual |
| `identification-where-bounded`: `Law.orbit_held`, `statesBelow_held`, `sameFuture_iff_below` | A list closed under the supplied law and containing the compared starting states yields the stated state bound and finite-record criterion for equality of registered futures | A finite route to an otherwise indefinite comparison once that bounded scope is warranted | Certification of list closure or state membership from arbitrary finite agreement; an exhaustive law-identification requirement for every scientific claim |
| `finite-fallible-inquiry-necessity`, §§10, 12–13 | The checked restrictions on discrimination, plus a weaker sufficient condition for qualitative beyond-reach equality | Constraints on a claim of reliable discrimination where its correspondence is justified | Actual error-law calibration, a uniquely required representation or the necessity of every premise used by one proof |

The first two rows are checked against the existing [Counterfactual source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Counterfactual.lean); the third against [Identification](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Identification.lean). Their canonical records retain their existing proof evidence. This round does not rerun unchanged proofs or count them again. In particular, the finite-sensitivity construction is a theorem about the supplied law, not a circular permission to choose a convenient law after seeing successful output.

### 14.2. Actual warrant has two connections

For an application, first identify the achievement without saying “accept this theory”: for example, a quantity within a declared tolerance, discrimination at stated coverage and error, or an intervention prediction in a stated range. Then distinguish two connections:

1. **Conditions to inference.** Explain why the declared restrictions license that inference. This is where a checked mathematical result, measurement analysis or valid statistical procedure contributes.
2. **Actual activity to conditions.** Give grounds for applying those restrictions to this preparation, record, range and use. Construction records, calibration, interventions and cross-checks can contribute here, with their own limits.

The two connections can be supported by overlapping bodies of evidence. “Independent warrant” does not mean logically unrelated evidence, statistical independence in every case, or a theory-free foundation. It means the grounds are not exhausted by the very success whose evidential interpretation depends on them. We have not proved a universal theorem that every such ground must be an independently measured quantity.

This yields a concrete proposed route for applications: specify the conclusion and error tolerance; identify the family of histories or laws for which the inference is valid; state why the actual activity falls within that family; and expose the changes that would defeat that inclusion. These are disclosed application obligations, not extra axioms inserted into the pure core. There is no requirement here to distinguish internally different realizations when those differences have no bearing on the warranted claim.

### 14.3. Evidence and substantive counterreview

The [E5–E7 dossier](SCIENTIFIC-INQUIRY-EVIDENCE.md#6-warrant-without-exhaustive-device-knowledge) examines metrological guidance, a primary experimental report and an adverse experimental case. Their conjunction supports the methodological distinction between task-relevant warrant and exhaustive device reconstruction. It does not establish that the repository's particular formal representation is necessary for those experiments. Bell locality assumptions must not be confused with the nondual starting point, and an outcome against one statistical family does not prove a unique ontology.

| Objection | Assessment and effect on the account |
|---|---|
| “You have only moved the assumption into a permitted family.” | Correct if membership is merely asserted. The second connection must be supported, and its uncertainty or failure retained. The family is not self-validating. |
| “Any unknown mechanism invalidates science.” | Too strong for the reviewed kinds of inference. The burden concerns the restrictions that license a particular conclusion. Unknown mechanisms inconsistent with those restrictions matter; compatible internal differences need not be separately resolved. This is not a guarantee against every unforeseen defect. |
| “Successful prediction already establishes those restrictions.” | §13's native omission witness separates successful answers from completeness of mechanism description. Application evidence must address the actual restriction, not just repeat the output. |
| “This proves our whole relational theory.” | It supports an explanatory role for relevant relations. Conventional measurement and statistical accounts remain adequate competitors at these local tasks. No reviewed source uniquely selects our full core. |
| “The conditional proofs are therefore merely assumptions.” | No. The proved consequences and sharp obstructions are real completed results. What remains open is their actual applicability and the wider indispensability claim; neither is supplied merely by the proof checker. |
| “Requiring reasons for reasons causes an endless regress.” | This round provides no final regress-stopping theorem. Practical warrant can be distributed, conditional and revisable. A purported ultimate guarantee needs a separate argument and is not obtained by naming the whole network. |

### 14.4. What is now the strongest warranted direction?

The candidate scientific foundation should preserve **the relations needed for the achievement actually explained**, including the conditions under which evidence counts and the scope of the conclusion. It should permit justified abstraction and uncertainty. The requirement that the scientist first know the device's complete law is not supported by this comparison and is removed from our proposed bridge. It was not a theorem of the core, so no core theorem is retracted.

The full necessity hypothesis now faces a specific discriminating test: choose a disputed core commitment and a scientific achievement fixed independently of it; compare explanations that retain the achievement while weakening or changing that commitment. A premise failure that merely breaks one theorem is insufficient. A missing variable in a narrower model is also insufficient. What is needed is either an adequate same-achievement explanation that genuinely dispenses with the commitment, or a warranted argument that every adequate such explanation preserves its content.

The most useful next comparison is already localized by §11's structural results: **when does an actual scientific explanation need preserved branching alternatives, rather than only matching realized records or possible completed traces?** The native branching example has already settled the abstract distinction; it must not be reproved. The new work would fix an intervention/continuation task independently, establish what alternatives that task actually warrants, and test whether an adequate trace-only account can meet it. This selects one disputed content for research without defining science to require it. Even a positive result would establish that content in the chosen scope, not necessity of the full conjunction.

**中文。** “完整界面在数学上存在”“知道实际装置的完整规律”“有根据地作出某项推断”是三种不同成就。共同脊柱已经完成前一种条件构造及有界辨识；本轮检查它们怎样消费实际证据，而不把经验根据藏入定义。结论是：科学说明应保存所说明成就需要的关系，并公开使证据有效的条件；可以有根据地抽象和保留未知。不再把穷尽装置知识作为通用门槛。接下来固定一个干预／接续任务，检验它是否真需要保留分支替代，而不只匹配记录和完整轨迹；原生数学区分已完成，实际对应才是新增义务。全核心必要性保持待检验，本轮没有新增定理、实验或独立结果。

## 15. Which continuation relations does a scientific task require?

13 October 2026, P101. Preparation changes the conditions of setting, actuation and later recording. Some of those conditions persist; others are consumed or made unavailable. An experimental controller and an investigated process acquire their differentiated roles within these relationships. Begin with this unfolding, then ask what a description must retain to explain the particular operation claimed.

**Results reused:** `tests-fix-likeness-where-determined`, `histories-fix-law-up-to-dead-ends`, `branching-tests-bisimulation`, `configurations-alike-by-relation`, `finite-continuation-plans`, and the existing `finite-fallible-inquiry-necessity`. **Delta:** fix a concrete continuation task independently of our terminology; compare lost and preserved continuation content; assess primary experimental and process-theoretic sources; distinguish relational necessity from the necessity of a graph format. **Evidence:** inherited source-bound proofs and [source dossier §7](SCIENTIFIC-INQUIRY-EVIDENCE.md#7-remaining-alternatives-actual-controls-and-the-limits-of-a-trace-comparison). No new theorem, executable adapter, experiment or independent review is claimed.

### 15.1. The actual task comes before the equivalence relation

Consider an apparatus advertised as accepting a measurement-setting command at a designated stage of an ongoing preparation. Its declared achievement concerns the available command family, the stage or timing window, execution reliability, and interpretation of the resulting records. Explaining only that each completed sequence has occurred somewhere does not yet explain which commands the apparatus can still accept at the relevant stage.

The delayed-setting experiment assessed in E8 gives this question a real scientific use. The present task concerns the coupled apparatus and its setting procedure, not a claim that a photon has already chosen a classical path or that an individual specimen can undergo incompatible measurements together. The experimental paper's particular schedule is retained; a general late-command acceptance task is a proposed comparison, not an additional achievement we attribute to that paper.

This yields two independently distinguishable explanatory scopes:

- **Completed-sequence scope:** which finite command/outcome sequences can occur in the declared preparation family?
- **Continuation scope:** at the reached stage and under the declared available information, which subsequent commands can still be executed with the advertised reliability?

A narrow answer to the first question can be scientifically useful. It becomes inadequate only if it is also offered as answering the second while omitting a difference that changes that answer. This does not classify every predictive model as defective.

### 15.2. The inherited witness identifies the lost content

In the existing `Becoming.Choosing` construction, `a` is followed either by a state retaining both `b` and `c`, or by an earlier split into a `b`-only and a `c`-only state. The checked `Choosing.sameTests` proves agreement on the whole possible-word family, with no atomic claims; `Choosing.not_alike` proves the failure of relational likeness. The [earlier branching study §4](../history/root-foundation/EXPLANATORY-BRANCHING-INTEGRATION.md#4-a-matched-target-that-exposes-the-missing-correlation) also retains its checked compound-question witness. Neither is reproved here.

The relevant difference is **whether the same reached condition retains the alternatives**, not whether the archive somewhere contains a successful `a,b` and a successful `a,c`. Interpretively assigning `a` to preparation and `b,c` to alternative setting operations identifies what needs empirical warrant. It does not establish an experiment-to-witness instance theorem. A real control system's timing, noise, observability and command mechanism are additional content absent from the small witness.

In particular, a transition's existence does not mean the command can force it. A responsive controller also needs access to whatever distinguishes the required responses, usable operations, and coverage of the possible successors. The existing finite-plan result addresses these distinctions at its own conditional scope; the branching graph alone does not.

### 15.3. Four completed inputs and their exact consumers

| Producer | Output reused | Consumer here and preserved limit |
|---|---|---|
| `tests-fix-likeness-where-determined`: `Choosing.sameTests`, `Choosing.not_alike` | Same possible words need not determine branching likeness; the witness has no atomic claims | Diagnoses the loss in a completed-sequence explanation; supplies no probabilities, command ownership or physical calibration |
| `histories-fix-law-up-to-dead-ends`: `same_finite_histories_iff` | For processes on the same state/action types, agreement on all finite traces with both endpoints retained is equivalent to pointwise step agreement | Admits a sufficiently informative history-based alternative; complete formal history families are not finite samples, and matching endpoint meanings needs warrant |
| `branching-tests-bisimulation`, with `configurations-alike-by-relation`'s `branching_bisimulation_iff` and `Alike.same` | Under image-finiteness, agreement on every finite modal test is equivalent to bisimulation; the existing bridge identifies the peripheral relation with the spine's relation | Explains the structural consequence if that whole semantic scope is warranted; no automatic physical ability to test arbitrary negations, conjunctions or repeated continuations. The general converse retains its classical dependencies |
| `finite-continuation-plans`: `viable_iff_plan`, `blind_second_step_fails`, `sensing_repairs_two_steps`, `settling_repairs_blind_two_steps` | Finite viability is equivalent to an observation-branching working plan under supplied transition, observation, target and admissibility relations; the concrete two-step witnesses distinguish missing information from changing the dependency | Separates a possible path from a plan working across its relevant information class; reused in its original module, with no newly claimed spine adapter, physical controller or infinite-plan guarantee |

The existing fallible-inquiry result adds an appropriate discipline for later applications: coverage and error must be declared separately. It does not let this study replace actual command-execution reliability with mere existential availability, nor does structural reach by itself prove timely transmission before a deadline.

### 15.4. A history-based rival can preserve the required content

It would be mistaken to conclude that science must use a branching graph instead of histories. The second row above directly blocks that inference: histories retaining the required endpoint information can carry the step law. A conditional history account can also retain command timing, preparation context and refusals. Such an account should be assessed on the same task, not rejected for its syntax.

Consequently there are three different comparisons: a flat set of feasible words; a family of histories retaining relevant conditions; and a description of the coupled command/response mechanism. Their scientific adequacy depends on which content each preserves. A model that explicitly changes the apparatus to remove the need for distinguishing a request changes the actual task mechanism; a relabeling that preserves the mechanism does not remove that need. The existing `settling_repairs_blind_two_steps` is a formal reminder of this distinction, not evidence that the particular experiment has that repair.

The source comparison makes a second correction. Hennessy–Milner-style semantic questions and physically executable tests are different objects. The primary process-theory sources assess this distinction; we do not import their analytical observer/process boundary as an independent ontology. An experimental procedure may support a subset of continuation questions without supporting the entire language used by the structural theorem. Our positive argument must preserve that subset's actual content before asking whether a stronger reconstruction follows.

### 15.5. Discriminating evidence and substantive counterreview

The [prospective protocol](SCIENTIFIC-INQUIRY-EVIDENCE.md#72-a-discriminating-protocol-still-unrun-here) retains both successful and failed commands at the designated stage. It compares late responsiveness with a preparation that has already lost an option, and with a history-based account that preserves the same response content. It remains unrun. The published experiment establishes relevance of the setting-operation relation at its reported scope; it is not a dataset comparison of our three proposed accounts.

| Challenge | Assessment |
|---|---|
| “You required a branching graph in the definition of success.” | No graph appears in the operation task: commands, timing, execution and records specify it. The existing witness diagnoses a particular content loss; history-based rivals retaining that content are admitted. |
| “Both successful sequences have been observed, so both options remained available in each preparation.” | Unsupported. The sequences may arise in different preparation conditions. A command-stage comparison must address that correlation and count failures. |
| “The paper proves the full late-branch model.” | It does not. The mapping is interpretive and limited to operation content; exact state correspondence, all-policy coverage and every unperformed alternative remain unestablished. |
| “Alternative commands require an agent outside the unfolding.” | No. Setting generation, delivery and actuation are related activities within it. Counterfactual variation is a scope of comparison whose applicability needs warrant, not an external cause or a proof of metaphysical free choice. |
| “A possible successor guarantees operational control.” | No. The response interface and successor coverage have separate obligations. The inherited finite-plan examples show why a first usable action or one successful path need not suffice. |
| “Testing both options means copying the exact state.” | No such operation is supplied. Supported repeated preparation, restoration, theoretical constraints or another justified method would be needed for the claim made; modal conjunction does not itself construct any of them. |
| “All histories agreeing proves arbitrary finite observations suffice.” | No. Complete endpoint-indexed families and finite empirical records have different scope. The positive history theorem does not waive correspondence. |
| “Any counterfactual success forces full bisimulation.” | Not established. The theorem requires its full modal question family and image-finiteness. One operational task does not establish either condition. |

### 15.6. Necessity judgment after this test

**Supported as a scoped philosophical argument:** an account claiming to explain a preserved command/continuation capability must preserve the distinctions that determine that capability under its declared conditions. Existing proofs give concrete, nonverbal examples of how forgetting the reached-condition relation loses such content. The new source assessment makes the operation question scientifically motivated and limits its application.

**Not supported:** a universal requirement that every scientific explanation use branching notation, that a commandable apparatus supplies every modal test, or that the reported experiment proves the whole structural or ontological reconstruction. The historical full-core target remains open; this comparison neither refutes the fuller account through a lossy representation nor makes it necessary by calling every adequate alternative generative.

The next exact connection is now **fallible command execution at a declared stage**: separate a record correlated with the command from a response actually conditioned by it, using the already checked finite discrimination and continuation results. A source-bound formal application must identify the command input, the response time, the available information and the success/error scoring. The current structural-reach bound is not already a deadline theorem. A new time-sensitive connection should be added only after checking the existing spine and its owners, not by rebuilding the generic branching or learning results.

**中文。** 本轮把“科学是否需要分支结构”落到具体任务：准备到某一步后，哪些后续指令仍能执行，什么读数因此有根据。已有原生反例说明，相同的可行轨迹清单会漏掉同一到达条件下保留哪些替代；已有历史定理又说明，保留起终点和完整有限历史可以恢复步骤关系。因此必要的是任务所需的接续内容，不是必须画分支图。实际控制、有限误差、重复准备及语义测试各有对应责任；延迟设置实验没有被当作完整分支模型的已证实例。复用的形式结果保持原范围，本轮新增的是科学任务对应、一手来源评估与实质反审，不新增定理或实验。完整核心普遍必要性仍待检验。

## 16. A distinction must arrive before the answer that uses it

13 October 2026, P104. A change enters ongoing activity, modifies a shared condition, and may be registered by further activity whose exchange changes what follows. Command production, relay and readout are differentiated roles within this unfolding. Their temporal ordering matters: a relation formed later cannot be counted as having transmitted an earlier difference.

**Reused results:** `comparison-where-the-rest-responds`, `testing-within-registration`, `finite-fallible-inquiry-necessity`; existing `TimedFeedback` is separately retained at its calibration/age scope. **Delta:** extend the shared spine with step-indexed potential propagation, prove deadline blindness and its relation to whole-course reach, then formally compose it with the existing statistical bound. This substantively new temporal statement is registered as `timely-response-necessity`; helpers are not independent findings. **Sources:** `Becoming/TimedResponse.lean` and the appended `TimedWeighted` section of `Becoming/FallibleInquiry.lean`. **Evidence:** final core `20261013T125224.520783Z`, periphery `20261013T125313.109762Z`; source-bound details are in the [integration review](SCIENTIFIC-INQUIRY-TIMING-REVIEW.json).

### 16.1. The exact temporal construction

`RegistersAt W obs h s c` means that `c` is required for `h` at step `s`, or is explicitly observed through `obs`. `TouchesAt` retains an actual nonzero give/take exchange at a named step in either course, on their shared present list. `Spread` begins only with a declared source exchanging at step `t`, affecting a condition at `t+1`. It can persist, or pass through registration at a step `s ≤ t` and a later response exchange at `t`, affecting its next level at `t+1`. `ReachedBy g D` asks whether such propagation enters a condition registered by `g` at some step no later than `D`.

Author counterreview tightened the initial draft: a requirement appearing only in a future step must not create an earlier registration edge. The final source uses `RegistersAt`, rather than the older whole-history `Registers` envelope, for both propagation and readout entry. Its bridge `registersAt_registers` permits reuse of the old structural relation. The first draft's passed receipt is preserved as history, not substituted for the final proof.

`Spread.has_earlier_source` proves that any propagated condition at step `t` has a source step strictly earlier than `t`. `reachedBy_within_response` proves that, when all source formations belong to the old varying part and presence agrees, a timed route lies within the existing whole-course responsive reach. Thus this is a refinement on native flows and webs, not another world model. The converse fails in the delayed witness.

These routes are **potential influence under the declared registration interface**. Their existence neither says that the available distinction changes an exchange nor gives a sufficient command-execution policy. The source predicate is supplied; the theorem does not discover it from correlated records.

### 16.2. What is proved, and under which conditions?

For two courses and deadline `D`, the local theorem requires:

1. Equal initial levels on all represented conditions. This is stronger than the older theorem's restricted common start; it excludes already-different informative records from this application.
2. Balance and equal present formation lists at every step strictly before `D`. Later exchanges, balances and presence need not agree.
3. Outside the step-indexed source, equal past registration implies equal exchange at that step. This is an explicit mechanism premise; appropriate common-law instances can use the previously checked response results.
4. A common readout that factors through complete native registration up to `D`, including relevant support information. The same `W`-based interface compares both level histories; applying it to changed physical interfaces needs its own warrant.

Under these conditions, `levels_alike_before` and `registration_alike_before` show equality outside timed propagation. `answer_alike_before` gives equal answers for **any output type**. Different answers therefore exclude being unreached (`different_answers_not_unreached`); positive membership is separately obtained when route membership is decidable (`different_answers_require_reached`). The constructive distinction is retained rather than silently importing excluded middle.

The statistical adapter supplies finite natural weights, paired opposite target labels and an explicit decision of timely reach. Its checked conclusion is:

\[
\text{committed-answer weight}
\leq \text{left error weight}+\text{right error weight}
       +\text{weight of pairs reached by their answer time}.
\]

The commitment term concerns the left course's non-abstaining answers, exactly as in the inherited bound; it is not silently redefined as a symmetric success rate. `error_budgets_require_timed_reach` consumes independently specified coverage and error budgets. If every pair is unreached, commitment equals the paired error total; that equality needs no route-decision assumption. Weights are not automatically probabilities, and pairing actual experiments remains a correspondence obligation.

### 16.3. Positive and adverse controls in one native description

The `Delayed` witness has two formations sharing one condition. The source exchanges across step one; the reader observes the condition. Both flows balance and their non-source responses meet the stated premise. Whole-course structural reach is present, but `not_reached_at_one` holds. At step one both answers are the same; at step two `reached_at_two` holds and the supplied reader distinguishes the alternatives. `constant_read_ignores` retains the further failure: an equally admissible constant reader ignores the reached signal.

These are exact mathematical examples, not apparatus measurements. They separate three claims: eventually connected, potentially reached by the answer step, and effectively using that distinction. Earlier `TimedFeedback` results concern acquisition age, drift and exposure bounds, while `finite-continuation-plans` concerns viable command policies. Neither already supplied this native propagation-to-discrimination composition, and neither is superseded by it.

### 16.4. Actual commands, correlated records and counterreview

The [source assessment](SCIENTIFIC-INQUIRY-EVIDENCE.md#8-timing-command-execution-and-causal-correspondence) supplies a further discipline: distinguish a command's assignment, delivery, actual actuation and recorded outcome. Comparing records grouped by a command is not yet a warranted comparison of changing that command while preserving the relevant response conditions. Our paired courses express such a comparison conditionally; the proof does not certify that an apparatus realizes it.

| Challenge | Assessment and consequence |
|---|---|
| “You defined the route as whatever explains success.” | No success or correctness occurs in `Spread`: only source exchange, preservation, time-specific registration and later exchange. Correctness enters separately through the statistical adapter. The actual source and interface nevertheless require warrant. |
| “The source is simply an external agent.” | No. It is a step-indexed family of formations in the same flow. The intervention comparison varies their activity; no ontologically outside controller is introduced. |
| “A future support relation was counted as earlier knowledge.” | The final `RegistersAt` correction excludes it. Physical access and the explicit observation relation still need correspondence. |
| “Some predictions are correct before their target happens.” | This theorem does not require a signal from a future target. Earlier informative conditions may explain prediction. A comparison with different informative initial records violates this theorem's common-start premise. |
| “A timely route guarantees reliable execution.” | Refuted by the ignored-signal control; finite-plan, actuation and success obligations remain separate. |
| “A step is a fixed physical duration.” | Not supplied. Real clocks, delays and substep ordering need an appropriate representation and uncertainty analysis. The result is not a light-speed, latency or continuous-time theorem. |
| “This removes balance or makes it scientifically universal.” | No. The new result localizes balance to the relevant prefix and keeps it explicit. P94's common-residual theorem remains intact; its timed extension is not proved here. |
| “The equations establish a unique scientific philosophy.” | No. Any adequate alternative preserving the same task-relevant temporal dependence remains admissible. The new theorem constrains the stated explanatory task, not all scientific questions. |

### 16.5. What is now complete, and what remains?

The precise **deadline connection is complete conditionally**: native ordered exchanges → bounded arrival in registration → bounded distinguishable response → the inherited coverage/error inequality. Twenty-two pure-core theorems and three peripheral composition theorems implement this one connection, with exact assumptions and checked witnesses. They are not twenty-five independent foundations. Thirty new core source declarations have empty axiom reports; the three statistical adapters retain only the inherited standard dependencies `propext` and `Quot.sound`.

The next substantive test concerns **which initial evidence and command assignments justify the paired comparison in an actual task**, including preselection, non-execution and record loss. It should consume this bound rather than rebuild it. Existing G0/J work, general continuation plans and quantum interpretation are not reopened. The full theory's universal indispensability is still an open hypothesis.

**中文。** 本轮补上真正的时间连接：同一展开中，改变须经实际顺序进入后续所识，才可能改变截止时的回答。在共同初态、截止前平衡及在场相同、其余经此前所识回应、共同完整读数等明示条件下，未及时进入的区别不能产生不同答案；作答覆盖因此受两侧错误与及时可达权重共同约束。未来才出现的支持条件不能倒算为此前的识，连通也不保证正确使用。原生延迟和忽略信号例子、实际对应及更强目标的边界均保留。新增25项形式定理服务于同一个必要性连接，不是25项独立发现；科学普遍必要性未因此完成。

## 17. Stronger foundations and the assessment of scientific standing

13 October 2026, P105. Ongoing activity leaves traces, forms instruments and inherited expectations, and sustains practices of questioning, reporting and correction. The roles of object, observer, evidence and critic differentiate within these relationships. Being physically affected does not itself make a record evidence for a specified claim: the relevant relation, alternatives and error controls need warrant. A supported institution can preserve error as well as knowledge.

**Results reused:** `scientific-inquiry-foundation`, `finite-fallible-inquiry-necessity`, `timely-response-necessity`, and the existing [scientific-philosophy counterreview](../history/root-foundation/SCIENTIFIC-PHILOSOPHY-COUNTEREXAMPLES.md). **Delta:** connect the completed causal-access constraints to a practice-level assessment of scientific standing; distinguish it from truth, warrant and full-core necessity; test the proposed assessment against counterexamples. **Supplied commitments:** empirical claims should receive support appropriate to their content and exposure to relevant error; these epistemic standards are argued for here, not derived from causal reach alone. **Evidence:** source assessment [§9](SCIENTIFIC-INQUIRY-EVIDENCE.md#9-demarcation-without-confusing-science-with-success), inherited checked results, and substantive author counterreview below. **Boundary:** no new mathematical proof, empirical experiment, independent review or complete demarcation theorem. **Integration:** update the same open foundation target; this is not another independent result.

### 17.1. What the stronger conclusion actually adds

The completed theorem has a precise consequence: under §16's common-start, prefix balance/presence, response and complete-readout premises, a distinction absent from timely registration cannot yield different answers. The finite bound then limits the claimed coverage and error performance. It concerns paired discrimination, not whether every isolated correct report requires adaptive learning. Earlier informative records, common causes and different initial information retain their stated treatment.

The stronger philosophical proposal concerns **empirical authority**: a practice claiming to distinguish unresolved alternatives owes an account of why its available evidence discriminates them, and a continuing practice claiming correction owes an operative route by which relevant defeats can alter its conclusions or methods. Mere willingness to follow good reasons supplies neither the reasons nor that route. The first burden concerns evidential warrant; the second concerns corrective capacity over an appropriate research horizon. Neither requires every investigator to change every belief after every criticism.

This goes beyond a bare declaration of falsifiability by examining the formation, selection, interpretation and uptake of evidence. It is an argued assessment standard, not a new consequence obtained simply by renaming `ReachedBy` as science. A reached signal can be ignored; a responsive reader can be systematically miscalibrated; an immutable instrument can contribute to a corrigible wider practice. Those earlier counterexamples remain decisive.

There are therefore three levels of strength: **checked conditional restrictions** on a declared discrimination task; **a philosophical account** of warranted, corrigible empirical practice; and **the full-core necessity hypothesis** across scientific domains. The first supports examination of the second without completing it, and neither currently establishes the third. No field is excluded from science solely because it challenges our framework.

### 17.2. Assess a claim-in-practice at a stated stage

The assessment unit is a specified claim or research programme, its evidential procedures, scope and development stage. A profession, journal, institution or mathematical style supplies context, not a verdict. The following questions guide review; they are not a universal checklist with a passing score.

| Question | Material to inspect | What a failure initially establishes |
|---|---|---|
| What is claimed, and with what confidence? | Target, range, alternatives, whether the contribution is exploratory, theoretical or confirmatory | An unclear or inflated claim, not automatically pseudoscience |
| What could make the evidential assessment less favorable? | Discriminating consequences, rival explanations, sensitivity to adverse findings and uncertainty | Missing test content or an unresolved comparison; absolute logical exclusion is not required for probabilistic claims |
| Why should these records bear on this target? | Calibration, provenance, controls, sampling, exclusions and relevant background knowledge | A warrant gap; receiving data alone does not repair it |
| Can another competent investigation challenge the inference? | Inspectable reasoning and methods, suitable access or protected audit, independent measurements and alternative analyses | A limitation on scrutiny; universal public release of protected data is not required |
| What actually happens when evidence conflicts? | Changes in confidence, correction of measurements, revised scope, altered methods, replacement or suspension | Distinguish diagnosis with testable consequences from repeated devices that insulate the favored conclusion |
| What was learned beyond redescribing the accepted examples? | New discriminations, constrained explanations, successful transfer, documented limitations or informative negative findings | A research programme may remain preliminary; positive prediction success is not required from every study |

Together these support defeasible judgments about empirical standing and warrant. We have not established a necessary-and-sufficient classifier of everything called science. Scientific investigation, ordinary inquiry, engineering and historical scholarship share some of these practices; the present account does not invent an exclusive boundary by subtracting their legitimate overlap. Formal mathematics has proof obligations and can support science without every theorem itself being an empirical hypothesis.

### 17.3. Substantive counterreview

| Challenge or case | Judgment and retained distinction |
|---|---|
| A testable prediction turns out false under careful investigation | A failed scientific hypothesis may be the product of good science. Truth and method are separate. Testing a pseudoscientific claim can itself be scientific. |
| A field studies an event that cannot be rerun | The historical event need not recur. Competing explanations may be assessed through surviving traces and their warranted relations; see E13. |
| A probability forecast assigns positive probability to every individual outcome | Scientific assessment can concern calibration and comparative performance over an appropriate evidential scope. One outcome need not logically falsify it. This is a conceptual case, not a newly proved probability theorem. |
| A well-conducted study fails to replicate | Investigate sampling, variation, scope, methods and error. A single failure neither establishes fraud nor disqualifies the field; see E14. |
| A novel theory has no feasible direct test yet | State its theoretical and indirect support and the missing test. Limited present confirmation is different from systematically evading relevant scrutiny while claiming established empirical authority. |
| An anomaly is attributed to equipment or an auxiliary assumption | Legitimate if the proposed diagnosis has independent reasons or further discriminating consequences. An anomaly does not automatically identify which component failed. |
| A research group changes beliefs frequently in response to rewards or pressure | Mere causal responsiveness is insufficient. The changes must be warranted for the declared target; consensus and persistence do not supply that warrant. |
| A practice advertises scientific authority but systematically suppresses adverse results or makes every possible outcome confirm it | Strong grounds for rejecting that authority and, where the pattern is established, identifying pseudoscientific practice. Honest error, scarce resources or one disputed judgment alone do not establish this pattern. |
| A private or isolated investigator cannot immediately share all material | Assess whether there is a credible route to appropriate scrutiny and correction, including protected review. Publication prestige and universal immediate access are not constitutive tests. |

The distinction between weak research and pseudoscientific insulation is consequential but does not license reading motives from a failed result. Assess documented procedures and responses over a suitable interval. The standard itself remains revisable if it repeatedly excludes warranted empirical achievements or admits practices shown to be insulated from relevant evidence.

### 17.4. Apply the same standard to the Theory of Becoming

Our conditional formal results have checked inferential support; this does not certify their applicability to an apparatus or prove the universal necessity of the representation. The philosophical account has explicit arguments and counterexamples. The universal scientific-foundation claim remains open. Describing those statuses separately is part of the present assessment, not a verdict that the whole project is either established empirical science or pseudoscience.

An important consequence for this programme is the distinction between **representing every outcome** and **empirically discriminating among outcomes**. A general formal language can represent successful and failed inquiry. That breadth is useful, but each occurrence is not thereby independent confirmation of a privileged substantive law. Conditional laws acquire empirical bearing through warranted local conditions and consequences. A universal formal identity is assessed by proof; a claim that it uniquely or necessarily captures actual science needs additional correspondence and necessity arguments.

Three findings would change our account. First, an independently warranted scientific achievement incompatible with an alleged necessary commitment would force revision of that commitment or of its claimed scope, after checking that the conflict is substantive rather than an omitted relation. Second, an adequate alternative preserving all the declared task content without our disputed commitment would undermine its necessity, even if our account remained useful. Third, a demarcation judgment that protects our theory solely by redefining successful competitors as unscientific would invalidate that judgment. Ren's full-theory conjecture receives no exemption from these tests.

The next useful comparison is a matched assessment of a warranted empirical claim, a carefully investigated failure and a practice that claims authority while insulating its verdict. State the review questions before assigning the labels, document the relevant evidence, and keep initial-information and actual-command pairing as the separate unresolved application of §16. This assessment has been specified here; it has not yet been validated as a cross-domain classification instrument.

**中文。** 可以推进到更强的哲学主张：经验权威须有可审查的辨别根据，持续纠错须有能实际影响判断的关系。科学性、结论真伪、证据强弱和纠错质量分别判断。可检验却错误的假说、诚实但薄弱的研究、尚待检验的理论，以及以科学名义系统性保护结论的实践，不能混为一类。现有逐时定理支持其中的机制必要条件；它既不直接定义科学，也未证明完整理论普遍必要。我们的“包容一切结果”同样不自动增加经验支持；真正的反例和充分的竞争说明必须能改变本理论。
