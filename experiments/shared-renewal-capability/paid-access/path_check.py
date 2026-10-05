#!/usr/bin/env python3
"""Check the displayed carrier-turnover route against the complete event table."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,importlib.util,json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('paid_access_model',HERE/'compute.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
PATH=['wear_A','bound_recycling','capture','bound_A_formation','capture',
      'wear_Q','Y_dissociation','free_Y_recycling','Y_binding','assemble','capture',
      'wear_G','bound_recycling','free_reproduction','capture','wear_Y',
      'bound_recycling','capture','bound_G_fabrication','Y_binding','capture']


def work(x):
    roles,bonds,f,mask,cap=x
    return 4-roles.count('D')+f+roles.count('Q')+roles.count('B')


def main():
    out={}
    for zeta in (0,1):
        x=model.P;prob=Q(1);rows=[]
        for name in PATH:
            candidates=model.events(x,zeta)
            total=sum(rate for _,rate,_ in candidates)
            selected=[(rate,nxt) for label,rate,nxt in candidates if label==name and nxt is not None]
            assert len(selected)==1,(name,x,selected)
            rate,nxt=selected[0]
            if nxt=='success':
                roles,bonds,f,mask,cap=x
                assert name=='capture' and roles.count('C')==1
                nxt=(tuple('Q' if s=='C' else s for s in roles),bonds,f,mask,cap+1)
                assert model.success(nxt)
            dw=work(nxt)-work(x)
            expected=1 if name=='capture' else -1 if name.startswith('wear_') or name in ('bound_A_formation','bound_G_fabrication') else 0
            assert dw==expected
            rows.append(dict(event=name,before=x,after=nxt,selected_rate=rate,
                             total_hazard=total,work_change=dw))
            prob*=Q(rate,total);x=nxt
        assert x[3]==15 and x[4]==6 and work(x)==5
        assert PATH.count('capture')==6
        assert sum(n.startswith('wear_') for n in PATH)==4
        assert sum('recycling' in n for n in PATH)==4
        entry_prob=Q(6,21)*Q(2,15)*Q(1,6)*Q(1,5+zeta)*Q(1,6)
        assert min(r['total_hazard'] for r in rows)*Q(10,26)>=1
        out[str(zeta)]=dict(steps=rows,return_path_probability=str(prob),
            entry_selected_path_probability=str(entry_prob),
            integrated_selected_path_by_H10_lower_bound=str(entry_prob*prob/Q(2**26)),
            final_state=x)
    result=dict(status='passed',turnover_steps=21,formation_steps=5,turnover_captures=6,
        total_captures=7,initial_work=6,entry_and_return_work=5,arms=out,
        method='Exact rational selected-path accounting; same enumerated event table, not an independent chemistry reconstruction',
        model_sha256=hashlib.sha256((HERE/'compute.py').read_bytes()).hexdigest(),
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'path-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','turnover_steps','total_captures','initial_work','entry_and_return_work')},indent=2))


if __name__=='__main__':main()
