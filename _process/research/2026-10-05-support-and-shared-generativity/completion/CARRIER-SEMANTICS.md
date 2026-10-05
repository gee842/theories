# Original carriers, material reuse and the count law

5 October 2026. AI-assisted semantic specification and exact finite check for the unchanged 42-channel, two-type, N=4 CF paid-access law. This extends the [typed ledger bridge](TYPED-RENEWAL-FORMALIZATION.md) to explicit carrier bookkeeping. It does not rerun a probability calculation or establish a molecular implementation.

The main result is a checked one-step correspondence: **summing the labelled reaction assignments gives exactly the existing mass-action rate, channel by channel and projected destination by projected destination, for every material configuration and every nonnegative free reserve.** The original-carrier marks do not change the physical count law. They record a stricter path event than returning to the same counts.

## 1. What persists, and what is marked as gone

At an entry \(P_{ij}(m)\), name the four material slots \(0,1,2,3\). Initially they carry \(A_i,CF,G_j,Y\), with a directed bond from the G slot to the Y slot. Free reserve is \(F=m\). Each slot has a permanent bit \(b_s\), initially zero, meaning that its original carrier has worn. The state consists of the four current material forms, the G–Y bond relation, the four bits and the free-packet count.

These are analyst labels on the trajectory, not newly installed physical labels, free measurements, or inputs available to a controller. A physical experiment that reads original-carrier turnover would have to implement and pay for its own identification and readout. The present labels define the event whose probability a model may later calculate.

The eleven unbound slot forms are

\[
R,C,CF,Y,D,A_0,A_1,G_0,G_1,GF_0,GF_1.
\]

A \(YG_i\) complex occupies **two** slots: a gate of type \(i\) and a Y, joined by a bond. Those slots remain distinct while bound. A bound packet in CF or GF adds no material slot in this declared ledger. Fuel-packet identities are not part of the original-carrier assay.

The transition conventions are explicit:

| Reaction family | Carrier bookkeeping |
|---|---|
| Assembly, capture and CF leakage | The same slot changes \(R\to C\to CF\to C\). Capture and leakage do not count as C wear. |
| G binding/dissociation with F or Y | Preserve the gate slot; Y binding also preserves the particular Y slot and adds/removes their bond. |
| C-, CF-, A-, G- or GF-wear | Convert the worn slot to D and set its bit. CF/GF wear returns the corresponding free packet as in the count law. |
| Bound G wear | Mark only the G slot; release the same Y slot unchanged. |
| Bound Y wear | Mark only the Y slot; release the same gate slot unchanged. |
| Recycling | Convert the consumed D slot to R; never clear its original-wear bit. The catalyst remains in its existing slot. |
| Fabricator formation/copying and gate fabrication | Convert the consumed R slot to the new A or G. Copying/fabrication preserve the catalyst A slot. |
| Free or permitted bound Y reproduction | Convert the R slot to a new Y; preserve the parental Y slot or the entire bound complex. |

Every wear sets \(b_s\leftarrow b_s\lor1\). It never resets another bit. A carrier born from reused material can itself wear later; that event remains allowed and simply leaves its already-set bit set. The record therefore counts the **first loss of each original**, not a ban on subsequent loss. Type changes after original wear are allowed whenever the ordinary formation reactions enable them.

This carrier map is a declared refinement of the chemistry. Reaction stoichiometry alone does not uniquely determine microscopic identity through a reaction. The chosen convention preserves the named catalysts and converts the named consumed material. A physical original-carrier interpretation would require identifying those carrier mappings in an implementation; count-law agreement alone cannot establish them.

## 2. Exact projection of event rates

Let \(z\) be a labelled state and \(\pi z=x\) its fourteen-species count state. Count each unbound form in the corresponding species, each gate–Y bond once as \(YG_i\), and retain F. Each typed reaction channel \(c\) has a set of concrete choices \(A_c(z)\) of its material participants. Every such choice produces the declared stoichiometric change \(\nu_c\):

\[
\pi z_a'=\pi z+\nu_c\qquad(a\in A_c(z)).
\tag{1}
\]

At unit positive coefficients, a concrete choice has rate one, or rate F when the reaction consumes a free packet. The original reaction inputs never repeat the same species, and contain at most one F. Therefore the existing mass-action channel rate is an affine polynomial in F, and the desired identity is

\[
\boxed{\sum_{a\in A_c(z)}q_a(z)=q_c(\pi z).}
\tag{2}
\]

The [independent checker](../../../../experiments/shared-renewal-capability/full-successor/carrier_check.py) implements the labelled assignments separately from the count-law producer. It reads only that producer's `vector` and `channels` declarations, without executing its numerical imports, graph construction or propagation. It then compares exact integer coefficients of the constant and F terms. Equality of both coefficients verifies (2) for every nonnegative integer reserve, without imposing a fuel cap. For F-consuming assignments, their rate is zero at F=0, so a formally listed negative fuel increment cannot produce a negative physical fuel count.

The finite material domain is exhaustive:

\[
11^4+4\cdot3\cdot2\cdot11^2+3\cdot2^2\cdot2^2
=17\,593.
\]

The terms enumerate zero, one and two gate–Y complexes. The check covers states with all original carriers still present, partly worn states, all-worn states, multiple copies, absent lineages and depleted material configurations. It does not select only promising histories.

Several microscopic assignments can produce the same labelled successor. They must be **summed**, not deduplicated. For example, from two A0 slots and one R slot, either A0 can catalyze copying into that same R slot. The two assignments give the same labelled successor but total propensity \(2F\). The checker includes this case explicitly.

Because the bits do not enter any rate, (1)–(2) hold for all admissible wear masks. They give the one-step generator correspondence for the specified lift. Claims about a stopped numerical kernel still require checking its state enumeration, boundary treatment and propagation separately.

## 3. Why all four original losses imply the ledger wear hypotheses

Until its bit is set, an original slot remains in its original functional family. A and G additionally retain their original type until wear; C can be free or charged, and G/Y can bind and dissociate without losing identity. The checker verifies that every nonwear transition preserves this role/type signature for each active participant it does not wear.

Initially the four original roles are A,C,G,Y. When a bit first changes from zero to one, the affected slot therefore undergoes a wear of that original role. Each wear affects at most one slot. Hence any finite trace reaching all four bits set has

\[
n_A\ge1,\quad n_C\ge1,\quad n_G\ge1,\quad n_Y\ge1.
\tag{3}
\]

This is the semantic implication needed by the checked ledger bounds. It remains valid with repeated later wears, arbitrary legal material reuse and changed successor types. The checker verifies the bit algebra for all sixteen masks and the original-role invariant across every compatible skeleton/mask transition. Induction extends these one-step statements along a labelled trace.

The converse does not follow from role counts alone: a wear count does not identify which carrier wore. Nor does a return to organization counts prove (3). The original marks supply the missing history-dependent event.

The checker also follows a concrete permitted trace from \(P_{00}(0)\): original A0 wear, paid recycling, capture, A1 paid formation, capture. The reused material becomes A1, while its original-A bit stays set. Its later A1 wear remains an ordinary allowed event with that bit still set. This is a bookkeeping witness, not a probability or control claim.

Combining (3) with a return to any \(P_{i'j'}(m')\) supplies the hypotheses of [reserve-sensitive turnover](RESERVE-SENSITIVE-TURNOVER.md):

\[
K_{\rm capture}\ge6+m'-m.
\]

The combination is currently an inspected/exhaustively checked semantic argument plus the separate Lean ledger theorem. It is not yet one end-to-end Lean proof of the labelled process.

## 4. Quotienting material whose original identity is already gone

The successor computation's [model](../../../../experiments/shared-renewal-capability/full-successor/model.py) keeps all live original slot positions fixed and permutes only slots whose bits are already set. This merges physically equivalent bookkeeping states after those original identities no longer matter to the assay. It must permute bond endpoints along with the material forms. It must never move an intact original or clear a bit.

The independent checker constructs this quotient separately by enumerating the permutation orbit of the already-worn slots. For every original-role-compatible labelled state, it verifies the same canonical representative, the same projected counts, and the same aggregate edge coefficients for each triple

\[
(\text{named channel},\ \text{canonical labelled target},\ \Delta F).
\]

Thus the checked property is stronger than merely matching total exit rates or unlabelled counts: the implementation also preserves the particular remaining-original identities relevant to future turnover. Different dead-material permutations cannot change the checked future transition law. Canonicalization intentionally forgets those dead materials' original slot identities; the four raw conserved slots and their quotient should not be described as identical representations.

This check applies to the model's `events`, `canonical`, `valid` and `count` behavior. It does not run `graph_skeletons`, verify a stopping convention, or certify a truncation or numerical probability calculation. An availability test that ignores F is not by itself a zero-access test when free F is positive; any use of that helper must include the actual reserve condition.

## 5. Completed checks and limits

The [exact record](../../../../experiments/shared-renewal-capability/full-successor/carrier-check.json) reports:

| Check | Cases |
|---|---:|
| Material skeletons | 17,593 |
| Per-channel polynomial equalities | 738,906 |
| Concrete labelled reaction assignments | 162,425 |
| Original-role-compatible skeleton/mask states | 37,154 |
| Compatible mask transitions | 339,207 |
| Successor-model state comparisons | 37,154 |
| Successor-model edge-coefficient comparisons | 313,546 |

All assertions passed using integer arithmetic and symbolic affine coefficients. There is no statistical tolerance. The record preserves the checker, count-law source, typed Lean source and checked successor-model hashes. The count-law source hash is `e7ab065ffa835bc9eb5aa2164e205c8efb5b3b06a0bdae7a79f3845018b2cb7e`; the checked successor-model hash is `6575e93ca13317f31e2e58031293aca3afd591209f100ce925e024d1611d7449`.

Run `PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/full-successor/carrier_check.py` from the repository root to reproduce. This writes only the checker's result record and does not execute either numerical propagation. The check relies on Python's execution of the exhaustive program and the source declarations it reads; it is not a Lean proof or a verified Python-to-Lean compiler.

The result closes a concrete semantic issue: a full-original-successor event can be tracked without altering the prescribed reaction rates, resurrecting original identities, rejecting later wears, or losing bond constituents. Whether such events are likely, whether either architecture improves their joint kernel from all entry histories, and whether the carrier convention describes real molecules are separate questions.
