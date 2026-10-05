# Integration development decisions and failures

5 October 2026. No held-out validation seeds were executed during these revisions. Development evidence uses only the four seeds named in `validation-plan.md`. This record distinguishes corrections from favorable-result tuning and preserves failed predictions.

## Initial v1

Implemented one persistent institution with ordinary contractual revenue, separate A/B outcomes, checking upkeep/rebuilding, runtime rule toggles, explicit council votes, and fresh prospective package checks. Seed 1103 demonstrated the main emerging path: a B grievance led to an inclusion vote and a package improvement. The initial material stress consumed resources and delayed inquiry, but did **not** destroy and rebuild the checker as anticipated. Simple and independent-noise controls showed no successful rule change. A transient opportunity passed before sufficient review funding accumulated. Low income exhausted service capacity.

Initial traces remain in `development-v1-seed1103.json`.

## v2 correctness and design corrections

Independent review identified several repairs:

* Freeze the actual installed incumbent. An initial automatic refit before the final check was an unannounced deployed model change; it was removed. Only an accepted candidate package can replace the installed package.
* Price coarse fitting, inner-validation forecasts, and both pilot forecasts consistently with final paired computation.
* Replace side-effecting `assert pay(...)` calls with explicit required payments, so optimized Python cannot remove transactions.
* Add chronological transaction hashing and per-round payment/receipt/minimum-balance records, plus optional full transactions.
* Keep context observation inside the world interface, precommit forecasts before outcome settlement, and use the root-approved synchronous settlement convention. No future receipts are spendable.
* Freeze and log forecast vectors, mandate, costs, stage keys, `W`, sample size, and alpha before final checking.
* Reject candidates with nonpositive enacted-target pilot gain before buying confirmation. The previous version unnecessarily confirmed candidates whose exploratory result already opposed them. Fresh checking remains separate for candidates that pass screening.
* Derive the ballot's next-payment guard from configured prices rather than a hardcoded amount.

The material-stress invoice was deliberately increased from 10 to 20 for ten rounds, and its return to the simple B relation was moved from round 300 to 400. This development intervention exercises the intended loss/rebuild pathway; it is not an estimated realistic shock. The original weaker shock's failure to cause loss is retained above and in its trace. The stronger shock caused loss/rebuild in development. The eventual substantive held-out result will be reported without further tuning.

Intermediate traces remain in `development-v2-seed1103.json`.

## v3 staged financing and final arms

The initial 140-unit review-wallet gate required near-maximal funding before knowing the candidate, purpose decision, or support width. Root and adversarial review identified that avoidable policy choice as a confounder in discovery delay. It was replaced by staged financing: afford the priced opening/construction/pilot/hearing plus reserve, then fix and finance the actual fresh-check size. Paid attempts that cannot finish are logged and consume their alpha index. A purpose change can persist through an unfinished check, with later genuinely fresh reconsideration.

The final five arms are full, fixed mandate, fixed rule, no renewal, and incumbent-only opening. The sixth proposed free-checker arm was not added. Centrally represented stakeholders with explicit causal votes are the scope; no decorative agent registry was added to imply independent adaptive minds.

All 120 development combinations (four seeds, six scenarios, five arms) were run. Main observations:

* Emerging full runs changed mandate and installed one rule/package in all four seeds; B errors were 36, 37, 46, and 45 of 700 services. Each ablation retained 303, 335, 327, and 326 B errors respectively.
* Material-stress full runs lost and rebuilt checking capability and made two package/rule changes in all four seeds. B errors were 80, 73, 83, and 79, compared with 153, 147, 157, and 151 in the ablated arms.
* Simple tasks needed no rule revision; protected exploration still cost money.
* Noise led to mandate expansion in two full seeds, but no rule/package adoption in any development seed. Purpose choice remains fallible and distinct from validated method improvement.
* Transient runs expanded the mandate, but the useful interaction ended before a funded fresh confirmation; no package change was installed.
* Poor-income full runs served only 365, 366, 365, and 356 requests per group before exhausting funds. The no-renewal arm served all 700 in each seed. Lower observed error counts in the failed full service therefore cannot be treated as improvement; unserved requests remain part of the fixed comparison population.

These observations are development diagnostics, not held-out estimates. No unsuccessful seed was removed.

## Final payment chronology correction

Root found that fitted-table charges occurred after calling the fitting routine, despite sufficient funds already being reserved. A charge callback now pays for coarse/singleton work before that work, and pays for the chosen pairs before their fitting. Amounts and all behavioral outputs are unchanged. All 120 development result records compare exactly before and after this fix. Their canonical digest is `98847c0a48af5ba0e0bb79fb64d5f52ee20aad5066ae2d1326dfaef5388cd977`; `prepaid-fit-correction-check.json` records the comparison. Transaction ordering/hashes and source hashes necessarily changed.

`development-v3-all-seeds.json` contains all final development records. Independent adversarial and purpose-integration audits are separate files. The root will create a combined freeze manifest including implementation, helper, evaluator, and audit sources before held-out execution. Any later correctness correction must be disclosed and trigger a full validation rerun; a merely unfavorable substantive result must remain a result.
