# Prospective preservation and admission of a question

5 October 2026. Exploratory exact finite calculation, written before this directory's first run. This is not a preregistered empirical study, an unrestricted discovery model, or a continuation of the preceding experiment's independent slow/fast transition law. All four mechanisms and the candidate are supplied to the modeler. The institution follows a fixed, observable procedure without receiving its world label.

## World and observation law

Independent episodes have four switch bits B. K=sum(B) has Binomial(4,1/4) distribution in every world. Conditional on K other than 2, words are uniform. At K=2, 0011 and 1100 together have probability q, split equally, and the other four words split 1-q equally. An independent fair endpoint Z is public; a fair initial state followed by B gives the equivalent joint law. Let d=sum(last two bits)-sum(first two bits).

| World | q | Next-switch probability r |
|---|---:|---|
| E: exchangeable, irrelevant order | 1/3 | 1/4 |
| P: clustered, predictive order | 1 | .45 if d>0; .05 if d<0; .25 otherwise |
| T: clustered, irrelevant order | 1 | 1/4 |
| U: exchangeable, predictive order | 1/3 | .45 if d>0; .05 if d<0; .25 otherwise |

Need Y has probability r for Z=0, 1-r for Z=1. A response costs .3 and perfectly prevents loss 1; effectiveness is a supplied structural assumption, not a causal effect estimated by the validation test. The incumbent responds exactly when Z=1. Its expected operating loss is .275 in all worlds. All worlds have identical joint laws of (K,Z,Y). E/U have identical entire historical laws; P/T also do. Whole episodes are independent conditional on the world. The world and task distributions remain constant during an episode and its independent audit, validation, and deployment cohorts.

## Chronology and cost

1. Before observing historical words or the later question, select m from 0 through 128. Retain full order in m independently selected historical windows, paying m*c_a. Routine K,Z records are common to every procedure; c_a pays the extra acquisition, retention, and reserved audit computation. Sampling cannot depend on observed order. This is one retention episode, not recurrent archive upkeep.
2. Q is revealed: with probability lambda it asks for continuation decisions; otherwise it asks a routine query entirely determined by K. Q is independent of the world and data. Extra order has no value for the routine query, whose common loss cancels. The continuation below occurs only for Q=1. Questions belong to a supplied two-question family, not an unforeseen language.
3. An audit-first procedure tests exchangeability using the retained order. Given J words with K=2, count X of 0011 or 1100 and reject when Pr[Bin(J,1/3)>=X]<=.05. No rejection for J=0. Sample size is fixed; there is no optional stopping or repeated testing. Rejection admits consideration of a supplied candidate, not deployment or a uniquely identified alternative.
4. An independent challenge flag can open validation if the audit does not: R=A+(1-A)*eta. For scalar expected loss this is affine in eta, so enumerating eta=0,1 suffices. Eta=1 makes positive m wasteful: retain m=0 as the direct-validation comparator. An ex ante randomized procedure chooses a workflow before data/Q/world; it is not a post-observation oracle.
5. If opened, fresh validation collects full order and the next Y for all L=1024 independent windows, costing L*c_v, including ineligible records. Every procedure operates the incumbent throughout a common fixed validation interval; its operating loss cancels. No free pilot outcomes are supplied. Only Z=0,d>0 cases enter the candidate test, selected before their Y is seen. Incumbent inaction makes their Y observable without treatment censoring.
6. The candidate adds response on Z=0,d>0. It otherwise preserves the incumbent. It pays f per future decision to obtain and interpret order, including ineligible decisions. Within the declared family q in [1/3,1], eligibility tau=(120+54q)/1024 >= tau_min=69/512. Test eligible need probability p against p_star=.3+f/tau_min using a fixed one-sided exact binomial test at .05. If p_star>=1, no acceptance is possible. This controls false acceptance of nonpositive NET deployment benefit, but does not certify recovery of sunk research costs. Validation sample and outcomes are independent of audit data conditional on world.
7. After validation, H=500 future decisions use the accepted policy or incumbent. All response costs, harm, record costs, and research expenses enter expected loss. Inquiry/record expense has a cap 6 on every realized branch (routine operation and response financing are separate). Maximum possible expense for audit-first is m*c_a+L*c_v+H*f; for direct validation it is L*c_v+H*f. Feasibility uses this conservative bound; all baseline m are feasible. No arm is described as spending the same realized amount as another.

## Exact targets and controls

Audit opening A_w(m) integrates J~Bin(m,27/128) and X|J~Bin(J,q). For q=1 it equals Pr[J>=3]. Validation power V_w integrates J_v~Bin(L,tau_w) and Y_count|J_v~Bin(J_v,p_w). Gross candidate improvement is Delta_w=tau_w*(p_w-.3). Expected incremental loss relative to the incumbent is

    C_w(m,eta;lambda) = m*c_a + lambda*R_w(m,eta)
                         * [L*c_v + V_w*H*(f-Delta_w)].

Products are evaluated conditional on world before averaging over priors. Baseline future question probability is .5; retain all five values in config. Exhaust every probability vector with denominator 10 over E,P,T,U, choosing among no inquiry, all feasible audit-first quotas, and direct validation. Store all world losses, all prior-grid decisions, and finite-workflow minimax-regret solutions with primal/dual residuals. A world-specific best workflow supplies the regret benchmark; this is not an oracle that bypasses validation or predicts every outcome. Randomization is permitted only ex ante. Optimality is restricted to this workflow class and fixed sample sizes, candidate, losses, and budget.

Controls: count/raw joint-law enumeration; exact audit size and q=1 power; E/T false validation and P/U power; true net-zero and test-threshold validation boundaries for q=1/3,2/3,1; all-paid cost decomposition; lambda=0 (no later continuation question); expensive and short-horizon cases; direct-validation comparator; a small independent multinomial enumeration of both tests; minimax LP primal/dual checks.

Code, protocol, config, tests, and analysis are copied byte-for-byte beside results with SHA256 hashes. Floating-point finite sums use SciPy; there is no Monte Carlo uncertainty or held-out empirical sample. Preserve failures and design revisions in the research log. Do not infer an empirical optimal audit quota, universal open-mindedness requirement, or ethical objective from these costs.
