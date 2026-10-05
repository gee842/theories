"""Independent H1/H2 implementation audit; imports only task-owned modules."""
import sys
sys.dont_write_bytecode=True
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import time

import model as candidate
import audit_oracle as oracle

HERE=Path(__file__).resolve().parent
assert Path(candidate.__file__).resolve()==HERE/'model.py'
engine=candidate.Engine(candidate.Config())

def to_oracle(s):
    return oracle.State(s.remaining,s.stock,s.cash,s.treasury,s.ready,s.belief,s.unlock)

def to_candidate(s):
    return candidate.State(s.t,s.x,s.b,s.treasury,s.ready,s.p,s.unlock)

def mode(s):
    return 'barred' if s.unlock==-1 else 'delayed'

def action_key(a):
    return a.support,a.test,a.repair_rule

counts=defaultdict(int)
seen=set()

def check_node(s):
    s=engine.normalize(s)
    if s in seen:return
    seen.add(s)
    os=to_oracle(s);om=mode(os)
    assert to_candidate(oracle.canonical(os,om))==s
    ca=engine.actions(s)
    oa=oracle.choices(os,om)
    assert tuple(map(action_key,ca))==tuple(map(action_key,oa))
    counts['nodes']+=1
    for a in ca:
        counts['actions']+=1
        tr=oracle.transition(os,oracle.Choice(a.support,a.test,a.repair_rule),om)
        for metric in ('expense','burden','tests','repairs','rebuilds','upkeep','inquiry_expense','output'):
            assert a.stage[candidate.INDEX[metric]]==tr[metric],(s,a,metric)
            counts['exact_stage_metric_comparisons']+=1
        actual=defaultdict(Q)
        expected=defaultdict(Q)
        for br in a.branches:
            actual[(br.signal,br.child)]+=br.probability
            assert br.expense<=s.cash
            assert br.child.cash+br.child.treasury+br.expense==s.cash+s.treasury+br.output
            counts['branch_ledgers']+=1
        for signal,pr,child in tr['branches']:
            expected[(signal,to_candidate(child))]+=pr
        assert actual==expected,(s,a,actual,expected)
        counts['exact_branch_distribution_comparisons']+=1
        for _,child in actual:
            check_node(child)

@lru_cache(None)
def independent_selected_evaluation(s,weights):
    """Follow candidate policy but evaluate only using independent events."""
    os=to_oracle(s);om=mode(os)
    os=oracle.canonical(os,om)
    if os.t==0:
        result={name:Q(0) for name in candidate.METRICS}
        result['failure']=Q(os.x==0)
        result['unrecovered']=Q(os.x<2)
        result['terminal_cash']=Q(os.b)
        result['terminal_treasury']=Q(os.treasury)
        return tuple(result[n] for n in candidate.METRICS)
    s=to_candidate(os)
    _,ai=engine.solve(s,weights)
    a=engine.actions(s)[ai]
    tr=oracle.transition(os,oracle.Choice(a.support,a.test,a.repair_rule),om)
    result=[tr.get(name,Q(0)) for name in candidate.METRICS]
    for _,pr,child in tr['branches']:
        cv=independent_selected_evaluation(to_candidate(child),weights)
        result=[value+pr*childvalue for value,childvalue in zip(result,cv)]
    return tuple(result)

started=time.perf_counter()
cases=[]
for horizon,x,b,r,p,access in product((1,2),(1,2,3),range(6),(0,1),(Q(0),Q(1,2),Q(1)),('barred','immediate','delayed')):
    s=candidate.make_state(horizon,x,b,5,r,p,access)
    ns=engine.normalize(s)
    check_node(ns)
    for name,weights in candidate.WEIGHTS.items():
        actual_values,_=engine.solve(ns,weights)
        independent_values=independent_selected_evaluation(ns,weights)
        assert actual_values==independent_values,(s,name,actual_values,independent_values)
        counts['independent_selected_policy_metric_vectors']+=1
        os=to_oracle(ns)
        expected_score,_,_=oracle.solve(os,weights,mode(os))
        actual_score=engine.score(actual_values,weights)
        assert actual_score==expected_score,(s,name,actual_score,expected_score)
        counts['independent_optimal_support_values']+=1
        # Ledger in exact selected-policy expectation, from original accounts.
        assert actual_values[10]+actual_values[11]+actual_values[1]==s.cash+s.treasury+actual_values[9]
        counts['expected_ledgers']+=1
    counts['initial_states']+=1

out={'status':'passed','runtime_seconds':time.perf_counter()-started,
     'scope':'base kernel H1/H2, all stock1..3, cash0..5 total5, ready0/1, prior0/half/1, barred/immediate/delayed, seven support directions',
     'counts':dict(counts),
     'candidate_model_sha256':sha256((HERE/'model.py').read_bytes()).hexdigest(),
     'protocol_sha256':sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest(),
     'oracle_sha256':sha256((HERE/'audit_oracle.py').read_bytes()).hexdigest(),
     'candidate_cache':str(engine.solve.cache_info()),
     'oracle_cache':str(oracle.solve.cache_info()),
     'limitations':'No independent H4 full optimization rerun; controls changing primitive parameters require separate kernel audit.'}
(HERE/'audit_compare_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
