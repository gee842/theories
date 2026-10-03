"""Structural feedback for the actual new viewer kit, with explicit stiffness assumptions."""
from pathlib import Path
import hashlib
import json
import math
import openseespy.opensees as ops
from member_graph import member_graph

HERE=Path(__file__).resolve().parent
DEMO=HERE.parents[2]
E=200e9
G=E/2.6
GRAVITY=9.81
XS=list(range(-9,10,3))
YS=list(range(-6,7,3))
H=3.2

def rhs(depth,width,thickness):
    inner_d=depth-2*thickness;inner_b=width-2*thickness
    area=depth*width-inner_d*inner_b
    iy=(width*depth**3-inner_b*inner_d**3)/12
    iz=(depth*width**3-inner_d*inner_b**3)/12
    # Thin-walled closed-section torsion approximation using the midline.
    enclosed=(depth-thickness)*(width-thickness)
    torsion=4*enclosed**2*thickness/(2*(depth+width-2*thickness))
    return dict(A=area,Iy=iy,Iz=iz,J=torsion)

COLUMN=rhs(.22,.22,.012)
BEAM=rhs(.18,.10,.006)
BRACE_A=math.pi*(.03**2-.027**2)
BRACE_I=math.pi*(.03**4-.027**4)/4

def solve(plan,storeys,pressure=500.,remove_braces=False,candidate_cross_braces=False):
    ops.wipe();ops.model('basic','-ndm',3,'-ndf',6)
    ops.geomTransf('PDelta',1,0,0,1)
    ops.geomTransf('PDelta',2,0,1,0)
    ops.uniaxialMaterial('Elastic',1,E,0.,E*1e-6 if candidate_cross_braces else E)
    nodes={};loads={};coords={};elements=[];brace_tags=[]
    for level in range(storeys+1):
        for x in XS:
            for y in YS:
                tag=len(nodes)+1;nodes[level,x,y]=tag;coords[tag]=(x,y,level*H)
                loads[tag]=[0.]*6
                ops.node(tag,x,y,level*H)
                if level==0:ops.fix(tag,1,1,1,1,1,1)
    def element(i,j,section=None,brace=False):
        tag=len(elements)+1
        if brace:
            ops.element('corotTruss',tag,i,j,BRACE_A,1);brace_tags.append(tag)
        else:
            s=section
            vertical=coords[i][2]!=coords[j][2]
            ops.element('elasticBeamColumn',tag,i,j,s['A'],E,G,s['J'],s['Iy'],s['Iz'],2 if vertical else 1)
        elements.append((tag,i,j,brace))
    graph=member_graph(plan,storeys)
    tags_by_point={tuple(round(c,8) for c in xyz):tag for tag,xyz in coords.items()}
    for xyz in graph['nodes']:
        if xyz not in tags_by_point:
            tag=len(coords)+1;tags_by_point[xyz]=tag;coords[tag]=xyz;loads[tag]=[0.]*6
            ops.node(tag,*xyz)
            if xyz[2]==0:ops.fix(tag,1,1,1,1,1,1)
    member_elements={}
    for segment in graph['segments']:
        if segment['kind']=='brace' and remove_braces:continue
        element(tags_by_point[segment['a']],tags_by_point[segment['b']],COLUMN if segment['kind']=='column' else BEAM,segment['kind']=='brace')
        member_elements.setdefault(segment['partId'],[]).append(elements[-1][0])
    if candidate_cross_braces and not remove_braces:
        for k in range(1,storeys+1):
            for x in [-9,-3,3]:
                for y in [-6,6]:element(nodes[k-1,x+3,y],nodes[k,x,y],brace=True)
            for x in [-9,9]:
                for y in [-6,3]:
                    element(nodes[k-1,x,y],nodes[k,x,y+3],brace=True)
                    element(nodes[k-1,x,y+3],nodes[k,x,y],brace=True)
    stage_time = plan['durationSeconds'] if storeys == plan['dimensions']['floors'] else max(
        p['installedAt'] for p in plan['parts'] if p['floor'] < storeys and p['floor'] >= 0 and p['kind'] != 'facade')
    total_mass=0.
    for p in plan['parts']:
        if p['temporary'] or p['floor']<0 or p['installedAt']>stage_time or (p['floor']>=storeys and not (p['kind']=='roof' and storeys==20)):
            continue
        x,height,gltf_z=p['finalPose']['position'];y=-gltf_z
        # Catalogue mass (including fittings/rails) is applied once at nearest
        # modeled level/node; this is a global stiffness screen, not deck design.
        k=max(1,min(storeys,round(height/H)))
        gx=min(XS,key=lambda a:abs(a-x));gy=min(YS,key=lambda a:abs(a-y))
        loads[nodes[k,gx,gy]][2]-=p['massKg']*GRAVITY
        total_mass+=p['massKg']
    if candidate_cross_braces:
        # Added fourteen braces per storey, same catalogued components. This is
        # a separately labelled design candidate, not the existing scene layout.
        extra_mass=14*storeys*23.396
        total_mass+=extra_mass
        for k in range(1,storeys+1):
            for x in XS:
                for y in YS:loads[nodes[k,x,y]][2]-=14*23.396*GRAVITY/35
    # A declared 3kPa useful-floor load probes the completed configuration.
    live=3000.*18*12
    for k in range(1,storeys+1):
        for x in XS:
            for y in YS:loads[nodes[k,x,y]][2]-=live/35
    # Four loaded carriers + four assembly machines on current workfront.
    for x in [-9,-3,3,9]:
        loads[nodes[storeys,x,-6]][2]-=(320+92.928+320)*GRAVITY
        loads[nodes[storeys,x,-6]][4]+=(320+92.928)*GRAVITY*.93
    ops.timeSeries('Linear',1);ops.pattern('Plain',1,1)
    for n,f in loads.items():ops.load(n,*f)
    ops.constraints('Plain');ops.numberer('RCM');ops.system('UmfPack')
    ops.test('NormUnbalance',1e-4,40);ops.algorithm('Newton')
    ops.integrator('LoadControl',.1);ops.analysis('Static')
    gravity_code=ops.analyze(10)
    ops.loadConst('-time',0)
    ops.timeSeries('Linear',2);ops.pattern('Plain',2,2)
    for k in range(1,storeys+1):
        for x in XS:
            for y in YS:ops.load(nodes[k,x,y],pressure*12*H/35,pressure*18*H/35,0,0,0,0)
    lateral_code=ops.analyze(10) if gravity_code==0 else None
    tops=[ops.nodeDisp(nodes[storeys,x,y]) for x in XS for y in YS]
    drift=max(math.hypot(ops.nodeDisp(nodes[k,x,y],1)-ops.nodeDisp(nodes[k-1,x,y],1),ops.nodeDisp(nodes[k,x,y],2)-ops.nodeDisp(nodes[k-1,x,y],2))/H for k in range(1,storeys+1) for x in XS for y in YS)
    brace_forces=[]
    for tag in brace_tags:
        force=ops.eleResponse(tag,'axialForce')
        value=force[0] if isinstance(force,list) else float(force)
        brace_forces.append(value)
    euler=math.pi**2*E*BRACE_I/(3**2+H**2)
    return dict(storeys=storeys,stageTimeSeconds=stage_time,pressureProbePa=pressure,candidateCrossBraces=candidate_cross_braces,gravityConverged=gravity_code==0,lateralConverged=lateral_code==0,
        sourceMemberCount=len(member_elements),analysisElementCount=len(elements),connectionNodeCount=len(coords),
        sourceMembersByKind={kind:sum(m['kind']==kind and m['partId'] in member_elements for m in graph['members']) for kind in ('column','beam','brace')},
        stairSupportMemberIds=[id for id in member_elements if id.startswith('stair-')],
        modeledComponentMassKg=round(total_mass,3),sectionProperties={'column':COLUMN,'beam':BEAM},
        roofMaxHorizontalDisplacementM=max(math.hypot(d[0],d[1]) for d in tops),
        roofMaxAbsXDisplacementM=max(abs(d[0]) for d in tops),roofMaxAbsYDisplacementM=max(abs(d[1]) for d in tops),
        maxInterstoreyDriftRatio=drift,braceEulerIdealPinnedN=euler,
        maxBraceCompressionDemandN=max([0]+[-f for f in brace_forces]),
        maxBraceTensionDemandN=max([0]+brace_forces),removeVisibleBraces=remove_braces,
        evidence='Conditional structural response; solver convergence is not member/joint adequacy')

def main():
    plan=json.loads((HERE/'site-plan.json').read_text())
    if plan['sourceSha256']!=hashlib.sha256((DEMO/'src/construction/runtime.ts').read_bytes()).hexdigest():
        raise ValueError('Runtime changed: re-export the actual site plan before structural analysis')
    if plan['contractSha256']!=hashlib.sha256((DEMO/'production/contracts/carrier-construction.json').read_bytes()).hexdigest():
        raise ValueError('Kit changed: re-export the actual site plan before structural analysis')
    for source,digest in plan.get('sourceDependencies',{}).items():
        if digest!=hashlib.sha256((DEMO/source).read_bytes()).hexdigest():
            raise ValueError(f'Planning dependency changed: re-export {source} before structural analysis')
    outputs=[solve(plan,n) for n in [1,2,5,10,20]]
    outputs.append(solve(plan,20,remove_braces=True))
    outputs.append(solve(plan,20,pressure=-500.))
    outputs.append(solve(plan,20,candidate_cross_braces=True))
    outputs.append(solve(plan,20,pressure=-500.,candidate_cross_braces=True))
    result={'schemaVersion':1,'runtimeSha256':plan['sourceSha256'],'contractSha256':plan['contractSha256'],
        'sourceDependencies':plan.get('sourceDependencies',{}),'compiledPlanSha256':plan.get('compiledSha256'),
        'analysisSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'memberGraphSha256':hashlib.sha256((HERE/'member_graph.py').read_bytes()).hexdigest(),
        'scope':'Source-inventory member graph including floor openings and stair headers at completed-storey snapshots; rigid assumed joints/fixed bases/PDelta elastic members',
        'assumptions':['3kPa useful-floor-load probe and simultaneous0.5kPa wind-pressure probes in both axes; not site/code-specific loads.',
        'Rigid beam-column joints assumed. Reversible joint rotational stiffness has not been established.',
        'Visible beam seat offsets projected to nearest half-storey connection datum; eccentric seat and column-saddle behavior remain unqualified. Intersecting header endpoints split the actual supporting beam/column.',
        'Screw pile heads modeled fixed without soil/pile qualification.',
        'Only visible X-plane diagonals modeled; no unmodeled Y-braces, core or floor diaphragm stiffness.',
        'Catalogue dead mass nodally lumped. Floor/cassette local bending, buckling, connection strength and fire loads excluded.',
        'Brace compression retains elastic stiffness even when ideal Euler demand is exceeded. Such a result is diagnostic, not feasible.',
        'Partial-bay erection and measured finite-grip reaction histories are not yet coupled.',
        'candidateCrossBraces cases add X braces in both directions and reduce compression stiffness to1e-6E; these are a labelled alternative, not current viewer geometry.'],
        'stages':outputs}
    (HERE/'results.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(outputs,indent=2))

if __name__=='__main__':main()
