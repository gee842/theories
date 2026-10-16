# Organized scales: primary evidence and correspondence

8 October 2026. This is an evidence assessment and descriptive reanalysis, not a new biological experiment. [Formal integration and completion obligations](ORGANIZED-SCALES-INTEGRATION.md).

## Enterococcal avoidance and retained experience

Filipowicz, Lalsiamthara and Aballay (2021), [TRPM channels mediate learned pathogen avoidance following intestinal distention](https://pmc.ncbi.nlm.nih.gov/articles/PMC8177887/), eLife 10:e65935. Read Results, Figures 1–8, their captions, Discussion and the assay definitions. Tissue-specific rescue implicates intestinal GON-2 and excretory-cell GTL-2; AWB/AWC interventions constrain learned odor preference. The precise transduction mechanism remained unresolved in this study. Its oxygen manipulation also shows that avoidance depends on competing conditions.

Original [source spreadsheets and provenance](../../../../sources/biological-scale-correspondence/elife-65935/README.md) are preserved unchanged. Our independent reanalysis extracts 268 diameter observations and 135 occupancy fractions. At one hour, anterior mean diameters are 14.469 µm for E. coli (n=11), 14.127 for P. aeruginosa (n=18), and 30.849 for E. faecalis (n=13). Units were verified against Figure 2B's axis.

| Strain | Occupancy at 4 h, 8% oxygen | Occupancy at 5 h, after chamber removal | Difference of means |
|---|---:|---:|---:|
| WT | 0.213991 | 0.340367 | +0.126376 |
| npr-1(ad609) | 0.248210 | 0.732793 | +0.484583 |
| npr-1(ok1447) | 0.261767 | 0.772273 | +0.510507 |

Each time/strain mean uses nine recorded fractions. These are descriptive comparisons, not new causal estimates or an individual memory trajectory. Blanks remain missing; original denominators and identifiers joining the figures are absent. We do not infer repeated individual measurements from spreadsheet positions.

## Identified neural execution

Filipowicz, Lalsiamthara and Aballay (2022), [Dissection of a sensorimotor circuit underlying pathogen aversion in C. elegans](https://pmc.ncbi.nlm.nih.gov/articles/PMC9548130/). Read the primary Results, neural simulation/ablation comparisons, Figures 1, 4–5 and assay methods. The proposed route connects AWB through AUA/RMG and command interneurons to motor activity. Ablation and training comparisons constrain execution of learned aversion. Simulation predicts candidate connections; genetic interventions supply additional evidence. This is a branching biological circuit, not the formal model's three unit-gain stages. It strengthens the neural-to-locomotion correspondence without providing the present model's retention equation, gains or costs.

## A newer epithelial-to-neural mechanism

Lei et al. (27 March 2026), [Proton signaling links epithelial sensing to neural control of host defense in C. elegans](https://pmc.ncbi.nlm.nih.gov/articles/PMC13187020/), Nature Communications 17:4493, doi:10.1038/s41467-026-71088-6. Read the primary Results through the avoidance experiments, Figure 4 caption and Discussion. In S. aureus/P. aeruginosa conditions, the reported route runs through epithelial GON-2/CMD-1/NHX-6, proton release and neuronal ASIC-1. Cell-specific rescues and bypass interventions connect signaling to locomotion/avoidance; cholinergic effects also return to intestinal immunity. Gross distention alone was insufficient to reproduce the epithelial calcium change. The immediate proton source remains unresolved.

This revises an overly broad reading of the older mechanistic gap: a concrete gut-to-neuron pathway now has experimental support. It does not establish that the same pathway implements the E. faecalis associative-learning mechanism. No raw data from this 2026 paper were reanalyzed here, and its molecular pathway was not encoded and calibrated in Lean.

## What the evidence changes in our account

The representation needs regional organization, a retained-history distinction, adequate support, competing context and activity that changes further contact. These requirements are reasons for revising descriptions; they do not force one particular numerical equation. The 2021, 2022 and 2026 results cannot be treated as independent replications of one complete model. Nor can success in a laboratory host–microbe interaction certify ecosystem regeneration or organism-wide cognition.

The [analysis script](../../../../experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/analyze_measurements.py), [read-only extraction](../../../../experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/extract_measurements.mjs) and [results](../../../../experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/results.json) preserve source cells, sample counts, means, sample SDs and fingerprints. Artifact-tool extraction was checked with read-only openpyxl; Python statistics was checked against NumPy to 1e-12. No workbook was altered, no missing value imputed, no inferential significance test added and no Lean parameter fitted to these values.
