# Delivered continuation in the existing shared-renewal process

The [protocol](PROTOCOL.md) tests whether actual C assembly happens again after initial recycling and assembly. It keeps the existing physical law unchanged and evaluates both catalytic preparations and all five original regulator arms. [compare.py](compare.py) and [results.json](results.json) preserve every case, both packet caps and the input hashes. This is a numerical model experiment, not empirical validation or a proved roundoff enclosure.

## What the new test requires

The primary event requires recycling and assembly by H, another assembly during (H,2H], and productive material throughout [0,2H]. Free fuel at H is separately tested and stratified. Material already made usable can fund another assembly; the assay does not require that the usable material remain in fuel form. No actor is given a free observation or control operation at H.

The common vocabulary has sixteen sequential profiles (j,b,f,n): initial recycling, initial assembly, intermediate free fuel, and later assembly, with thresholds 0 or1 and full-interval survival. It extends the old vocabulary, whose survival requirement ended at H. The resulting regions are for the fixed autonomous run, not every implementable intervention or all possible functions.

## Primary results

These are cap64 finite-chain probabilities. The columns correspond to H=tau, so the total horizons are 0.5,2 and6.

| Preparation | H=0.25 | H=1 | H=3 |
|---|---:|---:|---:|
| g=1, theta=0, absent regulator | 0.000274953 | 0.041728852 | 0.072436907 |
| g=1, theta=4, absent regulator | 0.001474052 | 0.088337499 | 0.103997669 |
| g=4, theta=4, absent regulator | 0.005174075 | 0.242925123 | 0.460460609 |
| g=4, theta=4, responsive regulator | 0.004386749 | 0.102110211 | 0.060042693 |
| g=8, theta=4, absent regulator | 0.008915218 | 0.331653746 | 0.658551031 |
| g=8, theta=4, responsive regulator | 0.006569434 | 0.083993430 | 0.029665878 |

Faster recycling improves repeated delivery at all three tested horizons in the g=1 comparison. This is compatible with its previously established loss of free-fuel readiness. At H=0.25 and reliability 0.5, the sequential regions are numerically incomparable: theta0 meets (0,0,1,0) while theta4 meets (1,0,0,0), and neither meets the other's distinguishing profile. The repeated-delivery profile itself remains below0.5 there. At H=1 the theta0 sequential region is empty while theta4 meets (0,0,0,0) and (1,0,0,0). These are scoped numerical region comparisons, not a global ordering.

All 384 constructed-versus-absent comparisons—four constructed arms, two source levels, three time windows and sixteen profiles—remain negative. Even the largest constructed-success-plus-overflow minus absent finite-success value is approximately -0.0007111021. Thus the earlier regulator failure is not explained solely by having measured free reserve: it also fails these delivered-continuation tests. This does not test a different allocation-control architecture or every new function its chemistry could support.

At g=8,H=3, the absent arm meets all sixteen profiles at reliability 0.5; the responsive arm meets none. Raising g from4 to8 also lowers the responsive arm's primary probability at H=1 and3 in these cases, despite increasing the absent arm's performance. Available source strength alone is not a sufficient condition for useful continuation under an arbitrary installed allocation law. This comparison does not uniquely attribute the change to a particular reaction.

## Free-fuel strata are informative but not randomized interventions

For g=1,theta4,H=1, approximately 46.0% of successful repeated-delivery trajectories have zero free fuel at H. At g=8,absent,H=3 that share is approximately 3.89%. These trajectories can still draw on usable material and later energy capture. Zero free fuel at one time does not by itself mean that continuation is impossible.

The saved results report each stratum's entry mass, joint success and their ratio. The preceding dynamics select the stratum: these conditional values do not measure the causal benefit or harm of removing a fuel packet. The ratios refer to the stopped chain, and are not silently promoted to exact conditional probabilities of the unbounded model. Original-event bounds apply to the unconditioned joint tests.

## Derivation and numerical scope

The [formal bridge](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/CONTINUATION-BRIDGE.md) derives the killed-generator identity and the equivalent positive marked process. Construction costs, wear and fuel sequestration remain in the generator. The A=0 face is invariant, so final A>0 certifies that productive activity never reached zero during the interval.

Every case was computed at packet caps 48 and 64. The largest probability shift is 4.01e-8. The largest cap64 overflow probability through the full horizon is 1.17e-14. Truncation has a coupling bound in exact arithmetic; sparse matrix-exponential actions and subtraction use ordinary float64 arithmetic. The disclosed 1e-10 comparison tolerance is not a theorem about roundoff. Raw minima, mass errors and fuel-partition residuals are retained. The [independent review](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/CONTINUATION-REVIEW.md) records checks using a separately reconstructed marked process.

The next mechanism must address a real competing use of productive material and repay its own costs. A second successful assembly supplies a concrete future function; it is not indefinite renewal, spontaneous selection of a useful architecture, an ordering of every future capability, or a universal tendency toward 善.
