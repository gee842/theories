"""Render the separate editable candidate at a recorded dynamics pose."""
import bpy,os,sys,json,math
from mathutils import Vector,Quaternion
sys.path.insert(0,os.path.dirname(__file__))
import build_carrier_construction as c
c.reset();c.materials();DIR=os.path.dirname(__file__)
def append(filename,rootname):
    with bpy.data.libraries.load(os.path.join(DIR,filename),link=False) as (src,dst):dst.objects=src.objects
    obs=[o for o in dst.objects if o]
    for o in obs:bpy.context.collection.objects.link(o)
    r=next(o for o in obs if o.name==rootname);keep={r,*r.children_recursive}
    for o in obs:
        if o not in keep:bpy.data.objects.remove(o,do_unlink=True)
    return r
robot=append('six-axis-carrier-candidate.blend','carrier')
trace=json.load(open(os.path.join(DIR,'../physics/carrier/candidate-continuous-step-92.928kg-mu0.65-sx0.16-trace.json')))
frame=min(trace['frames'],key=lambda f:abs(f['time']-14))
p=frame['position'];robot.location=(p[0],-p[2],p[1]);robot.rotation_mode='QUATERNION';robot.rotation_quaternion=Quaternion(frame['quaternionSourceWxyz'])
names={'hip_yaw':('hip_yaw',2),'shoulder':('hip',1),'elbow':('knee',1),'wrist_yaw':('wrist_yaw',2),'wrist':('wrist',1),'wrist_roll':('wrist_roll',0)}
for n,joints in frame['joints'].items():
    for j,angle in joints.items():suffix,axis=names[j];bpy.data.objects['limb_'+n+'_'+suffix].rotation_euler[axis]=angle
    for side,disp in zip(('a','b'),frame['jawOutwardDisplacementM'][n]):bpy.data.objects['limb_'+n+'_jaw_'+side].location.y=(-1 if side=='a' else 1)*(.045+disp)
beam=append('construction-kit.blend','kit_beam');beam.parent=robot;beam.location=(-.61,0,0);beam.rotation_euler=(0,0,math.pi/2)
column=append('construction-kit.blend','kit_column');column.location=(.93,0,1.6);column.rotation_euler.z=math.pi
c.box('inspection_ground',(0,-.06,0),(8,.12,8),'Floor',None)
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=32
scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.65,.7,.76,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=.45
for name,loc,power,size in [('Key',(-4,-5,6),1000,5),('Fill',(2,4,4),650,4)]:
    data=bpy.data.lights.new(name,'AREA');data.energy=power;data.shape='DISK';data.size=size;ob=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(ob);ob.location=loc;ob.rotation_euler=(Vector((.3,0,1.5))-ob.location).to_track_quat('-Z','Y').to_euler()
data=bpy.data.cameras.new('Candidate inspection');cam=bpy.data.objects.new('Candidate inspection',data);bpy.context.collection.objects.link(cam);cam.location=(-3.3,-4.8,3.5);cam.rotation_euler=(Vector((.15,0,1.6))-cam.location).to_track_quat('-Z','Y').to_euler();data.type='ORTHO';data.ortho_scale=4.15;scene.camera=cam
scene.render.resolution_x=1200;scene.render.resolution_y=1050;scene.render.resolution_percentage=100
scene.render.filepath=os.path.join(DIR,'six-axis-carrier-candidate-preview.png');bpy.ops.render.render(write_still=True)
bpy.context.view_layer.update();point=bpy.data.objects['limb_fl_grip_contact'].matrix_world.translation
cam.location=point+Vector((-.5,-.85,.36));cam.rotation_euler=(point-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.ortho_scale=.71
scene.render.resolution_x=1050;scene.render.resolution_y=950;scene.render.filepath=os.path.join(DIR,'six-axis-carrier-candidate-wrist.png');bpy.ops.render.render(write_still=True)
print('Recorded source time',frame['time'],'phase',frame['phase'])
