"""Separate editable six-axis packaging proposal. Does not overwrite production assets."""
import os,sys,math,bpy
from mathutils import Vector
sys.path.insert(0,os.path.dirname(__file__))
import build_carrier_construction as c
OUT=os.path.dirname(__file__)
c.reset();c.materials();original_join=c.consolidate_fixed_surfaces;c.consolidate_fixed_surfaces=lambda roots:None
r=c.robot('carrier','carrier');c.consolidate_fixed_surfaces=original_join
r['candidate_status']='Six-axis finite-contact candidate; separate from shared production contract'
r['asset_revision']='six-axis-packaged-continuous-v1'
r['dry_mass_specified_kg']=340;r['central_casing_source_dimensions_m']=[.66,.44,1.0]
r['suspension_unloaded_droop_m']=.12
# Rebuild the serviceable central casing inside the evaluated narrow envelope.
for ob in list(r.children):
    if ob.type=='MESH':bpy.data.objects.remove(ob,do_unlink=True)
c.box('central_frame',(0,0,0),(.54,.90,.36),'Clamps',r)
c.box('front_bulkhead',(.30,0,0),(.06,.96,.42),'Steel',r)
for yy in [-.46,.46]:c.box('frame_crossmember',(0,yy,0),(.60,.075,.44),'Steel',r)
for zz in [-.156,.156]:
    c.box('battery_slide_gasket',(-.10,0,zz),(.266,.79,.108),'Rubber',r)
    c.box('battery_pack',(-.10,0,zz),(.25,.77,.10),'White',r)
    for yy in [-.30,.30]:
        c.box('battery_latch',(-.1,yy,math.copysign(.213,zz)),(.075,.03,.012),'Steel',r)
        c.bolt('battery_latch_pin',(-.1,yy,math.copysign(.22,zz)),r,r=.005)
    for yy in [-.16,-.10,-.04,.02,.08,.14]:c.box('battery_vent',(-.10,yy,math.copysign(.209,zz)),(.10,.012,.004),'Clamps',r)
c.box('armour_gasket',(-.295,0,0),(.058,.89,.398),'Rubber',r)
c.box('rear_armour',(-.30,0,0),(.05,.87,.39),'Shell',r)
for yy in [-.36,.36]:
    for zz in [-.15,.15]:c.bolt('armour_screw',(-.33,yy,zz),r,'x',.007)
c.box('service_nameplate',(-.33,.28,0),(.005,.07,.21),'Steel',r)
for zz in [-.05,0,.05]:c.box('identity_mark',(-.334,.28,zz),(.003,.04,.016),'White',r)
c.box('stereo_camera_housing',(.307,.285,0),(.074,.07,.29),'Clamps',r)
for zz in [-.09,.09]:
    c.tube('camera_lens_rim',(.34,.285,zz),(.356,.285,zz),.024,'Steel',r,24)
    c.tube('camera_optic',(.356,.285,zz),(.359,.285,zz),.018,'Blue',r,24)

def ring(name,parent,axis,radius,tube_radius,material,offset=(0,0,0)):
    # Ring axes are SOURCE axes; Blender already uses source XYZ.
    bpy.ops.mesh.primitive_torus_add(major_segments=40,minor_segments=8,major_radius=radius,minor_radius=tube_radius)
    ob=bpy.context.object;ob.name=name;ob.parent=parent;ob.location=offset
    if axis=='x':ob.rotation_euler.y=math.pi/2
    elif axis=='y':ob.rotation_euler.x=math.pi/2
    ob.data.materials.append(c.M[material])
    for face in ob.data.polygons:face.use_smooth=True
    return ob

for code,sy,sz in [('fl',-1,1),('fr',1,1),('rl',-1,-1),('rr',1,-1)]:
    h=bpy.data.objects['limb_'+code+'_hip'];yaw=c.empty('limb_'+code+'_hip_yaw',r)
    yaw.location=h.location.copy();h.parent=yaw;h.location=(0,0,0);yaw['joint_axis_source']='Z';yaw['added_mass_specified_kg']=3
    # Vertical shoulder-yaw reducer with a short fixed cantilever mount.
    c.box('shoulder_mount',(0,sz*.48,-sy*.265),(.14,.06,.11),'Steel',r)
    c.tube('yaw_reducer',(0,-.036,0),(0,.036,0),.078,'Clamps',yaw,32)
    for yy in [-.042,.042]:
        c.tube('yaw_bearing',(0,yy-.006,0),(0,yy+.006,0),.078,'Steel',yaw,32)
        for k in range(6):
            a=k*math.tau/6;c.bolt('yaw_service_bolt',(.057*math.cos(a),yy,.057*math.sin(a)),yaw,'y',.0055)
    # Co-centred nested wrist rings preserve the evaluated three-axis pivot location.
    w=bpy.data.objects['limb_'+code+'_wrist'];k=w.parent
    # The distal0.10m is an annular wrist mount; the shaft stops before the moving gimbal.
    for mesh in list(k.children):
        if mesh.type=='MESH' and mesh.name.split('.')[0]=='lower_link':bpy.data.objects.remove(mesh,do_unlink=True)
    c.tube('lower_link',(0,0,0),(.55,0,0),.052,'PaleFrame',k)
    mount=c.empty('limb_'+code+'_wrist_mount',k,(.65,0,0))
    ring('fixed_yaw_outer_bearing',mount,'z',.100,.004,'Clamps')
    wy=c.empty('limb_'+code+'_wrist_yaw',k);wy.location=w.location.copy();w.parent=wy;w.location=(0,0,0);wy['joint_axis_source']='Z'
    roll=c.empty('limb_'+code+'_wrist_roll',w);roll['joint_axis_source']='X'
    keep=('grip_','jaw_','opposed_','screw_drive_','replaceable_','pad_contact_','limb_')
    for ob in list(w.children):
        if ob is roll:continue
        if ob.name.startswith(keep):ob.parent=roll
        elif ob.type=='MESH':bpy.data.objects.remove(ob,do_unlink=True)
    ring('outer_yaw_ring',wy,'z',.086,.008,'Steel')
    ring('pitch_yoke_ring',w,'y',.073,.008,'PaleFrame')
    ring('roll_bearing_ring',roll,'x',.058,.008,'Clamps')
    # Opposed short trunnions leave the crossing axes clear, rather than intersecting shafts.
    for sign in [-1,1]:
        c.tube('pitch_trunnion',(0,0,sign*.073),(0,0,sign*.091),.030,'Steel',w,24)
        c.tube('pitch_motor_cover',(0,0,sign*.086),(0,0,sign*.095),.038,'Copper',w,24)
    c.hollow_tube('roll_actuator_cover',(-.036,0,0),(-.008,0,0),.044,.005,'Copper',roll,24)
    ring('yaw_encoder_band',wy,'z',.086,.0015,'Copper')
    for ss in [-1,1]:c.box('yaw_yoke_arm',(ss*.073,0,0),(.024,.045,.08),'Steel',wy)
    # Match finite-model jaw identities: a is source-Y negative, b positive.
    ja=bpy.data.objects['limb_'+code+'_jaw_a'];jb=bpy.data.objects['limb_'+code+'_jaw_b']
    ja.name='jaw_swap_temporary';jb.name='limb_'+code+'_jaw_a';ja.name='limb_'+code+'_jaw_b'
    wy['additional_wrist_mass_specified_kg']=2
    # The rendered design stays within a0.105m conservative wrist envelope.
    wy['proposed_collision_sphere_radius_m']=.105

for ob in list(r.children_recursive):
    if ob.name.startswith('wheel_steering_'):
        ob.location.z=-.22
        c.tube('extended_suspension_rod',(0,-.06,0),(0,-.22,0),.014,'PaleFrame',ob.parent,20)
# The reusable file has no installation, scenery or lights; inspectable articulated roots remain.
c.OUT=OUT;c.SOURCE=OUT;c.save_export([r],'six-axis-carrier-candidate')
print('SIX_AXIS_CANDIDATE '+os.path.join(OUT,'six-axis-carrier-candidate.blend'))
