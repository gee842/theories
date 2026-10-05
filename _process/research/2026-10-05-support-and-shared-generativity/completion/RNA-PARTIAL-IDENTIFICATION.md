# RNA joint replacement: what is identified, bounded and still free

5 October 2026. AI-authored secondary derivation using the preserved primary sources and frozen [RNA identification audit](RNA-IDENTIFICATION-CONTRACT.md). New calculations are exact algebra and finite sums, not fitted parameters, new measurements, or a rerun of source extraction. The [certificate](../../../../experiments/shared-renewal-capability/rna-partial-identification/README.md) preserves the inputs and checks.

**Result.** Microscopic nonidentification does not necessarily prevent a joint RNA prediction. In a precisely declared two-RNA restriction of the published model, the author's computational preparation and transfer settings identify a joint probability of approximately **0.0866263712553**, uniformly over the two coefficients' printed rounding intervals. Conversely, the available physical measurements do not identify the corresponding droplet transition kernel. Even complete separate RNA trajectory distributions can agree while the joint task differs. A sharp mean-and-capacity bound and an explicit pair of such alternatives specify exactly what a joint measurement adds.

This task is one-stage net replacement of two RNA populations together with retention of their association. It does not require every original RNA molecule to have worn out, or replacement of replicase, ribosomes, compartments or externally supplied apparatus. It therefore does not measure the synthetic study's complete material-successor event. No RNA molecule is identified with CF, a gate, or a fabricator.

## 1. The target and the identification question

Keep the earlier assay fixed. Prepare equal-volume compartments, count initial host and parasite abundances \((H_0,P_0)\), incubate to a physical deadline \(T\), retain a fraction \(\rho=1/D\) of whole compartments, and assess immediately after retention, before fusion. Every original preparation is in the denominator. The event is

\[
E_T=\{H_0>0,P_0>0,H_T\ge DH_0,P_T\ge DP_0,\ R=1\},
\qquad J_T=\Pr(E_T).
\tag{1}
\]

Here R is the actual retention indicator. Multiplication by \(\rho\) is justified only when retention is conditionally uniform and independent of incubation outcome. Uniformly sampling a fixed fraction of a finite ensemble suffices for each tagged preparation's marginal probability; retention indicators across preparations need not be independent.

For a model M, let \(\mathcal O(M)\) denote the specified observable probability laws or population summaries. Its identified set is

\[
\mathcal I_J(o)=\{J_T(M):\mathcal O(M)=o, M\text{ satisfies the declared model class}\}.
\tag{2}
\]

The target is identified when this set is a singleton, even if many microscopic descriptions remain possible. Finite sample uncertainty is a separate problem: the three recorded replicates are not an exactly known population law. None of the bounds below turns a sample mean into a known population mean without stating that additional premise.

### A microscopic ambiguity that leaves this target unchanged

The source's Supplementary Text 4 uses the replicase-resolved equations reproduced in [the earlier contract, §4](RNA-IDENTIFICATION-CONTRACT.md):

\[
\dot x_i=x_i\sum_jc_{ij}e_j(1-\sum_lx_l/C),\qquad
\dot e_i=\tau_i x_i(1-\sum_le_l/C_E).
\]

The transformation \(e\mapsto\lambda e,\tau\mapsto\lambda\tau,C_E\mapsto\lambda C_E,c\mapsto c/\lambda\), with scaled initial enzyme, leaves every RNA trajectory x unchanged. Consequently it also leaves (1) unchanged when preparation and retention are fixed. **This scale ambiguity is a nuisance for the RNA-only target, not a proof of task nonidentification.** It matters for an enzyme-amount, energetic-cost or binding-state target. The source explicitly omits association/dissociation for lack of measured parameters. [Mizuuchi et al., Supplementary Text 4](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-022-29113-x/MediaObjects/41467_2022_29113_MOESM1_ESM.pdf).

Likewise, different on/off rates with the same Michaelis curve show a residence-time ambiguity. They do not by themselves prove different RNA replacement probabilities. That conclusion requires an association-resolved transient model, its initial bound state, and a demonstration that the target depends on them. Full microscopic parameter identification is not a prerequisite for every useful functional prediction.

## 2. A nontrivial prediction already fixed by the declared conventional model

Consider only HL2-228 host H and PL2-228 parasite P; the other three RNAs are absent. The conventional effective equations are

\[
\dot h=ah^2(1-(h+p)/C),\qquad
\dot p=bhp(1-(h+p)/C).
\tag{3}
\]

Use the source's computational settings C=300, D=5, normalized deadline T=2 and independent Poisson(10) starting counts for these two types. These are **model specifications**, not measured droplet occupancy, physical capacity, or a physical two-hour calibration. The original notebook initializes all five types; setting three to zero is our declared restriction. Its absent `211017.csv` is not reconstructed as an original file. We use the printed S23 coefficients, which the frozen workbook audit independently reconstructs. [Published model Methods](https://doi.org/10.1038/s41467-022-29113-x), [pinned author code](https://github.com/rmizuuchi/Mizuuchi_Evo_RNA_Complexity/tree/defaabf8633d25fd809ac9ddfec7d65f44083207).

Allow the full six-decimal rounding intervals

\[
a\in[2.7904395,2.7904405],\qquad
b\in[5.7118375,5.7118385].
\tag{4}
\]

They are display-precision enclosures, **not experimental confidence intervals**. Let r=b/a. Rational comparisons and integer powers establish

\[
2.046<r<2.047,\qquad 26.9<5^r<26.99.
\tag{5}
\]

For example, \(5^{2046}10^{1000}>269^{1000}\) and \(5^{2047}100^{1000}<2699^{1000}\) prove the second enclosure without floating-point exponentiation.

For positive initial integers h,p, the trajectory relation is \(p(t)=p[h(t)/h]^r\). Since r>1, both fivefold thresholds are first met when the host reaches 5h. A finite crossing is possible exactly when

\[
5h+5^r p<300.
\tag{6}
\]

The integer states satisfying the sufficient condition \(5h+26.99p<300\) and necessary condition \(5h+26.9p<300\) are identical:

| Initial parasite p | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Maximum successful initial host h | 54 | 49 | 43 | 38 | 33 | 27 | 22 | 16 | 11 | 6 |

Every h from 1 to the listed maximum is included. No positive-h state with p≥11 succeeds. Empty/singly occupied compartments fail. For h≥60, the host threshold alone reaches capacity; for p≥12 the lower bound in (5) already excludes success. A finite check of h=1,…,59 and p=1,…,11 therefore exhausts the positive states. There are 299 successful states, uniformly for (4).

### The finite deadline is certified, not replaced by an infinite-time limit

It remains to prove those states succeed by T=2. Put \(L=5h+26.99p<300\) and \(c=L/1500\). On 1≤u≤5, r>1 and (5) imply

\[
hu+pu^r\le(L/5)u,
\quad
T_*\le\frac1{ah}\int_1^5\frac{du}{u^2(1-cu)}
=\frac1{ah}\left[\frac45+c\ln\frac{5(1-c)}{1-5c}\right].
\tag{7}
\]

The rational grid for L gives L≤299.99, hence \(c\le29999/150000<1/5\) and the logarithm's argument is at most 120001. The finite Taylor sum \(\sum_{n=0}^{16}12^n/n!>120001\) proves \(\ln120001<12\). Since a>2.79 and h≥1,

\[
T_*<\frac{16/5}{2.79}=\frac{320}{279}<2.
\tag{8}
\]

Thus (6) is the actual deadline event throughout (4), not merely eventual feasibility. The notebook's terminal integer truncation does not change an inequality whose threshold 5h or 5p is an integer, when applied to the exact ODE solution; this does not certify the original numerical solver's error.

Let m(p) be the table's upper host bound. With independent uniform retention,

\[
\boxed{J_2=\frac{e^{-20}}5\sum_{p=1}^{10}\sum_{h=1}^{m(p)}
\frac{10^{h+p}}{h!p!}.}
\tag{9}
\]

The rational finite sum and a directed Taylor bound for \(e^{20}\) give

\[
\boxed{\frac{86626371255287543892294575296}{10^{30}}
<J_2<
\frac{86626371255287543892294575297}{10^{30}}.}
\tag{10}
\]

This is a prediction of the stated conventional model, stable to printed rounding. It does not establish robustness to measured biological variability, model error, or changing capacity, preparation, physical clock, mixing and retention. The earlier observed-extrema sensitivity of r is much wider than (4), is not a confidence interval, and crosses the r=2 capacity boundary for a fixed h=p=10. An ensemble of Poisson starts is also different from putting exactly ten of each RNA in every compartment: the latter cannot satisfy (6) at the central coefficients.

## 3. What means and capacity can identify without that ODE

Fix positive initial abundances h,p. Assume no net loss, and let new increments be \(X=H_T-h\), \(Y=P_T-p\). Suppose the only population information is

\[
X,Y\ge0,\quad X+Y\le M,\quad
\mathbb E X=\mu_x,\quad\mathbb E Y=\mu_y.
\]

Set thresholds a=(D−1)h, b=(D−1)p. The class contains arbitrary joint endpoint laws on this simplex; it does not impose (3). For compatible nonnegative means with \(\mu_x+\mu_y\le M\), the **sharp identified set** for \(p_A=\Pr(X\ge a,Y\ge b)\) is

\[
\boxed{\begin{cases}
\{0\},&M<a+b,\\
[0,\min(1,\mu_x/a,\mu_y/b)],&M\ge a+b.
\end{cases}}
\tag{11}
\]

Proof: the upper bound follows from \(a\mathbf1_A\le X\) and \(b\mathbf1_A\le Y\). The lower endpoint is attained by assigning probabilities \(\mu_x/M,\mu_y/M,1-(\mu_x+\mu_y)/M\) to (M,0),(0,M),(0,0). For the upper endpoint q<1, suppose q=μx/a is the smaller ratio. Put probability q at (a,y*) and the rest at (0,y0), choosing

\[
y_*\in[b,M-a]\cap
\left[\frac{\mu_y-(1-q)M}{q},\frac{\mu_y}{q}\right],
\qquad y_0=\frac{\mu_y-qy_*}{1-q}.
\tag{12}
\]

The interval is nonempty: its four endpoint comparisons follow respectively from M≥a+b, qb≤μy, μx+μy≤M and M≥0. This law attains q and both means. Exchange x and y for the other case. For q=1 use the single mean point; q=0 and M=0 are immediate. Mixing the lower and upper laws fills the whole interval without changing their means or support. The result also holds for integer counts when a, b and M are integers. In (12), split noninteger coordinates between adjacent integers within their success/failure regions. For q=1, the mean point lies in the triangle with integer vertices (a,b), (M−b,b), (a,M−a), so a mixture of those vertices preserves it. A noninteger count-capacity bound must first be replaced by its integer floor.

With independent retention, multiply (11) by ρ. If loss cannot be excluded, apply the same theorem directly to nonnegative endpoints H_T,P_T, thresholds Dh,Dp and a bound H_T+P_T≤C, rather than assuming nonnegative increments. For continuous abundances, unequal positive material costs can be handled by scaling X,Y, their means and thresholds by those costs; the resulting bound remains sharp in that continuous class. For integer counts, this scaling gives a continuous relaxation and hence a valid upper bound, but need not give a sharp integer bound. Sharpness then requires optimization over the actual weighted integer support. An actual valid resource bound is required. The code's C=300 does not supply a measured physical bound.

For example, let X,Y be nonnegative integers with 2X+3Y≤6, thresholds X,Y≥1, and means E[X]=7/5, E[Y]=1. The only successful integer state is (1,1), whose resource use is 5; every failure uses at most 6. Thus 29/5=E[2X+3Y]≤5q+6(1−q), giving q≤1/5. This is attained by weights 1/5, 2/5, 2/5 on (1,1), (3,0), (0,2). In contrast, the continuous mean point (7/5,1) itself succeeds and is feasible, so the scaled continuous upper bound is 1. This review correction does not alter the equal-cost theorem or the certificate in §2.

Equation (11) shows why even precise mean production and a shared capacity need not imply a positive lower bound on joint replacement. It also gives a genuine upper bound when the means are measured under the target conditions. For varying initial counts, those quantities must be conditioned on the initial state or treated in a joint optimization; substituting bulk means into a fixed-state formula is not justified.

### Full marginal success data improve the interval, but pairing remains relevant

If a matched experiment identifies \(p_H=\Pr(H_0>0,H_T\ge DH_0)\) and \(p_P=\Pr(P_0>0,P_T\ge DP_0)\), the elementary intersection bounds give

\[
\rho\max(0,p_H+p_P-1)\le J_T\le\rho\min(p_H,p_P).
\tag{13}
\]

These bounds are sharp when only the two event marginals and independent retention are imposed. Further resource/support restrictions can tighten them. If retention is only known to have marginal probability ρ, its dependence on production must also be included: the three-event bounds become \(\max(0,p_H+p_P+\rho-2)\le J_T\le\min(p_H,p_P,\rho)\). One cannot assume the factor ρ in that case.

## 4. An exact task-changing ambiguity, distinct from enzyme rescaling

Here is an explicit pair of endpoint/path laws for the observation map consisting of both individual RNA trajectory laws, but no matched cross-RNA observations. Start every compartment at H=P=1, take D=5 and capacity C=10, and let f(t) be any continuous nondecreasing function with f(0)=0 and f(T)=1. For a fair Bernoulli Z, define

\[
\begin{array}{lll}
\text{Aligned:}&H(t)=1+4Zf(t),&P(t)=1+4Zf(t),\\
\text{Opposed:}&H(t)=1+4Zf(t),&P(t)=1+4(1-Z)f(t).
\end{array}
\tag{14}
\]

Each RNA's entire marginal trajectory law is identical in the two alternatives; both mean paths equal 1+2f(t). All trajectories are nondecreasing and their total never exceeds 10. At the deadline, however,

\[
\begin{array}{c|c|c|c}
&\text{endpoint law}&\Pr(H_T\ge5,P_T\ge5)&J_T\ (\rho=1/5)\\ \hline
\text{Aligned}&\tfrac12(5,5)+\tfrac12(1,1)&1/2&1/10\\
\text{Opposed}&\tfrac12(5,1)+\tfrac12(1,5)&0&0.
\end{array}
\tag{15}
\]

Equation (14) describes continuous abundance paths. An integer-count version replaces 4f(t) by any common nondecreasing integer staircase s(t) from 0 to 4; its two marginal path laws and all endpoint claims remain identical to each other. Neither version asserts an elementary reaction mechanism or a finite-rate Markov law.

With exactly half of each endpoint type in an even-sized ensemble, even both aggregate RNA time courses agree exactly. The endpoint cross moment differs: E[HP]=13 versus 5, or covariance +4 versus −4. A matched joint tail count distinguishes the task directly; a cross moment separates this displayed pair but does not generally identify an arbitrary joint tail.

These alternatives are observation-equivalent **for the stated marginal/bulk observation class**. They are not solutions of the fixed deterministic ODE (3), an identification of elementary RNA chemistry, or a claim to reproduce every observation in the entire paper. They show which information the ODE supplies by assumption and which information a joint measurement would supply experimentally. Pairing two bulk fold measurements in one batch does not recover the joint distribution within its droplets.

## 5. Where the actual public evidence enters

| Preserved evidence | What it constrains | What it does not determine for (1) |
|---|---|---|
| Fig. 4 processed replicate folds, including paired donor/target rows | The measured bulk interaction contrasts and the authors' normalized effective coefficient transformation | The distribution of counts jointly within a droplet, matched initial counts, physical retention or joint failure frequency |
| SI S23 plus the pinned notebook | The declared effective ODE, computational capacity, random preparation and transfer rules; these permit (9) after our two-RNA restriction | Whether these closures and normalized clock apply to a new physical assay; the missing original CSV and unseeded realization remain unavailable |
| S19 strand-specific synthesis measurements | Selected bulk synthesis outputs at two and five hours | A within-compartment association/renewal transition or original-molecule turnover; the HL1 label ambiguity is unresolved |
| SI translation extension and protein-related assays | An explicit conventional alternative with latent replicase; some bulk enzyme-related information | Full calibrated active-enzyme and binding trajectories in each droplet; the RNA-only scaling symmetry need not prevent an RNA-only prediction |
| Dryad sequence-file listing | Availability of a PacBio archive and sequence-level evidence | A raw joint droplet trajectory table in that listing |

The relevant paired Fig. 4 observations were already preserved by the frozen audit. Reusing its JSON, without reopening or recalculating the workbook:

| Source row | Donor fold P | Reported target fold Q |
|---|---:|---:|
| 37 | 3.808441308 | 62.5324256670592 |
| 38 | 3.740502647 | 45.8889906340716 |
| 39 | 3.230509937 | 91.7231896186724 |

All three bulk records fail a donor fivefold threshold; this statement does not depend on how the target normalization is interpreted. But these were translation-uncoupled assays: replicase was preproduced, the later replication stage inhibited further translation, and target folds were normalized against a negative-control reaction. They are not three trials of (1), and their observed failure frequency is not a population zero-probability result. [Mizuuchi et al., interaction-assay Methods and Fig. 4](https://doi.org/10.1038/s41467-022-29113-x). The source normalization and biological regime must be transported and validated before using such means in (11).

The existing observations therefore support a sharply specified **conditional conventional prediction**, but not a numerically calibrated physical identified interval for the new droplet task. Formally, in a context-indexed model class that fixes all observed-regime laws while imposing no cross-regime transport relation on the new assay, the target kernel can vary without changing those laws. If the preparation's co-occupancy probability ω is known and no tighter task support restriction is imposed, the resulting design-only interval is [0,ρω]. If ω is also unspecified, it is [0,ρ]. These intervals describe that observation-model class; they do not assert that every endpoint law is chemically realizable by the actual clones. Independently measured resource, kinetic and retention restrictions must be imposed before calling a narrower interval physical.

The 2016 purified-replicase data concern different clones and do not fill this gap. The known printed evolved-host efficiency inconsistency remains unresolved; no disputed value, microscopic on/off choice, or CF interpretation enters the new certificate.

## 6. The minimal separating observation and a falsifiable contract

For identification of the count-and-retention target itself, the minimal missing datum is a **matched joint success indicator**, tied to the initial counts and actual retention of the same preparation. Recording H0,P0,HT,PT and R is a direct sufficient observation scheme. Full enzyme-residence identification is unnecessary if this is the sole target. Count empty, unsuccessful and lost preparations; a survivor-only dataset changes the denominator. Measuring both marginal threshold probabilities narrows the target by (13); measuring their coincidence removes the residual coupling ambiguity when retention is independently verified.

For a predictive test, use separate calibration data to establish the joint preparation law, a physical clock, effective kinetics under that preparation, and either a defensible capacity law or an explicit resource model. Freeze the resulting model class before evaluating joint outcomes. A set \(\Theta\) of shared permissible parameters gives the prediction interval

\[
\left[\inf_{\theta\in\Theta}J_T(\theta),\ \sup_{\theta\in\Theta}J_T(\theta)\right],
\quad
J_T(\theta)=\rho\sum_{h,p>0}p_0(h,p)\,
\mathbf1\{\text{capacity and deadline inequalities hold for }\theta\}.
\tag{16}
\]

The infimum/supremum is outside the sum because one parameter vector applies to all preparations. Taking separate optimal parameters for each occupancy yields only conservative bounds, not the sharp common-parameter identified set. Nuisance directions preserving the RNA kernel can be quotiented out. Stochastic kinetics replace the deterministic indicator by an independently specified joint transition probability; an ODE's mean trajectory does not identify that law.

For the declared normalized model, (10) is already such a prediction, with \(\Theta\) equal to (4). A matched assay outside a physically calibrated version of its predicted interval would falsify that conventional closure. A same-state/different-binding-state intervention from the earlier contract can then test whether association state explains the discrepancy. A positive result would support a richer conventional mechanism before it supported any broader theory.

The source outcomes were known before these secondary deductions. The exact certificate is a model calculation, the displayed alternatives are mathematical witnesses, and the physical joint experiment remains unrun. No held-out result or new empirical support for a universal renewal direction is claimed.

## Preservation and verification

Only this new note and the [new calculation directory](../../../../experiments/shared-renewal-capability/rna-partial-identification/README.md) are added. The checker verifies the frozen audit SHA-256 and its producer, checks all eight source hashes before and after its read-only use, and records its own producer hash. It reuses saved numerical observations; it does not execute the author notebook, fit a model, extract the workbook again, or integrate an ODE. Exact integer/rational inequalities certify (5), the 299-state classification, (8), the directed enclosure (10), and the displayed endpoint witnesses. The general sharpness proof of (11) is analytic; finitely many rational constructions provide implementation diagnostics, not its proof.

Read scope for this addition: previously preserved source paper, SI Text 4, S12/S23 and author-code cells, plus the frozen audit JSON. Fresh browser requests to the publisher and pinned repository failed through redirect/retrieval errors; the already preserved primary bytes supplied the source check. No new external source was downloaded, no earlier provenance artifact was changed, and no source ambiguity was silently resolved.
