# Exact certificate for the integrated reversible model

5 October 2026. Written before executing this audit. This is an algebraic validation protocol for a specified formal construction, not an empirical preregistration, a parameter fit or a molecular-feasibility test. The original integrated bound was supplied before this protocol was written.

Use the common N=4 material-fabricator model with both A0/A1 types. The initial core state is R3,Y1,F2, with other species absent. The event stops at the eighth forward source capture: it enters P_ij={Ai=C=YGj=1,F2} at capture two and returns there at capture eight after wear of all four functional carriers tagged at entry. Compare joint contributions J_i=P(first reaction forms Ai and the integrated event). Tags/flags are observations, not chemical control.

Inputs from the integrated proof are T=27, K=8, the rational lower bound L=1/808804024575624000000, and m=3/L=2426412073726872000000. Rates are beta=m; sigma0=sigma1=mu=m^2; kappa0=kappa1=k=m^3; copying rho0=1,rho1=2; all remaining positive constants are 1, with zeta0=0,zeta1=1. The proof supplies J0>=L and J1<=3/[2(1+m)]<L/2. Set the conservative comparison margin Delta=L/2; do not optimize it by simulation or parameter search.

Add charged H and spent Lf carriers with H initially B and Lf initially 1. Use capture (g/B)HC. Choose B=max(8,ceil(8TgN(K−1)/Delta)) from the source error bound. Standard potentials in k_B T units are D=Lf=0; C=Y=Ai=Gi=M; R=2M; F=3M; H=4M−ln B; GFi=4M−ln KF; YGi=2M−ln KY, where KF=alpha_b/rho_F=1 and KY=mu/nu=m². Retain passive binding pairs and add all reverse directions dictated by these same potentials. Type0 has no bound-reproduction pair; type1 has both directions.

Before the eighth capture, U<=9, H=B−j, Lf=3+j−U<=10. Added reverse rates have envelope c1*t+c3*t³+c4*t⁴, t=exp(−M), with c1=80m³+16m²+14m+136, c3=90, c4=80m³+80m²+360. Choose the smallest positive integer M such that 2^M>=max(2,2KF,2KY,8T(c1+c3+c4)/Delta). This is direct certification of an analytic inequality, not search over model outcomes. The elementary bound e>2 then certifies the required reverse-rate budget.

Checks required before reporting success:

1. Exactly conserve backbone N and carrier H+Lf+F+GF0+GF1 for every reversible pair.
2. Verify all 31 forward/reverse constant identities using exact monomials in t; template-free formation and catalyzed copying must have the same equilibrium constant. Use falling-factorial stochastic mass action, including Ai(Ai−1) and Y(Y−1), without a factor of one half.
3. Enumerate the bounded original pre-stop core states, with j=0..7 and carriers fixed by the bookkeeping identities. Check the reverse envelope and source-depletion bound throughout that domain. This enumeration does not purport to enumerate the much larger full reversible state class for the selected B.
4. Check detailed-balance edge identities on enabled transitions from the enumerated states by factorial ratios, never by computing factorials of the enormous source population. The rate-constant identity supplies the general algebraic proof beyond the enumerated states.
5. Certify source mismatch <=Delta/(8T), reverse hazard <Delta/(8T), per-branch event error <Delta/4, and remaining integrated gap >Delta/2. Save exact B, M, all rational bounds, state/edge counts, and source/checker hashes in the result JSON.

Failure requires reporting and preserving the failed check before revising the construction. No trajectory simulation, numerical matrix exponential, rate fitting or chemical-realizability claim is authorized by a successful algebraic check. The enormous uncalibrated rate hierarchy, large finite source stock, and extremely small certified probability margin must remain visible in the report.
