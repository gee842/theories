# Literature map: transformations that alter their own enabling conditions

Research date: 5 October 2026. This is a selective primary-source audit, not an exhaustive review or a novelty search. The existing integrated-evolution `README.md` and relevant `CLAIMS.md` entries were read as reference only. In particular, U01, U04, U05, U16, and U22 already label the accounting and observation results as conditional, established ingredients. No files in `/Users/ren/theories` were changed.

## What the comparison establishes

A theory written in transformations, relations, and observations has strong predecessors. Its useful contribution cannot consist in replacing familiar nouns with symbols. A more discriminating target is to connect **the maintenance of information, authorization, and execution prerequisites** under transformations that alter those prerequisites, and to state which claims survive replacement of their implementation. This is a proposed research target, not a demonstrated gap in all prior literature.

Three distinctions must survive that translation:

1. Structural existence of a route, its physical execution, and its availability to an observation-limited actor are different claims.
2. An institutional permission is a condition for a rule-compliant action. It does not erase the physical possibility of a prohibited action.
3. An abstraction may correctly predict isolated behavior yet discard the interaction needed to predict behavior after composition.

The twelve entries below were selected for the particular constraint or counterexample each contributes. “Transfer” and “limit” are this research session's interpretation unless a paper's result is explicitly identified.

## Twelve core sources

### L01 — Ashby: behavioral structure across material implementations

W. Ross Ashby (1956), *An Introduction to Cybernetics*. [Estate-hosted full text](https://ashby.info/Ashby-Introduction-to-Cybernetics.pdf).

**Established ingredient.** The opening chapters develop transformations and behavioral correspondences without requiring a particular material implementation; the book also develops coupling, partial observation, and regulation. Relevant anchors: §§1/2–1/6 and Parts I and III.

**Transfer and limit.** This is a direct antecedent for making domain words optional interpretations. The proposed program should claim a precise coupling of mechanisms, if it can establish one, rather than a new structural orientation. A mapping between two domains still needs to preserve the property being inferred. Behavioral correspondence does not supply shared ethical purposes.

**Access.** Full text available and opening material inspected; the root research agent additionally inspected §§1/2–1/6. No claim of a complete rereading.

### L02 — Interface automata: environment assumptions are part of composition

Luca de Alfaro and Thomas A. Henzinger (2001), “Interface Automata,” ESEC/FSE, pp. 109–120. [Author-institution record](https://research-explorer.ista.ac.at/record/4622); [full technical version](https://www.csd.uoc.gr/~hy565/docs/pdfs/papers/interface_automata.pdf).

**Established ingredient.** Interfaces distinguish input assumptions and output guarantees. Compatibility is optimistic: some environment can make the components work together. Alternating refinement weakens input assumptions and strengthens output guarantees.

**Transfer and limit.** A subsystem's capacity must record its reliance on the surrounding system. “Works in some environment” differs from “survives every allowed disturbance.” The proposed core must declare those quantifiers before comparing capacities or replacing components. Institutional permission, resource scarcity, and representation revision need explicit encodings; interface compatibility alone does not establish them.

**Access.** Full technical PDF, especially abstract and introduction, inspected. Its pagination differs from the published conference version.

### L03 — Open Petri nets: endpoint summaries lose interaction

John C. Baez and Jade Master (2020; arXiv revision 2022), “Open Petri Nets,” *Mathematical Structures in Computer Science* 30, 314–341. [Paper and version record](https://arxiv.org/abs/1808.05415); [full HTML](https://arxiv.org/html/1808.05415v6).

**Established ingredient.** Nets compose by identifying output and input places. Their process semantics is compositional. Theorem 23 and its following counterexample show that endpoint reachability semantics is only lax: relational composition of the separate summaries can be strictly smaller than reachability in the composite.

**Decisive example.** Tokens can travel from component P to Q, return to P, and reenter Q. A one-pass endpoint relation loses that interaction. The paper gives a composite with relation `{(n,n)}` whose separately composed reachability relations contain only `{(0,0)}`.

**Transfer and limit.** A mere set or count of attainable endpoints is insufficient for exact modular capacity comparison. Preserve interaction protocols, or prove a restricted interface makes a summary adequate. Token multiplicity supplies consumable quantities; catalysts, permissions, and observations require additional distinctions.

**Access.** Full HTML inspected, especially §§3–6, Theorems 17, 23, 24 and the strict-inclusion counterexample. This distinction is stronger than the abstract alone suggests.

### L04 — Autocatalytic sets: prerequisite closure differs from actual maintenance

Wim Hordijk and Mike Steel (2012), “Autocatalytic sets extended: Dynamics, inhibition, and a generalization,” *Journal of Systems Chemistry* 3:5. [Open full text](https://link.springer.com/article/10.1186/1759-2208-3-5).

**Established ingredient.** RAF structure separates reactions, catalytic relations, and a supplied food set. The paper adds simulations of molecular flow, treats inhibition, and generalizes the structural algorithm beyond chemistry. It explicitly distinguishes prior graph-theoretic analysis from dynamics.

**Transfer and limit.** This is a close precedent for activities producing each other's prerequisites. A cycle of enabling relations is not a quantitative survival guarantee. In the simulated examples, food is automatically replenished to a minimum concentration; that external support cannot be omitted when importing the result. A supplied reaction universe and kinetic assumptions are also not unrestricted creation of new possibilities.

**Access.** Full text inspected, especially Background, Part I: Dynamics, food replenishment, and spontaneous seeding of subRAFs. No claim that its structural RAF condition alone proves indefinite persistence under finite support.

### L05 — Partial-observation games: information states require objective-specific memory

Krishnendu Chatterjee and Laurent Doyen (2012; preprint 2011), “Partial-Observation Stochastic Games: How to Win when Belief Fails,” LICS. [Author preprint](https://arxiv.org/abs/1107.2141); [full HTML](https://arxiv.org/html/1107.2141v1).

**Established ingredient.** In finite stochastic games, pure strategies based only on current belief support can be insufficient for positive or almost-sure reachability, even when the opponent has perfect observation. The paper distinguishes observation structure, randomization, and memory requirements.

**Transfer and limit.** “Same information gives the same response law” is a constraint on admissible policies, not a theorem that every current information summary is sufficient. The proposed finite-horizon sure-winning recursion can be valid under its own assumptions without extending to every stochastic reachability problem. Keep sure, almost-sure, positive-probability, and expected-value objectives separate.

**Access.** Primary abstract and full HTML retrieved; the result stated above is explicitly in the abstract. This audit does not reproduce its complexity proofs.

### L06 — Unawareness: changing expressiveness is not ordinary uncertainty

Aviad Heifetz, Martin Meier, and Burkhard C. Schipper (2006), “Interactive Unawareness,” *Journal of Economic Theory* 130(1), 78–94. [Author-hosted working paper](https://faculty.econ.ucdavis.edu/faculty/schipper/unaw.pdf); [publication record](https://bse.eu/research/publications/interactive-unawareness).

**Established ingredient.** A lattice of state spaces with projections represents different expressive powers. An agent's possibility set can lie in a less expressive space. Event structure differs from an ordinary Boolean algebra over one fixed observational partition.

**Transfer and limit.** Refining observation over a fixed language and gaining a new representable distinction should be separated. The full lattice and its coherence conditions remain specified by the analyst. Thus this framework represents agent-relative unawareness; it does not prove generation of concepts outside every supplied metalanguage. A variable `O_t` needs comparable precision about what changes and how old descriptions embed or project.

**Access.** Full author PDF inspected, especially §2 and its description of the lattice and projections. Working-paper version and final article are distinguished.

### L07 — Institutional grammar: rules are not just physical constraints

Sue E. S. Crawford and Elinor Ostrom (1995), “A Grammar of Institutions,” *American Political Science Review* 89(3), 582–600. [Publisher abstract and bibliographic record](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/grammar-of-institutions/7D37CD3BC5ED2D9FD57D2EE292958F47).

**Established ingredient.** The grammar distinguishes rules, norms, and shared strategies, alongside physical conditions, and treats institutional regularities as constituted and reconstituted through interaction.

**Transfer and limit.** Authorization is not interchangeable with energetic availability. A faithful structural mapping should record who has standing, which procedure changes a rule, how compliance is implemented, and what prohibited actions remain physically possible. The grammar helps distinguish these questions; it is not by itself a dynamical law predicting how institutions revise themselves or a justification of their legitimacy.

**Access.** Publisher abstract and publication metadata inspected. A discovered full-PDF mirror failed to open. Detailed syntax and theorem-level claims are therefore not attributed on the basis of this session. The publisher's 2013 online date is not the article's original 1995 publication date.

### L08 — Price: selection is a decomposition, not an ethical direction

George R. Price (1970), “Selection and Covariance,” *Nature* 227, 520–521. [Primary scan](https://sites.santafe.edu/~altenber/LIBRARY/REPRINTS/Price_selection_Nature.1970.pdf). Related extension: Price (1972), “Extension of covariance selection mathematics,” *Annals of Human Genetics* 35(4), 485–490. [Publisher record](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1957.tb01874.x).

**Established ingredient.** The 1970 derivation separates change associated with differential contribution from change within the transmitted material; equation (4) retains the latter term. The paper expressly considers non-genetical interpretations.

**Transfer and limit.** A selection mapping needs a declared population, weights, trait, and parent–descendant or contribution relation. A covariance identity does not determine the mechanisms producing those values, guarantee renewal of support, or establish desirability of the selected trait. Selection over alternative rules and destruction of their shared support can therefore be separately modeled without contradicting the identity.

**Access.** The two-page 1970 scan was inspected; OCR is poor, so use the scan for exact notation. The 1972 scan was retrieved once but a repeat request timed out; detailed claims here rely on 1970. The 1972 DOI contains “1957” although the publisher verifies publication in 1972.

### L09 — Niche construction: selection can modify its resource environment

Kevin N. Laland, F. John Odling-Smee, and Marcus W. Feldman (1999), “Evolutionary consequences of niche construction and their implications for ecology,” *PNAS* 96(18), 10242–10247. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC17873/).

**Established ingredient.** A two-locus population-genetic model couples resource modification to selection, with independent resource renewal and depletion. Its analysis demonstrates changed equilibria and evolutionary dynamics under stated parameterizations.

**Transfer and limit.** Feedback from selected activity to future selective conditions is already an explicit mathematical subject. This source is particularly close to “transformations alter their own conditions of possibility.” Its supplied traits, dynamics, and environmental variable do not settle institutional authorization, open-ended representation change, or general cross-domain equivalence. The proposed program must add a discriminating theorem or predictive comparison beyond the feedback motif.

**Access.** Full article text was available in the search index, including abstract and model-discussion passages; direct opening encountered the site's browser check. Accordingly, no uninspected equation or theorem number is used here.

### L10 — Reflective rewriting: rules can be represented and transformed internally

Manuel Clavel (1998), “Reflection in General Logics, Rewriting Logic, and Maude.” [Publisher record and abstract](https://www.sciencedirect.com/science/article/pii/S1571066105825538). Related primary research: Clavel and Meseguer, “Reflection and strategies in rewriting logic.” [Research-group abstract](https://maude.cs.illinois.edu/papers/abstract/tcs4009.html).

**Established ingredient.** This work gives axiomatic notions of reflective logic, represents object-level theories at a metalevel, and establishes reflection for rewriting logic. The related paper develops internal strategy languages and correctness arguments.

**Transfer and limit.** Endogenous rule representations need not require a new logical foundation: a state can contain encoded rules and programs that edit them. But internal reflection does not eliminate the semantics in which those encodings and edits are interpreted. Distinguish change of an encoded rule from change beyond every specified metatheory. The costs and permission to perform reflection remain additional modeling choices.

**Access.** Primary publisher/research-group abstracts and the author's publication list inspected; full proofs not reviewed. Bibliographic pagination differs between the publisher record and author list, so page numbers are deliberately omitted pending reconciliation.

### L11 — Self-modifying agents: preservation results have a fixed evaluative reference

Tom Everitt, Daniel Filan, Mayank Daswani, and Marcus Hutter (2016), “Self-Modification of Policy and Utility Function in Rational Agents.” [Author-hosted full paper](https://www.hutter1.net/publ/selfmod.pdf); [version record](https://arxiv.org/abs/1605.03142).

**Established ingredient.** Theorem 16 proves an on-policy preservation result for initially optimal agents under modification-independent belief and initial utility, with value functions that anticipate self-modification. The paper explicitly notes limits concerning correction, value learning, and exploration.

**Transfer and limit.** Recursive modification can be analyzed exactly, but “safe” here is relative to the specified evaluation. Preserving that criterion may obstruct correction of an erroneous one. It does not establish agreement with human values, legitimate authority, off-policy behavior, or realistic finite-cost access to arbitrary modifications. The model explicitly overestimates modification availability.

**Access.** Full PDF inspected at model setup, Theorem 16, and its subsequent qualifications. This is a formal conditional result, not evidence that deployed self-modifying systems satisfy its assumptions.

### L12 — Corrigibility: preserving correction mechanisms is already a design target

Nate Soares, Benja Fallenstein, Eliezer Yudkowsky, and Stuart Armstrong (2015), “Corrigibility,” AAAI Workshop on AI and Ethics. [Primary full paper](https://intelligence.org/files/Corrigibility.pdf).

**Established ingredient.** The paper distinguishes obeying a shutdown signal, avoiding incentives to influence that signal, maintaining safety mechanisms, and preserving correctability through self-modification or subsystem creation. It studies failures of candidate utility constructions and states that the proposals do not establish all the desiderata.

**Transfer and limit.** An available correction action, an incentive to cooperate with it, and maintained ability to invoke it are separate objects. This supports modeling the correction process itself. The paper's programmer-centered authority does not answer broader questions of legitimate social control or value disagreement. A renewal-and-revision framework should not be described as an alignment solution simply because it preserves a correction route.

**Access.** Full paper inspected, particularly abstract, §1.1, and manipulation examples. Its open-problem statement describes that paper's result, not a claim about the entire field in 2026.

## Two additional anchors with narrower access

- **Viability theory.** Aubin, Bayen, and Saint-Pierre (2011), *Viability Theory: New Directions*. [Publisher page](https://link.springer.com/book/10.1007/978-3-642-16684-6). The accessible description and contents establish a directly relevant program of dynamics constrained to remain in acceptable sets, including renewable-resource management. The full book was not accessed; no particular tangency theorem or its assumptions were checked here. Use this as conceptual provenance, and prove the finite model's own recursion directly.
- **Comparison of information.** Blackwell (1953), “Equivalent Comparisons of Experiments,” *Annals of Mathematical Statistics* 24(2), 265–272, [DOI](https://doi.org/10.1214/aoms/1177729032). Publisher-page and PDF opening failed; bibliographic and abstract records were found. This is a relevant lead for decision-relative information comparison, not newly reviewed evidence for a theorem statement in this audit.

## Domain mappings: what must be preserved

The following is a proposed operational test, not a conclusion imported from the papers.

| Interpretation | Structural data needed | Invalid shortcut |
|---|---|---|
| Chemical or material renewal | Quantities, reaction prerequisites, kinetics, access to external inputs | Catalytic closure therefore indefinite operation |
| Cultural or institutional selection | Transmission/contribution links and weights; behavior affecting shared support | Popularity therefore viability or legitimacy |
| Human revision | Evidence access, candidate generation, standing, decision procedure, enactment route, and their costs | A formally admissible proposal therefore an executable correction |
| AI correction | Observation-dependent policies, physical intervention channel, permission/authority model, incentives, update semantics | Obedience now therefore durable correctability |
| Continued becoming (生生) | A declared family of protected capacities and transformations, including succession/replacement tests | Persistence, novelty, or a larger option set therefore ethical improvement |

For implementation equivalence, first fix the claim being transferred. A resource bound may require preservation of cumulative cost and inflow; a correction guarantee also requires preservation of observations, action control, and branching structure. An equivalence that retains only output traces or endpoint reachability may be too weak. Whether a specific abstraction is sufficient is a mathematical obligation, not settled by giving it a domain-neutral name.

## Most useful next research target

Construct a small finite pair of modules: an operating process and a process that can inspect, authorize, and enact a rule change. Give the latter a maintained resource and an observation channel. Compare an interface-preserving replacement with a replacement that preserves current output and endpoint reachability but destroys an interaction needed for correction. Prove the exact finite-horizon correction condition and exhibit the failed replacement.

This target joins the composition warning in L03, information limits in L05, and authority/execution distinction in L07 without pretending to solve unrestricted novelty. A positive result would establish a conditional abstraction criterion. An empirical extension would then test whether measured prerequisites actually predict intervention outcomes; that would be a separate evidential step.

## Claims this audit does not support

- That the general structural program or its ingredients are mathematically new.
- That any of these frameworks alone represents unrestricted concept creation.
- That a supplied evolving grammar escapes an analyst-specified semantic universe.
- That accounting and observation identities amount to a universal social law.
- That continued operation, increased options, or successful rule preservation is ethically good.
- That maintained correction capacity resolves disagreement over legitimate correction or solves alignment.

