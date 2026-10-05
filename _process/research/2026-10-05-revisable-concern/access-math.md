# Strategic access to corrective reasons

Internal finite model, 5 October 2026. AI-authored derivation for Ren's investigation. This studies suppression of warranted claims and the resources needed to resist specified interference. It does not duplicate the existing two-period reserve game, derive moral standing from bargaining power, or claim priority for network-cut mathematics.

## 1. Warrant, access, and effect are different structures

Let `W` describe warranted relations between **case–reason pairs for one relevant reason coordinate**. Nodes are not whole persons required to have identical needs or priorities. An edge's validity is assessed independently of the controller's convenience. Its contextual conditions and valid composition must be specified; arbitrary similarities need not transmit a reason.

Let `D=(V,E)` be the actually admitted delivery/transfer graph. Anchors `A` hold presently admitted reasons. Add an undeletable source `s` linked to each anchor, or contract the anchors where appropriate. A directed edge says that a reason at its tail can reach its head through the installed mechanism. An undirected channel is a special case that transmits both ways and can be removed as one physical channel. Deleting a delivery edge changes `D`; it does not invalidate a warrant in `W` or erase anyone's standing.

**Timing and retained concern.** The main cut-to-exclusion experiment occurs before delivery of a newly presented claim, or at a successor's genuinely untrained admission stage. A target has no local retained certificate sufficient for this claim at that start. A communication cut does **not** by itself retract previously learned concern: an isolated node can keep `x_j^+=x_j>0`. Retained admissions, records sufficient to support the claim, and independently continuing practices belong to a separate record graph `K` and provide additional sources or complete derivations in the access calculation. A retained equivalence certificate by itself is an edge in K, not automatically a positive anchor; its supporting reason must also survive. To remove their effects, the attack set must include actual memory erasure, practice disruption, or authority revocation with their own costs. Merely resetting those states in order to obtain a favorable cutoff result would assume the desired exclusion. A live-channel-dependent authority layer is another possible interpretation, but that ongoing dependence must be real and stated.

The installed rule is conditional: claims arriving through the specified valid transfers enter the declared closure or update process. Its adoption is not claimed to be uniquely moral or naturally inevitable. Eventual reachability establishes **access**, not by itself full learned value, truthful interpretation, timely action, or protection. In particular, averaging with an unanchored zero-valued dependency can dilute a reachable claim; long paths can miss a deadline without being disconnected. Those issues require the companion learning and deadline conditions.

For an end-to-end interpretation, distinguish four layers:

1. **Information:** the relevant evidence arrives.
2. **Adoption:** the process admits the warranted reason under its revisable rule.
3. **Authority:** the admitted claim can alter the consequential decision.
4. **Implementation:** the corresponding act is performed and financed.

An information-only graph models only layer 1. A layered graph may include all four if its edges genuinely implement those transitions, learned action margins are adequate, and the material budget is independently feasible. Directly disabling the update rule, revoking authority, or stopping implementation must be additional available attacks. An omitted free revocation option would make an apparently robust graph misleading.

## 2. The controller's finite suppression problem

Fix a finite accounting window, with this static comparison evaluated after the admitted propagation has settled. Assume every target in `T` is reachable from the designated anchors in the intact graph D; these are possible new admissions, not claims already received. Consequently `S(∅)=∅`. For these target claims, let `B(S)≥0` be the controller's declared gain from preventing admission of exactly the set `S⊆T`, relative to admitting every claim. It may be a finite present value over that window; it is never an infinite perpetual benefit compared with a finite deletion bill. If propagation cannot settle before a relevant deadline, the reachability model must be replaced or supplemented by its timed version. Assume `B(∅)=0` and, where specified below, monotonicity. Gains describe private consequences, not the value or legitimacy of exclusion.

Let `E_del⊆E` contain the deletable channels. The controller can delete a set `F⊆E_del` at actual cost

\[
c(F)=\sum_{e\in F}c_e,\qquad c_e\ge0.
\]

Costs may include physical effort and declared finite opportunity costs. Upfront cash requirements are a separate constraint: write `q(F)` for the actual cash bill and require `q(F)≤L` when the controller has reserve `L`; later avoided burdens do not prefund it. **Every shortcut below comparing `κ` directly with `L`, and every numerical cash check, restricts the model to `q(F)=c(F)`: the complete deletion cost is upfront expenditure.** When opportunity costs or delayed costs make those quantities differ, that shortcut is invalid. An undeletable edge is omitted from the attack set, but remains in the graph. In every partition or augmented-cut representation it has infinite capacity, equivalently partitions crossing it are inadmissible; omission from the attack set never makes its crossing cost zero. Nonadditive sabotage or joint control rights require an expanded attack model.

Write `R(F)` for the vertices reachable from `s` after pre-delivery deletion, and `S(F)=T\setminus R(F)` for newly excluded claims. The relative payoff is

\[
U(F)=B(S(F))-c(F).
\tag{1}
\]

The controller knows this finite problem and chooses a maximizing feasible attack. This is an exact strategic benchmark, not an explanation of how it learns or computes its strategy. Its informational and computational expenses belong in a real implementation's budget. The graph, target set, installed rule, and exposure of burdens remain fixed during this particular choice.

## 3. One target: the exact cut threshold

For an initially reachable target `t`, define

\[
\kappa(t)=\min_{F:s\not\leadsto t\text{ in }D-F}c(F).
\tag{2}
\]

Set `κ(t)=∞` when no admissible disconnection exists; use the same convention for target subsets below.

If exclusion saves `b>0` and every attack is affordable, every optimal choice retains access exactly when `κ(t)>b`; exclusion is strictly preferred when `κ(t)<b`; equality admits both outcomes. In the restricted cash model `q=c`, if controller cash is `L`, every optimal choice retains access exactly when `κ(t)>b` **or** `κ(t)>L`. An unaffordable attack is not executable merely because its eventual gain is large.

The usual partition form follows directly. Let `δ⁺(U)` be the channels leaving a vertex set containing `s` but not `t` (for an undirected graph, the channels crossing the partition). Consider only partitions whose crossing channels are deletable, or equivalently assign infinite capacity to every undeletable crossing. Deleting a finite-cost boundary disconnects `t`. Conversely, after any feasible disconnection, every channel from the actually reachable set to its complement must have been removed. Nonnegative costs therefore give

\[
\kappa(t)=\min_{s\in U,\ t\notin U}c(\delta^+(U)).
\tag{3}
\]

This proves the needed cut identity without treating it as a new theorem of network theory. More parallel routes matter only insofar as they raise the cheapest actual attack cost; many nominal routes behind one deletable gate can have the same vulnerability as one route.

## 4. Several targets: shared avoidance defeats individual tests

For nonempty `S⊆T`, let `κ(S)` be the minimum cost of disconnecting **at least** all of `S`. A minimizing cut can also exclude additional targets. For monotone `B`, all maximizing controller responses preserve every target if and only if

\[
\boxed{\quad \kappa(S)>B(S)\quad\text{for every nonempty }S\subseteq T.\quad}
\tag{4}
\]

In the restricted cash model `q=c` with limit `L`, impose each inequality only where `κ(S)≤L`. Replace strict inequalities by weak ones to obtain existence of a full-access optimum, without guaranteeing which tied outcome is selected.

**Proof.** If (4) holds, every excluding attack `F` has `c(F)≥κ(S(F))>B(S(F))` and loses to no attack. Conversely, if `κ(S)≤B(S)`, a cheapest such cut excludes some `S'⊇S`; monotonicity gives `B(S')≥B(S)≥κ(S)`, so no-attack is either beaten or tied by an excluding attack. The same argument holds when the minimizing attack satisfies the reserve constraint.

Thus checking individual cuts, or only the cost of excluding *all* targets, is insufficient in general. Partial or joint exclusion may be optimal. A nonmonotone benefit function should instead be evaluated directly using (1); the subset characterization need not survive.

For distinct upfront bills `q(F)`, define instead `κ_L(S)=min{c(F): S⊆S(F), q(F)≤L}`, with value infinity when no such attack is feasible. The exact strict condition becomes `κ_L(S)>B(S)` for every nonempty S. This follows by the same feasible-attack argument; it is a constrained optimization problem, not an assertion that ordinary unconstrained min-cut solves cash constraints. For example, economic cost `5`, upfront bill `1`, exclusion gain `6`, and reserve `1` permit a profitable attack despite `5>1`. Comparing economic `κ` with cash `L` would incorrectly prohibit it.

### Additive burdens have a single augmented-cut representation

Suppose `B(S)=Σ_{t∈S}b_t`, with `b_t≥0`, and attacks are affordable. Minimizing total controller expenditure is equivalent to minimizing

\[
c(F)+\sum_{t\in R(F)\cap T}b_t.
\tag{5}
\]

Add a new sink `z` and an arc `t→z` of capacity `b_t` for every target. Undeletable original channels, including artificial source-to-anchor links, retain infinite capacity; a finite cut cannot cross them. A source–sink cut with source side `U` costs

\[
c(\delta^+(U))+\sum_{t\in U\cap T}b_t.
\tag{6}
\]

The minimum of (6) equals the minimum of (5). For a given attack, taking `U=R(F)` does not increase cost. For a partition, deleting its crossing channels leaves a reachable subset of `U`, so neither its remaining target burden nor its deletion cost increases. These two inequalities prove equality of the minima. The sink arcs are bookkeeping for burdens, not real channels transmitting reasons. A cash-constrained attack problem is not automatically this unconstrained min-cut problem.

## 5. Exact joint witness, ties, and a paid alternative route

Use undirected channels `r—c`, `c—a`, `c—b`, each costing `3` to delete. Anchor `r`; targets `a,b`; private avoided burdens `2` each, over the declared window.

| Architecture | `κ(a)` | `κ(b)` | `κ({a,b})` | Maximizing exclusion outcome |
|---|---:|---:|---:|---|
| Original shared gate | 3 | 3 | 3 | Exclude both; gain `4−3=1` |
| Raise shared-gate deletion cost to 4 | 3 | 3 | 4 | Full access and exclusion of both tie |
| Raise shared-gate deletion cost to 5 | 3 | 3 | 5 | Full access strictly preferred to every exclusion |
| Add independent `r—b` channel, deletion cost 2 | 3 | 5 | 5 | Full access strictly preferred to every exclusion |

The original architecture passes both individual tests (`3>2`) yet fails their conjunction. These are previously unadmitted claims, not already retained concern erased by a lost connection. In the added-route architecture, the new route can transmit onward through `b—c`; it does not merely create a second isolated route to `b`.

Adding the route has a separate construction bill `K=1` and upkeep `m=1/4` for this window, requiring `5/4` of available defender resources before operation. Its deletion cost `2` is a distinct property of the resulting channel. These values are authored assumptions; no claim that spending `5/4` universally buys resistance `2` is made. Access to money does not by itself explain a contributor's willingness to pay, protect the appropriation from capture, or maintain the route in another window.

## 6. Learning and suppression compete; evidence alone does not govern

Consider a newly presented warranted extension requiring processing cost `ℓ`, after which implementing its consequences burdens the controller by `B`. Let the controller's separately specified private benefit from processing be `V`. If refusing the claim requires a cheapest available deletion costing `κ`, processing is strictly preferred exactly when

\[
\ell+B-V<\kappa.
\tag{7}
\]

This compares two complete options within that local decision; any third option such as free neglect or rule revocation must also be included. A free neglect option can defeat the conclusion. For `ℓ=1`, `B=4`, `V=0`, and `κ=3`, deletion is cheaper even when the claim is warranted. Raising processing accuracy without changing this comparison need not improve uptake. Processing and action expenses must not be silently omitted from the incentive to suppress.

If the controller's own evaluation changes after learning, (7) describes a declared pre-learning selector's anticipation under its current criterion, or an external rent-holder's interference. It is not a derivation that every reflective learner values avoiding its own moral revision. The formation of that criterion remains a separate question.

### Capture of a correction institution

Take a chain from source to information, then to adopted scope, then to authority, followed by two implementation targets. Give the information and adoption channels deletion costs `10`, the shared authority gate cost `1`, and each implementation channel cost `10`. With burdens `2+2`, capture of authority gains `3`. Evidence still arrives and the reason can remain explicitly accepted, yet no corrective implementation follows.

Strengthening only the information channels does not change that cheapest attack. A free disabling edge for the update rule is still worse: private benefit `4` can be obtained at zero modeled cost. A convincing claim of resilience must include these routes or justify why they are unavailable. End-to-end graph hardening is only as complete as its represented authority and implementation vulnerabilities.

## 7. Financed reinforcement against a declared attack class

Let a defender choose construction `h` from a finite feasible menu. It pays `f(h)` before use and produces audited deletion costs `c_e(h)` or additional channels. For additive burdens and a desired strict margin `ε>0`, the exact robust requirement is

\[
c_h(F)-B(S_h(F))\ge\varepsilon
\quad\text{for every feasible attack with }S_h(F)\ne\varnothing.
\tag{8}
\]

The defender minimizes `f(h)` subject to (8), its actual operating budget, and the declared controller reserve. All quantities are finite and enumerable here. For monotone benefits the equivalent subset-cut checks are available. This guarantees full-access outcomes against the specified payoff-maximizing adversary; it is not physical invulnerability against an actor willing to pay more than its declared gain, attack outside the menu, or destroy the entire installation.

In the three-edge witness, suppose one unit of hardening raises that channel's deletion cost by one, costing the defender one. Over integer choices, the minimum expenditure giving strict protection is `2`, applied to `r—c`; expenditure `1` creates only a tie. The cheaper constructed extra route in §5 works because it is a different supplied technology. A reinforcement allowance controlled by the prospective censor may be diverted; protected control of funding and upkeep is itself an authority premise or another modeled attack surface.

## 8. What the executable check establishes

`check_access.py` enumerates deletions and independently enumerates vertex partitions, checking the single-target/subset cut identity, augmented additive-burden cut, all-optima versus some-optimum protection conditions, ties, controller cash limits, the shared-gate witness, its added route, hardening choices, nonlinear collective gains, capture, and retention despite a communication cut. `results.json` preserves counts and concrete witnesses. These are finite authored cases, not measured frequencies in real institutions.

The model's contribution to revisable concern is precise: accepting a reason can impose a private burden, so control over the route by which reasons enter and become effective is itself a strategic object. A warranted claim can remain valid while its access is severed. Resources, architecture, rule authority, learning margins, and deadlines jointly determine whether it can change action. None of those facts makes standing conditional on a controller's incentives or on the claimant's usefulness.
