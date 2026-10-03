"""Loaded carrier locomotion using the construction kit's shared robot dimensions.

Reuses the measured-support gait controller; this is a local action of the new
site demonstration, not a claim that its complete task history is physical.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
DEMO = HERE.parents[2]
BASE = HERE.parent / 'climb-prototype' / 'prototype.py'
CONTRACT = DEMO / 'production/contracts/carrier-construction.json'
spec = importlib.util.spec_from_file_location('guarded_rail_controller', BASE)
gait = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gait)

GEOMETRY = {
    'coordinates': 'MuJoCo Z-up; browser p=(x,z,-y)',
    'linkLengthM': .65,
    'hipOffsets': {'fl': [0, -.32, .48], 'fr': [0, .32, .48],
                   'rl': [0, -.32, -.48], 'rr': [0, .32, -.48]},
    'railReachM': .75,
    'railSpacingM': .64,
    'receiverPitchM': .32,
    'storeyHeightM': 3.2,
    'chassisMassKg': 160,
    'upperMassKg': 12,
    'lowerMassKg': 10,
    'gripMassKg': 8,
    'cradleMassKg': 40,
    'dryMassKg': 320,
    'cradleCentreM': [-.61, 0, 0],
    'shoulderTorqueLimitNm': 3000,
    'elbowTorqueLimitNm': 2000,
    'status': 'Specified conceptual hardware, not hardware-qualified capacities',
}


def verify_contract():
    contract = json.loads(CONTRACT.read_text())
    robot = contract['robot']
    expected = {
        'linkLengthM': GEOMETRY['linkLengthM'],
        'dryMassKg': GEOMETRY['dryMassKg'],
        'cradleCOMSourceM': GEOMETRY['cradleCentreM'],
    }
    for field,value in expected.items():
        if robot[field] != value:
            raise ValueError(f'Physics/Blender contract mismatch: {field}')
    for limb,offset in GEOMETRY['hipOffsets'].items():
        if robot['joints'][limb]['hipSourceM'] != offset:
            raise ValueError(f'Physics/Blender hip mismatch: {limb}')
    if robot['representativeClimb']['chassisStartSourceM'] != [0,0,1.28]:
        raise ValueError('Physics/Blender climb origin mismatch')
    if robot['rail']['receiverPitchM'] != GEOMETRY['receiverPitchM']:
        raise ValueError('Physics/Blender rail pitch mismatch')
    return contract


def configure():
    gait.LENGTH = GEOMETRY['linkLengthM']
    gait.HIP = {k: tuple(v) for k, v in GEOMETRY['hipOffsets'].items()}
    gait.RAIL_X = GEOMETRY['railReachM']
    gait.PITCH = GEOMETRY['receiverPitchM']
    gait.START_Z = 1.28
    gait.STEPS = 10
    gait.LIMIT = GEOMETRY['shoulderTorqueLimitNm']
    gait.PD_KP = 22000.
    gait.PD_KD = 1800.
    gait.SWING_DURATION = 4.
    gait.CAPTURE_TIMEOUT = 7.
    gait.LOAD_DURATION = 1.
    gait.RAISE_DURATION = 5.
    gait.RAISE_SETTLE = 2.
    gait.BODIES = ['robot_chassis', 'payload_cradle', 'carried_beam'] + [
        f'limb_{n}_{part}' for n in gait.NAMES for part in ('upper', 'lower', 'grip')]


def model(scenario, payload_mass):
    """Rigid captive payload; finite member geometry, ideal point rail clamps."""
    q0 = gait.ik(gait.RAIL_X, 0)
    xml = ET.Element('mujoco', model='Construction carrier with restrained beam')
    ET.SubElement(xml, 'compiler', angle='radian', autolimits='true')
    option = ET.SubElement(xml, 'option', timestep=str(gait.DT), gravity='0 0 -9.81',
        integrator='implicitfast', solver='Newton', iterations='100', tolerance='1e-9')
    ET.SubElement(option, 'flag', energy='enable', fwdinv='enable')
    default = ET.SubElement(xml, 'default')
    ET.SubElement(default, 'geom', contype='0', conaffinity='0', rgba='.45 .49 .48 1')
    ET.SubElement(default, 'joint', limited='true')
    world = ET.SubElement(xml, 'worldbody')
    ET.SubElement(world, 'light', pos='-3 -4 8')
    equal = ET.SubElement(xml, 'equality')
    actuators = ET.SubElement(xml, 'actuator')
    robot = ET.SubElement(world, 'body', name='robot_chassis', pos=f'0 0 {gait.START_Z}')
    ET.SubElement(robot, 'freejoint', name='robot_free')
    ET.SubElement(robot, 'geom', name='chassis_collision', type='box', size='.33 .35 .50', mass='160')
    cradle = ET.SubElement(robot, 'body', name='payload_cradle', pos='-.61 0 0')
    ET.SubElement(cradle, 'geom', type='box', size='.11 .55 .08', mass='40', rgba='.18 .20 .21 1')
    beam = ET.SubElement(cradle, 'body', name='carried_beam', pos='0 0 0')
    # The catalogue's combined shell and connection mass supplies the inertia.
    # Exact component-mesh collision and clamp contacts remain a separate scope.
    ET.SubElement(beam, 'geom', name='payload_member', type='box', size='.05 1.5 .09',
        mass=str(payload_mass), rgba='.80 .79 .73 1')
    for name in gait.NAMES:
        _, y, z = gait.HIP[name]
        for k in range(gait.STEPS+1):
            offset = .08 if scenario == 'missed-grip' and name == 'fl' and k == 1 else 0
            ET.SubElement(world, 'site', name=f'rail_{name}_{k}',
                pos=f'{gait.RAIL_X} {y+offset} {gait.START_Z+z+gait.PITCH*k}', size='.012')
            ET.SubElement(equal, 'connect', name=f'lock_{name}_{k}', site1=f'grip_{name}',
                site2=f'rail_{name}_{k}', active=str(k == 0).lower(), solref='.008 1', solimp='.99 .99 .001')
        upper = ET.SubElement(robot, 'body', name=f'limb_{name}_upper', pos=f'0 {y} {z}', euler=f'0 {q0[0]} 0')
        ET.SubElement(upper, 'joint', name=f'{name}_shoulder', axis='0 1 0', range='-1.7 .3', ref=str(q0[0]), damping='10', armature='.2')
        ET.SubElement(upper, 'geom', type='capsule', fromto='0 0 0 .65 0 0', size='.05', mass='12')
        lower = ET.SubElement(upper, 'body', name=f'limb_{name}_lower', pos='.65 0 0', euler=f'0 {q0[1]} 0')
        ET.SubElement(lower, 'joint', name=f'{name}_elbow', axis='0 1 0', range='.4 2.5', ref=str(q0[1]), damping='8', armature='.15')
        ET.SubElement(lower, 'geom', type='capsule', fromto='0 0 0 .65 0 0', size='.045', mass='10')
        grip = ET.SubElement(lower, 'body', name=f'limb_{name}_grip', pos='.65 0 0')
        ET.SubElement(grip, 'geom', type='box', size='.08 .17 .08', mass='8')
        ET.SubElement(grip, 'site', name=f'grip_{name}', size='.01')
        for joint, limit in [('shoulder',3000),('elbow',2000)]:
            ET.SubElement(actuators, 'motor', name=f'{name}_{joint}', joint=f'{name}_{joint}',
                ctrlrange=f'-{limit} {limit}', forcerange=f'-{limit} {limit}')
    for y in [-.32,.32]:
        ET.SubElement(world, 'geom', type='box', pos=f'.75 {y} 3.2', size='.025 .025 3.2')
    return ET.tostring(xml, encoding='unicode')


def simulate(payload_mass=92.928, cycles=10, scenario='nominal', fps=20):
    contract = verify_contract()
    configure()
    gait.build_model = lambda selected: model(selected, payload_mass)
    xml, metrics, frames = gait.run(scenario, cycles, fps)
    metrics.update({
        'geometry': GEOMETRY,
        'contractRevision': contract['revision'],
        'contractSha256': hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        'payloadMassKg': payload_mass,
        'dryMassKg': GEOMETRY['dryMassKg'],
        'scope': 'Loaded vertical rail locomotion; captive rigid payload and ideal point grips',
        'controllerSourceSha256': hashlib.sha256(BASE.read_bytes()).hexdigest(),
        'modelSha256': hashlib.sha256(xml.encode()).hexdigest(),
        'evidenceClass': 'local-dynamics-with-idealized-restraints',
        'gripDemandWithinSpecifiedLimit': metrics['maxReactionN'] <= 16000.,
        'controllerGains': {'kp':gait.PD_KP,'kd':gait.PD_KD},
        'actionSeconds': {'swing':gait.SWING_DURATION,'load':gait.LOAD_DURATION,'raise':gait.RAISE_DURATION,'settle':gait.RAISE_SETTLE},
    })
    frames_out=[]
    for f in frames:
        frames_out.append({
            'time':f['time'],'phase':f['phase'],'cycle':f['cycle'],
            'position':f['bodies']['robot_chassis']['position'],
            'quaternion':f['bodies']['robot_chassis']['quaternion'],
            'joints':{n:{'shoulder':f['actuators'][n+'_shoulder']['position'],
                         'elbow':f['actuators'][n+'_elbow']['position']} for n in gait.NAMES},
            'torquesNm':f['torquesNm'],
            'bodies':f['bodies'],'activeRungs':f['activeRungs'],
            'railReactionsN':{n:[v[0],v[2],-v[1]] for n,v in f['railReactionsN'].items()},
        })
    trace={
        'schemaVersion':1, 'coordinates':'gltf-y-up', 'duration':metrics['durationSeconds'],
        'geometry':GEOMETRY, 'payloadMassKg':payload_mass,
        'initialPosition':[0,gait.START_Z,0],
        'modelSha256':metrics['modelSha256'],
        'contractRevision':metrics['contractRevision'],
        'contractSha256':metrics['contractSha256'],
        'scope':metrics['scope'], 'complete':metrics['complete'],
        'bindings':{'robot_chassis':'carrier', 'payload_cradle':'payload_mount',
            **{f'limb_{n}_{body}':f'limb_{n}_{node}' for n in gait.NAMES
               for body,node in [('upper','hip'),('lower','knee'),('grip','wrist')]}},
        'limitations':[
            'Only this declared local rail, pose, payload and gravity are simulated. Two installed column segments are needed for all support sites.',
            'Ideal point constraints represent engaged grips; jaw engagement and holding strength are not qualified.',
            'Rigidly attached payload represents an already locked cradle; pickup and release are not simulated.',
            'Robot/member contact geometry is inertial only; collision clearance is not validated.',
            'No frame compliance, wind, battery, sensors or whole-building route verification.',
        ],
        'frames':frames_out,
    }
    return xml,metrics,trace


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--payload-kg',type=float,default=92.928)
    parser.add_argument('--cycles',type=int,default=10)
    parser.add_argument('--scenario',choices=['nominal','missed-grip'],default='nominal')
    parser.add_argument('--public',action='store_true')
    args=parser.parse_args()
    if args.payload_kg <= 0 or args.payload_kg > 350:
        parser.error('payload must be positive and within the unqualified 350 kg design envelope')
    xml,metrics,trace=simulate(args.payload_kg,args.cycles,args.scenario)
    stem=f'{args.scenario}-{args.payload_kg:g}kg'
    (HERE/f'{stem}.xml').write_text(xml)
    (HERE/f'{stem}-metrics.json').write_text(json.dumps(metrics,indent=2,allow_nan=False)+'\n')
    (HERE/f'{stem}-trace.json').write_text(json.dumps(trace,separators=(',',':'),allow_nan=False)+'\n')
    if args.public:
        if not metrics['complete'] or not metrics['gripDemandWithinSpecifiedLimit'] or args.scenario != 'nominal':
            raise RuntimeError('Cannot publish a failed or aborted action as the nominal loaded trace')
        (DEMO/'public/assets/carrier-loaded-trace.json').write_text(json.dumps(trace,separators=(',',':'),allow_nan=False)+'\n')
        (DEMO/'public/assets/carrier-loaded-metrics.json').write_text(json.dumps(metrics,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in metrics.items() if k not in ('events','geometry')},indent=2))

if __name__=='__main__':main()
