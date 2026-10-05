"""Independent aggregation and ledger checks of the saved main results."""
from collections import defaultdict,Counter
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
rows=json.loads((HERE/'results/main.json').read_text())
control_groups=json.loads((HERE/'results/controls.json').read_text())
controls=[row for group in control_groups.values() for row in group]
summary=json.loads((HERE/'results/summary.json').read_text())
directions={'failure':(1,0,0,0),'recovery':(0,0,0,1),'expense':(0,1,0,0),
            'burden':(0,0,1,0),'failure_expense':(12,1,0,0),
            'failure_expense_burden':(12,1,4,0),'mixed':(4,1,1,4)}
groups=defaultdict(list);nested=defaultdict(dict);test_count=0;ledger_count=0
for row in rows:
    s=row['initial']
    assert set(row['probes'])==set(directions)
    for probe,r in row['probes'].items():
        v={key:Q(value) for key,value in r['metrics_exact'].items()}
        score=sum(w*v[n] for w,n in zip(directions[probe],('failure','expense','burden','unrecovered')))
        assert score==Q(r['support_value'])
        assert v['terminal_cash']+v['terminal_treasury']+v['expense']==s['cash']+s['treasury']+v['output']
        ledger_count+=1
        test_count+=int(v['tests']>0)
        groups[s['access'],s['stock'],s['belief'],probe].append(score)
        nested[s['stock'],s['cash'],s['belief'],probe][s['access']]=score
counts=Counter()
for (access,*_),scores in groups.items():
    assert len(scores)==6
    counts[access]+=int(len(set(scores))>1)
for values in nested.values():
    assert values['immediate']<=values['delayed']<=values['barred']
assert dict(counts)==summary['partition_sensitive_groups_out_of_63_per_access']
assert test_count==summary['main_probe_optima_using_paid_tests']==0
assert len(rows)==162 and ledger_count==1134 and len(nested)==378
assert len(controls)==30
assert (HERE/'model.py').read_bytes()==(HERE/'results/inputs/model.py').read_bytes()
out={'status':'passed','scope':'independent aggregation of saved outputs, not independent reoptimization',
     'main_states':len(rows),'ledger_and_probe_score_checks':ledger_count,
     'groups_each_access':63,'partition_sensitive':dict(counts),
     'access_order_comparisons':len(nested),'selected_optima_with_tests':test_count,
     'control_states':len(controls),'controls_by_label':{name:len(group) for name,group in control_groups.items()},
     'model_snapshot_matches_live':True,
     'main_json_sha256':sha256((HERE/'results/main.json').read_bytes()).hexdigest()}
(HERE/'audit_summary_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
