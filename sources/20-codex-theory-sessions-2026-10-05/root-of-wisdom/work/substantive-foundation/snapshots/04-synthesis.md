# Revising a decision rule while recovery is still possible

Sixth research cycle, 5 October 2026.

The next formal step is complete: the evaluator itself can now detect a changed condition, retain evidence, and pay to revise its selection rule. **A population can still afford to learn and revise its rule, yet lack enough resources to put the corrected rule into operation.** In the main experiment, paid revision still succeeds at epoch 27; at epoch 28 the evaluator becomes correct but cannot fund a successor. The population under the unchanged evaluator remains alive until epoch 32.

A second result prevents an overly broad interpretation. A differently endowed population can maintain a mixture of rules that works through either environment without identifying which environment it faces. The common constraint concerns an executable response to the duty. Diagnosis is one way to obtain that response; a funded robust alternative can substitute for it.

These are conditional mathematical results and exact constructed examples. They extend the cross-scale account without establishing empirical universality or a general law that successful systems must learn.

## What has changed in the formal account

The previous cycle supplied an evaluator that copied operating rules using early or later evidence. This cycle makes the evaluator's calibration a changing physical state. A query does not directly set that state: its report must survive a handoff, the replacement must be installed, an executable operating program must remain available, and its next carrier must be funded.

The three questions from earlier cycles therefore acquire a fourth:

| Question | What must actually be established |
|---|---|
| Could a response work? | A feasible policy exists under the declared information, access, and resource conditions. |
| Will the current rule choose it? | The implemented controller's actions meet the duty. |
| Can it reach a successor? | Required code, assets, records, and operating reserve survive a funded handoff. |
| Can the rule itself be repaired? | The actual revision path reaches a usable replacement before its support is lost. |

The new [revision certificate](revision-and-scale.md) makes the last statement precise. A supplied information-consistent controller must keep every physical and financial prefix valid; a decreasing finite rank ensures that revision finishes; its endpoint must enter a class where the installed controller actually sustains the declared duty. The rank belongs to the proof, not to an unpriced oracle inside the controller.

This is a sufficient certificate, not a claim that every possible adaptation has this form. A known good endpoint alone cannot certify the route to it.

## A previously good forecast becomes wrong

The [population experiment](evaluator-revision.md) retains the actual S and L programs from the previous repair model. S plans one cycle ahead and installs two diagnostic channels. L plans two cycles ahead and installs four. Their operating cash after two cycles remains 100 and 136, respectively.

The changed environment is a settlement contract. It introduces a 66-unit basic-plant allowance and a charge of 24 per installed auxiliary channel. The allowance is an explicit external input; the charge is an actual payment. S now remits 118 and L 106. The same early operating reports that supported the old forecast still appear, but the old forecast of final remittances is no longer correct.

With the constant per-parent grant of 150, ordinary audit, custody, and the 260-unit successor packet, the renewal-potential changes are:

\[
\Delta\Phi_{\rm old}=-12N_S+24N_L-2,
\]
\[
\Delta\Phi_{\rm changed}=6N_S-6N_L-2,
\]

before extra query/rewrite bills and treasury spill. Here `Φ=260N+R` is a bookkeeping measure of replacement funding, not literal cash. The child's 240-unit cash endowment remains a transfer in the separate cash account.

Thus each pure rule has a regime in which it depletes. The old evaluator selects L; its corrected forecast selects S. Both program payloads and the evaluator's model and scheduling registers are kept in a paid archive. A correct new ranking cannot recreate a program that has disappeared from every available source.

## Recovery has its own deadline

The initial state contains two L parents, treasury zero, the old evaluator, and both stored programs. The changed contract begins by the first epoch. An epoch still lasts two repair cycles; all treatments use the same birth boundary.

One stale epoch leaves one L parent and treasury 246. Thereafter, that parent consumes eight treasury units per renewal. The correction procedure pays twelve for a contract query, two to carry its report across the handoff, and 24 to install the revised evaluator. The current parents have already operated when the report arrives; the new evaluator controls their successors.

| Route | Latest successful epoch along this stale trajectory |
|---|---:|
| Paid query, retained report, paid revision | 27 |
| Free signal, revision still costs 24 | 28 |
| All observation and revision charges waived | 31 |
| No correction | Extinction at 32 |

At epoch 27, the paid route leaves one S with the full working endowment and treasury zero. Its later renewal is funded under the continuing support contract. At epoch 28, the same route installs the correct evaluator but leaves only 252, below the cost of one birth. No remaining parent can receive another per-parent grant.

This distinguishes loss of **one available recovery route** from visible collapse and from loss of **every possible route**. Epoch 27 is the exact deadline for this implemented procedure. A cheaper permitted signal, different allocator, credit, or authorized blind revision can alter it.

The experiment also implements a monitor for an unknown single change time, possibly no change at all. It queries every `q` epochs until a retained report triggers revision, then stops querying. From the stated initial state, every onset is handled exactly when `1≤q≤27`. This all-onset result follows from a finite reduction of the old-regime trajectory to a capped state and clock phases, followed by a post-revision invariant. It is not inferred from a long successful simulation.

The report is a supplied perfect inspection of a known contract parameter. Treasury and late remittances are not delivered to this evaluator outside the query interface. Cheaper inference may be available to an observer with different access. The result neither proves that inspection is universally necessary nor covers endless unanticipated regime changes.

## More accurate belief can produce worse execution

The separate [noisy-evidence model](paid-revision.md) removes the perfect-report assumption for a finite handoff. It does not insert a noisy detector into the population process. Its own likelihoods, fees, reserves, and deadline are separately specified.

The environment is equally likely to require rule A or B. Each paid signal indicates the correct regime with probability three quarters, independently conditional on that regime. A finite counter retains the evidence. Switching from the current A rule to B takes additional cash and time; a usable successor also needs six units left over.

A supplied three-probe majority rule identifies the right label with probability `27/32`, about 84.4%. With enough reserve and time, it delivers the usable successor at that rate. But at reserve twelve, its observations consume six and a B revision would leave only four for the child. Its usable-delivery probability falls to `27/64`, about 42.2%—below the 50% achieved by simply keeping A.

A controller that includes execution costs in its objective takes one probe in that state and succeeds with probability 75%. An exact decision calculation, exhaustive policy enumeration, and an independent analytical bound agree. Under the stated three-probe grammar, the optimal success probability is:

\[
V(R,D)=
\begin{cases}
27/32,&R\ge14,\ D\ge4,\\
3/4,&R\ge10,\ D\ge2\text{ and the first case fails},\\
1/2,&\text{otherwise, for }R\ge6.
\end{cases}
\]

The improvement concerns a declared probability of funded, timely delivery. Because the base noisy reports overlap between regimes, no finite policy in this grammar guarantees success on every admitted report sequence. This distinction matters when connecting learning to earlier sure-continuation results.

## Diversity can substitute for diagnosis

The larger mixed-population control starts with three S, one L, and treasury sixteen. It has a supplied quota allocator that alternates this cohort with two S and two L. Copies and births remain paid; the allocator uses the same charged archive and a finite clock. It performs no query or evaluator rewrite.

| Current cohort | Old-contract change before spill | Changed-contract change before spill |
|---|---:|---:|
| Three S and one L | −14 | +10 |
| Two S and two L | +22 | −2 |

Either fixed environment gives a gain of eight over the two epochs before treasury spill. An unannounced change can instead produce the crossing `−14−2`, so the initial reserve must cover sixteen. A closed invariant verifies all possible one-time change positions and every payment boundary; four carriers remain funded.

This is a different initial population and an additional admitted allocation rule. It is not a demonstrated no-query recovery from the original two L parents with treasury zero. Its importance is conceptual: **the need to distinguish an environment depends on the affordable responses available under uncertainty.** If a common response works across the remaining possibilities, identifying the true one is unnecessary for that duty.

The [formal memo](revision-and-scale.md) states the exact last-decision criterion. With no further information before installation, let `A*(x)` contain the payable, authorized, timely actions whose every admitted outcome meets the duty in possible state `x`. A sure common decision exists exactly when

\[
\bigcap_{x\in B}A^*(x)\ne\varnothing.
\]

For a longer protocol, this local intersection is insufficient: later information, memory, and financing must remain compatible along the whole route. The revision certificate checks that additional obligation.

## What carries across scale

The recurring constraint is now more specific than a requirement to preserve resources or acquire knowledge. A declared continuing duty needs a funded, timely route from the present configuration to its next required configuration. Information, diverse alternatives, shared reserves, inherited apparatus, and revision authority can complement or substitute for one another, but only through actual available mechanisms.

Scaling changes these mechanisms. A larger population can support integer mixtures unavailable to one carrier and share a fixed inspection or archive bill. It also requires more birth capital. The mixed control does not make size automatically beneficial; its founding support and allocator are explicit.

An exact scale correspondence must include the environmental change and the **whole revision path**: signal access, retention, interpretation, expense, delay, available code, installation, and successor finance. Correspondences between the settled old and new systems alone do not establish a correspondence between their transitions. Matching final accuracy or average expense can conceal different probabilities of reaching a usable endpoint.

This supports the original direction in a qualified form: the same operational constraints can recur across scales while predicting different outcomes because the affordable response sets and their implementation differ. Universal empirical applicability still requires independently measured mechanisms and tested mappings.

## What is established and what remains open

We now have an actual paid update of an evaluator, an exact recovery window, an unknown-onset monitoring guarantee, a noisy finite-memory revision frontier, and a robust mixed-population alternative. The [claim register](CLAIMS.md) separates these results from their assumptions. All three verification suites passed; general and infinite claims have explicit proofs in addition to finite checks.

The architecture has substantial precedents in dual control, costly change detection, and certified safe learning. The [primary-source audit](revision-audit.md) identifies what those sources establish and what this construction adds to the local research record. No priority claim follows.

The remaining outer assumptions are now visible: a known contract family, interpretable signals, available candidate code, and an update mechanism that remains valid. A useful next test is a change **outside** that family: present an anomalous return, permit paid tests and a bounded way to construct a new candidate, and compare revision with a funded robust fallback or legitimate finite closure. The empirical counterpart is still a registered same-function comparison across sizes, measuring these mechanisms before fitting the outcome. Neither test has been performed here.
