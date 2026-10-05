# Authority weights and the direction of correction

These deductions specify what the evaluator succession model can explain. They are algebraic identities and conditional propositions, not claims of mathematical novelty. The accompanying diagnostic enumerates decisions at saved states without generating new outcome worlds. [Scientific assessment](SCIENCE-ASSESSMENT.md) explains their broader significance and relation to existing research.

## Exact governance drift at a fixed state

Hold production, the rubric, demand, authority memory, and the amendment menu fixed. Let \(p_i^k\) be agent \(i\)'s contract share if amendment \(k\) is implemented, \(W_k\) its usefulness under frozen production, and \(c_k\) its amendment cost. The unchanged rubric is option zero. Each possible governor has utility and choice probabilities

\[
U_{ik}=p_i^k+\lambda W_k-c_k,
\qquad A_{ik}=\frac{\exp(\beta_g U_{ik})}{\sum_{j\in\mathcal K}\exp(\beta_g U_{ij})},
\]

where \(\mathcal K\) is the valid menu. Define

\[
m_i(s)=\sum_{k\in\mathcal K} A_{ik}(W_k-W_0),
\qquad M(s,\pi)=\sum_i\pi_i m_i(s).
\]

Thus \(m_i\) measures the expected immediate effect of appointing governor \(i\), and \(M\) averages that effect over appointment probabilities. This gives the exact identity

\[
\boxed{M(s,\pi)-M(s,U)
=\sum_i(\pi_i-1/n)m_i
=\operatorname{Cov}_{i\sim U}(n\pi_i,m_i).}
\]

Here \(U\) denotes uniform appointment and covariance uses population normalization \(1/n\). The sign depends on whether authority is allocated to governors whose decisions improve usefulness. Concentration alone does not determine the sign.

For the family \(\pi_i(b)=a_i^b/\sum_j a_j^b\), where positive \(a_i\) is the current authority memory,

\[
\frac{\partial\pi_i}{\partial b}
=\pi_i\left(\log a_i-\sum_j\pi_j\log a_j\right),
\quad
\boxed{\frac{\partial M}{\partial b}
=\operatorname{Cov}_{i\sim\pi}(m_i,\log a_i).}
\]

This derivative holds the state and governor responses fixed. It is not the derivative of long-run welfare under a changed policy: that also changes the states encountered and subsequent behavior. If all \(m_i\) are equal, both the policy difference and derivative vanish, whatever the concentration of authority.

## Enumeration of archived states

We evaluated every possible governor under the actual finite logit rule at epochs 80 and 99, from both source histories and both demand contexts. Epoch 80 is the first production period after the matched fork; the states match across the original appointment branches. Epoch 99 is the first later correction opportunity, sampled from the success-based continuation only. At each sampled state both hypothetical appointment policies act on exactly the same production and menu. States at epoch 99 are not asserted to match across the previously run branches.

The stable and changed-demand contexts themselves have different production and updated authority, including at epoch 80. The sign reversal across contexts is therefore a finding in those context-specific states, not a theorem that changing demand alone reverses the covariance with every other state variable fixed.

This is exploratory analysis motivated by the earlier results. No new significance tests, outcome trajectories, or claims of prospective confirmation are attached to it. The table reports the mean over 128 archived worlds of **success-based minus uniform expected frozen usefulness change**:

| Source history | Demand | Epoch 80 | Epoch 99 |
|---|---|---:|---:|
| Success-based | Unchanged | +0.001609 | +0.007382 |
| Success-based | Changed | −0.000969 | −0.068116 |
| Independent | Unchanged | +0.003102 | +0.006868 |
| Independent | Changed | −0.002479 | −0.056901 |

For example, at epoch 99 after success-based history and changed demand, success-based appointment gives an expected immediate gain of 0.007188, while uniform appointment gives 0.075304 on those same states. Both gains are positive; the former leaves substantially more of the available correction unused. The negative covariance occurs in 122/128 worlds for this sample. After independent history it occurs in 116/128 worlds at that date. At epoch 80 it occurs in 115/128 changed-demand worlds under either history.

The diagnostic includes amendment costs in decisions but measures gross usefulness changes. Reference option 7 is available on every evidence day even if it does not meet the qualifying threshold; that threshold controls mandatory correction in the protected arm. The enumeration reconstructs authority after the current epoch's memory update and reproduces each archived actual governor's full choice utilities and appointment weights.

All five identity checks pass at all eight sampled source/context/date combinations. Maximum covariance-identity error is \(5.56\times10^{-17}\); the concentration derivative agrees with a finite difference to \(1.05\times10^{-12}\). Records are in [diagnostic analysis](diagnostics-authority-signal/analysis.json), with per-world arrays alongside it. Reproduce from this directory using the existing numerical environment and `python analyze_authority_signal.py`.

## Two exact controls

**Common governance interests.** Remove only the private-share term from ordinary governance utility, retaining selfish production and every other rule. Then \(U_{ik}=\lambda W_k-c_k\) does not depend on the governor. Starting from identical states, identical amendment draws select identical rules. Production then also matches under shared draws, and induction gives identical production and rubric paths for any two policies differing only in appointment. Appointed identities can differ, but cannot affect outcomes. This does not equate ordinary and protected governance, which impose different decision rules. The diagnostic verifies the conditional version; the pathwise result is a deduction, not an additional trajectory experiment.

**Authority reassignment.** Permute the same appointment weights among governor identities. Averaging all assignments gives each governor expected weight \(1/n\), so the permutation-averaged frozen drift equals uniform drift. Even the \(n\) cyclic assignments suffice. Each assignment preserves the entire probability spectrum and its concentration. This isolates coupling to identities at that state. It does not establish that persistent concentration has no effects in other models. The diagnostic verifies the cyclic average exactly to numerical precision.

## Private redistribution and a restricted concentration gradient

For one candidate amendment, contract shares sum to one before and after, so \(\sum_i\Delta p_i=0\). Therefore

\[
\sum_i\pi_i\Delta U_i
=\lambda\Delta W-c+\sum_i(\pi_i-1/n)\Delta p_i.
\]

Uniform selection cancels private redistribution in average utility. It does not make the resulting decisions welfare-maximizing: averaging a nonlinear choice rule is different from choosing according to average utility.

Counterexample: three governors face a no-op or an amendment with \(\Delta p=(.05,.05,-.10)\), frozen individual usefulness \((0,0,1)\), \(\lambda=.25\), and zero cost. Then \(\Delta W=-.10\), while utility changes are \((.025,.025,-.125)\). As logit rationality grows, two governors adopt the harmful amendment and one refuses. Uniform appointment therefore yields expected harm approaching \(.0667\), despite negative average utility change.

In the separate smooth reduction with no memory and appointments \(\pi_i\propto p_i^b\), \(b\ge0\), the expected gradient of the private-share term obeys

\[
\sum_i\pi_i\nabla p_i
=\frac{\nabla\sum_i p_i^{b+1}}{(b+1)\sum_i p_i^b}.
\]

For \(b>0\), this component ascends a concentration measure on the share simplex; with \(b=0\), it vanishes. This supplies a precise conditional route from allocation-based authority to concentration pressure. It is not the exact simulator drift: memory, finite amendments, other payoff terms, and nonlinear logit choices remain essential differences. The full dynamics need not increase concentration monotonically.

## Why there need not be one underlying gradient

Even a smooth two-agent version need not optimize a shared scalar. Set \(p_1=\sigma(h(x-y))\), \(p_2=1-p_1\), and \(u_i=p_i+\lambda W(x,y)\), with \(W\) twice continuously differentiable. For the joint own-action gradient \(F=(\partial_xu_1,\partial_yu_2)\),

\[
\partial_yF_1=-h^2p_1(1-p_1)(1-2p_1)+\lambda W_{xy},
\quad
\partial_xF_2=+h^2p_1(1-p_1)(1-2p_1)+\lambda W_{xy}.
\]

These cross-partials generally disagree. Thus \(F\) cannot generally be the Euclidean gradient of a scalar potential. Equality on the line \(p_1=.5\) does not establish a potential on an open neighborhood. Other metrics, Lyapunov functions, or restricted representations require separate arguments. This is why feedback and individual optimization do not imply a common backpropagated objective. [Differentiable game mechanics](https://proceedings.mlr.press/v80/balduzzi18a.html) provides the established broader framework.

## What the attractor claims permit

For the linear adjustment case of the [authority model](AUTHORITY-MODEL.md),

\[
\dot q=\nu(C/(D\ell)-q),\qquad
\dot\ell=\rho(1-\ell)-\kappa q\ell,
\quad\nu,\rho,C,D>0,\quad\kappa\ge0,
\]

write \(R=\kappa C/\rho\). When \(D>R\), the unique positive equilibrium is \(q^*=C/(D-R)\), \(\ell^*=1-R/D\). Its Jacobian has trace \(-(\nu+\rho+\kappa q^*)<0\) and determinant \(\nu\rho>0\). The discriminant is nonnegative because \((\nu+\rho+\kappa q^*)^2\ge4\nu\rho\). Hence both eigenvalues are real and negative, including possible degeneracy. No Hopf bifurcation occurs by varying positive \(\nu\). The divergence is \(-\nu-\rho-\kappa q<0\), excluding periodic orbits entirely inside the positive quadrant by the Bendixson criterion. This establishes local equilibrium stability and a limit on possible dynamics, not global convergence or absence of transient certificate failure.

The finite-choice benchmark has a different limitation. If its rules are extended indefinitely with bounded utilities and recurring reference offers, finite logit temperature gives the reference option a uniformly positive probability \(\delta\) at every offer, under every governor. The probability of avoiding that option for \(k\) offers is at most \((1-\delta)^k\), by conditional probability multiplication. It tends to zero. Thus a permanently absorbing class that excludes the reference rubric is impossible under that extension. Extremely long escape times, immediate reversals, or high occupancy of low-usefulness states remain possible. Visiting the reference rubric alone does not guarantee restored production or lasting correction.

These distinctions favor measuring correction time, relapse, and time spent in harmful states. Neither a 160-epoch delay nor the separate two-state ODE establishes a universal meta-attractor.
