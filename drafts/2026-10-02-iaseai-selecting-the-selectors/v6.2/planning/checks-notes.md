# checks_v62.py: notes for the text

4 October 2026. This file maps every block of `v6.2/checks_v62.py` to its keys, its kind, what it asserts and the numbers it prints, so a drafter can cite `[num: XX(part)]`. The log is `v6.2/checks_v62.log` (default sizes). The last section lists findings and discrepancies between the memos.

**Run.** `python3 checks_v62.py > checks_v62.log` from `v6.2/`. Pure standard library. The default run passes all 188 assertions in 297 s (169 before the completion pass of 4 October, below) (timing per block is at the end of the log). Every assertion prints `[ok]` or `[FAIL]`, and the run ends with a count and the index of Codex's boundary cases. `python3 checks_v62.py XX YY` runs only the named blocks. `--legacy` re-runs v5 and earlier suites, as before.

**`--full`** adds only heavy grids in MP and QS:
- MP: multiplicity at N=6000, a finer-round smooth branch (d=0.025), the full s2_mpe/s2b tables, s2d, s2c_profile and s2e_check;
- SP(J): the full prop39 grid;
- QS(i): the replicator-with-mutation dynamics of s4_cost(c).

Every other script runs at its source's own size by default. That includes the 20,000-game sweep in ES, the 3,000 three-stock systems in CH, the 1,500 systems of s1, and the 400+600 settings of m04.

**Kinds.**
- *independent*: decided by direct computation (simulation, value iteration, best response, numerical Jacobian), not by the inequality under test.
- *identity*: the computed side is the stated formula rearranged. It catches slips; it is not independent evidence. A *valuation check* is an identity that values a fixed play path (EC).
- *derived*: evaluates formulas that other blocks check.

A block whose parts differ in kind says so in its header and marks the parts.

**Relabels (plan §7), done.**
- EC is now `identity: valuation check`. Its comment says why, and gives the core wording: "a valuation check confirms the algebra of (1)", not "200,000 random settings". ES(f) proves the point with exact rationals (0 disagreements in 20,000), and ES(d) is the incentive check.
- LG(C),(C′) are now identities. The comment gives the core wording "an algebraic check", not "to six digits".
- RH is now an identity, except its last line (grid best response), which stays independent.
- NB's derived thresholds are 0.9495 and 0.9793, with an assertion.

The v6.1 blocks keep their printed output byte for byte. Their extensions run after them under the same block code, with a sub-header `--- XX (v6.2 extension) [...]`. The v6.1 function bodies are untouched, apart from the three relabels and the NB and EC additions, which were made in the earlier, interrupted pass.

---

## Block by block

Part letters refer to the printed `(a)`, `(b)`, … in the log. For the v6.1 blocks with extensions, the extension parts continue the v6.1 lettering or numbering.

### v6.1 blocks (unchanged output, relabels as above)

FB, LG, TC, TH, CB, FA, AC, RH, FS, EC, BI, WG, T3, PE, FD, NB: as in v6.1. The only additions are EC's five-seed Monte Carlo check (`s6_ec_mc.py`) and NB's 0.9495/0.9793 assertion.

### CH: channel signs (`loopgain`, `chansign` S2, `delayosc` S2, `gammarange` S2). Independent; (h) derived.
Sources: m03 (A,B,D); f3 (B); Codex case 2; Sys s1 (a,a′,d); Math-Fable reviewer m1 (A,A′,B); Math-Opus reviewer s1_loopgain; Adv-O adv_checks §1.

- **(a) The ξ_r rule.** Every simulated sign agrees with the rule in 10/10 settings. Correction changes Γ with the sign of δ_f/(d+δ_f) − ξ_r; provision lowers Γ iff ξ_r < 1. Values:
  - log channel: Γ unchanged at 1.2857 when d goes 0.2→0.3 without diffusion; 0.8571→0.9643 with δ_f=0.1;
  - linear channel: 1.125→0.750;
  - k0 0.1→0.2: log 1.2857→1.0000; linear unchanged at 1.125; X² 1.75→2.25 (rises).
  - Γ_δ of a ratio channel at δ=0.9: 0.8526, 1.1571, 1.4087 for d = 0.1, 0.2, 0.4. It rises although Γ is unchanged.
- **(b) f3(B), numerical spectral radius.** Ratio form (r=2, δ_f=0.1): Γ = 0.71, 0.95, 1.07, 1.22 for d = 0.1, 0.2, 0.3, 0.6, with radius 0.943, 0.986, 1.029, 1.157. Level form (a=1.2): Γ = 3.0, 2.0, 1.5, 0.86, with radius 1.40, 1.30, 1.20, 0.90.
- **(c) Codex 2.** Raising d from 0.1 to 0.2 (r=1.8, δ_f=0.1) moves (Γ, Γ_δ) from (0.90, 0.579) to (1.20, 0.876).
- **(d) Sys s1.** Spectral radius > 1 iff Γ > 1 in 12/12.
- **(e) `delayosc`.** Net DC gain 0.25 < 1; modulus 1.0075; period 51.6; |y(600)| = 292.
- **(f) Three stocks** (log, linear, √). Perron root > 1 iff Γ > 1 in 2996/2996. The nonlinear gap grows iff Γ > 1 in 5/5; the case Γ = 1.201 is channels each too weak to open the loop opening it together. Price of standing = Γ_δ/(1−Γ_δ) in 189 systems, max relative error 7.1e-7.
- **(g) s1.** 1,500 random 1–3-channel systems, 0 mismatches. Price matches in 196 systems (max relative error 1.6e-6). Γ_δ ≤ Γ in 2,000 systems × 4 discount factors. Finite perturbations at Γ=1.5 > 1 > Γ_δ: per-unit PV falls with size (e.g. δ=0.85: 3.923 at 1e-6, 3.234 at 0.2).
- **(h) `gammarange` [derived].** r* = 1 + δ_f/d. At δ_f = 0.05 a month: 6.00, 3.50, 2.67, 2.00, 1.50 for d = 0.01–0.10. At δ_f = 0.10: 11, 6, 4.33, 3, 2.

### TD: time to decisiveness (`tdec` S2, `loopgain`). Independent; (c),(d) derived.
Sources: f3 (C); m03 (C); Sys s1 (b,c); Math-Fable reviewer m6 (3).

- **(a)** The exact multiplier is 1+(d+δ_f)(Γ−1): 1.4000, 1.1000, 1.0500, 0.7400. V6.1's factor is wrong where δ_f > 0 (1.0667, 1.0250, 0.8960).
- **(b) Simulated factors** 1.40000, 1.05000, 1.10000, 1.03000.
  - Nonlinear 1%→50%: 13 periods at Γ=3, d=0.2 (linear estimate 11.6); 50 and 144 periods in two other cases.
  - With diffusion (Γ=1.5, d=δ_f=0.05, r=3) the gap never reaches 50%: it settles short of decisive.
  - Same Γ=1.2: turnover 0.5 needs 41 periods, turnover 0.02 needs 980.
  - Two channels at Γ=1.2: the factor is the Perron root, 1.00877 for turnovers (0.3, 0.02) against 1.02000 for (0.1, 0.1).
- **(c) Secular roots** 1.1000, 1.0040, 1.0092: 41, 980 and 427 periods.

### CE: a point of enough (`compound`). Independent.
Sources: f3 (A); m04 (A,B,C); Codex 3a, 3b; Math-Opus reviewer s9_cap_edge; Math-Fable reviewer m1 (C).

- **(a) f3(A).** The local condition at K̄ = K* predicts the outcome in 10/10. Strict caps at 0.98 and 0.9 of K* hold. Diffusion alone restores the laggard. With none of the three flows the laggard is excluded (9.9e-324). With δ_f = 0.05 alone it **stalls at K = 0.36 = 0.16 K̄** (see findings).
- **(b) m04(A).** Codex's cap-equality case: the laggard falls to 2.4e-32. A cap at 0.98 K* restores it. A strict cap (0.97 K*) holds in 400/400 random settings, and the equality criterion predicts 400/400.
- **(c) m04(B).** The criterion φ > 0 agrees with simulation in 444/446. Both disagreements are laggards starting above an exclusion threshold that lies below 1% of the cap.
- **(d) m04(C).** n=5, r=1.5, cap 0.8. With none of sharing, provision or diffusion, laggards at 0.05 and 0.2 are excluded. With β=0.1, k0=0.05 or δ_f=0.15 alone, all return.
- **(e,f) Codex 3a/3b.** Both hold; the smallest inflow on Codex's grid is 7.5e-5.
- **(g) s9.** At a cap equal to K* without diffusion, the laggard returns iff Γ < n/(n−1) (4/4).
- **(h) m1(C).** φ′(K*) = +0.0100, so the laggard is excluded; caps at 0.98 and 0.90 hold.

### PD: price domain (`loopgain`, `standprice`). Independent. (Earlier pass; unchanged.)
- **Codex 1.** Γ_δ = 9/7. The printed multiplier is −4.5, while the true discounted advantage is +0.0107.
- **Cusp.** The exponent of PV/ε tends to α−1 = −0.4221 (last −0.4225); the fitted PV exponent is 0.5778 against 0.5779.
- **Γ > 1 > Γ_δ.** PV/ε → 8 from below; the gap shrinks by 0.357 per two decades.
- **δΛ* = 1.** PV/ε grows by 8.42 per two decades: logarithmic.

### SP: compounding prices standing, general form (`standprice`, `twoerrors`, `growprize` S3, `twochan`). Mixed: (A),(E),(I),(J) identity; (B),(C),(F),(G) independent. (Earlier pass; unchanged.)
- **(A)** 14 cases; max |θ_eff − (9) general| = 7.6e-8; the sign rule holds 14/14, with ties at (1−β)r = 1.
- **(B)** PV_rel/PV_com = 2.53846, 0.68750, 0.62264, 1.00000, 2.08108, 0.92958. Each exceeds 1 iff (1−β)r > 1.
- **(C)** Both closed-loop prices match the nonlinear simulation (max relative error 2.5e-5). Outside the domain (Grel_d = 1.066) the simulation gives +226 where the formula gives −16.2.
- **(D)** Net payoff reinvested is load-bearing: θ_eff = −0.1649 net against −0.3125 with gross winnings only.
- **(E)** The fixed-prize form misses e* by up to 15% when the prize grows.
- **(F)**
  - Without diffusion, narrowing coincides with instability in 24/24 cases.
  - With δ_f = 0.03 the thresholds separate: narrowing at r = 1.1421 = 1 + δδ_f/(1−δ(1−d)), instability at r = 1.2000 = 1 + δ_f/(κg).
  - Stationary fixed-prize case: Γ = 0.938 < 1, yet the objective narrows.
- **(G)** Test Γ's observable equals 1+θ (max error 4e-4).
- **(H)** Codex 9: 1+θ_Γ rises with provision, from 0.5846 to 0.8058.
- **(I)** `twoerrors`: Γ_δ* = nκ/((n−1)(1+κ)); n=4, κ=0.4 gives 0.381.
- **(J)** prop39.
- **Draft citations.** "[num: GP; m02 C]" in a unit draft means SP(C)/(F). GP was Opus's proposed name; the plan uses SP.

### MP: Markov-perfect contest (`loopgain`, `standprice`, `eqgain` S2). Independent. (Earlier pass; s2c and s2e added under --full.)
- **(a)** Static Tullock: r_pr/r = 2(n−1)/n exactly (1.000 to 1.800).
- **(b)** Two-period game: λ_full/λ_red = 2(n−1)/n.
- **(c) m01 table.**
  - MPE price against the envelope formula with measured r_pr: Γ = 0.2: 0.1164/0.1166; 0.3: 0.1941/0.1950; 0.4: 0.3099/0.3170.
  - At Γ = 0.45, Γ_eq = 1.11; at 0.6, Γ_eq = 2.83 and MPE/struct = 2.66.
  - r_eq > r_pr > r at every computed point.
  - Off parity (r=1): the laggard's price at s=0.25 is 57% of structural at Γ=0.3 and 25% at 0.6; the leader's at s=0.75 is 153%.
- **(d) Catch-up.** With L_sub = 100, r_eq/r = 0.993 < 1.
- **(e) Multiplicity** [finding held for outside review]. At Γ=0.2, d=0.05, N=3000 there are two converged fixed points: price 0.1169 (smooth) and 1.3919 (×12.5 structural). At Γ=0.3: 0.1969 and 1.5509 (×8.8). At d=0.1 only the smooth one appears.
- **(f) f2(1).** The MPE price equals the closed-loop gain of the partial-equilibrium loop to 0.5%. The expected-deviation multiplier is 1+d(Γ_eq−1).
- **(g) f2(2).**
  - Amplification ×1.12 to ×4.75.
  - Γ_eq = 1.96 at structural Γ = 0.6.
  - E|s−½| after 60 periods: 0.198 against 0.120 under the structural lottery.
  - The laggard's price at s=0.25 is 0.065; with shared loss it is negative (−0.039).
- **(h) s2.** With others fixed, the price equals Γ_δ/(1−Γ_δ). Under patience (δ=0.97) the amplification is ×7.87.
- **(i) Tug-of-war.** Effort is highest at parity.

### QS: capacity dynamics and `humancorr` (`corrrate`, `humancorr`, `capdyn` S4). Independent.
Sources: f5 (A); m06 (D,E); Sys s4_joint (E1, E1′, E1″), s5_joint2 (E2, E4a, E4b); Math-Fable reviewer m5_quasistatic; Math-Opus reviewer s4_cost (c).

- **(a) f5(A)**, threshold 0.1.
  - First failure at α_cor = 0.05: QS 28.8; R(0.3) 32.9; R(0.1) 38.1; R(0.03) 46.9; GA never; GM 28.9. At 0.09: 145.9 to 222.9. At 0.11: never.
  - Lag delay against the formula: 4.11/4.05, 9.29/9.16, 18.11/17.92, 8.40/8.41, 19.70/19.71, 40.23/40.24.
  - GA bound: q(600) = 7.29 ≤ 9.18 and 2.18 ≤ 3.78.
- **(b) m06(D)**, joint with one evaluation domain. Failure / capture:

  | α_cor | QS | Lag 0.1 | Lag 0.03 | Additive V=1 | Multiplicative V=1 |
  |---|---|---|---|---|---|
  | 0.05 | 13.0 / 25.4 | 22.5 / 36.9 | 31.3 / 47.5 | never | 23.8 / 58.9 |
  | 0.09 | 69.3 / 118.8 | 106.4 / 169.9 | 146.3 / 221.7 | never | never |
  | ≥ 0.1 | never | never | never | never | never |

  - Capture follows failure by 12–75 periods.
  - Lag delays 9.42/9.16, 18.23/17.92, 6.33/6.44 (within 2.8%).
  - Additive selection at α_cor = 0.01 fails transiently at t = 10.6, then certifies.
  - **`humancorr`:** the certificate holds eventually iff α_cor ≥ 0.1 + wδ_h, exactly (thresholds 0.10, 0.15, 0.20; 15/15).
- **(c) m06(E), reversal.** The minimal hold is 38.05 quasi-static, 44.34 with lag 0.1 (+17%) and 58.67 with lag 0.03 (+54%).
- **(d) s4_joint.**
  - E1: nothing fails at α_cor ≥ 0.1.
  - E1′: the largest α_cor captured within H is, under QS, 0.0852, 0.0926, 0.0963 for H = 150, 300, 600. Additive selection gives 0.0090.
  - E1″: the lag ratio q/q* tends to k/(k+g): 0.87, 0.40, 0.17. Under additive selection it tends to 0.
- **(e) s5 E2.** The hold after a withdrawn reform is 6–14% longer with the slowest lag (+13%, +14%, +6% for d2 = 0.7, 1.0, 2.0). Fast lags change it by under 1%.
- **(f) s5 E4a [`humancorr`, finite horizon].** Coupled thresholds 0.1449, 0.1902, 0.2313 against 0.0963 uncoupled. The shifts are +0.049, +0.094, +0.135 for δ_h = 0.05, 0.1, 0.2 (see findings).
- **(g) s5 E4b [`humancorr`, hysteresis].** d needed to undo capture: 0.634, 1.006, 1.675 for k_D = 0, 0.3, 0.6. That is ×1.59 and ×2.64 the quasi-static reform: the "1.6–2.6 times" of D2-fable §27(4).
- **(h) m5.** Fast selection reproduces the rate law; slow selection delays failure past T = 250.
- **(i) s4_cost(c).** Above the threshold nothing fails. Below it, no dynamics fails earlier than QS.
- **Completion pass (U04 merge note §4), three assertions inside the parts above:**
  - in (b), **S4.2(2)(b):** selection variance proportional to q (m06 "multiplicative") at α_cor = 0.05 fails at 23.8, is captured at 58.9, and ends at row sum 8.64e-8: capacity bounded, certificate held again (the "9×10⁻⁸" of S4);
  - in (d), **S4.2(2)(c):** variance proportional to q² at speed 0.1 (s4 GM(0.1)) is captured only below α_cor = 0.0627 at H = 150, 300 and 600 alike: bounded below the rate law (the "0.063 at every horizon" of S4);
  - in (d), **capture lag:** T_cap − T_cert across all 23 E1 runs with both dates is 8.3 to 84.6 periods (8.3 to 60.3 at α_cor = 0; 13.8–19.3 at 0.05; 38.2–46.8 at 0.08; 75.7–84.6 at 0.09). This is the "8 to 85" of S4 and of the `slowroute` Scope, and the "8 to 60" with correction not growing.
  - The block comment now reads "necessary if liminf q/q* > 0" (only "if" holds; U04 merge note §2 item 1).

### FF: falling floor and lump sum (`corrrate`, `costq`). Independent.
Sources: f5 (B,C); m06 (A,B,C); Codex 4; Math-Opus reviewer s7_Hf, s4_cost (b).

- **(a) Codex 4.** Cultivation stops at t = 0.5051; the certificate never fails although α_cor = 0.05 < 0.1.
- **(b) f5(B).**
  - α_cor > α_f alone is not sufficient: f0 = 0.1, α_cor = 0.051 fails at t = 38.4, while cultivation only ends at 588.
  - At α_cor = α_f: cultivation at the start means failure (f0 = 0.1 fails at 37.1; f0 = 0.17 at 58.0); none at the start (f0 = 0.3) holds.
  - α_cor ≥ 0.06 never fails.
  - d_f rises: 1.200, 1.978, 3.262.
- **(c) m06(B).** The three-case rule predicts the eventual certificate in 32/32. Equal rates fail at 15.4 with cultivation at the start and hold without it.
- **(d) s7_Hf.** Failures at 37.1 and 58.0; holds above α_f.
- **(e) f5(C), s4_cost(b).**
  - Lump-sum threshold exponents 0.25, 0.5, 0.3333, 0.25; per-unit 1/(2−ξ_f).
  - d* under the per-unit floor levels off at p²/f = 1.200.
  - Under a lump sum, d* = 0.465, 4.648, 46.48, 464.8, 4648 as γ falls from 1 to 1e-8.
- **(f) m06(C).** Exponents 0.2500, 0.3333, 0.4000, 0.2273. d* is 10, 100, 1000, 10000 under a lump sum, against 3.03 rising to 3.33 under a per-unit floor.

### SR: the silent route's two clocks (`slowroute`, `masking`). Independent.
Sources: f7 (F); Sys s5_joint2 (E3), s5b_clocks; plus an independent integration of T_A.

- **(a) f7(F).** Capture complete by t = 3.6 gives a silent crossing at t = 21.0. With capture midpoints 20 or 45, the alarm fires at t = 7.4, before the floor: (b),(c) without (e).
- **(b,c) s5 E3, E3′.**
  - At α_cor = 0.05 the alarm fires at 32.1 (V = 0.579) under every dynamics: capture is too slow.
  - At α_cor = 0: under QS, R(1) and R(0.1) the crossing is silent until V = 0.200 at t = 58.8.
  - At α_cor = 0, slow adjustment (R(0.03), additive) reverses the clocks: the alarm fires at 32.1.
- **(d) T_A [independent].** The formula in the drafted Scope, T_A = (ρ−h_V ē)⁻¹ ln[(1−V*/V0)/(1−V*/V_alarm)], equals direct integration: 26.111/26.112, 28.768/28.769, 12.771/12.771.

### ES: explicit-action enforcement (`enforce`, `relpunish`, `restraint`, `require` R4). Independent; (f) identity.
Sources: f6 (A–D); m07 (A–E); m08 (C); Math-Opus reviewer s3_enforce (1–4); Math-Fable reviewer m6 (2,5); Codex 6.

- **(a) Per-deviation p_d.** X (g=1, p_d=0.1) is deterred: 17.5 < 30, temptation 0.37 against sanction 1.62. Y (g=0.2, p_d=0.6) is not: 39.2 > 30, temptation 1.64 against 0.72.
- **(b) Breakouts during punishment.**
  - The closed forms equal value iteration. Exclusive: v = 0.8950, 1.2857, 1.6875. Independent: 0.8723, 1.2366, 1.5816.
  - New example: deterred at q = 0, not at q = 0.045, with v = 0.895 < C.
  - The independent form is valid at q = 0.6 (v = 1.6241).
- **(c) Window.** Enforceable at q ≤ 0.035; not at 0.036–0.055 although v < 1; v > C at 0.056. The predicted window is (0.0354, 0.0556).
- **(d) m07(C).** 20,000 random settings. Cooperation is sustained in 6,821; the punisher prefers to quit in 35. Where the punishment is credible, best response over all plans agrees with (14) in **19,965/19,965**.
- **(e) R4.** p̄ = 0.8642; (14) fails at p_d = 0.87 and 0.9 although D < C. When (1−δ)g ≤ δ(C−D), it holds at every p_d.
- **(f) [identity]** Exact rationals: 0/20,000 disagreements, so EC tests only the algebra.
- **(g) Windows by g.** [0.0498, 0.0555], [0.0354, 0.0555], [0.0159, 0.0555] for g = 0.5, 2, 5. Racing in punishment is credible. dp̄/dD = 0 at p̄ = 0.
- **(h) Homogeneity.** p̄ = 0.2963 at ×2 and ×10 scaling of all stakes. Scaling only g and D gives 0.1296 at ×2 and −0.0037 at ×10.
- **(i)** The q = 0.6 algebra.
- **(j) Continuations.**
  - Exchangeable: 0.000000.
  - Label-dependent: −8.1818; deviation worth −69.64, so cooperation is sustained.
  - Symmetric variant: deviation +4, not sustained.
  - Codex 6 ported.

### JX: scissors and detect link (`scissors`, `detectlink`, `jointscissors` S5, `zonesillus`, `enforce`, `standprice`).
Kinds by part: (a)–(c) and (e) independent; (d) identity; (f),(g) "[num, one reduced model, rivals not responding]".

Sources: m10 (A,B,C); f6 (F); Sys s3_zones; **both unit-draft scripts**, U05/A `checks/jx_joint_scissors.py` and U05/B `scripts/jx_joint.py`. Both are ported because the U05 merge has not chosen; their models differ (nonlinear against linearized T_dec).

- **(a) Largest enforceable Γ_δ.** θ0 = 0: 0.924, 0.852, 0.387, 0.108 at p_d = 0, 0.5, 0.9, 0.94; none above **0.9495**. θ0 = 0.4: none above **0.9793**.
- **(b) Common return.** At p_d = 0.9 the value is 0.387, 0.571 and 0.755 for Γᶜ_δ = 0, 0.3 and 0.6. The U05/B draft cites the 0.57 as "[num: NB]"; it is JX(b).
- **(c) Test G.**
  - D = C: +0.05, +0.09, +0.21, +0.34, +0.50, +0.82, +0.97 at p_d = 0, .5, .8, .9, .95, .99, 1.
  - D−C = 0.5: +0.05, +0.30, +0.92, +0.33, 0, 0, 0.
  - θ_rep by direct streams: −0.901, −0.812, −0.322, +0.005, +0.634, +0.937. At D−C = 0.5: 2.337 at p_d = 0.9, none at p_d = 1.
- **(d) detectlink [identity].** max |1−p̄ − (T−R)/(T−P+F)| = 4.4e-11 over 100,000 draws, with R = C, T = (1−δ)(C+g)+δD and P−F = (1−δ)(C+g)+δv. Prop 8.10's case T < R is p̄ ≥ 1.
- **(e) [independent]** The Poisson clock gives p_d = exp(−T_dec/τ) within 4 SE (0.4485/0.4493). The simulated deviation values agree with (14): 0.7384 deterred; 1.2347 not.
- **(f) U05/A model.**
  - D = C: restraint is enforceable iff the won share ω < 0.551. With one breakout technology throughout the threshold is 0.542; the objective blade alone gives 0.556; the breakout blade alone never closes.
  - At the crossing: Γ = 1.323, Γ_δ = 0.916, p_d = 0.100.
  - D−C = 0.5: thresholds 0.536 and 0.504.
  - Paths: with fixed provision and stakes growing 5%, the blades cross at t* = 31.8. With provision growing with the stakes, nothing moves: ω = 0.20, p̄ = 0.911.
  - Robustness: over 96 settings (both D−C values) the joint threshold lies at or below each blade's own in 96/96, strictly below in 84. The breakout blade alone closes in 12 of the 96.
- **(g) U05/B model** (linearized T_dec, δ = 0.8, d_K = 0.5, r = 1.5).
  - The blades meet at **t = 59**; at t = 47 if stage payoffs scale with the stakes.
  - They never meet when provision grows with the stakes.
  - Detection twice as fast: t = 60. Held self-model 0.4: t = 69.
  - p̄ starts at 0.842; the won share starts at 0.20.

### DL: delegation when the lock counts (`delegatelock`, `nearlock` S6). Independent.
Sources: f7 (A); m09 (check_delegation); Codex 7; U06/B `checks/dl_nearlock.py` (e). V6.1's SM(6) is the p = 1 predecessor.

- **(a) Ratios by k.** At p = 0.1: 1.002589, 1.000973, 0.999275 for k = 0, 1, 2, so the only pure equilibrium has 2 delegators. At p = 1: 1.4775, 1.576, 1.6417, so all delegate.
- **(b) Codex 7.** Holds.
- **(c) Neither corner an equilibrium** (20,000 draws each): 0 at p = 1; 1,586 at p = 0.5; 60 at p = 0.1.
- **(d) q_L = 1.** Not delegating is strictly better in 20,000/20,000 draws.
- **(e) `nearlock` (Remark S6.1).** Above the bound (1−q_L)(1+s)(1−ψ_1) < 1−ψ_0, not delegating is strictly better in 200,000/200,000 draws (source seed and draw order). Tightness at n = 2, 10, 100, 10⁴ (k = 0, p = 1, s = 5): ratio/bound 0.2857, 0.6667, 0.9524, 0.9995, equal to n/(n+s).

### AL: the alignment reviewer's checks of §6, whole (al_checks). Independent; parts marked [derived].
This block is added beyond the plan's list. The 06_S6 draft asks for al_checks "to be ported into a block of its own"; citations should read AL(part). All numbers reproduce the reviewer's log with the reviewer's seeds.

- **(6.1)** θ* = 0.9375; 1.4438 at ε = 10 with c fixed.
- **(6.2)** s* = 1.1628; the lone delegator wins with probability 0.5196.
- **(6.4)** With p = 1, at least one corner holds in 100,000/100,000 draws.
- **(6.7)** Private benefit → 1; common → 0. Tax 0.01 against an advantage of 0.005 → 0; against 0.02 → 1.
- **(BT)** 0.710950 with and without a shared harm; comply against abstain: 0.0241.
- **(6.8)** 0.630 from t = 1; 0.473 from t = 0; 1.6e-9 by 20,000.
- **(6.9)** Topology numbers; the adversarial blind spot.
- **(6.10)** 7.39 and 37.31 steps.
- **(6.11)** The interior solutions; marginal gains positive at t = 3–8; 3/16.
- **(bounded)** R* = 2.30, 4.61, 6.91, 13.8; satisficer 3.0.
- **(contest)** Intensity 0.25 → 250 under θ = −1 as c falls 1 → 0.001; bounded (0.62) at θ = 0.

### TR: the transition (`signal`, `pausevalue`, `readiness`, `readrule`; X11's staying-out identity). Kinds by part: (a)–(c) independent (brute-force search over strategy profiles); (d)–(f) direct computation; (g) simulation; (h) identity.
Source: U11/A `checks/tr_transition.py`, ported verbatim as one function with its seed (20261004) and draw order. Its 12 assertions reproduce the source log line for line (`planning/drafts/U11/A/checks/tr_transition.log`). About 2 s.

- **(a) `signal`(1).** The search, which does not use the condition, agrees with "separation iff c_S ≤ Π_S and c_R ≥ Π_R" in 300/300 random games.
- **(b) `signal`(2).** Over 200 games with 0 ≤ c_R < Π_R and 1−μ < ϖ*, no equilibrium has restraint after E above c_R/Π_R (max excess 0). The bounding hybrid equilibrium is found in 135/135 games with c_S ≤ Π_S c_R/Π_R.
- **(c) The printed example.** c_S = −0.05, c_R = 0.30, Π_S = 0.40, Π_R = 0.20 (μ = 0.5, ϖ* = 0.6) separates. With c_R = 0.05 it does not; R imitates with probability 0.667 and restraint after E is at most 0.25. The intuitive criterion removes pooling on N (E is equilibrium-dominated for R, −0.10, not for S, +0.30).
- **(d) `pausevalue`(1).** Shift invariance in 200 random hazard sequences.
- **(e) `pausevalue`(2).** Hazard 0.01 for 20 rounds, then 0.01/k^1.5: survival to round 10,000 is 0.7969 (limit 0.7968); unchanged at 0.01 a round, 2.25e-44.
- **(f) `readiness`, `readrule`(1).** 0.95⁷ = 0.6983. A fixed reading of 16 observations designed at noise 1 passes a met dimension with probability 0.953 at noise 1 and 0.372 at noise 2; seven pass with 0.7134 and 0.0010.
- **(g) `readrule`(2), SPRT** (α = 0.01, β = 0.05/7, 4,000 runs per cell). Observed false "met" 0.0075, 0.0057, 0.0060 and missed "met" 0.0037, 0.0035, 0.0067 at noise 1, 2, 4, all below the bounds 0.0101 and 0.0072. Mean readings when met 10.5, 38.7, 148.6. Seven dimensions: held back with probability at most 0.0505.
- **(h) [identity] X11, staying out alone.** Joining ε(1+ε)/2 against staying out ε (rival's decisive chance unchanged) and ε² (raised to 1−ε²), at ε = 0.05, 0.1, 0.3, 0.6.

### ML: meta-loop toy (`metaloop`). Derived (toy). Not cited in the core.
This block is added so that Sys s6 has a home; plan §9 moves the toy to the TESTS research programme. One fixed point at k = 2; three (bistable) at k = 12, θ_c = 0.

### CI extension (`blind`, `nested`, `require` R8). Independent.
Sources: f4 (A,C); m05 (A,B,D); Math-Fable reviewer m6 (1); Codex 5.

- **(f,g) Three regimes.** Tipping at 0.375 and 0.750 when s(0) > c > s(1). Evasion is global when s(0) < c; compliance is global when s(1) > c.
- **(h) Unequal costs** (0.1, 0.2), with sanction pairs:
  - (1, 1) and (0.15, 0.25): compliance → 1;
  - (1, 0.15): compliance → 1 although s_B < c_B;
  - (1, 0.05): evasion → 1.
- **(i) f4(C).** The compliant share is 0.999999975 at t = 20; compliers sort 0.88/0.12. Equal incidence preserves the ratio (1.000000). Unmatched: the safeguarded developer → 1. Matched: 2.0e-9 at t = 200. Zero tax: shares unchanged. Codex 5 holds.
- **(j) m05(D).** The matched twin eliminates the safeguarded developer (1.4e-87). A lead of 0.02 pays a tax of 0.01; a lead of 0.005 does not.
- **(k) `unravel` across types (Remark S9.1), added in the completion pass (U09 merge note §4 item 9).** Two types with c = 0.3: s₁ = 0.48(1−x) (tips at 0.375) and s₂ = 0.6−0.4x (tips at 0.75); x is the mass-weighted outside share; each type moves as x_k′ = x_k(1−x_k)(c_k − s_k(x)), integrated in logit coordinates without using the tipping shares.
  - Below min_k x_k† = 0.375, 400/400 random states return to full participation at type masses (0.5, 0.5), and 400/400 at (0.8, 0.2).
  - From x = 0.38 held by type 1: type 1 leaves and the outside share settles at 0.5 when its mass is 0.5 (type 2 stays); at mass 0.8 it carries x past 0.75 and type 2 follows (x → 1).
  - A third type of mass 0.1 with s = 0.24(1−x) < c at every x leaves from 1% outside while the other two return: full participation is impossible.

### PR extension (`onegroup`). Independent.
Sources: f4 (B); m05 (C); Codex 8; Math-Opus reviewer s5_misc.

- **(e)** 600 populations: total > 0 in 0/600 and within > 0 in 0/600; between > 0 in 13/600, none under affine fitness.
- **(f) Codex 8.** Between +0.00920, within −0.12416, total −0.11496.
- **(g)** Six transforms × 3,000 populations: total and within terms are never positive. Between-group counts: affine 0; exp 33; log 3; cube 10; logistic 121; step-like 346.
- **(h) s5_misc.** Between: −0.0025 linear, +0.0001 and +0.0005 concave; the total is negative in all three.

### CS extension (`influence`, `corrrate`, `costq`). Independent.
Sources: Math-Fable reviewer m4 (a–e); Math-Opus reviewer s4_cost (a); f5 (D).

- **(f) Size thresholds** 0.22361, 0.17167, 0.09982, 0.05000 equal f^{1/(2−ξ_f)}.
- **(g) Exponents.** At η ∈ {0.5, 1, 2} and ξ_v ∈ {0, 0.3, 1}: q* ∝ p^{(2−ξ_v)/η}, spending ∝ p^{2+(2−ξ_v)/η}.
- **(h) Splitting factor** k^{(2−ξ_v)/η}, e.g. 16 and 625 at η = 0.5.
- **(i) Rate law** at η = 0.5 (threshold 0.1333) and η = 2 (0.0667). Growth rates ±0.0600 and ±0.0300 match (g−(1+η)α)/η.
- **(j) Signs.** dq*/dγ < 0, dq*/dd < 0, dq*/dχ > 0.
- **(k)** 300 random (ξ_f, ξ_v, η): 0 mismatches.
- **(l) Ŷ scaling.** d ln q*/d ln p = (2−ξ_v)/η: 2, 1, 1, 3.

### DW extension (`pausefield`, `dwell`, `reachable`). Independent.
Sources: Sys s2_dwell, s2b_depth, s2c_pause. The method is independent of DW's: a backward-integrated separatrix and the analytic insulated path.

- **(a)** Reproduces DW's dwell to three decimals in 6/6 (1.886, 5.318, 10.453; 5.859, 10.343, 16.181). x_σ = 0.676 at ε = ζ and 0.984 at ε/ζ = 0.1 (G = 2).
- **(b) Hard floor λ on alternatives.** At G = 10, ε/ζ = 0.1 the dwell falls **10.45 → 3.81** at λ = 1e-3. Table for λ = 1e-2 to 1e-12 in the log.
- **(c) Mutation** at μ = λζ(G−1): 3.28 (λ = 1e-3) and 4.12 (1e-6) at G = 10, ε/ζ = 0.1. The log also gives the values from x0 = 0.99.
- **(d) Protected but non-recruiting share.** 10.44, essentially unchanged: the bound needs a recruitable lineage.
- **(e) Depth of lock-in.** At G = 2, ε = ζ: 3.45, 5.86, 8.17, 15.08, 28.90 for x0 = 1−0.1 down to 1−1e-12. The dwell grows roughly linearly with the age of capture.
- **(f) Frozen-share pause**, ε·d·T = ln(G/S(x_p)). At ε = ζ, G = 2: none needed at x_p = 0.3; ln 2 = 0.69 at x_p = 1/G; 1.50 at 0.6; impossible above x_σ = 0.68. Table for ε/ζ = 0.1 and G = 5 in the log.

### CR extension (`relpunish`). Independent.
Sources: f6 (E); m08 (A,B); Math-Fable reviewer m3_cor55; Math-Opus reviewer s3_enforce (5).

- **(d) Strictness.** Weak at ε = 0; strict at +0.02; not an equilibrium at −0.02.
- **(e) m08.** The deviator is held at −0.5; δ* = 0.706. Matching role assignments are strict. With anonymous perturbations a strict punishment exists in 300/300, 300/300 and 282/300 games (median δ* 0.708, 0.711, 0.713).
- **(f) m3.**
  - Every (a, b) holds the deviator at −0.5.
  - Both punishers prefer the Y role (+1.0 against −0.5), so role assignment needs coordination.
  - In the targeted-attack game a θ = −1 punisher is exactly indifferent between hurting the deviator and hurting its fellow (0.95 = 0.95).
- **(g) s3(5).** 400/400, 400/400, 372/400 games, all strict; median δ* 0.707, 0.711, 0.715. The RNG stream is advanced as in the source, so the counts reproduce the reviewer's log.

### TK extension (`talk`). Independent.
Sources: m09 (talk, talk_theta); Math-Opus reviewer s5_misc.

- **(d)** At θ = −1 the gap is b0·n/(n−2): 0.150, 0.100, 0.075, 0.0625 at b0 = 0.05. Informative talk needs a material bias below 0.0833, 0.125, 0.1667, 0.200.
- **(e) Unified form** b0(n−1−θ)/(n−1+θ): 19 combinations, max deviation 1.5e-8. n = 2, θ = −0.9 gives 1.33.
- **(f) Nonlinear third parties.** The state-units gap is 0.1498/0.1500 and 0.1001/0.1000 at grid resolution.

### HO extension (`safeguards`, `require` R1). Independent.
Sources: f7 (D); m09 (safeguards, R1); Math-Opus reviewer s8_logistic_margin, s5_misc (Allee).

- **(d) f7(D).** Δ = 0.08 dips to 0.1397. Δ_min = 0.108, 0.165, 0.355 for floors 0.2, 0.3, 0.5. With e_min = 0.1: 0.125, 0.192, 0.414, and the long-run level is 0.840.
- **(e)** Three integrators (f7, m09, s8) agree to 0.002.
- **(f) Allee host** (e_min = 0.1). Δ_min = 0.260, 0.306, 0.359, 0.423, 0.505 for A = 0.05 to 0.25, close to V_u. A shortfall there is permanent.
- **(g) R1.** τ = ν − 1/(2√(t+1)) has a long-run average of ν, yet the host crosses the floor at t ≈ 89. With τ = ν it never crosses.

### SH extension (`share`). Independent.
Sources: f7 (E) (Nash); m09 (uninvadable).

- **(f) Nash intensities.** 0.13125 (shared among all n) against 0.11250 (shared among the n−1 others) at β = 0.3; 0.07500 against 0.03750 at β = 0.6.
- **(g) Uninvadable intensities** with Ω_s = 0.5: 0.300 and 0.275 at β = 0.3; 0.225 and 0.175 at β = 0.6.

Both conventions match their Ω_eff.

### SM extension (`opaquecorr`, `homeostasis`, `topology`, `fallback`; `thrrep` S3). Independent; (13) derived; in (15) the branch-slope comparison derived; (16) derived.
Sources: f7 (B,C,G); m09 (opaque, absorb, topology); Math-Opus reviewer s5_misc (Lemma 8.2); `../v5/checks_v5.py` HO (15); written for Remark S3.1 (16).

- **(11) Prop 6.8.** The printed example gives 0.473 from t = 0 and 0.630 from t = 1, falling to 1.2e-9 by 20,000. Fable's replacement gives 0.5101 at 200 and at 20,000. Opus's gives 0.6888 at both.
- **(12) Prop 6.11(3).** Full delegation is a best response at t = 0–7. Marginal gains: +0.111, +0.023, +0.037, +0.102, +0.154, … Realized risk from t = 5: union bound 0.1875 = 3/16; exact 0.1836.
- **(13) Topology.** 0.531, 0.989, 0.940, 0.941, 0.994. Blind-spot catch 1.000, 0.950, 0.700.
- **(14) Lemma 8.2.** S^A ≥ S^C at H = 10, 30, 100: 0.8840/0.8126, 0.5507/0.4610, 0.0770/0.0615.
- **(15) `homeostasis`(2), the two-root example** (completion pass; U06 merge note §4). n = 2, s = 100, L_e = 0.5, L_c = 1, ψ₀ = 0.01, Δψ = 0.9: interior roots ι = 0.152949 and 0.937051, both global best responses on a 4,001-point grid, and the corner ι = 1 is also an equilibrium; realized hazards 0.2735 and 0.9785. Residual of (x+b_s)(1−ψ₀−x)^{n−1} = K_h: 3e-17. [derived] The branch slope of S6.2(2) equals a finite difference of the computed roots: −0.01208 on the lower branch, +0.00208 on the upper, so its sign differs between branches. The text still cites this example as "HO of `../v5/checks_v5.py`, run by `checks_v62.py --legacy`"; it can now cite [num: SM(15)].
- **(16) `thrrep` (Remark S3.1)** (completion pass; U03 merge note §4 item 10). From the stage payoffs of Proposition 3.7 (Υ = 3, n = 4), the reversion cutoff by bisection on discounted streams equals the formula: 0.1111, 0.4667, 0.9497 at λ = 0, 2, 50, and full depletion is dominant in each stage game, so reversion is credible. [derived: the stage payoffs are the model's.]

---

## Codex's boundary cases (plan §7), where each one runs

| Case | Block | Codex's numbering |
|---|---|---|
| Γ_δ ≥ 1 | PD(a) | 1 |
| Cap equality | CE(e) (also CE(b), s9, m1(C)) | 3a |
| Positive diffusion | CE(f) (also CE(a),(c)) | 3b |
| Falling positive f | FF(a) (also FF(b)–(d)) | 4 |
| Unequal incidence | CI(i) (also CI(h)) | 5 |
| Stochastic punishment asymmetry | ES(j) | 6 |
| p < 1 | DL(b) (also DL(a),(c)) | 7 |
| Nonlinear fitness | PR(f) (also PR(e),(g),(h)) | 8 |
| (extra) decay raises the gain | CH(c) | 2 |
| (extra) provision raises 1+θ | SP(H) | 9 |

The run ends with this index and asserts that all eight required cases ran and hold.

## Scripts and where they went

- **math-fable.**
  - f1: SP(A,B,D), PD(b).
  - f2: MP(f,g).
  - f3: CE(a), CH(b), TD(a,c).
  - f4: CI(f,i), PR(e).
  - f5: QS(a), FF(b,e), CS(l).
  - f6: ES(a–c,j), CR(d), JX(c).
  - f7: DL(a), SM(11–13), HO(d), SH(f), SR(a).
- **math-opus.**
  - m01: MP(a,c–e).
  - m02: SP(C,E,F,G), PD(c).
  - m03: CH(a,e), TD(b).
  - m04: CE(b–d).
  - m05: CI(g,h,j), PR(g).
  - m06: QS(b,c), FF(c,f).
  - m07: ES(a–e,h).
  - m08: CR(e), ES(j).
  - m09: DL(c), SM(11,12), TK(d,e), SH(g), HO(e,g).
  - m10: JX(a–c).
- **Reviewer scripts, v6.1.**
  - Codex: PD, CH, CE, FF, CI, ES, DL, PR, SP (all nine cases).
  - Math-Fable m1: CH(f), CE(h). m2: MP(b). m3: CR(f). m4: CS(f–j). m5: QS(h). m6: CI(g), ES(a,i), TD(d); its item (4) is prose.
  - Math-Opus s1: CH(g). s2, s2b: MP(h). s2c, s2e: MP(j,k) under --full. s2d: MP under --full. s3: ES(f,g), CR(g). s4: CS(k), FF(e), QS(i). s5: PR(h), HO(f), SM(14), TK(f). s6: EC. s7: FF(d). s8: HO(e). s9: CE(g).
  - Systems s1: CH(d,e), TD(d). s2, s2b, s2c: DW extension. s3: JX(c). s4: QS(d). s5: QS(e–g), SR(b). s5b: SR(c). s6: ML.
  - Alignment al_checks: AL.
  - Adv-O adv_checks: §1 → CH(h); §2 → SP(I); §3 → MP(i).
  - Adv-F prop39: SP(J).
- **Unit drafts.** U05/A `jx_joint_scissors.py`: JX(d–f). U05/B `jx_joint.py`: JX(d,g). U06/B `dl_nearlock.py`: DL(e). U11/A `tr_transition.py`: TR (whole).
- **Legacy, ported in part.** `../v5/checks_v5.py` HO's Δψ = 0.9 example: SM(15). The rest of v5 HO, and every other legacy block, still runs only under `--legacy`.
- **Written in the completion pass** (no source script; each asked for by a merge note): SM(16) `thrrep`; CI(k) `unravel` across types; QS's S4.2(2)(b),(c) and capture-lag lines.
- **Not ported, because they are not numerical checks of the theory.**
  - Evidence: `cites.py`, `cites2.py` (citation matching).
  - Fidelity: `units.py`, `sample.py` (loss scan and sampling, with paths to an old scratchpad).
  - Math-Opus `dbg_mpe.py`: a debugging scaffold for s2 with no claim.

## Findings and discrepancies

1. **CE: the stall level is 0.16 K̄, not "0.36 K̄".** D2-fable §3(d) and §29.9 say that with δ_f = 0.05 alone the laggard "stalls at 0.36 K̄". The simulation (f3's own) ends at K = 0.3624 with K̄ = 2.25, which is 0.16 K̄. The claim itself holds: φ(0+) = 0.056 > 0, yet min φ = −0.013 < 0. The assertion now states 0.16 and prints the correction.
   - Also: the "min φ = 0.0007" of D2-fable depends on the grid. It is 0.0001 on m04's 10,000-point grid and 7.5e-5 by Codex's exact factorization. The text should say "positive (minimum about 7.5×10⁻⁵)", not quote 0.0007.
2. **FF: a printed note in f5.py is wrong; D2-fable's statement is right.** f5's printed reading says that at α_cor = α_f, "f0 = 0.17: 1.06 > 1 → no cultivation, holds". A ratio d_f(0)/d0 = 1.06 > 1 means cultivation is on at the start, and the run fails at t = 58.0 (f5's own log line). The no-cultivation case is f0 = 0.3, which holds. FF asserts the correct reading.
3. **CI: "s_k ≥ c_k for every type" is sufficient, not necessary (D2-opus §22.4 is right).** D2-fable §6 and §18 word the compliance condition as "iff s_k ≥ c_k for every type that can evade". m05(B) has costs (0.1, 0.2) and sanctions (1, 0.15). B's evasion pays within its type (0.15 < 0.2), yet A's compliers beat B's evaders, and evasion vanishes. The "iff" is exact within a type, or where the evading type's payoff is the highest in the population. The plan's wording ("needs expected sanction ≥ gain from evasion, per type") should read as sufficient, or be stated within a type.
4. **QS/`humancorr`: the exact shift +wδ_h holds for pure erosion, and is smaller with recovery.** m06(D), with M′ = −δ_h M, gives thresholds exactly 0.15 and 0.20. Sys s5 E4a has recovery ρ_h(1−D)(1−M), with D rising to 1, and a horizon of 600. Its shifts are +0.049, +0.094, +0.135 for δ_h = 0.05, 0.1, 0.2. At δ_h = 0.2, ρ_h = 0.1 the shift is 0.135, not 0.2. The statement "+wδ_h" should name its premise: erosion at rate δ_h without recovery, as in D2-opus §9 Prop 4.6(3). The Systems figure is "about δ_h" only for small δ_h.
5. **The memos use different replacement examples for Prop 6.8, so their numbers differ.** Fable uses c_{b,t} = 1−2^{−(t+1)} from t = 0 and gets 0.5101. Opus uses c_{b,t} = 1−2^{−t} from t = 1 and gets 0.6888. Both are summable and both are checked (SM(11)). Choose one and cite it with its start index.
6. **Prop 6.11(3): the 3/16 is the union bound.** Fable's 3/16 = 0.1875 is Σ n·Δψ_t from t = 5, the union bound. Opus's exact realized risk is 0.1836. "At most 3/16" is true for both (SM(12)).
7. **Prop 10.3(2): two solution concepts, two sets of numbers.** Fable gives Nash intensities with Ω_s = 0: 0.13125/0.11250 and 0.07500/0.03750. Opus gives uninvadable intensities with Ω_s = 0.5: 0.300/0.275 and 0.225/0.175. Both confirm the same two Ω_eff formulas (SH(f,g)).
8. **Draft citations to rename.**
   - "[num: GP; m02 C]" → SP(C)/(F).
   - "[num: NB]" for the common-return value 0.57 → JX(b). NB prints 0.924/0.852/0.387 in its p_d table, but not 0.57.
   - "al_checks, block BT" → AL(BT); "blocks `bounded objective` and `contest`" → AL(bounded), AL(contest).
   - "[num: S6]" in the 60_s6 draft refers to the Supplement chapter, not a block. The numbers are AL(bounded), AL(contest).
9. **JX: the two U05 models disagree on which arm closes.**
   - In U05/A (nonlinear T_dec, r = 3) the breakout arm alone never closes the blades in the base case, and closes them in only 12 of 96 robustness settings. The objective arm does most of the closing: the joint threshold lies just below the objective arm's (0.551 against 0.556), and strictly below in 84/96.
   - In U05/B (linearized, r = 1.5) p_d is 0.0565 at the meeting (t = 59), which also says the objective arm dominates. Its text says so.
   - Neither model supports a sentence in which the breakout arm drives the scissors in these parameters. The cited meeting times (59/60/69, or 31.8 in U05/A) belong to different models and must not be mixed.
10. **MP multiplicity** (×12.5 and ×8.8 structural at d = 0.05) stays "[finding held for outside review]", as plan §3 requires. Nothing new here.
11. **TD: the 1%→50% time can be infinite under diffusion.** m03(C) at r = 3, d = δ_f = 0.05 (Γ = 1.5) never reaches 50% within 10,000 periods, although the linear estimate is 80.2. The nonlinear gap settles short of decisive. D2-opus §2 states this; D2-fable §5 does not. T_dec "about ln(Δ̄/ε0)/ln Λ*" needs "while the linearization holds" or "if the decisive gap is reachable".
12. **One loose assertion was tightened, none loosened.** One port initially failed for a floating-point equality (`== −0.5` in m3's check). It now uses a 1e-12 tolerance. No claim's tolerance was widened to make it pass.
13. **Block TR was cited and did not exist** (THEORY: `signal`'s proof and `readrule`'s sentence; SUPPLEMENT: the numerics of `signal`, `pausevalue` and `readrule`; DISCUSSION: X11's staying-out identity). It is now ported from U11/A and reproduces the source's log line for line; every number the text tags [num: TR] is printed (300, 200, 135; 0.667, 0.25; 0.7969 → "0.80", 2.25e-44; 0.953, 0.372, 0.7134, 0.0010; 10.5, 38.7, 148.6; 0.0505).
14. **Citations the text can now use** (for the text, not done here):
    - S6, `homeostasis` Numerics (2): "[num: HO of `../v5/checks_v5.py`, run by `checks_v62.py --legacy`]" → "[num: SM(15)]".
    - Remark S6.1 `nearlock`: its check is DL(e).
    - Remark S3.1 `thrrep`: its cutoffs are SM(16).
    - Remark S9.1 `unravel`, the part across types: CI(k).
    - Proposition S4.2(2)(b): the m06 run it cites is asserted in QS(b); (2)(c)'s "0.063 at every horizon" and the "8 to 85" are asserted in QS(d).
15. **A kind label corrected.** The SM extension's sub-header said "(12) derived". Part (12) is a grid best response (independent); the derived part is (13), the topology formulas, as this file already said. Only the printed header changed.
16. **"Multiplicative" means two different dynamics in the ported scripts.** In f5(A) and s4 E1 ("GM") the selection variance is proportional to q², and fast selection tracks the quasi-static date; in m06(D) ("multiplicative V=1") it is proportional to q, and capacity stays bounded. The existing f5(A) assertion ("multiplicative selection tracks QS") is right for its own dynamics and is kept; S4 names the dynamics by their variance, which avoids the clash. Read the log by variance, not by the word.
17. **S15 still describes `checks_v61.py`** (SUPPLEMENT S15: "about fifty seconds; log `checks_v61.log`", and "`python3 checks_v61.py --legacy`"). It should name `checks_v62.py`, 188 assertions, about 300 s, and the v6.2 blocks, TR among them (build notes §2.1; the registers task).
18. **No assertion failed** in the completion pass, and no tolerance was changed.

## Completion pass, 4 October: what was added

Asked by `planning/build-notes.md` §2.1 (Checks) and the merge notes. Every existing block, assertion and tolerance is unchanged; the previous log's lines are reproduced except four headers (CI and SM extension sub-headers and the DL header now name their new keys; the SM sub-header's kind label read "(12) derived", but the derived part is (13), see finding 15) and the timing and count lines.

| Request | Where | Assertions |
|---|---|---|
| Block TR, cited as [num: TR] (U11 §4 item 2) | TR (a)–(h) | 12 |
| DL(e) `nearlock` (U06 §4) | DL(e) | 1 |
| `homeostasis`(2) two-root example (U06 §4) | SM(15) | 1 |
| QS comment "iff" → "if"; an S4.2(2)(b) assertion; the capture-lag range 8–85 (U04 §4) | QS (b), (d) | 3 |
| `unravel` across types (U09 §4 item 9) | CI(k) | 1 |
| `thrrep` cutoffs 0.11/0.47/0.95 (U03 §4 item 10) | SM(16) | 1 |

Not done here, as before: porting the legacy-only blocks (v4.4 SV; v4.5 LD, N22, K7; v5 SR, FS, N13, CMP, K7 and the rest of HO). They are documented legacy blocks, labelled "legacy" in the text, and run under `--legacy` (not re-run in this pass). If ported, avoid the names FS and SR (U05 §4.7, U08 §4.3, U10 §4.9).

## Every block the text cites, and its status

Scanned in the assembled THEORY.md, SUPPLEMENT.md and DISCUSSION.md of 4 October 12:51 (and the same tags in `src/`), for `[num: …]` and `[identity: …]`.

| Cited as | Status |
|---|---|
| AC, BI, CB, CE, CH, CI (b, e, h, i, j), CR, CS, DW, EC, ES, FA, FB, FD, FF, FS, HO, JX, LG, MP, NB, PD, PE, PR, QS, RH, SH, SP, SR, T3, TC, TD, TH, TK, WG | exist in `checks_v62.py`; pass |
| SM, SM(1)–(7), SM(11)–(14) | exist; pass |
| DL, DL(a), (b), (c), (d) | exist; pass (DL(e) added, not yet cited) |
| AL(6.1), (6.2), (6.4), (6.7), (6.8), (6.9), (6.10), (6.11), AL(BT), AL(bounded), AL(contest) | exist; pass |
| **TR** (THEORY ×2, SUPPLEMENT ×3, DISCUSSION ×1 as "num: TR") | **added in this pass**; 12/12 pass |
| legacy v5 (alone), legacy v5 FS, CMP (also "CMP; S8"), N13, SR, K7, HO | documented legacy: blocks of `../v5/checks_v5.py`, run by `--legacy`; the HO example is now also SM(15) |
| legacy v4.5 (alone), LD, N22, K7 | documented legacy: `../v4/checks_v45.py` |
| legacy v4.4 (alone), SV | documented legacy: `../v4/checks_v44.py` |
| legacy v4.2 | documented legacy: `../v4/checks_v42.py` |
| "arithmetic of Proposition 4.5(4)" | not a block: arithmetic in the text |
| "S8" in "[num: legacy v5, CMP; S8]" | a Supplement chapter, not a block |
| bare [num] (THEORY 5 in body, SUPPLEMENT 5, DISCUSSION 1; plus the tag legends of THEORY §0, the symbols list and S0, and S15's sentence) | no block named. By context: THEORY §1 "leads compound below a structural gain of one" → MP; the §5 box "the first two close together" → JX(f); Proposition 10.1's heading and its two uses (THEORY ×3, SUPPLEMENT ×1) → legacy v4.5 N22 (the S10 full statement cites it); Remark S2.5 `gammarange` → CH(h); Remark S5.2 → JX(f); S4.2(2)(c) and (3) → QS; DISCUSSION X8 table "at parity" → MP(i). All have a home; none needs a new block |

## Timing (default run)

The per-block timings are printed at the end of `checks_v62.log`.
- Heaviest blocks: MP 72 s, HO 71 s, CH 29 s, QS 26 s, ES 22 s, DW 13 s, T3 13 s, CE 12 s, CI 11 s; TR 2 s.
- Total: 297 s.
- Result: 188 assertions passed, 0 failed (169 before this pass, plus 19).
