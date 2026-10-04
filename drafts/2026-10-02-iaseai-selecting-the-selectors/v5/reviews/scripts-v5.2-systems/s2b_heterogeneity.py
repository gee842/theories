"""S2b. Bistability of the Psi model requires combined reflexive gain B=k+ab/d to exceed 4s
(s = heterogeneity of actors' thresholds). Sweep s: width of the hysteresis band in beta."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("m", "s2_psi_model.py")
src = open("s2_psi_model.py").read().split('print("== S2a')[0]
ns = {}; exec(src, ns)
P = ns['P']; equilibria = ns['equilibria']
B = P['k'] + P['a']*P['b']/P['d']
print(f"B = k + ab/d = {B}")
for s in [0.25, 0.2, 0.15, 0.1, 0.05, 0.025]:
    Q = dict(P); Q['s'] = s
    band = [i/400 for i in range(0, 401) if len(equilibria(i/400, Q, 1500)) == 3]
    if band:
        print(f"  s={s:5.3f}  B/(4s)={B/(4*s):4.2f}  bistable beta in [{min(band):.3f}, {max(band):.3f}]  width={max(band)-min(band):.3f}")
    else:
        print(f"  s={s:5.3f}  B/(4s)={B/(4*s):4.2f}  monostable")
