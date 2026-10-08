# New living, sequential decisions and whole-history comparison

8 October 2026. AI-authored continuation of the [living-value investigation](LIVING-VALUE-SCOPE.md#21-does-conditional-care-exhaust-the-reasons), under the [continuing goal](../../../../sources/15-codex-theory-conversations/2026-10-08-knowledge-content-continuation.md#continuing-the-frontier-after-the-two-answers). The preceding round made progress by testing the restrictive premise in conditional care. This round examines a positive route to favorable new formation and checks its inference. The stronger goal remains necessity for adequate scientific philosophy, not merely a workable ethical model. The [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) and the completed G0/J account retain their scopes.

**Result:** a favorable complete-history comparison can follow from an initial mixed improvement and a warranted reallocation favoring the newly formed life. The argument needs neither a welfare value for nonexistence nor a prior deprived claimant. Its comparisons and their scope still need ethical warrant. Six new Lean theorems and thirteen declaration audits pass; all reported dependency lists are empty. A finite diagnostic shows why judgments at successive stages cannot silently replace the required whole-history comparisons. This does not certify an ethical rival or prove G0.

## 1. Primary argument and genealogy

Matthew Adelstein, “The Sequence Argument Against the Procreation Asymmetry,” *Utilitas* 36(4), 338–351 (2024), [publisher text](https://www.cambridge.org/core/journals/utilitas/article/sequence-argument-against-the-procreation-asymmetry/773D4C271F072ED88BCC45BD9F3A3963), DOI 10.1017/S0953820824000189. Read introduction, §§2.1 and 2.3, selected §§2.2 and 2.4, and conclusion; §3 was selectively inspected. His argument connects creation accompanied by an incumbent benefit, reallocation toward the guaranteed future life, and sequential equivalence. He also discusses transitivity and backward induction. We assess that route; stronger claims about demandingness are not adopted.

The source motivates this application; the formalization and its limited diagnostic below are ours. The repository already contains [a positive preorder route and incomparability analysis](HUIGEN-SELF-GROUND-AUDIT.md#61-affirmative-comparison-across-the-formation-of-a-life), plus [a temporal-neutrality assessment](WHOLE-PROCESS-GROUNDING-ARGUMENT.md#16-grounding-a-comparison-of-whole-continuations). Elementary transitivity, the creation/obligation distinction and the possibility of conditional care are credited prior content. The new contribution is an explicit assessment of this sequential route, its whole-history interpretation and its transport requirement, with actual Lean checking. Mathematical novelty is not claimed.

Access notes: Chappell's *Rethinking the Asymmetry* and Nebel's *Asymmetries in the Value of Existence* were located through [an institutional manuscript](https://eprints.whiterose.ac.uk/id/eprint/116418/1/Chappell_Asymmetry.pdf) and [an archived article](https://philarchive.org/archive/NEBAITv2); their bodies were not assessed for this result. A later Nebel paper, *The Procreation Asymmetry: Some Puzzles*, was located on [the author's publication list](https://jakenebel.com/); its archive retrieval returned 403. None is counted as independently inspected support. All access is link-only; no source bytes are imported.

## 2. Specify complete continuations before comparing them

Our reconstruction fixes three admitted continuations of one formative situation. In N, no additional life forms. In A, a life forms with a supported worthwhile continuation and an incumbent life receives an optional improvement. In B, the same new life forms with a richer supported continuation, while that optional incumbent improvement is absent. The incumbent's baseline conditions remain intact. Formation, support, agency, legitimate claims, risks and other consequences belong to the histories; they cannot be discarded as implementation details.

The candidate sufficient comparisons are:

| Comparison | Proposed ground | What remains to be warranted |
|---|---|---|
| A is better than N | An incumbent gain together with supported new living and no identified countervailing loss | The added life does not block the whole comparison. An absent objection alone does not establish that claim. |
| B is better than A | A sufficiently significant improvement for the same new life, compared with the optional gain forgone | The actual tradeoff, its scale and legitimate conditions warrant this whole comparison. A greater number alone is insufficient. |
| B is better than N | The two warranted comparisons compose in one transitive ordering | The relation really assesses the same complete histories and relevant scope. |

This is a positive route to the formation conclusion: B contains further living without leaving an incumbent gain as its sole final rationale. The conclusion is a comparison of whole continuations. It is not an assertion that the new life is better off than its nonexistence, nor that anyone is obligated to realize B.

The conditions are substantial but can be defended in concrete cases. G0 supplies the favorable significance of living; J1–J4 govern comparison, protection, responsibility and selection. That completed route can support particular applications. The present question is whether the comparisons have independently compulsory warrant for every adequate scientific philosophy. Their plausible application does not establish that universal extension.

## 3. Distinguish two forms of the argument

On the **whole-history reading**, A versus N and B versus A are assessed in one comparison relation. If both strict comparisons are justified and that relation is transitive, B versus N follows. The checked `whole_comparisons_favor_formation` verifies exactly this elementary inference. Its ethical work is in the two comparisons, rather than in an additional measure of generativity.

On the **stage-relative reading**, a reason for starting is assessed before the formative commitment, while a reason for redirecting is assessed after it. The changed history can create responsibilities, remove alternatives or change relevant access. A later warranted response does not automatically establish an initial ranking of complete plans. `transport_supports_initial_comparison` exposes the additional sufficient premise: the particular later comparison also holds in the initial complete-history assessment.

This is not an allegation that the primary author overlooked backward induction. The source discusses it and gives reasons to resist it. Our question is whether those reasons establish the comparison's required scope. Nor do we require every practical judgment to remain unchanged through every transition. The transport concerns the named pair of complete alternatives; its applicability depends on preserving the relevant facts, grounds and question.

Planning can recognize future conditions before they become actual. An initial appraisal of A and B should therefore include the life present in both continuations and the different conditions it would undergo. Simply postponing all attention to that life until a later calendar time would omit relevant content. But faithful prospective inclusion is still distinct from the warranted strength of the reallocation, and from the comparison with N, where the life does not form.

## 4. What the finite diagnostic checks

The three constructors in `FormationSequence.lean` stand for N, A and B as alternative complete continuations. Their stipulated incumbent gains are 0, 1 and 0. New living is represented by `none`, `some 1` and `some 3`. `none` means no newly formed bearer in that continuation, not an absent person's zero welfare. The numbers illustrate two supplied evaluation rules; they are not measured welfare or the theory's moral scale.

The initial rule counts only the incumbent gain. The later rule counts that gain together with the stipulated new-life quantity. Each induces a transitive strict comparison. A beats N initially; B beats A later; B does not beat N initially. The initial rule also fails to inherit the particular later B-over-A comparison. Both assertions are checked.

This diagnoses a specific inference failure from stage-local comparisons and separate transitivity alone. The restrictive initial rule is precisely contested ethical content. The construction neither proves that it faithfully represents any author's complete view nor certifies its normative adequacy. It does not preserve and then refute the fuller G0 account. The witness makes an omitted premise visible; it cannot decide which substantive account deserves acceptance.

The generic results range over arbitrary represented histories. `faithful_redescription_preserves_result` separately checks transfer to a differently described action when an explicitly supplied sameness relation preserves the relevant comparison. Identical terminal quantities do not establish that premise: the histories may differ in promises, actual interim losses, control or consent. Conversely, splitting one unchanged authorized sequence into more descriptive steps supplies no new ethical difference.

## 5. Counterreview of the affirmative route

**The initial comparison already crosses the formation boundary.** A rival permitting incomparability between histories with different lives may reject A-over-N even when A benefits an incumbent. The incumbent's benefit makes this a substantive challenge to that restriction, but it does not logically eliminate it. The inherited Broome/Rabinowicz/Bader assessment already explains why incomparability is not equivalent to a neutral contribution that can simply be cancelled. We do not reclassify that dispute as a mathematical error.

**The second comparison cannot be licensed by optionality alone.** Rescinding a benefit may violate a valid undertaking or impose an actual loss even if the final state resembles an earlier baseline. The whole-history reconstruction must account for this. A constructed case can exclude such claims only as an explicit conceptual condition; actual applications require evidence.

**A favorable comparison does not allocate responsibility.** Even if B is better than N, that alone does not specify who may act, whose support may be used, or what burden is owed. The existing practical account supplies those additional principles. The new proof does not derive population maximization, an obligation to reproduce or permission to replace existing lives.

**The narrow inference test does not defeat the strongest source argument.** The complete-history formulation is formally valid. The diagnostic refutes only the weaker substitution of two stage-specific rankings. A fair assessment must therefore return to the substantive premises rather than celebrate that diagnostic as a refutation of generative value or population ethics.

## 6. Validation and contribution to necessity

[Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/FormationSequence.lean), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/check_formation_sequence.py) and [actual compilation receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/formation-sequence-verification.json): **6 new theorems / 13 explicit declaration audits**, all empty dependency lists, Lean 4.29.1. The first compilation exposed a decidability elaboration issue; it was repaired with explicit arithmetic proofs. Both retained runs remain available. The scanner covers named top-level declarations, not a separate inventory of generated constructors and projections. No proof escape, empirical experiment or independent-agent acceptance is claimed.

The new result strengthens the positive case at a specified bridge: **warranted improvement involving an incumbent and new living, followed by warranted reallocation within that formed population, can establish favorable new formation**. It replaces an appeal to mere possibility with a checkable comparative route. It does not derive either ethical comparison from descriptive generativity or scientific competence. The account of G0 remains usable and complete at its authorized scope.

The remaining central obligation is the warrant for the initial cross-formation comparison, together with any claimed transport of the second comparison. It is not another missing transitivity proof. A fully justified instance would establish favorable formation in that case; universal necessity would still need the corresponding scope argument and the other commitments of the theory. The original goal remains active.

**完整历史中的两个有根据改善可以合成进一步生成的正面比较；先后情境中的理由不能在未说明对应时直接拼接。形式实查保留正面路线，也明确其伦理前提与普遍范围尚需什么根据。**

[Documentary and preservation checks](FORMATION-SEQUENCE-CHECKS.json) bind the new proof, prior proof receipts, source links and the owned bilingual M21 update. These checks do not certify philosophical truth or concurrent whole-table freshness.
