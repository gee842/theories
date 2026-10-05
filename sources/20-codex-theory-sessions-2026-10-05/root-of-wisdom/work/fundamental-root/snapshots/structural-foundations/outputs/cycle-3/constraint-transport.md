# Constraint transport across changes of scale and organization

Cycle 3 mathematical memo, 5 October 2026. The question is how the same conditional constraints can apply across scales while the outcomes differ. This memo extends the [first formal core](../formal-foundations.md) and [second-cycle results](../cycle-2/synthesis.md). It supplies a sufficient cross-scale policy-transport theorem, its composition rule, and counterexamples locating the required assumptions. The arguments specialize established refinement and control reasoning; no mathematical originality or empirical universality is claimed.

## 1. The unified object is a constrained control problem

At scale `s`, specify

`M_s = (Q_s, A_s, W_s, F_s, I_s, Π_s; ledger_s, clock_s)`.

Configurations include whichever physical carriers, relations, rules, representations, and actual controller memory the model needs. Actions are attempted operations; input and outcome choices belong to specified actors or the environment. `I_s` is the currently usable decision interface, not the analyst's state. `Π_s` contains implementable controllers with declared memory, communication, representation, and institutional restrictions. Financial and physical stocks retain their own units; permissions and information distinctions do not become conserved quantities.

Event order belongs to this object. An environmental event revealed before control can be handled by an environment node followed by a decision node. A hidden disturbance cannot be turned into such an observable branch. History-dependent disturbance restrictions, such as minimum fault spacing, must be represented in the state or otherwise carried into every transport argument. The results below use the declared adversarial transition paths; unstated fairness assumptions are not supplied.

A **test** specifies an initial uncertainty set, a protected condition, a target or recurring duty, a deadline or horizon, and any budget, access, and burden bounds. For a test `T`, write

`Cap(M_s,T)=1  iff  ∃π∈Π_s  ∀ admitted runs r of π: r satisfies T`.

This is the robust version. Expected loss, probability of success, almost-sure success, and observed behavior are different tests and have different transport requirements. The capacity profile is the collection of declared tests passed by a model. Its elements can distinguish recovery, inquiry, succession, resistance to an unauthorized change, or preservation of a function through replacement. It is not a scalar ethical ranking.

For one common ambient controller space, the bookkeeping can be organized as an intersection:

`Π_success = Π_physical ∩ Π_information ∩ Π_resource ∩ Π_permission ∩ Π_timing ∩ Π_duty`.

This is a definition, not an additional law. Its useful warning is that individual nonemptiness of the sets does not establish nonempty intersection. One controller may be informed but unaffordable, another affordable but uninformed. The one-token discovery/authorization counterexample in the first cycle already establishes this failure.

### The constraints are typed

| Constraint | Exact content once the model is declared | What it does not imply |
|---|---|---|
| Resource | Every required payment or conversion must fit the accessible inventory at its actual time; all prefix balances must be feasible. | Net terminal balance or positive average income is enough. |
| Information | Indistinguishable permitted decision information cannot produce systematically different action distributions under one rule. | More computation can recover a distinction absent from every allowed channel. |
| Authority and control | A policy must actually possess the rights, actuator access, and choices attributed to it; violations and enforcement need explicit semantics. | Formal permission is physically effective or ethically legitimate. |
| Timing | Necessary stages, communication, and contention must complete before the test's deadline; recurrent duty needs repeated access. | Every stage individually possible is jointly schedulable. |

These statements apply to every model satisfying their respective assumptions. Their numerical implications depend on stocks, interfaces, topology, timing, and environment. Whether a real system instantiates those assumptions is a separate evidential claim.

## 2. Three different meanings of change of scale

**Change of units or names.** A bijective relabeling, or a compatible positive change of resource/time units, can leave the control problem isomorphic. Budgets, costs, observations, action effects, and deadlines must all be transformed. Capacity then agrees for corresponding tests.

**Change of description.** A coarse model can summarize a finer one. Information is usually lost, so a proof is needed for the claims retained. A conservative abstraction may permit sound positive certificates while producing false negative results. “Coarser” alone does not specify which direction of implication holds.

**Change of physical organization.** Adding components, sharing channels, changing topology, centralizing authorization, or increasing transport distances changes the actual control problem. No capacity invariance follows. The same scheduling or budget inequality can remain applicable while its parameters and outcome change. In cycle 2, `ceil(n/k)+2` was invariant as a formula, while changing `n/k` changed the achievable deadline.

Some physical replications admit an exact scaled correspondence. That must be proved for the particular replication, including resource access and information routing. Replacing two local memories by one scalar count, or two local authorities by a hypothetical central chooser, is not merely changing units.

A current coarse label need not be a closed state. In a deterministic cycle `a→b→c→a`, let `a,b` share label `0` and let `c` have label `1`. The observed histories `10` and `00` both end at `0`, but their next labels differ. A model that retains only the final label loses predictive memory. In a finite controlled Markov model, common action menus and identical per-action probabilities to every aggregate block supply a sufficient controlled quotient condition. A history-dependent controller can still require its own memory in the state. [Givan, Dean, and Greig (2003), *Equivalence notions and model minimization in Markov decision processes*](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf).

## 3. Decision boundaries and local protocols

To compare different time resolutions, let one abstract action stand for a **concrete local protocol** between designated decision boundaries. It may contain several steps, internal observations, paid computation, communication, and adaptive actions. Its stopping rule must itself use allowed information. It is not simply a precommitted word of primitive commands.

This distinction is established in work on temporally extended, closed-loop options. That framework motivates the representation; it does not by itself establish the safety, authority, cash, and deadline conditions needed here. [Sutton, Precup, and Singh (1999), *Between MDPs and semi-MDPs*](https://people.eecs.berkeley.edu/~russell/classes/cs294/f05/papers/sutton%2Bal-1999.pdf).

Let `H` be an abstract model and `L` a concrete implementation. A boundary relation `R ⊆ Q_L × Q_H` associates their states at those decision points. Let `η` translate currently usable concrete information into abstract information. A compiler `κ` implements an abstract action using a concrete local protocol.

The compiler may use concrete observations during execution. It may not select a different protocol from an unavailable concrete state or an analyst's hidden abstract-state witness. Its memory, communication, interpretation, authorization, and cost belong to the modeled implementation.

## 4. A sufficient cross-scale transport theorem

**CT1 — Bounded protocol transport.** Fix protected sets `K_H,K_L`, target sets `G_H,G_L`, and a class of abstract controllers. Assume the following certificate.

1. **Initial coverage.** Every admitted concrete initial state has a related admitted abstract initial state.
2. **Information compatibility.** At every related boundary pair,
   `I_H(q_H)=η(I_L(q_L))`.
   If an interface is a permitted transcript or register state, this equality applies to that interface. The translation and compiler fit the declared memory/communication/computation restrictions. For distributed controllers, each component translation uses that component's accessible information, unless paid communication is part of the protocol.
3. **Uniform implementation.** The implementation of abstract action `a` is `κ(I_L,a)`, uniformly across concrete states indistinguishable to the controller. It is admitted at every related boundary state where the tested abstract controller can choose `a`.
4. **Every-prefix validity.** Against every admitted concrete environmental behavior, the entire protocol remains in `K_L`, respects physical and institutional action constraints, and satisfies every actual stock/credit payment at the time due. No unavailable branch is silently discarded.
5. **Bounded completion.** Every protocol branch reaches its next recognizable decision boundary after at most `ℓ` concrete ticks, for a finite declared `ℓ`. Failure or nontermination is not classified as completion.
6. **Outcome coverage.** From any related source pair, every terminating concrete branch ends at a state related to some abstract successor of `a`. All matched successors respect the abstract environmental restrictions and retain information compatibility. Safety and target membership translate in the required direction: an abstract safe/target boundary state implies a concrete safe/target boundary state.
7. **Continuation convention.** For safety through a physical horizon after early target arrival, the concrete target comes with an implementable safe continuation through that horizon. A safely absorbing target is sufficient. Without this clause the conclusion only asserts safety until target arrival.

If an admissible abstract controller keeps its run safe and reaches its target within at most `N` abstract transitions, its compiled concrete controller reaches `G_L` within at most `Nℓ` concrete ticks, remains safe throughout the execution, and satisfies the promised post-arrival safety convention.

**Proof.** Start from a related pair supplied by condition 1. The concrete controller computes only the information in condition 2, obtains the abstract controller's next action, and invokes its uniform implementation. Conditions 3–5 make this a valid finite local execution, including all intermediate states. Condition 6 extends a matching abstract run by one step and reestablishes the relation and usable interface. Induction therefore produces a matching abstract run for every concrete environmental branch. Every such abstract run is among those against which the abstract controller guarantees arrival. It reaches `G_H` by transition `N`; target translation gives concrete arrival at the corresponding boundary. Summing the protocol durations gives `Nℓ`. Every-prefix validity gives intermediate safety, and condition 7 supplies safety after arrival when required. ∎

The matching abstract-state path is a proof witness. The concrete controller never has to observe or store it beyond the explicitly implemented interface. Requiring this distinction prevents an existential simulation match from becoming free hidden information. Feedback refinement relations make closely related implementation restrictions precise: controllers using only symbolic/quantized information need more than an arbitrary state-informed matching argument. [Reissig, Weber, and Rungger (2017), *Feedback Refinement Relations for the Synthesis of Symbolic Controllers*](https://arxiv.org/abs/1503.03715).

CT1 is a sufficient certificate, not a necessary characterization of every capacity-preserving abstraction. It extends the previous one-step certificate to temporal protocols. Its proof uses established alternating/refinement logic, now with explicit prefix, information, and timing obligations. [Alur, Henzinger, Kupferman, and Vardi (1998), *Alternating Refinement Relations*](https://www.cis.upenn.edu/~alur/Concur98.html).

### Quantitative bounds, without hiding financing

More informative certificates can match each abstract transition of duration `τ_H` and nonnegative gross expense vector `c_H` with concrete protocol bounds

`τ_L ≤ λ τ_H + d`,

`c_L ≤ A c_H + o`,

where `λ,d ≥ 0`, `A` is a componentwise nonnegative matrix between compatible resource units, and `o ≥ 0` is charged per protocol invocation. For an abstract controller reaching its target within time `T`, gross budget `C`, and at most `N` invocations, summation yields

`T_L ≤ λT+Nd`,     `C_L ≤ AC+No`.

These are *gross-use* bounds up to target arrival. If the test counts expenses through a later horizon, the continuation expenses must also be bounded. The formulas do not prove the timing of liquidity or the availability of replenishment. Condition 4 still checks every prefix of the concrete ledger. An input arriving after a fee cannot pay that fee, even when the total gross expense bound is met. Authority is not a coordinate of `c` unless a specified maintenance payment really affects its enabling relation.

If the abstract clock has a positive minimum transition duration, a physical deadline can imply a bound on `N`. Otherwise the invocation bound must be supplied separately: a finite time horizon need not limit the number of zero-duration abstract transitions.

### Infinite safety and recurrent duties

If every concrete protocol is finite and valid, an abstract invariant transfers to the concatenated concrete execution. For a physical infinite-time claim, also require time divergence; a positive lower bound on elapsed time per completed protocol is one sufficient condition. Otherwise infinitely many steps might occur before a finite physical time.

A recurrent bounded-response duty can be encoded by obligation clocks in the protected state. Those clocks must be preserved or conservatively bounded at **internal** concrete steps. A new disturbance arriving halfway through a protocol cannot be ignored until a macro boundary merely because the abstract model samples there. Alternatively, explicit duration bounds can translate response deadlines if onset timing and response-event correspondence are separately certified. No fairness or liveness guarantee is obtained from endpoint matching alone.

## 5. Transport certificates compose

**CT2 — Transitivity with explicit overhead.** Suppose an `H→M` certificate and an `M→L` certificate satisfy CT1, use compatible interfaces and tests, and their compiled controllers can be nested within the admitted implementation class. Then replacing every primitive `M` step of the first protocol by its `L` implementation gives an `H→L` certificate.

The composed boundary relation is

`q_L R_LH q_H  iff  ∃q_M: q_L R_LM q_M and q_M R_MH q_H`.

The information translation is `η_MH ∘ η_LM`. Each internal `M` decision obtains its information through `η_LM`; no witness state is added to the controller. Initial coverage and endpoint correspondence compose. Every intermediate `M` state is protected by the first certificate, and every implementing `L` prefix is protected by the second. Finite bounds compose by addition along the nested protocols. This proves the qualitative claim.

For the quantitative version, suppose one `H` action uses at most `m` primitive `M` actions. Let the two certificates have bounds `(λ₁,d₁,A₁,o₁)` for `H→M` and `(λ₂,d₂,A₂,o₂)` for `M→L`. Then valid composite bounds are

`λ = λ₂λ₁`,  `d = λ₂d₁ + m d₂`,

`A = A₂A₁`,  `o = A₂o₁ + m o₂`.

**Proof of bounds.** Sum the second certificate over the at most `m` intermediate actions, obtaining `τ_L≤λ₂τ_M+md₂` and `c_L≤A₂c_M+mo₂`. Substitute the first certificate's bounds. Nonnegativity preserves the componentwise inequalities. ∎

Thus layers of description can preserve a guarantee while accumulating real overhead. A mutual pair of certificates with positive overhead does not imply identical reserve or deadline thresholds. Exact bijective, zero-overhead, time- and resource-preserving certificates give equality for corresponding tests. The one-way case supplies only its stated direction.

In particular, an abstract winning policy certified by CT1 transfers downward. An abstract failure does **not** prove concrete failure: the abstraction may admit an extra adverse branch. To transfer an impossibility result, supply a suitable reverse certificate, an implementable adversarial strategy, or an independent necessary constraint. This separates positive controller synthesis from negative diagnosis.

## 6. Six ways an apparent correspondence can fail

These examples are deliberately small; each isolates an omitted certificate condition.

1. **Hidden-state-dependent compilation.** Two indistinguishable concrete worlds require `apply0` and `apply1`. Each world separately has a successful implementation of abstract `repair`. No single permitted compiler can choose between them. A statewise existential action match is insufficient.
2. **Endpoint balance without payable prefixes.** A protocol starts with zero cash, prepays one unit, and receives one afterward. Its terminal net change is zero. It cannot start without a credit route. Intermediate stock feasibility is not an endpoint property.
3. **Endpoints safe, passage unsafe.** A path `s→bad→g` has a safe source and target, but does not implement a safe abstract transition `s→g`. A coarse endpoint relation erases the violation.
4. **Lost internal feedback.** The cycle-2 three-step diagnostic protocol adapts its final command to a received bit. Replacing it with a precommitted three-command batch keeps successful physical paths in both worlds but loses the sure guarantee. A macroaction must retain the local policy when that policy supplies its efficacy.
5. **Finite completion without a uniform deadline.** Nature chooses any positive integer `n`, and a protocol reaches the target after a forced `n`-step countdown. Every branch terminates, but no common finite deadline is guaranteed. A stronger example that permits indefinite stuttering can lose even eventual arrival.
6. **Local independence assumed over shared access.** Two tasks each require the same exclusive diagnostic channel during a one-slot window. Each is individually feasible; their simultaneous product is not. Shared resource, communication, or authorization interfaces invalidate the disjoint-product theorem.

The [transport checker](verification/check_constraint_transport.py) verifies an adaptive diagnostic protocol, rejects a hidden-state oracle and an unauthorized implementation, exhausts all 125 precommitted three-command words, and checks prefix payment, intermediate safety, directional abstraction, shared-channel contention, a quantitative two-layer bound, and an unsafe rule handoff. [All assertions passed](verification/constraint-transport-results.json). These finite checks are not a machine proof of CT1 or CT2. The unbounded-delay claim is proved directly, since no finite truncation can establish its universal statement.

## 7. Composition of real components is another operation

Certificate composition is a sequence of descriptions/implementations. Connecting two physical components is different. For independent components, the product of local safety controllers preserves the product safe set. When one component relies on another's output, the receiving component's assumed input contract must be supplied by the other's actual guarantee, with timing, quantity, and information semantics intact.

Circular promises need an initial bridge or an invariant over the joint state. “A will fund B after B repairs A” does not establish that either can make the first payment. The cycle-2 cold-start bridge of sixteen versus a ten-unit first repair gives an exact temporal version of this problem.

A component-level summary must also retain interactions needed by the composition. Open-Petri-net reachability can increase through back-and-forth boundary crossings that one-pass endpoint relations omit; the established relation is generally only an inclusion. [Baez and Master, *Open Petri Nets*, §6](https://arxiv.org/html/1808.05415v6). There is therefore no general warrant for replacing every component by an endpoint table and assuming the whole model remains equivalent.

For decentralized control, a global policy on pooled information is not automatically implementable by the separate actors. A correct composition certificate must either factor the decision rule into the available local interfaces or model the communication and coordination protocol that makes the rule available. A legitimate mandate and a physically accessible shared actuator remain different predicates.

## 8. Recursive change of rules and representations

Put the current rule/representation description `ρ` inside state, with operational configuration `(ρ,x)`. The rule can alter action menus, observation interpretation, resource dependencies, or later amendment procedures. A transition can change `ρ` itself. This represents recursive changes without assuming that each object-level rule is permanent.

The certificate must cover those changes too. Separate within-mode certificates `R_ρ` do not automatically cover the amendment between modes. A simple counterexample has two viable regimes: `(ρ₀,x=0)` and `(ρ₁,x=1)`. If an amendment changes only `ρ₀→ρ₁` while leaving `x=0`, it lands outside the second regime's protected set. Each regime is viable; the handoff is not certified.

A sufficient global condition is a joint protected set `J` in the tagged configuration space, including transition and amendment states, together with one admissible controller whose possible successors remain in `J`. This is the same invariant obligation used in recurrent repair. When changes also modify the compiler, report register, or authorization process, their physical implementation must preserve the corresponding certificate obligations. An ideal adapter that no longer exists after the amendment is not a continuing guarantee.

Expanding the test family can invalidate an earlier equivalence. A summary sufficient for yesterday's decisions may omit tomorrow's distinction. Consequently an implementation equivalence is always relative to the declared tests and interfaces; it is not an assertion that the two carriers are interchangeable for every future purpose.

The external mathematical semantics still specifies what descriptions mean and how transitions are interpreted. A fixed set of finite descriptions can express unbounded operational change, but this does not establish generation of every future concept. Analyst-level model revision, recognition of new stakeholders, and judgment about legitimate goals are not made endogenous merely by naming a state coordinate for them.

## 9. Closed formal core and open extension

| Closed within a declared model | Open work needed for application or extension |
|---|---|
| Run semantics, information interfaces, available actions, timing, and payment order | Whether these variables and transitions identify the real mechanisms |
| A specified test and controller/adversary class | Which duties and affected parties ought to define the test |
| Conditional balance, information, timing, and policy-transport proofs | Whether unmodeled substitutes, side channels, or enforcement failures exist |
| An explicit scale map and verified local protocol certificates | Whether the map remains valid after physical aggregation or organizational change |
| Finite-game computation or separately proved invariants | Whether an unbounded rule language admits a tractable or decidable verification procedure |
| Object-level rule changes covered by the state and certificates | New representations, changing purposes, and expansion of the analyst's model class |

The formal core is closed enough to prove implications. The world described by it need not be materially closed, empirically complete, or normatively settled. These are distinct forms of closure.

The resulting research program is specific: propose independently measurable prerequisite structure; derive its capacity implications; identify which correspondences preserve those implications across resolution or implementation; and expose failures when information, organization, resource access, or timing changes. A failed prediction should revise the mapping or the model rather than be absorbed by an after-the-fact redefinition of “support.”

## 10. Established machinery and present scope

This memo relies on a familiar division of work: alternating refinement identifies control quantifiers; feedback refinement sharpens interface implementability; temporally extended policies retain internal feedback; invariants and accounting verify paths; open-system composition exposes boundary interactions. The cited primary sources support those connections, not a claim that their assumptions already cover institutions, 生生, or all AI systems.

The new work in this session is the explicit integration of these proof obligations for the stated research problem, paired with checked examples and the separate paid scale model. It remains conditional research. Mathematical applicability across a declared class, implementation equivalence, physical replication, empirical cross-domain validity, and ethical value are different claims and require different evidence.
