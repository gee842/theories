"""Audit of paid access checks and selected maintenance honesty.

No empirical data. The two role populations are distinct. Withheld payments
enter a recorded, inert reserve and cannot automatically replenish either stock.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, replace
from pathlib import Path
import hashlib
import json
import platform

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize
from scipy.special import expit, logit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


@dataclass(frozen=True)
class Parameters:
    y0: float = 1.
    B: float = .8
    chi: float = 1.
    K: float = 1.
    L: float = 1.
    eta_c: float = 800./29.
    eta_g: float = 1600./29.
    mu_c: float = 1.
    mu_g: float = 1.
    kappa: float = 1.
    nu: float = 10.
    tau: float = .15
    allocation: float = .5
    work_fraction: float = .5

    @property
    def A(self):
        return self.chi*self.B


def terms(x, h, c, g, p, mode="ordinary"):
    q = (c/(p.K+c))**2 if mode != "no_signal" else 0.0*c
    detection = h*g/(p.L+g)
    if mode == "no_verification":
        detection = 0.0*g
    escrow_detection = detection if mode != "no_withholding" else 0.0*detection
    r = p.y0+p.A*q
    funds = p.tau*x*r
    verifier_budget = (1.-p.allocation)*funds
    user_advantage = detection*p.A*q-p.tau*r
    custodian_advantage = verifier_budget*(escrow_detection-p.work_fraction)
    return q, detection, escrow_detection, r, funds, verifier_budget, user_advantage, custodian_advantage


def physical_rhs(state, p, mode="ordinary"):
    x,h,c,g = state
    _,_,_,_,funds,v,su,sg = terms(x,h,c,g,p,mode)
    delivered = 0.0 if mode == "undelivered_verification" else 1.0
    return np.array([p.kappa*x*(1-x)*su, p.nu*h*(1-h)*sg,
                     p.eta_c*p.allocation*funds-p.mu_c*c,
                     delivered*p.eta_g*p.work_fraction*h*v-p.mu_g*g])


def jacobian(state, p):
    x,h,c,g = state
    q,d,_,r,f,v,su,sg = terms(x,h,c,g,p)
    qp = 2*c*p.K/(p.K+c)**3
    prob = g/(p.L+g)
    pp = p.L/(p.L+g)**2
    vx = (1-p.allocation)*p.tau*r
    vc = (1-p.allocation)*p.tau*x*p.A*qp
    e = d-p.work_fraction
    return np.array([
        [p.kappa*(1-2*x)*su, p.kappa*x*(1-x)*prob*p.A*q,
         p.kappa*x*(1-x)*(d-p.tau)*p.A*qp, p.kappa*x*(1-x)*h*pp*p.A*q],
        [p.nu*h*(1-h)*vx*e, p.nu*((1-2*h)*v*e+h*(1-h)*v*prob),
         p.nu*h*(1-h)*vc*e, p.nu*h*(1-h)*v*h*pp],
        [p.eta_c*p.allocation*p.tau*r, 0.,
         p.eta_c*p.allocation*p.tau*x*p.A*qp-p.mu_c, 0.],
        [p.eta_g*p.work_fraction*h*vx, p.eta_g*p.work_fraction*v,
         p.eta_g*p.work_fraction*h*vc, -p.mu_g],
    ])


def trajectory(initial, p, horizon=600., mode="ordinary", method="DOP853", samples=2001):
    x,h,c,g = initial
    assert 0<x<1 and 0<h<1 and c>0 and g>0
    start = [logit(x),logit(h),np.log(c),np.log(g),0.]

    def rhs(_t,z):
        xx,hh,cc,gg = expit(z[0]),expit(z[1]),np.exp(z[2]),np.exp(z[3])
        _,_,de,_,f,v,su,sg = terms(xx,hh,cc,gg,p,mode)
        delivered = 0.0 if mode == "undelivered_verification" else 1.0
        return [p.kappa*su, p.nu*sg,
                p.eta_c*p.allocation*f/cc-p.mu_c,
                delivered*p.eta_g*p.work_fraction*hh*v/gg-p.mu_g,
                (1-hh)*de*v]

    sol=solve_ivp(rhs,(0,horizon),start,method=method,rtol=1e-10,atol=2e-12,dense_output=True)
    assert sol.success,sol.message
    t=np.linspace(0,horizon,samples)
    z=sol.sol(t)
    return {"t":t,"x":expit(z[0]),"h":expit(z[1]),"C":np.exp(z[2]),"G":np.exp(z[3]),
            "reserve":z[4],"log_odds_x":z[0],"log_odds_h":z[1],"log_C":z[2],"log_G":z[3]}


def equilibrium(p):
    top=p.eta_c*p.allocation*p.tau*(p.y0+p.A)/p.mu_c
    c=brentq(lambda c:p.eta_c*p.allocation*p.tau*(p.y0+p.A*(c/(p.K+c))**2)-p.mu_c*c,
             0,top*1.01+1e-12,xtol=1e-13)
    f=p.tau*(p.y0+p.A*(c/(p.K+c))**2)
    g=p.eta_g*p.work_fraction*(1-p.allocation)*f/p.mu_g
    state=np.array([1.,1.,c,g])
    t=terms(*state,p)
    return {"state":state.tolist(),"funding":float(f),"user_margin":float(t[-2]),
            "custodian_return_margin":float(t[-1]),
            "custodian_probability_margin":float(g/(p.L+g)-p.work_fraction),
            "eigenvalues":np.linalg.eigvals(jacobian(state,p)).tolist()}


def design_threshold(a,b,m):
    # a,b already include output costs of both technology and custodian earnings.
    cubic=lambda g:b*g**3-a*g-2*a
    upper=1.
    while cubic(upper)<=0: upper*=2
    g_star=brentq(cubic,1e-14,upper)
    g_min=m/(1-m)
    g=max(g_star,g_min)
    c=(1+np.sqrt(1+8*b*g/a))/2
    value=(a*c+b*g)/((c/(1+c))**2*g/(1+g))
    return {"A_critical":float(value),"c":float(c),"g":float(g),
            "g_unconstrained":float(g_star),"g_honesty_floor":float(g_min),
            "honesty_constraint_active":bool(g_min>=g_star)}


def summary(tr):
    return {"final":{k:float(tr[k][-1]) for k in ("x","h","C","G","reserve")},
            "max_payer_share":float(tr["x"].max()),
            "horizon":float(tr["t"][-1])}


def run():
    OUT.mkdir(exist_ok=True)
    p=Parameters()
    eq=equilibrium(p)
    assert np.max(np.abs(np.array(eq["state"])-[1,1,3,3]))<1e-11
    assert abs(eq["user_margin"]-.12)<1e-12
    assert abs(eq["custodian_return_margin"]-.0271875)<1e-12
    assert max(eq["eigenvalues"])<0
    floor=np.array([.9,.9,2.5,2.1])
    box_terms=terms(*floor,p)
    lower_margins={"user_return":float(box_terms[-2]),
                   "custodian_detection_minus_cost":float(box_terms[1]-p.work_fraction),
                   "C_inward":float(physical_rhs(floor,p)[2]),
                   "G_inward":float(physical_rhs(floor,p)[3])}
    assert min(lower_margins.values())>0

    rng=np.random.default_rng(20261006)
    account_errors=[]
    derivative_errors=[]
    for _ in range(300):
        pp=replace(p,chi=rng.uniform(0,1),tau=rng.uniform(.02,.8),
                   allocation=rng.uniform(.05,.95),work_fraction=rng.uniform(.05,.95))
        state=np.array([rng.uniform(.01,.99),rng.uniform(.01,.99),rng.uniform(.1,10),rng.uniform(.1,10)])
        x,h,c,g=state
        for mode in ("ordinary","no_withholding"):
            q,d,de,r,f,v,_,_=terms(x,h,c,g,pp,mode)
            served=x+(1-x)*(1-d)
            common=(1-pp.chi)*pp.B*q*served
            gross=pp.y0+pp.B*q*served
            users=x*((1-pp.tau)*r+common)+(1-x)*(pp.y0+(1-d)*pp.A*q+common)
            service=pp.allocation*f
            verifier=pp.work_fraction*h*v
            honest_earnings=h*(1-pp.work_fraction)*v
            fraud_earnings=(1-h)*(1-de)*v
            withheld=(1-h)*de*v
            error=abs(users+service+verifier+honest_earnings+fraud_earnings+withheld-gross)
            assert error<2e-14
            account_errors.append(error)
        eps=1e-5
        finite=np.column_stack([(physical_rhs(state+eps*np.eye(4)[j],pp)-physical_rhs(state-eps*np.eye(4)[j],pp))/(2*eps) for j in range(4)])
        derivative_errors.append(float(np.max(np.abs(finite-jacobian(state,pp)))))
    assert max(derivative_errors)<1e-7

    designs=[]
    for _ in range(160):
        a,b=np.exp(rng.uniform(-6,-1,2))
        m=rng.uniform(.1,.9)
        analytic=design_threshold(a,b,m)
        gmin=m/(1-m)
        def objective(log_state):
            c,g=np.exp(log_state)
            return (a*c+b*g)/((c/(1+c))**2*g/(1+g))
        solutions=[]
        for guess in ((1.,max(gmin,1.)),(5.,max(gmin,5.)),(.3,max(gmin,.3))):
            sol=minimize(objective,np.log(guess),method="L-BFGS-B",
                         bounds=[(-8,10),(np.log(gmin),10)],
                         options={"ftol":1e-14,"gtol":1e-9,"maxiter":1500})
            solutions.append(sol)
        best=min(solutions,key=lambda s:s.fun)
        assert abs(best.fun-analytic["A_critical"])/analytic["A_critical"]<1e-7
        # Strictly above the threshold, construct an actual stable policy.
        aa=1.2*analytic["A_critical"]
        gg=max(analytic["g"],1.01*gmin)
        cc=(1+np.sqrt(1+8*b*gg/a))/2
        funding=a*cc+b*gg
        y0=max(1.,aa/.8)
        pp=replace(p,y0=y0,B=aa/.8,chi=.8,eta_c=1/a,eta_g=1/(b*m),
                   work_fraction=m,tau=funding/(y0+aa*(cc/(1+cc))**2),
                   allocation=a*cc/funding)
        derived=equilibrium(pp)
        assert max(derived["eigenvalues"])<0
        assert derived["user_margin"]>0 and derived["custodian_probability_margin"]>0
        designs.append({"a":float(a),"b":float(b),"m":float(m),"analytic":analytic,
                        "optimized_threshold":float(best.fun),"policy":asdict(pp),"equilibrium":derived})

    a=p.mu_c*p.K/p.eta_c
    b=p.mu_g*p.L/(p.eta_g*p.work_fraction)
    threshold=design_threshold(a,b,p.work_fraction)
    assert abs(threshold["A_critical"]-.4726017227793541)<1e-12
    initial=(.94,.93,2.7,2.4)
    trajectories={
        "accountable":trajectory(initial,p),
        "depleted_service":trajectory((.1,.93,.2,2.4),p),
        "no_withholding":trajectory(initial,p,mode="no_withholding"),
        "low_honest_share":trajectory((.94,.49,2.7,2.4),p),
        "infrastructure_only_seed":trajectory((.94,.49,100.,100.),p),
        "no_verification":trajectory(initial,p,mode="no_verification"),
        "undelivered_verification":trajectory(initial,p,mode="undelivered_verification"),
        "no_signal":trajectory(initial,p,mode="no_signal"),
        "custodian_incentive_failure":trajectory((.99,.99,3.,5.4),replace(p,work_fraction=.9),horizon=1000.),
    }
    # Exploratory repair after the first verification run. Both initial stocks
    # and the contract are imposed interventions, not endogenously selected.
    repair_p=replace(p,work_fraction=.2)
    repair_floor=np.array([.98,.99,2.9,1.05])
    repair_terms=terms(*repair_floor,repair_p)
    repair_rhs=physical_rhs(repair_floor,repair_p)
    assert repair_terms[-2]>0 and repair_terms[1]>repair_p.work_fraction
    assert min(repair_rhs[2:])>0
    trajectories["contract_only"]=trajectory((.94,.49,2.7,2.4),repair_p,horizon=1000.)
    trajectories["contract_and_capacity"]=trajectory((.94,.49,100.,100.),repair_p,horizon=1000.)
    for key,f in zip(("x","h","C","G"),floor):
        assert trajectories["accountable"][key].min()>=f-1e-8
    for key,val in zip(("x","h","C","G"),[1,1,3,3]):
        assert abs(trajectories["accountable"][key][-1]-val)<1e-7
    for name,tr in trajectories.items():
        if name not in ("accountable","contract_and_capacity"):
            assert max(tr[k][-1] for k in ("x","C","G"))<1e-7,(name,summary(tr))
        assert tr["h"][-1]>0
        assert np.diff(tr["reserve"]).min()>-1e-9
    failure_eq=equilibrium(replace(p,work_fraction=.9))
    assert failure_eq["user_margin"]>0 and failure_eq["custodian_probability_margin"]<0
    assert max(failure_eq["eigenvalues"])>0
    repair_eq=equilibrium(repair_p)
    repair=trajectories["contract_and_capacity"]
    in_box=np.ones(len(repair["t"]),dtype=bool)
    for k,lower,target in zip(("x","h","C","G"),repair_floor,repair_eq["state"]):
        in_box &= repair[k]>=lower
        assert abs(repair[k][-1]-target)<1e-7
    entry_indices=np.flatnonzero(in_box)
    assert len(entry_indices)>0

    second=trajectory(initial,p,method="Radau")
    discrepancy=max(np.max(np.abs(second[k]-trajectories["accountable"][k])) for k in ("x","h","C","G","reserve"))
    assert discrepancy<1e-7

    result={"status":"All specified model checks passed; not empirical validation.",
            "parameters":asdict(p),"equilibrium":eq,"protected_floor":floor.tolist(),
            "protected_floor_margins":lower_margins,"joint_design_threshold":threshold,
            "accounting_cases":len(account_errors),"max_accounting_error":max(account_errors),
            "jacobian_cases":len(derivative_errors),"max_jacobian_error":max(derivative_errors),
            "design_cases":len(designs),
            "active_honesty_constraints":sum(d["analytic"]["honesty_constraint_active"] for d in designs),
            "trajectories":{name:summary(tr) for name,tr in trajectories.items()},
            "user_only_success_custodian_failure_equilibrium":failure_eq,
            "exploratory_joint_repair":{"changed_work_fraction":.2,"protected_floor":repair_floor.tolist(),
                                        "first_sample_in_proved_region":float(repair["t"][entry_indices[0]]),
                                        "equilibrium":repair_eq,
                                        "meaning":"Imposed contract revision and supplied initial stocks; no endogenous adoption or cost-optimality claim."},
            "integration_max_difference":float(discrepancy),
            "versions":{"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,"matplotlib":matplotlib.__version__},
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/"verification.json").write_text(json.dumps(result,indent=2)+"\n")
    (OUT/"design-checks.json").write_text(json.dumps(designs,indent=2)+"\n")
    np.savez_compressed(OUT/"trajectories.npz",**{f"{name}_{key}":arr for name,tr in trajectories.items() for key,arr in tr.items()})
    plot(p,trajectories)
    print(json.dumps(result,indent=2))


def plot(p,tr):
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.spines.top":False,"axes.spines.right":False})
    fig,axes=plt.subplots(2,2,figsize=(12,8.5),layout="constrained")
    green,red,blue,amber="#247B64","#B24B42","#4267AE","#AE7B22"
    cases=(("accountable",green,"Paid checks + withheld fraudulent payments"),
           ("no_withholding",red,"Payment consequence disabled"),
           ("custodian_incentive_failure",amber,"Users initially benefit; fraud pays"))
    for ax,key,title in ((axes[0,0],"x","A. Payer participation"),(axes[0,1],"h","B. Custodians performing maintenance")):
        for name,color,label in cases:
            ax.plot(tr[name]["t"],tr[name][key],color=color,lw=2,label=label)
        ax.set(xlim=(0,220),ylim=(0,1.03),xlabel="Time",ylabel="Population share",title=title)
    axes[0,0].legend(fontsize=8,frameon=False,loc="center right")
    axes[0,1].axhline(.5,color="#888888",ls="--",lw=.8)
    axes[0,1].text(110,.52,"Reference maintenance cost fraction",color="#666666",fontsize=8)
    ax=axes[1,0]
    for name,color,label in cases[:2]:
        ax.plot(tr[name]["t"],tr[name]["G"],color=color,lw=2,label=label)
    ax.set(xlim=(0,150),ylim=(0,3.2),xlabel="Time",ylabel="Verification capacity G",title="C. Protection itself requires funded work")
    ax=axes[1,1]
    for name,color,label in (("accountable",green,"Healthy practice and capacity"),
                             ("low_honest_share",red,"Honest share .49, ordinary capacity"),
                             ("infrastructure_only_seed",blue,"Honest share .49, both capacities 100"),
                             ("contract_and_capacity",amber,"Both capacities 100 + revised contract")):
        ax.plot(tr[name]["t"],tr[name]["x"],color=color,lw=2,label=label)
    ax.set(xlim=(0,180),ylim=(0,1.03),xlabel="Time",ylabel="Payer participation x",title="D. Infrastructure alone need not restore an institution")
    ax.legend(fontsize=8,frameon=False,loc="center right")
    fig.suptitle("Maintaining correction includes maintaining accountable custodians",fontsize=16)
    fig.supxlabel("Illustrative model · two role populations · specified bypass and false-claim threats · no empirical fitting",fontsize=10)
    fig.savefig(OUT/"accountable-maintenance.png",dpi=180)
    fig.savefig(OUT/"accountable-maintenance.svg")
    plt.close(fig)


if __name__=="__main__":
    run()
