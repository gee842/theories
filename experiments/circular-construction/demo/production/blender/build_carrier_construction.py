"""Editable carrier-oriented prototype assets. Blender 4/5; SI geometry.
Run from any directory: blender --background --python <this file>.
The independent kit and robot libraries intentionally contain no erected building.
"""
import bpy, json, math, os
from mathutils import Vector
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
OUT=os.path.join(ROOT,'public/assets'); SOURCE=os.path.dirname(__file__)
REV='carrier-construction-v1'
# All modeling helper arguments are in the consumer's right-handed Y-up system.
# Blender uses (x,-z,y), and glTF export maps back to (x,y,z).
def v(p): return Vector((p[0],-p[2],p[1]))
def reset():
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    bpy.context.scene.unit_settings.system='METRIC'
    bpy.context.scene.unit_settings.scale_length=1

def mat(name,c,metal=0,rough=.45,alpha=1):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name);m.diffuse_color=(*c,alpha);m.use_nodes=True
    bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*c,alpha);bs.inputs['Metallic'].default_value=metal;bs.inputs['Roughness'].default_value=rough
    if alpha<1: bs.inputs['Alpha'].default_value=alpha;m.surface_render_method='DITHERED'
    return m
M={}
DETAIL=False
def materials():
    for n,c,mt,r,a in [('PaleFrame',(.77,.79,.72),.65,.32,1),('Steel',(.19,.25,.27),.8,.3,1),('Clamps',(.10,.13,.16),.7,.3,1),('Copper',(.70,.36,.16),.65,.3,1),('Shell',(.93,.68,.16),.45,.29,1),('White',(.88,.92,.89),.3,.3,1),('Rubber',(.045,.060,.065),0,.85,1),('Glass',(.20,.43,.48),.3,.17,.48),('Soffit',(.63,.40,.21),0,.65,1),('Floor',(.70,.70,.64),0,.65,1),('Mineral',(.48,.49,.43),0,.8,1),('Plant',(.18,.34,.15),0,.8,1),('Blue',(.1,.48,.67),.4,.3,1)]:M[n]=mat(n,c,mt,r,a)
def empty(name,parent=None,p=(0,0,0)):
    ob=bpy.data.objects.new(name,None);bpy.context.collection.objects.link(ob);ob.parent=parent;ob.location=v(p);return ob

def finish(ob,name,parent,material):
    ob.name=name;ob.parent=parent;ob.data.materials.append(M[material]);return ob

def bevel(ob,width=.004,segments=2):
    bpy.context.view_layer.objects.active=ob
    mod=ob.modifiers.new('manufactured_edge_radius','BEVEL');mod.width=width;mod.segments=segments
    bpy.ops.object.modifier_apply(modifier=mod.name)
    for face in ob.data.polygons:face.use_smooth=True
    norm=ob.modifiers.new('weighted_surface_normals','WEIGHTED_NORMAL');norm.keep_sharp=True;norm.weight=30
    bpy.ops.object.modifier_apply(modifier=norm.name)
    return ob

def box(name,p,s,material,parent):
    bpy.ops.mesh.primitive_cube_add(size=1,location=v(p));ob=bpy.context.object;ob.scale=(s[0],s[2],s[1]);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    finish(ob,name,parent,material)
    return bevel(ob,min(.009,min(s)*.16),3) if DETAIL else ob
def tube(name,a,b,r,material,parent,vertices=16):
    aa,bb=v(a),v(b);bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r,depth=(bb-aa).length,location=(aa+bb)*.5)
    ob=bpy.context.object;ob.rotation_mode='QUATERNION';ob.rotation_quaternion=(bb-aa).to_track_quat('Z','Y');finish(ob,name,parent,material)
    for face in ob.data.polygons:face.use_smooth=len(face.vertices)==4
    return bevel(ob,min(.002,r*.04),2) if DETAIL and vertices>8 else ob
def hollow_tube(name,a,b,r,t,material,parent,n=16):
    aa,bb=v(a),v(b);axis=(bb-aa).normalized();u=axis.cross(Vector((0,0,1)))
    if u.length<.01:u=axis.cross(Vector((0,1,0)))
    u.normalize();w=axis.cross(u);verts=[]
    for center,rad in [(aa,r),(bb,r),(aa,r-t),(bb,r-t)]:
        for k in range(n):verts.append(center+rad*(u*math.cos(2*math.pi*k/n)+w*math.sin(2*math.pi*k/n)))
    faces=[]
    for k in range(n):
        j=(k+1)%n;faces.extend([(k,j,n+j,n+k),(2*n+j,2*n+k,3*n+k,3*n+j),(j,k,2*n+k,2*n+j),(n+k,n+j,3*n+j,3*n+k)])
    mesh=bpy.data.meshes.new(name);mesh.from_pydata(verts,[],faces);mesh.update();ob=bpy.data.objects.new(name,mesh);bpy.context.collection.objects.link(ob);return finish(ob,name,parent,material)
def sphere(name,p,r,material,parent):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,radius=r,location=v(p));ob=finish(bpy.context.object,name,parent,material)
    for face in ob.data.polygons:face.use_smooth=True
    return ob
def bolt(name,p,parent,axis='z',r=.009,material='Steel'):
    x,y,z=p;offset={'x':(.007,0,0),'y':(0,.007,0),'z':(0,0,.007)}[axis]
    a=tuple(p[k]-offset[k] for k in range(3));b=tuple(p[k]+offset[k] for k in range(3))
    tube(name+'_hex',a,b,r,material,parent,6)
    # Recess is inset into the head, visible as a small dark socket.
    end=tuple(p[k]+offset[k]*1.06 for k in range(3));start=tuple(p[k]+offset[k]*.85 for k in range(3))
    tube(name+'_socket',start,end,r*.47,'Clamps',parent,6)

def reducer(parent,radius=.11):
    # Coaxial motor/planetary reducer packages; source joint axis Y maps to glTF Z.
    tube('reducer_housing',(0,0,-.07),(0,0,.07),radius,'Clamps',parent,24)
    for zz in [-.075,.075]:
        tube('reducer_flange',(0,0,zz-.008),(0,0,zz+.008),radius*.96,'Steel',parent,24)
        tube('bearing_seal',(0,0,zz-.010),(0,0,zz+.010),radius*.70,'Rubber',parent,24)
        tube('hinge_shaft',(0,0,zz-.012),(0,0,zz+.012),radius*.45,'PaleFrame',parent,20)
        for k in range(6):
            angle=k*math.tau/6;bolt('service_bolt',(radius*.78*math.cos(angle),radius*.78*math.sin(angle),zz+.01),parent,r=.0055)
    tube('encoder_cover',(0,0,-.093),(0,0,-.084),radius*.48,'Copper',parent,20)

def cable(parent,points,r=.008):
    # Fixed sections remain on one link. Joint crossings use coaxial sealed feedthroughs.
    for i in range(len(points)-1):tube('fixed_cable_conduit',points[i],points[i+1],r,'Rubber',parent,8)
    for p in [points[0],points[-1]]:sphere('conduit_gland',p,r*1.35,'Steel',parent)

def gripper(w,code):
    empty('limb_'+code+'_grip_contact',w,(.135,0,0))
    w['jaw_open_center_lateral_m']=.15;w['jaw_rail_capture_center_lateral_m']=.045;w['grip_contact_relative_source_m']=[.135,0,0]
    box('grip_bridge',(.02,0,0),(.075,.11,.34),'Clamps',w)
    # Cross roller guide and central opposed-lead screw drive the two jaw carriages.
    for yy in [-.037,.037]:tube('jaw_linear_guide',(.06,yy,-.14),(.06,yy,.14),.010,'PaleFrame',w,16)
    tube('opposed_leadscrew',(.044,0,-.14),(.044,0,.14),.008,'Steel',w,16)
    tube('screw_drive_motor',(.01,0,-.14),(.01,0,-.165),.031,'Copper',w,20)
    for ss in [-1,1]:
        j=empty('limb_'+code+('_jaw_a' if ss<0 else '_jaw_b'),w,(.09,0,ss*.15))
        box('jaw_carriage',(-.019,0,0),(.032,.102,.038),'Steel',j)
        box('grip_jaw',(.045,0,0),(.13,.11,.04),'PaleFrame',j)
        box('replaceable_jaw_pad',(.048,0,-ss*.018),(.095,.076,.004),'Rubber',j)
        for yy in [-.033,.033]:bolt('jaw_pad_fastener',(.045,yy,ss*.024),j,r=.005)
        # Narrow contact ribs are on the inner faces, not fake threads across the mechanism.
        for xx in [.025,.055,.085]:box('pad_contact_rib',(xx,0,-ss*.020),(.004,.067,.002),'Clamps',j)
    tube('grip_status_window',(-.019,.04,0),(-.023,.04,0),.007,'Blue',w,12)

def plate_bolts(parent,x,y,z):
    for dx in [-.075,.075]:
        for dz in [-.075,.075]:tube('bolt',(x+dx,y-.012,z+dz),(x+dx,y+.012,z+dz),.013,'Steel',parent,6)
def root(name,dims):
    r=empty(name);r['asset_revision']=REV;r['dimensions_y_up_m']=dims;r['origin']='bounding-box center unless contract explicitly says otherwise';return r

def hollow(parent,name,p,dims,t,material='PaleFrame',axis='y'):
    x,y,z=p;w,h,d=dims
    if axis=='y':
        for sign in [-1,1]:
            box(name+'_side',(x+sign*(w-t)/2,y,z),(t,h,d),material,parent)
            box(name+'_web',(x,y,z+sign*(d-t)/2),(w-2*t,h,t),material,parent)
    else:
        for sign in [-1,1]:
            box(name+'_flange',(x,y+sign*(h-t)/2,z),(w,t,d),material,parent)
            box(name+'_web',(x,y,z+sign*(d-t)/2),(w,h-2*t,t),material,parent)
def kit():
    global DETAIL
    DETAIL=False
    roots=[]
    r=root('kit_column',[.22,3.2,.22]);roots.append(r);hollow(r,'column',(0,0,0),(.22,3.2,.22),.012)
    for yy in [-1.58,1.58]:box('splice_plate',(0,yy,0),(.28,.022,.28),'Steel',r);plate_bolts(r,0,yy,0)
    # Integral twin climbing rails are delivered as part of each column.
    for zz in [-.32,.32]:
        hollow(r,'permanent_climb_rail',(.18,0,zz),(.045,3.2,.05),.003,'Steel')
        for k in range(10):
            yy=-1.44+k*.32
            hollow_tube('rail_bracket',(.135,yy,0),(.135,yy,zz),.018,.002,'PaleFrame',r)
            box('climb_receiver',(.15,yy,zz),(.075,.008,.10),'Copper',r)
    r=root('kit_beam',[3,.18,.10]);roots.append(r);hollow(r,'beam',(0,0,0),(3,.18,.1),.006,axis='x')
    for xx in [-1.48,1.48]:
        box('end_connection',(xx,0,0),(.022,.26,.18),'Steel',r)
        for yy in [-.075,.075]:tube('captive_pin',(xx-.018,yy,0),(xx+.018,yy,0),.017,'Copper',r,8)
    r=root('kit_beam_half',[1.5,.26,.18]);roots.append(r);hollow(r,'half_beam',(0,0,0),(1.5,.18,.1),.006,axis='x')
    for xx in [-.73,.73]:
        box('half_beam_end_connection',(xx,0,0),(.022,.26,.18),'Steel',r)
        for yy in [-.075,.075]:tube('half_beam_captive_pin',(xx-.018,yy,0),(xx+.018,yy,0),.017,'Copper',r,8)
    r=root('kit_brace',[3,3.2,.08]);roots.append(r);hollow_tube('brace_tube',(-1.5,-1.6,0),(1.5,1.6,0),.03,.003,'Steel',r)
    for a in [-1,1]:box('brace_eye',(a*1.48,a*1.58,0),(.12,.13,.02),'Copper',r)
    for kind in ['floor','roof','terrace']:
        r=root('kit_'+kind,[3,.16,1]);roots.append(r)
        box('upper_walking_skin',(0,.066,0),(3,.028,1),'Floor',r)
        box('mineral_insulation',(0,.002,0),(2.88,.085,.89),'Mineral',r)
        box('warm_removable_soffit',(0,-.062,0),(2.97,.016,.97),'Soffit',r)
        for zz in [-.48,.48]:hollow(r,'cassette_edge',(0,0,zz),(3,.14,.04),.0025,axis='x')
        for xx in [-1.48,1.48]:box('cassette_end',(xx,0,0),(.0025,.14,1),'PaleFrame',r)
        if kind=='roof':box('weather_membrane',(0,.084,0),(3,.008,1),'White',r)
        if kind=='terrace':
            for xx in [-1.45,1.45]:tube('terrace_post',(xx,.07,-.47),(xx,1.1,-.47),.022,'PaleFrame',r)
            box('terrace_guard',(0,.63,-.47),(2.86,.9,.012),'Glass',r)
            tube('terrace_handrail',(-1.5,1.1,-.47),(1.5,1.1,-.47),.022,'Copper',r)
    r=root('kit_facade',[1.5,3.02,.12]);roots.append(r)
    box('insulated_glazing',(0,.12,0),(1.42,2.64,.024),'Glass',r)
    for xx in [-.725,.725]:box('vertical_mullion',(xx,0,0),(.05,3.02,.10),'PaleFrame',r)
    for yy in [-1.485,1.485,-1.26]:box('horizontal_mullion',(0,yy,0),(1.5,.05,.10),'Copper',r)
    box('insulated_spandrel',(0,-1.37,0),(1.4,.2,.08),'Soffit',r)
    r=root('kit_core',[1,3.02,.12]);roots.append(r)
    box('dry_core_mineral',(0,0,0),(.96,3.02,.075),'Mineral',r)
    for zz in [-.05,.05]:box('core_fire_board',(0,0,zz),(1,3.02,.018),'Floor',r)
    for xx in [-.48,.48]:hollow(r,'core_edge',(xx,0,0),(.035,3.02,.12),.002)
    r=root('kit_stair',[1.1,2.69,3]);roots.append(r)
    r['origin']='midpoint of 1.6m rise and 3m run, including integral guard above flight'
    r['rise_m']=1.6;r['risers']=10;r['going_m']=.30
    for k in range(10):box('stair_tread',(0,-.66+k*.16,-1.35+k*.30),(1.1,.04,.30),'Floor',r)
    for xx in [-.49,.49]:hollow_tube('stair_stringer',(xx,-.8,-1.5),(xx,.8,1.5),.045,.004,'PaleFrame',r)
    for xx in [-.525,.525]:
        for k in [0,3,6,9]:
            yy=-.64+k*.16;zz=-1.35+k*.30
            hollow_tube('stair_guard_post',(xx,yy,zz),(xx,yy+1.0,zz),.019,.002,'PaleFrame',r)
        hollow_tube('stair_handrail',(xx,.20,-1.5),(xx,1.8,1.5),.021,.002,'Copper',r)
        hollow_tube('stair_intermediate_rail',(xx,-.30,-1.5),(xx,1.3,1.5),.014,.002,'PaleFrame',r)
    r=root('kit_landing',[3,.16,1.5]);roots.append(r)
    box('landing_walking_skin',(0,.066,0),(3,.028,1.5),'Floor',r)
    box('landing_mineral_core',(0,.002,0),(2.88,.085,1.39),'Mineral',r)
    box('landing_warm_soffit',(0,-.062,0),(2.97,.016,1.47),'Soffit',r)
    for zz in [-.73,.73]:hollow(r,'landing_edge',(0,0,zz),(3,.14,.04),.0025,axis='x')
    for xx in [-1.48,1.48]:box('landing_end',(xx,0,0),(.0025,.14,1.5),'PaleFrame',r)
    r=root('kit_core_half',[.75,3.02,.12]);roots.append(r)
    box('core_half_insulation',(0,0,0),(.71,3.02,.075),'Mineral',r)
    for zz in [-.05,.05]:box('core_half_board',(0,0,zz),(.75,3.02,.018),'Floor',r)
    for xx in [-.355,.355]:hollow(r,'core_half_edge',(xx,0,0),(.035,3.02,.12),.002)
    r=root('kit_entry',[1.5,3.02,.12]);roots.append(r)
    for xx in [-.725,.725]:box('entry_jamb',(xx,0,0),(.05,3.02,.12),'PaleFrame',r)
    for yy in [-1.49,.64,1.49]:box('entry_header',(0,yy,0),(1.5,.045,.12),'Copper',r)
    box('entry_transom',(0,1.07,0),(1.4,.80,.024),'Glass',r)
    # A hinged door is visibly open; separate persistent panel, not a wall hiding the opening.
    door=empty('entry_door_hinge',r,(-.70,-.425,0));door.rotation_euler.z=math.radians(-62)
    box('entry_door_leaf',(.695,0,0),(1.39,2.08,.024),'Glass',door)
    for xx in [.025,1.365]:box('door_leaf_stile',(xx,0,0),(.045,2.08,.05),'Steel',door)
    for yy in [-1.02,1.02]:box('door_leaf_rail',(.695,yy,0),(1.39,.045,.05),'Steel',door)
    tube('door_pull',(1.23,-.15,.06),(1.23,.15,.06),.013,'Copper',door)
    r=root('kit_service',[.6,3,.16]);roots.append(r)
    box('service_backplane',(0,0,.075),(.6,3,.002),'Steel',r)
    for xx,rr,mm in [(-.19,.035,'Copper'),(0,.05,'Blue'),(.19,.025,'White')]:tube('riser_pipe',(xx,-1.5,0),(xx,1.5,0),rr,mm,r)
    for yy in [-1.35,0,1.35]:box('pipe_bracket',(0,yy,0),(.58,.055,.12),'PaleFrame',r)
    r=root('kit_pile',[.4,2,.4]);roots.append(r)
    hollow_tube('pile_shaft',(0,-1,0),(0,1,0),.084,.010,'Steel',r,20)
    # Discrete helical flights communicate screw pile; shaft and 2 mm plate mass separately in contract.
    for yy in [-.8,-.65]:hollow_tube('helical_flight',(0,yy,0),(0,yy+.014,0),.20,.116,'PaleFrame',r,24)
    for yy in [-.98,.98]:tube('segment_coupler',(0,yy-.025,0),(0,yy+.025,0),.103,'Copper',r,12)
    r=root('kit_foundation',[.7,.26,.7]);roots.append(r)
    for zz in [-.24,.24]:hollow(r,'cap_grillage',(0,0,zz),(.7,.22,.16),.012,axis='x')
    box('baseplate',(0,.12,0),(.48,.024,.48),'Steel',r);plate_bolts(r,0,.14,0)
    tube('pile_socket',(0,-.25,0),(0,-.1,0),.11,'Steel',r)
    r=root('kit_planter',[1,.5,.5]);roots.append(r)
    box('planter_box',(0,-.12,0),(1,.24,.5),'Floor',r);box('growing_medium',(0,.01,0),(.94,.035,.44),'Mineral',r)
    for xx in [-.36,-.12,.12,.36]:sphere('plant',(xx,.14,0),.16,'Plant',r)
    r=root('kit_temporary_brace',[3,3.2,.08]);roots.append(r);hollow_tube('temporary_tube',(-1.5,-1.6,0),(1.5,1.6,0),.03,.003,'Shell',r)
    return roots

def robot(name,role):
    global DETAIL
    DETAIL=True
    r=root(name,[1.5,1.6,1.3]);r['origin']='chassis center; travel ground offset y=0.8 m';r['role']=role
    r['physics_axis']='source +X reaches frame, +Z is vertical; glTF (x,z,-y)'
    box('chassis',(0,0,0),(.56,.92,.48),'Clamps',r)
    box('front_structural_bulkhead',(.30,0,0),(.06,.96,.67),'Steel',r)
    for yy in [-.46,.46]:box('frame_crossmember',(0,yy,0),(.60,.075,.68),'Steel',r)
    for zz in [-.255,.255]:
        box('battery_slide_gasket',(-.18,0,zz),(.236,.804,.178),'Rubber',r)

    for zz in [-.255,.255]:box('battery_pack',(-.18,0,zz),(.22,.78,.17),'White',r)
    box('armour_gasket',(-.343,0,0),(.076,.886,.566),'Rubber',r)
    box('armour',(-.35,0,0),(.08,.87,.55),'Shell',r)
    for yy in [-.36,.36]:
        for zz in [-.20,.20]:bolt('armour_captive_screw',(-.392,yy,zz),r,'x',.009)
    for zz in [-.348,.348]:
        for yy in [-.30,.30]:
            box('battery_latch',(-.18,yy,zz),(.085,.035,.018),'Steel',r)
            bolt('battery_latch_pivot',(-.18,yy,zz),r,r=.006)
        for yy in [-.18,-.12,-.06,0,.06,.12]:box('battery_vent',(-.18,yy,zz),(.12,.014,.006),'Clamps',r)
    box('rear_service_nameplate',(-.394,.29,0),(.008,.084,.23),'Steel',r)
    for zz in [-.055,0,.055]:box('identification_mark',(-.400,.29,zz),(.003,.042,.017),'White',r)
    for zz in [-.285,.285]:
        cable(r,[(-.1,-.33,zz),(.17,-.33,zz),(.17,.25,zz)])

    for code,sy,sz in [('fl',-1,1),('fr',1,1),('rl',-1,-1),('rr',1,-1)]:
        h=empty('limb_'+code+'_hip',r,(0,sz*.48,-sy*.32));h.rotation_euler[1]=-.8
        h['joint_axis_source']='Y';h['link_length_m']=.65
        reducer(h,.115)
        tube('upper_link',(0,0,0),(.65,0,0),.065,'Shell',h)
        box('upper_link_service_cover',(.32,.057,0),(.43,.025,.085),'Shell',h)
        for xx in [.14,.50]:bolt('link_cover_screw',(xx,.078,0),h,'y',.0055)
        cable(h,[(.11,-.072,0),(.29,-.073,0),(.53,-.072,0)],.009)

        k=empty('limb_'+code+'_knee',h,(.65,0,0));k.rotation_euler[1]=1.6
        reducer(k,.085)
        tube('lower_link',(0,0,0),(.65,0,0),.052,'PaleFrame',k)
        box('lower_link_service_cover',(.34,.048,0),(.42,.020,.065),'White',k)
        for xx in [.17,.51]:bolt('lower_cover_screw',(xx,.064,0),k,'y',.005)
        cable(k,[(.10,-.058,0),(.29,-.059,0),(.55,-.058,0)],.007)

        w=empty('limb_'+code+'_wrist',k,(.65,0,0));w.rotation_euler[1]=-.8
        reducer(w,.062)
        gripper(w,code)
        consolidate_fixed_surfaces([h])
    for code,xx,zz in [('fl',-.26,-.39),('fr',.26,-.39),('rl',-.26,.39),('rr',.26,.39)]:
        gear=empty('ground_gear_'+code,r,(xx,-.53,zz))
        tube('retraction_hinge',(0,0,-.035),(0,0,.035),.045,'Steel',gear,20)
        tube('retraction_actuator',(-.085,.035,0),(-.05,-.045,0),.021,'Copper',gear,16)
        tube('suspension_damper',(0,-.005,0),(0,-.083,0),.022,'PaleFrame',gear,16)
        tube('damper_rod',(0,-.064,0),(0,-.10,0),.014,'Steel',gear,16)
        steer=empty('wheel_steering_'+code,gear,(0,-.10,0))
        tube('steering_kingpin',(0,.005,0),(0,.028,0),.033,'Clamps',steer,20)
        for zsign in [-1,1]:box('wheel_fork',(0,.025,zsign*.068),(.05,.1,.016),'PaleFrame',steer)
        wheel=empty('wheel_'+code,steer,(0,0,0))
        tube('wheel_tyre',(0,0,-.06),(0,0,.06),.17,'Rubber',wheel,32)
        for zzside in [-.064,.064]:
            tube('wheel_rim',(0,0,zzside-.004),(0,0,zzside+.004),.112,'Steel',wheel,24)
            tube('wheel_hub',(0,0,zzside-.006),(0,0,zzside+.006),.057,'Copper',wheel,20)
            for k in range(5):
                a=math.tau*k/5;bolt('wheel_lug',(.082*math.cos(a),.082*math.sin(a),zzside+.006),wheel,r=.007)
        # Recessed tread channels stay inside the existing 0.17 m tyre radius.
        for k in range(16):
            a=math.tau*k/16;blk=box('tyre_tread',(.169*math.cos(a),.169*math.sin(a),0),(.009,.017,.10),'Clamps',wheel)
            blk.rotation_euler[1]=-a
    sensor=empty('sensor_mast',r,(-.25,.52,0))
    tube('mast',(0,0,0),(0,.12,0),.023,'Steel',sensor)
    tube('lidar_base',(0,.10,0),(0,.145,0),.062,'Clamps',sensor,24)
    tube('lidar_window',(0,.145,0),(0,.19,0),.065,'Blue',sensor,32)
    tube('lidar_top',(0,.19,0),(0,.21,0),.067,'White',sensor,24)
    box('stereo_camera_housing',(.305,.285,0),(.08,.07,.29),'Clamps',r)
    for zz in [-.09,.09]:
        tube('camera_lens_rim',(.34,.285,zz),(.358,.285,zz),.024,'Steel',r,24)
        tube('camera_optic',(.358,.285,zz),(.361,.285,zz),.018,'Blue',r,24)
    tube('status_beacon',(-.31,.48,0),(-.31,.505,0),.015,'Blue',r,16)
    if role=='carrier':
        cradle=empty('payload_cradle',r,(-.48,0,0))
        for zz in [-.50,.50]:
            box('cradle_rail',(0,0,zz),(.06,.72,.075),'Steel',cradle)
            for yy in [-.30,.30]:
                box('cradle_mount',(.06,yy,zz),(.12,.08,.095),'PaleFrame',cradle)
                bolt('cradle_mount_bolt',(-.035,yy,zz),cradle,'x',.009)
            tube('restraint_screw',(-.10,-.30,zz),(-.10,.30,zz),.013,'Steel',cradle,20)
            tube('restraint_drive',(-.10,-.33,zz),(-.10,-.25,zz),.036,'Clamps',cradle,24)

            box('cradle_fork',(-.15,-.13,zz),(.34,.08,.12),'Copper',cradle)
            for yy in [-.135,.135]:
                clamp=empty('payload_clamp_'+('l' if zz<0 else 'r')+('f' if yy<0 else 'b'),cradle,(-.20,yy,zz))
                box('clamp_carriage',(.10,0,0),(.06,.055,.07),'Steel',clamp)
                box('clamp_bridge',(.055,0,0),(.10,.052,.06),'PaleFrame',clamp)
                box('clamp_paddle',(0,0,0),(.07,.09,.18),'Shell',clamp)
                box('restraint_pad',(.015,-math.copysign(.042,yy),0),(.04,.006,.145),'Rubber',clamp)
                for zzbolt in [-.06,.06]:bolt('retainer_pad_screw',(-.039,0,zzbolt),clamp,'x',.006)

        empty('payload_mount',r,(-.61,0,0));r['payload_mount_y_up_m']=[-.61,0,0]
    else:
        tool=empty('tool_shoulder',r,(.34,-.12,0));reducer(tool,.13)
        tube('tool_upper',(0,0,0),(.45,0,0),.065,'Shell',tool)
        elbow=empty('tool_elbow',tool,(.45,0,0));reducer(elbow,.09)
        tube('tool_forearm',(0,0,0),(.36,.20,0),.047,'PaleFrame',elbow)
        wrist=empty('tool_wrist',elbow,(.36,.20,0));box('dual_tool_head',(.06,0,0),(.24,.16,.22),'Clamps',wrist)
        tube('spindle_reducer',(.08,0,.065),(.17,0,.065),.047,'Copper',wrist,24)
        tube('fastening_spindle',(.12,0,.065),(.31,0,.065),.025,'Steel',wrist,20)
        tube('fastener_socket',(.31,0,.065),(.35,0,.065),.031,'PaleFrame',wrist,12)
        tube('inspection_light',(.12,.045,-.065),(.13,.045,-.065),.012,'Blue',wrist,16)
        for yy in [-.055,.055]:
            for zz in [-.065,.065]:bolt('toolplate_fastener',(.181,yy,zz),wrist,'x',.006)

        for zz in [-.08,.02]:box('part_support_finger',(.22,-.05,zz),(.25,.05,.035),'Copper',wrist)
        empty('tool_tip',wrist,(.35,0,0));empty('payload_mount',r,(-.61,0,0))
    consolidate_fixed_surfaces([r])
    return r

def ground_machine():
    r=root('ground_builder',[2.6,3.9,2.3]);r['origin']='ground contact plane, not chassis center'
    box('body',(0,.55,0),(1.65,.55,1.8),'Shell',r)
    for xx in [-1,1]:
        box('crawler_track',(xx,.28,0),(.36,.5,2.25),'Rubber',r)
        for zz in [-.9,-.45,0,.45,.9]:tube('track_roller',(xx-.19,.28,zz),(xx+.19,.28,zz),.21,'Steel',r,12)
    turret=empty('ground_turret',r,(0,.9,0));tube('slew_ring',(0,-.05,0),(0,.05,0),.55,'Steel',turret)
    boom=empty('ground_boom',turret,(0,0,0));tube('boom',(0,0,0),(0,2,-.8),.13,'Shell',boom)
    arm=empty('ground_stick',boom,(0,2,-.8));tube('stick',(0,0,0),(0,1,-.3),.10,'White',arm)
    head=empty('ground_tool',arm,(0,1,-.3));box('rotary_pile_head',(0,-.08,0),(.44,.40,.45),'Steel',head)
    tube('drill_socket',(0,-.28,0),(0,-.5,0),.10,'Copper',head);empty('payload_mount',head,(0,-.5,0))
    for xx in [-1.2,1.2]:
        for zz in [-.95,.95]:tube('deployable_outrigger',(xx*.55,.6,zz*.6),(xx,.12,zz),.07,'PaleFrame',r);box('outrigger_foot',(xx,.08,zz),(.45,.09,.40),'Steel',r)
    return r

def rover():
    r=root('cargo_rover',[3.5,.8,2]);r['origin']='ground contact plane'
    box('cargo_deck',(0,.51,0),(3.5,.16,2),'Steel',r)
    for xx in [-1.25,0,1.25]:
        for zz in [-.91,.91]:tube('cargo_wheel',(xx,.28,zz-.10),(xx,.28,zz+.10),.28,'Rubber',r,16)
    for xx in [-1.65,1.65]:box('cargo_retainer',(xx,.68,0),(.08,.3,2),'Shell',r)
    empty('cargo_mount',r,(0,.62,0));return r

def consolidate_fixed_surfaces(roots):
    # Preserve every articulated empty. Merge only sibling meshes sharing material;
    # clone fleets then share a small number of buffers instead of hundreds of bolts.
    parents=[]
    for rootob in roots:parents.extend([rootob]+[x for x in rootob.children_recursive if x.type=='EMPTY'])
    for parent in parents:
        groups={}
        for ob in list(parent.children):
            if ob.type=='MESH' and len(ob.data.materials)==1:
                groups.setdefault(ob.data.materials[0].name,[]).append(ob)
        for material,objects in groups.items():
            if len(objects)>1:
                bpy.ops.object.select_all(action='DESELECT')
                for ob in objects:ob.select_set(True)
                bpy.context.view_layer.objects.active=objects[0]
                bpy.ops.object.join()
                objects[0].name=parent.name+'__'+material

def save_export(roots,stem):
    consolidate_fixed_surfaces(roots)
    bpy.ops.object.select_all(action='DESELECT')
    for rootob in roots:
        rootob.select_set(True)
        for ch in rootob.children_recursive:ch.select_set(True)
    bpy.context.view_layer.objects.active=roots[0]
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(SOURCE,stem+'.blend'))
    bpy.ops.export_scene.gltf(filepath=os.path.join(OUT,stem+'.glb'),export_format='GLB',use_selection=True,export_yup=True,export_extras=True)
    return {'glb':stem+'.glb','roots':[r.name for r in roots],'bytes':os.path.getsize(os.path.join(OUT,stem+'.glb'))}
def build_libraries():
    reset();materials();report=[save_export(kit(),'construction-kit')]
    reset();materials();report.append(save_export([robot('carrier','carrier'),robot('assembler','assembler'),ground_machine(),rover()],'construction-robots'))
    json.dump({'revision':REV,'exports':report},open(os.path.join(OUT,'construction-assets.json'),'w'),indent=2)
    print('CONSTRUCTION_ASSETS '+json.dumps(report))

if __name__=='__main__':build_libraries()
