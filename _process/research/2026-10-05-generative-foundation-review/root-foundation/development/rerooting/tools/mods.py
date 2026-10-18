import json,sys
from collections import defaultdict,Counter
S=sys.argv[1]
rows=json.load(open(S+'/reach-rows.json'))
g=json.load(open(S+'/graph.json')); L=g['layers']
order=L['FOUNDATION']+L['CORE']
by=defaultdict(list)
for r in rows: by[r['module']].append(r)
tot=Counter()
out=[]
for m in order:
    rs=by[m]
    a=sum(1 for r in rs if not r['full_lts'])          # free: statement and proof
    b=sum(1 for r in rs if r['full_lts'] and not r['stmt_lts'])  # statement free, proof uses
    c=sum(1 for r in rs if r['stmt_lts'])               # statement reaches LTS
    th=lambda f: sum(1 for r in rs if r['kind']=='theorem' and f(r))
    out.append(dict(module=m,decls=len(rs),free=a,proof_only=b,stmt=c,
      thm_free=th(lambda r: not r['full_lts']),thm_proof=th(lambda r: r['full_lts'] and not r['stmt_lts']),thm_stmt=th(lambda r:r['stmt_lts'])))
    tot.update(dict(decls=len(rs),free=a,proof_only=b,stmt=c))
json.dump(out,open(S+'/module-reach.json','w'),indent=0)
print(tot)
cl=Counter()
for o in out:
    if o['decls']==0: k='empty'
    elif o['stmt']==0 and o['proof_only']==0: k='all free'
    elif o['stmt']==0: k='statements free, some proofs reach'
    elif o['free']+o['proof_only']==0: k='all statements reach'
    else: k='mixed'
    o['class']=k; cl[k]+=1
print(cl)
th=Counter()
for r in rows:
    if r['kind']=='theorem':
        th['all']+=1; th['free' if not r['full_lts'] else ('proof' if not r['stmt_lts'] else 'stmt')]+=1
print('theorems',th)
for o in out:
    print(f"{o['class'][:12]:12} {o['module']:32} d{o['decls']:4} free{o['free']:4} proof{o['proof_only']:4} stmt{o['stmt']:4}")
