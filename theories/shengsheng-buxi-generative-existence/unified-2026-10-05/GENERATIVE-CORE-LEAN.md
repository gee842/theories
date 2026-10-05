# A Lean-checked realization of the generative core

6 October 2026. Research directed by Yongxu Ren; formalization, exposition and internal review are AI-assisted. [Ren's request](../../../sources/15-codex-theory-conversations/2026-10-06-lean-generative-core-request.md) asks whether the candidate is complete at its core and whether Lean can prove its standing as a candidate. This development implements a precise part of the [governing foundation](GENERATIVE-GROUNDING.md), reusing the existing [generative-basis study](../../../experiments/integrated-correction/general-framework/generative-basis/README.md).

**Result:** the proposed causal core has an explicit nontrivial realization, general composition laws, a necessary-and-sufficient criterion for exact finite-path representation, and a conditional obstruction to indefinite continuation. These are mathematical grounds for a coherent formal candidate. They do not establish that the whole foundational derivation is complete.

## What completeness means in this result

The candidate says that activity changes the conditions of further activity, and those conditions shape subsequent activity. Its formal interface is:

```lean
structure Process (State : Type) (Action : Type) where
  step : State → Action → State → Prop
```

A state describes the conditions retained by the model. An action labels an event, intervention or activity. The relation states which actual successors are admitted. Mechanisms, resources, observations or selectors can occur within the state when they affect the declared transitions. They are not required to live in a separate meta-level. This is an interface for declared discrete dynamics; supplying the relation is not a derivation of its physical or historical origin.

`Enabled P s a` means there exists a successor of action `a` from `s`. `Trace P s word t` means the entire finite action word is realizable from `s` to `t`, through its actual intermediate states. `Feasible` means existence of such a path. These notions concern possibility. They do not yet mean a participant can observe, select, afford or guarantee that path unless those restrictions have already been faithfully represented.

The formalization deliberately does not declare a proposition named `Candidate` and then satisfy it by definition. It proves the following separate obligations and exhibits their limits.

## Exact representation has a complete local test

Let `P` be a concrete process, `Q` a proposed summarized process, and `q` its state-summary map. The central theorem is [local_exact_iff_trace_exact](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean):

\[
\begin{aligned}
&\forall s,a,u:\quad
 Q(q(s),a,u)\ \Longleftrightarrow\
 \exists t:\ P(s,a,t)\ \land\ q(t)=u\\
&\qquad\Longleftrightarrow\\
&\forall s,w,u:\quad
 \operatorname{Trace}_Q(q(s),w,u)\ \Longleftrightarrow\
 \exists t:\operatorname{Trace}_P(s,w,t)\ \land\ q(t)=u.
\end{aligned}
\]

In words: **exactly preserving projected one-step possibilities from every concrete starting state is necessary and sufficient for exactly preserving every finite action history and its projected endpoint.** The proof extends one-step preservation and realization along each finite word. Conversely, the history property applied to a one-action word gives the local property.

The words *every concrete starting state* matter. Combining outgoing edges found in different members of a summary class can invent a path that none of those members can actually execute. The lifting obligation prevents that reset. A second theorem proves that any summary preserving feasible words must distinguish two states whenever some word is feasible from one and impossible from the other.

The realization below instantiates both sides of that distinction. Adding a Boolean badge that changes on every event but does not affect the phase law gives a larger model; forgetting the badge satisfies the local criterion and therefore preserves every finite word and projected endpoint. Conversely, retaining only whether support is present merges depleted and revised states that permit different restoration histories. Lean proves that **no** process on this support-only summary can preserve all their feasible words. These are checked complete and incomplete summaries of the declared model, rather than an uninstantiated conditional criterion.

This is conditional representational completeness relative to the declared interface. It does not discover the correct state variables or transition law. It also does not certify observation-based policies, probabilities, timing, external outcomes not retained by `q`, or infinite behaviors. Such claims need additional preservation obligations. The earlier [probabilistic and structural notes](../../../experiments/integrated-correction/general-framework/generative-basis/formal/FORMAL.md) have broader contracts in prose; this Lean development does not claim to mechanize all of them.

## Composition and a substantive restriction

The [core](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean) proves that two paths compose precisely through a common actual intermediate state. A suffix must be possible from the state produced by the prefix. It also proves exact finite-path composition for a declared synchronous product: the same action word must satisfy both component relations. This product has no undeclared coupling; common resources, correlated events or interactions require a joint law that includes them.

[Depletion.lean](../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean) supplies a genuine limitation. If a natural-number reserve `r` strictly decreases on **every** admitted transition, then every trace obeys

\[
|w|+r(t)\le r(s).
\]

Consequently its length is bounded by the initial reserve, a nonempty return to the same state is impossible, and no infinite execution exists. The restriction is derived for arbitrary processes satisfying the displayed premise. Replenishment, a nonconsuming transition, or losses that are positive but summable in a real-valued reserve do not satisfy that premise. The theorem does not impose a universal scalar measure of generativity.

## A nontrivial realization under one law

[RootRealization.lean](../../../experiments/integrated-correction/general-framework/generative-basis/lean/RootRealization.lean) defines five phases and four event types. The phases are completely distinguished by two coordinates: whether current support is available and which operative rule setting is present. Lean checks that no further phase difference is needed by this encoding.

One initial use depletes the support and disables further use. A supplied revision is admitted only in the depleted phase. It leaves support absent but changes the rule setting; restoration becomes admissible exactly when support is absent and the rule is repair-capable, provided the external supply is present. Thus the setting affects future permissions rather than merely being an inert label.

From the same initial state under the same law, the file proves both:

- a path through revision and restoration to a nonempty renewal cycle, with a checked infinite supported trajectory;
- a path to terminal loss, after which no action or nonempty continuation is admitted.

The restoration step explicitly depends on continuing external provision. Without that provision it is disabled. The infinite trajectory is a possibility under that maintained input, not a guarantee over all paths or a closed finite-resource perpetual process. The revision rule, its available settings and restoration technology are supplied. There is no theorem here deriving a sensor, learning algorithm, concern or wisdom from depletion alone, and no costed origin of the revision apparatus.

## Checked boundaries

[BoundaryModels.lean](../../../experiments/integrated-correction/general-framework/generative-basis/lean/BoundaryModels.lean) establishes three independent finite countermodels:

1. Identical coarse observations can hide different action permissions; no classifier using only that observation can correctly recover both.
2. Each of two centers can individually receive a single resource while no one allocation serves both. Separate feasibility does not imply joint feasibility.
3. An operative selector can remain fixed throughout a nonconstant recurrent trajectory. Changing the selector would change the dynamics, but recurrence does not force that change.

These are boundaries of inference, not definitions of all information, learning or ethical value. In particular, recurring activity does not by itself establish revision of its selector.

## Verification and what remains open

The [reproduction instructions](../../../experiments/integrated-correction/general-framework/generative-basis/lean/README.md), [execution record](../../../experiments/integrated-correction/general-framework/generative-basis/lean/verification.json), source hashes and compiler logs retain the actual Lean check. The checker compiles frozen sources in a fresh temporary build with pinned Lean 4.29.1 and the standard library. It rejects incomplete proofs, custom axiom declarations and native decision shortcuts. Printed dependencies distinguish constructive proofs from proofs using standard Lean foundational axioms. The [internal review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/LEAN-CORE-REVIEW.md) checks the meaning of the claims separately from compilation. This is not independent human peer review.

The formal witness establishes satisfiability of these commitments relative to Lean's foundations. The exactness theorem settles the declared finite-path completeness question. Neither result establishes absolute consistency, unique minimality, empirical universality, or the explanatory completeness of the whole root.

**The remaining foundational gap is the origin of consequence-sensitive regulation and revisable learning.** Here a consequence-triggered rule change is representable and checked; its mechanism is still supplied. The next advance should derive such a mechanism under explicit material conditions, establish what consequences actually drive its retention or revision, and connect it to the existing learning and concern constructions without installing their unexplained capacities at the boundary. This directly advances the existing derivation map rather than replacing the governing goal with the completion of a transition-system library.

**Subsequent connection, 6 October 2026:** the [paid response-formation extension](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/ENDOGENOUS-REGULATION-LEAN.md) adds 32 checked theorem declarations for a concrete seven-event law. It proves trace equivalence with this root, then transports actual fuel budgets, a bootstrap obstruction and a response-formation witness through the same interface. A strictly decreasing rank bounds every physical event history in that finite-stock law. Its separate [CTMC implementation](../../../experiments/shared-renewal-capability/regulation/retention/README.md) checks consequence-coupled copying, source-dependent failure and resource tradeoffs. This supplies a concrete costed mechanism within the root; reaction chemistry remains a local input, and adaptive selection and revisable learning require further derivation.

**Further connection, 6 October 2026:** the [formed-variant package](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FORMED-VARIANT-SELECTION-LEAN.md) adds 53 audited declarations and another exact trace bridge to this root. It charges both competing variants' origins, proves a four-common-fuel requirement for the mixed restored-site state, and checks both useful copying and a paid inheritance counterpath. The separate expected-abundance comparisons remain outside Lean. This advances compatible formation-to-retention composition; the selection architecture is still a supplied local law.
