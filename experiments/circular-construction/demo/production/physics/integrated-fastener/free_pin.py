"""Incremental test only: pre-inserted free pin, not robot insertion."""
from pathlib import Path
import importlib.util, json
import mujoco
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('connector',HERE.parent/'connector-prototype/prototype.py')
connector=importlib.util.module_from_spec(spec);spec.loader.exec_module(connector)

def run(scenario='nominal',dt=.0005,save=True):
    xml=connector.model_xml(timestep=dt)
    # Recess slot rails inside the shaft radial envelope; their original box
    # corners protruded beyond the 12 mm shaft and became unintended shoulders.
    xml=xml.replace('pos=".04 0 .010" size=".005 .006 .002"', 'pos=".04 0 .007" size=".005 .004 .002"')
    xml=xml.replace('pos=".04 0 -.010" size=".005 .006 .002"', 'pos=".04 0 -.007" size=".005 .004 .002"')
    xml=xml.replace('pos="-.105 .085 .3375"','pos=".009 .085 .3375"')
    xml=xml.replace('<joint name="insertion" type="slide" axis="1 0 0" limited="false" damping="6"/>','<freejoint name="pin_free"/>')
    xml=xml.replace('<motor name="insertion_motor" joint="insertion" ctrlrange="-500 500" forcerange="-500 500"/>','')
    m=mujoco.MjModel.from_xml_string(xml); d=mujoco.MjData(m);mujoco.mj_forward(m,d)
    beam=m.body('beam').id;pin=m.body('pin').id
    dogs=[m.joint(n).id for n in ['dog_extension','dog_extension_opposite']]
    bq=m.jnt_qposadr[m.joint('beam_free').id]
    settled_since=None;gate=None;maxpen=0.;work=np.zeros(m.nu);rows=[];last=[]
    for step in range(round(5/dt)):
        t=d.time
        for i,j in enumerate(dogs):
            q,v=m.jnt_qposadr[j],m.jnt_dofadr[j]
            d.ctrl[i]=np.clip(-30-2000*d.qpos[q]-15*d.qvel[v],-100,100) if scenario=='no-latch' else 0
        load=2000*np.clip((t-gate-.3)/.5,0,1) if gate is not None else 0
        d.xfrc_applied[beam,:]=0;d.xfrc_applied[beam,0]=load
        d.xfrc_applied[beam,3:]=np.cross(np.array([d.xipos[beam,0],.085,.3375])-d.xipos[beam],np.array([load,0.,0.]))
        mujoco.mj_step(m,d);mujoco.mj_forward(m,d)
        work+=d.actuator_force*d.actuator_velocity*dt
        contacts=[];seats={'seat_left':0.,'seat_right':0.};axial={'dogBeam':0.,'headBracket':0.,'slotBeam':0.}
        for ci,c in enumerate(d.contact):
            f=np.zeros(6);mujoco.mj_contactForce(m,d,ci,f)
            a,b=m.geom(c.geom1).name,m.geom(c.geom2).name
            world=c.frame.reshape(3,3).T@f[:3];maxpen=max(maxpen,-float(c.dist))
            if f[0]>.001:
                contacts.append({'geomA':a,'geomB':b,'forceOnBWorldN':world.tolist(),'normalN':float(f[0])})
                for seat in seats:
                    if seat in [a,b]:seats[seat]+=abs(world[2])
                pair=a+'|'+b
                if 'dog' in pair and 'beam_bore' in pair:axial['dogBeam']+=abs(world[0])
                if 'pin_head' in pair and 'bracket_bore' in pair:axial['headBracket']+=abs(world[0])
                if 'pin_slot_' in pair and 'beam_bore' in pair:axial['slotBeam']+=abs(world[0])
        speed=np.linalg.norm(d.qvel[m.jnt_dofadr[m.joint('beam_free').id]:m.jnt_dofadr[m.joint('beam_free').id]+6])
        stable=min(seats.values())>.35*m.body_mass[beam]*9.81 and speed<.03
        if stable and settled_since is None:settled_since=t
        if not stable:settled_since=None
        if gate is None and settled_since is not None and t-settled_since>.4:gate=float(t)
        if t>4.75:last.append(axial)
        if step%round(.02/dt)==0:rows.append({'time':float(d.time),'beamPosition':d.xpos[beam].tolist(),'pinPosition':d.xpos[pin].tolist(),'pinQuaternion':d.xquat[pin].tolist(),'dogExtensionM':[float(d.qpos[m.jnt_qposadr[j]]) for j in dogs],'loadN':float(load),'seatsN':seats,'contacts':contacts,'motorWorkJ':work.tolist()})
    result={'scenario':scenario,'test':'Pre-inserted free-body pin retention; insertion NOT demonstrated','pinDofs':6,'equalityCount':m.neq,'timestepSeconds':dt,'seatGateSeconds':gate,'finalBeamAxialDisplacementM':float(d.qpos[bq]-2.8),'finalPinPositionM':d.xpos[pin].tolist(),'meanFinalAxialReactionsN':{k:float(np.mean([r[k] for r in last])) for k in ['dogBeam','headBracket','slotBeam']},'finalDogExtensionM':[float(d.qpos[m.jnt_qposadr[j]]) for j in dogs],'motorWorkJ':work.tolist(),'maxPenetrationM':maxpen,'warnings':int(sum(w.number for w in d.warning)),'finite':bool(np.isfinite(d.qpos).all()),'completeRobotFasteningCycle':False}
    if save:
        (HERE/f'free-pin-{scenario}.xml').write_text(xml)
        (HERE/f'free-pin-{scenario}-trace.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
        (HERE/f'free-pin-{scenario}-validation.json').write_text(json.dumps(result,indent=2)+'\n')
    return result
if __name__=='__main__':
    for scenario in ['nominal','no-latch']:print(json.dumps(run(scenario),indent=2))
