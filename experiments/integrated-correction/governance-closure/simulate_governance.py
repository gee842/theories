"""Paid governance, arbitrary minority messages, and conditional robust control."""
from pathlib import Path
from dataclasses import dataclass, replace, asdict
import hashlib
import importlib.util
import json
import sys

import numpy as np
from scipy.special import expit, logit
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent / "constitutional-extension/verify_extension.py"
OUT = ROOT / "results"
spec = importlib.util.spec_from_file_location("paid_governance_base", BASE)
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)


@dataclass(frozen=True)
class Params:
    gamma: float = .02
    L: float = 1.1
    d: float = .3
    eta_J: float = 2500.
    nu_z: float = 100.
    theta: float = .9
    eta_C: float = 800 / 29
    eta_G: float = 1600 / 29


P = Params()
INITIAL = np.array([.94, .93, 2.7, 2.4, .5, .92, 1.])
FMIN = .15 * .9 * (1 + .8 * (2.5 / 3.5) ** 2)
ML, DELTA, ALPHA, R, EMAX = .48, .02, 4., .5, .002
MODES = ["funded", "exact_observation", "free_ideal", "fixed_reallocate", "paid_fixed",
         "no_withholding", "truth_capture", "router_bypass", "sensing_outage", "actuator_outage"]


def physical(state, p, mode="funded"):
    x, h, c, g, m, z, j = state
    q = (c / (1 + c)) ** 2
    r = 1 + .8 * q
    dcheck = h * g / (p.L + g)
    f = .15 * x * r
    v = (1 - p.gamma) * .5 * f
    w = p.gamma * f
    dgcheck = 0. if mode == "no_withholding" else dcheck
    sx = .8 * q * dcheck - .15 * r
    sh = 10 * v * (dcheck - m)
    sz = p.nu_z * w * (dgcheck - p.d)
    dc = p.eta_C * (1 - p.gamma) * .5 * f - c
    dg = p.eta_G * m * h * v - g
    dj = p.eta_J * p.d * z * w - j
    deriv = np.array([x * (1-x) * sx, h * (1-h) * sh, dc, dg, 0., z * (1-z) * sz, dj])
    # Nine spending/retention/reserve flows; neither reserve is productive.
    ledger = np.array([(1-p.gamma)*.5*f, m*h*v, (1-m)*h*v,
                       (1-h)*(1-dcheck)*v, (1-h)*dcheck*v,
                       p.d*z*w, (1-p.d)*z*w, (1-z)*(1-dgcheck)*w, (1-z)*dgcheck*w])
    return deriv, (sx, sh, sz), (dcheck, f, v, w), ledger


def weighted_median(values, weights):
    order = np.argsort(values)
    ww = np.asarray(weights)[order]
    index = min(np.searchsorted(np.cumsum(ww), .5 * sum(weights), side="left"), len(order)-1)
    return float(np.asarray(values)[order[index]])


def honest_filter(y_g, y_m, target, p, epsilon=EMAX):
    # Every coordinate in this error box is covered; the median coordinates
    # need not originate from one sensor or form a realizable latent state.
    gl = max(2.1, y_g - epsilon)
    ml = max(ML, y_m - epsilon)
    mu = min(1., y_m + epsilon)
    lo = max(-R, -ALPHA * (ml-ML))
    k = p.eta_G * .9 * (1-p.gamma) * .5 * FMIN
    upper = .9 * p.L / (p.L+gl)**2 * (k*mu-gl) + ALPHA*(.9*gl/(p.L+gl)-mu-DELTA)
    hi = min(R, upper)
    if ml > mu + 1e-10 or lo > hi + 1e-10:
        return 0., lo, hi, False
    nominal = y_m * (1-y_m) * (target-y_g)
    return float(np.clip(nominal, lo, hi)), lo, hi, True


def certificate(state, p=P, theta=None):
    x,h,c,g,m,z,j = state
    theta = p.theta if theta is None else theta
    return np.array([x-.9,h-.9,c-2.5,g-2.1,m-ML,.9*g/(p.L+g)-m-DELTA,z-.9,j-1,theta*z-.5])


def command(t, state, target, p, mode, phase_active=False):
    x,h,c,g,m,z,j = state
    theta = .45 if mode == "truth_capture" and phase_active else p.theta
    honest_weight = theta*z
    # These controls do not use the paid observation channel at all. Avoid
    # evaluating a deliberately depleted, unused sensor in the benchmark.
    if mode in ("free_ideal", "fixed_reallocate"):
        accepted=0.;low=-R;high=R
        if mode=="free_ideal":
            deriv,_,terms,_=physical(state,p,mode)
            dd=g/(p.L+g)*deriv[1]+h*p.L/(p.L+g)**2*deriv[3]
            low=max(-R,-2*(m-.45))
            high=min(R,dd+2*(terms[0]-m-.02))
            accepted=float(np.clip(m*(1-m)*(target-g),low,high)) if low<=high else 0.
        return accepted,{"truthful_weight":honest_weight,"error_bound":None,"yg":None,"ym":None,
                         "feasible_honest_interval":low<=high,"lower":low,"upper":high,
                         "accepted_command":accepted,"capacity":R if mode=="free_ideal" else 0.,"theta":theta}
    err = .002 / max(j, 1e-200)
    if mode == "exact_observation":
        err = 0.
    oscillation = np.array([np.sin(.7*t), np.cos(.9*t), np.sin(1.3*t+1)])
    weights = [honest_weight/3]*3 + [1-honest_weight]
    # The dishonest mass includes both lying maintainers and shirkers.
    yg = weighted_median([*(g+err*oscillation),g+20], weights)
    ym = weighted_median([*(m+err*oscillation[::-1]),m-.4], weights)
    estimate_bound = 0. if mode == "exact_observation" else EMAX
    good, lo, hi, feasible = honest_filter(yg, ym, target, p, estimate_bound)
    outage = mode == "sensing_outage" and phase_active
    if outage:
        good, feasible = 0., False
    malicious = R*(1-m)  # valid physical range, pushes demands toward one
    accepted = weighted_median([good, malicious], [honest_weight,1-honest_weight])
    if mode == "router_bypass" and phase_active:
        accepted = malicious
    if mode == "paid_fixed":
        accepted = 0.
    capacity = j/(1+j)
    actual = float(np.clip(accepted,-capacity,capacity))
    if mode == "actuator_outage" and phase_active:
        actual = 0.
    return actual, {"truthful_weight":honest_weight,"error_bound":err,"yg":yg,"ym":ym,
                    "feasible_honest_interval":feasible,"lower":lo,"upper":hi,
                    "accepted_command":accepted,"capacity":j/(1+j),"theta":theta}


def encode(s):
    return np.array([logit(s[0]),logit(s[1]),np.log(s[2]),np.log(s[3]),s[4],logit(s[5]),np.log(s[6])])


def decode(y):
    return np.array([expit(y[0]),expit(y[1]),np.exp(y[2]),np.exp(y[3]),y[4],expit(y[5]),np.exp(y[6])])


def simulate(mode="funded",p=P,initial=INITIAL,schedule=((500.,3.8),),method="DOP853",step=.25):
    if mode in ("free_ideal","fixed_reallocate"):
        p=replace(p,gamma=0.,L=1.)
    # All interventions occur at a segment boundary; state is continuous.
    boundaries={0.,100.,sum(v[0] for v in schedule)}
    offset=0.
    for duration,_ in schedule:
        offset+=duration;boundaries.add(offset)
    endtime=sum(v[0] for v in schedule)
    boundaries=sorted(t for t in boundaries if t<=endtime)
    schedule_end=np.cumsum([v[0] for v in schedule])
    y0=encode(initial)
    times=[];states=[];targets=[];diagnostics=[];rates=[];log_states=[]
    for start,end in zip(boundaries[:-1],boundaries[1:]):
        target=schedule[np.searchsorted(schedule_end,start,side="right")][1]
        active=start>=100.
        def rhs(t,y):
            s=decode(y)
            d,slopes,_,_=physical(s,p,mode)
            u=command(t,s,target,p,mode,active)[0]
            return [slopes[0],slopes[1],d[2]/s[2],d[3]/s[3],u,slopes[2],d[6]/s[6]]
        sol=solve_ivp(rhs,(start,end),y0,method=method,rtol=3e-9,atol=3e-11,max_step=.5,dense_output=True)
        assert sol.success,sol.message
        tt=np.linspace(start,end,int(round((end-start)/step))+1)
        ys=sol.sol(tt);ss=decode(ys)
        for i,t in enumerate(tt):
            u,info=command(t,ss[:,i],target,p,mode,active)
            times.append(t);states.append(ss[:,i]);targets.append(target);rates.append(u);diagnostics.append(info);log_states.append(ys[:,i])
        y0=sol.y[:,-1]
    t=np.array(times);s=np.array(states).T;target=np.array(targets);u=np.array(rates)
    truth=np.array([v["truthful_weight"] for v in diagnostics])
    theta=np.array([v["theta"] for v in diagnostics])
    margins=certificate(s,p,theta)
    ledger=np.array([physical(s[:,i],p,mode)[3] for i in range(len(t))]).T
    fees=.15*s[0]*(1+.8*(s[2]/(1+s[2]))**2)
    majority_lost=np.flatnonzero(truth<=.5)
    jlow=np.flatnonzero(s[6]<1-1e-6)
    phase_errors=[];offset=0.
    for duration,value in schedule:
        end=offset+duration
        select=(t>end-min(20.,duration/5))&(t<=end)&(target==value)
        phase_errors.append(float(np.max(abs(s[3,select]-value))))
        offset=end
    summary={"mode":mode,"parameters":asdict(p),"initial":list(map(float,initial)),
             "initial_margins":certificate(initial,p).tolist(),"final_state_x_h_C_G_m_z_J":s[:,-1].tolist(),
             "minimum_margins_x_h_C_G_m_b_z_J_truth":margins.min(axis=1).tolist(),
             "operating_floor_breach":bool(margins[:4].min() < -1e-6),
             "all_protected_state_bounds_preserved":bool(margins.min() >= -1e-6),
             "phase_late_max_target_errors":phase_errors,
             "first_truth_majority_loss":float(t[majority_lost[0]]) if len(majority_lost) else None,
             "first_J_floor_breach":float(t[jlow[0]]) if len(jlow) else None,
             "minimum_truthful_weight":float(truth.min()),"minimum_J":float(s[6].min()),
             "integrated_fee":float(np.trapezoid(fees,t)),"integrated_ledger_flows":np.trapezoid(ledger,t,axis=1).tolist(),
             "maximum_ledger_residual":float(np.max(abs(ledger.sum(axis=0)-fees))),
             "rule_total_variation":float(np.trapezoid(abs(u),t)),
             "minimum_margin_controller_upper_minus_lower":float(min(v["upper"]-v["lower"] for v in diagnostics)),
             "fraction_samples_without_feasible_honest_proposal":float(np.mean([not v["feasible_honest_interval"] for v in diagnostics]))}
    return {"t":t,"state":s,"log_state":np.array(log_states).T,"target":target,"u":u,"truth":truth,"summary":summary}


def algebra():
    rng=np.random.default_rng(20261005)
    differences=[];ledgers=[];median_errors=[];gaps=[]
    for _ in range(2000):
        x,h=rng.uniform(.9,.999,2);c=rng.uniform(2.5,4);g=rng.uniform(2.1,8)
        m=rng.uniform(ML,.9*g/(P.L+g)-DELTA);z=rng.uniform(.9,.999);j=rng.uniform(1,5)
        s=[x,h,c,g,m,z,j]
        d,slopes,terms,flows=physical(s,P)
        # Existing equations after redirecting both budgets have corresponding
        # conversion coefficients; this is only a derivative cross-check.
        pp=base.replace(base.Parameters(),eta_c=P.eta_C*(1-P.gamma),eta_g=P.eta_G*(1-P.gamma),L=P.L,work_fraction=m)
        old=base.physical_rhs(s[:4],pp)
        # h's selection clock also uses the reduced verification budget.
        old[1]*=1-P.gamma
        differences.append(np.max(abs(d[:4]-old)))
        ledgers.append(abs(sum(flows)-terms[1]))
        reports=np.r_[g+rng.uniform(-EMAX,EMAX,5),rng.uniform(-1e6,1e6,3)]
        weights=np.r_[np.full(5,.81/5),np.full(3,.19/3)]
        med=weighted_median(reports,weights)
        median_errors.append(abs(med-g))
        for eg,em in ((-EMAX,-EMAX),(-EMAX,EMAX),(EMAX,-EMAX),(EMAX,EMAX)):
            u,lo,hi,ok=honest_filter(g+eg,m+em,4.,P)
            assert ok
            gaps.append(hi-lo)
            deriv,_,_,_=physical(s,P)
            bdot=.9*P.L/(P.L+g)**2*deriv[3]-u
            assert bdot+ALPHA*(.9*g/(P.L+g)-m-DELTA)>-1e-10
            assert u+ALPHA*(m-ML)>-1e-10
    assert max(differences)<1e-12 and max(ledgers)<1e-12 and max(median_errors)<=EMAX+1e-12
    dmin=.9*2.1/(P.L+2.1)
    lips_g=.9*P.L*(ALPHA+1)/(P.L+2.1)**2
    width=ALPHA*(dmin-ML-DELTA)-.225-2*EMAX*lips_g-4*ALPHA*EMAX
    lower=1/(P.eta_J*P.d*.9*FMIN)
    upper_c=1-2.5/(P.eta_C*.5*FMIN)
    upper_g=1-2.1/(P.eta_G*ML*.9*.5*FMIN)
    cstar=brentq(lambda c:P.eta_C*(1-P.gamma)*.5*.15*(1+.8*(c/(1+c))**2)-c,2,4)
    fstar=.15*(1+.8*(cstar/(1+cstar))**2)
    return {"max_derivative_difference":float(max(differences)),"max_ledger_residual":float(max(ledgers)),
            "max_median_error":float(max(median_errors)),"minimum_sampled_rate_interval_width":float(min(gaps)),
            "analytic_interval_width_lower_bound":width,"sampled_safe_states":2000,
            "funding_bounds_for_declared_floors":[lower,min(upper_c,upper_g)],
            "fee_window_separate_upper_C_G":[upper_c,upper_g],
            "clean_C_equilibrium":cstar,"clean_J_equilibrium":P.eta_J*P.d*P.gamma*fstar}


def run():
    OUT.mkdir(parents=True,exist_ok=True)
    checks=algebra()
    cases={"constant":[(500.,3.8)],"changing":[(100.,v) for v in (3.6,3.9,3.,4.7,3.8)]}
    data={}
    for name,schedule in cases.items():
        data[name]={}
        for mode in MODES:
            tr=simulate(mode,schedule=schedule)
            data[name][mode]=tr
            assert tr["summary"]["maximum_ledger_residual"]<1e-12
            if mode in ("funded","exact_observation"):
                assert tr["summary"]["all_protected_state_bounds_preserved"],tr["summary"]
            print(json.dumps({"case":name,"mode":mode,"complete":True}),flush=True)
    sweeps={"gamma":[],"theta":[],"initial_z":[]}
    corner=[.9,.9,2.5,2.1,.48,.9,1.]
    for gamma in (.002,.005,.008,.02,.04,.05,.08):
        tr=simulate(p=replace(P,gamma=gamma),initial=corner,schedule=[(300.,3.8)],step=.5)
        sweeps["gamma"].append({"gamma":gamma,"summary":tr["summary"]})
    for theta in (.45,.55,.6,.9):
        tr=simulate(p=replace(P,theta=theta),schedule=[(300.,3.8)],step=.5)
        sweeps["theta"].append({"theta":theta,"summary":tr["summary"]})
    for z in (.6,.8,.9,.95):
        initial=INITIAL.copy();initial[5]=z
        tr=simulate(initial=initial,schedule=[(300.,3.8)],step=.5)
        sweeps["initial_z"].append({"initial_z":z,"summary":tr["summary"]})
    independent={}
    for name,mode in (("constant","funded"),("changing","funded"),("constant","truth_capture")):
        other=simulate(mode,schedule=cases[name],method="Radau")
        error=float(np.max(abs(other["state"]-data[name][mode]["state"])))
        independent[name+"/"+mode]=error
        assert error<3e-5,(name,mode,error)
    result={"scope":"Conditional paid governance model; deterministic bounded-error technology; no empirical fitting.",
            "algebra":checks,"cases":{name:{mode:tr["summary"] for mode,tr in modes.items()} for name,modes in data.items()},
            "sweeps":sweeps,"second_solver_max_state_errors":independent,
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "baseline_sha256":hashlib.sha256(BASE.read_bytes()).hexdigest(),
            "protocol_sha256":hashlib.sha256((ROOT/"PROTOCOL.md").read_bytes()).hexdigest()}
    (OUT/"analysis.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(OUT/"trajectories.npz",**{f"{name}_{mode}_{key}":value for name,modes in data.items() for mode,tr in modes.items() for key,value in tr.items() if isinstance(value,np.ndarray)})
    plot(data)
    print(json.dumps({"completed":True,"algebra":checks,"solver_errors":independent}),flush=True)


def plot(data):
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.spines.top":False,"axes.spines.right":False})
    fig,ax=plt.subplots(2,2,figsize=(12,8),layout="constrained")
    colors={"funded":"#247B64","free_ideal":"#4267AE","paid_fixed":"#BB8B2F","truth_capture":"#B24B42","no_withholding":"#9169A5"}
    labels={"funded":"Paid robust governance","free_ideal":"Free ideal-state benchmark","paid_fixed":"Paid fixed rule","truth_capture":"Truthful majority removed","no_withholding":"Governance withholding removed"}
    for mode in ("funded","free_ideal","paid_fixed"):
        tr=data["changing"][mode]
        ax[0,0].plot(tr["t"],tr["state"][3],color=colors[mode],lw=1.8,label=labels[mode])
    tr=data["changing"]["funded"]
    ax[0,0].plot(tr["t"],tr["target"],ls=":",color="black",label="Requested target")
    ax[0,0].set(title="A. Financing and limited information constrain tracking",xlabel="Time",ylabel="Verification G")
    ax[0,0].legend(frameon=False,fontsize=8,loc="lower right")
    for mode in ("funded","truth_capture","no_withholding"):
        tr=data["constant"][mode]
        ax[0,1].plot(tr["t"],tr["state"][6],color=colors[mode],lw=1.8,label=labels[mode])
        ax[1,0].plot(tr["t"],tr["truth"],color=colors[mode],lw=1.8,label=labels[mode])
        ax[1,1].plot(tr["t"],tr["state"][3],color=colors[mode],lw=1.8,label=labels[mode])
    ax[0,1].axhline(1,color="black",ls=":",lw=1)
    ax[0,1].set(title="B. Observation and actuation require maintained capacity",xlabel="Time",ylabel="Governance capacity J")
    ax[0,1].legend(frameon=False,fontsize=8)
    ax[1,0].axhline(.5,color="black",ls=":",lw=1)
    ax[1,0].set(title="C. Paid delivery and truthful command weight differ",xlabel="Time",ylabel="Truthful command weight")
    ax[1,1].set(title="D. Loss of a prerequisite can defeat correction",xlabel="Time",ylabel="Verification G")
    fig.suptitle("Paid governance with a maintained truthful majority",fontsize=16)
    fig.supxlabel("Specified model · bounded sensor error · arbitrary minority messages · protected identity and command path",fontsize=9)
    fig.savefig(OUT/"governance-closure.png",dpi=180)
    fig.savefig(OUT/"governance-closure.svg")
    plt.close(fig)


if __name__=="__main__":run()
