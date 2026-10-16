# RNA renewal needs a measured transfer interface

5 October 2026. AI-authored primary-source review, exact identification arguments and an unrun observation contract. This adds evidence to the frozen [identification contract](RNA-IDENTIFICATION-CONTRACT.md) and [partial-identification result](RNA-PARTIAL-IDENTIFICATION.md); it does not modify their records or reinterpret the conditional 8.66% one-stage calculation as an experimental probability.

**Advance.** A 2026 compositional-memory study measures dual-color droplet composition after two rounds of mixing. A separate 2026 preprint measures local molecular exchange and RNA replication in adjacent aqueous droplets. These provide real observations of parts of the missing transfer/association interface. Neither inspected dataset identifies a repeated joint RNA-replacement probability, a complete droplet genealogy, or renewal of the supplied translation apparatus. The decisive missing object is a joint growth–transfer–restart law with a specified denominator and supplied-resource policy, rather than another microscopic rate fitted to bulk RNA means.

## 1. Which primary material was actually read

Original bytes, URLs, dates, licenses and hashes are preserved in a new [source addition](../../../../sources/24-rna-network-evidence-2026-10-05/repeated-renewal-addition/README.md) and its [manifest](../../../../sources/24-rna-network-evidence-2026-10-05/repeated-renewal-addition/MANIFEST.json). Page references below are one-based PDF pages. The earlier sources, notes, workbook audit and numerical certificate remain frozen.

| Primary source | Read scope | What it can supply here |
|---|---|---|
| Ledoux et al., *Compositional memory matters for early molecular systems* | Full author v6, posted 1 April 2026, 82 pages with SI; main methods and mixing SI read, key pages 12, 42, 43, 49 visually inspected. Published article DOI [10.1073/pnas.2537522123](https://doi.org/10.1073/pnas.2537522123); publisher PDF returned 403. | Two-round mixing snapshots, reported sample sizes, conditional calibration of mixing parameters, and separate bulk serial RNA measurements. Claims about exact equations below concern v6, not an unverified final publisher version. |
| Sono et al., *Molecular communication enables cooperative genomic RNA replication in all-aqueous droplet colonies* | [Author v1](https://www.biorxiv.org/content/10.64898/2026.08.15.744999v1.full.pdf), posted 17 August 2026, unreviewed; main methods/results read, pages 9, 14, 16 visually inspected. Two author analysis/preparation notebooks read at commit `df6166caa7616a48af39a16a992909ddb06844a4`; no execution. Supplemental figures not reviewed. | Public processed endpoint data availability and explicit segmentation, adjacency, reporter and normalization rules. |
| Yoshiyama et al., 2018, *Automated in vitro evolution of a translation-coupled RNA replication system in a droplet flow reactor* | [Published article](https://doi.org/10.1038/s41598-018-30374-0), main methods/results and original publisher SI; SI mixing figure visually inspected. | Direct tracer redistribution in a continuously mixed reactor and long ensemble RNA persistence under external feeding. |

The source addition preserves four complete PDFs and pinned original small code/provenance files. Three large Sono processed pickle files were retrieved to scratch and matched to their original pinned Git LFS hashes and lengths; they were not deserialized or numerically analyzed. Their original pointers and exact retrieval addresses are preserved. No large image archive is needed for the conclusions here. No raw droplet intensities were digitized or reconstructed, and no data were treated as newly held out after being inspected.

## 2. Two-round mixing is a measured physical interface

The compositional-memory study has two distinct experiments. Its RNA experiment follows four round-228 RNAs through 22 externally supplied five-hour cycles using sequence-specific bulk RT-qPCR. Its separate mixing assay images individual droplets containing green or red dextrans after two mixing/incubation rounds. These are complementary observations, not matched RNA lineages. [Author v6, pp. 10–15](https://www.biorxiv.org/content/10.64898/2026.03.03.709225v6.full.pdf).

The dye assay begins with separate 3 wt% FITC-dextran (10 kDa) and TRITC-dextran (155 kDa) populations. Mixing lasts one minute at the stated stirring speed, followed by five hours at 37°C; the second round reuses the post-incubated emulsion with fresh buffer/oil. The assay buffer lacks the protein components of the RNA translation mixture. The two colors report content mixing, not RNA synthesis or enzyme binding.

The following is a **manual transcription of printed sample sizes and author-inferred parameter bands**, not a reanalysis of underlying images:

| Stirring speed | Analyzed droplets, round 1 | Analyzed droplets, round 2 | Author v6 inferred mixing band |
|---|---:|---:|---|
| 2 krpm | 365 | 278 | s ∈ [0, 0.2] |
| 5.2 krpm | 403 | 320 | s ∈ [0.2, 0.4] |
| 16 krpm | 372 | 450 | s ∈ [0.5, 0.6] |
| 30 krpm | 680 | 582 | s ∈ [0.9, 1] |

Sample sizes are from SI Figs. S13–S14, p. 49; bands are from SI p. 43. Data from three independent experiments are pooled per condition. These droplet counts are not independent experimental replicates. The bands describe model-to-distribution matching; the paper does not give them as confidence intervals. The effective interaction-pool size is nC≈80, conditional on the maximal-stirring calibration, not a directly counted number of physical collisions. No statistical uncertainty interval for nC was found in the inspected version.

**Denominator.** The reported distributions select approximately circular images (circularity ≥0.7), manually exclude misidentified objects, and omit droplets whose two dye intensities are both below 105% of their respective backgrounds. They therefore describe selected dye-positive image droplets, not every prepared droplet, every retained droplet, or the joint success fraction of the original preparations. Their second-round measurements are fresh snapshots; no matched parent–child droplet identifiers are supplied in the inspected material.

**Calibration scope.** V6's main text calibrates 30 krpm to s=1 or s→1, while SI p. 42 explicitly says s=0.95 in estimating nC; preserve that distinction. The RNA benchmark separately uses s=0.79, which must not be silently substituted for the 16-krpm dye band. The second-round distribution comparison is a within-paper consistency check with previously inferred mixing parameters. The SI acknowledges that theory moves farther toward a single central mode than the measured distributions, and suggests a changed packet size. That uncertainty limits transport of a fitted scalar s to a different RNA mixture or round.

One printed SI formula requires an explicit warning. Its stated initial law is

\[
G\mid N=\begin{cases}0&\text{probability }1/2,\\N&\text{probability }1/2.\end{cases}
\]

For E[N]=μ and Var(N)=σ², elementary conditioning gives

\[
E[G]=\mu/2,\quad\operatorname{Var}(G)=\sigma^2/2+\mu^2/4,
\quad\boxed{\operatorname{Cov}(N,G)=\sigma^2/2.}
\tag{1}
\]

V6 p. 42 prints the additional μ²/4 term in the covariance too. For example, N∈{1,3} equiprobably with the stated conditional coin gives Var(G)=3/2 but Cov(N,G)=1/2. This is a printed inconsistency under the stated law. **No calibration implementation was located or inspected for this study, so its effect on the inferred s or nC is unresolved.** The present note neither silently corrects a fit nor declares the observed mixing invalid. It also does not assert the same error occurs in the final published SI.

The experimentally supported advance is that stirring changes a distribution of local composition and retains some compositional memory. A model that always replaces the population by completely pooled, independently re-inoculated droplets discards this measurable dependence. However, the paper's closure, including its Poisson re-inoculation and effective interaction pool, remains a model; the measured histograms do not identify every conditional transition in that closure.

## 3. Local exchange and local RNA production are separately measurable

Sono's preprint studies liposome/BSA-stabilized dextran/PEG aqueous droplets. The donor/receiver geometry permits small-molecule and protein communication while largely retaining RNA. Its primary figures and methods distinguish tracer exchange, replicase-supported RNA production and a cooperative RNA pair encoding replicase and nucleotide-diphosphate kinase. This is a different medium and genotype pair from HL2-228/PL2-228. In fact, the main text reports poor HL2-228 performance under the low-BSA condition and switches replicase RNA. The earlier effective coefficients cannot be transferred to it without new calibration. [Sono v1, pp. 5–9, 12–16](https://www.biorxiv.org/content/10.64898/2026.08.15.744999v1.full.pdf).

The useful physical observations are adjacency-dependent macromolecular exchange and RNA-replication reporter signals. Their measurement restrictions matter for identification:

| Observable | Actual operational meaning | Does not directly identify |
|---|---|---|
| Receiver/donor tracer fluorescence after four hours | Endpoint transfer normalized by donor mean, with prescribed labels and medium | An elementary on/off rate, residence time, or complete exchange path |
| RNA replication beacon signal | Sequence-specific minus-strand reporter; RNA1 and RNA2 use different beacon designs but the same fluorescence channel in separate assays | Simultaneous two-RNA success in the same colony; absolute functional new positive-strand counts |
| Adjacency | Two-dimensional segmented boundary separation below about 0.35 µm | A continuous three-dimensional contact history or inherited compartment identity |
| Cooperative production | Two-hour separate pretranslation, then mixing and four-hour replication; translation stopped with streptomycin during this cooperative assay | Replacement of the installed enzymes, repeated passage, or renewal of the supplied machinery |

The image denominator also has explicit filtering: area ≥100 pixels (about 6.2 µm²), removal of saturated liposome images, retention of the top 75% by Cascade Blue signal, and RNA-population classification with boundary-near objects excluded. Per-experiment summaries, not the full pooled droplet number, support the biological replicate comparisons. These rules are visible in the main methods and [pinned author notebooks](https://github.com/rmizuuchi/atps-droplet-colony-communication/tree/df6166caa7616a48af39a16a992909ddb06844a4).

The public processed datasets thus make endpoint exchange/adjacency associations potentially reanalyzable under their actual selection rules. They do not contain an observed sequence of two simultaneous RNA renewal outcomes across repeated transfer. Fluorescent minus-strand production is stronger evidence of replication than label retention alone, but it is not complete functional RNA replacement. The main paper also acknowledges background nucleotide-kinase-like activity in a negative control. No favorable quantitative probability is inferred from these datasets here.

Yoshiyama's earlier flow reactor supplies a third, narrower observation: SI Fig. S1 tracks spreading of a fluorescent transferrin tracer into the droplet volume after addition to a reactor already run for 48 hours. The calibration uses the low mixing duty and omits fresh-droplet flow during measurement. It supports actual fusion/division-mediated redistribution. Main-text RNA time series extend for hundreds of hours with external feeding, while parasite detection has a substantially higher floor than host RT-qPCR. Neither these averages nor this separate tracer curve gives a matched two-RNA transfer genealogy. [Yoshiyama et al., main paper and SI](https://doi.org/10.1038/s41598-018-30374-0).

## 4. The earlier one-stage event cannot simply be iterated

The frozen RNA calculation scores a tagged original compartment that produces at least D times each starting RNA abundance and then survives retention of a fraction ρ=1/D of whole compartments. It ends **before** fusion. That is a legitimate one-stage event under its declared model. It is not a closed repeated-renewal assay.

First, retaining an entire compartment does not divide its internal molecule counts by D. If an unchanged compartment must multiply both abundances by D in every round, with no partition, degradation, export or reset between rounds, then after n rounds

\[
D^n(H_0+P_0)\le C
\tag{2}
\]

is necessary for a finite count capacity C. Under the frozen two-RNA ODE, r=b/a>1 and p=p0(h/h0)^r strengthen the necessary finite-time condition to

\[
\boxed{D^n h_0+D^{nr}p_0<C.}
\tag{3}
\]

These statements concern the same contents in an unreset compartment. They are not bounds on a fed, repartitioned ensemble. Mixing/division can restore an occupancy scale compatible with another productive round, but then a different transition law and identity convention are required. The compositional-memory measurements directly concern this missing physical interface; they do not license deleting it from the assay.

Second, for one nonbranching tagged compartment with conditional survival probability at most ρ at each of n retention steps,

\[
\Pr(\text{tag survives all n steps})\le\rho^n.
\tag{4}
\]

This follows by conditioning successively on the full past; independence between different tagged compartments is unnecessary. Additional replication conditions can only decrease that event. A growing ensemble can nevertheless retain both RNA types. A *replicating sequence barcode with any surviving descendant* is a branching-lineage event and is not bounded by (4) without additional assumptions. A physical droplet that fuses with others also needs an explicit rule for what constitutes survival of its identity.

The appropriate target must therefore choose among retained original object, descendant lineage, and functional ensemble. None is interchangeable with the others. For complete carrier replacement, the ages and disappearance of original molecules must additionally be observed; new RNA production alone does not establish that stronger task. The abstract study's [repeated-renewal composition](REPEATED-RENEWAL-COMPOSITION.md) and [carrier formalization](CARRIER-TURNOVER-FORMALIZATION.md) make the corresponding clock, source and inherited-state obligations explicit.

## 5. Why two snapshots still do not identify a repeated task

Even exact per-round local-composition distributions do not generally identify a joint transition law. A finite witness makes the issue concrete. Let Z denote two coarse observable composition classes and suppose every round has P(Z=0)=P(Z=1)=1/2. All kernels

\[
K_\theta=\begin{pmatrix}\theta&1-\theta\\1-\theta&\theta\end{pmatrix},\qquad0\le\theta\le1,
\tag{5}
\]

preserve those snapshots. Yet a single marked path occupying class 1 at all n observations has probability

\[
\Pr(Z_0=\cdots=Z_{n-1}=1)=\tfrac12\theta^{n-1}.
\tag{6}
\]

Identity and complete alternation give 1/2 and 0 for every n≥2. This is an identification witness, not a claim that every such kernel fits the complete dye experiment. Pairing origin and destination observations, rather than collecting only another independent snapshot, separates these alternatives.

More generally, knowing exact marginal round-success probabilities p1,…,pn alone yields only

\[
\max(0,\sum_{k=1}^n p_k-(n-1))\le
\Pr(\text{every round succeeds})\le\min_k p_k.
\tag{7}
\]

One cannot multiply them without an independence assumption, nor infer conditional restart probabilities from a selected set of successful earlier rounds. The published dye histograms do not even directly supply the RNA p_k. A fitted mixing scalar is useful only together with the rest of its declared closure and independently checked applicability.

These limits concern task identification, not the nuisance enzyme-scale symmetry discussed in the earlier note. RNA production can be predicted without identifying every microscopic enzyme coefficient. It cannot be predicted across a changed transfer operation while leaving that operation unspecified.

## 6. An implementable, minimally sufficient repeated observation contract

A concrete next assay should target **finite ensemble renewal under an explicit externally supplied protocol**, and reserve stronger material-autonomy claims for additional measurements. One workable primary target is three consecutive cycles, with duration, transferred volume, mixing setting and supply quantities fixed before observing outcomes. No numerical threshold or direction is selected here from the new papers' results.

Prepare independent indexed reactor replicates. At the start and after each transfer/mixing step, measure both RNA totals per fixed reactor volume and their joint local occupancy distribution, with droplet volumes and the empty/one-type fraction retained. Choose positive RNA-total thresholds and a minimum joint-occupancy level from the preparation specification. Define an ensemble round success by: both post-transfer totals meet those fixed thresholds; the specified fraction of aqueous volume lies in droplets meeting both local RNA thresholds; and the immediately preceding growth stage produced the prespecified amount of newly synthesized, functional RNA of each type. Fixed reference thresholds avoid silently demanding geometric growth inside an unpartitioned container.

The primary three-round outcome is the conjunction in each **same indexed reactor replicate**. Its denominator is all prepared reactors, including failed, empty, lost and unproductive runs. This directly measures the repeated probability without a Markov assumption or per-droplet independence. Droplets within a reactor are subsamples for its local occupancy criterion, not additional independent repeats. Censored images or failed assays need prespecified failure/interval handling; the endpoint filters in the two new studies cannot simply be inherited as success-denominator exclusions.

The minimal extra measurements are specific:

1. **Simultaneous two-RNA readout.** Orthogonal reporters must observe both outputs in the same compartment/colony, with calibration to copies or concentration and correction for volume. Separate Cy5 assays do not suffice. Strand-specific and full-length/function checks distinguish inherited label, newly made minus strand and functional newly made RNA; they need not resolve every elementary catalytic step.
2. **The complete growth-to-restart interface.** Record the joint distribution immediately before transfer and immediately after the actual dilution, fusion/partition and fresh-medium addition. For a predictive conditional kernel, origin–destination links or an experimentally controlled labeled-source mixing experiment must distinguish retention, exchange and repartition. For the direct three-round ensemble probability, linked reactor-level outcomes suffice even if individual droplets cannot be followed.
3. **Clock and support ledger.** Record actual phase durations and delivered fresh substrate, translation mixture, proteins, compartment materials and mixing/temperature work or operational inputs. Record wasted/discarded material too. The cited experiments externally supply these conditions. Unless they are included as regenerated targets, the result is conditional RNA-ensemble renewal, not autonomous apparatus renewal.
4. **A held-out transfer challenge.** Estimate the preparation, growth and transfer law in a separate calibration block at fixed genotype and medium; then predict the complete three-round event at a prespecified altered mixing/partition condition, with no refitting to its outcome. Compare the source's partial-memory closure with the conventional complete-pooling closure using the same independently measured inputs. An improvement in conditional prediction would identify the contribution of compositional memory; it would not uniquely validate a universal generativity theory.

If a reusable one-step model is desired, its state must include enough of the joint RNA/volume distribution, inherited enzymes, resource/waste status and mixing environment to predict the next round. The measured conditional law must carry both the success mark and the next state, together with the phase clock and inputs. Iterating one unchanged kernel requires a tested time-homogeneous Markov closure and identical support policy. Phase-, time- or sufficient-history-indexed kernels can also be composed when their conditioning states and support policies are specified adequately; that composition does not require homogeneity. A single RNA mean, a single s, or a scalar one-round success probability is insufficient. Finite data permit conditional bounds and out-of-sample tests; they do not prove exact closure.

For the distinct *descendant-lineage* target, add heritable origin labels and an ancestry convention through fusion and division, then assess both RNA functions in descendants of the declared founders. Such labels themselves require specificity and perturbation controls. Repeated ensemble persistence can be measured without this genealogy, but must not be described as retention of the original association.

## 7. Evidence boundary and reproducibility

What is newly supported is a measurable compositional-memory interface and a feasible local communication/readout mechanism. The new studies go beyond bulk mean-source kinetics. Their available observations still leave simultaneous repeated joint replacement, full ancestry, the growth-to-restart conditional law, and replacement of supplied apparatus unidentified. This is a precise boundary of the inspected public material, not a claim that no unpublished or later data exist.

The [read-only check](../../../../experiments/shared-renewal-capability/rna-repeated-renewal/README.md) verifies all new original source hashes and sizes against the manifest, frozen Source 24 and evidence-note bytes against commit `e214ecf`, and the covariance/kernel algebraic witnesses. It does not extract new experimental numbers, run the original notebooks, fit mixing parameters or rerun the previous RNA probability calculation. The source manifest makes large available-but-unused payloads explicit. The observation contract above remains unrun.
