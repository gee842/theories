"""Render stored, actually simulated qpos snapshots; no interpolation or simulation here."""
import json
import mujoco
import numpy as np
import struct
import zlib
from prototype import HERE

def save_png(path, pixels):
    height,width,_=pixels.shape
    def chunk(kind,payload):
        return struct.pack('>I',len(payload))+kind+payload+struct.pack('>I',zlib.crc32(kind+payload)&0xffffffff)
    raw=b''.join(b'\0'+row.tobytes() for row in pixels)
    path.write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',width,height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b''))

trace=json.loads((HERE/'nominal-trace.json').read_text())
model=mujoco.MjModel.from_xml_path(str(HERE/'nominal.xml'))
model.vis.global_.offwidth=900
model.vis.global_.offheight=900
model.vis.headlight.ambient[:]=[.65,.65,.65]
model.vis.headlight.diffuse[:]=[.8,.8,.8]
for gid in range(model.ngeom):
    name=model.body(int(model.geom_bodyid[gid])).name
    if name=='robot_chassis': model.geom_rgba[gid]=[1,.55,.15,1]
    elif name.endswith('grip'): model.geom_rgba[gid]=[.2,1,.5,1]
    elif name.endswith('upper'): model.geom_rgba[gid]=[.3,.7,1,1]
    elif name.endswith('lower'): model.geom_rgba[gid]=[.75,.9,1,1]
    else: model.geom_rgba[gid]=[.5,.55,.6,1]
data=mujoco.MjData(model)
renderer=mujoco.Renderer(model,height=900,width=900)
cam=mujoco.MjvCamera()
cam.lookat[:]=[.30,0,3.0]
cam.distance=7.5
cam.azimuth=125
cam.elevation=-5
indices=[0,len(trace['frames'])//2,len(trace['frames'])-1]
for label,index in zip(['start','mid','end'],indices):
    frame=trace['frames'][index]
    # State restoration is offline evidence rendering only, never climb integration.
    data.qpos[:]=np.array(frame['qpos'])
    mujoco.mj_forward(model,data)
    renderer.update_scene(data,camera=cam)
    save_png(HERE/f'climb-{label}.png',renderer.render())
    print(label,frame['time'],frame['chassisPosition'])
renderer.close()
