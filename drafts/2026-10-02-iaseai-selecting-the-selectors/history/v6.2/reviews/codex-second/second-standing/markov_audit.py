"""Independent Bellman audits. Standard library; no manuscript imports."""
import math
import json
import sys

def passive(r=1.5,gamma=.6,decay=.2,discount=.97,cells=1500):
    won=gamma/r; jw=decay*(1+won)/2; jl=decay*(1-won)/2
    grid=[i/cells for i in range(cells+1)]
    def interp(v,s):
        q=s*cells; j=min(cells-1,max(0,int(q)))
        return v[j]+(q-j)*(v[j+1]-v[j])
    probs=[s**r/(s**r+(1-s)**r) for s in grid]
    v=[0.]*(cells+1)
    for it in range(20000):
        nv=[p+discount*(p*interp(v,(1-decay)*s+jw)+(1-p)*interp(v,(1-decay)*s+jl))
            for s,p in zip(grid,probs)]
        err=max(abs(a-b) for a,b in zip(v,nv)); v=nv
        if err<1e-11: break
    lam=discount*(interp(v,(1-decay)/2+jw)-interp(v,(1-decay)/2+jl))
    gd=gamma*discount*decay/(1-discount*(1-decay))
    return dict(r=r,gamma=gamma,decay=decay,discount=discount,cells=cells,
                passive_price=lam,formula=gd/(1-gd),iterations=it,error=err)

def solve(r=4., gamma=.2, decay=.05, discount=None, cells=3000,
          step=False, shared=0., sub=0., maxit=20000):
    if discount is None: discount=1/(1+decay)
    won=gamma/r
    low_jump=decay*(1-won)/2
    high_jump=low_jump+decay*won
    states=[i/cells for i in range(cells+1)]
    transitions=[]
    for s in states:
        a=(1-decay)*s+high_jump
        b=(1-decay)*s+low_jump
        transitions.append((a,b))
    def interp(v,s):
        q=s*cells
        j=min(cells-1,max(0,int(q)))
        return v[j]+(q-j)*(v[j+1]-v[j])
    def policy(s,v):
        sw=(1-decay)*s+high_jump
        sl=(1-decay)*s+low_jump
        a=1+discount*(interp(v,sw)-interp(v,sl))
        b=1+discount*(interp(v,1-sl)-interp(v,1-sw))
        aa=s**r*max(a,0)
        bb=(1-s)**r*max(b,0)
        p=aa/(aa+bb) if aa+bb else .5
        e1=max(a,0)*p*(1-p)/(1+shared)
        e2=max(b,0)*p*(1-p)/(1+shared)
        return p,e1,e2,a,b,sw,sl
    v=[3*((s>.5)-(s<.5)) if step else 0 for s in states]
    for it in range(maxit):
        vn=[]
        for s in states:
            p,e1,e2,a,b,sw,sl=policy(s,v)
            vn.append(p-e1-shared*(e1+e2)-sub*(1-s)**2+
                      discount*(p*interp(v,sw)+(1-p)*interp(v,sl)))
        err=max(abs(a-b) for a,b in zip(v,vn))
        v=[(a+b)/2 for a,b in zip(v,vn)]
        if err<1e-11: break
    p,e1,e2,a,b,sw,sl=policy(.5,v)
    h=1/cells
    left,right=policy(.5-h,v),policy(.5+h,v)
    req=(right[0]-left[0])/(2*h)
    def ownfixed(s):
        eother=policy(s,v)[2]
        return s**r*e1/(s**r*e1+(1-s)**r*eother)
    rpr=(ownfixed(.5+h)-ownfixed(.5-h))/(2*h)
    fac=discount*decay/(1-discount*(1-decay))
    gp=rpr*won*fac
    pred=gp/(1-gp)
    actual=discount*(interp(v,sw)-interp(v,sl))
    # Local slope is a different object from the finite winner/loser value.
    deriv=discount*decay*won*(interp(v,.5+h)-interp(v,.5-h))/(2*h)
    min_a=math.inf; bad=0; max_res=0.; zeroeff=0
    for i,s in enumerate(states):
        if not (0<s<1): continue
        p,ei,ej,A,B,_,_=policy(s,v)
        min_a=min(min_a,A,B)
        aa=s**r; bb=(1-s)**r
        actual_p=aa*ei/(aa*ei+bb*ej) if aa*ei+bb*ej else .5
        max_res=max(max_res,abs(actual_p-p))
        if A<=0 or B<=0: bad+=1
        if ei==0 and ej==0: zeroeff+=1
    return dict(r=r,gamma=gamma,decay=decay,discount=discount,cells=cells,
                step=step,it=it,err=err,price=actual,derivative_price=deriv,
                predicted=pred,req=req,rpr=rpr,geq=req*won,gpr=gp,
                min_contest_value=min_a,negative_states=bad,
                probability_residual=max_res,zeroeff_states=zeroeff,
                parity_value=interp(v,.5),v_near=[interp(v,.5+x/cells) for x in (-2,-1,0,1,2)])

if __name__=='__main__':
    cases=[dict(r=4,gamma=.2,decay=.05,cells=1500,step=False),
           dict(r=4,gamma=.2,decay=.05,cells=1500,step=True),
           dict(r=4,gamma=.2,decay=.05,cells=3000,step=True),
           dict(r=4,gamma=.45,decay=.1,cells=1500),
           dict(r=1.5,gamma=.6,decay=.2,discount=.97,cells=800)]
    if len(sys.argv)>1: cases=[json.loads(sys.argv[1])]
    for kw in cases:
        print(json.dumps(solve(**kw)),flush=True)
