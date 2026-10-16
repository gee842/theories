# Final independent review of the joint formation proof

5 October 2026. Internal collaborating-AI mathematical and conceptual review. This report covers the repaired proof in `joint-formation-math.md`, cross-checks the main `JOINT-FORMATION.md` report, and inspects the separately executed sensor/obstruction refinement. It does not claim external peer review or proof-assistant certification.

## Verdict

**ACCEPT for the explicitly specified conditional theorem and repertoire.** The material issues in `formal-review-initial.md` have been repaired. No additional mathematical repair is required for release.

Final reviewed SHA-256: `78588893049559c99f82c7886c3e9edc87e45209b48a6b90d0eba616fcfdb949`

This is the SHA-256 of the reviewed work file `work/development-02/joint-formation-math.md`. If the canonical mathematical appendix is copied byte for byte from it, the same acceptance applies. Changes to its content require checking the affected argument rather than merely retaining this hash.

## Why the repaired argument is sufficient

The proof now explicitly states that reserve B is the sole changing payoff-relevant inherited state in its class, and uses state-consistent finite-game continuations. This supports comparisons between safe and harmful admitted production that deliver identical cash: the operator cannot pay more for safeguarding in an unprotected profile while obtaining the same successor state. Historical patient harm is still reported, but is not silently assigned omitted strategic effects.

The cash-prefix identity and the selected-continuation invariant are correct. Crucially, the proof no longer pretends that every trustee deviation preserves the invariant. It bounds no-lesson and identity-route cash from above, independently of their off-region continuations. It also bounds warm open, cue, and optional evidence-only scores, allowing the operator to choose refusal for strategic reasons. The stated strict inequalities make the shared verified route exceed all these bounds.

The finite-horizon induction now joins the actors' choices. Given the high-region continuation value for N-1 episodes, the verified gate induces safeguarding; the trustee bounds establish its optimality and the cold learning choice; the attacked alignment branch optimally selects shared commercial learning and open production; and costly alignment suppression loses to no attack. The N=1 base case is immediate. This establishes an equilibrium selection and constant operator value throughout the region for every finite horizon, not merely a prescribed operator-response schedule.

The infinite-game extension is also adequate. The finitely branching history tree permits a pointwise convergent subsequence of finite-horizon pure equilibrium strategies. The persistent operator has uniformly bounded discounted payoff tails, and each dated trustee evaluates only its finite current episode. A profitable limiting-subgame deviation would therefore persist in sufficiently long finite games, contradicting subgame perfection. The construction proves existence with the strict selected high-region actions; it properly avoids claiming uniqueness of all off-path infinite strategies.

The Bellman-contraction observation is now explicitly restricted to a fixed trustee policy and used as corroboration. It no longer substitutes for whole-game equilibrium reasoning.

## Destructive attacks

The raid argument is correctly embedded in finite induction. With N periods left, any continuation after the current raid is bounded by r*S_N-k, while declining it permits the established protected continuation worth (r-c)*S_N. The strict bound k>c*S_N therefore rules out the raid even when it would send the account outside the viable region. The uniform k>c/(1-delta) bound passes to the discounted infinite game.

The proof correctly requires immediate actual payment, nonnegative later costs, and the universal gross-profit cap r. It explicitly excludes unmodeled loot or increased later production from that bound. The expensive-raid result is sufficient, not necessary; the cheap-raid harmful loop is a separate adverse calculation.

## Model and report correspondence

The cue witness now matches production: total cue-profile cost two, masking cost one-half, and warm masked score minus one-half. The optional evidence-only profile is clearly labeled as an analytical extension absent from the frozen computational menu. Its inability to displace the positive theorem's protected action is proved without claiming that every grid regime tested it.

The main report appropriately claims a constructive conditional solution of joint acquisition, selection, evidence/control purchase, finance, and reconstruction. It keeps the continuing account and role, physical technology, commercial ecology, primitive valence, and correspondence evidence explicit. It does not derive patient standing from acquired valuation or bargaining power. Cheap identity filtering and cheap precommitment against later care remain real failure boundaries rather than silently omitted counterexamples.

No empirical prevalence, human-psychology validation, unrestricted architecture optimum, or universal moral direction is inferred from the prototype. The acquired-concern mechanism and the institutional account objective remain distinct premises and modeled processes.

## Completed finite assay refinement

I inspected and reran `experiments/joint-formation/check_evidence_and_obstructions.py`. It passed eight stationary sensor/bypass cases, four rejected constant-cue cases, three self-data routing ambiguities, and 24 cheap-precommitment comparisons. It also explicitly reproduces two failures caused by changing polarity after calibration.

The sensor algorithm infers the polarity from received fixture signals; it does not read the hidden polarity when deciding release. For the stated stationary binary-transducer family and faithful fixture labels, its release mapping is correct. This is a completed finite identification refinement. It does not establish arbitrary reliability, justify fixture labels from nothing, measure the real cost of a sensor, or cover an unpriced attack on the fixture-to-operation relation.

The conceptual review has been updated to replace its earlier proposed-refinement status with this completed and limited verification record.
