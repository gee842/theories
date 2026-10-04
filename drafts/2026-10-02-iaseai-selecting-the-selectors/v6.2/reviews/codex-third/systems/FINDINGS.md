# Third review: systems and alignment, §§4–6 / S4–S6

Reviewed current source after the latest recorded repairs. No manuscript edits. Independent numerical checks are in `checks.py`; all pass.

## SYS3-01 — P2 — Applying the masked capability ceiling along a changing tax needs a relative-rate condition

**Keys:** `masked`, with `nested` and C9/C12. **Source:** `src/core/60_s6.md:71` (the two-premise finite-capability conclusion), `:75` (the tax is explicitly not fixed); `src/supp/06_S6.md:74–76`.

The fixed-positive-tax theorem is valid: holding S6's unindexed `c_k > 0` fixed, bounded sanctions `F ≤ F_max` and detection tending to zero imply `p_det F_max < c_k` beyond a finite capability. The scope issue arises when applying that ceiling while the tax also changes, an interpretation invited by the core's explicit statement at line 75 that the tax is not fixed. Such an application requires the positive tax not to fall faster than expected sanctions. Positivity at every capability does not supply that condition.

For the changing-tax extension, take capability `K ≥ 1`, `F = F_max = 1`, `p_det(K) = exp(-K)`, and tax `c(K) = exp(-2K) > 0`. Detectability tends to zero and sanctions remain bounded, but `p_det F > c(K)` at every capability. The within-type selection comparison favors countering at every capability, with no finite ceiling. This is not just a local sign example: along `K(t)=log(t+2)`, ordinary replicator dynamics is cumulative and the safe variant's payoff advantage is `1/(t+2)-1/(t+2)^2`, whose integral diverges. From equal shares, evasion tends to zero, reaching approximately `3.29742e-6` by `t=1,000,000`. This counterexample does not refute the theorem when its positive tax is held fixed.

**Repair:** explicitly state that the theorem holds the positive tax fixed. For applications with a moving tax, add a capability-uniform positive lower bound on it, or use the sharper relative condition `p_det(K) F_max < c(K)` eventually. If elimination by selection is claimed along a changing-capability path, also preserve the divergent-integral condition for the relevant payoff gap. C9 and C12 jointly determine that moving-path ceiling; merely keeping the tax positive is insufficient.

## SYS3-02 — P1 — The supplement retains the inference from failed assurance to vanishing survival that the core now withdraws

**Keys:** `masked`, `coverage`. **Source:** `src/supp/06_S6.md:78`, contrasted with repaired `src/core/60_s6.md:71–73` and `:83`.

The core now correctly says that an undetectable divergence can coexist with an intervention that makes residual hazard small, and marks the protection-standard response as a recommendation whose coverage premises are presumed rather than proved. S6 still says that beyond a shown-safe control capability, “nothing admission can see lowers the uncovered share,” concludes `(coverage lags)`, and directly invokes `coverage`. It neither derives the shrinking coverage ratio nor supplies `(residual floor)`. This is an incomplete propagation of prior SA-01, not an objection to the repaired core paragraph.

The old counterexample still applies verbatim to the remaining sentence: set `p_det,t=0`, let the uncovered share be one throughout, and let another intervention make the conditional irreversible-event hazard `h_t=2^(-t-2)`. Detection-based assurance fails maximally, but the hazard sum is `1/2` and limiting survival is approximately `0.577576190173`. Coverage lags alone therefore cannot invoke the loss-of-survival theorem; its independently stated residual-floor premise is false in this example.

**Repair:** bring S6 into line with the core: distinguish lack of an established assurance case from a claim about actual uncovered hazard, and invoke `coverage` only conditional on both of its named premises (plus shared failure for an every-actor result). Mark E2/E3 here as the same protection-standard recommendation as in the core.

## SYS3-03 — P2 — Bounded contest intensity does not establish a finite point of satiation

**Keys:** `enough`, contrasted with `boundedopt`. **Source:** `src/core/50_s5.md:90`; `src/supp/05_S5.md:117`; compare `src/core/60_s6.md:79` and `src/supp/06_S6.md:90`.

The last clause of `enough` says an objective bounded in the stakes is satiated. Its proof establishes only that replacing the prize with a bounded function bounds the equilibrium intensity. The supplied example `v(Ω)=1-exp(-Ω)` is strictly increasing at every finite Ω, so it has no finite point at which more becomes worthless. In the printed `n=4,r=1,c=1` contest, intensity is `3(1-exp(-Ω))/16`, positive for every Ω and tending to `3/16`; it does not stop. Thus this example cannot derive the earlier premise that hazardous variety stops growing at a need-defined level. The later `boundedopt` section already makes the relevant distinction between a bounded goal and a satisficer.

**Repair:** change the conclusion proved here to “a bounded prize bounds contest intensity at fixed costs,” and keep finite satiation / a stopping rule / a cap on hazardous scope as a separate premise. The finite-exposure theorem conditional on variety actually stopping remains valid; no changes to that result are needed.

## Repairs checked without a new finding

- `certificate` now excludes the invariant `x_i(0)=1` boundary and distinguishes eventual removal from a certificate for use at a decision. The pruning stability clause now excludes unit inbound gains.
- The fixed-power-law correction rate's sufficiency proof bounds the actual row sum uniformly below one for its stated initial and adjustment conditions. Its tracking condition is material and retained.
- The conditional-continuation interpretation in `detectlink` can represent delayed timing exactly; the explicit timing A/B formulas remain consistent with the one-period case. Do not repeat the former raw-payoff substitution objection against the repaired definition.
- `topology` now states independence across layers or the appropriate conditional probabilities.
- The core `masked` assurance/removal distinction is repaired; SYS3-02 is confined to the unrepaired supplemental inference.
