# Relative uniqueness, global coverage and mathematical explanation

8 October 2026, Asia/Bangkok. AI-authored research under [Ren’s direction](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#普遍唯一性的直接检验--direct-test-of-universal-uniqueness). The [current theory](../../../../theories/becoming/history/EXPLANATORY-NECESSITY.md) integrates the outcome. This directly follows the user’s request to test universal uniqueness against whole-constraint and mathematical explanations. The previous evidence-acquisition connection remains checked at its own scope; its proposed monitoring continuation is not silently substituted for this new central question.

**Result:** a genuine but question-relative uniqueness theorem is now checked: two exact, reduced presentations have a total, single-valued matching in both directions on their used codes. This establishes a unique correspondence of answer distinctions, not a unique generative mechanism or ontology. A matched tiling case gives a compact structural impossibility proof and an exact local/global correspondence; it supplies no basis for privileging temporal generation. **32 new Lean theorems / 74 audits including 42 inherited declarations pass. Of the 74, 62 have empty axiom dependencies and 12 use only Lean’s standard `propext`.** No custom axiom or proof hole is introduced.

## 1. The universal inference being tested

The affirmative route proposed in the conversation was: independently fixed explanatory target → necessary common relational content → sufficient common structure → uniqueness up to an appropriate equivalence. This study tests the last two arrows rather than adding another successful calibration example.

A fixed target must not be chosen merely to ensure that our preferred vocabulary wins. The concrete target here is: **can each cell of a specified finite board be covered exactly once by the specified allowed dominoes?** This is intelligible without first requiring a temporal narrative. The general uniqueness target is an arbitrary family of specified questions and their correct answers. `Exact` means accuracy on that family; it does not define philosophical explanation.

The [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) remains in force. Local changes and global compatibility concern the same board and the same possible coverage, not independent realms of constraint and flow. A mathematician’s construction and checking of the proof are organized activities within the whole. They are not therefore identical with the mathematical relationship that the proof establishes. Omitting the personal history of discovery from a coverage proof is not evidence that knowing exists outside generative reality.

## 2. The positive uniqueness theorem

For models `M`, questions `Q` and codes `C`, a `Presentation` contains both `encode : M → C` and `read : C → Q → Prop`. Interpretation is included explicitly. A code cannot disguise a change of decoder.

- `Exact target p`: reading the code of each model gives exactly the independently declared answers.
- `SameAnswers target m n`: all declared questions have the same answers in `m` and `n`.
- `Reduced target p`: models with the same answers receive the same code. This is an **additional minimality requirement**, not a consequence of accuracy or a definition of all adequate explanation.
- `Used p c`: some model has code `c`. Unused syntactic objects are excluded from the correspondence claim.
- `Matches p r c d`: one model is encoded by `c` and `d` in the two presentations.

The kernel theorem proves that exactness plus reduction makes equality of codes equivalent to agreement on all target answers. Consequently two such presentations induce the same distinctions. `relative_unique_correspondence` proves that every used code on either side matches exactly one code on the other. `matches_iff_equal_answers` characterizes that relation through the actual readings; `unique_matching` proves uniqueness among functional relations aligning each model’s encodings. No inverse function is chosen using classical choice.

This is a **relational bijection of used codes preserving the question-indexed answers**. It is not yet an isomorphism of causal/compositional operations, a category equivalence, an algorithm for finding a minimal presentation, or a theorem asserting that every target admits a computably accessible reduced presentation. The logical quantification is general in the supplied model and question types; the philosophical scope remains relative to that target and those conditions.

Two checked boundary cases prevent inflation. For a Boolean pair and a question only about the first coordinate, both the first-coordinate code and the full pair answer exactly. Only the former is reduced; accuracy alone therefore does not imply the minimality condition. If questions are extended to both coordinates, no decoder of the first coordinate can answer them all. A distinction irrelevant to one target can become indispensable to another. These are information-scope tests, not models of independently existing mental and physical substances.

**What this contributes:** uniqueness need not be an untestable aspiration. There is a precise relative theorem. **What it cannot contribute alone:** the theorem is neutral about whether the answers come from a generative, geometric, algebraic or whole-constraint explanation. Its force comes from fixed questions, exactness and reduction. It cannot establish generation’s unique foundation by being renamed a generative theorem.

## 3. One matched case for both rivals

The board is a list of cell occurrences; permutation expresses that list order is immaterial. `tile a b` specifies allowed pairings independently of color balance. A local placement removes an allowed pair from the remaining board, preserving the other occurrences. There is no primitive observer, intention, physical clock, cost account or actual robot in this mathematical interface.

The global certificate for a list of tiles requires every tile to be allowed and the concatenation of its cells plus the residual board to be a permutation of the initial board. This is a compact compositional condition, not a precomputed table of answers to all histories.

The checked correspondence is:

> A tile list has a local placement history leaving a residual board, up to its immaterial list order, **if and only if** it satisfies the global coverage condition.

For complete coverage the endpoint is exactly the empty board, so `complete_trace_iff` gives an exact equivalence without a residual permutation qualification. `global_realized` constructs a mathematical placement history from a global certificate; `trace_global` reads global coverage from any admitted finite history. The law allows any presently available allowed pair to be removed. Obstacles such as approach direction, motion clearance, changing geometry or fuel are outside this target. Adding them would require extending **both** sides of the comparison.

`two_tile_orders` supplies both orders for two allowed pairs on the same four-occurrence board. Where the pairs differ, the words differ; the theorem does not say that duplicate identical pairs create distinct orders. The global coverage target does not select a unique temporal order. This does not deny that a particular physical execution has an order.

The equivalence gives genuine support to a **shared relational-content** thesis. It equally preserves a global account. Neither implication of an equivalence independently shows which side explains the other more fundamentally.

## 4. The mathematical explanation and its limits

Define a cell’s charge as +1 or −1 from a two-coloring and the board’s balance as the sum. For any supplied tile relation whose pairs have opposite colors, every global tiling preserves the balance of its residual board. This theorem is proved directly over tile legality and coverage permutations; it does not invoke `Trace`, acquisition of evidence or a mathematician’s biography.

For the concrete 8×8 instance, cells are `Fin 64` with row `n / 8` and column `n % 8`. Horizontal adjacency is same-row distance one; vertical adjacency is distance eight. The coloring is computed from row-plus-column parity. Adjacency is **not** defined by the desired color property: `adjacent_opposite` checks that the independently defined adjacency has the property. The board removes indices 0 and 63. Its computed signed balance is −2. `mutilated_no_cover` proves that no global domino tiling exists; `mutilated_no_history` imports this conclusion into local placement histories.

This supplies a structural reason for non-coverability: each allowed tile contributes one cell of each color, while the target board has a mismatch. Writing the proof with induction over a finite certificate is not the claim that the explanandum requires an actual historical construction. There is no successful complete construction of this board to narrate.

The invariant is explanatory for this obstruction but is not a complete code of tiling possibilities. The separated board consisting of indices 0 and 3 has balance zero and cannot be covered; the empty board has the same balance and can be covered. These are checked against the same adjacency law. Thus balance does not recover all coverage answers, much less all placement relations. A target-relevant mathematical explanation need not encode everything a complete description of dynamics would encode.

This narrows one overly strong route: “every adequate local explanation must retain the full generating history or relation.” The fixed impossibility target is explained by a coarser obstruction. It does **not** refute the broader proposal that composability and realizability are themselves differentiated relational articulations of one generative whole. That constitutive identification requires a further defended argument.

## 5. Complete proof map

[ExplanatoryStructure.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryStructure.lean), **17 new theorems**:

| Group | Declarations | Result |
|---|---|---|
| Local/global correspondence (4) | `trace_global`, `global_realized`, `realizes_iff_global`, `complete_trace_iff` | Same finite coverage target in both presentations |
| Structural balance (6) | `balance_perm`, `opposite_pair_balance`, `legal_balance`, `global_balance`, `unbalanced_no_cover`, `unbalanced_no_placement_history` | General invariant and its obstruction, with tile/color law explicit |
| Concrete geometry and boundary (6) | `adjacent_opposite`, `mutilated_balance`, `mutilated_no_cover`, `mutilated_no_history`, `separated_balanced`, `separated_not_coverable` | Fixed 8×8 impossibility and balanced-but-uncoverable contrast |
| Order (1) | `two_tile_orders` | Both orders realize a two-pair covering |

[ExplanatoryUniqueness.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryUniqueness.lean), **15 new theorems**:

| Group | Declarations | Result |
|---|---|---|
| Exact reduced kernels (3) | `equal_codes_same_answers`, `reduced_exact_kernel`, `reduced_presentations_same_kernel` | Exactness forbids merging different answers; reduction fixes the converse |
| Used-code matching (6) | `matches_total_on_used`, `matches_functional`, `matches_inverse_functional`, `matches_iff_equal_answers`, `unique_matching`, `relative_unique_correspondence` | Total and uniquely determined correspondence in both directions under stated hypotheses |
| Scope counterexamples (6) | `short_exact`, `full_exact`, `short_reduced`, `full_not_reduced`, `first_summary_cannot_answer_both`, `balance_does_not_determine_coverability` | Exactness is not minimality; enlarged questions change what must be retained; balance loses coverage distinctions |

The counts include support lemmas and explicit instances; they are not counts of independent philosophical discoveries. The final uniqueness theorem and the other 13 purely presentation-theoretic declarations have empty printed dependencies. The one imported balance contrast in that module uses `propext` through the structural proof. In the structural module 6 declarations have empty dependencies and 11 use `propext` through standard list/integer lemmas. The exact inventory is preserved in the receipt.

## 6. Substantive counterreview

| Challenge | Disposition |
|---|---|
| Minimality hides uniqueness in a definition. | Reduction is explicit and stronger than exactness. The theorem identifies its mathematical consequence; the full exact Boolean-pair presentation shows the condition is not forced by accuracy. Why explanatory practice should prefer a particular reduction is not settled. |
| All questions have been chosen to favor generation. | The tiling question is fixed by allowed cells, pairings and exact coverage. The general theorem accepts any question family and hence does not privilege generation. Target choice remains a substantive obligation. |
| The structural account secretly uses generation through recursion. | Recursive proof checking and mathematical finite composition are distinguished from a temporal law of the explained board. The question whether all mathematical constitution is generative remains open; using an inductive proof does not settle it. |
| A global constraint account is only a lookup table. | This rival gives a compact legality/coverage relation and a color invariant. It preserves the same target and yields a general obstruction without enumerating all placement histories. No complexity superiority is asserted without a common cost measure. |
| The invariant loses geometry. | Correct; the separated two-cell counterexample records exactly that loss. It is adequate for the color obstruction, not the full coverage classification. |
| This defeats the fuller one-process account. | No. The result constrains temporal and full-recovery overclaims. It does not posit a separate static reality, refute relational constitution, or prove a rival ontology. |
| This is merely a new proof of an old puzzle. | The puzzle and color argument are credited below. The contribution is the checked matched comparison plus explicit relative uniqueness and scope boundaries, not mathematical priority. |

This is the authoring agent’s substantive counterreview. No independent agent was requested or used. The ethical branch is not declared complete or impaired by this result. The new contribution to its factual-grounding side is a distinction between a relevant obstruction, complete relational content and representation-dependent surplus; none independently supplies a normative standard.

## 7. Primary sources and inherited work

- **Emily Adlam, [Laws of Nature as Constraints](https://arxiv.org/html/2109.13836), version 2.** This round revisits §§2.1–2.2 and reads §5.1. The account explicitly accommodates time-evolution laws through possible-history constraints. It motivates giving a global comparator the same modal content. Our finite tiling equivalence is not a formalization of Adlam’s physics or endorsement of her ontology. We do not import a basic law/mosaic split into the project’s one-process method.
- **Adrian De Lon, Peter Koepke and Anton Lorenzen, [A Natural Formalization of the Mutilated Checkerboard Problem in Naproche](https://d-nb.info/1366629000/34), ITP 2021, DOI 10.4230/LIPIcs.ITP.2021.16.** Read abstract/introduction and §§3.5–3.9, especially allowed dominoes, exact coverage and the color argument. This is a primary antecedent for the puzzle’s formalization and structural proof. Their presentation states finite-set/color commitments explicitly. We build a separate `Fin 64` model and check adjacency/color correspondence; no reproduction of their proof engine, priority claim or result-count aggregation is made.
- **Tobias Nipkow and Lawrence Paulson, [Fun With Tilings](https://isa-afp.org/entries/FunWithTilings.html), Archive of Formal Proofs.** Read the entry abstract and metadata only. It records an earlier inductive formalization of tilings and a mutilated-board result. We did not inspect or rerun its full Isabelle proof. This prevents describing either the puzzle or its formal checking as new.
- **Inherited mathematical foundation work.** The [induction/initiality study](ROOT-MATHEMATICAL-INDUCTION-INTEGRATION.md) already establishes a precise generated-domain/universal-property correspondence while retaining the domain-admission and exclusive-priority questions. We do not repeat or re-count it. The current result concerns question-relative presentation kernels and a matched coverage target instead.
- **Philosophical mathematical-explanation comparison.** Search retrieved author-deposited abstracts for [Räz’s Euler study](https://philsci-archive.pitt.edu/18320/) and [Lange’s counterfactual-explanation challenges](https://philsci-archive.pitt.edu/20234/); direct full-text access was rejected. Only their abstract-level scope is credited. No detailed argument is attributed on that basis. The present structural-explanation assessment is our defended interpretation of the checked case, not a Lean theorem of explanatoriness.

Accessed 8 October 2026 local time. External materials remain link-only; no imported originals or replacement editions. The source assessment, matched rival and positive theorem together support the revised next test below.

## 8. Verification and preservation

Run `python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_structure.py` from the repository root. The [final immutable receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-structure-checks/20261007T221307.837907Z/receipt.json) binds five copied modules, fresh compilation with Lean 4.29.1 and source/log hashes. Thirty-two new theorem audits plus 42 inherited core/history/necessity audits give **74 total: 62 empty, 12 standard `propext` only**. The checker rejects holes, warnings, custom axioms and any dependency outside the disclosed allowlist. Standard library dependencies are recorded rather than silently reported as zero. No `Classical.choice`, `Quot.sound` or `sorryAx` appears in the checked theorem inventory.

`decide` proves the fixed finite geometry and count facts inside Lean; it is not an external numerical substitute for the general invariant and equivalence proofs. Finite-board verification does not generalize that particular geometry to all physical arrangements. Intermediate failed/successful runs remain development records and are not counted as separate results. Previous proof receipts and source modules remain unchanged.

[Document and binding checks](EXPLANATORY-STRUCTURE-CHECKS.json) separately verify the integration; [owned shared edits](EXPLANATORY-STRUCTURE-INDEX-EDITS.json) record C30/F22 changes and preserved unrelated entries. Index maintenance does not retroactively validate every cited theory or count as independent research review.

## 9. Integration and the next bridge

The new positive statement is **question-relative minimal answer structure is unique in the relational correspondence sense**. It provides a model for stating, proving and auditing a uniqueness claim. It does not establish that the underlying complete generative structure is uniquely determined by every local explanatory target.

The concrete comparison weakens the proposed route from “all explanation happens within generation” to “every explanation must privilege a chronological generative account.” The color obstruction shows why that inference needs a further bridge. A more promising substantive candidate concerns which distinctions can be **jointly realized and composed**, including what makes a proposed continuation possible or impossible. Calling all relations generative would erase this candidate’s content and is not adopted.

**Next test:** from preservation of fixed answers to preservation of independently specified composition/substitution relations. Compare whether both local and whole-constraint accounts must preserve the same operations and whether that yields a richer uniqueness theorem. The question family and operations must be motivated by the target, not selected solely to force an isomorphism. A rival preserving the target’s compositions without the alleged generative dependence would narrow the conjecture; a theorem showing that an independently necessary composition law forces the common structure would strengthen it. Universal foundation-wide coverage, explanatory direction and ontology remain separate obligations.


## 10. Authorized continuation: composition structure

Ren’s subsequent request for stronger structural uniqueness led to the [contextual-composition study](EXPLANATORY-COMPOSITION-INTEGRATION.md): 36 additional checked theorems establish induced composition, general existence, a canonical common factor and reduced structural isomorphism in a fixed word-language interface. The 32 results and frozen receipt above retain their original scope. The later existence construction discloses `Quot.sound` as well as `propext`; that later dependency does not alter this study’s earlier inventory. The unresolved bridge now concerns justification/recovery of the applicable composition interface, including boundary-sensitive partial joining.
