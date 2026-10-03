"""Force-controlled deterministic workcell; emits actual MuJoCo states, not keyframes."""
from pathlib import Path
import argparse, json, math
import mujoco
import numpy as np

HERE=Path(__file__).resolve().parent
DEMO=HERE.parents[2]
NAMES=['fl','fr','rl','rr']
BODIES=['robot_chassis']+[f'limb_{n}_{part}' for n in NAMES for part in ['upper','lower','grip']]+['robot_tool','lifted_beam','hoist_carrier']
C=np.array([[1.,0,0],[0,0,1],[0,-1,0]])

def smooth(a,b,t):
    u=float(np.clip(t,0,1)); return a+(b-a)*(3*u*u-2*u*u*u)

def pose(d,body):
    q=np.zeros(4); R=C@d.xmat[body].reshape(3,3)@C.T
    mujoco.mju_mat2Quat(q,R.ravel())
    return {'position':np.round(C@d.xpos[body],7).tolist(),'quaternion':np.round(q[[1,2,3,0]],8).tolist()}

def run(scenario='nominal',duration=24.,fps=25):
    m=mujoco.MjModel.from_xml_path(str(HERE/'workcell.xml')); d=mujoco.MjData(m)
    bodies={n:m.body(n).id for n in BODIES}
    initial_grip={}; mujoco.mj_forward(m,d)
    for n in NAMES: initial_grip[n]=d.xpos[m.body(f'limb_{n}_grip').id].copy()
    beam_id=bodies['lifted_beam']; mass=float(m.body_mass[beam_id]); weight=mass*9.81
    if scenario=='missed-seat':
        adr=m.jnt_qposadr[m.joint('beam_free').id]; d.qpos[adr+1]+=.8; d.mocap_pos[0,1]+=.8
        mujoco.mj_forward(m,d)
    actuator_joints=[int(m.actuator_trnid[i,0]) for i in range(m.nu)]
    frames=[]; events=[]; released=False; regripped=False; grip_released=False
    stable_since=None; max_pen=0.; max_speed=0.; max_solver=0; max_torque=0.
    seat_forces={'seat_left':0.,'seat_right':0.}; sling_forces=[0.,0.]; abort_reason=None
    def contact_data():
        nonlocal max_pen
        rows=[]; loads={'seat_left':0.,'seat_right':0.}
        for c in d.contact:
            wrench=np.zeros(6); mujoco.mj_contactForce(m,d,int(len(rows)),wrench)
            # Contact array index and output row index are kept identical.
            a=m.body(int(m.geom_bodyid[c.geom1])).name or 'world'
            b=m.body(int(m.geom_bodyid[c.geom2])).name or 'world'
            f=max(0.,float(wrench[0])); rows.append({'bodyA':a,'bodyB':b,'normalForce':round(f,3)})
            if a=='lifted_beam' and b in loads: loads[b]+=f
            if b=='lifted_beam' and a in loads: loads[a]+=f
            max_pen=max(max_pen,max(0.,-float(c.dist)))
        return rows,loads
    steps=int(duration/m.opt.timestep)
    for step in range(steps+1):
        t=float(d.time)
        # The robot is moved only by bounded motor torques against its rail locks.
        shoulder=smooth(0,.70,(t-1)/4)
        for i,j in enumerate(actuator_joints):
            name=m.joint(j).name; target=0.
            if 'shoulder' in name: target=shoulder
            elif 'elbow' in name: target=-shoulder
            elif name=='tool_extension': target=smooth(0,.24,(t-18)/2) if released else 0.
            if name.startswith('fl_') and 5.5<t<9.5:
                excursion=.13*math.sin(math.pi*(t-5.5)/4)**2
                target += excursion if 'shoulder' in name else -excursion
            qa=m.jnt_qposadr[j]; va=m.jnt_dofadr[j]
            kp,kd=(800.,70.) if 'extension' in name else (1800.,100.)
            d.ctrl[i]=np.clip(kp*(target-d.qpos[qa])-kd*d.qvel[va]+d.qfrc_bias[va],m.actuator_ctrlrange[i,0],m.actuator_ctrlrange[i,1])
        if t>=5.5 and not grip_released:
            d.eq_active[m.equality('lock_fl').id]=False; grip_released=True
            events.append({'time':round(t,3),'event':'front-left rail grip released; three locks retain chassis'})
        error=float(np.linalg.norm(d.xpos[m.body('limb_fl_grip').id]-initial_grip['fl']))
        if t>=9.5 and not regripped and error<.018:
            d.eq_active[m.equality('lock_fl').id]=True; regripped=True
            events.append({'time':round(t,3),'event':'front-left lock reacquired within 18 mm capture envelope','errorM':error})
        # Externally prescribed crane carrier. Tension is from compliant tendon dynamics.
        d.mocap_pos[0,2]=smooth(46.45,45.05,(t-10)/6)
        # Unilateral Kelvin-Voigt sling forces. A rope never pushes the beam.
        d.qfrc_applied[:]=0.; sling_forces=[]
        for side in ['left','right']:
            sid=m.site('beam_sling_'+side).id
            anchor=d.mocap_pos[0]+m.site_pos[m.site('hoist_'+side).id]
            delta=anchor-d.site_xpos[sid]; length=float(np.linalg.norm(delta)); direction=delta/length
            vel=np.zeros(6); mujoco.mj_objectVelocity(m,d,mujoco.mjtObj.mjOBJ_SITE,sid,vel,0)
            u=float(np.clip((t-10)/6,0,1)); carrier_v=np.array([0.,0.,(45.05-46.45)*6*u*(1-u)/6])
            extension_rate=float((carrier_v-vel[3:])@direction)
            tension=max(0.,30000*(length-1.4)+1200*extension_rate) if length>=1.4 and not released else 0.
            sling_forces.append(tension)
            mujoco.mj_applyFT(m,d,tension*direction,np.zeros(3),d.site_xpos[sid],beam_id,d.qfrc_applied)
        contacts,seat_forces=contact_data()
        speed=float(np.linalg.norm(d.qvel[m.jnt_dofadr[m.joint('beam_free').id]:][:3]))
        seated=min(seat_forces.values())>.35*weight and speed<.03
        if seated and stable_since is None: stable_since=t
        if not seated: stable_since=None
        if stable_since is not None and t-stable_since>.4 and not released:
            released=True; m.tendon_stiffness[:]=0.; m.tendon_damping[:]=0.
            events.append({'time':round(t,3),'event':'two physical seat contacts stable; hoist slings released','seatNormalN':sum(seat_forces.values())})
        if t>17 and not released: abort_reason='Seat load and velocity gate not satisfied: hoist support retained.'
        lock_loads={}
        for name in NAMES:
            eq=m.equality('lock_'+name).id
            indices=np.flatnonzero((d.efc_type[:d.nefc]==0)&(d.efc_id[:d.nefc]==eq))
            lock_loads['grip_'+name+'_constraintForceN']=float(np.linalg.norm(d.efc_force[indices[:3]])) if len(indices) else 0.
        max_speed=max(max_speed,speed); max_solver=max(max_solver,int(np.max(d.solver_niter))); max_torque=max(max_torque,float(np.max(np.abs(d.actuator_force[:8]))))
        if step % max(1,round(1/fps/m.opt.timestep))==0:
            locks=int(np.count_nonzero(d.eq_active)); support='two seats' if released else 'hoist slings'
            frames.append({'time':round(t,4),'bodies':{n:pose(d,idx) for n,idx in bodies.items()},'contacts':contacts,
                'actuators':{m.actuator(i).name:{'force':round(float(d.actuator_force[i]),4),'position':round(float(d.qpos[m.jnt_qposadr[j]]),6)} for i,j in enumerate(actuator_joints)},
                'metrics':{'beamMassKg':mass,'beamSpeedMps':speed,'beamSeatLoadN':sum(seat_forces.values()),'seatLeftLoadN':seat_forces['seat_left'],'seatRightLoadN':seat_forces['seat_right'],'hoistTensionN':sum(sling_forces),'activeGripLocks':locks,'frontLeftCaptureErrorM':error,'solverIterations':int(np.max(d.solver_niter)),'solverForwardInverseResidual':float(np.max(d.solver_fwdinv)),'contactCount':int(d.ncon),**lock_loads},
                'state':{'support':support,'connection':'seated, unfastened' if released else 'unconnected','note':abort_reason or ('Tool approaches; bolt mechanics are not simulated.' if t>18 else 'MuJoCo motor / contact dynamics')}})
        if step<steps: mujoco.mj_step(m,d)
    limits=['Concept robot dimensions, masses, friction and controller gains are design assumptions, not a validated machine.',
        'Rail clamps are switched ideal weld constraints with measured capture gating; clamp tooth engagement, pad compliance and structural rail strength are not resolved.',
        'Body raising and one grip release/reacquisition are simulated; repeated storey-to-storey locomotion is not implemented.',
        'The crane carrier follows a prescribed trajectory; unilateral spring-damper sling tensions (30 kN/m, 1.2 kNs/m, 1.4m unstretched length) and the beam rigid-body motion are simulated. Crane drive dynamics are not modeled.',
        'Physical seat contact and guarded sling release are simulated. Bolt insertion, thread engagement, bolt preload and connection certification are NOT simulated.',
        'The tool uses a bounded prismatic motor; it approaches the connection without tool/bolt contact. This is a partial beam-placement cycle, not completed fastening.',
        'The workcell uses rigid seats and an I-section compound collision shape; tower flexibility is analyzed separately and is not coupled back into MuJoCo.']
    trace={'schemaVersion':1,'coordinates':'gltf-y-up','units':{'length':'m','time':'s','force':'N'},
        'provenance':{'engine':'MuJoCo','engineVersion':mujoco.__version__,'model':'production/physics/mujoco/workcell.xml','description':'Actual bounded-actuator dynamics: four-limb rail-constrained body raise, individual grip cycle, compliant sling lowering, physical I-beam seating and condition-gated hoist release. Scenario: '+scenario+'.','limitations':limits,'coordinateConversion':'MuJoCo/Blender Z-up to glTF Y-up: p=(x,z,-y); Rg=C Rm C^T. MuJoCo wxyz quaternions exported xyzw.'},
        'bindings':[{'body':n,'assetId':'robot','node':n} for n in BODIES if n not in ['lifted_beam','hoist_carrier']]+[{'body':'lifted_beam','assetId':'site','node':'lifted_beam'},{'body':'hoist_carrier','assetId':'site','node':'ActiveHoist'}],
        'phases':[{'id':a,'label':b,'start':c,'end':e,'description':f} for a,b,c,e,f in [
            ('settle','Rail lock preload',0,1,'Four ideal locks support the articulated chassis under gravity.'),('raise','Actuated body raise',1,5.5,'Bounded shoulder and elbow torques raise the chassis against fixed rail grips.'),('regrip','Three-support grip cycle',5.5,10,'Front-left grip releases, articulates under motor torque and reacquires its original capture site; this is not a full walking gait.'),('lower','Receive suspended beam',10,16,'Prescribed crane carrier lowers a free rigid beam through tension-only spring-damper slings.'),('seat','Seat and verify support',16,18,'Two real collision seat reactions must carry the beam before sling release.'),('tool','Connection tool approach',18,duration,'Tool actuator approaches the seated member. Bolt insertion and preload are still outstanding.')]],'frames':frames}
    health={'scenario':scenario,'mujocoVersion':mujoco.__version__,'timestepSeconds':float(m.opt.timestep),'durationSeconds':duration,'beamMassKg':mass,'robotMassKg':float(sum(m.body_mass[bodies[n]] for n in BODIES if n not in ['lifted_beam','hoist_carrier'])),'events':events,'hoistReleased':released,'frontLeftRegripped':regripped,'finalSeatLoadsN':seat_forces,'finalBeamPositionZUp':d.xpos[beam_id].tolist(),'robotRaiseM':float(d.xpos[bodies['robot_chassis'],2]-43.9),'maxContactPenetrationM':max_pen,'maxBeamSpeedMps':max_speed,'maxLimbActuatorTorqueNm':max_torque,'maxSolverIterations':max_solver,'warnings':{str(mujoco.mjtWarning(i)):int(d.warning[i].number) for i in range(int(mujoco.mjtWarning.mjNWARNING))},'finiteState':bool(np.isfinite(d.qpos).all() and np.isfinite(d.qvel).all()),'abortReason':abort_reason,'completeFastenedCycle':False}
    return trace,health

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=DEMO/'public/assets/workcell-trace.json'); ap.add_argument('--scenario',choices=['nominal','missed-seat'],default='nominal'); args=ap.parse_args()
    trace,health=run(args.scenario); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(trace,separators=(',',':'),allow_nan=False)); (HERE/f'{args.scenario}-validation.json').write_text(json.dumps(health,indent=2,allow_nan=False)+'\n'); print(json.dumps(health,indent=2))
if __name__=='__main__': main()
