# Retained evidence can change the error law, under a retained valid model

5 October 2026. Conditional construction using established sequential testing, concentration and elementary probability. This study addresses the [fixed-batch reopening error](../../gap-resolution/formation-coupled/REOPENING-RESULTS.md); it does not supply an enduring observation/authority institution. All evidence and operating assumptions below matter.

## 1. The likelihood model and what a declaration means

Let \(\mathcal H=\{X_1,1-X_1,X_2,1-X_2\}\), with one fixed true expression \(h_*\). Each inquiry draws fresh independent fair binary attributes, randomizes action independently, and observes physical harm

\[
H_i=a_i\oplus h_*(X_i)\oplus\xi_i,
\quad \xi_i\overset{\mathrm{iid}}\sim\mathrm{Bernoulli}(\nu),
\quad 0<\nu<1/2.
\]

Write \(Y_i=H_i\oplus a_i\) and \(E_h(n)=\sum_{i=1}^n\mathbf1\{h(X_i)\ne Y_i\}\). Up to common factors from randomized actions and attributes,

\[
L_h(n)=\nu^{E_h(n)}(1-\nu)^{n-E_h(n)}.
\tag{1}
\]

Two labeled mismatch counts and \(n\) suffice to reconstruct all four likelihoods. This is sufficient compression for this supplied hypothesis family, not for arbitrary future questions. A declaration identifies an expression within that family. It does not certify the family's completeness, the noise rate, stationarity, legitimate values, or safe inquiry.

## 2. A time-uniform certificate that does not restart its error budget

For a declared lifetime error allowance \(\delta\in(0,1)\), announce \(h\) only when

\[
\boxed{L_h(n)/L_k(n)\ge 3/\delta\quad\text{for every }k\ne h.}
\tag{2}
\]

Otherwise retain the previous declaration, or remain undeclared if none exists. The rule may be inspected at arbitrary data-dependent times; our finite comparison inspects every five records.

**Conditional assurance.** If the true fixed expression is among the four hypotheses and all conditional observation laws remain those specified above, then

\[
\Pr_{h_*}\{\text{ever announce any }h\ne h_*\}\le\delta.
\tag{3}
\]

For each wrong \(h\), \(M_h(n)=L_h(n)/L_{h_*}(n)\) is a nonnegative likelihood-ratio martingale under \(h_*\), starting at1. Ville's inequality gives \(\Pr(\sup_nM_h(n)\ge3/\delta)\le\delta/3\). A wrong announcement requires at least one of the three wrong martingales to cross that threshold. The union bound proves (3). No independent error assumption across looks is used. This is an application of established sequential testing; see the likelihood-ratio and nonnegative-martingale discussion in [Howard et al., *Time-uniform, nonparametric, nonasymptotic confidence sequences*](https://arxiv.org/html/1810.08240v9).

For \(\nu=.1\), ratios are powers of9. With \(\delta=.05\), threshold60 is equivalent to requiring each alternative's error count exceed the nominee's by at least2. Crossing then requires ratio at least81, so the same proof sharpens the bound to \(3/81\approx.03704\). The finite computation need not attain that conservative bound.

Under continued stationary evidence, each wrong expression has a strictly higher expected mismatch rate than the true one. The strong law therefore makes every \(E_h(n)-E_{h_*}(n)\) diverge to positive infinity. Eventually the true expression meets (2) permanently, almost surely. A false early declaration may occur within the allowed error probability, but cannot remain permanently wrong under continued valid evidence. If inquiry stops prematurely, eventual correction is not supplied by this argument.

Correctness **between** announcements follows from (3) only because the same expression stays physically true. An unannounced environmental change can invalidate a formerly correct retained declaration without a new announcement. Further announcements can also be false when obsolete evidence is pooled; the martingale premise then fails. These are different events and the finite study records both.

## 3. Summable errors are a different possibility from constant replacement risk

Consider the simpler rule that always replaces the declaration by a minimum cumulative mismatch expression. For a wrong expression, the per-case loss difference

\[
D_i=\mathbf1\{h(X_i)\ne Y_i\}-\mathbf1\{h_*(X_i)\ne Y_i\}
\]

lies in[-1,1]. Its expectation is at least \(\Delta=1/2-\nu>0\): wrong-attribute expressions have this gap, while the true attribute's reversal has gap \(1-2\nu\). Hoeffding's bounded-sum inequality and a union bound give

\[
\Pr\{\widehat h_n\ne h_*\}
\le\min\{1,3\exp(-n\Delta^2/2)\}.
\tag{4}
\]

At the cumulative batch endpoints \(n_t=5t\), these bounds have a finite sum. The first Borel–Cantelli lemma therefore implies that only finitely many wrong replacements occur almost surely, without requiring independence between replacement errors. That statement does **not** bound the chance of making at least one early error by a chosen small \(\delta\).

A conservative chosen-risk alternative is to defer declarations until batch \(t_0\), where

\[
\frac{3e^{-ct_0}}{1-e^{-c}}\le\delta,
\qquad c=5\Delta^2/2.
\tag{5}
\]

Then the union bound covers every subsequent cumulative replacement. At \(\nu=.1,\delta=.05\), (5) first holds at14 batches, or70 inquiry cases. This is a sufficient bound, not an optimal sample requirement. The likelihood certificate exploits the fully specified finite family and is substantially less conservative in this example.

In contrast, discarding evidence and replacing from a fresh fixed five-case batch leaves correct-nomination probability \(p_5=.8511075\) at every look. In the stationary independent-batch experiment, the probability of at least one wrong replacement inT looks is \(1-p_5^T\), tending to1. Wrong replacements recur infinitely often almost surely. The repeated fixed-size error mechanism is therefore avoidable **within the retained stationary model**, not an unavoidable law of all revision.

If records must be reset, a different valid construction can allocate a summable allowance \(\delta_j\) to reset episodej, for example \(\delta/[j(j+1)]\), and use threshold \(3/\delta_j\) within that episode. This requires a valid fixed hypothesis during each episode and preserved error-budget bookkeeping. It is not permission to reuse \(\delta\) afresh at every reset. No such reset or change detector is implemented in this study.

## 4. Work, memory, and initial safety remain obligations

All finite arms receive exactly60 inquiry cases and60 record-work slots:120 effort units, expected30 physical inquiry harms and30 action-1 uses. Cumulative evidence gets no additional observations. It does require retained counters: at60 cases the pair uses12 binary digits rather than6 for two counts capped at5, excluding labels, clock, circuitry, declaration and event bookkeeping. These are representation sizes, not a measured full energy/time price. Arithmetic and reliable retention require an available operating substrate; neither is shown to reproduce itself here.

Continued inquiry entails an unbounded total case/record workload, and cumulative counters grow as \(O(\log n)\) bits. An institution that cannot maintain this workload or the necessary sufficient statistic cannot invoke the infinite-data conclusion. Conversely, stopping after a valid certificate preserves its error bound **only while the physical model remains unchanged**; it supplies no evidence about future changes.

**No-safe-exploration obstruction in the original operating state.** Before a conditional frame is installed, an action ratep independent of the current context produces two opposite target-class harms

\[
h_0=\nu+(1-2\nu)p,
\qquad h_1=\nu+(1-2\nu)(1-p),
\qquad h_0+h_1=1.
\tag{6}
\]

Thus no available blind response satisfies both group ceilings \(r<1/2\). Randomized inquiry has \(h_x=1/2\) for every context and also violates those ceilings if they cover experimental cases. Even if conditional proposals were immediately expressible, two initially indistinguishable worlds with opposite correct actions give harms summing to1 for any shared response at a fixed context; no information-compatible response meets both worlds' strict ceilings uniformly.

The original action repertoire contains no harmless pause, refusal or outside rescue that removes this obstruction. Adding one would require specifying its own consequences and obligations. Withholding a statistical declaration does not itself withhold the physical case or provide a safe action. Epistemic confidence, ordinary-service capability, whole-behavior safety and legitimate permission to investigate therefore remain distinct.

## 5. Scope of the constructive result

Retained sufficient evidence can replace a constant error hazard by summable error probabilities, and an established sequential certificate can control the chance of ever making a false declaration under stated assumptions. Neither requires a scalar social objective. The price is a valid, sufficiently identifiable observation model plus maintained evidence and operating capacity.

The changed-world comparison is a robustness test that deliberately violates the fixed-hypothesis premise; it is not a counterexample to (3). A future change-aware extension could spend explicit work on a fresh predictive check, suspend or qualify the current declaration after a statistically controlled alarm, and restart learning under an allocated error budget. Such a design would need to report detection delay, false alarms, extra investigation harms, and behavior during uncertainty. It is unrun and unvalidated here. Detecting a shift would still not decide which commitments should change, nor authorize harmful experimentation.
