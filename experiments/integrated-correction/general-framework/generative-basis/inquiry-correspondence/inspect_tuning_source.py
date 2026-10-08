#!/usr/bin/env python3
"""Read preserved source bytes to specify the next tuning-correspondence test.
Does not execute the upstream optimizer, identify a plant, or tune physical hardware.
"""
from pathlib import Path
from zipfile import ZipFile
import csv,hashlib,io,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
SOURCE=ROOT/'sources/tclab-benchmark'
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    archive=SOURCE/'CACE_2020_source.zip'
    member='2_PID/2_optimize_PID/data.txt'
    code_path=SOURCE/'extracted/2_PID/2_optimize_PID/tclab_optimal.py'
    code=code_path.read_text()
    checks={
      'fit':'na = 2',
      'output_error_fit':"scale=False,diaglevel=1,pred='model')",
      'residual':'ld1 = data[\'T1\'].values - yp[:,0]',
      'fixed_interval':'dt = 1.0',
      'residual_reuse':'T1[i+1] = y[0].value[1]+ld1[i+1]',
      'signed_movement':'mv_obj += Q1[i]-Q1[i-1]',
      'gain_grid':'x = np.arange(5.0, 80.1, 5.0)',
      'integral_time_grid':'y = np.arange(5.0, 80.1, 5.0)'}
    assert all(s in code for s in checks.values())
    with ZipFile(archive) as z:
        data=z.read(member)
        inventory=[{'member':n,'bytes':z.getinfo(n).file_size} for n in z.namelist() if n.startswith('2_PID/2_optimize_PID/')]
    rows=list(csv.DictReader(io.StringIO(data.decode())))
    duplicate=data==(SOURCE/'extracted/2_PID/0_initial_PID/data.txt').read_bytes()
    assert duplicate and len(rows)==599 and all(float(r['Q2'])==0 for r in rows)
    result={'status':'inspected','inspection_source_sha256':sha(Path(__file__).read_bytes()),
      'archive_sha256':sha(archive.read_bytes()),'optimizer_source_sha256':sha(code_path.read_bytes()),
      'training_member':member,'training_member_sha256':sha(data),'training_rows':len(rows),
      'byte_identical_to_already_preserved_initial_run':duplicate,'recorded_second_heater_commands_all_zero':True,
      'source_contracts':{k:{'statement':s,'line':next(i for i,l in enumerate(code.splitlines(),1) if s in l)} for k,s in checks.items()},
      'optimizer_directory_inventory':inventory,
      'next_test':'Resolve the signed/absolute objective discrepancy together with the model and disturbance-transfer contracts. The saved initial-data fit residual is reused under changed gains; treating that reuse as a physical counterfactual requires warrant. Preserve nominal-one-second versus measured-interval scope and the separate two-heater dataset.',
      'scope':'Static source and archival-data inspection only. This does not reproduce GEKKO output-error fitting or certify an optimum, residual invariance, physical efficacy, or ethics. Duplicate training bytes are one observational source.'}
    (HERE/'tuning-source-contract.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','training_rows','byte_identical_to_already_preserved_initial_run','recorded_second_heater_commands_all_zero','scope']},indent=2))
if __name__=='__main__':main()
