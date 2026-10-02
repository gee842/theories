# Selecting the Selectors — IASEAI'27 draft, v2 (2026-10-02)

*These notes were written by Claude Opus 5.5, which drafted the paper. Ren has not yet reviewed v2. Every sentence of the paper is AI-drafted; none is Ren's verbatim. The v1 notes, sources and PDF are kept in `versions/v1/` (v1 is also commit 09b34eb).*

**Title.** *Selecting the Selectors: Recursive Selection and the Evolution of Control over AI Evaluation.* v1's subtitle was "Cross-Domain Capture, and the Answerability of AI Development". The new subtitle names the new central result.

**Venue.** IASEAI'27. Full submissions close **5 October 2026, AOE**.

**Format.** AAAI Press format (AuthorKit27), anonymous. The main text ends at the top of page 9, about 8.3 of the 10 allowed pages. References and four appendices (proofs; numerics and robustness; experiment protocol; a discrete-time version) follow, 14 pages in all. Appendices do not count toward the limit, but reviewers need not read them, so the main text is self-contained.

## What changed from v1, and why

The reviews (`reviews/`) agreed that v1 was "not yet" an important paper. R5 (GPT 6 ASTRA, endorsed by Ren) named the missing step: *recursive selection creates second-order selection pressure for mechanisms that increase control over future selection.* The GPT handoff (`sources/03-meta-attractor/2026-10-02-meta-attractor-context-and-review-gpt.md`, §§9–17) set the work order. v2 follows it.

| Change | Source |
|---|---|
| New central section: selection for conversion capacity (Prop. 2), counterexamples (Cor. 1), scope (Cor. 2), assistance (Cor. 3), ratchet linking capacity to capture thresholds (Prop. 3), and a numerical demonstration (Fig. 2) | R5 §2; handoff §§11.1–11.6, §17 |
| Neutral definition of a meta-attractor; capture-dependent and field-level cases as special cases; pathology as three separate conditions (P1 depletion, P2 weakened correction, P3 lost safe reachability); generative meta-attractors | R5 §8; handoff §§9.9, 10, 12; R4 objection 5 |
| "Neutral rules" replaced by "baseline rules"; c_i > 0 stated as relative to a baseline, not a verdict on harm | handoff §9.9 |
| Cascade computed within the support (seed condition) | R2 W6; handoff §9.1 |
| Explicit two-way entry μ(1−2x) in the ODE; exact results stated for μ = 0; logit integration; no hidden clamp | R1 W6, R2 W9, R3 W5, R4 obj. 7; handoff §9.4 |
| Release after reform needs re-seeding | handoff §9.2 |
| True detection time t_det; detection-delay law (Prop. 6iii) that diverges at βx = V_alarm/K; strict silencing needs β ≥ V_alarm/K | R2 W3; handoff §9.3 |
| Masking derived as a panel average | R4 plan 3(a) |
| Certificates: isolated tests fail, rows certify, the core is exact, robust firewall (Prop. 4) | R1 W5, R2 W2, R3 W4(iii), R4 obj. 3; handoff §9.8 |
| Margin reforms; keystone sets; a keystone can re-absorb its own reform (feedback ψ) | R2 W4(a), W5, W8; R3 W4(iv) |
| Hyperbolic classification; positive real eigenvalue at mixed equilibria | R2 W7; handoff §9.5 |
| No "monotone spread" claim | handoff §9.6 |
| Damage versus depletion corrected (V → K(1−h/ρ) when h < ρ) | R2 W10; handoff §9.7 |
| Formation given formal roles (cost normalization, β depending on x_F); the keystone label kept structural | R1 W7, R2 W5, R3 W4(i), R4 obj. 4; handoff §9.10 |
| Indistinguishability remark; error-access graph and min-cut over control units; layers of closure, stating which enter the equations | corpus survey A1; Benchmark v0.6 §14; handoff §12; R5 §§5–6 |
| Ecologies of practices: the field model already allows a different practice in each domain (coalitional meta-attractor); competition within a domain left open | R5 §3; handoff §12 |
| Safe reachability R^K_{H,B} for P3; answerable-closures test marked as normative | R5 §7; handoff §12; corpus survey A4 |
| Dependence remark kept (power's second role) and turned into "keep exit cheap" | essay §6; corpus survey A5 |
| Relation to scalable oversight; judge-lineage evidence; obedience is not field alignment, now tied to Cor. 3 | R1 W1, W3; R4 §5 |
| Positioning: Klüver's earlier "meta-attractor", Campbell, Barberà–Jackson, Acemoglu–Egorov–Sonin, Bowles et al., Gerlee–Anderson (closest precedent for appropriability), Hamilton/Price, performative power, Kwak, Hanson–Yosifon, Morris, k-core literature | R1 W2, R2 W1, R3 W1–W2, R4 obj. 6; handoff §14 |
| Citation fixes: Zheng no longer cited for self-preference; Khan and Narechania–Sitaraman cited for the instrument only; Shumailov, Taori and Kleinberg–Raghavan dropped from the claims they did not support | R3 W8–W10 |
| Notation: sans-serif domain labels, calligraphic sets, "cascade hull", "uninvadable", Z_C for configurations | R3 W11, R4 §1 |
| Cut: cancer analogy, "power's two roles" section (one remark remains), states paragraph, agent-fleet anecdote | R1 W8, R2 W10, R3 W7, W12, R4 obj. 9 |
| Numerics: φ = 0.11 (no exact ties), offset θ grid, robustness table (β, ψ, μ) | R2 W4(c), W9 |
| Statement of Contributions shortened; claims "standard tools" plainly | R4 plan 2 |

## The results, in brief

All are AI-drafted, proved in Appendix A, and checked in `build/checks.log`.

1. **Selection for conversion capacity (Prop. 2).** A carrier with capacity q and success profile y has payoff W(q) = χ q yᵀMy − C(q) relative to an otherwise identical carrier with q = 0, where M_ij = c_i L_i R̂_ij, χ is appropriability and L_i is the share of the return realized within the selection horizon. Mean capacity rises iff W′ > 0 on the trait support (Price). The return increases with χ, every R̂_ij and every y_j, and decreases with every correction rate d_i (proved via a monotonicity lemma). It vanishes with shared support, no conversion, or a short horizon. Convex cost gives a finite q*.
2. **Counterexamples belong to the theory (Cor. 1).** Shared support (free-riding), late returns or fast correction, no influence over rules, sanctions, failed transmission.
3. **Scope (Cor. 2).** The return is superlinear in the number of domains a carrier occupies. This is the formal reason general-purpose presence matters.
4. **Assistance (Cor. 3).** Capable assistance that lowers the marginal cost of conversion multiplies q*; if it also speeds correction, the two effects have opposite signs. This is the formal version of "obedience is not field alignment" (R1's suggested headline, in conditional form).
5. **Ratchet (Prop. 3).** With conversion B⁰ + q̄B̂, internally sustaining sets, cores and hulls are nondecreasing in q̄, trajectories are ordered, and the return to capacity is nondecreasing in the captured set. Fig. 2: in the θ = 0.6 field, where capture launched from development stays put, χ = 0.8 drives mean capacity above 0.9 by t ≈ 28 and captures every domain by t ≈ 184. χ = 0.3 (just above the threshold 0.25 in development) does the same by t ≈ 388. χ = 0.1 makes capacity vanish, and capture stays in development. Freezing capacity at its initial mean also leaves capture in development. The net advantage of capacity in development rises from 0.10 to 0.51 once the field is captured.
6. **Certificates (Prop. 4)** and **reforms (Prop. 5).** See the table above.
7. **Detection (Prop. 6).** In the coupled field the simulated detection delays match the analytic formula to within 0.3 time units (β = 0.1: 13.0 vs 13.1; β = 0.3: 60.8 vs 60.8; β = 0.5: 231.0 vs 231.0). The floor holds up to β = 0.4 and is breached from β = 0.5; the alarm never fires for β ≥ 0.6.

## Modelling decisions worth knowing

- **Representative carriers, not lineage clubs.** The first implementation split *all* conversion, incidental included, by χ, with each variant's private stock generated by that variant's own share. Variants then competed winner-take-all whatever their capacity, and the cost of capacity tipped the race to q = 0 even at χ = 0.8. The final model applies χ only to cultivated conversion and gives each carrier type a private stock driven by the practice's success profile. Its aggregate is exactly the field model with conversion B⁰ + q̄B̂. The discarded version is still informative. If appropriable support scales with a lineage's *own* size, control capacity pays only for lineages that are already large: capacity then evolves in dominant lineages and acts as an entry barrier. This finding is not in the paper.
- **Entry shifts thresholds by order √μ.** Persistent entry removes near-threshold equilibria through saddle-node bifurcations. At μ = 10⁻⁴, capture tips at θ = 0.975 and is lost at θ = 0.275, against the μ = 0 thresholds 1 and 0.26 (checked at T = 4000). The hysteresis sweep therefore uses μ = 10⁻⁶, which reproduces the skeleton (up at 1.025, down at 0.225 on the offset grid). For the same reason the multistability claim at θ = 0.6 counts only configurations with margins ≥ 0.05: 13 of the skeleton's 23, three of which capture both selectors without full capture.
- **Depth of capture slows recovery.** Smaller μ lets capture deepen in logit terms. After the same successful reform, standards unwinds +52, +63, +88 and +113 time units later for μ = 10⁻³, 10⁻⁴, 10⁻⁶ and 10⁻⁸. This is the "entrenchment" effect R1 and R3 suggested reporting rather than hiding in a clamp.
- **Realistic masking means delay, not silence.** Measured same-family lifts are 3.4–8.4 points (Awuni et al. 2026). The paper says silence needs something shared by every lineage, which formation supplies.

## What v2 does not do

- No experiment was run. The three-arm protocol (resources only; conversion with fixed capacity; heritable capacity), the ablations and an LLM-agent version are in Appendix C. All reviewers named an experiment as what would make the paper important.
- No empirical estimate of conversion or of β. The identification route (logit-velocity regression on lagged shares) is in Section 8.
- Competition among practices within one domain, endogenous creation of domains, and strategic masking are open.
- The handoff's discrete-time model is Appendix D, audited and recomputed (Γ_T values 0.8192, 1.8822, 0.5859, 0.3764 match direct accumulation). It is GPT's construction; the continuous-time field version is new here.
- Left out, as in v1: the covariance argument, the historical layer, the corpus's own vocabulary, and the parts of *When Capability Outruns Correction* that belong to that paper.

## Claim, assumption, evidence (for Ren's review)

| Claim in the paper | Rests on | Evidence in the paper |
|---|---|---|
| Selection favors control capacity iff appropriable, persistence-weighted return > marginal cost | Heritable capacity; representative carriers; private stock per Eq. (3); replicator growth on horizon-averaged payoff | Prop. 2 (proof, App. A); Fig. 2 |
| Shared rule support blocks it (free-riding) | χ = 0 cancels the private return | Prop. 2(iii), Cor. 1(a); Fig. 2 (χ = 0.1) |
| Cross-domain presence amplifies it superlinearly | Uniform R̂, positive off-diagonal conversion | Cor. 2 (algebra) |
| Capable assistance raises selected capacity | Assistance lowers C′ | Cor. 3 (algebra); AI channel is a hypothesis about magnitudes |
| Capacity and capture reinforce each other | Aggregation to B⁰ + q̄B̂ (uniform, slowly changing composition) | Prop. 3; Fig. 2(b) |
| Isolated tests cannot certify; rows can; the core is exact | Field model, μ = 0, no ties | Prop. 4; random-field check in checks.log |
| Reforms unravel only down to the core; a keystone can re-absorb its own reform | Field model, μ = 0 | Prop. 5; ψ table |
| Captured evaluation delays detection without bound as βx → V_alarm/K | Panel-average masking, Eq. (6) | Prop. 6; β table (formula matches simulation) |
| GPAI raises appropriability, scope, masking and speed mismatch | Hypotheses | Table 1, cited evidence on judge lineage and access; no measurement |

## Verification done

- **Numbers.** Every number in the text and both data figures come from `build/figures.py` (with `field.py` and `carrier.py`) and are printed in `build/checks.log`. A rebuild from this folder reproduced checks.log byte for byte. The hysteresis sweep is cached in `hyst-cache.json`; without the cache the run takes about three minutes of CPU.
- **Proofs.** Written and checked in this session. They have not been reviewed by anyone else. The new ones are Props. 2–3, the certificate parts of Prop. 4, the margin-reform parts of Prop. 5, Prop. 6(iii), and the eigenvalue part of Prop. 1(ii) (R2's suggestion, proved via Perron–Frobenius). A mathematician should reread them.
- **References verified on the web on 2026-10-02**, in addition to the v1 list in `versions/v1/NOTES-v1.md`: Verga et al. (arXiv 2404.18796); Kwak (CUP, pp. 71–98); EU AI Act Art. 31; Ito & Yamamichi (PNAS Nexus 3(11) pgae455); Klüver 2002 (Theory and Decision Library A vol. 34); Acemoglu–Egorov–Sonin (AER 102(4):1446–76); Gao–Schulman–Hilton (PMLR 202:10835–10866); Burns et al. (PMLR 235:4971–5012); Campbell 1974 (Schilpp, Open Court; pages given as 413–463, one source says 412); Hanson & Yosifon (U. Pa. L. Rev. 152:129); Carpenter, Zucker & Avorn (NEJM 358(13):1354–61); Kendal, Giraldeau & Laland (J. Theor. Biol. 260:210–219); Gerlee & Anderson (Phys. Biol. 12(5):056001); Awuni et al. (arXiv 2609.17857); Li et al. (ICLR 2026); Perdomo et al. (PMLR 119:7599–7609); Laurito et al. (PNAS 122, e2415697122); Żatuchin (arXiv 2610.00369, posted 30 September 2026); Morris (RES 67(1):57–78); Kempe et al. (KDD 2003:137–146); Goel et al. (ICML 2025, author list); Zhang et al. (AAAI 2017:245–251); Turner et al. (AIES 2020:385–391); Barberà & Jackson (QJE 119(3):1011–1048); Bowles, Choi & Hopfensitz (J. Theor. Biol. 223:135–147); Krakovna et al. (CEUR 2419); Itao & Kaneko (PNAS 122(15)); Bhawalkar et al.; Brummitt et al.; Hardt et al.; Greenblatt et al.; Laland et al. 1999. Cited from knowledge and not rechecked this session: Hamilton 1964, Price 1970 (publication record checked in the handoff), Seidman 1983, Büthe & Mattli, Irving et al., Christiano et al. 2018, Leike et al. 2018, Bai et al. 2022, Yuan et al. 2024, Krueger et al. 2020, plus the v1 classics.
- **Anonymity.** main.tex, references.bib and the three scripts contain no names, project names, usernames or paths. build.sh names the local Tectonic path, but it is not supplementary material.
- **Build.** No overfull boxes and no undefined references under the draft style.

## Before submitting (deadline 5 October 2026, AOE)

1. **OpenReview account.** IASEAI warns that approval "can take up to two weeks". If Ren has none, this is the binding constraint.
2. **Build the submitted PDF with pdfLaTeX** from `submission/`, unchanged (for example on Overleaf). Upload main.tex, references.bib, fig-schematic.tex, fig-capacity.tex, fig-field.tex, fig-hysteresis.tex, tab-robust.tex, aaai2027.sty and aaai2027.bst. pgfplots 1.18 and the TikZ `calc` library are needed. Check that the main text still ends before page 10.
3. **Supplementary material.** Appendix B says a script "is available as supplementary material". Upload `build/figures.py`, `field.py`, `carrier.py` and `checks.log` (and `hyst-cache.json`, optional) if the form allows. Otherwise delete that sentence.
4. **Track.** Archival (AAAI Press proceedings; no parallel archival review) or non-archival. Both need in-person attendance.
5. **Title, abstract and author list** are frozen at the deadline.
6. **Competing-interests disclosure** per IASEAI policy; it is not shown to reviewers.
7. **AI assistance.** The guide is silent; acknowledgments are removed for review. Decide what the camera-ready says. The paper is AI-drafted from Ren's ideas, the essay, the GPT review and handoff, and the corpus.

## Open for Ren

- **Title.** Current: "…Recursive Selection and the Evolution of Control over AI Evaluation". Alternatives: "Selecting the Selectors: When Success Buys Control over Future Selection"; "Selection for Control over Selection: Capture, Correction and AI Evaluation".
- **"Meta-attractor" is not in the abstract** (R4 advised against it). It is defined in Section 3, with Klüver's earlier use cited. Add it to the abstract if you prefer.
- **Statement of Contributions** still says conceptual antecedents appeared in informal essays. Keep it only if a meta-attractor essay is publicly posted.
- **Cut material.** The agent-fleet anecdote, the cancer analogy, the states paragraph, and most of "power's two roles" are gone. Power survives as Remark 4 (dependence) and the "keep exit cheap" principle. Forsgren is still not cited.
- **A review round on v2** could check the new proofs and the positioning. The four-reviewer round on v1 is the reference point for its cost; it should not run without your go-ahead.
