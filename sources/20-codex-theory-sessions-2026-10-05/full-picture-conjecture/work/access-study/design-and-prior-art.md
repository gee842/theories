# Access projection: design audit and focused prior art

5 October 2026. Read `outputs/next-test.md`, the previous formal and prior-result reviews, and the frozen recoverable-inquiry snapshot. This memo precedes inspection of any new integrated access-study outcomes. It does not edit the protocol or the reference workspace.

## What this first study can learn

The permission bit will govern transfers because the code says it does. Showing that a forbidden transfer fails validates this programmed rule; it is not empirical evidence that authority causes failure in real institutions. More informative results are possible:

- A verified pair of admissible states with the same aggregate description but different attainable outcome sets refutes that **specified abstraction**.
- An independently derived condition under which aggregation is valid supplies a positive result and a boundary for the failure claim.
- Witness policies, account ledgers, and independent one-step calculations can verify that a strict performance gap follows from actual payment timing rather than an implementation error.
- Quantifying where the access constraint binds can distinguish resource amount from accessibility within the stipulated process.

This is a finite model and interface audit. It is not yet the second-implementation transport test, a model of institutions selecting their own permission rules, or a study of new question formation. Even if permission itself becomes a state variable, a supplied transition rule is different from explaining how that rule arises.

## Freeze the estimand before comparing descriptions

For the access-only question, start with the inherited sufficient operational state and add bank balance \(b\), treasury \(t\), and permission \(p\). Hold fault belief, stock, readiness, pending work, remaining horizon, primitive observations, and burden specification fixed in matched comparisons. The coarse map should replace \((b,t,p)\) with a declared subset such as total \(w=b+t\), while retaining the other inherited variables.

The broader “current output, stock, total cash” description in the prospective protocol also removes belief and readiness. It is valid as a deliberately coarse baseline, but its failure cannot isolate the importance of access. Use an access-only projection as the primary diagnostic and label the broader baseline separately.

Different claims require different tests:

| Claim | Required check | Insufficient evidence |
|---|---|---|
| Exact same-action state quotient | Equal projected kernels, matched primitive-action availability, projected costs/predicates, and the stated observation contract on every retained fiber | Equal optimal values at selected starting states |
| One-way controller refinement | Each selected abstract action has an executable concrete implementation using allowed information, with successor and specification preservation | For each hidden state, some suitable concrete action exists |
| Value equivalence | Equal optimal value for a named objective, horizon, observation, and admissible policy class | A single equal realized trajectory or close optimizer output |
| Attainable-vector equivalence | Equality of the declared vector sets, including the chosen policy randomization rules | Equality for one scalar weighting, or agreement on a small grid of weights |
| Predictive transport | Frozen mechanism and measurement rules predict held-out outcomes in an independently specified implementation | Two labels attached to one simulator, or repairing the model after the target result |

Equality of a value can hold accidentally despite different available behaviors. Conversely, primitive-action non-equivalence can coexist with equal operational value after an admissible action refinement. Both outcomes should be reported without forcing them into one binary notion of “same.”

## Pooling is the decisive positive case

Suppose permission allows free, instantaneous transfers before every relevant bill. Even then a literal action “transfer three” can be available in one partition of total funds and unavailable in another. Equal totals therefore need not define an exact quotient over those primitive action labels.

Two legitimate positive tests are available:

1. **Mandatory normalization.** Before each operational decision, move funds according to a fixed rule, such as filling the bank up to its cap. Compare states only at this normalized decision boundary. Check that the bank cap and the order of bills do not block a macro-action that total funds could otherwise finance. The resulting process is a particular modified interface, not automatically the original primitive-action process.
2. **Explicit refinement.** A macro-action names the operational expenditure; a concrete adapter implements the necessary transfers and payments. State which account information the adapter sees, whether it consumes time or funds, and whether it may transfer between subpayments. If the high-level controller sees only the total while the adapter reads balances, that extra implementation interface must be declared. A hidden-state-dependent mathematical existence argument is not an executable adapter.

The macro model can ignore transfer labels only if their timing, observation, costs, and any protected account relation are irrelevant to the declared query or correctly represented in the macro-action. If transfers cost a period, incur fees, require a reserve floor, have caps, or signal private information, total funds may cease to suffice.

A distinct positive quotient exists when treasury is forever inaccessible, cannot affect any other transition, and has no terminal or protected value: it can then be dropped while **bank balance is retained**. This does not vindicate total-cash aggregation. It identifies an inert variable for a particular question.

## Controls and pre-outcome expectations

| Control | Expected implication and qualification |
|---|---|
| Optional permission expansion, all else unchanged | The admissible policy set expands, so the best scalar objective cannot worsen and the attainable vector set cannot shrink. This weak result follows from nesting. Individual components of the optimizer's chosen vector can worsen under a tradeoff. |
| Treasury identically zero throughout the episode | Permission has no effect. An initially empty treasury is insufficient if later income overflow can replenish it. |
| Enough initially accessible funds for every possible registered bill | Access should be nonbinding over the tested horizon, provided bank caps and later rules do not invalidate the premise. A claimed permission advantage here suggests a confound or bug. |
| Free immediate pooling with a verified adapter or normalization | Operational-value agreement should hold under the declared cap/timing conditions. Do not infer literal transfer-action equivalence. |
| Horizon zero, no terminal valuation of access or account identity | Permission and partition cannot affect already completed operational outcomes. |
| Permission-label placebo | Change the label shown in records while keeping feasibility, execution, observations, and rewards unchanged. The attainable set should be unchanged; arbitrary policy tie-breaking can change a chosen trace without changing value. |
| Uninformative paid diagnosis plus direct repair | Paid tests should have no information value. A transfer benefit may still arise through direct repair and is then not an inquiry benefit. |
| Known absent fault | Do not automatically expect no repair: the inherited model lets repair improve stock even without its fault target. Use this control to expose the difference between fault removal and generic productive repair. |
| Transfers delayed until after current bills | Future pooled wealth cannot pay a current bill. Compare to immediate pooling to isolate timing. |
| Independent numerical policy evaluation | Recompute the optimizer's witness policy through latent-event enumeration or a small occupancy problem. Value agreement from two calls to the same recursion is weak verification. |

For constrained optimization, compare the same expected burden allowance while enforcing the same pathwise cash rules. Equal initial total cash is not equal realized spending, equivalent information, or equal distribution of burden. If permission reduces feasible actions, a benchmark may become infeasible; do not assign it an invented feasible cost.

### An analytical one-period witness

An optional predeclared boundary case uses the inherited dynamics with stock one, no readiness, bank zero, treasury three, and a fault known present. A repair costs three, clears the fault, and adds one to the stock update. Without transfer, no repair can be financed before income: damage probability .8 makes next stock zero with probability .8. With immediate authorized transfer, repair is feasible; next stock is one or three and never zero. Thus a collapse-probability difference of .8 is analytically expected.

This illustrates a programmed, binding cash-access constraint, not a surprising discovery. Check whether belief one and these balances are admissible initial states in the frozen study. If they are unreachable from its registered start, the witness refutes a global quotient over the enlarged state space but not a quotient restricted to the registered reachable states. It must be labeled accordingly.

To show that merely retaining permission is insufficient, compare bank three/treasury zero with bank zero/treasury three while permission is disabled in both. Same total and permission, different current repair availability. Conversely, under verified free pooling, the same partitions should give the same operational possibilities. These positive and negative tests concern the same access relation under different contracts.

## Avoiding an artificial information advantage

If the full controller sees bank, treasury, and permission while the aggregate controller sees only total, the comparison may combine a physical access restriction with loss of information about access. Both can matter, but identify them separately. If an action menu is displayed, it can reveal the supposedly omitted balance or permission. If failed transfer attempts consume time or reveal information, they must be in the transition and observation law. A hidden permission bit requires filtering; silently letting the optimizer read it grants extra knowledge.

Likewise, if the permission variable is publicly known and held fixed for each run, it can be encoded in the model index. Omitting it from a within-run state does not necessarily mean the controller lacks it. State whether the proposed quotient is required to work uniformly across permission interventions or only conditional on one known regime. A refutation of the former is not automatically a refutation of the latter.

## Two primary-source capsules

### Resource feasibility under partial observation

Brázdil, Chatterjee, Chmelík, Gupta, and Novotný, *Stochastic Shortest Path with Energy Constraints in POMDPs* (arXiv:1602.07565), sections 3–4, especially Remark 2 and the product-state construction. [Primary full paper](https://arxiv.org/pdf/1602.07565).

The authors distinguish expected cost from a resource condition holding along every execution until the target. They encode resource level into a product POMDP, with exhaustion represented by a sink, and explicitly assume observable resource levels. This is close prior art for enforcing available-cash constraints within a partially observed process. Our access study adds a particular two-account interpretation; it does not invent hard-resource POMDP planning. The source's single resource variable does not itself settle whether inaccessible treasury is an adequate substitute for spendable cash, and its algorithmic guarantees cannot be copied without matching its objective and assumptions.

### Executable controller refinement

Reissig, Weber, and Rungger, *Feedback Refinement Relations for the Synthesis of Symbolic Controllers*, 2017 journal paper; arXiv v3, sections IV, V.2, and Theorem VI.3. [Primary full paper](https://arxiv.org/pdf/1503.03715).

The paper explains why a relation adequate for some statewise simulations may still require unavailable concrete-state information when implementing a controller. Its feedback-refinement condition matches admissible inputs and includes projected concrete successors in abstract successors; the controller-transfer theorem makes the implementation requirement explicit. This directly motivates auditing our transfer adapter and its observation access. The paper concerns set-valued systems and specification satisfaction; citing it does not establish equality of stochastic probabilities, cost frontiers, or ethical criteria in our experiment. Those require their own preserved quantities and proof.

Both actual primary bodies were inspected. These are targeted precedents, not a comprehensive novelty search. No novelty claim is made.

## Claims to use and claims to avoid

**Supportable if checked:** “Within the frozen finite model, total cash does not preserve the registered correction problem under restricted transfers; these merged-state witnesses show the failure. A stated pooling interface restores the specified operational equivalence in its declared scope.”

**Avoid:** authority always improves outcomes; money is insufficient in every setting; institutional legitimacy has been derived; permission evolves endogenously merely because it is in the state; more allowed actions make every outcome component better; value equality proves exact causal equivalence; finite enumeration establishes unrestricted completeness; or one simulator establishes cross-domain transport.

The strongest useful result would pair a clean failure witness with a verified positive pooling condition and an explicit executable policy refinement. That maps the boundary of an abstraction instead of only demonstrating that its deliberately omitted gate exists.
