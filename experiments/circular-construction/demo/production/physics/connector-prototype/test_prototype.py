"""Behavioral checks for insertion, contact load path, and falsifying controls."""
import json
from pathlib import Path
from prototype import run


def test_all():
    results = {}
    for scenario in ['nominal','misaligned','no-latch','pullout']:
        summary, frames = run(scenario, save=True)
        results[scenario] = summary
        assert summary['finiteState'] and summary['maxWarningCount'] == 0
        assert summary['equalityCount'] == 0
        assert summary['maxPenetrationM'] < .001
        assert summary['peakInsertionActuatorN'] <= 500.0001
        assert -.0001 <= summary['finalDogExtensionM'] <= .0301
        assert -.0001 <= summary['finalDogOppositeExtensionM'] <= .0301
        assert not summary['completeRobotFasteningCycle']
        if scenario == 'nominal':
            assert summary['cleared'] and not summary['aborted']
            assert .01 < summary['finalBeamDisplacementXM'] < .025
            assert 1950 < summary['meanDogToBeamAxialContactN'] < 2050
            assert 1950 < summary['meanHeadToBracketAxialContactN'] < 2050
            assert summary['finalMotorForceN'] == summary['finalDogActuatorForceN'] == 0
            assert summary['finalDogExtensionM'] > .025 and summary['finalDogOppositeExtensionM'] > .025
            assert all(f['motorForceN'] == 0 and f['dogActuatorForceN'] == 0 and f['dogOppositeActuatorForceN'] == 0 for f in frames if f['time'] > 2.05)
            assert max(abs(f['beamDisplacementXM']-summary['finalBeamDisplacementXM']) for f in frames if f['time'] > 4.5) < .0001
        elif scenario == 'misaligned':
            assert summary['aborted'] and not summary['cleared']
            assert summary['peakInsertionBeamContactN'] > 25
            assert abs(summary['finalInsertionM']) < .001
            assert summary['finalDogExtensionM'] < .001
            assert all(f['loadN'] == 0 for f in frames)
        elif scenario == 'no-latch':
            assert summary['cleared'] and not summary['aborted']
            assert summary['finalBeamDisplacementXM'] > .5
            assert summary['meanDogToBeamAxialContactN'] == 0
            assert summary['finalMotorForceN'] == 0
        elif scenario == 'pullout':
            assert summary['finalInsertionM'] > .07
            assert 240 < summary['meanDogToBeamAxialContactN'] < 260
            assert summary['finalMotorForceN'] == -250
    repeat, _ = run()
    assert repeat == results['nominal'], 'deterministic repeat must be exact'
    half, _ = run(timestep=.00025)
    assert abs(half['finalBeamDisplacementXM']-repeat['finalBeamDisplacementXM']) < .0001
    assert abs(half['meanDogToBeamAxialContactN']-repeat['meanDogToBeamAxialContactN']) < 10
    results['halfTimestep'] = half
    Path(__file__).with_name('test-results.json').write_text(json.dumps(results,indent=2)+'\n')
    print('PASS: four scenarios, physical axial load path, no active motor retention, deterministic repeat, timestep halving')


if __name__ == '__main__':
    test_all()
