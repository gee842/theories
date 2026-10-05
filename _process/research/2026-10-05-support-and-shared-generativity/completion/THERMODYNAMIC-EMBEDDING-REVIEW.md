# Independent review of the reversible allocation embedding

5 October 2026. AI-assisted mathematical review by the integrating agent, separate from the construction's author. Read the full [proof](THERMODYNAMIC-EMBEDDING.md), [prospective algebraic protocol](../../../../experiments/shared-renewal-capability/thermo-embedding/PROTOCOL.md), checker source and saved results. No numerical simulation or independent rerun was needed or claimed. This is an independent analytic/code inspection within one collaborating AI team, not outside peer review or physical validation.

## Verdict

Accept the finite stopped-event embedding and perturbation argument at their stated scope. The single standard-potential assignment makes all retained reversible pairs consistent, including the large reverse factors required by strongly bound complexes. The analytical probability margin survives the certified unmatched-event bound. The result is stronger than backbone/work accounting and does not identify a molecular implementation.

## Checks

- The two conserved totals count GF in both the backbone and carrier inventories, and YG twice in the backbone inventory. H_f and L_f are finite carrier species. The initial F=H_f=L_f=1 preparation is explicitly charged to both arms.
- For reactant/product complexes alpha and gamma, the prescribed ratio exp[-phi·(gamma-alpha)] gives pi(n)q_forward(n)=pi(n')q_reverse(n') after factorial cancellation. The checker implements falling factorials, including Y(Y−1) for the reverse reproduction reaction.
- The unchanged binding ratios require potentials GF=4M−ln K_F and YG=2M−ln K_Y. Bound-wear reverse factors K_F exp(−M) and K_Y exp(−M) are retained. Omitting them would invalidate the claimed thermodynamic embedding; this construction does not omit them.
- Before the first forward capture on an original trajectory, H_f=1 and U≤1. Therefore g H_f C equals the original gC exactly until the stopped event. A reverse reaction producing F is not credited as a capture. After the first added reaction, the coupling is allowed to diverge; it does not require later carrier stocks or forward hazards to match.
- The reverse-rate envelope independently decomposes into: exp(−M) times 3(a+b+d+g+delta), 6 beta, 4k(1+theta), 3delta K_F and 2(delta+d)K_Y; exp(−3M) times 2ell+6ell_b K_F; and exp(−4M) times 6kappa. These yield the recorded coefficients 657116, 3666 and 974592. Conservative maxima need not occur simultaneously.
- The degree-seven positive Taylor sum for exp(5) is 2701/21>128, hence exp(−20)<2^−28. The rational bound is below1/400. Applying error below3/400 to each H=3 probability preserves the common0.1 reliability threshold and a strictly positive gap greater than120653/2764800.
- Removing both directions of the construction pair in the reference preserves detailed balance on the remaining edges. Other reverse channels can create G; the reference is therefore an approximation to the old absent-gate law for this finite event, not an exactly gate-free physical process for all time.

The saved exact check covers 512 states, 16 reaction pairs and 1,915 enabled forward/reverse identities, with the envelope checked on96 original pre-capture states in each arm. Those counts are the author's executed computational audit. This review verifies its implementation and mathematical role without presenting the same output as a second execution.

## Boundaries that must remain in the integration

1. The original reduced W is not the actual thermodynamic free energy. The construction assigns standard potentials and count-dependent mixing terms separately. Four packets in the separate turnover theorem is a minimum in that theorem's declared ledger, not a conclusion about4k_B T or this embedding's minimal chemical work.
2. H_f=1 suffices for one stopped capture. It cannot supply the four captures of the full turnover construction. A multi-capture embedding needs a larger explicit preparation and a bound on depletion-induced forward-rate changes, or a supplied chemical work source with its own ledger.
3. Reverse wear removes the old absorbing boundary. The old extinction and exact early-time coefficient claims do not automatically transfer. This finite chemical system relaxes toward detailed-balanced equilibrium; it is not a maintained chemical nonequilibrium steady state.
4. The construction retains the earlier comparison of channel-enabled versus channel-disabled laws. The separate material-fabricator theorem changes that modeling premise, but has not been embedded in this thermodynamic construction. Their successes cannot simply be multiplied into a single completed physical theorem.
5. Standard-potential compatibility does not establish attainable molecular specificity, absolute rates, elementary mechanisms, preparation cost, spatial mixing or identifiability. These remain physical obligations.

No correction to the submitted theorem was required after this inspection. Scope clarifications about carrier depletion, reverse seeding and finite-event transfer were communicated during development and are present in the reviewed source.

## Reviewed bytes

- Proof: `77eefb42eddb97b76ef4e6d3335d732a2e84874e415d5d2323b47c40638312b8`.
- Protocol: `30705808c424850c0c3ead30d3133ffef638997d999e94a8409a82465bc52894`.
- Checker: `4f9ceea0f9964b291fbe1bd45ec49822eb9bcf6f609fa936252f65cacd9f24ff`.
- Result JSON: `4e2de729860d5abbb258e880d5fe73000481adc2a1965a51f8f5b3d54e6d4b73`.

The primary-source record belongs to the proof's author and states the sections inspected. This reviewer additionally verified the Rao–Esposito publication identity and abstract at its linked arXiv record, without claiming to independently reread its entire derivation.
