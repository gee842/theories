"""Offline FK/route tests only; state assignment here does not advance a simulation."""
import json
import mujoco
import numpy as np
from scipy.spatial.transform import Rotation
import finite_grip_packaged as f

m=mujoco.MjModel.from_xml_string(f.model());d=mujoco.MjData(m);initial=d.qpos.copy()

def pose(name,foot,base,R):
    w=R.T@(foot-base)-np.array(f.HIP[name])-R.T@np.array([f.OFFSET,0,0])
    yaw=np.arctan2(w[1],w[0]);p=f.ik(np.hypot(w[0],w[1]),w[2])
    pre=Rotation.from_euler('z',yaw).as_matrix()@Rotation.from_euler('y',p[0]+p[1]).as_matrix()
    wy,wp,wr=Rotation.from_matrix(pre.T@R.T).as_euler('ZYX')
    for joint,value in zip(f.LIMITS,[yaw,p[0],p[1],wy,wp,wr]):
        jid=m.joint(name+'_'+joint).id
        assert m.jnt_range[jid,0]<=value<=m.jnt_range[jid,1]
        d.qpos[m.jnt_qposadr[jid]]=value

for angle in ([0,0,0],[.025,-.03,.02],[-.025,.03,-.02]):
    R=Rotation.from_rotvec(angle).as_matrix();base=np.array([.16,0,f.START]);d.qpos[:]=initial
    q=Rotation.from_matrix(R).as_quat();d.qpos[:3]=base;d.qpos[3:7]=q[[3,0,1,2]]
    for name in f.NAMES:
        target=np.array([f.RAIL,f.HIP[name][1],f.START+f.HIP[name][2]])
        pose(name,target,base,R);mujoco.mj_forward(m,d)
        assert np.linalg.norm(d.site_xpos[m.site(name+'_contact').id]-target)<1e-9
        assert np.linalg.norm(d.xmat[m.body('limb_'+name+'_grip').id].reshape(3,3)-np.eye(3))<1e-9
for t in np.linspace(0,9,19):
    d.qpos[:]=initial;base=np.array([.16,0,f.START]);d.qpos[:3]=base
    target=np.array([f.RAIL,-.32,f.START+.48])
    retreat=.055*(f.smooth(t/2) if t<2 else (1 if t<7 else 1-f.smooth((t-7)/2)))
    target[0]-=retreat;target[2]+=f.PITCH*f.smooth((t-2)/5)
    pose('fl',target,base,np.eye(3))
    for side in ('a','b'):d.qpos[m.jnt_qposadr[m.joint('fl_jaw_'+side).id]]=.105
    mujoco.mj_forward(m,d)
    assert np.linalg.norm(d.site_xpos[m.site('fl_contact').id]-target)<1e-9
    for contact in d.contact:
        names=[m.geom(g).name or '' for g in (contact.geom1,contact.geom2)]
        if any(name.startswith('fl_') for name in names):assert contact.dist>-.0001,(t,names,contact.dist)
print('Six-axis world-alignment and19-pose environment-clearance checks passed; these are not load tests.')
