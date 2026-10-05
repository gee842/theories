# Independent review of the installed renewal assays

5 October 2026. Internal collaborating-AI review for Ren. This review reconstructs and checks the declared mathematical process; it is not empirical validation or external peer review. The producer, protocol, and producer results were read but not modified.

## Verdict

**Accept the reported probability enclosures and fixed-reliability incomparability for the declared cases.** The event generator matches the [stochastic realization](STOCHASTIC-REALIZATION.md), the overflow and directed-arithmetic argument is valid for these inputs, and an independently implemented generator reproduces all 48 assay probabilities within the disclosed numerical tolerance.

The independent calculation is saved in [independent_check.py](../../../../experiments/shared-renewal-capability/independent_check.py) and [independent-check.json](../../../../experiments/shared-renewal-capability/independent-check.json). It never imports the producer. Exact integer checks cover drift and accounting; SciPy supplies a separate floating-point probability calculation. The floating-point agreement does not itself certify the producer's much narrower intervals.

At the common horizon \(H=0.25\) and reliability \(\alpha=0.5\), the exact installed-run reliable sets in the declared eight-profile vocabulary are

\[
\mathcal C^0=\{(0,0,0),(0,0,1)\},\qquad
\mathcal C^4=\{(0,0,0),(1,0,0)\}.
\]

Neither contains the other. The crossing is far from the threshold:

| Profile and event, with final active material at least one | \(\theta=0\) | \(\theta=4\) |
|---|---:|---:|
| \((0,0,1)\): at least one usable packet remains at the horizon | approximately 0.646107827851266 | approximately 0.344331590924957 |
| \((1,0,0)\): at least one recycling event was delivered | approximately 0.210619411506400 | approximately 0.659720171501266 |

These displayed decimals are summaries; the producer's lower and upper bounds establish the threshold decisions. This is a concrete failure of universal inclusion for this particular installed-process comparison, not a proof that stronger recycling never helps or that all physically admissible protocol classes have incomparable capability regions.

## What was independently implemented and executed

The checker reconstructs eight labeled reactions from a separate stoichiometric table and independent kinetic expressions. It discovers reachable states, then builds a sparse generator in a separate lexicographic state ordering. It aggregates the two recycling channels only when building transitions with the same destination. Both counters are capped at one; capture exceeding the reserve cap enters a separate absorbing overflow state.

The probability calculation uses `scipy.sparse.linalg.expm_multiply` on the transposed generator, starting from the declared point preparation. It independently reproduces the reachable-state counts and maximum exit rates:

| Reserve cap | \(\theta=0\): states / maximum exit rate | \(\theta=4\): states / maximum exit rate |
|---|---:|---:|
| 12 | 417 / 40 | 489 / 110 |
| 24 | 801 / 76 | 945 / 218 |

Every generator row sums to zero exactly in integer arithmetic; every off-diagonal rate is nonnegative; the overflow row is zero. All 48 reported profile classifications agree. For a separate truncation sensitivity check, the independent solver also repeats each case with the reserve cap increased by four.

The executed comparison used Python 3.11.2, NumPy 2.4.6, and SciPy 1.17.1 through `/private/tmp/meta-attractor-plot-env/bin/python`. The absolute comparison tolerance was **\(10^{-11}\)**. Maximum distance of a floating probability from its reported interval was **\(2.78\times10^{-15}\)**; maximum absolute probability change after increasing the cap by four was **\(3.89\times10^{-15}\)**. Those differences are consistent with ordinary floating-point roundoff. The tolerance is a checking threshold, not a proved error bound for SciPy, and the cap sensitivity is corroboration rather than the rigorous overflow bound.

Reproduction from the repository root:

```text
/private/tmp/meta-attractor-plot-env/bin/python experiments/shared-renewal-capability/independent_check.py
```

## Exact generator and accounting checks

For each of \(\theta=0,4\), the checker enumerates every nonnegative material composition with total three and every reserve count from zero through 24: **500 physical states per parameterization**, including states unreachable from the chosen preparation. It checks 1,676 and 1,772 positive labeled events respectively. Capture at reserve count 24 is checked at its actual untruncated target 25; an overflow placeholder is not substituted into these accounting identities.

Let \(J=FD(C+\theta Y)\). Exact integer summation of event increments gives

\[
\mathcal LR=J-R-RY,\quad \mathcal LC=R-C,\quad
\mathcal LY=RY-Y,\quad \mathcal LD=C+Y-J,\quad
\mathcal LF=C-F-J.
\]

Every event preserves total material, has a nonnegative successor, and requires its consumed inputs to be present. Capture intensity \(C\) never exceeds the declared incident packet intensity three. For the reduced work-equivalent quantity \(W=F+R+C+Y\), each capture adds one, leakage and either wear event remove one, and assembly/recycling leave it unchanged. Consequently

\[
\mathcal LW=C-F-C-Y=-F-Y
\]

at these parameter values. This is exact bookkeeping under the stated assignment of work value. It does not establish a molecular realization, entropy-production formula, or thermodynamic consistency beyond the supplied model.

The all-degraded material face is invariant at every enumerated reserve value. Thus the final active-material condition really does exclude a prior visit to that face. The final-reserve condition is a condition at \(H\); it does not require a positive reserve at every intervening time. Nonnegative reserve at every event follows separately from input availability.

Exact generator derivatives at the initial state also confirm the protocol's leading coefficients:

\[
\left.\frac{d}{dt}\Pr(J_t\ge1,A_t\ge1)\right|_{0}=1+\theta,
\]

\[
\left.\frac{d}{dt}\Pr(F_t\ge1,A_t\ge1)\right|_{0}=-(2+\theta),
\]

and the first derivative of the joint recycling-and-assembly event is zero, with quadratic coefficient \((1+\theta)/2\). These checks use integer/Fraction arithmetic, not a finite-difference fit. They corroborate the local expansion; the finite-horizon threshold crossing comes from the full probability calculation.

## Directed-interval audit

The [producer](../../../../experiments/shared-renewal-capability/certify.py) uses uniformization of the finite overflow-augmented chain. Its enclosure argument is sound for the six declared cases:

1. The maximum integer exit rate supplies a valid uniformization rate. Added diagonal mass is nonnegative, and the overflow state receives an absorbing self-loop in the uniformized chain.
2. Directed division encloses every nonnegative transition probability. Products and sums of nonnegative interval endpoints propagate lower and upper state probabilities correctly.
3. The six Poisson means are exactly \(2,5.5,10,27.5,76,218\). The directed multiplication therefore introduces no uncertainty in the mean for these inputs. The exponential is correctly rounded at the requested Decimal precision; its adjacent representable values enclose the exact initial Poisson weight even though exponential rounding is half-even rather than governed by the context's directed mode.
4. Recurrence multiplication and division give valid lower and upper Poisson weights. One minus the accumulated lower weight, rounded upward, bounds the full omitted Poisson tail. The selected-state lower sums omit that tail; the upper sums may assign all of it to success.
5. Up to the first transition above the cap, the original and capped processes coincide. Assigning zero success to overflow is a valid lower bound; assigning its entire probability to success is a valid upper bound. The producer adds the overflow partial-sum upper mass and the omitted Poisson tail once to each assay upper bound. It does not silently remove a capture propensity at the cap.

These arguments justify an enclosure for the original unbounded-reserve chain under its declared generator, subject to the usual correctness assumptions for the arithmetic implementation. No material arithmetic repair is needed for the saved cases.

**Extension boundary:** `certify()` is not automatically a general interval solver for arbitrary decimal horizons. If the product of rate and horizon is inexact at the working precision, a single downward-rounded mean cannot be used for both Poisson bounds. A general version must enclose the mean and handle its exponential and recurrence dependencies, including Python Decimal's default-context unary negation. The current means have only a few exact digits, so this possible extension problem does not affect the present result.

## Scope that must remain in the integrated theorem

The protocol fixes a singleton intervention class: run the already installed process. Its reliable set is exact for that class and this finite assay vocabulary. It is an inner bound for a larger controller class. The failure of an assay under this run does not rule out a paid intervention that changes the event schedule, capture, allocation, or stopping rule.

The incomparability compares **delivered recycling against retained reserve readiness**. Every profile requiring at least one assembly event remains below reliability one-half at \(H=0.25\). Thus this result does not establish a tradeoff between two successfully delivered productive functions. The reserve coordinate is an explicitly declared and consequential supporting-condition test; its inclusion is doing substantive work in the comparison. Removing that coordinate would change the capability question and its order.

Also, assembly requires prior recycling from this initial state, because no usable \(R\) is present initially and recycling is its only formation route. The equality of the assembly-only and recycling-plus-assembly probabilities is therefore structurally expected. It is not evidence for two independent achievements.

Changing \(\theta\) is a comparison between supplied catalytic preparations. The calculation neither constructs that change nor proves that any adaptive process selects it. Shared source conditions and matched preparation make the intervention comparison clear, but do not derive its physical attainability or construction cost. All six results are finite-horizon statements about a stipulated mesoscopic mechanism; they do not replace the finite-system absorption result with indefinite persistence.

No normative conclusion follows from the probability crossing. The result is useful for the descriptive theory because it makes a precise support/function tradeoff visible and prevents a stronger renewal coefficient from being assumed to enlarge every joint possibility. It does not identify either preparation with moral 善 or settle the broader positive directional claim.

## Provenance and reading scope

Read in full: the experiment [protocol](../../../../experiments/shared-renewal-capability/PROTOCOL.md), producer code, producer results, and the current stochastic realization. The repository instructions were followed. The checker was newly written and executed; it shares the stated mathematical model but neither imports nor invokes the producer implementation. This is independence of implementation within a collaborating AI team, not independence of empirical evidence.

The repository HEAD at execution was `b379528da1645db5b5c2eb559fce93831cfda2ec`. The assay files and stochastic realization were uncommitted working artifacts, so that commit is context rather than their immutable source revision. The following hashes identify the actual inspected bytes:

| Artifact | SHA-256 |
|---|---|
| Protocol | `6fb843a79c2bcc64189d1a27fcab4e6e39359343cd0f402cdf18302fefc1a3fd` |
| Producer | `5ca3b3730aa37e34267288c8ef05984e65322519af7edf0af8854bc9eb88eece` |
| Producer results | `25d2f18e55b021640678c4c19e1b74c571731c6ba8994a4f9fb13033b6f787da` |
| Stochastic realization | `8f4dfa02387770c66c95ee482b2b5527e3f50038d1952f63ec096f9ad048a48f` |
| Independent checker | `b1da1233ac1cbdf91965b6c2acdd91a3af0e73435c2dc756532dd83baa0f2521` |
| Independent results | `6383a9e6bce7c270524acd5492740253ace2be9615834393424735942445ad0b` |

Source hashes were checked again by the executable before it wrote its output. This review requests no change to the three producer artifacts. Future parameter, event, assay, or arithmetic changes need a new scoped check rather than reuse of this acceptance.
