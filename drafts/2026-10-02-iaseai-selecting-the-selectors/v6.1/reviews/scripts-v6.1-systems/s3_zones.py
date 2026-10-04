# S3: Remark S5.1 ("zones illustration") by direct evaluation of discounted streams, not by its closed form.
# Binary game (15): n=4, b=1, c=0.3, d=0.2, eps=1, delta=0.9. Objective J_i=u_i+theta*mean(u_-i).
# Cooperation: all restrain, J=0 each period.  One-shot deviation: stage gain g; then with prob p_d an absorbing decisive
# position worth D per period; otherwise reversion to all-racing forever (J=(1+theta)*u_race). Sustained iff V_coop>=V_dev.
n,b,c,dd,ep,delta=4,1.0,0.3,0.2,1.0,0.9
def u(i,a):
    return ep*b*(a[i]-sum(a[j] for j in range(n) if j!=i)/(n-1))-c*a[i]-ep*dd*sum(a)
def J(i,a,th):
    others=[u(j,a) for j in range(n) if j!=i]
    return u(i,a)+th*sum(others)/len(others)
def V_dev(th,pd,D,T=3000):
    a0=[1,0,0,0]; g=J(0,a0,th)
    race=[1]*n; P=J(0,race,th)
    # value iteration on the 3-state chain {decisive, punish}, direct summation
    v=g; disc=delta
    for t in range(1,T):
        v+=disc*(pd*D+(1-pd)*P); disc*=delta
    return v
def stage_race_dominant(th):
    # racing is a best response to all-racing in objectives? (credibility of the punishment)
    return J(0,[1]*n,th)>=J(0,[0,1,1,1],th)
def theta_rep(pd,D):
    lo,hi=-1.0,3.0
    if V_dev(hi,pd,D)>0: return float('inf')
    for _ in range(60):
        m=(lo+hi)/2
        if V_dev(m,pd,D)>0: lo=m
        else: hi=m
    return hi
A=ep*(b-dd)-c; B=ep*(b/(n-1)+dd)
print(f"A/B (stage-equilibrium threshold) = {A/B:.4f}")
for pd in (0,0.5,0.9,0.95,0.99,1.0):
    th=theta_rep(pd,0.0)
    print(f"   p_d={pd}: theta_rep={th:.3f}; punishment credible (racing a stage best response) at that theta: {stage_race_dominant(th-1e-9)}")
lo,hi=0.0,1.0
for _ in range(60):
    m=(lo+hi)/2
    if V_dev(0.0,m,0.0)<=0: lo=m
    else: hi=m
print(f"   theta=0 loses enforced restraint at p_d={lo:.4f}")
print(f"   D=0.5: theta_rep at p_d=0.9 = {theta_rep(0.9,0.5):.3f}; at p_d=1: {theta_rep(1.0,0.5)} (no theta<=n-1 sustains)")
print("Test G: gap in enforceable restraint between a wider and a narrower objective, as p_d rises")
pairs=[(-0.5,0.5),(0.0,1.0),(0.0,0.9)]
for D in (0.0,0.5):
    for (tn,tw) in pairs:
        row=[]
        for pd in (0.0,0.3,0.6,0.8,0.9,0.95,0.99,1.0):
            tr=theta_rep(pd,D)
            row.append(str(int(tw>=tr)-int(tn>=tr)))
        print(f"   D={D}, theta narrow={tn}, wide={tw}: gap at p_d=0,.3,.6,.8,.9,.95,.99,1 -> {' '.join(row)}")
# population version: theta uniform on [-1,3]; share able to restrain among 'wide' (theta>1) minus 'narrow' (theta<1)
print("   population, theta ~ U[-1,3], wide = theta>1, narrow = theta<1: share enforceable wide minus narrow")
for D in (0.0,0.5):
    row=[]
    for pd in (0.0,0.5,0.8,0.9,0.95,0.99,1.0):
        tr=theta_rep(pd,D)
        fw=max(0.0,min(1.0,(3-max(tr,1))/2)); fn=max(0.0,min(1.0,(1-max(tr,-1))/2))
        row.append(f"{fw-fn:+.2f}")
    print(f"   D={D}: "+" ".join(row))
