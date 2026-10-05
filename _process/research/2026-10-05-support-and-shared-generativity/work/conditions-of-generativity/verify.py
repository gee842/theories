"""Reproduce power thresholds, timing comparison, and arithmetic checks."""
from pathlib import Path
from fractions import Fraction as F
import itertools
import json
import math
import os

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT/'work/conditions-of-generativity'
OUT = ROOT/'outputs'
os.environ['MPLCONFIGDIR'] = str(WORK/'mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def field(y, power, a=1, b=1, k=1, loss=1, cost=1):
    r,c,d,e = y
    flux=k*e*c*d
    return (flux-a*r, a*r-b*c, b*c-flux, power-loss*e-cost*flux)

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

count=0
for a,b,k,loss,cost in itertools.product((F(1,2),F(1),F(2)), repeat=5):
    m=F(1); d=F(1,3); c=a/(a+b)*(m-d); r=b/a*c; e=b/(k*d)
    power=loss*e+cost*b*c
    assert field((r,c,d,e),power,a,b,k,loss,cost)==(0,0,0,0)
    alpha=a+b; p=k*e*c; q=k*d*c; s=p+loss+cost*q
    j=[[-alpha,-a,F(0)],[F(0),-p,-q],[-cost*b,-cost*p,-loss-cost*q]]
    coeff=[F(1),alpha+s,alpha*s+p*loss,alpha*p*loss+a*cost*b*q]
    for lam in (-2,-1,0,1):
        matrix=[[(F(lam) if i==n else F(0))-j[i][n] for n in range(3)] for i in range(3)]
        assert det3(matrix)==sum(coeff[i]*F(lam)**(3-i) for i in range(4))
    gap=coeff[1]*coeff[2]-coeff[3]
    assert gap==alpha**2*(p+loss)+cost*q*(alpha**2-a*b)+alpha*s*s+s*p*loss
    assert gap>0
    for y in [(F(0),F(1),F(2),F(3)),(F(2),F(0),F(1),F(0))]:
        derivatives=field(y,power,a,b,k,loss,cost)
        assert sum(derivatives[:3])==0
        assert derivatives[3]+cost*sum(derivatives[:2])==power-loss*y[3]-cost*b*y[1]
    count+=1

def power_equilibrium(power):
    if power<=1: return np.array([0.,0.,1.,power])
    d=2/(math.sqrt((power-.5)**2+2)+power-.5)
    return np.array([(1-d)/2,(1-d)/2,d,1/d])

initial=power_equilibrium(1.2)

def integrate(mode,step,horizon=180):
    n=round(horizon/step)
    time=np.linspace(0,horizon,n+1)
    y=np.empty((n+1,4)); y[0]=initial
    supplied=np.empty(n)
    for i in range(n):
        power=1.2 if mode=='constant' else (2.4 if i%round(60/step)<round(30/step) else 0.)
        supplied[i]=power
        def f(v): return np.asarray(field(v,power),dtype=float)
        v=y[i]; k1=f(v); k2=f(v+step*k1/2); k3=f(v+step*k2/2); k4=f(v+step*k3)
        y[i+1]=v+step*(k1+2*k2+2*k3+k4)/6
    return time,y,float(supplied.sum()*step)

trajectories={}; runs=[]
for mode in ('constant','intermittent'):
    time,y,total=integrate(mode,.01)
    _,fine,total_fine=integrate(mode,.005)
    error=float(np.max(abs(y-fine[::2])))
    mass_error=float(np.max(abs(y[:,:3].sum(axis=1)-1)))
    assert error<2e-8,(mode,error)
    assert mass_error<1e-11
    assert y.min()>=-1e-13
    assert abs(total-216)<1e-9 and abs(total_fine-total)<1e-9
    trajectories[mode]=(time,y)
    runs.append({'mode':mode,'total_supplied_usable_energy_t180':total,
                 'max_step_halving_difference':error,'max_material_error':mass_error,
                 'initial_R_C_D_E':initial.tolist(),'final_R_C_D_E':y[-1].tolist(),
                 'period_end_C':[float(y[round(t/.01),1]) for t in (0,60,120,180)]})

def linear_flow(q,t):
    root=math.sqrt(q); c=math.cosh(root*t); s=math.sinh(root*t)
    return math.exp(-t)*np.array([[c,root*s],[s/root,c]])

bounds=[]
for high in (2.4,2.41):
    low=high*math.exp(-4); r=math.sqrt(high); d=r*math.exp(-2)
    matrix=linear_flow(low,26)@linear_flow(high,34)
    trace=float(np.trace(matrix))
    formula=math.exp(-60)*(2*math.cosh(34*r)*math.cosh(26*d)
             +(r/d+d/r)*math.sinh(34*r)*math.sinh(26*d))
    upper=(2+(math.exp(2)+math.exp(-2))/4)*math.exp(-60+34*r+26*d)
    assert abs(trace-formula)<1e-12
    assert 0<trace<upper<1
    bounds.append({'high_energy_envelope':high,'low_energy_envelope':low,
                   'period_matrix':matrix.tolist(),'trace':trace,'analytic_trace_upper_bound':upper,
                   'analytic_determinant':'exp(-120)>0; direct floating determinant is ill-conditioned and not used'})

# Exact rational certificate for the envelope 2.41: r<1.553, e^-2<.136,
# so the exponent is below -1.69; the prefactor is below 3.884.
# e^1.69 > 1+1.69+1.69^2/2+1.69^3/6 > 3.884.
assert F(1553,1000)**2>F(241,100)
prefactor_bound=F(971,250)
exponent_bound=-60+F(1553,1000)*(34+26*F(17,125))
assert exponent_bound < -F(169,100)
lower_exp=sum(F(169,100)**n/F(math.factorial(n)) for n in range(4))
assert lower_exp>prefactor_bound
# e^2<7.4 and e^-2<.136 are verified by rational Taylor lower/upper bounds.
lower_e2=sum(F(2)**n/F(math.factorial(n)) for n in range(11))
tail_start=F(2)**11/F(math.factorial(11))
upper_e2=lower_e2+tail_start/(1-F(1,6))
assert upper_e2<F(37,5)
assert lower_e2>F(125,17)

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
 'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold'})
fig=plt.figure(figsize=(12,5.7))
grid=fig.add_gridspec(2,2,width_ratios=(1,1.2),height_ratios=(1,2),hspace=.22,wspace=.35)
left=fig.add_subplot(grid[:,0]); top=fig.add_subplot(grid[0,1]); bottom=fig.add_subplot(grid[1,1],sharex=top)
powers=np.linspace(0,3,400)
left.plot(powers,[power_equilibrium(p)[1] for p in powers],lw=2.6,color='#137d84')
left.axvline(1,color='#737780',ls='--',lw=1.2)
left.axhline(.5,color='#737780',ls=':',lw=1)
left.text(1.07,.455,'Supply threshold\nP = 1',va='top',color='#50545b')
left.text(.08,.512,'Material ceiling: C = 0.5',fontsize=9,color='#50545b')
left.plot(1.2,initial[1],'o',color='#137d84',ms=6)
left.set(xlim=(0,3),ylim=(0,.55),xlabel='Constant supplied usable power P',
 ylabel='Renewal machinery at equilibrium C*',title='Steady supply permits a maintained regime')
left.grid(axis='y',alpha=.14)
t=np.linspace(0,180,1801)
signal=np.where(np.mod(t,60)<30,2.4,0.)
top.step(t,signal,where='post',lw=1.8,color='#ae6138',label='30 on / 30 off')
top.axhline(1.2,color='#137d84',lw=1.6,ls='--',label='Constant')
top.set(ylim=(-.1,2.7),ylabel='Supplied power',title='Equal mean power can have different outcomes')
top.legend(loc='upper center',bbox_to_anchor=(.5,-.03),frameon=False,ncol=2,fontsize=8)
top.tick_params(labelbottom=False)
for mode,color,label in [('constant','#137d84','Constant: active equilibrium'),
                          ('intermittent','#ae6138','Interrupted: activity declines')]:
    time,y=trajectories[mode]
    bottom.semilogy(time,y[:,1],lw=2,color=color,label=label)
bottom.set(xlim=(0,180),xlabel='Time',ylabel='Renewal machinery C')
bottom.legend(loc='lower left',frameon=False,fontsize=8)
bottom.grid(axis='y',alpha=.15)
bottom.set_xticks([0,30,60,90,120,150,180])
fig.text(.035,.025,'Constructed model; a = b = k = loss = cost = M = 1. Right: same initial state, mean power 1.2. Time is dimensionless.',
 fontsize=9,color='#515960')
fig.subplots_adjust(bottom=.15,top=.9,left=.075,right=.985)
png=OUT/'conditions-of-generativity.png'; svg=OUT/'conditions-of-generativity.svg'
fig.savefig(png,dpi=170);fig.savefig(svg);plt.close(fig)

checks={'equilibrium_and_characteristic_checks':count,'simulation_runs':runs,
 'simulation_method':'Fourth-order Runge-Kutta, steps .01 and .005; every supply switch aligned to step boundary.',
 'timing_proof_bounds':bounds,'rational_certificate':{'exponent_upper':str(exponent_bound),
 'prefactor_upper':str(prefactor_bound),'lower_bound_exp_1_69':str(lower_exp),'passed':True},
 'figure_paths':[str(png),str(svg)],
 'claims':'Proofs establish threshold and collapse; trajectories illustrate one initial state and do not establish positive global attraction.',
 'all_checks_passed':True}
(WORK/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
