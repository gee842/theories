# Focused sources: higher-order interpretation and full domains

7 October 2026. AI-authored source assessment for the conditional higher-order reconstruction. Read with the [independent review](ROOT-MATHEMATICAL-HIGHER-ORDER-REVIEW.md). This note records definitions and source scope, not a newly checked completeness theorem for higher-order logic. No source bytes or empirical evidence were imported.

## 1. Standard and general interpretation in finite type theory

**Leon Henkin, “Completeness in the Theory of Types,” *Journal of Symbolic Logic* 15(2), 1950, pp. 81–91.** [Publication record](https://www.jstor.org/stable/2266967); [retrieved reproduction](https://aaronxyliu.github.io/download/PL/Henkin.pdf). This reviewer read printed pp. 81–84 in the reproduced primary article; the parent had also read that opening scope in the preceding discussion. The whole proof was not reviewed or newly formalized here.

Henkin distinguishes full function domains from selected domains. His standard interpretation uses every function between the relevant type domains. A general model must support the interpretation of the language, including abstraction; an arbitrary restricted collection of functions need not do so. The warning about closure appears already in p. 81 n. 5 and in the frame/general-model distinction on p. 84.

**Decision:** full-function transport in the new package should expose those domains and the maps covering them. A selected-domain variant requires its own closure and interpretation contract before being called a Henkin model. Henkin’s proof-system completeness result is not the theorem being claimed by this repository’s semantic correspondence.

## 2. Predicate quantifier ranges

**Jouko Väänänen, “Second-Order Logic and Foundations of Mathematics,” *Bulletin of Symbolic Logic* 7(4), 2001, pp. 504–520.** [Publisher record](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/secondorder-logic-and-foundations-of-mathematics/7A7D61BB970EA86FF9562C303F005ED8); [author-uploaded manuscript](https://www.researchgate.net/publication/220366329_Second-Order_Logic_and_Foundations_of_Mathematics). This reviewer read the opening semantic definitions on manuscript pp. 1–2, dated 21 August 2001. The [author-hosted published PDF](https://www.mv.helsinki.fi/home/jvaanane/secondorder.pdf) did not load in this review. Upload/online-display dates are not the article’s publication year.

The opening defines second-order interpretation through a first-order structure and an additional predicate domain. Predicate quantifiers range over that domain. Full models use every subset; Henkin models satisfy the stated deductive requirements. These definitions distinguish the semantic contract from the act of quantifying in a formal language.

**Decision:** replacing predicates by finite-subset ideals preserves full semantics only if the representation reaches every predicate and the binder ranges over all corresponding ideals. Restricting it to named, computable or principal ideals changes the question. The article’s wider philosophical claims and later proofs were not needed or assessed in this focused reading.

## 3. What the sources contribute to the new result

The source comparisons fix the interpretation of “full” and prevent a change of predicate range from being hidden by similar syntax. The local result must still be established by its own Lean definitions, binder cases and checked transport proof. Source authority does not replace those checks.

The [earlier completion package](COMPLETION-WARRANT-LEAN-INTEGRATION.md) already represents all predicates on a supplied carrier by ideals of finite subsets. The higher-order continuation must additionally show that this correspondence respects interpreted application, equality where present, and arbitrary nesting of the relevant binders. For finite simple types, full function-space transport and its connection to that concrete completion representation require their own checked statements.

These are conditional semantic questions within the theory’s relational account. Neither source is used to assume a separate mathematical realm or to prove that generative constitution is impossible. Nor does calling an interpretation full establish that the repository’s root uniquely grounds its entire domain. The present round can complete the conditional correspondence without claiming that stronger conclusion.
