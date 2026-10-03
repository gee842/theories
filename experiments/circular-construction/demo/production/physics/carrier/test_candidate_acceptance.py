"""Acceptance checks for the exact manufactured-envelope, loaded finite-step evidence."""
from pathlib import Path
import json,struct
import mujoco
HERE=Path(__file__).resolve().parent
stem='candidate-manufactured-step-92.928kg-mu0.65-sx0.16'
t=json.loads((HERE/(stem+'-trace.json')).read_text());v=t['metrics'];m=mujoco.MjModel.from_xml_path(str(HERE/(stem+'.xml')))
assert m.neq==0 and m.nmocap==0 and abs(m.body_mass.sum()-432.928)<1e-8
assert v['complete'] and v['contactQualityAccepted'] and v['manufacturedHousingEnvelopes']
assert not v['liveQposEdits'] and not v['appliedBodyForces']
assert .318<v['chassisAdvanceM']<.323
assert all(abs(a-.32)<.002 for a in v['finalLimbAdvanceM'].values())
assert v['minRetainedJawSideNormalN']>1000 and v['maxRetainedGripErrorM']<.03
assert v['maxNonGripCollisionN']<50 and v['maxPenetrationM']<.002 and v['maxJointLimitViolation']<.002
assert v['maxFrictionUtilization']<1.02 and v['maxDynamicForceResidualN']<50 and v['maxGripResultantN']<16000
limits={'hip_yaw':400,'shoulder':3000,'elbow':2000,'wrist_yaw':150,'wrist':400,'wrist_roll':150}
assert all(v['maxTorqueNm'][j]<=limit for j,limit in limits.items())
proofs=[e for e in v['events'] if e['event']=='finite-contact-proofload-accepted']
assert len(proofs)==4 and all(e['resultantN']>500 for e in proofs)
assert v['minRetainedUpwardSupports']==2 and v['minSignedVerticalReactionN']<0
for n in ('fl','fr','rl','rr'):
    for suffix in ('hip_motor_envelope','knee_motor_envelope','wrist_gimbal_envelope'):assert m.geom(n+'_'+suffix).id>=0
    assert m.geom('wheel_'+n).id>=0
# Actual editable candidate export has every proposed articulated pivot and contact marker.
glb=HERE.parents[1]/'blender/six-axis-carrier-candidate.glb';raw=glb.read_bytes()
size,kind=struct.unpack_from('<II',raw,12);assert kind==0x4e4f534a
nodes=json.loads(raw[20:20+size])['nodes'];names={n.get('name') for n in nodes}
for limb in ('fl','fr','rl','rr'):
    for suffix in ('hip_yaw','hip','knee','wrist_yaw','wrist','wrist_roll','grip_contact','jaw_a','jaw_b'):assert f'limb_{limb}_{suffix}' in names
print('Exact manufactured-envelope four-hand climb and editable GLB joint contract verified.')
f=json.loads((HERE/'candidate-continuous-fault-limb-92.928kg-mu0.65-sx0.16-metrics.json').read_text())
assert not f['complete'] and f['recoverySupported']
assert f['minRetainedJawSideNormalN']>1000 and f['maxRetainedGripErrorM']<.03
assert f['maxNonGripCollisionN']<50 and f['finalSpeedMps']<.005
start=next(e['time'] for e in f['events'] if e['event']=='supported-fault-hold-command')
end=next(e['time'] for e in f['events'] if e['event']=='supported-fault-hold-complete')
assert end-start>=5
print('Same-model injected closing-motor fault remains rejected with a measured five-second supported stop.')
