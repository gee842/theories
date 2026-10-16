# When constructed regulation fails to repay its costs

The first prespecified regulator extension gives a negative result. The regulator is built from initially absent material and can sense fuel through binding, but all four constructed arms reduce every tested joint success probability relative to the unmodified process in the declared cases. This is an AI-assisted calculation for a supplied reaction network, not a physical experiment or a refutation of beneficial regulation generally.

The [prospective protocol](PROTOCOL.md) fixed five arms, two source strengths, three horizons and eight joint profiles before calculation. All 240 distinct assay probabilities are in [results.json](results.json). The [network and accounting proof](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/PHYSICAL-REGULATION.md) and [construction-lag proof](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/REGULATION-LAG.md) specify the physical and analytical scope.

**Later, separate mechanism:** [paid response formation and retention](retention/README.md) implements a different seven-event law in which repair restores support access and captured fuel funds copies. Its source-dependent copying advantage and failure regimes do not supersede the negative results of this original network.

## Main comparison

At source strength g=8, horizon H=3, starting with three material units and no regulator:

| Installed process | Continued productive material | Recycling, capture-machinery assembly and a free packet jointly | Regulator ever constructed |
|---|---:|---:|---:|
| Absent regulator | 0.807111 | 0.692543 | 0 |
| Constructed inert burden | 0.313480 | 0.199485 | 0.817218 |
| Fuel binding only | 0.320967 | 0.201164 | 0.817218 |
| Constant inhibitor | 0.304258 | 0.193638 | 0.817218 |
| Fuel-responsive inhibitor | 0.315964 | 0.198790 | 0.817218 |

All tests require protected productive material `A=R+C+Y+YG>=1`; intact G alone does not count. Bound fuel does not count as a freely available packet. At reliability 0.5, the absent-regulator arm passes all eight profiles here, while every constructed arm passes none. This is an empty reliable region for this autonomous protocol and assay vocabulary, not absence of every possible activity.

The vocabulary deliberately retains the original productive and reserve functions. The new chemistry also introduces a fuel-dependent binding response, which these eight profiles do not count as a separate delivered function. A common extended vocabulary could therefore produce incomparable regions rather than an overall reduction: the original functions may decline while a new function becomes possible. Testing that requires an explicit, paid functional assay of regulation in both arrangements. Counting G species or adding a favorable name is insufficient. This study establishes loss of the declared old functions, not loss of every possible future function.

Across all six source/horizon combinations, each of the 192 constructed-versus-absent comparisons is unfavorable. The smallest separation between absent finite success and constructed success-plus-overflow is approximately 0.001345. At H=0.25 the reliable regions can nevertheless be equal because lower probabilities need not cross the chosen threshold. At later declared horizons, constructed-arm regions are strict subsets. Probability loss and thresholded capability loss remain distinct.

These are related mathematical comparisons, not 192 independent observations. Some profiles coincide from this preparation: assembling C first requires R supplied by recycling. The full report preserves this logical dependence instead of counting it as extra empirical support.

There are small differences among constructed arms: at g=8,H=3, fuel binding alone has a higher joint success estimate than responsive inhibition. We therefore cannot attribute a gain over constant inhibition to fuel feedback alone; the factorial controls matter. None outperforms the absent-regulator preparation in this comparison.

## What the result teaches

Construction diverts usable R from capture machinery and catalytic material while also spending fuel. With only three units, this is a substantial burden. More captured energy can fund more of that diversion: greater incident support does not by itself select useful expenditure. Our fixed construction law keeps making G whenever R and F are available, regardless of current regulatory need. This is an explanatory limitation of the proposed architecture, retained rather than repaired after seeing the results.

The isolated reversible binding subsystem has the intended response sign: more free fuel shifts regulator occupancy away from Y. That correct local response is compatible with worse whole-process outcomes. The theory therefore needs a paid mechanism governing when regulation is worth constructing and replacing, as well as the regulator's response law. Any such addition needs its own prespecified comparison and formation account.

The [response identity](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/REGULATION-RESPONSE.md) makes that next analysis exact for the stopped finite generator: a changed reaction contributes its rate times its effect on conditional future success, averaged along the changed process. The derivation includes construction debits and gives overflow qualifications. The integral has not yet been numerically decomposed by event or state in this experiment; this is a formal diagnostic available for the next study.

The short-time theorem establishes a construction delay and an early reserve cost independently of numerical outcomes. The finite-material absorption result also survives this extension. These boundaries rule out reporting the candidate as an all-times capability expansion or perpetual active state.

## Numerical scope and reproduction

[compare.py](compare.py) constructs the reachable continuous-time generator and computes transient probabilities using NumPy and SciPy. It uses an absorbing overflow state upon total usable packets exceeding K, retaining the true capture rate. Runs at K=32 and K=48 are both retained. Increasing the cap changes a reported assay by at most 0.00017199, so the smaller cap is not interchangeable with the larger one at arbitrarily high precision.

At K=48 the largest overflow probability is approximately 1.646e-9; the largest mass error is 4.33e-14. Finite success and finite success plus overflow bound truncation error in exact arithmetic. Floating-point arithmetic is not rigorously enclosed, so these are numerical estimates with measured sensitivity, **not** the directed-rounding certificates used in the earlier assay. Six displayed decimal places describe the selected estimates; they do not change that status. An internal [independent review](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/REGULATION-REVIEW.md) checks the implementation and accounting.

Run `python compare.py` with NumPy and SciPy available. Running it overwrites its own results and timing fields. It does not change the earlier experiment.

## Relation to external work

Actual biomolecular regulation has empirical precedents. Ceroni and colleagues report an engineered burden-responsive system in E. coli that preserved native expression capacity and improved batch protein yield; this supports the existence of useful regulation in their setup, not this reaction network or a universal trend. The [primary abstract and metadata](https://pubmed.ncbi.nlm.nih.gov/29578536/) and [author repository](https://hdl.handle.net/10044/1/57105) were inspected; the full methods and data have not been reanalyzed here. A separate [stochastic feedback study](https://arxiv.org/abs/1410.6064) motivates treating regulation at the reaction level, but its abstract is not a validation of our assumptions. These are prior-art and evidence-path anchors, not additional replications of this experiment.

Return to the [earlier joint assay](../README.md) or the [completion plan](../../../theories/becoming/history/COMPLETION-PLAN.md).
