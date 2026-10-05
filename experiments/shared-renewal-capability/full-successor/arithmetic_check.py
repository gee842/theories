"""Independent scalar-integer check of the limb step, including boundaries."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import hashlib,json,random
import numpy as np
from scipy.sparse import csr_matrix
import fixed
rng=random.Random(120971)
checks=0
for gamma in (1,2,7,357,807):
    for k in range(60):
        n=7;rows=[]
        for i in range(n):
            cuts=sorted([0,gamma]+[rng.randrange(gamma+1) for _ in range(n-1)])
            rows.append([cuts[j+1]-cuts[j] for j in range(n)])
        M=csr_matrix(rows,dtype=np.int64)
        values=[rng.randrange(fixed.SCALE+1) for _ in range(n)]
        if k%3==0:values=[0]*n
        if k%3==1:values=[fixed.SCALE]*n
        for up in (False,True):
            out=fixed.step(M,fixed.pack(values),gamma,up)
            for i,row in enumerate(rows):
                exact=sum(a*b for a,b in zip(row,values));expected=(exact+gamma-1)//gamma if up else exact//gamma
                assert fixed.unpack(out[i])==expected;checks+=1
j={'status':'all exact scalar comparisons passed','comparisons':checks,'seed':120971,'scope':'Limb implementation matches independent arbitrary-precision weighted integer division for declared boundary/random cases; analytic row-sum and limb-size proof supplies general bound','sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),Path(fixed.__file__))}}
Path(__file__).with_name('arithmetic-check.json').write_text(json.dumps(j,indent=2)+'\n');print(j)
