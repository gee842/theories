"""EC block S1c case 2 (C=3,g=1,D=3,P=1,pd=0.5,q=0,delta=.9): exact 22.000; checks log MC 22.414 at N=4000 -> z ~ +2.9."""
import random, math
C,g,D,U,P,pd,q,dl=3,1,3,0,1,0.5,0.0,0.9
Vexact=(C+g)+dl*(pd*D/(1-dl)+(1-pd)*P/(1-dl))
for seed in range(5):
    rnd=random.Random(seed); N=4000; tot=0; sq=0
    for _ in range(N):
        s=C+g; s+= dl*(D/(1-dl) if rnd.random()<pd else P/(1-dl)); tot+=s; sq+=s*s
    m=tot/N; sd=math.sqrt(sq/N-m*m)
    print(f"seed {seed}: MC mean {m:.3f} (exact {Vexact:.3f}), SE {sd/math.sqrt(N):.3f}, z={(m-Vexact)/(sd/math.sqrt(N)):+.2f}")
