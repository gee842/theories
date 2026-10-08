#!/usr/bin/env python3
"""Recompute coordinate moments using integer sufficient statistics.

No import of the analysis. Uses the original coordinates and a distinct
uncentered moment calculation, verifies all pair rankings and the Lean witness.
The computation is not an experimental validation of either drag law.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import re
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
SOURCE=ROOT/'sources/evolutionary-selection/day-2022/packing-data.zip'
LEAN=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SettlingCorrespondence.lean'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    result=json.loads((HERE/'settling-results.json').read_text())
    assert result['source_sha256']==sha(SOURCE)
    assert result['code_sha256']==sha(HERE/'analyze_settling.py')
    assert json.loads((SOURCE.parent/'manifest.json').read_text())['preserved_files'][SOURCE.name]['sha256']==sha(SOURCE)
    exact={}
    with zipfile.ZipFile(SOURCE) as z:
        for r in result['clusters']:
            lines=z.read('Experimental_Data/Snowflake_SEM_positions/'+r['cluster']+'.txt').decode().splitlines()
            p=[]
            for line in lines:
                tokens=line.split()[1:]
                assert all(re.fullmatch(r'-?\d+\.\d{6}',t) for t in tokens)
                p.append([int(t.replace('.','')) for t in tokens])
            n=len(p);assert n==r['cells']
            sums=[sum(row[k] for row in p) for k in range(3)]
            q=n*sum(sum(t*t for t in row) for row in p)-sum(t*t for t in sums)
            radius2=F(5*q,3*n*n*10**12)
            assert radius2==F(r['radius_squared_um2'])
            radius=math.sqrt(float(radius2))
            envelope=4*math.pi*radius**3/3
            solid=17.44*n
            bulk_density=(solid*1112.6+(envelope-solid)*997)/envelope
            bulk_speed=9.81*(2*radius*1e-6)**2*(bulk_density-997)/(18*9.81e-4)*60000
            assert math.isclose(bulk_speed,r['material_accounted_sphere_speed_mm_min'],rel_tol=1e-11)
            exact[r['cluster']]=(n,radius2)
    reversals=[]
    for a,b in itertools.combinations(exact,2):
        na,ra=exact[a];nb,rb=exact[b]
        # Compare exact squared speed scores, using division instead of the
        # analysis's cross multiplication.
        x=ra-rb;y=F(na*na)/ra-F(nb*nb)/rb
        if x*y<0:reversals.append((a,b))
    assert reversals==[(r['a'],r['b']) for r in result['reversed_pairs']]
    assert len(reversals)==result['summary']['reversed_pair_count']==33
    assert len(exact)*(len(exact)-1)//2==result['pairs_compared']==190
    assert sorted(exact,key=lambda x:exact[x][1],reverse=True)==result['uniform_ranking']
    assert sorted(exact,key=lambda x:F(exact[x][0]**2)/exact[x][1],reverse=True)==result['material_ranking']
    source=LEAN.read_text()
    for tag in ('01','04'):
        m=re.search(r'def radiusSquared'+tag+r' : Rat := (\d+) / (\d+)',source)
        assert F(int(m[1]),int(m[2]))==exact['particles-sphere-'+tag][1]
    assert exact['particles-sphere-01'][0]==128 and exact['particles-sphere-04'][0]==147
    files=['analyze_settling.py','check_settling.py','settling-results.json']
    out={'status':'passed','scope':'Independent integer-moment and exact pair-score computation, plus numerical bulk-density speed correspondence. Not measured hydrodynamics or author-code replication.',
         'checks':{'clusters':20,'coordinate_rows':2106,'pairs':190,'reversed_pairs':33,'lean_witness_source_correspondence':'passed'},
         'files_sha256':{n:sha(HERE/n) for n in files},'lean_source_sha256':sha(LEAN),'source_sha256':sha(SOURCE)}
    (HERE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out['checks'],indent=2))

if __name__=='__main__':main()
