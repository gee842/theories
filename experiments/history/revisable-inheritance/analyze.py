from pathlib import Path
from itertools import product
from dataclasses import asdict,replace
import json,hashlib,platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import *


def main():
    root=Path(__file__).resolve().parent;out=root/'results';out.mkdir(exist_ok=True)
    families=['homogeneous','ordered','expanded']
    main_rows=[solve(f,fm) for f in families for fm in FORMATS]
    costs=[Costs(diagnostic=d,ready=m,payload_bit=b)
           for d,m,b in product([.08,.16,.24],[.005,.03],[.001,.01])]
    grid=[solve(f,fm,c) for c in costs for f in families for fm in FORMATS]
    free=[dict(family=f,format=fm,risk=full_information_risk(f,fm)) for f in families for fm in FORMATS]
    controls=[]
    configs=[('base',Costs()),('cheap_signal',Costs(diagnostic=.24,ready=.005)),
             ('cheap_message',Costs(diagnostic=.24,ready=.03,payload_bit=.001))]
    restrictions=[('joint',{}),('no_payload',dict(allow_payload=False)),
                  ('absent_fixed',dict(ready_constraint=0)),('ready_fixed',dict(ready_constraint=1)),
                  ('no_current_test',dict(allow_diagnostic=False)),
                  ('no_payload_or_test',dict(allow_payload=False,allow_diagnostic=False))]
    for label,c in configs:
        for f in families:
            for name,kw in restrictions:
                controls.append(dict(cost_case=label,restriction=name,result=solve(f,'raw',c,**kw)))
    capscan=[solve('expanded','raw',replace(Costs(),cap=b)) for b in [.01,.012,.02,.04,.08,.12,.2,.4]]
    paths=[path_details(path,f) for f in families for path in
           [[0,0,0,0,0],[0,1,0,1,0],[0,0,0,1,0],[0,1,0,0,0]]]
    # Free prices and no current test recover full-information Bayes risks.
    zero=Costs(retention_bit=0,inspect=0,setup=0,payload_bit=0,ready=0,cap=0)
    for f,fm in product(families,FORMATS):
        r=solve(f,fm,zero,allow_diagnostic=False)
        assert abs(r['total_loss']-full_information_risk(f,fm))<1e-10
    result=dict(status='exploratory exact finite-team expectations; no sampled evaluation',
                source_hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest()
                               for name in ['PROTOCOL.md','model.py','test_model.py','analyze.py']},
                versions=dict(python=platform.python_version(),numpy=np.__version__,matplotlib=matplotlib.__version__),
                main=main_rows,grid=grid,free_information=free,controls=controls,
                capscan=capscan,history_examples=paths)
    (out/'analysis.json').write_text(json.dumps(result,indent=2)+'\n')
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(2,2,figsize=(12.8,8.7),layout='constrained')
    palette=['#64748b','#df8b3b','#368373','#3979b5']
    x=np.arange(3)
    for k,fm in enumerate(FORMATS):
        vals=[next(r['risk'] for r in free if r['family']==f and r['format']==fm) for f in families]
        ax[0,0].bar(x+(k-1.5)*.19,vals,width=.18,color=palette[k],label=fm)
    ax[0,0].set_xticks(x,['Constant-rate\nfamily','Ordered-regime\nfamily','Expanded\nfamily'])
    ax[0,0].set(ylabel='Expected operating loss',ylim=(0,.34))
    ax[0,0].set_title('A. Same record, different model-relative value',loc='left')
    ax[0,0].legend(ncol=4,fontsize=8,loc='upper center')
    pair=[path_details(p,'ordered') for p in [[0,0,0,1,0],[0,1,0,0,0]]]
    ax[0,1].bar(['0 → 0 → 0 → 1 → 0','0 → 1 → 0 → 0 → 0'],[p['need'] for p in pair],color=['#b7644f','#3979b5'])
    ax[0,1].axhline(.3,color='black',ls='--',label='Response threshold')
    ax[0,1].set(ylabel='Predicted next-period need',ylim=(0,.55))
    ax[0,1].set_title('B. Both end at 0 with two changes',loc='left')
    ax[0,1].legend(fontsize=8)
    for k,fm in enumerate(FORMATS):
        vals=[next(r['total_loss'] for r in main_rows if r['family']==f and r['format']==fm) for f in families]
        ax[1,0].bar(x+(k-1.5)*.19,vals,width=.18,color=palette[k],label=fm)
    ax[1,0].set_xticks(x,['Constant-rate\nfamily','Ordered-regime\nfamily','Expanded\nfamily'])
    ax[1,0].set(ylabel='Expected total loss, including inquiry',ylim=(0,.34))
    ax[1,0].set_title('C. Joint inspection, readiness, and communication',loc='left')
    ax[1,0].legend(ncol=4,fontsize=8,loc='upper center')
    cases=[('base','joint','Readiness\nwith testing'),('cheap_signal','no_payload_or_test','Readiness\nas a signal'),
           ('cheap_message','joint','Paid\nmessage')]
    selected=[next(c['result'] for c in controls if c['cost_case']==c1 and c['restriction']==c2 and c['result']['family']=='expanded') for c1,c2,_ in cases]
    ax[1,1].bar(np.arange(3)-.22,[r['readiness_probability'] for r in selected],width=.21,label='Ready',color='#368373')
    ax[1,1].bar(np.arange(3),[r['send_probability'] for r in selected],width=.21,label='Payload',color='#df8b3b')
    ax[1,1].bar(np.arange(3)+.22,[r['diagnostic_probability'] for r in selected],width=.21,label='Current test',color='#3979b5')
    ax[1,1].set_xticks(np.arange(3),[label for _,_,label in cases])
    ax[1,1].set(ylabel='Probability of selected action',ylim=(0,.3))
    ax[1,1].set_title('D. Capacity is also an observable message',loc='left')
    ax[1,1].legend(ncol=3,fontsize=8,loc='upper center')
    fig.suptitle('Preserving evidence for a changed question\nExact finite examples; supplied model families and common loss',fontsize=15)
    fig.savefig(out/'revisable-inheritance.png',dpi=180);fig.savefig(out/'revisable-inheritance.svg')
    print(json.dumps(dict(main=[{k:r[k] for k in ['family','format','total_loss','inquiry_cost','inspect_probability','send_probability','diagnostic_probability']} for r in main_rows],
                         counts=dict(grid=len(grid),controls=len(controls),capscan=len(capscan)),
                         example_pair=pair),indent=2))


if __name__=='__main__':main()
