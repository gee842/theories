# Prospective archives, conditional anomaly tests, and independent questions

Mathematical working memo, 5 October 2026. AI-generated research assistance under Ren's research direction. This memo derives a finite prospective-retention and revision procedure. Statistical tests, information constraints, and decision optimization used here are established methods, applied to an explicitly supplied question and candidate grammar. No experiment code is implemented here.

## 1. What is chosen before the future question is known

An institution routinely retains the total number of switches in each four-transition binary history. Before seeing those histories or the later question, it prepays retention of \(m\) randomly selected full switch words. The selection schedule is independent of their contents. Routine count records and their cost are common to all designs; \(c_a\) per selected window prices additional acquisition, retention, and reserved audit work.

Later, \(Q\sim\operatorname{Bernoulli}(\lambda)\) is revealed. If \(Q=0\), the task is the routine count question, which the count archive answers completely. If \(Q=1\), the task is the continuation decision described below. All post-question testing, validation, and deployment expenditure occurs only for \(Q=1\). The prepaid \(mc_a\) is incurred in either case. Initially take \(Q\) independent of world and archive; dependent questions require the corresponding conditional world prior instead.

This is uncertainty over which of two declared questions will matter. It is not a probability distribution over every unconceived question. Likewise, the candidate described below is supplied in a finite library but excluded from routine deployment until the specified procedure admits and validates it. A designer's meta-prior giving that candidate positive probability is not global Bayesian ignorance of its existence.

The archive constraint can be physical as well as monetary. With \(n\) fixed windows, three bits encode a count in \(\{0,\ldots,4\}\), while four encode its full switch word. Replacing \(m\) count records by raw words uses \(3n+m\) data bits if the selected locations are known from a shared prepaid schedule. This accounting does not claim that one extra bit appended to an existing count can reconstruct every raw word: it replaces the encoding for those windows. Schedule, linkage, and metadata costs must be included if they are not assumed available.

## 2. Four worlds that separate different failures

For each independent window, draw \(K\sim\operatorname{Binomial}(4,1/4)\). Conditional on \(K\ne2\), order the switches uniformly. Conditional on \(K=2\), give the two clustered words \(0011\) and \(1100\) total probability \(q\), equally split, and give each of the other four arrangements probability \((1-q)/4\). Start the associated state path from an independent fair binary state, making its final state \(Z\) fair and independent of the switch word.

Let \(D=K_{\mathrm{late}}-K_{\mathrm{early}}\). The next state equals \(Z\) with probability \(1-r\) and differs with probability \(r\). Define:

| World | Historical clustering \(q\) | Future switching probability \(r\) |
|---|---:|---|
| E: exchangeable | \(1/3\) | .25, regardless of order |
| P: persistent relationship | 1 | .45 if \(D>0\), .05 if \(D<0\), .25 if \(D=0\) |
| T: transient pattern | 1 | .25, regardless of order |
| U: unflagged relationship | \(1/3\) | .45 if \(D>0\), .05 if \(D<0\), .25 if \(D=0\) |

At \(q=1/3\), all six arrangements with \(K=2\) are equally likely, so the switch word is exactly iid Bernoulli\((1/4)\). At \(q=1\), its order is nonexchangeable while its entire count distribution remains the same. Individual switch-position marginals also remain .25. This conditional construction is deliberately different from independent early/late switching rates: the latter generally alter the total-count distribution and would not prove the count-level impossibility claimed here.

The active policy treats only when \(Z=1\), at cost \(c=.3\); untreated current need causes loss one. Its expected loss is .275 in every world. The supplied candidate additionally treats when \(Z=0,D>0\). It needs the ordering of the current deployment history, priced separately below. The response is assumed to prevent the loss, and diagnosing future need is assumed to yield a truthful label. Neither causal efficacy nor the alternative grammar is discovered by the order test.

## 3. Exact information limits

**Counts cannot distinguish these worlds.** The joint distribution of \((K,Z)\) is identical in E, P, T, and U. For any count-based randomized admission rule \(\phi\),

\[
\Pr_E(\phi=1)=\Pr_P(\phi=1)=\Pr_T(\phi=1)=\Pr_U(\phi=1).
\tag{1}
\]

If its false-admission probability in E is at most \(\alpha\), its power in P is at most \(\alpha\), however many count-only windows are retained. More computation cannot recover the discarded order.

The statement is stronger if routine records include one future need label \(Y\) per independent window. For each fixed \(K\), positive and negative \(D\) are symmetric. P and U therefore have average future switching probability .25 conditional on \(K\), exactly like E and T. The entire joint law of \((K,Z,Y)\) remains identical. One binary label per window cannot reveal the missing interaction after order has been erased. Repeated labels sharing a latent risk, or different observations, would be a different experiment.

**Raw history does not establish future transport.** Here raw history means the specified four-switch word together with its endpoint, not a record already linking that word to the future target. P and T have identical full historical distributions. So do E and U. Every archive-only gate has identical distributions within each pair, even with unlimited raw history. In particular,

\[
\Pr_U(\phi=1)=\Pr_E(\phi=1)
\tag{2}
\]

for a raw-history anomaly gate as well. No historical anomaly test can have both low size in E and high power to admit the useful relationship in U. Fresh observations linking order to future need are necessary to distinguish those pairs. The conclusions concern the declared observation channels, not an impossibility under every possible future investigation.

More generally, let \(P_w^{D_a}\) be the distribution of whatever archive data the gate actually receives, and write a randomized gate as an acceptance probability \(g(D_a)\in[0,1]\). Defining total variation as \(\operatorname{TV}(P,Q)=\sup_B|P(B)-Q(B)|\),

\[
\Pr_U(G=1)\le\Pr_E(G=1)+
\operatorname{TV}(P_U^{D_a},P_E^{D_a}).
\tag{2a}
\]

To verify this, use \(\mathbb E_P g=\int_0^1 P\{g>t\}\,dt\) and bound each probability difference by total variation. Thus external randomization cannot solve observational equivalence, and nearly equal archive laws allow at most correspondingly small power above size. The bound applies to the entire joint archive distribution, including its sample size and available public traces; it is not automatically the one-window distance when many independent windows are observed.

These facts separate preserving order, detecting nonexchangeability, and demonstrating that a response will help. They also prevent a successful anomaly detector from being mistaken for a general detector of useful new questions.

## 4. An exact conditional order gate

Under a homogeneous iid switching model with any \(h\), conditional on \(K=k\) all \(\binom4k\) orders are equally likely. Mixtures over \(h\) preserve that conditional law. For independent windows, conditional on their counts, the within-window orders remain independent and uniform. This removes the unknown homogeneous rate from the order test.

Among \(m\) prepaid raw windows, let \(M\) have \(K=2\), and let \(C\) of those be clustered, meaning \(|D|=2\). Under the exchangeability null,

\[
C\mid M\sim\operatorname{Binomial}(M,1/3).
\tag{3}
\]

Use the exact upper-tail probability \(\Pr\{\operatorname{Bin}(M,1/3)\ge C\}\) and reject when it is at most \(\alpha_a=.05\). With \(M=0\), do not reject. This is the complete conditional permutation calculation for the chosen order statistic, not a simulation approximation. Conditional validity for every count vector implies unconditional level at most .05. Discreteness makes it conservative at some sample sizes.

The conditioning principle is standard permutation-test mathematics; [Hemerik and Goeman, *Exact testing with random permutations*](https://arxiv.org/abs/1411.7565), give a primary treatment of exact permutation validity. Here the six possible arrangements are summarized analytically, so no sampled-permutation correction is needed.

The number of raw windows is fixed before the histories, and the gate is evaluated once. Repeatedly checking the same ordinary binomial tail until it passes would require a different sequential guarantee. Selecting windows because their order looks anomalous would also invalidate (3). A fixed independent random subset avoids that selection.

## 5. Exact audit power and a finite resource requirement

Let \(b(n,p;j)=\Pr\{\operatorname{Bin}(n,p)\ge j\}\), and let \(k_\alpha(n,p)\) be its smallest rejection count, allowing \(n+1\) when no attainable count rejects. In these four worlds,

\[
\rho_2=\Pr(K=2)=\frac{27}{128},\qquad
M\sim\operatorname{Binomial}(m,\rho_2).
\]

The exact audit admission probability in a world with clustering probability \(q\) is

\[
A_q(m)=\sum_{j=0}^{m}\Pr(M=j)\,
b\bigl(j,q;k_{\alpha_a}(j,1/3)\bigr).
\tag{4}
\]

For P and T, \(C=M\), and \((1/3)^3<.05<(1/3)^2\). Thus

\[
\boxed{A_P(m)=A_T(m)=\Pr\{\operatorname{Bin}(m,27/128)\ge3\}.}
\tag{5}
\]

For E and U, \(A_E(m)=A_U(m)\le.05\). At \(m=28\), P/T audit power is approximately .953299; at \(m=27\), it is .944477. Consequently 28 prepaid raw windows are the smallest fixed number achieving at least .95 power against this particular clustered alternative. This is not .95 power against U, against every nonexchangeable pattern, or under arbitrary dependence.

If homogeneous switch rates vary more broadly, the conditional size guarantee remains valid, but \(\Pr(K=2)=6h^2(1-h)^2\) changes the number of useful windows. Without a lower bound away from \(h=0,1\), no uniform finite audit budget guarantees many informative \(K=2\) windows. Statistical validity and enough diagnostic exposure are separate requirements.

## 6. Fresh validation and a net deployment threshold

An admitted candidate is frozen before a fresh, independent validation pool of \(\ell\) histories and subsequent need labels is acquired. The whole pool is paid for, including cases outside the candidate context. Eligibility \(I=\mathbf1\{Z=0,D>0\}\) is determined from history before its future need label is observed. There is no extension until enough successes appear.

Because

\[
\Pr(K=1)+\Pr(K=3)=\frac{120}{256},
\qquad \Pr(K=2)=\frac{54}{256},
\]

the eligibility probability is

\[
\tau_q=\tfrac14\{\Pr(K=1)+\Pr(K=3)+q\Pr(K=2)\}
=\frac{120+54q}{1024}.
\tag{6}
\]

Hence \(\tau_E=\tau_U=69/512\) and \(\tau_P=\tau_T=87/512\). Given the eligible count \(J\), the number of future need events \(S\) has distribution

\[
J\sim\operatorname{Binomial}(\ell,\tau_w),\qquad
S\mid J\sim\operatorname{Binomial}(J,p_w),
\tag{7}
\]

where \(p_P=p_U=.45\) and \(p_E=p_T=.25\).

Suppose executing the candidate also costs \(f=.002\) per deployment case to retain or inspect order. The gross action improvement is \(\tau_w(p_w-c)\), and net deployment improvement is \(\tau_w(p_w-c)-f\). A test against \(p\le c\) alone would not certify that extra expense.

The proposed conservative correction uses a supplied eligibility lower bound \(\tau_{\min}=69/512\), valid for the declared \(q\in[1/3,1]\), and tests against

\[
\boxed{p_* = c+\frac{f}{\tau_{\min}}
\simeq .3148405797.}
\tag{8}
\]

If a candidate is nonbeneficial after deployment expense, then

\[
\tau(p-c)\le f\quad\Longrightarrow\quad
p\le c+f/\tau\le c+f/\tau_{\min}=p_*.
\tag{9}
\]

Therefore rejecting \(p\le p_*\) by the exact \(\operatorname{Bin}(J,p_*)\) upper tail at \(\alpha_v=.05\) controls acceptance of any nonpositive net deployment policy under these assumptions. Random \(J\) is harmless because the bound holds conditionally for every \(J\), and eligibility precedes the outcome. The lower bound on eligibility is part of the model, not a value inferred from the hidden world. If it fails, the net-benefit guarantee need not hold.

If \(p_*\ge1\), the conservative rule never accepts; its assumed deployment expense cannot be overcome at the supplied worst-case eligibility by evidence that a probability exceeds \(p_*\).

The exact validation probability is

\[
V_w(\ell)=\sum_{j=0}^{\ell}
\Pr\{\operatorname{Bin}(\ell,\tau_w)=j\}\,
b\bigl(j,p_w;k_{\alpha_v}(j,p_*)\bigr).
\tag{10}
\]

It certifies neither recovery of sunk inquiry costs nor truth of an entire temporal model. It tests the declared policy's net deployment contrast. In a domain where treatment efficacy itself is unknown, observing need would not identify its causal effect; a suitable randomized causal comparison would be required.

## 7. An independent route for asking an unflagged question

When the anomaly gate does not open, a predeclared independent challenge coin can admit the candidate with probability \(\eta\). This is independent of unseen validation and deployment outcomes. Conditional on world \(w\), the probability of running validation is

\[
\boxed{R_w(m,\eta)=A_w(m)+(1-A_w(m))\eta
=\eta+(1-\eta)A_w(m).}
\tag{11}
\]

Fresh validation gives adoption probability \(R_wV_w\). With \(\eta=0\), nonbeneficial adoption in E is at most \(\alpha_a\alpha_v=.0025\), using independence of the two pools conditional on E. In T the anomaly is real, so the corresponding bound is only \(\alpha_v=.05\). With challenges, the general null-policy bound is \(R_w\alpha_v\le\alpha_v\). Multiplying the two .05 levels for every world would be incorrect.

The audit cannot give high admission probability to U: \(R_U\le\eta+(1-\eta)\alpha_a\). Thus obtaining admission probability at least \(1-\beta\) in U requires

\[
\eta\ge\frac{1-\beta-\alpha_a}{1-\alpha_a}
\tag{12}
\]

when the numerator is positive; the actual audit size can make the requirement stronger. This is an admission constraint, not a guarantee that finite validation has enough power. Independent questioning matters here because U provides no archival anomaly at all, not merely because too few old records were retained.

## 8. Exact prospective risk, costs, and resource feasibility

For one deployment, the candidate's gross operating improvements over the baseline are

\[
\begin{aligned}
\Delta_P&=.15(87/512)=.02548828125,\\
\Delta_U&=.15(69/512)=.02021484375,\\
\Delta_E&=-.05(69/512)=-.00673828125,\\
\Delta_T&=-.05(87/512)=-.00849609375.
\end{aligned}
\tag{13}
\]

Let \(H\) future deployments follow validation and let each of the \(\ell\) validation cases cost \(c_v\). Relative to common routine costs and the continuation baseline \(\lambda H(.275)\), exact world-specific incremental expected loss is

\[
\boxed{
C_w(m,\eta)=mc_a+
\lambda R_w(m,\eta)
\left[\ell c_v+V_w(\ell)H(f-\Delta_w)\right].
}
\tag{14}
\]

Audit retention is prepaid even when the later question is routine. Validation cost is incurred whenever the candidate is admitted, whether it passes or fails. Deployment order cost is incurred only on adoption. Failed audits and inconclusive validation are not free. Audit and validation probabilities multiply conditional on world; after mixing worlds, multiplying their marginal probabilities would generally be wrong.

With world prior \(\pi_w\), optimize \(\sum_w\pi_w C_w\) over feasible pre-data choices. A hard episode budget, unlike an expected-cost objective, must cover the most expensive permitted realized branch. For any workflow able to validate and adopt, a sufficient constraint is

\[
mc_a+\ell c_v+Hf\le B.
\tag{15}
\]

Storage bounds and any separate resource types impose additional constraints. A low probability \(\lambda\) of receiving the continuation question does not make an unaffordable realized branch feasible.

For \(\eta=0\), define

\[
W_w(m)=A_w(m)\left[HV_w(\ell)(\Delta_w-f)-\ell c_v\right].
\tag{16}
\]

The audit-first design beats no inquiry exactly when \(\lambda\sum_w\pi_wW_w(m)>mc_a\). Thus, if the expected bracket is positive, its question-frequency threshold is \(\lambda>mc_a/\sum_w\pi_wW_w(m)\). With only P assigned prior \(\pi\) and a fixed mixture of E/T assigned probability \(1-\pi\), let its mean bracket be \(W_N\). When \(W_P>W_N\), the equivalent prior threshold is

\[
\pi>\frac{mc_a/\lambda-W_N}{W_P-W_N}.
\tag{17}
\]

A threshold above one means that this workflow cannot pay even at certainty of P. These are ordinary conditional decision thresholds, not an ethical argument against retaining evidence whose purposes this loss function omits.

## 9. Why scalar Bayes optimization selects endpoint challenge rules

For fixed \(m\), (14) is affine in \(\eta\). Therefore an endpoint \(\eta=0\) or \(\eta=1\) attains its minimum under any fixed scalar Bayesian expected-loss objective, absent another constraint; interior values can tie when the slope is zero.

At \(\eta=1\), validation always occurs for \(Q=1\), regardless of the audit. Its candidate, validation sample size, and validation rule are unchanged. Every \(m>0\) then adds audit expense without changing decisions, so direct validation with \(m=0\) weakly dominates, strictly if \(c_a>0\). It pays nothing when \(Q=0\), unlike a prepaid archive.

Consequently the finite Bayesian comparison need only include no inquiry, audit-first workflows for feasible \(m\), and direct validation. A direct route is not a statistical loophole: it acquires fresh ordering-to-outcome data, an observation channel absent from a count-only archive. Its success does not contradict (1). It does show that archive-induced inability to revise is conditional on an institution requiring archival anomaly before buying new evidence.

For robust comparison over the supplied worlds, define each workflow's regret relative to the best workflow in the same finite set for that world. A lottery \(x_j\) over workflows solves the finite linear program

\[
\min_{x,t}t,\qquad
\sum_jx_j=1,\quad x_j\ge0,\quad
\sum_jx_j\bigl(C_w(j)-\min_k C_w(k)\bigr)\le t\quad\forall w.
\tag{18}
\]

The comparator knows the world but remains restricted to those workflows; it is not a clairvoyant controller of each future state. A minimax-regret lottery can benefit from mixing endpoint workflows because a maximum over worlds is nonlinear. Every workflow in its support must individually meet any hard branch budget. This does not establish optimal robustness to worlds outside the declared set.

## 10. Admission, validation, and updating must remain distinct

Rejection of exchangeability makes an order-sensitive question admissible in this procedure. It does not identify which supplied candidate transports to current need. T and U demonstrate both directions of failure: an anomaly can be useless for action, and a useful action relationship can have no archival anomaly.

The admission rule supplies a transition into a finite candidate library; it does not generate previously inconceivable alternatives. If a Bayesian implementation later uses the same audit data for model probabilities, the gate is not an additional independent observation: for observed data \(D_a\) and deterministic gate \(G(D_a)\), \(\Pr(w\mid D_a,G(D_a))=\Pr(w\mid D_a)\). If only the gate result survives, its likelihood \(\Pr_w(G)\) must instead be used. A \(p\)-value is not that likelihood. The fresh validation pool in this proposal avoids reusing the gate data as a confirmatory policy test.

The prospective design answers a bounded question: what evidence should be prepaid before knowing which declared future task will arise, when retention, fresh testing, and deployment all have costs? It does not show that more raw storage or more admission is always better. Counts can be sufficient for routine estimation yet erase a later diagnostic signal; raw history can still be unable to justify transport; fresh evidence and an independent route to asking a question can restore a revision opportunity. Those are distinct, testable constraints on a specified institution's ability to change its conclusions.

## 11. Audit of the finite implementation

The inspected `experiments/prospective-revision/model.py` and `PROTOCOL.md` implement the mixtures, question timing, validation threshold, cost decomposition, and finite minimax-regret problem above. The six tests include independent small trinomial enumeration, explicit branch-cost enumeration, observation-law equivalence, and a linear-program primal/dual certificate. The inspected saved results report a minimax primal/dual gap of approximately \(2.7\times10^{-15}\); this is numerical verification within the finite supplied workflow class, not an empirical uncertainty interval or proof of optimality among all possible inquiries.

With the recorded baseline \(\lambda=.5\), \(\ell=1024\), \(H=500\), \(c_a=.02\), \(c_v=.002\), and \(f=.002\), audit-28 admits U's useful candidate through both gates with probability .0271941 conditional on the continuation question. Direct validation adopts it with probability .9383754. Their incremental expected losses in U are respectively +.4658416 and −3.2490902. These values include all specified costs. They illustrate the exact identification limit: preserving an anomaly-sensitive archive does not make useful but historically unflagged questions likely to be considered.

Across the recorded 286 denominator-ten world priors at that question frequency, direct validation minimizes loss in 233, no inquiry in 49, and an audit-first workflow in four. These are grid counts under chosen costs, not probabilities over real institutions or a universal frequency of optimal practices. They provide a useful counterexample to the claim that prospective preservation is always the best source of revision. In this model, purchasing fresh target-linked evidence often dominates prepaying historical order merely to decide whether that fresh evidence may be purchased.
