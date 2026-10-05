"""Exploratory basin and cross-level feedback analysis. No empirical data."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import expit, logit

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/"constitutional-extension/verify_extension.py"
spec=importlib.util.spec_from_file_location("constitutional_model",BASE)
base=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=base
spec.loader.exec_module(base)
P=base.Parameters()
OUT=ROOT/"results"


def vector_rhs(z):
    x,h=expit(z[:2]);c,g=np.exp(z[2:])
    q=(c/(1+c))**2
    d=h*g/(1+g)
    r=1+.8*q
    f=.15*x*r
    v=.5*f
    return np.array([d*.8*q-.15*r,10*v*(d-.5),
                     P.eta_c*.5*f/c-1,P.eta_g*.5*h*v/g-1])


def classify(x,h,c,g):
    labels=np.zeros_like(x,dtype=np.int8)
    labels[(h<.5-1e-8)|((x<.15-1e-8)&(c<.4-1e-8))]=-1
    labels[(x>.9+1e-8)&(h>.9+1e-8)&(c>2.5+1e-8)&(g>2.1+1e-8)]=1
    return labels


def basin_grid(n=51,step=.04,horizon=600.):
    values=np.linspace(.01,.99,n)
    xx,hh=np.meshgrid(values,values)
    z=np.array([logit(xx.ravel()),logit(hh.ravel()),
                np.full(xx.size,np.log(3.)),np.full(xx.size,np.log(3.))])
    labels=classify(expit(z[0]),expit(z[1]),np.exp(z[2]),np.exp(z[3]))
    times=np.full(xx.size,np.nan)
    times[labels!=0]=0
    for k in range(int(horizon/step)):
        active=np.flatnonzero(labels==0)
        if not len(active):break
        a=z[:,active]
        k1=vector_rhs(a);k2=vector_rhs(a+step*k1/2)
        k3=vector_rhs(a+step*k2/2);k4=vector_rhs(a+step*k3)
        z[:,active]=a+step*(k1+2*k2+2*k3+k4)/6
        b=z[:,active]
        found=classify(expit(b[0]),expit(b[1]),np.exp(b[2]),np.exp(b[3]))
        selected=active[found!=0]
        labels[selected]=found[found!=0]
        times[selected]=(k+1)*step
    return {"x_initial":xx,"h_initial":hh,"labels":labels.reshape(xx.shape),
            "entry_time":times.reshape(xx.shape),"last_log_state":z,
            "step":step,"horizon":horizon}


def fixed_points(m=.5):
    p=base.replace(P,work_fraction=m)
    eq=base.equilibrium(p)
    cr=eq["state"][2]
    rho=p.eta_g*m*(1-p.allocation)*p.mu_c/(p.eta_c*p.allocation*p.mu_g)
    points={"full_participation":eq["state"],"no_genuine_maintenance":[1,0,cr,0]}
    def margin(c):return .8*(c/(1+c))**2*rho*c/(1+rho*c)-.15*(1+.8*(c/(1+c))**2)
    cb=brentq(margin,1e-10,1000)
    xb=cb/(p.eta_c*p.allocation*p.tau*(1+p.A*(cb/(1+cb))**2))
    if xb<1:points["mixed_users"]=[xb,1,cb,rho*cb]
    hb=(m+np.sqrt(m*m+4*m/(rho*cr)))/2
    if hb<1:points["mixed_custodians"]=[1,hb,cr,rho*hb*cr]
    if m>.15:
        qi=.15/(.8*(m-.15))
        if qi<1:
            ci=np.sqrt(qi)/(1-np.sqrt(qi))
            xi=ci/(p.eta_c*p.allocation*p.tau*(1+.8*qi))
            hi=(m+np.sqrt(m*m+4*m/(rho*ci)))/2
            if xi<1 and hi<1:points["fully_mixed"]=[xi,hi,ci,rho*hi*ci]
    result={}
    for name,state in points.items():
        residual=float(np.max(np.abs(base.physical_rhs(state,p))))
        assert residual<1e-10
        eig=np.linalg.eigvals(base.jacobian(state,p))
        result[name]={"state_x_h_C_G":list(map(float,state)),"residual":residual,
                      "eigenvalues_real_imag":[[float(v.real),float(v.imag)] for v in eig],
                      "unstable_directions":int(np.sum(eig.real>1e-8))}
    return result


def adaptive_rule(epsilon,target=4.,horizon=600.,method="DOP853"):
    z0=np.array([logit(.94),logit(.93),np.log(2.7),np.log(2.4),logit(.5)])
    def rhs(_t,z):
        x,h=expit(z[:2]);c,g=np.exp(z[2:4]);m=expit(z[4])
        p=base.replace(P,work_fraction=m)
        _,_,_,_,f,v,sx,sh=base.terms(x,h,c,g,p)
        return [sx,p.nu*sh,p.eta_c*.5*f/c-1,p.eta_g*m*h*v/g-1,epsilon*(target-g)]
    sol=solve_ivp(rhs,(0,horizon),z0,method=method,rtol=1e-10,atol=1e-12,dense_output=True)
    assert sol.success,sol.message
    time=np.linspace(0,horizon,3001)
    z=sol.sol(time)
    x,h=expit(z[:2]);c,g=np.exp(z[2:4]);m=expit(z[4])
    d=h*g/(1+g);v=.5*.15*x*(1+.8*(c/(1+c))**2)
    lower=g/(P.eta_g*h*v)
    upper=d  # zero slack for a nonnegative custodian return difference
    collapse=(h<=.1)&(m>=.9)&(c<=108/29)&(g<=1)&(x<1)
    ids=np.flatnonzero(collapse)
    desired_m=target/6
    desired=base.equilibrium(base.replace(P,work_fraction=desired_m))
    # C, user and custodian blocks decouple from the (G,m) response pair here.
    pair=np.linalg.eigvals([[-1.,6.],[-epsilon*desired_m*(1-desired_m),0.]])
    cp=base.replace(P,work_fraction=desired_m)
    desired_terms=base.terms(1,1,3,target,cp)
    eig=np.array([-desired_terms[-2],-P.nu*desired_terms[-1],-49/58,*pair],dtype=complex)
    assert max(eig.real)<0
    return {"t":time,"x":x,"h":h,"C":c,"G":g,"m":m,"log_state":z,
            "instantaneous_m_lower":lower,"instantaneous_m_upper":upper,
            "summary":{"epsilon":epsilon,"target":target,"horizon":horizon,
                       "final":[float(a[-1]) for a in (x,h,c,g,m)],
                       "maximum_m":float(m.max()),"minimum_h":float(h.min()),
                       "first_collapse_certificate_sample":float(time[ids[0]]) if len(ids) else None,
                       "fraction_of_samples_with_empty_m_interval":float(np.mean(lower>upper)),
                       "desired_equilibrium_eigenvalues_real_imag":[[float(v.real),float(v.imag)] for v in eig]}}


def run():
    OUT.mkdir(exist_ok=True)
    points=fixed_points()
    assert points["full_participation"]["unstable_directions"]==0
    assert points["mixed_users"]["unstable_directions"]==1
    assert points["mixed_custodians"]["unstable_directions"]==1
    assert points["fully_mixed"]["unstable_directions"]==2
    # Boundary eigenvalue calculations are independent direct substitutions.
    mlow=29/186;mhigh=5/6
    assert abs(base.equilibrium(base.replace(P,work_fraction=mlow))["user_margin"])<1e-12
    assert abs(base.equilibrium(base.replace(P,work_fraction=mhigh))["custodian_return_margin"])<1e-12
    for m in np.linspace(.02,.98,101):
        eq=base.equilibrium(base.replace(P,work_fraction=float(m)))
        assert (max(eq["eigenvalues"])<0)==(mlow<m<mhigh)
    first=basin_grid()
    refined=basin_grid(step=.02)
    mismatch=int(np.sum(first["labels"]!=refined["labels"]))
    assert mismatch==0,mismatch
    # Audit points near the slowest detected transitions, plus spatial coverage.
    flat_time=refined["entry_time"].ravel()
    longest=np.argsort(np.nan_to_num(flat_time,nan=1e9))[-16:]
    spread=np.linspace(0,len(flat_time)-1,16,dtype=int)
    chosen=np.unique(np.r_[longest,spread])
    independent=[]
    for idx in chosen:
        x0=refined["x_initial"].ravel()[idx];h0=refined["h_initial"].ravel()[idx]
        tr=base.trajectory((float(x0),float(h0),3.,3.),P,horizon=600.,samples=3001)
        found=classify(tr["x"],tr["h"],tr["C"],tr["G"])
        nonzero=found[found!=0]
        label=int(nonzero[0]) if len(nonzero) else 0
        expected=int(refined["labels"].ravel()[idx])
        assert label==expected,(idx,label,expected)
        independent.append({"x0":float(x0),"h0":float(h0),"label":label})
    controllers={"slow":adaptive_rule(.1),"fast":adaptive_rule(1.),
                 "lower_target_fast":adaptive_rule(10.,target=3.6)}
    assert max(np.abs(np.array(controllers["slow"]["summary"]["final"])-[1,1,3,4,2/3]))<1e-7
    assert controllers["fast"]["summary"]["first_collapse_certificate_sample"] is not None
    assert max(controllers["fast"][k][-1] for k in ("x","C","G"))<1e-7
    assert max(np.abs(np.array(controllers["lower_target_fast"]["summary"]["final"])-[1,1,3,3.6,.6]))<1e-7
    control_ref=adaptive_rule(1.,method="Radau")
    error=max(np.max(np.abs(control_ref[k]-controllers["fast"][k])) for k in ("x","h","C","G","m"))
    assert error<1e-6,error
    counts={"proved_loss_region_entry":int(np.sum(refined["labels"]==-1)),
            "proved_recovery_region_entry":int(np.sum(refined["labels"]==1)),
            "unresolved":int(np.sum(refined["labels"]==0))}
    result={"scope":"Exploratory model analysis; numerical basin entries use analytical region certificates, not validated interval integration.",
            "canonical_parameters":base.asdict(P),"equilibria":points,
            "full_participation_stability_interval_m":[mlow,mhigh],
            "basin_slice":{"fixed_C":3,"fixed_G":3,"grid":list(refined["labels"].shape),
                           "horizon":600,"step":.02,"counts":counts,"half_step_classification_disagreements":mismatch,
                           "adaptive_solver_spot_checks":independent},
            "controllers":{name:tr["summary"] for name,tr in controllers.items()},
            "fast_controller_second_integrator_max_difference":float(error),
            "base_source_sha256":hashlib.sha256(BASE.read_bytes()).hexdigest(),
            "analysis_source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/"analysis.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(OUT/"basin-slice.npz",**{k:v for k,v in refined.items() if isinstance(v,np.ndarray)})
    np.savez_compressed(OUT/"controller-trajectories.npz",**{f"{name}_{k}":v for name,tr in controllers.items() for k,v in tr.items() if isinstance(v,np.ndarray)})
    plot(refined,controllers,mlow,mhigh)
    print(json.dumps(result,indent=2))


def plot(grid,controllers,mlow,mhigh):
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.spines.top":False,"axes.spines.right":False})
    fig,axes=plt.subplots(2,2,figsize=(12,8.6),layout="constrained")
    green,red,blue,grey="#247B64","#B24B42","#4267AE","#DDDDDD"
    ax=axes[0,0]
    cmap=ListedColormap([red,grey,green])
    mesh=ax.pcolormesh(grid["x_initial"],grid["h_initial"],grid["labels"],cmap=cmap,
                       norm=BoundaryNorm([-1.5,-.5,.5,1.5],3),shading="nearest",rasterized=True)
    ax.axhline(.5,color="white",ls="--",lw=1)
    ax.text(.08,.15,"Operating loss",color="white")
    ax.text(.66,.94,"Recovery",color="white")
    ax.set(xlabel="Initial payer share x",ylabel="Initial genuine-maintenance share h",
           title="A. Basin slice at C = G = 3, fixed m = .5",xlim=(0,1),ylim=(0,1))
    ax.text(.03,.96,"Numerical entry into proved regions",transform=ax.transAxes,fontsize=8,color="white")
    ax=axes[0,1]
    mm=np.linspace(.01,.99,400)
    pp=6*mm/(1+6*mm)
    lx=-(.45*pp-.2175)
    lh=-10*.10875*(pp-mm)
    ax.axvspan(mlow,mhigh,color=green,alpha=.10)
    ax.axhline(0,color="#888888",lw=1)
    ax.plot(mm,lx,color=blue,lw=2,label="Bypass invasion growth")
    ax.plot(mm,lh,color=red,lw=2,label="False-completion invasion growth")
    ax.set(xlabel="Fixed maintenance fraction m",ylabel="Growth rate of a rare alternative",
           title="B. Local stability changes at two thresholds")
    ax.legend(frameon=False,fontsize=8)
    ax.text(.25,.025,"Both alternatives decline in shaded interval",fontsize=8,color=green)
    ax=axes[1,0]
    for name,color,label in (("slow",green,"Slower rule response (epsilon = .1)"),
                             ("fast",red,"Faster rule response (epsilon = 1)")):
        tr=controllers[name]
        ax.plot(tr["t"],tr["G"],color=color,lw=2,label=label)
    ax.axhline(4,color="#888888",ls="--",lw=1,label="Feasible target")
    ax.set(xlim=(0,100),ylim=(0,5),xlabel="Time",ylabel="Verification capacity G",
           title="C. Same feasible target, different outcomes")
    ax.legend(frameon=False,fontsize=8,loc="lower right")
    ax=axes[1,1]
    for name,color in (("slow",green),("fast",red)):
        tr=controllers[name]
        ax.plot(tr["t"],tr["m"],color=color,lw=2,label=f"{name.capitalize()} response: required work m")
        ax.plot(tr["t"],tr["h"],color=color,lw=1.7,ls="--",label=f"{name.capitalize()} response: genuine practice h")
    ax.set(xlim=(0,100),ylim=(0,1.03),xlabel="Time",ylabel="Fraction",
           title="D. A rule response can amplify the failure it targets")
    ax.legend(frameon=False,fontsize=8,loc="center right")
    fig.suptitle("Coupled dynamics of institutional maintenance and rule revision",fontsize=16)
    fig.supxlabel("Illustrative model · A/B: fixed rules · C/D: an explicit adaptive rule · no empirical fitting",fontsize=10)
    fig.savefig(OUT/"systems-atlas.png",dpi=180)
    fig.savefig(OUT/"systems-atlas.svg")
    plt.close(fig)


if __name__=="__main__":run()
