# Support inherited by formation and subsequent revision

**Status, 6 October 2026:** mathematical contribution and Lean formalization by Codex. This closes the resource-account interface between the existing paid formation law and the conditional continuation theorem. It adds a local access constraint and an actual continuation bound after formation. It supplies necessary conditions for a future joined learning mechanism; it does not assert that the formation process already learns.

The exact source is [FormationSupport.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/FormationSupport.lean). The package [README and verification record](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/README.md) accompany the controller interface study. The underlying process is the unchanged [FormedSelection.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean), connected exactly to the root by [FormationRoot.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/formal/FormationRoot.lean). The generic theorem comes from [ResourceContinuation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean).

## 1. The transition being addressed

The formed-variant study starts with no response variants and no repaired site. Its enabled event law charges for forming either response type, associating a resident, repairing the site and copying a resident or free template. Repair changes whether source capture is possible. Capture changes whether a local copy is possible. The law therefore provides actual state changes on which further development depends.

The present question is what support remains available after that development, under the **same state history**. A subsequent mechanism may not inherit the newly formed structure while receiving the original fuel and source again. This is an interface requirement for the planned derivation of revision of selectors.

We retain the supplied sixteen-event repertoire, integer stocks, Boolean local store, material bound and event guards. Only enabled events occur in this relation. Costs of attempted but rejected events, stochastic rates, physical energy units and external replenishment are not modeled by these theorems. No success measure, beneficial outcome or reward enters the account laws.

## 2. Four accounts of one process

For a state (s), let

\[
F(s)=\text{common fuel},\qquad
L(s)=\mathbf 1[\text{local fuel is stored}],\qquad
S(s)=\text{remaining source},
\]

and define usable reserve (U=F+L) and closed energy stock (E=F+L+S). The name `energy` is inherited from the discrete model: its units are the model's resource packets, not a measured thermodynamic quantity.

For event (a):

- (d(a)) is the existing expenditure count. Formation, association, repair, copying and leakage cost one. Capture, free/resident wear and site damage cost zero in this account.
- (c(a)=1) exactly for capture and is zero otherwise.
- \(\ell(a)=1\) exactly for a local copy of either type or a local leak.

For every permitted transition (s\xrightarrow{a}t), Lean derives from its guards and updates:

\[
\begin{aligned}
U(t)+d(a)&=U(s)+c(a),\\
L(t)+\ell(a)&=L(s)+c(a),\\
S(t)+c(a)&=S(s),\\
E(t)+d(a)&=E(s).
\end{aligned}
\]

These exact equalities imply four instances of `SustainLaw`. Capture is provision across the usable or local boundary and an equal withdrawal across the source boundary. It supplies no credit to the closed boundary. A repaired site makes a transfer possible; it does not create the transferred resource.

The concurrent [FormationAccounts.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/formal/FormationAccounts.lean) gives a boundary-indexed version of the usable, source, closed and common accounts, including exact trace equalities and a reaction/leakage split. The overlapping results concern the **same supplied event law** and are consistency checks, not independent empirical evidence. The additional work here is the local-store account, capture necessity, local-copy budget and explicit post-repair continuation.

## 3. The universal theorem applies to the actual histories

For any root trace (s\xrightarrow{w}t), `root_trace_account` constructs its `SupportTrace` with exact expenditure, provision and positive-credit-event totals. Every actual intermediate state is retained. Event-only weights are valid here because the concrete model defines these quantities by event; the generic theorem also accommodates state-dependent weights.

Applying `support_trace_bound` yields

\[
\begin{aligned}
\sum_w d+U(t)&\le U(s)+\sum_w c,\\
\sum_w \ell+L(t)&\le L(s)+\sum_w c,\\
\sum_w c+S(t)&\le S(s),\\
\sum_w d+E(t)&\le E(s).
\end{aligned}
\]

The local and source inequalities combine to give

\[
\sum_w\ell+L(t)+S(t)\le L(s)+S(s).
\]

Every local copy is one local expenditure, so **the total number of local copies of both types together is bounded by the initially stored local packet plus the initial source packets**. This bound does not include bulk copies, which consume common fuel through a different event channel. Having common fuel cannot bypass the local-copy guard.

If (L(s)=0) and \(\sum_w\ell>0\), `local_expenditure_requires_capture` proves that the actual word (w) contains a capture event. This is operational dependence on an enacted support transfer. Counting an outcome as desirable is unnecessary. Conversely, a sufficient numerical stock alone does not guarantee access: capture still requires the repaired site and an empty local store, while copying still requires an appropriate template and material capacity.

The budget is a necessary constraint on possible continuation. It is not an instruction implemented by the process to maximize this budget, and it is not a derived reward signal.

## 4. Formation does not reset the continuation budget

Given any actual combined trace

\[
s\xrightarrow{u\mathbin{+\!+}v}t,
\]

the exact trace decomposition produces an actual intermediate state (m) with

\[
s\xrightarrow{u}m\xrightarrow{v}t.
\]

`root_prefix_continuation_bound` then establishes

\[
\sum_v d+E(t)\le U(m)+S(m),\qquad
\sum_v c+S(t)\le S(m).
\]

These are bounds at the real handoff. They preserve the spent common fuel and depleted source from the prefix. A future observation, probe or revision law must be realized as actual events with an account compatible with this successor state before these existing formation results and the new controller results can be called one constructive mechanism.

## 5. The paid witness saturates the accounts

The existing mixed-formation witness executes

\[
\text{form H},\ \text{form A},\ \text{associate A},\ \text{repair},\
\text{capture},\ \text{local copy A}.
\]

It begins with (F=4,L=0,S=1). Its first four events form both variants, install A and repair the site, spending all four common units. Lean checks the actual handoff:

\[
U(m)=0,\qquad S(m)=1.
\]

The remaining capture and local-copy events spend the one accessible source packet. The same full history has demand 5, usable credit 1 and one credit-bearing event. It ends with (U=0,S=0), saturating (5=4+1).

`copied_cannot_pay_more` proves that every continuation from that actual final state has zero further expenditure and zero capture. Zero-demand damage or wear may still occur; zero expenditure does not imply there are no remaining events. The original formation model separately has a stronger decreasing-rank proof excluding an infinite event history under its closed finite-stock law.

A second checked boundary concerns cycles. If a root trace returns to its **complete starting state**, including the source and fuel stores, its expenditure and capture totals must both be zero. Thus a recurring site configuration with a depleted source is not an executable closed state cycle to which indefinite renewal may be attributed. Continuing provision requires an explicitly extended law or a larger supplied support account.

## 6. Formal status and next unresolved connection

The module contains **25 audited theorems**, including account derivations, generic trace transport, bounds, necessity, closed-cycle restrictions and the concrete witness. Compilation uses pinned Lean 4.29.1. Its reported dependencies are confined to the standard logical axioms `propext` and `Quot.sound`; there are no added axioms or proof holes. The final package checker rebuilds this module and its dependencies from frozen sources and records their hashes.

This supplies a concrete support interface for the learning study. Separately specifying an observation/update controller does not prove that the formation process implements it. The next constructive obligation is a continuing mechanism in which an actual consequence changes a physically retained selector, the selector alters later permitted responses, and every probe, construction and update inherits and consumes the actual support state. A model with only external scoring, replayed stocks or assumed successful identification would leave that obligation open.
