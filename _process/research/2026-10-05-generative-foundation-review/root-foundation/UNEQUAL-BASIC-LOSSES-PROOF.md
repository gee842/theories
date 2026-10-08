# Unequal basic losses: checked diagnostic and scope controls

8 October 2026. AI-authored formal note supporting the current joint-loss comparison inquiry. The [basic-conflict chapter](../../../../theories/becoming/chapters/BASIC-CONFLICT-JUDGMENT.md) already contains BC1's equivalent rescue and BC2's warranted one-to-one severity argument. This module neither re-proves them nor claims that their complete ethical contents have been encoded. The present normative proposal is named **LC**, separately from those existing commitments. The [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) governs its interpretation.

**Checked result:** a two-tier cumulative comparison is exactly the unanimous comparison within a specified additive diagnostic family. That family agrees on each of two separate numerical sensitivities while disagreeing on a crossed case. Duplicate report counts and a compressed direct-interruption profile can also misrepresent the actual relationships. These are standard mathematical diagnostics and concrete representation controls, not a new ethical utility theorem.

## Exact objects and hypotheses

The [Lean module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/UnequalBasicLosses.lean) imports the unchanged `PracticalJudgment` comparator. A profile `(l,h)` counts losses in two supplied tiers, both intended to lie within a specified basic-loss scope. Its cumulative coordinates are `(l+h,h)`: all losses and losses at the higher threshold.

`CumulativeLE a b` says that neither coordinate of `a` exceeds the corresponding coordinate of `b`. `CumulativeLT` additionally requires one coordinate to decrease strictly. The diagnostic cost is

\[
D_{x,y}(l,h)=x(l+h)+yh,\qquad x,y\in\mathbb N,
\quad x>0,\ y>0.
\]

Thus the lower-tier weight is `x` and the higher-tier weight is `x+y`. Positivity and the extra severity increment are explicit. This is a family of natural-number diagnostics, not a chosen exchange rate or a scale of experienced welfare. Its universal quantifier ranges over this family only; it does not range over all warranted ethical positions.

Any ethical application must independently justify the actual loss relationships, the tiers, the relevant scope, permissible combination, whole-history adequacy, permissions and competing claims. A positive integer difference is not automatically an ethically decisive difference. LC supplies its own defended comparison reason; the mathematics cannot eliminate an otherwise justified claim to a chance, establish obligation, or confer authority.

## What the fourteen theorems establish

1. `positive_linear_diagnostics_iff` proves the underlying two-coordinate result: all positive natural linear diagnostics agree exactly when each coordinate is no larger. When a coordinate inequality fails, the proof constructs an admissible coefficient which exposes it.
2. `cumulative_iff_all_positive_diagnostics` and `strict_cumulative_iff_all_positive_diagnostics` apply that result to the two supplied severity thresholds. The strict equivalence requires a strict decrease somewhere, not merely equal diagnostic values.
3. `cumulative_strict_irrefl` and `cumulative_strict_trans` establish consistency of this fixed-profile strict relation. The already checked finite-frontier theorem can consequently be reused on a finite nonempty menu. This does not establish consistency of every cross-context ethical extension.
4. `individual_sensitivities_agree` verifies that every diagnostic favors fewer losses at the same tier and one lower-tier loss over one higher-tier loss. These are the numerical projections relevant to the separate BC1 and BC2 questions. The theorem does not encode their permissions, histories, opportunities or complete normative rationales.
5. `one_higher_two_lower_cross_thresholds` and `positive_diagnostics_reverse_crossed_case` show the remaining joint indeterminacy. One higher-tier loss and two lower-tier losses cross the thresholds. Parameters `(x,y)=(1,2)` favor the latter; `(2,1)` favor the former. Both members retain the individual sensitivities just checked. Those sensitivities therefore do not select a joint exchange rate within this diagnostic class. This is not a countermodel to full G0/J/BC1/BC2.
6. `same_reported_grounds_same_inventory`, `duplicating_reports_does_not_multiply_grounds` and `duplicate_row_count_can_reverse_comparison` check the distinction between reported descriptions and their referenced grounds. Under a fixed supplied inventory, reports with the same membership select the same inventory entries. Duplicating reports cannot enlarge this selection, although counting raw rows can reverse a comparison.
7. `equal_direct_profiles_different_common_continuation`, `direct_profile_does_not_determine_continuation` and `common_support_distinguishes_histories_in_existing_comparator` supply the common-support control below.

The report result deliberately does not discover ethical units. For the selected inventory to give an actual count, its entries must be correctly identified, complete for the scope and nonduplicated. The invariance theorem alone does not require those substantive properties and therefore cannot certify them. Renaming, splitting or merging real losses is not validated merely by assigning matching identifiers.

## A common-support relationship which the count omits

The constructed support history has a main supply, a substitute supply and a relay. Its one supplied continuation law is

\[
(\text{main supply available}\lor\text{substitute available})
\land\text{relay available}.
\]

Interrupting the substitute and interrupting the relay each produce a direct-interruption count of one. The first preserves the provision through the main supply; the second prevents it. The proof shows that no classifier using only that direct profile can recover the provision's continuation for every represented history. The inherited comparator distinguishes the two when this continuation is the indexed protection and other represented gains are fixed.

This is **not** a case of two complete, ethically certified loss profiles with unexplained unequal value. A substitute-supply interruption is not by itself established as a basic living loss. The control instead demonstrates that counting directly interrupted positions can omit consequences determined by the very same support relationship. The omitted consequence is derived from that law, not added by freely toggling an ethical predicate. Restoring the relationship can require revising the proposed loss units or profile, rather than adding an arbitrary “synergy bonus.” The interruption retained by the favored history is still in its loss list; favoring a continuation does not erase it.

The whole here is no additional bearer which absorbs the differentiated losses. Supply, substitution, relay and continuation are roles of the same provision. The mathematical separation makes explicit what the direct count omits.

## Verification and preservation

The [dedicated checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_unequal_basic_losses.py) compiled unchanged source snapshots using **Lean 4.29.1** and retained theorem signatures and a dependency audit for every explicit top-level declaration. No `sorry`, added axiom, unsafe implementation or native-decision escape is accepted by its scanner. Generated constructors, projections and derived instances are kernel checked through compilation; they are not counted as separately requested declaration audits.

The final [passing receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/unequal-basic-losses-verification.json) points to [run `20261008T101800.695865Z`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/unequal-basic-losses-checks/20261008T101800.695865Z/verification.json). It records **14 new theorems and 23 new declaration audits**, plus the inherited module's 30 theorems/46 audits, which are not new results. Seventeen retained artifacts include source/checker snapshots, compiler logs, signature files and dependency logs.

A retained `Controls.lean` additionally compiles two worked applications. `CumulativeLT (2, 0) (1, 1)` preserves the total number while reducing higher-tier loss. `CumulativeLT (2, 0) (1, 2)` improves both cumulative coordinates: two lower-tier losses compare favorably to one lower-tier and two higher-tier losses within the diagnostic. Both checked examples are recorded separately and add no theorem or declaration-audit count. Their ethical correspondence remains independently justified. The second example prompted this final check; the fourteen theorem statements and proofs remain unchanged.

For the new module, 9 audited declarations have no axiom dependencies, 9 use only `propext`, 3 use `propext` and `Quot.sound`, and 2 use those with `Classical.choice`. No new or project-specific axiom is introduced. The receipt separately records inherited dependencies and the Lean binary hash.

- New source SHA-256: `4507b58f1e43264aecf96e600ef0cc5a0fb942a7d6b9d69d8caa32e97b8bf94f`.
- Dedicated checker SHA-256: `4333c9aeb26e43ffbaee5c56db2fc14cc17572675e8c313e0e224b555b175f3e`.
- Shared helper SHA-256: `b9f56e1700c03f0019a486d0f3c097f70c2ce20414da9e7b231131b8ed4a8308`.

The source and dedicated checker are frozen at this receipt. No earlier comparator or shared README was modified. The formal result provides a bounded consistency and insufficiency test for the joint comparison inquiry; it leaves the substantive LC argument and actual correspondence to their independent assessment.
