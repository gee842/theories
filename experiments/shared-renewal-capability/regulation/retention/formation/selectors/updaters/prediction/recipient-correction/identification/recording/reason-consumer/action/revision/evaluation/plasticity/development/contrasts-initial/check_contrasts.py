"""Compare saved, independently reconstructed histories; no simulator execution."""
from copy import deepcopy
from pathlib import Path
from fractions import Fraction
import gzip,json,hashlib
HERE=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def paths(data,case,arm,prod):return data['cases'][case]['variants'][arm]['producers'][prod]['paths']
def physical(state,ignore_sign=False):
    s=deepcopy(state)
    # Only the declared finite recipe choice differs in a matched control.
    s.pop('controls')
    if ignore_sign:
        for x in s['links']+s['retired']:
            if x is not None:x['sign']='declared_conductance_difference'
    return s

def training_prefix(row):
    trace=row['runtime_trace'];cut=next((j for j,r in enumerate(trace) if r['event']=='evaluation.assess'),len(trace))
    return trace[:cut]

def verify(data):
    counts=dict(conventional_histories=0,conventional_states=0,matched_histories=0,matched_prefix_states=0,
        fixed_marginal_endpoints=0,revision_histories=0)
    comparisons=[]
    for case in ('aligned','opposed','mixed','aligned_revision'):
        for prod in ('variable','conventional','fixed_normal'):
            aa=paths(data,case,'active',prod);cc=paths(data,case,'conventional',prod)
            assert len(aa)==len(cc)
            for a,c in zip(aa,cc):
                assert a['predecessor_ref']==c['predecessor_ref'] and a['probability']==c['probability']
                assert len(a['runtime_trace'])==len(c['runtime_trace'])
                for x,y in zip(a['runtime_trace'],c['runtime_trace']):
                    assert x['event']==y['event'] and physical(x['state'])==physical(y['state'])
                    counts['conventional_states']+=1
                assert a['metrics']==c['metrics'];counts['conventional_histories']+=1
    for case in ('aligned','opposed','mixed','aligned_revision'):
        controls=('frozen_sign',) if case=='aligned_revision' else ('inert','identity_gated')
        for arm in controls:
            eligible=Fraction(0);choice_difference=Fraction(0)
            for prod in ('variable','conventional','fixed_normal'):
                for a,c in zip(paths(data,case,'active',prod),paths(data,case,arm,prod)):
                    assert a['predecessor_ref']==c['predecessor_ref'] and a['probability']==c['probability']
                    ta,tc=training_prefix(a),training_prefix(c)
                    assert len(ta)==len(tc),(case,arm,a['predecessor_ref'])
                    for x,y in zip(ta,tc):
                        assert x['event']==y['event']
                        assert physical(x['state'],True)==physical(y['state'],True),(case,arm,x['event'])
                        counts['matched_prefix_states']+=1
                    counts['matched_histories']+=1
                    if case=='aligned_revision':counts['revision_histories']+=1
                    if prod=='variable':
                        if a['metrics']['training_complete']:eligible+=Fraction(a['probability'])
                        if a['metrics']['assessment']!=c['metrics']['assessment']:choice_difference+=Fraction(a['probability'])
            comparisons.append(dict(case=case,control=arm,variable_completed_training_mass=str(eligible),
                variable_choice_difference_mass=str(choice_difference)))
    for prod in ('variable','conventional','fixed_normal'):
        base=paths(data,'aligned','active',prod)
        for case in ('opposed','mixed'):
            for a,b in zip(base,paths(data,case,'active',prod)):
                assert a['predecessor_ref']==b['predecessor_ref']
                sa=training_prefix(a)[-1]['state'];sb=training_prefix(b)[-1]['state']
                # Across different recipient pairings only endpoint totals, own
                # teaching and inherited knowledge are matched, not X trajectories.
                for key in ('core','physical','binding','native','reserves','costs'):
                    assert sa[key]==sb[key],(prod,case,key)
                assert sa['packets']['own']==sb['packets']['own']
                assert sum(sa['packets']['recipient'])==sum(sb['packets']['recipient'])
                counts['fixed_marginal_endpoints']+=1
    return dict(status='saved_history_contrasts_passed',counts=counts,comparisons=comparisons,
        scope='Full matched pre-assessment histories differ only in declared recipe and link conductance. Conventional counterparts match every event/state/metric modulo implementation recipe tag. Across distinct X words, only listed endpoint quantities are equated; recipient paths and source-slot positions can differ.')

if __name__=='__main__':
    data=json.loads(gzip.decompress((HERE/'results.json.gz').read_bytes()))
    r=verify(data);r['source_sha256']={x:sha(HERE/x) for x in ('check_contrasts.py','results.json.gz','model-verification.json','cases.json')}
    (HERE/'contrast-verification.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r['counts']))
