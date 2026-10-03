"""Two-storey cutaway inspection of the exact reusable stair and landing kit."""
import bpy,sys,os,math
from mathutils import Vector
sys.path.insert(0,os.path.dirname(__file__))
import build_carrier_construction as c
c.reset();c.materials()
with bpy.data.libraries.load(os.path.join(c.SOURCE,'construction-kit.blend'),link=False) as (src,dst):dst.objects=src.objects
library={ob.name:ob for ob in dst.objects if ob and not ob.parent}
def use(name,p,yaw=0):
    original=library[name];members=[original]+list(original.children_recursive);copies={old:old.copy() for old in members}
    for old,new in copies.items():
        bpy.context.collection.objects.link(new)
        if old.parent in copies:new.parent=copies[old.parent]
    r=copies[original];r.location=c.v(p);r.rotation_euler.z=yaw;return r
# Ground walking level=.16; open shaft x[-3,0],z[-3,3].
for zz in [-2.5,-1.5,-.5,.5,1.5,2.5]:use('kit_floor',(-1.5,.08,zz))
for f in range(2):
    H=f*3.2
    use('kit_stair',(-2.15,H+.96,0))
    use('kit_stair',(-.85,H+2.56,0),math.pi)
    use('kit_landing',(-1.5,H+1.68,2.25))
    use('kit_landing',(-1.5,H+3.28,-2.25))
    for xx in [-3,0]:
        for zz in [-3,0,3]:use('kit_column',(xx,H+1.6,zz))
        use('kit_beam',(xx,H+1.51,1.5),math.pi/2)
    for zz in [1.5,3]:use('kit_beam',(-1.5,H+1.51,zz))
    for zz in [-3,-1.5]:use('kit_beam',(-1.5,H+3.11,zz))
    # Floor strips outside the opening show a real connected storey edge.
    for zz in [-2.5,-1.5,-.5,.5,1.5,2.5]:use('kit_floor',(1.5,H+3.28,zz))
    # Far enclosure only; two sides intentionally omitted for this cutaway inspection.
    for xx in [-2.5,-1.5,-.5]:use('kit_core',(xx,H+1.67,3.08))
# Entrance at core near wall, and floor connection visible through it.
use('kit_entry',(-1.5,1.67,-3.08))
for xx in [-2.625,-.375]:use('kit_core_half',(xx,1.67,-3.08))
c.box('inspection_ground',(0,-.06,0),(16,.12,16),'Floor',None)
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=32
scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.65,.70,.75,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=.65
for name,loc,power,size in [('Key',(-6,-9,12),1700,8),('Fill',(5,4,9),1100,7)]:
    data=bpy.data.lights.new(name,'AREA');data.energy=power;data.shape='DISK';data.size=size;ob=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(ob);ob.location=loc;ob.rotation_euler=(Vector((-1,0,3))-ob.location).to_track_quat('-Z','Y').to_euler()
data=bpy.data.cameras.new('CirculationInspection');cam=bpy.data.objects.new('CirculationInspection',data);bpy.context.collection.objects.link(cam);cam.location=(10,10,8);cam.rotation_euler=(Vector((-1,0,3))-cam.location).to_track_quat('-Z','Y').to_euler();data.type='ORTHO';data.ortho_scale=10.5;scene.camera=cam
scene.render.resolution_x=1250;scene.render.resolution_y=1200;scene.render.resolution_percentage=100;scene.render.filepath=os.path.join(c.OUT,'construction-circulation-preview.png');bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(c.SOURCE,'construction-circulation-preview.blend'))
