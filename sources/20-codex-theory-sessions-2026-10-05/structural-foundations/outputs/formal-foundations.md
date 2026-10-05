# Formal foundations: transformations that change their enabling conditions

Research memo, 5 October 2026. This is a proposed modeling core and a set of conditional results, not a universal social law or an originality claim. The existing project was read as reference, especially its `README.md` and claims U01, U04–U05, U16, U20–U25, P01, and N01. Nothing in the parent research directory was modified.

## Main finding

The provisional signature `S = (X,T,R,O)` is a useful modeling checklist, but it does not yet specify a dynamical system. Its components conceal choices about what is currently actual, who can choose a transformation, what an attempted transformation does, what an observer can retain, and which interventions are being held possible. Those choices change theorems.

A small controlled transition system is sufficient for the present research. Rules, representations, support relations, and controller memory can be ordinary components of a configuration. Their revision is then a transition that changes later transitions or later information. This is expressive without assuming a fixed operational vocabulary, but it still uses a declared external mathematical language. It does not explain unrestricted concept generation merely by allowing an interpreter to rewrite its own program.

The substantive candidate for the program is not the new tuple. It is a disciplined way to state, test, and compose constraints on *temporally accessible revision*, while current activity changes the resources, interfaces, and authority needed for that revision.

## 1. Audit of the provisional signature

| Component | Missing distinction | Required clarification |
|---|---|---|
| `X`: configurations | Space of possible configurations versus actual configuration | Specify an actual `q ∈ Q`, or an initial uncertainty set/distribution. |
| `T`: transformations | Label, command, enabled operation, realized event, and policy | Give attempted-action labels and their outcome relation; distinguish controller choices from environmental outcomes. |
| `R`: enabling quantities and relations | Divisible stock versus connection, entitlement, tool, or dependency | Quantities require units and balances; relations require typed predicates or graphs. Paying a cost does not prove that the relation exists or works. |
| `O`: distinctions | Potentially measurable versus acquired versus retained versus currently usable information | Specify the decision interface, its acquisition/update process, and permitted controller memory. |
| `Φ`: update | Determinism, timing, closure, and the origin of rules | State how environmental inputs and failed attempts work, which parts are endogenous, and what remains fixed in the analyst's semantics. |

Writing `e_t ∈ T_t` assumes the transformation is already available when selected. If inquiry is supposed to discover a candidate, its generation must be a modeled transition, not a free selection from the analyst's full `T`. Likewise, if the rule selecting transformations is the object of explanation, optimizing externally over all policies provides a benchmark rather than that explanation.

`X_t ⊆ X_(t+1)` is not needed in general. Replacement can discard old states, descriptions can be incomparable, and more syntactic distinctions need not increase useful control. A typed change between descriptions is less restrictive than monotone expansion.

## 2. Proposed semantic core

Use

`M = (Q, A, W, F, {I_i}, Π)`.

* `Q` is the set of complete modeled configurations. It may contain material states, rule descriptions, access relations, institutions, agent identities, grammars, retained records, and actual controller memory. This is a type declaration, not a claim that these are all one kind of substance.
* `A` is an ambient set of attempted-action labels. A label is not a guarantee that the operation is known, allowed, affordable, or successful.
* `W` is a disturbance/input interface. Which inputs may occur after which histories must be declared. Omit `W` and absorb it into `F` if no interface distinction is needed.
* `F(q,a,w) ⊆ Q` is the set of successor configurations. Nonempty values describe admitted outcomes; emptiness denotes an unavailable physical transition in the partial convention.
* `I_i(h)` is agent `i`'s **currently permitted decision information** after a realized history `h`. It is not automatically the full history of earlier signals.
* `Π` is the declared class of admitted controllers or joint protocols. Its information, memory, representation, implementation, and action-menu restrictions are part of the model.

One step has an explicit order: current information is available; a controller chooses an attempt; a permitted input occurs; an outcome in `F` occurs; information and memory are updated. Other orders are valid models, but generally different ones. An input revealed before the action supplies information unavailable when it is revealed afterward.

For robust claims, nature resolves the declared inputs and any residual nondeterminism. A stochastic version supplies a probability kernel and a measurable structure, rather than silently assigning probabilities to a set of possibilities. For multiple agents, a joint action is a tuple, and each coordinate must be generated from that agent's interface. Pooling the interfaces creates a stronger controller unless communication is actually modeled.

### Failed attempts, menus, and authority

There are two useful conventions, which must not be mixed:

1. **Partial execution:** an admitted controller must choose an action physically enabled in every state consistent with its information. An attempted unavailable action is not a trajectory of this model.
2. **Explicit attempted execution:** every representable attempt has an outcome, possibly denial, delay, damage, or sanction. Such outcomes are in `F` and can themselves reveal information. A special failure state prevents a deadlock from being incorrectly counted as safety.

The second convention is usually better when studying institutions or learning from refusal. The first is compact for safety proofs. Neither grants agents access to the full ambient `A`: current representable menus must be enforced through `Π` or explicit local protocol state.

Keep three statements separate:

* `Phys(q,a)`: the attempted effect is physically executable under the declared inputs.
* `Perm_i(q,a)`: the institution recognizes agent `i` as permitted to do it.
* `Enforced(q,a)`: permission or denial has a specified effect on the actual transition.

One may define an effectively permitted action set using all three when warranted. An unauthorized act can remain physically possible; a formally authorized act can remain infeasible. Whether permission is legitimate is a further evaluative question, not determined by any of these predicates.

### Memory warning

Letting a policy condition on the complete observation history gives it perfect recall for free. Charging for archives while leaving that policy class unchanged does not model forgetting: the policy still remembers the deleted record.

For paid memory, include memory registers in `q`, charge their storage/update as required, and restrict decisions to `I_i(h)` containing the permitted current registers and current inputs. Any persistent random seed or hidden controller state that can carry past information must be included too. A clock, a public signal, a refusal, or another agent can also preserve information; deleting a named archive does not erase those channels.

For finite-memory models it is often convenient to make `I_i(h)=ι_i(q_last)` because `q_last` already includes the controller's actual memory. Full-history policies can be retained as a clearly identified upper bound. Their standard belief-state recursion is not automatically a solution for a controller that must pay to retain its beliefs.

**Checked memory counterexample:** reveal a fair hidden bit, forcibly erase the only permitted memory register, and later require the controller to guess the bit. No intermediate choices, new signals, or other carriers are available. Every decoder using the erased current interface has success probability `1/2`, including randomized decoders. A perfect-recall decoder succeeds with probability `1`. An archive-deletion model that still lets the decoder use the original signal therefore has not charged for losing that information. The finite deterministic decoder enumeration is saved in the [verification script](verification/check_foundation_examples.py) and [results](verification/foundation-example-results.json).

## 3. Endogenous rules and changing representations

A useful configuration decomposition is

`q = (x, d, m, b, g)`.

Here `x` is the modeled carrier configuration, `d` a current description of local rules and representations, `m` retained controller memory, `b` typed stocks, and `g` typed access/dependency/permission relations. A model need not use every coordinate. A fixed external interpreter specifies how `d` determines current menus, observation procedures, and transition clauses. Revision transitions can replace `d`, revise the interpreter description inside `d`, alter `g`, or replace the carrier while preserving a tested function.

Two levels must stay distinct:

* **Object-level revision:** the system changes a represented rule, vocabulary, measurement procedure, or interpreter through an operation described by the present model.
* **Analyst-level revision:** a researcher changes `Q`, `F`, the interface, or the evaluation because the old model omitted a relevant phenomenon.

The first can explain a particular endogenous change if its generating mechanism and costs are specified. It cannot establish that the second has been eliminated. Reifying more interpreter levels does not remove the final mathematical semantics under which the reification is interpreted.

### F1. Fixed-ambient representation lemma

**Status:** elementary encoding fact; no novelty claimed.

Let `D` be a set of local descriptions, and `X_d` the configuration set valid under `d`. Suppose a declared transition relation specifies changes `(d,x) → (d',x')`, including changes of description. Then

`Q = ⨿_(d∈D) X_d = {(d,x): d∈D, x∈X_d}`

is a single fixed state space representing exactly those changes. Retain the same action labels, inputs, observation maps, and annotations on each tagged state/transition. Projection from a tagged run to its sequence of local descriptions and configurations, and tagging in the reverse direction, are inverse maps on runs.

**Proof:** a local transition is, by construction, exactly an edge between its source and target tagged states. Induction gives the run correspondence at every finite length; the same componentwise correspondence handles infinite runs. The transferred annotations preserve the specified information and costs. ∎

**Consequence:** fixed mathematical `Q` does not imply a fixed operational action set, fixed finite dimension, or fixed vocabulary available to the modeled system. A set of finite descriptions can support unboundedly many generated states and arbitrarily long descriptions.

**Limit:** the lemma assumes a declared set `D` and declared cross-description transitions. It establishes representability, not effective generation, computability, learnability, or completeness for future scientific concepts. An arbitrary lookup-table encoding can fit any finite trace while predicting nothing. Finite strings are countable; representing arbitrary real parameters requires an explicit idealization or a suitable larger domain.

### Representation change needs a relation to use, not just new names

When comparing vocabularies `L_d` and `L_d'`, declare which old questions are translated, which meanings are preserved, and which genuinely new tests become expressible. A semantic correspondence might require

`M' ⊨ translate(φ)  iff  reduct(M') ⊨ φ`

for old sentences `φ` in its scope. This kind of invariance under signature change is established in institution theory. It is optional machinery when a simple interpretation map will suffice. It does not guarantee that a new representation is true or beneficial. [Goguen and Burstall, *Institutions*](https://cseweb.ucsd.edu/~goguen/pps/ins.pdf).

## 4. Capacity is indexed by a test and quantifiers

For initial uncertainty `B ⊆ Q`, safety requirement `K`, target `G`, horizon `T`, admitted inputs, and controller class `Π`, define the robust revision capacity test

`Cap_M(B,K,G,T;Π) = 1`

iff some `π ∈ Π` generates only runs that stay in `K` through time `T` and visit `G` by time `T`. Count blocked execution as failure unless the duty explicitly permits stopping. Include resources, retained representations, and authorization in the state or policy constraints so they cannot be supplied for free during the test.

This is the **safe-through-horizon** convention. A different convention only requires safety until the first target visit. The two agree when target states are safe and absorbing, or when a guaranteed safe continuation is supplied after arrival; otherwise they must not be interchanged.

This definition says what is being evaluated. It is not itself an explanation of why the capacity exists or why anyone will use it. In a probabilistic model, replace the Boolean test by a specified success probability, risk bound, or value functional. These are different questions from a robust guarantee.

At least four capacities must be distinguished:

| Capacity | Typical quantifier | Meaning |
|---|---|---|
| Physical reachability | Some run reaches `G` | A favorable sequence exists. |
| Full-information controllability | Some state-informed policy succeeds against all admitted inputs | An informed external controller could guarantee the test. |
| Interface-restricted controllability | Some `π ∈ Π` using only current permitted information guarantees the test | A controller of the declared kind could do so. |
| Actual protocol performance | The implemented selector/protocol is used | What this system in fact does, or its success law. |

The first three form the expected nesting only when they share the same actions, resource rules, initial set, and disturbance assumptions; changing those assumptions can invalidate an apparent comparison. Under partial observation, a policy must act uniformly on histories with equal permitted information.

An intervention such as “supply a diagnostic,” “restore a reserve,” or “transfer authority” defines a *different specified experiment*. Its existence does not mean the original system currently has the resulting capacity. Both the intervention and the means of implementing it need a declared boundary.

There is no canonical scalar “size of possibility.” Counting duplicate action labels can double a menu without adding any behavior. Adding a coercive or destructive action can expand reachability while harming people. Costs, protected constraints, observers, and useful functions belong in capacity comparisons. The project's ethical commitments remain independently stated.

## 5. Implementation equivalence must preserve control and information

Equality of a realized output trace is very weak. Even equality of all ordinary event traces can erase when a choice is made and who controls it. Resource balances and observation interfaces are further discriminators.

### F2. A finite-horizon sufficient capacity-transfer criterion

**Status:** a direct simulation argument, following established alternating-refinement reasoning; stated here in a restricted, auditable form. It is sufficient, not necessary, and is not a novelty claim.

Consider an abstract system `H` and a concrete system `L`. For this result use configurations that include actual controller memory, so their decision interfaces are `ι_H(q_H)` and `ι_L(q_L)`. Absorb admissible disturbances into successor sets `Post_H(q_H,a_H)` and `Post_L(q_L,a_L)`. The systems share a step horizon. Let `R ⊆ Q_L × Q_H`, an information map `η`, and an action implementation map `κ(i_L,a_H)` satisfy:

If an admitted disturbance can block an attempted action, include that outcome as failure rather than dropping it when forming `Post`. A physically enabled policy in this theorem has a nonempty successor set under every admitted disturbance. The tested policy is a function of its current interface (including any permitted clock), with its actual persistent memory already in the configuration; it is not an additional perfect-recall controller outside the state.

1. Every concrete initial state has at least one related abstract initial state.
2. Related states satisfy `ι_H(q_H)=η(ι_L(q_L))`. The maps `η` and `κ` can actually be implemented within the declared information, computation, memory, and payment limits.
3. For every related pair and each abstract action admitted by the tested abstract controller, `a_L=κ(ι_L(q_L),a_H)` is concretely admitted and physically enabled. Thus the same concrete action is selected at indistinguishable concrete decision points; a hidden-state-dependent match is insufficient.
4. Every concrete successor of that action has an abstract successor of the abstract action related by `R`. Formally, for all `q_L' ∈ Post_L(q_L,a_L)`, there exists `q_H' ∈ Post_H(q_H,a_H)` with `q_L' R q_H'`.
5. `q_L R q_H` and `q_H ∈ K_H` imply `q_L ∈ K_L`; similarly, `q_H ∈ G_H` implies `q_L ∈ G_L`.
6. If a separate cumulative expenditure bound is part of the test, matched concrete steps cost no more, component by component in compatible units, than their abstract steps; the concrete allowance is at least the abstract allowance. Alternatively encode budget feasibility in `K` and use state condition 5. For replenishing stocks, prefer explicit stock-state matching rather than a crude cumulative-cost comparison.

Then an abstract admitted controller guaranteeing safety through `T` and target attainment by `T` lifts to an admitted concrete controller with the same guarantee.

**Proof:** use the abstract controller on `η(i_L)` and implement its action using `κ`. By conditions 2–3, this is an allowed concrete policy, without access to hidden states. Pick a related abstract initial state using condition 1. For any concrete run, condition 4 extends a related abstract run one step at a time. Its information and actions are exactly those of the abstract policy, because of condition 2; nature's matched outcomes are among those against which the policy guarantees success. The abstract run therefore stays safe and reaches its target by the horizon. Condition 5 transfers these facts at the same steps. Summing the nonnegative stepwise cost bounds proves the optional expenditure claim. ∎

The abstract-state witness in this proof is used by the analyst; it is not an uncharged private memory of the concrete controller. The implementation only uses `η(i_L)` and `κ`.

Mutual transfer under a declared interface and test class gives a useful notion of capacity equivalence. An observation- and label-preserving bisimulation with matching controllers is a convenient stronger sufficient condition. If probabilities matter, matching successor supports alone is insufficient: probability kernels require an appropriate matching of probability mass. If a concrete action expands into several steps, timing, intervening observations, costs, and intermediate safety require a separate refinement argument. [Alur, Henzinger, Kupferman, and Vardi, *Alternating Refinement Relations*](https://www.cis.upenn.edu/~alur/Concur98.html); [Rutten, *Universal Coalgebra*](https://ir.cwi.nl/pub/48/).

### C1. Equal ordinary traces, different controlled capacity

System `H` has `h0 --a--> h1`; at `h1`, the controller can choose `b` to a target or `c` to a nontarget.

System `L` has `l0 --a--> {lb,lc}`, with nature choosing the successor. At `lb` only `b` executes; at `lc` only `c` executes. The completed ordinary event traces of both systems are exactly `{ab, ac}`. Nevertheless, `H` can guarantee occurrence of `b` by step 2, and `L` cannot: nature may choose `lc`. Full observation of this branch would not restore the missing action.

This is a partial-execution example. If refused attempts are modeled as events, those refusal traces expose another observable difference. The point is that ordinary successful event traces discard branching, refusal, and control information; it is not a claim that every possible complete interactive semantics fails to preserve capacity.

This counterexample was enumerated by the [small checker](verification/check_foundation_examples.py); both trace sets agree and the computed two-step winning statuses differ. The [saved results](verification/foundation-example-results.json) also retain the memory and shared-reserve checks. Reproduce them from the task root with `python3 outputs/verification/check_foundation_examples.py`; the script uses only Python's standard library.

## 6. Composition: the boundary is part of the result

For two systems with disjoint private resources, no conflicting actuator or authorization, no hidden shared environmental constraint, and compatible clocks, define a synchronous product:

`Q = Q1 × Q2`, `A = A1 × A2`,

`Post((q1,q2),(a1,a2)) = Post1(q1,a1) × Post2(q2,a2)`.

Each local controller continues to use only its local interface. If each controller maintains `Kj` for all its local admitted outcomes, their pair maintains `K1 × K2`. **Proof:** each product successor has a component in the corresponding safe set; induction applies. This is an elementary special case, not a general theorem that locally viable institutions compose into a viable society.

The product equation is an assumption about independence and compatibility. Coupled inputs, shared permissions, information leaks, network topology, and contested budgets usually require an explicit interface rather than this product. Established input/output automata illustrate why component interfaces, input assumptions, and composition operators must be specified. [Lynch and Tuttle, *An Introduction to Input/Output Automata*](https://groups.csail.mit.edu/tds/papers/Lynch/CWI89.html).

Even endpoint reachability relations need not compose exactly. For open Petri nets, Baez and Master prove `R(Q) ∘ R(P) ⊆ R(Q ⊙ P)` and give a strict example: a token must move from `P` to `Q`, return to `P`, and move to `Q` again. One-pass endpoint relations omit that reentry. Thus a component summary must retain the interactions needed for the proposed composition theorem. This is a different issue from the disjoint-product lemma above. [*Open Petri Nets*, §6, Theorem 23 and its following example](https://arxiv.org/html/1808.05415v6).

### C2. Local feasibility does not compose when a reserve is double-counted

Two one-step tasks each consume one unit and each meet their duty if funded. Each is feasible when separately analyzed against an accessible one-unit reserve. If both refer to the *same* reserve and both duties are simultaneous, the joint requirement is two units and the composition is infeasible. No new conservation law is involved: the error is duplicated access to a stock.

Similar counterexamples arise when two operations need the same exclusive actuator or incompatible authorizations. Conversely, joining two systems can create a previously absent circulation or information path and make revision possible. Composition can enlarge or destroy capacities; the direction is not fixed by the word “composition.”

For accounting across a chosen boundary, distinguish gross conversion, external transfers, internal transfers, and dissipative losses. Summing genuinely matched internal transfers cancels them. A “self-sustaining” component can still rely on persistent boundary inputs, and functional substitution must be represented rather than treated as creation from nothing.

## 7. What this contributes, and what remains open

The core is deliberately small: configurations, typed attempted transformations, inputs/outcomes, accessible information, and admissible controllers. Resource and institutional assertions appear where they alter enablement, outcomes, information, costs, or tests. This permits the earlier accounting, indistinguishability, financing, and revision results to live in one explicit semantics without pretending that their mechanisms are identical.

Four decisions follow:

1. Keep `S=(X,T,R,O)` as an informal lens; use `M` plus an actual/uncertain initial configuration for proofs.
2. Treat endogenous rules as data with explicit interpreters and paid enactment, while recording the fixed meta-semantics.
3. Treat capacity as a profile indexed by interfaces, intervention class, duty, protected constraints, and horizon. Distinguish its existence from its actual use and ethical desirability.
4. Demand an interface-preserving simulation or direct test before transferring a theorem across implementations. Similar vocabulary or identical output curves are insufficient.

The productive next mathematical task is to combine recurrent paid memory and revision with resource renewal in one small model, then identify a useful abstraction satisfying F2. For example: can a compact summary of reserve, retained evidence, current grammar, and enactment access preserve finite-horizon revision guarantees across two implementations? A counterexample would identify a missing interface or temporal dependency. A successful abstraction would make an implementation-independent conditional claim possible. This is narrower and more testable than asserting that all change is an instance of one evolutionary law.

## Primary-source map and evidential limits

* **State semantics and implementation equivalence:** [Rutten (2000), *Universal Coalgebra: A Theory of Systems*](https://ir.cwi.nl/pub/48/) supplies an established general setting for state-based behavior and bisimulation. It does not make the present social mappings valid automatically.
* **Who controls a branch:** [Alur, Henzinger, Kupferman, and Vardi (1998), *Alternating Refinement Relations*](https://www.cis.upenn.edu/~alur/Concur98.html) directly addresses collaborative/adversarial component choices and refinement. F2 is a deliberately elementary interface-constrained instance of the same strategy-transfer idea, not a claim that the full published theorem has been reproduced here.
* **Open-system composition:** [Lynch and Tuttle (1989), *An Introduction to Input/Output Automata*](https://groups.csail.mit.edu/tds/papers/Lynch/CWI89.html) supplies concrete interface and composition semantics. The product lemma here only uses a disjoint synchronous special case.
* **Representation changes:** [Goguen and Burstall (1992), *Institutions: Abstract Model Theory for Specification and Programming*](https://cseweb.ucsd.edu/~goguen/pps/ins.pdf) separates signatures, sentences, models, and satisfaction under changes of notation. This clarifies semantic preservation; it is not an empirical theory of institutional authority, despite the shared word.
* **Distributed information:** [Halpern and Moses (1990), *Knowledge and Common Knowledge in a Distributed Environment*](https://groups.csail.mit.edu/tds/papers/Halpern/JACM90.pdf) models distinctions between individual and group information. The present memo does not import a universal requirement of common knowledge for coordination.
* **Changing relational structure:** [Leifer and Milner (2006), *Transition Systems, Link Graphs and Petri Nets*](https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/abs/transition-systems-link-graphs-and-petri-nets/B331FC9E81E3068AC014D6BC2323C132) connects graph-based reactive structure with observable transitions and congruential behavioral equivalence. This is useful if the next model needs explicit rewiring; it is unnecessary overhead for the present small examples.

All literature links above were checked on 5 October 2026. These are focused precedents, not a systematic novelty search. The encoded models, proofs, and constructed examples establish conditional formal facts. Domain mappings require separately measured variables and mechanisms; normative conclusions require separately defended commitments.
