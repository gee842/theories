# Gut load, measurement calibration and colonization dynamics

Boddu, Martini, Nemenman and Vega (2025), [*Variance in C. elegans gut bacterial load suggests complex host-microbe dynamics*](https://doi.org/10.1371/journal.pcbi.1013110). Original code/data archive from [Zenodo version 1.0.0](https://doi.org/10.5281/zenodo.14291768), CC BY 4.0. [Manifest](manifest.json) preserves archive and metadata hashes. Archive MD5 matches the publisher's `1753ae890020663d2b254136206461c0`. No archived notebook was executed or rewritten.

The [new analysis](../../../experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/renewal/README.md) reads three members directly from `satyaspandana-varianceinwormgut-e1955ae/Data/`:

- `CFU Mapping.csv`: 169 matched fluorescence/viable-count records; three zero counts are preserved but excluded from log-count regression. Train on 70 positive T48 records, test on 96 T72 records. This differs from the authors' T72 calibration fit.
- `Migration_Compiled.csv`: 1,625 cohort records. Its stored `logGreen` is natural log; the new analysis computes log10 from `Green` explicitly.
- `Migration_run2_Compiled.csv`: 1,969 rows, including identical T0 sequences under the two migration labels: 346 high and 348 low records are repeated baselines. These are not independent replication observations.

Read the calibration and migration source notebooks as methodological evidence. The inverse-tanh functional form is the authors' conventional measurement model; no originality or superiority of generative theory is claimed. Changing sample counts, supplied inhibition/migration interventions, and missing longitudinal identities prevent interpreting every distribution shift as an individual bacterial birth or an identified switching rate.
