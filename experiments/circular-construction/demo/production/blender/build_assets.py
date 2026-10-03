"""Reproducible SI-scale architectural/mechanical asset kit. Blender 5.2+.
Run: blender --background --python production/blender/build_assets.py
Geometry is authored Z-up; glTF exporter maps (x,y,z) -> (x,z,-y).
Meshes describe a design concept, not a certified robot or engineered tower.
"""
import bpy, math, os, json, shutil
from mathutils import Vector
from collections import defaultdict
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
OUT=os.path.join(ROOT,'public/assets')
SOURCE=os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT,exist_ok=True)

# All dimensions in metres. Open flange/web profiles are true solid geometry.
MAT={}
def material(name,color,metal=0,rough=.5):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    s=m.node_tree.nodes.get('Principled BSDF'); s.inputs['Base Color'].default_value=(*color,1)
    s.inputs['Metallic'].default_value=metal; s.inputs['Roughness'].default_value=rough
    MAT[name]=m; return name

def setup():
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    MAT.clear()
    for args in [('Steel',(.29,.36,.40),.78,.32),('EdgeSteel',(.52,.59,.61),.75,.3),('Bolts',(.12,.16,.19),.85,.28),('SafetyOrange',(.96,.23,.035),.4,.31),('Rubber',(.025,.035,.041),.05,.66),('Concrete',(.53,.55,.52),0,.89),('Deck',(.70,.70,.64),.2,.72),('Glass',(.18,.28,.29),.25,.22),('Frame',(.19,.22,.23),.75,.32),('CraneYellow',(.95,.60,.08),.3,.42),('Asphalt',(.12,.14,.15),0,.92),('Gravel',(.27,.29,.26),0,1),('Paint',(.88,.83,.63),0,.78),('White',(.8,.84,.82),.25,.32),('Blue',(.055,.17,.26),.4,.38),('Lens',(.08,.64,.81),.45,.13),('Timber',(.42,.29,.14),0,.88)]: material(*args)
    bpy.context.scene.unit_settings.system='METRIC'; bpy.context.scene.unit_settings.scale_length=1

class Geo:
    def __init__(self): self.parts=defaultdict(lambda:[[],[]])
    def solid(self,vs,fs,mat):
        verts,faces=self.parts[mat]; n=len(verts); verts.extend([tuple(v) for v in vs]); faces.extend([tuple(n+i for i in f) for f in fs])
    def box(self,c,size,mat):
        x,y,z=c; a,b,d=[s/2 for s in size]
        self.solid([(x-a,y-b,z-d),(x+a,y-b,z-d),(x+a,y+b,z-d),(x-a,y+b,z-d),(x-a,y-b,z+d),(x+a,y-b,z+d),(x+a,y+b,z+d),(x-a,y+b,z+d)],[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)],mat)
    def extrusion(self,p,q,profile,mat,ref=(0,0,1)):
        p,q=Vector(p),Vector(q); w=(q-p).normalized(); v=Vector(ref)
        if abs(w.dot(v))>.95: v=Vector((0,1,0))
        u=v.cross(w).normalized(); v=w.cross(u).normalized(); n=len(profile)
        vs=[o+u*x+v*y for o in [p,q] for x,y in profile]
        fs=[tuple(range(n-1,-1,-1)),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
        self.solid(vs,fs,mat)
    def beam(self,p,q,depth=.44,width=.22,web=.014,flange=.022,mat='Steel'):
        a,b,t,f=width/2,depth/2,web/2,flange
        shape=[(-a,-b),(a,-b),(a,-b+f),(t,-b+f),(t,b-f),(a,b-f),(a,b),(-a,b),(-a,b-f),(-t,b-f),(-t,-b+f),(-a,-b+f)]
        self.extrusion(p,q,shape,mat)
    def tube(self,p,q,r=.035,mat='Steel',sides=10):
        # Foliage primitives use rounded crown geometry, with the same single
        # authored primitive count as the former cylindrical plant proxies.
        if mat in {'Planting','LeafLight'}:
            a,b=Vector(p),Vector(q); center=(a+b)/2; h=(b-a).length/2
            vs=[]; rings=9
            for j in range(rings):
                angle=math.pi*j/(rings-1); rr=max(.001,r*math.sin(angle))
                for i in range(sides):
                    t=2*math.pi*i/sides; vs.append(center+Vector((rr*math.cos(t),rr*math.sin(t),h*math.cos(angle))))
            fs=[tuple(range(sides-1,-1,-1)),tuple(range((rings-1)*sides,rings*sides))]
            for j in range(rings-1):
                for i in range(sides):
                    k=j*sides+i; nxt=j*sides+(i+1)%sides
                    fs.append((k,nxt,nxt+sides,k+sides))
            self.solid(vs,fs,mat); return
        self.extrusion(p,q,[(r*math.cos(i*2*math.pi/sides),r*math.sin(i*2*math.pi/sides)) for i in range(sides)],mat)
    def bolt(self,p,axis=(0,1,0),r=.019):
        p=Vector(p); a=Vector(axis)
        self.tube(p-a*.006,p+a*.012,r*1.25,'EdgeSteel',12)
        self.tube(p+a*.012,p+a*.030,r,'Bolts',6)
    def drilled_plate(self,center,thickness,width,height,mat='EdgeSteel'):
        # Four rectangular quarter plates with actual cylindrical through-holes.
        # Annular face topology leaves empty hole space in both source and GLB.
        c=Vector(center); n=16
        for sy in [-1,1]:
            for sz in [-1,1]:
                cy,cz=sy*width/4,sz*height/4; outer=[]; inner=[]
                for i in range(n):
                    a=2*math.pi*i/n; dy,dz=math.cos(a),math.sin(a)
                    radius=min(width/4/max(abs(dy),1e-8),height/4/max(abs(dz),1e-8))
                    outer.append((cy+dy*radius,cz+dz*radius)); inner.append((cy+dy*.024,cz+dz*.024))
                vs=[]
                for xx in [-thickness/2,thickness/2]:
                    for ring in [outer,inner]: vs.extend([c+Vector((xx,y,z)) for y,z in ring])
                fs=[]
                for i in range(n):
                    j=(i+1)%n
                    fs.extend([(i,j,n+j,n+i),(2*n+i,3*n+i,3*n+j,2*n+j),(i,2*n+i,2*n+j,j),(n+i,n+j,3*n+j,3*n+i)])
                self.solid(vs,fs,mat)
    def commit(self,name,parent=None,bevel=0):
        root=empty(name,parent)
        for mat,(vs,fs) in self.parts.items():
            me=bpy.data.meshes.new(name+'_'+mat); me.from_pydata(vs,[],fs); me.materials.append(MAT[mat]); me.update()
            if mat in {'Planting','LeafLight'}:
                for polygon in me.polygons: polygon.use_smooth=True
            ob=bpy.data.objects.new(name+'_'+mat,me); bpy.context.collection.objects.link(ob); ob.parent=root
            if bevel:
                mod=ob.modifiers.new('Manufactured edge radius','BEVEL'); mod.width=bevel; mod.segments=2
                mod=ob.modifiers.new('Weighted corner normals','WEIGHTED_NORMAL')
        return root

def empty(name,parent=None,location=(0,0,0)):
    e=bpy.data.objects.new(name,None); bpy.context.collection.objects.link(e); e.parent=parent; e.location=location; return e

def joint(g,x,y,z,axis='x',detail=True):
    # Exposed welded seat, paired fin plates, backing plate and hex bolt heads.
    if axis=='x':
        for sign in [-1,1]:
            sx=x+sign*.19
            g.box((sx,y,z-.18),(.22,.28,.035),'EdgeSteel'); g.box((x+sign*.19,y,z),(.020,.25,.36),'EdgeSteel')
            if detail:
                for dy in [-.072,.072]:
                    for dz in [-.105,.105]: g.bolt((x+sign*.207,y+dy,z+dz),(sign,0,0),.016)
    else:
        for sign in [-1,1]:
            g.box((x,y+sign*.19,z-.18),(.28,.22,.035),'EdgeSteel'); g.box((x,y+sign*.19,z),(.25,.02,.36),'EdgeSteel')

def tower(planned=False):
    setup(); site=empty('ConstructionSite'); site['units']='metres'; site['storeys']=20; site['storey_height']=3.6; site['frame']='6m grid / 36m x 24m footprint'; site['active_floor']=12
    finish_levels=20 if planned else 8
    site['stage']='Planned inhabited design study; not simulated construction or occupancy' if planned else 'Active construction at level 12'
    site['finish_levels']=finish_levels
    material('TemporaryBrace',(.38,.43,.22),.45,.55)
    # Removable concept finishes carry no structural or physics credit.
    for args in [('PaleStone',(.88,.82,.70),.08,.68),('WarmSoffit',(.67,.40,.18),0,.65),('BronzeTrim',(.26,.20,.12),.65,.36),('Planting',(.16,.27,.12),0,.95),('LeafLight',(.27,.37,.16),0,.96),('Paving',(.62,.61,.54),0,.88)]: material(*args)
    site['simulation_note']='Architectural/mechanical visualization geometry; dynamics are supplied by the external simulation.'
    xs=list(range(-18,19,6)); ys=list(range(-12,13,6))
    # Complete steel skeleton allows full twenty-storey comprehension.
    for level in range(1,21):
        z=level*3.6; terrace_depth=6.0 if level in [3,4,10,11,17,18] else 3.0; g=Geo(); group=empty(f'Level_{level:02d}',site); group['floor']=level
        for x in xs:
            for y in ys:
                # Vary column section at lower and upper storeys.
                d=.40 if level<=10 else .34
                g.beam((x,y,z-3.6),(x,y,z),d,d,.023,.031)
                if level%3==1:
                    g.box((x,y,z-3.25),(d+.03,d+.03,.028),'EdgeSteel')
                if level<=12:
                    joint(g,x,y,z-.17,detail=level==12 or (abs(y)==12 and level<5))
        for y in ys:
            for a,b in zip(xs[:-1],xs[1:]):
                if not planned and level==12 and y==-12 and a==6: continue
                g.beam((a+.21,y,z-.19),(b-.21,y,z-.19),.48,.23)
        for x in xs:
            for a,b in zip(ys[:-1],ys[1:]): g.beam((x,a+.21,z-.19),(x,b-.21,z-.19),.42,.20)
        # Visibly triangulated outer bays and core bays.
        for y in [-12,12]:
            for x in [-18,12]:
                g.tube((x+.18,y,z-3.4),(x+5.82,y,z-.45),.052,'EdgeSteel')
                g.tube((x+5.82,y,z-3.4),(x+.18,y,z-.45),.052,'EdgeSteel')
        g.commit('StructuralSteel',group)
        if level<=(20 if planned else 12):
            d=Geo()
            for x in range(-18,18,6):
                for y in range(-12,12,6):
                    if not planned and level==12 and x>=6 and y==-12: continue
                    d.box((x+3,y+3,z+.032),(5.89,5.89,.09),'Deck')
                    # Actual corrugated underside and separate floor cassette edge channels.
                    d.box((x+3,y+.065,z-.11),(5.84,.08,.21),'EdgeSteel')
                    d.box((x+3,y+5.935,z-.11),(5.84,.08,.21),'EdgeSteel')
                    if level==12 or level==1:
                        for r in range(15): d.box((x+.2+r*.4,y+3,z-.043),(.11,5.85,.048),'EdgeSteel')
            d.commit('FloorCassettes',group)
        if level<=finish_levels:
            f=Geo()
            for side in [-1,1]:
                for x in range(-18,18,2):
                    yy=side*(12.0-terrace_depth if side==-1 and -6<=x<6 and level>=2 else 11.68)
                    # Small setbacks reveal steel column rhythm behind panels.
                    f.box((x+1,yy,z-1.8),(1.88,.06,2.58),'Glass')
                    for xx in [x+.035,x+1.965]: f.box((xx,yy-.035,z-1.8),(.055,.13,3.5),'Frame')
                    f.box((x+1,yy,z-.31),(1.94,.16,.52),'PaleStone')
                    f.box((x+1,yy,z-3.52),(1.95,.1,.075),'Frame')
            for side in [-1,1]:
                for y in range(-12,12,2):
                    f.box((side*17.68,y+1,z-1.8),(.06,1.88,2.58),'Glass')
                    f.box((side*17.68,y+.035,z-1.8),(.13,.055,3.5),'Frame')
                    f.box((side*17.68,y+1,z-.31),(.16,1.94,.52),'PaleStone')
            facade=f.commit('FacadeModules',group)
            facade['finish_scope']='Recessed glazing and 3–6m south terraces; planned design study' if planned else 'Completed levels 1–8, recessed glazing and 3–6m south terraces; original module count retained.'
    # Add-on finish modules leave engineering frame and active workcell intact.
    # Complete only levels 1–8: open level 12 and future ghost steel stay legible.
    architecture=empty('ArchitecturalFinish',site)
    architecture['scope']='Concept finish, completed levels 1–8 and forecourt; no structural or physics credit.'
    architecture['removal']='Hide this hierarchy and FacadeModules to inspect the engineering frame.'
    architecture['engineering_part_counts']='Steel, deck, core and glazing-module counts unchanged; additional finish primitives excluded from the engineering/planning inventory.'
    architecture['design']='Pale framing, recessed glazing, 3–6m south terraces, warm soffits and planted frontage.'
    for level in range(1,finish_levels+1):
        z=level*3.6; depth=6.0 if level in [3,4,10,11,17,18] else 3.0; terrace_y=-12+depth/2; finish=Geo()
        for side in [-1,1]:
            finish.box((0,side*12.28,z-.17),(36.5,.30,.30),'PaleStone')
            finish.box((side*18.28,0,z-.17),(.30,24.5,.30),'PaleStone')
            for x in [-18,-12,-6,6,12,18]:
                finish.box((x,side*12.32,z-1.92),(.18,.52,3.28),'PaleStone')
            for y in [-12,-6,0,6,12]:
                finish.box((side*18.32,y,z-1.92),(.52,.18,3.28),'PaleStone')
            for x in [-16,-14,-10,-8,8,10,14,16]:
                finish.box((x,side*12.10,z-1.92),(.075,.36,3.27),'BronzeTrim')
        if level>=2:
            # Thin finish beneath existing deck: no extra structural floor.
            finish.box((0,terrace_y,z-.29),(11.65,depth-.1,.075),'WarmSoffit')
            for x in range(-5,6):
                finish.box((x,terrace_y,z-.345),(.05,depth-.1,.025),'BronzeTrim')
            terrace_z=z-3.6
            for xx in [-5.8,5.8]:
                finish.box((xx,terrace_y,terrace_z+.14),(.12,depth-.1,.18),'PaleStone')
            finish.tube((-5.82,-11.79,terrace_z+1.09),(5.82,-11.79,terrace_z+1.09),.025,'BronzeTrim')
            for x in range(-5,6):
                finish.box((x,-11.79,terrace_z+.59),(.025,.025,1.0),'BronzeTrim')
            for x in [-4.6,4.6]:
                finish.box((x,-10.9,terrace_z+.29),(1.70,.75,.46),'PaleStone')
                finish.box((x,-10.9,terrace_z+.56),(1.57,.62,.20),'Planting')
                for dx in [-.50,0,.50]:
                    finish.tube((x+dx,-10.9,terrace_z+.6),(x+dx,-10.9,terrace_z+.98),.24,'LeafLight',10)
            if level in [3,4,10,11,17,18]:
                # Deep garden rooms: larger recoverable planter/tree assemblies
                # occupy terrace floor space without removing engineering decks.
                for x in [-3.3,3.3]:
                    finish.box((x,-8.2,terrace_z+.35),(2.5,1.6,.65),'PaleStone')
                    finish.box((x,-8.2,terrace_z+.7),(2.3,1.4,.10),'Planting')
                    finish.tube((x,-8.2,terrace_z+.7),(x,-8.2,terrace_z+2.15),.065,'Timber',12)
                    for dx,dy,h,r in [(-.35,0,1.8,.58),(.35,.12,2.0,.62),(0,-.2,2.55,.50)]:
                        finish.tube((x+dx,-8.2+dy,terrace_z+h-.50),(x+dx,-8.2+dy,terrace_z+h+.50),r,'LeafLight',16)
                    finish.box((x,-9.3,terrace_z+.45),(2.4,.4,.10),'WarmSoffit')
        module=finish.commit(f'FinishModule_{level:02d}',architecture)
        module['storey']=level; module['assembly']='Removable visual fascia, fins, soffits and terrace components.'
    forecourt=Geo()
    # Ground frontage avoids existing crane, staging stacks and containers.
    forecourt.box((-4,-16.8,.02),(33,8,.12),'Paving')
    for x in range(-20,13,3): forecourt.box((x,-16.8,.085),(.018,8,.005),'BronzeTrim')
    for yy in [-14.5,-17.5,-20.5]: forecourt.box((-4,yy,.085),(33,.018,.005),'BronzeTrim')
    forecourt.box((0,-13.1,3.32),(12,2.5,.18),'PaleStone')
    forecourt.box((0,-13.1,3.20),(11.7,2.35,.045),'WarmSoffit')
    for xx in [-5.8,5.8]: forecourt.box((xx,-14.15,1.64),(.18,.18,3.16),'PaleStone')
    for x,y in [(-17,-16.4),(-10,-18.7),(9,-18.7),(-17,-20),(15,-17.5),(-9,-14.2)]:
        forecourt.box((x,y,.40),(3.8,1.9,.65),'PaleStone')
        forecourt.box((x,y,.75),(3.55,1.65,.16),'Planting')
        forecourt.tube((x,y,.75),(x,y,3.5),.10,'Timber',10)
        # Deterministic small polygonal canopy clusters keep the model editable.
        for dx,dy,h,r in [(-.65,0,3.3,1.05),(.55,.15,3.7,1.15),(0,-.35,4.25,1.02),(0,.25,4.8,.75)]:
            forecourt.tube((x+dx,y+dy,h-.65),(x+dx,y+dy,h+.65),r,'Planting' if dx else 'LeafLight',12)
        forecourt.box((x,y-1.12,.43),(3.5,.45,.11),'WarmSoffit')
        for dx in [-1.35,1.35]: forecourt.box((x+dx,y-1.12,.23),(.14,.32,.34),'BronzeTrim')
    # Layered low planting beds edge a clear central entrance walk.
    for x in [-14,-7,7,14]:
        forecourt.box((x,-21,.30),(5.2,1.5,.4),'PaleStone')
        forecourt.box((x,-21,.54),(5,1.3,.12),'Planting')
        for dx in [-2,-1,0,1,2]:
            forecourt.tube((x+dx,-21,.55),(x+dx,-21,1.20),.45,'LeafLight',12)
    # Timber entrance ceiling and fine slats make the sheltered arrival readable.
    for x in range(-5,6): forecourt.box((x,-13.1,3.16),(.06,2.35,.05),'BronzeTrim')
    landscape=forecourt.commit('LandscapedForecourt',architecture)
    landscape['scope']='Visual paving, entrance canopy, six planter/tree clusters and four low planting beds and benches; no logistics or landscape validation.'
    # Global transverse restraint matches the structural model's Y-direction X bays.
    temporary=Geo()
    for level in range(1,21):
        z0,z1=(level-1)*3.6,level*3.6
        for xx in [-18,18]:
            for y0,y1 in [(-12,-6),(6,12)]:
                temporary.tube((xx,y0,z0),(xx,y1,z1),.052,'TemporaryBrace')
                temporary.tube((xx,y1,z0),(xx,y0,z1),.052,'TemporaryBrace')
                for yy,zz in [(y0,z0),(y1,z0),(y0,z1),(y1,z1)]:
                    temporary.box((xx,yy,zz),(.03,.27,.27),'TemporaryBrace')
    temporary.commit('TemporaryYBraces',site)
    # Demountable core: each storey is composed of framed precast panel cassettes.
    # Accessible splice hardware and recesses expose the intended disassembly path.
    core_root=empty('ConcreteCore',site)
    core_root['assembly']='Sixteen 3.6m demountable steel-framed precast cassette storeys'
    core_root['recovery']='Panels and stair modules may be recovered and reused following inspection and connection assessment.'
    core_root['structural_credit']='No core stiffness credit is taken in the OpenSees model.'
    site['foundation_scope']='Foundations and crane pads remain residual site scope; no complete concrete recovery is claimed.'
    for level in range(20 if planned else 16):
        z=level*3.6; core=Geo()
        # Two cassettes form each side wall. 40mm horizontal and 60mm vertical
        # joints remain open in the geometry rather than being drawn textures.
        for sign in [-1,1]:
            x=sign*4.2
            for cy in [.1,3.9]:
                core.box((x,cy,z+1.8),(.30,3.70,3.46),'Concrete')
                for yy in [cy-1.855,cy+1.855]:
                    core.box((x,yy,z+1.8),(.42,.05,3.54),'Steel')
                for zz in [z+.045,z+3.555]:
                    core.box((x,cy,zz),(.42,3.76,.05),'Steel')
                # Exterior lifting sockets with dark recessed insert centers.
                for yy in [cy-1.05,cy+1.05]:
                    core.tube((x+sign*.15,yy,z+3.18),(x+sign*.169,yy,z+3.18),.046,'EdgeSteel',16)
                    core.tube((x+sign*.170,yy,z+3.18),(x+sign*.173,yy,z+3.18),.023,'Rubber',16)
                if level:
                    for yy in [cy-1.4,cy+1.4]:
                        core.box((x+sign*.229,yy,z),(.035,.23,.40),'EdgeSteel')
                        for dy in [-.064,.064]:
                            for dz in [-.12,.12]: core.bolt((x+sign*.251,yy+dy,z+dz),(sign,0,0),.019)
        # Rear panels are split on the centerline with matching module frames.
        for cx in [-2.1,2.1]:
            core.box((cx,5.8,z+1.8),(4.10,.30,3.46),'Concrete')
            for xx in [cx-2.065,cx+2.065]: core.box((xx,5.8,z+1.8),(.05,.42,3.54),'Steel')
            for zz in [z+.045,z+3.555]: core.box((cx,5.8,zz),(4.16,.42,.05),'Steel')
            if level:
                for xx in [cx-1.6,cx+1.6]:
                    core.box((xx,6.029,z),(.23,.035,.40),'EdgeSteel')
                    for dx in [-.064,.064]:
                        for dz in [-.12,.12]: core.bolt((xx+dx,6.051,z+dz),(0,1,0),.019)
            for xx in [cx-1.1,cx+1.1]:
                core.tube((xx,5.95,z+3.18),(xx,5.969,z+3.18),.046,'EdgeSteel',16)
                core.tube((xx,5.970,z+3.18),(xx,5.973,z+3.18),.023,'Rubber',16)
        # Doorway uses two recoverable wall panels plus a separate lintel cassette.
        for cx in [-2.45,2.45]:
            core.box((cx,-1.8,z+1.8),(3.42,.28,3.46),'Concrete')
            for xx in [cx-1.73,cx+1.73]: core.box((xx,-1.8,z+1.8),(.04,.36,3.54),'Steel')
            for zz in [z+.045,z+3.555]: core.box((cx,-1.8,zz),(3.48,.36,.05),'Steel')
            if level:
                for xx in [cx-1.3,cx+1.3]:
                    core.box((xx,-2.005,z),(.23,.035,.40),'EdgeSteel')
                    for dx in [-.064,.064]:
                        for dz in [-.12,.12]: core.bolt((xx+dx,-2.031,z+dz),(0,-1,0),.019)
            for xx in [cx-.9,cx+.9]:
                core.tube((xx,-1.94,z+3.18),(xx,-1.962,z+3.18),.046,'EdgeSteel',16)
                core.tube((xx,-1.963,z+3.18),(xx,-1.966,z+3.18),.023,'Rubber',16)
        core.box((0,-1.8,z+3.20),(1.38,.28,.70),'Concrete')
        core.box((0,-1.8,z+2.83),(1.42,.36,.045),'Steel')
        core.box((0,-1.8,z+3.555),(1.42,.36,.05),'Steel')
        # Replaceable precast treads on paired bolted flight stringers, with landing.
        for k in range(10):
            core.box((-1.8,-.7+k*.28,z+.18+k*.18),(1.3,.30,.13),'Concrete')
            core.box((1.8,2.0-k*.28,z+1.98+k*.18),(1.3,.30,.13),'Concrete')
        for xx in [-2.39,-1.21]: core.beam((xx,-.82,z+.01),(xx,2.08,z+1.82),.15,.065,.009,.012)
        for xx in [1.21,2.39]: core.beam((xx,2.12,z+1.80),(xx,-.78,z+3.62),.15,.065,.009,.012)
        core.box((0,2.65,z+1.80),(4.95,1.10,.15),'Concrete')
        core.box((0,-1.1,z+3.6),(4.95,1.02,.15),'Concrete')
        module=core.commit(f'CoreModule_{level+1:02d}',core_root)
        module['storey']=level+1; module['reusable_after_inspection']=True
        module['joint_type']='Bolted cassette frames and accessible splice plates; inspect panel, inserts, frame and connections before reuse.'
    # Active floor temporary edge protection, with opening where member enters.
    rails=Geo(); z=43.2
    for x in range(-18,19,3):
        if 6<=x<=12: continue
        rails.tube((x,-12,z+.1),(x,-12,z+1.12),.027,'CraneYellow')
    for a,b in [(-18,5.6),(12.4,18)]:
        for dz in [.55,1.1]: rails.tube((a,-12,z+dz),(b,-12,z+dz),.023,'CraneYellow')
        rails.box(((a+b)/2,-12,z+.16),(b-a,.04,.16),'CraneYellow')
    rails.commit('ActiveFloorSafetyRails',site)
    beam=Geo(); beam.beam((-2.8,0,0),(2.8,0,0),.45,.30,.009,.018,'SafetyOrange')
    for s in [-1,1]:
        beam.drilled_plate((s*2.785,0,0),.03,.34,.45)
        for y in [-.085,.085]:
            for zz in [-.1125,.1125]: beam.bolt((s*2.806,y,zz),(s,0,0),.018)
        beam.box((s*1.6,0,.225),(.13,.08,.10),'Steel')
        beam.tube((s*1.6,-.049,.225),(s*1.6,.049,.225),.028,'Bolts')
    active=beam.commit('lifted_beam',site,bevel=.002); active.location=(9,-12,44.7)
    active['length']=5.6; active['section']='I 450 x 300 x 9 / 18mm'; active['mass_kg']=638.563; active['assembled_center']=[9,-12,43.425]
    seat=Geo()
    for xx in [6,12]:
        seat.box((xx,-12,43.18),(.65,.5,.04),'EdgeSteel')
        for yy in [-12.22,-11.78]:
            seat.box((xx,yy,43.37),(.65,.025,.38),'EdgeSteel')
            for dx in [-.2,.2]: seat.bolt((xx+dx,yy,43.32),(0,-1 if yy<-12 else 1,0),.022)
    seat.commit('ActiveConnectionSeats',site)
    # Binding origin is the actual MuJoCo mocap carrier. Runtime builds rope
    # geometry from tendon sites; no sling or crane cable is baked into this mesh.
    rig=Geo(); rig.beam((-1.6,0,0),(1.6,0,0),.11,.11,.015,.020,'CraneYellow')
    rig.box((0,0,.40),(.55,.36,.60),'CraneYellow')
    for yy in [-.21,.21]: rig.tube((0,yy-.03,.4),(0,yy+.03,.4),.21,'Bolts',24)
    rig.tube((0,0,.08),(0,0,.15),.055,'EdgeSteel')
    for ss in [-1,1]:
        rig.tube((ss*1.6,-.09,0),(ss*1.6,.09,0),.065,'EdgeSteel',20)
    hoist=rig.commit('ActiveHoist',site); hoist.location=(9,-12,46.45)
    hoist['binding']='hoist_carrier'; hoist['sling_sites']=[[-1.6,0,0],[1.6,0,0]]
    # Positive geometry for the paired rails used by ideal grip locks in MJCF.
    gr=Geo()
    for yy in [-12.25,-11.75]:
        gr.box((6.06,yy,43.9),(.06,.09,2.8),'EdgeSteel')
        for zz in [42.7,43.9,45.1]:
            gr.box((6.06,(yy-12)/2,zz),(.09,.25,.10),'Steel')
            gr.box((6.13,yy,zz),(.08,.17,.24),'Steel')
            for dz in [-.073,.073]: gr.bolt((6.181,yy,zz+dz),(1,0,0),.019)
    gr.commit('RobotGripRails',site)
    # Detailed crane tower, four chords, diagonal lattice and trolley rails.
    crane=Geo(); cx,cy=24,-12
    crane.box((cx,cy,.4),(6,6,.8),'Concrete')
    for z0 in range(0,85,3):
        for dx in [-.9,.9]:
            for dy in [-.9,.9]: crane.tube((cx+dx,cy+dy,z0),(cx+dx,cy+dy,z0+3),.095,'CraneYellow')
        for s in [-1,1]:
            crane.tube((cx-.9,cy+s*.9,z0),(cx+.9,cy+s*.9,z0+3),.05,'CraneYellow')
            crane.tube((cx+s*.9,cy-.9,z0),(cx+s*.9,cy+.9,z0+3),.05,'CraneYellow')
            crane.tube((cx-.9,cy+s*.9,z0),(cx+.9,cy+s*.9,z0),.055,'CraneYellow')
    for xx in range(-21,37,3):
        for dy,dz in [(-.7,0),(.7,0),(0,1.6)]: crane.tube((xx,cy+dy,81+dz),(xx+3,cy+dy,81+dz),.07,'CraneYellow')
        for side in [-1,1]:
            crane.tube((xx,cy+side*.7,81),(xx+3,cy,82.6),.037,'CraneYellow')
            crane.tube((xx,cy,82.6),(xx+3,cy+side*.7,81),.037,'CraneYellow')
            crane.tube((xx,cy+side*.7,81),(xx+3,cy-side*.7,81),.036,'CraneYellow')
    crane.box((32,cy,81.7),(3.5,3,1.3),'Concrete'); crane.box((22,cy-1.3,79.8),(2,1.6,2),'CraneYellow'); crane.box((21.8,cy-2.12,80.05),(1.5,.04,1.13),'Glass')
    crane.box((9,cy,81),(.9,2,.22),'Bolts')
    for xx in [-15,36]: crane.tube((cx,cy,87),(xx,cy,82.6),.035,'Bolts')
    crane.commit('TowerCrane',site)
    yard(site)
    if planned:
        site['planned_scope']='20 facade/finish storeys, 20 core modules and full floor cassettes; same 36 x 24m steel grid. Visual design only; no added simulation evidence.'
        architecture['scope']='Planned concept finish at levels 1–20 and forecourt; no structural or physics credit.'
        core_root['assembly']='Twenty planned 3.6m demountable steel-framed precast cassette storeys; design study only.'
        # Remove construction-only objects from the separate design asset.
        for name in ['TowerCrane','ActiveFloorSafetyRails','lifted_beam','ActiveConnectionSeats','ActiveHoist','RobotGripRails','TemporaryYBraces','ExternalMaterialHoist','SiteAndFabricationYard']:
            ob=bpy.data.objects.get(name)
            if ob:
                for child in list(ob.children_recursive): bpy.data.objects.remove(child,do_unlink=True)
                bpy.data.objects.remove(ob,do_unlink=True)
        ground=Geo(); ground.box((0,0,-.2),(95,80,.4),'Gravel'); ground.box((0,0,-.06),(39,27,.2),'Concrete')
        ground.commit('PlannedGround',site)
    # Dedicated close view floor cassette, fin plate assembly in site staging area.
    return site

def yard(site):
    g=Geo(); g.box((0,0,-.2),(95,80,.4),'Gravel'); g.box((0,-30,-.025),(88,12,.08),'Asphalt')
    g.box((0,0,-.06),(39,27,.2),'Concrete')
    for x in range(-42,45,6): g.box((x,-30,.024),(3,.12,.008),'Paint')
    # Pre-staged beam stacks on sleepers and packaged floor cassettes.
    for row in range(4):
        yy=19+row*2.2
        for xx in [-13,-9]: g.box((xx,yy,.16),(.25,1.8,.25),'Timber')
        for k in range(3):
            for j in range(3): g.beam((-14,yy-.6+j*.6,.53+k*.50),(-8,yy-.6+j*.6,.53+k*.50),.44,.22,.014,.022)
    for stack in range(3):
        for k in range(4):
            g.box((3+stack*6.3,22,.3+k*.25),(5.9,5.9,.12),'Deck')
            g.box((3+stack*6.3,19.1,.22+k*.25),(5.9,.08,.12),'EdgeSteel')
    # Containers, doors, corrugation, stair access, cable reels and safety barriers.
    for xx in [-29,-22]:
        g.box((xx,8,1.4),(6.05,2.44,2.7),'Blue')
        for k in range(25): g.box((xx-2.95+k*.24,6.75,1.4),(.035,.055,2.6),'EdgeSteel')
        g.box((xx+3.055,8,1.4),(.035,2.3,2.55),'White')
        for yy in [7.4,8.6]: g.tube((xx+3.1,yy,.2),(xx+3.1,yy,2.6),.026,'Bolts')
    for x in range(-39,40,3):
        for y in [-22,31]:
            g.box((x,y,.42),(2.7,.36,.8),'Concrete')
            g.tube((x-1.2,y,.85),(x-1.2,y,2),.028,'CraneYellow')
            g.tube((x-1.2,y,1.9),(x+1.2,y,1.9),.025,'CraneYellow')
    g.commit('SiteAndFabricationYard',site)
    # Lift rails and perforated external cage, visible on right elevation.
    h=Geo()
    for z in range(0,48):
        h.box((18.8,4,z+.5),(.25,.25,1),'EdgeSteel')
        if z%3==0: h.tube((18,4,z),(19,4,z),.045,'Steel')
    h.box((19.1,4,38),(2,2.5,.15),'CraneYellow')
    h.box((19.1,4,40.3),(2,2.5,.12),'CraneYellow')
    for xx in [18.2,20]:
        for yy in [2.8,5.2]: h.tube((xx,yy,38),(xx,yy,40.3),.04,'CraneYellow')
        for yy in [2.8+j*.15 for j in range(17)]: h.tube((xx,yy,38),(xx,yy,40.3),.008,'Bolts',6)
    h.commit('ExternalMaterialHoist',site)

def robot(reset=True, link_length=.32, shoulder_angle=-.35, elbow_angle=.35):
    if reset: setup()
    root=empty('robot_chassis'); root['units']='metres'; root['coordinate_system']='Z up, forward +X; GLTF converts to Y up'
    root['description']='Four articulated climbing limbs, opposed flange grippers, central torque tool. Link meshes extend +X from MuJoCo body pivots.'
    body=Geo(); body.box((0,0,0),(.40,.43,.66),'Rubber'); body.box((-.225,0,0),(.07,.39,.60),'SafetyOrange')
    body.box((.22,0,0),(.06,.36,.52),'EdgeSteel')
    for s in [-1,1]:
        body.box((-.265,s*.192,0),(.04,.035,.56),'EdgeSteel')
        for zz in [-.25,.25]: body.bolt((-.27,s*.145,zz),(-1,0,0),.017)
    body.box((-.273,0,.24),(.08,.27,.075),'Bolts')
    for yy in [-.088,.088]: body.tube((-.32,yy,.245),(-.345,yy,.245),.024,'Lens',16)
    for zz in [-.16,-.10,-.04,.02,.08]: body.box((-.27,.06,zz),(.02,.20,.017),'Bolts')
    body.box((0,0,.366),(.29,.31,.07),'Bolts')
    for yy in [-.17,.17]: body.tube((0,yy,.35),(0,yy,.44),.022,'EdgeSteel')
    body.tube((0,-.17,.44),(0,.17,.44),.022,'EdgeSteel')
    body.box((.14,0,-.43),(.08,.15,.34),'EdgeSteel')
    body.commit('BodyHousing',root,bevel=.008)
    for name,sy,sz in [('fl',-1,1),('fr',1,1),('rl',-1,-1),('rr',1,-1)]:
        shoulder=empty('limb_'+name+'_upper',root,(0,sy*.25,sz*.32)); shoulder['joint_axis']='Y'; shoulder['joint_limits_rad']=[-2.4,2.4]
        shoulder.rotation_euler[1]=shoulder_angle
        upper=Geo()
        upper.tube((0,-.065,0),(0,.065,0),.091,'EdgeSteel',24)
        upper.tube((0,sy*.067,0),(0,sy*.090,0),.064,'SafetyOrange',24)
        upper.beam((.035,0,0),(link_length-.02,0,0),.09,.08,.022,.016,'SafetyOrange')
        upper.tube((.025,sy*.055,.057),(link_length-.08,sy*.055,.057),.023,'Rubber')
        upper.tube((.14,sy*.056,.057),(link_length,sy*.056,.057),.012,'EdgeSteel')
        upper.tube((0,sy*.093,0),(link_length-.09,sy*.093,.037),.009,'Bolts')
        for xx in [0,link_length]: upper.bolt((xx,sy*.079,0),(0,sy,0),.019)
        upper.commit(name+'_UpperLinkGeometry',shoulder,bevel=.003)
        elbow=empty('limb_'+name+'_lower',shoulder,(link_length,0,0)); elbow['joint_axis']='Y'; elbow['joint_limits_rad']=[-2.7,2.7]
        elbow.rotation_euler[1]=elbow_angle
        lower=Geo(); lower.tube((0,-.065,0),(0,.065,0),.073,'EdgeSteel',20)
        lower.tube((0,sy*.067,0),(0,sy*.087,0),.043,'Bolts',20)
        lower.beam((.03,0,0),(link_length-.02,0,0),.07,.07,.018,.013,'White')
        lower.tube((.025,sy*.065,-.044),(link_length-.08,sy*.065,-.044),.020,'Rubber')
        lower.tube((.15,sy*.065,-.044),(link_length,sy*.065,-.044),.011,'EdgeSteel')
        lower.commit(name+'_LowerLinkGeometry',elbow,bevel=.003)
        wrist=empty('limb_'+name+'_grip',elbow,(link_length,0,0)); wrist['joint_axis']='Y'
        hand=Geo(); hand.tube((0,-.062,0),(0,.062,0),.065,'SafetyOrange',20)
        hand.box((.045,0,0),(.07,.22,.13),'EdgeSteel'); hand.tube((.09,-.135,0),(.09,.135,0),.022,'Bolts',16)
        for sign in [-1,1]:
            jaw=Geo(); jaw.box((.125,sign*.10,0),(.16,.036,.14),'Steel'); jaw.box((.198,sign*.076,0),(.045,.07,.14),'Rubber')
            jr=jaw.commit(name+('_JawLeft' if sign==-1 else '_JawRight'),wrist,bevel=.003); jr['travel_axis']='Y'; jr['stroke_m']=.075
        hand.commit(name+'_GripActuator',wrist,bevel=.003)
    tool=empty('robot_tool',root,(.25,0,-.55)); tool['joint_axis']='X'; g=Geo()
    g.box((-.10,0,0),(.08,.18,.15),'EdgeSteel'); g.tube((-.10,0,0),(.035,0,0),.06,'SafetyOrange',24)
    g.tube((.035,0,0),(.075,0,0),.045,'Bolts',16); g.tube((.075,0,0),(.12,0,0),.022,'EdgeSteel',6)
    g.commit('TorqueTool',tool,bevel=.002)
    return root

def export(root,stem):
    bpy.ops.object.select_all(action='DESELECT')
    for ob in [root]+list(root.children_recursive): ob.select_set(True)
    bpy.context.view_layer.objects.active=root
    bpy.ops.export_scene.gltf(filepath=os.path.join(OUT,stem+'.glb'),export_format='GLB',use_selection=True,export_extras=True,export_yup=True,export_apply=True)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(SOURCE,stem+'.blend'))

def lighting_camera(location,target,lens=44,warm=False):
    scene=bpy.context.scene; scene.world.use_nodes=True; scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.36,.43,.50,1); scene.world.node_tree.nodes['Background'].inputs[1].default_value=.5
    data=bpy.data.lights.new('Sun','SUN'); data.energy=3; data.angle=.12; ob=bpy.data.objects.new('Sun',data); bpy.context.collection.objects.link(ob); ob.rotation_euler=(.4,-.5,-.5)
    if warm:
        data.energy=3.2; data.color=(1.0,.78,.52); data.angle=.18
        ob.rotation_euler=(Vector((0,0,25))-Vector((-45,-65,70))).to_track_quat('-Z','Y').to_euler()
        scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.52,.64,.78,1)
        scene.world.node_tree.nodes['Background'].inputs[1].default_value=.65
        fill=bpy.data.lights.new('Warm frontage fill','AREA'); fill.energy=22000; fill.shape='DISK'; fill.size=35; fill.color=(1,.84,.65)
        light=bpy.data.objects.new('Warm frontage fill',fill); bpy.context.collection.objects.link(light); light.location=(10,-40,30)
        light.rotation_euler=(Vector((0,-10,25))-light.location).to_track_quat('-Z','Y').to_euler()
    camdata=bpy.data.cameras.new('PresentationCamera'); cam=bpy.data.objects.new('PresentationCamera',camdata); bpy.context.collection.objects.link(cam); cam.location=location
    cam.rotation_euler=(Vector(target)-cam.location).to_track_quat('-Z','Y').to_euler(); camdata.lens=lens; scene.camera=cam
    scene.render.engine='CYCLES'; scene.cycles.samples=16; scene.cycles.use_denoising=True
    scene.render.resolution_x=1440; scene.render.resolution_y=1440; scene.render.resolution_percentage=100
    scene.view_settings.view_transform='AgX'; return cam

def update_asset_manifest():
    # Derive inventory from exported GLBs, including separate future-study kit.
    path=os.path.join(OUT,'asset-manifest.json')
    manifest=json.load(open(path)) if os.path.exists(path) else {}
    for name in sorted(os.listdir(OUT)):
        if not name.endswith('.glb'): continue
        data=open(os.path.join(OUT,name),'rb').read()
        length=int.from_bytes(data[12:16],'little')
        doc=json.loads(data[20:20+length]); entry=manifest.setdefault(name,{})
        entry.update(bytes=len(data),nodes=len(doc.get('nodes',[])),meshes=len(doc.get('meshes',[])),materials=len(doc.get('materials',[])))
        entry.setdefault('animationNodes',[])
    for name,levels,boxes,tubes in [('tower-site.glb',8,619,115),('planned-architecture.glb',20,1495,231)]:
        manifest[name]['architecturalFinish']={'storeys':levels,'addedVisualBoxes':boxes,'addedVisualTubes':tubes,'materials':['PaleStone','WarmSoffit','BronzeTrim','Planting','LeafLight','Paving'],'scope':'Concept finish primitives excluded from existing engineering/planning inventory; no structural or physics credit.','countBasis':'Authored Geo.box and Geo.tube calls; plant tube calls generate rounded foliage crowns.','gardenRoomLevels':[3,4,10,11,17,18] if levels==20 else [3,4]}
    manifest['planned-architecture.glb']['status']='Future architectural design study; not simulated construction or occupancy.'
    manifest['planned-architecture.glb']['animationNodes']=[]
    manifest['planned-architecture.glb']['plannedInventory']={'steelBeamColumnPrimitives':1860,'floorCassettes':480,'glazingModules':1200,'coreStoreys':20,'finishModules':20,'note':'Planned steel closes the active beam bay; 20 facade/core/floor/finish storeys. Additional finish pieces are visual components, not validated individual construction lifts.'}
    with open(path,'w') as stream: json.dump(manifest,stream,indent=2); stream.write('\n')

def main():
    root=tower(); lighting_camera((116,-151,104),(0,0,32),50); export(root,'tower-site')
    # Presentation-only rigging uses the same initial world attachment sites.
    # Added AFTER site GLB export and excluded from runtime assets.
    ropes=Geo()
    for xx in [7.4,10.6]: ropes.tube((xx,-12,46.45),(xx,-12,44.925),.012,'Bolts')
    for yy in [-12.12,-11.88]: ropes.tube((9,yy,47.15),(9,yy,81),.013,'Bolts')
    preview_ropes=ropes.commit('PreviewRigging_NotExported'); preview_ropes['presentation_only']=True
    # Assembled editable presentation scene contains both robot assets.
    left=robot(False); left.location=(5.4,-12,43.9)
    right=robot(False); right.location=(12.6,-12,43.9); right.rotation_euler[2]=math.pi
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(SOURCE,'assembly-preview.blend'))
    bpy.context.scene.render.filepath=os.path.join(OUT,'tower-site-preview.png'); bpy.ops.render.render(write_still=True)
    # A second genuine Blender closeup exposes joint and section detail.
    cam=bpy.context.scene.camera; cam.location=(21,-29,50); cam.rotation_euler=(Vector((9,-11,43.5))-cam.location).to_track_quat('-Z','Y').to_euler(); cam.data.lens=56
    bpy.context.scene.render.resolution_x=1600; bpy.context.scene.render.resolution_y=1000
    bpy.context.scene.render.filepath=os.path.join(OUT,'workcell-preview.png'); bpy.ops.render.render(write_still=True)
    # Isolated upper core modules expose physical seams and reversible hardware.
    saved_visibility={ob:ob.hide_render for ob in bpy.context.scene.objects}
    core=bpy.data.objects['ConcreteCore']; keep={core,*core.children_recursive}
    for ob in bpy.context.scene.objects:
        if ob.type not in {'LIGHT','CAMERA'} and ob not in keep: ob.hide_render=True
    for module in core.children:
        if module.get('storey',0)<11:
            for ob in module.children_recursive: ob.hide_render=True
    cam.location=(16,-23,58); cam.rotation_euler=(Vector((0,1,47))-cam.location).to_track_quat('-Z','Y').to_euler(); cam.data.lens=48
    bpy.context.scene.render.resolution_x=1200; bpy.context.scene.render.resolution_y=1200
    bpy.context.scene.render.filepath=os.path.join(OUT,'core-modules-preview.png'); bpy.ops.render.render(write_still=True)
    for ob,value in saved_visibility.items(): ob.hide_render=value
    root=robot(); lighting_camera((-2.6,-3.1,2.0),(.15,0,0),65); bpy.context.scene.render.resolution_x=1200; bpy.context.scene.render.resolution_y=1000; export(root,'climber-robot')
    bpy.context.scene.render.filepath=os.path.join(OUT,'climber-robot-preview.png'); bpy.ops.render.render(write_still=True)
    # Separate, explicitly marked future asset. Never used by active simulation.
    root=tower(planned=True); lighting_camera((65,-130,8),(0,0,34),48,warm=True)
    export(root,'planned-architecture')
    bpy.context.scene.render.filepath=os.path.join(OUT,'planned-architecture-preview.png'); bpy.ops.render.render(write_still=True)
    stats={name:os.path.getsize(os.path.join(OUT,name)) for name in os.listdir(OUT) if name.endswith(('.glb','.png'))}
    for name in ['assembly-preview.blend','planned-architecture.blend']:
        shutil.copy2(os.path.join(SOURCE,name),os.path.join(OUT,name))
    update_asset_manifest()
    print('ASSET_MANIFEST '+json.dumps(stats))
if __name__=='__main__': main()
