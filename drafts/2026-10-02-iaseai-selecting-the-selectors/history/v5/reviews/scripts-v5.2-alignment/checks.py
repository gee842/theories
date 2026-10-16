import math
n,b,c,d=4,1.0,0.3,0.2
def theta_star(eps,gb=1.0,gd=1.0,gc=0.0):
    # standing scales eps^gb, harm eps^gd, private cost eps^gc
    B=b*eps**gb; D=d*eps**gd; C=c*eps**gc
    return (B-D-C)/(B/(n-1)+D)
print("A. theta* (paper scaling)", [round(theta_star(e),3) for e in (1,10,100)])
print("   limit", round((b-d)/(b/(n-1)+d),3))
print("B. harm superlinear eps^1.5", [round(theta_star(e,gd=1.5),3) for e in (1,10,100)])
print("C. private cost scales with eps too", [round(theta_star(e,gc=1.0),3) for e in (1,10,100)])
print("D. AI lowers private cost (eps^-0.5)", [round(theta_star(e,gc=-0.5),3) for e in (1,10,100)])
# effect of lowering d (technical alignment lowering shared harm per unit)
for dd in (0.2,0.1,0.05):
    th=(1*(b-dd)-c)/(1*(b/(n-1)+dd)); loss=c+n*1*dd
    print(f"E. d={dd}: theta*={th:.3f}, all-race loss per principal={loss:.2f}")
# Accuracy step: kappa=0.4 vs theta*
print("F. kappa=0.4 < theta*(1)=%.3f -> race persists at accuracy"%theta_star(1))
# Prop 5.11 comparison: serial chain f per link bridging factor m; redundant direct checks each bridging full gap
f,k=0.9,6
serial=f**k
red_paper=1-(1-f)**k
f_full=f**k  # a single check bridging the whole gap, if reliability compounds per amplification step
red_fair=1-(1-f_full)**k
print(f"G. serial={serial:.3f}, redundant(paper, f=0.9 each)={red_paper:.6f}, redundant(each spans full gap, f={f_full:.3f})={red_fair:.3f}")
rho=0.05
print(f"   with common cause rho={rho}: cap {1-rho:.2f}; fair redundant with cc: {(1-rho)*red_fair:.3f}")
# hybrid: redundancy r at each of k layers
for r in (2,3):
    per=1-(1-f)**r
    print(f"H. serial chain with {r}-fold redundancy per layer: {per**k:.4f}")
