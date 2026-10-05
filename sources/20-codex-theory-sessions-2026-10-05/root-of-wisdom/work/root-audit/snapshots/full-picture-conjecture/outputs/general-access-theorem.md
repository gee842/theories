# A general theorem of funding access and payment timing

Proof appendix, 5 October 2026. This extends the [earlier access proof](access-proof.md) and accompanies [Removing assumptions and proving a general theory of generation](proving-generative-theory.md). The earlier frozen model and results retain their original scope. The results below are elementary and no novelty is claimed.

## Result and proof strategy

Removing unnecessary assumptions is a legitimate route to a stronger theory. Here it produces an actual strengthening: **the entire round's bill need not fit within the cash cap, income need not arrive only at round end, and transfer access need not be unrestricted at every instant.** Under precisely stated financial rules, there is an exact characterization of which income/payment schedules are feasible. It separates total resources from the timing and capacity through which they become spendable.

Some other assumptions cannot simply disappear while preserving the original conclusion. Fees, deadlines, account-dependent risks, and additional information admit countermodels to total-funds equivalence. A stronger theory can include them and derive a more general result. It must then retain the distinctions they make relevant, or prove that those distinctions are inoperative for the selected question.

There are three different operations on an assumption `A`:

1. Prove the conclusion without `A`: genuine dispensability.
2. Derive `A` from explicit more general premises `B`: an explanatory reduction, with `B` now load-bearing.
3. Replace `A` by a weaker condition characterizing precisely when the conclusion holds: a sharper theorem.

The schedule characterization below accomplishes the third and yields instances of the first. The local refinement theorem explains how to compose independently checked financial, informational, and physical conditions. Neither is a proof that all possible physical or institutional arrangements obey the favorable special case.

## Exact finance theorem with bounded transfer opportunities

Let cash capacity be `C≥0`, initial cash `0≤b₀≤C`, initial treasury `t₀≥0`, and total `N₀=b₀+t₀`. Funds may be nonnegative **real** quantities. A finite sequence of events is ordered as follows at event `j`:

1. Nonnegative income `i_j` arrives. Fill cash to `C`; retain all overflow in treasury.
2. Treasury-to-cash transfer is allowed, up to amount `r_j≥0`, subject to treasury availability and the cash cap.
3. A nonnegative atomic bill `c_j` must be paid from cash before proceeding.

Transfers have no fee, loss, or other consequence relevant to this financial feasibility problem. Transfers go **only from treasury to cash**. The transfer limit is a per-event opportunity, not an unmodeled shared quota depleted across events. Initial funds, incomes, limits, and bills are given for the schedule being tested. Later an operational policy can generate these quantities adaptively.

There are finitely many events within each considered execution. A transfer is one bounded action, not infinitely many retries squeezed before a deadline. Waiting until a transfer arrives changes which event admits the opportunity; it does not move that opportunity before an earlier bill.

Write

\[
N_j=N_0+\sum_{k=1}^{j}(i_k-c_k).
\]

The **greedy cash recurrence** is

\[
B_0=b_0,\qquad
B_j=\min\{C,N_{j-1}+i_j,B_{j-1}+i_j+r_j\}-c_j.
\tag{G}
\]

Stop and declare failure at the first `B_j<0`.

**Theorem 1 — exact causal feasibility.** A lawful transfer schedule pays all bills if and only if recurrence (G) never becomes negative. Whenever payment through event `j` is feasible, `B_j` is the maximum achievable cash balance immediately after that payment. Greedy execution achieves it without knowing future incomes, limits, or bills.

**Proof.** All feasible histories through event `j−1` have the same total `N_{j−1}`. If one such history has cash `b`, income first gives `a=min(C,b+i_j)` cash and total `N_{j−1}+i_j`. The greatest permitted transfer is

\[
\min\{r_j,C-a,N_{j-1}+i_j-a\},
\]

so maximum prepayment cash is

\[
a+\min\{r_j,C-a,N_{j-1}+i_j-a\}
=\min\{C,N_{j-1}+i_j,b+i_j+r_j\}.
\]

This expression is nondecreasing in `b`. Inductively the largest prepayment cash is therefore achieved by the earlier greedy balance, giving (G). If even this amount is below `c_j`, no lawful history pays the bill. Otherwise paying it yields the maximum subsequent cash, and the same induction continues. The greedy transfer uses current cash, current total, and the currently available limit only. It needs no future information. ∎

This is more than the assertion that “feasible schedules are feasible”: it gives a single online algorithm and explicit inequalities that decide feasibility without searching all transfer choices.

## Equivalent funding and storage inequalities

For integers `1≤s≤j`, write `D_{s:j}=Σ_{k=s}^j c_k`, `I_{s:j}=Σ i_k`, and `R_{s:j}=Σ r_k`; an empty sum is zero.

**Theorem 2 — exact schedule characterization.** The schedule is feasible if and only if all the following hold:

\[
\begin{aligned}
D_{1:j}&\le N_0+I_{1:j} &&\text{for every }j, \tag{T}\\
D_{1:j}&\le b_0+I_{1:j}+R_{1:j} &&\text{for every }j, \tag{A}\\
D_{s:j}&\le C+I_{s+1:j}+R_{s+1:j}
&&\text{for every }1\le s\le j. \tag{S}
\end{aligned}
\]

(T) is a total-funds prefix bound: future income cannot pay earlier bills. (A) bounds how much can have become accessible from the initial cash and subsequent income/transfer opportunities. (S) is the storage bound: just before bill `s` at most `C` can be in cash; subsequent bills require that stored amount plus later accessible inflows. Setting `s=j` gives the individual bill condition `c_j≤C`. None of these alone suffices in general.

**Proof.** Set `d_j=i_j+r_j−c_j`. The algebraic recurrence (G), continued symbolically even past a hypothetical negative value, is

\[
B_j=\min\{C-c_j,N_j,B_{j-1}+d_j\}.
\]

Unrolling gives

\[
B_j=\min\left\{
b_0+\sum_{k=1}^j d_k,
\min_{1\le s\le j}\left[C-c_s+\sum_{k=s+1}^j d_k\right],
\min_{1\le s\le j}\left[N_s+\sum_{k=s+1}^j d_k\right]
\right\}.
\]

The final inner term equals `N_j+Σ_{k=s+1}^j r_k`. Since all `r_k≥0` and `s=j` is allowed, its minimum is exactly `N_j`. Therefore

\[
B_j=\min\left\{
N_j, b_0+I_{1:j}+R_{1:j}-D_{1:j},
\min_{1\le s\le j}
\left[C+I_{s+1:j}+R_{s+1:j}-D_{s:j}\right]
\right\}.
\tag{C}
\]

All these quantities are nonnegative for every `j` precisely when (T), (A), and (S) hold. Before any first failure the symbolic recurrence is the actual greedy trajectory, so Theorem 1 establishes necessity and sufficiency. ∎

This is a universal theorem **over the declared financial class**, including every permitted choice of real-valued data and every finite length. Its universality is mathematical and exact. Whether a real payment system belongs to this class is a separate factual question.

## Substantive relaxations of the original pooling assumptions

**Full round bill below the cap is unnecessary.** If an unrestricted treasury-to-cash refill is permitted before **each atomic bill**, maximum prepayment cash is `min(C,N_{j−1}+i_j)`. Feasibility reduces to

\[
c_j\le C\quad\text{and}\quad N_j\ge0
\qquad\text{for every }j.
\tag{R}
\]

Any round may contain several such events, so its total spending can exceed `C`. Example: `C=1`, initial `(b,t)=(0,2)`, two bills each of one, and refill before each bill. Both are paid. One initial normalization followed by no further transfer fails on the second bill. We have replaced `whole round bill≤C` by an exact schedule condition, not simply discarded a protection against overdraft.

An atomic bill cannot be subdivided just to evade the cap unless the actual payment interface permits installments and the intervening transfers. The theorem uses the declared event granularity.

**Income need not come only at the end.** Any interleaving can be represented by splitting the event sequence. Its order matters through (T), (A), and (S). An income of one just before a bill can finance it; the same income just after the deadline cannot. Lossless overflow storage remains an explicit premise.

**Access need not be immediate everywhere.** A barred moment has `r_j=0`; a restricted opportunity has finite `r_j`; a later unlock changes subsequent limits. These schedules are covered by the same theorem. The conclusion is exact feasibility under that schedule, not that all schedules are equivalent at equal totals.

**The capacity may vary with an observed schedule.** With capacity `C_j` at event `j`, the same argument replaces `C` in (G) by `C_j` and in (S) by `C_s`, provided any forced overflow on a capacity decrease is returned to treasury without loss. This is a direct algebraic extension of the proof; the bounded checker below uses constant capacities only.

**Deterministic future histories are unnecessary.** In an operational process, let incomes, limits, and bills depend causally on the retained observed history and nonfinancial actions. Apply the recurrence along the realized history. Greedy remains causal. A fixed operational policy is financially implementable on all admitted branches exactly when all of its resulting branches satisfy the inequalities; an almost-sure version uses probability-one branches under the stated kernel. This is a statement about a fixed adaptive policy, not permission for a controller to select different first actions using future realizations.

The supplied limit/arrival mechanism must remain the same under the compared financial schedules. In particular, it cannot secretly depend on the actual transfer amounts in a way omitted from the model. Such a dependence requires retaining its additional state.

## Stronger pooling by policy refinement

Theorems 1–2 can replace once-per-round normalization inside a preservation theorem.

Fix the initial split, a public event/transfer-opportunity mechanism, and a declared operational policy class. Suppose:

- The physical and primitive observation kernels depend on the retained nonfinancial state and nonfinancial actions, not on the actual cash/treasury split or transfer amounts.
- The retained outcomes include operational payments and physical consequences, but exclude transfer amounts, intermediate account paths, and other quantities on which the financial implementations differ.
- The capacity/limit/income rules obey Theorem 1, and future opportunities do not change merely because the actual controller previously transferred more.
- Policies have enough admissible memory/private randomness to simulate a chosen controller's virtual ledger; income and transfer-opportunity updates needed for that ledger are observed or legitimately simulable.
- Greedy transfers are authorized and executable at each permitted opportunity. They consume exactly the resources and elapsed time represented by the declared interface.

**Theorem 3 — greedy-scheduler equivalence.** The set of attainable retained operational trace laws under arbitrary lawful transfers equals the corresponding set under compulsory greedy transfers, for the same initial state and opportunity mechanism.

**Proof.** Every greedy execution is an allowed arbitrary-transfer execution, proving one inclusion. Conversely, fix an arbitrary lawful controller. A greedy controller stores a virtual copy of its financial ledger, history, and private random state, executes its transfer decisions virtually, and selects the same nonfinancial actions. Couple the primitive observations and physical outcomes. Totals agree, while Theorem 1 gives actual cash at least virtual cash at each payment. Thus every virtual payment is actually feasible. By the common physical/observation kernels the operational outcomes agree in law; observed income and opportunities update both ledgers. Induction gives the other inclusion for any finite execution. ∎

This proof constructs the refinement; it does not assume equality of the final attainable sets. It also shows why normalization need not be imposed as an extra axiom: within this financial class it is a **derived implementable choice**.

**When total alone is enough.** Under unrestricted refill before every atomic bill, the attainable operational laws from same-total splits coincide, with feasibility characterized by (R), provided the retained observation does not lose extra information contained in the split. The initial split may be stored by a policy emulator as a virtual starting ledger; it must not reveal hidden environmental information absent from the macro information state.

**When total alone is still insufficient.** With bounded or absent later transfers, the greedy state generally needs both `N` and `B`, or enough public history to reconstruct `B`. For example, start canonical at `(cash,total)=(1,2)` with cap one and no later transfers. Income one followed by payment one ends at `(0,2)`; payment one followed by income one ends at `(1,2)`. Current total is the same, but a subsequent bill of one is affordable only in the second case. Public history can retain this difference; total as a memoryless state cannot. The general theorem enlarges coverage without falsely claiming the old reduced state remains sufficient everywhere.

## General local refinement certificate

The useful abstraction principle is broader than financial normalization. It can allow positive durations, more complicated controllers, or implementation changes **when the retained interface accounts for them correctly**.

Let `q:Z→S` relate concrete states to macro states. At macro decision boundaries, let observations be compatible with the same macro observation rule. For every admitted macro action `a`, supply a concrete adapter that:

1. Uses only information available to its actual controller and its permitted memory/randomness.
2. Completes in finitely many admissible concrete steps, respecting resources and deadlines; no infinite internal execution is hidden as one step.
3. Produces, for every concrete state in the relevant fiber, the same joint law of next projected state, retained observations, and retained cost/outcome/time increments as the macro kernel for `(q(z),a)`.

The item 3 equality must hold conditional on **every reachable concrete history and adapter memory state** compatible with that boundary, not only after averaging over hidden adapter memory. Equivalently, include the relevant adapter memory and implementation phase in `Z` and require the kernel equality uniformly on those augmented states. This is the uniformity needed for the induction below; recording memory mathematically does not itself pay for its implementation.

If internal observations are retained, include them in that joint macro output; if they inform later concrete choices, the adapter must model those choices causally. Hidden environmental states are not granted to the adapter merely because the analyst writes them in `Z`.

**Local-to-global refinement lemma.** Such an adapter lifts every admissible macro observation-history policy to a concrete policy with the same retained finite trace law.

**Proof.** Compose the macro policy with the adapter at each decision boundary. Condition on the joint state/history at the boundary. The policy is nonanticipatory by item 1, its implementation is feasible by item 2, and the next retained-state/output law agrees by item 3. Iteration proves equality of every finite joint trace law. ∎

This lemma is a compositional proof rule, not an empirical law and not a stand-alone explanation of reality. Its usefulness is that item 3 is a local, independently checkable kernel equation rather than the desired whole-policy conclusion. The financial construction above gives a substantive way to discharge feasibility and build an adapter.

One-way refinement yields inclusion of attainable sets. Equality requires a reverse causal construction or another argument that the concrete implementation has no extra retained possibilities. Theorem 3 supplies that argument by virtual-ledger emulation. Equality of one optimized scalar, a few support directions, or efficient frontiers is insufficient to infer equality of every policy outcome law.

Zero physical duration is therefore stronger than the abstract requirement. A positive-duration implementation can refine a macro action whose duration, hazards, and outputs match it. It cannot refine an instantaneous action with a tighter deadline merely by deleting time from the notation. Likewise, a nonzero cost can be retained in a suitable macro model; it cannot generally be omitted while claiming the original expense and feasibility laws are unchanged.

## Independence witnesses and exact failure points

**Fees.** Capacity one, total one, bill one. From `(b,t)=(1,0)` pay directly. From `(0,1)`, a transfer of one with fee one charged to treasury requires two treasury units, so the bill is impossible. The same typing and accounting vocabulary allows both states; zero fees do not follow from it. Including fees in a more general law is possible, but same-total equivalence then needs another sufficient statistic or a separate symmetry argument.

**Deadlines and permission.** Same total one, zero current cash, bill one now. A transfer allowed now pays it. A transfer allowed only after the bill does not. Future access cannot be treated as current access. Theorem 2 handles this difference rather than denying it.

**Account-dependent risk.** Suppose a cash seizure occurs before a later payment, while treasury is protected, and a transfer opportunity exists after the seizure. Transferring early can lose funds that leaving them in treasury preserves. Greedy cash dominance no longer guarantees equal future totals. Location-neutral dynamics is therefore an independent sufficient premise, not a consequence of the word “resource.”

**A shared transfer quota.** Even without fees or seizure, a total transfer quota is different from independent per-event limits. Let cap one, initial `(b,t)=(0,2)`, and at most one unit transferred over the entire execution. There is a transfer opportunity, then income one, bill one, another transfer opportunity, and another bill one. Early maximum transfer uses the quota; the subsequent income overflows into treasury, and the second bill fails. Deferring the quota lets income pay the first bill and a later transfer pay the second. To cover this institution, retain the remaining quota and solve its scheduling problem; the current greedy theorem does not apply.

**Information.** Let a hidden bit be equiprobable and let `(b,t)=(H,1−H)`. An observer of the split knows `H`; total alone is always one. With a later action guessing `H`, the success probabilities can be one versus one-half. Financial fungibility does not erase the informational content of an account history. Retaining the appropriate posterior can repair this particular loss.

**Policy implementation.** A fixed device that spends whenever cash is present may behave differently after normalization, even though a programmable controller can choose to abstain. The all-policy equivalence requires that the policy class contain the constructed emulators. Physical execution and its memory cost cannot be inferred merely from mathematical existence of a policy.

These examples refute deletion of the respective assumptions **from the stated equivalence claim**. They do not prove that every favorable assumption is individually necessary in every special model. For example, an irrelevant fee may leave a coarse success predicate unchanged, or a known delay may fit within a generous deadline. Necessity is always relative to the claimed query and model class.

## Assumption audit

| Original sufficient assumption | Stronger status established here |
|---|---|
| Entire round bill at most cash cap | Dispensable; replace by exact prefix/storage constraints. With refill before every atomic bill, each individual bill must fit. |
| Income only after the round | Dispensable; interleaved income is covered explicitly. |
| Immediate unrestricted access at all relevant times | Unnecessary for feasibility characterization; bounded and delayed opportunities are covered. It cannot be deleted from same-total equivalence without an adequate replacement. |
| Compulsory maximum normalization | Derivable as an equally expressive scheduler within the stated neutral, independent-opportunity class. |
| Deterministic schedules | Unnecessary; the causal greedy proof applies to adaptive realized histories with branchwise feasibility. |
| Fixed capacity | Can become an observed varying capacity when overflow on reduction is retained losslessly. |
| Free, lossless transfers | A sufficient condition for the present formula. Fees/losses require a different recurrence and can defeat same-total equivalence. |
| Location-neutral dynamics and query | A preservation requirement relative to the selected outcomes; cannot be dropped indiscriminately. |
| Split contains no omitted hidden-state information | Information must be preserved or correctly summarized; account aggregation alone does not prove it. |
| Free/sufficient controller memory | Requires implementation or a restricted controller theorem. The virtual-ledger proof alone cannot remove it. |
| Finite horizon | Every finite-length theorem is proved. A single causal adapter valid forever can also match all finite-dimensional distributions of well-defined infinite processes, subject to implementation and nonexplosive timing conditions. This does not prove infinite survival, finite lifetime burden, or a physically unbounded controller. |

The last row requires one indefinitely valid construction, not an unrelated choice of controller for each horizon. The present financial algorithm is causal and horizon-independent, but its applicability must continue to hold at every event; unspecified future institutions are not included automatically.

## Verification and scope

`financial_schedule_verify.py` independently enumerates all permitted integer transfer amounts rather than using the recurrence to generate its oracle. It compares the exact reachable cash sets with the greedy maximum and independently evaluates (T), (A), and (S).

The completed run checked 504,840 schedules, 1,032,816 evaluated prefixes, and 141,494 fully feasible schedules. The domain has capacities 1–3, initial total 0–4 with every valid initial split, per-event income 0–1, transfer limit 0–2, bill 0–3, and lengths 1–3. Separate witnesses cover spending above the round cap, deadline delay, prohibition of borrowing future income, history-dependent liquidity at equal current totals, the failure of greedy filling with a shared transfer quota, and a transfer-fee counterexample. Results are in `financial_schedule_checks.json`.

The general proofs concern nonnegative real amounts and arbitrary finite sequence length. The finite integer checks test implementation and the derived characterization; they do not establish the general theorem in place of the proof, nor empirical universality. No prior frozen artifact or original source was edited.

The checker, numerical results, assumption ledger, and independent review are included in the [evidence bundle](universality-audit-evidence.zip).
