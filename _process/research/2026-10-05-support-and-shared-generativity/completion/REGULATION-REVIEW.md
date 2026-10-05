# Independent review of the constructed regulator comparison

5 October 2026. Internal collaborating-AI review for Ren. This checks the stipulated mathematical model and its implementation; it is not empirical validation or external peer review.

## Finding

**All 192 constructed-versus-absent comparisons favor the absent-regulator arm on the prespecified primary assays.** The saved cap-48 results contain 240 case-profile records: five arms, two sources, three horizons, eight profiles. The 192 comparisons are the four constructed arms against the matched absent baseline. They are related model calculations, not independent observations.

Every comparison remains unfavorable after crediting the constructed arm with its entire reported overflow probability. The smallest remaining baseline advantage is **0.00134475549**, at g=4, H=0.25, inert burden, profile (0,0,0).

At g=8, H=3:

| Event | Absent | Responsive |
|---|---:|---:|
| Protected plant remains active | 0.807110745338 | 0.315963873052 |
| Recycling, resident assembly and a free packet jointly, with activity | 0.692543383317 | 0.198790301728 |
| Regulator ever constructed | 0 | 0.817217913192 |
| Intact regulator remains | 0 | 0.369207859026 |

At reliability 0.5 and H=3, every constructed arm passes none of the eight profiles at either source; absent passes six at g=4 and eight at g=8. At H=0.25 the reliable regions are equal despite lower constructed-arm probabilities. Formation and useful performance are distinct outcomes.

No material reaction, accounting, or numerical implementation error was found that reverses this result. The candidate fails the declared comparison; it must not be reported as improving the tested plant functions.

## Independent checks

Read the complete [protocol](../../../../experiments/shared-renewal-capability/regulation/PROTOCOL.md), [primary code](../../../../experiments/shared-renewal-capability/regulation/compare.py), [experiment report](../../../../experiments/shared-renewal-capability/regulation/README.md), [physical note](PHYSICAL-REGULATION.md), and [lag proof](REGULATION-LAG.md). All primary result records were parsed and classified.

The new [checker](../../../../experiments/shared-renewal-capability/regulation/independent_check.py) and [check results](../../../../experiments/shared-renewal-capability/regulation/independent-check.json) never import or execute the producer. They reconstruct its 19 reactions using separate stoichiometric vectors and kinetic expressions.

- **Exact accounting:** all 3,009 physical states with weighted material N=3 and total packets U<=48, under ten arm/source configurations: 30,090 state/parameter combinations and 146,200 positive labeled events. Checks cover nonnegative successors, material conservation, all eight coordinate drifts, and the U/W/T/L/A identities. Cap-edge capture uses its actual untruncated target.
- **Bound constituents:** bound Y retains reproduction and its original wear rate; regulator wear is present in all three forms; GF fuel is counted in U and twice in W, but excluded from the free-packet assay. YG counts twice in material and W, and once in protected plant A. The A=0 face is invariant.
- **Lag:** exact integer generator powers recover construction coefficient kappa*g*(1+theta)/2 at order h³, its negative in the reserve-readiness difference, and bound-Y occupancy coefficient kappa*g*(1+theta)*mu/8 at order h⁴. These agree with the separate proof; they are not finite-horizon approximations used in the numerical comparison.
- **Independent probabilities:** separate graph construction and floating-point uniformization recompute 32 profile probabilities for g=8, absent/responsive, H=1 and 3, cap 48, plus formation, intact-regulator and overflow readouts. Other networks were audited and reclassified, not independently solved. Maximum profile discrepancy from the producer's matrix exponential is **4.05e-13**, below the declared **1e-10** comparison tolerance.

The selected independent graphs reproduce 1,857 absent states and 6,584 responsive states, with maximum exit rates 434 and 443. Integer generator rows sum to zero. Overflow preserves the actual capture rate and is triggered by total packets, not free packets alone.

The physical note also received a separate internal read-only proof review; no substantive issue was found in its finite-copy binding-sign proof or absorption extension. These establish scoped properties of the model, not a favorable full-process outcome.

## Numerical status

The run used Python 3.11.2, NumPy 2.4.6 and SciPy 1.17.1. The independent method sums a uniformization series rather than calling `expm_multiply`. Its weights, tail estimates and matrix products are floating point. The tolerance is a comparison threshold, **not a proved roundoff bound**.

Cap-48 maximum overflow is **1.64554749e-9**. The largest cap-32 to cap-48 assay change is **0.000171989621**. Every saved reliability classification is at least **0.00200705735** from its threshold, including the reported overflow allowance.

Finite success and success plus overflow bound model truncation in exact arithmetic. Neither solver encloses floating-point error rigorously. These are independently checked numerical findings, not the directed-rounding certificates of the earlier assay. The substantial margins support the reported signs without upgrading their arithmetic status.

Reproduce from the repository root:

```text
/private/tmp/meta-attractor-plot-env/bin/python experiments/shared-renewal-capability/regulation/independent_check.py
```

## Scope

The loss concerns the original plant functions and free-reserve tests. The new chemistry also supplies fuel-responsive binding, which those eight profiles do not assess as a separate delivered function. A common extended functional vocabulary could yield incomparable regions. Establishing that requires an explicit, paid regulation assay applicable to both arrangements; counting G species, formation, or isolated equilibrium responsiveness is insufficient. Such an extension would not reverse this completed negative comparison.

The eight profile inequalities do not prove stochastic dominance on every upward set of the full outcome space. They also do not order all physically implementable controllers or all future capabilities. No normative judgment or universal positive direction follows. The ledger shows where costs occur; attributing the entire finite-time loss to one event type requires a further causal decomposition.

## Provenance

HEAD at execution was `c5cf2ccec506936908b0c1b580c8f5d31e87fd74`; these regulation files were uncommitted working artifacts. The hashes below identify the actual bytes. All three primary artifacts were checked unchanged before writing the independent result.

| Artifact | SHA-256 |
|---|---|
| Protocol | `d8ca147ed3890f26203ac9c0d03f6e05dbdf7010dcd926c836e1cc429bb34747` |
| Primary code | `6b3163a619b28435cc016aefb14a92519bd459af27ee9fd9f380c73e5bf3c66f` |
| Primary results | `5c6221564684327c05484fe803069d19e2a8f4a0e12830785d83004ba387b87f` |
| Independent checker | `4079be96a5f60afeca198f107e40849f8faabe09eebccd95c42485f8bc83858d` |
| Independent results | `fa4b30e159597de7b18930199daeb1e953172a78eabadb82267af4bd4ab7ff71` |
| Physical note | `de69fe40bd6f693c0c99f6eb87fd062810d2b696eb6f8057be6dd6d036b6bccc` |
| Lag proof | `26a145703d6c27ef868e238bddd468ef3295fda14ac52bced683fcfb3280e4ea` |

The frozen protocol, primary code/results, shared indexes and common specification remain unchanged by this review.
