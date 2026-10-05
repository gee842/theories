# Constructed physical regulation: prospective comparison

5 October 2026. AI-assisted extension of the shared-renewal assay. Written before computing its outcomes. This is a mathematical model experiment, not observations of a physical organism or proof of universal direction.

## Fixed question

Does a physically constructed fuel-responsive inhibitor improve the existing joint renewal assays after paying material and energy costs? Compare the whole coupled process, beginning with no regulator. Preserve all outcomes, including failures. A correct response sign in an isolated binding assay is insufficient to predict a net whole-process advantage.

## Supplied realization

State order is `(R,C,Y,D,F,G,GF,YG)`. The original network is unchanged except that `Y` in recycling denotes free catalyst. Bound `Y` keeps its reproductive function: `R+YG→Y+YG` at rate `beta*R*YG`. Its wear `YG→G+D` has the same per-Y rate as free Y. Capture rate is `g*C`.

Regulator reactions are `R+F→G` (rate `kappa*R*F`), `G→D` (`delta*G`), `G+F→GF` (`alpha*G*F`), `GF→G+F` (`rho*GF`), bound fuel leakage `GF→G` (`ell*GF`), regulator wear `GF→D+F` (`delta*GF`), `G+Y→YG` (`mu*G*Y`), `YG→G+Y` (`nu*YG`), regulator wear `YG→Y+D` (`delta*YG`), and Y wear as above. Binding, delays and sequestration are explicit. No policy or free sensor is added.

Material is `N=R+C+Y+D+G+GF+2YG`; usable packet inventory is `U=F+GF`. The reduced work ledger is `W=N-D+U`. Construction spends one packet; recycling spends one packet; leakage and structural wear are losses. Binding affinities and physical chemical potentials are not identified by this bookkeeping alone.

## Prespecified cases and controls

All runs start `(0,1,1,1,1,0,0,0)`, with N=3. Original `a=b=beta=d=k=ell=1`, recycling amplification `theta=4`, regulator `delta=rho=nu=1`. Capture parameter is separately `g=4` and `g=8`; this gives more incident support than the earlier g=1 example, but does not guarantee support is captured or effectively used.

| Arm | kappa | alpha | mu | Purpose |
|---|---:|---:|---:|---|
| absent | 0 | 0 | 0 | Original process at the same g |
| burden | 1 | 0 | 0 | Constructed inert material burden |
| buffer | 1 | 4 | 0 | Fuel binding without catalytic inhibition |
| inhibitor | 1 | 0 | 4 | Constant inhibitor without fuel binding |
| responsive | 1 | 4 | 4 | Fuel-responsive inhibition |

Constructed arms share unit costs/rates, not necessarily equal realized expenditures. Five arms separate fuel binding, inhibition, and construction burden. No parameter tuning or post-hoc favorable arm substitution is authorized within this fixed comparison.

Horizons are H=0.25, 1, 3. Primary readouts are the same eight `(j,b,f)` profiles in `{0,1}^3`: at least j recycling events, at least b `R→C` assemblies, at least f **free** packets at H, and protected productive material `A=R+C+Y+YG>=1` at H. The A=0 face is invariant. An inhibitor-only remnant cannot pass. Report probabilities and the alpha=0.5 reliable region. This finite assay vocabulary is not all possible generativity and this autonomous run is not an optimized controller class.

Secondary readouts are probability any regulator was constructed and probability an intact regulator remains. These distinguish physical formation from net utility. They do not establish evolved origin, learned adaptation, or self-maintenance of a reaction repertoire.

## Calculation and interpretation

Construct the reachable generator, augmenting recycling, assembly and first-construction flags. Stop at an absorbing overflow state upon total packet U exceeding K=32; preserve the true outgoing capture rate. Compute the finite-chain transient law with SciPy sparse matrix exponential. For each assay, finite-chain success plus overflow bounds the original success **up to unverified floating-point arithmetic error**. This is a numerical estimate with explicit model truncation, not the earlier directed-rounding certificate.

Repeat all ten networks with K=48 as a truncation sensitivity check; report mass errors and the greatest assay difference. Report any ambiguity at reliability thresholds. A separate implementation/review checks reactions, material and work identities, and the lag coefficient; checks are not external empirical validation.

Positive outcomes support only that particular installed mechanism, preparation, parameter regime, horizon and assay. Negative outcomes remain part of the model's predicted boundary. Even a favorable result cannot establish monotonic expansion of all possibilities, formation of new reaction laws, thermodynamic identification, or a universal trend toward 善.
