# Independent audit: formalizing the proposed root

Prepared 5 October 2026. This audits the candidate in `outputs/root-of-wisdom-cross-session-assessment.md`; it does not claim that the candidate has become a necessary-and-sufficient definition of wisdom.

## Recommended mathematical object

Formalize a **capacity and its constraints**, rather than identifying wisdom with an optimization score or with whatever a revision operator approves.

A situated deliberative state can be written

\[
s=(L,H,\mathcal M,N,A,B,D).
\]

Here:

- `L` is the current representational language, including distinctions, represented beings, possible harms, and response descriptions.
- `H` is the accessible evidential history. Its interpretation remains contestable.
- `M` is a nonempty collection of empirical models admitted by current evidence and assumptions. It need not be a probability distribution.
- `N` is the explicitly avowed normative position: standing, reasons, protections, priorities, and unsettled conflicts. It need not be a total ordering or scalar utility.
- `A` is the set of presently available responses, including acting, refraining, seeking help, investigating, and stopping. Actual interventions and recommendations about unavailable interventions must be distinguished.
- `B` records relevant time, capacities, permissions, and material means.
- `D` is a retained record of claims, objections, consequences, commitments, and reasons for changes. Retention itself is bounded; the specification must say what a proposed preservation condition requires.

The proposed architecture has two mathematical parts:

\[
J(s)\subseteq A,\qquad \mathsf{Rev}\subseteq S\times X\times S.
\]

`J` is a judgment correspondence: currently defensible responses under the declared evidential and normative standards. It may contain multiple responses. It may be empty when standards conflict or no satisfactory response is available. Empty does not automatically mean the actor is unwise; naming an impossible demand can be a good judgment.

`Rev` is a revision relation responding to a challenge `x`. Challenges include observations, consequences, testimony, counterarguments, changed circumstances, and discovered alternatives. A relation is preferable to a purported universal update function: reasonable revisions may be nonunique and the theory does not yet supply an algorithm that generates all relevant challenges.

For actual executable policies, information consistency and resource constraints belong in the specification. For judgments about what ought to be done, record the distinction between a warranted recommendation and the agent's ability to realize it. Otherwise the account confuses wisdom with power.

### Mutual correction as a substantive structural condition

Draw dependencies from `N` to inquiry priorities and representation, from empirical findings to feasible ways of responding to concern, and from considered responses to further evidential and normative questions. A formal implementation should exhibit cases where changing each relevant input changes a warranted output, while holding the other declared inputs fixed. Merely drawing arrows or saying every component may change proves nothing.

A defensible revision should satisfy independently specified conditions appropriate to its kind:

1. Empirical claims remain answerable to accessible observations and stated intervention assumptions; the revision must not silently discard inconvenient observations.
2. Normative changes preserve the challenge and provide reasons that can be examined under both the old and new positions. This establishes traceability, not moral validity.
3. Changes of language or measures record what old distinctions lose representation and why. New language is permitted; exact translation is not universally possible.
4. Proposed conduct distinguishes unavailable means, unavoidable loss, and uncertainty from promised success.
5. The architecture permits settled judgment, urgent action, refusal, and stopping. Revision is a conditional capacity, not a required ritual on every occasion.

The ethical proposal of non-arbitrary consideration is an explicit normative axiom to defend. Neither the transition structure nor symmetry alone supplies it. In particular, formalize concern for beings unable to articulate or reciprocate claims; making voiced objection necessary would contradict the proposal's standing criterion.

## Proposition 1: empirical completeness and non-arbitrary consideration do not uniquely determine judgment

Take two affected beings and two responses with fully known benefit vectors:

\[
v(a)=(3,0),\qquad v(b)=(1,1).
\]

Consider these evaluative rules on nonnegative benefits:

\[
U_1(v)=v_1+v_2,\qquad U_2(v)=\sqrt{v_1}+\sqrt{v_2}.
\]

Both are invariant under exchanging the two beings' identities; both strictly increase when either being's benefit increases and the other is unchanged. Thus both meet these limited formal tests of non-arbitrary and positive consideration. Nevertheless,

\[
U_1(a)=3>2=U_1(b),\qquad U_2(a)=\sqrt3<2=U_2(b).
\]

**Conclusion.** The same complete factual description and these ethical symmetry/monotonicity constraints permit opposite judgments. Additional evaluative reasons or commitments are required. This is an elementary countermodel, not a claim that either rule is the correct morality or that all relevant goods are numerically commensurable.

The result blocks a central overclaim: making a model more complete cannot, by itself, turn the proposed root into a unique moral decision procedure. It also blocks using identity invariance as a sufficient definition of ethical concern.

## Proposition 2: a shared optimal response removes the instrumental value of a costly pure-information query

For this proposition only, take a finite current state set `W`, finite available action set `A`, a declared utility `u(a,w)`, and any probability distribution on `W`. Suppose one response `a*` satisfies

\[
\forall w\in W,\ \forall a\in A:\quad u(a^*,w)\geq u(a,w).
\]

A pure-information query supplies a signal `Y`; it changes neither the state, available responses, their consequences, nor the utility. After querying, the actor chooses any signal-contingent response `d(Y)` from `A`. The query incurs a fixed positive cost `c`, assessed in the same declared utility.

Pointwise, `u(d(Y),w) <= u(a*,w)`. Taking expectation over states and signals gives

\[
\mathbb E[u(d(Y),w)]-c
\leq \mathbb E[u(a^*,w)]-c
<\mathbb E[u(a^*,w)].
\]

**Conclusion.** Immediate `a*` strictly dominates every policy that first purchases such a query. With zero cost the query cannot improve the declared expected utility. The proof does not need the query to reveal the state correctly.

**Boundary.** This is conditional on the current possibility set and utility. The conclusion need not survive an omitted state, affected being, action, consequence, independent duty to inquire, or a query that changes what actions are possible. Hence it supports optional inquiry, not complacency about model adequacy. A more general comparison can use costs to each affected party and partial orders, but the simple theorem must not silently pretend to settle those conflicts.

## Additional failure modes the parent formalization should avoid

### Endogenous scores do not certify improvement

Suppose actual conduct remains unchanged and the evaluator is replaced by a rule assigning that conduct a higher score. The transition can satisfy any condition defined solely as an increase in the current self-selected score. Such progress is vacuous unless at least some consequences, claims, comparison standards, or revision reasons are preserved across the change. Preservation gives inspectability; it still cannot mathematically ensure the reasons are morally sufficient.

### Choice correctness does not identify wise capacity

If an agent has only one available response, every selection rule returns it. Wise and unwise agents can exhibit the same behavior, and the resulting outcome may be terrible. One successful or failed outcome therefore does not identify the relevant capacity. Evidence about a capacity requires reasoning and response across specified contrasts, while acknowledging that verbal explanations can also mislead.

### Closed representation cannot certify its own completeness

If an omitted distinction induces no difference in any accessible input to a deterministic deliberation process, the process produces the same output whether that distinction is present or absent. Randomization changes this to the same output distribution. Thus guaranteed discrimination of the two situations is impossible without an additional distinction-making channel or a response acceptable in both. This does not show that all missing possibilities are unknowable; it identifies the exact restriction under which a guarantee is impossible.

### Frozen meta-criteria and unrestricted self-revision each have a cost

A fixed higher-order acceptance rule leaves some commitments foundational. An unrestricted rule allowing the system to replace every standard can rationalize anything. A fallible practice can acknowledge this tradeoff by retaining objections, stating current commitments, allowing reasoned challenges, and leaving some disputes unresolved. It should not advertise that practice as an algorithm that escapes every normative assumption.

## Suggested claim strength

A justified initial claim is:

> We have formalized a family of situated, ethically committed, corrigible judgment processes and proved conditional constraints on some of their decisions. We hypothesize that their integration captures a practical root of wisdom.

A stronger claim—necessary and sufficient for wisdom in a declared domain—requires an independently specified target, evidence of discrimination from rival accounts, and boundary cases. A universal root is stronger still. These gaps do not make the formalization worthless; they locate what its mathematics does and does not establish.
