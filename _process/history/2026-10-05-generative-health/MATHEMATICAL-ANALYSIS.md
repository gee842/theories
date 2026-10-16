# Generative continuation through changing forms

Research candidate / internal mathematical analysis. Prepared 5 October 2026. This is a scoped derivation and conceptual diagnostic, not an established universal theory of health or a claim of theorem priority.

## 1. The answer that can presently be defended

A process can continue through changing forms when its activity repeatedly makes the capacities required for subsequent activity available, and when replacement or revision can be established before the currently indispensable capacities fail. Some capacities can be conserved, some renewed, some substituted, and some made unnecessary by changing the organization. The relevant continuity is functional and causal; the material carriers and organizational forms need not remain identical.

The distinctive generative question is whether the process can also establish changed ways of continuing, rather than merely reproduce the current arrangement. This requires paying transition costs while meeting whatever obligations remain in force during the transition. The construction below makes that requirement quantitative and shows why a system can be indefinitely viable yet have no capacity to establish a successor.

This statement does not make all self-renewing processes healthy. The functions and consequences being protected must be specified, including those of affected participants. A durable oppressive organization can satisfy a maintenance condition; a productive tumor can make more of its own capacities while damaging its host. The mathematical distinction between continuation and transformation does not by itself supply an ethical boundary.

## 2. What is invariant, what continues, and what becomes possible

Three objects should remain distinct:

1. **Invariance under a description change.** The root-foundation's attainable response-profile set is unchanged by a faithful translation preserving observations, interventions, uncertainty, policies, and retained consequences. This compares two descriptions of the same situation. It is not a quantity conserved as the situation changes.
2. **Viability under actual change.** A process remains within declared functional requirements while its capacities and surroundings change. This concerns a real trajectory or set of trajectories.
3. **Transformability.** From its actual present situation, a process can establish a different functioning arrangement through a feasible transition. The transition includes its information, material costs, time, permissions, and burdens.

Generativity can include creating new forms or capacities; viability can be achieved without doing so. Conversely, producing novelty need not preserve viable continuation. Unrestricted novelty and sustained plural futures are stronger claims than either property alone.

The existing [composition note](../2026-10-05-generative-foundation-review/final-synthesis/COMPOSITION-AND-SCOPE.md) already proves switching with establishment: if every actual transition from one certified mode arrives in the next mode's certified region, the union of those regions is invariant. It also explicitly charges handoff costs and delays. Repeating that proposition would not advance the inquiry. The following model calculates when one of its indispensable establishment premises is true.

## 3. A paid successor-establishment model

An incumbent organization supplies a service whenever its functioning capacity is at least a threshold. It must keep supplying that service until a successor is ready.

Let:

- `c(t)` be incumbent functioning capacity;
- `c_* > 0` be its required service floor;
- `u(t) in [0,1]` be the fraction of available effort allocated to incumbent maintenance;
- `alpha > 0` be incumbent renewal productivity;
- `delta > 0` be incumbent depreciation rate;
- `x(t)` be usable progress toward establishing a successor;
- `beta > 0` be successor-establishment productivity;
- `K > 0` be the progress required for a completed successor.

For measurable controls and absolutely continuous trajectories, suppose

\[
\dot c=\alpha u-\delta c,
\qquad
\dot x=\beta(1-u),
\qquad
c(0)=c_0\ge c_*,\quad x(0)=0.
\tag{G1}
\]

Require `c(t) >= c_*` throughout establishment. At `x=K`, the successor becomes functional. That last premise must be independently established in an application: `K` must include the necessary tools, competence, commissioning, permissions, and any required initial reserve. Renaming unfinished preparation as an installed successor would change the claim.

The model assumes construction progress does not decay or fail, the parameters are known, capacity can be observed, and effort has already been made available. These are strong simplifications. It does not obtain energy or material for free: effort stands for a specified externally supported work budget, whose further dependencies would have to be included if the scope covers them.

Define the maintenance fraction required at the floor and the time for the inherited reserve to run down without maintenance:

\[
p=\frac{\delta c_*}{\alpha},
\qquad
t_0=\frac{1}{\delta}\log\frac{c_0}{c_*}.
\tag{G2}
\]

Assume `p <= 1`, so the incumbent can be maintained indefinitely once it reaches its floor. Let `[r]_+ = max(r,0)`.

### Proposition G1: exact establishment frontier

The maximum successor progress attainable by time `T`, while the incumbent supplies continuous service, is

\[
X_{\max}(T)=\beta\left[\min(T,t_0)+(1-p)[T-t_0]_+\right].
\tag{G3}
\]

Consequently a successor requiring `K` can be established by deadline `T` if and only if

\[
K\le X_{\max}(T).
\tag{G4}
\]

An optimal establishment schedule is

\[
u^*(t)=
\begin{cases}
0,&t<t_0,\\
p,&t\ge t_0,
\end{cases}
\tag{G5}
\]

stopped when the successor is ready. Its incumbent trajectory is

\[
c^*(t)=\max\{c_*,c_0e^{-\delta t}\}.
\tag{G6}
\]

**Proof.** Nonnegative maintenance implies `c(t) >= c_0 exp(-delta t)` by the integrating-factor formula. The service constraint separately gives `c(t) >= c_*`. Thus every admissible incumbent trajectory lies pointwise above (G6), which schedule (G5) attains.

Integrating the incumbent equation gives

\[
\alpha\int_0^T u(t)\,dt
=c(T)-c_0+\delta\int_0^T c(t)\,dt.
\tag{G7}
\]

Both occurrences of `c` on the right have positive coefficients. Their simultaneous pointwise minimum is (G6); hence (G5) minimizes total maintenance effort. Since

\[
x(T)=\beta\left(T-\int_0^T u(t)\,dt\right),
\]

it maximizes establishment progress. It uses zero maintenance for the first `min(T,t_0)` units and fraction `p` afterward, proving (G3). Necessity of (G4) follows from maximality: any policy completing earlier can be extended in the incumbent model to time `T` with `u=1`, maintaining capacity above its floor because `p<=1`, and retaining its completed progress. For sufficiency, run (G5) until its continuous nondecreasing progress first reaches `K`. The incumbent has remained functional at every earlier instant. ∎

The schedule prioritizes current construction because maintaining a larger incumbent stock incurs more depreciation. This priority is a result of (G1), not a robust-policy recommendation: it deliberately consumes the incumbent's buffer and eventually operates exactly at the service floor. Unmodeled shocks can therefore invalidate its service claim. If construction progress depreciates, future demand requires a reserve margin, or maintenance yields learning, the optimal schedule can change. The theorem proves an available implementable schedule under its observation assumptions; actual adoption, retained authorization, and faithful execution are further conditions, not consequences of optimality.

### Corollary G1a: earliest completion

If `K/beta <= t_0`, the earliest completion time is `K/beta`. If `K/beta > t_0` and `p < 1`, it is

\[
T_{\min}=t_0+\frac{K/\beta-t_0}{1-p}.
\tag{G8}
\]

If `p=1`, a successor is establishable only when `K <= beta t_0`. No waiting policy can construct more than this inherited-reserve allowance.

### Corollary G1b: viability can exclude every nonzero successor

Set `c_0=c_*` and `alpha=delta c_*`. Then `p=1`, `t_0=0`, and `X_max(T)=0` for every `T`. The incumbent can function forever with `u=1`, but no positive successor project can ever be completed.

This is a concrete counterexample to the inference that persistent functioning entails preserved capacity to change. It does not rely on malign intent, poor information, or political capture: all available effort is structurally committed to keeping the present arrangement alive.

### Corollary G1c: strictly positive productive margin makes every finite project eventually feasible

When `p<1`, `X_max(T)` diverges with `T`. Every finite project `K` is eventually feasible under the model's assumptions. A deadline can still make it impossible. Greater intelligence or rescheduling cannot defeat (G4) without changing a modeled quantity or relaxing a requirement.

The two terms in (G3) identify two distinct ways to pay for change: a usable inherited reserve and a recurrent margin after maintenance. Recurrent margin is not universally necessary: an adequate reserve can fund a particular transition, and a successor can introduce a more productive renewal method. It is also not sufficient outside this model if missing information, permissions, parts, or coordination block establishment.

## 4. Checked numerical witnesses

For `alpha=2`, `delta=1`, `c_*=1`, `beta=1`, and `K=2`:

| Initial capacity | Maintenance fraction p | Initial reserve duration t_0 | Earliest completion |
|---|---:|---:|---:|
| 1 | 1/2 | 0 | 4 |
| e | 1/2 | 1 | 3 |

In the first row, the entire frontier is exactly `X_max(T)=T/2`.

At a deadline of `T=2.5`, the second case can construct only `1 + (1/2)(1.5) = 1.75`, so no admissible effort schedule can finish the project.

For `alpha=1`, `delta=1`, `c_*=1`, and `beta=1`, the incumbent is exactly maintainable but has no recurrent margin. Starting at `c_0=1` permits no construction at all. Starting at `c_0=e` permits at most one unit, regardless of the deadline. Initial prosperity can therefore conceal an inability to keep paying for transformation after its inherited allowance is exhausted.

These are exact substitutions, not observations about real organizations. The proof, rather than simulation, establishes the optimality and impossibility claims.

## 5. From a single handoff to changing forms

Let organizational modes be nodes in a directed graph. Each mode supplies declared protected functions. An edge from mode `i` to mode `j` exists only if there is an implementable establishment policy that:

1. maintains the obligations that remain in force throughout the handoff;
2. pays its resource, time, information, permission, and coordination costs;
3. arrives within mode `j`'s functioning region.

For a handoff satisfying (G1), equation (G4) determines whether this edge exists by a given deadline. A list of attractive successor designs does not establish any such edges.

The existing switching theorem then certifies any actual sequence of these paid transitions. This is an application of that theorem, not a new theorem. If elapsed times have a positive lower bound, an infinite sequence does not accumulate into finite time. More general nonaccumulation assumptions can replace that bound.

There is no free reset between handoffs. A successor's initial capacity, construction stock, control competence, and reserve must be delivered by the preceding paid transition or an explicitly counted external source. It is invalid to consume an inherited buffer, rename the organization, and initialize the same buffer again without a modeled production event. The graph discussion supplies no indefinite continuation claim unless all successive establishments satisfy this accounting, including the machinery that chooses and executes them.

Several distinctions become inspectable:

- A mode may be viable while having no outgoing establishment edge to a different mode.
- A feasible change may land in a viable mode from which no further revision is feasible.
- An organization may possess several feasible transitions while its installed decision or selection rule never allows them.
- A large collection of possible forms may still be fragile if every feasible transition depends on the same vulnerable resource or permission.

A strongly connected collection of functioning modes supplies one finite notion of revisability: each member can reach the others through safe paid handoffs. It is sufficient for that particular mutual-access property, not necessary for all desirable development, and not a proof of open-ended creativity. Alternating forever between two forms would satisfy recurrence without producing novelty. Desirable irreversible development can leave earlier modes inaccessible.

For a specified family of changed future requirements, the relevant stronger test is whether required responses remain attainable after change. It must respect actual information: the process cannot choose the correct successor according to a hidden circumstance it has no way to distinguish. No finite maintenance certificate guarantees response to wholly unrestricted future novelty.

## 6. Mechanisms that can carry the general answer

The mathematics and previous root results support a mechanism-level answer rather than a single universal conserved quantity:

- **Recurrent provision:** capacities subject to continuing loss receive sufficient timely replacement, substitution, or relief from the dependence. The root's turnover results make parts of this necessary under explicit assumptions.
- **Paid establishment:** a successor becomes functional before the capacities needed during its establishment fail. G1 calculates one exact resource-and-time boundary.
- **Consequential responsiveness:** where changed circumstances require changed responses, information reaches an executable correction process. This is additional to renewal: the root already gives persistent accurate and inaccurate renewal regimes.
- **Retention of the means of revision:** the actual process renews not only service production but the competence, evidence, permissions, and resources needed to establish altered service arrangements. Their maintenance and replacement cannot be assigned to an unmodeled permanent governor.
- **Compatibility across affected functions:** maintaining one actor's capacities does not imply maintaining the jointly protected functions of others. Shared-resource and burden constraints must be checked together.

These are operational questions, not a new universally minimal list of ontological dimensions. Particular domains can instantiate them with very different carriers. Some systems receive organizational renewal from outside their chosen boundary. Some functions need no active correction over the relevant horizon. Some justified transformations end a process rather than preserve it.

## 7. What this advances and what remains unresolved

The useful advance is a constructive distinction between *functioning indefinitely* and *being able to establish another way of functioning*. The minimal model supplies an exact frontier, an executable optimal policy, a deadline impossibility result, and a counterexample to equating viability with generative health. It explains a recognizable failure mode: current commitments can consume all the capacity required to make a different future possible.

This is an elementary optimal-control calculation assembled for the present inquiry. No novelty relative to the broader maintenance, replacement, or viability literature has been established. The inherited switching, turnover, information, and invariance results should be cited as already present in the project rather than counted again as new findings.

For a real application, `c`, `c_*`, `alpha`, `delta`, `beta`, `K`, and the deadline must be identified independently enough for the frontier to risk a false prediction. If every failure can be retrospectively called missing capacity, the statement becomes a vocabulary rather than an explanation. Useful validation would calibrate maintenance and construction separately, then predict an untested handoff deadline or a change in feasible successor set.

The most defensible condensed answer is therefore:

> A process sustains further becoming when it can repeatedly provide what continuing activity requires and establish changed arrangements before those requirements fail. Its current activity must leave or create enough real capacity for that establishment. The forms can change because continuity belongs to the supported functions and their causal handoffs, not necessarily to any one carrier. Calling this healthy additionally requires an account of which futures and affected beings the continuation serves.

The mathematical claim is conditional, and its ethical scope remains explicit. This analysis does not prove that reality as a whole must value continuation, that all possible futures can remain available, or that every persistent process is generatively healthy.
