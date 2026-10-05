# A paid learning–action–correction–succession loop

Internal formal research note, 5 October 2026. This is an exactly specified mechanism specimen and its closure conditions, not an empirically complete theory of conscience. It extends the shared-feature learning interface developed in the accompanying learning audit. It supplies neither phenomenal experience nor universal moral standing by mathematical stipulation.

## 1. What is learned, and what remains a premise

Three quantities start at zero:

- `w`: the learned adverse value of a shared outcome feature. An independently experienced adverse event originally supplies teaching magnitude `β>0`; subsequent rehearsal can replay its stored trace. Fresh suffering is not required at each update.
- `g`: learned alignment between that feature in self-related experience and a recipient's situation. Independently observed structural or role matches supply target `G∈[0,1]`.
- `z`: the estimated efficacy of a proposed repair, measured as the fraction of recipient harm actually prevented.

The effective transferred concern weight is `v=gw`. Neither `v` nor its initial presence is assumed. The model nevertheless **does** assume that aligned features share an action-value route, so that another's predicted adverse outcome can influence choice through `gw`. Learning alone does not prove that natural systems will adopt this routing instead of an identity gate. The teacher's primitive valence, alignment evidence, available repertoire, scheduled rehearsal, audit access, and transfer mechanism are explicit premises. A preserved teaching archive can retain the original outcome record even when its learned action-value association weakens; its storage, content fidelity, and copying must also be paid. If that archive degrades, constant `β,G` must be replaced by their actual time-dependent values.

Let a generation have `m≥1` operating intervals. During every paid interval,

\[
w^+=(1-\delta-\eta)w+\eta\beta,
\qquad g^+=(1-\kappa)g+\kappa G,
\qquad z^+=(1-\gamma)z+\gamma E.
\]

Here `0<η≤1`, `δ≥0`, `δ+η≤1`, and `0<κ,γ≤1`. The first rule is rehearsal plus leakage; the second is alignment learning; the third is error-driven revision of an action's causal efficacy. At succession, retained contents become

\[
(w,g,z)_{n+1,0}=(t_w w_{n,m},t_g g_{n,m},t_z z_{n,m}),
\qquad 0\le t_i\le1.
\]

Transmission has an explicit resource cost. Multiplicative loss is an idealized model of attenuation, not a universal account of cultural inheritance. Repeated local calibration may restore what transmission loses.

**Timing:** each interval begins with the current `w,g,z`. Its decision is made before that interval's learning update. Costs are paid, the chosen action and declared validation probe occur, actual outcomes and material returns are observed, and then the updates are applied. After the last update of a generation, paid transmission initializes the next generation. A new successor therefore cannot use a later refresher lesson for its first decision.

## 2. Actual outcomes and a critic that can be wrong

Consider a controlled recipient situation with independently established baseline harm `H>0`. An unprotected outcome has harm `H`. Repair has actual efficacy `Q≤1`, hence actual harm `(1−Q)H`. A negative `Q` means the purported repair worsens the recipient's condition.

In the exact specimen, a feasible paid probe compares this baseline with a separately measured recipient outcome after the candidate intervention:

\[
E=(H-H_{\mathrm{after}})/H=Q.
\]

This is **not a free access to true efficacy**. Probe construction, measurements, baseline comparison, and any compensation or recipient burden must be included in the costs and harm accounting. The result assumes a controlled setting where this comparison is identifiable. With unknown baselines, selective observations, noisy measurement, or adaptive recipients, the equality is unavailable and an additional identification argument is needed. A deterministic divisible population is one implementation: the observed fractions are exact aggregate quantities. A finite stochastic individual trial does not inherit an almost-sure version of these conclusions merely by substituting mean efficacy.

The audit runs on its declared paid schedule even if the incumbent policy is currently withholding repair. Otherwise a mistaken low estimate could prevent all further evidence, and the specified `z` update would be fictitious. The validation schedule is an installed scaffold; this theorem does not explain its selection. Actual recipient outcomes, rather than the observer's comfort, are the critic's target.

**Separate probe-harm ledger.** One concrete validation regime uses a separately metered cohort of mass `ρ>0` per interval. It receives the candidate intervention in a controlled challenge with known per-unit baseline `H`; no untreated trial arm is needed because that baseline is independently known. Its actual residual harm is

\[
L_k^{\rm probe}=\rho(1-Q)H,\qquad
L_k^{\rm operating}=\begin{cases}(1-Q)H&\text{repair chosen},\\H&\text{otherwise},\end{cases}
\qquad L_k^{\rm total}=L_k^{\rm operating}+L_k^{\rm probe}.
\]

These are actual harms, not resource fees. In the conservative comparison where no probe means no extra challenge exposure, the no-repair, no-probe reference has harm `H`. Thus operating-recipient protection alone does not establish total harm reduction. With continuous repair, total harm is `(1+ρ)(1−Q)H`, below that reference precisely when `Q>ρ/(1+ρ)`. At the untrained start, operating repair is absent and the extra probe harm is already incurred. Compensation may consume resources or benefit someone afterward; it never erases an incurred harm from this ledger.

The executable favorable specimen sets `ρ=1/10`, `Q=4/5`, `H=10`. Each probe therefore adds harm `1/5`; operating harm falls from `10` to `2` once repair is chosen, and total harm then equals `11/5`. Its resource audit fee `1` separately pays `ρ[a+(1−Q)b]=16/25` for the probe intervention and `9/25` for measurement. The fee must be recomputed if efficacy or protocol changes. Induced-probe burdens, consent, and acceptability are not settled by these arithmetic comparisons. Any claimed all-recipient safety condition must constrain this separate harm ledger, including the bootstrap, rather than only the resource budget.

## 3. Learned transfer changes a decision with fully counted private costs

Let `b=min(d,e)≥0` be the cheaper private cost of tolerating an unprotected encounter (`d`) or bypassing its private consequences (`e`). Both leave recipient harm `H`. A repair attempt costs `a>0`; failures still incur their share of private unprotected costs. Estimated burdens are therefore

| Choice | Estimated private cost | Estimated recipient harm |
|---|---:|---:|
| Best unprotected response | `b` | `H` |
| Attempt repair | `a+(1−z)b` | `(1−z)H` |

Adding learned recipient weight `v=gw` gives the exact strict-choice condition

\[
\boxed{\ z\,[b+Hgw]>a\ }.
\tag{1}
\]

Ties select the unprotected action in this specimen. Taking `a>b` rules out repair being selected solely for private return when `0≤z≤1`: a strictly positive learned contribution is then necessary. This avoids incorrectly treating repair expenditure `a` as its entire private cost when some repairs fail.

When chosen, actual repair costs `a+(1−Q)b` and leaves actual recipient harm `(1−Q)H`. Choice and outcome must be reported separately. A high `z` can produce confident harmful intervention if the true `Q` is negative. A corrective decrease in `z`, followed by less intervention, is a success of criticism—not a loss of wisdom. For `0<Q≤1`, the selected repair produces real harm reduction; a required recipient standard `H_max` further requires `(1−Q)H≤H_max`, independently of the choice threshold.

## 4. An exact succession threshold

For the favorable stationary case assume `0<Q≤1`, fixed teachers and efficacy, paid valid updates, and positive transmission `t_i>0`. Write

\[
r_w=1-\delta-\eta,\quad A_w=\eta\beta;
\qquad r_g=1-\kappa,\quad A_g=\kappa G;
\qquad r_z=1-\gamma,\quad A_z=\gamma Q,
\]

and `S_m(r)=1+r+…+r^{m−1}`. Each coordinate has generation map

\[
x_{n+1,0}=R_x x_{n,0}+t_x A_x S_m(r_x),
\quad R_x=t_x r_x^m<1.
\]

Its unique periodic start value is

\[
\boxed{\ x_*={t_x A_x S_m(r_x)\over1-t_x r_x^m}\ }.
\tag{2}
\]

Within this periodic orbit each nonnegative coordinate rises from its generation-start minimum toward its local learning target. From the completely untrained state, generation-start values rise monotonically:

\[
x_{n,0}=x_*\,(1-R_x^n).
\tag{3}
\]

Consequently the least protection score in every sufficiently late generation is its score at the start. The following equivalence is exact:

> **Eventual durable-protection theorem.** From `w=g=z=0`, a finite generation exists after which repair is strictly preferred at every operating interval if and only if
> \[
> \boxed{\ z_*[b+H g_*w_*]>a.\ }
> \tag{4}
> \]
> The conclusion additionally needs continuing payment and valid outcome evidence. It is eventual, not safety from the untrained starting time.

**Proof.** Equations (2)–(3) follow by summing an affine recurrence. Transmission never raises a nonnegative coordinate, so its periodic minimum is at succession. Starting from zero, all three start coordinates approach that minimum from below. The decision score is continuous and nondecreasing in these coordinates. If (4) holds, a finite start crosses the threshold and all subsequent phases remain above it. If (4) fails, every generation-start score is at most `a`, so the all-phase conclusion fails. Equality does not establish strict preference. This proves the equivalence.

Equation (4) is a joint learned-transfer threshold, not a definition of inclusion as reproductive fitness. `g_*` and `w_*` are learned from non-protection teachers; `z_*` is checked against actual recipient results. A failed inequality permits intermittent late-generation repair while excluding durable repair immediately after succession.

“Protection” in this theorem concerns the operating recipient. The conclusion does not include validation recipients, guarantee a reduction in total harm, or retroactively protect the untrained bootstrap. Those require the separate probe-harm ledger and its own constraints.

If validated lower bounds `g_min,z_min>0` are independently preserved, define

\[
T={a/z_{\min}-b\over H g_{\min}}.
\]

Then the sufficient stationary valence condition is `w_*>T`, equivalently

\[
\eta\beta>{T(1-t_w r_w^m)\over t_w S_m(r_w)}.
\tag{5}
\]

It is exact when those bounds are the actual minima and their phases coincide. It displays the competing contributions of teaching strength, leakage, transmission, and rehearsal. A zero transmission factor gives a zero start coordinate; with decisions before refresher training, strict all-phase protection requiring that coordinate is impossible. A paid refresh-before-decision stage can change this timing assumption, but must be modeled rather than silently credited.

## 5. Expansion has an exact boundary too

For a finite set of recipient classes `j`, use separately learned `g_j`, efficacy estimates `z_j`, and known `H_j,a_j,b_j`. One shared `w` is sufficient; parallel audit and alignment costs must grow as required by the actual implementation. Durable protection of every declared class occurs exactly when

\[
\min_j\{z_{j,*}[b_j+H_jg_{j,*}w_*]-a_j\}>0,
\tag{6}
\]

subject to each class's actual efficacy and the joint resource condition. A new class with positive independently warranted feature alignment can become protected without ever rewarding or punishing the actor. A class with `G_j=0` cannot acquire transferred concern through this channel. No generalization to an arbitrary unfamiliar identity is proved without a matching feature relation.

For infinitely many classes, pointwise eventual protection is weaker than a single finite time or positive margin for all. Bounded `w` cannot overcome unbounded class thresholds. Nor does this channel determine which beings have moral standing: its learned coverage can remain inadequate and require architectural or ethical revision.

## 6. Payment and the order of events

Let `C_k≥0` include **all costs paid before an interval's return**: rehearsal, alignment observations, audits and probes, selected action, common upkeep, and transfer when scheduled. Let actual replenishment `Y_k≥0` arrive afterward. Resource stock satisfies

\[
B_k\ge C_k,\qquad B_{k+1}=B_k-C_k+Y_k.
\tag{7}
\]

This prevents payment with a later return before it exists. For any realized finite bootstrap of length `N`, the exact minimum starting reserve is

\[
\boxed{\ D_N=\max\left(0,\max_{0\le k<N}\left[C_k-\sum_{i<k}(Y_i-C_i)\right]\right).\ }
\tag{8}
\]

It includes every prefix, so financing only the mean cost is insufficient. This condition applies while `w,g,z` are still forming, when repair may be absent or misguided.

For a repeated, fully paid `m`-interval operating schedule, put `P_0=0`, `P_j=Σ_{i<j}(Y_i−C_i)` and `E=P_m`. An indefinitely solvent execution with a finite initial reserve exists **if and only if**

\[
\boxed{\ E\ge0\quad\hbox{and}\quad
B_0\ge D:=\max(0,\max_j[C_j-P_j]).\ }
\tag{9}
\]

If `E<0`, every finite reserve is eventually exhausted. If `E≥0`, each later generation begins with at least as much reserve as the first. This proves necessity and sufficiency. Surplus `E` can be discarded or transferred after every generation, producing a bounded repeating buffer; capacity at least `B_0+max_{0≤j≤m} P_j` suffices for this particular discard schedule. The maximum includes the final receipt at `j=m`, before surplus disposal. It need not be the minimal capacity among all disposal schedules.

For a bootstrap followed by this repeating regime, check (8) on the bootstrap **and** require the stock at its end to be at least `D`. Equation (4) together with (9) is an exact closure test only when the specified operating and bootstrap costs have actually been counted. If repair costs more than the unprotected option, an all-repair cost envelope may conservatively finance the entire learning phase. Otherwise compute the realized choices explicitly.

Replenishment is a physical/environmental premise requiring its own causal account. A permanently maintained external supply is not explained by writing `Y_k` into an equation. Likewise, finite storage does not create infinite work. These results expose what the proposed continuing process must obtain; they do not manufacture those conditions.

## 7. Correcting a harmful action rather than endlessly increasing concern

Suppose a previously favored repair actually has `Q<0`. With paid valid probes and no succession during `k` revisions,

\[
z_k=Q+(z_0-Q)(1-\gamma)^k.
\]

For nonnegative bounded `w≤w_max`, `g≤g_max`, let `M=b+Hg_max w_max`. If `M=0`, the repair score is already zero and cannot exceed `a>0`. If `M>0`, the false intervention is certainly stopped once

\[
z_k\le {a\over b+Hg_{\max}w_{\max}}.
\tag{10}
\]

The right side is positive, so the crossing is finite for a negative target. This supplies a usable detection bound. It does not erase damage before detection; the probe regime and bootstrap need safety bounds and accounting. A fixed probe schedule can continue harming its validation cohort after operating repair stops. The correction check records that harm; ending or changing such probes requires an additional rule and changes the available update sequence. Unknown environmental change also requires continued audit access and a finite response time. The stationary theorem cannot promise correct action immediately after unobserved change.

Concern and criticism therefore have different roles: `gw` makes recipient effects action-relevant; `z` can overturn an initially mistaken understanding of which act helps. Greater concern paired with a corrupted critic can amplify harm.

### Separate improvement: an exact-evidence gate on the critic's own probes

Retain the fixed-schedule failure above as a counterexample. An improved policy adds a candidate-specific `has_valid_assay` flag and a persistent `suspended` record. Subject to a prefunded expense and exposure allowance, a candidate without a valid assay may receive one bounded pilot. Immediately after each valid assay, set `has_valid_assay=true`; if its **actual assay signal `E≤0`**, suspend both ordinary deployment of that candidate and further active probe exposure. This gate reads `E` directly because the controlled specimen has `E=Q`; waiting for the smoothed estimate `z` to become nonpositive would discard available evidence. Suspension takes effect after observation and cannot undo actions or harm already incurred in that interval.

For stationary `Q>0`, every valid assay is positive. From the all-zero learning state, `z` becomes positive after the first assay and stays positive with positive transmission. This gate therefore leaves the favorable recurrence and theorem unchanged **while the independent resource and exposure rules continue to authorize its schedule**. A finite lifetime probe quota would change that schedule and requires a new maintenance calculation.

For the negative example, `Q=−2/5`, `z_0=4/5`, and `γ=1/2`: one assay changes `z` to `1/5`, but the gate already suspends the candidate because `E=−2/5`. Exactly one cohort of mass `1/10` was exposed, so induced probe harm is `7/5=1.4`; no later active probes are run. The earlier smoothed-estimate crossing and fixed-probe failure remain valid for the original policy, not the gated one.

The rejection record must remain available to successors, with its storage and transfer paid; attenuation of `z` alone must not erase it and silently authorize a fresh pilot. Reopening requires a declared new candidate or justified evidence of changed conditions, possibly from passive observations, plus renewed allowance. Consent, a bounded pilot's actual harm limit, and funding remain premises. The exact-sign rule gives no immediate guarantee for noisy or biased assays; those need a separately justified evidence and exposure policy. This refinement makes the validation procedure itself revisable without claiming that validation is harmless.

## 8. A stable harmful loop and a self-distress control

Expand the action family with an action `M` that hides the observer's distress cue without improving the recipient. This requires **separate private cue-relief and recipient-efficacy channels**: `M` removes the private distress loss but has recipient efficacy `Q_M=0`. Its total private cost is the masking expense alone. It is not a repair from the earlier table, where failure to protect the recipient also retains private loss; substituting `Q_M=0` into that table would wrongly add `b`. If the critic substitutes observer-cue relief for recipient outcome, every use supplies `E_M=1`. Thus `z_M` can converge toward maximal apparent recipient efficacy even as actual harm remains `H`.

Concrete values: `H=10`, `v=1`, private unprotected loss `d=6`, repair cost `4`, and cue-masking cost `1`. Suppose both repair and mask are initially predicted to remove both the observer's cue and all recipient harm. Their perceived burdens are `4` and `1`, so masking wins. It actually removes the observer's private loss but leaves recipient harm `10`. If the only audit reads that same relieved observer cue, the apparent success reinforces itself. A return of at least the paid masking-and-learning costs can make this loop materially persistent. Resource solvency and accurate prediction of observer relief therefore do not establish recipient-directed correction.

**Control.** Meter recipient outcomes through a channel the masking action cannot suppress, and compare actions that equally relieve the observer's distress while differing in recipient benefit. With correctly learned mask efficacy `0`, the example's world-directed burdens are `1+vH=11` for mask and `4` for successful repair, so repair is chosen. Test this under private choice, no anticipated reciprocity, and real opportunity costs; the behavioral contrast is evidence for world-directed valuation, not a proof of subjective experience or uniquely identified motivation. Independent measurement and protected critic access are substantive premises whose failure can undo the closure.

## 9. An optional material bridge: care can renew its own support

The reserve conditions can be coupled to a concrete productive state instead of stipulating a permanently sufficient receipt. Let `X_n≥0` denote an affected recipient's shared productive capacity. With `0<ℓ≤1`, effective all-generation care `u_n∈{0,1}`, and restored capacity `p≥0`, suppose

\[
X_{n+1}=(1-\ell)X_n+p u_n,
\qquad \mathcal Y_n=y_0+sX_n,
\quad y_0,s\ge0.
\tag{11}
\]

Here `p` is capacity restoration accomplished by the paid intervention; `y_0` and `sX` require ongoing physical input and work-conversion mechanisms. They are not work created by concern itself. Assume the total cost `C` of the all-care generation includes operation, learning, outcome audits, and succession; the within-generation arrival schedule remains subject to (8).

After learned care becomes continuous, `X_n→X_*=p/ℓ`. A strict surplus

\[
\boxed{\ y_0+s p/\ell>C\ }
\tag{12}
\]

makes generation net receipts positive after a finite time. With a finite reserve covering the learning period, capacity build-up, and every cost-before-return prefix, this productive coupling then sustains the specified care process. If the reverse strict inequality holds, generation deficits eventually have a positive lower bound, and every finite reserve fails without another source or changed practice. Neither sign changes the recipient's standing.

At equality, failure is **not** automatic: if capacity starts below `X_*`, the remaining deficits sum to the finite amount `s(X_*−X_start)/ℓ`, plus any intra-generation reserve requirement. That amount can be financed by a finite stock. This boundary case matters because persistent positive deficits need not have unbounded cumulative size.

Equation (11) is one sufficient material mechanism, not a requirement for deserving care. An unproductive recipient may still warrant protection supported by other resources. Nor does productive care guarantee that the resulting surplus is allocated back to learning or protection: the specified budget rule must retain authority over it. Capture, depletion of external inputs, or changed efficacy breaks the stated closure.

## 10. Executable specimen and limits

`dynamics_checks.py` implements exact rational recurrences, decision comparisons, succession, prefix solvency, a negative-efficacy correction, and the masking counterexample. Results are in `dynamics-checks.json`. It checks both a fully paid durable regime and a lossy-transmission regime that fails at each generation's beginning. These are mathematical checks and constructed examples, not observations of human or biological development.

The closed loop is:

`stored adverse experience → learned shared feature value + alignment → predicted recipient effect → chosen act → actual recipient outcome → paid causal criticism → renewed resources → paid succession → relearning`.

The theorem establishes an eventual maintained learned capacity under declared conditions. It leaves open the natural origin of the shared routing, reliable critic institutions, ongoing supply, and their coexistence under selection. It also leaves open the normative adequacy of the recipients and harms represented. Those are specific remaining explanatory tasks, rather than a fixed concern parameter hidden inside an alleged explanation of its own origin.
