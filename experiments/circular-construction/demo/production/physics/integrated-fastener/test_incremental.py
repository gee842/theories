"""Validate limited claims; never asserts robot insertion succeeded."""
import json
from pathlib import Path
import free_pin, approach
HERE=Path(__file__).resolve().parent
r=approach.run();n=free_pin.run();negative=free_pin.run('no-latch');fine=free_pin.run(dt=.00025,save=False)
assert r['nominal']['hoistReleased'] and not r['missed-seat']['hoistReleased']
assert r['nominal']['distanceTipToHeadM']>.09
for result in [n,negative,fine]:
    assert result['finite'] and result['warnings']==0 and result['equalityCount']==0 and result['pinDofs']==6
    assert result['seatGateSeconds'] is not None
    assert not result['completeRobotFasteningCycle']
assert .012<n['finalBeamAxialDisplacementM']<.016
assert abs(n['meanFinalAxialReactionsN']['headBracket']-2000)<10
assert abs(sum(n['meanFinalAxialReactionsN'][k] for k in ['dogBeam','slotBeam'])-2000)<10
assert n['motorWorkJ']==[0.,0.]
assert n['meanFinalAxialReactionsN']['slotBeam']==0 and fine['meanFinalAxialReactionsN']['slotBeam']==0
assert abs(n['meanFinalAxialReactionsN']['dogBeam']-fine['meanFinalAxialReactionsN']['dogBeam'])<2
assert negative['finalBeamAxialDisplacementM']>.25
assert negative['meanFinalAxialReactionsN']['dogBeam']==0
assert abs(n['finalBeamAxialDisplacementM']-fine['finalBeamAxialDisplacementM'])<.001
assert n['maxPenetrationM']<.001 and fine['maxPenetrationM']<.001
report={'limitedIncrementalChecksPassed':True,'integratedFasteningPassed':False,'retainingLoadPathConverged':True,'loadPathDogReactionDifferenceN':abs(n['meanFinalAxialReactionsN']['dogBeam']-fine['meanFinalAxialReactionsN']['dogBeam']),'claims':['Actual two-seat gate enables bounded maximum-stroke tool approach','Existing robot geometry cannot align or reach mating pin-head location','Pre-inserted six-DOF pin retains 2 kN with contact-only axial path','Recessed slot rails eliminate unintended slot bearing; dog/head load path agrees within 2 N across timesteps','No-latch control fails retention','No robot insertion or complete fastening is demonstrated'],'fineTimestep':fine,'coarseFineDisplacementDifferenceM':abs(n['finalBeamAxialDisplacementM']-fine['finalBeamAxialDisplacementM'])}
(HERE/'test-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
