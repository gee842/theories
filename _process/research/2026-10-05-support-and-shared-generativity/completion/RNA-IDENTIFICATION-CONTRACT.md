# What the RNA evidence identifies, and a joint renewal test

5 October 2026. AI-authored secondary source-data audit, exact identifiability arguments and an unrun prediction contract. This advances the [earlier RNA review](PHYSICAL-EVIDENCE-RNA-NETWORK.md). It identifies neither CF nor any other abstract gate/fabricator symbol with an RNA molecule.

**Advance.** The original interaction workbook and the author's simulation notebook are now preserved. All 15 host-donor entries of the published effective rate matrix reconstruct from the measured replicate fold changes to their printed precision. These inputs yield an exact, falsifiable boundary for joint host/parasite replenishment in a two-RNA restriction of the conventional model. They do not identify enzyme-association lifetimes or a complete joint renewal probability. Exact parameter symmetries explain part of that gap. The primary next test is a stated joint droplet outcome with independently measured occupancy and kinetics, not a retrospective claim that the published coexistence validates our theory.

## 1. Accessible evidence and the actual reconstruction

The [source addition](../../../../sources/24-rna-network-evidence-2026-10-05/identification-addition/README.md) preserves the publisher's original XLSX, the author notebook and README at commit `defaabf8633d25fd809ac9ddfec7d65f44083207`, and Dryad metadata. URLs, byte lengths and SHA-256 hashes are in its separate manifest; the older source record is unchanged. The [read-only audit](../../../../experiments/shared-renewal-capability/rna-identification/README.md) and its [JSON output](../../../../experiments/shared-renewal-capability/rna-identification/audit.json) retain every source row used below. No workbook was modified or recalculated, and the original notebook was not executed.

The workbook has six sheets: `Fig. 4`, `Fig. S1`, `Fig. S5`, `Fig. S13`, `Fig. S14`, `Fig. S19`. The numerical data are interaction fold changes and strand-specific measurements; the other sheets contain gel-scan material. There is no numerical Fig. 5 transfer-trajectory sheet in this file. The linked Dryad file listing contains one PacBio sequence archive, not an interaction-rate or droplet-trajectory table; its metadata were inspected, its 25 MB archive was not downloaded. Other measurements may exist outside these inspected public files.

For round 228, `Fig. 4!N10:Q57` has donor/target labels and replicate fold changes. These are the published processed assay outcomes called raw data in the workbook, not instrument-level qPCR Ct records. The experimental protocol first translated replicase for two hours without UTP, then diluted threefold into fresh system with UTP and a translation inhibitor for another two-hour assay. RNA2 fold changes were normalized by a negative-control reaction. These interventions separate translation from the later RNA replication assay; they do not directly measure elementary association rates. [Mizuuchi et al., Methods](https://doi.org/10.1038/s41467-022-29113-x).

The numeric S23 matrix can be reconstructed as follows. For donor j, let alpha be its mean self fold change without a second RNA. In a paired assay let beta be the donor's mean fold change and gamma the target's mean fold change. Supplementary Fig. S12 defines

\[
R_{jj}=\alpha,\qquad R_{ij}=\alpha\,\frac{\gamma}{\beta}.
\tag{1}
\]

The natural logarithms of the retained R values reproduce S23. The target-mean screen \(\gamma>1.5\), with lower values set to zero, reproduces every off-diagonal entry; diagonal entries use alpha. This disambiguation matters: HL3→PL2 has \(R\approx1.62670\) but \(\gamma\approx1.36918\), and its published entry is zero. The screen is therefore not simply `R > 1.5`. It is an assay convention, not proof of absent chemistry. The parasite-donor zero rows follow the supplied no-replicase specification. The notebook stores donor j by rows and target i by columns, matching the printed S23 table even though the equations write k_ij.

All 15 measured host-donor entries agree with the visually inspected numeric S23 table to less than \(5\times10^{-7}\). No plotted points were digitized. This is a reconstruction of the authors' effective input transformation, not an independent validation of its mechanism.

The host HL2-228 and parasite PL2-228 supply a useful concrete pair:

| Quantity | Source cells | Descriptive value |
|---|---|---:|
| HL2 self fold alpha | `Fig. 4!P30:P33`, four observations | 16.2881769625 |
| HL2 fold with PL2, beta | `Fig. 4!P37:P39`, three observations | 3.5931512973 |
| PL2 fold with HL2, gamma | `Fig. 4!Q37:Q39`, three observations | 66.7148686399 |
| Effective cross fold alpha·gamma/beta | Derived | 302.4263373612 |
| Host coefficient a=ln(alpha) | Derived | 2.7904395049 |
| Parasite coefficient b=ln(alpha·gamma/beta) | Derived | 5.7118377350 |

The large cross coefficient includes normalization by the donor's reduced paired output. It is not the observed parasite fold itself and is not an elementary catalytic rate. This measured contrast already distinguishes support of another RNA from preserving the donor's own production.

### Code and provenance limitations

The [pinned author notebook](https://github.com/rmizuuchi/Mizuuchi_Evo_RNA_Complexity/tree/defaabf8633d25fd809ac9ddfec7d65f44083207) references `211017.csv`; the repository tree contains only the notebook and README, so that input is absent there. The reconstructed matrix above is kept as an audit result, not passed off as the missing original CSV. Code cell 3 specifies 300,000 compartments, capacity 300, dilution 5, 1.3 fusion/division operations per compartment and `reaction_time = 2`. It initializes independent Poisson occupancies, solves within-compartment ODEs, truncates final counts to integers, retains a random fifth of compartments, and applies binomial redistribution after pairwise fusion. Neither a physical per-hour elementary rate nor an exact original simulation trajectory follows from these normalized settings and unseeded random draws. The publication's biological rounds last five hours; a physical clock conversion for a new prediction needs independent validation.

Two unresolved source issues remain. `Fig. S19!B11:B13` says HL1-158, whereas its supplementary caption describes round-228 clones; those observations are not silently relabeled. The [Bansho kinetic inconsistency](PAID-ACCESS-PHYSICAL-CONSTRAINTS.md) also remains: its printed evolved-host kcat and Km imply a different efficiency and reduction factor from the table's efficiency row. No kinetic calibration below uses that disputed derived row. S19 does provide strand-specific two- and five-hour synthesis measurements, but not molecule age, bound-complex residence, or a joint droplet transfer trajectory.

## 2. An exact joint replenishment boundary in the conventional model

Restrict the published effective equation to HL2 host H and PL2 parasite P. This is a declared two-RNA model, not the complete five-lineage experiment. Let h,p be the normalized counts/concentrations in one compartment, C its shared capacity, and a,b the two coefficients above:

\[
\dot h=ah^2\left(1-\frac{h+p}{C}\right),\qquad
\dot p=bhp\left(1-\frac{h+p}{C}\right).
\tag{2}
\]

Assume positive h0,p0, h0+p0<C, no mutation, immigration or degradation, and the model's common saturation factor. Along its trajectory below capacity,

\[
\frac{d\ln p}{d\ln h}=r:=\frac ba,
\qquad
\boxed{p=p_0(h/h_0)^r.}
\tag{3}
\]

Let D>1 be the dilution factor. Define a local *joint replacement criterion*: before transfer, both types have made enough net copies that their counts are at least D times their own starting counts. Under uniform transfer this offsets each type's dilution loss in expectation; it is not almost-sure persistence or renewal of the externally supplied translation machinery.

Put \(u=h/h_0\) and \(u_* = \max(D,D^{1/r})\). Both replacement inequalities hold exactly when \(u\ge u_*\). Since the total population increases toward C, a finite time reaching that threshold exists if and only if

\[
\boxed{h_0u_*+p_0u_*^r<C.}
\tag{4}
\]

Equality permits only asymptotic approach, not a finite-time crossing. If (4) holds, its exact model time is

\[
T_* =\frac1{ah_0}
\int_1^{u_*}\frac{du}
{u^2[1-(h_0u+p_0u^r)/C]}.
\tag{5}
\]

Equation (5) specifies the deadline once a physical clock and independently determined model parameters are available. No time conversion or numerical fit is supplied here.

For the central reconstructed coefficients r≈2.046931218>1, D=5 gives

\[
5h_0+26.961467219\,p_0<C.
\tag{6}
\]

At the code's C=300 and a precisely specified starting droplet h0=p0=10, the required total is about 319.6147: **joint fivefold replacement is impossible in this restricted model even with an unlimited deadline.** Equal initial occupancies must instead be below approximately 9.38630. Strong parasite support can therefore conflict with replenishing both populations from the same finite capacity. This is a consequence of the conventional kinetics, not an added favorable force or an observation of failure in the published five-RNA experiment. The author's Poisson initialization is not a population in which every droplet has exactly ten of each type.

The empirical direction is not robustly settled by these few replicates. Taking independent extrema of the observed alpha, beta and gamma values gives r from about 1.83196 to 2.28850, spanning the critical r=2 for h0=p0=10,C=300,D=5. This is a descriptive sensitivity range, **not a confidence interval** or an assertion that the unpaired extrema occurred together. Capacity 300 is a model setting, not an independently measured universal capacity of these molecules. Genotype-specific resource consumption could invalidate the shared count-capacity closure. Equations (4)–(5) remain the falsifiable conditional prediction; the present data do not finish its calibration.

## 3. A precise association-and-replacement observable

For an ensemble of equal-volume prepared compartments, record the actual joint initial occupancy law \(p_0(h,p)\). Count empty and singly occupied preparations as failures for this joint task. Incubate with the same measured fresh translation/fuel mixture, then retain a uniform fraction 1/D of whole compartments. Assess the target **immediately after retention and before fusion/mixing**:

\[
\mathcal E_T=\{H_0>0,P_0>0,
H_T\ge D H_0,\ P_T\ge D P_0,
\text{the compartment was retained}\}.
\tag{7}
\]

The denominator is every original preparation, not only occupied, productive or surviving compartments. This task measures both RNAs' replacement output together with persistence of their association through one specified transfer stage. It does not assert reproduction or replacement of ribosomes, membranes or other supplied apparatus. Whole-compartment retention matches the author's computational dilution step; an actual implementation must verify that physical sampling realizes that operation. Fusion or leakage before assessment requires a different kernel.

In the deterministic within-compartment model with independent uniform retention,

\[
J_T=\Pr(\mathcal E_T)=\frac1D
\sum_{h,p>0}p_0(h,p)\,
\mathbf1\{\text{(4) holds and }T\ge T_*(h,p)\}.
\tag{8}
\]

Equation (8) is a complete baseline prediction once its stated inputs are fixed. A stochastic within-compartment model replaces the indicator by a joint transition probability; the ODE and aggregate means alone do not select that noise law.

Bulk marginal means cannot substitute for the joint occupancy input. Consider two explicitly different preparation laws. In A, half the compartments have (H,P)=(1,1) and half are empty; in B, half have (1,0) and half (0,1). Both individual occupancy distributions and both means are identical. At C=300 the pair in A satisfies (4), whereas no compartment in B can support this joint target without mixing or a new source of the missing type. For a sufficient model deadline and D=5, (8) gives J_A=1/10 and J_B=0. This is an exact witness for nonidentification from marginal initial observations, not a claim that complete future bulk trajectories of A and B are identical. Creating these occupancy laws experimentally also has costs and controls; a costless partner shuffle is not assumed.

## 4. Two structural limits on microscopic identification

### RNA-only trajectories cannot determine latent replicase scale

Supplementary Text 4 proposes, writing x for RNA and e for translated replicase,

\[
\dot x_i=x_i\sum_j c_{ij}e_j(1-\sum_lx_l/C),
\quad
\dot e_i=\tau_i x_i(1-\sum_le_l/C_E).
\tag{9}
\]

For any lambda>0, transform

\[
e'_i=\lambda e_i,\quad
\tau'_i=\lambda\tau_i,\quad C'_E=\lambda C_E,
\quad c'_{ij}=c_{ij}/\lambda.
\tag{10}
\]

With correspondingly scaled initial e, substitution leaves every x trajectory exactly unchanged and gives \(\dot e'=\lambda\dot e\). Zero initial replicase is preserved. Linear dilution or resetting e to zero preserves this equivalence across rounds. Thus RNA-only data under this observation scheme cannot separately identify absolute active-replicase production, concentration capacity and catalytic coefficients. The authors' choices tau=1 for hosts and C_E=30 fix this scale by assumption. The measured effective coefficients already incorporate translation, so interpreting c in (9) as an independently measured elementary catalytic coefficient is an additional identification step.

This symmetry is scoped to (9) and RNA-only observations; it does not assert that every auxiliary measurement in the full paper is invariant. Absolute, active-enzyme calibration could break it. The paper's nominal purified-replicase concentrations and protein gels supply additional information, but the retrieved workbook does not establish the required active-enzyme time course in each droplet. Changing enzyme amount may also change resource burdens absent from (9), giving another discriminating observable rather than a free physical symmetry.

### Even Michaelis constants do not determine association residence

In the declared elementary catalytic scheme \(E+X\rightleftharpoons EX\to E+2X\), steady Michaelis measurements identify

\[
v=\frac{k_{cat}E_{tot}X}{K_m+X},\qquad
K_m=\frac{k_{off}+k_{cat}}{k_{on}}.
\tag{11}
\]

For a fixed kcat and Km, every \(k_{on}>k_{cat}/K_m\), with \(k_{off}=k_{on}K_m-k_{cat}\), yields exactly the same entire steady velocity curve, but a different bound-complex lifetime \(1/(k_{off}+k_{cat})\). This is an exact nonidentifiability witness for that observation model, not for arbitrarily rich time-resolved microscopic observations or a claim that RNA polymerization is literally one elementary step.

For example, use the unambiguous original-host component values from [Bansho et al., Table 1](https://webpark2056.sakura.ne.jp/papers/2016_Bansho.pdf): kcat=0.22/min and Km=0.76 nM. The two algebraic witnesses

\[
(k_{on},k_{off})=(1,0.54),\qquad(2,1.30)
\tag{12}
\]

have on-rate units nM^-1 min^-1 and off-rate units min^-1. Both satisfy (11), while their complex lifetimes are 25/19 and 25/38 minutes. These on/off pairs were not measured or fitted, and the 2016 clone's constants are not assigned to HL2-228. The construction demonstrates precisely why an effective replication advantage or a Michaelis curve does not determine a retention/association kernel.

## 5. Measurement contract and a discriminating check

Before evaluating (7), fix its physical deadline and the model inputs using measurements separate from that evaluation. The following table identifies the present evidence and the additional identifying observations, rather than filling gaps with favorable constants.

| Required quantity | What the inspected publication identifies | Additional observation required for this prediction |
|---|---|---|
| Clone identity and composition | Defined clones, fold-change donor/target labels; one S19 label remains ambiguous | Verified sequences for the actual two-RNA preparation and contamination controls |
| Joint occupancy law p0(h,p), volume, transfer retention | Poisson initialization and uniform retention are code assumptions; bulk concentrations/lineages are measured | Joint single-compartment counts and volume distribution before incubation, plus actual retention/mixing measurements |
| Effective a,b and uncertainty in physical time | Replicate fold data reconstruct the normalized input matrix | Independent time-resolved two-RNA assays, including donor output, active replicase and nutrient conditions; a clock calibration |
| Shared capacity or explicit resource balance | C=300 is supplied by the simulation | Saturation/resource measurements across compositions; retain unequal nucleotide costs or other limitations if a shared C fails |
| Association and transient enzyme availability | SI explicitly omits association/dissociation for lack of parameters | Bound-complex fractions, residence times and active-enzyme production/decay under the same conditions |
| Joint new RNA output and failure probability | Bulk normalized fold changes and selected strand-specific synthesis measurements | Joint per-compartment synthesis/count trajectories through the specified retention stage, with failures retained |

The complete conventional prediction is (4), (5) and (8), or a separately justified stochastic replacement. A measured violation of the capacity boundary under independently calibrated inputs would reject this two-RNA/shared-capacity closure. It would not by itself establish generativity theory: missing resources, template specificity, association or translation dynamics are conventional competing explanations.

A second, more discriminating observation can test the missing association state directly. Prepare matched total RNA counts, total active replicase and resources, but measure different initial bound-complex allocations. The RNA-only model has the same state and therefore predicts the same continuation. In a validated association-resolved mechanism, \(\dot X_i(0)=k_{cat,i}[EX_i](0)\), so different measured binding states give different initial production even before bulk RNA counts separate. Joint host/parasite synthesis within the independently measured binding-relaxation window tests whether that hidden state is needed to predict the later joint replacement task. Matched handling, complex-preparation costs and active-enzyme controls are part of this intervention, not assumed away. No numerical residence-time prediction can be obtained from (11) alone.

This adds an experimentally recognizable state and an independently testable boundary to the theory's request for a joint continuation account. A binding-aware conventional model can explain a positive result; independent support for a broader theory would require an additional transferable bound or prediction beyond that model. No favorable result, prospective registration or held-out validation is claimed here. The source outcomes were known before this secondary derivation, and the proposed new joint experiment has not been run.

## Read scope and preservation

Read the original paper's interaction assays, simulation Methods and availability statements; visually inspected supplementary Text 4 and numeric/diagrammatic Figs. S12 and S23; inspected the source workbook's sheet structure and exact Fig. 4/S19 cell labels and values; read every author-notebook code cell. The audit confirms all preserved original PDF/workbook/notebook hashes before and after analysis. The workbook and pinned notebook hashes are respectively `544fa34ee8706c85e7137d69201e4d51da635bc1994fcd085811abc9ee545bde` and `83e1509f2694edd1ec96476dc51a8c784ceaae56e86cd49961efdf07c2b77878`.

The article was obtained through its public primary URL; the research browser's initial publisher/PMC retrieval failed, but direct public downloads worked. The publication's short code link resolved to the author repository. No author was contacted, no external account changed, and no raw sequencing, unprovided Ct files or unavailable long-term numeric trajectories were reconstructed. The new source files are preserved as an addition to source record 24; earlier PDFs, mathematical witnesses and shared indexes remain unchanged.
