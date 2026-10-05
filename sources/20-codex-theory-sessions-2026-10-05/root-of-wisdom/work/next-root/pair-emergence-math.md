# Relative parts within a connected exchange process

New constructed example for the next-root branch, 5 October 2026. This is an extension of this thread's diffusion derivation, not an inherited theorem claimed on behalf of another session. All current theories and source files are preserved.

## Mechanism and exact decomposition

Four sites carry nonnegative quantities \(x_i\). Sites 1 and 2 exchange at rate \(k\), as do sites 3 and 4. Each of the four between-pair edges has rate \(\varepsilon/2\). Let \(k,\varepsilon\ge0\), measured in inverse time. Then

\[
\dot x=Gx,\qquad
G=\begin{pmatrix}
-k-\varepsilon&k&\varepsilon/2&\varepsilon/2\\
k&-k-\varepsilon&\varepsilon/2&\varepsilon/2\\
\varepsilon/2&\varepsilon/2&-k-\varepsilon&k\\
\varepsilon/2&\varepsilon/2&k&-k-\varepsilon
\end{pmatrix}.
\tag{P1}
\]

Nonnegative off-diagonal entries and zero column sums give positivity and conservation of total amount. For \(\varepsilon>0\) the graph is connected, including when \(k=0\). The four mutually orthogonal eigenvectors are

\[
v_0=(1,1,1,1),\quad v_c=(1,1,-1,-1),\quad
v_A=(1,-1,0,0),\quad v_B=(0,0,1,-1).
\]

Their respective decay rates are

\[
\boxed{0,\quad2\varepsilon,\quad2k+\varepsilon,\quad2k+\varepsilon.}
\tag{P2}
\]

This is a complete exact solution because these vectors form a basis. Writing

\[
g=\tfrac14\sum_i x_i(0),\quad
c=\tfrac14[x_1(0)+x_2(0)-x_3(0)-x_4(0)],
\]
\[
u=\tfrac12[x_1(0)-x_2(0)],\quad
v=\tfrac12[x_3(0)-x_4(0)],
\]

the solution is

\[
x(t)=g v_0+c e^{-2\varepsilon t}v_c
+u e^{-(2k+\varepsilon)t}v_A
+v e^{-(2k+\varepsilon)t}v_B.
\tag{P3}
\]

Define pair means \(a=(x_1+x_2)/2\), \(b=(x_3+x_4)/2\). Then

\[
\dot a=\varepsilon(b-a),\quad
\dot b=\varepsilon(a-b),\qquad
a(t)-b(t)=[a(0)-b(0)]e^{-2\varepsilon t}.
\tag{P4}
\]

In contrast,

\[
x_1(t)-x_2(t)=[x_1(0)-x_2(0)]e^{-(2k+\varepsilon)t},
\]

and likewise for sites 3 and 4. The pair means are an exact closed *joint* description, even though either pair alone remains affected by the other whenever \(\varepsilon>0\). The coarse generator is \(\begin{pmatrix}-\varepsilon&\varepsilon\\\varepsilon&-\varepsilon\end{pmatrix}\); the averaging map \(Q\) satisfies \(QG=\bar GQ\).

## Quantified scale on which two coherent parts are distinguishable

Fix a relative tolerance \(0<\delta<1\). Require every within-pair contrast to have decreased to at most \(\delta\) of its initial magnitude, while the between-pair contrast retains at least \(1-\delta\) of its initial magnitude. For \(k,\varepsilon>0\), exactly the times in

\[
\boxed{
\frac{\log(1/\delta)}{2k+\varepsilon}
\le t\le
\frac{-\log(1-\delta)}{2\varepsilon}
}
\tag{P5}
\]

satisfy both multiplicative requirements. If initial within-pair contrast is zero, its requirement is automatically satisfied; P5 is a uniform window for arbitrary within-pair preparations. Initial between-pair contrast must be nonzero to observe an actual distinction in an unforced trajectory. An allowed preparation can instead excite the corresponding mode and measure its decay. No spontaneous creation of contrast is claimed.

For \(\varepsilon>0\), the interval is nonempty exactly when

\[
\boxed{
\frac{k}{\varepsilon}\ge
\frac{\log(1/\delta)}{-\log(1-\delta)}-\frac12.
}
\tag{P6}
\]

For example, at \(\delta=0.05\) the required ratio is approximately 57.904. The choice \(k=100\), \(\varepsilon=1\) supplies a window from about 0.01490 to 0.02565 time units. Within that window the pairs are internally coherent to the stated relative standard while at least 95% of the initial pair contrast remains. These numerical decimals illustrate P5–P6; the inequalities themselves are analytic.

A corresponding absolute approximation is immediate. Reconstruct \(\widehat x=(a,a,b,b)\). Then

\[
\|x(t)-\widehat x(t)\|_\infty
=\tfrac12 e^{-(2k+\varepsilon)t}
\max\{|x_1(0)-x_2(0)|,|x_3(0)-x_4(0)|\}.
\tag{P7}
\]

The coarse response P4 is exact for every preparation. P7 quantifies the error when reconstructing individual-site quantities from that coarse description.

## A conditional selection result, not only validation of a chosen partition

The generator can itself select the proposed pairs under a specified criterion. Hold fixed the microscopic site coordinates and choose the partition given by the signs of the **slowest decaying nonconstant mode**. If \(\varepsilon>0\) and \(k>\varepsilon/2\),

\[
0<2\varepsilon<2k+\varepsilon.
\]

The slowest nonconstant eigenvalue is therefore simple, with eigenspace spanned by \((1,1,-1,-1)\). Its positive and negative entries determine \(\{1,2\}\) and \(\{3,4\}\), uniquely up to exchanging the names of the two groups. In this precise sense the pair boundary is recovered from the dynamics rather than arbitrarily declared. For a useful finite-time approximation the stronger quantitative separation P6 may be needed; merely having a simple slow mode supplies no chosen error tolerance.

Both alternative balanced pairings also admit exact two-state closures: their contrast vectors \((1,-1,1,-1)\) and \((1,-1,-1,1)\) decay at \(2k+\varepsilon\). Thus exact coarse closure by itself does not select the physically slower partition. The explicit retention criterion does real work.

At \(k=\varepsilon/2\), all nonconstant modes have the same rate, and this criterion cannot select a partition. At \(0\le k<\varepsilon/2\), the slow eigenspace has dimension two, so a simple-eigenvector criterion again yields no unique pair boundary. The selected microscopic variables and the spectral criterion remain premises; this result is not uniqueness under arbitrary nonlinear redefinitions or a proof of a privileged cosmic decomposition.

## Limiting cases and what the example does not prove

- **\(\varepsilon=0,k>0\):** the pairs are disconnected. Each pair mean is conserved. Internal contrast decays, and there is no finite upper limit on the coherence window. This is exact dynamical independence between pairs in this model.
- **\(k=0,\varepsilon>0\):** the graph is a connected complete bipartite graph. Pair contrast decays at \(2\varepsilon\), faster than the proposed pairs' internal contrast at \(\varepsilon\). These pairs therefore do not have the desired timescale separation at small tolerances. Merely drawing a grouping does not create relative autonomy.
- **\(k=\varepsilon/2>0\):** all six edges have the same rate. All three nonconstant modes decay at \(2\varepsilon\). Every permutation of sites preserves the generator. No one of the three pair partitions is selected by this dynamics; all pair-mean closures remain exact but the slow/fast argument distinguishes none. For \(\delta<1/2\), no common coherence/contrast-retention window exists for arbitrary initial contrasts.
- **\(k=\varepsilon=0\):** every configuration is stationary. No relaxation creates a coherent approximation from an arbitrary initial state, although an already coherent preparation remains coherent.

With a large rate ratio, actual differences in couplings warrant a useful pair description for a stated task and time scale. This is stronger than assigning names to arbitrary subsets. It still does not derive the historical formation of the coupling matrix, the physical site decomposition, a unique ontology, or a unique preferred partition from symmetry alone. The matrix's preserved symmetries can exchange the two pairs and swap members within each pair. The proposition concerns relative coherence and retained distinguishability, not a claim that parts cease to be real or that a connected graph proves metaphysical monism.

## Verification

`check_pair_emergence.py` verified all algebraic claims over 49 nonnegative rational parameter pairs, including zero coupling, zero internal exchange, and the equal-edge degeneracy. It checked positivity, conservation, symmetry, all four eigenmodes, exact pair closure, contrast derivatives, connectedness, limiting identities, conditional selection of the unique slow mode, both alternative balanced-partition contrast vectors, and full-mode reconstruction on 81 rational states. The analytic basis calculation provides the all-state proof; the finite checks supplement it. `pair-emergence-checks.json` preserves every checked parameter case and separately labeled floating-point window examples.
