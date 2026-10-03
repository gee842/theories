"""Render a loaded articulated carrier from the same generated reusable assets."""
import bpy, os, sys, math
from mathutils import Vector
sys.path.insert(0,os.path.dirname(__file__))
import build_carrier_construction as c
c.reset();c.materials()
def append_role(filename,rootname):
    with bpy.data.libraries.load(os.path.join(c.SOURCE,filename),link=False) as (src,dst):dst.objects=src.objects
    objects=[ob for ob in dst.objects if ob]
    for ob in objects:bpy.context.collection.objects.link(ob)
    root=next(ob for ob in objects if ob.name==rootname)
    keep=set([root]+list(root.children_recursive))
    for ob in objects:
        if ob not in keep:bpy.data.objects.remove(ob,do_unlink=True)
    return root
r=append_role('construction-robots.blend','carrier');r.location.z=.8
beam=append_role('construction-kit.blend','kit_beam');beam.location=(-.61,0,.8);beam.rotation_euler.z=1.57079632679

c.box('preview_ground',(0,-.05,0),(10,.1,10),'Floor',None)
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=24
scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.66,.72,.76,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=.5
for name,loc,power,size in [('Key',(-4,-4,6),800,5),('Fill',(2,4,4),600,4)]:
    data=bpy.data.lights.new(name,'AREA');data.energy=power;data.shape='DISK';data.size=size;ob=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(ob);ob.location=loc;ob.rotation_euler=(Vector((0,0,.6))-ob.location).to_track_quat('-Z','Y').to_euler()
data=bpy.data.cameras.new('Preview');cam=bpy.data.objects.new('Preview',data);bpy.context.collection.objects.link(cam);cam.location=(-4.2,-4.7,3.4);cam.rotation_euler=(Vector((.1,0,.85))-cam.location).to_track_quat('-Z','Y').to_euler();data.type='ORTHO';data.ortho_scale=5.3;scene.camera=cam
scene.render.resolution_x=1100;scene.render.resolution_y=900;scene.render.resolution_percentage=100
scene.render.filepath=os.path.join(c.OUT,'construction-carrier-preview.png');bpy.ops.render.render(write_still=True)

# Inspect the actual closing jaws with a short independent receiver-section coupon.
# This authored static closeup is not a contact simulation or construction scene.
for name in ['limb_fl_jaw_a','limb_fl_jaw_b']:
    ob=bpy.data.objects[name];ob.location.y=math.copysign(.045,ob.location.y)
bpy.context.view_layer.update()
contact=bpy.data.objects.get('limb_fl_grip_contact')
if contact:
    position=contact.matrix_world.translation
    bpy.ops.mesh.primitive_cube_add(size=1,location=position)
    rail=bpy.context.object;rail.name='inspection_receiver_coupon';rail.scale=(.045,.05,.44);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);rail.data.materials.append(c.M['Steel'])
    cam.location=position+Vector((.52,-.75,.43));cam.rotation_euler=(position-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.ortho_scale=.74
    scene.render.resolution_x=1000;scene.render.resolution_y=900
    scene.render.filepath=os.path.join(c.OUT,'construction-clamp-preview.png');bpy.ops.render.render(write_still=True)
