# A maintained route from participant harm to rule revision

Constructed finite mechanism, 5 October 2026. This note supplies an exact model and proofs for the new investigation. It does not model the invention, legitimacy, or strategic enforcement of the initial protocol. The executable implementation is `check_model.py`; complete results are `model-checks.json`. All Q and ledger entries in the JSON are in ninths of a unit.

## Physical and procedural specification

Shared productive capacity is E, an integer stock with capacity 3. At E≥2, one round yields 10 units, consumes 2 units of shared capacity and replaces those 2 units from its output. Thus E stays constant while production continues. Below 2, production fails and remaining E is consumed. This idealized technology assumes continuing access to an unmodeled feedstock/energy source; it is not a closed physical universe.

An affected participant has a resource reserve B∈{0,…,6}, receives p units of output and has a required draw of 2 per round. The protected floor is B≥1; this is capacity to keep a specified function and communication option available, not a complete welfare measure. A fee of 1 is consumed when a claim is filed. If incoming resources plus reserve cannot cover the draw, the implementation records unmet demand explicitly. B=0 denotes loss of the protected capacity, not biological death. Production does not require this particular participant's activity. Consequently shared production can persist while the participant is deprived.

Two implemented allocation templates have equal gross output and shared renewal:

| Allocation | Shared | Correction carrier | Participant | Incumbent |
|---|---:|---:|---:|---:|
| F | 2 | f | 3 | 5−f |
| X | 2 | f | 1 | 7−f |

For the principal f=11/9, the incumbent receives 34/9 under F and 52/9 under X. Both cover an incumbent operating requirement of 2 if one is included; the difference of 2 favors X. Outside a binding claim, a supplied current-return comparison/replacement mechanism therefore installs X. This is a stipulated incumbent decision/replacement rule, not a biological selection theorem. Labels F and X name different allocations, not complete judgments about fairness or evil.

The correction carrier has available-work reserve Q∈[0,K]. It must pay upkeep m=1 from existing Q **before** the round's production receipts. A new claim also consumes k=2 from Q before production. If upkeep cannot be paid, the carrier ceases operating, pending or active authority is lost, and subsequent earmarked receipts are discarded rather than magically resurrecting it. A reconstruction procedure is not included. Zero stock immediately after already-paid fees is permissible: that round's service has been paid, and production receipts arrive before the next round's upkeep.

The participant channel has a signal connection and an implemented binding allocation gate. With both available, the following finite protocol operates:

1. Outside an upheld claim, X is selected. If B≤h=4 and the participant can pay 1, filing occurs automatically if Q≥m+k=3. No voluntary bargaining or consent is inferred from this automatic reaction.
2. A filed claim leaves X in force for d=2 rounds, including the filing round. Its processing costs are the initial k plus continuing upkeep. At the end of those rounds, the operative gate imposes F.
3. F remains in force until B reaches its capacity M=6. The claim then releases and current-return replacement again installs X.

The gate, its authority, a correct B signal, allocation templates, thresholds and protected earmark f are supplied parts of the implementation. They are not costless: maintenance and each activation are charged, and access, authority, or earmark withdrawal can disable correction. Their original construction and protection from strategic sabotage are not derived. This is a model of operational reproduction of an already implemented route to correction.

For an operative carrier, with I=1 on filing and 0 otherwise,

\[
Q_{t+1}=\min\{K,Q_t-m-kI_t+f\},
\qquad Q_t\ge m+kI_t.
\]

The inequality is a payment condition, not permission to borrow next round's receipts. Participant accounting is

\[
\tilde B_t=B_t-cI_t,\quad
D_t=\min\{2,\tilde B_t+p_t\},\quad
B_{t+1}=\min\{M,\tilde B_t+p_t-D_t\},\quad c=1.
\]

The implementation tracks the unmet draw 2−D and every cap overflow. Allocation sums to gross output; fees and upkeep are consumed, not returned to the producer. No funding source is counted twice.

## Recurrent correction and exact limits

**Proposition 1: the principal cycle.** Set h=4, d=2, M=6, c=1, K=3, f=11/9. From E∈{2,3}, B=6, Q≥23/9, and an operative carrier with signal and authority, the protocol keeps B≥1 and maintains indefinitely recurrent correction. From Q=23/9 it follows the exact nine-round cycle below. From Q=3, two initial rounds discard excess Q receipts and enter the same cycle.

| Pre-round B | Pre-round Q | Allocation | Filing? | Post-round B | Post-round Q |
|---:|---:|---|---|---:|---:|
| 6 | 23/9 | X | no | 5 | 25/9 |
| 5 | 25/9 | X | no | 4 | 3 |
| 4 | 3 | X | yes | 2 | 11/9 |
| 2 | 11/9 | X | no | 1 | 13/9 |
| 1 | 13/9 | F | no | 2 | 15/9 |
| 2 | 15/9 | F | no | 3 | 17/9 |
| 3 | 17/9 | F | no | 4 | 19/9 |
| 4 | 19/9 | F | no | 5 | 7/3 |
| 5 | 7/3 | F | no | 6 | 23/9 |

**Proof.** Substitute in the payment and participant equations. Every Q prepayment is feasible, the minimum B is 1, the end state equals the initial state, and E is unchanged. Deterministic repetition proves indefinite operation. A finite trajectory alone would not do so; equality of the full state closes the argument. ∎

Cycle accounting independently verifies 90 units of gross output: 18 shared renewal, 11 correction funding, 19 participant allocation, and 42 incumbent allocation. The correction allocation exactly pays 9 units of upkeep and one fee of 2. The participant allocation exactly pays 18 units of draw and one filing fee of 1. Caps discard nothing on this recurrent cycle.

**Proposition 2: sharp thresholds for the supplied protocol.** With M=6, h=4, d=2, c=1 and funded initialization, perpetual protection requires and is possible at:

\[
f\ge\frac{11}{9},\qquad K\ge3.
\]

For f=11/9 and K=3, starting at B=6 in X requires Q₀≥23/9. With generous Q funding and capacity, delay d at threshold h preserves the participant floor precisely when

\[
h-c-d\ge1\qquad(d\ge1).
\]

**Proof of timing.** The participant loses c at filing and one on each of d X rounds, reaching h−c−d before F can replenish it. If this is below 1, the protected condition fails; more money in the correction fund cannot reverse that elapsed loss. If it is at least 1, the subsequent F rounds restore B monotonically.

**Proof of cycle length and funding.** For general M,h,c and d≥1 within this protocol, the X interval before triggering lasts M−h rounds; processing adds d X rounds; restoring the post-processing stock requires M−h+c+d F rounds. Hence

\[
L=2(M-h)+c+2d.
\]

One activation is required in every such cycle. The Q ledger over n cycles, including nonnegative discarded excess W, is

\[
Q_{nL}=Q_0+n\{L(f-m)-k\}-W_{nL}.
\]

If L(f−m)<k, finite Q cannot fund indefinitely many cycles. For the principal parameters L=9, m=1, k=2, giving f≥11/9. At equality, the displayed cycle attains the bound. For any larger f in the admissible budget range, the monotonic Q update funds at least the same actions and clips any surplus. Missing the latest safe trigger cannot restore protection by filing later: a late claim begins at B<4 and its c+d cost crosses the floor. Therefore waiting for funds does not evade the lower bound.

**Proof of liquidity.** A filing requires upfront m+k=3, so K<3 makes it impossible regardless of future income. At K=3 the cycle proves sufficiency. From B=6 the first claim must occur after two ordinary X rounds. These accumulate 2(f−m)=4/9, requiring Q₀+4/9≥3, or Q₀≥23/9. Such Q₀ also pays every earlier upkeep. ∎

These are sharp bounds for this release-at-M protocol. Permanently maintaining F, altering filing rules, adding recovery resources or changing the claim lifetime defines a different model and can change the bounds. For example, a perpetually locked F benchmark has no recurring claim cost.

## Controlled comparisons and failures

All three principal comparisons use the same production, funding f=11/9, capacities, initial stocks and routine correction upkeep:

* **Externally locked F:** B stays 6, E stays 3, and Q stays 3. This is a deliberately external benchmark; it receives permanent protection by stipulation and is not a demonstrated self-maintaining institution.
* **Incumbent-only revision:** participant access is disabled; the current-return rule selects X. At round 6, B=0. Thereafter E=3, Q=3, output remains 10, and one unit of participant draw remains unmet every round. The carrier can remain funded yet fail to translate the participant's condition into binding action. This is not an impossibility result about all possible benevolent controllers.
* **Effective participant channel:** the displayed recurrent correction cycle maintains E, B and the carrier.

At f=m=1 and initial Q=3, one claim can be funded. Q subsequently remains at 1, enough for routine upkeep but insufficient for another activation; B reaches 0 at round 15. A working office and an effective remedy are therefore distinct in this mechanism. A capacity of 26/9 never permits the first filing. Adding one processing round, d=3, crosses the B floor at round 5 even though correction later restores B; eventual recovery does not establish uninterrupted protection.

After the first successful recovery at round 9, the model separately withdraws the protected surplus earmark, participant signal access, and binding authority. All three interventions cause subsequent failure of the participant floor while shared production continues. Thus initial success does not establish that the system can protect its own correction constitution against capture.

## Exact verification and scope

The principal finite state space contains 2,380 canonical states: E=0,…,3, B=0,…,6, Q in ninths from 0 to 3, the ordinary/queued/recovery modes and the absent-carrier state. Every transition was enumerated and all successor states remained inside the space. Every orbit was followed to its exact repeated full state. Of 1,008 initially protected states, 272 remain protected indefinitely. There are seven recurrent attractors; two preserve the protected conditions, one at E=2 and one at E=3.

The code also checks the payment-order threshold, initial liquidity, timing family and intervention comparisons, while auditing resource conservation at every evaluated transition. An independent Fraction implementation by another reviewer reproduces 45 successive principal rounds and examines 149 safe parameter cases independently. The general proof carries the continuum funding claim; the finite sweeps are corroboration rather than proof over every real parameter.

This is an executable conditional mechanism with exact accounting. It establishes neither an empirical institutional law nor that evolution necessarily favors this correction structure. Affected standing, honest information and binding execution are operationalized here, while their origin, legitimacy and strategic robustness remain explicit unsolved parts. The result strengthens the question of regeneration: maintenance of shared production can coexist with deprivation, and preserving correction requires resources, usable access, enforceable consequences and timely operation together.
