# Shared generative support and its transmission across two levels

7 October 2026. AI-authored supporting formal audit of Ren's proposed evolutionary connection: generation sustains further realization, while selection at a containing level may pressure its differentiated subsystems toward generativity. **Result: a checked positive mechanism, an exact coupling threshold and a matched negative case. This is one generation, not a theorem of long-run or universal convergence.**

The contribution to the universal normative investigation is precise: it tests whether selection for a collectively productive consequence automatically selects the structure producing that consequence. Ethical quality, the authority of selection's outcomes and practical reasons for all intelligence remain separate questions. No moral predicate occurs in the Lean source.

## Existing work reused and preserved

[GENERATIVE-SELECTION §1](../../../../theories/becoming/history/GENERATIVE-SELECTION.md#1-shared-dependence-and-the-selection-of-its-maintenance) already distinguishes support's physical importance from the relative retention of its producers. Its additive-common-return cancellation and its conditional constructive mechanisms remain credited. This new multiplier law is different: neither the old neutrality formula nor its stronger convergence hypotheses silently transfers here.

[Consequence-retention selection](../../../history/2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-RETENTION-SELECTION.md) already gives a more detailed material route through formed access, repair and competing copying, including wear and transfer to an alternative structure. Its analytical stochastic results retain their original validation scope; this new small Lean interface is not a retrospective migration of that study.

[LIANGZHI-EVOLUTION](../../../../theories/becoming/chapters/LIANGZHI-EVOLUTION.md) credits checked distinctions between selected templates, transmitted response structures and developmental reconstruction. The current model assumes faithful response transmission and therefore does not repeat the earlier template-versus-offspring result as a discovery. Allowing transmission change would require that earlier interface, rather than treating all descendant opportunities as faithful copies.

The [existing multilevel memo](../../../../experiments/integrated-correction/systems-dynamics/review/MULTILEVEL.md) already explains that cross-level coupling can change the consequences of locally favorable dynamics; a common objective and a fixed universal hierarchy are not established. The present study checks a narrower, exact demographic comparison. None of these older packages was rebuilt or newly certified here.

## Representation and supplied law

The [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) applies. Two collectives describe differentiated sites of support formation and reproduction within one represented process. They are not independently constituted substances joined by an external selector. Their actual formation and the persistence of their boundaries are outside this one-generation interface.

Within a collective, let `a` be the number carrying a support-producing response and `h` the number carrying another response. Identify the first response by its effect **before** comparing reproductive success: each of its carriers contributes `k` units to the shared support multiplier,

\[
U=b+ka.
\]

The declared descendant law is

\[
(A,H)=\bigl(U\,2a,\;U\,3h\bigr).
\]

Both responses have equal access to the shared multiplier; their per-carrier descendant rates are two and three. These rates are supplied. They could represent an opportunity difference associated with producing support, but this model does **not** derive the difference from a material expenditure or measure a biological cost. The support variable is a specified productive opportunity multiplier, not a conserved resource account or a scalar measure of ethical value.

Two collectives initially have equal size four, with compositions `(3,1)` and `(1,3)`. Their offspring are pooled without additional loss, sorting or mutation. The pooled initial supporter fraction is `4/8`. The comparison changes `k` while preserving `b=1`, both compositions, both relative rates and faithful transmission.

**All these ingredients remain supplied:** response variation, initial association, shared support production, conversion into descendant counts, the rates, faithful transmission, one-generation timing and pooling. Calling the law generative does not discharge their derivation. Conversely, the support-producing response is not defined as whichever response later wins; it has the same independent effect in both cases.

Here *collective success* means the number of carrier descendants contributed by a collective. It does not mean that whole collectives themselves replicate faithfully or that their group identities survive pooling. This is a comparison of within-collective change and differential demographic contribution, with a fixed initial grouping. A recursive group-lineage theory needs additional succession and regrouping mechanisms.

## Exact checked results

The source is [RecursiveGenerativeSelection.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean), namespace `RecursiveGenerativeSelection`.

1. **Cross-product criterion.** `cross_compare_iff` proves
   \[
   a(A+H)<A(a+h)\quad\Longleftrightarrow\quad aH<Ah.
   \]
   For positive population totals this is the exact comparison of the initial and descendant supporter frequencies. Lean checks the integer inequalities directly; no unchecked division operation or floating-point approximation enters the proof. The algebra also holds at zero totals, where frequency language does not apply.
2. **Actual productive consequence.** `more_supporters_produce_more_support` proves that `k>0` and a larger supporter count give strictly more shared support under this law. The producer's label thus refers to a fixed consequence, not to its relative fitness.
3. **Within-collective loss.** `supporter_share_falls_within` proves strict supporter-frequency decline whenever both types and shared support are positive. `descendant_totals_positive` separately checks an applicable positive denominator. The shared benefit does not erase the specified two-versus-three transmission disadvantage.
4. **Whole pooled comparison.** `pooled_counts` proves
   \[
   A_{\mathrm{pool}}=8b+20k,\qquad H_{\mathrm{pool}}=12b+18k.
   \]
   `global_supporter_share_rises_iff` proves that the pooled supporter frequency strictly exceeds its initial `1/2` **if and only if `k>2b`**, using cross products. `support_contribution_threshold` checks the corresponding cancellation. This threshold is for the declared compositions, rates and timing; it is not a universal biological constant.

The matched witnesses check the following values and comparisons as closed Lean propositions:

| Quantity | Weaker coupling: `b=1, k=1` | Stronger coupling: `b=1, k=3` |
|---|---:|---:|
| Support multipliers, rich / poor collective | `4 / 2` | `10 / 4` |
| Rich collective descendants `(A,H)` | `(24,12)` | `(60,30)` |
| Poor collective descendants `(A,H)` | `(4,18)` | `(8,36)` |
| Rich / poor descendant totals | `36 / 22` | `90 / 44` |
| Pooled descendants `(A,H)` | `(28,30)` | `(68,66)` |
| Pooled supporter frequency | `28/58 < 1/2` | `68/134 > 1/2` |
| Supporter frequency within each collective | Falls in both | Falls in both |

`weak_coupling_witness` and `strong_coupling_witness` each explicitly check: more shared support in the rich collective, exact output counts, positive collective totals, higher output by the rich collective, lower supporter share within both collectives, and the stated pooled direction. Positive collective totals imply a positive pooled total. Initial collective totals are both four.

The general proofs use constructive natural-number arithmetic and cancellation. The concrete cases use kernel-checked `decide`; no `native_decide` or numerical simulation substitutes for the proof.

## What the cases establish

The affirmative case shows that differential contribution through actual support formation **can overcome** an adverse within-collective comparison. It preserves the user's proposed route as a meaningful mechanism. Favorable cross-level propagation is neither impossible nor merely a change of label.

The negative case preserves the same independently specified support-producing response, actual shared benefit, higher collective output and faithful transmission. Yet the producer's global frequency falls. It therefore rejects the **unqualified one-generation inference** from “support-rich collectives are more productive” to “their support-producing structure must increase throughout the larger population.” No freely toggled moral judgment produces this difference.

The negative case does not show that these producers become extinct, that the whole arrangement collapses, or that selection never favors generativity. The positive case does not show fixation, permanent stability, further group formation or improvement at every higher scale. Both cases end at the pooled descendants. Applying the mechanism again would require a specified next grouping, continued support production, compatible transmission and the appropriate comparison over the next interval. Repeating an assumed favorable inequality at every level would not derive those conditions.

The nonproducing response is not thereby shown to be wholly degenerative or ethically bad. In this representation it benefits from a contribution it does not make, and reproduces faster within each collective. The full consequences of its activity are not represented. Nor is the support-producing response thereby morally good in every wider continuation. Biological success, support generation and justified ethical quality cannot be identified by this count alone.

The result sharpens the research bridge: **support generation → differential collective contribution → actual transmission of the generating structure** requires a sufficiently favorable coupling of these relations. Universal normative warrant still requires an argument for ethical significance and practical force, including where selection and actual good diverge.

## Verification and dependency audit

Fresh Lean **4.29.1** build with source bytes copied to a new temporary directory and `LEAN_PATH` restricted to that directory. The source contains **12 theorem declarations, including three arithmetic helpers, and three definitions: 15 audited declarations, all with empty axiom dependencies**. The [audit file](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelectionAudit.lean) covers each named declaration. There are no unproved placeholders, custom axioms, classical choice, `propext` or `Quot.sound` dependencies. Empty dependency lists do not remove the supplied model law or substantive premises described above.

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/recursive-generative-selection-verification/check.py
```

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/recursive-generative-selection-verification/check.py) invokes the pinned compiler for `--version`, builds `RecursiveGenerativeSelection.olean` from the copied source, and checks `RecursiveGenerativeSelectionAudit.lean`. [verification.json](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/recursive-generative-selection-verification/verification.json) records the exact successful command arguments, timestamp, compiler version and commit, source SHA-256 values, checker hash, log hashes and complete declaration list. [axioms.txt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/recursive-generative-selection-verification/axioms.txt) records the 15 empty audits; [compiler.txt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/recursive-generative-selection-verification/compiler.txt) is empty after a successful exit. Exact checked source bytes are retained under the receipt's `sources/` directory; no compiler binaries or caches are added.

This completes the formal support at its stated one-generation scope. It does not complete recursive evolutionary explanation or the governing universal metaethical objective.
