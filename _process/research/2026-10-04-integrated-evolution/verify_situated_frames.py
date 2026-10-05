"""Conditional frame-formation model checks; no empirical validation.

Initial predictions before the first run:
* Weak initial inquiry and representation converge to exclusion at u=0.
* A stronger initial frame can change the outcome at matched inquiry/output.
* A small protected introduction rate leaves a stable low-coverage regime.
* A rate above the analytic saddle-node removes that regime.
* A long but not a short protected pulse can enter the unassisted high basin.
* With no actual benefit, maintained introductions impose continuing trial cost.
* Without evidence admission, protected trials do not produce frame coverage.

The first stronger-frame prediction failed at q0=.05,z0=.9. That case and
the fully covered q0=.05,z0=1 case are retained. Matched q0=.1 illustrations
were selected after checking basins; these are exploratory model calculations.
"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp, quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
B, C, LAM, MU = 4., 1., 1., 1.
QSTAR, ZSTAR = C*MU/(LAM*(B-C)), C/B
UCRIT = MU/LAM*(np.sqrt(B)-np.sqrt(B-C))**2
QFOLD = MU/LAM*(np.sqrt(B/(B-C))-1)
ZHI = LAM/(LAM+MU)

def field(t, y, b=B, c=C, lam=LAM, mu=MU, u=0., beta=0.):
    q, z, error, spent, exposure = y
    return [(1-q)*(q*(b*z-c)+beta*z+u),
            lam*q*(1-z)-mu*z,
            -(1-q)*error, c*q, lam*q]

def run(initial=(.1,.05), b=B, lam=LAM, u=0., pulse=None, beta=0.,
        horizon=160., tol=1e-9):
    state = np.array([*initial,1.,0.,0.])
    pieces = [(0.,horizon,u)] if pulse is None else [(0.,pulse,u),(pulse,horizon,0.)]
    ts, ys = [], []
    for start, end, effort in pieces:
        times = np.linspace(start,end,max(3,int((end-start)*20)+1))
        sol = solve_ivp(lambda t,y: field(t,y,b=b,lam=lam,u=effort,beta=beta),
                        [start,end],state,t_eval=times,rtol=tol,atol=tol*.01,
                        max_step=.1)
        assert sol.success
        ts.append(sol.t if not ts else sol.t[1:])
        ys.append(sol.y if len(ys)==0 else sol.y[:,1:])
        state = sol.y[:,-1]
    t, y = np.concatenate(ts), np.hstack(ys)
    assert np.all(y[:2] >= -1e-9) and np.all(y[:2] <= 1+1e-9)
    assert np.min(np.diff(y[3])) >= -1e-9
    return t,y

def jac(q,z,u=0.,b=B,lam=LAM):
    return np.array([[(1-2*q)*(b*z-C)-u,b*q*(1-q)],
                     [lam*(1-z),-lam*q-MU]])

def roots(u):
    vals = np.roots([LAM*(B-C),LAM*u-C*MU,MU*u])
    return sorted(float(v.real) for v in vals if abs(v.imag)<1e-10 and 0<v.real<1)

# Final review: q=1 is an invariant boundary even in the absent-benefit world.
assert field(0,[1.,.2,1.,0.,0.],b=0.,u=.1)[0] == 0.
assert field(0,[1.,.2,1.,0.,0.],b=0.,u=.1)[3] == C

equilibria = []
for name,q,z,u,sign in [('closed',0.,0.,0.,'stable'),
                       ('saddle',QSTAR,ZSTAR,0.,'saddle'),
                       ('high',1.,ZHI,0.,'stable')]:
    assert np.linalg.norm(field(0,[q,z,0,0,0],u=u)[:2]) < 1e-12
    eig = np.linalg.eigvals(jac(q,z,u))
    if sign=='stable': assert np.all(eig.real<0)
    else: assert np.min(eig.real)<0<np.max(eig.real)
    equilibria.append({'name':name,'q':q,'z':z,'eigenvalues':eig.tolist()})

for u in [.02,.05]:
    rr=roots(u)
    assert len(rr)==2
    for index,q in enumerate(rr):
        z=LAM*q/(LAM*q+MU)
        assert np.linalg.norm(field(0,[q,z,0,0,0],u=u)[:2]) < 1e-12
        eig=np.linalg.eigvals(jac(q,z,u))
        assert np.all(eig<0) if index==0 else np.min(eig)<0<np.max(eig)
        equilibria.append({'name':f'protected_u{u}_{index}','q':q,'z':z,
                           'eigenvalues':eig.tolist()})

assert len(roots(.1))==0
zfold=LAM*QFOLD/(LAM*QFOLD+MU)
assert np.linalg.norm(field(0,[QFOLD,zfold,0,0,0],u=UCRIT)[:2]) < 1e-12
assert abs(np.linalg.det(jac(QFOLD,zfold,UCRIT))) < 1e-12

specs = [
    ('weak_frame',{}),
    ('stronger_frame',{'initial':(.1,.9)}),
    ('initial_prediction_failed',{'initial':(.05,.9)}),
    ('full_frame_insufficient',{'initial':(.05,1.)}),
    ('weak_proposal_origination',{'initial':(.05,.05),'beta':.2}),
    ('strong_proposal_origination',{'initial':(.05,.05),'beta':1.2}),
    ('small_protected_rate',{'u':.02}),
    ('above_fold',{'u':.1}),
    ('short_pulse',{'u':.1,'pulse':1.}),
    ('long_pulse',{'u':.1,'pulse':50.}),
    ('absent_benefit',{'b':0.,'u':.1}),
    ('blocked_evidence',{'lam':0.,'u':.1,'initial':(.05,0.)}),
]
curves, records = {}, []
for name,kwargs in specs:
    t,y=run(**kwargs)
    _,fine=run(**kwargs,tol=1e-11)
    err=float(np.max(abs(y-fine)))
    assert err<1e-6
    curves[name]=(t,y)
    records.append({'case':name,'parameters':kwargs,'final_time':float(t[-1]),
                    'final_q_z_familiar_error_cost_exposure':y[:,-1].tolist(),
                    'maximum_q_on_output_grid':float(np.max(y[0])),
                    'tolerance_refinement_error':err})

assert curves['weak_frame'][1][0,-1] < 1e-8
assert curves['stronger_frame'][1][0,-1] > .99999
assert curves['initial_prediction_failed'][1][0,-1] < 1e-8
assert curves['full_frame_insufficient'][1][0,-1] < 1e-8
assert curves['weak_proposal_origination'][1][0,-1] < 1e-8
assert curves['strong_proposal_origination'][1][0,-1] > .99999
assert abs(curves['small_protected_rate'][1][0,-1]-roots(.02)[0]) < 1e-8
assert curves['above_fold'][1][0,-1] > .99999
assert curves['short_pulse'][1][0,-1] < 1e-8
assert curves['long_pulse'][1][0,-1] > .99999
assert abs(curves['absent_benefit'][1][0,-1]-.1)<1e-8
assert abs(curves['blocked_evidence'][1][0,-1]-.1)<1e-8
assert curves['blocked_evidence'][1][1,-1] == 0.
assert curves['weak_frame'][1][2,-1] < 1e-20

# Exactly funded diagnostic exposure: integral lambda*q = lambda/c * total cost.
for name,kwargs in specs:
    lam=kwargs.get('lam',LAM)
    _,y=curves[name]
    assert np.max(abs(y[4]-(lam/C)*y[3])) < 1e-9

# Positive first-discovery probability is insufficient for maintained representation.
# This optional diagnostic calculation assumes an independent Poisson trigger,
# with intensity lambda*q along the pre-discovery policy trajectory. It is not
# the same process as the deterministic fraction z and is not used to infer it.
_,closed=curves['weak_frame']
exposure=float(closed[4,-1])
no_trigger=float(np.exp(-exposure))

# Same inquiry/output, different frame: bracket the separating initial coverage.
# This is a numerical basin boundary, not an exact or universal threshold.
lo,hi=0.,1.
for _ in range(27):
    mid=(lo+hi)/2
    _,y=run(initial=(.1,mid),horizon=120.)
    if y[0,-1]>.5: hi=mid
    else: lo=mid

# Check the sufficient rectangle after the long pulse before withdrawing support.
t,y=curves['long_pulse']
idx=int(np.argmin(abs(t-50)))
assert y[0,idx]>QSTAR and y[1,idx]>ZSTAR
long_pulse_state=y[:2,idx].tolist()

# Independent derivative checks at interior points for the Dulac divergence.
for q,z,u in [(.1,.2,0.),(.4,.3,.02),(.8,.4,.1)]:
    expected=-u/q**2-(LAM*q+MU)/(q*(1-q))
    h=1e-6
    def transformed(qq,zz):
        return np.array(field(0,[qq,zz,0,0,0],u=u)[:2])/(qq*(1-qq))
    num=(transformed(q+h,z)[0]-transformed(q-h,z)[0])/(2*h)
    num+=(transformed(q,z+h)[1]-transformed(q,z-h)[1])/(2*h)
    assert abs(num-expected)<1e-6

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,2,figsize=(12.4,8.8),layout='constrained')
ax=axs[0,0]
grid=np.linspace(.012,.988,30)
Q,Z=np.meshgrid(grid,grid)
DQ=Q*(1-Q)*(B*Z-C); DZ=LAM*Q*(1-Z)-MU*Z
ax.streamplot(grid,grid,DQ,DZ,color='#d5dce2',density=.8,linewidth=.7,arrowsize=.7)
ax.plot(grid,LAM*grid/(LAM*grid+MU),'--',color='#888888',lw=1,label='Frame balance')
ax.axhline(ZSTAR,color='#aaaaaa',lw=1,ls=':',label='Policy balance')
for name,color,label in [('weak_frame','#c45145','Initial frame .05'),
                          ('stronger_frame','#2c7c7b','Initial frame .90')]:
    t,y=curves[name]; ax.plot(y[0],y[1],color=color,lw=2,label=label)
    ax.scatter(y[0,0],y[1,0],color=color,s=35,zorder=5)
ax.scatter([0,1],[0,ZHI],s=60,c='#152d43',zorder=6)
ax.scatter([QSTAR],[ZSTAR],s=65,facecolor='white',edgecolor='#152d43',zorder=6)
ax.set(xlim=(-.015,1.015),ylim=(-.015,1.015),xlabel='Inquiry practice share q',
       ylabel='Retained frame coverage z',title='A. Equal aims and initial activity, different basins')
ax.legend(loc='upper right',fontsize=8,frameon=False)

ax=axs[0,1]
us=np.linspace(0,UCRIT,300)
disc=np.maximum((LAM*us-C*MU)**2-4*LAM*(B-C)*MU*us,0)
low=(C*MU-LAM*us-np.sqrt(disc))/(2*LAM*(B-C))
saddle=(C*MU-LAM*us+np.sqrt(disc))/(2*LAM*(B-C))
ax.plot(us,low,color='#c45145',lw=2,label='Stable low coverage')
ax.plot(us,saddle,color='#888888',ls='--',label='Saddle')
ax.axhline(1,color='#2c7c7b',lw=2,label='Stable high activity')
ax.axvline(UCRIT,color='#b48738',ls=':',label=f'Fold at {UCRIT:.4f}')
ax.scatter([UCRIT],[QFOLD],color='#b48738',s=35,zorder=6)
ax.set(xlim=(0,.115),ylim=(-.025,1.05),xlabel='Protected introduction rate u',
       ylabel='Equilibrium inquiry practice share q',title='B. Small protected channels can leave the trap intact')
ax.legend(loc='center right',frameon=False,fontsize=8)

ax=axs[1,0]
for name,color,label in [('weak_frame','#888888','No protection'),
                         ('small_protected_rate','#c45145','u = .02 throughout'),
                         ('above_fold','#2c7c7b','u = .10 throughout'),
                         ('long_pulse','#b48738','u = .10 until time 50')]:
    t,y=curves[name]; ax.plot(t,y[0],color=color,lw=2,label=label)
ax.axvline(50,ls=':',color='#b48738',lw=1)
ax.set(xlim=(0,100),ylim=(-.025,1.05),xlabel='Time',ylabel='Inquiry practice share q',
       title='C. Sustained support can enable later withdrawal')
ax.legend(loc='center right',frameon=False,fontsize=8)

ax=axs[1,1]
t,y=curves['weak_frame']
ax.semilogy(t,np.maximum(y[0],1e-30),color='#c45145',lw=2,label='Inquiry share q')
ax.semilogy(t,np.maximum(y[2],1e-30),color='#152d43',lw=2,label='Familiar prediction error')
ax.set(xlim=(0,30),ylim=(1e-15,2),xlabel='Time',ylabel='Value, logarithmic scale',
       title='D. Familiar prediction improves while inquiry disappears')
ax.legend(loc='lower left',frameon=False,fontsize=8)
fig.suptitle('Endogenous experience and frame retention in a common-interest model',fontsize=15)
fig.savefig(OUT/'situated-frame-dynamics.png',dpi=180)
fig.savefig(OUT/'situated-frame-dynamics.svg')
plt.close(fig)

report={'status':'passed','scope':'Conditional model checks, not empirical evidence',
        'parameters':{'b':B,'c':C,'lambda':LAM,'mu':MU},
        'prediction_correction':'Initial q=.05,z=.9 did not recover. That case and q=.05,z=1 are retained; matched q=.1 examples selected after inspecting basins.',
        'proposal_origination_threshold_beta':C*MU/LAM,
        'analytic_thresholds':{'q_saddle':QSTAR,'z_saddle':ZSTAR,
                               'u_fold':UCRIT,'q_fold':QFOLD},
        'equilibria':equilibria,'cases':records,
        'numerical_initial_z_basin_boundary_at_q0_10':[lo,hi],
        'long_pulse_withdrawal_q_z':long_pulse_state,
        'closed_trajectory_exposure_t160':exposure,
        'optional_poisson_no_trigger_probability_t160':no_trigger,
        'verification':['equilibrium residuals and eigenvalue signs',
                        'saddle-node residual and zero determinant',
                        'twelve trajectories including the retained failed initial prediction',
                        'bounded fractions and monotone cumulative trial cost',
                        'absent-benefit q=1 invariant boundary and its recurring cost',
                        'exact cost to diagnostic exposure accounting',
                        'Dulac divergence finite-difference comparison']}
(OUT/'situated-frame-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
