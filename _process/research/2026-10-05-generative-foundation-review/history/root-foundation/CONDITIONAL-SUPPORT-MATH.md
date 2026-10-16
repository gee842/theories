# Conditional necessity of renewed support: a checked deadline

**Status, 6 October 2026:** AI-assisted mathematical elaboration of Ren's request to establish necessary consequences for every reality satisfying explicit properties of its laws. The [Lean module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean) contains 18 audited declarations. All 18 compile under Lean 4.29.1 with empty reported axiom dependencies. The package's [verification record](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/verification.json) records the clean build and source hashes. This is a quantified natural-time support theorem, not an empirical identification of the laws of our universe.

## Connection addressed

The [turnover study](TURNOVER-AND-CLOSURE.md) proposed a finite deadline for an acyclic explanation of vulnerable support. This module formally establishes the deadline from actual episode-level local premises. It strengthens the root's representation of possible histories with a necessity result: under these laws, no function requiring a currently functioning support episode can continue indefinitely through a bounded hierarchy of exclusively vulnerable supports.

The supplied inputs remain the support roles, episode boundary, natural time coordinate, lifetime bounds, and causal parent relation. The theorem does not originate those inputs or derive learning, evaluation, or concern. Its contribution to the accepted derivation is to make one organizational dependency precise: continuation has a support obligation that cannot be met indefinitely by a bounded chain of nonrecurrent, finite-lived functional roles.

## Episode semantics and local premises

Let `Kind` be any type of functional support roles and `Episode` any type of functioning episodes. Neither type must be finite. There can be arbitrarily many copies or simultaneous births. For episode \(e\), write its role as \(k(e)\), birth as \(b(e)\), and expiry as \(x(e)\). All times are natural numbers. An episode is functioning at time \(t\) when

\[
b(e)\le t\le x(e).
\]

Expiry is inclusive. The assumptions are:

1. **Ordered lifetime.** \(b(e)\le x(e)\le b(e)+\tau_{k(e)}\), with the role-specific duration \(\tau_i\in\mathbb N\).
2. **Initial boundary.** Episodes inherited at the boundary start at zero. Their \(\tau_i\) bounds remaining functioning time from that boundary. Earlier prehistory is not reconstructed by this model.
3. **Actual live parent.** Every episode born after zero has an episode \(p\) with \(b(p)<b(e)\le x(p)\). Its role supplies a permitted support edge \(k(p)\to k(e)\). The earlier birth together with the expiry inequality makes the parent functioning at the child's actual birth.
4. **Coverage.** This parent requirement covers every positive-time birth of the episodes being explained. An externally introduced organized replacement or spontaneous formation lacking such a parent lies outside this premise. External energy and raw materials need not be excluded; their conversion into organized support still has to satisfy the stated parent law.

The formal conclusion concerns functioning episodes. To transfer its deadline to a separately specified organizational function, also establish that occurrence of that function requires at least one currently functioning episode from this model. That dependency is an application premise; an arbitrary function outside this interface is not bounded by the theorem.

The strict earlier-birth requirement excludes a mutually dependent batch whose members all first become functional at the same instant and have no earlier live parent. Such a model would require an explicit batch/event representation. Natural time already excludes an infinite descending sequence of birth times. We do not prove a real-time theorem by silently identifying real time with this coordinate.

The parent premise is causal and domain-specific. A recorded ancestor, a label of influence, or a person who originally issued an instruction is not sufficient. If an instruction remains effective through stored material, a continuing institutional role, or another carrier, that carrier must appear as the relevant functioning episode. If several parents are jointly required, selecting any actually required live parent gives the safe upper bound here; the theorem does not turn a necessary parent into a sufficient cause.

## The local-potential theorem

Suppose a function \(d:\mathrm{Kind}\to\mathbb N\) satisfies two independently checkable inequalities:

\[
\tau_i\le d_i,
\qquad
i\to j\Longrightarrow d_i+\tau_j\le d_j.
\tag{S1}
\]

Then every actual episode satisfies

\[
x(e)\le d_{k(e)}.
\tag{S2}
\]

Consequently, if episode \(e\) functions at \(t\), then \(t\le d_{k(e)}\).

**Proof.** Induct strongly on the actual birth time. An initial episode expires by its duration, hence by its type potential. For a positive-time birth, the parent has an earlier birth, so induction bounds its expiry by its own type potential. The child starts no later than this expiry and lasts at most its type duration. The edge inequality in (S1) bounds its expiry by the child's potential. No resetting, hypothetical parent substitution, or instantaneous type-level cycle is used. This is `expiry_le_potential`; `alive_le_potential` adds the functioning-time conclusion.

This is a local certificate with a global consequence. We supply lifetime bounds and inequalities on permitted support interfaces; we do not supply the assertion that all realized episodes end by the deadline. The latter is derived for every episode history satisfying the premises.

## A bounded-rank deadline

Assume a uniform duration bound \(\tau_i\le L\) and a strict support rank:

\[
i\to j\Longrightarrow r(i)<r(j).
\tag{S3}
\]

Then \(d_i=(r(i)+1)L\) satisfies (S1), yielding

\[
x(e)\le (r(k(e))+1)L.
\tag{S4}
\]

If all ranks lie in \(\{0,\ldots,n-1\}\), every functioning episode obeys the common deadline

\[
t\le nL.
\tag{S5}
\]

These results are `expiry_le_rank_deadline`, `alive_le_rank_deadline`, `bounded_rank_deadline`, and `no_alive_after_bounded_rank_deadline`. Without a common rank bound, `late_alive_requires_higher_rank` proves the precise residual claim:

\[
t>(q+1)L\quad\Longrightarrow\quad r(k(e))>q.
\tag{S6}
\]

Thus long continuation requires progressively higher rank under a strictly increasing hierarchy. Uniform finite-ranked coverage makes that impossible past a finite deadline. A finite type set with a supplied strict rank is one instance; finite episode counts are unnecessary.

The module also represents type edges as a `Generative.Process Kind Unit`. Along every type trace, rank grows by at least its number of edges. A nonempty trace returning to its starting role is consequently impossible (`strict_rank_bounds_type_trace`, `strict_rank_excludes_nonempty_type_cycle`). This proves that the rank certificate excludes cycles. **The converse finite-acyclic-graph-to-rank theorem and general finite-graph cycle extraction are not formalized in this module.** Accordingly, its checked conclusion is a deadline for rank-certified hierarchies, not an unconditional graph-cycle inference from observed persistence.

The potential theorem supports unequal lifetimes and can be sharper than (S5). For a role chain with durations 2, 3, and 5, potentials 2, 5, and 10 satisfy (S1). The final deadline is 10; using a common lifetime bound of 5 with three ranks gives the looser bound 15. These figures illustrate the general theorem rather than provide empirical estimates.

## Checked witnesses and failure boundaries

| Model | Declared local facts | Checked consequence |
|---|---|---|
| `renewing` | One role; episode \(e_n\) is born at \(n\), expires at \(n+2\), and has \(e_{n-1}\) as live parent for positive births. The permitted type edge is a self-loop. | An episode functions at every natural time; there is a nonempty type cycle; no strict type rank exists. |
| `finiteInitial` | Exactly the same permitted role self-loop, but only one initial episode, expiring at time 2. | The type cycle exists, yet nothing functions after time 2. A permitted cycle supplies neither actual renewal nor its success. |
| `infiniteChain` | Role \(n\) occurs in episode \(n\), lives from \(n\) through \(n+2\), and supplies role \(n+1\). Every episode has the required live parent. | Functioning at every natural time coexists with strictly increasing ranks and absence of any nonempty type cycle. The rank range is unbounded. |
| External arrivals | An episode arrives at each \(n\) and expires at \(n+2\); no internal support edge exists. | Functioning at every time and finite duration coexist, while the universal internal-parent premise fails. |

The recurrent witness assumes the declared conversion law and any resources it requires. It does not prove an energetically isolated perpetual process. The dying witness shows a particularly elementary insufficiency of a permitted cycle; it does not yet analyze the separate failures of resource competition, activation, conversion delays or simultaneous demands.

An immortal basal supplier falls outside any uniform finite lifetime bound. A birth credited merely to a long-dead ancestor falls outside the live-parent premise. Effective support carried by a durable stored intermediate must be included and bounded on its own terms. These omissions cannot be relabeled as renewal without changing the empirical claim.

## What this adds and what would change the account

The proposed law class now has an observable exclusion: after independent identification of \(n\), \(L\), and the parent/rank interfaces, functioning after \(nL\) rejects their conjunction. It does not by itself identify which premise failed. Candidate explanations include an omitted live supplier, longer-lived stored organization, external organized entry, a recurrent channel, or an unbounded sequence of new roles. The distinction matters for empirical work.

This is a universal conditional result because its proof ranges over arbitrary carriers and episode histories satisfying the assumptions. It establishes no priority for the elementary induction method. It formalizes the theoretical distinction between inherited functioning and conditions that can actually be reconstructed. Empty reported axiom dependencies mean that these checked declarations require no axioms beyond Lean's underlying proof rules; the displayed model premises remain explicit hypotheses.

The next foundational connection remains actual dependencies → formation and differential retention of responses → revision of selectors. The support theorem gives a precise necessity those mechanisms may need to satisfy. It does not select a successful mechanism, supply a reward, or establish that longer continuation is better for all affected centers. The model must still preserve whose support is sustained, whose capacities are depleted, and which mechanisms are produced by the actual history.
