# Full admission: focused primary-source assessment

7 October 2026. AI-authored source note supporting the [independent admission review](ROOT-MATHEMATICAL-ADMISSION-REVIEW.md). This round adds one primary reading, limited to the source's own account of mathematical unfolding and its foundational commitments. It is not a source survey or a substitute for the new Lean checks.

## Primary reading and exact scope

Solomon Feferman, **“Predicativity.”** The author's [publication list](https://math.stanford.edu/~feferman/papers/papers.html) identifies publication in *The Oxford Handbook of Philosophy of Mathematics and Logic*, edited by Stewart Shapiro, Oxford University Press, 2005, pp. 590–624, and warns that posted versions can differ from publication. The text consulted was the [author-hosted 35-page draft](https://math.stanford.edu/~feferman/papers/predicativity.pdf), principally PDF pp. 24–29, “Predicativity as unfolding” and “What is predicativity? (Summary).” Opening and other search-returned passages were inspected for orientation; neither a complete reading nor collation against the published edition is claimed. No source bytes were imported or replaced.

**Source content used (paraphrase).** Feferman treats schematic unfolding as open to meaningful new substitutions, with operations admitted through their introduction and established definedness. He explicitly identifies the logical operations taken for granted and distinguishes unfoldings with and without a join operation. His summary treats predicativity as relative to accepted starting concepts, rather than identifying it simply with finiteness. He does not conclude that only predicative mathematics is justified; stronger infinitary closure conceptions require examination of where and how they are used. [Author draft, PDF pp. 24–29](https://math.stanford.edu/~feferman/papers/predicativity.pdf).

## Decision for this study

**Our inference:** the useful comparison is the form of the admission question: what follows from accepting an independently articulated starting conception, and which operations, totalities and quantifier ranges enter in answering it? Calling a closure “generative” or “open-ended” is insufficient to specify that range. This does not make Feferman's particular starting concepts or restrictions mandatory for Ren's theory.

In the present Lean module, `DirectedUnionClosed` explicitly quantifies over every ambient directed predicate family. This fact comes from the reviewed source code, not from Feferman. Its equivalence with fullness is proved in that module. The philosophical task is to warrant that full range, or explain a principled revision of the target, while preserving the successful representation results.

We do not import the article's proof-theoretic strength results as new checked repository theorems, equate finite/cofinite predicates with Feferman's predicative systems, or claim that predicative alternatives preserve the independently fixed full higher-order target. The same-content structural rival in the review accepts that full target. Its unresolved disagreement concerns the explanation of admission.

## Preserved genealogy

The distinction between selected/general and full higher-order domains remains supported by the already read primary sources in [the previous source note](ROOT-MATHEMATICAL-HIGHER-ORDER-SOURCES.md); those readings were not repeated or counted as new evidence. The repository's own prior P2/P3 separation is preserved in [the closure resolution](MATHEMATICS-CLOSURE-RESOLUTION.md). The new checked admission characterization and recursive graph interpretation must receive their actual formal scope rather than a novelty claim borrowed from this source comparison.
