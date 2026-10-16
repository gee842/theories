# One-round experience → later information investment: inconclusive

5 October 2026. **The prespecified exploratory lag test does not detect a change in later investment.** The equal-session estimate is −0.29 percentage points, with an approximate 95% interval from −10.60 to +10.02 points. This is not an equivalence result: effects of practically meaningful size remain compatible with these data.

The question was proposed after the positive contemporaneous information result. A [separate protocol](SUCCESSION-PROTOCOL.md) was frozen before constructing lagged outcomes. We tested exactly one lag, one endpoint and the complete eligible population; no additional lags, filters or endpoints were searched after seeing the result.

## Fixed design and result

Use each person's randomized higher/lower information experience at round t of Experiment 1, followed by their big/small investment choice if externally assigned authority at t+1. Current citizens and authorities both qualify. Group and role assignment are documented as randomized afresh. The causal interpretation requires those assignment draws to ignore prior accuracy and behavior, and treatment not to change participation. These assumptions are explicit; the original assignment software was not independently audited.

The join contains 342 eligible person-opportunities, 87 distinct participants and six sessions; 161 received the higher-accuracy draw. All 90 study participants have complete 20-round records, all adjacent joins exist, and authority places per session/round are fixed. Among the eligible observations, 268 were citizens and 74 authorities in the preceding round. We did not analyze those as separate effects.

| Frozen statistic | Result |
|---|---:|
| Equal-session centered-HT estimate | **−0.29 percentage points** |
| Exact rational value | −1/342 |
| Approximate six-session t95 interval | **−10.60 to +10.02 points** |
| Leave-one-session-out range | −3.51 to +2.11 points |
| Opportunity-weighted HT sensitivity | +0.58 points |
| Raw next-investment rate after higher accuracy | 60.87% |
| Raw next-investment rate after lower accuracy | 59.12% |
| Ordinary raw difference | +1.75 points |

The centered-HT score uses the known one-half treatment probability rather than estimating it from realized group counts. Equal-session weighting also differs from pooling all observations. These choices were fixed before the lagged results; favorable raw differences do not replace the frozen estimate. The small number of sessions makes interval coverage approximate. Shared prior-group treatment and repeated participants are encompassed by session-level inference, not counted as independent observations.

## What this changes

The immediate behavioral information effect and the later investment effect must remain separate. The earlier intervention reanalysis supports a contemporaneous institutional response. This additional analysis leaves the proposed one-round experience-to-maintenance-choice link **unsupported at the available precision**. It prevents us from treating immediate improvement as evidence that actors will reproduce the conditions producing that improvement.

Even a positive lagged result would only identify a short-run response under external role reassignment, potentially through payoffs, attention, punishment experience or beliefs. It would not establish endogenous successor selection, infrastructure survival, lasting preference formation or a cross-domain feedback law. The title and filenames refer to a next-role test; this is not organic institutional succession.

The exact [joined observations](results/succession_joined_rows.csv), [session estimates](results/succession_session_effects.csv), [full results and checks](results/succession_analysis.json), and [code](analyze_succession.py) are saved. Run `python analyze_succession.py` with the same NumPy/SciPy environment as the main analysis. Protocol SHA-256: `f32589ab0e9b408e838d562075ced67b5c66ee4a3a8f857138e570a5a079bb3f`.
