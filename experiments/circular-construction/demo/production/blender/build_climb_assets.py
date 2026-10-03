"""Separate robot/rail fixture assets for the isolated validated climb trace.
Run: blender --background --python production/blender/build_climb_assets.py
The existing tower/workcell assets are never overwritten by this build.
"""
import os,sys,json,math
import bpy
from mathutils import Vector
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from build_assets import robot,Geo,empty,setup,export,lighting_camera,ROOT,OUT,SOURCE
CONTRACT_PATH=os.path.join(ROOT,'production/physics/climb-prototype/geometry-contract.json')
contract=json.load(open(CONTRACT_PATH))

def climber():
    root=robot(link_length=contract['linkLengthM'],shoulder_angle=contract['initialShoulderAngleRad'],elbow_angle=contract['initialElbowAngleRad'])
    root['scenario']='Isolated full-storey rail climb; separate from beam-receiving robot'
    root['link_length_m']=contract['linkLengthM'];root['geometry_contract']='production/physics/climb-prototype/geometry-contract.json'
    for limb in ['fl','fr','rl','rr']:
        bpy.data.objects['limb_'+limb+'_upper']['joint_limits_rad']=contract['jointRangesRad']['shoulder']
        bpy.data.objects['limb_'+limb+'_lower']['joint_limits_rad']=contract['jointRangesRad']['elbow']
    return root

def fixture():
    root=empty('ClimbRailFixture'); root['units']='metres';root['receiver_pitch_m']=contract['receiverPitchM']
    root['scope']='Isolated rail fixture; intended as the visible ideal-lock receiver geometry for climb validation.'
    g=Geo();g.beam((.76,0,0),(.76,0,5.75),.36,.40,.018,.024)
    g.box((.70,0,-.07),(1.25,1.55,.14),'EdgeSteel')
    for xx in [.23,1.16]:
        for yy in [-.56,.56]:g.bolt((xx,yy,.012),(0,0,1),.037)
    for yy in contract['railY']:
        g.box((contract['railX'],yy,2.85),(.06,.075,5.7),'EdgeSteel')
        for zz in [.2,1.1,2,2.9,3.8,4.7,5.6]:
            g.box((.655,yy,zz),(.22,.15,.12),'Steel')
            g.bolt((.527,yy,zz),(-1,0,0),.020)
    g.commit('RailSupportGeometry',root)
    for r in contract['railReceivers']:
        x,y,z=r['position'];g=Geo()
        # Two independent receiver grids per rail: exact contract positions.
        g.box((x+.008,y,z),(.03,.14,.027),'SafetyOrange' if '_f' in r['name'] else 'Blue')
        g.tube((x-.014,y,z),(x-.020,y,z),.018,'Bolts',12)
        ob=g.commit(r['name'],root);ob['capture_position_blender_m']=r['position']
    return root

r=climber(); lighting_camera((-2.4,-3.1,2.0),(.15,0,0),65);export(r,'climber-robot-climb')
setup();f=fixture();lighting_camera((-6.5,-8,5.6),(.55,0,2.75),62);export(f,'climb-rail-fixture')
# Append robot without resetting fixture/materials by parameterized base function.
r=robot(False,contract['linkLengthM'],contract['initialShoulderAngleRad'],contract['initialElbowAngleRad']);r.location=contract['startChassisPosition']
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(SOURCE,'climb-evidence-preview.blend'))
bpy.context.scene.render.resolution_x=1000;bpy.context.scene.render.resolution_y=1400
bpy.context.scene.render.filepath=os.path.join(OUT,'climb-evidence-preview.png');bpy.ops.render.render(write_still=True)
print('CLIMB_ASSETS',json.dumps({n:os.path.getsize(os.path.join(OUT,n)) for n in ['climber-robot-climb.glb','climb-rail-fixture.glb','climb-evidence-preview.png']}))
