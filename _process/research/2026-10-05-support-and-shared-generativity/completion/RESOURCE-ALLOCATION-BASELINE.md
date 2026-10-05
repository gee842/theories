# A physical resource-allocation baseline for useful regulation

5 October 2026. AI-authored primary-source reconstruction and algebraic analysis of Weiße, Oyarzún, Danos and Swain (2015), *Mechanistic links between cellular trade-offs, gene expression, and growth*, PNAS 112, E1038–E1047, [DOI 10.1073/pnas.1416533112](https://doi.org/10.1073/pnas.1416533112). Companion to the [Ceroni physical-evidence audit](PHYSICAL-EVIDENCE-CERONI.md). This is a conventional mechanistic comparison, not a fit to Ceroni, a new validation experiment, or a biological identification of the repository's abstract regulator G.

The useful result is a conditional physical boundary: inhibition can improve growth when the allocation released from target expression exceeds the new controller's allocation cost. Higher total target production then requires the productive population gain to repay the reduction in production per cell over the actual batch. Weiße's resource competition already supplies this explanation. The derivation below makes its assumptions, finite resource budget, and missing costs explicit; it does not establish an additional prediction unique to our theory.

## 1. Sources and reading scope

Read the published ten-page paper and its 21-page supplementary information, including the complete basic model, growth-law derivations, fitting procedure, synthetic-gene extension and population extension. The [authors' publication page](https://swainlab.bio.ed.ac.uk/publications.html) links the [published paper](https://swainlab.bio.ed.ac.uk/papers/pnas15.pdf), [SI](https://swainlab.bio.ed.ac.uk/papers/pnas15sup.pdf), and bioRxiv model files. The [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4352769/) supplied a second primary publication access route. Important equations were checked against rendered SI pages rather than relying only on extracted text.

The [bioRxiv supplementary page](https://www.biorxiv.org/content/10.1101/014787v1.supplementary-material) links the [original model archive](https://www.biorxiv.org/highwire/filestream/3786/field_highwire_adjunct_files/1/014787-2.zip). Inspected its complete Facile reaction specification, MATLAB driver and MATLAB differential equations, plus SBML species/parameter declarations. The archive contains the cellular model with a gratuitous-protein channel and antibiotic complexes. It does not contain the fitting data, posterior samples, a fitting pipeline, or the finite-population simulation scripts. No supplied code was executed and no SBML import was validated.

Exact public downloads, retrieved 5 October 2026, were read in temporary storage; this note is the only new repository artifact. Download lengths and SHA-256 hashes identify the inspected source versions:

| Source | Bytes | SHA-256 |
|---|---:|---|
| Author-linked published PDF | 3,919,611 | `3cff2c79b842b6e17a7f913763974ac613ae3f479f60b0e729f0389ad1ff0121` |
| Author-linked SI PDF | 734,069 | `18a975f2c0d5d216b38e6e0082c17513a952f2c1a1573f1d21b0f9d7249dc8ee` |
| BioRxiv model ZIP | 6,951 | `f290d059f463de2fa22864c2bea98e131f66a8df56e345d8d1e02dadc61af374` |

The raw MATLAB ODE member, `model_code/cellmodel_odes.m`, has SHA-256 `25d2830d9fcb17072058c8c949fc8e11e021980e827c768b4be79bd980b97f7c`; the reaction member, `model_code/cellmodel.eqn`, has SHA-256 `3f657a743ee39abe891456f0f1148e3051f568430e0f8cb70619dc9f03fa5a8b`. Files were inspected read-only. Access failures from individual web interfaces were resolved through these publicly linked author versions, not through inferred abstracts.

## 2. The actual cellular mechanism

The basic model has fourteen intracellular states, measured as molecule numbers per cell: internal nutrient \(s_i\), available biosynthetic resource \(a\), free ribosomes \(r\), transporter \(e_t\), metabolic enzyme \(e_m\), other housekeeping proteins \(q\), and four pairs of free mRNA \(m_x\) and ribosome-bound mRNA \(c_x\), with \(x\in\mathcal X=\{r,t,m,q\}\). Here \(r\) denotes ribosomes, **not** the target-production rate used in the Ceroni audit. A constant cell volume of \(1\,\mu\mathrm m^3\) converts bimolecular rates to these units. The basic environment has fixed external nutrient \(s\); depletion is a separate population extension.

The resource \(a\) is an intentionally coarse variable, not a measured ATP concentration or a thermodynamic free-energy state. Translation spends it; transcription depends on its availability but its resource consumption is omitted. Proteins do not degrade in the basic model; free mRNAs do. Each mRNA binds at most one ribosome. There is no explicit polymerase pool, polysome, protein-folding stress, chaperone sensor, cell-division event or variable cell volume. [Paper, Results; SI S1](https://swainlab.bio.ed.ac.uk/papers/pnas15sup.pdf).

For protein length \(n_x\), the rates in SI Eqs. 7–11 are

\[
v_I=e_t v_t\frac{s}{K_t+s},\qquad
v_C=e_m v_m\frac{s_i}{K_m+s_i},\qquad
\gamma(a)=\gamma_{\max}\frac{a}{K_\gamma+a},\qquad
\nu_x=\frac{\gamma(a)c_x}{n_x}.
\]

\[
\omega_x=w_x\frac{a}{\theta_x+a}\quad(x=r,t,m),\qquad
\omega_q=w_q\frac{a}{\theta_{\rm nr}+a}
\frac{1}{1+(q/K_q)^{h_q}}.
\]

\(\theta_t=\theta_m=\theta_q=\theta_{\rm nr}\), and the default assumes \(w_t=w_m=w_e\). The \(w_x\) combine gene dosage, induction and transcriptional properties; they are not direct counts of one molecular operation. \(\nu_x\) has units of completed protein molecules per cell per minute; \(\gamma\) is amino acids per translating ribosome per minute.

The differential equations are SI Eqs. 1–6, with the import/catabolism abbreviations above:

\[
\begin{aligned}
\dot s_i&=v_I-v_C-\lambda s_i,\\
\dot a&=n_s v_C-\sum_{x\in\mathcal X}n_x\nu_x-\lambda a,\\
\dot r&=\nu_r-\lambda r+
\sum_{x\in\mathcal X}(\nu_x-k_b r m_x+k_u c_x),\\
\dot e_t&=\nu_t-\lambda e_t,\quad
\dot e_m=\nu_m-\lambda e_m,\quad
\dot q=\nu_q-\lambda q,\\
\dot m_x&=\omega_x-(\lambda+d_m)m_x+\nu_x-k_b r m_x+k_u c_x,\\
\dot c_x&=k_b r m_x-k_u c_x-\nu_x-\lambda c_x.
\end{aligned}
\]

Translation returns the ribosome and mRNA to their free pools. Making a new ribosome therefore contributes both the release term within the sum and the extra \(\nu_r\). Bound mRNAs have no separate degradation term in these equations. Increased target mRNA can sequester ribosomes, consume translation resource and displace enzymes that replenish that resource. Reduced enzyme production can then depress the target's own production. This feedback arises from the reactions rather than from an instruction to maximize growth.

### Growth is a closure with a specified mass scale

Let \(L\) be the actual protein mass per modeled cell in amino-acid units, renamed here to distinguish it from the fixed reference mass \(M_s\):

\[
L=n_r\Bigl(r+\sum_xc_x\Bigr)+n_t e_t+n_m e_m+n_q q,
\qquad R_t=\sum_xc_x.
\]

Summing the cellular equations gives

\[
\dot L=\gamma R_t-\lambda L.
\]

At balanced growth, \(\dot L=0\). The authors specify a reference mid-log mass and use the closure

\[
\lambda=\frac{\gamma R_t}{M_s}
\tag{W-growth}
\]

also away from steady state. Thus \(\dot L=\lambda(M_s-L)\): \(L=M_s\) is invariant if prepared initially, but is not imposed instantly on arbitrary initial states. This distinction follows directly from SI Eqs. 12–14 and S1.2.5. The supplied driver starts with ten free ribosomes, resource \(a=1000\), and other molecular states zero, far below \(M_s=10^8\); it integrates toward a cellular steady state. That initialization must not be relabeled a mass-consistent physical batch preparation.

Adding a stable target protein \(p\) adds \(p,m_p,c_p\), its translation consumption and binding terms, its mass \(n_p p\), and \(c_p\) in the growth closure (SI S4). Target synthesis therefore contributes to instantaneous total mass production, even though it does not supply the machinery for future synthesis. A controller protein must be added in the same paid way. Merely inserting a target-inhibition function while leaving the controller out of the resource equations makes it free by construction.

## 3. A conditional gain/failure boundary

The following is an algebraic consequence of the conventional model, not an additional law supplied by our theory.

In balanced growth, write protein mass fractions as \(\phi_x=n_x x/M_s\), and distinguish free-ribosome fraction \(\phi_r=n_r r/M_s\) from total-ribosome fraction. Define

\[
\tau_\gamma=\frac{n_r}{\gamma(a)},\qquad
\tau_t=\frac{n_t}{n_s v_t},\qquad
\tau_e=\tau_t(1+w_m/w_t),\qquad
D=\tau_\gamma+\frac{K_t+s}{s}\tau_e.
\]

SI Eq. 37 gives, for a gratuitous target,

\[
\phi_p\simeq1-\phi_q-\phi_r-\lambda D.
\tag{W-allocation}
\]

The reduction assumes small resource dilution relative to the metabolic flux, negligible internal-nutrient dilution relative to consumption, and a sufficiently fixed enzyme ratio with common transcriptional resource dependence. Equal transporter/metabolic lengths in the default model support the ratio reduction. Balanced growth and these conditions must be checked before applying it to time-varying batch data. \(D\) generally changes with nutrient availability and resource state. In the translation-limited regime, \(\tau_e(K_t+s)/s\ll\tau_\gamma\), and for negligible free-ribosome fraction, this reduces to SI Eq. 40: \(\lambda\simeq(1-\phi_q-\phi_p)/\tau_\gamma\).

Add a controller protein fraction \(\phi_C\) that affects target expression but does not itself import/metabolize nutrient. With \(A=1-\phi_q-\phi_r\), the analogous allocation equation is

\[
\lambda\simeq\frac{A-\phi_p-\phi_C}{D}.
\tag{1}
\]

For a baseline without controller and an inhibited target with controller, **conditional on matched \(A,D\)**,

\[
\lambda_1-\lambda_0\simeq
\frac{\phi_{p,0}-\phi_{p,1}-\phi_{C,1}}{D}.
\tag{2}
\]

The resulting growth boundary is

\[
\boxed{\phi_{p,0}-\phi_{p,1}>\phi_{C,1}.}
\tag{3}
\]

It is an allocation boundary for the declared approximation. It is not a universal net-cost formula: altered housekeeping, resource-dependent elongation, RNA synthesis, folding/repair, preparation, replacement and controller delay can change or invalidate the matched comparison. If both arms already contain dCas9, compare their **incremental** controller allocation; if the counterfactual omits dCas9, its entire burden and preparation belong in the comparison. Ceroni's installed-controller experiments do not measure beneficial assembly from zero.

For a stable target at balanced growth, \(\nu_p=\lambda p\). Equation (1) consequently gives

\[
\nu_p\simeq\frac{M_s}{n_pD}\,
\phi_p(A-\phi_p-\phi_C).
\tag{4}
\]

This explains why induction need not increase production indefinitely. Under the same restrictive matched-parameter approximation, inhibiting from \(\phi_{p,0}\) to \(\phi_{p,1}<\phi_{p,0}\) increases production **per cell** precisely when

\[
(\phi_{p,0}-\phi_{p,1})(\phi_{p,0}+\phi_{p,1}-A)
>\phi_{C,1}\phi_{p,1}.
\tag{5}
\]

Growth improvement, Eq. (3), need not satisfy the stronger production criterion, Eq. (5). The fractions and \(D\) are endogenous steady-state outcomes in the original model; treating them as independently tunable experimental knobs would be another approximation. Equations (2)–(5) are transparent candidate boundaries to check, not numerical predictions for the Ceroni strains.

## 4. Finite batch accounting and observed output

SI S6 adds cell number \(N\) and a shared external nutrient pool:

\[
\dot N=(\lambda-d_N)N,\qquad
\dot s=k_{\rm in}-v_I N-d_s s.
\tag{6}
\]

All cellular states retain the equations above. \(s\) is the authors' number-based environmental variable; transferring it to measured concentration requires a declared culture volume and consistent conversion of \(K_t,k_{\rm in}\). \(d_N\) can denote removal/death; in a chemostat it equals the dilution rate \(d_s\). Closed batch sets input and removal to zero. Exponential growth with a constant fitted \(\lambda\) is not the full batch model.

Using the actual mass \(L\), direct differentiation gives

\[
Q=N(L+n_s s_i+a)+n_s s,
\qquad
\dot Q=n_s(k_{\rm in}-d_s s)
-d_NN(L+n_s s_i+a).
\tag{7}
\]

The cancellation uses \(\dot L=\gamma R_t-\lambda L\), \(\sum_xn_x\nu_x=\gamma R_t\), and Eq. (6). With a mass-consistent preparation \(L=M_s\), this is exactly SI Eq. 61. For arbitrary intracellular initialization, replacing \(L\) by the fixed \(M_s\) before the calculation is unwarranted. The abstract resource balance counts translated material as retained resource: it is not a calorimetric conservation law for the open biochemical cell, with heat and all chemical reservoirs resolved.

For the no-death closed batch with nonnegative states, \(Q=Q(0)\). In particular, on the fixed-mass manifold,

\[
N(t)M_s\le Q(0).
\tag{8}
\]

Thus growth cannot continue exponentially without limit. The target and controller share this finite protein/material budget. If identical resource preparations eventually convert all accessible pools into protein with identical fixed mass and no losses, their asymptotic cell numbers coincide; regulation can then change timing and allocation without increasing this idealized terminal biomass bound. Residual pools, incomplete conversion, maintenance losses, death and finite harvest time change that comparison. None can be inferred from an endpoint OD alone.

For stable target protein, let \(P=Np\). SI Eq. 59 and the added-target equation imply

\[
\dot P=N\nu_p-d_NP.
\tag{9}
\]

Growth dilution cancels: division redistributes protein and does not destroy total molecules. For a closed batch without target degradation,

\[
P(T)=P(0)+\int_0^T\nu_p(t)N(t)\,dt.
\tag{10}
\]

With matched initial target pools, the difference decomposes exactly as

\[
\Delta P(T)=
\int_0^T\left[
(\nu_{p,1}-\nu_{p,0})N_0
+\nu_{p,1}(N_1-N_0)
\right]dt.
\tag{11}
\]

When inhibition lowers per-cell synthesis, the first term is negative. Higher batch production requires the second term to exceed that loss. The controller's costs must already affect \(\nu_p,N\) and the initial resource preparation; adding an unrelated scalar penalty afterwards does not repair omitted chemistry. Equation (11) is an accounting decomposition, not causal mediation identification from two output curves.

Fluorescence needs an observation model. If \(U,F_m\) are population totals of immature and mature reporter, with maturation \(k\), losses \(\delta_U,\delta_M\), and calibrated detector coefficient \(c\),

\[
\dot U=N\nu_p-(k+\delta_U)U,\qquad
\dot F_m=kU-\delta_MF_m,\qquad
F_{\rm obs}=cF_m+F_{\rm bg}.
\tag{12}
\]

The contribution of synthesis at time \(t\) to mature reporter at \(T\) is weighted by

\[
K(T-t)=\frac{k\{e^{-\delta_M(T-t)}-
e^{-(k+\delta_U)(T-t)}\}}{k+\delta_U-\delta_M},
\tag{13}
\]

with continuous limit \(ku e^{-\delta_Mu}\) when the denominator vanishes. Loss rates must include relevant population removal if that removes measured reporter. The appropriate measured-output comparison is Eq. (11) with this common kernel, plus initial-pool contributions if unequal. These observation equations are an added analytical bridge, **not equations reported or calibrated by Weiße**. OD requires its own biomass/cell-size calibration; it is not automatically \(N\). The Ceroni audit preserves the corresponding distinction between fluorescence per OD, total fluorescence and translation rate.

## 5. What was identified and what remains unmeasured

Weiße's SI S3 identifies eight fitted parameters: \(w_r,w_e,w_q,\theta_r,\theta_{\rm nr},K_\gamma,K_q,k_{\rm cm}\), with \(K_\gamma\) obtained through fitting \(K_p=\gamma_{\max}/K_\gamma\). Growth rate and ribosomal mass fraction from Scott et al. (2010), strain EQ2, supplementary Table S2 columns 1–2, supplied the observations. The antibiotic conditions were 0, 2, 4, 8 and 12 µM chloramphenicol. Six nutrient-quality values \(n_s\) were chosen on a logarithmic spacing from 0.08 to 0.5; they were not independently measured energy yields. Adaptive MCMC supplied posterior distributions; the defaults are modes of the separate marginal distributions. [SI S3](https://swainlab.bio.ed.ac.uk/papers/pnas15sup.pdf).

The antibiotic extension traps translating complexes in inactive complexes at rate \(c_mk_{\rm cm}c_x\); these inactive ribosomes are diluted and counted in total ribosomal content. Broad posterior distributions, parameter correlations and the reported spread of information-matrix eigenvalues show that fitting the growth relations does not uniquely identify every microscopic parameter. SI S3.4 reports poorer fits in the two richest conditions and sensitivity to the chosen nutrient-quality mapping; fitting those qualities too caused overfitting with the available data. This is useful calibration evidence with explicit limitations, not an independently validated parameterization for another host, medium or controller.

Other constants mix literature values and modeling choices. Representative defaults are \(M_s=10^8\) amino acids, mean nonribosomal length 300 amino acids, \(\gamma_{\max}=1260\) amino acids per ribosome per minute, \(K_\gamma\simeq7\), \(n_s=0.5\), \(d_m=0.1\,\mathrm{min}^{-1}\), and \(\theta_r\simeq426.87\) versus \(\theta_{\rm nr}\simeq4.38\). The population illustrations instead use \(n_s=100\) and \(K_\gamma=3\times10^8\). Figure S5 initializes a cellular steady state, then resets transporter abundance to one to create a lag before consuming an unreplenished nutrient pool. It illustrates the extension; it is not a measured calibration of lag, controller construction or restart cost.

The model recovers growth relations and predicts host interactions in an engineered repressilator. Its gene-regulation evolutionary examples introduce competing variants in a specified architecture; they do not derive the origin of that architecture. In the single-nutrient chemostat example, the most competitive modeled enzyme-expression strategy has the lowest resident population yield among the compared strategies (paper Fig. 4C–D). With two nutrients, the trade-off and stable strategy change. These are model predictions, but they already show why competitive retention and higher collective yield need distinct criteria. Qualitative agreement, fitted data and untested predictions must retain different evidential roles. This review independently checked neither the original Scott raw observations nor the MCMC implementation, which was absent from the inspected archive.

### Source discrepancies relevant to reuse

The SI and distributed code should not be treated as silently interchangeable:

- SI Table S2 prints ribosome length \(n_r=7459\); the Facile specification, MATLAB driver and SBML parameter use **7549**. This note does not resolve which was used for every published result.
- SI Eq. 18 omits \(n_s\) on its right-hand side although preceding Eq. 17 contains it and following Eq. 19 incorporates it through \(\tau_m=n_m/(n_s v_m)\). The rate/mass derivations above retain the core resource equation.
- SI Eq. 20 prints \(K_m+s\) in the import term; SI Eq. 7, Eq. 21 and the distributed ODE use \(K_t+s\). The default values coincide, but symbolic generalization must keep import and metabolism distinct.

These are visible source discrepancies, not recovered author corrections. The exact identities here were derived from the explicitly displayed basic equations. Protein degradation in the repressilator extension, extra maintenance or resource recycling requires its own revised budget; Eq. (7) cannot simply be asserted for a changed reaction list.

## 6. The next discriminating calculation

The immediate useful comparison is a paid, finite-batch host/controller model, with baseline resource competition and observation laws fixed before evaluating a new outcome. For a Ceroni-type system it needs constitutive dCas9 synthesis, sgRNA production and turnover, burden sensing, target-promoter repression, controller binding/response delay, and measured growth/production readouts. Weiße supplies a host scaffold, not those controller equations. The basic omission of transcriptional resource spending is especially relevant when the added controller signal is an RNA: giving sgRNA an equation but no production cost is not full accounting.

First determine whether independently observed host/controller states can support the reduced boundary in Eq. (3). If its steady-state or matched-\(D\) assumptions fail, retain the full equations instead. Then evaluate Eq. (11), or its fluorescence-weighted counterpart, over a fixed finite harvest time. Separate identification data from the conditions used to test predicted positive and negative effects: low versus high target demand, controller burden, response delay and nutrient limitation. Growth rate, total/per-cell reporter and a capacity proxy alone are unlikely to identify all hidden states; additional resource/proteome and controller time courses, or honest parameter bounds, are needed. Endpoint product identities from the published workbook are not kinetic identification.

This provides a concrete conventional null: paid inhibition can help, hurt or merely shift output in time through resource competition. A new theory must add an independently stated quantitative restriction—such as a narrower gain boundary or a joint output-and-continuation probability derived from identified physical rates—and show where it changes predictions relative to that null. Calling the successful arm “more generative,” reproducing Eq. (11), or observing that a costly controller sometimes fails does not discriminate. A stochastic continuation claim would additionally require a justified event law and observations of variability or failure, which these deterministic ODEs and existing batch means do not supply.

No such additional identified restriction has been established here. The advance is the physical accounting and conditional failure boundary within an existing mechanism. The already-inspected Ceroni results remain retrospective evidence; a preregistered test would require genuinely unevaluated outcomes and a frozen comparison protocol. No universality, spontaneous architecture formation or mapping of G to a molecule follows from this review.
