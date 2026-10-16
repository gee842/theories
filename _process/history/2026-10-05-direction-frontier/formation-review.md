# Independent review of paid response formation

5 October 2026. Reviewed:

- `/Users/ren/Documents/Codex/2026-10-05/fo/work/direction-frontier/verify_math.py`
- `/Users/ren/Documents/Codex/2026-10-05/fo/work/direction-frontier/EXPLORATION.md`
- `/Users/ren/Documents/Codex/2026-10-05/fo/work/direction-frontier/math-note.md`, including the newly completed proofs available during this review.

No canonical files were changed. This is a second mathematical and conceptual review, not an external peer review or empirical validation.

## Verdict

**Accepted. No substantive error found in the construction, threshold, exact resource identity, stationary composition proof, small-exploration limit, or the exploration's account of their force.**

The model supplies positive examples and open-region failures under the same resource law. It demonstrates paid construction of an initially absent effective response within a supplied repertoire. It does not explain arbitrary invention, why the exploration allocation exists, formation of direct moral valuation, or universal selection for inclusion. The text states those distinctions accurately.

## 1. Re-derived selection threshold

Let `C=B+K>0`, `b=min(d,e)`,

\[
S_0=A-\lambda b>0,
\qquad S_1=A-c-\lambda a-\lambda(1-q)b>0.
\]

For faithful construction, `W0=S0/B`, `W1=S1/C`. Directly,

\[
BC(W_1-W_0)
=B S_1-C S_0
=\lambda b(Bq+K)-B(c+\lambda a)-KA.
\]

Thus the strict advantage condition and equality boundary in the manuscript are exact. The assumptions `B>0`, `K≥0` and positive retained resources justify cross-multiplication and subsequent positive-matrix arguments.

Useful boundary checks agree with interpretation:

- If `K=c=a=0`, no response disadvantage is artificially charged; a positive repair benefit gives an advantage when there is returned loss.
- If `q=0`, response cannot have a positive advantage under positive S0 and nonnegative extra costs. The apparently positive `lambda b K` term cannot overturn `K A` while `A>lambda b`.
- If there are no harmful encounters, a costly channel cannot gain an advantage from this supplied mechanism.
- Increasing d after d≥e changes no resource flow, hence no selection comparison. The bypass obstruction is exact.

The example gives `W1=37/22` and threshold `b>70/11`. At e=2 the ordinary factor is 19/10; at e=10 it is 3/2. Both examples have both faithful-reproduction factors above one. The alternative outcomes are therefore not created by comparing two extinct populations.

## 2. Construction matrix and a complete one-generation ledger

Independently reconstruct the matrix by allocating each parent's retained resources, instead of starting from the supplied matrix. A parent places `(1-mu)` into its own recipe, `mu alpha` into recipe 1, and `mu(1-alpha)` into recipe 0. Divide the resulting two allocations by their actual unit costs B and C. This gives exactly

\[
M=\begin{pmatrix}
(1-\mu\alpha)S_0/B & \mu(1-\alpha)S_1/B\\
\mu\alpha S_0/C & [1-\mu(1-\alpha)]S_1/C
\end{pmatrix}.
\]

Costly mutants buy fewer offspring; resource fractions have not been confused with head-count mutation probabilities. The column-weighted identity is

\[
(B,C)Mn=S_0n_0+S_1n_1.
\]

The stronger full-input ledger also checks:

\[
A(n_0+n_1)
=Bn'_0+Cn'_1
+cn_1+\lambda an_1
+\lambda b[n_0+(1-q)n_1].
\]

The terms on the right are successor construction, type-1 operating cost, paid attempted repairs, and private fallback cost. No resource is created by switching recipes. Common costs have already been debited in defining A; the recurring source of A is explicitly supplied.

A helpful algebraic view is to use capital coordinates `z=diag(B,C)n`. The similar matrix is

\[
\widetilde M=
\begin{pmatrix}
(1-\mu\alpha)W_0 & \mu(1-\alpha)W_1\\
\mu\alpha W_0 & [1-\mu(1-\alpha)]W_1
\end{pmatrix}.
\]

This is an ordinary positive reproduction-and-redistribution map for capital. Returning to head counts is what produces the construction-cost adjustment in the population ratio. This confirms that the model is using an established mathematical structure with a transparent resource interpretation, not asserting a new selection principle.

## 3. Positive formation and convergence

With `S0,S1>0`, `0<mu≤1`, `0<alpha<1`, every matrix entry is strictly positive. Starting from nonzero population of either type gives both positive types after one census. In particular

\[
n'_1=\mu\alpha S_0n_0/C>0
\]

when type 1 starts absent and `n0>0`. This is deterministic positive mass; the text correctly does not claim a guaranteed successful first trial for finite indivisible populations.

Let `r=n1/n0`. Then

\[
f(r)={M_{10}+M_{11}r\over M_{00}+M_{01}r}.
\]

The fixed equation has negative product of roots and one positive root. Independent expansion gives

\[
\det M=(1-\mu)W_0W_1\ge0,
\quad
f'(r)={\det M\over(M_{00}+M_{01}r)^2}\ge0.
\]

Furthermore, `f(r)-r` has the sign of a downward quadratic with its unique nonnegative zero r*. It is positive below r* and negative above. Monotonicity of f prevents crossing, so the iterates converge monotonically to r*. At mu=1 the map is constant and convergence takes one step. Initial pure type 1 is covered because positivity yields a finite ratio after one census. The proof is complete.

## 4. Small-exploration limit and the equality case

As mu→0 with every other parameter fixed, the diagonal difference tends to `W0-W1` and the off-diagonal entries are order mu. For `W0>W1`,

\[
r_*\sim {\mu\alpha B W_0\over C(W_0-W_1)}\longrightarrow0.
\]

For `W1>W0`,

\[
r_*\sim {B(W_1-W_0)\over\mu(1-\alpha)C W_1}\longrightarrow\infty.
\]

These expansions agree with the manuscript's exact root argument and establish the limiting shares. They concern the stationary composition for each positive mu. They do not license exchanging the long-time limit with mu=0, nor do they establish convergence for any chosen time-varying exploration schedule.

At `W0=W1`, substitution yields

\[
r_*={\alpha B\over(1-\alpha)C}
\]

for every positive mu. The responsive head-count share is therefore not generally alpha when K>0, because alpha is a capital allocation. The text handles this correctly.

The model does not imply universally increasing protection share. A start above the stationary share moves downward. At a disadvantage, small exploration creates only small supported minority mass. At mu=1, allocation fixes the capital composition even if the two reproduction factors differ. These are natural consequences of the supplied rule, not proof defects.

## 5. Absolute continuation and protected consequences

With `E=Bn0+Cn1`,

\[
E'=BW_0n_0+CW_1n_1
\]

implies `min(W0,W1)E≤E'≤max(W0,W1)E`. Both factors below one imply geometric extinction of deterministic mass; both above one imply geometric growth of capital under the supplied recurring source. A factor straddling one requires the actual dominant eigenvalue, rather than a conclusion from relative composition alone.

In particular, capital growth presumes an external A allocation for every parent at every generation. As population grows the aggregate source demand grows too. The text expressly calls this an open resource regime; it makes no claim that a fixed finite reservoir funds it. A future ecological extension would need a new resource equation and would generally change these conclusions.

Under matched exposure per parent, harm per normalized interaction is `lambda H(1-qx)`. Increased x reduces this specified harm when `lambda Hq>0`; increased population can nevertheless increase total harm. The manuscript states this distinction and does not call one response trait an exhaustive measure of wisdom.

## 6. Paid variation and the conceptual claim

The extra construction cost K is paid for every responsive successor, and the trial fractions use resources unavailable for faithful reproduction. This is a real opportunity cost. The model therefore improves on introducing a magically free mutant.

What remains supplied is equally important: a common constructor, both available recipes, an effective warning-to-action route, successful-repair fraction, the exploration fraction and allocation, and the continuing resource source. These are legitimate premises for a bounded mechanism. Calling this “construction within a supplied repertoire” is accurate. Calling it invention of the repertoire, endogenous evolution of the exploration rule, direct moral motivation, or recognition of novel powerless recipients would not be accurate.

EXPLORATION.md preserves that distinction. It also correctly identifies the next bridge as formation and transfer of concern, not merely better prediction or stronger private feedback. The new model explains one instrumental route for paid protective response to form and spread; the v parameter in the separate action example still exposes rather than solves evaluative inclusion.

## 7. Independent verification

A separate reviewer script was created:

`/Users/ren/Documents/Codex/2026-10-05/fo/work/direction-frontier/formation-review-check.py`.

It imports no author model and reconstructs the matrix from per-parent resource-allocation events. Its results are saved to `formation-review-checks.json`:

- 5,184 exact rational reconstructions verify the threshold identity, determinant, positivity, and complete one-generation resource accounting.
- 765 equal-fitness cases verify the exact capital-adjusted stationary ratio, including unequal alpha and unequal construction costs.
- 36 independent eigenvector checks cover small exploration from 10^-2 to 10^-6 in favorable, unfavorable, equal-fitness, and absolutely declining regimes.

All checks passed. The general claims rest on the proofs, not these finite checks. No additional substantive correction is requested.
