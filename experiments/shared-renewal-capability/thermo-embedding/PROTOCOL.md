# Exact algebraic audit of the reversible allocation embedding

5 October 2026. Written before running the new checker. This is a prospective computational check of a derived algebraic construction, not a parameter fit, preregistered empirical test, or molecular-realization claim. The original finite-rate allocation witness and its probability bounds were already known when this protocol was written.

The task is to verify whether a finite, reversible mass-action extension can preserve the same first-capture reliability comparison. Use the original witness at deadline 3 without changing its forward constants: a=b=d=delta=nu=1, g=4, beta=3384, k=1, theta=4, ell=ell_b=141, kappa=162432, mu=159189, alpha_b=4, rho=1. Both arms start at core state (R,C,Y,D,F,G,GF,YG)=(2,0,1,0,1,0,0,0). Add one high-potential carrier H_f and one spent carrier L_f to both arms. The absent arm omits both directions of the construction channel.

Fix the dimensionless energy scale M=20 before execution. With K_F=alpha_b/rho and K_Y=mu/nu, assign standard potentials in k_B T units: D=L_f=0; C=Y=G=M; R=2M; F=3M; H_f=4M; GF=4M−ln K_F; YG=2M−ln K_Y. All fuel-consuming reactions produce L_f; capture is H_f+C reversible to F+C. Keep both existing passive binding directions exactly. For every other forward channel choose its reverse constant from these potentials, using falling-factorial stochastic mass action. The 2Y reverse uses Y(Y−1), with no extra factor of one half.

Required checks:

1. Enumerate the finite state class with material R+C+Y+D+G+GF+2YG=3 and fuel-carrier H_f+L_f+F+GF=3. Verify both conservation laws for every reaction.
2. Verify local detailed balance on every enabled state/channel pair by exact monomial arithmetic in t=exp(−M), including factorial multiplicities. Equilibrium weights are proportional to the product of z_i^n_i/n_i!, where z_i=exp(−potential_i). This is an algebraic rate check, not numerical integration.
3. On the original paths before their first forward capture, U=F+GF is 0 or 1, H_f=1, and L_f=2−U. Verify the total newly added reverse propensity is bounded coefficientwise by A t+B t^3+C t^4, with A=657116, B=3666, C=974592. Existing passive binding reverses are excluded from this perturbation total.
4. Certify exp(5)>128 using its degree-seven Taylor partial sum. Hence t=exp(−20)<2^(−28). Use exact fractions to show A/2^28+B/2^84+C/2^112<1/400. Each arm's first-capture probability therefore changes by less than 3/400 by deadline 3, using the first-added-event coupling bound.
5. Apply this error to the existing absent upper bound 6769/110592 and constructed lower bound 2209/18432. Require the perturbed bounds still strictly straddle reliability 1/10 and the guaranteed gap remains positive. Report every rational result and assertion, not fitted or simulated probabilities.

Do not search rates or energy scales, execute trajectory simulation, estimate a molecular free energy, or present successful assertions as laboratory validation. The exact initial fuel stores and material precursors are part of the preparation. Thermal contact remains an ideal isothermal bath; finite fuel stores remove the need for an infinite chemical reservoir during this particular stopped assay. The reduced work-equivalent W is not equated to physical free energy.

If a check fails, preserve the output and report the failed identity before changing the construction. A revision would be an explicit correction, not a new independent validation round.
