"""Attempt robot-mounted contact magazine/pusher; output is evidence, not success."""
from pathlib import Path
import json, xml.etree.ElementTree as ET
import mujoco, numpy as np
import free_pin
HERE=Path(__file__).resolve().parent

def build(timestep=.0005,scenario="nominal"):
    canonical=HERE.parent/'mujoco'
    root=ET.fromstring((canonical/'workcell.xml').read_text());root.find('option').set('timestep',str(timestep))
    c=ET.fromstring(free_pin.connector.model_xml())
    root.append(c.find('asset'));world=root.find('worldbody');cw=c.find('worldbody')
    beam=world.find("body[@name='lifted_beam']")
    for name in ['seat_left','seat_right']:
        g=world.find("body[@name='%s']/geom"%name);g.set('friction','0 0 0');g.set('condim','1')
    for g in cw.find("body[@name='beam']").findall('geom'):
        if g.get('name','').startswith('beam_bore'):beam.append(g)
    bracket=cw.find("body[@name='support_bracket']");bracket.set('pos','6.2 -12 43.2');world.append(bracket)
    pin=cw.find("body[@name='pin']");pin.set('pos','5.831 -11.915 43.326606');pin.remove(pin.find('joint'));ET.SubElement(pin,'freejoint',{'name':'pin_free'});world.append(pin)
    nose=pin.find("geom[@name='pin_nose']");nose.set('type','sphere');nose.set('size','.006');nose.set('pos','.044 0 0');nose.attrib.pop('quat',None)
    for g in pin.findall('geom'):
        if g.get('name') in ['pin_slot_top','pin_slot_bottom']:
            g.set('pos','.04 0 '+('.007' if g.get('name')=='pin_slot_top' else '-.007'));g.set('size','.005 .004 .002')
    for body in [beam,bracket,pin]:
        for g in body.iter('geom'):
            g.set('friction','0 0 0');g.set('condim','1');g.set('solref','.003 1');g.set('solimp','.99 .999 .0001')
    chassis=world.find("body[@name='robot_chassis']");tool=chassis.find("body[@name='robot_tool']");tool.set('pos','.25 .085 -.573394');tool.find('joint').set('range','0 .5');tool.remove(tool.find('geom'))
    ET.SubElement(tool,'geom',{'name':'pusher','type':'box','pos':'.114 0 0','size':'.006 .025 .02','mass':'4','friction':'0 0 0','condim':'1','solref':'.003 1'})
    magazine=ET.SubElement(chassis,'body',{'name':'magazine','pos':'.25 .085 -.573394'})
    ET.SubElement(magazine,'joint',{'name':'magazine_retract','type':'slide','axis':'1 0 0','range':'-.5 0','damping':'30'})
    for name,pos,size in [('floor','.29 0 -.030','.215 .042 .004'),('roof','.29 0 .030','.215 .042 .003'),('side_a','.29 .041 0','.215 .004 .027'),('side_b','.29 -.041 0','.215 .004 .027')]:
        ET.SubElement(magazine,'geom',{'name':'magazine_'+name,'type':'box','pos':pos,'size':size,'mass':'.5','friction':'0 0 0','condim':'1','solref':'.003 1','solimp':'.99 .999 .0001'})
    gate=ET.SubElement(magazine,'body',{'name':'magazine_gate','pos':'.238 0 0'})
    ET.SubElement(gate,'joint',{'name':'gate_open','type':'slide','axis':'0 1 0','range':'0 .10','damping':'20'})
    ET.SubElement(gate,'geom',{'name':'magazine_gate_contact','type':'box','size':'.004 .042 .030','mass':'.3','friction':'0 0 0','condim':'1','solref':'.003 1'})
    stop=ET.SubElement(world,'body',{'name':'receiving_stop','pos':'11.815 -12 43.45'})
    ET.SubElement(stop,'joint',{'name':'stop_retract','type':'slide','axis':'0 1 0','range':'0 .6','damping':'30'})
    sg=ET.SubElement(stop,'geom',{'name':'receiving_stop_contact','type':'box','size':'.01 .16 .25','mass':'20','friction':'0 0 0','condim':'1','solref':'.003 1','solimp':'.99 .999 .0001'})
    if scenario=='missing-stop':sg.set('contype','0');sg.set('conaffinity','0')
    actuators=root.find('actuator')
    for a in c.find('actuator'):
        if a.get('name')!='insertion_motor':actuators.append(a)
    ET.SubElement(actuators,'motor',{'name':'magazine_retract_motor','joint':'magazine_retract','ctrlrange':'-500 500','forcerange':'-500 500'})
    ET.SubElement(actuators,'motor',{'name':'gate_motor','joint':'gate_open','ctrlrange':'-100 100','forcerange':'-100 100'})
    ET.SubElement(actuators,'motor',{'name':'stop_motor','joint':'stop_retract','ctrlrange':'-2000 2000','forcerange':'-2000 2000'})
    xml=ET.tostring(root,encoding='unicode');(HERE/f'mounted-{scenario}{"-fine" if timestep<.0005 else ""}.xml').write_text(xml);return xml

def run(scenario="nominal",timestep=.0005):
    build(timestep,scenario);source=(HERE.parent/'mujoco/simulate.py').read_text()
    model_name='mounted-'+scenario+('-fine' if timestep<.0005 else '')+'.xml'
    source=source.replace("mujoco.MjModel.from_xml_path(str(HERE/'workcell.xml'))", "mujoco.MjModel.from_xml_path(str(HERE/"+repr(model_name)+"))")
    source=source.replace('smooth(0,.24,(t-18)/2)','smooth(0,.382,(t-18)/5)')
    source=source.replace('contacts,seat_forces=contact_data()', 'hook(m,d,released)\n        contacts,seat_forces=contact_data()')
    ns={'__file__':str(HERE/'mounted_attempt.py'),'__name__':'mounted_simulator'};exec(compile(source,'reused_canonical_simulator','exec'),ns);ns['HERE']=HERE
    rows=[];events=[];cleared=False;work=None;maxpen=0.;peak=0.;retained=[];peak_event=None;penetration_event=None
    def hook(m,d,released):
        nonlocal cleared,work,maxpen,peak,peak_event,penetration_event
        if work is None:work=np.zeros(m.nu)
        t=float(d.time);dog=m.body('retention_dog').id;beam=m.body('lifted_beam').id
        if released and not cleared and d.xpos[dog,0]-.005>d.xpos[beam,0]-2.77+.002:
            cleared=True;events.append({'time':t,'event':'dog back clears beam lug face'})
        for name in ['dog_extension','dog_extension_opposite']:
            j=m.joint(name).id;q,v=m.jnt_qposadr[j],m.jnt_dofadr[j];aid=m.actuator('dog_retractor'+('_opposite' if name.endswith('opposite') else '')).id
            d.ctrl[aid]=0 if cleared and scenario!="no-latch" else np.clip(-30-2000*d.qpos[q]-15*d.qvel[v],-100,100)
        j=m.joint('gate_open').id;q,v=m.jnt_qposadr[j],m.jnt_dofadr[j];target=.10 if released and t>17 else 0
        d.ctrl[m.actuator('gate_motor').id]=np.clip(2000*(target-d.qpos[q])-40*d.qvel[v],-100,100)
        j=m.joint('magazine_retract').id;q,v=m.jnt_qposadr[j],m.jnt_dofadr[j];target=-.4 if cleared and t>25 else 0
        d.ctrl[m.actuator('magazine_retract_motor').id]=np.clip(3000*(target-d.qpos[q])-100*d.qvel[v],-500,500)
        if cleared and t>25:
            j=m.joint('tool_extension').id;d.ctrl[m.actuator('tool_extension').id]=np.clip(-800*d.qpos[m.jnt_qposadr[j]]-70*d.qvel[m.jnt_dofadr[j]],-500,500)
        j=m.joint('stop_retract').id;q,v=m.jnt_qposadr[j],m.jnt_dofadr[j];target=.6*np.clip((t-25)/1.5,0,1) if cleared else 0
        d.ctrl[m.actuator('stop_motor').id]=np.clip(8000*(target-d.qpos[q])-200*d.qvel[v]+d.qfrc_bias[v],-2000,2000)
        departed=(d.qpos[m.jnt_qposadr[m.joint('stop_retract').id]]>.4 and d.qpos[m.jnt_qposadr[m.joint('tool_extension').id]]<.02 and d.qpos[m.jnt_qposadr[m.joint('magazine_retract').id]]<-.35)
        load=2000*np.clip((t-28)/.5,0,1) if cleared and departed else 0
        d.xfrc_applied[beam,:]=0;d.xfrc_applied[beam,0]=load
        d.xfrc_applied[beam,3:]=np.cross(np.array([d.xipos[beam,0],-11.915,43.5375])-d.xipos[beam],np.array([load,0.,0.]))
        work+=d.actuator_force*d.actuator_velocity*m.opt.timestep
        contacts=[]
        for ci,c in enumerate(d.contact):
            f=np.zeros(6);mujoco.mj_contactForce(m,d,ci,f)
            if -float(c.dist)>maxpen:penetration_event={'time':t,'geomA':m.geom(c.geom1).name,'geomB':m.geom(c.geom2).name,'penetrationM':-float(c.dist)}
            maxpen=max(maxpen,-float(c.dist))
            a,b=m.geom(c.geom1).name,m.geom(c.geom2).name
            if f[0]>.001 and any(s in a+'|'+b for s in ['pin','dog','pusher','magazine','bore','receiving_stop']):
                world=c.frame.reshape(3,3).T@f[:3]
                if float(f[0])>peak:peak_event={'time':t,'geomA':a,'geomB':b,'normalN':float(f[0]),'penetrationM':max(0,-float(c.dist))}
                contacts.append({'a':a,'b':b,'normalN':float(f[0]),'forceOnBWorldN':world.tolist()});peak=max(peak,float(f[0]))
        if t>30.25:retained.append(contacts)
        if round(t/m.opt.timestep)%40==0:rows.append({'time':t,'seatGateReleased':released,'pinPositionM':d.xpos[m.body('pin').id].tolist(),'toolPositionM':d.xpos[m.body('robot_tool').id].tolist(),'contacts':contacts,'workJ':work.tolist(),'loadN':float(load),'supportsDeparted':bool(departed),'dogExtensionM':[float(d.qpos[m.jnt_qposadr[m.joint(n).id]]) for n in ['dog_extension','dog_extension_opposite']],'stopPositionM':d.xpos[m.body('receiving_stop').id].tolist(),'magazinePositionM':d.xpos[m.body('magazine').id].tolist(),'beamPositionM':d.xpos[beam].tolist()})
    ns['hook']=hook
    trace,health=ns['run'](duration=30.5,fps=10)
    reactions={'dogBeam':0.,'headBracket':0.,'toolPin':0.,'receivingStop':0.}
    for contacts in retained:
        for contact in contacts:
            pair=contact['a']+'|'+contact['b'];force=abs(contact['forceOnBWorldN'][0])/len(retained)
            if 'dog' in pair and 'beam_bore' in pair:reactions['dogBeam']+=force
            if 'receiving_stop' in pair:reactions['receivingStop']+=force
            if 'pin_head' in pair and 'bracket_bore' in pair:reactions['headBracket']+=force
            if any(n in pair for n in ['pin','dog']) and any(n in pair for n in ['pusher','magazine']):reactions['toolPin']+=contact['normalN']/len(retained)
    health['robotMassKg']+=2.3
    health.update({'scenario':scenario,'meanFinalRetainingAxialN':reactions,'seatFriction':0,'pinDofs':6,'fasteningEqualityCount':0,'totalEqualityCount':4,'completeRobotFasteningCycle':False,'dogCleared':cleared,'eventsFastener':events,'maxAllContactPenetrationM':maxpen,'maxPenetrationEvent':penetration_event,'peakFastenerContactN':peak,'peakFastenerContactEvent':peak_event,'motorWorkJ':work.tolist(),'finalPinPositionM':rows[-1]['pinPositionM'],'finalBeamAxialDisplacementM':rows[-1]['beamPositionM'][0]-9.,'finalDogExtensionM':rows[-1]['dogExtensionM'],'notice':'Retractable receiving stop supports insertion and is withdrawn before proof. Isolated proposed tool geometry, ideal rail clamps; inspect contact proof and negative control before accepting.'})
    (HERE/f'mounted-{scenario}{"-fine" if timestep<.0005 else ""}-validation.json').write_text(json.dumps(health,indent=2)+'\n');(HERE/f'mounted-{scenario}{"-fine" if timestep<.0005 else ""}-trace.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
    print(json.dumps(health,indent=2))
if __name__=='__main__':
    for scenario in ['nominal','no-latch']:run(scenario)
