# Available questions, retained answers and revisable inquiry

6 October 2026. AI-authored comparator and scope note under the [shared nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). Named connection: **consequences of inquiry → changes in which questions remain attainable → the requirements for revising an operative inquiry criterion**. The current result concerns the available-question frontier, not an implemented learner of that frontier or a derivation of what ought to matter. It reuses the [existing three-class apparatus argument](INQUIRY-CONTINUATION-MATH.md) and preserves the distinct [inquiry-sufficiency result](INQUIRY-SUFFICIENCY-INTEGRATION.md).

## The closest directly verified antecedent

**Edward F. Moore, “Gedanken-Experiments on Sequential Machines,” *Automata Studies* (1956), pp. 129–153.** The [primary paper](https://www.cs.cmu.edu/~cdm/resources/Moore1956-gedanken-experiments.pdf) was directly inspected for the preceding [source note](INQUIRY-CONTINUATION-SOURCES.md). Printed pp. 130 and 135–136 expressly permit one-copy experiments to branch on preceding outputs. Theorem 1, pp. 138–139, distinguishes the availability of a test for each pair of states from an experiment identifying every possible initial state. Different first inputs destroy different remaining distinctions. The same discussion explains why knowledge of the final state need not recover the initial state. This is the precise antecedent for the present separation of individually answerable questions from their jointly answerable conjunction. No quantum analogy or claim of historical novelty is required.

**Blackwell comparison is relevant but not directly verified here.** David Blackwell, “Equivalent Comparisons of Experiments,” *Annals of Mathematical Statistics* 24(2) (1953), 265–272, [publisher DOI](https://doi.org/10.1214/aoms/1177729032), is the standard bibliographic candidate for comparing statistical experiments through decision performance and postprocessing. The primary PDF endpoint returned an HTML access page during this bounded search. Therefore this note does not claim to have checked its theorem statement or transfer its general stochastic equivalence theorem. The elementary deterministic factorization below is proved directly and does not depend on that uninspected source. In particular, we do not attribute a theorem about physically executable joins or restorative mechanisms to Blackwell.

## The deterministic comparison needed for this study

Let \(X\) be the fixed finite set of admitted starting alternatives. An executable deterministic inquiry policy \(\pi\) produces an accessible retained transcript \(m_\pi(x)\). Include every accessible channel and retained datum, not just a convenient sensor bit. A finite factual question is a function \(f:X\to V\). It is answered exactly by the transcript if there is an available decoder \(d\) with

\[
f=d\circ m_\pi.
\]

At the information level, such a function \(d\) exists exactly when

\[
m_\pi(x)=m_\pi(x')\Longrightarrow f(x)=f(x').
\]

Necessity follows by applying the decoder to equal records. For sufficiency define \(d\) on each realized transcript by the common answer of its fiber; the condition makes the definition independent of the representative. This is the same elementary constancy condition already established for retained questions in [meta-revision](../../../../theories/becoming/chapters/META-REVISION.md). It does not prove that an information-level decoder is formed, affordable or correctly calibrated.

Order question partitions from coarser to finer. Under a declared policy interface closed under the required decodings, attainability is downward closed: an attainable question also answers every coarsening. The joint question \((f,g)\) has equality kernel \(\ker f\cap\ker g\). It is the least partition finer than both. Physical attainability need not be closed under this join.

In the existing apparatus, let \(X=\{A,B,C\}\), with the behavioral meanings fixed in [C2–C3](INQUIRY-CONTINUATION-MATH.md#proposition-c2--every-pair-of-initial-classes-is-contextually-distinguishable). The binary questions “is it \(A\)?” and “is it \(B\)?” are separately attainable through probes at different learned output phases. Their joint answers are \((1,0),(0,1),(0,0)\), so the joint question identifies the three classes. The one-packet impossibility excludes that joint question. Consequently there is no greatest attainable question: any greatest one would refine both binary partitions and hence answer their unattainable join. This implication uses the same one-packet interface and the decoder-closure premise; it is not an extra empirical claim.

A nominal reset is insufficient to restore joins. A sufficient condition is that an actual common continuation can reestablish the conditions for the second inquiry about the same starting target, while retaining the first answer and preserving all obligations of the combined execution. Run the first protocol, restore, run the second, retain both answers. This supplies the joint question. Where every pair of attainable questions can be combined this way, pairwise join closure follows; for finite \(X\), repeated finite joining yields a greatest attainable partition. This is a sufficient conditional construction, not a necessity theorem about the only possible mechanism for joins. The apparatus's ordinary phase reset does not replenish its consumed source packet.

## The time at which a demand becomes available matters

If the question is revealed before choosing the experiment, the relevant condition is

\[
\forall f\in\mathcal F\ \exists\pi_f,d_f\ \forall x\in X:
\quad d_f(m_{\pi_f}(x))=f(x).
\]

If one experimental stage must finish before the question is revealed, and no further native inquiry is then permitted, the stronger condition is

\[
\exists\pi\ \forall f\in\mathcal F\ \exists d_f\ \forall x\in X:
\quad d_f(m_\pi(x))=f(x).
\]

The two binary questions above satisfy the first condition but not the second. If the latter held, both decoders applied to the same retained transcript would answer the joint question. This makes the quantifier difference concrete without positing a numerical value of information.

Late demand must not be confused with a ban on waiting. If an actual waiting continuation preserves the packet, relevant target, memory and other requirements until the question arrives, the learner can then use the corresponding question-specific experiment. Conversely, deadlines, decay or obligations can defeat that continuation. The present comparison establishes no universal recommendation to wait, experiment or preserve every option. Their relevance must be explained through the continuing activity, not supplied by an analyst's preference for maximal information.

## What active learning and abstraction refinement already contribute

The initial source task also checked two established mechanisms. They remain useful comparators for a subsequent implemented criterion study, but they do not remove the present incompatibility of experiments.

**Angluin, “Learning Regular Sets from Queries and Counterexamples” (1987), pp. 87–106.** Directly re-read the [primary paper](https://homepages.math.uic.edu/~lreyzin/papers/angluin87.pdf), §2.2 and Figure 1, printed pp. 93–95, alongside §2.1's table definitions. When two retained rows agree but their action successors differ on an existing suffix, L* adds the action-prefixed suffix as a new experiment. An equivalence counterexample first adds its prefixes to access histories, then table repair creates the needed distinctions. The termination argument bounds the strict growth of distinguishable rows by the target's minimal states. The membership/equivalence contract and the goal of exact regular-language identification remain supplied. This directly supports acquired revision of operative questions, not acquisition of the ultimate relevance or ethical criterion.

**Clarke, Grumberg, Jha, Lu and Veith, “Counterexample-guided Abstraction Refinement,” CAV 2000, pp. 154–169.** Directly inspected [the author-hosted primary paper](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Counterexample-guided%20Abstraction%20Refinement.pdf), §2 Theorem 1, §3, §4.2–4.3 and Theorem 4 (PDF pages 5, 7–13). The specification is supplied. The abstract model overapproximates concrete behavior; a real counterexample is reported, while a spurious one guides refinement. The algorithm isolates an unrealizable path prefix and separates states that the abstraction had combined. The stated completeness scope covers specifications whose counterexamples are paths or loops. Finding the coarsest refinement is not guaranteed by the implemented heuristic. This is the closest verified comparator for consequence-relative representational sufficiency under a fixed claim. Its symbolic access to a concrete program is not automatically an experimental interface available to our formed learner.

These two sources were checked beyond abstracts. No general theorem of either paper is reproduced as a newly discovered mathematical result. A Rivest–Schapire scan was located during the initial search, but its substantive text was not successfully inspected and is not used as evidence.

## Preserve the branch's already established advances

The [acquisition study](../../../../theories/becoming/chapters/ABSTRACTION-ACQUISITION.md) already implements counterexample-driven distinguishing-suffix formation. The [inquiry-interface argument](INQUIRY-INTERFACE-ARGUMENT.md) additionally identifies acquired control of actual sampling duration under an unchanged uniqueness rule. The [sufficiency analysis](INQUIRY-SUFFICIENCY-MATH.md) identifies the actual `010` prefix whose next observation eliminates neither candidate yet changes what their newly next predictions require. Separately, the concern branch's [inquiry revision](../../../../theories/becoming/chapters/INQUIRY-REVISION.md) forms a contact and uses acquired evidence to rewrite the operative encounter requirement from six to four under an explicit new local law. This note neither duplicates those constructions nor restores a blanket claim that evidence-dependent criterion changes are absent.

The present addition is a constraint on the stronger connection: **different relevant questions can require incompatible expenditures of an existing opportunity, with no available inquiry that first learns everything and postpones all selection.** A mechanism that revises which question it pursues must therefore be evaluated through its actual target, timing, evidence and changed possibilities. The source comparisons do not provide that mechanism or justify its target for it.

Within the nondual account these are differentiated relations of the same activity: an encounter both makes an answer available and changes what can next be encountered; a retained distinction participates in choosing a continuation. A local question or restoration law being supplied identifies this representation's scope. It does not place meaning, value or the conditions of knowing outside generative reality. A substantive positive next result would show those relations acquired or revised in an actual continuing history, with misleading revisions and preserved counterexamples. No new experiment, empirical cognition evidence, universal ethics or unique mathematical constitution is claimed here.
