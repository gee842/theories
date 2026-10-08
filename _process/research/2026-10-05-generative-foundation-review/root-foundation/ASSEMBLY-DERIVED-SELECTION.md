# 从局部组装推出重建与选择

**Contact continuation completed at a narrower interface, 8 October 2026.** [Actual transmission and encounter reconstruction](CONTACT-RECONSTRUCTION-INTEGRATION.md) now derive the local rate from retained component contacts and rebuild a bond in each seed. The correspondence reuses this study’s attempt/success tree, not its terminal copying operation or offspring-count formulas. New variation and stage-aggregation restrictions qualify how a future population interface can be composed. The historical results and supplied premises below retain their original scope.

8 October 2026. AI-authored continuation following Ren's “继续”. This closes a specific part of the [previous reconstruction frontier](RECONSTRUCTIVE-SELECTION-INTEGRATION.md): an executable, supported assembly programme now determines the propagule column of the descendant matrix. Its reconstruction fraction and lost production are joint consequences of the same histories. **37 new Lean theorems / 57 new declaration audits pass; the full imported closure has 166 audits.** This is a conditional theoretical derivation, not a molecular model or an empirical superiority claim.

**核心结果：重建率与繁殖代价不能随意分别指定。成功得早的分支消耗较少、留下更多后继，因此一次发育成功的概率不等于后继中重建者的比例。可遗传规则若增加组装尝试，会同时改变这两者；是否获得选择优势，要由完整接续及真实消耗共同决定。**

## The local process and its inherited rule

A local state records available support, consumed support, whether a bond between two positions exists, and an inherited attempt limit n. The bond supplies a minimal organized relation. The installed rule permits at most n attempts, stops on success, and cannot proceed without support. Each actual attempt consumes one unit, including unsuccessful attempts. A paid rewrite can change the installed limit while debiting another support unit. Every admitted terminal history retains the resulting rule.

Successful bonding has a checked correspondence to the existing `DevelopmentalAssociation.aggregate` event on two positions. Failed paid attempts are a new declared operation. This is a partial correspondence for the successful event, **not an embedding of the whole programme in the earlier cellular model**: the old projection omits the new rule, and that cellular model has no failed-attempt operation. The local assembly route is not silently identified with daughter attachment during division.

The programme builds a finite tree of possible histories. Each unresolved attempt succeeds with supplied conditional probability p; the other branch has weight 1−p. For 0≤p≤1, the expectation operator has unit total mass and preserves nonnegative observables. It evaluates the actual terminal states, rather than assigning the desired descendant rates to the initial state.

Terminal reproduction follows an explicit copying law: each remaining support unit and one precursor unit produce one descendant census unit, carrying the installed rule and the terminal organized/unorganized state. A precursor unit means one whole modeled descendant unit; this is not an identified molecule or a conserved count of individual cells. The batch operation accounts for used support and unused precursors. With B support and B precursor units initially allocated, all terminal branches can execute this operation, including the zero-offspring branch. The original pair's material is not an extra offspring credit.

This copying law, the unit work cost, the initial stocks and the local success law are premises. The contribution is their joint, restricted consequence across inherited attempt limits. The process does not explain biochemical synthesis, measurement of success, mutation supply or continuing provision. These are differentiated relations within one history, not an independent organism acting on a fundamentally separate environment.

## What the history determines

For an initially unlinked state with B support units, define:

- C_n: expected support consumed by assembly;
- S_n: probability that assembly has succeeded at the terminal state;
- A_n and D_n: expected numbers of organized and unorganized descendants.

The biological interpretation uses integer 0≤n≤B. The algebraic recurrences are rational; evaluating them outside the supported domain does not describe a realizable negative stock. Lean proves, by evaluation of the finite tree,

\[
\begin{aligned}
C_{n+1}&=1+(1-p)C_n,&C_0&=0,\\
S_{n+1}&=p+(1-p)S_n,&S_0&=0,\\
A_{n+1}(B)&=p(B-1)+(1-p)A_n(B-1),&A_0(B)&=0,\\
D_{n+1}(B)&=(1-p)D_n(B-1),&D_0(B)&=B.
\end{aligned}
\]

The recursion stops immediately after a successful attempt. It therefore does not charge every history the maximum n attempts. The checked identities are

\[
A_n+D_n=B-C_n,\qquad S_n=pC_n,\qquad
D_n=(1-p)^n(B-n),\qquad S_n+(1-p)^n=1.
\]

Thus neither total production nor reconstruction can be selected independently after choosing the programme. A revision to n changes the admitted histories and both outputs. A paid rewrite also changes B; the rewrite theorem explicitly evaluates the new rule with the remaining budget, not with the old budget restored.

## The reconstruction fraction must be weighted by actual descendants

Let T_n=A_n+D_n>0. The fraction entering the organized stage is

\[
r_n=A_n/T_n.
\]

It generally differs from S_n, the fraction of developmental histories that succeed. The checked joint-output identity is

\[
A_n-S_nT_n=(1-S_n)(n-C_n).
\]

The right side is nonnegative for 0≤p≤1 because C_n≤n. Successful histories can finish early and contribute more offspring than late failures. Multiplying success probability by average output discards this dependence. For B=3, n=2 and p=1/2, success occurs with probability 3/4, but 5/6 of expected descendants are organized. Neither number is a quantitative-genetic heritability coefficient.

A separate kernel-checked example gives **opposite signs for the growth test** when S_n is substituted for r_n while preserving total expected output. This limits the rival that averages success and production independently. A conventional model preserving the joint history obtains exactly the same correction; the result is not a refutation of conventional probability or life-cycle theory.

## From the programme to selection

For the simplest alternating life-cycle slice, an organized unit produces F unorganized census units, while a propagule executes the assembly programme. F remains supplied; organized-stage production and the absence of direct O-to-O offspring have not been derived here. In the notation of the earlier study, q=0. With a positive reference growth factor lambda,

\[
K_n=\frac1\lambda
\begin{pmatrix}0&A_n\\F&D_n\end{pmatrix},
\qquad g_n=T_n/\lambda,\quad r_n=A_n/T_n.
\]

The checked `effective_kernel` equality recovers the previous developmental matrix with f=F/lambda and q=0. The entire P column is now computed from the programme. The earlier theorem supplies the exact expansion criterion, for F,A_n>0 and D_n<lambda:

\[
J_n:=FA_n+\lambda D_n-\lambda^2>0.
\]

The new composition theorem gives a positive weighting and geometric lower bound at every finite population time when the derived kernel remains appropriate. It uses the actual nonnegative outputs of the finite tree. It does not infer an infinite supply of new budgets from a finite assembly account; repeated identical stock allocation remains a condition on applying the population recurrence.

For one additional allowed attempt, Lean proves

\[
J_{n+1}-J_n=(1-p)^n
\left[(F-\lambda)p(B-n-1)-\lambda\right].
\]

For p<1, the sign is determined by the bracket. This expression separates the remaining production that successful reconstruction redirects from the support lost on the added attempt. It is a derived consequence of the local programme, not an independently installed reward function.

**A genuine local invasion comparison requires the resident factor.** If the n-attempt resident satisfies J_n=0, the stage vector (lambda−D_n,F) is checked to reproduce by factor lambda. It is positive when F>0 and lambda>D_n. Under the positive-return and subcritical P conditions for the mutant, the n+1-attempt variant has a strict expansion certificate exactly when

\[
(F-\lambda)p(B-n-1)>\lambda.
\]

This is a deterministic rare-lineage invasion condition in the fixed resident context. An arbitrary reference lambda, or a larger J alone, is not a proof that one resident displaces another. The model does not establish stochastic establishment probability, fixation or later ecological feedback. A checked witness uses p=1/2, B=4, F=18 and lambda=6: the one-attempt resident is at its growth factor and the two-attempt variant has a strict expansion certificate.

## More reliable reconstruction can lose its advantage

The final supported attempt offers a general adverse result. When B=n+1, 0<p<1 and lambda>0, allowing that last attempt increases S but strictly lowers J. If that attempt succeeds, it leaves no support for descendants. If it fails, it still consumes the last unit. This conclusion does not depend on a particular favorable F.

For a concrete checked reversal, take p=1/2, B=3, F=11 and reference lambda=15/4:

| Attempt limit | Success probability S | Expected assembly cost C | Organized output A | Unorganized output D | Descendant reconstruction fraction r | J |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1/2 | 1 | 1 | 1 | 1/2 | 11/16 |
| 2 | 3/4 | 3/2 | 5/4 | 1/4 | 5/6 | 5/8 |
| 3 | 7/8 | 7/4 | 5/4 | 0 | 1 | −5/16 |

The first rule has a checked expansion weighting. The three-attempt rule fails the positive-margin condition despite a higher success probability and r=1. In the latter case, failed histories leave no offspring at all; a perfect fraction among surviving offspring does not imply adequate total replacement. This fixed-reference example is distinct from the resident-bound invasion example above. No optimum growth strategy is inferred by maximizing J at an arbitrary reference.

## What has been explained and what remains supplied

| Earlier free input | Replacement in this study | Remaining premise |
|---|---|---|
| Propagule output g | Terminal offspring counts from paid histories | Initial B, unit cost, copying/production law and reference factor |
| Reconstruction fraction r | Organized offspring divided by total offspring, preserving joint history | Conditional success probability p and faithful rule/state copying |
| Independent reconstruction cost | Expected count of actual paid attempts | The cost per attempt and whether the supplied programme describes the system |
| Criterion for an additional attempt | Derived resident-relative invasion inequality | Resident context, permitted rule change and no unrepresented density or mixing effects |

This closes the finite assembly-to-population connection on the stated slice. It does **not** complete a molecular derivation of all coefficients or a minimal assumption-free foundation. The informative restriction is that a single programme constrains several outcomes across changes of n. Counting parameters alone would not establish greater explanatory economy: this programme supplies structure absent from a free-rate matrix, and that structure needs independent justification.

## Strong comparison and primary reading

Pichugin and Traulsen's [2020 life-cycle model](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008406) already represents costs of fragmentation through delay, risk or loss and derives consequences for life-cycle selection. This is an appropriate strong comparator. Our finite stopping programme is a narrower, different mechanism; it is not a replication or improvement of their model. The [preserved source](../../../../sources/evolutionary-selection/reconstructive-selection/README.md) records this round's rereading of the model and cost definitions.

Three comparisons have different outcomes. The previous free-rate matrix is recovered on the computed slice. The approximation that multiplies separate average success and output can give the wrong growth sign. The equally informed conventional finite-tree or branching-process account gives the same expectations and threshold. We have a demonstrable gain over the lossy approximation, and a completed internal derivation; we have not demonstrated a gain over the strong mechanistic rival.

The earlier [2018 collective-heritability comparison](RECONSTRUCTIVE-SELECTION-INTEGRATION.md#strong-comparative-assessment), [2024 scaffold stability assessment](EVOLUTIONARY-ORGANIZATION-INTEGRATION.md) and [connectionist learning recovery obligation](EVOLUTION-THEORETICAL-INTEGRATION.md#5-what-theoretical-completion-still-requires) retain their separate meanings. This study introduces no new empirical observations or measured rates.

## Formal verification and correspondence

[AssemblyDerivedSelection.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/AssemblyDerivedSelection.lean) imports the actual reconstruction threshold and developmental-association modules. The [fresh-build receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/assembly-derived-selection-verification/verification.json) records 37 new theorems and 57 new audits, with 166 audits including imported declarations. It compiles source snapshots in an isolated directory with Lean 4.29.1, rejects placeholders and custom axioms, reports standard logical dependencies and binds sources, checker and logs by hashes. The 28 earlier threshold theorems are reused, not recounted as new results.

The proof checks local conservation, terminal production and rule retention, successful-event correspondence, normalization and positivity of finite weights, exact tree expectations, joint-output identities, selection correspondence, resident-relative invasion and adverse witnesses. These proof claims do not certify the biological applicability of p, B, F or the copying law. The [integration checks](ASSEMBLY-DERIVED-SELECTION-CHECKS.json) separately bind the documents and indexes; they are not independent scientific review.

## Author counterreview and the next unresolved connection

**Is r merely renamed p?** No. The tree derives r from both success timing and descendant production. The checked cases r=5/6 with p=1/2 and S=3/4, and r=1 with S=7/8, rule out that identification. p remains a local primitive whose physical derivation is still open.

**Does the terminal copying law hide the desired result?** It is a strong assumption: a successfully formed relation is copied to descendants. We explicitly model that operation and its stocks, but have not derived its chemistry. The calculation is informative within this law because it constrains cost and output jointly; changing the production mechanism can change the selection condition. Generalizing to different yields from successful and failed branches is a substantive extension, not an automatic theorem here.

**Are actual stochastic lineages proved to expand?** The finite tree has normalized nonnegative weights under the probability bounds. The population result concerns the induced deterministic expected-count recurrence under its supplied context. Individual lineages may still die out. No unproved branching-process survival theorem is used.

**Can current success prove the evolved rule is good?** No. These results concern reproductive continuation. Their relevance to generative alignment is to identify how costly capacities for reconstruction may be retained or eroded. Applying the programme to evaluation or concern requires a separate correspondence, and G0 plus the practical commitments continue to supply the stated ethical grounds.

**The next frontier is the law of successful assembly and copying itself.** The current model explains how an inherited stopping rule changes a complete descendant column. The remaining derivation must let formed contacts or component states change p and the production/copying relation, while retaining the joint histories and their costs. It should test which new independently supported restriction follows. The named connectionist recovery remains open; repeating the now-completed finite assembly derivation is not the next task.
