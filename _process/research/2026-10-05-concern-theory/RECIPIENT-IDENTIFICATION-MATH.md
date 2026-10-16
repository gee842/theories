# Paid identification from another center's positive receipt

6 October 2026. AI-authored continuation of [recipient-specific correction](../../history/2026-10-05-support-and-shared-generativity/completion/RECIPIENT-CORRECTION-MATH.md), [finite recording fidelity](RECORDING-FIDELITY-MATH.md), and [noisy concern inputs](TRANSFER-EVIDENCE-MATH.md). The named bridge is **actual recipient receipt → qualified response correspondence → later paid use**, preserving the real formed predecessor, separate resource accounts and unresolved evidence. This is an identification interface for functional concern, not a derivation of valuation, standing or concern's installation.

The [protocol and executable](../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/README.md) extend the existing coupling producer. The [formal package](../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/formal/README.md) verifies the deterministic client contract and concrete continuation. Original stochastic preparation and prefix reachability have their own independently checked executable evidence.

## 1. What the current receipt identifies

Fix a target during the specified diagnosis-and-use interval. Its productive orientation is Z∈{0,1}. An executed action A and an actual source opportunity V∈{0,1} give target receipt

\[
C=V\mathbf1\{A=Z\}.
\tag{1}
\]

The actor receives the paid action-tagged target receipt. It does not receive Z or V. Target identification and the receipt channel are calibrated local premises. Another center's receipt is not the actor's private income: a recipient capture enters the recipient's reserve, while the actor's private receipt remains zero.

**I1 — Positive identification and zero ambiguity.** C=1 implies A=Z. C=0 alone does not determine Z: action zero with (Z,V)=(0,0) or (1,1) produces the same zero receipt. The source packet, actor costs and acquired zero record can agree in these two worlds. No decoder of that accessible record can return the correct orientation in both.

The finite-history version matters. Consider a fixed finite adaptive policy and a history containing only zero receipts. Its commands are determined by those same acquired records, paid stocks and any same policy random choices. Suppose availability is independently p∈(0,1) in each world, a member of the admitted outage class. If n_z commands match orientation z along that history, its zero-receipt probability under Z=z is (1−p)^{n_z}>0. Under either orientation the failures have the same expenditure and source losses, hence the same accessible resource history. Declaring an exact orientation on that history must be wrong in one possible world. Randomized policies do not fix this: restrict to any positive-probability common finite action/record history and its common decision rule.

For a balanced sequence of 2k attempts before a positive receipt, the all-zero history has probability (1−p)^k in both worlds. No finite number of failures turns that history into a zero-error orientation certificate. This does not prohibit a explicitly risk-bounded negative-evidence inference under a stronger specified statistical model; it prohibits treating nonreceipt as an exact opposite-orientation label.

A positive receipt qualifies an orientation, not its future capture probability. Even after Z is identified, Pr(C=1 for A=Z) depends on future availability. Nor does an old positive identify a target after its response law changes.

## 2. The finite state is paid and inherited

The actual coupling predecessor supplies a five-valued register q and binary last-action field, together with its fuel, active circuit, updater, normal/inverted coupler, acquired-record flag and lifetimes. Eligibility is exactly the existing client predicate: live circuit/updater/coupler, normal coupler, written q∈{0,4}. This does not assume the actor prediction is correct in every inherited history.

A new atomic four-unit recoding recipe is explicitly supplied. It copies the actual inherited bit b into both target cells and resets recipient qualification to false:

\[
q=b_A+2c_R,\qquad \text{old last field}=k_R,
\quad (b_A,c_R,k_R)=(b,b,0).
\tag{2}
\]

The old last-action interpretation ends in this stabilized suffix. No third permanent bit or observer's witness flag is added. The eight combinations of actor bit, recipient candidate and qualification have distinct encodings within the inherited five-by-two capacity. This cardinality fit is not a physical derivation of the wiring: the recoding, target access and stabilized hold remain supplied functional recipes. Using q alone would not provide these eight states.

The actor action reads b_A; the recipient action reads c_R. Actor queries pay the same writes but preserve both cells and the qualification flag. Recipient acquired receipts update as follows:

\[
(c,k)\longmapsto
\begin{cases}
(1-c,0),& k=0,\ C=0,\\
(c,1),& k=0,\ C=1,\\
(c,1),& k=1,\ C\in\{0,1\}.
\end{cases}
\tag{3}
\]

Missing evidence preserves the previous state. The first branch chooses the next exploration action; it does not claim that 1−c is the true orientation. The flag remains false. There is no special observer-controlled final-use phase: each recipient query follows this same rule.

**I2 — Qualification invariant.** Suppose Z stays fixed, target identity and the receipt channel are faithful, and qualification is initially false or already sound. Then at every completed query,

\[
k_R=1\Longrightarrow c_R=Z.
\tag{4}
\]

Recipient queries preserve the actor cell. Actor queries and missing evidence preserve all recipient memory. If a later qualified recipient action is actually feasible and available, it delivers the declared packet to that recipient.

**Proof.** A previously qualified candidate is preserved. An unqualified zero leaves qualification false; no truth claim is created. An unqualified positive sets qualification only when (1) proves the executed candidate equals Z. Induction gives (4). The update changes only the recipient candidate/flag, proving actor noninterference. The action function reads that candidate, so a qualified available execution satisfies (1) and delivers the packet. ∎

This is not a claim that outcome-selected retained bits form an unbiased Bernoulli sample. Qualification is deliberately selected by a positive event, but its inference target is Z and the no-false-positive law entails the label. Using only those positives to estimate availability would instead yield a biased estimate. Raw attempts, absences and costs remain in the experiment's audit; they are not silently available as free permanent controller counters.

A no-exploration rule can hold a wrong inherited candidate forever: C remains zero even when every opportunity is available. A failure-label rule can falsely qualify the opposite orientation after an outage, and can reverse a previously correct record. The specified conventional finite-state table has exactly the same physical information, memory, prices and transition law as (3), so its complete path distribution agrees. No advantage arises from a different description of the mechanism.

## 3. Whole-query admission and escrow

The final protocol uses an explicit fully prefunded query contract. Setup costs four atomically. Each subsequent query requires eight actor fuel units **before any query phase**:

\[
8=1_{\rm retention}+1_{\rm target}+3_{\rm work}
 +1_{\rm acquisition}+2_{\rm writes}.
\tag{5}
\]

After the first two payments, three units are set aside for acquisition and the two-field write, before work occurs. Work then spends three. Acquisition spends one escrow unit; writing spends two. Sham or missing-evidence writes carry the same bill. The escrow is protected by the supplied phase law, so any admitted work has a payable observation and commitment regardless of its outcome. A recipient return cannot finance any actor-side stage. An actor return cannot finance its own admission either.

If the complete eight-unit bill is unavailable, no query is admitted and no partial query bill is charged. Stabilized access ends; the old payload may physically remain but cannot command subsequent trials. Its scheduled packet and later unused packets are lost. This atomic admission law is a declared interface change, not a theorem that arbitrary partial-payment mechanisms behave identically. In particular, it is distinct from the predecessor's sequential setup payments and skipped post-return writes.

With actor fuel F, recipient reserve R, packet count P and escrow e, the formal energy account is

\[
\mathcal E=F+R+10P+e.
\]

Each step satisfies

\[
\mathcal E_{t+1}+\mathrm{paid}_t+\mathrm{waste}_t=\mathcal E_t.
\tag{6}
\]

Reservation moves fuel to escrow, without spending it twice. Work transfers a successful packet to the appropriate reserve or loses it. The commit burns the remaining escrow. Induction proves the finite-trace ledger, including failed-admission packet losses. The already existing two material backing slots persist; no additional permanent state capacity is introduced by the mathematical model.

The source guard and clock remain physical. Every scheduled exposure uses one of the packets declared at the start of preparation, including unavailable, wrong-action and inactive exposures. Opportunity availability is not inferred just from the existence of these source packets.

## 4. Finite exploration without an iid shortcut

While unqualified, faithful acquired zeros toggle the recipient candidate. For a stable Z, every two completed recipient queries without qualification therefore contain one matching action. Assume each matching attempt has a conditional opportunity floor

\[
\Pr(V_t=1\mid\text{complete pre-outcome history},\ A_t=Z,
\ \text{this target and admitted trial})\ge\lambda>0.
\tag{7}
\]

This premise permits history dependence and does not require independent availability. It must apply to matching actions after the actual history, not merely to a marginal average. For example, availability can occur only on wrong actions while having marginal frequency one half; then every receipt is zero despite that favorable marginal frequency.

**I3 — Paid finite opportunity bound.** If the channel and writes are faithful and complete, then

\[
\Pr\{\text{unqualified and at least }2k
\text{ recipient queries completed}\}\le(1-\lambda)^k.
\tag{8}
\]

At a specified deadline, if J is the event of being unqualified with fewer than 2k completed recipient queries,

\[
\Pr\{\text{unqualified}\}\le\Pr(J)+(1-\lambda)^k.
\tag{9}
\]

**Proof.** Let B_j be the event that j matching attempts have completed without an acquired positive. At the next such attempt, conditional on its pre-outcome history, the probability of zero is at most 1−λ. Its occurrence is decided before that outcome; any earlier interruption only removes paths. Iterated conditional expectation gives Pr(B_j)≤(1−λ)Pr(B_{j−1})≤(1−λ)^j. On the event in (8), all preceding observed recipient receipts were zero, so toggling provided at least k matching attempts; that event is contained in B_k. Partition the unresolved event by whether the quota completed to obtain (9). ∎

To omit Pr(J), the system must actually support the quota on every still-unqualified path being claimed: enough original source opportunities, actor fuel, channel access, paid storage, circuit retention and scheduling. A bound conditional on survivors is not an unconditional reliability theorem. The current executable's rational availability branch law supplies a specific finite fixture for (7); it is not empirical identification of that floor.

The generalized bound does not create unbounded experimentation from finite resources. Nor does it add recipient opportunities to the actual five-exposure suffix: that suffix has only three recipient queries, so its general worst-case matching-attempt count is finite. Its exact all-history calculation remains necessary for the particular witness frequency.

## 5. A continuation from the actual formed predecessor

Thirteen ten-unit packets plus the original one-unit source input are declared before the original preparation. The old eight-exposure coupling process runs unchanged; five packets remain for recipient, actor, recipient, actor, recipient. Original failed preparation, ineligible hardware, incorrect inherited records and all resource failures remain in the unconditional results.

An actual eligible endpoint has fuel28, circuit lifetime6, updater lifetime2, normal coupler lifetime2, written q0 and old last0. The saved producer fixture obtains this endpoint from the actual preparation and eight exposures. Lean checks its exact eligibility and paid retrofit, then a complete five-query trace under actor orientation0, recipient orientation1 and available opportunities. It does not claim to have formalized the preceding stochastic coupling process.

The actor balance along this witness is

\[
28\xrightarrow{\rm setup}24
\xrightarrow{R}16\xrightarrow{A}18
\xrightarrow{R}10\xrightarrow{A}12
\xrightarrow{R}4.
\tag{10}
\]

The first recipient action mismatches, pays its bill, and explores without qualifying. The second recipient action obtains a real positive, pays its already reserved evidence/write bill, and qualifies. The third reads the retained qualified candidate and obtains another recipient receipt. Actor commands remain correct in between. The final recipient reserve is20, remaining source is zero, setup cost4, query expenditure40 and lost source10:

\[
28+50=4+40+10+4+20.
\tag{11}
\]

This is a conditional path; the available recipient source outcomes have their declared probabilities. The independent unconditional computation reports strict qualified-later-use probability 1/32 in the primary availability-three-quarters case and 1/18 in the noiseless case. These are probabilities over original preparation and all continuation histories, not success frequencies after selecting eligible survivors.

For this specific correct-actor/available-actor path, the five query entry balances after setup are F−4, F−12, F−10, F−18 and F−16. Each must be at least8. Thus the exact entrance threshold is F≥26. At F25, the second actor opportunity sees only7: no query or partial payment occurs, access ends and the last recipient use cannot take place. The Lean theorem proves the general budget equivalence and checks the boundary instance.

## 6. What would change the claim

The qualification guarantee fails if the recipient target changes after a positive: the old flag can remain true while its candidate becomes wrong. It also fails under false-positive receipt contamination, incorrectly reported target identity, or unmodeled corruption of the retained flag/candidate. The target-change, absent-channel and no-opportunity cases remain explicit adverse controls. Missing observation is not entered as a zero receipt. An incorrect inherited actor cell is preserved rather than secretly corrected; it can prevent funding of later recipient work.

To distinguish availability from mismatch directly, an additional physical observation law is needed. A paid same-opportunity availability latch could license decoding a zero only when its positive report entails actual availability and remains valid through the action. That requires specified sensing, disturbance, timing and retention costs. Current source quantity or an analyst's availability variable is not such a sensor. The present positive-witness mechanism avoids importing one.

The result closes a finite identification obligation for the installed recipient route: qualified evidence is grounded in the recipient's own actual support receipt, and its paid retained state changes later action. It does not derive the target/receipt calibration, recoding chemistry, no-false-positive plant, stable interval, opportunity floor, shared route, willingness to bear the costs, or another center's normative standing. Exact orientation identification also does not supply the signed efficacy probability or perpetual evidence capacity required by broader concern results. Those interfaces and their adverse regimes remain part of the unfinished unified foundation.
