# Review R2: mathematics and modelling

*AI review. Ren asked for peer reviewers on 2026-10-02. The reviewer was a Claude Opus 5.5 subagent, briefed as an applied mathematician working on dynamical systems, evolutionary games, monotone systems and threshold cascades. It read the anonymous submission (main.tex, the figure sources, references.bib, and PDF text via pypdf), not NOTES.md or the corpus. It re-ran figures.py from scratch and wrote an independent implementation in the session scratchpad. Its report is reproduced verbatim below.*

---

IASEAI'27 REVIEW: "Selecting the Selectors: Recursive Selection, Cross-Domain Capture, and the Answerability of AI Development"

**How I reviewed it.** I could not render the PDF pages because poppler is not installed. I read main.tex, the pgfplots figure sources and references.bib, and extracted the PDF text with pypdf to confirm the layout: main text runs to p. 9, within the limit. I checked every statement against Appendix A. I re-ran figures.py from scratch with no cache (about 6 minutes) in a scratch directory, and I wrote an independent implementation of the model for the robustness checks below. Nothing under /Users/ren/theories was modified, and NOTES.md was not read.

## 1. Summary

The paper models a "field" of n selection domains. Each domain i has:
- a share x_i of decisions following a practice P, which would lose under neutral rules (c_i > 0);
- a stock of rule support r_i, which offsets that cost.

Adoption in domain j generates rule support in domain i through a conversion matrix B (eqs. 1–2). Using normalized conversion R_ij = a_i b_ij/(c_i d_i), the paper shows the following:
- **Prop. 1.** A corner configuration E_S is linearly stable if S is internally sustaining (s_i(S) > 1 on S) and externally closed (s_i(S) < 1 off S). No mixed equilibrium is linearly asymptotically stable.
- **Prop. 2.** Capture spreads along a threshold closure cl(S).
- **Corollaries 1–3.** No local certificate exists, one-domain reforms are re-absorbed, and capture can persist beyond its origin.
- **Prop. 3 and Cor. 4.** A sustained reform at one domain prunes the captured set down to a core. This defines "keystones".
- **Prop. 4 and Remarks 2–3.** A shared condition V is depleted by development and observed through an evaluator whose capture masks the depletion (eqs. 4–5). A captured evaluator silences the alarm, so correction becomes a race. Remark 3 adds dependence-driven conversion.

A six-domain illustration (development, evaluation, standards, procurement, formation, information) shows:
- a cascade under hub coupling θ;
- protection of the selectors by firewalls;
- re-absorption of a one-domain reform;
- hysteresis in θ;
- a closure race.

The second half maps the parameters to general-purpose AI and proposes tests and design principles.

## 2. Scores

| Criterion | Score (1–10) |
|---|---|
| Relevance | 7 |
| Quality | 5 |
| Clarity | 7 |
| Originality | 4 |
| Significance / impact | 4 |

- **Overall recommendation (archival track):** weak reject. With the 3-day fixes below this could move to borderline or weak accept.
- **Confidence:** 4/5. I am confident on the mathematics and less so on the AI-governance literature.

## 3. Strengths

- **The question is important and well posed.** Risk located in a relation (success converting into control over future selection) rather than in a component is a real gap in AI-safety modelling. Section 3 and Table 1 separate concentration, capture, damage, collapse and closure. That is useful conceptual hygiene.
- **The model is minimal and tractable.** The corner-and-threshold structure is derived, not assumed. The proofs are short and mostly correct. The Statement of Contributions admits that the tools are standard.
- **Several takeaways are crisp and usable.**
  - A one-domain reform relapses while inbound conversion from captured domains exceeds one.
  - Hysteresis means reforms must overshoot.
  - Mutual support can make the origin dispensable.
  - Detection depends on the independence of the selectors.
- **The scoping is careful.** The paper calls its results possibility results, states its normative premises, says when the account loses force, and declines to accuse particular actors.
- **Reproducibility is exemplary.** The from-scratch run reproduced checks.log, fig-field.tex, fig-hysteresis.tex and hyst-cache.json byte for byte. My independent implementation reproduces every number quoted in Section 4.5:
  - capture times P 48, E/I 61, S 78, F 125;
  - inbound conversion 0.5 into the firewalled selectors;
  - silencing threshold x_E ≥ 0.857;
  - in the coupled field the alarm never fires and V drops below the 0.3 floor at t = 210;
  - with the selectors firewalled, the alarm fires at 74.7 and V bottoms out at 0.458;
  - with β = 0 the alarm fires at 74.6;
  - recapture of standards at t = 42, with inbound conversion 1.6 without the firewall and 0.6 with it;
  - hysteresis switches at θ = 1.05 and 0.25 (and never on the way down for φ = 0.2).
- **The tests are genuinely discriminating.** The proposed convertibility experiment holds the reward fixed and varies whether winners shape the next round's criteria. That is a good design.

## 4. Weaknesses

### 4.0 Correctness audit, statement by statement

| Item | Verdict |
|---|---|
| Lemma 1 | Correct. |
| n = 1 analysis | Correct. Φ is a valid gradient-like function (it needs b > 0, which R > 1 ensures). |
| Prop. 1(i) | Correct. It can be stated as an "iff": when s_i(S) = 1 the configuration is never asymptotically stable. It is unstable if R_ii > 0, and lies on a line of equilibria if R_ii = 0. |
| Prop. 1(ii) | Correct, because a Metzler matrix's spectral abscissa is at least its largest diagonal entry, which is 0 here. It can be strengthened (W7). |
| Prop. 1(iii) | Correct. |
| Prop. 2 | False as stated (W6). |
| Cor. 1 | Correct as mathematics. The inference "no test of domains one at a time can certify a field" is false (W2). |
| Cor. 2 | Correct. "Holds only if s_i(C) < 1" should read "only if s_i(C) ≤ 1". |
| Cor. 3 | Correct, but the wording is off (W10). |
| Prop. 3 | Correct. It should be extended to margin reforms (W8). |
| Cor. 4 | Correct after a one-line fix to the comparison state (W8). |
| Remark 1 | The "carriers" part is true by construction, because identities are not in the state space. The re-absorption part is Cor. 2. |
| Prop. 4 | Correct, but it follows directly from eq. (5) (W3). |
| Remark 2 | The conditions are necessary but use the wrong detection time (W3). |
| Remark 3 | Correct. The paper should add that the extended system stays cooperative in the order (x up, r up, V down), since ∂ṙ_i/∂V ≤ 0 and ∂V̇/∂x_D ≤ 0. So all the comparison arguments carry over. |
| Table 1, "Damage" row | Inaccurate (W10). |

### W1 [Major] The mathematics is not new, and the paper does not engage the literature where these results already live

Because the Jacobian at a corner is block-triangular, Prop. 1(i) reduces the stable equilibria of the ODE to the strict fixed points of a monotone Boolean threshold map, F(S) = {i : Σ_{j∈S} R_ij > 1}, with self-loops included. After that, everything is classical:
- **The closure cl(S)** is the final active set of a weighted linear-threshold (Granovetter) model, that is, bootstrap percolation with weighted thresholds. See Granovetter 1978, Kempe–Kleinberg–Tardos (KDD 2003) and Chalupa–Leath–Reich (1979).
- **The core** is a weighted k-core found by iterated pruning (Seidman 1983). The closure/core duality is the standard bootstrap-percolation/k-core duality.
- **Internally sustaining and externally closed sets** are weighted analogues of the cohesive sets in Morris (2000, REStud, "Contagion"). The set of stable configurations is the equilibrium lattice of a game of strategic complements (Milgrom–Roberts 1990; Vives 1990). Its least element is ∅ and its greatest is core(N).
- **"Unravelling" and "keystones"** are almost word for word the anchored k-core problem: Bhawalkar, Kleinberg, Lewi, Roughgarden and Sharma, "Preventing Unraveling in Social Networks" (ICALP 2012; SIAM J. Discrete Math. 2015). The keystone-set question is the collapsed k-core problem (Zhang et al., AAAI 2017), which is NP-hard.
- **Cascades into individually subcritical units through coupling** are the "tipping cascade" and "domino" results: Brummitt–Barnett–D'Souza (J. R. Soc. Interface 2015, "Coupled catastrophes"), Klose et al. (ERL 2021) and Wunderling et al. (ESD 2021).
- **Cor. 1** is the micro- versus macroprudential "fallacy of composition" in financial contagion: Gai–Kapadia 2010, Haldane–May 2011, Acemoglu–Ozdaglar–Tahbaz-Salehi (AER 2015).
- **The invasion and saturation structure of corners** is the invasion-graph formalism of community assembly (Hofbauer–Schreiber, J. Math. Biol. 2022).
- **The n = 1 model** is essentially niche construction with a linearly accumulating, decaying resource (Laland–Odling-Smee–Feldman, PNAS 1999). Multi-community eco-evolutionary games with environmental feedback are studied in Betz–Fu–Masuda (Bull. Math. Biol. 2024).
- **"Selecting the selectors" as a concept** is the central object of endogenous-institutions political economy: Barberà–Jackson (QJE 2004, self-stable constitutions), Acemoglu–Egorov–Sonin (AER 2012). See also behaviour–institution coevolution (Bowles–Choi–Hopfensitz, J. Theor. Biol. 2003).

Prop. 4 is algebra on eq. (5), and Remark 3 solves an affine equation. None of this makes the paper wrong. But the theorems cannot carry the contribution. The paper should claim the reduction (ODE to weighted threshold network) and the AI mapping, and cite the work above. "Complete characterization", "cascade theorem" and "unravelling theorem" overstate what is new.

One positioning opportunity: as I read Kulveit et al. (2025), mutual reinforcement across societal systems is central to the gradual-disempowerment argument. This paper could be pitched as the first formal model of that cross-system reinforcement.

### W2 [Major] The "no local certificate" claim is overstated, and as used in §7 it is incorrect

The claim appears in the Abstract, Contribution 2, Cor. 1 and §7 ("Audit fields, not sectors"). Cor. 1 only proves that certification from domain-internal quantities (R_ii, or isolated dynamics) is impossible. A test that each domain runs on its own full inbound row does certify the field. Three precise statements, all provable with the paper's own tools:

- **(a) A decentralized sufficient certificate.** If Σ_j R_ij < 1 for every i, every solution with x(0) in [0,1)^n converges to no capture.
  - Proof: Lemma 1 gives limsup r_i ≤ Σ_j b_ij/d_i. So eventually a_i r_i − c_i ≤ c_i(Σ_j R_ij − 1)/2 < 0, and logit x_i tends to −∞.
  - Each regulator needs only its own row, which is exactly the "one row" that §7 calls insufficient.
  - Check: 60 random fields with all row sums < 1, started at x_i = 1 − 10^−3 and r_i = 5, all converged to no capture (largest final share about 1e−131).
- **(b) An exact certificate.** No capture attracts every state with shares below one if and only if core(N) = ∅, up to ties s_k = 1.
  - The "if" direction is the pruning argument from the proof of Prop. 3, run with no reform.
  - Conversely, if core(N) is non-empty with strict inequalities, E_core(N) is the maximal stable capture configuration. External closure holds because each pruned k had s_k(C_m) < 1 for some C_m containing core(N).
  - Every stable E_S has S ⊆ core(N).
  - Example: R = [[0.5, 0.6, 0], [0, 0.5, 0], [0, 0, 0.2]] has a row sum of 1.1 but an empty core. So row sums are conservative.
- **(c) A robust firewall.** If row E sums to less than one, x_E → 0 from any state, whatever is captured elsewhere.
  - The minimum-cost robust firewall for a selector is a fractional knapsack over its inbound channels.
  - Margin levers (c_E, d_E, a_E) scale the whole row.
  - The paper's own firewalled illustration already satisfies this: row E = 0.2 + 0.3 + 4·0.1 = 0.9.

Joint assessment is needed for three things only: the exact (less conservative) certificate, the seed-specific question "is E in cl(seed)?", and keystone identification. It is not needed for certification as such. Corrected, the claim becomes a constructive and more useful result.

### W3 [Major] The closure result is built into the observation model, and its strong form needs very large masking

Eq. (5) moves the reported condition a fraction βx_E of the way toward perfect health. Prop. 4(ii) follows at once: if βx_E·K ≥ V_alarm, then y > V_alarm for every V > 0.

- **(a) Calibration.** Strict silencing needs β ≥ V_alarm/K, which is 0.6 in the example. A captured evaluator would have to report at least 60% health when true health is zero. That is not the "statistical" lineage effect motivated in §5; measured self-preference and correlated-error effects are modest. In the coupled field:

  | β | Alarm time (unmasked: 74.6) | Min V | Outcome |
  |---|---|---|---|
  | 0.1 | 87.7 | 0.43 | correction holds the 0.3 floor |
  | 0.2 | 106.4 | 0.39 | holds |
  | 0.3 | 135.4 | 0.34 | holds |
  | 0.4 | 186.9 | 0.27 | floor breached |
  | 0.5 | 305.7 | 0.17 | floor breached |
  | ≥ 0.55 | never (within t = 400) | — | silenced |

  With realistic masking, evaluator capture delays detection, and the delay grows with β. That is the defensible message, and it is still important.

- **(b) Remark 2 uses the wrong detection time.** t_A, the time when the true V reaches V_alarm, is not when the alarm fires. The alarm fires at t_det = inf{t : V(t) ≤ V_eff(x_E(t))}, which is at or after t_A and is pushed back continuously by partial capture. The stated conditions are necessary, but the race is not "t_A versus t_E". Example: with κ_E = 0.25, x_E crosses 0.857 only at t_E = 90.8, after t_A ≈ 74.6, yet the alarm never fires, because partial masking had already lowered V_eff. Remark 2 should be restated in terms of t_det and V_eff(x_E(t)).

I recommend a signal-detection formulation: the alarm probability depends on the signal-to-noise ratio, and evaluator error is correlated with lineage. That would tie β to measured LLM-judge effects and make "closure" quantitative.

### W4 [Major] The illustration's headline outcomes depend on design choices the paper does not discuss

- **(a) No feedback into development.** The illustration sets R_Dj = 0 for j ≠ D, so development is a pure source. That is why doubling c_D unwinds the field in Fig. 2d. With feedback ψ = R_Dj, the reformed row of D over the captured set is (1.3 + ψ·|C|)/2. Re-running the paper's scenarios:
  - Coupled field with β = 0:
    - The reform keeps V above the 0.3 floor only up to about ψ = 0.10 (min V 0.328).
    - At ψ = 0.13 the field eventually unwinds, but V falls to 0.115.
    - For ψ ≥ 0.14 the reform fails and the field stays captured (the analytic threshold is ψ = 0.14).
  - Firewalled field:
    - The floor holds at ψ = 0.15.
    - At ψ = 0.20 the floor is breached (min V 0.18).
    - At ψ = 0.24 the reform fails (analytic threshold about 0.233).

  "Development is a keystone" stays true: holding x_D = 0 still empties the core. But that is not what makes the liability lever work. The lever works only if it pushes D's own inbound sum below one, and Cor. 2 applies to keystones too. For AI, feedback from procurement revenue, standards references and evaluation legitimacy into development is plausibly strong, so this is exactly the case that matters. The correct rule is: a margin reform at keystone i unravels E_S if it makes x_i → 0 against the remaining captured set, that is, if the reformed s_i(S) < 1.

- **(b) Multistability before general-purpose coupling.** At θ = 0.6, where the paper says "capture stays in development", there are 13 strictly stable configurations:
  - no capture;
  - development alone;
  - all ten sets of development plus three other domains, including {D, E, S, F}, with both selectors captured;
  - full capture (row sums 1.3).

  So general-purpose coupling changes whether selector capture is reachable from a development seed, not whether it can exist. That changes the AI narrative: shocks or coordinated pushes could capture the selectors with no increase in coupling.

- **(c) Exact ties.** 0.6 + 4·0.1 = 1 and 0.3 + 0.3 + 4·0.1 = 1 create 15 configurations at θ = 0.6 that sit exactly on a stability boundary. The point plotted at θ = 0.30 in Fig. 3a is one of these: the row sum evaluates to 0.9999999999999999 in the script. In exact arithmetic E_N is not asymptotically stable there, because ξ̇_i ≈ κ_i c_i ξ_i Σ_j R_ij ξ_j (with ξ_i = 1 − x_i). Perturbing φ (for example to 0.11) avoids this.

- **(d) "What decides correction is the independence of the selectors, not the coupling as such" is true by construction.** With β = 0, y equals V, so the alarm fires at the same time in every field.

What does hold up: the silenced alarm in Fig. 2c is not a knife-edge result. The alarm stays silenced for h from 0.008 to 0.012 (it flips at h = 0.014), for κ_E from 0.25 to 0.5, and for β down to 0.55. Partial masking is what makes it robust.

### W5 [Major] The modelling assumptions limit what the model can say, and several AI and design claims go beyond it

- **Only corners are stable.** The relative payoff a_i r_i − c_i does not depend on x_i, so ∂ẋ_i/∂x_i = 0 at interior equilibria. That is what drives Prop. 1(ii). With heterogeneous thresholds within a domain (Granovetter-style), stable "partial capture" equilibria appear, and the field becomes a continuous monotone map rather than a Boolean one. The "complete characterization" is specific to the model. It also covers hyperbolic equilibria only; Hirsch's generic-convergence results (1985, 1988, for irreducible B) should be cited, or the claim qualified.
- **No emergence.** With c_i > 0 everywhere, no capture is always stable, which is a strong Allee effect. Capture needs an exogenous seed (x_D = 0.9, r_D = 1.5), so the model explains spread and persistence, not origin. Allowing c_D ≤ 0 at the origin (a first-mover advantage that converts into rule support elsewhere) would fix this and match the AI story better.
- **Speed decides basins, not thresholds.** For n = 1 and R = 1.5, the critical initial share on the separatrix is:

  | κ/ε | inherited r(0) = 0 | r(0) = 2 |
  |---|---|---|
  | 1 | 0.82 | 0.48 |
  | 10 | 0.998 | 0.025 |
  | 0.1 | 0.69 | 0.65 |

  Fast adoption makes inherited rules decisive. That cuts both ways: it also makes reforms that reset the rule stock more effective. "The risk lies in the mismatch", and listing speed among the "parameters that decide these outcomes" in the abstract, overreach. Speed decides timing, basins and the race.
- **Formation.**
  - §5 says Cor. 2 explains why reforms elsewhere are re-absorbed while formation stays captured.
  - §7 calls evaluation and formation "keystones of epistemic closure (Prop. 4)".
  - But formation does not appear in Prop. 4. It is not a keystone in the illustration; only D is.
  - Its slowness enters no threshold, and re-absorption caused by F would need a large R_iF (it is 0.1 in the illustration).
  - Either model formation's epistemic role (for example, β or E's inbound row depending on x_F) or drop the claim.
- **Growing conversion is not modelled.** "Conversion among the captured domains can grow until they sustain one another" (§7) is not a model dynamic, since B is constant; Fig. 3b compares two values of φ.
- **Keystone status can shift rather than disappear.**
  - When the origin stops being a keystone, other domains can become keystones. At θ = 0, φ = 0.2, every non-development domain is a keystone of full capture: removing any one prunes the other four. So a sustained reform of evaluation alone would unwind the field. That supports "firewall the selectors" better than the current text does.
  - At θ = 1.2, φ = 0.2 there is no single keystone, but every pair {D, k} is a keystone set. The keystone notion should be generalized to sets.
- **Two abstract claims need qualifiers.**
  - "Only reforms at keystone domains unravel a configuration" holds for single-domain reforms begun near E_S.
  - "A reform confined to one domain is re-absorbed while the domains that feed it remain captured" leaves out that a margin reform within that domain (raising c_i or d_i, lowering a_i) holds once it brings s_i(C) below one, as Cor. 2 itself says.
- **Persistence across carriers is assumed, not derived.** It is built into the state space. Only the re-absorption part of Remark 1 is a result.
- **AI enters only as hypothesized parameter shifts.** There is no path to estimating R_ij, which is dimensionless and involves a latent r_i. Question 3 below gives one route.

### W6 [Major on correctness; one-line fix] Proposition 2 is false as stated, because the faces x_j = 0 are invariant

**Counterexample.**
- Setup: n = 3 and all of a, c, d, κ, ε equal to 1. R_11 = 1.5, R_21 = 1.5, R_31 = 0.5, R_32 = 0.8, and every other entry 0.
- Closure: cl({1}) = {1, 2, 3}, because s_2({1}) = 1.5 and s_3({1, 2}) = 1.3.
- Trajectory: start at x = (0.9, 0, 0.5), r = (1.5, 0, 0). Then x_1 → 1, x_2 stays at 0, r_3 → 0.5, and x_3 → 0.
- So domain 3 is in cl(S) and starts with x_3(0) > 0, yet it is not captured.
- I verified this numerically. With x_2(0) = 10^−6 instead of 0, the cascade does reach domain 3.

**What breaks and how to fix it.** The induction step uses x_j → 1 for domains j in S_k \ S that started at exactly zero. The correct statement computes the closure within the support: S_{k+1} = S_k ∪ {i : x_i(0) > 0 and s_i(S_k) > 1}. Alternatively, assume x_j(0) > 0 on cl(S) \ S. Prop. 4's "E ∈ cl(S)" needs the same caveat. Cor. 2 is fine, since it uses a single step. The numerics avoid the problem only because of the 10^−4 floor, which is not part of the model (W9).

### W7 [Minor] Prop. 1(ii) can be sharpened

Write the (x_I, r_I) block as M = [[0, K], [G, −D]], with K and D positive diagonal and G = diag(ε)·B_II ≥ 0. Then λ > 0 is an eigenvalue of M exactly when ρ([λ(λI + D)]^−1 GK) = 1. That equation has a solution whenever B_II is not nilpotent, that is, whenever the conversion digraph on I has a cycle.

So every mixed equilibrium is linearly unstable with a real positive eigenvalue, except in non-generic cases where it lies on a continuum. In a random check, all 30,853 mixed equilibria in random fields with n from 2 to 5 had a real positive eigenvalue.

### W8 [Minor] The proofs of Prop. 3 and Cor. 4

- **The comparison state in Cor. 4.** The proof uses "the same shares, with r lowered to its values at E_{S\{i}}". That state is not below the reformed state if b_ki = 0 for some k. In that case r_k at E_S equals r_k at E_{S\{i}}, and a nearby state can have r_k below it. Use min{r_k, r_k at E_{S\{i}}} instead. That state is within ‖r − r^S‖ of E_{S\{i}}, so it lies in the basin for states near E_S. The upper comparison is not needed for k in S \ {i}.
- **Margin reforms.** The numerics apply a margin reform (c_D from 1 to 2), not "hold x_i = 0". The comparison argument extends: the reformed vector field is no larger than the original (Kamke), and the pruning step only needs x_i → 0. Prop. 3 should be stated for reforms that drive x_i → 0, together with the condition in W4(a).

### W9 [Minor] Invariant faces and the entry floor

The theorems are proved for the unclamped ODE, whose faces are invariant. The numerics clamp shares to [10^−4, 1 − 10^−12].
- **Effect on the quoted capture times.** None for floors from 10^−4 down to 10^−12, almost none at 10^−3 (E 60, F 124), and clearly shifted at 10^−2 (E 49, F 99).
- **What the floor does silently.** It supplies the positivity that Prop. 2 needs.
- **Fix.** Add an explicit entry term such as μ_i(x̄_i − x_i). That keeps the system cooperative, removes the invariant faces, and shifts the hyperbolic E_S by O(μ). Alternatively, state the positivity assumptions in the theorems.

The upper clamp at 1 − 10^−12 is good practice. Without it, shares round to exactly 1.0 and stick to the invariant face; I ran into this in my own checks.

### W10 [Minor] Smaller issues

- **Table 1.**
  - The row "h < ρ: lock-in without depletion" is wrong. Under capture V → K(1 − h/ρ) < K, which is partial depletion. The real distinction is V → 0 (when h > ρ) versus V → K(1 − h/ρ) > 0 (when h < ρ).
  - The caption says "Five distinctions" for six rows.
- **The s_i(S) convention.** s_i(S) includes R_ii when i is in S but not when i is outside S. This difference is what separates internal sustainability from invasion, so it should be stated.
- **Cor. 3.** "Stable irrespective of the state of domains outside C" is misleading, since E_C fixes those states at 0. It should say irrespective of their outbound conversion.
- **The "Agents" anecdote.** It is unverifiable and does not "show" capture. Drop it or document it.
- **Script label.** checks.log labels the selectors result "Prop. 3"; in the paper it is Prop. 4.
- **Space.** Some prose in §3 could be trimmed (the cancer analogy, "Power's two roles") to make room for the certificate theorem and the robustness table.

## 5. Could this paper, in its current version, be an important paper that advances alignment?

Not yet.

From a dynamical-systems perspective:
- The formal results are known structures (threshold-network fixed points, bootstrap closure, k-core pruning) applied to a new setting.
- The closure result is a property of the assumed observation equation.
- The AI-specific content is a set of hypotheses about parameter sizes, with no measurement.

The paper provides a good formal vocabulary: inbound conversion, re-absorption, keystones. It could become important for AI governance if it delivered at least one of these:
1. **An operational result.** The exact and decentralized certificates and the robust-firewall theorem (W2), plus an identification result for R from observable data (Question 3).
2. **Evidence.** A convertibility experiment (even a small pilot with LLM agents), or an estimate of inbound conversion into evaluation for one real evaluator ecosystem.
3. **A non-obvious dynamic result.** For example, stochastic escape times and stochastically stable configurations as functions of coupling, or a quantitative detection-delay law in β and lineage overlap.

It does not advance alignment in the narrow sense of making systems pursue intended goals. Its contribution is to structural risk and governance. The "obedience is not field alignment" point is already in Critch and Krueger (2020) and the multi-principal literature.

## 6. Questions for the authors

1. Does "domain-level audit" mean an audit of domain-internal incentives (R_ii) only? Will you adopt the row-sum and core certificates and revise §7 accordingly?
2. Why is R_Dj = 0? How do Fig. 2d and the keystone message change with feedback into development (W4a)?
3. How would R_ij be estimated, given that r_i is latent? Integrating eq. (2) gives
   d/dt logit x_i = κ_i c_i [ Σ_j R_ij (k_i ∗ x_j)(t) − 1 ] + (a decaying transient),
   where k_i(s) = ε_i d_i e^(−ε_i d_i s).
   - So R_ij is identified from share data alone, as minus the ratio of the distributed-lag coefficient to the intercept in a logit-velocity regression.
   - This needs variation that is not collinear across j.
   - It would also give a direct statistical test of s_i(C) > 1.
4. What β do you consider realistic for the AI-judge lineage channel? At that value, does "closure" survive, or does it become a detection delay?
5. What mechanism links formation to closure in the model?
6. How does the initial capture of development arise, given that no capture is always stable?
7. Were the exact ties (0.6 + 4·0.1 = 1, and so on) intentional?
8. Can you say anything about non-equilibrium attractors when B is reducible? In the illustration, development is a pure source.
9. Is the agents case documented anywhere?

## 7. Concrete revisions, ranked by impact

### Feasible within 3 days (deadline 5 October)

1. **Fix the certificate claim.** Replace the interpretation of Cor. 1 with three statements: certification from internal incentives is impossible, a row-level test is sufficient, and the joint core test is exact. Add the robust-firewall corollary. Revise the Abstract, Contribution 2 and §7.
2. **Reposition the mathematics (W1).** Add the citations listed there. Recast the Statement of Contributions as "a reduction to a weighted threshold network, plus the AI mapping".
3. **Make the correctness fixes.**
   - Prop. 2 with the closure computed within the support.
   - The min fix in the Cor. 4 comparison state.
   - Prop. 3 for margin reforms, with the condition under which a keystone itself is re-absorbed.
   - Prop. 1(i) as an "iff" and the strengthened Prop. 1(ii).
   - Remark 2 restated with t_det.
   - The Table 1 Damage row.
   - Note that Remark 3 preserves monotonicity.
4. **Add a one-page robustness appendix.** Pure Python; a few hours with the existing script. Cover:
   - feedback into development (ψ);
   - masking strength β, harm rate h, selection speed κ_E, and the entry floor;
   - parameters that avoid exact ties;
   - the multistability at θ = 0.6;
   - the keystones at θ = 0, φ = 0.2.
5. **Calibrate or qualify the masking.** Report detection delay as a function of β, and state that strict silencing needs β ≥ V_alarm/K.
6. **Tone down the overclaims:**
   - "complete characterization";
   - "only keystone reforms unravel";
   - formation as a keystone of closure;
   - growing conversion;
   - speed as outcome-deciding;
   - "independence decides correction".
7. **Clean up.** Make positivity explicit (an entry term, or hypotheses in the theorems), drop or document the agents anecdote, and fix the script label.

### Longer-term

1. **Estimation.** Identify and estimate R from panel data (funding, personnel flows, lineage overlap, share time series), with a recovery study. Produce at least one empirical estimate of inbound conversion into evaluation.
2. **Experiment.** Run the convertibility experiment with LLM agents: fixed reward, varying whether winners shape the next round's criteria. Pre-register the prediction that persistence and hysteresis appear only when conversion is enabled.
3. **Stochastic version.** Add finite-population noise in each domain. Study metastability, escape rates (Freidlin–Wentzell) and stochastic stability (Young 1993) of configurations as functions of coupling. This would also validate the early-warning claims, which need noise.
4. **Firewall and keystone design as optimization.** Find the minimum-cost intervention that keeps E out of cl(seed) or out of core(N). Show NP-hardness via the anchored and collapsed k-core problems. Give exact integer programs for realistic n (6 to 20 domains, so exact search is feasible). Contrast this with the robust row-level knapsack.
5. **Closed-form race.** In the fast-adoption limit (κ → ∞), the model becomes a piecewise-linear system in the style of Glass networks, which gives explicit capture and detection times.
6. **Richer models.** Partial capture via heterogeneous thresholds. Several competing practices, to ask whether pluralism acts as a check. Endogenous conversion, to formalize the "window closes" claim. Strategic masking and strategic investment in conversion.

---

**Verification scripts.** Everything is outside the repo, in the session scratchpad:
- **Re-run of figures.py:** `run_nocache.Oal0/`.
- **Independent checks:** `review/`.
  - `model.py` is the independent implementation.
  - `checkA.py` is the Prop. 2 counterexample.
  - `checkB.py` checks spectra at mixed equilibria.
  - `checkC4.py` tests the row-sum certificate.
  - `checkConfigs.py` enumerates configurations, keystones and ties.
  - `checkD.py` and `checkPsi2.py` cover robustness to feedback (ψ), harm rate, κ_E and the floor.
  - `checkBeta.py` covers masking strength.
  - `checkE2.py` computes the separatrix.
