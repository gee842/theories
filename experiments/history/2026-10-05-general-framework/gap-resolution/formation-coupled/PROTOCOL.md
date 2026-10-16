# Finite formation and succession join — protocol before execution

5 October 2026. Frozen before numerical execution. This is a synthetic finite-kernel calculation, not external causal validation. No parameter search is planned. The model joins mechanisms previously analyzed separately; numerical results will be reported regardless of sign.

## Environment and independent outcomes

- Horizon 25 rounds; inquiry batch size 5; physical response noise ν=.10.
- Each case independently draws two fair binary attributes. The physical correct action is X1 (j=1,θ=0). Harm is `(action XOR correct_action) XOR Bernoulli(.10)`. The learner is not supplied j or θ.
- Independent outcomes: four context-conditional expected harm rates, actual realized case harms, and action-1 burden. Prospective plural commitments require each expected harm≤.20 and expected action-1 burden≤b. These are expected response constraints, not guaranteed zero harm or pathwise quotas.
- Main proposed burden ceiling b=.45; infeasible proposal control b=.40. The formation model's analytic minimum burden is7/16. Every candidate's own assumed response model yields this same feasibility boundary; acceptance never reads whether the candidate is physically correct.

## State and initial condition

State `(k,q,c,ell,e1,e2,f,v)` has skill carriers k∈{0,1,2}, installed practice q∈{volume,adaptive}, a pending complaint c∈{0,1}, batch progress ell∈{0,…,4}, two mismatch counts, installed expression f∈{none,X1,1−X1,X2,1−X2}, and ratified plural commitment v∈{0,1}. The finite batch length and counters make the process Markov. Initial state is skill2, adaptive, no complaint, empty counts, no frame, unratified proposed commitments.

The initial public assessment records pooled harms and burden. Ratification adds the four separate group ceilings and the proposed burden ceiling. The proposal and ratification rule are declared normative assumptions, not inferred ethical truths. The model does not claim that this ratification rule is a complete account of goal formation.

## Work and transition order

Every round has exactly two effort units; unused inquiry allocation is not quietly available for extra ordinary work.

1. **Choose the portfolio using actual state.** Volume performs F: two ordinary cases. Adaptive at skill1 performs T: one ordinary case plus one training slot, adding a carrier before turnover. Adaptive at skill2 with a pending complaint and no installed frame performs Q: one randomized experimental case plus one inquiry/record slot. Otherwise it performs F. At skill0 only F is implementable. If training is blocked, the attempted T instead becomes F, with no training or inquiry. Q requires skill2.
2. **Execute cases.** Ordinary action is0 unless a frame, ratified commitment, positive skill and execution authority are present. Enabled conditional action uses the installed expression to predict the needed action. In its predicted-one class it chooses action1 with probability7/8; otherwise action0. Q uses an independent fair randomized action. All harms follow the actual physical response law. Training and inquiry each displace one ordinary case relative to F; Q's experimental case and its outcomes are counted separately from ordinary service.
3. **Complaint and inquiry.** Each actual harm independently generates an admitted complaint with probability.5. A previous complaint remains pending. Q increments its sample count; linked records increment mismatches of X1 and X2 against `(harm XOR action)`. At five records, the linked institution nominates uniformly among the smallest of `(e1,5−e1,e2,5−e2)`. The aggregate-only institution paid the same inquiry work but cannot use X links and nominates uniformly among all four expressions. The batch counters then reset, and the selected frame is admitted. The fixed authority to admit this supplied grammar is assumed in all arms.
4. **Ratify with available claims, not analyst truth.** A nominated candidate is ratified if its own supplied response family says all proposed ceilings can be met. This holds for b=.45 and fails for b=.40. The rule assumes the specified participants' endorsements, not a truth oracle. An incorrect frame can therefore be ratified and fail actual constraints. When b=.40, the candidate remains represented but the proposal stays unratified; the institution does not invent a relaxation.
5. **Outcome-dependent turnover.** After cases and any training, turnover has probability `.05+.20*(realized harms/number of cases)`, hence lies in[.05,.25]. It removes one carrier if present. Conditional on turnover, a successor is adaptive with probability `k_post*w_q/(1+k_post*w_q)`, with w_adaptive=4 and w_volume=.25, using the preceding installed practice q. These are inherited appointment weights, not a global welfare score.
6. **Transmission.** On turnover, the inquiry archive, complaint record, frame/interpreter, and commitment record are transmitted jointly with probability.90. Otherwise all are erased. At skill0 this package is unusable and is set empty; skill0 is absorbing, with no external entrant or immortal teacher. Both partial inquiry and an installed frame can be lost. The successor need not reproduce the work needed to regain them.

Fresh context and response noise are redrawn each case, but j,θ,ν stay fixed throughout all batches. Outcome-dependent attrition, interruptions and archival loss are inside the same transition kernel. No product of separately measured marginal success probabilities is used.

## Arms fixed before results

1. **Linked/main:** the specified kernel, b=.45.
2. **Aggregate:** same work requirements and gates, but attribute-to-outcome links unavailable to nomination. Realized cumulative work may subsequently differ because outcomes and succession feed back; this is matched cost per portfolio and inquiry episode, not forced matching of post-treatment work totals.
3. **Execution blocked:** linked discovery/ratification, but ordinary response always action0.
4. **Training blocked:** T unavailable as described above.
5. **Infeasible burden:** linked, b=.40.
6. **Protected succession benchmark:** linked/main physical turnover retained, but every positive-skill successor is adaptive and the package is always transmitted. This bundles protected selection and retention and is explicitly exogenous; it is not a pure appointment treatment or a solution to preserving that protection.

## Computation and metrics

Enumerate the entire reachable finite transition distribution each round in double precision, aggregating identical successor states; do not sample trajectories. Retain positive branches without a pruning threshold. Cache transitions and report roundwise mass error and maximum reachable state count. Sum branch probabilities, not naive gate products.

Primary endpoint: probability at round25 of an actually enabled policy satisfying every proposed expected harm ceiling and burden ceiling under the physical environment. Also report skill-positive probability, frame-present probability, exact-correct-expression probability, ratified-commitment probability, probability of ratification with actual constraints violated, expected skill count, expected cumulative ordinary cases, inquiry cases/slots, training slots, actual harms and action-1 uses, turnovers, archive erasures, and nominations. Report roundwise endpoint curves and all six arms.

Checks: state/probability validity, mass conservation, physical group outcome profiles, candidate-only ratification, inquiry mismatch law, exact standalone nomination probability versus FORMATION.md, two effort units per round in all arms, inability to execute without the stated package, zero protected-benchmark skill loss, zero true plural success when burden is infeasible or execution blocked, and failure/survival relationships. Any failed check or numerical issue is retained and repaired transparently; comparisons are mathematical interventions in a supplied model, not empirical effects.
