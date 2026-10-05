# Finite revisable methods and limits of completeness

Research memo for Ren, 5 October 2026. This memo examines whether a finite method can support continuing, situated understanding while its representations and purposes remain revisable. The answer is conditionally yes for extension, and no for several stronger claims of universal completion or self-certification. These are different questions. The most useful candidate is a discipline of scoped claims and concrete revision witnesses, rather than an alleged final representation of everything.

The mathematical results below are established observations or elementary derivations. The proposed audit practice is a research design choice. No novelty, metaphysical completeness, human exceptionalism, AI consciousness, or ethical legitimacy is established.

## What finite and open ended can mean

Four kinds of finitude must be separated: a finite description of rules; finitely many internal states; finite resources in each episode; and a fixed upper bound on resources across every episode. A finite program can generate arbitrarily long outputs when its time and storage can grow. That does not put an infinite completed record into any finite execution. A machine whose complete accessible memory has only b binary units can occupy at most 2^b memory states; unbounded external records or an unbounded clock must be counted if they participate in its reasoning.

An elementary example is the rule that, for each natural n, emits the claim that n squared is nonnegative. Its description is finite and its possible sequence of distinct claims is unbounded. It offers no evidence of judgment, wisdom, discovery, or increasing practical understanding. A compact description can entail infinitely many consequences without its owner having computed, retained, or understood each one.

The mathematical existence of an unbounded sequence is also different from a feasible endless trajectory. Continuation requires the actual supply of memory, energy, attention, time, and enabling relations assumed by the sequence. The inherited claim register already develops this point for inquiry funding and recovery; none of the results below establish an inexhaustible material supply.

“The world is infinite” is not needed for this research proposal and has not been established. The weaker claim is that a current observer has not justified a final closure of all relevant questions. Some restricted domains do permit complete, finite answers. Treating every domain as necessarily inexhaustible would itself mistake a sweeping interpretation for a result.

## A precise limit on completion through effective revision

**Conditional proposition.** Let T_0, T_1, ... be an increasing sequence of sound theories containing Peano arithmetic. Suppose one algorithm enumerates the axioms of T_n from n. Then the union T_infinity is a sound, effectively enumerable arithmetic theory and is incomplete.

**Proof.** Dovetail the axiom enumerations for every n to enumerate the union. A proof uses only finitely many axioms, which all belong to some stage because the sequence is increasing. Thus each theorem of the union is a theorem at a sound stage. The union is sound and effectively axiomatized, so arithmetic incompleteness applies.

This proposition is an application of established incompleteness, not a new theorem. Gödel's original Proposition VI assumes the stronger omega-consistency condition; soundness here implies it. His Proposition XI also limits internal consistency proofs under its specified formalization. The claims concern suitably strong, effective arithmetic theories; they do not concern every language, every finite model, or every kind of understanding. [Gödel 1931, translation by B. Meltzer, Propositions VI and XI](https://homepages.uc.edu/~martinj/History_of_Logic/Godel/Godel%20%E2%80%93%20On%20Formally%20Undecidable%20Propositions%20of%20Principia%20Mathematica%201931.pdf).

**Interpretation.** Settling a previously undecidable claim by extending a theory does not establish that the extending procedure settles all arithmetic truth. The proposition assumes soundness from the analyst's perspective; it does not give the learner a test for its own soundness. It permits continuing increases in theorem coverage.

**Boundary.** If revisions retract statements, their simple union is not the agent's eventual accepted theory and this proof cannot be applied to that union as if it were. If external inputs are not effectively generated, the autonomous enumeration assumption also fails. Neither exception by itself provides a complete or reliable method. Identifying an oracle mathematically is not constructing a physically available source of infallible answers.

Turing's 1939 work is directly relevant historical precedent for sequences of stronger formal systems. The opening sets out ordinal-indexed extensions and asks what kind of coverage they achieve. Its full technical treatment was not verified in this session, so no detailed theorem about those ordinal progressions is relied upon here. [Publication and reproduced opening](https://apice.unibo.it/bin/view/Publication/TuringPlms45); [primary publication DOI](https://doi.org/10.1112/plms/s2-45.1.161).

## Self modification and internal observers

**Simulation observation.** Suppose an agent's memory, interpreter, and current code have finite encodings, and each code revision and state transition is effective. A fixed universal interpreter can store the current code as data, execute one step, update the code, and continue. Self-modification therefore does not by itself escape computability. New sensors and external inputs change the available information and must be modeled as inputs. They are not created by rewriting the interpreter.

Turing constructs universal simulation in Sections 6 and 7 and proves specific general decision procedures impossible in Section 8, including deciding whether an arbitrary machine ever prints a specified symbol. His original circle-free problem should not be carelessly renamed the modern halting problem without qualification. These results support limits on uniform effective decision procedures, not the claim that nothing can be proved about particular programs. [Turing 1936](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf).

An internal observer can have correct information about itself. For example, a program can store its own source text and accurately report its current counter. No contradiction follows. A representation of an observer can also appear inside that observer's larger causal model. Such inclusion does not guarantee exhaustive representation, correct semantic interpretation, accurate introspection, or adequate computation.

**Elementary prediction counterexample.** Assume a predictor must announce a definite bit p before a target acts, the target receives p, and its permitted action is to output 1−p. The announced prediction cannot equal the target's output. This is a consequence of the specified feedback channel and target policy. Removing disclosure, restricting the target, predicting a different variable, or using probabilistic criteria changes the problem. It does not prove that observers cannot predict themselves or that all world-modeling is impossible.

Self-reference is thus neither a magic source of truth nor an automatic inconsistency. The recursion theorem supplies productive forms of computational self-reference; its conditions matter. A useful source for later study is Moschovakis's research treatment of Kleene's theorem, whose explicit fixed-point statement was checked in the publisher excerpt. The entire paper was not retrieved. [Moschovakis 2010](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/kleenes-amazing-second-recursion-theorem/7ABD80C4DDD01A643217D8CD5E8268CD).

## A small exact test of mistaking a part for the whole

Let H be a finite set of possible histories and r:H→Z the entire retained representation available to a decision procedure. Let q:H→{0,1} be a declared question.

**Proposition on distinguishability.** There exists a function g with g(r(h))=q(h) for every h in H if and only if q is constant on every fiber of r, meaning every set of histories that r maps to the same z.

**Proof.** Necessity: if r(h_0)=r(h_1), a single g receives the same argument in both cases and cannot return two different answers. Sufficiency: when q is constant on each fiber, define g(z) as that common value. Its value outside the image of r is irrelevant.

**Corollary.** A representation supports every binary question about H exactly if and only if r is injective. If it merges h_0 and h_1, the question “Was the history h_0?” distinguishes them and cannot be answered from r alone. This universal class of questions is very demanding; it is not a practical requirement to retain everything.

This is an elementary representation/identification result, closely related to inherited U20 and U22. It concerns informational possibility, not computational tractability or normative importance. Over an infinite domain, the existence of g need not imply that g is computable.

**Worked example.** Let H={00,01,10,11}; retain r(h)=the number of ones. The question “Was there exactly one 1?” is perfectly answered. The question “Was the first symbol one?” cannot distinguish 01 from 10. Under the uniform distribution over the four histories, the minimum error for the latter question from r is 1/4: the ambiguous fiber occurs with probability 1/2 and has conditional error 1/2. Retaining the ordered pair gives zero error. The same summary is complete for one question and incomplete for another.

**Counterweight.** If the only admissible question is the number of ones, discarding order loses nothing for that question. If retaining order is costly, doing so can be worse under the stated objective. Neither proposition makes maximal recording wise.

**Inherited example checked.** In the earlier source, histories 00010 and 01000 share endpoint zero, length, and two switches. For the supplied slow-then-fast versus fast-then-slow family, the first history's posterior probability of acceleration is 29241/29362. Its next-state-one probability is 26329/58724≈0.4483516109; the other's is ≈0.0516483891. A response threshold of 0.3 gives opposite actions. I independently checked these fractions. The exact question, switching rates, priors, and acquisition design remain assumptions. The older summary stays truthful while losing adequacy for the new question.

There is primary statistical precedent: Robert and colleagues show that a statistic sufficient inside each candidate model need not be sufficient for comparing the models; retained information and computational effort are separate issues. Their particular ABC setting should not be generalized to every form of learning. [Robert et al. 2011, especially Section 1.3 and Equation 1](https://arxiv.org/html/1102.4432v4).

## Distinguishing no current evidence from no possible evidence

The preceding proposition freezes the entire available representation. An active learner can sometimes acquire information that separates an ambiguous pair. To assess a proposed correction policy, its full transcript must include actions, sensor observations, inherited traces, randomization, visible resource use, and deadlines. An action can itself carry information.

If two worlds induce identical distributions of that complete transcript under a policy, the policy has the same distribution of final reports in both worlds. It therefore cannot classify both worlds with certainty when the required answers differ. With equal priors, the minimum binary classification error for two specified transcript laws P and Q is (1−TV(P,Q))/2. This is established statistical decision theory; inherited U22 and U26 already use corresponding bounds.

A failure under one policy does not establish impossibility under every possible policy. Conversely, an experiment that could distinguish the worlds in principle does not establish that an agent can afford it, complete it before the deadline, interpret its result, or perform the appropriate response. The policy quantifier must be uniform: one executable observation-based policy must work across the declared worlds, rather than granting a different hidden-state-informed policy to each world.

## An operational proposal for revisable claims

**Proposal, not theorem.** Attach a scope record to every consequential claim: the question; represented histories and model family; the observation and intervention interface; inference rule; evaluative criteria; resource and time bounds; and the conditions that would require rechecking it. Keep the labels “assumption,” “conditional derivation,” “empirical support,” and “evaluative commitment” separate.

Then search for a concrete revision witness: two cases the current representation treats alike but that make the target claim differ, or that require incompatible adequate responses. Finding a pair defeats the broad claim. The appropriate repair may be a narrower scope, a new distinction, a new experiment, an abstention, a changed response, or acknowledgment of unresolved disagreement.

The audit itself has a scope. Failure to find a pair certifies completeness only when the relevant finite search is exhaustively covered or a suitable proof is available. Heuristic search over a finite batch is evidence of surviving those tests. It is not evidence that all unimagined alternatives have been considered. This limitation should appear in the audit's own record.

The proposal can remain revisable: its record format, search methods, and priorities can be replaced when they fail. If “revisability” is itself abandoned, the successor may still be coherent or useful in some narrow sense, but it no longer satisfies this proposed discipline. That is a definitional boundary and a normative choice, not a contradiction forced by nature.

## Representational and purpose changes are different

In the provisional S=(X,T,R,O), specify whether X is the observer's current representation of configurations or an analyst's hypothesized state space. Specify whether O denotes actual available measurement channels, predicates expressible in the agent's language, or distinctions already learned. These are different objects. Defining O to contain all distinctions does not give the observer access to them.

To represent the agent's causal participation, one can include its memory, code, goals, evaluator, permissions, and sensor state among the modeled components. This makes feedback and revisions representable; it does not validate the model. If T changes the available representation or observation channel, cross-stage claims need an explicit translation or a statement that their meanings have changed. A score called “accuracy” before and after a target redefinition need not measure the same thing.

Purpose revision introduces a separate difficulty. Hold all predicted consequences fixed. One evaluation ranks action a over b, another ranks b over a. Better prediction alone cannot choose between those evaluations. A decision requires an additional normative criterion, deliberative procedure, authority relation, or practical commitment. Treating the evaluator as a physical process explains how evaluations arise; it does not make its ranking ethically justified.

Nor is preservation of all options automatically wise. A harmful option can deserve closure, inquiry can impose costs, and irreversible action can sometimes be warranted. “Preserve correction where valuable and legitimate” is more defensible than unconditional maximum reversibility, but its terms require explicit ethical and institutional work.

## Audit of the parent synthesis toy

The proposed two-world toy has operating losses A:[a=0,b=8,wait=3] and B:[a=8,b=0,wait=3], with identical routine observations. For a lottery with probabilities p_a,p_b,p_w, mean loss across worlds is 4(p_a+p_b)+3p_w≥3; hence worst-world loss≥3 and waiting attains 3.

A timely binary symmetric diagnostic of known error e, costing one resource unit and available within the pathwise budget, gives minimax operating loss min(3,8 min(e,1−e)). Signals may be inverted if e>1/2. At e=0.1 the operating loss is 0.8 in each world; the loss is 8 on an erroneous signal, so this is not pathwise safety. If diagnostic expenditure also enters the scalar objective at weight one, the optimum is min(3,1+8 min(e,1−e)), which is 1.8 at e=0.1. The budget-only versus objective-cost convention must be explicit.

Removing action a leaves all permitted actions in world A with operating loss at least 3, so the diagnostic cannot reduce minimax loss below 3. Adding world C with the same signal law as A and losses [8,8,3] also restores the minimax lower bound 3. A valid old-family certificate can therefore fail after family expansion. These are exact finite illustrations with no originality claim.

## Rejected formulations and open disagreements

- Rejected: “Any finite foundation must be closed.” Finite rule descriptions can generate indefinitely many extensions under expanding resources.
- Rejected: “Self-rewriting reasoning escapes formal limits.” Effective rewriting can be simulated by a fixed universal machine under the stated assumptions.
- Rejected: “Gödel proves that the world is infinite or that humans exceed machines.” Those conclusions are outside the theorem's scope.
- Rejected: “An internal observer cannot know itself.” Specific self-knowledge and formal self-reference are possible; universal self-certification is a stronger claim.
- Rejected: “No anomaly means no important omitted distinction.” The inherited U22 construction and the fiber test show why the observation interface matters.
- Rejected: “More retained data, prediction, flexibility, or survival always means more wisdom.” Relevant losses, costs, affected parties, and legitimate purposes are additional commitments.
- Rejected: “A finite core unifies every tradition.” Mathematical compatibility does not establish historical or philosophical equivalence.
- Open: Which kinds of departure from present purposes count as correction, which as legitimate change, and which as manipulation?
- Open: Can agents discover useful new distinctions without a researcher supplying the alternative cases? The present audit still requires a candidate generator.
- Open: What resource allocation supports enough independent challenge without making inquiry prohibitively costly?
- Open: How should disagreements over scope, evidence, and ends be adjudicated when participants lack shared authority or common losses?

## Concrete next experiment

Use the two-world toy and its third-world challenge as a small held-out evaluation of the proposed scope-record practice. Give one agent only an optimization objective and another the same tools and budget plus the scoped-claim procedure. Randomize which limitation changes: missing observation, delayed observation, missing action, changed losses, or an unannounced additional world. Assess whether the agent identifies the invalidated assumption, distinguishes expected performance from pathwise guarantees, asks for a genuinely discriminating observation, and avoids claiming a universal solution. Keep the model family, computational budget, and evaluation procedure fixed in advance for the first trial; report adverse cases and costs as well as gains.

This can evaluate a narrow improvement in reasoning practice now. It cannot establish that the proposed discipline is the unique root of wisdom. A later study would need independently proposed changes and disagreement over purposes rather than only researcher-authored alternatives.

## Records and source limits

Read-only local references were the integrated claim register, its research README, and the 5 October source “Inherited evidence under model revision.” Relevant inherited entries include U05, U20–U22, U24–U26, and related resource constraints. These are project records and constructed results, not independent empirical validation. No file in /Users/ren/theories was changed.

Primary sources checked in substantive passages: Gödel's 1931 paper in Meltzer's translation; Turing's 1936 paper; Robert and colleagues' 2011 paper. Turing's 1939 opening and publication details, and the explicit fixed-point statement in Moschovakis's publisher excerpt, were checked with the full-text limitations stated above. Rice and Blackwell records were located but their full papers were not retrieved; no additional theorem in this memo depends on pretending otherwise. All uncited small propositions and proofs above are explicit elementary derivations, with established status rather than originality claims.
