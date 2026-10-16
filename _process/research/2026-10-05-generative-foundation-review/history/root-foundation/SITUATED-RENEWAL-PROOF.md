# Situated renewal or replacement under actual dependency use

7 October 2026. AI-authored proof contribution to the requested general connection: continuation → necessary generativity → restoration or transformation when inherited arrangements fail → situated adequate ways. The checked operational layer is [SituatedRenewal.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean). It reuses the [relational process core](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean) and the earlier [continuation-renewal theorem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean).

**Result:** for an arbitrary indexed family of support dependencies in one actual process, demand beyond a dependency's inherited support requires an actual support addition or route replacement before that finite demand window ends. If the inherited route cannot add support during the window, an actual change away from that inherited route is necessary. When required demand keeps exceeding the currently inherited support, these responses occur arbitrarily late on the same continuing history. The requirement concerns some response meeting the dependency, not every response or one prescribed recipe.

The theorem is uniform over arbitrary state, action, dependency-index and route types. It introduces no particular organism, centralized contributor, moral predicate or global quantity to maximize. The universal quantification of this conditional result is not an identification of all living relationships with its premises, nor a proof of ethical authority.

## The premise is a local accounting law, not recurrence

`DependencyLaw P Index Route` records differentiated relationships within the same `Generative.Process P`:

- `route i s`: the provision route for dependency `i` at actual state `s`;
- `remaining i s`: its remaining support at that state;
- `demand i s a t`: the required use on the actual transition `s —a→ t`;
- `added i s a t`: support added during that transition.

The substantive local law is:

\[
P(s,a,t)\ \land\ r_i(t)=r_i(s)
\quad\Longrightarrow\quad
q_i(t)+d_i(s,a,t)\le q_i(s)+g_i(s,a,t).
\]

Here `q` denotes remaining support, `d` required use and `g` added support. When the route persists, its actual use must be covered by remaining or added support. The coordinates are natural numbers in the units of that particular dependency. There is no summation across dependency types and no interpretation as an ethical scalar. Different indices may describe different levels or relations; using them as physical quantities requires validating their units and avoiding double counting in the application.

This law does not already assert that renewal, replacement or an infinite execution occurs. It admits idle histories, exhaustion and termination, replenishing histories, and route changes. It does not say that every route change is helpful. It is a supplied correspondence obligation to an independently specified process, like the native port's already derived draw/arrival and material equations in [direct port renewal](DIRECT-PORT-RENEWAL.md). One must identify the support, demand and route meanings in that process and establish the inequality from its transitions. Renaming arbitrary variables “support” would not accomplish that correspondence.

`Response` abbreviates the independently inspectable disjunction

\[
g_i(s,a,t)>0\quad\lor\quad r_i(t)\ne r_i(s).
\]

The support addition can be consumed during the same transition; the definition does not require the endpoint stock to increase. It also does not certify complete restoration, a working replacement or moral adequacy. Those stronger properties are not hidden in this name.

## Actual histories and the finite deadline

A `Window` contains the actual transition at every offset in a finite sequence of states and actions. `window_is_trace` converts it into a `GenerativeCore.Trace` with the same action word and endpoints. `sumWindow_append` proves that actual accumulated use composes across a reached intermediate state. Nothing refreshes the remaining support at a boundary.

For a window beginning at time `s` and containing `L` transitions, define

\[
D_i(s,L)=\sum_{k=0}^{L-1}d_i(x_{s+k},a_{s+k},x_{s+k+1}).
\]

`window_account_or_response` proves a constructive alternative:

1. The endpoint retains the inherited route and `q_i(x_{s+L}) + D_i(s,L) ≤ q_i(x_s)`; or
2. Some actual transition at offset `k<L` adds support or changes route, and the route immediately before that response is still the route inherited at `s`.

The proof composes the local inequalities through the actual intermediate support amounts. While no route change occurs and no support is added, the intermediate terms cancel. At the first encountered positive addition or route change, it returns that actual event. It uses decidable equality of represented routes and decidable natural-number quantities, rather than assuming a renewal-or-depletion disjunction as its starting premise.

`response_before_exhaustion` now follows: if

\[
q_i(x_s)<D_i(s,L),
\]

the bounded alternative is impossible because endpoint support is nonnegative. The second alternative must hold before that window finishes. This is a deadline in **actual accumulated demand**. There can be arbitrarily many zero-demand or unrelated steps between uses; they cannot falsely count as depletion. No fixed global-clock response rate follows without a further bound on those gaps.

The theorem is about an actual window. It does not infer a feasible window merely from anticipated demand or from a planner's preferred outcome. If support cannot be restored or replaced, the process may fail to continue far enough to realize that demand. Termination is a permitted counter-outcome, not an event the proof silently excludes from the model.

## When inherited arrangements cannot restore support

`inherited_failure_requires_replacement` adds a situated failure law: during this window, every actual transition that starts on the inherited route and keeps that route adds zero support. It need not fail in every possible state, for all time, or for all other dependencies.

Together with demand exceeding inherited support, this forces an actual transition whose pre-transition route is the inherited route and whose post-transition route differs from it. If the response had merely added support while retaining the inherited route, it would contradict the failure law. The conclusion is therefore a change of provision route, rather than a relabeling of ineffective maintenance as success.

This establishes **replacement is necessary for the specified continued use when restoration through the inherited arrangement fails**. It establishes neither that every inherited arrangement should be replaced nor that every replacement works. A route may represent a distributed provision relation rather than a particular individual, and changing it need not mean destroying or replacing every participant. The application must define its route identity and preserve the same relevant dependency across alternative arrangements. Otherwise an apparent “replacement” could merely drop the function being investigated.

## Recurrent requirements, distinct roles and existing renewal

`every_required_dependency_recurrently_responds` follows a single actual continuing history. For each indexed dependency and each reached start time, assume there is a finite subsequent window whose actual demand exceeds the support remaining at that start. Then for each such dependency and start, some later actual transition adds support or replaces its route.

The quantifier order is:

\[
\forall i\ \forall s\ \exists n\ge s:\ \operatorname{Response}_i(n).
\]

The witnessing event may differ for different dependencies and different times. No finite index family, central controller, common contributor, identical timing or individually mandatory recipe follows. The index family consists of dependencies satisfying the stated continuing-use hypothesis; an unused coordinate does not become a requirement merely because it can be named.

For the special case of positive demand on every actual transition, `no_response_strictly_depletes` derives a strict decline in remaining support when route and supply are unchanged. `response_within_remaining_bound` then invokes the existing `ContinuationRenewal.renewal_within_rank_plus_one_steps` theorem. A response occurs between time `s` and `s + q_i(x_s)`, inclusive: at most `q_i(x_s)+1` actual transitions. This recovers the earlier rank deadline from the actual support accounting law. The more general cumulative-demand theorem does not need positive use on every global step.

The result is necessary, not a sufficient continuation policy. A choice of a response can still be infeasible, can fail to meet another dependency, or can replace a route with an inadequate alternative. Joint feasibility is retained in the actual `P.step` relation; independently available responses cannot simply be combined without checking that relation. A sufficient situated policy must certify its actual outcomes and the retained conditions of further activity. The accompanying policy study handles that separate direction; this module does not assume such a policy exists.

## A checked limit on the first inference

`continuation_without_required_use_has_no_response` constructs an idle process with arbitrarily many actual steps, zero demand, zero added support and one unchanged route. Its accounting law holds, and it never has a response. This is not proposed as an organism or as a counterexample to a independently grounded living dependency. It demonstrates exactly why abstract continuation alone does not imply regeneration: the continuing activity's actual dependence and use must be identified.

The existing alternating example in `ContinuationRenewal` supplies another retained limit: recurrent renewal need not generate unbounded new configurations, diversity or complexity. This module does not erase it. Restoration of support, replacement of provision, formation of further organization and expansion of possible life remain distinct claims.

## What this proves toward the requested connection

The general operational connection is now a checked implication:

**Actual continued dependency use + local support accounting → timely support addition or route replacement. Failure of inherited replenishment + that continued demand → actual replacement of the inherited route.**

This is more informative than listing case-specific repairs or defining all continuation as “generativity.” It explains which continuation requires a response, when that response must occur, why a failed inherited route cannot remain the sole provision route, and why the conclusion remains open among situated alternatives.

The application to 生 still requires identifying actual living relationships with these dependencies, as well as consequences that a model's support coordinates omit. The practical or ethical reason to preserve, restore or transform a given pattern is not supplied by its resource necessity. Ren's [positive direction](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md) remains the substantive candidate being investigated; this theorem supplies its general operational dependency relation without defining more 生 as mere resource persistence or asserting universal ethical authority.

## Verification

The module imports only `GenerativeCore` and `ContinuationRenewal`. A direct Lean **4.29.1** check passed all **17 declaration audits**: eleven empty reports and six depending only on `propext` and `Quot.sound`. There is no `Classical.choice`, custom axiom, proof hole or `native_decide`. The arithmetic theorems inherit named standard logical dependencies; this is not no-assumptions completion.

The [fresh combined checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/check_situated_continuation.py) subsequently passed **four modules and 92 audits**, including **42 new declaration audits and 24 new named theorems** across `SituatedRenewal` and `SituatedContinuation`. The [source-bound receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/situated-continuation-verification.json) records the exact sources, commands and logs for run `20261007T155755.741665Z`, with no source changes during compilation. Of the 42 new audits, 35 are empty and seven use only `propext` and `Quot.sound`: the six arithmetic results here and the same-history dependency composition in `SituatedContinuation`. The combined result includes the separately proved sufficient implementation certificate; it does not synthesize an implementation, establish empirical universality or supply ethical authority. No new empirical evidence is asserted.
