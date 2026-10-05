"""Exact enclosures for a consequence of the source's Poisson/multinomial closure.
No biological fit, image analysis or physical renewal probability is computed.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
SOURCE=ROOT/'sources/24-rna-network-evidence-2026-10-05/repeated-renewal-addition/Ledoux-2026-v6.pdf'
EXPECTED='83819c129c833c01a8a3af25ca1b640b878e77ef6ed517085d579cfbc29b5dd7'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED
SCALE=10**20
def exp_bounds(x):
    x=F(x);term=total=F(1)
    for n in range(1,101):term*=x/n;total+=term
    first=term*x/101;ratio=x/102
    assert ratio<1
    return total,total+first/(1-ratio)
def display(lo,hi):
    return {'lower_numerator':lo.numerator*SCALE//lo.denominator,'upper_numerator':-(-hi.numerator*SCALE//hi.denominator),'denominator':SCALE}
rows=[];factorizations=0
for a in (1,2):
    seg=[(a,0),(0,a)];col=[(a,a),(0,0)]
    for coord in (0,1):assert sorted(x[coord] for x in seg)==sorted(x[coord] for x in col)
    exp_lo,exp_hi=exp_bounds(F(a,2));ulo,uhi=1/exp_hi,1/exp_lo
    mixlo,mixhi=(1-uhi)**2,(1-ulo)**2
    colo_lo,colo_hi=F(1,2)*(1-uhi**2)**2,F(1,2)*(1-ulo**2)**2
    dlo,dhi=mixlo-colo_hi,mixhi-colo_lo
    assert (dhi<0 if a==1 else dlo>0)
    for field in (seg,col):
        for s in (F(0),F(1,2),F(1)):
            for h0,p0 in field:
                lh=(1-s)*h0+s*F(a,2);lp=(1-s)*p0+s*F(a,2);lam=lh+lp
                if not lam:continue
                for h,p in [(0,0),(1,0),(0,1),(1,1),(2,3)]:
                    poisson_multinomial=lam**(h+p)/factorial(h+p)*F(factorial(h+p),factorial(h)*factorial(p))*(lh/lam)**h*(lp/lam)**p
                    split=lh**h*lp**p/F(factorial(h)*factorial(p))
                    assert poisson_multinomial==split;factorizations+=1
    rows.append({'a':a,'segregated_s0':'0','co_located_s0':display(colo_lo,colo_hi),'either_field_s1':display(mixlo,mixhi),'co_located_s1_minus_s0':display(dlo,dhi),'co_located_sign':'negative' if a==1 else 'positive'})
out={'status':'passed','producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source':str(SOURCE.relative_to(ROOT)),'source_sha256':EXPECTED,'source_read_scope':'Author v6 PDF p8 equations2-3; diagnostic fixes d=1, no deletion; independent species Poisson law derived by splitting.','scope':'Conditional model co-occupancy task, not replication or repeated renewal; no parameter fit or external validation. Source dye calibration is a separate packet model.','arithmetic':'Exact Fraction Taylor100 with geometric remainder for exp(a/2); reciprocal bounds; displayed outward at1e20.','factorization_diagnostics':factorizations,'rows':rows}
(HERE/'mixing-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'passed','factorization_cases':factorizations,'signs':[row['co_located_sign'] for row in rows]}))
