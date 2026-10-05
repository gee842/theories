# How to prove and validate the proposed theory

5 October 2026. Research memo responding to the proposal that current assumptions could be removed, derived, or recognized as universal invariants. Reference files were not altered. Proposed targets below are not claimed as new results or completed proofs.

**That proposal is legitimate. The existence of assumptions does not establish that a theory cannot become fundamental. The next task is to show which assumptions can be discharged, which invariances follow, and why the resulting structure applies to the intended phenomena.** “Conditional” describes the present logical form; it is not a ceiling on future generality.

## What removing an assumption can accomplish

Suppose the current theorem is A ∧ B ⇒ T. There are several genuinely different advances:

| Advance | Proof obligation | What changes |
|---|---|---|
| Remove a redundant premise | Prove B ⇒ T without A | The theorem applies to a larger class |
| Derive a premise | Prove B ⇒ A, then B ⇒ T | A ceases to be an independent assumption |
| Replace several premises by a deeper principle | Prove G ⇒ A ∧ B | Explanatory compression is possible; G's meaning and applicability remain to be established |
| Weaken the premise or conclusion | Prove A′ ∧ B ⇒ T′, stating the ordering and approximation error | A wider, possibly approximate law replaces the old one |
| Characterize necessity | Prove T ⇒ A under the same surrounding scope | A becomes a necessary condition for the stated result, not necessarily a condition satisfied everywhere |
| Promote A to a candidate universal law | State A for all intended real cases and derive testable consequences | A has acquired empirical scope; mathematical derivation alone has not established that scope |

Changing a definition so that every admitted object satisfies A is also legitimate, but establishes membership in that defined class. It does not demonstrate that every intended real object belongs. Likewise, proving G ⇒ A does not require G to be assumption-free; it requires a clear account of whether G is mathematical, constitutive, empirical, or normative. The aim is a short, powerful basis, not a count of zero premises.

For each apparently indispensable premise, try to construct a model satisfying the others while violating the conclusion. A genuine countermodel shows that the premise cannot simply be dropped from that statement. It may instead motivate a deeper law excluding the countermodel, a new conclusion, or a different interpretation. Conversely, failing to find a countermodel is not a proof of redundancy.

## “Invariant” needs an object and an allowed transformation

Write a claim in the form I(g·M)=I(M), or a commuting equation comparing two procedures, and specify the domain of M and the transformations g. State whether this is an exact equality, a bound, or an equivalence for named queries. A change of coordinates, a change of policy, and replacement of the physical mechanism are different operations.

| Proposed invariance | What must be fixed | What would defeat the claim |
|---|---|---|
| Representation independence | Renamings or coordinate changes and their transformation rule | Two admissible representations disagree on the same declared quantity |
| Conservation through time | Evolution law, conserved quantity, and relevant exchanges | An allowed trajectory changes the quantity after the registered exchanges are accounted for |
| Controlled persistence | Disturbances, information, feasible controllers, and protected region | An allowed disturbance defeats every admissible controller from a claimed maintainable state |
| Causal mechanism stability | Which interventions may change which mechanisms | An admitted intervention changes a mechanism asserted to remain fixed |
| Abstraction preservation | Projection, actions/adapters, observation interface, and preserved queries | A merged pair or translated policy produces different retained outcomes |
| Universality across domains | Measurement bridge, model class, allowed parameter substitutions | A target satisfies the independently checked admission conditions but violates the predicted relation |
| Stability under theory extension | Allowed additions and interpretation of old claims | A permitted extension changes a previously guaranteed answer |

The transformation class is part of the content, not an evasive exception. Here is a direct mathematical reason. If an allowed transformation can send any state to any other, every scalar invariant under all those transformations must be constant: for arbitrary x,y choose g with g·x=y and obtain I(y)=I(x). This does not rule out informative invariants under structured transformations. Relabeling a graph, for example, need not change its connectivity, although arbitrary edge deletion can. Nor does covariance of an equation require each individual solution or every measurable quantity to remain unchanged.

For a predicate rather than a scalar, the analogous point is simple: if admitted models include both a case satisfying P and a case violating P, permitting unrestricted replacement between them precludes preservation of P. Thus “all transformations” must mean all transformations of a declared relevant kind, or else establish why the apparent countertransformations are impossible. A transformation set can itself be derived from a deeper principle; that would strengthen, rather than eliminate, this obligation.

## Five different parts of a whole-theory case

| Layer | What an adequate result looks like | What it does not establish by itself |
|---|---|---|
| Definitional and representational | Precise primitives; explicit interpretation; constructive encoding and preservation for every member of the stated class | That the class exhausts reality, or that an encoding selects the world's actual laws |
| Conditional mathematical | Axioms are jointly satisfiable; desired consequences are derived; assumptions and limiting cases are exposed | That a real target satisfies those axioms |
| Characterization and uniqueness | Necessary and sufficient conditions; where possible, uniqueness up to a specified equivalence | That the characterized property is universally instantiated, or that mathematical uniqueness is ontological uniqueness |
| Empirical invariant law | Independently operationalized quantities obey a restrictive relation across relevant settings and interventions, including challenging cases | Deductive proof that no unobserved case can ever violate it |
| Normative justification | Stated evaluative premises, reasons supporting them, consistency and conflict analysis, and valid derivation of obligations under them | That feasibility or persistence alone selects whose interests must count |

These layers can support one another. An empirical pattern can suggest a theorem; a theorem can reveal a decisive experiment; a conceptual argument can justify a measurement or normative premise. The distinction prevents evidence from one layer being silently counted as completion of another.

A full mathematical result can quantify over infinitely many models without enumerating them. A physical universality claim can become exceptionally well supported without being premise-free or logically deduced from finite observations alone. The remaining gap is specific: on an unrestricted domain, models can agree with all finitely tested cases and differ elsewhere. A deeper theory may exclude those alternatives, but the exclusion and its warrant need to be supplied. This is a demand for a defensible bridge, not an argument that scientific generality is impossible.

For the intended ontological reach, additionally give an inclusion argument: what counts as a phenomenon, how the account represents it, what would count as a missing kind, and which rival descriptions are equivalent or incompatible. A universal representation theorem over a declared mathematical class is progress toward that obligation. Merely renaming its elements “all existence” is not an inclusion argument. Nor should failure to finish that argument erase a successful scoped result.

## An achievable central proof target

**Target: characterize continuation and correction possibilities independently of the implementation's irrelevant details, with explicit resource, timing, and information interfaces.** This can become a universal mathematical theory over a declared class even though each member has its own dynamics.

Start with finite controlled processes and deterministic observations, the current established setting. Let B be the nonempty set of states consistent with an actor's information. Define S(z) as the actions that are physically executable from z, satisfy the declared resource/timing rules, and keep every allowed next state inside the protected set. Then robust one-step continuation using that information is possible exactly when

\[
\bigcap_{z\in B} S(z)\ne\varnothing.
\]

This characterization has an immediate proof: a successful actor must choose one action on the common information, so that action lies in every S(z); an action in the intersection is executable and safe for every compatible state. The statement assumes the actor can implement a selected action; limitations of computation, memory, or authority must enter feasibility or a separate implementation requirement. Under the usual sure-safety semantics, randomization cannot help when this intersection is empty: every action used with positive probability must itself be safe in all compatible states.

The result is general within its semantics, yet does not say every state is maintainable or that diagnosis is always necessary. Additional information matters when it separates states needing incompatible actions. A shared safe action permits correction without diagnosis. Extend the characterization recursively to finite horizons, then prove which observation/action/resource translations preserve the recursion. The existing safety result provides a starting point.

The stronger abstraction target should have three parts:

1. **Sufficiency:** the declared correspondence of transition laws, observations, feasible actions, costs, and protected outcomes transfers policies and their retained outcome laws or guarantees.
2. **Necessity for the exact contract:** when claiming equality of all projected state/output laws for every initial state and action, differing projected one-step laws supply an immediate witness against the claim. Do not claim those same conditions are necessary for merely equal optimal values or a smaller observation-only query set.
3. **Constructive failure and relative uniqueness:** produce a distinguishing action, observation branch, cost, or protected predicate when the contract fails. For a fixed surjective projection satisfying exact aggregation, the quotient transition law is fixed by the pushed-forward law. This is uniqueness of that quotient law; it does not prove there is one uniquely minimal description for every query or every ontology.

For the pooling theorem, primitive transfer operations and operational spending have different interfaces. Necessity claims must allow the adapter and its internal information if that is the advertised equivalence. An equality theorem for same-action quotients must not be applied unchanged to action refinements. A finite list of sufficient engineering assumptions also need not be individually necessary; special systems may preserve the desired values accidentally. Seek a necessary-and-sufficient operational condition, then list free instant transfers as one way of satisfying it.

These proof targets would identify what survives across implementations and exactly where it fails. They would be mathematical foundations for a general theory of correction, not a proof that every feature of existence reduces to correction.

## The empirical and normative bridges

An empirical continuation law should freeze its variables, bridge measurements, transformation/intervention class, tolerances, and predicted relationship before integrated outcomes are known. Use independent local measurements to instantiate it in a different mechanism, then test the integrated prediction. Compare serious rival models with comparable calibration access. An independent solver of the same process checks implementation; a different process tests transport; measurements in a physical or institutional target test applicability there.

For example, a target service can share measured capacity, fault belief, accessible maintenance credits, and time with another history yet differ in deadline distribution. If the frozen theory claims these retained variables are sufficient, a reproducible difference in recovery caused by the omitted deadlines refutes that sufficiency claim. It need not refute every theorem in the framework. Adding deadline state is a revised hypothesis requiring a fresh test; it must not be counted as the old prediction succeeding.

When an empirical invariance appears to fail, distinguish a bad measurement, an ineligible intervention, a false bridge, and a false law. That investigation is legitimate, but admission criteria cannot be silently changed after every counterexample. A purported “universal” law that excludes each failed case solely because it failed has lost its empirical restriction.

Normative work needs an equally explicit bridge. Prove what follows from a chosen commitment to continuation, agency, equal standing, or another end, and argue why that commitment should hold. If the same descriptive premises are compatible with different allocations of protection, dynamics alone have not selected between them. A constitutive argument about what it means to act or inquire might narrow that gap, but its scope, rival interpretation, and additional evaluative step need examination. A physically implemented evaluator's existence is not proof of its legitimacy.

## A practical sequence for proving the whole claim

Create a dependency ledger linking each central claim to its definitions, proof premises, interpretation premises, and evidence. For every premise, attempt redundancy proof, deeper derivation, and countermodel. Establish satisfiability before accepting a large proof closure; identify actual added axioms rather than only registry connectivity. Prove the strongest characterization available for the central operational claim, including explicit failure witnesses. Then test the same declared law and bridges in progressively different settings.

Finally state the whole theory as a conjunction of precise claims and mark each as proved, empirically supported, philosophically argued, or open. Some could eventually follow from a common core. That would be a substantive result only if the core and interpretation carry independent content and all required bridge claims are accounted for. No blanket impossibility argument is needed, and no success in one layer should be substituted for the unfinished others.

## Focused primary sources

**Noether, *Invariant Variation Problems* (1918), M. A. Tavel's English translation; §1, Theorems I–II and the paragraph applying them to the variational equations; §2.** [Actual primary text](https://arxiv.org/pdf/physics/0503066), PDF pp. 1–5. Noether defines invariance relative to a group acting on specified variables and a variational integral. Finite-parameter continuous symmetries yield divergence identities, becoming conservation equations on solutions; groups involving arbitrary functions yield identities among the variational equations. Her result is a powerful general theorem with explicit structure, not a claim that every transformation conserves every property. Noether's framework is an analogy for specifying what must be preserved here; this memo does not claim our finite access model is variational or has a Noether charge.

**Pearl, *Causal inference in statistics: An overview* (2009), §§3.2–3.2.2, printed pp. 107–110.** [Author-hosted primary paper](https://web.cs.ucla.edu/~kaoru/SS-2009-57-Sup.pdf). Structural mechanisms are treated as autonomous under specified changes to other mechanisms. The intervention operator replaces selected equations while retaining the others; this distinguishes intervention from conditioning. Identification is relative to a supplied assumption class. Thus causal invariance is an explicit claim about permitted mechanism changes, not uniform invariance under every possible alteration of a system. Applying that interpretation to our empirical targets requires evidence about which changes actually leave the claimed mechanism intact.

**Reissig, Weber, and Rungger, *Feedback Refinement Relations for the Synthesis of Symbolic Controllers*, arXiv v3, Definition V.2, Theorems V.4–V.5 and VI.3.** [Primary paper](https://arxiv.org/pdf/1503.03715), PDF pp. 9–14. The authors give admissible-input and successor conditions for controller refinement and prove a converse for their particular universal controller-transfer property. This is a useful precedent for upgrading sufficient assumptions into a characterization. Their necessity result has an explicit interface and system class; it is not necessity for every conceivable abstraction, stochastic outcome criterion, or implementation adapter. Our proposed generalization must retain those distinctions.

Actual primary bodies were read. These concise source capsules are each below 150 words; no verbatim text is reproduced. The proof architecture and project-specific targets are our proposed analysis, not attributions to these authors.
