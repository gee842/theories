# When an issued operation actually completes

6 October 2026. AI-authored continuation of [protocol composition](PROTOCOL-COMPOSITION.md), under the same [five foundation requirements](GENERATIVE-GROUNDING.md#completion-of-the-unified-foundation). **Accepted conditional result:** the fresh Lean 4.29.1 build passes 34 new theorem audits across three additive modules. Separate internal AI review accepts the mathematical and source scope; the full unified foundation remains ongoing.

The connection is physical execution → a delivered observation or update → continued use from the actual resulting state. The earlier composition theorem relates **completed** physical operations to abstract learning steps. It deliberately does not establish that an issued operation can finish. The present contract addresses that missing implication without adding a learning apparatus or changing a physical law.

## The three additional conditions

Fix the actual micro-event process, the command committed for this operation, and its completion boundaries. The command's permitted events remain a restriction of that actual process. Let `D` be a declared domain of states in which the operation can continue, and let `r` assign a natural-number rank to those states. Require:

1. **An enabled next event.** Every state in `D`, including an admitted entry state, has at least one actual permitted next event.
2. **Preserved ability to continue.** Every permitted successor that is not yet a completion boundary remains in `D`.
3. **Strict internal progress.** Every such nonboundary successor has a smaller rank.

These conditions cover every permitted branch, not just a chosen successful trace. If loss of funding, interruption or an environment response can occur, it must satisfy the same conditions or put that application outside this contract. A decreasing rank cannot create an enabled event, and an enabled event alone cannot exclude an infinite loop.

The proved conclusion is precise: starting in `D`, every maximal discrete execution of the committed operation reaches its first subsequent boundary after at least one and at most `r(start)+1` micro-events. A finite execution that stops unfinished while an event remains enabled is an incomplete prefix, not a maximal execution. An external scheduler that simply declines to take further events is not certified by calling that prefix a run.

**Argument.** Strict descent bounds unfinished paths. Preservation keeps every unfinished endpoint inside `D`, and enabledness excludes finite deadlock there. Consequently a maximal operation can neither remain internal indefinitely nor end internally. It must reach a boundary, and the existing block bound limits its length. The [mathematical specification](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROTOCOL-COMPLETION-MATH.md) supplies the exact quantified statement.

This is a sufficient bounded-completion contract. It is not a necessary characterization of every terminating process, and it does not establish elapsed time, fairness of an external scheduler, or almost-sure completion under a probabilistic law. An always-available internal self-loop violates its rank condition even if another available event completes the operation.

## Completion is not success by definition

A completion boundary may retain success, a recorded failure or another distinguished result. The proof must preserve whichever outcomes the actual process admits. A claim that the desired task succeeds needs a further outcome proposition.

A paid deadlock is not automatically a completed failure report. If the process has no physical abort, reporting or reset event from that state, assigning it a label does not give a controller a new observation or permission to continue. Likewise, a refused entry need not count as an issued operation. Both remain visible limitations on where the contract applies.

The observation and next memory must still be decoded from the actual boundary states through the existing implementation contract. The new completion conditions do not create an observation channel, authenticate its meaning, or supply a free memory register.

If admission is claimed on the basis of an actor's incomplete information, the progress contract must cover every actual state compatible with that information. Restricting attention afterward to hidden states in which an operation could afford to finish does not establish an implementable guarantee. A sharper state-dependent mathematical guard and an observable sufficient admission rule are different claims.

## Resources remain at the actual boundaries

Each completed operation remains an actual micro-history. The existing account theorem applies at every cut, including cuts inside an operation. Future receipts do not pay an earlier bill; any required prepayment comes from event guards or a separately justified stronger account law.

For another operation to be guaranteed, the first operation's **actual endpoint** must satisfy that next operation's entry conditions. The checked finite-repetition corollary uses a boundary domain that admits the next decoded command and contains every actual returned successor. This one reusable domain supports any finite number of operations and is stronger than the horizon-specific premises needed for one funded finite job. It does not replenish source, reset a lease or repair a consumed component. Repeatedly proving the same one-operation contract with its initial resources restored would change the process.

In the existing paid example, usable fuel is spent before a source unit is converted into a return. With positive fuel and source, the nonstalling version completes in two events. A zero-fuel entry cannot start. A paid entry with no source becomes stuck internally. Adding an internal stall preserves every completed macro outcome while admitting an infinite busy execution. Consuming the final source unit allows that operation to finish but leaves the endpoint outside the next operation's guarantee.

## The actual predictor application

The contract is instantiated on the unchanged [paid predictor protocol](PREDICTION-PROTOCOL.md). Its continuing domain directly lists the remaining enabled phase guards and retained command. Its rank is three at entry, two after rent, one after work and zero after writing. Every finite maximal admitted trial follows exactly `[rent, work, write, finish]` to its actual `cycleEnd`, and no admitted infinite internal execution exists. This strengthens the earlier correspondence of completed trials with an actual completion guarantee at the declared entry states.

The sharp admission guard uses the deterministic work outcome when checking whether later writing is affordable. It supplies no advance sensor. A separately proved sufficient guard reserves current fuel for rent, work and writing, assumes maintenance does not exceed the matched packet return, and requires the existing score, packet and lease conditions. This guard covers a mismatch as well as a match. It remains a mathematical condition on current physical fields; accessible measurement and an installed admission controller are further claims. Actual observed shortages and returned states that cannot begin again are checked counterexamples to broader scope.

## Verification

The [reproducible package](../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/protocol-completion-README.md) contains 13 general results, eight paid-example results and 13 predictor results. The fresh build also checks 244 inherited theorem audits across the full 15-module dependency closure. Eight new results have no axiom dependencies; the remaining dependencies are limited to the declared standard `propext`, `Quot.sound` and `Classical.choice`. No custom axiom, admission or unchecked native decision is used. Counts describe audited declarations, not independent empirical confirmations.

The [review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROTOCOL-COMPLETION-REVIEW.md) separates source checking, prose interpretation and empirical limits. Failed proof attempts are retained as development provenance. No new physical experiment is claimed.

## Scope in the current foundation

The [application audit](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROTOCOL-COMPLETION-APPLICATIONS.md) distinguishes the paid example, the four-phase predictor, the complete stochastic exposure law and the acquired evaluator. Their transition laws and completion claims remain separate.

In particular, the accepted [evaluative-uptake construction](EVALUATIVE-UPTAKE.md) proves actual paid selected histories under explicit conditions. Its wider event repertoire also permits control-setting actions; no blanket termination theorem for all of those events is inferred here. The ongoing actual-successor and justified-revision studies retain their own contracts. Completing one operation is neither whole-learner succession nor indefinitely sustained correction.

This advances compatible composition, requirement 3, by identifying when a completed-history abstraction can also carry a bounded completion guarantee. It does not replace the central derivation of justified evaluative influence, its continuing use or its empirical identification. The common account becomes more informative by keeping possibility, actual completed effect and guaranteed completion distinct.

## Mathematical ancestry

The proof method is established total-correctness reasoning. Dijkstra's guarded-command account combines enabled alternatives with obligations on every allowed branch and uses decreasing quantities in termination arguments. The contribution here is its connection to this repository's actual protocol states, inherited memory and resource accounts, not a new method of proving termination. [Dijkstra, EWD472](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html).

Execution semantics matter. Lamport's treatment distinguishes safety, liveness and fairness and explains the role of stuttering in specifications. The present bounded micro-event claim must not be silently promoted into a real-time or unrestricted-scheduler guarantee. [Lamport, *Safety, Liveness, and Fairness*](https://lamport.org/tla/safety-liveness.pdf).
