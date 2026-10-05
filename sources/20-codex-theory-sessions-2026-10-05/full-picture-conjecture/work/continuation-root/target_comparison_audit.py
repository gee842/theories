"""Post-freeze analysis of saved independent target results only."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

BASE = Path(__file__).parent
data = json.loads((BASE/'target-outcomes.json').read_text())
metrics = ('failure','completion','expense','tests','restarts','terminal_cash','terminal_treasury')


def fiber_key(case, keep_policy=True):
    key = (len(case['jobs']), case['fault_prior'], case['initial_cash'],
           case['finance'], case['enactment'])
    return key+(case['policy'],) if keep_policy else key


def summarize(policies):
    fibers = defaultdict(list)
    for row in data['cells']:
        if row['case']['policy'] in policies:
            fibers[fiber_key(row['case'])].append(row)
    varying_failure = varying_vector = pairs = distinct_failure = distinct_vector = 0
    for rows in fibers.values():
        vectors = [tuple(Q(row['outcomes'][m]) for m in metrics) for row in rows]
        failures = [v[0] for v in vectors]
        varying_failure += len(set(failures)) > 1
        varying_vector += len(set(vectors)) > 1
        for a,b in combinations(vectors,2):
            pairs += 1
            distinct_failure += a[0] != b[0]
            distinct_vector += a != b
    return {'policies':policies, 'fibers':len(fibers),
            'failure_varying_fibers':varying_failure,
            'vector_varying_fibers':varying_vector,
            'queue_pairs':pairs, 'different_failure_pairs':distinct_failure,
            'different_vector_pairs':distinct_vector}


indexed = {(tuple(r['case']['jobs']),r['case']['fault_prior'],r['case']['initial_cash'],
            r['case']['finance'],r['case']['enactment'],r['case']['policy']):r
           for r in data['cells']}
ranking = defaultdict(list)
for row in data['cells']:
    c = row['case']
    if c['policy'] == 'serve':
        other = indexed[(tuple(c['jobs']),c['fault_prior'],c['initial_cash'],
                         c['finance'],c['enactment'],'restart_first')]
        gain = Q(row['outcomes']['failure'])-Q(other['outcomes']['failure'])
        ranking[fiber_key(c,False)].append({'jobs':c['jobs'],
                                          'failure_reduction_by_restart':str(gain)})
reversals = [{'coarse_state':list(k), 'comparisons':v}
             for k,v in ranking.items()
             if any(Q(x['failure_reduction_by_restart'])>0 for x in v)
             and any(Q(x['failure_reduction_by_restart'])<0 for x in v)]
witness = [indexed[(jobs,'1',3,'barred','enabled',policy)]
           for jobs in ((1,),(3,)) for policy in ('serve','restart_first')]
result = {'predictor_comparison':{k:data[k] for k in ('status','cell_count','coordinate_count','differences','prediction_sha256')},
          'primary_coarse_admissible_policies':summarize(['serve','restart_first','inspect_then_repair']),
          'supplementary_all_policies':summarize(['serve','restart_first','inspect_then_repair','deadline_aware']),
          'ranking_groups':len(ranking), 'ranking_reversal_groups':len(reversals),
          'ranking_reversals':reversals, 'selected_witness':witness,
          'scope':'Exact prospective synthetic composition check; deadline counterexample was anticipated. Policy4 uses omitted deadlines and is excluded from primary same-policy coarse-admissibility counts.'}
(BASE/'target-comparison-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='ranking_reversals'},indent=2))
