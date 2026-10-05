# An exact criterion for indefinite safe continuation

Formal memo, 5 October 2026. The mathematics is standard safety-game/controller-synthesis mathematics, applied here to make the proposed continuation criterion exact. No novelty or empirical universality is claimed. Original sources, prior frozen experiments, and existing outputs were not changed.

## The positive result

For a fixed finite partially observed system, **indefinite safe continuation is possible exactly when the current information belongs to a family of safe information states that the controller can keep closed under every allowed observation and disturbance.** That family can be computed. Membership produces one finite-memory controller; nonmembership produces a finite-horizon obstruction.

This resolves a quantifier question positively within the stated class:

\[
\forall H\;\exists\pi_H\;\text{safe through }H
\quad\Longleftrightarrow\quad
\exists\pi\;\forall H\;\text{safe through }H.
\]

The right side admits an explicitly constructed finite-state controller. This implication does not hold for arbitrary infinite action branching, and it concerns sure safety rather than positive survival probability, eventual progress, or novel concept formation.

## 1. Model and operational meaning

Let

\[
\mathcal M=(X,A,F,Y,h,K),
\]

where `X`, `A`, and `Y` are finite, `A` is nonempty, `h:X→Y` is the current observation, `K⊆X` is the specified safe set, and `F(x,a)⊆X` is a **nonempty** successor set. One round is:

1. The controller has its observation history and remembers its own previous actions.
2. It selects one action.
3. The environment selects any successor allowed by `F`.
4. The controller observes the new `h(x)`.

Actions may have different physical/institutional preconditions. An unavailable action leads to an explicit unsafe sink, so it cannot count as a successful continuation. The sink has a self-loop. This totalization also makes physical deadlock unsafe rather than treating the absence of future trajectories as vacuous safety. If a terminal success is intended to count as safe instead, declare it explicitly as an appropriate absorbing state; that is a different specification.

The model can include stocks, cash, transfer permissions, readiness, pending work, sensors, and policy/model/evaluator carriers. The theorem does not supply their transition laws. It also does not derive `K` or the legitimacy of its protection from dynamics. A transition may change those carriers provided that change is included in the specified `F` and remains within the modeled state type.

The controller initially knows that the actual state lies in a nonempty set `B₀`. For the main statement, `B₀` is observation-homogeneous: all its states produce the observed initial signal. If uncertainty is specified before the initial observation, apply the theorem to each nonempty `B₀∩h⁻¹(y)` after observing `y`; a sure guarantee requires all initially possible cells to win.

A deterministic observation-history policy has the form

\[
\pi(y_0,a_0,y_1,\ldots,a_{t-1},y_t)\in A.
\]

It cannot select different actions for hidden states consistent with the same history. “Sure safety through `H` transitions” means every admissible path starting in `B₀` has `x_t∈K` for all `0≤t≤H`. Indefinite sure safety means this for every finite time on every infinite path. The environmental quantifier is unrestricted within `F`; no fairness or favorable probability is assumed.

## 2. Exact information states

Let

\[
\mathscr B_K=\{B\subseteq K:B\ne\varnothing,\ h\text{ is constant on }B\}.
\]

These are safe observation-homogeneous beliefs. Here “belief” means a set of still-possible states, not a probability distribution.

For action `a` and next observation `y`, define

\[
\operatorname{Post}_a(B)=\bigcup_{x\in B}F(x,a),
\qquad
\operatorname{Upd}(B,a,y)=\operatorname{Post}_a(B)\cap h^{-1}(y).
\tag{1}
\]

Empty updates are impossible observations and impose no obligation. A nonempty update that contains an unsafe state is losing. In particular, unsafe states must **not** be deleted before forming the update. Safety need not itself be observable.

**Exactness lemma.** Starting with `B₀`, repeated update (1) gives exactly the states that can occur at the end of some concrete path consistent with the complete observation/action history.

**Proof.** Initially this is the meaning of `B₀`. A possible successor has a predecessor in the previous belief, is allowed by the selected action, and has the new observation; these are exactly the union and intersection in (1). Conversely, every state in that intersection extends a consistent predecessor path. Induction proves both directions. ∎

## 3. The greatest fixed point

For a family `W⊆𝔅_K`, define

\[
\Phi(W)=\left\{B\in\mathscr B_K:
\exists a\in A\ \forall y\in Y,
\operatorname{Upd}(B,a,y)\ne\varnothing
\Rightarrow\operatorname{Upd}(B,a,y)\in W
\right\}.
\tag{2}
\]

This is a **common-action** condition for all hidden possibilities. It is not the weaker condition that each hidden state separately has some safe action.

Start with all safe beliefs and delete failures:

\[
W_0=\mathscr B_K,\qquad W_{n+1}=\Phi(W_n).
\tag{3}
\]

The operator is monotone and `W₁⊆W₀`, hence the sequence descends. If

\[
M=|\mathscr B_K|
=\sum_{y\in h(K)}\left(2^{|K\cap h^{-1}(y)|}-1\right),
\]

then at most `M` strict deletions of families can occur. Thus `W_M` is already the greatest fixed point `W*`; an implementation may perform one additional equality check to detect stabilization. Equivalently, `W*` is the union of all families `V⊆𝔅_K` satisfying `V⊆Φ(V)`.

### Theorem 1: necessary and sufficient conditions

For any initial nonempty observation-homogeneous `B₀`, the following are equivalent:

1. `B₀∈W*`.
2. There is an observation-history policy guaranteeing indefinite safety.
3. There is a deterministic controller using at most `M` belief-memory states that guarantees indefinite safety.
4. For every finite horizon `H`, some observation-history policy guarantees safety through `H` transitions.
5. Some observation-history policy guarantees safety through `M` transitions.

More precisely,

\[
B\in W_H
\quad\Longleftrightarrow\quad
\text{there exists a policy guaranteeing safety through }H.
\tag{4}
\]

**Proof of (4).** At horizon zero, the condition is exactly that all possible current states are safe. For `H+1`, a policy must choose one first action. For each possible next observation, its residual observation-history policy must survive `H` more transitions from the exact updated belief. By induction, this means every nonempty updated belief belongs to `W_H`, which is precisely (2). Conversely, choose such a first action and a witnessing residual policy for each possible observation, then join them into one contingent policy. ∎

**Proof of the infinite theorem.** At each `B∈W*`, choose an action `α(B)` witnessing (2). Store the current belief, issue `α(B)`, and update memory by (1). The actual state belongs to the stored belief by the exactness lemma. Every possible next belief remains in `W*`, hence inside `K`. Induction gives safety at all times. This controller uses at most `|W*|≤M` reachable belief-memory states.

An indefinitely safe policy survives each finite horizon. Equation (4) therefore puts its initial belief in every `W_H`. Finite stabilization makes that intersection `W*`, and also makes survival through `M` sufficient. These implications establish all five equivalences. ∎

This is a constructive answer rather than a finite list of supportive examples: compute the fixed point and its witnesses. The computation may be exponentially large because the controller's information states are subsets of physical states.

### Executable controller and what execution costs

The construction is an explicit finite input/output machine. Memory can be a bitset of `|X|` bits plus a finite action/observation interface; the strategy table chooses `α(B)`, and a precomputed transition table maps `(B,a,y)` to the next belief. Impossible observations can be routed to a separately specified error state. They are excluded from the proved guarantee because the stated model assigns them no possible transition.

“Executable” here means that a finite-state implementation can be generated. It does not mean every physical actor can afford or authorize it. If maintaining that memory, computing updates, executing actions, or operating the sensor consumes resources, those requirements must be incorporated into the system or controller class. A restricted controller may not implement the synthesized machine. This is where the framework's demand to account for the mechanisms realizing correction enters the application, rather than being silently supplied by an ideal mathematical policy.

## 4. Finite failure certificates

Give a safe losing belief its removal rank

\[
\rho(B)=\min\{r\ge1:B\notin W_r\}.
\]

Give an unsafe belief rank zero. If `ρ(B)=r`, then for every action there is a possible observation whose updated belief is unsafe or has rank below `r`. Otherwise that action would have retained `B` in `W_r`.

This supplies a finite certificate: against **every** observation-history policy there exists a concrete path, from **some** initial state in `B`, that leaves `K` within `r` transitions. Follow that policy's actions and select a lower-rank observation at each stage. When rank zero is reached, the exactness lemma gives a concrete unsafe path consistent with the resulting history.

The quantifiers are important:

\[
\forall\pi\;\exists\text{ a bad concrete path from some }x_0\in B.
\]

The certificate does not say one initially fixed hidden state defeats every possible policy, or that every state in a losing belief is individually losing. Nor does it assume an adversary can physically revise an already chosen hidden state; exact belief semantics supplies a consistent concrete path for each policy. The certificate exactly negates the required uniform guarantee over all initial possibilities.

## 5. Removing finiteness for existence

The deepest existence statement does not require finite `X`, `A`, or `Y`. Work with sets, the same nonempty-successor and observation semantics, arbitrary causal observation-history strategies, and ordinary set theory with choice. Define `𝔅_K` and `Φ` by (1)–(2) as before, and define

\[
W^{\nu}=\bigcup\{V\subseteq\mathscr B_K:V\subseteq\Phi(V)\}.
\tag{5}
\]

### Theorem 2: arbitrary-set invariant-family characterization

An initial belief permits indefinite sure safety if and only if it lies in `W^ν`. Equivalently, it belongs to a family of safe beliefs with a common feasible action at each belief whose every possible observation update remains in that family.

**Proof.** Monotonicity shows the union in (5) is postfixed. Its image under `Φ` is again postfixed, so maximality gives `Φ(W^ν)⊆W^ν`; hence `W^ν=Φ(W^ν)`.

Select a witnessing action at each member of `W^ν`. Repeated causal belief updates then keep every actual state safe, exactly as in Theorem 1. Choice supplies the simultaneous selector; nonempty successors and the usual dependent-choice principle give a continued path rather than a vacuous absence of plays.

Conversely let `V` be the family of beliefs from which some observation-history strategy wins forever. The first action of any such strategy has, after each possible observation, a residual strategy winning from the exact successor belief. Therefore `V⊆Φ(V)`, and consequently `V⊆W^ν`. ∎

This removes finite-state and finite-action assumptions **for mathematical existence**. It does not establish a finite algorithm, finite memory, computability, a measurable selector, or physical implementability. Infinite-state families can require genuinely unbounded memory. The fixed point may require transfinite descent if computed by repeated deletion; finite-horizon survival need not identify it.

### Theorem 3: finite action choices suffice for the horizon interchange

Even with infinite state and observation sets, if the candidate controller actions at each belief form a fixed finite set, then

\[
W^{\nu}=\bigcap_{n<\infty}W_n.
\tag{6}
\]

Consequently the two finite/infinite-horizon quantifier orders agree. This still does not imply finite memory or an effective algorithm.

**Proof.** Let `B∈⋂W_n`. For each `n`, let `A_n(B)` be the actions whose every nonempty updated belief belongs to `W_n`. These are nested, nonempty subsets of a finite action set. Their intersection is nonempty. An action in that intersection has all updates in `⋂W_n`. Thus `⋂W_n` is postfixed and is contained in `W^ν`. The reverse inclusion follows by induction from `W^ν=Φ(W^ν)`. ∎

Finite game branching also gives the familiar compactness proof: safe partial contingent policies at each finite depth form a finitely branching tree; restriction preserves safety, and an infinite branch gives one coherent policy. Theorem 3 shows that finite controller choices are enough for this safety result even when observation/successor branching is infinite. Neither argument should be confused with a physical compactness law.

## 6. Countermodels and separations

### Same hidden possibilities, incompatible actions

States are `u,v,⊥`, safe set `{u,v}`, with `h(u)=h(v)` and `⊥` unsafe. Actions are `a,b`:

| Current state | `a` | `b` |
|---|---|---|
| `u` | `v` | `⊥` |
| `v` | `⊥` | `u` |
| `⊥` | `⊥` | `⊥` |

Each singleton belief wins, but `{u,v}` loses immediately: no first action is safe for both possibilities. This refutes `∀x∈B ∃a safe(x,a) ⇒ ∃a ∀x∈B safe(x,a)`.

If the initial belief is `{u}`, a controller can alternate `a,b,a,b,…` forever even though every safe observation is identical. A policy depending only on the current observation chooses one constant action and fails within two transitions. Belief memory is therefore substantive, not decorative; two memory states suffice in this example.

### Infinite first-action branching breaks the horizon implication

Let safe states be `s` and all nonnegative integers, with an unsafe sink `⊥`. At `s`, action `choose(n)` moves to integer `n`. At integer `k>0`, every action decrements it; from zero every action goes to `⊥`. There are no further resource arrivals.

For every finite `H`, choose a sufficiently large `n` and survive `H`. Every fixed policy nevertheless chooses some finite `n` at its first step and fails after `n+2` transitions. Thus `∀H∃π_H` holds and `∃π∀H` fails. The initial action choice is infinitely branching.

Here `W_n={s}∪{k:k≥n}`. Their countable intersection is `{s}`, but `Φ({s})=∅`, so `s` is removed at the next, transfinite stage `ω+1`. This identifies exactly why finite-horizon approximations alone are incomplete in the unrestricted set-based theorem.

### Infinite state can require unbounded memory despite two actions

Let the safe state be a hidden counter `n≥0`, initially zero, with a constant observation and actions zero/one. The only safe action at `n` is one when `n` is a positive power of two, and zero otherwise; the correct action advances to `n+1`, the incorrect action enters `⊥`.

A controller with an unbounded counter can win. No deterministic finite-memory controller can: with constant input its eventual action stream is periodic, while the required power-of-two indicator has unbounded gaps between ones and is not eventually periodic. Theorem 3 gives existence, not finite memory, once state finiteness is removed.

### Safety does not imply recurrence, work, or novelty

A single safe state with a self-loop permits indefinite safety. If that state contains no service, investigation, renewal, or progress, none is implied. The property protected by `K` must therefore say what continued existence actually requires; a separate progress condition may also be necessary.

For partially observed recurrence, do not simply require that the belief become a subset of the target infinitely often. In a hidden deterministic two-state alternation `u↔v`, with constant observation and initial belief `{u,v}`, every concrete path visits target `{u}` infinitely often, yet the belief remains `{u,v}` forever. Requiring target-certainty at repeated times would be strictly stronger. The companion fully observed Büchi analysis supplies a least/greatest fixed-point construction. The appendix below gives the exact finite partial-observation reduction by adding a set of outstanding obligations; the ordinary belief alone is insufficient for that naive target test.

### Positive survival probability is a different quantifier

In a process with an independent probability one-half of fatal failure each step, the probability of surviving `H` steps is positive for every finite `H`, but the probability of surviving forever is zero. This does not contradict Theorem 1: no policy in that process guarantees even the first step against all allowed outcomes. A risk threshold, almost-sure guarantee, expected lifetime, and sure safety must be stated separately.

## 7. What this supplies to the proposed root theory

The theorem gives an exact necessary-and-sufficient continuation condition for a broad, explicit class: **a maintainable safe family of information states with a common action for all currently possible situations**. It puts resources, access, sensing, memory, and execution into one test when their mechanisms are included in the model. It also gives a testable failure form: some information state has no action whose possible consequences remain maintainable.

The arbitrary-set version shows that finiteness is not logically essential to this characterization. Finiteness supplies the stronger constructive consequences: finite termination of the calculation, a finite controller, a bounded obstruction, and a finite-horizon decision bound. Finite action choice preserves one further consequence without finite state: the horizon quantifiers agree.

These are genuine deductions. They do not discover the world's correct state space, transition law, observation channel, implementable controller class, or protected predicate. A universal claim about reality would still need a justified representation and preservation argument for those ingredients. Nor does closure inside a supplied state space establish unanticipated ontology formation. A declared finite collection of model revisions can be represented as states; unrestricted future revisions are a further claim.

The earlier four-round computations do not automatically establish the premise of this indefinite theorem. They studied expected outcome vectors and supplied stochastic mechanisms. The present theorem requires sure safety and either the fixed-point certificate or survival through the complete belief bound `M` in one unchanged finite model. Agreement at a few selected horizons, under changing model assumptions, cannot substitute for that condition.

## 8. Independent exact verification

`formal_continuation_verify.py` contains a bitset greatest-fixed-point solver and a separate oracle that searches observation-consistent action assignments over **explicit concrete state paths**. The oracle does not call the solver's predecessor or belief-update routine. It assigns the same action to paths with identical observation/own-action histories, so it cannot accidentally grant hidden-state control.

The completed run exhausts every nondeterministic transition table with two safe states, one absorbing unsafe state, and two actions: `7^4=2,401` transition tables. All five partitions of the three states into observations are included, giving 12,005 games. Every safe observation-homogeneous initial belief is checked through its complete finite-belief horizon bound.

Results:

- 100,842 explicit finite-horizon policy-tree comparisons, all matching the fixed-point layers.
- 19,976 concrete plant/controller product edges checked for the extracted controllers' closure and safety.
- 29,504 losing-belief/action obligations checked for a lower-rank or immediately unsafe observation successor.
- Largest losing rank in this exhaustive domain: three.
- Worked examples cover incompatible hidden actions, memory-dependent safety, safe stuttering, hidden-phase recurrence, and a finite countdown obstruction.

Exact results and model/controller tables are in `formal_continuation_checks.json`. These finite calculations test the construction and certificates; the written proofs carry the arbitrary finite and set-based statements. No Lean build was run.

## Sources and mathematical status

This is an application of established imperfect-information game methods, not a newly discovered law. Chatterjee, Doyen, Henzinger, and Raskin study observation-based controller synthesis, knowledge-set constructions, and fixed-point methods for these games; they explicitly distinguish sure winning, almost-sure winning, and memory requirements. Their broader results are not all needed for the elementary safety proof above. [Algorithms for Omega-Regular Games with Imperfect Information, 2007](https://arxiv.org/abs/0706.2619), [open paper](https://arxiv.org/pdf/0706.2619).

The set-based proof is provided in full so its use of choice and its absence of an algorithmic guarantee remain visible. The physical resource and access interpretation comes from this workspace's earlier `outputs/access-proof.md` and the subsequent `work/universality-audit/formal-assumptions.md`; no original source material was modified.

## Appendix: exact safe recurrence with partial observation

The preceding safety result can be strengthened to require recurring physical progress, provided the progress condition is explicitly registered. Return to the **finite** model of section 1 and fix `P⊆K`. The objective is

\[
\forall\text{ admissible concrete paths},\quad
\bigl(\forall t,\ x_t\in K\bigr)
\ \land\
\bigl(\forall n\ \exists t\ge n,\ x_t\in P\bigr).
\tag{7}
\]

This is sure safety plus a physical-state Büchi condition. No environmental fairness is added.

### Obligation-state construction

An information state is now `(B,O)`, where `B∈𝔅_K` and `O⊆B\P`. The set `O` tracks endpoints of histories whose required visit to `P` remains outstanding since the latest reset. Initialize

\[
(B_0,O_0)=(B_0,B_0\setminus P).
\]

After action `a` and possible observation `y`, let

\[
B'=\operatorname{Post}_a(B)\cap h^{-1}(y),
\]

and, for nonempty `B'`, define

\[
O'=\begin{cases}
B'\setminus P,&O=\varnothing,\\
\bigl(\operatorname{Post}_a(O)\cap h^{-1}(y)\bigr)\setminus P,
&O\ne\varnothing.
\end{cases}
\tag{8}
\]

A successor belief containing an unsafe state goes to an unsafe sink. An unavailable action at any state in `B` also goes to the unsafe sink, consistent with the totalization used above. The safe constructed state space is

\[
\Gamma=\{(B,O):B\in\mathscr B_K,\ O\subseteq B\setminus P\},
\qquad T=\{(B,\varnothing)\in\Gamma\}.
\]

Both `B` and `O` are computed from the initial information and observation/action history. Treating `(B,O)` as fully observed therefore grants no hidden-state information. Only nonempty next beliefs are available as environmental observation choices.

For `S⊆Γ`, let `CPre(S)` contain the constructed states having an action all of whose possible constructed successors lie in `S`. Define

\[
W_{\rm rec}
=\nu Z\subseteq\Gamma\;\mu Q\subseteq\Gamma
\left[(T\cap\operatorname{CPre}(Z))\cup\operatorname{CPre}(Q)\right].
\tag{9}
\]

The inner least fixed point gives a finite adversarial reachability rank to a completed obligation with a return action into `Z`; the outer greatest fixed point makes this repeatable. The companion `progress-and-sources.md` proves the fully observed Büchi fixed-point result used here.

### Theorem 4: exact partially observed safe recurrence

There exists a deterministic observation-history controller satisfying (7) from `B₀` if and only if

\[
(B_0,B_0\setminus P)\in W_{\rm rec}.
\]

When the condition holds, a controller can be implemented by storing `(B,O)` and selecting the memoryless rank policy extracted from (9). The number of safe memory states is at most

\[
|\Gamma|
=\sum_{y\in h(K)}
\left(2^{|P\cap h^{-1}(y)|}\,
3^{|(K\setminus P)\cap h^{-1}(y)|}-1\right)
\le 3^{|K|}-1.
\tag{10}
\]

The factors count, for each target state, absence/presence in `B`, and for each non-target state, absence, membership in `B\O`, or membership in `O`. An implementation may add one error-memory state for impossible signals. Memory affordability and physical execution still require the application-specific checks already stated.

**Proof of reduction, completed obligations imply physical recurrence.** Between resets, equation (8) propagates precisely those compatible histories that have not yet visited `P`, deleting a history's endpoint when that history reaches `P`. If `O` becomes empty, every compatible concrete path has met its current obligation. Whenever `O` is empty, the next step starts a new obligation round. If emptiness occurs infinitely often, every actual path has a `P` visit in each successive completed round and hence infinitely many visits. Safe constructed beliefs ensure actual safety. A winning policy of the finite fully observed Büchi game therefore gives a valid observation-history policy for (7).

**Proof of reduction, physical recurrence implies repeated completion.** Map any winning observation-history policy into the constructed game using its causally reconstructed `(B,O)` history. Suppose a resulting infinite constructed path had `O` nonempty forever after some time. From that time onward there is no reset, and the nonempty sets in (8) witness compatible finite concrete histories of arbitrarily large length avoiding `P`. Their prefixes form a finitely branching tree, rooted in a finite set of actual states. An infinite branch exists. Its root has a concrete prefix consistent with the earlier observation/action history because it lies in `B`. Attach that prefix to the branch. The resulting admissible concrete path follows the original policy and eventually avoids `P` forever, contradicting (7). Thus every constructed path visits `T` infinitely often. The fully observed Büchi theorem now gives membership in (9) and a memoryless constructed-state controller. ∎

The finite-branching argument is load-bearing in this reduction. The arbitrary-set **safety** theorem earlier is not automatically an arbitrary-set Büchi theorem. A set of arbitrarily long finite outstanding histories need not contain an infinite outstanding history without an appropriate compactness/branching condition.

### Interpretation and checks

For the hidden alternation `u↔v` with `P={u}` and `B₀={u,v}`, the first obligation is `{v}`; its next endpoint is `u∈P`, so it clears even though the full belief remains `{u,v}`. The construction therefore accepts the genuine physical recurrence rejected by the naive target-certainty test. A hidden nonprogressing self-loop creates an outstanding path that never clears and is correctly rejected.

The root's separately implemented `partial_progress_verify.py` was read and reviewed against this construction. It checked 4,608 two-state plant/observation/safety/target cases, including empty-successor actions, against exhaustive memoryless strategies in the constructed game. It additionally certified the extracted controllers on their concrete plant/controller product graphs, where a reachable non-target cycle would refute recurrence. The reported 11,520 constructed safe states and 3,962 certified concrete states are totals across those cases. See `partial-progress-results.json`. This review found no required correction. The general equivalence rests on the proof above, not on the finite enumeration.

This closes the stated finite problem of **indefinite protected recurrence under partial observation**. The target may represent a registered renewal, service, or correction event. The theorem does not make every safe loop productive, derive which target ought to matter, or establish unrestricted novelty. If physical elapsed time matters, durations and deadlines need explicit treatment; infinitely many logical transitions alone do not rule out a Zeno time convention.
