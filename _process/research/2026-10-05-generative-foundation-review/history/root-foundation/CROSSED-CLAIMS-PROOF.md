# Crossed claims: coupled chances and a changing-menu control

8 October 2026. AI-authored formal account for the [current argument](CROSSED-CLAIMS-ARGUMENT.md). The [source ledger](CROSSED-CLAIMS-SOURCES.md) and [independent review](CROSSED-CLAIMS-REVIEW.md) carry the philosophical assessment. This module provides conditional mathematical tests, not a proof of LR's ethical local-stability commitment.

**New result:** replacing a solo route with a newly feasible joint route can preserve previous individual chance floors through the same actual tickets while increasing protection at another position. Strict equality of all individual probabilities can reject this improvement. A separate concrete control shows how a strongest-claim filter can change a choice because of an available route it does not itself select.

The [aggregation-context study](AGGREGATION-CONTEXT-INTEGRATION.md) already established the upgrade and composition diagnostics: 6 theorems/15 audits. This round does not repeat its generic cycle or strict-extension obstruction. [LC](UNEQUAL-BASIC-LOSSES-PROOF.md) likewise retains its 14/23 scope; positive-weight disagreement is not offered again as the new result.

## One joint provision, three differentiated requirements

The [new source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CrossedClaims.lean) distinguishes requirements P, Q and R and three possible routes:

| Route | Protected requirements |
|---|---|
| `solo` | P |
| `other` | Q and R |
| `joint` | P and Q |

These are roles within a stipulated provision, not ontologically independent value owners. Q's appearance in two routes represents one requirement protected through different mutually exclusive outcomes; it is not a second claimant. Selecting a route and protecting an individual requirement are different events.

For the intended crossed-loss interpretation, P may face a graver basic loss than either Q or R. The initial `solo`/`other` comparison therefore need not satisfy BC1's equivalent-stakes assumptions. The code does not assume equal gravity, establish a fair initial lottery, or derive a probability from severity. It tests what follows **if** some chance allocation or floor is already justified in the actual circumstances.

Efficacy, timing, authority, burdens and all relevant unrepresented consequences remain correspondence conditions. The new route must actually be available and independently permissible. A Boolean protection entry alone cannot certify equal quality of support or absence of a hidden cost.

## The positive coupling

Natural ticket weights `(a,b,c)` represent a finite rational lottery over the three routes, with total `N=a+b+c>0`. The protected-ticket numerators for P, Q and R are respectively `a+c`, `b+c` and `b`. The probabilities have the same denominator `N`.

The transfer replaces each `solo` ticket with `joint`, giving `(0,b,a+c)`. It leaves every other ticket's route unchanged. This is stronger than comparing only marginal chance totals: on a ticket formerly producing solo protection, P remains protected, R remains unprotected and Q gains protection. On the other tickets, no protection changes. The initial assumption that a jointly feasible replacement exists is doing substantive work.

| Checked theorem | Exact contribution |
|---|---|
| `replacement_preserves_each_ticket` | P and R retain their protection on each route replacement; Q never loses protection and gains it on replaced solo tickets |
| `joint_strictly_extends_solo_protection` | The unchanged `PracticalJudgment.Better` comparator recognizes the additional indexed protection when other represented gains are fixed |
| `transfer_conserves_total_and_chances` | The denominator is preserved; P and R's numerators stay fixed; Q's increases by `a` |
| `transfer_preserves_any_satisfied_floor` | With a positive original total, every supplied individual ticket floor already met is still met after transfer |
| `transfer_strictly_improves_q` | Positive solo weight makes Q's improvement strict |

The floor result covers any floor expressed on this lottery's common denominator, not only equal floors or a half chance. A baseline using only the old routes has `c=0`, but no particular values of `a` or `b` are selected by the theorem. If `a=0`, the transfer adds no protection for Q; strict improvement requires positive solo weight. The proof uses ticket counts with a common denominator, not arbitrary real-valued probability distributions. In particular, this is not a proof that a 50–50 lottery is fair, that full transfer is the uniquely permissible policy, or that every later decision must preserve every historically received probability.

The result supports a concrete conditional response to new joint capacity. Existing warranted chances need not be discarded or flattened into a new equality requirement when additional protection can be attached to the same tickets. The normative reason to take that opportunity still uses the declared ethical commitments and the full relevant history.

## Exact equality is an additional, potentially costly constraint

`EqualPersonalChances` equates the three protected-ticket numerators. The theorem `equal_personal_chances_iff` proves that this holds precisely when `c=0` and `a=b`. Thus, if the lottery is nonempty, exact equality requires positive solo tickets and gives the joint route no tickets.

`equal_chances_have_improving_replacement` then establishes that every such lottery has the specified transfer: the total stays fixed, every individual chance is preserved or improved, Q's increases strictly, and the resulting chances are no longer all equal. The retained application example starts from `(1,1,0)` and checks protected-ticket numerators `(1,2,1)` after transfer. The common denominator remains two.

This tests an overstrong universal equality requirement. It does not refute fair-chance claims generally, claim that P/Q/R have equal ethical strength, or turn probability improvement into a complete account of fairness. The positive comparison concerns actual jointly available protections; no expected-welfare score is used. Remaining losses in any realized draw still occur, and no separate harm or participation right is cancelled by arithmetic.

## A specific global relevance filter

The final control uses three stipulated disjoint rescue groups: one claim of gravity 10, two of gravity 6 and four of gravity 4. All can be supplied as basic claims in the diagnostic; these values are illustrative inputs, not a measured scale. The anchor is the greatest gravity in the available menu. The algorithm assigns zero score to a group whose gravity is below half that anchor; otherwise it multiplies group size by gravity.

`unselected_strong_route_changes_filtered_choice` verifies that the menu containing only the middle and lower groups selects the lower group. Adding the strongest group's route changes selection to the middle group, while the strongest route itself is unselected. The lower group's score changes from 16 to zero. The actual middle/lower rescue content has not changed in this construction; the specified algorithm changes its treatment through the larger menu.

This is a concrete reconstruction for the relevance challenge discussed through Privitera in the [source assessment](CROSSED-CLAIMS-SOURCES.md). It is not the article's literal example, a newly discovered general inconsistency, or a formalization of the full ARC theory. Zero is the filter's assignment, not proof that the excluded living requirements cease to matter. A context-sensitive defender may justify a real change of grounds; the numerical cutoff alone supplies no such justification. The local normative LR candidate is not identified with this global algorithm.

## Actual checking and frozen scope

The [dedicated checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_crossed_claims.py) compiled source snapshots under **Lean 4.29.1**, retained signatures for all eight new theorems, and audited every explicit top-level declaration. The [passing receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/crossed-claims-verification.json) points to [run `20261008T103855.124036Z`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/crossed-claims-checks/20261008T103855.124036Z/verification.json): **8 new theorems / 23 declaration audits**, with 17 retained artifacts. The single `Controls.lean` example is recorded separately and adds no theorem count.

For the new module, 13 declarations have empty dependency lists, 6 use only `propext`, 2 use `propext` and `Quot.sound`, and 2 use those together with `Classical.choice`. No project-specific axiom or proof escape is introduced. Generated structure/inductive/deriving helpers are kernel checked but not separately counted as requested audits. The imported unchanged `PracticalJudgment` module has 30 inherited theorems/46 audits; those counts are not added to the new contribution.

- New source SHA-256: `ce23a0d674433152ae2e80455f932283b5b96bafb1061f3197c75b17bfb97f28`.
- Dedicated checker SHA-256: `c465579f1c5edd10d8b141d014f4ba3e89be6ca5556075823739c0c2c13a3166`.
- Shared checker helper SHA-256: `b9f56e1700c03f0019a486d0f3c097f70c2ce20414da9e7b231131b8ed4a8308`.

Source, checker and receipt are frozen. No earlier Lean source or shared README was changed. The verification establishes the declared implications, not the substantive warrant of LR, an all-purpose fair lottery, or empirical availability of the joint route.
