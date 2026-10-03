"""SI-unit, 3D staged-equilibrium study. Run with demo/numerical/.venv/bin/python."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import openseespy.opensees as ops

HERE = Path(__file__).resolve().parent
DEMO = HERE.parents[2]
PHYSICS = DEMO / "production/physics/mujoco/nominal-validation.json"
E, NU, RHO, G0 = 200e9, 0.3, 7850.0, 9.81
G = E / (2 * (1 + NU))
XS, YS, H = list(range(-18, 19, 6)), list(range(-12, 13, 6)), 3.6
ACTIVE_SPAN = 5.6
MASS_RELATIVE_TOLERANCE = 1e-10


def section(d, b, tw, tf):
    """I section: local z is depth, so Iy is the strong-axis inertia."""
    hw = d - 2 * tf
    return dict(depthM=d, widthM=b, webM=tw, flangeM=tf,
                A=2*b*tf+hw*tw, Iy=(b*d**3-(b-tw)*hw**3)/12,
                Iz=(2*tf*b**3+hw*tw**3)/12,
                J=(2*b*tf**3+hw*tw**3)/3, E=E, G=G)


SECTIONS = {"lowerColumn": section(.40, .40, .023, .031),
            "upperColumn": section(.34, .34, .023, .031),
            "xBeam": section(.48, .23, .014, .022),
            "yBeam": section(.42, .20, .014, .022),
            "activeBeam": section(.45, .30, .009, .018)}
BRACE_AREA = math.pi * .052**2


def validate_active_mass(physics):
    section_mass = SECTIONS["activeBeam"]["A"] * ACTIVE_SPAN * RHO
    imported_mass = physics["beamMassKg"]
    relative_error = abs(section_mass-imported_mass)/section_mass
    if not math.isfinite(relative_error) or relative_error > MASS_RELATIVE_TOLERANCE:
        raise ValueError(f"Active beam mass mismatch: section {section_mass:.12g} kg, "
                         f"MuJoCo {imported_mass:.12g} kg; relative error {relative_error:.6g}")
    return dict(status="passed",sectionDerivedMassKg=section_mass,
                importedMassKg=imported_mass,relativeError=relative_error,
                relativeTolerance=MASS_RELATIVE_TOLERANCE)


def beam(tag, i, j, s, transform):
    ops.element("elasticBeamColumn", tag, i, j, s["A"], E, G,
                s["J"], s["Iy"], s["Iz"], transform)


def solver():
    ops.constraints("Plain")
    ops.numberer("RCM")
    ops.system("UmfPack")
    ops.test("NormUnbalance", 1e-5, 30)
    ops.algorithm("Newton")
    ops.integrator("LoadControl", .1)
    ops.analysis("Static")


def stage(storeys, physics, missing_braces=False):
    ops.wipe()
    ops.model("basic", "-ndm", 3, "-ndf", 6)
    # Horizontal member depth is vertical. Columns have local z along global Y, matching the Blender extrusion.
    ops.geomTransf("PDelta", 1, 0, 0, 1)
    ops.geomTransf("PDelta", 2, 0, 1, 0)
    ops.uniaxialMaterial("Elastic", 1, E)
    nodes, gravity, coords = {}, {}, {}
    for k in range(storeys+1):
        for x in XS:
            for y in YS:
                n = len(nodes)+1
                nodes[k,x,y] = n
                coords[n] = (x,y,k*H)
                gravity[n] = [0.0]*6
                ops.node(n,x,y,k*H)
                if k == 0:
                    ops.fix(n,1,1,1,1,1,1)
    elements = []
    brace_tags = []

    def add(i,j,s,transform,is_brace=False):
        tag = len(elements)+1
        length = math.dist(coords[i],coords[j])
        area = BRACE_AREA if is_brace else s["A"]
        if is_brace:
            ops.element("corotTruss",tag,i,j,area,1)
            brace_tags.append(tag)
        else:
            beam(tag,i,j,s,transform)
        weight = area*length*RHO*G0
        # Explicit equivalent nodal self-weight. Local distributed-load bending omitted.
        for n in (i,j):
            gravity[n][2] -= weight/2
        elements.append((tag,i,j,is_brace))

    deck_area = 0.0
    for k in range(1,storeys+1):
        for x in XS:
            for y in YS:
                add(nodes[k-1,x,y],nodes[k,x,y],SECTIONS["lowerColumn" if k<=10 else "upperColumn"],2)
        for y in YS:
            for a,b in zip(XS[:-1],XS[1:]):
                if k==12 and y==-12 and a==6:
                    continue
                add(nodes[k,a,y],nodes[k,b,y],SECTIONS["xBeam"],1)
        for x in XS:
            for a,b in zip(YS[:-1],YS[1:]):
                add(nodes[k,x,a],nodes[k,x,b],SECTIONS["yBeam"],1)
        # X-plane perimeter braces reproduce the visible outer-bay arrangement.
        for y in (-12,12):
            for x in (-18,12):
                add(nodes[k-1,x,y],nodes[k,x+6,y],None,None,True)
                add(nodes[k-1,x+6,y],nodes[k,x,y],None,None,True)
        # Assumed temporary Y-plane braces provide stability without crediting the core.
        # The negative case omits the entire east-face temporary Y-brace system.
        for x in (-18,18):
            for y in (-12,6):
                if missing_braces and x==18:
                    continue
                add(nodes[k-1,x,y],nodes[k,x,y+6],None,None,True)
                add(nodes[k-1,x,y+6],nodes[k,x,y],None,None,True)
        # Four-node tributary area distribution; the two visible floor-12 openings remain.
        for a,b in zip(XS[:-1],XS[1:]):
            for c,d in zip(YS[:-1],YS[1:]):
                if k==12 and a>=6 and c==-12:
                    continue
                deck_area += 36
                for x,y in ((a,c),(a,d),(b,c),(b,d)):
                    gravity[nodes[k,x,y]][2] -= 3000*36/4
    construction = {}
    active = storeys>=12
    if active:
        for x,key,offset in ((6,"seat_left",.2),(12,"seat_right",-.2)):
            n = nodes[12,x,-12]
            force = physics["finalSeatLoadsN"][key]
            construction[n] = [0,0,-force,0,offset*force,0]
        # Lump the 137 kg robot to the adjacent column; its x=5.4 CG gives a 0.6 m arm.
        n = nodes[12,6,-12]
        construction[n][2] -= physics["robotMassKg"]*G0
        construction[n][4] -= .6*physics["robotMassKg"]*G0
    ops.timeSeries("Linear",1)
    ops.pattern("Plain",1,1)
    for n,load in gravity.items():
        ops.load(n,*load)
    solver()
    gravity_code = ops.analyze(10)
    ops.loadConst("-time",0)
    ops.timeSeries("Linear",2)
    ops.pattern("Plain",2,2)
    for n,load in construction.items():
        ops.load(n,*load)
    # A declared 0.5 kPa pressure probe in each horizontal axis, not a code wind load.
    lateral = {}
    for k in range(1,storeys+1):
        for x in XS:
            for y in YS:
                n = nodes[k,x,y]
                lateral[n] = [500*24*H/35,500*36*H/35,0,0,0,0]
                ops.load(n,*lateral[n])
    service_code = ops.analyze(10) if gravity_code==0 else -999
    ops.reactions()
    reaction = [sum(ops.nodeReaction(nodes[0,x,y],d+1) for x in XS for y in YS) for d in range(3)]
    applied = [sum(v[d] for loads in (gravity,construction,lateral) for v in loads.values()) for d in range(3)]
    profiles = []
    max_drift = 0.0
    for k in range(1,storeys+1):
        disps = [ops.nodeDisp(nodes[k,x,y]) for x in XS for y in YS]
        drift = max(math.hypot(ops.nodeDisp(nodes[k,x,y],1)-ops.nodeDisp(nodes[k-1,x,y],1),
                               ops.nodeDisp(nodes[k,x,y],2)-ops.nodeDisp(nodes[k-1,x,y],2))/H for x in XS for y in YS)
        max_drift = max(max_drift,drift)
        profiles.append(dict(floor=k,zM=k*H,meanDxM=sum(v[0] for v in disps)/35,
                             meanDyM=sum(v[1] for v in disps)/35,
                             maxHorizontalM=max(math.hypot(v[0],v[1]) for v in disps),
                             minDzM=min(v[2] for v in disps),maxStoreyDriftRatio=drift))
    brace_forces = [float(ops.eleResponse(t,"axialForce")[0]) for t in brace_tags]
    return dict(case=f"{storeys}-storey"+("-missing-east-face-braces" if missing_braces else "-nominal"),
                storeys=storeys,nodeCount=len(nodes),elementCount=len(elements),braceCount=len(brace_tags),
                status="converged" if gravity_code==service_code==0 else "solver-failed",
                gravityReturnCode=gravity_code,combinedReturnCode=service_code,
                activeBeamIncluded=active,robotIncluded=active,deckLoadedAreaM2=deck_area,
                appliedForceN=applied,baseReactionN=reaction,
                forceBalanceRelative=max(abs(reaction[i]+applied[i]) for i in range(3))/abs(applied[2]),
                roofMaxHorizontalM=profiles[-1]["maxHorizontalM"],
                maxStoreyDriftRatio=max_drift,
                braceAxialForceRangeN=[min(brace_forces),max(brace_forces)],
                floorProfiles=profiles)


def local_beam(physics,missing_seat=False):
    ops.wipe()
    ops.model("basic","-ndm",3,"-ndf",6)
    ops.geomTransf("Linear",1,0,0,1)
    s = SECTIONS["activeBeam"]
    length,segments = ACTIVE_SPAN,10
    for j in range(segments+1):
        ops.node(j+1,6.2+length*j/segments,-12,43.425)
    ops.fix(1,1,1,1,1,0,0)
    ops.fix(segments+1,0,1,0 if missing_seat else 1,0,0,0)
    for j in range(segments):
        beam(j+1,j+1,j+2,s,1)
    weight = physics["beamMassKg"]*G0
    ops.timeSeries("Linear",1)
    ops.pattern("Plain",1,1)
    for j in range(segments):
        ops.eleLoad("-ele",j+1,"-type","-beamUniform",0,-weight/length,0)
    solver()
    code = ops.analyze(10)
    # A missing vertical seat admits a rigid-body rotation about the left pin.
    # Exact virtual-work check avoids relying on platform-specific singular-solver detection.
    work_per_radian = weight*length/2 if missing_seat else 0
    if missing_seat:
        return dict(case="active-beam-missing-right-seat",status="unstable-mechanism",
                    solverReturnCode=code,kinematicNullMode="rotation about left-seat global Y axis",
                    unbalancedGravityMomentNm=work_per_radian,
                    displacementResultsSuppressed=True)
    ops.reactions()
    numerical = -ops.nodeDisp(segments//2+1,3)
    analytical = 5*(weight/length)*length**4/(384*E*s["Iy"])
    return dict(case="active-beam-two-seats",status="converged" if code==0 else "solver-failed",
                solverReturnCode=code,spanM=length,massKg=physics["beamMassKg"],
                seatReactionsN=[ops.nodeReaction(1,3),ops.nodeReaction(segments+1,3)],
                midspanDeflectionM=numerical,closedFormDeflectionM=analytical,
                closedFormRelativeError=abs(numerical-analytical)/analytical)


def run():
    physics = json.loads(PHYSICS.read_text())
    mass_validation = validate_active_mass(physics)
    results = [stage(n,physics) for n in (11,12,20)]
    negative = stage(12,physics,True)
    nominal = results[1]
    negative["roofDisplacementRatioToNominal"] = negative["roofMaxHorizontalM"]/nominal["roofMaxHorizontalM"]
    negative["topStoreyDriftRatioToNominal"] = negative["floorProfiles"][-1]["maxStoreyDriftRatio"]/nominal["floorProfiles"][-1]["maxStoreyDriftRatio"]
    return dict(schemaVersion=1,engine="OpenSeesPy",engineVersion=ops.version(),units="m, N, kg, Pa",
                qualification="Concept-stage elastic equilibrium and support-sensitivity study; no safety certification.",
                coordinateSystem="Z-up; viewer mapping (x,y,z) -> (x,z,-y)",
                geometry=dict(footprintM=[36,24],gridM=6,storeyHeightM=3.6,activeFloor=12),
                material=dict(E=E,G=G,poisson=NU,densityKgM3=RHO),sections=SECTIONS,
                activeBeamMassValidation=mass_validation,
                brace=dict(areaM2=BRACE_AREA,radiusM=.052,model="Elastic solid circular truss; compression buckling omitted"),
                loads=dict(deckDeadPa=2250,constructionLivePa=750,lateralProbePa=500,
                           activeBeamMassKg=physics["beamMassKg"],robotMassKg=physics["robotMassKg"],
                           importedSeatLoadsN=physics["finalSeatLoadsN"]),
                source=dict(path=str(PHYSICS.relative_to(DEMO)),sha256=hashlib.sha256(PHYSICS.read_bytes()).hexdigest()),
                stageMethod="Independent partial-height equilibrium models; gravity held before workcell and lateral load ramp. No stress-free activation or construction-history carryover.",
                assumptions=["All beam-column joints rigid; fixed foundations; no slab diaphragm constraint.",
                             "Temporary Y-plane braces are assumed additions; X braces follow visual bay locations.",
                             "Concrete core contributes no stiffness, mass or gravity; this is a steel-frame-only subsystem.",
                             "Deck and member gravity lumped to joints; frame member local gravity bending is not captured.",
                             "Active floor-12 beam is a pin-seated gravity load only, with no frame stiffness credit.",
                             "Robot weight and 0.6 m eccentricity condensed to the adjacent column; dynamic grip forces omitted.",
                             "P-Delta geometry, elastic material. No yielding, brace buckling, joint slip, wind dynamics or seismic loads.",
                             "Floor-12 openings persist; stage 20 assumes future decks above current visual deck level.",
                             "No member, connection, stability, foundation or serviceability acceptance criteria are certified."],
                stages=results,negativeBraceCase=negative,
                activeBeam=local_beam(physics),negativeSeatCase=local_beam(physics,True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=HERE/"results.json")
    parser.add_argument("--public",action="store_true")
    args = parser.parse_args()
    payload = run()
    data = json.dumps(payload,indent=2,allow_nan=False)+"\n"
    args.output.write_text(data)
    if args.public:
        (DEMO/"public/assets/tower-structure.json").write_text(data)
    print(json.dumps({"output":str(args.output),"stages":[{k:s[k] for k in ("case","status","roofMaxHorizontalM","maxStoreyDriftRatio","forceBalanceRelative")} for s in payload["stages"]],
                      "braceSensitivity":payload["negativeBraceCase"]["topStoreyDriftRatioToNominal"],
                      "seatNegative":payload["negativeSeatCase"]},indent=2))
