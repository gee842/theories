# Independent empirical audit

Date: 2026-10-05. Reviewer: the separate formal-analysis agent. Scope: raw outcome reconstruction, experimental units, the frozen primary estimator and uncertainty calculation, group-weight sensitivity, code transitions, and coder disagreement. No primary file or source workbook was modified.

**Finding:** the reported arithmetic is reproducible. The observed facilitation contrast is positive under both declared weighting schemes. The inspected records do not establish randomized treatment allocation across sessions or repeated endogenous institutional renewal. These are interpretation limits, not computational errors.

## Independent reconstruction

I read the original workbooks with the bundled Python and `openpyxl` in read-only, cached-value mode. No macros ran. I reconstructed group and session records directly, rather than importing or rerunning `analyze.py`, then inspected the producer's implementation for consistency. Means and variances were independently calculated as exact rational numbers. Because the bundled environment lacks SciPy, the Student-t critical value and tail probability were checked using independently implemented numerical integration of its density and bisection. Doubling the integration resolution changed the critical-value CDF by less than (10^{-14}).

In `Dataset2_Main.xlsx`, `Data!H2:H289` identifies groups; B contains `SessID`; E–G contain original treatment, graph treatment and facilitation; CD–CF contain the three enforcement-system codes. Every group has four participant rows, and all populated group-level fields agree within group. There are 72 groups and no missing primary codes. Graph treatments 1–6 map to CNN, FNN, NCN, NFN, PCN, PFN, respectively; the original-treatment and facilitation fields agree with this mapping.

Removing the group prefix through the first underscore from `SessID` gives **31 actual sessions**: 21 with two groups and ten with three groups. Every session has a single treatment. As a separate identity check, all 72 group-sheet headers in `Dataset1_ChatCodes.xlsm` reproduce those same session date/times after normalizing the date/time separator. The archive's 72 distinct prefixed identifiers must not be treated as 72 independent sessions.

The primary endpoint is exactly

\[
Y_g=\mathbf 1\{ES_{g,2}\ge2,\ ES_{g,3}\ge2\}.
\]

It uses communication opportunities, not universally the same experimental rounds, and does not condition inclusion on the first opportunity.

| Treatment | Groups | Actual sessions | Mean of session outcomes | Sample variance across sessions | Group-weight mean |
|---|---:|---:|---:|---:|---:|
| CNN | 11 | 4 | 1/12 | 1/36 | 1/11 |
| FNN | 11 | 5 | 1/2 | 1/4 | 5/11 |
| NCN | 11 | 4 | 1/12 | 1/36 | 1/11 |
| NFN | 14 | 6 | 1/2 | 1/90 | 1/2 |
| PCN | 13 | 6 | 1/18 | 1/54 | 1/13 |
| PFN | 12 | 6 | 1/2 | 0 | 1/2 |

The three facilitated-minus-ordinary session contrasts are (5/12, 5/12, 4/9). Their equally weighted mean is

\[
\widehat\Delta=\frac{23}{54}=0.4259259259.
\]

Writing (s_j^2,n_j) for each of the six treatment-cell session variances and counts, the declared variance estimator and Satterthwaite degrees of freedom are

\[
V=\sum_{j=1}^{6}\frac{s_j^2}{9n_j}
 =\frac{223}{29160}=0.007647462277,
\qquad
\nu=\frac{V^2}{\sum_j(s_j^2/(9n_j))^2/(n_j-1)}
 =7.1803572202.
\]

Thus SE is 0.0874497700, the approximate 95% interval is **[0.2201883672, 0.6316634846]**, and the two-sided Student-t p value is **0.00168700350**. All agree with the primary output. This is an approximate sampling calculation with only 4–6 sessions per cell, conditional on its sampling assumptions; it is not an exact randomization test or a solution to allocation confounding.

The independently reconstructed group-weight contrasts are (4/11, 9/22, 11/26), whose equal-regime average is (57/143=0.3986013986). This matches the frozen sensitivity analysis and does not replace the primary estimator.

## Transition and measurement checks

Exactly **66/72** groups have the same ES category at all three opportunities. The six changing groups are 8: (1,2,2), 34: (1,1,3), 42: (1,1,3), 52: (0,1,1), 63: (1,1,3), and 65: (0,2,2). From opportunity 2 to 3, only three groups change; each changes from 1 to 3.

An unchanged coarse category establishes recorded persistence, not a fresh decision, active renewal, consent, or maintained enforcement capacity. Within-category revision could also go undetected. These data cannot distinguish several mechanisms producing identical category sequences.

In `Dataset1_ChatCodes.xlsm`, sheet `Kappa (Interrater Reliability)`, H2:J73 contains coder 1's ES codes and K2:M73 coder 2's. Main-workbook CD–CF agrees with coder 1 in **all 216** group-opportunity cells. The two coders disagree on **19/216** cells, spanning eight groups. Crucially, **5/72 group endpoints** change between coders: groups 1, 11, 13, 20, and 69. Category-level reliability is therefore not equivalent to perfect reliability of this derived binary endpoint.

As an explicitly post-result measurement sensitivity, applying the same endpoint and weights to coder 2 yields (217/540=0.4018518519), versus the primary (23/54=0.4259259259). This preserves the positive direction but is not an independently selected or adjudicated primary outcome. No alternate significance claim is made. The 19 cell disagreements and six changing group trajectories have different units; they do not show that the six observed changes are coding artifacts.

## Assignment and mechanism limits

The primary paper describes random assignment, but the authors' operational protocol instructs experimenters to consult a Treatment Order Log and load the treatment scheduled for the day/session. I independently verified that instruction in the raw binary `Protocol_author.doc`; its separate statement of random assignment concerns group membership. The actual order log or its allocation procedure is not available in the inspected material. The correct interpretation is therefore a **session-scheduled intervention contrast, with causal interpretation conditional on credible treatment allocation or exchangeability**. Session-level uncertainty does not remove possible calendar, recruitment, or experimenter confounding. See the separately dated [design audit](DESIGN-AUDIT.md) and [author protocol](https://osf.io/download/p3bs7/).

The recorded agreement needs support from at least two group members; it is not unanimous approval. ES≥2 measures retained permission for a category of sanctions, not actual sanction use or a moral ordering of institutions. The apparatus, membership and later withdrawal of enforcement are imposed by the experiment. There is no tested succession or internally maintained observation/authority mechanism. These qualifications are consistent with the [source paper](https://doi.org/10.1371/journal.pone.0307832) and the revised result report.

The audit identifies **no remaining computational blocker** for the frozen endpoint and estimators. It supports a reproducible, limited empirical comparison; it does not validate the complete proposed cross-domain theory. Secondary token and penalty means were not independently recomputed in this audit.

## Source preservation

The frozen protocol SHA256 is `d99f55eb37b822aa5baec339bde0ea56e46c92260bde924d8b89ff2472fb4891`. Source hashes were checked after read-only extraction and agree with the recorded manifest:

- Main workbook: `46a9b16c9d82d7ab914a942ac9fce6aabae34729d43519cab3d22fdf0c7b8a6b`.
- Chat/coder workbook: `2913ab8d24be76f1447b3a5545347940609b9d279cf47b3a85bc5ef3e1483e0b`.
- Author protocol: `0f7517a8739a54e62c919460043b389a0c262c6a6e810804edb5004a1138cca5`.

This review leaves the primary analysis, frozen protocol and all source data unchanged.

The independent reconstruction is preserved in [review_check.py](review_check.py), with [its results](results/review_check.json). It passes 737 assertions, mostly row-consistency checks; that count is a software audit detail, not 737 independent empirical tests. It runs with the bundled Python and imports no primary-analysis functions.
