"""Checks of explicit selection and replacement models, not empirical validation."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
from scipy.special import expit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent

# Inherited production versus copying of current expenditure savings.
a, delta, eta, mu, K = 9., 1., 1., 1., 1.
uH, uL = .5, .1
du = uH-uL
CH_star = 3+np.sqrt(7)
ucrit = .25

def practice_rhs(t, state, copying):
    logE, logC, logit = state
    E, C, x = np.exp(logE), np.exp(logC), expit(logit)
    effort = uL+du*x
    return [a*np.exp(logC-logE)/(1+C/K)-delta-effort*C,
            eta*effort*E-mu,
            (eta-copying)*E*du]

def practice_run(copying, initial=(2., CH_star, .99), tol=1e-9):
    E0, C0, x0 = initial
    times = np.linspace(0, 150, 3001)
    sol = solve_ivp(lambda t,z: practice_rhs(t,z,copying), [0,150],
                    [np.log(E0),np.log(C0),np.log(x0/(1-x0))],
                    t_eval=times, rtol=tol, atol=tol*.01, max_step=.05)
    assert sol.success
    values = np.vstack([np.exp(sol.y[0]),np.exp(sol.y[1]),expit(sol.y[2])])
    assert np.all(values[:2] > 0)
    assert np.all((values[2]>0)&(values[2]<=1))
    assert np.max(values[0]+values[1]/eta) <= max(E0+C0/eta,a*K/min(delta,mu))+1e-7
    return times, values

practice_cases = []
practice_curves = []
for name, copying, initial in [
    ('Inherited production dominates', .5, (2.,CH_star,.99)),
    ('Current-cost copying dominates', 1.5, (2.,CH_star,.99)),
    ('Selection-compatible but depleted', .5, (.05,.001,.99)),
    ('Balanced transmission', 1., (2.,CH_star,.99)),
]:
    t, z = practice_run(copying, initial)
    _, fine = practice_run(copying, initial, 1e-11)
    error = float(np.max(np.abs(z-fine)))
    assert error < 1e-6
    practice_cases.append({'case':name,'copying':copying,'initial':initial,
                          'final_t150_E_C_x':z[:,-1].tolist(),
                          'max_E':float(np.max(z[0])),
                          'tolerance_refinement_error':error})
    practice_curves.append((t,z))
assert abs(practice_cases[0]['final_t150_E_C_x'][0]-2) < 1e-6
assert abs(practice_cases[0]['final_t150_E_C_x'][1]-CH_star) < 1e-6
assert practice_cases[0]['final_t150_E_C_x'][2] > .99999
assert max(practice_cases[1]['final_t150_E_C_x'][:2]) < 1e-6
assert 0 < practice_cases[1]['final_t150_E_C_x'][2] < .99
assert max(practice_cases[2]['final_t150_E_C_x'][:2]) < 1e-6
assert np.max(np.abs(practice_curves[3][1][2]-.99)) < 1e-12

# Check microscopic production/switching against the aggregated derivatives.
for E,C,x,copying in [(2.,5.,.4,.5),(.4,.2,.8,1.5),(4.,3.,.1,1.)]:
    CH,CL=C*x,C*(1-x)
    J=copying*E*du*CH*CL/C
    dCH=(eta*uH*E-mu)*CH-J
    dCL=(eta*uL*E-mu)*CL+J
    assert np.isclose(dCH+dCL,(eta*(uL+du*x)*E-mu)*C)
    assert np.isclose((dCH-x*(dCH+dCL))/C,(eta-copying)*E*du*x*(1-x))

# Actual budget split between contributor returns and shared renewal.
B,h,c,fee,decay,activity_scale,E_floor = 4.,1.,1.,.2,1.,.1,.7
def appropriation_rhs(t,z,phi):
    E, x = np.exp(z[0]), expit(z[1])
    activity=E/(activity_scale+E)
    surplus=phi*B/(h+x)-c-fee*phi
    # E'=E*(public_flow/(L+E)-delta).
    return [(1-phi)*B*x/((h+x)*(activity_scale+E))-decay,
            activity*surplus]

appropriation = []
for phi in [.1,.3,.5,.8]:
    interior=phi*B/(c+fee*phi)-h
    selected_x=float(np.clip(interior,0,1))
    positive_E=(1-phi)*B*selected_x/(h+selected_x)/decay-activity_scale
    item={'retained_fraction':phi,'formal_selected_share':selected_x,
          'formal_positive_support':positive_E,
          'meets_strict_floor':positive_E>E_floor}
    # Formal roots are not asserted reachable when support vanishes.
    if positive_E > 0:
        sol=solve_ivp(lambda t,z:appropriation_rhs(t,z,phi),[0,1000],
                      [np.log(1.),np.log(.5/.5)],rtol=1e-10,atol=1e-12,max_step=.2)
        assert sol.success
        Efinal,xfinal=np.exp(sol.y[0,-1]),expit(sol.y[1,-1])
        assert abs(Efinal-positive_E)<1e-6
        assert abs(xfinal-selected_x)<1e-6
        item['numerical_final']=[float(Efinal),float(xfinal)]
    appropriation.append(item)
assert abs(appropriation[1]['formal_positive_support']-.226666666666666) < 1e-10
assert abs(appropriation[2]['formal_positive_support']-.8)<1e-12
assert abs(appropriation[3]['formal_positive_support']-.3)<1e-12
phi_star=np.sqrt(h*c/(B-h*fee))
raw_interior_peak=(np.sqrt(B-h*fee)-np.sqrt(h*c))**2/decay-activity_scale
assert 0 < phi_star*B/(c+fee*phi_star)-h < 1
phi_boundary=5/9
assert abs((1-phi_boundary)*B/(h+1)/decay-activity_scale-71/90)<1e-12
for test_x in [.2,.9,.9999]:
    actual_surplus=phi_boundary*B/(h+test_x)-c-fee*phi_boundary
    assert np.isclose(actual_surplus,10*(1-test_x)/(9*(1+test_x)))
    assert actual_surplus>0

# Logistic adoption with a mature seed and a fixed maturation delay.
epsilon, gain, delay, speed, flow_scale, reserve = .01,2.,2.,1.,1.,.5
q=epsilon/(1-epsilon)
def adoption(t, s=speed):
    return expit(np.log(q)+s*np.asarray(t))
def mature(t, s=speed):
    t=np.asarray(t)
    return np.where(t<delay,epsilon,adoption(t-delay,s))
def primitive_x(t,s=speed):
    return (np.logaddexp(0,np.log(q)+s*t)-np.log1p(q))/s
def support_change(t,s=speed):
    t=np.asarray(t)
    mature_integral=np.where(t<delay,epsilon*t,
                            epsilon*delay+primitive_x(np.maximum(t-delay,0),s))
    return flow_scale*(gain*mature_integral-primitive_x(t,s))

k=np.exp(speed*delay)
onset_threshold=gain*(1-epsilon)/(1-gain*epsilon)
w=(k-gain)/(gain-1)
t_min=np.log(w/q)/speed
required_reserve=max(0.,-float(support_change(t_min)))
t_established=delay+np.log(1/((gain-1)*q))/speed
t_cross=brentq(lambda t:reserve+float(support_change(t)),0,t_min)
assert abs(t_min-6.27949009892797)<1e-11
assert abs(required_reserve-.72916943260247)<1e-11
assert abs(t_cross-4.937242488202401)<1e-10
for t in [.25,1.,2.,4.,t_min,8.,12.]:
    numerical=quad(lambda z:flow_scale*(gain*float(mature(z))-float(adoption(z))),
                   0,t,points=[delay] if t>delay else None,epsabs=1e-11)[0]
    assert abs(numerical-float(support_change(t)))<1e-9

overlap_checks=[]
for s in [.25,.5,1.,2.]:
    area1=quad(lambda t:float(adoption(t,s)-mature(t,s)),0,delay,epsabs=1e-11)[0]
    area2=quad(lambda t:float(adoption(t,s)-mature(t,s)),delay,np.inf,epsabs=1e-10)[0]
    assert abs(area1+area2-delay*(1-epsilon))<1e-8
    grid=np.linspace(0,delay+20/s,10001)
    pending=adoption(grid,s)-mature(grid,s)
    assert np.min(pending)>-1e-12
    full_handoff_service=1-mature(grid,s)+gain*mature(grid,s)
    assert np.min(full_handoff_service)>=1
    overlap_checks.append({'speed':s,'integrated_overlap':area1+area2,
                           'expected':delay*(1-epsilon),
                           'sampled_peak_overlap':float(np.max(pending))})

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'text.color':'#22323F','axes.labelcolor':'#22323F'})
fig,axes=plt.subplots(1,3,figsize=(13.2,4.6),facecolor='#FCFCFA')
for idx,color,label in [(0,'#087F83','Inherited production dominates'),
                         (1,'#BD4E36','Current-cost copying dominates')]:
    t,z=practice_curves[idx]
    for ax,j in zip(axes,[2,1,0]):
        ax.plot(t,z[j],color=color,lw=2.3,label=label)
for ax,title,ylabel in zip(axes,['Practice share','Functioning capacity','Support stock'],
                          ['High-effort share x','Total repair capacity C','Support E']):
    ax.set(title=title,xlabel='Time (model units)',ylabel=ylabel,xlim=(0,60))
    ax.set_ylim(bottom=0)
    ax.set_facecolor('#FCFCFA')
    ax.grid(alpha=.17)
fig.suptitle('Transmission can undermine the practice sustaining repair',x=.065,ha='left',
             y=.985,fontsize=15,fontweight='bold')
fig.legend(*axes[0].get_legend_handles_labels(),loc='lower center',
           bbox_to_anchor=(.5,.05),ncol=2,frameon=False)
fig.text(.065,.015,'Illustrative model, not fitted data. Both cases start near the same '
         'functioning equilibrium. Only the copying response differs.',fontsize=9,color='#65737D')
fig.subplots_adjust(left=.065,right=.98,top=.80,bottom=.25,wspace=.28)
fig.savefig(OUT/'practice-transmission.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(OUT/'practice-transmission.svg',facecolor=fig.get_facecolor())

times=np.linspace(0,10,2001)
x,mature_share=adoption(times),mature(times)
fig,axes=plt.subplots(1,2,figsize=(11.8,4.6),facecolor='#FCFCFA')
axes[0].plot(times,1-x+gain*mature_share,color='#BD4E36',lw=2.3,label='Retire at adoption')
axes[0].plot(times,1-mature_share+gain*mature_share,color='#087F83',lw=2.3,
             label='Retain predecessor until maturation')
axes[0].axhline(1,color='#65737D',ls=':',label='Required service')
axes[0].set(title='Delivered function',ylabel='Service relative to requirement')
draw=-support_change(times)
axes[1].plot(times,draw,color='#BD4E36',lw=2.3)
axes[1].axhline(reserve,color='#65737D',ls='--',label='Initial reserve = 0.5')
axes[1].fill_between(times,reserve,draw,where=draw>reserve,color='#BD4E36',alpha=.16)
axes[1].plot(t_min,required_reserve,'o',color='#BD4E36')
axes[1].annotate('Required reserve: 0.729',xy=(t_min,required_reserve),
                 xytext=(4.6,1.07),arrowprops={'arrowstyle':'->','color':'#65737D'},fontsize=9)
axes[1].set(title='Cumulative draw with immediate retirement',ylabel='Draw on initial reserve',
            ylim=(-.4,1.35))
for ax in axes:
    ax.set_xlabel('Time (model units)')
    ax.set_xlim(0,10)
    ax.set_facecolor('#FCFCFA')
    ax.grid(alpha=.17)
    ax.legend(frameon=False,fontsize=8,loc='lower left')
axes[0].legend(frameon=False,fontsize=8,loc='upper left')
fig.suptitle('A better successor can spread before it can perform the work',x=.07,ha='left',
             y=.985,fontsize=15,fontweight='bold')
fig.text(.07,.08,'Illustrative model: mature successors deliver twice the service; '
         'new adopters take 2 time units to mature. Initial mature share: 1%.',fontsize=9)
fig.text(.07,.025,'Full predecessor retention requires 1.98 unit-times of duplicate '
         'capacity. This is sufficient overlap, not a universal minimum.',fontsize=9,color='#65737D')
fig.subplots_adjust(left=.07,right=.975,top=.80,bottom=.25,wspace=.25)
fig.savefig(OUT/'replacement-gap.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(OUT/'replacement-gap.svg',facecolor=fig.get_facecolor())

record={'status':'passed','scope':'Conditional mathematical examples, not empirical validation',
        'practice_transmission':{'parameters':dict(a=a,delta=delta,eta=eta,mu=mu,K=K,uH=uH,uL=uL),
                                 'critical_effort':ucrit,'cases':practice_cases},
        'appropriation':{'parameters':dict(B=B,h=h,c=c,fee=fee,decay=decay,
                                          activity_scale=activity_scale,E_floor=E_floor),
                         'cases':appropriation,'interior_optimal_retention':float(phi_star),
                         'interior_peak_support':float(raw_interior_peak),
                         'nonhyperbolic_boundary':{'phi':phi_boundary,'support':71/90,
                             'surplus_identity_verified':True,
                             'meaning':'zero linear exponent; quadratic decline of rare noncontributors'}},
        'replacement':{'parameters':dict(epsilon=epsilon,gain=gain,delay=delay,speed=speed,
                                        flow_scale=flow_scale,reserve=reserve),
                       'deficit_onset_exp_sL_threshold':onset_threshold,
                       'time_of_minimum_support':float(t_min),
                       'required_reserve':required_reserve,
                       'floor_crossing_time':float(t_cross),
                       'successor_alone_establishment_time':float(t_established),
                       'overlap_checks':overlap_checks},
        'limitations':['Transmission and retention mechanisms are specified assumptions.',
                       'Fixed operating scale in appropriation is not a population model.',
                       'Full-retention overlap is sufficient, not necessarily minimal.',
                       'No empirical experiment or deployment benchmark was run.']}
(OUT/'selection-and-replacement-checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
