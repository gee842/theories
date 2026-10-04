# Third review: transition and arrangement comparison

Reviewed current source for §§8–12, S8–S11, related X8/X10/X11 and TESTS. No manuscript edits. The independent arithmetic/closed-form reproducer is `counterexamples.py`; it ran successfully. The two findings below merit correction. Remaining items are lower-priority propagation or boundary notes, not additional claims that the overall design is disproved.

## 1. P2 — Preserving detection does not preserve the probability of stopping a breakout

**Location:** `src/core/b0_s11.md:40`, stable key `detectlink` as used in narrow E1; compare its definition at `src/core/50_s5.md:40`, and execution delay at `src/core/c0_s12.md:28`.

The narrow-E1 paragraph claims, with a theorem tag, that removing AI from strategic/escalatory decisions leaves breakout probability unchanged because detection is unchanged. The cited definition makes timely detection the probability of being **detected and answered** within the breakout time. The inference omits the response clock. With a decisive time of 2, detection at .5 and effective response taking .5, breakout probability is zero. Keeping exactly the same detector while human authorization makes response take 2 raises breakout probability to one. No stochastic assumptions are needed.

**Scope check:** This does not contradict the static delegation theorem. Its finite-speed survival comparison remains valid within its model. The error is the separate cross-model claim of unchanged breakout probability. X11:54 exempts bounded, reversible cyber defence from E1; it does not exempt an irreversible strategic/use-of-force response, which is explicitly in narrow E1's scope. An assumption that response latency is unaffected would save the claim, but is not stated or entailed by retaining the detector.

**Repair:** Say that narrow E1 leaves breakout probability unchanged *where it preserves the complete detection-and-response distribution*, and otherwise require measuring the latency change in C7 and verifying the enforceability bound after it. Retain the recommendation and static theorem with their actual conditions.

## 2. P2 — Rival verification still treats the repaired certificate as current independence

**Location:** `src/supp/10_S10.md:45–47` (`rivalverify`), propagated to `src/core/a0_s10.md:53`.

The proposition says a verifier with full inbound row sum below one “is captured by none” of the sources counted. Its proof invokes `certificate`(2), whose repaired conclusion is eventual removal, conditional on starting below the invariant full-capture boundary. A certificate bounds asymptotic amplification; it does not certify the verifier's present decisions as independent.

A zero-inbound verifier already suffices as a counterexample. Set normalized support initially 2, its decay rate .01, selection speed and cost 1, and captured share initially .99. Then row sum is zero throughout, but

`u(t) = log(99) + 200*(1-exp(-.01*t)) - t`.

At t=50 the uncaptured share is only `3.4896e-15`; only later does capture disappear (u(1000)≈−795.414). This is an exact trajectory of the same one-domain equations, not a different model. At the separately excluded endpoint x(0)=1, capture never disappears under this control.

**Repair:** Restate `rivalverify` as eventual removal under the certificate's initial-state and parameter premises. Separate certification of the conversion channels from a present-state independence test, including a transient/residence requirement before relying on the verifier's decisions. Propagate to §10's summary. This is an incomplete propagation of an accepted earlier fix.

## Lower-priority notes

- **Complete pooling endpoint** (`src/core/a0_s10.md:28`, `src/supp/10_S10.md:17`): “changes no choice and no ordering” needs β<1. At β=1, payoffs (2,1) become (1.5,1.5); strict ordering and selection disappear, and a relative objective is identically zero. The blanket prose at §10:27/34 also needs to respect the domain qualifications already given in part (2). The selected-positive-intensity conclusion under “others only” sharing is already correctly qualified in the detailed sentence, so do not relitigate that resolved result.
- **Comparative-static wording** (`src/supp/11_S11.md:8,15`, `relaxtrust`): the proof correctly handles raising R with other payoffs fixed, or lowering T with other payoffs fixed. Merely requiring T−R to fall with R>P−F does not imply g_C rises. At υ=.5, P=F=0, S=−1, changing (R,T)=(2,3) to (1,1.2) lowers T−R from 1 to .2 but raises the belief threshold from .5 to .5556. State the componentwise change or require dR−(1−υ)dT>0, holding P,F,υ fixed. Because “raising the value … relative to …” could be intended componentwise, this is a precision note rather than a top-level finding.
- **Reversibility propagation**: §12:36 now supplies the shared timing-and-independent-corrector qualification requested previously. S8:56 and X8:145,155,162,166 still describe temporary loss of overrule/capture categorically as irreversible, while X8:168–171 calls the proposed design's correction routes reversible. Update these cells to carry the shared condition locally or explicitly refer to it. Read with §12's new qualification, this is a propagation defect, not a fresh proof that the ranking fails.
- **Dwell endpoint propagation**: S11:91 now correctly says the dwell is an infimum and release must be strictly beyond it. S11:99 still says “iff ... held for T_min” and “minimum capture time,” as does core §11:93. Carry the already accepted endpoint correction through those statements.

## Repairs that should stand

- Readiness now registers the lower level at the threshold; the supplement correctly limits guarantees to the registered noise family and separates the indifference zone. I did not treat absence of operational institutional thresholds as a mathematical counterexample.
- Tier 2 now accounts for dormant execution means, execution delay and failure of actuation; advance commitment is no longer treated as removal of every enforcement problem.
- The pause statement now requires positive survival to the pause and a uniformly summable post-pause hazard envelope in its proof.
- The core's new shared reversibility qualification expressly restores the recovery-time condition for delegation and the before-loss requirement for standby service.
