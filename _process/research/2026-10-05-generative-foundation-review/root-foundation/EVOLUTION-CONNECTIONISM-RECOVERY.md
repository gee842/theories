# From developmental organization to a learning direction

**Completed continuation, 8 October 2026.** [The theoretical study and counterreview](EVOLUTION-DEVELOPMENTAL-MEMORY.md) closes the bounded memory/interference/restoration connection selected in §8 below, with 28 additional checked theorems / 44 new audits. The present 29-theorem recovery remains unchanged at its original scope. The next unresolved connection concerns consequences of interference entering update-rule formation or revision.

8 October 2026. AI-authored theoretical result and author counterreview, following Ren's instruction to “continue to push theoreticalfrontier” and the [prospective protocol](EVOLUTION-CONNECTIONISM-RECOVERY-PROTOCOL.md). **29 new Lean theorems / 41 explicit declaration audits pass.** This closes the selected single-step recovery and derives a finite recurrent extension with explicit sufficient conditions and counterexamples. It does not complete the larger memory/generalization programme or establish broad theoretical superiority.

**中文结论：**从发育过程本身可推出关系改变的实际后果，再由明确的选择关系判断其方向。单步且性状方向相合时，恢复Hebb式方向；多步时，方向须经过实际反馈路径传播。在明确的符号相容条件下，非线性tanh发育保留此方向，有限关系改变也不降低终点选择分数。条件之外，初始和最终性状均相合仍不足以保证它；选择关系自身变化及形成代价另有贡献。这里的“方向相合”是数学符号关系，不是伦理对齐。

## 1. The theoretical transition

The previous [assessment](EVOLUTION-THEORETICAL-INTEGRATION.md) asked whether the generative programme could recover a named connectionist result rather than simply translate an existing reconstruction model. This study addresses:

**a changed developmental relationship → its effects throughout development → differential evaluation of the resulting outcome → a possible learning-like direction of inherited change.**

The first two arrows now have an exact finite-history calculation. The evaluation relation is explicit. An actual population's mutation supply, transmission and replacement remain additional causal relations; a favorable score change is not a proof that the mutation occurs or fixes.

Organism, developmental interaction and selective conditions are local analytical roles within one unfolding. Holding a selective relation fixed identifies a restricted comparison; it does not put that relation outside generative reality. The changing-selection result below removes that particular restriction while keeping its newly supplied dependence visible. No moral verdict is inferred from the selection score.

## 2. The named result and correspondence

Watson et al. use recurrent nonlinear development and directional selection. Their analysis derives a Hebbian direction in a single-step linear slice and relates it to simulations with recurrent tanh development. They also distinguish their algebraic argument from the more complex recurrent case. This study recovers the restricted analytical result and supplies a sufficient recurrent condition; it does not refute their reported simulations. [Watson et al., 2014, printed pp.1127–1128 and 1134–1135](https://www.richardawatson.com/_files/ugd/395d71_73b2fb6f638842949320c0dd26ccfd89.pdf).

Write the stipulated development as

\[
p_{t+1}=(1-\delta)p_t+\tau\,\sigma(Bp_t),\qquad p_0=g,
\]

and the stipulated score as \(W=1+s^\top p_T\). A change \(w\) alters the one coefficient \(B_{ab}\); all other coefficients and the initial profile are held fixed in this comparison. Our \(\tau,\delta\) correspond to the source's interaction and decay constants. The finite vector dimension and horizon are arbitrary. The source's numerical values \(\tau=1,\delta=0.2,T=10\) are admitted, but no full simulation is rerun.

| Source role | Formal definition | What is assumed |
|---|---|---|
| Embryonic profile and regulatory interactions | `Profile`, `Network`, `develop` | Finite dimension, specified initial profile and recurrence |
| Change to one inherited coefficient | `perturb` | The changed coefficient is available to compare; its mutation probability and inheritance are not derived |
| Directional selection | `score` | The stated linear terminal score; no universal biological fitness interpretation |
| Developmental effect of that change | `response` | **Derived** recursively from the same development; no independent response table is supplied |
| Changing selective conditions or formation burden | `netScore` | Explicit differentiable extensions, separately assessed below |

The [source record](../../../../sources/evolutionary-selection/comparative-direction/README.md#developmental-learning-recovery) identifies the inspected pages and preserved original. Terms and equation mappings are an explanatory audit, not something a theorem checker can establish by itself.

## 3. Recovery of the one-step direction

For one linear developmental step, the checked exact difference is

\[
\Delta W=\tau\,w\,g_b\,s_a.
\]

If \(\tau>0\) and \(g_b=m s_b\) for some \(m>0\), then

\[
\Delta W>0\quad\Longleftrightarrow\quad w s_a s_b>0.
\]

Thus the beneficial direction agrees with the correlation of the selection signs. This is a direction condition, not a derived mutation size or fixed learning rate. We compare score differences directly. Interpreting a normalized selection coefficient additionally requires a positive baseline fitness; that interpretation is not hidden in the formal statement.

Theorems: `input_perturb`, `one_step_difference`, `one_step_score_difference`, `beneficial_iff_hebbian`. A declared cost changes the exact condition to

\[
C(w)-C(0)<\tau w g_b s_a,
\]

as checked by `one_step_cost_threshold`. The cost function is an additional law, not a quantity derived from the generative orientation or the source article.

## 4. Recovering the response through recurrent development

Let \(B(w)\) be the changed network and \(q_t=\partial p_t/\partial w\). Rather than assuming an effective learning gradient, the proof derives

\[
q_0=0,\qquad
q_{t+1,i}=(1-\delta)q_{t,i}
+\tau\sigma'((B(w)p_t)_i)
\left(\mathbf 1_{i=a}p_{t,b}+\sum_jB(w)_{ij}q_{t,j}\right).
\]

The direct effect and its subsequent propagation are both retained. `developmental_response` proves this for every finite horizon and dimension under the stated differentiability hypothesis. `tanh_derivative` and `tanh_developmental_response` specialize it to the source's nonlinear activation. `fixed_selection_response` then derives

\[
\frac{dW}{dw}=\sum_i s_iq_{T,i}.
\]

This is ordinary sensitivity propagation, using the chain and product rules. Its contribution here is to make the source-mapped developmental dependence explicit and checked; neither the calculus nor differentiation through recurrence is claimed as a new invention. In particular, the sign need not be determined by the directly connected pair alone.

## 5. A constructive recurrent condition

The positive result does not stop at a counterexample. Suppose

- \(s_i\in\{-1,1\}\), \(\tau\ge0\), and \(\delta\le1\);
- \(s_i g_i\ge0\): the initial profile agrees weakly with those directions;
- \(s_i B_{ij}s_j\ge0\): the interactions preserve those directions in signed coordinates.

The last condition permits negative interactions between oppositely signed traits. It restricts the whole operative network; final phenotype agreement alone is weaker. `development_preserves_orientation` proves that the stated initial agreement continues through every developmental step for an odd, sign-preserving activation. The response theorems then preserve the sign of the coefficient's propagated effect when the activation derivative is nonnegative.

For tanh, these activation properties are checked. `tanh_hebbian_from_initial_orientation` establishes

\[
(s_as_b)\frac{dW}{dw}\ge0
\]

at every compatible network. This is a sufficient condition, not a necessary characterization of all successful networks.

The final three theorems strengthen the derivative statement. Changing the coefficient by \(s_as_b u\), for any \(u\ge0\), preserves network compatibility. Along that entire ray the terminal score is nondecreasing. Therefore

\[
W(B)\le W\!\left(B+s_as_b u E_{ab}\right)
\]

for the declared tanh development. This covers finite changes, including changing a zero coefficient into a nonzero relationship. It is a weak inequality: zero initial activity, zero interaction gain or other degeneracies can give equality. It does not show spontaneous formation of biochemical machinery or stochastic selection of the new coefficient.

The condition provides a closed regime of compatible developmental change. It still assumes a fixed selection pattern and the stated initial signs. It does not derive fast adaptation of those signs, convergence into the regime, competing-pattern memory or the origin of the developmental law.

## 6. Two genuine limits

**Developmental feedback can reverse the pairwise direction.** Take two coordinates, \(g=s=(1,1)\), linear activation, \(\tau=1,\delta=0\), and

\[
B(w)=\begin{pmatrix}-3&w\\0&0\end{pmatrix}.
\]

The new connection is absent at \(w=0\). The checked developmental states are

\[
p_1=(-2+w,1),\qquad p_2=(4-w,1).
\]

For \(0<w<4\), both initial and terminal profiles agree positively with the selection directions, yet the new positive interaction changes the terminal score by \(-w\). Its immediate positive effect has been reversed by the subsequent native feedback. This is an exact counterexample to an unrestricted recurrence claim. It uses the linear member of the model family, not the article's specific tanh simulation, and does not negate the sufficient condition above: the negative self-interaction violates it.

**A changed selection relation can reverse an otherwise favorable trait change.** In the one-coordinate linear example, the profile becomes \(1+w\) while the selecting coefficient becomes \(1-2w\). For \(0<w<1/2\), both remain positive, but the checked score change is \(-w-2w^2<0\). An account that follows development while silently freezing the relation selecting its outcomes gives the wrong comparison for this declared case.

More generally, with the explicit extensions \(s=s(w)\) and \(C=C(w)\), `changing_selection_response` proves

\[
\frac{d}{dw}\left(1+s(w)^\top p_T(w)-C(w)\right)
=s(w)^\top q_T+s'(w)^\top p_T-C'(w).
\]

The three terms distinguish changed developmental effects, changed selection relations and changed burdens. The formula is the standard product rule applied to the full declared relationship. We have not derived the functions \(s(w)\) or \(C(w)\) from an ecological or reproductive mechanism. Calling them endogenous would not discharge that missing explanation.

## 7. What this adds to the generative theory

The previously named recovery obligation now has a concrete answer. A learning-like direction follows from how an altered relationship generates an outcome and how that outcome enters selection. The immediate local correlation is sufficient in a restricted slice. In a recurrent process, the complete propagation of consequences matters; the checked sign-compatible regime explains when the simpler rule survives that propagation. Changing the selecting relation supplies another causal contribution rather than automatically preserving the old rule.

This sharpens the proposed connection between organization and the evolution of organization. The theory can ask which formed relations make the preservation condition hold, which histories destroy it, and which changes to selection retain or overturn the gain. Existing [reconstruction](EVOLUTIONARY-ORGANIZATION-INTEGRATION.md), [updater formation](../../../../theories/becoming/chapters/UPDATER-FORMATION.md) and [goal revision](../../../../theories/becoming/chapters/GOAL-FORMATION-AND-REVISION.md) remain relevant completed mechanisms. This new mathematical branch is not their already-joined physical history.

The advance is a source-mapped recovery and a precise conditional extension within this programme. A conventional account using the same recurrence and calculus obtains the same result. No exclusive mathematical capability, priority over the literature or broad reduction of assumptions has been established.

For the wider alignment programme, the result clarifies causal premises: a relationship's favorable local effect need not survive later feedback or revision of the selection rule. It supplies no ethical warrant for \(W\). G0 and the completed practical commitments retain their separate justificatory role within the same generative account.

## 8. Counterreview and the next precise frontier

**Does the positive condition assume the conclusion?** It assumes signed compatibility of the interactions, not monotonicity of the complete developmental outcome. The latter is derived, and compatibility is shown to survive the specified finite changes. However, this is a deliberately favorable regime; showing that evolution reaches or retains it remains a different problem.

**Is this a recovery of associative memory?** No. It recovers the selected directional result. Multiple attractors, recall from corrupted inputs and generalization across novel combinations require additional dynamical arguments. Differentiability and a favorable gradient alone do not establish them.

**Does the adverse case refute evolutionary connectionism?** No. It defeats a stronger unrestricted interpretation. The source already distinguishes its analytical slice from recurrent numerical evidence. Our sufficient condition and counterexample state that distinction more precisely at this formal scope.

**Have formation and selection been fully derived?** The developmental response is derived; the native law, available coefficient change, selective relation and optional cost remain supplied. Existing formation results cannot be silently substituted for those inputs without a valid correspondence. This limitation concerns the current comparison, not a denial of the completed conditional foundation.

The next theoretical connection is **inherited changes across differing selection patterns → preservation or loss of developmental memory and continued revisability**. The single-pattern sign-compatible regime cannot simply be assumed under incompatible target changes. A useful continuation must derive the relevant inherited update and developmental behavior in the same stated model, including interference and failure, and assess whether the existing formation/reconstruction results supply its required relations. Recovering one memory or generalization result would advance that target; another representation-equivalence proof would not. No new empirical dataset is the prerequisite.

## 9. Verification and scope

The [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/ConnectionistRecovery.lean), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/check_connectionist_recovery.py) and [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/connectionist-recovery-verification.json) record a fresh build with Lean 4.30.0-rc2 and pinned Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`. All 29 theorems and 12 other explicit declarations are audited. Standard logical dependencies are disclosed; no new axiom, `sorry`, `admit` or `native_decide` is admitted. Source, compiler, checker, import and log hashes bind the result. Mathlib is reused as a pinned dependency; its previously uncached hyperbolic-derivative module was built.

Compilation and dependency audit are new validation. No empirical experiment, population simulation, independent-agent acceptance or repository-wide proof audit is claimed. The bounded recovery task is complete; the broader evolutionary theory remains under development.
