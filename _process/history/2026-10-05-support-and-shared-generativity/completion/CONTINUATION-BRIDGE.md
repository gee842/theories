# From a present preparation to delivered continuation

5 October 2026. AI-assisted formal bridge and fixed-model calculation. This implements the proposed continuation assay in the [opportunity audit](REGULATION-OPPORTUNITY-AUDIT.md). It changes the tested functions, not the earlier physical reactions or results.

## 1. Sequential joint event

For fixed H,tau>0 and (j,b,f,n) in {0,1}^4, define

\[
E_{jbfn}=\{J_H\ge j,\ B_H\ge b,\ F_H\ge f,
 B_{H+\tau}-B_H\ge n,\ A_s\ge1\text{ for }0\le s\le H+\tau\}.
\]

J counts recycling, B counts C assembly, F is freely available fuel and A=R+C+Y+YG is productive material. Intermediate free fuel and later delivered assembly are distinct coordinates of the same common test. A repeated function can be funded by useful stock or subsequent recycling. Each tested arrangement faces the same event semantics and time windows.

The original process keeps A=0 invariant. Hence its full path-survival requirement equals A_(H+tau)>=1. This simplification would fail in a model with paid restart from A=0; such a model must retain the path condition or redefine the task explicitly. The analyst's counter/window does not become a free mechanism for the actor.

## 2. Exact finite-chain proposition

Let Q be the row generator on the common augmented states (including the saturated historical flags), and let C contain only the nonnegative off-diagonal propensities of the labeled C-assembly events. These events change physical state, even when the historical B flag is already1. Set K=Q-C. It retains the full negative diagonal and therefore kills probability at the assembly hazard. Let h be the final productive-survival indicator, zero on the overflow state. Let D_(j,b,f) select the intermediate prefix test and A>0. From initial row distribution p0,

\[
\Pr_{\mathrm{cap}}(E_{jbf0})=p_0e^{HQ}D_{jbf}e^{\tau Q}h,
\tag{1}
\]

\[
\boxed{\Pr_{\mathrm{cap}}(E_{jbf1})=
p_0e^{HQ}D_{jbf}(e^{\tau Q}-e^{\tau K})h.}
\tag{2}
\]

The subscript cap denotes the packet-capped process. Formula(2) subtracts the surviving paths with no further assembly from all surviving paths. Historical assembly before H cannot satisfy the continuation requirement.

**Proof.** The Markov property at the deterministic time H supplies the common conditional future. In the killed chain, paths are removed precisely when a new assembly occurs, with every other event and the assembly waiting hazard unchanged. Thus e^(tau K)h counts no-further-assembly surviving paths. Subtraction gives exactly the desired event. The prefix selector charges the actual distribution produced by the same first stage; no separately optimized continuation is installed. ∎

An equivalent positive construction augments the future with a flag for the first later assembly. Its generator is

\[
\widetilde Q=\begin{pmatrix}K&C\\0&Q\end{pmatrix}.
\tag{3}
\]

Its rows sum to zero. Starting in the upper block after prefix selection and testing (0,h) at the end gives(2). Unlike the diagnostic block matrix used in the earlier Duhamel check, this matrix **is** a Markov generator. Duhamel's identity also gives the entrywise-nonnegative representation

\[
e^{\tau Q}-e^{\tau K}=\int_0^\tau e^{sK}C e^{(\tau-s)Q}\,ds.
\tag{4}
\]

The positive marked process is useful for independently checking numerical subtraction. Both formulas are exact for the declared finite chain; ordinary matrix-exponential software alone does not provide a roundoff enclosure.

## 3. Truncation, conditioning and capability interpretation

Couple the original process and the capped chain until the first overflow of U=F+GF. Treat overflow as assay failure, preserving its full incoming rate. For any of the sequential events,

\[
p_{\mathrm{cap}}(E)\le p_{\infty}(E)
\le p_{\mathrm{cap}}(E)+o_{\mathrm{cap}}(H+\tau)
\tag{5}
\]

in exact arithmetic. The bound uses overflow from the original preparation through the whole interval, not only through H. A finite arithmetic enclosure would have to bound the numerical calculation separately.

For the primary prefix J_H>=1,B_H>=1, the fuel selectors F_H=0 and F_H>=1 partition it. Their unconditioned joint-success probabilities therefore sum to the primary event (1,1,0,1). The entry states have been selected by the preceding dynamics. A difference between their conditional success ratios does not identify a causal effect of holding fuel.

If exact stopped joint and entry masses are p_c and q_c>0, their original conditional ratio can conservatively be bounded between p_c/(q_c+o_cap(H)) and min(1,(p_c+o_cap(H+tau))/q_c). These bounds follow by separately bounding numerator and denominator; the saved float ratios are labeled as stopped-chain descriptives instead. No conditioning is used to remove unsuccessful paths from the main comparison.

At a fixed reliability, the sequential profile set is a capability region for the one autonomous protocol. It is an inner bound for broader intervention classes. Probabilities for one repeated function do not establish inclusion of every possible future capability, indefinite persistence or moral goodness.

## 4. Prespecified calculation and result

The [protocol and complete results](../../../../experiments/shared-renewal-capability/continuation/README.md) evaluate H=tau in{0.25,1,3}; the two original g=1 catalytic preparations theta0/4; and all ten previously fixed regulator preparations at g4/8. Both caps 48/64 are retained. No controller or rate was tuned against these outcomes.

In the original g=1 pair, faster recycling increases the primary repeated-delivery probability at each tested horizon. This coexists with reserve-readiness losses. All 384 constructed-versus-absent sequential-profile comparisons remain numerically unfavorable. At g8,H3, the unregulated repeated-delivery probability is approximately 0.658551 while the responsive regulator gives 0.029666. Both start with no regulator and pay the declared costs.

The numerical result therefore closes one specific ambiguity: the old regulator's failure extends beyond a free-fuel assay to delivered continuation. It does not establish that every paid controller is harmful. A controller acting on a different competitive branch is a new architecture requiring its own mechanistic derivation and common-preparation comparison.

The [independent review](CONTINUATION-REVIEW.md) supplies a separate labeled-reaction reconstruction and marked-process computation. Such numerical agreement is distinct from a proof-assistant check, directed arithmetic or physical identification.
