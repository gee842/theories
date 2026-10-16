# Recurrent inquiry, bounded reserves, and paid renewal

Mathematical working memo, 5 October 2026. AI-generated research assistance under Ren's research direction. The probability arguments below are applications of established ruin and absorbing-chain mathematics. Their contribution here is to make the funding, observation, and shutdown assumptions explicit; no mathematical originality or universal institutional law is claimed. This memo does not implement an experiment.

## 1. Resource accounting before a survival claim

Let \(R_t\in[0,B]\) be the liquid reserve available before inquiry period \(t\), with \(B<\infty\). A functioning inquiry service pays \(c_t\ge c>0\) before receiving that period's credited return \(A_t\ge0\). Provided the expense can be paid,

\[
R_{t+1}=\min\{B,R_t-c_t+A_t\}.
\tag{1}
\]

For the constant-cost case, define shutdown time \(T=\inf\{t:R_t<c\}\). The initial reserve is assumed to cover at least one period. Shutdown is absorbing only when no outside transfer, subsequent ordinary income, retained claim, or other institution can rebuild this inquiry function. Without that assumption, \(T\) is a first outage, not permanent extinction.

The credited amount is an allocation of resources, not itself their production. Let \(S_t\) be actual distributable output after the production expenses and prior obligations being modeled. A financially feasible allocation must satisfy

\[
0\le A_t\le S_t.
\tag{2}
\]

Inquiry expense, resources left for other uses, discarded or distributed overflow above \(B\), and any debt must appear in the accounting. A base allocation that costs nothing elsewhere would give its institution an extra resource source. Conversely, an output-funded base allocation is not an external subsidy merely because it is not credited to a new successful revision.

Payment timing matters. Equation (1) requires prefunding from the reserve. If output is available before inquiry, the affordability test instead includes that output. Neither convention may be changed silently when comparing funding rules.

## 2. Conditional shortfall theorem

**Claim.** Suppose shutdown is absorbing and there are an integer \(L\ge1\) and \(\epsilon>0\) such that, conditional on every surviving history at each block boundary, the probability of shutdown during the next \(L\) periods is at least \(\epsilon\). Then

\[
\Pr(T>nL)\le(1-\epsilon)^n,
\qquad \Pr(T=\infty)=0,
\qquad \mathbb E[T]\le L/\epsilon.
\tag{3}
\]

**Proof.** Conditional survival of each next block is at most \(1-\epsilon\). Taking conditional expectations gives
\(\Pr(T>(n+1)L)\le(1-\epsilon)\Pr(T>nL)\); induction proves the first inequality. Its limit proves almost-sure shutdown. Sum the survival probabilities in blocks to obtain the expectation bound. Independence, identical period returns, and a Markov assumption are unnecessary.

A sufficient resource mechanism is a uniformly possible reward-free block: with conditional probability at least \(\epsilon\), every inquiry that remains fundable during the next \(L=\lceil B/c\rceil\) periods receives \(A_t=0\). Repeated positive expenses exhaust the reserve within that block. This is a safe block length; a nonintegral \(B/c\) can cause shutdown earlier. The definition permits the service to stop within the block, so it does not require observations or attempted inquiries after shutdown.

For constant cost and a conditional probability at least \(p_0>0\) of zero credit at every still-operating step, the chain rule supplies \(\epsilon=p_0^L\). This lower bound must hold after adverse histories as well as typical ones. A positive unconditional probability of a zero-return period is insufficient: returns could alternate deterministically, or the system could enter a safe class where further long shortfalls are impossible.

The same argument applies when shortfall blocks have small positive funding: if costs exceed allocations by at least \(d>0\) throughout a sufficiently long block, reserve depletion follows. Thus replacing success credits by an output-funded base allocation does not by itself evade the theorem. It must remove or sufficiently change the relevant shortfall mechanism.

For horizon \(H\), the theorem gives the conditional lower bound

\[
\Pr(T\le H)\ge1-(1-\epsilon)^{\lfloor H/L\rfloor}.
\tag{4}
\]

It is a bound for the stipulated funding process, not an empirical forecast for an institution whose \(\epsilon\) is unknown. A tiny \(\epsilon\) can make the bound weak over every practically relevant horizon.

Uniformity can be relaxed. If block \(n\) has a history-uniform killing probability at least \(\epsilon_n\), then survival through \(N\) blocks is bounded by \(\prod_{n=1}^N(1-\epsilon_n)\). Divergence of \(\sum_n\epsilon_n\) suffices for almost-sure shutdown. Summable hazards need not force shutdown: independent killing events with summable probabilities below one have a positive chance of never occurring.

## 3. Positive average return is not a survival guarantee

Consider \(c=1\), \(B=2\), and independent credited returns 3 with probability one-half and 0 otherwise. Before reserve clipping, each operating period has expected net return \(3/2-1=1/2>0\). A success restores the reserve to two; two consecutive zero returns exhaust it. Therefore shutdown is almost sure.

With living reserve states ordered as \(1,2\), the substochastic transition matrix is

\[
Q=\begin{pmatrix}0&1/2\\1/2&1/2\end{pmatrix}.
\tag{5}
\]

Writing expected remaining lifetimes as \(e_1,e_2\) gives \(e_1=1+e_2/2\) and \(e_2=1+e_1/2+e_2/2\), so \(e_1=4\) and \(e_2=6\). The spectral radius is \((1+\sqrt5)/4<1\).

This does **not** exhibit positive drift of the clipped reserve in every state. At the ceiling, gains cannot increase its balance while losses can reduce it. Positive mean project returns and positive reserve drift are different claims. The overflow can be used elsewhere rather than destroyed, but it cannot protect this inquiry service unless the accounting permits it to return later.

More generally, let \(B=kc\), let every success reset the reserve to \(B\), and let independent failures have probability \(q\in(0,1)\). Shutdown is the first run of \(k\) failures. Starting at full reserve,

\[
\mathbb E[T]=\frac{1-q^k}{(1-q)q^k}.
\tag{6}
\]

One derivation writes the remaining-time recursions for the current number of consecutive failures and solves them backward. The mean grows exponentially with buffer size even though eventual shutdown remains certain. A union bound over candidate runs gives

\[
\Pr(T\le H)\le\max(0,H-k+1)q^k.
\tag{7}
\]

For example, the sufficient finite-horizon condition \(Hq^k\le\delta\) makes outage probability at most \(\delta\). Infinite-horizon ruin and strong practical reliability can therefore coexist. No comparison should report the former while suppressing the latter.

## 4. Finite killed-chain calculation

When cash is discretized and all retained environmental, proposal, validation, and policy variables have finite state, a fixed institutional rule induces a finite Markov chain. Let \(Q\) be its living-to-living transition matrix and \(\nu\) its initial row distribution. Then

\[
\Pr_\nu(T>n)=\nu Q^n\mathbf1.
\tag{8}
\]

If every reachable living state has a path of positive probability to shutdown, finiteness provides a common block length and positive killing bound. The living states are transient, \(\rho(Q)<1\), and

\[
N=(I-Q)^{-1}=\sum_{n\ge0}Q^n,
\qquad \mathbb E_\nu[T]=\nu N\mathbf1.
\tag{9}
\]

For a living-state vector of expected one-step expense or benefit \(g\), cumulative expectation before shutdown is \(\nu Ng\), with action and terminal costs included at the correct transition. These are standard absorbing-chain formulas; see Grinstead and Snell's [*Introduction to Probability*, section 11.2](https://math.dartmouth.edu/~prob/prob/prob.pdf), and the authored [Princeton exposition of the fundamental matrix](https://lips.cs.princeton.edu/the-fundamental-matrix-of-a-finite-markov-chain/).

A reachable closed living class invalidates the premise and may give positive survival probability. A continuous reserve, an unbounded archive, or a policy depending on the entire raw history does not automatically define a finite chain. Time-dependent finite-horizon rules instead yield products \(\nu Q_0Q_1\cdots Q_{n-1}\mathbf1\). Aggregating away a predictive state variable can also invalidate the proposed transition matrix.

For a controlled process, the theorem is uniform over policies only if its shortfall condition holds under every allowed policy. A controller permitted to avoid all costs indefinitely can preserve cash by ceasing inquiry; that is survival of an account, not continued provision of the inquiry service. Maintaining a duty to investigate requires a separately specified service criterion.

## 5. Why paying only for improvements can exhaust support after success

A separate deterministic mechanism does not require bad luck. Suppose one-time successful revisions monotonically raise an operating value \(V_t\le V_{\max}\), and the service is credited at most a multiple of each increment:

\[
0\le A_t\le\gamma(V_{t+1}-V_t).
\tag{10}
\]

Summation gives \(\sum_t A_t\le\gamma(V_{\max}-V_0)\). With initial reserve \(R_0\), recurring cost at least \(c\), and no other funding, the total number \(M\) of affordable inquiry periods satisfies

\[
Mc\le R_0+\gamma(V_{\max}-V_0).
\tag{11}
\]

The institution can improve successfully and still lose the means to investigate again. That conclusion depends on **one-time marginal credit**, bounded cumulative improvement, and a positive continuing expense. It does not apply to a retained royalty on continuing output, genuinely recurrent new opportunities with unbounded positive variation, or costless dormancy. In a changing environment, the sum of positive improvements can be unbounded even when \(V_t\) itself stays bounded; monotonicity cannot be omitted from this proof.

Real credits need not equal true improvements. An experiment may use (10) as an idealized accounting certificate, but an implemented funding authority should not silently observe the simulator's hidden causal effect or a same-case counterfactual. Observable revenue, paid randomized comparisons, and their explicitly noisy estimates are distinct possibilities.

## 6. A base allocation funded from actual output

Under the timing in (1), if actual distributable output satisfies \(S_t\ge c\) every period and the rule assigns \(A_t=c\), then a constant-cost service beginning with \(R_0\ge c\) never loses reserve. This is an invariant feasibility certificate. The output floor is a substantive premise, not supplied by the existence of a desirable inquiry function.

An elementary fair accounting comparison can give both rules the same actual output \(S_t=c+J_t\), where \(J_t\) is the observable successful-project receipt. A credit-only rule allocates \(A_t=J_t\); a base rule allocates \(A_t=c\). The rest remains available for other uses, subject to the same total accounting. Their different inquiry survival comes from allocation, not resource creation. The base has an opportunity cost, and survival alone does not prove that this allocation improves total welfare.

If production itself depends on inquiry, include the productive stock and its losses in the state. If \(S_t<c\) can persist with uniformly positive conditional probability for sufficiently long blocks, the paid base is also vulnerable. A base backed by finite inherited fuel likewise lacks an indefinite guarantee. The result identifies a condition for financial feasibility; it does not explain why a productive floor exists or certify the desirability of permanent inquiry.

External restart changes the mathematical object. A whole-system model must include the institution that pays rebuilding, the reserves or productive output from which it pays, and the time needed to restore the function. Positive recurrence with repeated outages is possible; describing that as either uninterrupted survival or permanent extinction would be incorrect. A recurrently productive replacement can preserve the function without preserving its original provider.

## 7. Endogenous proposals and valid evidence

A suitable local mechanism has participants receive noisy situated observations \(O_{it}\), form proposals by a declared finite mapping \(g_i(O_{i,0:t})\), and select a proposed policy for fresh validation. The funding authority sees only the specified proposal, evidence, output, and public traces. It does not receive the hidden best policy or a proposal guaranteed to be corrective.

For a validation outcome \(D_t\), a transparent observable credit rule can take the form

\[
A_t=\min\{S_t,\ a(D_t,\text{observed receipts},\text{public history})\}.
\tag{12}
\]

The shortfall theorem then asks whether this entire proposal-to-credit mechanism permits long runs of zero or inadequate allocation. Correct negative findings, no actionable proposal, a useful candidate missed by finite validation, and a harmful proposal rejected by validation can all give no success credit while consuming legitimate inquiry resources. Their relative probabilities must come from the model, not from labeling every nonpayment a failure of learning.

Fresh validation can make each adaptively nominated candidate's test conditionally valid, but a fixed per-period level \(\alpha\) is not an infinite-horizon familywise guarantee. If that guarantee is desired, a sequence of conditional levels with \(\sum_t\alpha_t\le\bar\alpha\) suffices by a union bound. Maintaining power as thresholds become stricter may require additional sample expense; finite reserves and perpetual reliability cannot be assessed independently of the statistical protocol.

Financial survival is also distinct from epistemic value. False proposals can receive observable receipts, true proposals can lack appropriable cash returns, and a well-financed institution can keep testing harmful or irrelevant policies. The experiment should report realized production, harms, false deployments, warranted rejection, and periods of working inquiry, rather than equating credited money or survival with successful coordination.

## 8. Scope and useful falsifying controls

The strongest defensible claim is conditional: a costly service with bounded accessible reserves and recurrently possible uncompensated shortfalls cannot operate forever without outage. This depends on a positive lower bound on expenses during required service, the reserve ceiling, the stochastic shortfall condition, and the lack of a replenishment route after shutdown. It is not a theorem that every success-funded research institution must disappear, that continuous inquiry is always needed, or that base funding is always preferable.

The informative controls remove these premises one at a time: allow reserves to grow without bound; make dormant capacity free; require inquiry only on finitely many occasions; provide actual recurring output sufficient for a paid allocation; permit an explicitly funded restart; eliminate sufficiently long shortfalls; or let their conditional hazards become summable. The comparison should also include an environment already understood, where expensive perpetual questioning can have negative net value.

For the implemented finite model, useful outputs are exact or simulated survival over the declared horizon, expected outage time, full paid expenditure, useful and harmful revisions, and the amount returned to other production or consumption. If a bounded-reserve simulation shows eventual collapse, the result should first be checked against the elementary shortfall theorem. Only differences unexplained by that accounting identity support a more specific claim about proposal formation, institutional evaluation, or sustained correction.

## 9. Audit of the implemented inquiry-renewal model

The inspected `experiments/inquiry-renewal/model.py`, `test_model.py`, and `PROTOCOL.md` implement a fixed inquiry procedure on independent new projects. Local counts select a candidate before fresh validation; an independent monitoring cohort produces an observable, noisy credit indicator. The latent orientation is not given to the procedure. Recognized credit earns an institutional award from ordinary output, not direct access to the simulator's hidden true benefit. The bounded-score telescoping theorem in section 5 is a separate mathematical module; this experiment instead has recurrent new opportunities and does not instantiate that theorem's monotone bounded score.

The reserve timing and killed matrix are consistent. A period is active when its opening balance satisfies \(b_t\ge c\). Its transition includes the current inquiry expense and any end-of-period award. For a zero floor, balances below \(c\) are absorbing and `transition[cost:, cost:]` is the living-state matrix. Its fundamental matrix counts the final paid active round that leaves the service unable to fund another. Starting from a living state, activity after \(H\) transitions equals \(\Pr(T>H)\), while summing opening-state activity over \(H\) rounds gives \(\mathbb E[\min(T,H)]\). There is no extra inquiry period hidden at shutdown. The code's block length \(\lceil B/c\rceil\) is conservative and valid for its integer-cost, integer-balance zero-floor cases.

I independently reran all six tests successfully. They check local proposal enumeration, fresh validation/monitoring, recognition versus evidence, per-project error scope, pathwise cash conservation, independently enumerated short reserve paths, the six-round lifetime certificate, and paid restart. Current project data are independent of the past determining opening reserves, so multiplying expected active-round count by the per-active expected operating gain, harm, and adoption probabilities is valid; no independence between the same round's gain and credit is assumed.

For the standard useful-project case, elementary rational enumeration gives

\[
r=0.373252459768706041529801022154661\ldots.
\tag{13}
\]

Thus the zero-floor rule has positive uncapped mean income \(5r-1\simeq .8662623\) per active round. With cap eight and initial reserve eight, an independent 70-digit Decimal linear solve gives \(\mathbb E[T]=98.60839117471514\ldots\). The implementation's probability of being active after 1,000 transitions is approximately \(2.01536\times10^{-5}\); its conditional-block upper bound is .049187, substantially looser.

The cap-32 control prevents an overstatement about practical risk. Its mean lifetime is \(1{,}112{,}450.713357362\ldots\) from the high-precision check, and its probability of activity after 1,000 transitions is .9991408105. The NumPy mean has relative error approximately \(5.25\times10^{-11}\), despite matrix condition number \(4.88\times10^6\); its linear residual is about \(2.33\times10^{-10}\). This verifies useful numerical precision while retaining the distinction between a finite-horizon result and almost-sure eventual shutdown. The high-precision audit used exact rational project probabilities and an independent Decimal elimination in memory; it changed no experiment code or saved results.

The floor-one rule is paid from the supplied six-unit output each round. From a zero balance it has one inactive round, then funds uninterrupted inquiry; hence 99 active rounds within a 100-round run. With a floor below expense, paid accumulation can instead produce intermittent restart, as the cost-two/floor-one control shows. Ordinary production persists even after the zero-floor inquiry account fails, so this is extinction of a funded inquiry function under its transfer rule, not extinction of the whole productive institution.

Finally, the constant-grant benchmark \(\mu=5r\) matches only the performance rule's nominal conditional mean grant during active rounds. It does not match capped deposits, total calendar-time allocation, lifetime expenditure, or grants after shutdown. It also uses the supplied exact stationary \(r\), so it is not a learned funding policy. Its main-case uninterrupted operation illustrates what smoothing can achieve at those prices, but it cannot be described as an equal-spending comparison or an isolated variance intervention for every parameter regime.
