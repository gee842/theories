"""Conservative casing clearance audit over recorded states; no dynamics or force claims."""
import json,xml.etree.ElementTree as E
from pathlib import Path
import mujoco,numpy as np
HERE=Path(__file__).resolve().parent
stem='candidate-continuous-step-92.928kg-mu0.65-sx0.16'
root=E.fromstring((HERE/(stem+'.xml')).read_text())
for n in ('fl','fr','rl','rr'):
 for name,parent,typ,size,quat in [
  ('hip_motor_envelope',f'limb_{n}_upper','cylinder','.116 .094','.70710678 .70710678 0 0'),
  ('knee_motor_envelope',f'limb_{n}_lower','cylinder','.086 .094','.70710678 .70710678 0 0'),
  ('wrist_gimbal_envelope',f'limb_{n}_wrist_yaw','sphere','.105',None)]:
  args={'name':n+'_'+name,'type':typ,'size':size,'mass':'0'}
  if quat:args['quat']=quat
  E.SubElement(root.find(f".//body[@name='{parent}']"),'geom',args)
xml=E.tostring(root,encoding='unicode');m=mujoco.MjModel.from_xml_string(xml);d=mujoco.MjData(m)
t=json.loads((HERE/(stem+'-trace.json')).read_text());C=np.array([[1,0,0],[0,0,1],[0,-1,0.]])
penetrations=[];maxdepth=0
for f in t['frames']:
 d.qpos[:3]=C.T@np.array(f['position']);d.qpos[3:7]=f['quaternionSourceWxyz']
 for n,joints in f['joints'].items():
  for j,v in joints.items():d.qpos[m.jnt_qposadr[m.joint(n+'_'+j).id]]=v
  for side,v in zip(('a','b'),f['jawOutwardDisplacementM'][n]):d.qpos[m.jnt_qposadr[m.joint(n+'_jaw_'+side).id]]=v
 mujoco.mj_forward(m,d)
 for c in d.contact:
  names=[m.geom(g).name or '' for g in (c.geom1,c.geom2)]
  if any('envelope' in n for n in names) and c.dist<-.0001:
   maxdepth=max(maxdepth,-float(c.dist));penetrations.append({'time':f['time'],'geoms':names,'depthM':-float(c.dist)})
r={'scope':'Recorded20Hz poses; conservative zero-mass manufactured housing proxies; not a dynamics rerun','frames':len(t['frames']),'maxPenetrationM':maxdepth,'penetrationCount':len(penetrations),'examples':penetrations[:20]}
(HERE/'manufactured-envelope-audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
(HERE/'manufactured-envelope-audit.xml').write_text(xml)
