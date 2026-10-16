# Turnover must account for inherited reserve

5 October 2026. AI-assisted formal delta to [Typed renewal](TYPED-RENEWAL-FORMALIZATION.md). The earlier source and note remain unchanged. This result is needed when an organization enters with free reserve \(m\) and its successor finishes with a possibly different reserve \(m'\).

The separate [ReserveTurnover.lean](../../../../experiments/shared-renewal-capability/formal/ReserveTurnover.lean) checks the following theorem for the same concrete two-type reaction vocabulary. For any enabled typed trace from \(x\) to \(y\), assume total fabricators \(A_0+A_1\) and total gates \(G_0+G_1+GF_0+GF_1+YG_0+YG_1\) are restored. If at least \(n\) wears occur in each of the four roles \(A,G,C,Y\), then

\[
\boxed{K_{\rm capture}\ge 6n+W(y)-W(x).}
\tag{1}
\]

There is no assumption that the work ledger \(W\) returns to its initial value. The proof uses the frozen typed-to-ledger projection and the exact accounting identity

\[
K_{\rm capture}
=W(y)-W(x)+K_{\rm leak}+2n_A+2n_G+n_C+n_Y.
\tag{2}
\]

Restoring fabricators and gates equates their birth counts with their wear counts. Leakage is nonnegative. Equation (1) follows without any assumption about stochastic rates or success probabilities.

The file also defines every mixed-type organization

\[
P_{ij}(m):\quad A_i=CF=YG_j=1,\ F=m,
\]

with all other species absent. It verifies nonnegativity for \(m\ge0\), total fabricators and gates equal to one, and

\[
W(P_{ij}(m))=5+m.
\]

Consequently, any such trace between organizations with possibly changed types and reserve satisfies

\[
\boxed{K_{\rm capture}\ge6n+m'-m.}
\tag{3}
\]

For one wear in every role, this becomes \(K_{\rm capture}\ge6+m'-m\). Reserve restoration \(m'=m\) recovers the six-capture bound. Increasing reserve makes the lower bound stronger; spending inherited reserve weakens it. The weaker lower bound does not establish that a path attaining it exists. It prevents an assay from counting consumed inherited reserve as if it had been renewed during that assay.

These remain role-count statements. They neither encode original-carrier identity nor assert that a positive typed succession path exists. A separate tagged model must supply the original-wear hypotheses. No entry probability, return probability, kinetic advantage, or unlimited renewable supply is inferred. The ledger continues to count declared packets and active material, rather than calibrated thermodynamic free energy.

Lean 4.29.1 compiled the new source successfully. The [execution record](../../../../experiments/shared-renewal-capability/formal/reserve-lean-verification.json) preserves source, compiler, dependency and output hashes; [compiler output](../../../../experiments/shared-renewal-capability/formal/reserve-lean-output.txt) records only the standard Lean axioms used by these proofs. There are no proof placeholders, custom axiom declarations, or native decision shortcuts. New source SHA-256: `c0e6ba1c9f3adb1980121e2e0e2f55358256acdae356921638bffd4d8d212b55`.

The [reproduction script](../../../../experiments/shared-renewal-capability/formal/reserve-check.py) checks the frozen dependency hashes, builds them in a temporary directory, and writes only `reserve-*` execution records. Run `PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/formal/reserve-check.py` from the repository root with the pinned toolchain installed. The imported `TypedRenewal.lean` retains SHA-256 `73d0fea4f9fbf2a51560b850d608d2cc83a6ac8db80a8b7b2981f5f76a5a193c`; its earlier note retains SHA-256 `edb466f965a017142f56b0b9673be5cc53fe3794e825b280f165954b7cc01378`.
