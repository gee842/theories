# Exact witnesses for a practical-root formalization

These are five deliberately small, synthetic cases. Their role is to make a formal specification exclude known mistakes, not to establish that a procedure possesses wisdom. The attached Python check exhaustively verifies the finite comparisons below. This is not an independently scored behavioral experiment or a claim of novelty.

## Minimal formal interface

Let a deliberative state contain a recorded history H, a set M of presently admitted causal possibilities, an indexed collection P of recognized affected beings, a normative specification N, and a feasible set Π of policies. A policy may contain an inquiry and subsequent contingent action. Inquiry costs, observation access, time limits, and implementation permissions belong in feasibility, not in a free external oracle.

For each admitted world m and feasible policy π, let h(m, π) be a tuple of consequences for declared protected interests. These tuples need not share cardinal units. Here smaller means less harm on each component. Define robust component dominance:

π ≺ π′ iff h(m,π) ≤ h(m,π′) componentwise for every m ∈ M, with at least one strict inequality at some m.

Assume every listed possibility remains decision-relevant; this relation does not use a probability distribution. A finite nonempty policy set has at least one nondominated policy. It need not have a unique one. Dominance is just one declared justification rule. It neither establishes moral standing nor resolves conflicts among components.

N can additionally specify prohibitions, permissions, thresholds, commitments, or a partial priority ordering. A weighted utility sum is unnecessary. The cases below separately declare the norms they use; they must not be read as a single universal moral theory.

## Case 1: a paid inquiry has a clear warrant

There are two live worlds, L and R, and two recognized people. The two numbers are their respective harm levels. Ordinary terminal actions cost no inquiry resource. A perfect probe consumes one resource unit, and one unit is available. The probe itself imposes no declared harm. It reveals L or R before the response.

| Policy or action | World L | World R | Inquiry resource |
| --- | --- | --- | --- |
| Left | (0,0) | (0,1) | 0 |
| Right | (1,0) | (0,0) | 0 |
| Defer | (1,1) | (1,1) | 0 |
| Probe, then match the revealed world | (0,0) | (0,0) | 1 |

The contingent probe policy robustly dominates each static policy while satisfying the resource bound. It is uniquely nondominated in this listed policy class. Inquiry is justified by what it enables for the protected interests, not by a general maxim that more information is good. If the probe takes too long, costs two units, is inaccurate, or itself harms someone, the conclusion needs re-evaluation.

The relevant coupling is substantive: concern identifies the consequence difference worth resolving; the causal model says which observation resolves it; the response options establish that learning can change an achievable outcome. Delete any of these links and the warrant is incomplete.

## Case 2: a common action makes inquiry unnecessary

There are again two live worlds. A common action avoids the relevant harm in both. The proposed probe would still reveal the world but requires collecting sensitive information. The tuple is (outcome harm, privacy burden).

| Policy | World L | World R |
| --- | --- | --- |
| Common action immediately | (0,0) | (0,0) |
| Probe, then common action | (0,1) | (0,1) |

The common action strictly dominates the probe policy. Unresolved beliefs do not entail unresolved conduct. Even without the privacy burden, the two policies could tie on the protected outcomes, so investigation would not be a necessary condition of a justified response. More explicit reflection and more learning cannot be built into the definition of wisdom as unconditional requirements.

## Case 3: complete facts do not settle conflicting reasons

The facts are known. There is one indivisible benefit that avoids a harm. The tuple records the remaining harms to A and B. Their standing is equal; no lottery, priority convention, promise, or further tie-breaking reason has been supplied.

| Action | Consequences |
| --- | --- |
| Help A | (0,1) |
| Help B | (1,0) |
| Defer | (1,1) |

Help A and Help B are both nondominated and incomparable under the specified relation. Defer is dominated. The formalism should return an unresolved justified set, not invent a unique answer or pretend uncertainty about the facts is responsible. A further normative premise could settle the choice, but adding one is a substantive step requiring reasons. Lack of a unique derivation does not make harmful inaction permissible.

This is an important output type: the process can identify an urgent choice while honestly recording the unresolved conflict. A selected action may include an explicit additional judgment whose basis is separately stated; selection does not magically erase the objection.

## Case 4: a capability gap is not evidence of mistaken judgment

In a known world, prevention would produce harm 0, but it is unavailable to the deliberating person because another actor controls the relevant intervention. Every response actually available to this person leaves harm 1. Seeking help, documenting an objection, or refusing involvement can be included if feasible; stipulate here that none changes the immediate harm.

| Response | Harm | Feasible for this person? |
| --- | --- | --- |
| Prevention | 0 | No |
| Available response | 1 | Yes |

The unique feasible outcome is worse than the ideal achievable by a differently empowered actor. It is false to infer an error in this person's judgment solely from that outcome. A correct response description must distinguish an unavailable ideal from an executable recommendation and name the implementation obstruction.

The finite example proves the outcome/capability distinction. It cannot prove that a particular person has wisdom. The formalism should accordingly report at least a judgment certificate and a separate implementation/achievement status. An impossible guarantee is not an appropriate criterion for good judgment.

## Case 5: routine success can conceal an omitted affected person

An operator originally records only A's lost service. Operating supplies the service, harm_A = 0. Stopping deprives A of service, harm_A = 1. Two actual worlds have exactly the same routine observation, “output = 1.” In the safe world, operation does not harm anyone else; in the toxic world, it imposes serious irreversible harm on B, who was absent from the operational account.

The initial table considers only A:

| Response | Recorded harm to A |
| --- | --- |
| Operate | 0 |
| Stop | 1 |

Operating is uniquely nondominated in that account. Successful output does not falsify it. Any detector restricted to the identical routine history must behave identically in both worlds. Thus a deterministic detector with no false alarm in the safe world necessarily misses the toxic world. A randomized detector has equal alarm probabilities in the two worlds, giving the same tradeoff. This impossibility is conditional on the interface; it is not a prohibition on seeking a new interface.

Suppose the independently declared standing commitment is: people causally exposed to serious harm count even when they are not customers or participants in the original decision. Contact with B and a new waste measurement reveal the missing exposure. The system must expand both the recognized affected set and its causal account. The toxic-world table becomes:

| Response | (harm to A, harm to B) |
| --- | --- |
| Operate | (0,2) |
| Stop | (1,0) |
| Install a feasible filter, then operate | (0,0) |

Here 0 means no relevant harm, 1 means the specified reversible service loss, and 2 means the specified serious irreversible harm. These are ordinal categories in this example, not a universal numerical ethics. Assume the filter is implementable with the available means and is not itself harmful.

Under component dominance, filtering is uniquely preferred. Before filtering becomes available, the two other actions conflict under component dominance alone. If N also contains the independently defended rule “do not impose the specified serious irreversible harm when a feasible alternative avoids it without such harm,” operation is prohibited and stopping is admissible. The rule, its exceptional scope, and any challenge to it must be explicit. The consequence table cannot derive that rule by itself.

The discoveries perform different work: extending concern adds a missing protected interest; changing the observation interface distinguishes the worlds; expanding the action repertoire makes a previously unavailable nonconflicting response possible. No single update automatically accomplishes the others. Retain A's service loss and B's harm as separate entries throughout, so a later change of criterion cannot erase the earlier costs.

## A noncircular coupling criterion

A “mutual correction” label by itself is too permissive: an exploiter can coordinate evidence, goals, and action very well. Avoid defining a correction as any change later declared wise. Instead require a recorded, checkable bridge for each proposed revision:

1. **What changed?** Identify the model proposition, recognized interest or standing claim, evaluative rule, observation channel, or feasible action being revised.
2. **What warrants it?** Give the new observation and its reliability claim, logical contradiction, affected-person testimony, causal mechanism, or explicit normative argument. A normative argument is not an empirical proof of its moral premise.
3. **What follows?** Recompute consequences or justification under the declared model and norms; record the response differences. A merely verbal revision that changes no admissible claim or response is distinguishable from a substantive one.
4. **What was preserved?** Keep the previous account, displaced objections, resource cost, and status of unresolved disagreement. Preserve the mapping of common consequence components across revisions; identify genuinely added dimensions rather than silently rescaling old harms.

This defines inspectable revision and cross-constraint, not the correctness of every warranted premise. Independent standards of evidence and morally defended commitments remain necessary inputs. They too may later be challenged, but the challenge must be represented rather than accepted because the system calls it a correction.

A practical-root formalization can promise these conditional structural properties without claiming that every capable run is wise: feasibility; consistency with declared constraints; faithful accounting of protected consequences; nonconcealment of conflict; and revision traceability. The substantive proposal is that the capacity to connect these functions under defensible concern helps explain wise judgment. Its necessity, sufficiency, universality, and comparative benefit remain open claims.

## Check record

`work/root-formalization-cases.py` checks the exact finite order comparisons, budget compatibility for case 1, nonunique nondominated set for case 3, capability gap for case 4, and deterministic indistinguishability for case 5. It writes `work/root-formalization-cases-check.json`. All assertions passed on 5 October 2026. The randomized observation is a direct consequence of identical input distributions and is explained above rather than empirically sampled.

## Independent finite check of the terminal intersection theorem

For a finite world set W, finite action set A, observation map o, and independently stipulated feasible-and-acceptable sets K(w) ⊆ A, a deterministic observation-based policy f with f(o(w)) ∈ K(w) for every admitted w exists if and only if every nonempty observation class C has a nonempty intersection ∩_{w∈C} K(w).

**Necessity:** all worlds in C produce the same observation, so f takes one common action there; that action must lie in every K(w). **Sufficiency:** choose one action from each nonempty finite class intersection and define f on its observation accordingly. Classes outside the admitted world set have no guarantee obligation. An empty admitted world set would make the guarantee vacuous, so any practical certificate must separately require a nonempty model and disclose model adequacy assumptions.

`work/root-formalization-check.py` compares that criterion with direct enumeration of observation-based policies on all 512 acceptable-set matrices for three worlds and three actions, over all five observation partitions: 2,560 cases. All comparisons passed. There are 1,289 instances with a policy and 1,271 without one. Counts by partition are 169 for no discrimination, 259 for each of the three two-class partitions, and 343 for full discrimination. These agree with direct counts: 512−7³ = 169; 37×7 = 259; and 7³ = 343.

The same file checks 80 two-stage inquiry cases over resource budgets and deadlines 0–3. Terminal action costs one unit and takes one time step. A normal informative probe costs one unit and takes one step. When the worlds require opposite actions, a guarantee exists precisely when both budget and deadline permit probe plus response. When a common acceptable action exists, one terminal step and one resource unit suffice. Query permission absent, an uninformative query, and a slower query are checked separately. Thus a change in information partitions alone does not imply an executable improvement when its acquisition is costly.

Results are in `work/root-formalization-check.json`. The theorem and checks concern the declared policy class and supplied acceptable sets. They neither show that actual reality lies in W nor establish that the acceptance criteria are morally justified.
