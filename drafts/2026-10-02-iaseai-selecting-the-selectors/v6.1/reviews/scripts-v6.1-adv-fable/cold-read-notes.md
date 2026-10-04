# Cold-read belief log (THEORY.md only, before companions)

Verified by hand (correct):
- Prop 2.2: Jacobian = diag(1-d_j-δ_fj) + a b^T (rank one). Secular eq. gives threshold Σ_j (1-β)κ_jΩ r_j /(n X^j (d_j+δ_fj)) = 1; with nX^j=(κ_jΩ+nk_0j)/d_j this is Γ=1. OK.
- Prop 2.3(1): dp_i = r u_i/(nK*); unstable iff κΩ(1-β)r > (d_K+δ_f)S* = κΩ+nk_0+δ_f S*. OK.
- Prop 3.6(1): FOC gives e(θ)=rΩ(n-1-θ)/(n²(c+(1+θ)ℓ)). OK.
- Prop 3.9 formula: from price c=Γ_δ/(1-Γ_δ) on relative payoff, zero-sum future winnings valued (n-1-θ_0)/(n-1) by a θ_0 actor; θ_eff=(θ_0-q)/(1+q), q=Γ_δ(n-1-θ_0)/(n(1-Γ_δ)). Algebra matches (9). Limits Γ_δ→0 gives θ_0, Γ_δ→1 gives -1. OK.
  BUT: valid only for Γ_δ<1 (geometric sum); denominator n-(1+θ_0)Γ_δ and the series diverge beyond. "Where the loop gain is high" must mean Γ_δ→1⁻. Also depends on FIXED prize Ω making future winnings zero-sum.
- Prop 4.5(2) rate law: q*∝e^{(α_ctl-α_cor)t/η}; cultivated G_ev ∝ q*/d ∝ e^{[(α_ctl-α_cor)/η - α_cor]t}; bounded iff α_cor ≥ α_ctl/(1+η). OK.
- Prop 4.11: after release x grows iff a·(b x_p/d) > c iff x_p>1/G. OK.
- Prop 5.2(1) and ceilings 3, 1.857, 1, 0.333 at θ=0,0.4,1,2 (n=4,r=1); θ_g=(r(n-1)-1)/(1+r)=1. OK.
- Prop 5.4(1),(2): standard deviation/continuation algebra; p̄_d matches. OK.
- Prop 5.7 log utility: s=θ/(1+θ). OK.
- Prop 5.15(2): n/(n-2) bias holds when third parties' payoffs are unaffected by the receiver's action. OK (model-specific).
- Prop 6.1(1),(2). OK.

Where I stopped believing / weakened:
1. §2.3 title & §12.4: "meta-attractor" used as the headline noun, while Def 2.4 says any attractor claim about the world is a conjecture. The name carries an attractor connotation that the results license only in the field model (Prop 4.9). Mechanism ≠ attractor.
2. §3.5 Prop 3.9: regime (Γ_δ<1) and fixed prize. AI is positive-sum; with a growing divisible prize the future is not zero-sum and θ_Γ need not → -1. The result is Powell 1991 formalized; the "manufacture" is first-order, others fixed.
3. §4.6 Thm 4.12: content is condition (e) (capture before evidence), admitted "a condition to check". Theorem by assumption; the title "No viable race through the host" oversells.
4. §5.3 Thm 5.12: content is in (coverage lags)+(residual floor); admitted as central crux. Honest, but then §0's "endangers whoever would win" rests on it.
5. §7.2 Thm 7.1: not a theorem, a summary of previous propositions. §9 Prop 9.1 same.
6. §8.3(d) benign winner: Prop 5.7 one-shot, unconstrained winner contradicts §3.4's own κ>0 interdependence ("the winner still depends on those it would dominate"). Hegemonic stability at its strongest is a repeated game with the hegemon needing followers; the paper's reply leans on Prop 7.2's unestablished premise.
7. §12.1 tier 1 "on any reading of the cruxes": item 1 (narrow E1) depends on q_L and the tactical-advantage case the paper itself concedes in §11.3; item 6 (sharing divisible gains as they arise) is not "mostly accepted by regulated-competition" camp and depends on C6/C8.
8. §12.1 tier 2 trigger uses "estimated time to a decisive position" — an estimate produced inside the field whose masking the paper itself models (§4.4); no independent channel named for the trigger.
9. Restatement: chain (accelerate/regulate/language) at §2.4 end, §7.1, §12.4; "one host no outside" at §3.6, §7.2, §12.2, §12.4; "change the basin then add speed" at §2.6, §5.5, §12.4; "we are one" §3.6, §3.7, §5.4, §7.2, §12.4.
10. Typos: "Theorem Theorem 10.5(3)" (R1 row), "Proposition Proposition 9.2" (§8.3(b)).
