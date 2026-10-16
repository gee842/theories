# S2c: Prop 4.11's share-freezing pause with rule-making insulated: required length ln(z0/S(x_p))/(eps d),
# S = separatrix height at the frozen share; compare with the "at least ln G/(eps d)" in the scope of Prop 4.11.
import math, importlib.util, io, contextlib
spec=importlib.util.spec_from_file_location("s2","s2_dwell.py"); s2=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(s2)
for eps in (1.0,0.1):
    for G in (2,5):
        pts=s2.separatrix(G,eps)
        row=[]
        for xp in (0.1,0.3,1/G,0.6,0.8,0.95):
            S=s2.zsep(pts,s2.logit(xp))
            T=math.log(G/S) if S>0 else float('inf')
            row.append(f"x_p={xp:.2f}: S={S:.2f}, eps*d*T={T:.2f}")
        print(f"eps/zeta={eps}, G={G} (ln G={math.log(G):.2f}, x_sigma={s2.x_sigma(pts):.3f}): "+"; ".join(row))
