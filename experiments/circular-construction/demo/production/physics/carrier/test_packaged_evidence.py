"""Validate the saved motor/contact experiment's scope and independent gates."""
from pathlib import Path
import json
import mujoco
import numpy as np
HERE=Path(__file__).resolve().parent
stem='candidate-packaged-limb-92.928kg-mu0.65-sx0.16'
t=json.loads((HERE/(stem+'-trace.json')).read_text());v=t['metrics']
model=mujoco.MjModel.from_xml_path(str(HERE/(stem+'.xml')))
assert model.neq==0 and model.nmocap==0
assert abs(model.body_mass.sum()-432.928)<1e-8
assert v['complete'] and v['contactQualityAccepted'] and v['sequenceComplete']
assert not v['liveQposEdits'] and not v['appliedBodyForces']
assert abs(v['finalLimbAdvanceM']['fl']-.32)<.002
assert v['minRetainedJawSideNormalN']>1000
assert v['maxRetainedGripErrorM']<.03
assert v['maxNonGripCollisionN']<50
assert v['maxPenetrationM']<.002 and v['maxJointLimitViolation']<.002
assert v['maxFrictionUtilization']<1.02 and v['maxDynamicForceResidualN']<50
assert v['maxTiltRad']<.2
assert any(e['event']=='finite-contact-proofload-accepted' and e['resultantN']>500 for e in v['events'])
# A signed downward reaction is admissible only with all three physical clamps retained.
signed=[f for f in t['frames'] if f['phase']=='move' and any(a[2]<-100 for n,a in f['contactForcesSourceN'].items() if n!='fl')]
assert signed
for f in signed:
    for name in ('fr','rl','rr'):assert min(f['jawSideNormalN'][name].values())>1000
    assert f['dynamicForceResidualN']<50
# The low-friction counterpart must remain rejected; missing measurement windows are not passes.
low=json.loads((HERE/'candidate-packaged-hold-92.928kg-mu0.2-metrics.json').read_text())
assert not low['complete'] and low['abortReason']
print('Packaged single-hand contact/clearance/proofload evidence and low-friction rejection verified.')
