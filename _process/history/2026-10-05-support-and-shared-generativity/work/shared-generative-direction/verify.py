"""Check capability inclusion, stationary ordering, and shared renewal."""
from pathlib import Path
from fractions import Fraction as F
import itertools
import json
import math
import os
ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'work/shared-generative-direction'; OUT=ROOT/'outputs'
os.environ['MPLCONFIGDIR']=str(ROOT/'work/renewing-access/mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def feasible(q,m,w):
    return min(q)>=0 and sum(q)<=m and q[0]+2*q[1]<=w
def vertices(m,w):
    candidates=[(F(0),F(0)),(min(m,w),F(0)),(F(0),min(m,w/2)),(2*m-w,w-m)]
    return [q for q in candidates if feasible(q,m,w)]
inclusions=0
for m0,w0,m1,w1 in itertools.product(map(F,range(1,6)),repeat=4):
    direct=all(feasible(q,m1,w1) for q in vertices(m0,w0))
    formula=m1>=min(m0,w0) and w1>=min(2*m0,w0)
    assert direct==formula
    inclusions+=1
assert feasible((4,0),4,4) and not feasible((4,0),3,6)
assert feasible((0,3),3,6) and not feasible((0,3),4,4)
assert all(feasible(q,4,6) for q in vertices(F(4),F(4)))

rates={
 'baseline':([F(5,2),F(2)],[F(1),F(2)]),
 'renewal':([F(5,2),F(7,4)],[F(1,2),F(1)]),
 'formation_loss_only':([F(5,2),F(7,4)],[F(1),F(2)])}
expected={'baseline':[F(1,6),F(5,12),F(5,12)],
          'renewal':[F(4,59),F(20,59),F(35,59)],
          'formation_loss_only':[F(16,91),F(40,91),F(35,91)]}
markov={}
for name,(birth,death) in rates.items():
    weights=[F(1)]
    for i in range(2): weights.append(weights[-1]*birth[i]/death[i])
    pi=[v/sum(weights) for v in weights]
    assert pi==expected[name]
    for i in range(2): assert pi[i]*birth[i]==pi[i+1]*death[i]
    markov[name]={'birth_rates':list(map(str,birth)),'loss_rates':list(map(str,death)),
                  'stationary_probabilities':list(map(str,pi)),
                  'mean_capacity_level':str(sum(i*p for i,p in enumerate(pi)))}
for cut in (1,2):
    assert sum(expected['renewal'][cut:])>sum(expected['baseline'][cut:])
    assert sum(expected['formation_loss_only'][cut:])<sum(expected['baseline'][cut:])
assert F(90,59)-F(5,4)==F(65,236)
assert F(5,4)-F(110,91)==F(15,364)
# Starting at level 1, the initial derivative of probability(level >= 2) is lambda_1.
assert rates['renewal'][0][1]<rates['baseline'][0][1]

def field(z,g=F(73,6),theta=1):
    r,c,y,d,e=z
    j=e*d*(c+theta*y)
    return (j-r-4*r*y,r-c,y*(4*r-1),c+y-j,g*c-e-j)
equilibrium=(F(1,4),F(1,4),F(1,8),F(3,8),F(8,3))
assert field(equilibrium)==(0,0,0,0,0)
for z in itertools.product((F(0),F(1,4)),repeat=5):
    f=field(z)
    assert sum(f[:4])==0
    assert f[4]+sum(f[:3])==F(73,6)*z[1]-z[4]-z[1]-z[2]

jac=[[F(-5,2),0,-1,F(9,64)],[1,-1,0,0],[F(1,2),0,0,0],[1,F(73,6),0,F(-73,64)]]
# Central differences are exact here: each individual reduced coordinate has degree at most two.
zstar=[equilibrium[i] for i in (0,1,2,4)]
def reduced(z):
    r,c,y,e=z
    f=field((r,c,y,1-r-c-y,e))
    return [f[i] for i in (0,1,2,4)]
for col in range(4):
    plus=zstar.copy(); minus=zstar.copy(); h=F(1,100)
    plus[col]+=h; minus[col]-=h
    diff=[(v-w)/(2*h) for v,w in zip(reduced(plus),reduced(minus))]
    assert diff==[row[col] for row in jac]
coeff=[F(1),F(297,64),F(877,128),F(265,128),F(73,128)]
def det4(m):
    total=F(0)
    for perm in itertools.permutations(range(4)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        total+=sign*math.prod(m[i][perm[i]] for i in range(4))
    return total
for x in (-2,-1,0,1,2):
    m=[[(F(x) if i==j else F(0))-jac[i][j] for j in range(4)] for i in range(4)]
    assert det4(m)==sum(v*F(x)**(4-i) for i,v in enumerate(coeff))
_,aa,bb,cc,dd=coeff
assert aa*bb-cc==F(243509,8192)
assert aa*bb*cc-cc*cc-aa*aa*dd==F(51651371,1048576)

g=73/6; c=(1+math.sqrt(19/67))/4
initial=np.array([c,c,.0001,1-2*c-.0001,(g-1)*c])
target=np.array(list(map(float,equilibrium)))
def integrate(step,horizon=120):
    z=initial.copy(); max_mass_error=0.; lowest=float(z.min())
    sampled=[z.copy()]
    def f(z): return np.asarray(field(z,g),dtype=float)
    for i in range(round(horizon/step)):
        p=f(z); q=f(z+step*p/2); r=f(z+step*q/2); s=f(z+step*r)
        z+=step*(p+2*q+2*r+s)/6
        max_mass_error=max(max_mass_error,abs(sum(z[:4])-1))
        lowest=min(lowest,float(z.min()))
        if (i+1)%round(1/step)==0: sampled.append(z.copy())
    return np.asarray(sampled),max_mass_error,lowest
coarse,mass0,min0=integrate(.004)
fine,mass1,min1=integrate(.002)
step_error=float(np.max(abs(coarse-fine)))
end_error=float(np.max(abs(fine[-1]-target)))
assert step_error<1e-8 and end_error<1e-7
assert max(mass0,mass1)<1e-11 and min(min0,min1)>=0

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                     'axes.spines.top':False,'axes.spines.right':False})
fig,(left,right)=plt.subplots(1,2,figsize=(12,5.7))
gray='#626b78'; teal='#137d84'; rust='#ad5d35'
left.fill([0,4,2,0],[0,0,2,3],color=teal,alpha=.12)
left.plot([0,4,2,0,0],[0,0,2,3,0],color=teal,lw=2.5,label='Renewed material: (m, e) = (4, 6)')
left.fill([0,4,0],[0,0,2],color=gray,alpha=.12)
left.plot([0,4,0,0],[0,0,2,0],color=gray,lw=2,label='Before: (4, 4)')
left.plot([0,3,0,0],[0,0,3,0],color=rust,ls='--',lw=2,label='Material depleted: (3, 6)')
left.scatter([4,0],[0,3],color=[gray,teal],s=32,zorder=5)
left.set(xlim=(-.12,4.35),ylim=(-.08,3.35),xlabel='Jointly built capacity q₁',ylabel='Jointly built capacity q₂',
         title='A new possibility can coexist with a lost one')
left.legend(frameon=False,fontsize=8,loc='upper right',bbox_to_anchor=(1,-.15))
left.grid(alpha=.12)
xs=np.arange(3); width=.24
for offset,(name,color,label) in zip((-1,0,1),[
 ('baseline',gray,'Baseline'),('renewal',teal,'Slower formation, lower loss'),
 ('formation_loss_only',rust,'Slower formation only')]):
    right.bar(xs+offset*width,list(map(float,expected[name])),width,color=color,label=label)
right.set(xticks=xs,xticklabels=['0','1','2'],ylim=(0,.69),
          xlabel='Certified capacity level n',ylabel='Long-run probability',
          title='Retention can outweigh slower formation')
right.legend(frameon=False,fontsize=8,loc='upper left')
right.grid(axis='y',alpha=.12)
fig.text(.07,.025,'Constructed examples. Left: equal assay horizon and budgets after upkeep. Right: supplied effective transition rates.',
         color=gray,fontsize=9)
fig.subplots_adjust(left=.075,right=.985,top=.9,bottom=.25,wspace=.3)
fig.savefig(OUT/'shared-generative-direction.png',dpi=180)
fig.savefig(OUT/'shared-generative-direction.svg'); plt.close(fig)

checks={'capability_inclusion_cases':inclusions,'stationary_examples':markov,
 'transient_counterexample':'From n=1, derivative of Pr(n_t>=2) is 7/4 under renewal, versus 2 at baseline.',
 'shared_renewal':{'equilibrium_R_C_Y_D_E':list(map(str,equilibrium)),
 'characteristic_coefficients':list(map(str,coeff)),
 'routh_margins':[str(aa*bb-cc),str(aa*bb*cc-cc*cc-aa*aa*dd)],
 'rare_Y_growth_exponent':'sqrt(19/67), independent of theta',
 'initial_R_C_Y_D_E':initial.tolist(),'final_R_C_Y_D_E':fine[-1].tolist(),
 'max_step_halving_difference_at_integer_times':step_error,
 'max_final_equilibrium_error':end_error,'max_material_error':max(mass0,mass1),
 'minimum_coordinate':min(min0,min1),'numerics':'RK4 .004/.002, horizon120; numerical connecting witness only.'},
 'all_checks_passed':True}
(WORK/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
