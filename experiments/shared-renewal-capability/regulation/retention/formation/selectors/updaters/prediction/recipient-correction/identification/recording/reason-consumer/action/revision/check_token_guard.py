"""Post-review regression: actual funded endpoints cannot reuse a retired token.

This producer diagnostic exercises the corrected API; it is not the independent
oracle and it does not change the frozen 28-case experiment.
"""
from copy import deepcopy
from pathlib import Path
import gzip
import hashlib
import importlib.util
import json

HERE=Path(__file__).resolve().parent


def main():
    spec=importlib.util.spec_from_file_location('_retired_token_model',HERE/'model.py')
    model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
    packed=(HERE/'results.json.gz').read_bytes();data=json.loads(gzip.decompress(packed))
    checked=[]
    for name,case in data['cases'].items():
        if case['law']['mode']=='voluntary':continue
        for producer,arm in case['producers'].items():
            for i,row in enumerate(arm['paths']):
                s=row['state'];c=s['parent']['parent']['producer']['core'];a=s['parent']
                if not (s['final_completed'] and c['active'] and c['fuel']>=8 and c['source']>=10
                        and a['scope'] and a['permission'] and a['delivery']):continue
                assert s['latch'] is None and s['imported'] is None
                actual=deepcopy(s);trace=[]
                model.trial(actual,case['law'],row['observer']['final_law'],True,'faithful',trace,'final')
                assert actual==s and len(trace)==1 and trace[0]['event']=='final_scope_or_phase_blocked'
                checked.append(dict(case=name,producer=producer,index=i,fuel=c['fuel'],source=c['source']))
    assert any(x['case']=='old_archive_replay' and x['fuel']==18 and x['source']==20 for x in checked)
    result=dict(scope='Supplemental post-review producer regression on actual saved funded endpoints; not an additional frozen experimental arm or independent checker.',
        model_sha256=hashlib.sha256((HERE/'model.py').read_bytes()).hexdigest(),
        result_sha256=hashlib.sha256(packed).hexdigest(),
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        checked_endpoints=checked,count=len(checked),all_blocked_without_state_change=True)
    (HERE/'token-guard-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Blocked retired-token reuse without stock injection or state change at',len(checked),'actual funded endpoints.')


if __name__=='__main__':main()
