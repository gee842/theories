# Model revision and inherited records: prior-art audit

5 October 2026. This memo evaluates a proposed joint experiment with paid history retention, inquiry capacity, and transmission. Its first benchmark is a symmetric binary Markov chain whose unknown switching probability is \(h\in\{.05,.45\}\). A legacy representation retains only the last state under a supplied known-\(h\) model; an expanded representation can use historical transitions to infer \(h\). No experiment is reported here.

The defensible distinction is **an observation about the past versus a recommendation conditional on a model of what persists into the present**. An accurate record can remain accurate while the policy once inferred from it becomes inappropriate. This neither establishes that history never recurs nor describes historians as uniformly assuming that it does. Indeed, both states of this benchmark recur almost surely under either of its transition laws. Learning can change the response to recurrence without preventing recurrence itself.

## Five primary precedents

**1. Robert, Cornuet, Marin, and Pillai (2011), [Lack of confidence in approximate Bayesian computation model choice](https://doi.org/10.1073/pnas.1102900108), [full arXiv v4 manuscript](https://arxiv.org/pdf/1102.4432v4).** Equation (1) shows that sufficiency within each candidate model need not imply sufficiency for comparing the models: the full Bayes factor can contain a data-dependent factor absent from the summary-based calculation. Their Poisson/geometric example also illustrates how an augmented summary restores joint sufficiency. This is a particularly direct antecedent of our claim that a summary adequate for an old question can lose evidence needed by an expanded model. It also blocks an overclaim that full raw records are always uniquely necessary. The June 2011 v4 manuscript was inspected; the publication title and DOI were checked separately.

**2. Gelman and Shalizi (2013), [Philosophy and the practice of Bayesian statistics](https://stat.columbia.edu/~gelman/research/published/philosophy.pdf).** Their published article distinguishes posterior inference within a model from checking that model against observations and revising its structure. They illustrate how discrepancies led to progressively expanded social-science models. This is a primary methodological argument and application, not a theorem that every archive should be retained or that Bayesian practice inherently excludes revision. It closely precedes the proposal to preserve evidence that can challenge the representation through which it was first interpreted. Sections 2–4 of the published article were inspected.

**3. Shalizi (2009), [Dynamics of Bayesian Updating with Dependent Data and Misspecified Models](https://arxiv.org/pdf/0901.1342v5).** Under Assumptions 1–7, Theorem 3 states that a positive-prior set whose essential infimum divergence rate exceeds the essential infimum over the whole hypothesis class loses posterior probability almost surely. Thus learning can concentrate on the best available approximation while the represented class remains wrong. The theorem has substantial likelihood, prior, and data-process conditions; it is not unrestricted convergence to truth. The inspected v5 is identified by the author as matching the journal version except formatting. This supplies a precise boundary on claims that more evidence alone corrects an inadequate model class.

**4. Pearl and Bareinboim (2011), [Transportability of Causal and Statistical Relations: A Formal Approach](https://ftp.cs.ucla.edu/pub/stat_ser/r372-aaai-corrected-reprint.pdf).** Selection diagrams specify permitted differences between source and target mechanisms. The S-admissibility result supplies conditional-effect transfer and, for pretreatment context, target reweighting. Other structures can prevent transfer. These conditions assume causal knowledge; historical records alone do not identify them. The corrected reprint, especially Theorem 2 and Corollary 1, was inspected.

**5. De Oliveira, [Blackwell’s Informativeness Theorem Using Diagrams](https://henriquedeoliveira588309899.wordpress.com/wp-content/uploads/2020/12/blackwells-informativeness-theorem-using-diagrams.pdf), author manuscript dated November 2017.** This primary proof of the established Blackwell theorem relates information comparisons to garbling and the decision rules that can be implemented. It supplies the right baseline: a full record can reproduce any fixed deterministic summary of itself, so its optimal gross decision value cannot be lower when extra information can be ignored and costs and feasible actions are held fixed. Strict benefit, affordable retention, useful timing, and value for a particular task require further analysis. The full manuscript was inspected in the preceding audit.

These sources support established mathematical and methodological foundations. A transparent joint resource-and-information example could still be useful, but priority should not be claimed for model-relative sufficiency, model checking, support restrictions, or transportability.

## Exact result for the proposed Markov benchmark

Let \(D=(X_0,\ldots,X_n)\) be a completely observed consecutive binary history, with a fixed known observation length \(n\). Conditional on a constant \(h\), let

\[
P_h(X_{t+1}\ne X_t\mid X_t)=h.
\]

Assume the initial-state distribution \(p_0\) is known and independent of \(h\). Define the number of flips

\[
K(D)=\sum_{t=1}^{n}\mathbf 1\{X_t\ne X_{t-1}\}.
\]

The history likelihood factorizes as

\[
P_h(D)=p_0(X_0)h^{K(D)}(1-h)^{n-K(D)}.
\]

Consequently, \(K\) is sufficient for inference about \(h\) in this family. For prediction from the current endpoint, retain \(T=(K,X_n)\), together with \(n\) if the length is not already public. The historical order beyond these quantities adds no information for this constant-\(h\) inference and prediction task. This is an elementary likelihood factorization, not a new sufficiency theorem.

With prior weights \(w_L,w_H>0\) on \(h_L=.05,h_H=.45\), the updated probability of the faster-switching law is

\[
q(D)=\frac{w_H h_H^K(1-h_H)^{n-K}}
{w_L h_L^K(1-h_L)^{n-K}+w_H h_H^K(1-h_H)^{n-K}}.
\]

The one-step probability of need, conditional on \(X_n=0\), is

\[
b_{n+1}=.05(1-q)+.45q.
\]

For \(X_n=1\), it is \(.95(1-q)+.55q\). In this two-point family, the posterior mean of \(h\) also uniquely determines \(q\), so it encodes the entire parameter posterior. For broader families, the mean alone generally does not suffice for multi-step prediction, learning, or control; retain the relevant posterior or sufficient statistics.

With equal prior weights and four observed transitions:

| History | Last state | Flip count | Posterior probability of \(h=.45\) | Next-step need probability |
|---|---:|---:|---:|---:|
| 00000 | 0 | 0 | .1009988825 | .0903995530 |
| 01010 | 0 | 4 | .9998476074 | .4499390430 |

Both histories produce the same known-\(h=.05\) one-step forecast, .05, when the legacy model is taken as given. Under the revised uncertain-\(h\) model, they recommend different actions if untreated need costs 10 and prevention costs 3: the action threshold is .3. A last-state-only representation cannot distinguish these histories; the count summary can, and performs identically to the full history for this model.

The relevant older claim is **predictive sufficiency under a supplied transition law**, not statistical sufficiency for estimating a parameter that the old model already fixes. Nor does last-state predictive sufficiency imply that the discarded sequence is useless for checking the adequacy of that law.

If \(X_0\sim\operatorname{Bernoulli}(1/2)\) independently of \(h\), then \(X_n\) is also marginally fair for either \(h\), so the endpoint alone supplies no information about \(h\). If \(X_0\) is instead fixed and known, the endpoint reveals the parity of the total number of flips and is informative:

\[
P_h(X_n=X_0)=\tfrac12[1+(1-2h)^n].
\]

A comparison must use that likelihood rather than pretending the last-state-only successor has no information at all.

### When the count-summary equivalence stops holding

The equivalence depends on the observation and model class. With diagnoses at irregular times \(t_i\), let \(\Delta_i=t_i-t_{i-1}\). The observed endpoints differ with probability

\[
p_h(\Delta_i)=\tfrac12[1-(1-2h)^{\Delta_i}].
\]

The likelihood therefore depends on changed and unchanged endpoints **by time gap**, not just their total count. Retaining timestamps or the relevant counts stratified by gap restores the appropriate likelihood for this model. Observation timing, selection rules, undetected failures, or transmission decisions can carry additional information. They must be included or explicitly rendered uninformative.

Likewise, if the expanded family allows \(h\) to change within the history, the locations of flips can matter. A count sufficient under every constant-\(h\) law need not suffice under that expansion. This does not make raw storage intrinsically superior: another summary may suffice for the particular larger family. The correct question is which distinctions an admissible future model or decision might need.

## Two exact boundaries on revision

### Conditioning cannot create prior support

For a finite or dominated model with likelihood \(L_D(\theta)\) and proper positive finite evidence denominator,

\[
\Pi(A\mid D)=
\frac{\int_A L_D(\theta)\,d\Pi(\theta)}
{\int L_D(\theta)\,d\Pi(\theta)}.
\]

Thus \(\Pi(A)=0\) implies \(\Pi(A\mid D)=0\). This is immediate from Bayes' rule. If an observation has zero marginal likelihood under the whole model, ordinary conditioning is undefined; it does not automatically specify a replacement model. The statement concerns null sets under the posterior's domination by its prior, not the misleading claim that continuous-parameter learning is impossible because each singleton has zero probability.

A literal prior assigning probability one to \(h=.05\) cannot learn \(h=.45\) by accumulating transitions. The experiment must distinguish three mechanisms: updating positive weights within the already represented two-point family; externally supplying an expanded family or revised prior; and actually generating the new alternative. Only the first is ordinary parameter learning. The proposed benchmark supplies the alternative and can test the inheritance required to evaluate it; it does not explain its discovery.

There is also a planning constraint. A predecessor who truly rules out every model revision need not value an archive for future revision. If an optimizing planner anticipates a probability of future model changes, that metamodel is part of its supplied information. Describe a known-\(h\) representation as a legacy or restricted comparator where appropriate; do not simultaneously give it no doubt and credit it with optimally purchasing protection against that doubt. When reanalyzing old data under the new family, do not use a posterior already based on that history as the prior and then count the same history a second time.

### No genuinely lossy summary preserves every possible future question

For a finite record space, suppose a deterministic summary \(S\) merges distinct histories \(d_0,d_1\). Consider two equally likely hypotheses that generate \(d_0\) and \(d_1\), respectively, and a decision asking which hypothesis generated the record under zero-one loss. The full record permits zero loss; observing only \(S\) leaves minimum expected loss \(1/2\). Therefore no noninjective summary preserves optimal performance for **all** possible model families and decision questions.

This is a simple information-loss construction, consistent with the classical comparison of experiments, not a novel universal law. Its scope is intentionally unrestricted. Restricting future questions can permit excellent or exact compression; acquisition and retention costs can make that compression preferable. Even a lossless archive preserves only what was recorded, not unmeasured context, discarded perspectives, or later concepts absent from the original observation interface.

## Historical transfer requires an invariance claim

One clean transport example uses pretreatment context \(Z\). If the relevant context-specific intervention response is invariant across past and present, and the causal conditions needed for the reweighting hold, then

\[
P_{\mathrm{now}}(Y\mid\operatorname{do}(a))
=\sum_z P_{\mathrm{past}}(Y\mid\operatorname{do}(a),z)
P_{\mathrm{now}}(z).
\]

Historical conditional findings can remain useful while their old aggregate recommendation fails because context changed. A changed response mechanism can invalidate the formula. Policy can itself alter subsequent experience; an old observational association is not thereby an invariant intervention response.

Our constant-\(h\) benchmark has a stable physical transition law and a changing representation of it. Do not describe it as simultaneously proving adaptation to arbitrary mechanism change, successful causal transport, and unforeseen model discovery. These are separate extensions.

## What the next experiment can contribute

The sharp first comparison is among an inherited action instruction, an inherited last-state observation, a correctly priced sufficient count summary, and a full record, with exact inference from all surviving public traces and silence. Under identical feasible responses and equal representation costs, the count-summary and full-record arms should have identical values in the stated constant-\(h\) benchmark. If they do not, inspect omitted metadata, different feasible policies, or a numerical error before interpreting a discovery.

Charge retention, transmission, and inquiry capacity separately. A cheaper summary can dominate full records in net value even when their gross information values coincide. Report costs and attainable decisions; do not identify record volume with inherited knowledge. To make sequence preservation useful, add a declared larger model family or future question for which transition locations matter, and retain an appropriately sufficient compressed comparator if one is known.

A resulting contribution would be an auditable account of **which inherited distinctions support a specified revision, when paying to preserve them changes action, and what their continued use requires**. It would not prove that historians are mistaken, that events cease to recur, that raw archives are always necessary, or that a legitimate social objective follows from predictive accuracy. Historical observation, model adequacy, present relevance, and the authority to act remain distinct claims.
