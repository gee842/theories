# Uniform indexed assembly: primary-source assessment

7 October 2026. AI-authored focused source note for the [assembly review](ROOT-MATHEMATICAL-ASSEMBLY-REVIEW.md). One primary research text was newly inspected; no source bytes were imported or replaced.

## New primary reading

Solomon Feferman and Thomas Strahm, **“The unfolding of non-finitist arithmetic.”** The [author's publication list](https://math.stanford.edu/~feferman/papers/papers.html) records *Annals of Pure and Applied Logic* 104 (2000), pp. 75–96, and cautions that posted versions can differ. We read the [author-hosted 24-page text](https://math.stanford.edu/~feferman/papers/unfolding.pdf), introduction pp. 1–2 and §4 pp. 7–9, inspecting the adjacent syntax/axiom descriptions for context. We did not review the whole proof-theoretic analysis or collate the draft with the published version. The publication-list link initially resolved to a duplicated `papers/papers/` path and failed; the author-hosted PDF above was successfully read.

**Content used (paraphrase).** The introduction asks which further operations and principles acceptance of a starting schematic system warrants, while reserving additional foundations for further justification. Section 4 specifies predicate-forming operations and their axioms. Join forms an indexed predicate from a predicate-valued operation, with explicit definedness at every index as its premise. Extensional identity and logical operations are stated separately. Predicate variables are not quantified over in the object's formulas; the partial-function sorts are likewise not full quantified domains. The intermediate unfolding omits the Join axiom. [Author text, pp. 1–2 and 7–9](https://math.stanford.edu/~feferman/papers/unfolding.pdf).

## What this contributes

Our comparison concerns the **admission contract**. Specifying a uniform family-forming operation, establishing its definedness and admitting arbitrary arguments for it are distinguishable tasks. Join retains the index; our proposed projection forgets it. The paper's formulation is therefore a comparison that makes the necessary inputs explicit, not the same theorem as our indexed union.

We do not borrow its proof-theoretic equivalences as newly Lean-checked results, infer a ceiling on Ren's root, or treat this unfolding as an interpretation of the independently fixed full higher-order target. We also do not adopt its stipulated ordering of basic types as a metaphysical division. It provides a worked account of how formation and range commitments can be recorded, not a verdict on universal admission.

## Reused genealogy

The [previous admission source note](ROOT-MATHEMATICAL-ADMISSION-SOURCES.md) read Feferman's later “Predicativity” discussion of unfolding and relative foundational commitments. That earlier reading motivated this focused examination of the original joint research paper; it is not counted again as independent evidence. The repository's earlier [closure resolution P2](MATHEMATICS-CLOSURE-RESOLUTION.md#proposition-p2--which-union-closure-yields-all-subsets) already states the unrestricted increasing-sequence/fullness distinction as a hand argument. The new formal round must identify its checked migration and its additional argument about independently admitted families without claiming that distinction as a new discovery.
