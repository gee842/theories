# Independent review of the financial schedule theorem

5 October 2026. Reviewed `formal-assumptions.md`, `financial_schedule_verify.py`, `financial_schedule_checks.json`, and the earlier `outputs/access-proof.md`. This review independently checked the algebra and causal reasoning. It did not rerun the 504,840-schedule enumeration or modify the theorem author's files.

**Verdict: the finance recurrence, necessary-and-sufficient inequalities, and greedy policy-emulation argument are sound within the stated class. No blocking issue remains after the author's clarification.** The memo correctly distinguishes general schedule feasibility from same-total equivalence. The separate local-to-global lemma now explicitly requires its kernel identity uniformly over reachable adapter memory/history, or over an expanded state containing that memory. The corrected wording was inspected.

## 1. Independent recurrence check

Use the memo's notation: cash cap C, initial cash b₀, total N₀, event income iⱼ, transfer limit rⱼ, and bill cⱼ. All are finite nonnegative real amounts, with valid initial balances. Let b be cash after the previous event. Crediting income produces

\[
a=\min(C,b+i_j),\qquad N^+=N_{j-1}+i_j.
\]

The allowed transfer interval has upper endpoint min(rⱼ,C−a,N⁺−a). Thus maximum prepayment cash is

\[
a+\min(r_j,C-a,N^+-a)
=\min(C,N^+,b+i_j+r_j).
\]

This expression is nondecreasing in b. With the same total and event data, a larger cash balance cannot make this event's maximum attainable cash smaller. The transfer upper endpoint is attained, so the theorem concerns a maximum, not merely a supremum. Induction establishes both feasibility equivalence and the exact largest postpayment balance.

The rule needs the current financial state and current permission limit. It does not use any later income, later limit, or later bill. It can fill cash before learning the current bill amount, though the associated operational policy still needs its own causal and admissibility specification. If the bill exceeds the greatest current cash, the event is infeasible regardless of future income.

## 2. Independent derivation of the cuts

Write dⱼ=iⱼ+rⱼ−cⱼ. Then the algebraic recurrence is

\[
B_j=\min(C-c_j,N_j,B_{j-1}+d_j).
\]

Repeated substitution gives branches originating from the initial cash, an earlier capacity bound, or an earlier total-funds bound. The last kind simplifies as

\[
N_s+\sum_{k=s+1}^j d_k
=N_j+\sum_{k=s+1}^j r_k.
\]

Because rₖ≥0, the minimum over s is Nⱼ, attained at s=j. Consequently

\[
B_j=\min\left\{
N_j,
b_0+\sum_{k=1}^j(i_k+r_k-c_k),
\min_{1\le s\le j}\left[C+\sum_{k=s+1}^j(i_k+r_k)-\sum_{k=s}^j c_k\right]
\right\}.
\]

Nonnegativity of every term for every deadline j is exactly the memo's total-funds, cash-delivery, and interval-storage system. Requiring every prefix matters: a positive final expression cannot retroactively repair an earlier unpaid bill. Continuing the algebra after a hypothetical failure is harmless because the proof explicitly compares it to physical execution only through the first failure.

The storage cut correctly excludes income and transfer at event s from the right-hand inflow sum: they have already been compressed into the at-most-C balance immediately before bill s. The s=j case correctly requires each indivisible bill to fit the cap. Multiple bills can exceed the cap in aggregate when separately permitted refills intervene.

The proof also covers C=0, zero bills, and zero income by inspection, although the computational grid starts at cap one. For varying observed capacity Cⱼ, replacing C by Cⱼ in the recurrence and by Cₛ in the storage cut is valid if forced excess cash returns losslessly to treasury before the event's payment. The original checker does not verify this extension numerically; the memo says so.

## 3. Policy refinement and information

Theorem 3 fixes the initial split and opportunity mechanism. That is important: it does not say arbitrary same-total splits are equivalent under bounded transfer limits. A greedy controller can keep a virtual ledger for any given admissible controller, use that controller's private randomization and operational decisions, and maintain at least as much actual cash. Totals stay equal because transfers preserve them and the same realized payments/incomes occur. The common operational kernel then supplies the same physical outcome and observation law.

This is a causal construction, not an existence argument selecting a different first action after learning the future. Its validity requires that the virtual ledger updates be available from legitimate information, that the operational actions can be executed in the actual system, and that the compared opportunity mechanism not change because actual transfers differ. The memo states these requirements.

The shared lifetime-quota example is a valid counterexample outside the theorem's class: early greedy transfer consumes the quota, later income overflows into treasury, and the remaining bill cannot be funded. Delaying transfer preserves the quota for after the first payment. This directly demonstrates why independently available per-event limits cannot silently stand in for a history-dependent shared quota.

For adaptive operational policies, testing every resulting branch under the fixed causal policy is appropriate. A probability-one formulation also needs the declared stochastic kernel and measurable execution; the memo does not claim a branchwise worst-case guarantee follows from an almost-sure one. Its finite-dimensional-distribution statement for infinite processes appropriately demands one indefinitely valid causal construction and well-defined, nonexplosive execution. It expressly does not infer infinite survival from finite-horizon checks.

## 4. Local refinement clarification

The general adapter lemma allows memory-dependent adapters but originally stated its one-step joint-law contract primarily in terms of a concrete state z. The necessary precise reading is:

> At every reachable decision history and adapter-memory state, the conditional joint law of next projected state, retained observations, and retained cost/outcome/time increments equals the specified macro kernel, with the same legitimate information interface.

Alternatively, include all memory affecting the adapter in Z and impose the contract for every relevant expanded state. A one-step equality averaged over an unspecified distribution of memory would not justify repeated conditional composition. The author incorporated this clarification, and the corrected statement now supports the induction. The added statement that an atomic bill cannot be subdivided without a real installment interface also correctly fixes the event granularity.

## 5. Exact residual assumptions and verification scope

The finance theorem still needs fungible nonnegative funds, lossless overflow, no borrowing, a cash cap, free treasury-to-cash transfers at declared opportunities, and the stated event order. Its simple dominance argument does not cover account-specific losses, interest, reserve obligations, fees, or a depleted shared quota without reanalysis. The policy theorem additionally needs common operational/observation laws, partition-neutral retained outcomes, legitimate ledger information, and a controller class containing the emulator. These are substantive restrictions, not consequences of merely calling something a resource.

The checker independently enumerates transfer choices and carries the exact reachable cash set; it does not generate its oracle from the greedy recurrence. The closed-form inequalities are evaluated through separate sums. Its loop sizes independently reproduce the declared scenario count: 35 valid initial (cap,total,cash) triples times (24+24²+24³) schedules equals 504,840. The 1,032,816 reported prefixes count evaluated visits, including repeated prefixes across different complete schedules; they should not be described as that many distinct schedules or independent observations.

The updated checker also includes direct shared-quota and fee witnesses. Their code matches the written examples, and their conclusions were checked by hand. The saved outputs report complete agreement on the integer grid. This review did not re-execute that run and therefore does not claim independent reproduction. The general real-valued result is supported here by independently checked algebra and induction. Neither the computation nor this review establishes empirical universality or a complete theory of all financial institutions.
