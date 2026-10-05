# Independent review of delivered continuation

5 October 2026. AI-assisted review. **The assay semantics, labeled-generator construction and selected independent calculations pass.** This is a fixed follow-up to known model results, specified before its own computation. It is neither empirical evidence nor a new favorable physical architecture.

## Scope and method

Read the full [protocol](../../../../experiments/shared-renewal-capability/continuation/PROTOCOL.md) and producer; audited all 24 saved networks, 72 horizon cases and 1,152 profile probabilities. The sixteen sequential profiles require selected recycling, assembly and fuel conditions at H, optional additional assembly during (H,H+tau], and productive survival throughout. They differ from the old eight-profile vocabulary, whose survival requirement ended at H. The physical reaction law is unchanged; the g=1 comparisons vary the supplied Y-recycling coefficient only.

The primary calculation correctly removes the off-diagonal rate of every **labeled** later C-assembly event while retaining that rate in the generator diagonal. Historical assembly flags can already be saturated: they must not suppress the counting of another actual assembly. If C denotes the assembly-arrival matrix, Q−C describes no-later-assembly paths. Subtracting its surviving mass from ordinary surviving mass gives the requested later-event probability. Since A=0 is invariant, positive final A is equivalent to positive A throughout the trajectory from the declared preparation. Overflow is absorbing failure.

The [independent checker](../../../../experiments/shared-renewal-capability/continuation/independent_check.py) never imports either producer. It uses the previously independently reconstructed stoichiometry, freshly specified propensities including theta, and its own sorted reachable graphs. Exact integer checks cover material/work increments, dead-face invariance, zero generator row sums and the assembly killing rate. Instead of subtracting two probabilities, it marks whether a later assembly has occurred, with generator

\[
M=\begin{pmatrix}Q-C&C\\0&Q\end{pmatrix}.
\]

Its off-diagonal entries are nonnegative and rows sum to zero. Starting the later interval in the unmarked block and reading productive survival in the marked block counts an actual later assembly directly.

At cap 48, four prespecified cases were independently recomputed at all three horizons: g=1/theta=0 and 4 without G, and g=8/theta=4 without G or with the responsive architecture. All sixteen profiles were checked in each case: **192 probabilities**, plus prefix masses, fuel partitions and overflow. Maximum profile/prefix discrepancy was **3.675e−14**, below the declared 1e−10 implementation tolerance. Both implementations use SciPy exponential actions, but different response constructions and independent event/state reconstruction. Agreement does not provide a rigorous roundoff enclosure. Full results and input hashes are in [the check record](../../../../experiments/shared-renewal-capability/continuation/independent-check.json).

## What the result establishes

For the primary profile (1,1,0,1), the cap 64 repeated-delivery probabilities at g=1 are:

| H=tau | theta=0 | theta=4 |
|---|---:|---:|
| 0.25 | 0.000274953 | 0.001474052 |
| 1 | 0.041728852 | 0.088337499 |
| 3 | 0.072436907 | 0.103997669 |

Thus the earlier loss of free-fuel readiness under stronger recycling does not establish impaired repeated delivery. Both remain below the declared 0.5 reliability threshold on this primary test. The comparison concerns different supplied catalytic coefficients; it does not charge a physical process for discovering or constructing the larger coefficient.

The regulator failure also survives the new functional test. All **384 distinct constructed-versus-absent profile comparisons at cap 64** have lower success under construction. Their truncation-difference upper bounds, evaluated in floating point, are also negative. The weakest deficit is approximately 0.0007111021. At g=8 and H=tau=3, absent-regulator primary success is **0.6585510308**, versus **0.0296658779** for the responsive arm. At that case and reliability 0.5, all sixteen sequential profiles pass without the regulator and none pass with any constructed arm. This conclusion is confined to the declared vocabulary, preparations and horizons.

Fuel strata partition the primary event correctly; the maximum saved partition residual is 1.11e−16. Entry probabilities and joint successes are retained separately. Conditional success compares different selected populations, not interventions that add or remove a packet. For example, in the responsive g=8, H=3 case, conditional later success is about 0.1411 among zero-fuel entries and 0.1181 among positive-fuel entries. This does not show that fuel is harmful: the strata differ in their other state coordinates and histories. No causal fuel-effect claim follows from either ordering.

## Numerical limits and provenance

Maximum cap-48-to-64 change across all profiles is 4.01018e−8. Maximum initial-preparation overflow through H+tau is 4.01545e−8 at cap 48 and 1.16112e−14 at cap 64. In exact arithmetic, finite success is a lower bound and adding overflow is an upper bound for the original process. The current floating values are not interval-certified endpoints. All saved half-reliability classifications agree with the protocol; none is numerically unresolved, and the smallest threshold separation is about 0.0002410673. The minimum saved subtraction value is zero; no negative value was silently repaired by this checker.

The result supports separating stock readiness from delivered continuation. It supplies neither indefinite regeneration, an ordering over all possible functions, a benefit of this G architecture, nor emergence of a useful architecture. It preserves the earlier negative experiment while testing a further function in the same process.

Check-time HEAD was `fceb4f2bb89c98e5b93c3d3641d1f16893e87e8f`; continuation files were uncommitted. Every producer input hash matches current bytes. The primary results hash is `8996ff812ed000f8cc5dff4194b16ca5e68979067bc7d05eaf87ccc34a8e6234`; complete source and checker hashes are preserved in the check record. No model, protocol or producer file was edited during this review.
