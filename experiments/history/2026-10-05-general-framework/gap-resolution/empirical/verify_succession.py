"""Independent backward join from each actual next-round authority."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import csv
import hashlib
import json
import math
from scipy.stats import t

ROOT = Path(__file__).resolve().parent
source = ROOT/'data'/'Experiment_1.tab'
with source.open() as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
lookup = {(r['session'], r['subject'], int(r['period'])): r for r in rows}
assert len(lookup) == len(rows)
scores = defaultdict(list)
joined = {}
for successor in rows:
    p = int(successor['period'])
    if p == 1 or int(successor['z_isenforcer']) == 0:
        continue
    key = successor['session'], successor['subject'], p-1
    prior = lookup[key]
    z = int(prior['g_accuracy'])-int(prior['e_biginvestment'])
    y = int(successor['e_biginvestment'])
    scores[key[0]].append(Fraction((2*z-1)*(2*y-1)))
    joined[key] = z, y
means = {s: sum(v)/len(v) for s,v in scores.items()}
n = len(means)
avg = sum(means.values())/n
se = math.sqrt(float(sum((v-avg)**2 for v in means.values())/(n*(n-1))))
width = t.ppf(.975,n-1)*se
interval = [float(avg)-width,float(avg)+width]
saved = json.loads((ROOT/'results'/'succession_analysis.json').read_text())
r = saved['result']
assert str(avg) == r['exact_equal_session_estimate'] == '-1/342'
assert len(joined) == r['n_eligible_opportunities'] == 342
discrepancies = [abs(float(avg)-r['equal_session_estimate']),abs(se-r['session_standard_error'])]
discrepancies += [abs(a-b) for a,b in zip(interval,r['approximate_t95_interval'])]
for s in r['sessions']:
    assert str(means[s['session']]) == s['exact_estimate']
with (ROOT/'results'/'succession_joined_rows.csv').open() as f:
    published = list(csv.DictReader(f))
assert len(published) == len(joined)
for row in published:
    key = row['session'],row['subject'],int(row['current_period'])
    assert joined[key] == (int(row['z_higher_accuracy']),int(row['next_big_investment']))
assert max(discrepancies) < 1e-14
for path, field in [(source,'data_sha256'),(ROOT/'SUCCESSION-PROTOCOL.md','protocol_sha256'),
                    (ROOT/'analyze_succession.py','code_sha256'),(ROOT/'analyze.py','summary_dependency_sha256')]:
    assert hashlib.sha256(path.read_bytes()).hexdigest() == saved[field]
out = {'backward_joins_verified': len(joined), 'estimate_exact': str(avg),
       'interval': interval, 'max_difference': max(discrepancies), 'input_hashes_match': True,
       'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'limitation': 'The documented independent role reassignment assumption cannot be verified from endpoint records alone.'}
(ROOT/'results'/'succession_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
