# Recipient renewal: exact reserves, changing targets and repeated succession

6 October 2026. AI-authored mathematical extension under [generative grounding](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md). **Status: analytical propositions with proofs below, plus 39 checked Lean declarations for the signed-ledger and primary repeated-block contract; executable refinement is a separate acceptance obligation.** This note studies the connection **actually copied learner → fresh recipient evidence → paid changed action → copying of the acquired response**, followed through repeated finite generations. It is not a proof of inclusive concern, indefinite physical renewal or a complete alignment solution.

The accepted [recipient-transmission result](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/RECIPIENT-TRANSMISSION.md) leaves a successful child with recipient stock 10, child cash 0, a correct same-recipient estimate, and the original actor's separate stock 8. Its old source packets are exhausted. The prospective [successor-learning protocol](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/successor-learning/PROTOCOL.md) supplies the stage-wise continuation studied in Sections 2–5. That contract is a supplied local law. These results explain what follows from it; they do not derive its prices, addressing calibration, update recipe, packet source or component production.

The distinct [repeated-generation protocol](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/transmission/renewal/PROTOCOL.md) governs actual-state composition. Its [formal source and scope](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/transmission/renewal/formal/README.md) and [fresh pinned verification](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/transmission/renewal/formal/verification.json) establish reserve recursion, ledger concatenation, exact block guards, variable-schedule composition, arbitrary finite two-warm-up affordability and exact one-/zero-warm-up depletion bounds. They assume the stated event outcomes and access law, import only `Std`, and do not certify stochastic simulation, calibration, component production, ethical direction or the separate analytical price/noise propositions.

## 1. A general theorem about future action and actual resources

Let an intended finite event trace have accounts indexed by \(a\). Account \(a\) starts with stock \(b_a\), must retain floor \(f_a\), and experiences signed increments \(\delta_{a,t}\) after primitive event \(t\). Positive increments add usable stock; negative increments consume or transfer it. Resolve a work payment and its later return into different primitive events. Resolve a transfer as a simultaneous debit and credit; do not count it as dissipation. Non-resource guards, actual component access and policy consistency are separate conditions on the intended trace.

Define prefix displacement and reserve requirement by

\[
D_{a,k}=\sum_{t=1}^{k}\delta_{a,t},\qquad
L_a=\max_{0\leq k\leq T}(-D_{a,k}).
\]

**Proposition 1 — exact pathwise liquidity.** Subject to the separate non-resource guards, the whole intended trace is affordable while preserving all floors exactly when

\[
b_a\geq f_a+L_a\quad\text{for every account }a.
\]

**Proof.** The actual stock after prefix \(k\) is \(b_a+D_{a,k}\), by induction over primitive events. All floors hold exactly when \(b_a+D_{a,k}\geq f_a\) for every \(a,k\). Rearranging and taking the finite maximum gives the condition. The zero prefix includes the starting floor. Payment guards are satisfied precisely when their post-debit stocks satisfy the same inequalities. ∎

This is a conditional, pathwise theorem. For an adaptive policy, first specify the intended outcome branch; a liquidity failure may stop that branch. A robust reserve over an allowed set of branches is the supremum of their corresponding \(L_a\). An expected final surplus is neither the pathwise reserve nor a guarantee that action reaches the event producing that surplus.

**Corollary 1.1 — no borrowing from an unreceived future.** If a prefix debit exceeds current spendable resources, a later positive return does not enable that prefix. A ledger that nets a payment against its own later return can therefore accept an impossible operation.

**Corollary 1.2 — separate accounts matter.** A positive sum of stocks cannot pay an account's deficit unless an accessible transfer event occurs before the deficit. In particular, recipient production does not pay original-actor or learner bills merely because all three appear in the same analyst's total.

**Corollary 1.3 — components have their own prefix law.** For any nonrenewed part type with one unit irreversibly consumed per completed copy, initial stock \(m\) permits at most \(m\) completed copies. Source energy does not create a blank or routing component unless an explicit production/reclamation event supplies it. More energy alone is not a proof of continued construction.

The relation to Ren's future argument is direct but bounded: an intended continuation entails requirements on enabling conditions outside an actor's present record or boundary. A controller can fail by misrepresenting those conditions, by losing access to them, or by consuming them before their needed use. The theorem does not make the continuation desirable or settle whose continuation ought to govern a conflict.

## 2. Exact ordered-payment bounds for the declared learner

In the prospective protocol, a probe charges retention 1, target access 1 and work 3 **before** its outcome. Its actual recipient return, if any, arrives next. Outcome acquisition 1 and writing 1 occur afterward. Recipient stock finances any missing learner cash by an actual transfer, with recipient floor \(f=1\). The copied learner starts with cash zero; because each supplied fee is immediately spent, learner cash returns to zero after each paid stage. The reduction to one recipient reserve is valid for this declared transfer law, not for the original actor's independent account.

Write pre-return cost \(c=5\), post-return cost \(e=2\), total probe cost \(C=7\), and successful packet \(r=10\). A fully paid correct probe changes recipient stock by \(r-C=3\); a fully paid unsuccessful probe changes it by \(-C=-7\). These equalities do not identify why the unsuccessful probe failed.

For the primary, calibrated, available-source history, let initial recipient reserve be \(B\), and let \(n\) correct warm-up probes precede a target reversal. Immediately before reversal,

\[
S=B+3n.
\]

The retained estimate still selects the former productive action. The next probe fails, and the paid faithful update changes only the recipient cell. The next probe uses the changed action and succeeds. The donor for the next copy is the actual learner; its missing donor-hold unit is transferred from the recipient, while the original actor remains separate.

| Stage | Recipient reserve after stage | Prior-return liquidity requirement |
|---|---:|---:|
| Warm-up probes | \(S=B+3n\) | Each correct probe needs at least \(f+c=6\) at entry |
| Failed probe, acquired outcome and paid correction | \(S-7\) | \(S\geq f+C=8\) |
| Corrected work prepaid | \(S-12\) | \(S\geq f+C+c=13\) |
| Corrected return and post-return acquisition/write | \(S-4\) | Already affordable at \(S\geq13\) |
| Recipient-funded donor hold | \(S-5\) | Included in next condition |
| Own use, template read, assembly, commit and seed transfer | \(S-14\) | \(S\geq15\) |
| Correct copied action returns 10; recipient pays final hold 1 | \(S-5\) | Already affordable at \(S\geq15\) |

**Proposition 2 — sharp primary reserve bounds.** With sufficient declared source packets and receiver parts, paid stable addressing, enabled actuation, a faithful updater, no source outage, and a target stable through corrected and copied use:

1. The unsuccessful probe can complete its correction exactly when \(S\geq8\).
2. The corrected productive probe can also complete exactly when \(S\geq13\).
3. The whole specified learning-and-retransmission path completes exactly when \(S\geq15\).
4. On completion, final recipient reserve is \(B+3n-5\), learner and grandchild cash are zero, and the original actor's stock is unchanged.

These equivalences are conditional on arriving at the reversal with the assumed correct inherited estimate and actual stock \(S\); reaching that state also requires the warm-up conditions. **Proof.** Apply Proposition 1 to the table's primitive payments and transfers. The largest pre-return debit for correction and corrected use is 12. Copy preparation adds the donor hold plus own use/read/assembly/write/seed, a ten-unit prefix following reserve \(S-4\); its largest deficit is 14. Return and final hold leave \(S-5\). The earlier thresholds follow from the corresponding shorter prefixes. ∎

At the accepted \(B=10\), no warm-up allows a written correction but cannot initiate corrected productive use. One warm-up gives \(S=13\): correction and productive use are possible, but paid copying cannot complete. Two warm-ups give \(S=16\) and final reserve 11. The two warm-ups acquire their gain from two actual ten-unit packets with fourteen units of paid work/learning costs; they are not a free reserve reset.

The exact minimal warm-up count at these prices, for \(B\geq6\), is

\[
n_{\min}=\max\left(0,\left\lceil\frac{15-B}{3}\right\rceil\right).
\]

If \(B<6\), this count formula does not manufacture an affordable first correct probe; the initial prepayment obstruction must be resolved by an explicitly supplied mechanism.

### General prices

Let a successful probe return \(r\), a grandchild action return \(r_g\), a probe charge \(c\) before and \(e\) after its outcome, and \(C=c+e\). Let \(K\) be the recipient-funded donor hold plus the complete recipient copy/use/assembly/write/seed prefix, and let \(h\) be final retention. Assume \(r\geq e\), \(r_g\geq h\), and that the seed covers the grandchild's pre-return bills. All required parts and access guards remain additional premises.

**Proposition 3 — price-parametric route bound.** A single failed correcting probe, corrected successful probe and correct copied continuation starting at reserve \(S\) is affordable exactly when

\[
S\geq f+\max\{C+c,\;K+2C-r\}.
\]

Its final reserve is

\[
S+r+r_g-2C-K-h.
\]

**Proof.** Failure costs \(C\); the next work return cannot arrive before another \(c\) is prepaid. This produces deficit \(C+c\). The corrected probe ends at \(S+r-2C\), from which the full copying prefix \(K\) must be paid. This produces deficit \(K+2C-r\). The assumptions on post-return costs mean neither remaining post-return phase increases the required reserve. Summing the realized increments gives the final stock. ∎

This formula exposes why cheaper evidence, greater packet yield or less expensive copying change distinct constraints. A high final surplus can coexist with an unaffordable \(C+c\) prefix. Conversely, lowering copy costs may improve repeated renewal without changing the informational reliability of the learner.

## 3. Repeated finite generations without resetting history

At a completed copying boundary, the new child has zero cash and a currently correct inherited estimate, the recipient has the actual reserve \(B_{j+1}\), and one receiver bundle plus all used source packets have been consumed. This is the required entry interface for another block; reconstructing \(B=10\), replacing the record or restoring parts would be a different experiment.

For generation \(j\), let \(n_j\) be its number of actual successful warm-ups, followed by one reversal, one paid failed/correcting probe, one corrected successful probe and a correctly copied action. Under the same conditional laws,

\[
B_{j+1}=B_j+3n_j-5,
\qquad
B_j=B_0+\sum_{i<j}(3n_i-5).
\]

**Proposition 4 — finite repeated composition.** Suppose the full primitive-event stock and component account is inherited at every completed boundary, every non-resource guard remains satisfied, and generation \(j\) is allocated \(n_j+3\) previously declared ten-unit source packets and one unused blank/routing bundle. Then the prescribed finite lineage completes exactly when each generation's actual reserve satisfies its warm-up entry condition and

\[
B_0+\sum_{i<j}(3n_i-5)+3n_j\geq15.
\]

**Proof.** Induct over generations. Proposition 2 supplies the exact next boundary, which is used unchanged as the induction hypothesis. The inequality is exactly its copying threshold at that boundary. Component/source availability is checked independently; it is not inferred from reserve. ∎

For constant \(n\), the net reserve change per full generation is \(3n-5\).

| Warm-ups per generation | Net reserve change | Entry reserve for full generation | Consequence |
|---:|---:|---:|---|
| 0 | \(-5\) | \(15\) | Every completion consumes reserve; finite initial reserve limits repetitions |
| 1 | \(-2\) | \(12\) | Same obstruction, even though each generation can learn successfully |
| 2 | \(+1\) | \(9\) | The reserve condition propagates from any \(B_0\geq9\) |
| \(n\geq2\) | \(3n-5\) | \(\max(6,15-3n)\) | Nonnegative drift and entry solvency under the stipulated stable warm-ups |

For \(n=0\) or \(1\), initial \(B_0\) above the corresponding threshold \(T_n\) permits exactly

\[
1+\left\lfloor\frac{B_0-T_n}{5-3n}\right\rfloor
\]

complete prescribed generations before the next generation fails, assuming source/parts outlast the reserve. This is the number of completed blocks; a later failed block can still leave sunk payments, occupied carriers and lost opportunities.

At \(n=2,B_0=10\), any finite \(g\) admitted generations have \(B_g=10+g\). They require **\(5g\) new ten-unit packets and \(g\) unused receiver bundles**. Their new expenditure is \(39g\), source loss is \(10g\), and recipient gain is \(g\):

\[
50g=39g+10g+g.
\]

The original actor retains its independent stock. Earlier occupied carriers remain material state; successful copying does not create blank replacements or refund the original actor. The result is an arbitrarily long *finite, conditionally supplied* lineage. An infinite lineage would require an account of indefinitely replenished usable source, parts, access and calibrated learning—not merely writing an infinite index on this recurrence.

### Frequency condition and its limit

Across an arbitrary completed history, let \(N\) be fully paid learner probes, \(F\) unsuccessful probes, and \(G\) completed generic copying continuations with correct grandchild use. At primary prices,

\[
B_{\mathrm{end}}-B_0=3N-10F-G.
\]

Each successful probe gains 3; each failure costs 7, which is ten less than success; each complete copy/use/hold continuation costs the recipient one net unit. Thus a necessary long-run reserve condition for an unbounded completed history with limiting frequencies is

\[
10\lim(F/N)+\lim(G/N)\leq3.
\]

With exactly one corrective failure per generation, \(N=(n+2)G\), this is \(3n-5\geq0\). It is a condition on actual failures, not just target switch count: an outage, address error or misleading update can add failures. It is also insufficient by itself. Failure clustering can create an arbitrarily large negative prefix even when the terminal or limiting average is favorable. Proposition 1, not the mean, supplies the pathwise condition.

## 4. Why renewed evidence is different from a lucky inherited response

Assume binary actions and that the retained faithful rule infers the current productive action from a reliable receipt: after successful action \(a\), retain \(a\); after unsuccessful action \(a\), store \(1-a\). This rule is sound only when an unsuccessful response establishes mismatch—for example, a binary deterministic plant with an available packet, enabled actuation and the calibrated target identity held fixed.

**Proposition 5 — one-update tracking under the specified plant.** After a target reversal, the inherited correct action becomes wrong. One paid reliable outcome plus a paid faithful write stores the new productive action. If the target and addressing remain unchanged before the next action, that action succeeds. The actor cell remains invariant if the write addresses only the recipient cell.

**Proof.** A binary reversal changes productive action from \(a\) to \(1-a\). The old command \(a\) fails; sound decoding supplies \(1-a\), and the paid write stores it in the addressed cell. The next action reads that cell, hence chooses \(1-a\). ∎

This establishes only finite acquired response revision. It does not establish discovery of a new learning architecture or correction of the update rule itself.

A frozen response supplied with the currently correct bit ties a faithful learner on stable targets, subject to matched fees. A prescheduled action sequence may also match a public deterministic switching schedule without learning. Consequently, a temporal success pattern by itself is not sufficient identification of recipient learning.

The needed causal comparisons are:

1. Retain the same actual preparation, stocks, target schedule and action history up to the first informative outcome, then clamp only the paid write to the inherited bit. Divergence in later commands identifies that write's causal contribution.
2. After actual correction, keep copying costs and access unchanged but copy the originally inherited bit. Divergence in descendant action identifies transmission of acquired information.
3. Pair stable and switched environments, or let a hidden switch draw occur after inheritance independently of the controller, with equal pre-switch information. A lucky frozen bit cannot solve both opposite target states at the first post-switch decision.
4. Include an exact conventional table controller with the same receipt, memory, costs and guards. Matching performance identifies the mechanism's behavior; it precludes claiming an advantage merely from a new vocabulary.

**Proposition 6 — first-decision informational obstruction.** Consider two possible target states with disjoint successful action sets and identical decision-time controller information. Every deterministic controller selects the same action in both, so it fails in at least one. For equally likely binary opposite states, any randomized controller with randomness independent of the target has first-decision success probability at most one-half.

**Proof.** The decision is a function of the same information (and, if present, independent randomness). No realized action belongs to both disjoint success sets. Under equal binary alternatives, its average success probability is at most one-half. ∎

Fresh informative interaction can remove that ambiguity for later decisions; inherited compute or a larger internal record cannot remove it solely by being large. Past evidence, reliable environmental cues and inherited structures can provide relevant information, so this proposition is not a demand for permanent connectivity. It identifies the discriminating relation that a success claim must actually supply.

## 5. Outages, silence and the failure of a negative-label shortcut

Let the physical receipt be

\[
y_t=\mathbf 1[a_t=\theta_t]\,z_t,
\]

where \(\theta_t\) is the productive action and \(z_t\in\{0,1\}\) denotes available source/capture conditions. For the same chosen action \(a\), the observation \(y=0\) is compatible both with \(\theta=1-a,z=1\) and with \(\theta=a,z=0\).

**Proposition 7 — ambiguous nonreceipt.** A receipt-only decoder cannot infer a unique productive action from nonreceipt on the unrestricted class above. More faithful copying or longer retention of that same ambiguous bit does not restore the missing distinction.

**Proof.** The two displayed worlds give the same action/receipt pair and require opposite decoded answers. Any decoder of only that pair gives the same answer in both and is wrong in at least one. ∎

A paid missing-evidence event is a separate case: absence of a received report cannot be treated as an observed failure without a supplied channel law. Even a genuinely observed nonreceipt remains ambiguous under outages. This is the explicit limit of Proposition 5's negative update, and should be exercised as an adverse case in the experiment rather than silently repaired by an analyst's diagnostic.

Available next mechanisms have different obligations:

- A separate calibrated source-availability signal can disambiguate nonreceipt, but its sensing, authentication, material access and payment must be supplied and tested.
- Positive-only qualification is sound under no false-positive receipts; obtaining it requires exploration and source opportunities. An all-zero finite history remains unresolved if arbitrary outages are allowed.
- Statistical identification is possible under additional persistent-source/noise assumptions and sufficient paid samples, with error bounds rather than certain truth. Those assumptions are not consequences of faithful recording.

If outages can suppress every attempted discrimination, no finite reserve guarantees identification on that environment class. If failures can continue arbitrarily long while every fully paid trial costs a positive amount and no return is received, no finite reserve guarantees continued action either. Epistemic access and material access are two distinct bottlenecks.

## 6. What this advances and what could change the account

The current bridge can become stronger than one-generation persistence: the same acquired template can finance new evidence, act after an unannounced change, and furnish the actual changed template for a descendant, with a compositional reserve theorem and finite source/component account. At the primary prices, two genuine warm-up gains suffice for a repeated block with positive reserve drift. This identifies a mechanism by which access to external conditions sustains a capacity to correct future action.

The conclusion changes if independent checks find hidden reserve restoration, cross-account spending without transfer, a source return before its bill, reuse of occupied parts, a copy of an audit label instead of runtime memory, or controls whose learned behavior disappears under identical ancestry. A noiseless positive result must be qualified further if outages produce mislearning, rapid changes defeat liquidity, or wrong descendants remain funded by surplus: productive use, copying and retention are different observables.

Remaining supplied premises are the local construction/update recipes; fixed binary repertoire; stable target address and actor/recipient cell distinction; receipt calibration; cost and packet laws; recipient floor and funding policy; accessible copying; source/part inventory; and the association between the contributing learner and copied template. Origin, revision and robustness of these conditions are still research tasks.

Nothing here implies that a system which depends on others thereby recognizes their justified standing. A coercive institution or exploiter may preserve precisely the dependencies that support its control. To advance from conditional learning renewal toward alignment and governance, the next bridge must explain and test **which consequences can revise action and the rules of revision when the affected center lacks private leverage, and how the power to change those rules is retained without being captured**. The liquidity and identifiability results constrain that bridge; they do not decide its normative direction.
