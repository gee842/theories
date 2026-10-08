#!/usr/bin/env python3
"""Post-hoc diagnostic of an initial-reference adjustment, with both outcomes kept.
It tests a proposed explanation after inspecting the validation discrepancies;
it is not a preregistered comparison or independent ambient-temperature evidence.
"""
from pathlib import Path
import hashlib,json,sys
sys.dont_write_bytecode=True
import numpy as np
import analyze_tuning as study
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    f=json.loads((HERE/'tuning-model.json').read_text());train=study.load(ROOT/f['training_source'])
    a=[r[0] for r in f['parameters']['a']];b=[r[0] for r in f['parameters']['b'][0]];c=f['parameters']['c'][0]
    residual=np.array(f['training_output_residual'])[:,0]
    base=json.loads((HERE/'tclab-results.json').read_text());runs=[]
    for r in base['physical_runs'][1:]:
        data=study.load(ROOT/r['path']);delta=data[0]['T1']-train[0]['T1']
        changed_c=c+delta*(1-sum(a));pred=study.plant_inputs(data,a,b,changed_c);actual=np.array([v['T1'] for v in data])
        runs.append({'label':r['label'],'source':r['path'],'source_sha256':sha(ROOT/r['path']),
          'initial_reading_difference_celsius':delta,'adjusted_intercept':changed_c,
          'without_transferred_residual':study.describe((pred-actual)[2:]),
          'with_initial_run_residual':study.describe((pred+residual-actual)[2:])})
    result={'status':'passed','checker_sha256':sha(Path(__file__)),'analysis_source_sha256':sha(HERE/'analyze_tuning.py'),
      'fit_sha256':sha(HERE/'tuning-model.json'),'runs':runs,
      'scope':'Post-hoc diagnostic. Coefficients a,b remain fixed; only c is adjusted by initial reading difference times (1-sum(a)). Initial reading is not certified ambient temperature. Improvement in one run and worsening in the other are retained; neither model is validated universally.'}
    (HERE/'tuning-reference-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
