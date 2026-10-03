"""Repeated four-limb rail gait: bounded motor dynamics and guarded fixed-site clamps."""
from pathlib import Path
import argparse
import json
import math
import mujoco
import numpy as np

HERE = Path(__file__).resolve().parent
NAMES = ('fl', 'fr', 'rl', 'rr')
HIP = {'fl': (0, -.25, .32), 'fr': (0, .25, .32), 'rl': (0, -.25, -.32), 'rr': (0, .25, -.32)}
LENGTH = .45
RAIL_X = .55
PITCH = .30
START_Z = 1.2
STEPS = 12
LIMIT = 450.
DT = .002
CAPTURE = .004
CAPTURE_SPEED = .025
PD_KP = 12000.
PD_KD = 220.
SWING_DURATION = 2.5
CAPTURE_TIMEOUT = 4.5
LOAD_DURATION = .6
RAISE_DURATION = 3.
RAISE_SETTLE = 1.
C = np.array([[1., 0, 0], [0, 0, 1], [0, -1, 0]])
BODIES = ['robot_chassis']+[f'limb_{n}_{part}' for n in NAMES for part in ('upper', 'lower', 'grip')]


def ik(x, z):
    c = (x*x + z*z - 2*LENGTH**2)/(2*LENGTH**2)
    if abs(c) > 1: raise ValueError(f'unreachable endpoint {x}, {z}')
    elbow = math.acos(c)
    return np.array([-math.atan2(z, x)-elbow/2, elbow])


def build_model(scenario='nominal'):
    q0 = ik(RAIL_X, 0)
    limbs, sites, locks, motors = [], [], [], []
    for name in NAMES:
        _, y, z = HIP[name]
        for k in range(STEPS+1):
            # An offset receiver is physically outside this planar limb's reachable plane.
            offset_y = .08 if scenario == 'missed-grip' and name == 'fl' and k == 1 else 0
            sites.append(f'<site name="rail_{name}_{k}" pos="{RAIL_X} {y+offset_y} {START_Z+z+PITCH*k}" size=".012" rgba="1 .6 .1 1"/>')
            locks.append(f'<connect name="lock_{name}_{k}" site1="grip_{name}" site2="rail_{name}_{k}" active="{str(k==0).lower()}" solref=".008 1" solimp=".99 .99 .001"/>')
        limbs.append(f'''<body name="limb_{name}_upper" pos="0 {y} {z}" euler="0 {q0[0]} 0">
          <joint name="{name}_shoulder" axis="0 1 0" range="-1.7 .3" ref="{q0[0]}" damping="5" armature=".08"/>
          <geom type="capsule" fromto="0 0 0 {LENGTH} 0 0" size=".035" mass="8"/>
          <body name="limb_{name}_lower" pos="{LENGTH} 0 0" euler="0 {q0[1]} 0">
            <joint name="{name}_elbow" axis="0 1 0" range=".4 2.5" ref="{q0[1]}" damping="5" armature=".05"/>
            <geom type="capsule" fromto="0 0 0 {LENGTH} 0 0" size=".03" mass="6"/>
            <body name="limb_{name}_grip" pos="{LENGTH} 0 0"><geom type="sphere" size=".035" mass="3"/><site name="grip_{name}" size=".01"/></body>
          </body></body>''')
        for j in ('shoulder', 'elbow'):
            motors.append(f'<motor name="{name}_{j}" joint="{name}_{j}" ctrlrange="-{LIMIT} {LIMIT}" forcerange="-{LIMIT} {LIMIT}"/>')
    return f'''<mujoco model="Isolated repeated rail-climb prototype">
      <compiler angle="radian" autolimits="true"/>
      <option timestep="{DT}" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="80" tolerance="1e-9"><flag energy="enable" fwdinv="enable"/></option>
      <default><geom contype="0" conaffinity="0" rgba=".35 .48 .60 1"/><joint limited="true"/></default>
      <worldbody><light pos="-2 -3 7"/>{''.join(sites)}
        <geom name="rail_left" type="box" pos="{RAIL_X} -.25 3" size=".025 .025 3"/>
        <geom name="rail_right" type="box" pos="{RAIL_X} .25 3" size=".025 .025 3"/>
        <body name="robot_chassis" pos="0 0 {START_Z}"><freejoint name="robot_free"/>
          <geom type="box" size=".18 .21 .27" mass="69"/>{''.join(limbs)}
        </body>
      </worldbody><equality>{''.join(locks)}</equality><actuator>{''.join(motors)}</actuator>
    </mujoco>'''


def smooth(u):
    u = np.clip(u, 0, 1)
    return float(u*u*(3-2*u))


def run(scenario='nominal', cycles=STEPS, fps=10):
    if scenario not in ('nominal', 'missed-grip') or not 1 <= cycles <= STEPS:
        raise ValueError('Unknown scenario or cycle count outside 1..12')
    xml = build_model(scenario)
    m = mujoco.MjModel.from_xml_string(xml)
    d = mujoco.MjData(m)
    mujoco.mj_forward(m, d)
    chassis = m.body('robot_chassis').id
    joints = [int(m.actuator_trnid[i, 0]) for i in range(m.nu)]
    qa = np.array([m.jnt_qposadr[j] for j in joints])
    va = np.array([m.jnt_dofadr[j] for j in joints])
    grip_ids = {n: m.site('grip_'+n).id for n in NAMES}
    rail_ids = {(n, k): m.site(f'rail_{n}_{k}').id for n in NAMES for k in range(STEPS+1)}
    eq_ids = {(n, k): m.equality(f'lock_{n}_{k}').id for n in NAMES for k in range(STEPS+1)}
    fixed_sites = m.site_pos.copy()
    fixed_eq = m.eq_data.copy()
    anchored = {n: 0 for n in NAMES}
    events, frames = [], []
    metrics = {'minActiveSupports': 4, 'minLoadedSupports': 4, 'maxTorqueNm': 0., 'maxReactionN': 0., 'maxCaptureErrorM': 0., 'maxCaptureSpeedMps': 0., 'maxSupportErrorM': 0., 'maxJointLimitViolationRad': 0., 'maxChassisTiltRad': 0., 'maxSolverIterations': 0, 'maxConstraintResidual': 0., 'minUpwardSupports': 4, 'minSupportVerticalN': 1e9, 'maxChassisSpeedMps': 0.}
    phase, phase_start, cycle, limb_index = 'settle', 0., 0, 0
    desired_z = START_Z
    swing = None
    released_from = None
    rejected_error = None
    abort = None
    recover = False
    complete = False
    initial_z = float(d.xpos[chassis, 2])
    initial_potential = float(d.energy[0])
    motor_work = 0.
    clamp_work = 0.
    settled_z = None
    start_target = None
    target = None
    max_time = 8 + cycles*(4*(CAPTURE_TIMEOUT+LOAD_DURATION)+RAISE_DURATION+RAISE_SETTLE)
    step = 0

    def speed(sid):
        v = np.zeros(6)
        mujoco.mj_objectVelocity(m, d, mujoco.mjtObj.mjOBJ_SITE, sid, v, 0)
        return float(np.linalg.norm(v[3:]))

    def begin_swing(n, k, returning=False):
        nonlocal phase, phase_start, swing, released_from, start_target, target
        swing = n
        released_from = anchored[n]
        if not returning:
            # Every continuing support must actually carry upward rail reaction.
            for other in NAMES:
                if other == n: continue
                eq = eq_ids[other, anchored[other]]
                rows = np.flatnonzero((d.efc_type[:d.nefc] == 0) & (d.efc_id[:d.nefc] == eq))
                if len(rows) != 3 or d.efc_force[rows[2]] <= 5:
                    raise RuntimeError('Release inhibited: fewer than three positive retained supports')
            d.eq_active[eq_ids[n, released_from]] = False
            anchored[n] = None
            events.append({'time': float(d.time), 'event': 'release', 'limb': n, 'fromRung': released_from, 'toRung': k})
        phase = 'recover' if returning else 'swing'
        phase_start = float(d.time)
        start_target = d.site_xpos[grip_ids[n]].copy()
        target = d.site_xpos[rail_ids[n, k]].copy()

    while d.time < max_time:
        t = float(d.time)
        elapsed = t-phase_start
        if phase == 'settle' and elapsed >= 1.5:
            settled_z = float(d.xpos[chassis, 2])
            begin_swing(NAMES[limb_index], cycle+1)
        if phase in ('swing', 'recover'):
            returning = phase == 'recover'
            k = cycle if returning else cycle+1
            err = float(np.linalg.norm(d.site_xpos[grip_ids[swing]]-target))
            vel = speed(grip_ids[swing])
            if elapsed >= SWING_DURATION and err < CAPTURE and vel < CAPTURE_SPEED:
                assert sum(v is not None for v in anchored.values()) == 3
                d.eq_active[eq_ids[swing, k]] = True
                anchored[swing] = k
                metrics['maxCaptureErrorM'] = max(metrics['maxCaptureErrorM'], err)
                metrics['maxCaptureSpeedMps'] = max(metrics['maxCaptureSpeedMps'], vel)
                events.append({'time': t, 'event': 'recapture', 'limb': swing, 'rung': k, 'errorM': err, 'speedMps': vel, 'recovery': returning})
                phase = 'abort-hold' if returning else 'load'
                phase_start = t
                swing = None
            elif elapsed > CAPTURE_TIMEOUT:
                if returning:
                    abort = 'Recovery capture failed; remaining three supports retained.'
                    break
                rejected_error = err
                abort = 'Missed receiver: position/speed capture gate failed; no next release authorized.'
                events.append({'time': t, 'event': 'capture-rejected', 'limb': swing, 'rung': k, 'errorM': err, 'speedMps': vel})
                recover = True
                begin_swing(swing, cycle, returning=True)
        elif phase == 'load' and elapsed > LOAD_DURATION:
            # Check the new support carries a real nonzero reaction before another release.
            eq = eq_ids[NAMES[limb_index], cycle+1]
            rows = np.flatnonzero((d.efc_type[:d.nefc] == 0) & (d.efc_id[:d.nefc] == eq))
            if len(rows) == 3 and np.linalg.norm(d.efc_force[rows]) > 5:
                limb_index += 1
                if limb_index < 4:
                    begin_swing(NAMES[limb_index], cycle+1)
                else:
                    phase, phase_start = 'raise', t
                    events.append({'time': t, 'event': 'raise-start', 'cycle': cycle+1})
        elif phase == 'raise':
            desired_z = START_Z + PITCH*(cycle+smooth(elapsed/RAISE_DURATION))
            if elapsed >= RAISE_DURATION+RAISE_SETTLE:
                cycle += 1
                events.append({'time': t, 'event': 'raise-complete', 'cycle': cycle, 'chassisZ': float(d.xpos[chassis, 2]), 'advanceM': float(d.xpos[chassis, 2])-initial_z})
                if cycle == cycles:
                    phase, phase_start = 'final-hold', t
                else:
                    limb_index = 0
                    begin_swing(NAMES[limb_index], cycle+1)
        elif phase == 'final-hold' and elapsed >= 1:
            complete = True
            break
        elif phase == 'abort-hold' and elapsed >= 1:
            break

        qtarget = []
        for n in NAMES:
            if n == swing:
                u = smooth((t-phase_start)/SWING_DURATION)
                world = start_target+(target-start_target)*u
                world[0] -= .07*math.sin(math.pi*u)**2
                # Live chassis inverse kinematics controls released tip without overwriting state.
                local = d.xmat[chassis].reshape(3, 3).T @ (world-d.xpos[chassis])-np.array(HIP[n])
                qtarget.extend(ik(local[0], local[2]))
            else:
                foot_z = START_Z+HIP[n][2]+PITCH*anchored[n]
                qtarget.extend(ik(RAIL_X, foot_z-desired_z-HIP[n][2]))
        # Static grasp load distribution balances the six unactuated free-base DOFs.
        # This computes motor feedforward only; no support forces are applied directly.
        jacs = []
        for n in NAMES:
            if anchored[n] is None: continue
            jac = np.zeros((3, m.nv))
            mujoco.mj_jacSite(m, d, jac, None, grip_ids[n])
            jacs.append(jac.T)
        grasp = np.concatenate(jacs, axis=1)
        static_forces = np.linalg.lstsq(grasp[:6], d.qfrc_bias[:6], rcond=1e-8)[0]
        feedforward = d.qfrc_bias[va]-(grasp @ static_forces)[va]
        d.ctrl[:] = np.clip(PD_KP*(np.array(qtarget)-d.qpos[qa])-PD_KD*d.qvel[va]+feedforward, -LIMIT, LIMIT)
        # Only actuator inputs and equality activation are ever modified during integration.
        mujoco.mj_step(m, d)
        mujoco.mj_forward(m, d)
        motor_work += float(d.actuator_force @ d.actuator_velocity)*DT
        clamp_work += float(d.qfrc_constraint @ d.qvel)*DT
        reactions, errors = {}, {}
        for n in NAMES:
            k = anchored[n]
            if k is None:
                reactions[n] = [0., 0., 0.]
                continue
            eq = eq_ids[n, k]
            rows = np.flatnonzero((d.efc_type[:d.nefc] == 0) & (d.efc_id[:d.nefc] == eq))
            # Connect residual is site1-site2: J^T lambda gives force on grip site1.
            reactions[n] = d.efc_force[rows].tolist()
            errors[n] = float(np.linalg.norm(d.site_xpos[grip_ids[n]]-d.site_xpos[rail_ids[n, k]]))
        loads = [float(np.linalg.norm(v)) for v in reactions.values()]
        metrics['minActiveSupports'] = min(metrics['minActiveSupports'], sum(v is not None for v in anchored.values()))
        if t >= 0:
            metrics['minLoadedSupports'] = min(metrics['minLoadedSupports'], sum(v > 5 for v in loads))
            metrics['minUpwardSupports'] = min(metrics['minUpwardSupports'], sum(v[2] > 5 for v in reactions.values()))
            metrics['minSupportVerticalN'] = min(metrics['minSupportVerticalN'], *(v[2] for n,v in reactions.items() if anchored[n] is not None))
        metrics['maxReactionN'] = max(metrics['maxReactionN'], *loads)
        metrics['maxSupportErrorM'] = max(metrics['maxSupportErrorM'], *errors.values())
        metrics['maxTorqueNm'] = max(metrics['maxTorqueNm'], float(np.max(np.abs(d.actuator_force))))
        metrics['maxJointLimitViolationRad'] = max(metrics['maxJointLimitViolationRad'], float(np.max(m.jnt_range[joints, 0]-d.qpos[qa])), float(np.max(d.qpos[qa]-m.jnt_range[joints, 1])))
        metrics['maxChassisTiltRad'] = max(metrics['maxChassisTiltRad'], math.acos(np.clip(d.xmat[chassis].reshape(3,3)[2,2],-1,1)))
        metrics['maxSolverIterations'] = max(metrics['maxSolverIterations'], int(np.max(d.solver_niter)))
        metrics['maxConstraintResidual'] = max(metrics['maxConstraintResidual'], float(np.max(d.solver_fwdinv)))
        metrics['maxChassisSpeedMps'] = max(metrics['maxChassisSpeedMps'], float(np.linalg.norm(d.qvel[:3])))
        if step % round(1/(fps*DT)) == 0:
            body_poses = {}
            for name in BODIES:
                bid = m.body(name).id
                quat = np.zeros(4)
                mujoco.mju_mat2Quat(quat, (C @ d.xmat[bid].reshape(3, 3) @ C.T).ravel())
                body_poses[name] = {'position': (C @ d.xpos[bid]).tolist(), 'quaternion': quat[[1,2,3,0]].tolist()}
            frames.append({'time': float(d.time), 'phase': phase, 'cycle': cycle, 'chassisPosition': d.xpos[chassis].tolist(), 'chassisQuaternionWxyz': d.xquat[chassis].tolist(), 'qpos': d.qpos.tolist(), 'torquesNm': d.actuator_force.tolist(), 'gripPositions': {n:d.site_xpos[grip_ids[n]].tolist() for n in NAMES}, 'activeRungs':dict(anchored), 'railReactionsN':reactions, 'supportErrorM':errors,
                'bodies': body_poses, 'contacts': [],
                'actuators': {m.actuator(i).name: {'force': float(d.actuator_force[i]), 'position': float(d.qpos[qa[i]])} for i in range(m.nu)},
                'metrics': {'activeGripLocks': sum(v is not None for v in anchored.values()), 'upwardSupports': sum(v[2] > 5 for v in reactions.values()), 'climbAdvanceM': float(d.xpos[chassis,2])-(settled_z or initial_z), 'completedClimbCycles': cycle, **{'grip_'+n+'_constraintForceN': loads[i] for i,n in enumerate(NAMES)}, **{'grip_'+n+'_verticalForceN': reactions[n][2] for n in NAMES}},
                'state': {'support': f'{sum(v is not None for v in anchored.values())} ideal rail clamps', 'connection': 'no building connection simulated', 'note': phase+': bounded motor dynamics; each receiver is fixed'}})
        step += 1
        if not (np.isfinite(d.qpos).all() and np.isfinite(d.qvel).all()):
            abort = 'Nonfinite state'
            break
    if not complete and abort is None: abort = 'Simulation time budget exceeded'
    metrics.update({'scenario':scenario,'mujocoVersion':mujoco.__version__,'complete':complete,'cyclesCompleted':cycle,'durationSeconds':float(d.time),'chassisAdvanceM':float(d.xpos[chassis,2])-initial_z,'settledAdvanceM':float(d.xpos[chassis,2])-(settled_z or initial_z),'finalChassisPosition':d.xpos[chassis].tolist(),'finalRungs':anchored,'finalReactionN':reactions,'massKg':float(m.body_mass.sum()),'weightN':float(m.body_mass.sum()*9.81),'captureCount':sum(e['event']=='recapture' and not e['recovery'] for e in events),'releaseCount':sum(e['event']=='release' for e in events),'rejectedCaptureErrorM':rejected_error,'recovered':recover and all(v is not None for v in anchored.values()),'abortReason':abort,'finiteState':bool(np.isfinite(d.qpos).all() and np.isfinite(d.qvel).all()),'fixedAnchorsUnchanged':bool(np.array_equal(fixed_sites,m.site_pos) and np.array_equal(fixed_eq,m.eq_data)), 'motorMechanicalWorkJ':motor_work, 'railConstraintWorkJ':clamp_work, 'potentialEnergyRiseJ':float(d.energy[0])-initial_potential,'warnings':{str(mujoco.mjtWarning(i)):int(d.warning[i].number) for i in range(int(mujoco.mjtWarning.mjNWARNING))},'events':events})
    return xml, metrics, frames


def viewer_trace(metrics, frames):
    phases = []
    for f in frames:
        if not phases or phases[-1]['label'] != f['phase']:
            if phases: phases[-1]['end'] = f['time']
            phases.append({'id': 'climb-'+str(len(phases)), 'label': f['phase'], 'start': f['time'], 'end': f['time'], 'description': 'Actual MuJoCo state; cycle '+str(f['cycle']+1)})
    phases[-1]['end'] = metrics['durationSeconds']
    return {'schemaVersion': 1, 'coordinates': 'gltf-y-up', 'units': {'length':'m','time':'s','force':'N'},
        'provenance': {'engine': 'MuJoCo', 'engineVersion': mujoco.__version__, 'model': 'production/physics/climb-prototype/'+metrics['scenario']+'.xml',
            'description': 'Four-limb rail ascent from bounded motor torques, with sequential guarded release, advance, recapture and chassis rise. '+metrics['scenario'],
            'coordinateConversion': 'p=(x,z,-y); Rg=C Rm C^T; quaternions xyzw. Local prototype origin: translate all positions together to place on tower.',
            'limitations': ['Concept robot; 0.45 m links and 137 kg assumed mass.', 'Ideal point clamps: force reactions, no clamp moments, teeth, latch or strength model.', 'Rigid world rails; no tower compliance feedback.', 'Limb/rail and limb/limb collisions disabled; clearance and snagging require separate validation.', 'No construction payload, beam, crane, battery, sensing or certified control modeled.']},
        'bindings': [{'body': n, 'assetId': 'robot', 'node': n} for n in BODIES], 'phases': phases, 'events': metrics['events'], 'frames': frames}


def geometry_contract():
    q0 = ik(RAIL_X, 0)
    return {'coordinates': 'MuJoCo Z-up', 'viewerConversion': 'p=(x,z,-y); orientations Rg=C Rm C^T',
        'linkLengthM': LENGTH, 'linkAxis': 'local +X', 'railX': RAIL_X, 'railY': [-.25,.25], 'railSpacingM': .5,
        'receiverPitchM': PITCH, 'storeyHeightM': STEPS*PITCH, 'startChassisPosition': [0,0,START_Z],
        'hipOffsets': HIP, 'initialShoulderAngleRad': float(q0[0]), 'initialElbowAngleRad': float(q0[1]),
        'jointRangesRad': {'shoulder': [-1.7,.3], 'elbow': [.4,2.5]}, 'torqueLimitNm': LIMIT,
        'upperMassKg': 8, 'lowerMassKg': 6, 'gripMassKg': 3, 'chassisMassKg': 69,
        'capturePositionToleranceM': CAPTURE, 'captureSpeedToleranceMps': CAPTURE_SPEED,
        'railReceivers': [{'name':f'rail_{n}_{k}', 'position':[RAIL_X,HIP[n][1],START_Z+HIP[n][2]+PITCH*k]} for n in NAMES for k in range(STEPS+1)],
        'clamp': {'type':'ideal point connect', 'solref':[.008,1], 'solimp':[.99,.99,.001]},
        'bodyNames': BODIES, 'visualGeometry': {'chassisHalfExtentsM':[.18,.21,.27], 'upperRadiusM':.035, 'lowerRadiusM':.03, 'gripRadiusM':.035}}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--scenario', choices=['nominal','missed-grip'], default='nominal')
    p.add_argument('--cycles',type=int,default=STEPS)
    args = p.parse_args()
    xml, metrics, frames = run(args.scenario,args.cycles)
    (HERE/f'{args.scenario}.xml').write_text(xml)
    (HERE/f'{args.scenario}-metrics.json').write_text(json.dumps(metrics,indent=2,allow_nan=False)+'\n')
    (HERE/f'{args.scenario}-trace.json').write_text(json.dumps(viewer_trace(metrics,frames),separators=(',',':'),allow_nan=False)+'\n')
    (HERE/'geometry-contract.json').write_text(json.dumps(geometry_contract(),indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in metrics.items() if k!='events'},indent=2))

if __name__ == '__main__': main()
