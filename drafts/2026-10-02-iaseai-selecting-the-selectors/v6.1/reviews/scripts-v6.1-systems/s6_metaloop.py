# S6: a toy closure of the generative loop "through what all share": the loop runs through the common weight on others
# (theta_Gamma, Prop 3.9), not through any winner.  Rule-making by actors with working objective theta_Gamma sets the
# convertibility of the next period's rules, hence Gamma_delta; Gamma_delta sets theta_Gamma (eq. 9).
# Gamma' = Gmin + (Gmax-Gmin) * S(k*(theta_c - theta_Gamma(Gamma))), S logistic.  Count fixed points and their stability.
import math
n,th0=4,0.5
def thG(G): return (n*th0-(n-1)*(1+th0)*G)/(n-(1+th0)*G)
def S(v): return 1/(1+math.exp(-v))
def F(G,k,thc,Gmin=0.1,Gmax=0.98): return Gmin+(Gmax-Gmin)*S(k*(thc-thG(G)))
for k in (2.0,6.0,12.0):
    for thc in (-0.2,0.0,0.2):
        fps=[]; prev=None
        N=20000
        for i in range(N+1):
            G=0.0+0.999*i/N
            h=F(G,k,thc)-G
            if prev is not None and (h==0 or (h>0)!=(prev[1]>0)):
                g0=prev[0]; slope=(F(G+1e-6,k,thc)-F(G-1e-6,k,thc))/2e-6
                fps.append((round(G,3),'stable' if abs(slope)<1 else 'unstable', round(thG(G),2)))
            prev=(G,h)
        print(f"k={k}, theta_c={thc}: fixed points (Gamma, stability, theta_Gamma): {fps}")
