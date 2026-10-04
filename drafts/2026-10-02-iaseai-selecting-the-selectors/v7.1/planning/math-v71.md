# Mathematical readiness corrections for V7.1

Implemented 4 October 2026 in V7.1 only. V7 and earlier versions were not edited. Result declaration keys and their order are unchanged; no assembly or generated-document edits were performed by this reviewer.

## Changes

- R1 and the necessary part of the safeguards theorem now require constant-speed replicator selection when liability changes sign relative to the private advantage. The cumulative-selection definition explicitly supplies its one-sided bound only on positive-gap intervals. The earlier positive-gap load result is retained. S9 derives the exact signed-gap identity and gives a smooth payoff-monotone cumulative counterexample to the broader claim. The safeguards margin is stated from the state when it takes force; a varying margin can satisfy the sufficient pointwise bound without satisfying a constant-margin necessity claim. Files: `src/core/30_s3.md`, `src/core/90_s9.md`, `src/core/a0_s10.md`, `src/supp/00_S0.md`, `src/supp/09_S9.md`, `src/supp/10_S10.md`.
- Concentration and objective narrowing are distinct. S3 supplies a fixed-prize case with stable equal standing, a positive relative continuation premium, and no common premium. The core points forward to that distinction. Files: `src/core/20_s2.md`, `src/supp/03_S3.md`.
- The correction requirement's scope comparative static is conditional: at fixed total size and cost factors, increasing the return while not lowering conversion into evaluation raises the requirement. Diversification at fixed total activity has either sign depending on cross-domain conversion. The explicit reversal keeps evaluation separate from occupied domains. Files: `src/core/40_s4.md`, `src/supp/04_S4.md`.
- Functional protection and shared cognitive understanding are separated. Pure common benefit remains invisible among otherwise alike carriers; correlated local benefits and existing constraints can protect without a cognitive model. Shared understanding remains the author's proposed route to deliberate coordination, not a necessity theorem. Files: `src/core/30_s3.md`, `src/supp/03_S3.md`.
- R5 and independent assurance apply on every branch, broad E1 included. A zero tax removes the specified selection pressure; it does not establish adoption, persistence through entry or replacement, or safety. R4/Q7 allow equally effective durable containment and require a verifiable disposition of built capability. Files: `src/core/90_s9.md`, `src/core/a0_s10.md`, `src/supp/09_S9.md`.
- Test G now establishes objective sensitivity in its specified game, strongest at intermediate escape probabilities when decisive value exceeds cooperation; it does not establish discrimination against a specified rival theory of structural realism. Files: `src/supp/05_S5.md`, `src/supp/14_S14.md`.
- The load proof now refers to the combined share of maximal-load carriers, allowing tied race carriers. Current supplement title/script references use V7.1. The counterexample and numerical indices retain V7 block RV and add V7.1 block RP. Files: `src/supp/03_S3.md`, `src/supp/00_S0.md`, `src/supp/10_S10.md`, `src/supp/14_S14.md`, `src/supp/15_S15.md`.

`src/supp/02_S2.md` was inspected and needed no edit. Required opening, Chinese-guide and current-CLAIMS propagation was sent to the parent reviewer; the parent owns those changes. Historical CLAIMS sections were not edited.

## Verification

`verification/readiness_checks.py` is standard-library-only and exposes `run_checks()`, returning a dictionary with eight named successful groups, raising on failure. Both standalone execution and `python3 checks_v71.py RP` pass; the integrated block reports eight gates passed and zero failed.

| Group | Witness and retained result |
|---|---|
| `cumulative_counterexample` | Average liability 6/7, positive cumulative advantage growing by 0.2 per cycle, but race logit falling by 2 per cycle. Analytical host floor 0.988252565; independent integrated minimum 0.999674536. |
| `constant_speed_replicator` | Same liability path raises logit by 0.2 per cycle at unit speed; host crosses its 0.3 floor at about 68.755. Both host integrations agree under step halving. |
| `narrowing_without_concentration` | Structural gain 0.5; relative price 9/19 exceeds common price zero while the exact stock gap contracts by 0.9 per period. |
| `fixed_total_scope` | Independent capacity optimization and correction-root search recover requirements 1 to 0.70710678 under diagonal conversion, and 1 to 1.22474487 under stronger cross-domain conversion. |
| `functional_without_cognitive` | A protective trait with local benefit above cost rises from 0.1 to 0.99959157 by time 100; removing the local benefit preserves the otherwise-alike negative selection result. |
| `fixed_verified_containment` | Bellman iteration with fixed credible punishment gives cooperation value 1 against deviation value 0.2 at escape probability 0.001; the bound is 0.00988889, and a 0.02 escape control fails. |
| `noncompetitive_growth` | Exponential hazardous variety against linear coverage leaves a residual hazard at least 0.005 from time 3, independently of a competition variable. |
| `zero_tax_without_safety` | Zero tax is neutral selection while an independent constant hazard still drives limiting survival to zero. |

All declaration-key sequences in the fourteen owned/authorized source files were compared against V7 and are identical. Control-character scan passes. The parent runs full assembly, reference validation and the default numerical suite.

These are analytical witnesses and numerical regression checks, not an empirical calibration, a proof of punishment credibility, or certification of every inherited theorem or complete institutional design. The repairs resolve the material findings assigned to this reviewer; publication-ready status still requires the broader evidence, interface and human specialist review identified in the readiness assessment.
