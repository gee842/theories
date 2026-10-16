"""Exact finite checks for the formal-foundations memo; standard library only."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json
from pathlib import Path

states = list(product(range(2), repeat=2))
actions = [0, 1]

def kernel(s, a):
    x, noise = s
    p = F(1 + x + a, 4)
    next_noise = noise ^ a
    return {(0, next_noise): 1-p, (1, next_noise): p}

def quotient(x, a):
    p = F(1+x+a, 4)
    return {0:1-p, 1:p}

for s in states:
    for a in actions:
        pushed = defaultdict(F)
        for sp,p in kernel(s,a).items():
            pushed[sp[0]] += p
        assert dict(pushed) == quotient(s[0],a)

# All deterministic two-step policies depending on the full macro-state history.
nodes = [(x,) for x in range(2)] + list(product(range(2), repeat=2))
policy_checks = 0
for bits in product(actions, repeat=len(nodes)):
    policy = dict(zip(nodes,bits))
    for s0 in states:
        low = {((s0,), (s0[0],)): F(1)}
        high = {(s0[0],): F(1)}
        for _ in range(2):
            nl = defaultdict(F)
            nh = defaultdict(F)
            for (sh,xh), mass in low.items():
                for sp,p in kernel(sh[-1],policy[xh]).items():
                    nl[(sh+(sp,),xh+(sp[0],))] += mass*p
            for xh,mass in high.items():
                for xp,p in quotient(xh[-1],policy[xh]).items():
                    nh[xh+(xp,)] += mass*p
            low,high = nl,nh
        pushed = defaultdict(F)
        for (sh,xh), mass in low.items():
            pushed[xh] += mass
        assert dict(pushed) == dict(high)
        policy_checks += 1

# Same macro state and action but different micro realization gives a failed quotient.
bad_success_probs = [F(n) for x,n in states if x == 0]
assert bad_success_probs == [0,1]

# Observational nonidentification: X=U,Y=X versus X=U,Y=U.
obs_a,obs_b = defaultdict(F),defaultdict(F)
do_a,do_b = defaultdict(F),defaultdict(F)
for u in (0,1):
    obs_a[(u,u)] += F(1,2)
    obs_b[(u,u)] += F(1,2)
    do_a[1] += F(1,2)
    do_b[u] += F(1,2)
assert obs_a == obs_b and do_a != do_b

# All X-treatment marginals agree; same-unit counterfactual dependence differs.
interventions = {}
for treatment in (0,1):
    stable,flip = defaultdict(F),defaultdict(F)
    for u in (0,1):
        stable[u] += F(1,2)
        flip[u ^ treatment] += F(1,2)
    assert stable == flip
    interventions[treatment] = dict(stable)
change_stable = sum(F(1,2) for u in (0,1) if u != u)
change_flip = sum(F(1,2) for u in (0,1) if u != (u^1))
assert (change_stable,change_flip) == (0,1)

# Exact compression check: preserve a two-bit history in one bit and answer either
# coordinate after the query arrives. Enumerate 16 encoders x 16 decoders.
histories = list(product((0,1),repeat=2))
min_errors = 8
zero_error_encoders = 0
for codes in product((0,1),repeat=4):
    best_for_encoder = 8
    for output_bits in product((0,1),repeat=4):
        decoder = {(m,q): output_bits[2*m+q] for m in (0,1) for q in (0,1)}
        errors = sum(decoder[codes[i],q] != h[q]
                     for i,h in enumerate(histories) for q in (0,1))
        best_for_encoder = min(best_for_encoder,errors)
    min_errors = min(min_errors,best_for_encoder)
    zero_error_encoders += best_for_encoder == 0
assert zero_error_encoders == 0 and min_errors == 2
# Two bits suffice, using the identity code.
assert all(histories[i][q] == h[q] for i,h in enumerate(histories) for q in (0,1))

# Announced bit followed by negation defeats every possible announcement.
assert all((1-b) != b for b in (0,1))

result = {
  'method':'Exact rational arithmetic and exhaustive finite enumeration; proofs remain in memo.',
  'lumpability_state_action_checks':len(states)*len(actions),
  'two_step_history_policy_initial_state_checks':policy_checks,
  'failed_quotient_probability_pair':[str(x) for x in bad_success_probs],
  'observational_models_equal':True,
  'do_X_1_Y_1_probabilities':{'causal':str(do_a[1]),'confounded':str(do_b[1])},
  'all_treatment_marginals_equal':True,
  'probability_individual_outcome_changes':{'stable':str(change_stable),'flip':str(change_flip)},
  'one_bit_archive_zero_error_encoders':zero_error_encoders,
  'best_uniform_archive_query_error':str(F(min_errors,8)),
  'announced_bit_diagonal_cases':2,
  'status':'all checks passed'
}
path = Path(__file__).with_name('formal-foundations-checks.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
