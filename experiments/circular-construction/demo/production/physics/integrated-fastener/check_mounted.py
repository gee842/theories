"""Check saved runs of the explicit receiver, mounted magazine, and free pin."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
read=lambda name:json.loads((HERE/name).read_text())
n=read('mounted-nominal-validation.json');f=read('mounted-nominal-fine-validation.json');bad=read('mounted-no-latch-validation.json');missing=read('mounted-missing-stop-validation.json')
traces={name:read('mounted-'+name+'-trace.json') for name in ['nominal','nominal-fine','no-latch','missing-stop']}
checks={}
for name,result in [('nominal',n),('nominal-fine',f)]:
    rows=traces[name];reaction=result['meanFinalRetainingAxialN']
    checks[name]={
        'realSeatGate':result['hoistReleased'],
        'freePinNoFasteningWeld':result['pinDofs']==6 and result['fasteningEqualityCount']==0,
        'dogCleared':result['dogCleared'],
        'proofLoadApplied':rows[-1]['loadN']==2000,
        'receiverPhysicallyWithdrawn':rows[-1]['stopPositionM'][1]>-11.6,
        'receiverContactAbsentDuringProof':reaction['receivingStop']<.01,
        'toolContactAbsentDuringProof':reaction['toolPin']<.01,
        'dogCarriesProof':abs(reaction['dogBeam']-2000)<20,
        'headCarriesProof':abs(reaction['headBracket']-2000)<20,
        'boundedBeamSlack':.010<result['finalBeamAxialDisplacementM']<.020,
        'penetrationBelow1mm':result['maxAllContactPenetrationM']<.001,
        'contactPeakBelow10kN':result['peakFastenerContactN']<10000,
        'finiteNoWarnings':result['finiteState'] and sum(result['warnings'].values())==0,
        'receiverActuallySupportedInsertion':any(any('receiving_stop' in c['a']+'|'+c['b'] and abs(c['forceOnBWorldN'][0])>1 for c in row['contacts']) for row in rows if 18<row['time']<25),
        'pusherActuallyContactedPin':any(any('pusher' in c['a']+'|'+c['b'] and 'pin_head' in c['a']+'|'+c['b'] and c['normalN']>1 for c in row['contacts']) for row in rows if 18<row['time']<25),
    }
checks['controls']={'missingLatchEscapes':bad['finalBeamAxialDisplacementM']>.25 and bad['meanFinalRetainingAxialN']['dogBeam']<1,'missingStopBlocksLatch':not missing['dogCleared'] and traces['missing-stop'][-1]['loadN']==0}
checks['timestep']={'beamDisplacementWithin1mm':abs(n['finalBeamAxialDisplacementM']-f['finalBeamAxialDisplacementM'])<.001,'dogLoadWithin20N':abs(n['meanFinalRetainingAxialN']['dogBeam']-f['meanFinalRetainingAxialN']['dogBeam'])<20}
result={'integratedPrototypeSequencePassed':all(all(group.values()) for group in checks.values()),'completeConstructionFasteningCertified':False,'checks':checks,'timestepDisplacementDifferenceM':abs(n['finalBeamAxialDisplacementM']-f['finalBeamAxialDisplacementM']),'coarsePeakContactN':n['peakFastenerContactN'],'finePeakContactN':f['peakFastenerContactN']}
(HERE/'mounted-test-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if not result['integratedPrototypeSequencePassed']:raise SystemExit(1)
