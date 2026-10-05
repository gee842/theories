# How continuation capacity becomes actual behavior

This cycle advances the theory from feasible responses to **the mechanisms that actually choose, learn, and transmit them**. The choices now depend on available funds, retained observations, installed apparatus, and an explicit decision rule. The rule's objective and basic update procedure remain declared assumptions.

The strongest new result is a mechanism for losing future capacity through a locally successful choice. In the repair model, a one-cycle planner's first repair succeeds and leaves more cash than the alternative, but it also makes sustainable repair unaffordable. A two-cycle planner builds the sustainable design. A short-horizon successor can then maintain that inherited design successfully. Building, choosing, inheriting, and maintaining capacity have different conditions.

The [adoption study](adoption-dynamics.md), [paid-learning study](paid-learning.md), and [selection and scale theorem](selection-and-scale.md) solve distinct declared problems under a common operational framework. Their proofs and checks do not constitute an empirical universal law or an explanation of every form of evolution.

## From possible control to an implemented process

The earlier capacity question asks whether some admissible policy can meet a declared duty. The next question fixes the actual decision mechanism and follows its consequences.

Represent its configuration as

\[
z_t=(q_t,g_t,m_t),
\qquad z_{t+1}\sim K_\sigma(\cdot\mid z_t),
\]

where `q` includes the physical process, assets, access, and cash; `g` is the current rule or program; and `m` is its real retained memory. `Kσ` contains the actual action selection, environmental law, observation delivery, learning updates, and any succession channel, in their stated order. A deterministic mechanism is a special case. A robust analysis instead admits a declared set of environmental transitions.

This adds causal content to the theory. A winning policy does not have to be inserted by the analyst at every step. A specified controller may choose a different action; a paid observation may alter its estimate; a lost register may prevent that update; a successor may inherit assets while using a different rule.

Four objects therefore remain distinct:

| Object | What the model now determines |
|---|---|
| Feasible capacity | Which duties some permitted controller can fulfill |
| Actual selection | Which action the implemented rule chooses from its information |
| Learning | How observations and paid memory change a retained estimate and later action |
| Transmission | Which assets, records, programs, and permissions reach a successor |

These mechanisms can interact through the configuration. Their existence does not imply that selection improves the protected capacity, that more information is always worth buying, or that retaining one institution is the right duty.

## A successful action can eliminate future continuation

The main experiment retains the previous eight-module repair process. Every module needs diagnosis, authorization, and execution. Diagnostic channels are shared; all production stops until repair finishes. Fault waves occur exactly eight slots apart and repairs must finish within six slots. Operating support, diagnostic upkeep, and repair stages are all paid.

At each fault boundary, the controller can buy additional channels at 30 units each or discard channels without refund. It starts with cash 240, no channels, and a cash cap of 240. These purchase and removal actions are new compared with the earlier fixed-design experiment.

The actual rule forecasts the next `h` complete cycles, chooses the payable design sequence leaving the greatest terminal cash, executes its first choice, and replans at the next boundary. It uses no infinite-viability filter. If its preferred horizon is unaffordable, it uses the longest shorter feasible horizon. Its model knowledge, objective, and computation are supplied.

At the first decision, two channels leave 140 after one cycle, three leave 134, and four leave 128. A one-cycle planner chooses two. A two-cycle planner chooses four because this leaves 136 after two cycles, exceeding the best alternatives.

| Realized outcome | One-cycle planning | Two-cycle planning |
|---|---:|---:|
| Installed channels | 2 | 4 |
| Cash after cycle 1 | 140 | 128 |
| Cash after cycle 2 | 100 | 136 |
| Cash after cycle 3 | 60 | 144 |
| Fourth fault | Complete repair unavailable | Continues |

The important boundary appears **before** the fourth fault. With `k` channels already installed, exact indefinite continuation capacity in this model is

\[
\boxed{b\ge88+30\max(4-k,0).}
\]

Four channels need 88 cash for the next repair and then earn a net eight per complete cycle. Fewer channels require purchasing the missing apparatus first. Every complete cycle using a smaller design loses support, so detours cannot finance the missing upgrade. Larger installed designs can discard excess channels and use four.

Thus `(240,0)` begins inside the viable set, but the short-horizon rule's first successful cycle ends at `(140,2)`, which needs 148. **It has lost the capacity to continue indefinitely under any admitted policy.** Changing to a more farsighted rule afterward cannot rescue that state without additional resources or a changed repair route.

The alternative ends at `(128,4)`, safely above its requirement of 88. The proof gives an invariant for all subsequent cycles; the conclusion is not extrapolated from a long simulation.

This makes the feedback in the original idea concrete: an action selected for its current result changes the conditions under which later changes can become effective. The cash balance alone obscures it. The initially preferred outcome has more cash, but the other outcome has the apparatus that makes its cash sufficient.

## Adoption and succession can favor different rules

The same short-horizon rule that fails to build four channels retains them when they are already installed. For every inherited cash level from 88 to 240, it chooses four and maps cash to `min(240,b+8)`.

A successor can therefore remain viable by inheriting the sustainable apparatus even if it does not inherit the predecessor's longer horizon. Physical assets carry part of the difference. This is a constructed result about this process; it does not establish that existing institutions deserve preservation or that inherited practices remain appropriate after circumstances change.

The financing threshold helps explain adoption. Under an ample-funding, nonbinding-cap comparison between two fixed-return designs, let the more expensive design add installation expense `A` and improve each cycle's cash return by `Δg>0`. A terminal-cash planner favors it precisely when

\[
\boxed{h\,\Delta g>A,}
\]

with the supplied lower-cost tie rule at equality. Here `A=60` and `Δg=48`, so one cycle rejects the investment and two cycles favor it. This comparison assumes the installation payment is possible. A longer forecast cannot create the missing first payment.

Two controls prevent an automatic preference for maintenance. With no faults, zero channels permitted, and a nonbinding cash cap in that control, the same rule chooses no diagnostic apparatus. With the duty ending after one completed cycle and costless harmless closure explicitly permitted, two channels fulfill the finite duty and leave the greatest cash. Indefinite continuation is one declared test among others.

## Learning changes adoption only through usable evidence

The [paid-learning model](paid-learning.md) makes the actor uncertain about a persistent regime. In the base case, the high regime has fault probability `1/2`, the low regime has probability zero, and the supplied prior assigns probability `1/5` to the high regime. Probe outcomes and the later deployment fault are independent conditional on that regime.

The controller chooses a fixed number of probes before observing them. Each costs 0.08; retaining one memory bit costs 0.02 per probe interval. Its actual register can retain whether any probe was positive, retain the count, retain only the last sample, or lose the evidence. Its deployment decision receives only the final physical register. It cannot consult the analyst's observation history.

Maintained readiness costs one and reduces a later fault's repair bill to six; the substitute repair costs fourteen. The supplied selector minimizes expected learning expense plus deployment expense and a separately declared loss if repair is unaffordable. Actual cash and that imputed loss are recorded separately.

With fifteen cash units, two probes and a retained “any positive” bit are optimal among the declared candidate protocols. They reduce the expected score from 1.4 without inquiry to 1.15. In the high regime, the actor adopts readiness with probability `3/4`; in the low regime it never does. The decision is an outcome of acquired evidence and the specified update rule.

For the admitted `N=0,…,8` probes with that register in the funded base case, the exact score is

\[
J_N=0.8+0.6\,2^{-N}+0.1N.
\]

The last term pays for obtaining and retaining the evidence. This displays a finite tradeoff between reducing uncertainty and consuming support. Erasing the bit restores the prior-based decision while leaving the inquiry bill paid. Increasing observation or memory prices can make no inquiry the selected protocol.

The memory representation matters when the regimes overlap. In a separate control, one positive observation and two positives call for different decisions. A count register then outperforms the “any positive” register despite its larger retention cost. This is selection among a supplied representation menu, not invention of an unrestricted new concept.

### An expected-score improvement can accept a loss of guarantee

At starting cash eight, the same two-probe protocol minimizes the supplied expected score but has failure probability `1/40`. The retained evidence can miss the high regime, leading to no maintenance and an unaffordable substitute repair when a fault arrives.

Yet always maintaining without probes costs at most seven and repairs every admitted deployment fault. A sure-feasible controller exists; the expected-score selector chooses a different tradeoff. The result distinguishes criteria rather than calling either calculation mistaken.

There is also a direct support limit on learning. Starting from 7.1, paying 0.2 for two probes and their register leaves 6.9, below the seven needed to maintain and repair a fault. The funded two-probe procedure has consumed the margin required for the sure guarantee. The actual score-minimizing protocol at that starting cash uses one probe instead. This retains the physical option to maintain, while its chosen action rule still accepts a 0.05 failure risk. Acquiring information and retaining the ability to act on it are separate requirements.

These are finite deployment episodes. They do not establish that a learning process finances itself indefinitely, discovers its own likelihood model, or safely explores an unknown world without resets.

## A rule must survive its own succession process

The [transmission model](selection-and-scale.md) isolates another mechanism. Each operating cycle starts with two reserve units, then owes one service unit and one succession unit. An external receipt of two arrives **after** succession has been paid.

A reserve-preserving operation produces one unit of visible output without using reserve. A consuming operation produces two output units but spends one reserve unit. Output is not a cash receipt. The first rule completes every cycle; the second reaches the succession payment without enough cash.

An initially successful rule can still fail if transmission changes it. Suppose each paid handoff independently corrupts the preserving rule into the consuming rule with probability `μ`, and corruption is irreversible in this model. Then

\[
\boxed{\Pr(\text{complete }N\text{ cycles})=(1-\mu)^{N-1}.}
\]

The first cycle is completed before its handoff can affect the next one. Any positive fixed corruption probability makes infinite survival probability zero under this particular channel law. This concerns a specified vulnerable mechanism; it does not imply that every succession process inevitably fails.

The physical plant still admits a successful controller. That existence does not give the installed corrupted program a free means to replace itself. Paid transmission, reliable transmission, and the availability of a good rule are distinct facts.

This experiment models inheritance and transmission fidelity. Population-level differential reproduction or imitation would require an additional contribution and population-update mechanism. It is not established merely because a label is copied.

## The stronger condition for transfer across scales

A capacity-preserving map says that an effective controller can be implemented at another level. Certified transfer of actual behavior requires the induced closed-loop dynamics to correspond, including learning and transmission effects relevant to the test. Internal procedures need not be literally identical when their joint observable behavior agrees.

The new theorem supplies two forms:

- For robust statements, every actual concrete transition must have a corresponding actual abstract transition, with the required information, payment, safety, and timing obligations preserved.
- For probabilistic statements, the **joint law** of the next event and state must map correctly from every relevant detailed state. Matching possible outcomes or separate one-time frequencies is insufficient.

Under the exact joint-kernel condition, corresponding initial distributions give equal observable trajectory laws. Under a uniform one-step total-variation error `ε` and initial error `δ`, the finite-horizon trajectory discrepancy is at most `min(1,δ+Nε)` after `N` steps. That approximate bound alone supplies no infinite sure guarantee.

For the actual planning rule, a useful special case is a bijection between feasible planning trees, a positive affine transformation of terminal scores, preserved tie order, and corresponding replanning updates. The adopted actions then transfer too.

The repair experiment checks a physical replication: multiply modules, cash, cap, and admissible channel counts by the same integer. Durations stay fixed, every financial quantity scales, and the terminal-cash ordering is preserved. Both the short-horizon failure and longer-horizon continuation transfer. The replicated menu is restricted to the exact scaled image; admitting extra intermediate designs would change the decision problem.

This makes the cross-scale thesis more demanding and more useful. The same feasibility constraints can apply while outcomes change. To predict the same **actual** behavior under a scale change, the selection, learning, and inheritance mechanisms must also be mapped.

## What this cycle establishes

The theory now contains explicit mechanisms for three formerly open links: adoption from known financial forecasts, adoption from paid uncertain evidence, and succession through a paid transmission channel. It also identifies when those mechanisms preserve or lose future capacity and what a faithful change of scale must retain.

The ingredients connect to established control, learning, and transmission research. The [source audit](selection-audit.md) records the precise connections and access limits. For example, [Watkins and Dayan's learning theorem](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf) has explicit sampling and update assumptions; it does not supply a general guarantee that a resource-limited learner survives while gathering data. The current finite Bayesian example makes its own narrower assumptions and proves its own results.

All three computational checkers pass. The [claim register](CLAIMS.md) separates the formal results from constructed examples and open hypotheses, and the [verification receipt](verification/verification-receipt.json) preserves reproducibility information. Independent reviews checked the funding chronology, exact viable region, actual planning behavior, finite memory, transmission timing, and scale proofs. No empirical observations were collected.

The next explanatory bridge is selection **among the selectors themselves**: who gets copied, appointed, financed, or replaced, based on which measured outcomes and over which window. A concrete next model should hold the renewal process fixed, let early and delayed outcomes affect contributions to successors, report absolute continuation alongside variant shares, and charge the observation and transmission mechanisms. This would test whether locally favored decision rules spread before their deferred costs become visible. It would extend the present theory without assuming that selection must protect viability.
