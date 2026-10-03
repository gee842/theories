"""Render stored candidate poses offline; never called by the dynamics controller."""
from pathlib import Path
import argparse,json,struct,zlib
import mujoco,numpy as np
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--stem',default='candidate-proofload-limb-92.928kg-mu0.65-sx0.16');args=ap.parse_args()
trace=json.loads((HERE/(args.stem+'-trace.json')).read_text())
m=mujoco.MjModel.from_xml_path(str(HERE/(args.stem+'.xml')));d=mujoco.MjData(m)
m.vis.global_.offwidth=1100;m.vis.global_.offheight=900
m.vis.headlight.ambient[:]=.5;m.vis.headlight.diffuse[:]=.8
for gid in range(m.ngeom):
    n=m.geom(gid).name or ''
    if n.startswith('column_'):color=[.8,.8,.75,1]
    elif n.startswith('rail_'):color=[.34,.38,.42,1]
    elif n.startswith(('receiver_','bracket_')):color=[.7,.45,.12,1]
    elif 'pad_' in n:color=[.08,.09,.08,1]
    elif 'jaw_' in n:color=[.2,.65,.35,1]
    elif 'chassis' in n:color=[.9,.4,.08,1]
    elif 'upper_' in n or 'lower_' in n:color=[.27,.55,.75,1]
    else:color=[.5,.55,.57,1]
    m.geom_rgba[gid]=color
r=mujoco.Renderer(m,height=900,width=1100);camera=mujoco.MjvCamera();camera.lookat[:]=[.3,0,1.6];camera.distance=4.4;camera.azimuth=-135;camera.elevation=-12
C=np.array([[1,0,0],[0,0,1],[0,-1,0.]])
def save(path,p):
    h,w,_=p.shape
    def chunk(t,b):return struct.pack('>I',len(b))+t+b+struct.pack('>I',zlib.crc32(t+b)&0xffffffff)
    path.write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b''.join(b'\0'+row.tobytes() for row in p)))+chunk(b'IEND',b''))
for label,t in [('supported',7),('withdrawn',11),('recaptured',trace['frames'][-1]['time'])]:
    f=min(trace['frames'],key=lambda f:abs(f['time']-t));d.qpos[:3]=C.T@np.array(f['position']);d.qpos[3:7]=f['quaternionSourceWxyz']
    for n,js in f['joints'].items():
        for j,v in js.items():d.qpos[m.jnt_qposadr[m.joint(n+'_'+j).id]]=v
        for labelj,v in zip(('a','b'),f['jawOutwardDisplacementM'][n]):d.qpos[m.jnt_qposadr[m.joint(n+'_jaw_'+labelj).id]]=v
    mujoco.mj_forward(m,d);r.update_scene(d,camera=camera);save(HERE/(args.stem+'-'+label+'.png'),r.render())
    print(label,round(f['time'],3),f['phase'])
r.close()
