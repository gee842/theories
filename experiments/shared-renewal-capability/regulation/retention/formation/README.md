# From absent variants to differential reconstruction

6 October 2026. AI-authored development under Ren's unified-foundation roadmap. The [mathematical account](../../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FORMED-VARIANT-SELECTION-MATH.md) joins paid variant formation and local consequence return in one law. The [protocol](PROTOCOL.md) records the analytically chosen fixture, its pre-run correction and the comparisons.

Initially there are no response molecules and no associations. A damaged capture site can produce either of two response types at equal rates and equal cost. Either type can associate and copy; only A repairs. A repaired site captures real fuel, which its resident can spend on copying. Formation remains active whenever its physical conditions hold. No stage installs a preferred founder, a seeded contest, fresh precursor or replenished fuel.

The available chemistries, type inheritance, site and local-access reactions are supplied. This is a conditional construction of their instances and consequences, not their origin from unspecified physics or an empirical chemical model.

## Main result

The primary preparation has precursor M=3, common fuel F=4, incident source E=1 and a damaged, vacant, locally empty site. Productive rates are one; damage, wear, leakage and symmetric bulk copying rates are 10⁻⁶. At H=12 the following are rounded readings of the outward enclosures in [results.json](results.json):

| Arm | Expected A−H | A copies with H already present | Fresh captures | Expected A fraction, empty population assigned 1/2 |
|---|---:|---:|---:|---:|
| Effective local return | 0.113318292 | 0.046659551 | 0.113331714 | 0.522220962 |
| Repair disabled | 0 | 0 | 0 | 0.500000000 |
| Equally priced ineffective repair | −0.000000059 | 0 | 0 | 0.510444397 |
| Capture disabled | 0.000000405 | 0 | 0 | 0.514444249 |
| Copying disabled | 0 | 0 | 0.113331827 | 0.514444270 |
| Shared return and common copying | 0.027209847 | 0 local copies | 0.051019833 | 0.504535138 |

The primary positive abundance comparison exceeds the conservative analytical bound 0.00387 against both repair controls. Copying while H is present separately exceeds 0.00638. The zero-loss terminal values are exactly **17/150** for expected A−H and **7/150** for that mixed-copy mark. The mark is counted across all histories, with zero on failed histories; no conditioning on successful or surviving populations is used.

**Different statistics answer different questions.** Copying-disabled dynamics have equal expected A and H counts but a mean A fraction above one half. Population sizes correlate with composition because A can change resource consumption and stop damage-triggered formation. An average fraction alone would falsely suggest a copying-selection effect here. Likewise, the shared-return arm has positive expected abundance contrast; the earlier fixed-seed frequency martingale cannot be applied to this process with ongoing formation. The ineffective-repair arm also lacks full type-swap symmetry. Only the repair-disabled arm has the exact symmetry used to conclude zero expected contrast.

The distinction is structural, not a quirk of the empty-population convention: that population is empty with only very small probability in these primary comparisons. Neither abundance, frequency nor capture is a universal measure of generative success.

## Paid history and failure boundaries

One positive path is:

**H forms → A forms → A associates → A repairs → fuel is captured → A copies while H remains present.**

The first four events spend all four common fuel units. The last event spends newly captured local fuel. Both variants and their actual competition for precursor are present before repair. Lean proves a matching lower bound: an intact site with H present, reached from this initially empty organization under the base law, requires at least four initial common fuel units.

Three units can support a useful clonal founder but cannot support that mixed route. This exposed a weakness in the initial M=2,F=3 proposal before the main numerical run; the smaller model remains a diagnostic. Fewer than three common units cannot bootstrap repair and capture from absence regardless of incident source size.

The [formal counterpath](formal/README.md) also preserves a failure of contributor-specific return: with more starter fuel, A forms and repairs, wears out, and H forms/associates and uses the repaired site to copy. The primary four-unit fixture's lack of H local copies therefore does not establish universal protection against appropriation.

With catalytic repair loss σ=10⁻⁴ and other nuisance rates 10⁻⁹, changing only E from one to zero reverses expected A−H at H=12: approximately **+0.113297003** versus **−0.000011333**. Both signs have separate analytical bounds. The same work chemistry can favor or disfavor its useful type depending on accessible source support. These rates are an uncalibrated existence witness. The response does not learn to alter its rule when its source disappears.

All positive-wear finite-stock cases eventually lose every response molecule. Their terminal A−H is zero. The observed advantage and its bounds concern the declared finite horizon, not an enduring evolutionary attractor.

## Verification

[process.py](process.py) enumerates the complete reachable graph, keeps channels with distinct event meanings separate, and computes exact terminal expectations by rational backward recursion. The strict rank 4E+2(F+f)+c+A+H decreases on each base event; controls and catalytic-loss events also decrease it. Finite-time expectations use outward nonnegative interval arithmetic and rational exponential/Poisson-tail bounds from the [previously reviewed implementation](../model.py), with the dependency hash recorded.

```sh
python3 check.py
python3 independent_check.py
python3 formal/check.py
```

[results.json](results.json) records nine primary arms, four fuel diagnostics, the clonal fixture and two source/work-cost comparisons. It preserves event counts, population observables, exact terminal rewards, path probabilities, source hashes and numerical enclosures. The independent checker reconstructs the process separately; its numerical agreement is not itself a proof of directed rounding. The [internal review](../../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FORMED-VARIANT-SELECTION-REVIEW.md) states the accepted scope and limitations.

The [Lean package](formal/README.md) adds 53 audited theorem declarations for discrete transitions: fuel and precursor accounting, formation ancestry, truthful copying, bootstrap and mixed-history resource bounds, the concrete mixed path, an appropriation counterpath and exact connection to the existing causal root. Kinetic propensities, stochastic expectations, negative-control variants and Python refinement are not mechanized by that package.

## What this advances

The earlier formation law had one type; the subsequent selection argument began with two pre-existing types. This construction closes that preparation gap for an explicit finite law. It does not claim either earlier kinetic model is an exact quotient of the new one: locality and association retain consequential distinctions that an aggregate regulator count omits.

The next missing mechanism is **revision of selection rules themselves**. The present law changes occupants and resources but fixes the available response types, association chemistry and copying rule. Changing these parameters between analyst-selected arms is not endogenous revision. A next construction must form alternative access or copying mechanisms, account for their inheritance and costs, and explain which consequences retain or change them. Individual learning and the representation/evaluation capacities needed for concern remain further obligations.
