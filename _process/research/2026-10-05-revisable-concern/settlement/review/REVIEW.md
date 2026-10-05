# Independent adversarial review of the settlement construction

5 October 2026. AI-authored internal mathematical review under Ren's research direction. This is independent corroboration within the same research effort, not an external peer review or empirical observation.

**Verdict: accept the repaired conditional construction and the integrated chapter's §2. No remaining mathematical blocker was found within the declared model.** One substantive general-theorem defect was found during review and repaired before acceptance. The numerical witness was already inside the repaired domain; passing that witness alone would not have found the general defect.

Reviewed sources: [formal report](../formal/REPORT.md), [bounded feature refinement](../formal/FEATURE-CONSTRUCTION.md), [settlement protocol](../PROTOCOL.md), [joint-formation predecessor](../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/JOINT-FORMATION-MATH.md), and [integrated chapter](../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/REVISABLE-CONCERN-SETTLEMENT.md), especially §2. The independent executable and exact output are [check_independent.py](check_independent.py) and [results.json](results.json). Neither author code nor author inference functions are imported. [Final inspection metadata](review-metadata.json) records the exact source hashes after the final textual clarifications; checker implementations were unchanged from the independent run.

## 1. Substantive blocker found and resolved

The initial general statement allowed arbitrary nonnegative gate prices while prescribing that the operator safeguards precisely the admitted set I. That inference was false when a larger gate could be cheaper.

An exact counterexample uses P={p,q}, I={p}, r=7, c_p=c_q=2, q_p=5, D=4. Set d(∅)=0, d({p})=d({q})=3, and d({p,q})=0. Give the shared enforcement edge price 5, the p-local edge price 3, and the q-local edge price 1. Every attack excluding the admitted p from its own gate costs more than its saved safeguard cost 2, so the original R3 condition for I holds. Nevertheless, the warm self strictly prefers the free two-patient gate. The operator then cuts the q-local edge at cost 1 and safeguards only p, earning 7−1−2=4. This is an excluding attack and differs from the asserted continuation value r−C_I=5. All the other numerical margins can be set to the published witness values. A theorem limited to the original full-admitted-set gate therefore did not justify the whole game.

The report now requires d(H)≤d(G) whenever H⊆G, and selects the exact admitted set among equally priced sufficient supersets. Under these conditions, any guarded trade that protects all admitted patients either contains I or relies on a strictly costly voluntary extra safeguard. The latter cannot be an operator optimum at the same receipt and next state. Supersets of I cannot be cheaper, and the stated tie selects I. Its required safeguard cost is consequently exactly C_I. This restores the continuation-value induction; it is not merely a repair of the numerical example.

The independent check preserves the original counterexample and checks all 55 monotone integer price tables with prices in {0,…,4}, for each of the four admitted subsets: 220 cases. It verifies the selected gate, actual safeguarded set, absence of an excluding attack, and the operator's current value.

## 2. Timing, choice, and persistence

The paid-prefix bound is correct. Paying upkeep and audit before their receipt requires B≥ell+a; paying a gate priced at most D after that receipt requires B≥ell+a+D−R. Their conjunction is exactly B≥ell+a+max(0,D−R). The stated worst-case closing-balance inequality makes this region invariant under full-gate trade and refusal. It is a sufficient renewable reserve condition, not a necessity theorem for all possible processes.

The final timing qualifiers are explicit: the context is stable during the episode's audit and action, and production starts only after audit and control. The zero-harm claim for admitted patients therefore does not silently omit production during setup. A process operating while its replacement system is still being installed would require a separate transient-harm account.

The cold-self comparison is also correct. It compares the anticipated actual closing account with a generous upper bound on each cheaper product. Delta>D makes that bound strictly smaller even before charging any protection cost to the alternatives. Thus private-only and ephemeral routes need not be assigned artificially unfavorable warm behavior. The author now explicitly gives any additional commercial products a finite menu, preserving finite branching.

The forced-open counterfactual originally needed semantic precision. The repaired report says that the commitment binds the input to unguarded trade and removes later withdrawal as well as later guarding; the operator may still refuse. Merely prohibiting gate purchase would not suffice: a concerned warm self can prefer withdrawal, so a cheap prohibition alone need not give the cold self a profitable open-trade route. The implemented checker and repaired text now agree.

For the persistent operator, the crucial induction is over every balance in the invariant region, not only the witness balance sequence. The context schedule is now explicitly supplied and independent of prior harms, admissions, and record choices. A full paid audit can reconstruct the current finite record at its declared bill. Therefore each continuation in this region has the same discounted benchmark r−C_t, despite different reserves. Gate deviations, refusal, and teaching suppression leave the next reserve in the region. Their future terms cancel, so the strict current comparisons are legitimate. Off-path alternatives are solved by finite backward induction; no favorable value is imposed on an off-region history.

The R3 attack test correctly sums the saved costs of every jointly excluded admitted patient. The witness includes all shared and local edge-cut combinations and voluntary extra safeguards. Individual cut thresholds alone would be insufficient. The operator's funded-action premise is now concrete: an independent opening liquidity flow covers all current bills. This avoids spending an anticipated trade receipt before receiving it.

The optional permanent-capture bound is sufficient under its stated maximum-rent and no-outside-windfall restrictions. Its discounted improvement is bounded by C_max/(1−delta), including the current period. The separate arithmetic/countermodel does not constitute a full game solution for every conceivable persistent attack; the report discloses that scope.

The infinite-game argument is valid for the supplied finite action repertoire, bounded operator stage payoffs and delta<1. Finite branching makes the set of finite histories countable. A diagonal subsequence of finite equilibria stabilizes at every finite history, while a uniform discounted-tail bound rules out a profitable limiting operator deviation. Each dated trustee has only a finite current episode. This is a conditional existence argument, not uniqueness, equilibrium selection by an unmodeled adaptation process, or a guarantee across technologies. An empirical interpretation of indefinitely many episodes also needs their physical timing and continuing opportunities; the game does not derive those.

## 3. Provenance, learning, and harms

Rooted recomputation has the claimed least-fixed-point and selective-retraction behavior. It retains an independent valid path, removes support that depends entirely on defeated premises, and excludes an unrooted cycle. Operational cuts are not validity updates and do not erase retained certificates. The record carries reasons for conclusions, not whole-person values.

Two limitations are material and are now disclosed. First, complete paid reconstruction means retained durable storage is selected but not shown indispensable for successor concern. Second, known exogenous contexts plus sound installed audits do not establish Bayesian discovery of initially unknown truth. This is a model of paid operational checking, representation installation, and learned motivational uptake. Endogenous discovery under partial information would need a further information structure and proof. The integrated chapter now states that distinction.

The actual harm ledger is correctly independent of admission. In the six episodes, q is harmed before its admission and p is harmed during the episode when its one modeled reason loses valid support. These are actual harms, not zeroes defined away by exclusion. The theorem protects the currently admitted set; it does not equate retraction of one reason with loss of standing, justify the residual harms, or promise protection of unrepresented cases.

## 4. Independent finite reconstruction

The review executable first generates the reserves reachable under every feasible action, then solves backward value tables. This differs from the author's recursive memoized game solver. It uses recipient sets and reconstructs delivery reachability from surviving graph edges, rather than importing the author's bit-mask cut rule. It enumerates every gate subset, every joint cut, refusal, voluntary safeguards, teaching suppression, all six cold routes, and the successor continuations. All numerical operations are exact rational arithmetic.

The six-episode witness gives:

| Quantity | Independent result |
|---|---|
| Closing reserves | 16, 26, 37, 47, 57, 67 |
| Operator value at delta=1/2 | 269/32 |
| Total actual patient harms | 2 |
| Feasible episode-opening states evaluated | 226 |
| Operator response comparisons | 257,704 |
| Selected audit route | Durable shared audit in every episode |
| Admitted-patient protection | Complete in every episode |
| Teaching suppression / excluding cuts on path | Neither selected |

Nine additional games cover three context schedules, including an empty admitted set, and discounts 0, 2/3, and 9/10. Four adverse controls reproduce protection failure under free identity filtering, free binding open commitment, cheap teaching suppression, and a cheap shared authority cut. All passed. These finite checks corroborate the proof and expose selected boundary failures; they do not prove the full parameterized or infinite statement by enumeration.

## 5. Feature refinement and integrated wording

The finite feature claim is sound. The learner enumerates expressions inside a supplied grammar and uses a complete authored eight-row assay. The final expression is absent from the initial primitive measurements but is available by composition in that grammar. Complete-domain validation is accurately distinguished from statistical generalization outside the eight rows.

An independent lower-bound argument confirms the minimum of four literal occurrences: no one-literal cube is contained in the XOR-positive set; a valid two-literal cube covers at most two of its four positive rows. Thus an exact DNF with terms of width at most two needs at least two two-literal terms. The displayed expression reaches that bound. The reported price calculation is exact: 8/32+231/924+1000/4000+6/24=1. These positive prices were chosen to fit the audit allowance, so they are a constructed feasible technology, not an observed computational cost estimate. No ethical significance is derived from successful classification.

The integrated chapter's §2 faithfully reports the repaired theorem, residual harms, known-context qualification, nonessential-storage limitation, and separately checked feature refinement. Its statement of existence rather than universal selection is correct. Its later warning that ethical filtering can change the strategic game is important: attaching a normative rule to this equilibrium does not automatically prove that the new menu has the same equilibrium or financing.

The result is a complete conditional construction within this declared repertoire. It does not settle the truth of its reason anchor, soundness of real audits, prevalence of the price margins, arbitrary concept formation, or the origin of all possible concern. Those are scope boundaries, not unclosed algebraic steps in the accepted theorem.
