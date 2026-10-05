"""Exact diagnostics of marked renewal composition; no physical probability fit."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
# Each atom is probability, successor, elapsed time, gross charged support.
K={0:[(F(3,5),0,1,2),(F(3,10),1,2,1)],1:[(F(1,2),0,1,1),(F(1,4),1,3,2)]}
def value(kernel,x,n,h,b):
    if h<0 or b<0:return F(0)
    if n==0:return F(1)
    return sum((p*value(kernel,y,n-1,h-t,b-c) for p,y,t,c in kernel[x]),F(0))
# Four explicitly enumerated two-cycle atoms: RR, RD, DR, DD.
paths=[(F(9,25),2,4),(F(9,50),3,3),(F(3,20),3,2),(F(3,40),5,3)]
checks=[]
for h,b,expected in [(3,3,F(33,100)),(5,4,F(153,200)),(2,4,F(9,25)),(5,2,F(3,20))]:
    got=value(K,0,2,h,b)
    enum=sum((p for p,t,c in paths if t<=h and c<=b),F(0))
    assert got==expected==enum
    checks.append({'cycles':2,'deadline':h,'budget':b,'probability':str(got)})
A={0:[(F(9,10),0,1,1)],1:[]};B={0:[(F(9,10),1,1,1)],1:[]}
for x in (0,1):assert sum((a[0] for a in A[x]),F(0))==sum((a[0] for a in B[x]),F(0))
assert value(A,0,1,1,1)==value(B,0,1,1,1)==F(9,10)
assert value(A,0,2,2,2)==F(81,100) and value(B,0,2,2,2)==0
# A uniform reset approximation changes row0 by delta including the cemetery.
delta=F(1,100);Ahat={0:[(F(89,100),0,1,1)],1:[]}
errors=[]
for n in (1,2,5,10,100):
    error=abs(value(A,0,n,n,n)-value(Ahat,0,n,n,n))
    assert error<=min(F(1),n*delta)
    errors.append({'cycles':n,'exact_event_error':str(error),'uniform_operator_bound':str(min(F(1),n*delta))})
inputs=[ROOT/'_process/research/2026-10-05-support-and-shared-generativity/completion/FULL-SUCCESSOR-RESULT.md',ROOT/'experiments/shared-renewal-capability/full-successor/certificate.json']
out={'status':'all exact assertions passed','scope':'Finite abstract Markov-renewal witnesses; not CF or RNA fitted kinetics, independent evidence, or proof of the general analytic theorems.','producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'marked_kernel':{str(x):[{'probability':str(p),'successor':y,'duration':t,'gross_cost':c} for p,y,t,c in row] for x,row in K.items()},'budget_and_deadline_checks':checks,'same_one_cycle_success_different_repetition':{'each_row_success_mass':['9/10','0'],'fresh_preparation_one_cycle_both':'9/10','two_cycles_A':'81/100','two_cycles_B':'0','reason':'Successful endpoint distribution, including hidden support state, differs; observation retains success/time/cost but omits successor state.'},'approximation_checks':errors}
(HERE/'exact-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'marked_cases':len(checks),'error_cases':len(errors)}))
