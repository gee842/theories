# Removing assumptions and proving a general theory of generation

Investigation for Ren, 5 October 2026.

**Removing assumptions, deriving them from deeper principles, and proving invariance are legitimate ways to strengthen this theory. Describing a result as conditional identifies its current proof obligations; it does not set a ceiling on its eventual importance.** The right objective is a compact, nontrivial account of when continued generation is possible, what prevents it, and which changes preserve those possibilities.

This investigation makes one concrete advance: financial feasibility can be characterized beyond the earlier restriction on total spending per round. A stronger characterization accommodates transfers with limited capacity, delayed opportunities, and income between payments. This broader result does not preserve the earlier conclusion that total funds alone suffice under every access regime. It illustrates how to pursue the wider claim without treating every special condition as a universal fact.

## What a proof of the central claim would establish

Let a system description include its possible changes, observations, feasible actions, resource flows, and the capabilities to be protected. Let \(G(M,z)\) mean that the specified form of continued generation is attainable from state \(z\) in system \(M\). The strongest useful central target has the form

\[
\forall M\in\mathcal C\;\forall z,\qquad
G(M,z)\iff C(M,z),
\]

where \(\mathcal C\) is the declared system class and \(C\) is an independently specified structural condition. The two directions do different work. Sufficiency proves that the conditions guarantee the possibility. Necessity proves that every successful case must satisfy the conditions.

The condition must have content beyond “whatever allows generation.” It should be stated through independently identifiable features, yield forbidden cases, and ideally be easier to check than solving the original continuation problem. A characterization that simply renames the desired outcome is correct by definition but supplies no explanatory gain. No claim is made here that the displayed equivalence has already been proved for the whole theory.

There are several possible meanings of \(G\). Remaining active, retaining the capacity to recover, producing recurring novelty, and protecting the future capabilities of multiple affected parties are different properties. A repeating process can remain active without generating anything new. A process can maintain itself while reducing another process's options. The theory can address all these properties, but each needs its own criterion and the bridges between them need arguments.

This respects situationality. A universal characterization need not say that every system continues, or that one intervention is always reasonable. It can explain both continuation and failure under one law. It also need not determine every microscopic detail: a fundamental constraint can leave many mechanisms possible while ruling out a significant class of outcomes.

## How to discharge an assumption

Suppose the present argument is \(A\land H\Rightarrow T\), where \(H\) is the assumption under examination.

| Result of the audit | What must be shown | Consequence |
|---|---|---|
| The assumption is dispensable | \(A\Rightarrow T\) | Remove it and enlarge the theorem's scope |
| It follows from the remaining basis | \(A\Rightarrow H\) | It is no longer an independent premise |
| It is an overly strong special case | Find a weaker condition that still implies the conclusion | Replace it with the broader condition |
| Its variation changes the answer | Construct a case satisfying the other premises where the conclusion fails | Retain the distinction or generalize the law to explain both cases |
| It is proposed as a law of the intended world | Give an independent interpretation and restrictive consequences | Establish applicability through argument and evidence appropriate to that claim |

Deriving several assumptions from a deeper principle can be a major unification. The deeper principle's consistency, content, and applicability still matter. Making an assumption true by defining the admitted class around it proves a result for that class; coverage of the intended phenomena remains a separate obligation.

The strongest possible theory may therefore retain some foundational commitments and turn many former assumptions into variables. “Transfers are immediate” can become a value of a timing parameter. “Repair is effective” can become a measured response law. A unified theory then predicts how those variations change attainable outcomes.

## An assumption we can now remove

The earlier pooling proof required enough cash capacity to cover the entire round's bill before any income arrived. That is sufficient but unnecessarily restrictive when payments, income, and transfer opportunities occur within a round.

For the stronger theorem, an event consists of income arriving, an opportunity to transfer funds from treasury into cash, and a bill falling due. Arbitrary finite sequences of income arrivals, opportunities, and bills can be represented by inserting events with zero values for unused components. Cash capacity is \(C\), initial cash is \(b_0\), and total initial funds are \(N_0\). Event \(j\) has income \(i_j\geq0\), transfer limit \(r_j\geq0\), and bill \(c_j\geq0\).

Income is credited to cash up to capacity, with excess retained in treasury. Transfers are free, can be chosen anywhere from zero to the permitted amount, and have no other effects. The per-event opportunities do not consume an omitted shared transfer quota. Borrowing is excluded, and an indivisible bill cannot be split artificially to evade the cash cap. Define

\[
N_j=N_{j-1}+i_j-c_j,
\qquad
B_j=\min\{C,N_{j-1}+i_j,B_{j-1}+i_j+r_j\}-c_j,
\quad B_0=b_0.
\]

**All bills in the sequence can be paid if and only if this greedy recurrence remains nonnegative at every payment.** At any fixed total balance, putting more funds into cash cannot reduce the next attainable cash balance under these rules. The recurrence therefore gives the greatest cash balance reachable after every successfully funded prefix. If it fails, every other admissible transfer schedule fails at that prefix. If it succeeds, it constructs a funding schedule.

With unrestricted refill immediately before each payment, the characterization reduces to two requirements: each individual bill fits the cash capacity, and cumulative spending never exceeds initial total funds plus income already received. Total spending over a round may exceed the capacity many times. For example, a wallet holding at most one unit can pay two separate one-unit bills from a two-unit treasury if it can refill between them.

The general recurrence also explains why total funds alone sometimes fail to predict feasibility. One unit locked in treasury until after a payment deadline cannot pay the one-unit bill due now. The same total available before the deadline can. A universal theory should retain that causal difference; proving that delays never matter would contradict the example.

The written argument applies to nonnegative real-valued amounts and every finite event sequence under its premises. An exact finite checker compared the recurrence, exhaustive transfer choices, and an equivalent set of funding inequalities across **504,840 schedules and 1,032,816 examined prefixes**, with no disagreement. These constructed checks support the derivation; they are not empirical observations or the proof of the wider theory. The [general access proof](general-access-theorem.md) records the theorem, its full conditions, and its relation to policy transfer.

## What invariance would mean here

An invariance claim needs a specified change and something preserved by it. Changing coordinates, changing the controller, changing the available information, changing a physical mechanism, and extending a model are different changes. A useful proposal is that implementations related by a stated correspondence preserve the same attainable continuation possibilities, even though their material details differ.

That proposal needs an executable correspondence: the translated actor must have the information, access, time, and resources required to perform its translated actions. A correspondence that uses unavailable future information does not establish attainable continuation. Controller-refinement theory provides precedents for proving both sufficient conditions and converses under explicit interfaces. [Reissig, Weber, and Rungger, sections V–VI](https://arxiv.org/pdf/1503.03715).

Unrestricted preservation under arbitrary changes would be much stronger and often empty. If permitted changes can carry any state to any other, every scalar quantity invariant under all those changes must be constant. This follows immediately by taking any two states and applying a permitted transformation between them. Meaningful universality usually concerns all changes of a specified relevant kind, or a law whose form applies across varying mechanisms.

The physics comparison supports this discipline. Noether's theorem starts with a specified variational structure and a specified continuous symmetry; its conservation conclusions follow within that structure. It does not establish that every property survives every alteration. [Noether, section 1](https://arxiv.org/pdf/physics/0503066). Our access model is not claimed to have a Noether conservation law.

## A more general structural result to build on

A simple characterization already connects information, action, and continuation. Consider a finite action set, and let \(B\) be the nonempty collection of states compatible with what an actor knows. Assume all these current states lie in the declared protected set. Let \(S(z)\) contain the actions that the actor can execute from state \(z\), within the resource and timing rules, and whose allowed successors all remain in that protected set.

An action guaranteeing one-step continuation despite this uncertainty exists exactly when

\[
\bigcap_{z\in B}S(z)\neq\varnothing.
\]

Necessity follows because one action chosen from the same information must work in every compatible state. Sufficiency follows by choosing an action in the intersection. This assumes that the actor can implement that choice; computational, memory, or authorization limits must be included if relevant. It is a robust guarantee, not an expected-risk optimum.

This result explains two apparently different situations through the same relation. Information can help when compatible states require conflicting actions. Information is unnecessary for this guarantee when one available action already works across them. Resource access, timing, and efficacy affect the feasible safe-action sets. More information changes which states remain compatible.

The characterization is elementary and is not claimed as a new discovery. It is a useful basis for deriving longer-horizon conditions, identifying failure witnesses, and proving which descriptions preserve those conditions. Those extensions must retain the actor's information and implementation limits. Merely listing information, resources, and action as important does not establish the required equivalences.

## The additional obligation for indefinite generation

“For every finite duration, some policy can continue that long” is not automatically the same as “one policy can continue indefinitely.” The order of the quantifiers matters:

\[
\forall H\;\exists\pi_H
\quad\not\Rightarrow\quad
\exists\pi\;\forall H.
\]

For example, from one fixed initial decision state, a system can permit a choice of any finite reserve \(n\), then consume one unit at each step with no replenishment. Every finite horizon can be met by choosing a sufficiently large reserve. No permitted initial choice yields an infinite run. The example uses unbounded initial branching; additional compactness or finite-branching conditions can support an infinite-path argument, with further care for policies, uncertainty, and implementability.

Consequently, an indefinite-generation theorem must specify what persists, under which disturbances, by which admissible policy, and whether its guarantee is sure, probabilistic, or an expectation. Recurring novelty needs a progress condition beyond staying inside a safe set. These are precise obligations rather than a claim that such a theorem is impossible.

## How to establish the full intended reach

The proof program has four connected obligations. First, state the central properties and a small basis with enough precision to construct models and countermodels. Second, prove the strongest necessary-and-sufficient structural results and identify which assumptions are redundant, derived, or essential for the advertised conclusion. Third, prove preservation under explicit changes of representation and implementation. Fourth, establish that the intended real cases satisfy the interpretation and admission conditions without defining membership by whether the prediction succeeds.

The last obligation requires more than reproducing a supplied model. Our proposed second implementation remains untested: independently measure a task-processing service's local failure, monitoring, repair, payment, and scheduling behavior; freeze its mapping and integrated predictions; then compare against outcomes not used to fit those predictions and against a serious alternative with comparable information. This can challenge whether the supposedly sufficient state omits something such as deadlines. It would provide evidence about that transfer, not a deductive proof covering every possible future application.

Where the theory judges an outcome unreasonable, specify whether it violates a feasibility bound, defeats a stated goal, rests on a false expectation, or conflicts with an ethical commitment. Those judgments can be related, but continued operation alone does not settle whose future possibilities ought to count. Normative premises need their own justification.

**The productive route is to prove an increasingly general characterization of the conditions for continued generation.** This investigation has replaced a restrictive financial-feasibility premise with a broader exact characterization. The whole-theory equivalence, its coverage of the intended world, and its claims about indefinite novelty or justified conduct remain distinct proof obligations.

## Evidence and scope

The [evidence bundle](universality-audit-evidence.zip) contains the assumption ledger, proof-strategy memo, mathematical derivation, exact checker and results, and independent review. The ledger examines existing formal and operational claims; it is not an exhaustive audit of the entire philosophical corpus. No full Lean rebuild was run, no reference repository was modified, and the earlier frozen experiments and archives retain their original scope.
