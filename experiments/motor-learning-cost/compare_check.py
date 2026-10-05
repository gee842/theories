#!/usr/bin/env python3
"""Compare independently fixed empirical calculations, including original cells."""
from pathlib import Path
import hashlib
import json
import math

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT/'sources/29-motor-learning-cost-2026-10-06/cost_of_error_data.xlsx'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    producer = json.loads((HERE/'results.json').read_text())
    independent = json.loads((HERE/'independent-results.json').read_text())
    extracted = json.loads((HERE/'extracted.json').read_text())
    receipt = json.loads((HERE/'verification.json').read_text())
    assert sha(SOURCE) == producer['source_sha256'] == independent['source_sha256']
    assert sha(HERE/'PROTOCOL.md') == producer['protocol_sha256'] == independent['protocol_sha256']
    assert sha(HERE/'analyze.py') == receipt['program_sha256']
    assert sha(HERE/'independent_check.py') == independent['checker_sha256']
    for name, expected in receipt['outputs'].items():
        assert sha(HERE/name) == expected, name
    counts = {'source_values':0,'mean_trial_coordinates':0,'window_means':0,
              'component_changes':0,'participant_contrasts':0,'aggregate_fields':0}
    errors = []
    def equal(a, b, kind):
        assert math.isfinite(float(a)) and math.isfinite(float(b))
        assert math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12),(kind,a,b)
        counts[kind] += 1
        errors.append(abs(a-b))
    row_start = {('EXP1','LARGE COST'):6, ('EXP1','SMALL COST'):30,
                 ('EXP2','LARGE COST'):54,('EXP2','SMALL COST'):78}
    bounds = {'pre':(52,59),'early':(62,69),'late':(70,78)}
    def col(n):
        out=''
        while n:
            n,k=divmod(n-1,26);out=chr(65+k)+out
        return out
    seen=set()
    for r in extracted['records']:
        e,c,p,w = r['experiment'],r['source_label'],r['participant_id'],r['window']
        key=(e,c,p,w)
        assert key not in seen;seen.add(key)
        row=row_start[(e,c)]+p-1
        expected_cells=[f'{col(k)}{row}' for k in range(bounds[w][0],bounds[w][1]+1)]
        assert r['sheet']=='ADAPTATION' and r['source_row']==row and r['cells']==expected_cells
        assert len(r['values'])==len(expected_cells)
        for cell,value in zip(r['cells'],r['values']):
            equal(value,independent['source_amplitude_cells'][cell],'source_values')
        coords=independent['mean_trial_coordinates'][e+'/'+c][w]
        assert len(coords)==len(r['mean_trial_coordinates'])
        for a,b in zip(coords,r['mean_trial_coordinates']):equal(a,b,'mean_trial_coordinates')
    assert len(seen)==240
    seen=set()
    for person in producer['participants']:
        e,p=person['experiment'],person['participant_id']
        assert (e,p) not in seen;seen.add((e,p))
        ref=next(x for x in independent['participants'][e] if x['id']==p)
        for c in ('LARGE COST','SMALL COST'):
            for w in ('pre','early','late'):
                equal(person['window_means'][c][w],ref['window_means'][c][w],'window_means')
            for w in ('early','late'):
                equal(person['changes'][c][w],ref['deltas'][c][w],'component_changes')
        for w in ('early','late'):equal(person['contrast'][w],ref['opposed_contrasts'][w],'participant_contrasts')
    assert len(seen)==40
    for e in ('EXP1','EXP2'):
        for w in ('early','late'):
            for pkey,ikey in [('paired_contrast','opposed'),('source_small_change','initial_small_change'),('source_large_change','initial_large_change')]:
                a,b=producer['groups'][e][w][pkey],independent['aggregate'][e][w][ikey]
                for pk,ik in [('n','n'),('mean','mean'),('sample_sd','sd'),('standard_error','se'),('df','df')]:
                    equal(a[pk],b[ik],'aggregate_fields')
                for x,y in zip(a['ci95'],b['ci95']):equal(x,y,'aggregate_fields')
                equal(a['t_critical'],(b['ci95'][1]-b['mean'])/b['se'],'aggregate_fields')
    for w in ('early','late'):
        a,b=producer['between_cohorts'][w],independent['between_cohort'][w]
        for pk,ik in [('n_EXP1','n_exp1'),('n_EXP2','n_exp2'),('mean_difference_EXP2_minus_EXP1','mean'),('standard_error','se'),('df','df')]:
            equal(a[pk],b[ik],'aggregate_fields')
        for x,y in zip(a['ci95'],b['ci95']):equal(x,y,'aggregate_fields')
        equal(a['t_critical'],(b['ci95'][1]-b['mean'])/b['se'],'aggregate_fields')
    result={'status':'passed','scope':'Independent XML parsing and independently implemented paired estimators and t/Welch quantiles agree. This is a reproducibility check of a retrospective secondary analysis, not a new experiment or causal identification.',
            'source_sha256':sha(SOURCE),'protocol_sha256':sha(HERE/'PROTOCOL.md'),
            'counts':counts,'max_absolute_difference':max(errors),
            'tolerance':{'absolute':1e-12,'relative':1e-12},
            'producer_code_inspected_by_independent_reconstructor':False,
            'independent_statistics_library':independent['versions'],
            'producer_statistics_library':receipt['versions'],
            'files_sha256':{p:sha(HERE/p) for p in ['analyze.py','results.json','extracted.json','inventory.json','verification.json','independent_check.py','independent-results.json','compare_check.py']}}
    (HERE/'independent-verification.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'counts':counts,'max_absolute_difference':result['max_absolute_difference']},indent=2))

if __name__=='__main__':main()
