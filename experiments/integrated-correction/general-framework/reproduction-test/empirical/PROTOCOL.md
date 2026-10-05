# Repeated institutional choice: frozen exploratory protocol

Frozen 2026-10-05 before inspecting individual/group numerical outcomes in the downloaded workbooks. This is a post-publication exploratory reanalysis: the paper's favorable abstract, qualitative claims, and some published resource summaries were already known. This is not a preregistered replication or a test blinded to the authors' conclusions. No dataset switching or endpoint searching will follow the result.

## Source, design, and access

DeCaro et al. (2024), *Learning from regulatory failure*, [PLOS ONE](https://doi.org/10.1371/journal.pone.0307832), [public author archive](https://osf.io/v3drm/). Two original Excel workbooks, the codebook, and appendix are locally preserved unchanged. The archive API reports public read access and no assigned node license. The article is CC BY; we do not infer a separate data redistribution license.

The study has 72 persistent groups of four people and nine rounds. Each group has exactly three communication-plus-sanction opportunities. CNN/FNN have them in rounds 1–3, NCN/NFN and PCN/PFN in rounds 4–6. F adds prompts to discuss sanction purposes, hear disputes, and resolve concerns. C has the same communication and sanction technology without those prompts. Thus facilitation is a bundle, not a pure increase in information. N initially has neither communication nor sanctions; P initially has sanctions without communication. The apparatus is experimentally removed later; its removal will not count as endogenous institutional failure.

The paper reports random assignment of groups to treatments. Assignment-only inspection shows 31 actual sessions, each containing a single treatment and 2–3 groups. `SessID` includes a group prefix; the actual session is the suffix after its first underscore. Counts CNN/FNN/NCN/NFN/PCN/PFN are 4/5/4/6/6/6 sessions and 11/11/11/14/13/12 groups. The assignment algorithm and allocation probabilities across sessions are not established by these records. Causal interpretation therefore depends on the reported random assignment being credible at the effective clustered level and no relevant cross-session confounding. No exact randomization test will be claimed.

## One primary contrast

The authors' ES coding distinguishes no agreed enforcement system (0), agreement not to use monetary sanctions (1), permission for independent conditional sanctions (2), and coordinated conditional sanctions (3). At least two members must express agreement; this is not unanimous consent. We do not impose moral or welfare rankings on these labels.

For every group, define **Y = 1 if ES ≥ 2 in both communication opportunity 2 and opportunity 3, and 0 otherwise**. This is joint retention of a sanction-permitting agreement as recorded by the coders. It is not the average of the two permissions, a newly observed vote in each period, actual sanction use, paid apparatus maintenance, or succession to new members. Do not condition inclusion on the first opportunity's agreement, which is already affected by treatment.

Average Y across groups in each actual session. Within each initial-regime pair (CNN/FNN, NCN/NFN, PCN/PFN), compare the mean session outcome under F versus C. The primary effect is the equal-weight average of these three differences. This targets an equally weighted mixture of initial regimes and sessions, rather than an individual-weighted population effect. All three pairs are retained whatever their signs.

Use the sum of the six independent sample-mean variance contributions, each divided by nine, for the standard error; use Welch–Satterthwaite degrees of freedom for an approximate two-sided 95% t interval and p-value. Report all six cell sizes and means and all three contrasts. There are only 4–6 sessions per cell, so the interval remains approximate. No alternate endpoint becomes primary if this contrast is weak, negative, or undefined.

## Fixed secondary diagnostics, without additional significance claims

1. Report the 4×4 ES transition counts for opportunities 1→2 and 2→3, separately by all six treatments, and counts whose three codes are constant. A constant-code model is a competing account of persistence; a changed code shows recorded revision but not why it occurred. Unchanged codes do not prove renewed deliberation. Coding errors can create apparent change.
2. Report group-level joint-retention fractions as a weighting sensitivity, without replacing the session-weighted result.
3. Report separate descriptive group means of collected tokens and triggered sanctions during the three available communication rounds. These are outcomes of resource management and punishment, not measures of institutional reproduction; no mediation or outcome→later-choice coefficient will be estimated. No claim that sanctions improve welfare follows merely from the primary endpoint.

The causal arrow from experienced cooperation/failure to later support is not isolated: realized outcomes and choices co-evolve, and facilitation can directly change deliberation. No instrumental-variable exclusion restriction is justified. The data can support a bounded effect on retained institutional choice, not validation of the entire feedback loop.

## Extraction and audit

Use `Dataset2_Main.xlsx`, sheet `Data`, group identifiers and `ES Rd1`, `ES Rd2`, `ES Rd3`. Deduplicate the four person rows only after verifying repeated group fields agree wherever populated. Retain all groups. Missing primary ES values remain missing and are reported; do not impute zero. If missingness prevents the declared contrast, report that limitation rather than substitute an endpoint. Verify treatment mapping against `GraphTreatmentNum`, `OrigTreatmentNum`, and facilitation labels. Keep period mapping explicit. Check independently recorded coder columns in the chat workbook only as a measurement audit; do not select the coder giving a preferred result. Save source hashes, exact extraction ranges, derived group/session rows, analysis code, and results for independent review.

The original workbooks will not be edited, macros will not be run, and no raw transcript reclassification will be used to search for a desired effect.
