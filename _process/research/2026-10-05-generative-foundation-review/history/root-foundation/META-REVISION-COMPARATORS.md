# Selecting generators and retention policies: comparator and stopping boundary

6 October 2026. AI-authored research note. Named connection: retained models and evidence → consequence-sensitive selection of candidate generators and evidence-retention policies. This follows [model-family revision](MODEL-FAMILY-REVISION-COMPARATORS.md) and the actual [revision continuation](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/README.md). It assesses the next derivation, rather than adding a selector whose reward would already assume the result.

## Design conclusion

The present branch supports a substantive terminal-budget and information-boundary study. It does not yet support a demonstrated derivation of a generator/retention selector from organizational consequences. The missing element is not a known optimization algorithm: it is a physically available connection from competing policies through their consequences to differential retention or revision, together with resources to execute that connection.

An analyst can score correct prediction, identify the true simulated machine, or assign future-query usefulness. Those scores do not become learner inputs merely because they are useful evaluation measures. A local prediction-comparison receipt is already more defensible than a hidden true-model label, but choosing its scalar error as the selector's reward still introduces a task criterion unless its effect on the system's operation is established. Numeric reward is not necessary in principle: resource-mediated persistence of competing mechanisms could supply selection. That mechanism must be present and traced, rather than renamed after an external score.

## Three primary comparators

**Rational metareasoning prices computation against a given consequential value.** Russell and Wefald treat computations as choices whose value derives from their effect on eventual external actions and the time consumed. Their formalization explicitly starts with a world-state utility function, possible computational actions, and estimates of their outcome distributions. Their practical search procedure uses simplifying assumptions and prior statistical information; they also discuss the regress caused by evaluating the evaluators. This is a direct antecedent for cost-sensitive selection over procedures. It does not explain the origin of the supplied utility or guarantee that another level of optimization closes that origin question. Their single-step approximation can miss steps that only become useful through later computations, so a negative immediate return is not a general stopping theorem. [Russell and Wefald, *On Optimal Game-Tree Search using Rational Meta-Reasoning* (IJCAI 1989), official full text, §§2–4](https://www.ijcai.org/Proceedings/89-1/Papers/053.pdf).

**Bandit selection learns an unknown payoff, while assuming what counts as payoff.** Auer, Cesa-Bianchi and Fischer specify a fixed finite set of arms and observed rewards from repeated choices. Their basic stochastic model assumes independent, identically distributed rewards within each arm and independence across arms. UCB1's finite-time expected-regret guarantee uses rewards supported in \([0,1]\) and compares against the arm with greatest expected reward. No prior knowledge of those distributions is required, but the reward interface, available arms, and repeated-play setting are already given. Treating candidate generators as arms is therefore an ordinary reduction, conditional on meaningful repeatable trials and feedback. Irreversible evidence deletion, depletion, or policy-dependent changes to later opportunities can violate that simple reduction. [Auer, Cesa-Bianchi and Fischer, *Finite-time Analysis of the Multiarmed Bandit Problem* (2002), author-hosted full text, §§1–2 and Theorem 1](https://homes.di.unimi.it/cesa-bianchi/Pubblicazioni/ml-02.pdf).

**Unknown future requests permit useful guarantees without a future-task distribution.** Sleator and Tarjan study online paging with fixed-size pages, limited fast memory, and slower memory from which evicted pages remain recoverable. A miss has stipulated unit cost. Their lower and upper bounds compare online rules with an offline rule that knows future requests; LRU has a worst-case competitive guarantee despite lacking a request distribution. This prevents the overclaim that unknown futures make all warranted retention policy impossible. The guarantees are conditional on the storage, cost, and comparison model, and do not promise the exact best decision for every sequence. Recoverable eviction also differs from irreversibly discarding historical evidence. [Sleator and Tarjan, *Amortized Efficiency of List Update and Paging Rules* (1985), author-hosted full text, §4, Theorems 5–6](https://www.cs.cmu.edu/~sleator/papers/amortized-efficiency.pdf).

The relevant sections of all three papers were checked in full text. These are formal/computational comparators, not evidence that the present architecture has acquired a selector. No novelty is claimed for expected-value computation, bandit updating, or online retention itself.

## Exact limits without an unrestricted impossibility claim

Consider two equally costly policy options: preserve evidence item \(A\), or preserve item \(B\). Capacity permits one item; a discarded item cannot be reconstructed. Before selection the learner's accessible state is identical in two permitted continuations. In one, the next required use needs \(A\); in the other it needs \(B\). Keeping the needed item succeeds and keeping the other fails. No deterministic selector choosing between these two options is best in both continuations. A randomized selector choosing \(A\) with probability \(p\) has respective success probabilities \(p\) and \(1-p\); its worst-case success is at most one-half. The future can be fixed before the random draw, so this argument does not require an adversary who sees that draw.

This example excludes a universally exact best selector for this explicitly restricted action menu. It leaves open minimax, competitive, Bayesian, learned-distribution, and task-specific policies. It does not show that memory selection is futile or that retaining everything is always feasible or useful. Allowing arbitrary encodings requires a separate information argument: to answer every coordinate query of an arbitrary \(n\)-bit historical record exactly, the retained encoding must be injective, since two different records differ in some coordinate. Fewer than \(2^n\) possible retained states cannot provide that guarantee. A prior restriction on the records, a narrower query family, approximate answers, or an external archive changes the problem.

A parallel generator example has the same form. Two candidate-generation recipes require the same present cost and are indistinguishable by all presently accessible evidence, but each supplies the useful candidate in a different admitted continuation. Without further information, a criterion for trading the alternatives, or resource-mediated selection through later consequences, the current record does not warrant declaring either uniformly superior. Merely adding an oracle estimate of future usefulness supplies the missing distinction.

## What the actual terminal state permits

The saved [results](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/results.json) record these completed continuations:

| Retained current model | Fuel | Source packets | Live logical cells |
|---|---:|---:|---:|
| H3 after unchanged apparatus | \(72475/65536\) | 0 | 33 |
| H4 after declared phase insertion | \(64123/65536\) | 0 | 35 |

These are inherited outcomes, not a newly provisioned experiment. The currently exposed revision port supports action and read, and credits no resource income. Every native operation costs at least \(1/4\), before preparation, rent, commits, or retention. Therefore the H3 and H4 branches permit at most four and three additional native operations respectively within that interface. This is a lower-bound accounting argument; it is not a claim those maxima are attainable by a complete policy.

The H4 branch cannot pay even the stipulated installation surcharge of one for a newly installed mechanism. H3 can pay that surcharge alone, so excluding its installation requires the full positive preparation/write/rent bill for a specified mechanism. Neither statement excludes already installed cheaper operations, a different physical implementation, future resource arrivals, or unmodeled interfaces. An honest stopping result names the interface and charges to which it applies.

More generally, if accessible resources start at \(B<\infty\), no income is possible through the admitted interface, and each counted experimental operation costs at least \(c>0\), at most \(\lfloor B/c\rfloor\) such operations can occur. Charging still more meta-selection levels cannot remove this bound. Conversely, the bound says nothing about how the system should trade the finitely available operations; deriving that choice needs more than accounting.

## A constructive continuation's admission conditions

A positive study would need to identify, before computing results:

1. Which generators or retention policies are physically available, how their differences arise, and what installation, execution, and retention cost.
2. Which consequence channel the system can itself access, or which direct material consequences differentially preserve the competing mechanisms. Hidden evaluator labels cannot substitute for this connection.
3. How a consequence changes subsequent policy availability or selection through an implemented update, including the update's own costs and failure modes.
4. Which resource stream supports repeated selection, which temporal/task assumptions justify transfer, and how irreversible loss and incompatible future demands remain represented.

These conditions permit supplied local mechanisms where they are labeled. They prevent presenting an externally supplied optimizer and objective as a derivation of their own origin. Compare any eventual mechanism with ordinary metareasoning, bandit, or retention policies under the same accessible evidence and resources. Separate proof, executable synthetic outcomes, and any later empirical identification.

For the present branch, the stronger research move is to establish the terminal resource bound, preserve the unavailable interfaces, and state the exact no-universal-retention result. That is a completed assessment of this continuation's limits. It leaves the governing generative-foundation objective open: the next positive bridge must obtain a consequential selection mechanism and a viable resource loop, rather than receive them invisibly through the analyst's success measure.
