# Retained evidence and changing worlds — protocol before execution

5 October 2026. This protocol is frozen before calculating the present comparison. It responds to the known fixed-size-replacement limitation in the earlier reopening study. It is a synthetic evidence-procedure test, not a new empirical experiment or a self-maintaining succession model.

## Shared physical family and work budget

Use exactly the earlier four expressions X1,1−X1,X2,1−X2, with independent fair binary attributes and physical harm `(action XOR true_expression(X)) XOR noise`, noise Bernoulli(.10). Each inquiry action is independently randomized fairly. The observed record is `(X1,X2,action,harm)`; define Y=harm XOR action, and two mismatch counts against X1,X2. The four hypothesis errors are `(e1,n−e1,e2,n−e2)`.

There are12 consecutive batches of5 fresh cases:60 inquiry cases in every arm, consuming60 case effort units and60 inquiry/record effort units. Every arm sees the same distribution of evidence, even after a certificate is obtained; no stopping savings are credited. Every inquiry has expected physical harm.50 and action-1 use.50, so the shared60-case inquiry budget entails expected30 harms and30 action-1 uses. These are inquiry costs, not costs eliminated by a more reliable declaration.

Two environments are fixed in advance:

1. Stationary: true expression X1 for all60 cases.
2. Changed: true expression X1 for cases1–30, then1−X1 for31–60. The shift is not announced to any procedure, and no procedure resets automatically at the shift.

Noise, context distribution and permissible actions remain otherwise unchanged. Data pooling after the shift violates the stationary single-hypothesis likelihood model by design.

## Three procedures

At each five-case batch boundary:

- **Latest-batch replacement:** discard previous mismatch counts, choose uniformly among the minimum empirical mismatch expressions in the latest5 records, and replace the incumbent declaration.
- **Cumulative replacement:** retain mismatch counts for every observed record, choose uniformly among minimum cumulative mismatches, and replace the incumbent declaration.
- **Cumulative sequential certificate:** retain the same cumulative counts. Declare h only if its likelihood is at least3/δ times each of the other three likelihoods, with δ=.05. With noise.10, likelihood ratio is9 to the power of the error-count difference, so all three gaps must be at least2. If no expression qualifies, retain the previous declaration; if none has ever qualified, remain undeclared. A qualifying expression is declared even if it matches the retained declaration; new false-declaration metrics include any qualifying wrong expression, while expression-change metrics count only changed labels.

All procedures begin without a declaration. None reads the actual expression or change time when selecting an expression. The exact known four-hypothesis response family and noise rate are assumptions of the certificate, not quantities validated by the computation.

## Finite calculation and metrics

Enumerate the full finite probability distribution at the12 batch boundaries in double precision, without trajectory sampling or probability pruning. Batch increments of true-attribute mismatch are Binomial(5,.10) before the shift and Binomial(5,.90) afterward; irrelevant-attribute mismatch is an independent Binomial(5,.50). Validate these increments against raw-case enumeration. For the latest-batch procedure retain only the current declaration and event flags; cumulative procedures retain both counts and the declaration/event flags. Ties use explicit random probabilities.

Primary metrics at each boundary: probability the retained declaration equals the current physical expression, probability it is wrong, probability still undeclared, probability of a **new wrong declaration at this boundary**, probability of at least one wrong declaration so far (relative to the physical truth when declared), and expected number of expression changes. Distinguish a formerly correct declaration becoming stale after the shift from a new false declaration. Report probability of retaining a wrong declaration without a fresh qualifying declaration at this boundary for the certificate arm. The before-shift endpoint at case30 uses X1; after-shift endpoints from35 onward use1−X1.

Report same data/work budget, endpoint counter sizes, and computation/retention assumptions. Two counts each need `ceil(log2(n+1))` bits for cumulative evidence, versus `ceil(log2(6))` for latest-batch counts, excluding shared labels, n/clock, machinery and declaration/event bookkeeping. No total physical cost is inferred from bit counts; repeated retention and likelihood computation require an operating substrate that is assumed available here.

Checks: state probability conservation, raw-case/batch mismatch equivalence, no oracle in decision functions, likelihood-gap/certificate consistency, exact standalone five-record accuracy agrees with the earlier mathematical result, stationary wrong-declaration probability respectsδ (a finite check, not the proof), old declaration retention under no certificate, same query count and explicit work/harm budgets, and preservation of the changed-environment limitation. Do not optimize the change time, batch size, horizon, δ or noise after seeing results.

## Formal question and safety boundary

Derive a time-uniform stationary false-declaration guarantee from likelihood-ratio martingales and Ville's inequality, and a separate summability result for cumulative empirical replacements. Distinguish finite sampled performance, eventual correctness under continued stationary evidence, and never making any wrong declaration. Neither guarantee supplies lawful exploration: at the original blind initial state, the two opposite target classes have harm expectations summing to1, so no blind response can meet both floors below.50. Randomized inquiry also has harm.50 in every context. No safe abstention/deferral option is included in that original operating repertoire. The study must not relabel epistemic assurance as whole-behavior safety or legitimate permission to conduct the experiments.
