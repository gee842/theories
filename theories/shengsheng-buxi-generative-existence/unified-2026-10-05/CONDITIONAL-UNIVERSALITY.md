# Conditional universality: laws of what is held, enacted and arrives, and of support

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

- \(h(s)\): what is held available for further activity, or an independently justified nonnegative support certificate;
- \(e(s,a,t)\): what this event enacts;
- \(\alpha(s,a,t)\): what arrives during this event.

These names were adopted on 6 October 2026 at [Ren's direction](../../../sources/15-codex-theory-conversations/2026-10-07-market-names-and-continuation.md), replacing reserve, demand and credit, which carried an exchange picture. The three quantities are aspects of one continuing activity, not an owner's balance. The statements are unchanged.

The local law is

\[
\boxed{h(t)+e(s,a,t)\le h(s)+\alpha(s,a,t)}
\tag{U1}
\]

for **every admitted transition**: no event enacts more than was held plus what arrived, so nothing appears from nowhere. The inequality permits additional unrecorded losses. What is enacted and what arrives may depend on the actual source, event and successor. Events that enact nothing are allowed; the generic law does not equate change with enactment. In Lean the law is `SustainLaw`.

The quantities must use commensurate units within this one supporting quantity. Natural numbers define the checked discrete class. Application to continuous magnitudes needs justified discrete bounds or a separately proved ordered-number extension; it is not automatic rounding. A mathematical potential may also be valid, but then its interpretation as a certificate rather than a freely exchangeable material stock must remain explicit.

The law alone is deliberately permissive. Assigning zero to all quantities satisfies it for every process. Setting what is enacted equal to an invented arrival is equally uninformative. Its explanatory content comes from an independent account of what is consumed, what arrives, what remains usable and which quantities can become unbounded. The analyst's outcome score does not operate the mechanism or supply what arrives.

## 3. The universal prefix bound

For an actual finite history \(s_0\xrightarrow{a_0}s_1\cdots\xrightarrow{a_{n-1}}s_n\), define what is cumulatively enacted and what cumulatively arrives along those exact edges:

\[
E_n=\sum_{k<n}e(s_k,a_k,s_{k+1}),\qquad
\Lambda_n=\sum_{k<n}\alpha(s_k,a_k,s_{k+1}).
\]

Summing U1 gives

\[
\boxed{E_n+h(s_n)\le h(s_0)+\Lambda_n.}
\tag{U2}
\]

The Lean development proves this for actual supported traces and execution segments, retaining intermediate states. Every prefix obeys the same bound. An eventual total cannot repair an earlier violated prefix. Within-event ordering is only as detailed as the primitive process: if the order of enacting and arriving within an event matters, that event must be refined or its admissibility justified independently. U2 is a necessary constraint, not a proof that every numerically consistent event can occur.

Consequences include:

1. If what cumulatively arrives is bounded by \(B\), what is cumulatively enacted cannot exceed \(h(s_0)+B\).
2. If what is actually enacted is cumulatively unbounded, what actually arrives is cumulatively unbounded.
3. If every event enacts at least one unit, an \(n\)-event history requires \(n\le h(s_0)+\Lambda_n\).
4. If at most \(K\) units arrive in any one event, the count \(N_n\) of events in which something arrives satisfies \(n\le h(s_0)+K N_n\) in that positive-enactment subclass.
5. An infinite lawful execution in that subclass must have an event in which something arrives in every suffix window longer than what is held at the start of that window. Consequently such events occur arbitrarily late.

These are universal necessities for the law class. The existence of an infinite execution is a hypothesis when used, not a consequence. The law derives that continued enactment requires continued arrival; it has not yet identified whether what arrives is imported, internally produced, or a combination.

A family of supporting quantities indexed by support type satisfies U2 **coordinate by coordinate**. This does not require adding money, competence, information access and authority into one numerical value. If any indispensable coordinate fails its independently justified bound, the proposed joint history cannot meet all the stated conditions.

There is also a constructive counterpart. Supported histories concatenate through their actual shared boundary state, adding what is enacted, what arrives and arrival-event counts. If an executable history returns to its starting state, Lean proves that every finite number of repetitions is executable, with each total multiplied by the repetition count. For a nonempty cycle this permits arbitrarily long histories. What it enacts must be covered by what arrives. This is possible recurrence under the supplied transition law; it does not force a process to choose that cycle. A depleting external supplier must be included in the state or justified as an ongoing input, rather than hidden behind an apparent local return.

## 4. Transport across implementations

To apply the result, a concrete process may map into a simpler process through a state map \(q\) that preserves each concrete step as an admitted abstract step. Pull back what the abstract process holds, enacts and receives through \(q\). U1 then holds on the concrete process, so its histories inherit U2.

A forward step-preserving map suffices for this necessary bound; a two-way exact representation is stronger than needed here. The map must preserve the quantities and meanings used by the law. Merely assigning the same names to unrelated variables does not supply the bridge. This transport does not give a participant access to the mapped state, prove a policy implementable, or preserve probabilities.

The existing concrete regulation and variant studies can use this interface when what they enact, what arrives and their successors satisfy the law. Their particular chemistry remains a legitimate local input. The generic theorem imposes a common constraint without pretending that one specific chemistry governs every realization.

## 5. From arrival to support ancestry

The law of what is held, enacted and arrives cannot by itself prove internal repair or a renewal cycle. The separate support theorem identifies a law class in which continuing organization has a finite deadline if its production dependencies have bounded acyclic depth.

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

The formal package supplies an admitted consume/restore process to show that the law class is nonempty and compatible with indefinite activity sustained by what arrives. That witness's restoration rule and input are supplied; it is not a costed derivation of the apparatus that repairs it.

The relevant failure boundaries are equally important:

| Stronger proposed inference | Why the stated conditions do not establish it |
|---|---|
| Infinitely many events require replenishment | Events that enact nothing can continue indefinitely. The theorem requires unbounded cumulative enactment or its positive-enactment subclass. |
| Continually positive loss must exhaust what is held | A positive real-valued loss can have finite total. Unbounded cumulative enactment is the relevant condition. |
| Repeated arrival guarantees continuation | What arrives can be inadequate for the rate of enactment, unavailable at a required prefix, or unusable by the necessary mechanism. |
| Few replenishments cannot support many events | One arbitrarily large arrival defeats a uniform frequency bound unless what arrives per event is capped. |
| A finite lifetime always forces a type cycle | An infinite acyclic succession of new support types can continue while violating the bounded-rank premise. |
| A cycle guarantees self-maintenance | Availability, timing, gain, resources, startup and joint dependencies can still fail. |
| A renewed process must learn or widen concern | Renewal places no such requirement on its response or evaluation mechanism. |

The original [fixed-selector countermodel](../../../experiments/integrated-correction/general-framework/generative-basis/lean/BoundaryModels.lean) remains applicable. Recurrent functioning is not itself selection over selectors.

## 7. Verification, premise review and meaning of universality

The new [Lean package](../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/README.md) contains the exact statements, checker, frozen-source hashes and compiler logs. A fresh Lean 4.29.1 build passed **60 new theorem audits**: 21 accounting and composition results, 21 realization and boundary results, and 18 support results. It also rebuilt 18 inherited core audits. Of the 60 new audits, 34 first reported empty axiom dependencies and 26 depended on Lean's standard `propext` and `Quot.sound`. On 6 October 2026, following Ren's rule of no assumptions and no axioms, those 26 proofs were rewritten constructively; all 63 audits (60 plus three helper lemmas) are now empty. There are no custom axioms or proof holes. Explicit model hypotheses and Lean's underlying logic remain; this is not an axiom-free account of existence. The [separate internal review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONDITIONAL-UNIVERSALITY-REVIEW.md) checks the interpretation, counterexamples and source-to-theorem correspondence. This is AI-assisted internal review, not human peer review or empirical validation.

The mathematics uses ordinary cumulative-sum, ranking and ancestry arguments. The advance is a checked, reusable connection from explicit local law properties to constraints on all admitted histories, with compatible representation maps and preserved support distinctions. It is not presented as a new physical law, proof that all reality is digital, or certification that these are the weakest possible assumptions.

The universal reading is therefore exact: **every process satisfying the displayed conditions obeys the corresponding conclusion, regardless of its implementation**. Evidence must establish the interpretation and adequacy of those conditions in a real system. The theory can cover both generative and degenerative histories because the law class permits adequate provision, insufficient provision, depletion and stopping.

## 8. Connection to the unified derivation

**Checked continuation, 6 October 2026:** [the learning-interface extension](LEARNING-INTERFACE.md) now proves the sustaining laws for the actual formed-variant process, including its local capture requirement and spent-resource handoff. It also proves a general complete-feedback obstruction to incompatible next-response requirements and constructs a separately costed diagnostic witness. This connects the support theorem to an existing mechanism and an information-flow requirement; controller formation and revision remain open explanatory tasks.

The shared foundation asks how activities alter the conditions of further activities. This development identifies a conditional necessity within that account: enactment beyond what was inherited as held requires actual arrival, and bounded acyclic replacement dependencies impose a continuation deadline. Sensing, models, selectors and their reconstruction are subject to these constraints wherever their material implementations satisfy the same conditions.

These results do not insert a reward or preinstalled learner. They expose the support obligations that a proposed origin of learning must meet. The [parallel concrete programme](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FORMED-VARIANT-SELECTION-INTEGRATION.md) now joins formation of competing response variants to differential retention under one paid history. Its inheritance and access mechanisms remain supplied; deriving their formation and revision must retain the same accounting discipline. Applying the present general theorems to that construction still requires explicit interface proofs.

The next explanatory bridge remains the mechanism by which actual consequences change the generation, retention or evaluation of responses. Conditional universality will advance by proving additional cross-model consequences of such local couplings, while concrete constructions establish that the couplings can form and empirical identification establishes where they occur. Unique-ontology language is no longer the gate that this universal research programme has to pass.
