"""Check PROTOCOL.md predictions P1-P7 against results.json. Writes check.json."""
from pathlib import Path
import hashlib
import json
import statistics

HERE = Path(__file__).resolve().parent
receipt = json.loads((HERE / 'first-run-receipt.json').read_text())
raw = (HERE / 'results.json').read_bytes()
assert hashlib.sha256(raw).hexdigest() == receipt['results_sha256']
R = json.loads(raw)['results']


def vals(policy, test, key):
    return [R[policy][s][test][key] for s in sorted(R[policy], key=int)]


def mean(policy, test, key):
    return statistics.mean(vals(policy, test, key))


def summary(policy, test, key):
    v = vals(policy, test, key)
    return dict(mean=round(statistics.mean(v), 4), min=round(min(v), 4), max=round(max(v), 4))


P = {}
P['P1_self_only'] = dict(value=summary('self', 'train', 'met'), passed=mean('self', 'train', 'met') <= 0.1)
P['P2_proxy_capture'] = dict(proxy_excess=summary('proxy', 'train', 'excess'),
                             access_excess=summary('access', 'train', 'excess'),
                             passed=mean('proxy', 'train', 'excess') >= 0.5 and mean('access', 'train', 'excess') <= 0.1)
P['P3_access'] = dict(met=summary('access', 'train', 'met'), excess=summary('access', 'train', 'excess'),
                      rule_met=summary('record_rule', 'train', 'met'),
                      passed=mean('access', 'train', 'met') >= 0.9 and mean('access', 'train', 'excess') <= 0.1
                      and abs(mean('access', 'train', 'met') - mean('record_rule', 'train', 'met')) <= 0.05)
tr = mean('access', 'train', 'met')
P['P4_generalization'] = dict(
    new_claimant=summary('access', 'new_claimant', 'met'), large_claims=summary('access', 'large_claims', 'met'),
    identity_only_large=summary('access_identity_only', 'large_claims', 'met'),
    passed=abs(mean('access', 'new_claimant', 'met') - tr) <= 0.1
    and abs(mean('access', 'large_claims', 'met') - tr) <= 0.1
    and mean('access', 'large_claims', 'met') - mean('access_identity_only', 'large_claims', 'met') >= 0.2)
P['P5_missing'] = dict(missing_excess=summary('access', 'missing_records', 'excess'),
                       train_excess=summary('access', 'train', 'excess'),
                       passed=mean('access', 'missing_records', 'excess') > mean('access', 'train', 'excess'))
P['P6_forged'] = dict(access_withheld_forged=summary('access', 'forged_records', 'withheld_unmet'),
                      access_withheld_train=summary('access', 'train', 'withheld_unmet'),
                      proxy_excess_forged=summary('proxy', 'forged_records', 'excess'),
                      proxy_excess_train=summary('proxy', 'train', 'excess'),
                      passed=mean('access', 'forged_records', 'withheld_unmet') > mean('access', 'train', 'withheld_unmet')
                      and mean('proxy', 'forged_records', 'excess') >= mean('proxy', 'train', 'excess'))
fa = vals('access', 'scarce_symmetric', 'first_choice_A')
fs = vals('access', 'scarce_symmetric_swapped', 'first_choice_A')
extreme = [x for x in fa if x is not None and (x >= 0.9 or x <= 0.1)]
P['P7_symmetric_tiebreak'] = dict(first_choice_A=fa, swapped_first_choice_A=fs, extreme_seeds=len(extreme),
                                  passed=len(extreme) >= 7 and any(x >= 0.9 for x in extreme)
                                  and any(x <= 0.1 for x in extreme))

table = {}
for pol in R:
    table[pol] = {t: {k: summary(pol, t, k) for k in ('met', 'excess', 'retained', 'withheld_unmet')}
                  for t in R[pol]['0']}
out = dict(results_sha256=receipt['results_sha256'], passed_all=all(p['passed'] for p in P.values()),
           predictions=P, table=table)
(HERE / 'check.json').write_text(json.dumps(out, indent=1) + '\n')
for k, v in P.items():
    print(k, v['passed'])
