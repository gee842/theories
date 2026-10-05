# Physical association, evolving functions and supplied support

5 October 2026. AI-authored primary-source audit and mathematical interpretation. This is external evidence relevant to formation and retention, alongside the earlier [engineered-feedback audit](PHYSICAL-EVIDENCE-CERONI.md). It is not a calibration of the A/G reaction model or an experimental test of the new integrated theorem. No new laboratory experiment or numerical reproduction was performed.

## What the inspected experiments establish

**Mizuuchi, Furubayashi and Ichihashi (2022).** A replicase-encoding RNA diversified during supported droplet transfer. The main lineage ran for 240 rounds; each round included five hours at 37°C, fivefold dilution, fresh translation system, and droplet mixing. Five late lineages were reported. Reconstitution with five selected clones instead retained four for at least 22 rounds; HL3 disappeared. Removing HL2 also lost PL2. Other removal experiments were inconclusive because removed RNAs reappeared. Two additional trajectories shared an evolved starting mixture, so they are not independent starts from the original ancestor. Results and Supplementary Text 1 say round 76; Methods says round 74. Preserve that discrepancy. The simulation uses effective replication coefficients inferred from separate replication assays, not elementary chemical hazards. These facts support conditional formation of new interactions and coexistence with externally renewed conditions. [Published article](https://doi.org/10.1038/s41467-022-29113-x), Results, Methods and Supplementary Text 1.

**The supplementary model matters.** Its original coefficients already combine translation, catalysis and template effects. Supplementary Text 4 explicitly models translated replicases and obtains similar reported dynamics, but omits RNA–replicase association/dissociation because the requisite experimental parameters were unavailable. Fig. S12 constructs interaction edges from mean replication above a 1.5-fold cutoff; these are assay-dependent edges, not a complete causal inventory. Fig. S23 supplies the effective rate matrix. Neither graph completeness nor microscopic identification follows. [Supplementary information](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-022-29113-x/MediaObjects/41467_2022_29113_MOESM1_ESM.pdf), Text 4 and Figs. S12, S23.

**Bansho et al. (2016).** In the tested transfer system, bulk host/parasite populations became undetectable, whereas droplets supported renewed replication and oscillations. Supplied translation mixtures and repeated dilution were part of both conditions. Compartments raised effective local concentrations and allowed parasite-free host encounters. Later biochemical comparisons attributed much of the evolved host's parasite resistance to changed replicase specificity. This supports an effect of physical association and specific interactions; it does not establish that every compartment or every cooperative activity is favored. The paper also reports measurement uncertainty, particularly for parasites, so disappearance below detection should not be silently equated with proved molecular extinction. [Published article](https://doi.org/10.1073/pnas.1524404113), Results, Figs. 1–4 and Table 1.

The two publications arise from related experimental work; they are complementary evidence, not independent confirmation by unrelated laboratories. Their observed differences cannot be credited to our later theory's prediction. They motivate a mechanism class and provide a conventional baseline that any new theory must meet.

## A formal consequence of the published model

The following is our derivation from the stated model, not a newly observed result. Let X_i denote the abundance of type i in a randomly selected equal-volume compartment, S=sum_i X_i, and C the local carrying capacity. The model's within-round kinetics is

\[
\dot X_i=X_i\sum_j k_{ij}X_j(1-S/C).
\tag{1}
\]

For bounded states, averaging and differentiation commute. Define m_i=E[X_i] and W_j=X_j(1-S/C). Then exactly

\[
\boxed{\dot m_i=\sum_j k_{ij}\{m_iE[W_j]+\operatorname{Cov}(X_i,W_j)\}.}
\tag{2}
\]

Equation (2) is an identity, not an additional law or a closure approximation. Two populations with the same marginal means can have different joint encounter distributions and hence different production. The covariance can have either sign. Changes in compartment occupancy, saturation, competitors and enzyme availability must therefore be represented before inferring a direction from average abundance. Equal means do not certify equal situations.

Define N_i,r as the count in a fixed retained volume (or fixed number of equal-volume compartments). Suppose transfer retains each molecule with marginal probability 1/D, and subsequent redistribution conserves the retained total. Then

\[
E[N_{i,r+1}\mid\text{post-reaction counts}]=N^{\rm post}_{i,r}/D.
\tag{3}
\]

Consequently a mean stationary regime with E[N_i]>0 requires E[N_i^post]=D E[N_i]. This is a balance of expectations, not an expectation of a fold-change ratio. It gives neither existence of that stationary regime nor almost-sure persistence. Finite-window coexistence does not establish a positive stationary distribution for a finite absorbing transfer process. A finite population can fail through sampling or mutation even where the mean balance holds. Mere dilution by adding volume divides concentration without necessarily removing molecules; it would not justify (3) for the total count. Extra immigration or biased retention also changes (3).

The joint distribution belongs to the state of the coupled situation. It cannot be reconstructed merely by adding an isolated individual's replication rate to a free environmental benefit. This is one precise implementation of Ren's requirement that centers be understood through their relations. It leaves the sign of the resulting feedback to calculation.

## How this changes the practical research path

The [integrated formation/turnover certificate](INTEGRATED-FORMATION-RENEWAL.md) and [reversible extension](INTEGRATED-THERMODYNAMICS.md) establish a finite mathematical possibility at uncalibrated rates. The next physical question is whether produced support remains sufficiently associated with the organization whose continuation depends on it. The [retention analysis](USEFUL-RETENTION-MECHANISM.md) develops one candidate association mechanism. The RNA evidence suggests investigating association, specificity and replenishment together, but supplies no identification between an RNA molecule and our abstract fabricator A, gate G or work packet F.

A useful validation sequence is:

1. **Identify one actual process.** State which measured molecular species, complexes and transfers constitute production, capture, wear and renewal. Estimate interaction and depletion rates from measurements separate from the eventual comparison. Use an error set when elementary rates are not identified; do not fill them by choosing favorable constants.
2. **Derive its return mechanism.** Include the joint encounter distribution, fuel and external maintenance. Calculate how much delivered function returns to continued production, how much is lost or available to competitors, and how renewed organization is actually generated. Test source depletion and mixing that disrupts useful association. Association is a candidate cause, not a synonym for favorable selection.
3. **Fix a common joint task.** Measure delivered activity in a later round together with declared protected functions, renewal, support consumed and failures. Count failed lineages and preparations. A survivor-only average and an increase in one type's frequency cannot substitute for this joint test.
4. **Separate estimation from evaluation.** Specify the comparison, adverse regimes and acceptable prediction error before evaluating held-out outcomes. Controls must account for the energy, dilution and concentration changes introduced by their interventions. A hypothetical free shuffle of molecular partners is not automatically a realizable control.
5. **Require an added explanatory result.** Conventional compartmentalized replication already predicts association-dependent coexistence and collapse. Our contribution must deliver a checked additional bound, invariant, cross-system transfer or quantitative boundary. Re-describing the same observation as generativity adds no independent evidence.

This pathway can finish an identified mechanism and test its transport to another system. It cannot by itself prove an unrestricted tendency of reality or identify descriptive generativity with moral goodness. The positive universal objective remains open, with explicit scope rather than an assumed favorable sign.

## Preserved sources and read scope

Original downloaded PDFs and SHA256 hashes are in [source record 24](../../../../sources/24-rna-network-evidence-2026-10-05/README.md). Inspected material includes the two main papers' relevant Results/Methods, and Mizuuchi supplementary Texts1,4 and captions S12,S23. Supplementary figures not quantitatively analyzed, raw sequencing, source workbooks and the authors' simulation code were not reanalyzed. No values have been digitized from a plotted image. The article/code links are source provenance, not an execution record.
