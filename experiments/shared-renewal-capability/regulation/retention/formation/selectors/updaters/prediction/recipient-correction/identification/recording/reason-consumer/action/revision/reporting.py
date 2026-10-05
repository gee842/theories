"""Post-run descriptive scopes derived from preserved endpoints, no transitions.

The original supported_command scalar intentionally remains byte-for-byte in
the first result. This report separates the selected fresh and historical view.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import gzip
import hashlib
import json

HERE=Path(__file__).resolve().parent


def sha(b):return hashlib.sha256(b).hexdigest()


def observations(state, mode, final_law):
    p=state['parent']['parent']['producer'];w=state['parent']['parent']
    fresh=state['selected_bank']=='fresh'
    context=state['fresh']['epoch'] if fresh else p['context']
    cache=bool(p['cache_valid'] and p['read_count']==3 and p['cache_context']==context)
    publication=bool(cache and w['publication_current'] and w['phase']=='published' and
        w['publication'] is not None and w['publication']['context']==context)
    command=None
    if mode=='conventional' and cache:
        vals={int(d if x else 1-d) for d,x in zip((0,1,0),p['cache']) if x is not None}
        if len(vals)==1:command=next(iter(vals))
    elif publication:
        mask=w['publication']['mask']
        if mask[0] and bool(mask[1])!=bool(mask[2]):command=int(mask[2])
    wrong=command is not None and command!=final_law
    rootonly=bool(publication and w['publication']['mask']==[True,False,False])
    return dict(fresh_supported_command=int(fresh and command is not None),
        historical_supported_command=int(not fresh and command is not None),
        fresh_wrong_at_final_law=int(fresh and wrong),
        historical_wrong_at_final_law=int(not fresh and wrong),
        fresh_completed_publication=int(fresh and publication),
        fresh_rootonly_publication=int(fresh and rootonly),
        fresh_completed_fact_cache=int(fresh and cache))


def main():
    packed=(HERE/'results.json.gz').read_bytes();raw=gzip.decompress(packed)
    manifest=json.loads((HERE/'result-files.json').read_text())
    assert sha(packed)==manifest['compressed_sha256'] and sha(raw)==manifest['uncompressed_sha256']
    result=json.loads(raw);out={}
    for name,case in result['cases'].items():
        out[name]={}
        for producer,arm in case['producers'].items():
            sums=defaultdict(Fraction)
            for row in arm['paths']:
                vals=observations(row['state'],case['law']['mode'],row['observer']['final_law'])
                assert vals['fresh_supported_command']+vals['historical_supported_command']==int(row['metrics']['supported_command'])
                assert vals['fresh_wrong_at_final_law']+vals['historical_wrong_at_final_law']==int(row['metrics']['supported_wrong'])
                for k,v in vals.items():sums[k]+=Fraction(row['probability'])*v
            out[name][producer]={k:str(v) for k,v in sorted(sums.items())}
    receipt=dict(scope='Post-first-run reporting clarification; derived from preserved endpoints, no transition rerun.',
        meaning='Support means a structurally available selected-view command, not permission, affordability or universally true current-law knowledge. Historical support remains old evidence. Wrong-at-final-law is an observer diagnostic; late change and false acquisition violate distinct positive premises.',
        source_sha256={'results.json.gz':sha(packed),'decompressed_results':sha(raw),
            'result-files.json':sha((HERE/'result-files.json').read_bytes()),'reporting.py':sha(Path(__file__).read_bytes())},
        cases=out)
    (HERE/'reporting.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(out['primary']['variable'],indent=2))


if __name__=='__main__':main()
