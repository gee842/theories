# Recursive future capacity under paid succession

Research candidate / internal mathematical analysis. Prepared 5 October 2026. This memo applies finite viability and resource-accounting methods to constructed succession. It does not claim a new universal invariant, a novel general dynamic-programming theorem, or a scalar definition of health.

## 1. The question that a present solution does not answer

A system can currently solve a task, or even possess solutions to many tasks, while lacking an affordable way to deliver a capable successor. The relevant new contract is not merely “respond correctly now.” It is:

> Respond to the announced task through actual construction and validation, pay the handoff, and leave a successor from which this obligation remains feasible for subsequent tasks.

This is more demanding than current performance, but it is not outside generic viability theory. The existing root foundation's attainable response profiles already permit history-dependent consequences, and its composition result already covers paid mode changes. Bounded recurring service is also already represented there by deadline counters. Calling the new contract a different fundamental invariant would rebrand those results.

What adds operational content is specifying and measuring how a constructed artifact changes the next state's available constructions, validation costs, and transfer requirements. The quantitative result below distinguishes an ample but exhaustible initial endowment from recursively affordable capability. It permits different successive forms and does not require copying the incumbent.

## 2. A succession state and an independently specified resource account

Let `z` range over a finite set of productive configurations. It records the tools and components actually delivered, retained evidence with its valid scope, the available construction and checking interfaces, and any environmental memory relevant to future tasks. A configuration is not merely its displayed output. All independently protected nonresource requirements are included in the admissible state definition.

Let `b>=0` be a single genuinely fungible resource balance. This could be a declared work budget. The model does not add unlike things such as legitimacy and processor time into one unit.

At each episode, a task `q` is announced from a finite nonempty set `Q(z)`. Announcement is an actual information interface, not analyst access to a hidden correct answer. The process selects an available episode policy `a` from the finite set `A(z,q)`. Such a policy must construct a response, validate it under the declared correctness contract, provide the required service by its deadline, and deliver a successor. Its execution has three independently assessed consequences:

- `c(z,q,a)>=0`: the maximum cumulative net resource draw at any intermediate point relative to the opening balance, accounting for receipts when actually delivered and including construction, checking, and handoff;
- `d(z,q,a)`: net resource expenditure over the episode, after actual receipts;
- `f(z,q,a)`: the delivered successor configuration.

The transition is feasible when `b>=c`, and ends at `(f,b-d)`. Physically consistent accounting has `c>=max(0,d)`. A net-positive receipt is not free energy: its source and conditions of delivery must be part of the declared model. If replenishment is an external recurring allowance, say so. If earned from successful service, count it only when actually delivered.

Failure to solve or hand off is not admitted as a successful transition. A program that only halts on favorable inputs must not receive a certificate for universal correctness. When a policy has internal trial branches, its costs and outputs must include those branches. The simple result below uses deterministic episode transitions; robust branches can be included by taking a worst-case maximum over their specified outcomes. Expected performance and probabilistic reliability require different contracts.

## 3. Minimum reserve for successive changed tasks

Define `H_n(z)` as the smallest initial resource balance sufficient to complete the next `n` task episodes, for every task sequence permitted by the model, with the task observed before choosing its response. Use extended nonnegative values, with infinity for impossibility. Then

\[
H_0(z)=0,
\]

\[
\boxed{
H_{n+1}(z)=
\max_{q\in Q(z)}\min_{a\in A(z,q)}
\max\bigl\{c(z,q,a),\ d(z,q,a)+H_n(f(z,q,a)),\ 0\bigr\}.
}
\tag{S1}
\]

The minimum over an empty action set is infinity. If tasks must follow a change pattern rather than repeat arbitrarily, encode its automaton in `z` and `Q(z)`. If the task is not observed, the selector must use a common action or an observation-based episode policy; the displayed max–min order must not grant unavailable knowledge.

### Proposition S1: exact recursive reserve and a succession certificate

For finite states, tasks, and actions with the declared deterministic accounting, (S1) is the exact minimum reserve for `n+1` episodes. Moreover, put

\[
H_\infty(z)=\sup_{n\ge0}H_n(z).
\tag{S2}
\]

Starting at `(z,b)`, indefinite response and paid succession against every permitted task sequence is possible if and only if `b>=H_infinity(z)`. Where this quantity is finite, a task-dependent choice of episode policy can keep

\[
\boxed{b-H_\infty(z)\ge0}
\tag{S3}
\]

through all successions, even while `z` changes.

**Proof.** For a chosen task and episode policy, the initial balance must finance its peak draw `c`, and its ending balance `b-d` must finance the remaining `n` episodes. These are exactly the inequalities inside (S1). Taking the best available policy after each announced task and then the worst possible task proves the finite recursion by induction.

The operator in (S1) is monotone, and `H_1>=H_0`, so `H_n` increases. A finite minimum commutes with the limit of increasing sequences: if every candidate limit exceeds a threshold, all candidates exceed that threshold after some common finite index. Finite maxima and the displayed affine operations also commute with this limit. Thus `H_infinity` is a fixed point of (S1). Where it is finite, for every announced task a minimizing action exists and satisfies `c<=H_infinity(z)` and `d+H_infinity(f)<=H_infinity(z)`. Starting with `b>=H_infinity(z)` makes that action executable and leaves `b-d>=H_infinity(f)`. Induction establishes the infinite claim. Conversely, a policy that succeeds indefinitely must suffice for each finite prefix, and therefore requires `b>=H_n(z)` for every `n`, hence `b>=H_infinity(z)`. ∎

This is a standard finite resource/viability dynamic program specialized to paid construction and succession. Its value here is the measurable distinction it induces, not theoretical priority. `H_infinity` is relative to the announced task family, allowed disturbances, resource accounting, available tools, and protected outcomes. It is not a universal numerical measure of health.

For stochastic but bounded episode branches, the inner certificate becomes the maximum of `c_w` and `d_w+H_n(f_w)` over all allowed outcomes `w`. This yields a hard guarantee only when every admitted branch can meet the contract; rare possible failure cannot be averaged away. A finite chance-constrained experiment should report its probabilities instead of invoking this robust certificate.

## 4. A concrete threshold separating solved artifacts from productive inheritance

Consider a restricted mode whose full pipeline cost for task `q` is `C_q>0`, paid before a recurring receipt `r>=0`. After the handoff, the same functional toolkit is again delivered, so `f(z,q)=z`, `c=C_q`, and `d=C_q-r`. “Same toolkit” means actual maintained or reconstructed capabilities; the displayed solution can change each episode. Suppose all task sequences are allowed and let `C_max=max_q C_q`.

Then

\[
\boxed{
H_n(z)=C_{\max}+(n-1)(C_{\max}-r)_+,\qquad n\ge1.
}
\tag{S4}
\]

Consequently,

\[
\boxed{
H_\infty(z)=
\begin{cases}
C_{\max},&C_{\max}\le r,\\
\infty,&C_{\max}>r.
\end{cases}}
\tag{S5}
\]

**Proof.** In this restricted mode, (S1) reduces to `H_(n+1)=max(C_max,C_max-r+H_n)`; direct induction gives (S4), and its limit gives (S5). The worst task can recur. If it cannot, use the actual task-transition model rather than substituting its maximum. ∎

The conditions include liquidity as well as net balance. Even when `C_max<=r`, a system beginning with `b<C_max` can fail before the receipt arrives. An eventual return cannot finance work that must already have occurred.

When `C_max>r`, a rich initial balance can conceal depletion. If `b>=C_max`, the number of worst-case episodes that can be completed is exactly

\[
1+\left\lfloor\frac{b-C_{\max}}{C_{\max}-r}\right\rfloor.
\tag{S6}
\]

This predicts a failure horizon from independently measured costs. It does not retrospectively define every failure as lost generativity.

### A matched-output example with the same external flow

Two initial configurations have the same correct current answer, resource balance `b=9`, and first-episode cost five. In both cases the next task is announced before its response is selected, every completed episode returns three resource units **after** the construction/checking/handoff work, and all offered responses are correct. Both consequently have `H_1=5`.

The first initial configuration delivers a successor that requires five units for every later task as well. Its reserves satisfy `H_n=5+2(n-1)`. Starting with nine units, it completes three episodes and cannot finance a fourth: its balances after the three receipts are seven, five, and three.

The second initial configuration's equally costly first handoff delivers a reusable productive interface. Subsequent tasks cost either two or three units, including their onward handoffs. Its later reserve requirement is three; its initial reserve requirement is `max(5,2+3)=5` for every positive horizon. With the same initial nine units and the same three-unit external flow, it remains affordable under every sequence of the two supplied tasks.

The checked certificate assigns potential five to the second initial configuration and three to its repeatable successor. Every allowed task admits an episode whose peak draw is at most that potential and whose net cost plus successor potential is no greater. That induction, not a finite successful run, establishes the conditional infinite-horizon claim. The useful interfaces and costs are stipulated in this toy witness; the actual circuit experiment investigates how real constructed packages produce different finite costs.

### Receipt timing in the circuit experiment

The stationary illustration above credits `r` after work. The actual `experiments/constructive-succession/model.py` credits `flow` at the **start** of each episode, before service, target acquisition, search, checking, installation, and handoff. The general recursion handles either convention, but their finite liquidity bounds differ.

For a stationary pipeline with task maximum cost `C_max` and a guaranteed start-of-episode credit `r`, a balance measured immediately **before** that credit has `c=max(0,C_max-r)` and `d=C_max-r`. The minimum opening balance for `n` tasks is then

\[
\boxed{H_n^{\rm precredit}=n(C_{\max}-r)_+.}
\tag{S7}
\]

Equivalently, measure the state immediately after the current inflow and apply (S4). The indefinite affordability threshold remains `C_max<=r`; the required initial liquidity changes. A receipt unavailable after failure must not be borrowed before it arrives. The circuit experiment has changing packages and costs, so (S7) is a stationary comparison, not a fit to its outcome trajectories. Four successful handoffs do not certify indefinite viability.

### A factorial inheritance witness

Suppose the construction experiment independently obtains these total per-episode costs on its repeated changed-task class:

| Delivered inheritance | Build, validate, and pay handoff | Recurring receipt |
|---|---:|---:|
| Current solution only | 14 | 9 |
| Reusable tools | 11 | 9 |
| Reusable evidence | 11 | 9 |
| Both tools and evidence | 8 | 9 |

For example, each inheritance channel can save four units of work while costing one to maintain and transfer, for a net saving of three. Only the joint mode crosses the recurring affordability boundary. This is **additive cost savings crossing a feasibility threshold**, not proof of a mysterious interaction between tools and evidence. A finite run can show a large interaction on survival even when the underlying work reductions are additive.

All modes can be given equal initial balances, answer correctness, and first-task output. Their later behavior differs because delivered capabilities alter subsequent pipeline costs. A large solution archive or reserve can outperform a toolkit initially while still having unbounded `H_n` if it cannot replenish what each episode consumes.

If tasks do not reuse the retained components, their construction savings can vanish while transfer costs remain. Then inheritance can lower performance. Likewise, evidence about a previous artifact does not automatically validate a changed artifact. Reuse requires an explicit transport contract: identical component semantics and inputs, or a checked composition rule. Validation on a different task cannot simply be relabeled inherited correctness.

## 5. Structural predictions for the constructive experiment

1. **Equal current answers can mask different recursive reserves.** Match first-task correctness and initial balances, then change task compositions. Tool and evidence inheritance should help only when they reduce measured future costs or expand actual construction paths.

2. **A second handoff is diagnostic.** A funded initial package can temporarily rescue a successor. If that successor cannot pay to deliver the package onward, the apparent improvement should disappear on later transitions. Do not reset budget, tools, construction records, or evidence between generations.

3. **Terminal breadth can misrank continuing capacity.** Count ready solutions separately from feasible new constructions and from `H_n` or its finite empirical analogue. One-step coverage can improve while the resources needed for repeated response grow faster.

4. **Threshold interaction should be explained by costs.** If tools plus evidence succeed where either alone fails, test whether their measured cost reductions simply cross the renewal boundary. Compare both cost trajectories and completion rates.

5. **Liquidity and deadlines matter independently of averages.** A mode with positive long-run balance can fail during a costly construction or transfer. Record peak draw and actual intermediate resource balance, not only final net expenditure.

6. **Unrelated tasks provide a meaningful negative control.** If retained components or valid evidence do not apply, transfer overhead should reduce or eliminate the advantage. A universal improvement from inheritance would invite examination of uncharged costs or hidden access.

7. **Selection and delivery remain separate.** A good pipeline that exists in the action set but is not selected or authorized establishes possibility only. Compare the installed policy's choices and delivered artifacts with the best feasible finite policy where calculation permits.

These are predictions for a supplied bounded grammar and explicitly sampled task process. No finite circuit experiment can establish unrestricted creation of new goals, ontologies, or all future responses. A changing displayed program is not by itself evidence that the construction rules have changed.

## 6. What the recursive formulation contributes

The meaningful continuity is neither an immutable solution nor a conserved count of options. It is an affordable sequence of causal handoffs that repeatedly puts actual responding and further construction within reach. Closed or recurrent viable sets express that mathematically once the contract is specified; they do not supply the mechanisms or values by themselves.

The resource potential above makes three independently testable claims possible: predict the reserve required for a finite succession horizon; predict when a one-time advantage must be exhausted; and identify how a delivered tool or valid piece of evidence changes future pipeline costs. Reconstructing those costs from observed failures would make the exercise circular. Measure the interfaces and costs first, freeze the task process, and test withheld changed tasks and later handoffs.

For shared health, the contract must still identify whose service, burdens, standing, and continuity count. The end of an institution can satisfy it if participants and protected commitments continue through other arrangements. Relabeling successors cannot erase losses to particular people. The mathematics characterizes recursive feasibility of an explicitly chosen contract; it does not derive the contract's ethical legitimacy from survival.

## 7. Independent exact verification

[verify_reserve.py](verify_reserve.py) independently materializes complete contingent policy trees for a toy graph with three productive configurations, two announced tasks, and two possible responses per task. It scores each tree by rolling out every task word and calculating the largest actual prefix draw, without using (S1) to score the tree. The minimum agrees with (S1) in all checked cases through three episodes: 49,356 policy trees and 394,008 task rollouts. Additional exact rational-cost cases agree through two episodes.

A separate direct enumeration of task words checks 2,100 stationary formula cases across task costs one through five, receipts zero through six, horizons one through six, and both pre-work and post-work receipt timing. The matched-output witness above is checked across twelve horizons and by its explicit inductive potential certificate. Another check reverses the task/action quantifier order: cheap task-specific responses require reserve one when the task is announced, but hiding the task before action yields the escalating requirement `4+3(n-1)` in that constructed example. The observation interface therefore changes the answer.

All checks passed; [RESERVE-VERIFICATION.json](RESERVE-VERIFICATION.json) records the exact results. These finite numerical checks corroborate the calculations and catch timing or quantifier mistakes. They are not empirical validation, a substitute for the proof, or evidence of indefinite success by the circuit experiment.
