# Certifying the combined process, including revision of its controllers

5 October 2026. This is a compositional certificate and an exact semantic characterization for a declared installed process. The state set may be infinite. Controllers, representations, evaluators, permissions, records, and successors can change through that process. The result does not assume that a successful policy is automatically selected or installed, and it does not identify continuing production with universal goodness.

This note extends the two-way representation contract in [completeness bridge](completeness-bridge.md), the installed-process distinction in the theories workspace's `closure-study/FORMAL.md`, the local-dependency result in `generative-basis/formal/STRUCTURAL-CLOSURE.md`, and the paid revision certificate R6.1 from the structural-foundations cycle 6. The proof methods are standard invariant, well-foundedness, and transition-system arguments; no mathematical-priority claim is made.

## 1. The object is the actual joint process

Let Z be a set of configurations. It need not be finite, countable, or bounded in the length of represented programs. A configuration can contain:

\[
z=(x,\mu,c,m,r,g,e,\theta,a,b,\ell,p).
\]

Here x is the plant/environment condition; μ the operative mechanism or interpreter configuration; c the installed controller code; m its actual working memory; r stored observations and evidence; g the available candidate expressions or programs; e the evaluator/checker configuration; θ the current represented evaluative commitments; a permissions and execution gates; b a joint resource ledger; ℓ carrier/training/succession state; and p the actual protocol phase and event/obligation monitors. These are roles, not a mandatory ontology or a claim that all real systems possess all these registers.

The installed joint transition relation is

\[
z\xrightarrow{\gamma}z',
\tag{1}
\]

where γ records the actual microstep's delivered events, resource transfers, and elapsed time. Equation (1) includes the outcomes of the **installed** code under every admitted environmental outcome. It is not an existential choice of a better external controller. If several actors act, their individual proposal maps must each use that actor's permitted observation and memory; the joint relation then describes their actual interaction. This allows analysis of a fixed decentralized institution without claiming a general decentralized synthesis algorithm.

Each actor's proposal distribution is equal at histories with the same permitted observation and installed internal state, including the operative code, parameters, and memory. A hidden full state can be used by the analyst when defining (1); it cannot be an undeclared argument of a participant's rule. If randomness or a coordinating signal affects proposal selection, its availability and joint law are part of the interface. A rule label must actually change later action selection when changed; adding an unused “endogenous evaluator” field is not a mechanism.

Use physical microsteps whenever internal phases matter. A macrostep may stand in for them only after its every-prefix contract has been proved. This includes sensing, inference, checking, admission, actual execution, replenishment, code copying, report retention, training, installation, and evaluator or commitment revision.

**Totality and termination.** We require at least one admitted actual successor from every continuing configuration. Unavailable actions, denied permissions, exhausted funds, interpreter errors, and deadlocks must have explicit outcomes. A deadlock is a losing sink for a continuing-duty specification unless the stated objective permits termination. Legitimate completion, authorized refusal, or exit can instead have a terminal outcome accepted by a finite duty. Representing that outcome by an absorbing formal state does not claim continuing physical activity.

## 2. Specify duties independently of self-reported success

Let K⊆Z be the declared acceptable configuration set. K may include recoverable error, rest, suspended inquiry, and bounded revision. It excludes only the independently stated violations: an actual cash shortfall, an unexecuted deadline obligation, a prohibited physical harm, falsified provenance, or another specified outcome. No universal ranking of those concerns is derived here.

The institution's score, label of success, or represented norm θ is separately recorded. Revision of θ may be legitimate, but a score change alone does not change a recorded physical outcome or prove that another person's standing has been protected. There are two different contracts:

1. Preserve a stated physical/relational protection envelope while revising forecasts, weights, procedures, or subsidiary criteria inside it.
2. Permit the protection specification itself to change according to an explicitly supplied revision procedure, with versioned commitments, standing, reasons, and treatment of existing obligations.

The second is a trace-level specification of legitimate revision, not a derivation that the current regime's preferred criterion is correct. Add the required history or finite/unbounded monitor to Z. Historical harm and already incurred obligations cannot disappear merely because a later register uses different words. If the user elects to change the external analytical specification, report it as a changed question.

For a continuing duty, let E₁,…,E_q be independently interpreted **transition events**. Examples are delivered service, completed maintenance, a successor actually receiving usable competence, or an effective response to a registered challenge. Repeatedly visiting a state labelled “can revise” is not repeated revision. A reported event must correspond to its actual physical condition. The safety-plus-recurrence property is

\[
\forall t\ge0:\ z_t\in K,
\qquad
\forall j\le q:\ E_j(\gamma_t)\text{ occurs infinitely often}.
\tag{2}
\]

Require recurrence only where the stated duty warrants it. A theory can explain a good rest, completed task, proper refusal, or legitimate ending. It need not require every module to run forever or every evaluator to change continually.

## 3. Exact safety on arbitrary state sets

For a totalized relation Δ induced by (1), define

\[
F(A)=K\cap\{z:\Delta(z)\subseteq A\}.
\]

The greatest fixed point

\[
W=\nu A\,F(A)
\tag{3}
\]

exists by monotonicity on the powerset lattice. For any initial configuration, membership in W is equivalent to every actual admitted run remaining in K. More generally, an initial set B is safe exactly when B⊆W.

**Proof.** W⊆K and Δ(W)⊆W, so induction preserves K along every run. Conversely let A be all configurations reachable from B. If all actual runs are safe, every finite reachable prefix is in K, so A⊆K, and reachability gives Δ(A)⊆A. Thus A is post-fixed for F and A⊆W. This uses the explicit serial/termination convention so a finite bad or deadlocked execution is not erased from the run semantics. ∎

This is an exact characterization of the installed process, not an optimizer. No maximization over hypothetical replacement rules appears in (3). If the installed institution declines a viable repair, that refusal is an actual edge and may defeat the property.

The theorem does not supply a terminating algorithm on arbitrary infinite Z. Ordinary finite fixed-point iteration is available when the full model and relevant distinctions are finite and effective. On arbitrary sets, transfinite characterization or another proof may be necessary.

## 4. Exact safety and recurring progress through well-founded ranks

A relation is *forward well-founded* here when it admits no infinite forward chain. In ordinary set theory with dependent choice, this is equivalent to the usual well-foundedness of the inverse relation and permits an ordinal-valued rank that strictly decreases along forward edges.

For A⊆Z and each event E_j, form the no-event relation

\[
R_j=\{(z,z')\in A^2:\exists\gamma,
\ z\xrightarrow{\gamma}z'\ \land\neg E_j(\gamma)\}.
\tag{4}
\]

The existential γ matters: if the same pair of endpoints can arise both with and without the delivered event, the no-event edge remains. Endpoint equality alone cannot certify event delivery.

**Theorem C — exact installed-process characterization.** Under the stated totality/termination convention and ordinary well-founded recursion, all actual runs from B satisfy (2) **if and only if** there is a set A and, for each required event j, a rank ρ_j:A→Ord such that:

\[
\begin{aligned}
&B\subseteq A\subseteq K,\\
&z\in A\land z\xrightarrow{\gamma}z'\quad\Longrightarrow\quad z'\in A,\\
&z\in A\land z\xrightarrow{\gamma}z'\land\neg E_j(\gamma)
\quad\Longrightarrow\quad \rho_j(z')<\rho_j(z).
\end{aligned}
\tag{5}
\]

Ranks may reset or increase when the corresponding actual event occurs. They are mathematical witnesses, not free inputs available to the controller.

**Sufficiency.** The first two lines give safety by induction. If E_j occurred only finitely often on a run, its suffix after the last occurrence would have a strictly decreasing infinite ordinal rank, which is impossible. Hence every required event recurs. This argument applies separately to each j, under the same actual joint process. It does not splice together different successful controllers. ∎

**Necessity.** Let A be the states reachable from B, including actual controller memory, installed code, pending obligations, and any history needed for the transition semantics. Safety gives A⊆K and reachability gives closure. If R_j had an infinite forward chain, prepend a finite run from B to its first state and choose the corresponding no-event transition for each chain edge. This would give an admitted run with only finitely many E_j events, contradicting (2). R_j is therefore forward well-founded. Define by well-founded recursion

\[
\rho_j(z)=\sup\{\rho_j(z')+1:(z,z')\in R_j\}.
\tag{6}
\]

Because A is a set, the successor ranks form a set of ordinals and the supremum exists. Equation (6) strictly decreases on each no-event edge, providing (5). ∎

For state-labelled progress P_j, this yields the familiar form: the relation restricted to A∖P_j is well-founded, with a rank decreasing on transitions that stay outside P_j. Entry into P_j resets progress. Actual event monitors are preferable when the outcome is a delivered action rather than a standing state property.

**Finite case.** If A is finite, R_j must be acyclic. The length of the longest no-event path from a state supplies a natural-number rank, bounded by |A|−1. Checking these ranks or the equivalent absence of an event-free cycle certifies **sure** recurrence. This is stronger than a finite Markov chain's probability-one recurrence, which may allow a probability-zero path that delays the event forever.

**Why ordinals are useful.** Infinite state does not require finite ranks. A node may branch to countdowns of every finite length and still have no infinite event-free path; its ordinal rank can be ω. There is no uniform finite completion bound in that example. The theorem consequently characterizes eventual recurrence without incorrectly supplying bounded latency.

The necessity construction is semantic: it does not purport to compute a rank from every program. The usable noncircular certificate is the sufficiency direction, where a concrete invariant and rank are supplied independently and checked against the actual local transitions. Taking A to mean “the successful states” without discharging those checks is not a certification procedure.

## 5. Local contracts that certify the whole rather than assume it

Decompose the actual microstep relation into declared component relations Δ_i selected by real guards or phases. A component may be formation, evidence acquisition, checking, admission, execution, maintenance, teaching, succession, or revision. Synchronous joint events can be one component. The relations must cover every actual allowed step, including environmental interference, denial, error, and fallback.

Choose an independently defined joint invariant

\[
H(z)=H_{\rm plant}\land H_{\rm funds}\land H_{\rm records}
\land H_{\rm authority}\land H_{\rm code}\land H_{\rm succession}
\land H_{\rm duty}.
\tag{7}
\]

This decomposition is illustrative. It can be a phase-indexed disjunction of local assertions rather than a conjunction that all phases satisfy identically. Establish:

1. **Initial coverage.** Every declared initial uncertainty state satisfies H. Assumptions about initial code, endowment, records, authority, and skills appear here.
2. **Actual dispatch and nonblocking.** On H the installed proposal/dispatch mechanism selects only declared components, according to available information, and every selected component has a defined nonempty outcome set. A denial is an outcome, not a deleted branch.
3. **Local preservation.** For every component i and actual state satisfying H and its selection guard, every Δ_i outcome satisfies H. If a component is a macrostep, all intermediate states also satisfy the relevant physical/payment protections.
4. **Local progress.** For each required event j, every Δ_i outcome without E_j strictly lowers the chosen well-founded rank. An emitted E_j must satisfy the physical event interpretation, not merely set a flag.
5. **Complete interaction accounting.** Shared resource transfers, shared noise, permissions, hidden guards, and interference used in any local proof agree with the same joint process.
6. **Time contract.** For indefinite physical operation, elapsed time along infinite admitted runs diverges. Bounds on latency require corresponding duration bounds, not just step counts.

Then H and the ranks satisfy Theorem C's sufficient conditions. This is a composition theorem because each component is proved from the current joint invariant and its actual step semantics; global continuation follows by induction and well-foundedness. None of the component proofs is allowed to assume that another component “will always rescue” it without that rescue and its schedule being represented in the transition relation and rank.

A cycle of dependencies is not logically circular. Maintenance can sustain inquiry; inquiry can produce useful proposals; executed proposals can restore maintenance resources. Initial coverage supplies a base case and each actual step preserves the joint assertions. What would be circular is assuming perpetual maintenance in the inquiry proof and perpetual inquiry in the maintenance proof without proving either from an initially valid state and their actual transitions.

For asynchronous interleavings, include the actual scheduler. A scheduler that may starve a required component forever usually defeats the rank condition. An adequate scheduler realization can establish progress on every path of the resulting relation. Alternatively, explicitly restricting executions by a fairness assumption requires a separate fair-liveness argument: Theorem C characterizes every path of the actual relation, and deleting unfair infinite paths alone does not supply its rank certificate. Do not prove an unconditional all-path theorem by quietly discarding unfair paths.

### Shared funds and interference

Use one ledger per actual resource, with nonnegative balances and transfer identities at every payment prefix. Two modules cannot each spend the same reserve merely because each is separately affordable. Receipts are available only after the transition that delivers them. A promise, a forecast, future output, an unapplied grant, and cash already transferred to a successor are distinct states.

A module must preserve the other modules' needed facts or explicitly transform them into compatible successor facts. Read/write footprints and frame conditions are useful sufficient checks; relying on them requires verifying that hidden guards and selectors do not read omitted variables. Coupled simultaneous updates require a joint proof. Two separately correct marginal transition laws need not preserve a joint harm event when disturbances are correlated.

### Formation, checking, and admission

Candidate generation is the actual mapping from available records, grammar, memory, and resources to proposed code. It need not enumerate all possible meanings. Its output contract records exactly which candidates it can produce and what the succeeding checker can evaluate. A candidate existing in the analyst's hypothesis class is not enough.

Checking consumes real evidence and resources. An accepted report's semantic force must be proved for the declared evidence model. A statistical score with nonzero false acceptance cannot be silently promoted to an all-branch truth guarantee. Safety can instead be maintained by a verified execution envelope/fallback, with statistical usefulness certified separately. Admission requires the available authority, actual installation, and retained runnable payload. An acceptance bit without installation is not a delivered correction.

Maintenance must restore the conditions the next round actually uses. Succession must transfer sufficient program, records, rights, skills, and working resources. An abstract identity of the successor's name or a “copy successful” flag does not prove competent operation. These obligations close the route between modules rather than just show that good endpoints exist.

## 6. Mechanisms and evaluators can revise themselves inside the certificate

Z can contain code strings, interpreters, representations, candidate grammars, evaluative parameters, and validation procedures that change at runtime. The theorem does not require these registers to remain constant. It requires that the actual revision transitions satisfy the same state and progress obligations as any other component.

There are constructive ways to discharge that obligation:

- Admit only programs from a grammar with proved preservation rules.
- Verify finite candidate programs over an explicitly finite local contract.
- Require proof-carrying updates checked by an implemented sound verifier.
- Restrict the actions of an uncertain new controller through a separately certified execution envelope, while allowing the controller's predictions and proposals to change.

These are examples, not mutually exclusive necessities. A verifier that accepts a supplied proof still needs physical computation, memory, installation authority, and an actual soundness argument. A stored certificate is not magically true because the state calls it a certificate.

If the verifier, norm-review procedure, or interpreter itself may change, its update must also preserve the contract governing later steps. Formally, the quantification in local preservation ranges over every reachable μ, c, e, and θ, including newly generated ones. This is not an infinite tower of external governors: it is one transition system containing the governors' physical states. It does retain a declared mathematical interpretation and a proof obligation for the whole admitted mechanism family. Self-revision does not prove that the interpretation is empirically correct from nowhere.

No fixed finite menu of programs is required for the theorem. An unbounded typed syntax and growing records can be included in an infinite Z; closure can be proved by structural induction on generated programs. But a claim to cover every future meaningful concept requires an additional adequacy argument. New syntax alone does not manufacture new physical actions or a correct meaning for its symbols.

### Dependency closure beyond finite state

For a declared coordinate set I and mode-specific old-state read dependencies, begin with the coordinates determining the protected outcomes, permitted observations, permissions, and required monitors. Define

\[
R_{n+1}=R_n\cup\bigcup_{i\in R_n,\lambda}\operatorname{Pa}_i^\lambda,
\qquad R_* =\bigcup_{n<\omega}R_n.
\tag{8}
\]

Even when I is infinite, R_* is the least parent-closed set containing the seed. If i∈R_*, it is in some R_n, so all its parents are in R_{n+1}; every other closed set contains all R_n by induction. Thus finiteness is needed for finite termination of the closure algorithm, not for this leastness result.

For dynamically selected mechanisms, the dependency list must include the selector/code reads or conservatively cover every admitted mechanism. Such closure may expand to all of I and may be infinite or noncomputable. If the update functions and shared fresh-noise contract meet the structural theorem's hypotheses, equal retained states and common noise still give equal retained successor states coordinate by coordinate. Measurability is additionally required for probability-law claims on infinite products. This is representation closure; it does not prove that the retained process is safe or recurrent. Theorem C supplies that separate dynamical obligation.

## 7. Duties allowing rest, resolution, and legitimate exit

The combined architecture should not turn `GF production` into the definition of a good process. For a response duty, a more appropriate specification is

\[
\mathbf G(\text{request }r\Rightarrow\mathbf F\text{resolution }r).
\tag{9}
\]

Create an actual monitored obligation token when r is admitted. It can be discharged only by the specified resolution—possibly successful work, an authorized refusal with the required reasons and protections, or a legitimate exit—not by deleting the record.

A sufficient certificate assigns a well-founded rank to every active token, decreasing on each transition during which that token remains unresolved. Token removal must itself satisfy the resolution contract. Then no token remains pending forever. Multiple overlapping requests need token-specific accounting; completing a stream of easy new requests must not conceal an old unfulfilled one.

For a single outstanding obligation, a monitor can track whether it is pending. Recurring return to a nonpending state represents repeated resolution only if genuine resolution clears the monitor and the cleared condition is represented as a distinguishable state before any replacement request. If one transition resolves an old token and admits a new one, the pending bit may remain true even though each token is resolved; use actual resolution events or token-specific ranks in that case. If there are no requests, rest is permitted and no manufactured production is demanded. Deadlines can instead use age counters and make overdue tokens violations of K.

An accepted finite completion state may be absorbing in the mathematical model. This satisfies a completed finite duty, not an assertion of inexhaustible generation. Evaluating that case under an inappropriate recurring-production objective would answer the wrong question.

## 8. Stochastic progress is a separate useful extension

The exact ordinal characterization above concerns **every admitted path**. A process with random retries can have an event-free infinite path of probability zero and therefore fail sure recurrence while succeeding with probability one.

For a stochastic extension, take a well-defined actual joint path law (for example a measurable kernel on a standard Borel configuration space) with H almost-surely invariant. Suppose that, at every admitted history in H, the conditional probability of delivering event E_j within the next L_j microsteps is at least ε_j>0. This bound must include the installed scheduler, memory, code revision, shared funds, and environmental regime; it cannot be an average across histories that hide a failing subgroup.

Then the probability of no E_j during n successive L_j-step windows is at most `(1−ε_j)^n`, without independence. Conditioning successively proves the bound. Its limit is zero, so after every fixed time another E_j occurs almost surely. A countable union over starting times shows E_j recurs infinitely often with probability one. The same argument handles finitely or countably many declared event types by intersection of probability-one events. A uniform positive lower bound on step durations, or another time-divergence argument, is still needed for physical-time recurrence; merely positive durations can sum to a finite time.

This is a sufficient stochastic progress condition, not an exact algorithm for arbitrary kernels. If an irreversible unacceptable outcome retains a uniform positive conditional risk at infinitely many opportunities, infinite-horizon protection can instead have probability zero. Neither an empirical sample with no failures nor small finite-horizon error automatically proves a zero-risk invariant.

## 9. Concrete certification contract for the 23-phase combined witness

The checked executable witness has physical phases 0,…,22; each baseline transition advances to the next phase. It combines paid acquisition, candidate formation, fresh paid checking, evaluator amendment, regeneration, admission, actual execution, maintenance, training, succession, and an adversarial change between complete rounds. Environmental truth remains stable within a round under the declared contract, and changes at the round boundary. Both the stability interval and the sustaining fallback receipts are explicit assumptions of this constructed system.

For an event emitted on source phase p, use

\[
\rho_p(z)=(p-\operatorname{phase}(z))\bmod23.
\tag{10}
\]

Every baseline non-event transition lowers this natural rank by one. At phase p the event must actually occur, and the rank can reset from 0 to 22. If a control advances through phase p without delivering the required event, (5) fails: the non-event edge increases the rank. A stalled non-event phase also fails strict decrease. This catches missing event delivery rather than crediting a printed schedule.

The code checker should establish at least:

| Item | Required concrete assertion |
|---|---|
| Initial uncertainty | Every declared initial truth table, installed program, evaluator, and reserve is covered |
| Information | Actions depend only on phase, allowed linked records, installed evaluator/memory, and permitted public values |
| Funds | All microstep debits are payable; receipts are delivered at their stated phase; no duplicated resource or free report carry |
| Evidence | Records retain condition–outcome linkage; checking is distinct from proposal generation under the declared truth contract |
| Generation | The implemented grammar and evaluator actually produce the candidate that is later checked; no analyst-injected answer |
| Admission | Accepted runnable code is retained and actually installed under the authority gate |
| Execution | Event credit requires the installed program's actual output to satisfy the independently declared task condition |
| Maintenance | The next-round capacity used by the controller is physically restored and charged |
| Succession | The successor receives the actual archived program, records, evaluator and verifier through paid training/handoff; usable funds remain in the explicitly continuing institutional ledger |
| Revision | An observed failure changes the evaluator rule and later proposals; a changed score never overrides physical correctness |
| Environment | Every admitted round-boundary change is enumerated; no hidden favorable change is supplied on demand |
| Recurrence | Each required actual delivered event obeys its non-event rank on every reachable edge |

The finite witness need not revise its evaluator infinitely often: a one-time correction followed by continued checking can meet the declared duty. Nor does this small grammar establish discovery of arbitrary unrepresented concepts. It demonstrates an actual closed composition of the listed roles, subject to the explicit resource and environmental contract.

## 10. What this closes

The joint-process result goes beyond a collection of independently viable ingredients. It gives an exact safety/recurring-event criterion on arbitrary declared state sets, and local, checkable sufficient conditions for an installed mechanism whose controllers, evaluators, records, and carriers are themselves produced and revised inside the process.

The order of work is concrete: specify local mechanisms and their interpretation; derive the relevant boundary; prove initial coverage; verify every actual component and interference step; verify actual progress or request-resolution ranks; then compose. A positive result certifies the combined process. A failed condition identifies an uncovered input, resource prefix, observation distinction, installation step, revision, or no-progress loop.

This does not require global nontermination of everything, infinite novelty, universal moral agreement, or an unrestricted terminating evaluator. It also does not establish empirical coverage by naming a complete state space. Extending the certificate to a new substantive setting requires its mechanism, observation, resource, outcome, and disturbance correspondence. Cross-tradition accounts can guide which dependencies and failure mechanisms deserve investigation, but textual resemblance alone does not discharge those correspondence obligations or identify distinct ontologies.
