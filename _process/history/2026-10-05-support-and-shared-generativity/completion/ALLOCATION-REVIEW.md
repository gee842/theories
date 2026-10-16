# Independent review of paid allocation control

5 October 2026. AI-assisted review. **The local allocation theorem, paid finite-deadline comparison and early disadvantage are mathematically sound under their stated reaction law.** No missing active reaction or mismatch between the compared targets was found. This establishes a positive conditional mechanism from an equal regulator-free preparation; it does not revise the original G architecture's negative results.

## Reading and independent work

Read [ALLOCATION-CONTROL.md](ALLOCATION-CONTROL.md) in full, including the subsequently added short-time proof; read the complete [exact checker](../../../../experiments/shared-renewal-capability/allocation/exact_check.py) and [saved results](../../../../experiments/shared-renewal-capability/allocation/exact-check.json). Checked the proposed event change against the existing material/gate reaction table. Independently derived the local first-step equations, the successful and unsuccessful race probabilities, the finite-horizon timing argument and the cubic difference. Recomputed the displayed witness using separate exact rational arithmetic, without importing or running the producer checker. No parameter search or trajectory simulation was performed.

The clarification that the local background expectation excludes Y wear is correct: the separate factor exp(−ds) already charges that hazard. The background includes association, dissociation and gate wear. This makes the local finite-horizon comparison precise.

## Reaction and timing audit

The changed architecture suppresses bound reproduction through zeta=0. The earlier architecture had zeta=1 and cannot inherit this proof. Free-Y reproduction remains active, so protection must actually be constructed and bound before competition consumes the relevant precursor.

From S=(2,0,1,0,1,0,0,0), the construction race includes assembly, free-Y reproduction, Y wear and packet leakage. Initially C, D and all gate forms are absent, so capture, recycling and binding are disabled. Construction spends one R and the sole F, reaching one remaining R, one Y and one G. In that state the binding race includes assembly, reproduction and both constituent wear hazards. After binding, the selected route requires assembly before dissociation or either constituent wears; bound reproduction is disabled only because the new architecture specifies zeta=0.

After C assembles, there is no R or packet. Capture, C wear and total-Y wear have constant relevant rates g, b and d. Gate dissociation, rebinding or gate wear can occur meanwhile, but change neither C nor total Y. The final capture factor is therefore g/(g+b+d), and its relevant waiting rate is g+b+d, not the full microscopic exit rate. This distinction is correctly retained in the note and checker.

The absent-arm failure route—two reproductions, then leakage—has every competing rate in its denominators. It leaves R=C=F=GF=0, from which the stated network cannot create new R or C or capture a packet. A subset of eventual failures therefore gives a valid upper bound at every deadline. Other paths are not assumed to fail.

The four selected success phases have exponential relevant waiting times conditional on their successful outcomes. The Markov property justifies multiplying their race probabilities and phase-completion factors. Requiring each phase to finish within H/4 is a conservative sufficient condition for delivery by H. It does not omit the time spent constructing the gate.

## Exact witness and reversal

For the displayed parameter values, independent exact arithmetic gives:

| Quantity | Exact value |
|---|---:|
| Each of the three absent-failure race probabilities | 47/48 |
| Paid construction and binding race probabilities | 47/48 each |
| Protected assembly and capture probabilities | 1/4 and 2/3 |
| Relevant phase rates | 331776, 162576, 4, 6 |
| Absent success upper bound | 6769/110592 |
| Paid success lower bound by H=3 | 6627/55296 = 2209/18432 |
| Guaranteed difference | 6485/110592 |

The first five exponential-series terms give exp(3)>131/8>16. Thus every selected phase completes within three quarters of a time unit with conditional probability at least 15/16, and the product exceeds 3/4. The displayed bounds rigorously separate reliability 1/10. They are analytical rational bounds, not floating-point probability estimates. The large rate constants establish a nonempty declared parameter class; their molecular feasibility has not been identified.

The same task has a strict early disadvantage. Stop at the first fresh capture, with separate success and failure flags. Before stopping, total free-plus-bound fuel cannot exceed its initial one packet, so the process has a finite state space. For the common baseline generator Q0 and construction increment B, Bf=BQ0f=0. On transient states Q0f=gC·1{Y+YG>0}. Consequently only BQ0²f contributes to the third-order difference. Its value at S is 2kappa(ag−2ag)=−2kappa·a·g, yielding

\[
\Pr_{\mathrm{gate},S}(\mathcal E_h)-\Pr_{\mathrm{absent},S}(\mathcal E_h)
=-\frac{\kappa a g}{3}h^3+O(h^4).
\]

The saved exact third derivative, −1299456, and cubic coefficient, −216576, match the witness. Strict small-time disadvantage plus the positive H=3 bound proves at least one time crossover. Neither its location, uniqueness nor monotonicity is established.

## Accepted scope

The common event is **first fresh capture by the deadline with C and total Y present at that capture**. It is a delivered event. It does not require those structures or the packet to remain at the deadline. The initially supplied packet is excluded from the delivery count. Both arms start from the same S without regulator material, and the construction debit is inside the reaction law.

The supported path from the original preparation to S is valid, including its rate product and packet/material accounting. It does not extend the net advantage to that original preparation: construction competes along the approach, and the two arms can reach S with different probabilities and delays. The theorem also supplies no advantage of fuel-responsive switching over a constant inhibitor, no whole-capability-region inclusion, and no architecture-discovery or indefinite-renewal result. Material/work-equivalent accounting is explicit; chemical potentials, achievable rate constants and thermodynamic reverse pathways remain unidentified.

This is a substantive bridge: a physically specified competition can irreversibly remove the means of acquiring further support, while a constructed interaction can avert enough of that loss to repay its modeled cost. The result remains conditional on a supplied architecture, preparation, rate class and joint task.

## Provenance

Review-time HEAD: `fceb4f2bb89c98e5b93c3d3641d1f16893e87e8f`; these allocation artifacts were uncommitted. Inspected SHA-256 values:

- Note: `93ba1c7d550d64b3176e34c1826ae45889b0a68907e33d0c766825273be7f60b`.
- Exact checker: `421a1bb9b5bd8cdd1e85d4cc5f35381fc94a60869794bb2143ef9b1471873363`.
- Saved checker result: `3dcc31aeb217407dc3fcf8d77cbf7c45548bbd2f56f9aab23ae8a764a550d9d4`.

The saved result's checker hash matches the inspected code. No source, protocol, model or shared specification was changed by this review.
