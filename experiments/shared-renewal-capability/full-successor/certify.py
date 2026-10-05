"""Directed certificates for all-route first turnover and support restoration."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import sys
sys.dont_write_bytecode=True
import hashlib,json,time
import numpy as np
import compute,fixed
HERE=Path(__file__).resolve().parent
TAIL_RECORD=HERE.parent/'full-successor-critique/exact-check.json'

def main():
    start=time.monotonic();bounds=json.loads(TAIL_RECORD.read_text());epsilon=Fraction(bounds['analytic_mobile_pool_upcrossing_bounds_H10']['40']['upper_exact'])
    g=compute.build();print('Certificate graph prepared',g['n'],flush=True)
    # Full prefix law; absorbing organizations classify the omitted first entrance.
    xs,rows,Q,Qe,rewards,groups=compute.count.graph()
    tail_cert={}
    for cutoff in (3,4):
        reward=np.array([groups[k] is not None and x[compute.count.IX['F']]>cutoff for k,x in enumerate(xs)]+[False,False])
        val=fixed.certify(Qe.astype(np.int64),reward,progress=lambda n,N:print('entry-tail',cutoff,n,N,flush=True))
        val['original_upper_exact']=str(Fraction(val['upper_exact'])+epsilon);tail_cert[str(cutoff)]=val
        print('entry-tail complete',cutoff,float(Fraction(val['original_upper_exact'])),flush=True)
    assert Fraction(tail_cert['4']['original_upper_exact'])<Fraction(1,10**16)
    output={'status':'in_progress','created_at_utc':datetime.now(timezone.utc).isoformat(),'entry_tail_certificates':tail_cert,'free_packet_overflow_upper_exact':str(epsilon),'queries':{}}
    for j in (0,1):
        for m in (None,0,1,2,3,4):
            Q=compute.matrix(g,j,m)
            reward=np.zeros(g['n'],dtype=bool)
            for u,ai,gj,f in g['success']:
                if m is None or f>=m:reward[u]=True
            key=f'gate{j}_entry'+('all' if m is None else str(m))
            val=fixed.certify(Q,reward,progress=lambda n,N:print(key,n,N,flush=True))
            output['queries'][key]=val
            print('complete',key,val['lower_decimal'],val['upper_decimal'],flush=True)
            (HERE/'certificate-progress.json').write_text(json.dumps(output,indent=2)+'\n')
    totals={}
    for j in (0,1):
        full=output['queries'][f'gate{j}_entryall'];lo=Fraction(full['lower_exact']);hi=Fraction(full['upper_exact'])+epsilon
        rlo=sum(Fraction(output['queries'][f'gate{j}_entry{m}']['lower_exact']) for m in range(5))
        rhi=sum(Fraction(output['queries'][f'gate{j}_entry{m}']['upper_exact']) for m in range(5))+epsilon+Fraction(tail_cert['4']['original_upper_exact'])
        # The error for the union of disjoint entry-reserve events is one overflow
        # probability, not five: their coupled outcome indicators cannot overlap.
        totals[str(j)]={'turnover_lower_exact':str(lo),'turnover_upper_exact':str(hi),'turnover_decimal':float(lo),'restoring_lower_exact':str(rlo),'restoring_upper_exact':str(rhi),'restoring_decimal':float(rlo)}
    contrasts={}
    for name in ('turnover','restoring'):
        lo=Fraction(totals['0'][name+'_lower_exact'])-Fraction(totals['1'][name+'_upper_exact']);hi=Fraction(totals['0'][name+'_upper_exact'])-Fraction(totals['1'][name+'_lower_exact'])
        contrasts[name]={'lower_exact':str(lo),'upper_exact':str(hi),'lower_decimal':float(lo),'upper_decimal':float(hi),'sign':'positive' if lo>0 else 'negative' if hi<0 else 'unresolved'}
    paths=[HERE/'PROTOCOL.md',HERE/'model.py',HERE/'compute.py',HERE/'fixed.py',Path(__file__),TAIL_RECORD,HERE.parent/'full-entry/compute.py']
    output.update(status='passed',totals=totals,contrasts=contrasts,graph={'states':g['n'],'material_skeletons':len(g['skel']),'free_packet_cap':compute.CAP,'restoring_entry_reserve_max':4},input_sha256={str(p.relative_to(HERE.parent.parent.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},elapsed_seconds=time.monotonic()-start,scope='Directed finite-law probabilities plus analytic overflow and omitted-entry errors; no molecular identification or broad capability ordering')
    (HERE/'certificate.json').write_text(json.dumps(output,indent=2)+'\n');(HERE/'certificate-progress.json').unlink();print(json.dumps(contrasts,indent=2),flush=True)

if __name__=='__main__':main()
