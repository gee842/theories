# V7 transition corrections

Implemented only the ten assigned source units, plus this note and `verification/transition_checks.py`. No v6.2 files changed. Stable declaration keys are unchanged. Ren's E1/[E2,E3] branch and the trust/verification passage in §11 are verbatim; the shared-fate framing and values remain intact.

## Implemented

- **Rival verification:** `rivalverify` and §10 now state eventual removal under the certificate's initial-state and fixed-margin premises. A zero-inbound-row, strongly captured transient demonstrates the limit. X10 requires a present-state/residence assessment of captured share and inherited support in addition to a channel certificate before executive force is assigned or restored. §12's estimators and coercive correctors carry this distinction.
- **Narrow E1:** unchanged detection preserves breakout probability only if the complete detection-and-response clock is preserved. Human authorization latency enters C7; X10 includes drills of that clock and X11 carries the qualification. The static certain-lock theorem and Ren's branch remain unchanged.
- **Reversibility:** S8's method, X8's table and §12 apply the surviving-independent-corrector and before-loss conditions to every path. Temporary capacity loss can recover when the interval remains available. X8 now includes an explicit irreversible branch for a design's masked hazard, failed standby or delayed repair. The ranking remains a provisional value judgment; no probability advantage is inferred from a merely named remedy.
- **Risk-bound propagation:** removed the remaining §8/§12 summaries saying every worst case necessarily exceeds the tolerance. A possible irreversible branch does not imply a probability bound above tolerance; comparative bounds remain unestimated.
- **Pooling:** β<1 preserves ordering while scaling selection speed; β=1 makes relative payoffs neutral and every choice optimal for the relative objective. Positive-interior intensity formulas require a positive effective prize. Broad headlines now concern divisible-prize sharing among all, with the other conventions qualified.
- **Additional same-formula domain correction:** under others-only sharing, positive effective prize for every β requires Ω_s > (ϱ n/(n−1)−1)Ω_e. The older Ω_s>Ω_e/(n−1) is the ϱ=1 special case. The proposition and proof now agree at arbitrary stated promise reliability.
- **Trust:** the comparative statics hold other relevant primitives fixed; a fall in T−R alone is insufficient. Lower exit incentives require reducing a positive relative premium while holding its absolute part fixed. A common intervention relaxes all three constraints only if all three required changes are established.
- **Dwell:** the boundary is an infimum; successful release from the capture basin is strictly later, with a margin. `capturebasin` distinguishes entry into the basin from asymptotic arrival at the absence equilibrium and excludes the invariant x=1 start.
- **Fudenberg–Koh:** checked the full primary source, Theorem 1(c), Definition 4 and the following discussion: [Cooperating against Catastrophe, v1](https://arxiv.org/html/2609.28291v1). §8 and X8 now say the constructed pacing profile is an MPE at high effective hazard while the everywhere-racing profile is not. There is no high-hazard uniqueness claim. The constructed profile can race indefinitely from an unsafe initial state; equilibrium existence does not by itself establish E3's realized path. The private-capability/monitoring-lag extension remains acknowledged, and mapping this paper's mechanisms into the source's effective hazard remains explicitly open.

## Verification

`python3 verification/transition_checks.py` passes all seven independent standard-library test groups:

1. Identical detector with delayed response changes breakout probability 0→1; preserving total timely response preserves it.
2. Row sum zero can coexist with captured share exceeding 1−3.5e−15 at time 50; eventual removal and a controlled present-state case both checked.
3. Partial and complete payoff pooling.
4. General promise-reliability bound and cancellation of a positive positional prize under others-only sharing.
5. The trust counterexample and valid componentwise changes.
6. Releases on opposite sides of the dwell boundary, checked at two RK4 resolutions; the exact saddle remains fixed.
7. An exact constant-hazard case satisfying Fudenberg–Koh's high-hazard condition whose pacing profile races indefinitely from above the cutoff. At α=2, β=1, discount=3, safety speed=.5 and hazard=2, the cutoff is log(4)/10, derived directly from the waiting and racing payoffs.

A separate source check confirms stable keys and the protected Ren branch/trust paragraphs. No full assembly was run here, to avoid conflicting with the root's build.

## Propagation for the root

- **EVIDENCE EV11 / TESTS research-status prose:** replace any remaining “unique pacing MPE,” “abstract only,” or “needs the full paper” description with the source scope above. The mapping between models still needs work; source reading itself is done.
- **TESTS C7 and tier-2 estimator:** state total detection plus effective response under the proposed human-authorization procedure. A detector-only latency is not the measure.
- **TESTS C2/C4/D4 and claims about certificates:** distinguish valid conversion-channel certificates from measured present independence; include inherited support and captured share, especially after reassignment or recertification.
- **CLAIMS / LEDGER:** update `share`, `rivalverify`, `relaxtrust`, `dwell`/`capturebasin` scopes and record that the repaired reversibility comparison now includes late/failed design correction explicitly.
- **Front matter:** no guarantee that every worst-case probability crosses the tolerance; no generic claim that pooling changes no choices at β=1; no broad claim that any positive positional prize forces positive selected intensity under every sharing convention.
- **Checks:** the independent verification script can be run separately or included in V7's verification entry point. Do not relabel its seven test groups as seven manuscript theorems or an empirical validation.

## Final systems-audit propagation

The additional masked-admission joins in §8, X8 and §12 C12 now distinguish deterrence (detection × enforceable sanction versus the changing C9 tax) from independent assurance. Falling detection alone is not failure if the tax falls faster. E2/E3 and capability bounds following missing assurance are protective recommendations, preserving broad E1 as the preferred branch, not consequences of an unproved residual hazard floor. The tier-2 masked-class trigger now refers to an independently assessed safety case failing rather than detection decline alone.

The independent script now has **eight** passing groups; its added test checks both the fixed-tax failure and faster-falling-tax success cases, and a summable realized hazard despite zero evaluation detection.

A final read-only scan found these active external propagation points (reported to the root, not edited here): S9's masked-admission paragraph at `src/supp/09_S9.md:15`; the detector-only masked trigger at `src/reg/TESTS.md:150`; and the EV11 lag-extension sentence at `src/reg/EVIDENCE.md:198`, which had inverted high risk into removal of pacing instead of pacing sustained at every lag. The definition-like conditional “where every worst case crosses the tolerance” at `src/core/10_s01.md:27` and START-HERE:39 is not itself a new theorem error, but could be aligned with §8's unestimated-bound language. Historical ledger quotations were excluded from stale-claim findings.
