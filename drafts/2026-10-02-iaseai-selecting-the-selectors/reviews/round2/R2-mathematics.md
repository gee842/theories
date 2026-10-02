# Review R2 (round 2): mathematics and modelling

*AI review of v2. On 2026-10-02 Ren asked for "another round of independent review like before, how ready is this for the reviewers?". The reviewer was a Claude Opus 5.5 subagent, briefed as an applied mathematician working on dynamical systems, evolutionary game theory, monotone systems and threshold cascades. It read only the anonymous v2 PDF, `submission/` (main.tex, references.bib, figure and table sources) and `build/figures.py`, `field.py`, `carrier.py` and `checks.log`. It did not read NOTES.md, the round-1 reviews or the corpus. It re-ran the numerics from scratch and wrote independent implementations. Its report is reproduced verbatim below.*

---

# Review: "Selecting the Selectors: Recursive Selection and the Evolution of Control over AI Evaluation" (IASEAI'27, archival track)

**Reviewer expertise:** dynamical systems, evolutionary game theory, monotone (cooperative) systems, threshold cascades.

**Page references** are to the 14-page draft PDF: main text pp. 1–9, references pp. 9–12, Appendix A pp. 12–13, Appendices B–D pp. 13–14.

## 1. Summary

The paper asks when selection favours practices that acquire control over later selection.

**Field model (§3, Prop. 1).** There are n selection domains (for AI: development, evaluation, standards, procurement, formation, information). In each domain a practice holds a share x_i and enjoys rule support r_i. Success in domain j converts into support in domain i at rate b_ij (Eqs. 1–2). Define normalized conversion R_ij = a_i b_ij/(c_i d_i). A vertex configuration Z_C is then stable iff C is internally sustaining (s_i(C) > 1 on C) and uninvadable (s_i(C) < 1 off C). No equilibrium with an interior share is linearly stable.

**Capacity (§4).** Carriers have heritable conversion capacity q, of which a fraction χ is appropriable. Averaging the appropriable stock over a selection horizon gives W(q) = χ q yᵀMy − C(q), with M_ij = c_i L_i R̂_ij (Eq. 4). Capacity is therefore selected iff χ yᵀMy > C′(q) (Prop. 2).
- Cor. 1: counterexamples.
- Cor. 2: scope.
- Cor. 3: assistance.
- Prop. 3, a "ratchet": with aggregate conversion B⁰ + q̄B̂, internal sustainability, the core and cascade hulls are monotone in q̄.

**Coupled fields (§5).**
- Certificates (Prop. 4): a row sum below one certifies its domain, and the weighted core is exact.
- Cascades, reforms and keystone sets (Prop. 5).

**Detection (§6).** A practice depletes a shared condition V. Correction relies on a masked panel report Ṽ = V + βx_E(K − V). Prop. 6 gives a detection threshold, a silencing condition, and a delay bound that diverges at βx̄ = V_alarm/K. Four remarks cover recalibration, min-cuts, formation and dependence.

**Application (§§7–9).** The model is mapped to frontier AI, with tests and governance principles: lower the appropriability of rule-making, firewall the selectors, certify rows, reform keystone sets.

**Numerics.** A pure-Python script generates the six-domain illustrations (Figs. 2–4, Table 2).

## 2. Scores

| Criterion | Score (1–10) |
|---|---|
| Relevance | 8 |
| Quality | 5 |
| Clarity | 6 |
| Originality | 5 |
| Significance/impact | 5 |

**Overall recommendation (archival track): borderline.**
- As submitted I would lean towards weak reject, because several false statements in §§5–8 and Remark 3 can be checked quickly.
- With the must-fix list in §5, I would move to weak accept.

**Confidence: 4/5.**

## 3. Strengths

1. **A well-posed question, framed in value-neutral terms.**
   - "When is the capacity to reshape selection itself selected?" is the right question.
   - Separating capture (stability of Z_C) from pathology (P1–P3) avoids conflating concentration, capture and harm.

2. **The core field mathematics is correct, and the proofs are short and complete.** I checked every statement by hand and numerically; see the table in §4.
   - Prop. 1(ii) is a neat argument. A zero-diagonal Metzler block cannot be Hurwitz. A Perron–Frobenius crossing of ρ(Ω(λ)) = 1 then gives a positive eigenvalue whenever B_MM has a cycle.
   - Prop. 4(b)–(c) pairs a conservative, decentralized certificate (row sums) with an exact one (the weighted core). Both are legible to policy makers.

3. **Actionable structure.** The monotone structure yields crisp rules:
   - "check the reformed row against what remains captured";
   - "a keystone can re-absorb its own reform" (the ψ < 0.14 example);
   - "firewall the selector's row".
   Together they give a usable vocabulary for evaluator independence, counted in control units.

4. **Exemplary reproducibility.** I copied figures.py, field.py and carrier.py to my own directory and ran them without hyst-cache.json (5 min 27 s wall, 210 s CPU).
   - checks.log is byte-identical to the authors' file.
   - The recomputed hyst-cache.json is identical to theirs.
   - fig-capacity.tex, fig-field.tex, fig-hysteresis.tex and tab-robust.tex are byte-identical to both build/ and submission/.
   - Every number in the text, Figs. 2–4 and Table 2 traces to the log, with the exceptions in W9.
   - In the authors' own code, detection times change by at most 0.05 across step sizes DT ∈ {0.1, 0.05, 0.025}.

5. **Independent confirmation of the numerics.** I wrote my own code from the equations: an adaptive Dormand–Prince 5(4) integrator in original coordinates, logit coordinates for long μ = 0 runs, and a separate carrier implementation. It reproduces:
   - **Fig. 2.** χ = 0.8: q̄ > 0.9 at t = 28, full capture at t = 183 (the paper reports 184 because it samples every 2 units). χ = 0.3: 247 and 387 (paper 248 and 388). χ = 0.1: the high-capacity type is displaced.
   - **The χ = 0.25 threshold.** In a scan, capacity declines in development at χ = 0.24, is neutral at 0.25, and rises at 0.26.
   - **The 0.89 threshold.** With frozen capacity, the capacity cost included and μ = 10⁻⁸, q̄ = 0.885 stays in development and q̄ = 0.895 cascades.
   - **Cascade times.** P/E/I/S/F at 42.5/55.3/55.3/66.7/105.4. Standards are re-absorbed at 37.2.
   - **Detection delays** of 13.08/31.77/60.78/112.15/230.97/387.38, against Table 2's 13.0/31.7/60.8/112.2/231.0/387.4.
   - **Table 2:** the ψ and μ rows.
   - **Fig. 4.**
   - **Persistence under entry.** I simulated from each Z_C. Exactly 13 of the 23 θ = 0.6 configurations persist at μ = 10⁻⁴, including DESF, DEPF and DEFI. The 10 with margin 0.01 collapse to D.

6. **Honest scoping in many places.**
   - Counterexamples (Cor. 1).
   - "The numbers illustrate the propositions and estimate nothing".
   - Explicit normative premises and falsifiers.
   - An identification strategy (§8).
   - An admission that the tools are standard.

## 4. Weaknesses

### 4.0 Statement-by-statement verdicts

Wherever R_ij is used, c_i > 0 is implicitly required (see W8).

| # | Statement (location) | Verdict | Evidence / fix |
|---|---|---|---|
| 1 | n = 1 analysis (p. 3; App. A p. 12) | Correct | Equilibria, eigenvalues, saddle determinant and the dΦ/dt identity checked. |
| 2 | Lemma 1 (p. 12) | Correct | Kamke condition holds. The formation extension needs g_i ≥ 0 (implicit). |
| 3 | Prop. 1(i) (p. 3) | Correct with a fix | Needs c_i > 0 for all i as a standing assumption. p. 3 explicitly allows c_i ≤ 0, and then s_i is meaningless. 4,412 hyperbolic configurations in random fields (n = 2–5): the s-criterion agrees with Jacobian stability, 0 mismatches. |
| 4 | Prop. 1(ii) (p. 3; proof p. 12) | Correct | 229/229 random mixed equilibria with a cycle in B_MM have a positive real eigenvalue. In 171 acyclic cases the spectral abscissa is exactly 0 (non-hyperbolic). The result depends on the payoff being independent of x_i (W6). |
| 5 | Eq. (4): W(q) with M = cLR̂ (p. 4; proof p. 12) | Correct under its assumptions | Numerical horizon average matches χq yᵀMy to 1.4·10⁻⁸ (200 random cases). Unstated assumptions: y is frozen over the horizon, ζ is reset to 0 at each horizon, and the cost does not depend on carrier size. c_i cancels: M_ij = a_i b̂_ij L_i/d_i. |
| 6 | Prop. 2(i), (iv) | Correct | (iv) holds for fixed y. |
| 7 | Prop. 2(ii) | Correct | Continuous-time Price identity verified numerically. |
| 8 | Prop. 2(iii) | Correct with a fix | "Increases" should read "is nondecreasing". The proof's "linear in … each y_j" is false: yᵀMy is quadratic in y_j, and monotonicity holds only because M ≥ 0. State that b̂ is held fixed when varying d_i or R̂_ij. ℓ(u) is decreasing (verified). |
| 9 | Cor. 1(a)–(d) | Correct | (b) is a limit statement. Better: "when ε_i d_i T is small enough that χyᵀMy < C′(q)". |
| 10 | Cor. 1(e) | Overstated | Without transmission, capacity does not respond to selection; it is not "selected against". The proof's transmission term E[WΔq]/W̄ divides by a relative payoff that can be ≤ 0; it should use absolute fitness. |
| 11 | Cor. 2 (p. 4) | Correct as stated | It assumes weight one on each domain, so carrier size grows with \|S\|. |
| 12 | §8 prediction (a), "holding size fixed … superlinearly" (p. 8); the scope readings in the abstract and §7 | False / overstated | Spread a fixed total size Y over \|S\| domains. The return is Y²cL[φ̂ + (η̂ − φ̂)/\|S\|]. It decreases in \|S\| if η̂ > φ̂. If φ̂ > η̂ it increases but is concave and bounded by Y²cLφ̂. It is never superlinear. |
| 13 | Cor. 3 (p. 4) | Overstated | The factor 1 + α holds only for the quadratic cost of (iv). For C = γq³/3 the factor is √(1 + α): 1.41 rather than 2 at α = 1. |
| 14 | Aggregation to B⁰ + q̄B̂ (p. 4) | Not justified as stated | Three problems (details in W2). (1) It omits the capacity cost, which enters as c_i + γq̄; the paper's own 0.89 uses that cost. (2) It requires representative production, which contradicts Eq. (3). (3) It requires q̄ to be uniform across domains, which fails in the paper's own run. |
| 15 | Prop. 3(i) (p. 4; proof p. 12) | Correct for fixed costs; false once the capacity cost is included | Fixed costs: 0/2,000 random nesting violations, and 0/40 trajectory-ordering violations with q̄(t) ≤ q̄′(t). Cost included: 105/2,000 violations. For n = 1 with b⁰ = 1.2, b̂ = 0.01, γ = 0.5, R = 1.20/0.96/0.81 at q̄ = 0/0.5/1. Sufficient condition: c_i b̂_ij ≥ γ b⁰_ij entrywise. It holds in the paper's parameters. |
| 16 | Prop. 3(ii) | Correct | Trivial. |
| 17 | Prop. 4(a) (p. 5) | Correct | Construction checked for m = 2, 3, 5: the only stable configurations are ∅ and N. |
| 18 | Prop. 4(b), (d) | Correct | 180 random runs, 0 violations. |
| 19 | Prop. 4(c) | Correct; wording | From near the top state, the limit support equals core(N) in 120/120 random fields (logit coordinates). The first clause is garbled. "No capture attracts every state with all shares below one" should read "every share tends to zero from every state with all shares below one". |
| 20 | Prop. 5(i) | Correct | 60 random fields, 0 violations. |
| 21 | Prop. 5(ii) | Correct | Randomized reforms in logit coordinates, each setting the reformed s_i(C) to 0.9. In 98/108 every domain outside core(C∖Q) fell below 0.007 within 30,000 units. In the other 10, the reformed domains had collapsed and the rest were unwinding in sequence, as the proof predicts: e.g. dz/dt = −0.32 at z = 1024. Reforms leaving s_i > 1 were re-absorbed in 58/58. "From states near Z_C" should say "near the reformed equilibrium", since a d- or b-reform moves r. At μ = 0, unwinding time grows without bound with the duration of capture. |
| 22 | Prop. 5(iii) | Correct | Needs re-seeding when μ = 0, as stated. |
| 23 | "Finding a minimum keystone set is the collapsed k-core problem, NP-hard" (p. 5) | False | Under the paper's definition, core(C∖Q) ≠ C∖Q, Q is a keystone set iff some k ∈ C∖Q has s_k(C) − Σ_{j∈Q}R_kj < 1. The minimum is found greedily for each k, in O(\|C\|² log\|C\|). Brute force agrees with greedy on 271/271 random cores. Two related problems are NP-hard: the smallest Q that empties the core (it contains minimum feedback vertex set), and the budgeted maximum-collapse problem (collapsed k-core; Zhang et al. 2017). |
| 24 | "Stability of Z_C involves only the rows in C and the inbound conversion from C" (p. 5) | Correct | |
| 25 | Prop. 6(i)–(iii) (p. 6; proof p. 13) | Correct (elementary) | My independent simulation matches the logistic analogue in the proof to within 0.08 for β ≤ 0.5, and 0.34 at β = 0.55. |
| 26 | "For β ≥ 0.6 the alarm never fires" (p. 6; Table 2) | False at β = 0.6 | With μ = 10⁻⁴, x_E = 1 − O(μ), so βx_E < 0.6. The alarm then fires at t ≈ 2,359, when V ≈ 3·10⁻⁴, beyond the 600-unit horizon. The claim is true for β ≥ 0.61. This follows from Prop. 6(ii) itself. |
| 27 | Remark 1 (p. 6) | Correct but trivial; title overstated | The non-identifiability holds only for a snapshot with x_E unknown. With known dynamics, recalibration becomes possible: Fig. 3c itself shows Ṽ rising while V falls, which is a detectable anomaly. |
| 28 | Remark 2 | Correct as a necessary condition | Menger-type; verbal. |
| 29 | Remark 3, first half | Correct with a fix | The row multiplier needs g_i < c⁰_i. "If g_i ≥ c⁰_i the practice holds the domain with no rule support" needs strict >; at equality the domain is neutral. |
| 30 | Remark 3, second half: β = β⁰ + β¹x_F makes mixed-lineage panels fail | Does not follow | In Eq. (6), β multiplies x_E, so out-of-lineage evaluators stay accurate whatever x_F is. Statements built on this: p. 6 "which formation supplies"; p. 7 "Shared formation raises it for every lineage at once"; p. 9 "covers formation". |
| 31 | Remark 4 | Correct | Threshold algebra and cooperativity in the order (x↑, r↑, V↓) checked. |
| 32 | Identification (p. 8) | Correct derivation | Needs the kernel rate ε_i d_i to be known, or nonlinear estimation. |
| 33 | Appendix D | Correct | Γ_T = 0.82/1.88/0.59/0.38 and the derivative formula verified. |
| 34 | ψ < 0.14 for the keystone reform (p. 5; Table 2) | Correct for μ = 0 | At μ = 10⁻⁶ and 10⁻⁸ the outcome switches between ψ = 0.1395 and 0.1405. At μ = 10⁻⁴ (the paper's rate) the field unwinds up to ψ = 0.142 and stays captured from 0.145. So "only if" fails at the simulated μ for ψ ∈ (0.140, 0.142]; this is the predicted O(√μ) shift. |
| 35 | "Each of them is a keystone (inbound 0.88 without it)" (p. 13) | Number wrong | The right value is 0.96 (= 0.3 + 3·0.22). The script computes inbound conversion into the *removed* domain. The conclusion is unchanged. |
| 36 | "General-purpose coupling changes which configuration a development seed reaches, not which can exist" (p. 5) | False as worded | There are 23 stable configurations at θ = 0.6 and only 2 at θ = 1.2. |
| 37 | "Keystone status shifts from the origin to sets of selectors" (p. 8) | Misdescribes App. B | App. B shows keystone pairs that all contain D. At θ = 0 every remaining domain is a keystone, not specifically the selectors. |
| 38 | "At μ = 10⁻⁴ capture tips at θ = 0.975 and is lost at θ = 0.275" (p. 13) | Correct but unscripted | Confirmed by my runs: from a fresh start, θ = 0.975 tips after about 1,930 units (it does not tip at μ ≤ 10⁻⁶). A quasi-static sweep with 1,500 units per step misses the tipping. figures.py computes neither number. |
| 39 | Frozen-capacity counterfactual and "threshold 0.89" (pp. 5, 13) | Direction correct; details inconsistent | 0.89 is the μ → 0 value with the capacity cost (confirmed in item 5 of §3). The script's counterfactual omits the cost, although its log line says "cost +0.025". At μ = 10⁻⁴ the frozen threshold is ≈ 0.72–0.75 without the cost and ≈ 0.83–0.85 with it. |
| 40 | "χ = 0.25, at which capacity starts to pay in development" (p. 5) | Correct only for representative carriers | With own-success production as Eq. (3) defines it, the threshold is 0.55–0.6 from a 50/50 start, and a rare high-capacity type cannot invade (W1). |
| 41 | "Net advantage of capacity in development is five times its initial value" (p. 5) | Correct, but driven by one parameter | The ratio 0.510/0.102 comes from capacity adding feedback into development (ψ̂ = 0.1), which incidental conversion lacks. With ψ̂ = 0 the ratio is 1.17. Cascade timing is unaffected. |

### 4.1 Weaknesses, most serious first

**W1 [MAJOR]. The illustration of the central result does not implement the model stated in the text, and the quoted threshold depends on the difference.**

What the text specifies:
- Eq. (3) defines appropriable support through the carrier's *own* success profile y: "its share of decisions in each domain".
- W(q) charges a carrier-level cost C(q) and resets ζ at each horizon.

What carrier.py does instead:
- (a) It credits type k with appropriable support produced from the *whole practice's* success, χq_k Σ_j b̂_ij X_j. This is the "(representative carriers)" assumption, disclosed only in Appendix B and the Limitations. A type therefore receives carrier-keyed support generated by other types' decisions.
- (b) It charges the cost per decision (0.05q).
- (c) It lets types compete separately in each domain, so no carrier spans domains. The selection gradient in domain i is the row χc_i(R̂X)_i − γ. The quadratic form yᵀMy is never exercised, and no figure illustrates Cor. 2.
- (d) It has no horizon (L_i = 1).

The quoted χ = 0.25 is γ/R̂_DD under (a)–(d).

I reran the same field with appropriable production from the type's own success (y_jk = x_jk, as Eq. 3 states), everything else unchanged:
- The χ threshold from a 50/50 start moves to 0.55–0.6.
- At χ = 0.3, 0.4 and 0.5 the high-capacity type is displaced and capture stays in development.
- A high-capacity type that starts at 5% cannot invade even at χ = 0.8. Under the paper's variant it invades, and every domain is captured by t ≈ 200.

The reason is structural. With own-success production the per-decision return χΣ_j R̂_ij x_jk scales with the type's own frequency, while its cost scales with its own decisions. This creates positive frequency dependence and an invasion barrier.

Making carriers span domains (common type frequencies, fitness equal to the decision-weighted payoff) changes little in either variant. The qualitative ratchet survives at high χ (χ ≥ 0.6 under own-success production).

This is the headline result, so the text and the code must agree. The invasion barrier is also a sharper prediction than anything the paper currently makes: capacity is selected first among carriers that already dominate.

**W2 [MAJOR]. The aggregation behind the ratchet (p. 4) is incomplete, and Prop. 3 fails once the missing term is added.**

Summing the type-specific share equations gives exactly
d/dt logit X_i = κ_i[a_i(r_i + Σ_k f_ik ζ_ik) − c_i − γq̄_i].
So the aggregate field has conversion B⁰ + q̄B̂ *and cost c_i + γq̄*. It also needs (a) from W1 and a q̄ that is uniform across domains.

q̄ is not uniform in the paper's own run. At χ = 0.8 and t = 50, q̄ by domain (D/E/S/P/F/I) is 0.99/0.93/0.87/0.97/0.70/0.93.

The paper mixes the two conventions:
- "Mean capacity above 0.89" includes the cost: figures.py prints (0.6 + 0.5q)/(1 + 0.05q) > 1.
- "Inbound conversion 0.85" at q̄ = 0.5 excludes it.
- So does the scripted frozen-capacity counterfactual.

With the cost included, Prop. 3(i) fails in general (counterexamples in row 15). Please:
- state the aggregate together with its three assumptions;
- add the entrywise sufficient condition c_i b̂_ij ≥ γb⁰_ij;
- apply the cost in the counterfactual.

**W3 [MAJOR as a group; each fix is small]. False or overstated statements that a reviewer can check quickly.**

- **(i) Keystone NP-hardness (p. 5; row 23).** Suggested replacement: "Under this definition a minimum keystone set is computable in polynomial time. Finding the smallest reform set that unravels all of C, or the budgeted maximum-collapse set, is NP-hard in general. For R ∈ {0, ½} on an undirected graph the former is minimum feedback vertex set."
- **(ii) §8 prediction (a) (row 12).** Suggested replacement: "Holding per-domain presence fixed, investment rises superlinearly with the number of domains. Holding total size fixed, it rises with scope only if cross-domain conversion per unit capacity exceeds within-domain conversion (φ̂ > η̂), and then saturates."
- **(iii) Formation masking (row 30).** Model it explicitly, for example Ṽ = V + min{1, βx_E + β_F x_F}(K − V). Prop. 6 then holds with βx_E replaced by βx_E + β_F x_F, and silencing no longer requires in-lineage evaluators: β_F x_F ≥ V_alarm/K suffices.
- **(iv) Cor. 3.** Add "under the quadratic cost of (iv); for any convex C the selected capacity rises".
- **(v) "β ≥ 0.6 never fires".** Replace with "never fires for β > 0.6/x_E; at β = 0.6 the alarm fires only at t ≈ 2,360, after V < 10⁻³".
- **(vi) Small corrections:** 0.88 → 0.96; "not which can exist"; "keystone status shifts … to sets of selectors" (rows 35–37).
- **(vii) AI control (p. 7).** The paper calls the monitor in Greenblatt et al. (2024) "a trusted one of different provenance … a firewall in our terms". In that work the trusted monitor is GPT-3.5 and the untrusted model is GPT-4, from the same developer; trust comes from the capability gap. Under the paper's own control-unit accounting, the two would be one unit.
- **(viii) Abstract and §1.** "Its kernel is the cross-domain conversion that also decides whether capture is stable" is not accurate. The kernel is the persistence-weighted *cultivated* conversion diag(cL)R̂, while capture is decided by R⁰ + q̄R̂. The two coincide only if R̂ ∝ R⁰.

**W4 [MAJOR]. Novelty is overstated, and the closest precedents are missing.**

The Statement of Contributions places the novelty in the capacity result. That result is a horizon average of a linear ODE plus the Price equation, and its structure has direct antecedents:
- **Krakauer, Page & Erwin (2009, Am. Nat. 173:26–40).** Constructing a shared niche leads to a tragedy of the commons that eliminates niche construction, unless the niche can be monopolised. This is essentially Cor. 1(a) and the appropriability condition.
- **Lehmann (2008, Evolution 62:549–566).** An inclusive-fitness analysis of niche-constructing traits whose effects persist across generations. It weights returns by relatedness to future beneficiaries and by persistence, which is the structure of χ and L_i.
- **Kylafis & Loreau (2008, Ecology Letters 11:1072–1081).**
- **Economics:**
  - appropriability (Arrow 1962; Teece 1986);
  - collective action and selective incentives in lobbying (Olson 1965);
  - rent seeking (Tullock 1967; Krueger 1974);
  - standard setting with essential patents (Lerner & Tirole 2006, 2015; Simcoe 2012). This is the direct empirical analogue of "appropriability of rule-making".

Other citation issues:
- Gerlee & Anderson (2015) is not "the closest precedent".
- Replicator dynamics are used but never cited. Hofbauer & Sigmund (1998) is in references.bib but not cited.

The field results are, as the paper itself says, standard:
- Prop. 4(c) is the top-trajectory / greatest-fixed-point argument for monotone systems (cf. Morris 2000).
- Props. 1 and 6 are direct linearization and algebra.

The honest description is: a new combination and application, built with standard mathematics.

**W5 [MINOR]. The role of μ is under-reported in quantitative statements.**

Exact results are for μ = 0, but several statements apply μ = 0 thresholds to μ = 10⁻⁴ runs:
- the ψ "only if" (row 34);
- "never fires" (row 26);
- the frozen threshold (row 39);
- the θ tipping point (row 38).

Timings scale with log(1/μ):

| μ | 10⁻³ | 10⁻⁴ | 10⁻⁶ | 10⁻⁸ | 0 |
|---|---|---|---|---|---|
| Full capture time, χ = 0.8 | 120 | 183 | 266 | 273 | 273 |
| Full capture time, χ = 0.3 | 233 | 387 | 578 | 708 | 868 |

Unwinding times vary in the same way (+52 to +113 in Table 2).

Measured threshold shifts match m* ≈ 2√(R_self μ/(κc)), using the reformed quantities of the switching domain. For example, the predicted ψ crossover is 0.1446, and the observed one lies between 0.142 and 0.145. Please state which μ each number refers to, and give the √μ rule in the main text.

**W6 [MINOR]. The model's structure drives its all-or-nothing results.**

The payoff a_i r_i − c_i does not depend on x_i, so Eq. (1) behaves as a switch.
- Any negative frequency dependence, a term −e_i x_i (congestion, product differentiation, antitrust caps), puts −κx(1 − x)e on the diagonal at interior equilibria. Partial capture can then be stable, and both Prop. 1(ii) and "stability belongs to sets of domains" fail.
- Linear conversion is what makes the k-core analogy exact.

Both points belong in the Limitations.

**W7 [MINOR]. Density and clarity.**
- Nine pages carry many verbal constructs that no result uses: the reachability sets of P3, layers of closure, error-access graphs, control units, the closure test, answerability.
- Meanwhile the assumptions that matter sit in Appendix B: representative carriers, the per-horizon reset of ζ, and the μ-dependence. Reviewers are not obliged to read the appendices.
- In Fig. 3d the "never" label is clipped.

**W8 [MINOR]. Technical details.**
- State c_i > 0 for all i as a standing assumption.
- Write M_ij = a_i b̂_ij L_i/d_i (c_i cancels).
- Fix the wording of Prop. 4(c) (row 19), the proof of Prop. 2(iii) (row 8), Cor. 1(e) (row 10), the strict inequality in Remark 3 (row 29), and "near Z_C" in Prop. 5(ii) (row 21).
- Prediction (d) refers to "the share of evaluated items produced by the judge's lineage", but the model's gap βx_E(K − V) depends on panel composition, not item provenance.
- "Any heritable trait whose effect on later selection is appropriable … obeys the same condition" (p. 4) is an unproved generalization; the form of the return depends on the mechanism.

**W9 [MINOR]. Reproducibility gaps.**
- The μ = 10⁻⁴ tipping and loss thresholds (p. 13) are not produced by the script.
- The persistence of the 13 configurations under entry is inferred from their margins (≥ 0.05), not simulated. The claim is true; I simulated it.
- The counterfactual's code and log disagree about the cost.

**W10 [MINOR]. No empirical anchoring.**
- No parameter is measured.
- The mapping from same-family preference in percentage points to β is not given. Awuni et al. (2026) report a 3.4–8.4 pp lift.
- Predictions (b) and (c) are qualitative.

## 5. Readiness

**Estimated probability of archival acceptance as it stands: about 25%**, against a base rate of roughly 19%.
- The paper is more rigorous and better engineered than the median submission.
- But it is dense and abstract.
- A technical reviewer can find W1–W4 within an hour.
- A governance reviewer may see an uncalibrated toy model.

**Must fix before submission** (each item could be grounds for rejection):
1. **The W3 statements:** keystone NP-hardness, prediction (a), formation-β, Cor. 3, β = 0.6, 0.88, "not which can exist", "sets of selectors", AI-control provenance, and the kernel claim in the abstract.
2. **A correct aggregation paragraph and ratchet condition (W2),** including the capacity cost, and fix the counterfactual's cost.
3. **Reconcile Eq. (3) with the simulation (W1).** At minimum, move the representative-carrier assumption into the main text and add one sentence on the own-success result (threshold 0.55–0.6, invasion barrier). Preferably show both variants in Fig. 2 or Table 2.
4. **Related work and novelty wording (W4).** Cite Krakauer et al. 2009, Lehmann 2008, Kylafis & Loreau 2008, Olson, Arrow/Teece, Lerner & Tirole, and Hofbauer & Sigmund. Replace "all formal content is new" with "new results in this setting, obtained with standard tools".
5. **Smaller fixes:** the c_i > 0 standing assumption, the wording of Prop. 4(c), and a statement of which μ each quantitative claim refers to.

**What would raise the probability most within three days.** Do items 1–4 and recover space by trimming the verbal constructs in §§3, 6 and 9 (W7). Use that space for:
- (i) one paragraph of robustness, covering the production assumption, the capacity range, cost curvature and μ;
- (ii) a two-sentence statement of the sharpest testable prediction: the appropriability condition, together with the invasion barrier under own-success production.

I would expect this to bring the probability to about 35–40%.

## 6. Could this paper, in its current version, be an important paper that advances alignment?

**No, not in its current version.** It could become a useful reference for work on structural risk and governance.

**What it contributes:**
- A clear condition for when the capacity to shape evaluation is selected: appropriability × persistence × conversion, against marginal cost. This justifies a concrete lever: make rule-making non-appropriable through interface-neutral standards, rotating held-out benchmarks and conflict-of-interest rules.
- A precise vocabulary for evaluator independence: inbound conversion below one, counted in control units.
- A detection-delay law that motivates measuring same-lineage masking in AI judges.

**Why it is not yet important:**
- The formal core is elementary, and it is close to known results in niche-construction theory and the economics of appropriability.
- The quantitative illustration of the main result rests on a modeling choice that the main text does not state, and that choice reverses the conclusions at moderate χ (W1).
- The channel the paper relies on for silencing, shared formation, is asserted rather than modeled (Remark 3).
- No parameter is estimated.
- Per-system alignment, the field's central technical problem, lies outside the model by design.

**What would change this:**
- Running the cheap simulated-carrier experiment of Appendix C, to see whether rising capacity appears only when returns are appropriable.
- Estimating inbound conversion and β for one real evaluation ecosystem, for example LLM-judge provenance and benchmark authorship.

## 7. Questions for the authors

1. Eq. (3) defines y as the carrier's own share, yet carrier.py credits each type with support produced by the whole practice. Which mechanism do you intend? Under own-success production, do you accept a threshold of about 0.55–0.6 and an invasion barrier for rare high-capacity carriers?
2. Is capacity a carrier-level trait that spans domains? If so, why does the simulation evolve type frequencies separately in each domain, and which figure illustrates the quadratic form or Cor. 2?
3. Does the aggregate in Prop. 3 include the capacity cost? Your 0.89 does; the text and the 0.85 figure do not. Will you add the condition c_i b̂_ij ≥ γb⁰_ij?
4. Prediction (a) holds "size" fixed. Do you mean per-domain share or total size? If total size, how do you reconcile the prediction with Cor. 2?
5. How should shared formation enter Eq. (6) so that mixed-lineage panels fail?
6. Which keystone problem is NP-hard?
7. How would you estimate β from same-family preference measured in percentage points? What β does a 3–8 pp lift imply?
8. The fivefold rise in the return to capacity after capture comes from ψ̂ = 0.1, which incidental conversion lacks. What is the empirical case for capacity adding feedback into development?
9. What empirical quantity does μ represent, given that timings scale with log(1/μ) and thresholds shift by O(√μ)?
10. Are the field conclusions robust to within-domain frequency dependence (network effects or congestion) and to saturating conversion?
11. In Prop. 2, why reset ζ to 0 at each horizon rather than carry stocks across horizons? With carried stocks L_i → 1, and the persistence weighting changes.

## 8. Concrete revisions, ranked by impact

**(a) Feasible before 5 October**

1. **Correct the W3 statements** using the replacement text given there (about an hour).
2. **Rewrite the aggregation paragraph and Prop. 3:**
   - the aggregate is (B⁰ + q̄B̂, c_i + γq̄);
   - list the assumptions: representative production, and q̄ uniform across domains and slowly changing;
   - add the sufficient condition c_i b̂_ij ≥ γb⁰_ij;
   - put the n = 1 counterexample in a footnote.
3. **Reconcile Eq. (3) and carrier.py.**
   - Cheapest route: keep the code, define the representative-carrier mechanism in §4, and add one sentence of robustness (under own-success production the threshold is 0.55–0.6 from a 50/50 start, and rare carriers cannot invade).
   - Better: add an own-success curve to Fig. 2. Each of these is about 10 lines of code.
4. **Fix figures.py:**
   - apply the cost in the counterfactual;
   - add the μ = 10⁻⁴ θ-sweep with at least 2,500 units per step;
   - simulate the persistence of the 13 configurations;
   - correct the keystone "inbound" printout.
5. **Related work and novelty wording (W4);** cite replicator dynamics.
6. **Wording and assumptions:** add the c_i > 0 standing assumption, fix the wording of Prop. 4(c) and Cor. 1(e), and fix the proof of Prop. 2(iii).
7. **Add one sentence on μ:** exact results are for μ = 0; thresholds shift by O(√μ), as in the ψ and θ examples; timings scale with log(1/μ).
8. **Trim** the constructs in §3, §6 and §9 that no result uses, and fix the Fig. 3d label.

**(b) Longer-term**

1. Run the Appendix C experiment and report it.
2. Build a model of firms that span domains, with own-success production and per-carrier versus per-decision costs. Derive the size threshold for investing in capacity and the fixed-size scope result, and test them on data on participation in standards bodies or benchmark authorship.
3. Model formation in the observation equation, and make β (and strategic masking) endogenous.
4. Add within-domain frequency dependence and saturating conversion, and characterize when partial capture is stable.
5. Calibrate one field: estimate R_ij with the distributed-lag strategy of §8, and β from LLM-judge panels.

## Verification scripts

All files are in `/private/tmp/claude-501/-Users-ren-theories/f263a065-8a67-4878-a3b3-e65dcc1d8b2a/scratchpad/review2/R2/`. Logs sit next to each script (`*.log`, `*.out`, `*_results.txt`).

- **`repro/`** — clean rerun of the authors' figures.py, field.py and carrier.py with no cache. The regenerated checks.log, hyst-cache.json, fig-*.tex and tab-robust.tex are all byte-identical to the authors'.
- **`ind_field.py`** — my independent field model: original coordinates, my own Dormand–Prince 5(4) integrator, and utilities for core, hull, configurations and Jacobians.
- **`ind_carrier.py`** — my independent carrier model with switchable variants: representative or own-success production; per-domain or cross-domain carriers; linear or quadratic cost; any set of capacity types.
- **`t1_configs_certs.py`** — Props. 1, 4 and 5(i); persistence of configurations under entry; keystone complexity; 0.88 vs 0.96.
- **`t2_capacity_base.py`** — Fig. 2.
- **`t3_capacity_robust.py`** — model variants, type sets, step size, μ and ν, ±10% parameter changes, χ scans.
- **`t4_detect_keystone.py`** — detection delays, the ψ threshold, hysteresis, the frozen-capacity threshold.
- **`t5_diagnostics.py`, `t5_beta.py`** — the θ = 0.975 tipping protocol; β = 0.6 over a long horizon.
- **`t6_capacity_theory.py`** — W(q), ℓ, the Price identity, scope at fixed size, Cor. 3 with cubic cost, the ratchet with and without cost, Appendix D.
- **`t7_misc.py`** — the remaining quoted field numbers.
- **`t8b_reform_logit.py`, `t8d_reform_slowcases.py`** — randomized test of Prop. 5(ii), including the slow cases.
- **`t9_core_logit.py`** — Prop. 4(c).
- **`t10_frozen_mu0.py`** — the 0.89 skeleton threshold.

Two scripts are superseded and should be ignored. In `t8_reform.py` and the core part of `t5_diagnostics.py`, shares underflow to exactly 1 in original coordinates and stick on the invariant face. The logit-coordinate versions above are the authoritative ones.
