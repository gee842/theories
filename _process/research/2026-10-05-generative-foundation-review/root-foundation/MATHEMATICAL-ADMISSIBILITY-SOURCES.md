# Directed completion: sources, mathematical role and admission scope

6 October 2026. AI-authored source and scope note under the [shared nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). Named transition: **finite generative approximations → admissible ideal objects → uniquely extended continuous operations**. This is a conditional domain-theoretic articulation of mathematical completion, not a new theorem in domain theory, a physical realization result or a proof that the root uniquely determines every mathematical truth.

## Directly inspected primary sources

**Samson Abramsky and Achim Jung, “Domain Theory,” *Handbook of Logic in Computer Science*, vol. 3 (1994), pp. 1–168.** Inspected the [author-hosted corrected and expanded edition](https://www.cs.ox.ac.uk/people/samson.abramsky/handbook.pdf), which preserves theorem numbering. References below use that edition's printed pages, also its PDF page numbers. It has 167 PDF pages; it should not be described as a byte-identical copy of the published chapter.

| Location | Directly checked content |
|---|---|
| §2.1.4, Definition 2.1.8, p. 13 | Directed sets are nonempty; ideals are directed lower sets. |
| §2.1.5–2.1.6, Definitions 2.1.13/17, pp. 14–15 | Directed completeness and Scott continuity. |
| §2.2.2–2.2.3, Propositions 2.2.4/7, pp. 18–19 | Compact bases and algebraic reconstruction. |
| §2.2.6, Propositions 2.2.22/24/25 and Corollary 2.2.26, pp. 26–28 | Ideal completion, extension from a basis, reconstruction of a domain and determination of continuous maps by basis values. |

Proposition 2.2.24 is a weak extension property for general abstract bases; its reflexive-poset specialization gives equality on embedded generators. Principal generation then supplies uniqueness. The source's distinction between a general abstract basis and a poset must be preserved. No effective enumeration of all ideals is asserted.

**Dana Scott, “Semilattices, Domains, and Computability,” CCA 2009, p. 17.** Directly read the entire [one-page primary invited-talk abstract](https://drops.dagstuhl.de/storage/01oasics/oasics-vol011-cca2009/OASIcs.CCA.2009.2252/OASIcs.CCA.2009.2252.pdf). It explicitly identifies an algebraic lattice with the ideal completion of its compact-element semilattice, while treating that identification as established background. It is a concise primary genealogy source, not a detailed proof of the unrestricted poset theorem or the present philosophical interpretation. [Publisher record](https://doi.org/10.4230/OASIcs.CCA.2009.2252). Scott's 1970 *Outline* was located bibliographically through Oxford, but its substantive text was not inspected and is not a proof source here.

**Henning Urbat and Thorsten Wißmann, “Well-Founded Coalgebras Meet Kőnig's Lemma,” CSL 2026, Article 24.** Directly inspected §1, pp. 24:1–24:3 of the [publisher-hosted primary paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/LIPIcs.CSL.2026.24/LIPIcs.CSL.2026.24.pdf). It recalls the classical finitely branching tree lemma and distinguishes that result from the authors' broader coalgebraic generalization. We use only the classical lemma, not the new generalization. The source also flags its connection to selection principles in foundations. The application below is therefore stated in ordinary classical set mathematics, without a premise-free or effective path-selection claim.

The papers were read selectively at these locations; no exhaustive review is claimed. External originals remain link-only references. No prior scientific run, local source bytes or shared index was changed for this source note.

## What the proposed completion must say precisely

Fix a poset \(P\) whose order represents the selected approximation relation. Use **nonempty** directed lower sets as ideals. If the empty ideal is admitted instead, a new bottom is introduced and the extension contract changes; that convention must not drift between examples.

The construction makes all ideals available and orders them by inclusion. Its original points are principal ideals \(\downarrow p\). The compact elements are exactly those principals. Thus the admissibility proposal does substantive work: it identifies a completed element through a coherent directed family of finite approximants, while requiring every such admitted family to have a completion. The word “finite” here names the compact-approximation role; an arbitrary supplied poset element is not thereby a physically finite structure or an effectively describable object.

For a monotone map \(f:P\to D\), with \(D\) a dcpo, the intended extension is

\[
\widehat f(I)=\sup_{p\in I}f(p).
\]

Its continuity and agreement on principals follow from the directed-union calculation. Every ideal is the directed union of its principals, so any continuous extension agreeing there has the same value. This supplies a role-relative reason for the operation's value: once its finite action and directed-continuity requirement are fixed, no independent choice at the ideal object remains.

The corresponding uniqueness of the completed carrier needs the full role. Require an order-faithful identification of \(P\) with a compact basis and require every element to be the directed supremum of its approximants from that basis. Merely embedding the original points as *some* compact elements permits additional independent structure and does not establish uniqueness. These requirements define a category of admissible completions; uniqueness within it is not an argument that no other notion of mathematical completion is legitimate.

Continuity is also essential. On \(\mathbb N\cup\{\infty\}\), the constant-zero map to \(\{0<1\}\) and the map that is zero on finite numbers but one at \(\infty\) agree on all finite numbers. The latter is monotone but does not preserve their directed supremum. Agreement on finite approximants alone therefore does not fix arbitrary operations at ideal elements.

## The examples expose the strength of admission

For finite words ordered by prefix, an ideal cannot contain incompatible prefixes. Its union is either a finite word, with a principal ideal, or a uniquely determined infinite word. Conversely every such word determines its ideal of finite prefixes. This realizes finite and infinite words as one approximation structure. It does not mean that one machine finishes an infinite sequence of actions.

For finite subsets of a set \(U\), ordered by inclusion and including the empty finite subset, an ideal \(I\) is determined by \(V=\bigcup I\). Directedness and downward closure imply that it consists of exactly the finite subsets of \(V\). Conversely every subset \(V\subseteq U\) determines such an ideal. Accordingly, **admitting all ideals yields all subsets**. It does not derive the availability of every subset from a merely finite generative procedure. The construction and its quantification over all ideals occur in the stated ambient set theory.

This makes the directed-completeness premise testable. Finite subset formation and finite union do not already force that enlarged domain. For example, among subsets of \(\mathbb N\), the increasing finite initial sets have union \(\mathbb N\), which is absent from the finite-subset carrier. Requiring that particular supremum adds it. Requiring every directed family adds the corresponding full range, including families that are not supplied by one chosen executable enumeration. A countable basis need not make its ideal completion countable or make every ideal computable.

There is a narrow and defensible sense of conservativity: the principal embedding preserves and reflects the original order, and compact positive information appearing at a directed supremum already occurs at an approximating stage. These statements must not become “every finitely written statement is unchanged.” A short formula can quantify over the enlarged carrier. Nor does the free ideal embedding necessarily preserve a directed supremum already present in \(P\) when its old supremum is now required to count as compact. Existing infinitary relations require their own preservation contract.

## Compatible action prefixes and a coherent history

A useful supporting application uses histories rather than undifferentiated endpoint labels. Fix an infinite action word. Assume a finite nonempty set of admissible initial configurations and finitely many successors for each required action from each configuration. Suppose every finite prefix has a feasible history from that initial set, with every prefix obligation included in feasibility.

Form the tree of those finite histories, adding a common root above the initial configurations. It has arbitrarily deep nodes and finite branching. Kőnig's lemma provides one infinite branch. That branch is a coherent represented history realizing the fixed action word and all modeled finite-prefix conditions. The conclusion is stronger than merely choosing unrelated witnesses for each length, but depends on their being organized in this finitely branching tree. It does not ensure effective identification of the branch or an actually executed infinite physical history. Limit-only obligations are not proved by checking only finite prefixes.

The finite-initial condition cannot simply be omitted. Let an initial state be an arbitrary finite budget \(n\), and let each occurrence of one action decrease it by one, with no action possible at zero. Every finite action word is feasible for some initial budget. No single initial budget supports the infinite word. The added root now has infinitely many children, and the inference fails. This is a conditional mathematical counterexample, not a new experiment or a universal resource law.

## Relation to the existing branch and the stronger claim

The [closure-resolution study](MATHEMATICS-CLOSURE-RESOLUTION.md) already distinguishes finite-character closure from stronger infinitary closure and separates finite subset generation from fullness. The [immanent identity study](../../../../theories/becoming/chapters/IMMANENT-MATHEMATICAL-IDENTITY.md) already exhibits the compatible \(\mathbb N\)-profile corresponding to an extra infinite point and requires a realization argument for inverse limits. The [model-admissibility study](MATHEMATICS-MODEL-ADMISSIBILITY.md) separately treats consistency, truth profiles and structural selection. Ideal completion advances none of those by erasing their boundaries. It instead supplies a positive, precisely specified admission role with a uniqueness and operation-extension result.

The philosophical argument is therefore conditional and substantive: if mathematical objects in this domain are to be constituted by these coherent finite approximations, if all their directed totalities are admitted, and if admissible operations respect those limits, the carrier and operations are fixed up to the specified structural equivalence. Defending those *if*s through the generative account remains necessary. Their being locally supplied does not put them outside generative reality; their being called immanent does not establish their necessity. The live frontier is whether this role fits the intended subject and whether the root warrants the selected closure, rather than whether a completion theorem alone confers universal metaphysical priority.
