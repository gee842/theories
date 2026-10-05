"""Reproduce the endogenous-capture and functional-succession examples."""
from pathlib import Path
from fractions import Fraction as F
import itertools
import json
import math
import os

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work/renewing-access'
OUT = ROOT / 'outputs'
os.environ['MPLCONFIGDIR'] = str(WORK / 'mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def field(y, g, a=1, b=1, k=1, loss=1, cost=1):
    r, c, d, e = y
    flux = k*e*c*d
    return (flux-a*r, a*r-b*c, b*c-flux, g*c-loss*e-cost*flux)

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

count = 0
for a,b,k,loss,cost in itertools.product((F(1,2),F(1),F(2)), repeat=5):
    m=F(1); s=(a+b)/a
    for fraction in (F(1,4),F(3,4)):
        c=fraction*m/s; r=b*c/a; d=m-s*c; e=b/(k*d)
        v=loss*b/(k*c*d); g=cost*b+v
        fold=cost*b+4*s*loss*b/(k*m*m)
        assert g>fold
        assert field((r,c,d,e),g,a,b,k,loss,cost)==(0,0,0,0)
        assert e==v*c/loss
        alpha=a+b; p=k*e*c; q=k*d*c; u=p+loss+cost*q
        jac=[[-alpha,-a,F(0)],[F(0),-p,-q],[v,-cost*p,-loss-cost*q]]
        coefficients=[F(1),alpha+u,alpha*u+p*loss,alpha*p*loss-a*v*q]
        for lam in (-2,-1,0,1):
            matrix=[[(F(lam) if i==j else F(0))-jac[i][j] for j in range(3)] for i in range(3)]
            assert det3(matrix)==sum(coef*F(lam)**(3-i) for i,coef in enumerate(coefficients))
        constant=coefficients[-1]
        assert constant==a*k*v*c*(2*s*c-m)
        assert (constant>0)==(fraction>F(1,2))
        gap=coefficients[1]*coefficients[2]-constant
        assert gap==alpha**2*u+alpha*u*u+u*p*loss+a*v*q
        assert gap>0
        for y in ((F(0),F(1),F(2),F(3)),(F(2),F(0),F(1),F(0))):
            z=field(y,g,a,b,k,loss,cost)
            assert sum(z[:3])==0
            assert z[3]+cost*(z[0]+z[1])==(g-cost*b)*y[1]-loss*y[3]
        count+=1
    c=m/(2*s); d=m/2
    assert cost*b+loss*b/(k*c*d)==cost*b+4*s*loss*b/(k*m*m)

g=17.
cp=(1+1/math.sqrt(2))/4
cm=(1-1/math.sqrt(2))/4
active=np.array([cp,cp,1-2*cp,16*cp])

def integrate(initial, step, horizon=60):
    n=round(horizon/step)
    ts=np.linspace(0,horizon,n+1)
    ys=np.empty((n+1,4)); ys[0]=initial
    def f(v): return np.asarray(field(v,g),dtype=float)
    for i in range(n):
        y=ys[i]
        k1=f(y); k2=f(y+step*k1/2); k3=f(y+step*k2/2); k4=f(y+step*k3)
        ys[i+1]=y+step*(k1+2*k2+2*k3+k4)/6
    return ts,ys

trajectories={}; runs=[]
for label,initial in [('activation',(1.,0.,0.,0.)),('failure',(.01,0.,.99,0.))]:
    ts,ys=integrate(initial,.004)
    _,fine=integrate(initial,.002)
    step_difference=float(np.max(abs(ys-fine[::2])))
    mass_error=float(np.max(abs(fine[:,:3].sum(axis=1)-1)))
    assert step_difference<1e-8,(label,step_difference)
    assert mass_error<1e-11
    assert float(fine.min())>=-1e-13
    if label=='activation':
        assert np.max(abs(fine[-1]-active))<1e-8
    else:
        assert np.max(fine[:,:2].sum(axis=1))<=.01+1e-13
        assert np.max(fine[:,3])<=.17+1e-13
        assert max(fine[-1][[0,1,3]])<1e-18
    trajectories[label]=(ts,ys)
    runs.append({'preparation':label,'initial_R_C_D_E':list(initial),
                 'final_R_C_D_E':fine[-1].tolist(),
                 'max_step_halving_difference':step_difference,
                 'max_material_conservation_error':mass_error,
                 'minimum_coordinate':float(fine.min())})

# An exact rational certificate for the analytically proved collapse region.
small=F(1,100); energy_bound=17*small; decay_margin=1-energy_bound
assert energy_bound==F(17,100) and decay_margin==F(83,100)

# Check the succession formulas against the seven-coordinate vector field.
succession_error=0.
for t in np.linspace(0,20,201):
    x=cp*math.exp(-t); y=cp*(1-math.exp(-t))
    substrate=math.exp(-cp*(t-(1-math.exp(-t))))
    product=1-substrate
    flux=active[3]*(x+y)*active[2]
    derivative=np.array([flux-active[0],-x,active[0]-y,x+y-flux,
                         17*(x+y)-active[3]-flux,-y*substrate,y*substrate])
    exact=np.array([0.,-x,x,0.,0.,-y*substrate,y*substrate])
    succession_error=max(succession_error,float(np.max(abs(derivative-exact))))
    assert abs(x+y-cp)<1e-14
    assert abs(substrate+product-1)<1e-14
    if t>0: assert y*substrate>0
assert succession_error<1e-13

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                     'axes.spines.top':False,'axes.spines.right':False})
fig,(left,right)=plt.subplots(1,2,figsize=(12,5.5))
teal='#137d84'; rust='#ad5d35'; gray='#5c6370'
supplies=np.linspace(9,24,700)
root=np.sqrt(np.maximum(0,1-8/(supplies-1)))
left.plot([0,24],[0,0],lw=2.6,color=gray,label='Stable inactive state')
left.plot(supplies,(1+root)/4,lw=2.6,color=teal,label='Stable active branch')
left.plot(supplies,(1-root)/4,lw=1.8,ls='--',color=rust,label='Saddle branch')
left.plot(9,.25,'o',color=gray,ms=5)
left.annotate('Positive equilibria appear\nat g = 9',xy=(9,.25),xytext=(1,.39),
              fontsize=9,arrowprops={'arrowstyle':'->','color':gray},color=gray)
left.axvline(17,color=gray,ls=':',lw=1)
left.scatter([17,17,17],[0,cm,cp],c=[gray,rust,teal],s=25,zorder=4)
left.set(xlim=(0,24),ylim=(-.025,.50),xlabel='Available incident support g',
         ylabel='Machinery at equilibrium C',title='The same support permits two stable regimes')
left.legend(frameon=False,loc='center left',bbox_to_anchor=(.02,.26),fontsize=9)
left.grid(axis='y',alpha=.15)
for label,color,name in [('activation',teal,'Initially usable material: R = 1'),
                          ('failure',rust,'Mostly degraded material: R = 0.01')]:
    ts,ys=trajectories[label]
    right.semilogy(ts[1:],ys[1:,1],color=color,lw=2.4,label=name)
right.axhline(cp,ls=':',color=gray,lw=1)
right.set(xlim=(0,20),ylim=(1e-10,1),xlabel='Time',ylabel='Capture and renewal machinery C',
          title='Two preparations under identical support g = 17')
right.legend(frameon=False,loc='lower left',fontsize=9)
right.grid(axis='y',alpha=.15)
fig.text(.06,.04,'Constructed dimensionless model; all other parameters = 1. Both preparations start with C = E = 0.',
         fontsize=9,color=gray)
fig.text(.06,.008,'Branch stability and the small-preparation failure region are proved. The activation trajectory is a numerical witness.',
         fontsize=9,color=gray)
fig.subplots_adjust(bottom=.2,top=.88,left=.075,right=.985,wspace=.29)
png=OUT/'renewing-access-to-support.png'; svg=OUT/'renewing-access-to-support.svg'
fig.savefig(png,dpi=180); fig.savefig(svg); plt.close(fig)

checks={'exact_rational_equilibrium_and_characteristic_checks':count,
        'equilibrium_R_C_D_E':active.tolist(),'fold_g':9,'example_g':17,
        'numerical_runs':runs,'integration_method':'RK4, steps .004 and .002, horizon 60',
        'small_preparation_certificate':{'A_upper':str(small),'E_upper':str(energy_bound),
                                         'coefficient_in_A_prime_le_minus_coefficient_C':str(decay_margin)},
        'succession_max_vector_field_residual':succession_error,
        'interpretation':'Arithmetic and numerical checks supplement the written proofs; neither prove global active convergence.',
        'all_checks_passed':True}
(WORK/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
