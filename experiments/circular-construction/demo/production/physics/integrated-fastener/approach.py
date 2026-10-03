"""Collision-enabled maximum-stroke approach, reusing canonical control/gates.
No pin is inserted. Canonical rail weld and disabled chassis collision remain.
"""
from pathlib import Path
import json, hashlib
import numpy as np
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'mujoco'

def run():
    xml=(SOURCE/'workcell.xml').read_text()
    old='<geom type="capsule" fromto="0 0 0 .12 0 0" size=".035" mass="4" contype="0" conaffinity="0"/>'
    assert xml.count(old)==1
    xml=xml.replace(old,'<geom name="approach_tool_contact" type="capsule" fromto="0 0 0 .12 0 0" size=".035" mass="4"/>')
    (HERE/'workcell.xml').write_text(xml)
    source=(SOURCE/'simulate.py').read_text()
    assert source.count('smooth(0,.24,(t-18)/2)')==1
    source=source.replace('smooth(0,.24,(t-18)/2)','smooth(0,.35,(t-18)/2)')
    source=source.replace('frames=[]; events=[];', 'work=np.zeros(m.nu); frames=[]; events=[];')
    source=source.replace('if step<steps: mujoco.mj_step(m,d)','if step<steps:\n            work += d.actuator_force*d.actuator_velocity*m.opt.timestep\n            mujoco.mj_step(m,d)')
    source=source.replace('return trace,health', "health['actualIntegratedMotorWorkJ']=work.tolist()\n    return trace,health")
    ns={'__file__':str(SOURCE/'simulate.py'),'__name__':'reused_canonical_simulator'}
    exec(compile(source,str(SOURCE/'simulate.py'),'exec'),ns); ns['HERE']=HERE
    results={}
    for scenario in ['nominal','missed-seat']:
        trace,health=ns['run'](scenario)
        f=trace['frames'][-1];tool=f['bodies']['robot_tool'];p=np.array(tool['position']); p=np.array([p[0],-p[2],p[1]])
        # Compute actual +X capsule endpoint using exported quaternion.
        import mujoco
        q=tool['quaternion'];R=np.zeros(9);mujoco.mju_quat2Mat(R,np.array([q[3],q[0],q[1],q[2]]))
        C=ns['C'];R=C.T@R.reshape(3,3)@C
        tip=p+R@np.array([.12,0,0]);hole=np.array([6.215,-11.915,43.5375]);head=np.array([6.148,-11.915,43.5375])
        health.update({'toolCollisionEnabled':True,'actualToolEndpointZUpM':tip.tolist(),'holeCenterZUpM':hole.tolist(),'tipToHoleCenterM':(hole-tip).tolist(),'tipToAccessiblePinHeadM':(head-tip).tolist(),'distanceTipToHeadM':float(np.linalg.norm(head-tip)),'completeRobotFasteningCycle':False,'canonicalSimulatorSHA256':hashlib.sha256((SOURCE/'simulate.py').read_bytes()).hexdigest()})
        trace['provenance']['description']='Isolated collision-enabled maximum-stroke tool approach; canonical controller and actual seat gate. No insertion or fastening.'
        trace['provenance']['model']='production/physics/integrated-fastener/workcell.xml'
        for frame in trace['frames']:
            if frame['time']>18:frame['state']['note']='Maximum bounded tool stroke; still out of lug reach; no pin insertion.'
        (HERE/f'approach-{scenario}-trace.json').write_text(json.dumps(trace,separators=(',',':'))+'\n')
        (HERE/f'approach-{scenario}-validation.json').write_text(json.dumps(health,indent=2)+'\n')
        results[scenario]=health
    return results
if __name__=='__main__':
    for scenario,result in run().items():print(scenario,json.dumps(result,indent=2))
