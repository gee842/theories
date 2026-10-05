# Conditional universality: laws of expenditure, provision and support

6 October 2026. Research direction: Yongxu Ren. AI-assisted theory, Lean development and separate internal review, following [Ren's proposal and instruction](../../../sources/15-codex-theory-conversations/2026-10-06-conditional-universality-request.md). This extends [the deeper root](DEEPER-GENERATIVE-ROOT.md) and advances the explicit-grounding and cross-model generality obligations of [the unified foundation](GENERATIVE-GROUNDING.md).

## 1. The universal target

Ren's proposed form is: **for any reality whose laws have specified properties, derive what necessarily follows.** The mathematical target is

\[
\forall P,\quad A(P)\Longrightarrow G(P),
\]

where \(P\) is a declared process, \(A\) specifies independently interpretable local law conditions, and \(G\) is a consequence about its possible histories. Application to a reality requires an adequate realization of those conditions. A theorem over the class and evidence that a system belongs to the class are distinct achievements.

This is the active form of the universal research ambition. A proof that only one metaphysical ontology is conceivable is not a prerequisite for it. Nor does conditional universality weaken the requirement to explain learning, selectors and concern within the process: a downstream capacity must still be derived under visible conditions, not inserted as an unexplained reward or authority.

The present development supplies substantive continuation constraints for a class of laws. It does not assert that every lawful process renews, learns or improves. Static, exhausting and recurrent-but-unlearning dynamics remain admissible outside stronger subclasses. The [earlier exact representation theorem](DEEPER-GENERATIVE-ROOT.md#5-keeping-history-prevents-an-unexplained-memorylessness-assumption) explains how finite admissibility can be represented; the results here constrain what can occur under additional local laws.

## 2. A local law with no assumed renewal

Let \(P\) be any process with states \(S\), event labels \(A\), and an admitted transition relation \(s\xrightarrow a t\). No finite-state, determinism, benevolent policy or scalar utility assumption is made.

For one stated support, specify natural-number quantities:

- \(r(s)\): usable reserve or an independently justified nonnegative support certificate;
- \(d(s,a,t)\): demand charged to this event;
- \(c(s,a,t)\): provision credited during this event.

The local law is

\[
\boxed{r(t)+d(s,a,t)\le r(s)+c(s,a,t)}
\tag{U1}
\]

for **every admitted transition**. An inequality permits additional uncredited losses. Demand and credit may depend on the actual source, event and successor. Zero-demand events are allowed; the generic law does not equate change with expenditure.

The quantities must use commensurate units within this one support account. Natural numbers define the checked discrete class. Application to continuous magnitudes needs justified discrete bounds or a separately proved ordered-number extension; it is not automatic rounding. A mathematical potential may also be valid, but then its interpretation as a certificate rather than a freely exchangeable material stock must remain explicit.

The law alone is deliberately permissive. Assigning zero to all quantities satisfies it for every process. Assigning demand equal to invented provision is equally uninformative. Its explanatory content comes from an independent account of what is consumed, what arrives, what remains usable and which quantities can become unbounded. The analyst's outcome score does not operate the mechanism or supply the credited input.

## 3. The universal prefix bound

For an actual finite history \(s_0\xrightarrow{a_0}s_1\cdots\xrightarrow{a_{n-1}}s_n\), define cumulative demand and provision along those exact edges:

\[
D_n=\sum_{k<n}d(s_k,a_k,s_{k+1}),\qquad
C_n=\sum_{k<n}c(s_k,a_k,s_{k+1}).
\]

Summing U1 gives

\[
\boxed{D_n+r(s_n)\le r(s_0)+C_n.}
\tag{U2}
\]

The Lean development proves this for actual ledger traces and execution segments, retaining intermediate states. Every prefix obeys the same bound. An eventual total cannot repair an earlier violated prefix. Within-event ordering is only as detailed as the primitive process: if payment and receipt order matters, that event must be refined or its admissibility justified independently. U2 is a necessary constraint, not a proof that every numerically balanced transaction can occur.

Consequences include:

1. If cumulative provision is bounded by \(B\), cumulative demand cannot exceed \(r(s_0)+B\).
2. If actual cumulative demand is unbounded, actual cumulative provision is unbounded.
3. If every event demands at least one unit, an \(n\)-event history requires \(n\le r(s_0)+C_n\).
4. If each positive-credit event supplies at most \(K\) units, its count \(N_n\) satisfies \(n\le r(s_0)+K N_n\) in that positive-demand subclass.
5. An infinite lawful execution in that subclass must have a positive-credit event in every suffix window longer than the reserve available at the start of that window. Consequently such events occur arbitrarily late.

These are universal necessities for the law class. The existence of an infinite execution is a hypothesis when used, not a consequence. The account derives that continued expenditure requires continued provision; it has not yet identified whether that provision is imported, internally produced, or supplied by a combination.

A family of accounts indexed by support type satisfies U2 **coordinate by coordinate**. This does not require adding money, competence, information access and authority into one numerical value. If any indispensable coordinate fails its independently justified bound, the proposed joint history cannot meet all the stated conditions.

There is also a constructive counterpart. Accounted histories concatenate through their actual shared boundary state, adding demand, provision and credited-event counts. If an executable history returns to its starting state, Lean proves that every finite number of repetitions is executable, with each total multiplied by the repetition count. For a nonempty cycle this permits arbitrarily long histories. Its demand must be covered by provision. This is possible recurrence under the supplied transition law; it does not force a process to choose that cycle. A depleting external supplier must be included in the state or justified as an ongoing input, rather than hidden behind an apparent local return.

## 4. Transport across implementations

To apply the result, a concrete process may map into a simpler process through a state map \(q\) that preserves each concrete step as an admitted abstract step. Pull back the abstract reserve, demand and provision through \(q\). U1 then holds on the concrete process, so its histories inherit U2.

A forward step-preserving map suffices for this necessary bound; a two-way exact representation is stronger than needed here. The map must preserve the quantities and meanings used by the account. Merely assigning the same names to unrelated variables does not supply the bridge. This transport does not give a participant access to the mapped state, prove a policy implementable, or preserve probabilities.

The existing concrete regulation and variant studies can use this interface when their costs, receipts and successors satisfy the law. Their particular chemistry remains a legitimate local input. The generic theorem imposes a common constraint without pretending that one specific chemistry governs every realization.

## 5. From provision to support ancestry

Provision accounting alone cannot prove internal repair or a renewal cycle. The separate support theorem identifies a law class in which continuing organization has a finite deadline if its production dependencies have bounded acyclic depth.

Use natural-number time and functioning episodes. An episode has a type \(i\), birth time \(b\) and expiry time \(e\). It functions at times \(b\le t\le e\): expiry is inclusive. Specify:

1. Each episode expires within a finite bound \(L\) after its birth.
2. Initial episodes are born at time zero.
3. Every later episode has an earlier-born parent functioning at its birth; the parent-to-child type pair is an allowed production dependency.
4. Every dependency strictly increases a natural-number type rank.

These conditions do not assume a sustaining loop. The parent condition excludes spontaneous or externally supplied organized episodes from the closed account; raw material and energy may still be legitimate inputs if the specified parent is required to form the functioning episode.

The derived deadline is

\[
\boxed{e\le (\operatorname{rank}(i)+1)L.}
\tag{U3}
\]

If all relevant ranks are at most \(H\), no episode is functioning strictly after \((H+1)L\). Equivalently, ranks in `Fin n` give the common bound \(t\le nL\) for functioning. Thus observed functioning beyond that bound refutes the conjunction of the rank certificate, lifetime bound, parent requirement and boundary specification.

A more general local certificate permits unequal durations \(\tau_i\). If type deadlines \(T_i\) satisfy \(\tau_i\le T_i\) and every permitted edge \(i\to j\) satisfies \(T_i+\tau_j\le T_j\), each actual episode of type \(i\) expires by \(T_i\). This global conclusion follows by induction on birth time; it is not supplied as a premise. U3 follows by taking \(T_i=(\operatorname{rank}(i)+1)L\).

The [mathematical companion](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONDITIONAL-SUPPORT-MATH.md) records the exact quantified contract and proof. This is a **rank-certified acyclic** theorem. It does not silently claim that this Lean module extracts a cycle from every arbitrary finite graph. Nor does exceeding the deadline uniquely identify a cycle: an omitted outside supplier, a longer-lived support or unboundedly many dependency levels can invalidate another premise.

The episode model describes an admitted catalogue of births, expiries and actual parent relations. Its type-level process represents permitted dependency edges, not the full dynamics generating that catalogue. To bound an organizational function, separately establish that its occurrence requires a currently functioning episode covered here. To combine this theorem with U2, establish both interfaces on the same implementation; two necessary constraints alone do not construct a jointly feasible process.

The older [turnover and closure theorem](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/TURNOVER-AND-CLOSURE.md) gives a broader prose argument for finite-type cycle necessity. The new mechanization retains its bounded-rank scope. A role/type cycle is different from a full-state return; distinct replacement tokens can form a forward causal lineage while their types recur and their environment changes.

## 6. Witnesses, counterexamples and limits

The formal package supplies an admitted consume/restore process to show that the accounting class is nonempty and compatible with indefinite provision-supported activity. That witness's restoration rule and input are supplied; it is not a costed derivation of the apparatus that repairs it.

The relevant failure boundaries are equally important:

| Stronger proposed inference | Why the stated conditions do not establish it |
|---|---|
| Infinitely many events require replenishment | Zero-demand events can continue indefinitely. The theorem requires unbounded cumulative demand or its positive-demand subclass. |
| Continually positive loss must exhaust a reserve | A positive real-valued loss can have finite total. Unbounded cumulative demand is the relevant condition. |
| Repeated provision guarantees continuation | Provision can be inadequate for the demanded rate, unavailable at a required prefix, or unusable by the necessary mechanism. |
| Few replenishments cannot support many events | One arbitrarily large receipt defeats a uniform frequency bound unless per-receipt credit is capped. |
| A finite lifetime always forces a type cycle | An infinite acyclic succession of new support types can continue while violating the bounded-rank premise. |
| A cycle guarantees self-maintenance | Availability, timing, gain, resources, startup and joint dependencies can still fail. |
| A renewed process must learn or widen concern | Renewal places no such requirement on its response or evaluation mechanism. |

The original [fixed-selector countermodel](../../../experiments/integrated-correction/general-framework/generative-basis/lean/BoundaryModels.lean) remains applicable. Recurrent functioning is not itself selection over selectors.

## 7. Verification, premise review and meaning of universality

The new [Lean package](../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/README.md) contains the exact statements, checker, frozen-source hashes and compiler logs. A fresh Lean 4.29.1 build passed **60 new theorem audits**: 21 accounting and composition results, 21 realization and boundary results, and 18 support results. It also rebuilt 18 inherited core audits. Of the 60 new audits, 34 report empty axiom dependencies; the other 26 depend only on Lean's standard `propext` and `Quot.sound`. There are no custom axioms or proof holes. Explicit model hypotheses and Lean's underlying logic remain; this is not an axiom-free account of existence. The [separate internal review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONDITIONAL-UNIVERSALITY-REVIEW.md) checks the interpretation, counterexamples and source-to-theorem correspondence. This is AI-assisted internal review, not human peer review or empirical validation.

The mathematics uses ordinary cumulative accounting, ranking and ancestry arguments. The advance is a checked, reusable connection from explicit local law properties to constraints on all admitted histories, with compatible representation maps and preserved support distinctions. It is not presented as a new physical law, proof that all reality is digital, or certification that these are the weakest possible assumptions.

The universal reading is therefore exact: **every process satisfying the displayed conditions obeys the corresponding conclusion, regardless of its implementation**. Evidence must establish the interpretation and adequacy of those conditions in a real system. The theory can cover both generative and degenerative histories because the law class permits adequate provision, insufficient provision, depletion and stopping.

## 8. Connection to the unified derivation

The shared foundation asks how activities alter the conditions of further activities. This development identifies a conditional necessity within that account: expenditure beyond inherited support requires actual provision, and bounded acyclic replacement dependencies impose a continuation deadline. Sensing, models, selectors and their reconstruction are subject to these constraints wherever their material implementations satisfy the same conditions.

These results do not insert a reward or preinstalled learner. They expose the support obligations that a proposed origin of learning must meet. The parallel concrete programme is forming competing response variants and carrying their differential retention through actual successor conditions; its later selector-revision mechanism must retain the same accounting discipline.

The next explanatory bridge remains the mechanism by which actual consequences change the generation, retention or evaluation of responses. Conditional universality will advance by proving additional cross-model consequences of such local couplings, while concrete constructions establish that the couplings can form and empirical identification establishes where they occur. Unique-ontology language is no longer the gate that this universal research programme has to pass.
