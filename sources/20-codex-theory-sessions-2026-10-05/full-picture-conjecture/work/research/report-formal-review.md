# Formal review of the integrated synthesis

Reviewed `outputs/full-picture-synthesis.md`, 5 October 2026. No report edits made.

**Assessment:** the exact finite safety proposition and its information-set proof are mathematically sound under the stated nonempty-transition, common-action, observation, and protected-set assumptions. The numerical examples inspected are consistent. I found no theorem-breaking error. Three small precision corrections are recommended, the first two materially affect scope.

## 1. Qualify the stochastic aggregation requirement

Current wording: “For stochastic dynamics, exact aggregation at the selected level requires ... any two states merged by q [have] equal pushed-forward next-state laws.”

This is the strong lumpability requirement, appropriate when the quotient must work uniformly over admissible initial states and actions. It is not necessary for a compressed process to be Markov under one specially chosen initial law (weak lumpability). Add the uniform scope explicitly.

Suggested replacement: “For a stochastic state quotient that must work for every admissible initial state and action, exact aggregation requires equal pushed-forward next-state laws for any two states merged by q.”

An explicit reason this qualification matters: states a,b merge to 0 and c maps to 1. Let rows in order (a,b,c) be a=(0,0,1), b=(1/2,1/2,0), c=(1/4,1/4,1/2), and initial law (1/4,1/4,1/2). Conditional on every macro history ending at 0, hidden a and b remain equally likely; the next macro observation is a fair bit. The macro process is therefore Markov for this initial law, although a and b have next-macro-1 probabilities 1 and 0. Starting from a or b individually exposes the failure of a common quotient kernel. This counterexample need not be added to the synthesis; the one phrase suffices.

## 2. State the physical implementation limit beside the safety theorem

The earlier endogenous-policy paragraph correctly warns against optimizing over unrealizable policies. The theorem's W recursion nevertheless ranges over ideal observation-history policies. Its result is existence of a mathematical controller, not a guarantee that the currently installed carrier p executes it or can be replaced with it at the stated cost.

Suggested sentence after the proposition proof: “Here W describes existence of an observation-history controller; applying it to a physically realized policy requires that its memory, computation, authorization, and implementation costs are included or separately certified. It does not establish that the current policy carrier realizes a winning controller.”

This is a scope clarification, not a flaw in the proof. To see why it matters, one can put a hidden carrier that always consumes into the otherwise identical device model. An abstract safe controller still exists, while the installed controller destroys an E=1 device. Exact plant/observation quotients do not automatically match the execution law of installed controllers.

The theorem correctly does **not** require the actor to observe q(z). The equality h=hbar∘q is enough, and the proof via q(Phi)=Phibar is valid. B is appropriately defined as compatible with one observed history. If explicit action-availability relations are used instead of failure states, their matching must remain in the statement, as it already does.

## 3. Label the .85 diagnostic optimum as allowing randomization

The .85 upper bound is correct when randomized tests are allowed. Achieving it takes every double-positive outcome plus probability 2/9 of the mixed-outcome class: .01+(2/9)(.18)=.05 false positive and .81+(2/9)(.18)=.85 power. A deterministic test has maximum power .81 at this size because each ordered mixed outcome alone contributes .09 false-positive probability.

Suggested wording: “Even allowing randomized decisions, the maximum detection probability is .85.” This strengthens the impossibility statement and makes the attaining rule precise. The three-sample majority rule remains deterministic and its .028/.972 rates are correct.

## Tuple reconciliation and other checks

- The report's M=(Z,A,F,h) is adequate as a reduced operational core because it explicitly attaches typed semantics, resource/access accounts, clocks, normative predicates, and initial information set B outside the tuple. My longer tuple packages these as metadata. No extra symbols are needed for correctness.
- The exact quotient preserves only the declared safety problem, observations, and action-conditioned successors. The report does not overclaim general causal or ethical equivalence.
- The scalar objections are appropriately about adding heterogeneous resources without conversion rules and erasing protected differences. They do not forbid justified task-specific scalar objectives.
- The SCM observational-equivalence/intervention counterexample is correct. It uses explicit structural assignments rather than inferring causal equivalence from observational agreement.
- The pure-selection scaling example is correct and the model-class caveat prevents mistaken claims about invariance of fixed density-dependent models.
- The public bit-reversal example and instantaneous Boolean-loop examples have the stated restricted scope. No inappropriate universal self-prediction impossibility is asserted.
- The positive device example explicitly labels E=3 charging as overcharge failure, so the modulo-like arithmetic is not being presented as ordinary linear energy accounting.
- The finite-reserve mean lifetime of six and the bridge 2−log(3) follow from the stated timing and dynamics. They are not evidence for universal social laws.
- The report preserves the distinction between represented evaluator e and justified specification N and does not derive ethics from persistence.

After the three wording corrections, I consider the formal portions ready for the stated research scope. Broader cultural/source accuracy is outside this review.
