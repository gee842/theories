# Whole comparison and situated practical restriction: checked correspondence

7 October 2026. AI-authored mathematical investigation for the session target of universal meta-ethics of all intelligence. This round tests the inference **whole-continuation comparison → situated practical comparison**, and the converse proposal to recover a common whole comparison from compatible situated judgments. It establishes representation conditions and genuine structural limitations. It does not prove the ethical warrant of the relation or its practical authority across intelligence.

## Exact target and representation

The [source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean) represents complete continuations at the declared scope by `Whole`. An index identifies a differentiated decision position within the same process; its option domain and realization map identify the continuations compared there. These are analytical presentations of relations within one unfolding, not primitive owners facing an independent environment. The module does not derive their formation, their empirical identification, or the completeness of the represented continuations.

For each index `i`, the independently supplied local binary relation is `Lᵢ(a,b)` and the realization is `rᵢ(a)`. A common relation `Q` is represented faithfully exactly when

`Lᵢ(a,b) ↔ Q(rᵢ(a), rᵢ(b))`.

This contract concerns contextual comparison of two options. It does not represent every pro tanto reason, the content of each supporting ground, endorsement, permission, duty, blame or actual choice. In particular, calling this contract `Descends` neither defines morally justified action nor proves that all morally valid local comparisons must obey it.

The whole relation is an arbitrary binary relation: no numerical total, complete ranking, transitivity, fixed objective or favorable direction is imposed. Its restriction can differ between situations because the available continuations and their grounds differ. Whether a proposed `Q` deserves an ethical interpretation, and why that interpretation has practical force, remain substantive obligations.

## Checked results

Fourteen theorems are kernel checked. Their substantive mathematical groups are:

1. **Exact common-relation existence.** A local family descends from some common whole relation if and only if its judgments agree whenever both ordered realizations match across presentations. The constructive common relation records a local comparison whenever a chart witnesses it. This is an existence theorem for a relation, not for an ethical ordering.
2. **Coverage and uniqueness.** Every extension agrees on each pair co-realized in some chart. If every ordered pair is so represented, all extensions agree everywhere. If a pair is unrepresented, the compatible family has two extensions disagreeing there. This last statement ranges over arbitrary binary relations; additional global conditions, such as a specified transitive order, can constrain otherwise unrepresented comparisons.
3. **Point coverage is insufficient.** Two singleton charts represent both Boolean continuations individually but never compare them. Covering every continuation is weaker than covering every ordered comparison.
4. **Faithful recoding.** When both realizations are preserved, comparison is preserved. This covers duplication, changed indexing and refinement at the specified pairs, provided that the same whole relation remains justified. It does not establish that actual learning or self-modification preserves its grounds, options or correct verdicts. Warranted correction can change them.
5. **A nontrivial obstruction to assembling an order.** Three charts represent `{a,b}`, `{b,c}` and `{c,a}` and locally assert `a<b`, `b<c` and `c<a`. They are compatible, every ordered whole pair is covered, and each local relation is irreflexive and transitive. Nevertheless no common irreflexive transitive relation extends all three. Thus even complete pair coverage and compatible local strict orders are insufficient for a global strict order. The failed property is joint transitivity; no free moral predicate is toggled in this counterexample.
6. **The weak-signature correspondence limit.** Given a strict whole relation and an actual favorable represented pair, both its restriction and an empty practical relation satisfy the independently supplied strictness requirements, while disagreeing on that pair. This shows what the weak signature fails to determine. It is not a substantive refutation of a fuller constitutive proposal whose relevant relationships the signature has omitted.
7. **Ranking does not determine its supporting grounds.** A finite information-loss example assigns supporting entries `[2]` and `[1]` to two alternatives, then `[1]` and `[]`. The sums induce the same strict comparison on every pair, yet the lower alternative has positive supporting entries only in the first presentation. The numbers are toy encodings, not ethical weights or a proposed summation of the whole. Preserving comparison alone cannot establish preservation of every reason or ground.

The first result is structurally distinct from the inherited [reason-transport and ground-coverage proof](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean). That work concerns unary reason claims, warranted seeds and implication closure. This work concerns binary whole-continuation comparisons, realization fibers and pair coverage. Neither result supplies first ethical warrant. These are elementary representation results, not claims of novel mathematics in the wider literature.

## Nondual correspondence and substantive limitations

The index and option domains are not an ontology of independently established agents. Their formation and the scope of their analytical separation remain to explain in the generative account. Whole histories must retain the relationships material to the comparison, including action, undergoing, formation, authority and subsequent consequences where relevant.

That completeness requirement makes compatibility substantive only where actual overlap exists. If every history includes a distinct choosing token and the images of different charts never overlap, compatibility can be vacuous. Constructing a single relation on those disjoint images then establishes no agreement on shared grounds or universal ethical authority. Conversely, dropping the choosing history solely to manufacture overlap may erase relevant grounds. A faithful comparison needs an independently justified correspondence, not a convenient equality.

The relation need not distinguish different grounds that support the same verdict. A proof of preserved comparison therefore cannot itself certify preserved burdens, response modes, standing or legitimate exclusions. These require a richer representation and substantive justification. This is one reason the module is a correspondence audit rather than a definition of adequate intelligence.

The universal inference advanced is precise: **if** whole-grounded ethical comparison is established and **if** a situated representation preserves the relevant whole continuations, the representation cannot introduce a new comparison merely through renaming or recutting. The difficult antecedents are not discharged by the theorem. No conclusion about inevitable recognition, compliance, the exclusive necessity of this vocabulary, or no-assumptions completion follows.

## Validation and dependency record

The separate [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/check_practical.py) copies source bytes into a fresh directory, invokes Lean **4.29.1**, compiles the module, and runs generated `#print axioms` audits for all 31 declared definitions, structures, inductives and theorems. All 14 theorem proofs and all 31 declaration audits pass with empty axiom sets. The scanner rejects proof escapes; it is an additional check, not a replacement for kernel validation. The source imports no other research module, and no finite runtime simulation substitutes for the general proofs.

The [current receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/practical-verification.json) binds the source and checker hashes and confirms unchanged source bytes during checking. The [retained successful run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/practical-verification/20261007T112137.294648Z/verification.json) includes source, checker, compiler commands, compilation output and generated audit source/output. The pinned compiler reports commit `f72c35b3f637c8c6571d353742168ab66cc22c00`.

| Artifact | SHA-256 |
|---|---|
| `WholePracticalRestriction.lean` | `b7036c386f34acdd6fbb2041ce81161b3aa433593e003aa7655391c430e7db87` |
| `check_practical.py` | `5983c5783b54e1af8d87273b9a4e9d2ce7d1d70c07f121e31e684591299275d8` |
| `practical-verification.json` | `fd810ce8d7e8e63678647e3c7bed73238ce7ffe1063b193a24a71ddcc9523b19` |

Earlier failed compilation attempts and intermediate successful versions remain under `practical-verification/`. One compiled intermediate supporting-entry theorem used `propext` and `Quot.sound` through a membership decision procedure and failed this checker's empty-dependency contract. Its log is preserved; using the explicit list-membership constructor removes those dependencies in the final source. This was a proof-engineering change, not a change to the claim. The first checker version retained source but not its failed compiler output; a recorded byte-identical rerun preserves that failure. Attempt notes identify these limitations instead of presenting every saved directory as a completed verification.

No files or receipts belonging to the concurrent `WholeGroundCoverage` / `CutCoverageAudit` investigation were changed. This round's proof checks are distinct from independent philosophical review and empirical identification. Empty dependency reports concern Lean declarations; they do not eliminate the supplied types, relations, correspondence requirements or ethical premises.
