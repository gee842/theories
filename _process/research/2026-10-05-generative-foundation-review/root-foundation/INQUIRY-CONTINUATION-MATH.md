# Distinguishing inquiry when an encounter changes what can follow

6 October 2026. AI-authored hand proofs for **contextual identity → jointly executable distinguishing inquiry under irreversible changes of access**. The [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md) governs the interpretation. An inquiry is activity within the configuration it investigates. Its outcomes can both distinguish alternatives and change the conditions of subsequent encounters. The separation into candidate, observation, retained history and action is an analytical representation of those connected roles, not a claim that observer and world are fundamentally independent.

The [prior identity proofs](IMMANENT-MATHEMATICAL-IDENTITY-MATH.md) quantify over alternative continuations from a specified state. This note asks when the distinctions established by those alternative continuations can actually be acquired along **one** continuing history. The distinction matters when testing consumes, transforms or closes a condition needed by another test. We credit the existing [inquiry-interface reconstruction](INQUIRY-INTERFACE-ARGUMENT.md): an acquired receipt already changes a retained method and the duration of later sampling. Consequence-dependent sampling is not being claimed absent or invented here. The present addition is a general exact criterion for a finite identification task, together with a concrete obstruction in the existing apparatus.

These are self-contained finite transition and decision-tree arguments. They do not claim mathematical priority, a new Lean proof, empirical confirmation, or derivation of every mathematical truth. Ordinary finite-set and logical reasoning remain mathematical background. The source law and calibrated interface used below remain premises of the local realization; being supplied to that model does not place them outside generative activity.

## 1. What is to be identified must persist through the investigation

Let \(L\) be a finite nonempty set of possible **initial target labels** and \(X\) a finite nonempty set of current configurations. A label describes the target fixed before inquiry; it is not an extra observation available to the investigator. Current configurations include all conditions relevant to the claimed continuation: accessible retained effects, source stock, physical phase and action-dependent changes cannot be omitted when they matter.

A belief is a nonempty subset

\[
B\subseteq L\times X.
\tag{C1}
\]

The pair \((\ell,x)\) means that initial target \(\ell\) remains compatible with the observed history and its present configuration could be \(x\). Several initial labels may lead to the same current configuration. They must remain separate pairs if the question still concerns the initial target. Conversely, several current configurations can share one initial label. Neither situation licenses replacing a question about the initial target by a question about the present state.

Take finite action and observation sets \(A,O\). For each action \(a\), let

\[
R_a\subseteq X\times O\times X
\tag{C2}
\]

give its possible observation and successor pairs. An action is enabled at \(x\) when at least one such pair exists. It is **common feasible** at \(B\) when enabled at every current configuration occurring in \(B\). Actual failed attempts with observable consequences must be represented by their own observation and successor in \(R_a\). They must not be silently erased as undefined actions.

After common feasible \(a\) and observed \(o\), the exact updated belief is

\[
U(B,a,o)=\{(\ell,x'):\exists x\ ((\ell,x)\in B\ \land\ (x,o,x')\in R_a)\}.
\tag{C3}
\]

Only nonempty successor beliefs are possible. Write \(\operatorname{Succ}(B,a)\) for their set and \(\operatorname{lab}(B)=\{\ell:\exists x\ (\ell,x)\in B\}\). A terminal belief is one with a single initial label:

\[
\mathcal T=\{B:|\operatorname{lab}(B)|=1\}.
\tag{C4}
\]

The transition law carries \(\ell\) unchanged while updating \(x\). This is how the mathematical representation preserves the original question through its effects. If the intended question is instead about present state, future behavior or an appropriate next action, specify that different terminal condition explicitly. The theorem below permits such variants, but their answers are not initial-state identification.

The finite model represents uncertainty by alternatives and possible outcomes. It does not assign those alternatives probabilities or introduce an analyst's reward, entropy objective or preferred stopping score. Its exactness depends on the declared transition and observation contract. In a deterministic apparatus every enabled action has exactly one observation/successor pair at each state. The relational form also covers robust inquiry with nondeterministic outcomes: the guarantee then concerns every admitted outcome.

## 2. An exact criterion for one terminating identifying inquiry

Let \(\mathcal B\) be the finite set of nonempty beliefs in \(L\times X\), or a finite subcollection closed under all admitted updates from the initial belief. Define

\[
W_0=\mathcal T,
\qquad
W_{n+1}=W_n\cup
\{B:\exists a\text{ common feasible at }B,\
\operatorname{Succ}(B,a)\subseteq W_n\}.
\tag{C5}
\]

Here \(\mathcal T\) is restricted to \(\mathcal B\) when necessary. Let \(W=\bigcup_{n\ge0}W_n\). Finiteness implies stabilization after at most \(|\mathcal B|\) strict additions of stages. There are at most \(2^{|L||X|}-1\) beliefs in the full space; this is a size bound, not an efficient implementation claim.

### Theorem C1 — Finite identification and the least fixed point

For an initial belief \(B\), the following are equivalent:

1. \(B\in W\).
2. A finite decision tree starting at \(B\) uses common feasible actions, updates by (C3), and ends in \(\mathcal T\) on every possible branch.
3. Some deterministic observation-history policy correctly identifies the initial label and terminates for every history admitted by the stated transition law.

If \(B\in W_n\), there is such a policy using at most \(n\) actions. If \(B\notin W\), no such policy exists, even if it retains the entire accessible history and performs unbounded computation between encounters.

**Proof.** For \(B\in W_0\), output its unique label. Inductively, a newly included belief has an action all of whose nonempty successors lie in \(W_n\). Choose that action and attach the already constructed trees. The result has height at most \(n+1\). This proves 1⇒2 and the height statement; following a finite decision tree proves 2⇒3.

For 3⇒2, unfold the policy into its tree of feasible observation histories. Each node has finitely many possible outcomes, because \(O\) is finite. Correct termination means every leaf has unanimous initial label. It also means there is no infinite branch. A finitely branching tree with nodes at arbitrarily large depths has an infinite branch: starting at its root, choose a child whose subtree has unbounded depth, which exists because there are finitely many children, and repeat. Thus the policy tree has a finite height and is finite. Reading it backward shows a terminal node in \(W_0\), and a node whose children have height at most \(n\) in \(W_{n+1}\). Its root belongs to \(W\), proving 2⇒1 as well. ∎

The finite-branch argument concerns all admitted outcomes, rather than only the probability-one paths of an independently stochastic environment. It must not be applied unchanged to probabilistic termination guarantees in an environment whose transitions themselves are probabilistic. It also does not imply a finite bound for arbitrary infinite outcome sets or an infinite belief graph.

### Corollary C1a — Belief is sufficient for a winning policy at this scope

If an identifying policy exists, one can choose its action from the current labeled belief alone. At a nonterminal belief choose an action decreasing its least index of membership in (C5). Along every branch that nonnegative rank decreases until termination.

**Proof.** For a belief first entering at \(n+1\), (C5) supplies an action with every successor in \(W_n\). The rank strictly decreases. ∎

This is an existence result relative to an exact belief update and known transition contract. It does not make that update computationally inexpensive, explain how its law was acquired or prove that a physical learner can afford its representation.

### Corollary C1b — A certificate of failure preserves an unresolved branch

If \(B\notin W\), then \(B\notin\mathcal T\), and every common feasible action has a possible successor outside \(W\). Repeatedly selecting such a successor defeats any proposed policy: it either stops while more than one initial label remains, becomes unable to continue under the common-feasibility contract, or continues indefinitely.

**Proof.** At stabilization \(W\) is a fixed point of (C5). A nonterminal belief outside it cannot have a common action whose successors are all inside, since the next stage would then include it. Repeat this fact along the policy's selected actions. ∎

The adverse branch is a possible history under the represented law, not a hostile intention attributed to the process. Where physically impossible outcomes have been admitted by an overbroad representation, this certificate concerns that representation and calls for correcting its correspondence before drawing an application-level conclusion.

## 3. The apparatus after its existing sensor investigation

The relevant realization is [the existing diagnosis controller and native port](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/diagnosis.py), documented in [its experiment README](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/README.md). We use its factored expanded class, not the smaller family that rules out blocked transfer. The original three-state model has cyclic outputs \(001\); its phase transition and reset behavior have already been investigated. Sensor operations resolve current phase, reset behavior and the parity

\[
\rho=\tau\mathbin{\oplus}\sigma
\tag{C6}
\]

of the readiness reversal \(\tau\) and sensor reversal \(\sigma\). They leave four parameter configurations: \(\tau\in\{0,1\}\), \(\sigma=\rho\oplus\tau\), and \(b\in\{0,1\}\), where \(b=1\) means blocked transfer. Current phase, \(\rho\), reset behavior and the accessible preprobe history are common to this comparison.

For an original learned output \(o\in\{0,1\}\), a probe's actual arrival is

\[
y=(o\oplus\tau)(1-b).
\tag{C7}
\]

The source holds one packet of ten units. A probe consumes that packet whether or not arrival occurs. Productive arrival adds ten units to the apparatus's fuel; nonarrival wastes the packet. Under the declared calibrated-receipt premise the probe reports \(y\). A subsequent probe with source less than ten has the same source-unavailable outcome. Ordinary phase advancement, resetting and sensor reading cannot replenish the source. Computation does not create a source packet.

The four hidden parameter configurations induce three **preprobe behavioral classes**:

| Initial target | Physical condition within the admitted family | Arrival at learned output 1 | Arrival at learned output 0 |
|---|---|---:|---:|
| \(A\) | Open transfer, \(\tau=0\) | 1 | 0 |
| \(B\) | Open transfer, \(\tau=1\) | 0 | 1 |
| \(C\) | Blocked transfer, either \(\tau\) | 0 | 0 |

These labels are fixed by their actual intervention-response profiles under the initial source condition. They are not arbitrary predicates appended to a weaker representation. The two configurations in \(C\) have equal sensor parity and identical probe responses; the interface cannot distinguish them even before consumption. The target of this study is \(\{A,B,C\}\), not an unjustified demand to recover every hidden parameter separately.

The comparison uses all information accessible at the interface, including actual fuel consequences if they are readable. Audit-only hidden flags, internal world fields and source/waste logs remain unavailable. Those are explicitly not inputs to the original controller. Permitting the controller to read them would change the interface and the task.

For the impossibility below we **relax** computation, memory and fuel constraints: allow arbitrarily much processing and ordinary fuel while keeping exactly one source packet and the unchanged command law. This removes possible funding failures as an explanation of failure. It does not assert that the actual saved runs have unlimited support, nor that ordinary fuel can replace the source packet. A policy impossible under this more permissive contract is also impossible under the original tighter funding constraints.

## 4. Pairwise distinction does not compose into one complete inquiry

### Proposition C2 — Every pair of initial classes is contextually distinguishable

There is a feasible distinguishing continuation for each pair among \(A,B,C\), given sufficient ordinary fuel for the stated commands. A probe at learned output 1 separates \(A\) from either other class. A probe at learned output 0 separates \(B\) from \(C\).

**Proof.** The learned cycle permits reaching either output with phase advances; reset is unnecessary. Apply (C7) and the table. The same chosen probe is enabled in both compared initial configurations because both still have a packet. ∎

The three witnesses are alternative continuations from the same preprobe condition. They are not three encounters already executed in one history. The contextual identity result warrants treating the three response profiles as different. It does not by itself provide a jointly executable procedure for identifying which one is actual.

### Theorem C3 — One packet cannot uniformly identify the three initial classes

Under the admitted family, calibrated interface and source law above, no deterministic adaptive policy using only accessible interactions can terminate with the correct initial label for every \(A,B,C\). This remains true with unbounded computation, memory and ordinary fuel.

**Proof.** Until its first probe, every command history has identical observations in the three cases. Sensor readings depend only on common phase and \(\rho\); phase movement and reset have the same laws. Any fuel consumed by identical commands or computations is equal. Therefore a deterministic policy chooses the same preprobe history and the same first probe phase in all three cases. Stopping without a probe cannot correctly assign three different labels to that common history. Never probing cannot provide a terminating identification either.

At the first probe there are two possibilities.

* If its learned output is 1, \(A\) yields arrival 1, while \(B\) and \(C\) both yield 0. On the latter branch both consume the one packet without arrival. Their phase, sensor parity, reset law, accessible receipt, source remainder and fuel history agree.
* If its learned output is 0, \(B\) yields arrival 1, while \(A\) and \(C\) both yield 0. The negative pair again has equal source, fuel and every other accessible condition.

Thereafter the negative pair has identical future observations for every adaptive continuation. Phase/read/reset operations remain equal. Further probes produce the same source-unavailable failure and, where applicable, the same pre-failure interface consumption. Any history-dependent internal computation proceeds from the same accessible history, so its effects cannot distinguish the pair. Induction on further actions preserves equality of the whole accessible transcript. The distinct **initial** labels therefore remain compatible forever. Any eventual output is wrong in at least one member of the pair. ∎

This proof includes fuel as a possible observation. It does not obtain ambiguity by hiding the ten-unit arrival from a system that can otherwise detect it. The two cases retained on the adverse branch both have zero arrival; all consequent fuel observations agree. It also survives an observed failed attempt whose interface operation consumes fuel, because that consumption is equal in the surviving pair.

### Corollary C3a — Randomization cannot guarantee zero-error completion either

No randomized policy can identify the initial class with zero error and almost-sure termination separately for each of the three deterministic cases under the same one-packet interface. In particular, randomizing which phase to test first does not remove Theorem C3.

**Proof.** Represent all internal random choices by one random tape, with the same distribution independently of the hidden initial class. For each class, zero-error almost-sure termination supplies a probability-one set of tapes on which the policy terminates with the correct label. There are three classes, so the intersection of those three sets still has probability one and is nonempty. Fix a tape in it. With that tape fixed the controller is deterministic and correctly terminates on all three classes, contrary to C3. ∎

The tape is a mathematical coupling argument, not new information delivered to the controller. The result does not prohibit policies that sometimes decline to identify, accept a risk of error or succeed only for selected classes. Those are different guarantees. Nor does it deny learning useful partial information: the positive branch identifies one class exactly, and the negative branch rules that class out.

### Proposition C4 — Current behavioral collapse is not initial identification

After the negative first probe, the two surviving initial classes have the same current future behavior at the admitted interface, yet the initial identification target still has two possible values.

**Proof.** The transcript induction in C3 establishes equality of all subsequent accessible outcomes. In the labeled belief representation the two possibilities have distinct \(\ell\) values even if their current configurations are merged into one behavioral class. Hence (C4) is not satisfied. ∎

A procedure can therefore know everything relevant to the remaining interface while being unable to recover a previous distinction. In the terminology used for finite-state experiments, knowing the resulting state and identifying the starting state are different problems. We need not erase their relation or call this a metaphysical separation: the probe's real effects explain why they diverge in this history.

## 5. What a second packet changes—and what it does not

### Proposition C5 — Two initial packets suffice for the three behavioral classes

In the counterfactual variant with twenty source units, the same stable command law, calibrated observations, adequate ordinary fuel and no other changes, at most two probes identify \(A,B,C\): first probe at learned output 1; if it reports 1, identify \(A\); if it reports 0, advance to learned output 0 and probe again. Its report 1 identifies \(B\), and its report 0 identifies \(C\).

**Proof.** After the negative first probe, ten source units remain, so the second probe is enabled. The first probe rules out \(A\); (C7) then separates \(B\) from \(C\) at output 0. A positive first probe already isolates \(A\). ∎

This is a counterfactual sufficiency argument, **not** a fresh packet inserted into the actual history, an executed funded construction, or a demonstrated renewal mechanism. Ordinary reset still does not restore the source. The proof identifies the precise change of continuation conditions that removes this obstruction.

### Proposition C5a — More packets do not identify the two blocked parameterizations

Within the declared command interface, no number of packets distinguishes the two configurations with blocked transfer and common \(\rho\), phase and reset behavior.

**Proof.** Their sensors depend on common \(\rho\). Their probes always give zero arrival, consume the same stock and incur the same fuel operations. Phase/reset behavior is the same. Induction on any adaptive command history gives identical observations and support changes. ∎

Thus the two-packet result identifies the independently specified **behavioral target**, not every theoretical parameter. A claim about the blocked readiness flag would need an additional interaction that depends on it or a separately justified restriction on the family. More repetition of the unchanged interaction does not supply that relation.

## 6. When pairwise tests do become jointly sufficient

For comparison, suppose a finite set of targets admits a finite distinguishing experiment for each distinct pair. Each selected experiment must be executable and terminate for **every currently compatible target**, using common feasible actions at each encountered belief; being executable only for the selected pair is insufficient. Its complete observed transcript must update the compatible target set exactly, retaining the actual target. Suppose further that, after each experiment, its observations can be retained and the configuration can be restored to the common test-start condition for every surviving target, while preserving the initial target and enough conditions for the remaining tests. Restoration is an operative assumption; it does not follow from calling an action `reset`.

### Proposition C6 — Reusable pairwise experiments identify a finite target set

Under those common-executability, termination, exact-update, restoration and retention premises, a target set of size \(m\) can be identified with at most \(m-1\) pairwise experiments.

**Proof.** If at least two labels remain, choose two and execute their distinguishing experiment. Common executability and termination provide a complete observed transcript whichever compatible target is actual. The selected pair's possible transcripts are disjoint by the distinguishing guarantee, so exact updating rules out at least one selected label while retaining the actual target. Retain the outcome, restore the common testing condition for the surviving alternatives, and repeat. Each experiment decreases the number of possible labels by at least one. After at most \(m-1\) experiments one remains. ∎

For deterministic experiments a distinguishing transcript means simply unequal transcripts for the selected pair. For nondeterministic experiments, disjoint possible transcript sets are needed; merely finding two possible unequal transcripts is insufficient. The restoration premise can be replaced by a weaker sufficient continuation condition captured exactly by C1. It is stated here to make clear which otherwise implicit reuse assumption fails in the one-packet apparatus.

## 7. Contribution, retained premises and revision conditions

The positive result is not merely that resources sometimes limit cognition. **The same encounter can generate an informative consequence and remove the relation through which a still-relevant distinction could be tested.** A list of available counterfactual distinctions therefore differs from an executable identifying inquiry. C1 accounts for both together by carrying forward the initial question and all consequential state changes. C3 supplies a concrete instance already latent in the native source law, beyond a failure of its particular saved controller.

This narrows the continuation from the prior identity study. Contextual identity identifies distinctions supported by alternative continuations; inquiry additionally needs an appropriate path through those possibilities. The existing adaptive sampling result shows acquired consequences changing an enacted path. The new theorem identifies exactly when a finite path-selection policy can finish a specified identification task. It does not derive which question should govern continued activity or how the criterion for sufficient inquiry itself forms and changes; those remain the specific wider targets identified in [the inquiry-interface argument](INQUIRY-INTERFACE-ARGUMENT.md).

The local inputs are explicit: an adequately complete configuration representation; a fixed initial target; a correct transition and observation contract; finite state/outcome support for C1; common feasibility or explicit failure outcomes; calibrated readings for C2–C5; the retained learned cycle and accessible history; unchanged parity/reset behavior during the apparatus comparison; one nonrenewing source packet for C3; and appropriate ordinary fuel where a positive execution is asserted. Mathematical exactness neither derives those inputs nor makes their wider provenance irrelevant.

The obstruction would be revised by a substantive change preserving the stated task while supplying another informative accessible consequence, a way to retain and compare a probe-relevant effect omitted from this representation, a nonconsuming test, reproducible fresh instances, or actual source restoration. Such a finding would change the represented continuation possibilities and require recomputing (C5). It would not be a freely toggled interpretation of an otherwise unchanged target. An implementation that distinguishes the negative pair using only the stated unchanged interface would refute C3 or reveal an error in its mapping to the native law.

The two-packet counterfactual shows a sufficient changed condition; it does not establish that the actual process can form that condition. Equal mathematical profiles likewise do not establish ethical interchangeability or a universal rule to continue testing. Identification can be unnecessary, destructive or inappropriate to a larger concern. The result advances one precise connection within the generative account while preserving that account's stronger philosophical and empirical obligations.
