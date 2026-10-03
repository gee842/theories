"""Small declared design sweep, not a global optimization or fabrication clearance proof."""
import json
import prototype as p

rows=[]
for length in (.32,.34,.36,.40,.45):
    p.LENGTH=length
    try:
        _,m,_=p.run(cycles=1)
        row={'linkLengthM':length, **{k:m[k] for k in ('complete','settledAdvanceM','minUpwardSupports','maxReactionN','maxTorqueNm','maxJointLimitViolationRad','abortReason','rejectedCaptureErrorM')}}
        row['rejectedCapture']=[e for e in m['events'] if e['event']=='capture-rejected']
    except (ValueError,RuntimeError) as e:
        row={'linkLengthM':length,'complete':False,'error':str(e)}
    rows.append(row)
    print(row,flush=True)
(p.HERE/'geometry-sweep.json').write_text(json.dumps(rows,indent=2,allow_nan=False)+'\n')
p.LENGTH=.36
_,metrics,_=p.run()
(p.HERE/'minimum-tested-metrics.json').write_text(json.dumps(metrics,indent=2,allow_nan=False)+'\n')
print('Smallest tested geometry full-storey:', metrics['complete'], metrics['settledAdvanceM'], flush=True)
