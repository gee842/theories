# Enough information for an action can be less than enough for a full account

This is an elementary finite decision result. It sharpens the earlier observation-fiber test by making the question of interest explicit.

Let M be a finite set of candidate models, Z a set of represented information states, r:M→Z the available model distinction, A a finite common action set, and L_m(a) the stipulated expected loss of action a under m. A policy g:Z→A attains each model's own minimum loss exactly when, for every represented state z, the sets of optimal actions have a common member:

\[
\bigcap_{m:r(m)=z}\operatorname{argmin}_{a\in A}L_m(a)\ne\varnothing.
\]

Necessity follows because g(z) must be optimal for every model mapped to z. Sufficiency follows by selecting a member of each intersection. Randomization does not repair an empty intersection if the requirement is exact optimality under every model: a mixture has minimum expected loss only when its positive-probability actions are individually optimal there. This argument assumes a common action meaning and linear expected loss of the lottery.

The criterion is weaker than knowing all losses. Two indistinguishable models can assign different losses to the same action while agreeing that it is best. Conversely, if their strictly best actions differ, no policy using only the shared representation can match both model-specific optima. A minimax policy may still be justified, but it answers a different question.

Example: losses for actions a and b are (1,4) in one model and (2,5) in another. The exact loss is unidentified, but a is optimal under both. Replacing the second model with (5,2) destroys that shared optimum. The same informational coarseness can therefore preserve one decision problem and fail another.

These facts do not make additional information valueless for every future decision. They show why a disciplined account must specify whether its claim concerns a best action, an exact risk, a threshold guarantee, or later questions. Demanding a full representation before acting can be an error. Accepting a stable action as proof of a full representation can be an error too.

The prospective pilot includes a matched pair testing this distinction. The result above was written before inspecting those instances or any participant output. It is not a newly discovered theorem and does not validate the proposed six-question discipline.
