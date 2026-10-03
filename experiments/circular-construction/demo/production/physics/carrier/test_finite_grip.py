"""Validate the measured finite-contact hold and preserve rejected-motion outcomes."""
from pathlib import Path
import json
import numpy as np
import mujoco
HERE=Path(__file__).resolve().parent
hold=json.loads((HERE/'finite-hold-92.928kg-mu0.65-metrics.json').read_text())
low=json.loads((HERE/'finite-hold-92.928kg-mu0.2-metrics.json').read_text())
recap=json.loads((HERE/'finite-recapture-92.928kg-mu0.65-sx0.12-metrics.json').read_text())
step=json.loads((HERE/'finite-step-92.928kg-mu0.65-sx0.12-metrics.json').read_text())
model=mujoco.MjModel.from_xml_path(str(HERE/'finite-hold-92.928kg-mu0.65.xml'))
assert model.neq==0 and model.nmocap==0
assert hold['complete'] and hold['contactQualityAccepted']
assert hold['minRetainedUpwardSupports']==4
assert hold['maxPenetrationM']<.002 and hold['maxChassisDriftM']<.001
assert hold['maxNonGripCollisionN']==0 and hold['finalSpeedMps']<.001
loads=np.array(list(hold['finalContactForcesSourceN'].values()))
assert np.all(loads[:,2]>500)
assert abs(loads[:,2].sum()-hold['totalMassKg']*9.81)<5
assert np.linalg.norm(loads.sum(axis=0)[:2])<5
assert all(6000<v<10000 for v in hold['finalJawNormalSumN'].values())
assert not low['complete'] and low['abortReason']
assert recap['sequenceComplete'] and not recap['complete'] and not recap['contactQualityAccepted']
assert not step['complete'] and step['abortReason']=='Retained contact load gate failed' and step['minRetainedUpwardSupports']<3
assert not any(hold['warnings'].values())
print('PASS: finite contacts carry measured full weight; low-friction, poor capture quality and step support loss remain rejected.')
