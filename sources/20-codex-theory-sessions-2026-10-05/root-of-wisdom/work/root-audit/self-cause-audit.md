# Audit of self-modeling and causal-foundations sessions

Audit date: 5 October 2026. Scope: the locally copied final Markdown reports, proofs, and claim registers in `work/root-audit/snapshots/recursive-self-modeling/outputs/` and `work/root-audit/snapshots/causal-foundations/outputs/`. No source workspace was modified. This review checked selected exact counterexamples; it did not rerun either complete simulation. Locators below refer to these snapshots.

## Verdict

Neither session establishes a completed, uniquely fundamental “root of wisdom.” Both explicitly deny the relevant stronger conclusions. But they substantially improve the candidate: **the route by which understanding is corrected must itself be understood, maintained, and open to correction.** That route includes evidence access, interpretive adequacy, enactment, resources, and evaluative authority. Adding a verbal meta-level supplies none of those automatically.

The positive contribution is a mechanism-level account of parts of revisability. It rules out several tempting substitutes for wisdom: recursive description, internal agreement, confidence, stable control, self-maintenance, and the ability to revise a goal. It does not establish that these operational conditions are sufficient for wisdom, necessary for every wise act, or the deepest possible account of wisdom.

## Strongest finished results

### 1. Correction has three separate achievements

**Access** means obtaining a new observation in time. **Discrimination** means that the observation distinguishes relevant possibilities with specified error properties. **Effective revision** means that an implemented change meets a separately stated outcome criterion. A guarantee of one does not entail the next.

The exact confidence-gate counterexample has an ordinary stream equal to zero before and after a hidden change. The model remains certain, never buys an informative reference, and never detects the error. Any computation confined to the same history inherits its inability to distinguish the worlds. A scheduled or otherwise protected observation can preserve access without a prior anomaly.

The precise finite coverage result is conditional: for N covered intervals and B post-boundary purchases including a terminal sample, the smallest attainable worst gap is ceil(N/B). Noise, unreliable references, finite persistence, missing enactment capacity, or exhausted lifetime resources prevent upgrading that access result into a universal correction guarantee.

**Locators:** `recursive-self-modeling/outputs/correction-access/formal-note.md:5–27` (three achievements and exact gate failure), `:29–76` (coverage and resource limits), `:113–166` (identification and effective revision). The cross-session methodological summary is `recursive-self-modeling/outputs/research.md:228–234`.

### 2. More reflective machinery did not establish more wisdom or even better control

In the first completed comparison, a joint estimator using ordinary data beat the retained-correction approach in all eight primary comparisons; nested and flat implementations of one estimator were behaviorally identical in all 10,000 matched stage/world/seed comparisons. These are supplied simulation results and implementation equivalence, not a universal architectural ranking.

The later 90,000-episode study (2,000 independent paired seeds) found that surprise and periodic access improved the chosen hidden-change mixture but worsened initially unknown constant-bias cases. Surprise checking sometimes spent its entire correction budget before the change. Protected checking supplied later observations but could slow useful initial calibration. There was no universally best gate.

**Locators:** `recursive-self-modeling/outputs/claims.md:35–48`; `recursive-self-modeling/outputs/correction-access/report.md:57–105`. The claim that model depth alone operationalizes wisdom is expressly rejected at `recursive-self-modeling/outputs/research.md:205–218`.

### 3. An apparently well-anchored model can agree with its sensors while regulating the wrong thing

For dynamics x_next = a x + u + g, observations y = x + b and z = x + d, the transformation x′ = x + c, b′ = b − c, d′ = d − c, g′ = g + (1 − a)c preserves all observation histories and observation-based actions in a shift-closed class. It does not preserve error against an unchanged absolute target. Thus consistency among multiple sensors need not anchor absolute meaning.

The completed forcing experiment gives a sharper, but narrower, demonstration: a three-state estimator assuming g = 0 can interpret unmodeled forcing by shifting both inferred sensor biases. It receives every scheduled reference yet its nominal 90% intervals cover only about 2.5% in the hidden-forcing worlds. This is misspecification of that estimator, not proof every estimator must fail. The finite simulation retains fixed initial priors and therefore does not satisfy the full shift-closed assumptions of the general impossibility argument.

An “external anchor” here means evidence or justified structure outside the unresolved representational symmetry—not a knower outside the physical world, and not an incorrigible authority. Known forcing, an independently justified reference, or an initial-distribution assumption can change what is identifiable; each has its own scope and warrant.

**Locators:** `recursive-self-modeling/outputs/experiment/identifiability-proof.md:5–33`; `recursive-self-modeling/outputs/correction-access/anchor-mechanism.md:5–39,93–107`; `recursive-self-modeling/outputs/correction-access/report.md:107–158`.

### 4. Including the observer removes an explanatory omission, not all foundational questions

The causal-foundations account represents models, policies, purposes, resources, and amendment processes within one larger process. It proves that changing an effective mechanism can occur as a state change under a larger fixed rule. A finite staged example lets an institution pay to acquire evidence, request an amendment that opens its blocked deployment gate, and enact the record-responsive action. Success becomes 1 rather than 1/2 without the amendment channel.

The channel, probe, candidate grammar, initial resources, and short support horizon remain supplied. Writing an unknown process as a state variable is not a theory of its formation. The construction demonstrates reachable self-revision, not unrestricted novelty, legitimacy, consciousness, or a final ontology.

**Locators:** `causal-foundations/outputs/formal-results.md:7–47`; `causal-foundations/outputs/causal-foundations.md:155–178`; `causal-foundations/outputs/sources-and-claims.md:9–23,79–89`.

### 5. The meaning and adequacy of a representation depend on what it preserves

A representation needs a decoding rule, task/referent, and evidence of the claimed use. A causal kernel additionally needs intervention semantics; an observational conditional is not automatically an intervention effect. The exact abstraction theorem preserves specified macro path laws only when all merged states have the same pushed-forward response under each admitted intervention, with compatible observation chronology, admissibility, and outcomes. It does not preserve unrepresented harms or differently informed controllers' opportunities.

Two equally observationally adequate models can predict different effects of intervention. Even matching the treatment marginals can leave individual counterfactuals unresolved. Consequently neither “we have one causal story” nor “everything fits” establishes that a model preserves what matters to practical judgment.

**Locators:** `causal-foundations/outputs/formal-results.md:17,31–35,49–110,112–134`; `causal-foundations/outputs/causal-foundations.md:116–151`.

### 6. Describing purposes does not justify them

The same transition equations permit opposite external rankings. Describing how a goal is produced or revised does not establish its justified authority. In the institutional example, reversing the internal goal makes it satisfy its changed criterion perfectly while scoring zero on the original criterion. This does not refute moral realism or imply arbitrary values; it isolates an additional question that causal description does not answer alone.

**Locators:** `causal-foundations/outputs/formal-results.md:186–192`; `causal-foundations/outputs/causal-foundations.md:168–178,194–211`; `recursive-self-modeling/outputs/research.md:218,234`.

## Independent check in this audit

The exact calculations saved in `work/root-audit/self-cause-checks.json` passed:

- At a = 4/5 and zero noise/control, worlds (x,b,d,g) = (0,0,0,0) and (1,−1,−1,1/5) emit identical zero readings forever while accumulating respectively 0 and 60 squared-state loss over 60 steps against the same physical target.
- With g = 3/20 and k = 1/2, r = g/(1−a) = 3/4. Under perfect estimation of x−r, the transformed next state equals (3/10)(x−r); exact rational recurrence was checked for 20 steps. Hence convergence to estimated zero can coexist with displacement from the supplied physical zero. The general convergence argument follows because abs(3/10) < 1; this does not prove convergence of the noisy filter in the simulation.
- The fair-bit models X = U,Y = X and X = U,Y = U have the same observational law but P(Y=1 | do(X=1)) equal to 1 and 1/2. Internal observational agreement therefore leaves a consequential intervention ambiguity.
- A binary policy that follows the opposite internal target always fails the original matching criterion. Achieving a revised target is not automatically an improvement under that original criterion.

These checks corroborate the selected arithmetic, not the full simulation reports or a general theory of wisdom.

## Constructive implications for reaching the root

These sessions suggest a stronger research criterion than seeking one self-confirming sentence: a proposed root should explain and help maintain a **realizable, self-correctable connection among understanding, consequences, and justified action**. It should apply to the proposal's own evidence channels and evaluation rules.

To turn that into evidence rather than a definition, use a bounded case in which the initial diagnosis, reference, access gate, or evaluative criterion can be wrong. Require the process to distinguish which component failed, secure discriminating evidence, enact a correction in time, and preserve remaining correction capacity. Compare with a simpler process given the same evidence and resources. Keep affected interests and stable outcome checks separate from the actor's changing internal score.

A particularly informative next test would pair two failures: (a) a true error hidden behind ordinary model confidence, requiring protected access; (b) a wrong assumed reference/dynamics anchor, requiring revision of the interpretation rather than more measurements of the same kind. A policy that handles only one should not be labeled generally wise. Any third normative case must declare and defend its evaluative premises instead of presenting them as a result of the first two technical tests.

This is a path to a more justified account and an implemented practice of wisdom. It is not yet a proof that the candidate is the unique root, a sufficient definition of wisdom, or something that this assistant possesses as lived judgment.
