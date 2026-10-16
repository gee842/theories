# Checked typed reactions and their resource ledger

5 October 2026. AI-assisted mathematical formalization, continuing the [paid-access protocol](../../../../experiments/shared-renewal-capability/paid-access/PROTOCOL.md) and the [first Lean ledger](../../../../experiments/shared-renewal-capability/formal/README.md). This is a semantic bridge for the stated reaction model, not an empirical validation.

The new [TypedRenewal.lean](../../../../experiments/shared-renewal-capability/formal/TypedRenewal.lean) proves that every enabled trace of the concrete two-type reaction system projects to an enabled trace of the frozen resource ledger. The projection is derived from explicit inputs and outputs; it is not an assumed simulation hypothesis. The old construction obstruction and the six-capture turnover bound now apply to these typed traces through that proved map.

## 1. Concrete state and reaction vocabulary

The state has fourteen integer coordinates,

\[
x=(R,C,CF,Y,D,F,A_0,A_1,G_0,G_1,GF_0,GF_1,YG_0,YG_1).
\]

`Nonnegative x` requires every coordinate to be nonnegative. Each event has a concrete input vector and output vector. `Enabled e x` requires nonnegative state and all input quantities, including catalysts, to be present. The step is ordinary coordinatewise integer subtraction and addition. Enabled steps and traces preserve nonnegativity.

There are 42 concrete event instances: twelve unindexed events and fifteen families indexed by the two architecture types. The vocabulary includes free-packet fabrication and copying, both kinds of binding and dissociation, each constituent wear channel, source capture, free and bound leakage, both free-packet recycling channels, and the three declared paid-access families:

\[
D+CF\to R+C,\quad
R+CF\to A_i+C,\quad
A_i+R+CF\to A_i+G_i+C.
\]

The bound-reproduction constructor is exclusively

\[
R+YG_1\to Y+YG_1.
\]

There is no type-0 counterpart. There is also no bound-packet copying, no CF-catalyzed free-packet recycling, no \(CF\to C+F\) release, and no reverse-chemistry extension. This is exactly the forward reaction vocabulary declared for the paid-access experiment. The all-positive unit coefficients motivate this enabled vocabulary, but rates themselves are not formalized in this file.

## 2. The proved projection

Let \(\pi\) retain the six untyped coordinates and sum each pair of architecture coordinates:

\[
A=A_0+A_1,\quad G=G_0+G_1,\quad
GF=GF_0+GF_1,\quad YG=YG_0+YG_1.
\]

Let \(\phi\) forget the type of an event. For every concrete event and state the kernel checks

\[
\pi(\operatorname{in}(e))=\operatorname{in}(\phi(e)),\qquad
\pi(\operatorname{out}(e))=\operatorname{out}(\phi(e)),
\]

\[
\boxed{\pi(\operatorname{step}(e,x))
=\operatorname{step}(\phi(e),\pi(x)).}
\tag{1}
\]

It also checks

\[
\operatorname{Enabled}(e,x)
\Rightarrow\operatorname{Enabled}(\phi(e),\pi(x)).
\tag{2}
\]

Induction then transfers every finite enabled typed trace, with its mapped event list, to an enabled ledger trace. An optional allowed-event predicate transfers whenever its mapped events satisfy the ledger predicate. In particular, the predicate excluding the three access families maps exactly to the frozen bare-storage predicate. This predicate condition does not assume equations (1) or (2); those are separately proved from the reaction definitions.

The projection is deliberately one-way. At \(R=YG_0=1\), the pooled bound-reproduction event is enabled while the concrete type-1 event is disabled. `pooled_enabled_does_not_lift` checks this example. Thus neither pooled enabledness nor a pooled positive path establishes typed reachability. No kinetic lumping or equality of stochastic laws is asserted.

## 3. Consequences now connected to the typed system

The transferred ledger is

\[
N=R+C+CF+Y+D+A+G+GF+2YG,
\qquad W=N-D+F+CF+GF.
\]

Material \(N\) is preserved on typed traces. For any pair \(i,j\), consider the organization \(P_{ij}\) having \(A_i=CF=YG_j=1\), with all other quantities zero. Along any bare-storage typed trace from this state, neither type can subsequently enable free-packet fabricator formation, fabricator copying, or gate fabrication. This transfers the availability obstruction, rather than imposing a special prohibition on those reactions.

For any typed trace restoring \(W\), total \(A\), and total gates \(G+GF+YG\), let \(n_A,n_G,n_C,n_Y\) count the four role-wear families. If each is at least \(n\), the checked theorem gives

\[
\boxed{K_{\rm capture}\ge 6n.}
\tag{3}
\]

For one such turnover, a further new theorem checks the exact-loss consequence. If all four wear counts are at least one and exactly six captures occur, then

\[
K_{\rm leak}=0,\qquad
K_{A\rm birth}=K_{G\rm birth}=1,\qquad
n_A=n_G=n_C=n_Y=1.
\tag{4}
\]

The proof uses the checked work and carrier-balance identities, which yield

\[
K_{\rm capture}=K_{\rm leak}+2n_A+2n_G+n_C+n_Y
\]

when those endpoint quantities are restored. At the six-capture minimum, leakage, any extra fabricator or gate birth, or any extra wear is incompatible with the hypotheses. This formalizes the arithmetic core of the experiment's exact-budget rejection argument. It does not prove all of its implementation-level pruning rules.

The wear hypotheses in (3) and (4) count roles. This state has no original-molecule labels. The assertion that all four *original* carriers wore, its projection to these wear-count hypotheses, and the tagged enumerator's bookkeeping remain separate obligations. A count return alone is not proof of original-carrier succession. These are packet-ledger bounds, not calibrated free-energy requirements.

## 4. Verification and inspected code correspondence

[The execution record](../../../../experiments/shared-renewal-capability/formal/typed-lean-verification.json) records successful compilation with Lean 4.29.1, commit `f72c35b3f637c8c6571d353742168ab66cc22c00`. [Compiler output](../../../../experiments/shared-renewal-capability/formal/typed-lean-output.txt) prints the axiom dependencies of the principal theorems. No `sorry`, custom axiom declaration, or `native_decide` occurs in the typed source, and no printed theorem depends on `sorryAx`. The reported dependencies are only Lean's standard `propext`, `Classical.choice`, and `Quot.sound`, where used; the input/output projection equalities need no axioms.

Frozen SHA-256 values:

| Item | SHA-256 |
|---|---|
| `TypedRenewal.lean` | `73d0fea4f9fbf2a51560b850d608d2cc83a6ac8db80a8b7b2981f5f76a5a193c` |
| Imported `RenewalLedger.lean` | `1c78c6dae53bc9b7c15ae3a24a63d83558d585fa07a4c402c25c571229514e74` |
| Actual Lean compiler binary | `b48bc5ab229bd8b320a224b87e20fc428dba6fa8a1c054bd4fa6def846e19997` |
| Typed compiler output | `527214af93e6ddcc3dd8e5262f4a22a4afe0038eab09393408e1b4b755862769` |

The [reproduction script](../../../../experiments/shared-renewal-capability/formal/typed-check.py) builds the frozen dependency in a temporary directory, compiles the typed source, saves its output and hashes, and removes the temporary imported object. It writes only new `typed-*` records, leaving the old source and execution records unchanged. To reproduce, run `PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/formal/typed-check.py` from the repository root with the pinned toolchain installed; this intentionally replaces the typed execution records with the new run.

An independent AI critic read the complete typed source and found no substantive mismatch in the 42-event vocabulary or the scope of its projection and budget claims. That review did not independently compile the file; the linked execution record supplies the compiler evidence.

I also inspected `channels()` in the new [unpruned entrance producer](../../../../experiments/shared-renewal-capability/full-entry/compute.py), at source SHA-256 `e7ab065ffa835bc9eb5aa2164e205c8efb5b3b06a0bdae7a79f3845018b2cb7e`. All 42 inputs and outputs matched this typed table, including preserved catalysts, type-1-only bound reproduction, the three access families and the absent optional channels. This is a read-only source comparison, not a machine-checked Python-to-Lean translation or a numerical rerun.

## 5. Remaining formal interfaces

The new result closes the typed-stoichiometry-to-ledger interface. It does not yet check original-carrier tags, any concrete positive typed formation/turnover path, mass-action propensities, CTMC construction, stopping and overflow semantics, equality with either Python enumerator, uniformization arithmetic, or the probability certificate. It also does not validate a molecular implementation, the maintained source, feasible rate scales, or a universal direction of generativity. The next proof interface is to lift a tagged event law to this typed law and establish the exact enumerator correspondence; the ledger bound can then be reused without another informal projection assumption.
