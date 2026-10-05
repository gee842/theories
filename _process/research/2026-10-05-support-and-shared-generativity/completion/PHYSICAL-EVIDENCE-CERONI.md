# Physical evidence audit: burden-responsive gene-expression control

5 October 2026. AI-assisted primary-source review for Ren's integrated generativity research. This is a completed methods and source-data audit, with a small **exploratory secondary calculation** and a proposed next test. It is neither a preregistered validation nor an experimental replication.

**Finding.** Ceroni et al. provide a real, deliberately engineered example in which a controller's ongoing expression burden can be outweighed by relief of a larger expression burden. The intervention preserves a reporter of host expression capacity, improves growth in tested conditions, and can increase later whole-culture fluorescent product despite reducing output per unit biomass. This supports a conditional mechanism worth identifying. It does not identify our artificial G network, establish inclusion of joint capability regions, explain the controller's origin, or discriminate the integrated theory from ordinary resource-allocation and feedback explanations. Source-data inconsistencies also limit controller-specific quantitative reconstruction.

## 1. Sources, provenance, and actual reading scope

Primary reference: F. Ceroni et al., **Burden-driven feedback control of gene expression**, *Nature Methods* 15, 387–393 (2018), [DOI 10.1038/nmeth.4635](https://doi.org/10.1038/nmeth.4635). Accepted 1 February 2018; published 26 March 2018.

The publisher's main article is subscription-limited. The complete accepted **text** was obtained from the [Imperial author repository](https://hdl.handle.net/10044/1/57105), via its linked `Ceroni_ARTICLE file.docx`. Read scope: introduction, results, discussion, data/code statements, references, all three main figure legends, and all Online Methods. This DOCX is not a copy of the final typeset figure panels. The publisher supplement was independently obtained and read: all captions, Tables 1–7, and Notes 1–3; Figures S8, S9, S12, S14, S15 and Table S6 were additionally inspected as rendered pages. The four-page reporting form was read in full. The Supplementary Data 3 workbook was inventoried and the relevant S8, S9, S12, S13 and S14 cells checked, including arrays labeled raw data and their corresponding calculated summaries.

Exact downloaded bytes, URLs, sizes and SHA-256 hashes are retained in [the evidence manifest](evidence/ceroni-2018/MANIFEST.json). Retained originals:

- [Accepted manuscript](evidence/ceroni-2018/Ceroni_ARTICLE-accepted.docx).
- [Publisher supplementary text and figures](evidence/ceroni-2018/41592_2018_BFnmeth4635_MOESM1_ESM.pdf), 26 pages.
- [Life Sciences and Flow Cytometry reporting summaries](evidence/ceroni-2018/41592_2018_BFnmeth4635_MOESM2_ESM.pdf), four pages.
- [Supplementary Data 3](evidence/ceroni-2018/41592_2018_BFnmeth4635_MOESM5_ESM.xlsx), original workbook, unchanged.

The publisher's public article page supplies the supplement links. The [NCBI BioProject record](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA418979) independently confirms GSE107093 and 90 sequencing experiments/BioSamples. The GEO web page itself returned a browser challenge during this audit. Raw sequence files were not downloaded or reprocessed. Supplementary Data 1–2 and source data for main Figures 1–2 were located but not analyzed. [Addgene's author deposit](https://www.addgene.org/browse/article/28193144/) lists the feedback plasmid #109391, reporters and monitor strains; material availability is distinct from our obtaining or testing them. No authors were contacted.

## 2. What physically responds, and what was built

The causal route is:

\[
\text{induced construct expression}
\longrightarrow \text{host stress/resource competition}
\longrightarrow P_{htpG1}\text{ activity}
\longrightarrow \text{sgRNA production}
\longrightarrow \text{dCas9–sgRNA repression of the construct promoter}.
\]

The discovery study used two *E. coli* backgrounds, DH10B and MG1655, carrying a chromosome-integrated constitutive sfGFP monitor. Four inducible constructs exercised different loads: native LacZ expression, a large VioB–mCherry fusion in two designs, and a Lux pathway. Empty plasmids exposed to the same inducers control for backbone and inducer effects. RNA was collected 15 and 60 minutes after induction; 90 samples were planned across biological triplicates and one low-library empty-DH10B sample was excluded.

The transcriptional response identified several heat-shock-associated promoters. **The measured sensor is a promoter response, not a direct meter of a conserved energy reserve.** The authors explicitly leave the precise upstream activation mechanism incompletely understood. Their interpretation includes polymerase/ribosome competition and possible limitation of folding and protein-quality-control resources. Supplementary Note 3 also stresses that relative mRNA abundance and protein-production rates cannot be directly equated; reduced translation can itself reduce mRNA stability. Neither transcript fractions nor GFP fluorescence uniquely identify separate transcriptional, translational, chaperone, or energetic shortages.

The controller is an externally constructed medium-copy plasmid containing constitutive dCas9 expression and an htpG1-driven sgRNA. It is supplied alongside a burdensome expression plasmid. The main controlled target, H2, expresses VioB–mCherry from pBAD with a stronger ribosome-binding sequence than H3. A targeting guide recruits dCas9 to repress pBAD. Guide mismatches tune repression; a different guide retargets a lacP-driven luciferase construct. These are real physical interventions, not fitted labels.

Crucially, constitutive dCas9 was chosen to make the subsequent sgRNA response rapid. Cells have already been transformed and grown before target induction. There is no matched experiment starting with zero controller material and asking whether the complete architecture forms, pays its initial construction cost, and becomes beneficial within the declared horizon. The design and screening of promoters and guides occur through laboratory work outside the modeled cell. Consequently, **this experiment is closest to an installed-controller comparison, not our constructed-from-zero G arm**. Ordinary cellular expression subsequently produces and replenishes controller molecules, but the study does not track molecule-level replacement, controller wear, segregation loss, or the total preparation work.

Locations: accepted manuscript Results, Online Methods “Design/Construction of the burden-based feedback system”; supplement S8 and Notes 2–3.

## 3. Cost ledger and what the measurements actually certify

| Physical obligation | Evidence actually present | Remaining identification gap |
|---|---|---|
| Host machinery and source | Living cells in specified M9/fructose medium with supplements, aeration, temperature and antibiotics | Nutrient uptake, ATP/work conversion, oxygen limitation and waste fluxes are not jointly measured |
| Controller formation | Plasmid construction and transformation; constitutive dCas9; induced/basal sgRNA | Preparation cost and initial protein abundance are not charged from a common zero-controller preparation |
| Controller running cost | S8 varies dCas9-promoter designs and measures growth, GFP and mCherry; high-expression designs can impose additional burden | No separate energetic/material debit per controller molecule; exact rate-level reconstruction encounters workbook discrepancies below |
| Sensing and actuation | Burden-responsive htpG1, guide targeting, target repression; scrambled-guide open-loop comparator | Sensor transfer law, dCas9/sgRNA abundance, binding occupancy and delays are not identified independently |
| Renewal of productive organization | Growth/biomass and continuing reporter expression | No direct assay of repair or retained ability to implement a second newly requested function |
| Replacement, inheritance, selection | Plasmids maintained during culture under antibiotic selection; endpoint flow-cytometry observations | No long-term selection experiment, architecture-discovery process, or quantified failure/replacement hazards |

The experiment does **not** treat regulation as costless: dCas9 expression was deliberately tuned because it is burdensome, and S8 includes uninduced and induced comparisons. Some high-cost dCas9 variants lose growth relative to H2 even when induced. The physical costs are therefore partly incorporated in observed net performance. They are not resolved into the conservation/work ledger required by our specification. Growth differences include the effects of both controller expense and changes in target expression. In particular, basal repression can partly relieve even uninduced H2 leakage; a comparison against H2 is not a pure price measurement for dCas9.

An interpretable secondary check uses the **induced** S8 measurements, where the selected raw-array means agree with their supplied summaries. `Fig S8 Raw Data B`, row 5, gives one-hour growth rates of 0.305717 h⁻¹ for H2 (J), 0.452353 for Pdcas-2 (E), and 0.256940 for Pdcas-6 (I); each cell contains three values. The corresponding GFP-rate means in row 33 are 1247.018, 11912.845 and 6274.044 fluorescence units per OD per hour. Thus Pdcas-2 has a net growth improvement of 0.146636 h⁻¹, whereas Pdcas-6 has a net loss of 0.048777 h⁻¹ despite a higher GFP-capacity readout than H2. These are descriptive package effects, not separately identified dCas9 energetic prices or significance tests. They supply a real example of why improved sensing or one protected proxy is insufficient for a favorable joint conclusion. No mapping of these design labels to the final FB promoter is assumed.

The most important controls are different in purpose:

1. **H2 alone:** net practical effect of adding the full controller package under the stated cultivation protocol, including its extra plasmid/expression burden. Dual-plasmid and single-plasmid cultures also have different antibiotic combinations/doses in the reported batch procedure, so this is not an isolated molecular intervention.
2. **Scrambled-guide open loop:** carries the regulator components but disables intended target repression. This better probes the usefulness of closing the targeting loop. It is not necessarily perfectly cost-matched after induction: different target burden changes htpG1 activity, guide abundance, growth and dilution.
3. **Weak fixed induction:** H2 at 0.002% arabinose is compared with feedback at 0.5%. Approximate matching at 37°C followed by comparison at 30°C tests whether static attenuation substitutes for feedback. It does not compare to the best possible open-loop schedule at every temperature, nor isolate temperature's effects on sensor, target, cell physiology and fluorophore kinetics.
4. **Guide-mismatch series:** changes regulatory gain and exhibits the host-capacity/output tradeoff. It does not independently calibrate promoter occupancy or resource price.

The assay outputs must retain their definitions. At 15-minute sampling spacing, the methods estimate

\[
\widehat\mu(t)=\frac{\log OD(t+15)-\log OD(t-15)}{30\,\mathrm{min}},\qquad
\widehat q_G(t)=\frac{G(t+15)-G(t-15)}{30\,\mathrm{min}\;OD(t)},
\]

with the analogous red-fluorescence rate for target output and a reported background correction. Thus “per cell” is operationally **per optical-density unit**, not a direct cell count. GFP production is a reporter of available expression capacity, not simultaneous measurement of all native functions. Optical density, fluorescence maturation and brightness, changing cellular composition, and normalization need an observation model when transferring conditions. Endpoint total red fluorescence is a proxy for accumulated product; it is neither an absolute protein mass nor the instantaneous production rate.

RNA-seq normalization gives relative expression information. It does not determine a complete material budget or absolute mRNA numbers per cell. The authors themselves propose spike-ins, mRNA turnover measurements and ribosome profiling for further disambiguation. There is no independently calibrated CTMC generator, quantitative controller model or parameterized formation/loss model for the complete feedback system in the inspected paper and supplement. The rate formulas are data reduction, not a predictive dynamical identification.

## 4. What is established, with its controls and limits

The experiments support a burden-responsive host promoter, targeted feedback action, and preservation of the specified GFP/growth proxies across the tested inducer, strain and temperature conditions. Retargeting supports modularity within the demonstrated designs. S9's scrambled-guide comparisons and S12a's weak-induction comparison provide more relevant evidence than an absent-controller comparison alone. They already address conventional control questions.

The batch result is a temporal tradeoff: less fluorescent product per biomass can coexist with more biomass and more total product at a later horizon. Early and late batch series must remain separate: the 0–12-hour experiment was started at higher OD to avoid low-OD artifacts, while the 16–24-hour series uses a different preparation. They cannot be concatenated into one continuously observed trajectory or used to infer a single exact crossing time.

Sampling limitations matter. The reporting form specifies three biological replicates for controller characterization and RNA-seq; the initial burden assay and S7 use two in some panels. Some manuscript captions/methods use broader three-replicate language. Use each panel's documented replication instead of assuming one n everywhere. Randomization and blinding were not used. The late-batch spreadsheet contains one scalar for each construct/time/readout, without replicate identities or a recoverable sampling distribution. It does not support independent re-estimation of uncertainty for controller-specific yield effects. Five time points from one culture are not five independent cultures. Flow-cytometry events from a culture are not independent culture replicates.

S15 reports no detected escape population during the 24-hour assay and repetition with similar results. That does not prove that no mutation arose, quantify its detection limit, or establish evolutionary retention without antibiotic support. The study offers no causal evidence about spontaneous discovery or prevalence of its engineered architecture.

### Source-data issues that must remain visible

These are observations of the preserved files, not proposed corrections or allegations about the experiments.

**A. S14a controller labels disagree.** In `Fig S14a raw data`, columns C–F are headed `H2`, `FB5`, `FB`, `FB2`. The plotted S14a legend assigns the numerical trajectories to H2, FB2, FB5, FB. For example, the 24-hour trajectory with OD700 0.1228 and yield 20667.4 is workbook column F, headed FB2; the corresponding highest curve is plotted as FB. The workbook's column D trajectory is plotted as FB2, and E as FB5. H2's C trajectory agrees. Do not silently permute labels. The discrepancy is consistent with a permutation among feedback variants, but without sample metadata that explanation is not verified.

**B. S8 raw arrays do not always reproduce supplied summaries.** In `Fig S8 Raw Data A`, D32 contains the three Pdcas-1 GFP values at one hour: 26303.5714, 27625, 27203.3898, whose mean is 27043.9871. The corresponding `Fig S8 Mean and Std values A` E34 is 19199.8631. For Pdcas-4 growth at one hour, the raw-array mean from G5 is 0.5150552 h⁻¹ while K6 in the summary is 0.6486900 h⁻¹. These are not rounding errors. An undocumented adjustment or mistaken export may explain them; the inspected files do not resolve which. H2's GFP standard-deviation cell R34 also repeats its mean rather than the standard deviation of its raw array. Do not use these summary cells as an independently validated controller-cost calibration.

**C. S13's mean/SD worksheet is exactly equal, cell for cell, to S9's mean/SD worksheet.** S9 concerns the scrambled-guide open loop; S13's caption describes H2 alone. Their raw sheets are not wholly identical, but overlapping blocks and the identical summaries require clarification before claiming independent H2-versus-feedback evidence from those S13 summaries.

**D. Several construct/condition details remain unresolved.** Table S6 contains guide sequences for FB, FB1, FB3, FB4, FB5 and open loop, but not FB2 used in the batch comparison. S12b's BL21 temperature is 30°C in its plot and workbook header, while its caption says 37°C. Preserve these conditions as uncertain when defining a validation set.

These limitations affect parameter identification and precise subgroup attribution. They do not by themselves erase the qualitative targeting and burden-response observations.

### A calculation invariant to the displayed feedback-label permutation

The following is a transparent **post-inspection worksheet calculation**, not held-out prediction. Column letters are authoritative locators; the contradictory controller names are not repaired. S14a row 6 contains 24-hour OD700, row 13 fluorescence/OD, and row 20 total fluorescence.

| S14a column | Workbook heading, unverified | OD700 | Red fluorescence/OD | Total red fluorescence | OD ratio to H2 | Per-OD ratio to H2 | Total ratio to H2 |
|---|---|---:|---:|---:|---:|---:|---:|
| C | H2 | 0.0132 | 575636.364 | 7598.4 | 1 | 1 | 1 |
| D | FB5 | 0.0170 | 511717.647 | 8699.2 | 1.287879 | 0.888960 | 1.144873 |
| E | FB | 0.0720 | 240430.556 | 17311.0 | 5.454545 | 0.417678 | 2.278243 |
| F | FB2 | 0.1228 | 168301.303 | 20667.4 | 9.303030 | 0.292374 | 2.719967 |

All three non-H2 trajectories show greater final OD, lower red fluorescence per OD, and higher total red fluorescence than H2. If the mismatch is confined to feedback-variant labels as suggested by matching curves, that conclusion survives any such permutation. The smallest and largest total ratios across these columns are 1.144873 and 2.719967. These are observed ratios, **not confidence bounds**, and no exact ratio is attributed to the fully matched controller.

The product identity

\[
\frac{Y_i}{Y_0}=\frac{B_i}{B_0}\frac{p_i}{p_0}
\]

holds to ordinary floating-point error below \(4\times10^{-15}\) for the displayed cells, where \(B\) is OD and \(p=Y/B\). Because fluorescence/OD is computed using the same yield and OD, this is an arithmetic audit and explanatory decomposition, **not three independent measurements or confirmation of a causal growth model**.

Reproduction requires only the preserved workbook: load the S14a sheet without changing it; for each column D, E and F, divide rows 6, 13 and 20 by the corresponding C-cell, then check the first two ratios' product against the third. These cell references and exact source hash in the manifest fix the calculation without a derived duplicate data file.

## 5. Bridge to the common formal specification

| Common interface | Defensible instantiation here | Not supplied by this paper |
|---|---|---|
| Preparation \(\mathsf P\) | Identified strain, reporter, plasmids, preculture, medium, initial OD, temperature, antibiotics | Equal full construction work or equal zero-controller starting state |
| Observation \(\mathsf O\) | OD, GFP/red fluorescence, RNA-seq, selected single-cell fluorescence | Direct free resource, controller occupancy, repair reserve or all relevant microstates |
| Protocol \(\Pi\) | Installed plasmid/guide choice, inducer concentration, temperature and cultivation schedule | All physically feasible controllers, free rewiring, or actor access to analyst-only states |
| Law \(\mathbb P\) | Empirical culture/readout distributions under documented interventions | Identified full event law, joint path-law error bound or regime-transition law |
| Ledger \(\mathsf L\) | Actual growth and expression carry some net burdens; culture inputs documented | Conservation/heat/work ledger, preparation and replacement debits |
| Tests \(\mathsf T\) | Reporter-expression, growth and accumulated-product thresholds, if declared | Fixed-reliability region inclusion; open-ended native capacity; ethical standing |

The assays are **installed-protocol outcomes**, not an optimized capability region. A natural future joint event would require product above a declared threshold at time H while retaining a GFP-expression threshold and viable biomass over declared times. That event needs aligned culture-level trajectories, a measured observation model, and thresholds fixed before validation. Separate marginal means or values pooled across different experiments do not estimate it. With only three independent cultures, even three observed successes would not establish a high-reliability claim; cell-level event counts cannot solve that replication problem.

The original abstract G network conserves a specified modeled material stock and gates a particular recycling reaction through fuel-dependent binding. Here the target is gene expression in an open, dividing metabolic system, and the sensor is stress-responsive transcription. Their resource species, source, loss channels, actuation target and initial preparation differ. No evidence justifies identifying G with dCas9, free fuel with htpG1 activity, or Y recycling with heterologous expression. Transfer needs a newly specified biological event/observation model and a justified mapping, while retaining the G architecture's unfavorable results.

## 6. Existing explanation and a discriminating next calculation

There is already a mechanistic comparator. [Weiße et al. (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4352769/) construct coupled resource, gene-expression and population-growth dynamics with finite energy, ribosomes and proteome. Their equations connect nutrient metabolism, expression competition, growth dilution and population increase. The model does not obtain direction by maximizing a generic objective. It is a suitable baseline family, with its approximations exposed; the Ceroni findings do not uniquely favor our theory over it. Ordinary feedback explains attenuated sensitivity, while resource allocation plus population growth explains why a lower instantaneous output can produce a higher later total.

### Finite-batch accounting before an exponential approximation

The paper's measured \(\widehat q\) is a fluorescence-production rate per OD. Integrating \(\widehat q(t)OD(t)\) therefore reconstructs changes in that fluorescence signal, subject to discretization and the same background correction; it does not independently predict protein synthesis. A biological model should instead distinguish nascent product production \(r_i(t)\) from maturation and loss. For example, let \(U_i\) and \(M_i\) be total immature and mature fluorescent protein in a fixed observed culture volume, and let \(B_i\) be productive biomass. A declared observation model is

\[
\dot U_i=r_i(t)B_i(t)-(k_i+\delta_{U,i})U_i,
\qquad
\dot M_i=k_iU_i-\delta_{M,i}M_i,
\qquad F_i=c_iM_i+F_{{\rm bg},i}.
\tag{A}
\]

Here the kinetic constants and fluorescence coefficient require calibration; (A) is an audit proposal, **not equations supplied or fitted by Ceroni et al.** Removal through sampling, washout or loss of measured cells must be included if material is followed across the full flask. The plate-reader values come from standardized aliquots: absolute product per flask additionally needs culture volume, sampling history and fluorescence-to-protein calibration. OD units can be used for B only with the corresponding per-OD r; changing B to cell number or mass requires its own calibration.

For constant maturation/loss coefficients the contribution of newly synthesized protein to background-corrected fluorescence at horizon T is

\[
F_i(T)-F_i^{\rm initial}(T)
=c_i\int_0^T r_i(t)B_i(t)K_i(T-t)\,dt,
\]

\[
K_i(u)=\frac{k_i\,[e^{-\delta_{M,i}u}-e^{-(k_i+\delta_{U,i})u}]}{k_i+\delta_{U,i}-\delta_{M,i}},
\tag{B}
\]

using \(K_i(u)=k_i u e^{-\delta_{M,i}u}\) at the equal-rate limit. The initial term propagates pre-existing immature and mature pools. A time-varying environment needs the corresponding nonstationary kernel. Growth dilution belongs in a per-biomass intracellular concentration equation; it is not an extra destruction term for total culture molecules. Actual death/removal is different and needs accounting.

Under **matched initial contributions, common observation coefficient and common nonnegative kernel**, the exact output difference obeys

\[
\frac{F_1(T)-F_0(T)}{c}
=\int_0^T K(T-t)
\left[(r_1(t)-r_0(t))B_0(t)
+r_1(t)(B_1(t)-B_0(t))\right]dt.
\tag{C}
\]

This remains valid for finite-batch resource depletion and time-varying production/growth. When regulation reduces per-biomass synthesis, its fluorescence output improves precisely when the second, biomass-mediated term exceeds the first term's deficit. Controller synthesis, ribosome occupancy, depletion and preparation must influence the actual r and B trajectories; their expense is not omitted merely because it is not written as a separate reward penalty. If construction lowers initial biomass, that loss also enters B. If temperatures or other conditions change the observation kernel, equation (C)'s common-kernel attribution no longer applies: use (B) separately and estimate those changes.

Equation (C) gives a concrete boundary to calculate from independently identified dynamics. It is an accounting identity, not evidence that the inequality is favorable. The available late-batch scalar data support the endpoint decomposition above; they do not identify r, the maturation kernel, resource depletion or culture-level uncertainty well enough to validate (C)'s causal terms separately. No unlimited exponential growth assumption is needed for (C).

A minimal calculation makes the necessary sign boundary explicit. Let \(B_i\) be viable productive biomass, \(q_i\) protein production per unit biomass, and \(P_i\) accumulated product. In a declared loss-free, constant-rate interval with equal starting biomass and zero initial product,

\[
\dot B_i=\mu_iB_i,\qquad \dot P_i=q_iB_i.
\]

For controller attenuation \(q_1=\kappa q_0\), \(0<\kappa\le1\), and **net** growth change \(\Delta\mu=\mu_1-\mu_0\),

\[
\frac{P_1(T)}{P_0(T)}=
\kappa\frac{\mu_0}{\mu_0+\Delta\mu}
\frac{e^{(\mu_0+\Delta\mu)T}-1}{e^{\mu_0T}-1}.
\tag{1}
\]

Use continuous limits if a growth rate is zero. This elementary baseline predicts an initial output deficit when \(\kappa<1\), a possible later gain if net growth relief is sufficient, and no gain when \(\Delta\mu\le0\) with \(\kappa\le1\). A simple resource-price decomposition \(\Delta\mu=s(1-\kappa)-c_{\rm ctrl}\) is a **testable additional assumption**, with burden slope \(s\) and controller debit \(c_{\rm ctrl}\) independently estimated; it must not be imposed to make a desired result hold. Controller expense belongs in \(\Delta\mu\), not subtracted a second time. In finite batch growth, resource depletion, maturation and product loss require the corresponding time-dependent equations. Equation (1) is not a fit to the 24-hour experiment and not a universal theorem.

The immediate calculation should compare two explanatory models on an explicitly declared regime:

1. **Static-allocation baseline:** burden-dependent growth and fixed target attenuation with measured controller costs. Include biomass, resource depletion where relevant, reporter maturation, and initial product. It predicts yield and GFP readouts without adaptive sensing.
2. **Paid feedback model:** add measured htpG1 activity, sgRNA/dCas9 formation, promoter occupancy, response delay, turnover and resource use to the same host model. Do not give it a free controller or free observations. Identify these extra parameters from sensor-only, non-targeting, controller-expression and targeting calibrations, not from the eventual yield advantage.

Compute a gain/failure surface over controller cost, target load, induction timing and assay horizon. Predict the sign of both target yield and the declared joint event, with uncertainty. Compare closed loop to H2 alone, a non-targeting controller, and an attenuation-matched open-loop controller. A useful adverse region is low target load or high controller expression, where expense is expected to exceed relief; another is a horizon shorter than controller activation/repayment. Predetermine a meaningful error tolerance and a criterion for the stronger model's improvement rather than accepting any positive point.

**What can be done now:** reproduce the unambiguous arithmetic above; audit readout and replicate metadata; use clearly identified S9/S12 observations as retrospective model checks. S12a can challenge a crude claim that a fixed weak induction has exactly the same response as feedback across temperature, but the outcome has already been read. It cannot now be a pristine held-out test. The public S8/S14 inconsistencies and absence of directly measured controller states prevent a defensible independent kinetic parameterization in this audit. No parameter fit or predictive model selection has been completed.

**What must precede independent validation:** resolve sample/construct identity and raw replicate availability, obtain sensor/controller calibration data, then freeze the model, parameter-identification procedure, costs, comparison policies, thresholds, primary endpoint, culture-level replication and adverse regimes before evaluating new measurements. Existing data may be used in a timestamped, clearly labeled secondary-analysis plan; it cannot retrospectively become a preregistered experiment. Never stitch the separate early/late batch preparations or resolve labels by choosing the assignment that best fits a favored theory.

For a discriminating test of the **integrated theory**, one further obligation comes first: state a quantitative constraint or prediction that is not already implied by the resource-allocation/feedback baseline. A prospective bound on joint success or on the loss of a previously available function could count if it follows from independently recognizable premises and beats a stated baseline on new data. Renaming the baseline's output as shared generativity, proving a standard response identity, or recovering the known higher-yield result does not supply that distinction. No such uniquely identifying empirical prediction is established here.

## 7. Status for integration

The selected workbook arithmetic is now preserved in a [reproducible read-only audit](../../../../experiments/shared-renewal-capability/physical-evidence/README.md). Its script and results record exact source hashes before/after reading, source cells, recomputed means, ratios and summary-sheet comparisons. All nine checks of the reported observations passed. This checks our transcription and arithmetic; it neither resolves the source discrepancies nor supplies new experimental observations. The primary assistant also independently checked the selected S14a values, S8 raw arrays and equality of the S9/S13 summary sheets directly from the preserved workbook.

- **Empirically supported in a bounded engineered system:** burden-responsive control can preserve specified host proxies and improve later aggregate production while reducing per-biomass output; actual controller burden matters.
- **Completed in this audit:** full accepted methods review; supplement/reporting review; public-data/material inventory; exact source preservation; source-data discrepancy record; permutation-insensitive descriptive calculation; a concrete conventional-model sign boundary and next comparison.
- **Open:** independent physical parameter identification, molecule/work accounting, culture-level joint reliability, beneficial construction from zero, architecture discovery/retention, transport to our G process, incremental predictive content over existing methods, and universality.

This evidence branch advances the completion plan from an abstract-only candidate to a usable, bounded mechanism and data audit. It supplies neither a positive result for the failed G regulator nor completion of the universal generative-direction claim.
