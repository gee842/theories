# Acquired gain revision with finite continuing support

6 October 2026. This is a new, explicitly supplied local realization of repeated revision in the same delayed plant used by the varying-gain analysis. It is not an extension of an existing concern learner's actual endpoint. [SupportedRevision.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/SupportedRevision.lean) compiles under the pinned Lean 4.30.0-rc2/Mathlib environment: 26 theorem audits report only `propext`, `Classical.choice` and `Quot.sound`. The root's fresh combined receipt governs package acceptance; the author compilation is not an empirical test.

## Actual consequence, acquired observation and later gain

One state contains the delayed pair `(x,y)`, the stored previous first coordinate, retained gain bit, optional acquired overshoot bit, event phase, available fuel and original source-packet count. The gains are `1/4` and `3/4`. Three successive events form a cycle:

1. **Operate:** pay one fuel unit, advance the actual pair to `(x−k*y,x)`, store old `x`, clear the previous observation, and transfer one existing three-unit packet into fuel.
2. **Acquire:** pay one fuel unit and retain whether old and new first coordinates have opposite signs.
3. **Update:** pay one fuel unit; select gain `1/4` after reported overshoot and `3/4` otherwise. The next operation consumes that retained choice.

The phase law prevents an old observation from authorizing repeated updates without another operation and acquisition. Transfer from a source packet is an explicit supplied operating return, not inferred from performance or treated as newly created support. The update price includes the declared retained write; no separate passive wear, elapsed-time maintenance or autonomous invention of the schedule is modeled.

Starting from `(1,1)` with gain `3/4`, faithful cycles reach `(1/4,1)`, `(-1/2,1/4)` and `(-9/16,-1/2)`. The second acquired report changes the gain to `1/4`; the third changes it back to `3/4`. These are revisable retained choices generated through the actual outcome channel, not an arbitrary time-indexed gain list relabeled learning.

The clamped reader pays the same bills but always reports no overshoot. Its first two plant endpoints match the faithful history; it retains `3/4` after the second and reaches `(-11/16,-1/2)` at the third operation. Thus the acquired report causally changes the later gain and trajectory. Both routes remain inside the safe interval. This comparison does **not** establish that faithful sensing is necessary for stability, optimal control, or better regulation; a fixed gain in the certified interval is also a relevant simpler comparator.

## What is proved jointly with funding

The module reuses [ResourceContinuation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean)'s actual `AccountLaw` and `SupportTrace`. Every event costs one unit. Fuel receives three on operation while the original packet inventory decreases by one; total support `fuel + 3*packets` decreases by exactly one per event. An arbitrary funded prefix of `N` complete cycles spends `3N`, receives `3N` into the fuel account through those original packets, and preserves the actual intermediate states. With positive original fuel and at least `N` original packets, fuel after each complete cycle equals its original value and packets equal the original count minus `N`.

The same certified history projects to [AdaptiveCore](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/AdaptiveCore.lean)'s delayed trajectory under its actually retained gains. The finite-prefix theorem in [VaryingFeedback](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/VaryingFeedback.lean) yields

\[
E(s_N)\le (3/4)^{\lfloor N/3\rfloor}E(s_0),\qquad
E(x,y)=\max(|x|,|y|,|x-y|).
\]

Here `N` counts plant operations, each accompanied by paid acquisition and update. The theorem needs gain bounds only for this finite prefix. No hypothetical funded future supplies its certificate.

At exhausted packet inventory, another operation is disabled even though the retained gain remains safe. More generally, every actual event word is bounded by original total support, with residual support retained in the inequality. The inherited unbounded-credit theorem rules out an infinite execution under this finite closed account. Arbitrarily long separately provisioned finite histories are not one infinite funded history. Continued replenishment would require an explicitly added source law and account.

## Scope of the mechanism

The supplied elements are the delayed plant, safe gain menu, overshoot channel and calibration, observation-to-gain rule, phase sequence, packet conversion and costs. The construction demonstrates paid, consequence-mediated repeated revision compatible with a common regulation bound and finite continuation. It does not acquire the safe interval, establish the best switching criterion, derive a physical source of unlimited support, or identify ethical significance. Existing updater and method-formation studies remain relevant predecessors at their own scopes; their resources and endpoints are not silently imported into this new realization.
