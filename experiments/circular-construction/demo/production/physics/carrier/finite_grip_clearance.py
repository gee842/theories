"""Spatial finite-contact carrier candidate; baseline and synchronized candidates preserved.

No equality restraints, mocap bodies, applied body forces or live qpos edits.
This separate model preserves simulate.py's ideal-point comparison evidence.
"""
from pathlib import Path
import argparse, hashlib, json, math
import xml.etree.ElementTree as E
import mujoco
from contact_load_allocator import allocate
import numpy as np
from scipy.spatial.transform import Rotation

HERE=Path(__file__).resolve().parent
DEMO=HERE.parents[2]
CONTRACT=DEMO/'production/contracts/carrier-construction.json'
NAMES=('fl','fr','rl','rr')
HIP={'fl':(0,-.32,.48),'fr':(0,.32,.48),'rl':(0,-.32,-.48),'rr':(0,.32,-.48)}
L=.65; OFFSET=.135; RAIL=.75; START=1.44; PITCH=.32; DT=.00025
LIMITS={'hip_yaw':400.,'shoulder':3000.,'elbow':2000.,'wrist_yaw':150.,'wrist':400.,'wrist_roll':150.}
C=np.array([[1,0,0],[0,0,1],[0,-1,0.]])

def ik(x,z):
    cosine=np.clip((x*x+z*z-2*L*L)/(2*L*L),-1,1)
    elbow=math.acos(cosine)
    shoulder=-math.atan2(z,x)-elbow/2
    return np.array([shoulder,elbow,-shoulder-elbow])

def vec(x):return ' '.join(str(float(v)) for v in x)
def sub(root,kind,**args):return E.SubElement(root,kind,{k:str(v) for k,v in args.items()})

def model(payload=92.928,mu=.65):
    xml=E.Element('mujoco',model='Carrier finite sliding jaws and actual rail throat')
    sub(xml,'compiler',angle='radian',autolimits='true')
    opt=sub(xml,'option',timestep=DT,gravity='0 0 -9.81',integrator='implicitfast',solver='Newton',iterations=100,tolerance='1e-9',cone='elliptic',impratio=20)
    sub(opt,'flag',energy='enable')
    default=sub(xml,'default')
    sub(default,'joint',damping=5,armature=.05,limited='true')
    sub(default,'geom',contype=2,conaffinity=1,condim=4,friction=f'{mu} .005 .0001',solref='.002 1',solimp='.999 .9999 .0002',rgba='.55 .60 .61 1')
    world=sub(xml,'worldbody');act=sub(xml,'actuator')
    sub(world,'light',pos='-3 -4 6')
    # Column near side: source X=.93, original template yaw pi.
    for y in [-.104,.104]:sub(world,'geom',name='column_y_'+str(y),type='box',pos=vec((.93,y,2.4)),size='.11 .006 2.4',contype=1,conaffinity=2,rgba='.7 .72 .7 1')
    for x in [.826,1.034]:sub(world,'geom',name='column_x_'+str(x),type='box',pos=vec((x,0,2.4)),size='.006 .098 2.4',contype=1,conaffinity=2)
    for side,y in [('left',-.32),('right',.32)]:
        sub(world,'geom',name='rail_'+side,type='box',pos=vec((RAIL,y,2.4)),size='.0225 .025 2.4',contype=1,conaffinity=2)
        for k in range(15):
            z=.16+k*.32
            sub(world,'geom',name=f'receiver_{side}_{k}',type='box',pos=vec((.78,y,z)),size='.0375 .05 .004',contype=1,conaffinity=2,rgba='.7 .4 .15 1')
            sub(world,'geom',name=f'bracket_{side}_{k}',type='capsule',fromto=vec((.795,0,z,.795,y,z)),size='.018',contype=1,conaffinity=2)
    robot=sub(world,'body',name='robot_chassis',pos=vec((0,0,START)))
    sub(robot,'freejoint',name='base')
    sub(robot,'geom',name='chassis_shell',type='box',size='.33 .35 .50',mass=160)
    cradle=sub(robot,'body',name='payload_cradle',pos='-.61 0 0')
    sub(cradle,'geom',name='cradle_inertia',type='box',size='.11 .55 .08',mass=40,contype=0,conaffinity=0)
    beam=sub(cradle,'body',name='carried_beam')
    sub(beam,'geom',name='locked_payload',type='box',size='.05 1.5 .09',mass=payload)
    q0=ik(RAIL-OFFSET,0)
    for name in NAMES:
        up=sub(robot,'body',name=f'limb_{name}_upper',pos=vec(HIP[name]),euler=vec((0,q0[0],0)))
        sub(up,'joint',name=name+'_shoulder',axis='0 1 0',range='-2.4 2.4',ref=q0[0],damping=10,armature=.2)
        sub(up,'geom',name=name+'_upper_collision',type='capsule',fromto='0 0 0 .65 0 0',size='.065',mass=12)
        low=sub(up,'body',name=f'limb_{name}_lower',pos='.65 0 0',euler=vec((0,q0[1],0)))
        sub(low,'joint',name=name+'_elbow',axis='0 1 0',range='-2.7 2.7',ref=q0[1],damping=8,armature=.15)
        sub(low,'geom',name=name+'_lower_collision',type='capsule',fromto='0 0 0 .65 0 0',size='.052',mass=10)
        wrist=sub(low,'body',name=f'limb_{name}_grip',pos='.65 0 0',euler=vec((0,q0[2],0)))
        sub(wrist,'joint',name=name+'_wrist',axis='0 1 0',range='-2.7 2.7',ref=q0[2],damping=4,armature=.03)
        sub(wrist,'geom',name=name+'_wrist_housing',type='cylinder',quat='.70710678 .70710678 0 0',size='.062 .07',mass=5)
        sub(wrist,'geom',name=name+'_bridge',type='box',pos='.02 0 0',size='.0375 .17 .055',mass=1)
        sub(wrist,'site',name=name+'_contact',pos=vec((OFFSET,0,0)),size=.008)
        for sign,label in [(-1,'a'),(1,'b')]:
            jaw=sub(wrist,'body',name=f'{name}_jaw_{label}',pos=vec((.09,sign*.045,0)))
            sub(jaw,'joint',name=f'{name}_jaw_{label}',type='slide',axis=vec((0,sign,0)),range='-.003 .105',damping=25,armature=.002)
            sub(jaw,'geom',name=f'{name}_jaw_{label}_steel',type='box',pos=vec((.045,sign*.001,0)),size='.065 .019 .055',mass=1)
            sub(jaw,'geom',name=f'{name}_pad_{label}',type='box',pos=vec((.048,-sign*.018,0)),size='.0475 .002 .038',mass=0,priority=1,rgba='.08 .09 .10 1')
            sub(act,'position',name=f'{name}_jaw_{label}',joint=f'{name}_jaw_{label}',kp=200000,kv=900,ctrlrange='-.04 .105',forcerange='-8000 8000')
        for j,limit in LIMITS.items():sub(act,'motor',name=name+'_'+j,joint=name+'_'+j,ctrlrange=f'-{limit} {limit}',forcerange=f'-{limit} {limit}')
    # Additional articulation and mass are a NEW candidate, not hidden baseline support.
    for name in NAMES:
        upper=robot.find(f"body[@name='limb_{name}_upper']")
        robot.remove(upper)
        yaw=sub(robot,'body',name=f'limb_{name}_hip_yaw',pos=vec(HIP[name]))
        sub(yaw,'joint',name=name+'_hip_yaw',axis='0 0 1',range='-.6 .6',damping=5,armature=.03)
        sub(yaw,'geom',name=name+'_hip_yaw_motor',type='cylinder',size='.08 .04',mass=3)
        upper.set('pos','0 0 0');yaw.append(upper)
        lower=upper.find(f"body[@name='limb_{name}_lower']")
        old=lower.find(f"body[@name='limb_{name}_grip']");lower.remove(old)
        wy=sub(lower,'body',name=f'limb_{name}_wrist_yaw',pos='.65 0 0')
        sub(wy,'joint',name=name+'_wrist_yaw',axis='0 0 1',range='-.6 .6',damping=3,armature=.015)
        sub(wy,'geom',name=name+'_wrist_yaw_inertia',type='cylinder',size='.06 .025',mass=1,contype=0,conaffinity=0)
        old.set('pos','0 0 0');old.set('name',f'limb_{name}_wrist_pitch');wy.append(old)
        roll=sub(old,'body',name=f'limb_{name}_grip')
        sub(roll,'joint',name=name+'_wrist_roll',axis='1 0 0',range='-.6 .6',damping=3,armature=.015)
        sub(roll,'geom',name=name+'_gimbal_inertia',type='sphere',size='.055',mass=1,contype=0,conaffinity=0)
        for item in list(old):
            if item is not roll and item.tag not in ('joint','inertial') and item.get('name')!=name+'_wrist_housing':old.remove(item);roll.append(item)
    return E.tostring(xml,encoding='unicode')

def smooth(t):
    u=np.clip(t,0,1);return float(u*u*(3-2*u))

def simulate(mode='hold',payload=92.928,mu=.65,clamp=4000.,duration=8.,fps=20,shift_x=0.):
    xml=model(payload,mu);m=mujoco.MjModel.from_xml_string(xml);d=mujoco.MjData(m)
    mujoco.mj_forward(m,d)
    bid=m.body('robot_chassis').id
    sid={n:m.site(n+'_contact').id for n in NAMES}
    motors={m.actuator(i).name:i for i in range(m.nu)}
    qadr={m.joint(i).name:int(m.jnt_qposadr[i]) for i in range(m.njnt)}
    vadr={m.joint(i).name:int(m.jnt_dofadr[i]) for i in range(m.njnt)}
    jointnames=[n+'_'+j for n in NAMES for j in LIMITS]
    qas=np.array([qadr[n] for n in jointnames]);vas=np.array([vadr[n] for n in jointnames])
    aids=np.array([motors[n] for n in jointnames])
    limits=np.array([LIMITS[j] for n in NAMES for j in LIMITS])
    # Initial condition only: engaged jaws touching rails. No live state edits follow.
    initial_qpos=d.qpos.copy()
    targets={n:np.array([RAIL,HIP[n][1],START+HIP[n][2]]) for n in NAMES}
    phase='settle';begin=0.;released=None;events=[];frames=[];step=0;complete=False;abort=None
    desired_z=START;desired_x=0.;rungs={n:0 for n in NAMES};index=0
    metrics={'maxTiltRad':0.,'maxChassisDriftM':0.,'maxPenetrationM':0.,'maxNonGripCollisionN':0.,'maxContactForceN':0.,'maxJawNormalSumN':0.,'minRetainedUpwardSupports':4,'maxTorqueNm':{j:0. for j in LIMITS},'maxSolverIterations':0,'maxJointLimitViolation':0.,'maxHingeLimitViolationRad':0.,'maxJawLimitViolationM':0.}
    support={n:np.zeros(3) for n in NAMES};normals={n:0. for n in NAMES};contactcount={n:0 for n in NAMES}
    non_grip=[]
    jaw_sides={n:{'a':0.,'b':0.} for n in NAMES}
    metrics.update({'minRetainedJawSideNormalN':1e9,'maxRetainedGripErrorM':0.,'maxFrictionUtilization':0.,'maxDynamicForceResidualN':0.,'minSignedVerticalReactionN':0.})
    previous_com_velocity=np.zeros(3)
    allocation=None;allocation_key=None;allocation_time=-1.;allocation_report={}
    def record(event,**kwargs):events.append({'time':float(d.time),'event':event,**kwargs})
    def contacts():
        for n in NAMES:jaw_sides[n]={'a':0.,'b':0.}
        loads={n:np.zeros(3) for n in NAMES};normal={n:0. for n in NAMES};counts={n:0 for n in NAMES};bad=[]
        for ci in range(d.ncon):
            co=d.contact[ci];gn=[m.geom(int(g)).name or '' for g in (co.geom1,co.geom2)]
            force=np.zeros(6);mujoco.mj_contactForce(m,d,ci,force)
            # Contact normal points geom1 -> geom2; force is on geom2.
            world=co.frame.reshape(3,3).T@force[:3]
            found=False
            for n in NAMES:
                for side in (0,1):
                    if (gn[side].startswith(n+'_jaw_') or gn[side].startswith(n+'_pad_')) and gn[1-side].startswith('rail_'):
                        loads[n]+=world*(1 if side==1 else -1);normal[n]+=abs(force[0]);counts[n]+=1;found=True
                        label='a' if '_a' in gn[side].removeprefix(n) else 'b'
                        jaw_sides[n][label]+=abs(force[0])
                        if abs(force[0])>1:metrics['maxFrictionUtilization']=max(metrics['maxFrictionUtilization'],float(np.linalg.norm(force[1:3])/(mu*abs(force[0]))))
            if not found and np.linalg.norm(world)>1:bad.append({'geoms':gn,'forceN':float(np.linalg.norm(world))})
            if -float(co.dist)>metrics['maxPenetrationM']:
                metrics['maxPenetrationM']=-float(co.dist);metrics['worstPenetration']={'time':float(d.time),'geoms':gn,'forceN':float(np.linalg.norm(world))}
            metrics['maxContactForceN']=max(metrics['maxContactForceN'],float(np.linalg.norm(world)))
        return loads,normal,counts,bad

    while d.time<duration:
        mujoco.mj_forward(m,d)
        t=float(d.time);elapsed=t-begin
        if phase=='settle' and elapsed>2.:
            if min(min(jaw_sides[n].values()) for n in NAMES)<1000 or max(np.linalg.norm(d.site_xpos[sid[n]]-targets[n]) for n in NAMES)>.035:
                abort='Initial contact support gate failed';record('hold-rejected',support={n:support[n].tolist() for n in NAMES});break
            record('four-contact-hold-accepted')
            if mode=='hold':phase='hold';begin=t
            else:
                phase='shift' if shift_x else 'unload';begin=t;released=None if shift_x else NAMES[index];record('body-shift-command',targetX=shift_x) if shift_x else record('release-command',limb=released)
        elif phase=='shift':
            desired_x=shift_x*smooth(elapsed/2.)
            if elapsed>3.:
                phase='unload';begin=t;released=NAMES[index];record('unload-command',limb=released)
        elif phase=='unload' and elapsed>1.:
            retained_now=[n for n in NAMES if n!=released]
            if np.linalg.norm(support[released])<200 and min(min(jaw_sides[n].values()) for n in retained_now)>1000:
                phase='open';begin=t;record('measured-load-transfer',limb=released,remainingUpwardN={n:float(support[n][2]) for n in retained_now},releasedLoadN=float(np.linalg.norm(support[released])))
            elif elapsed>6:abort='Measured unloading gate failed';break
        elif phase=='hold' and elapsed>3.:
            complete=True;break
        elif phase=='open' and elapsed>1.5:
            if all(d.qpos[qadr[released+'_jaw_'+letter]]>.09 for letter in ('a','b')):
                phase='move';begin=t;record('jaw-open-confirmed',limb=released)
            elif elapsed>3:abort='Jaw opening stalled';break
        elif phase=='move' and elapsed>9.:
            phase='close';begin=t;record('capture-command',limb=released)
        elif phase=='close' and elapsed>1.5:
            captured=min(jaw_sides[released].values())>1000 and abs(support[released][2])>50
            capture_target=targets[released]+np.array([0,0,PITCH if mode in ('step','limb') else 0])
            err=float(np.linalg.norm(d.site_xpos[sid[released]]-capture_target))
            if captured and err<.03:
                record('finite-contact-recapture',limb=released,errorM=err,upwardN=float(support[released][2]));rungs[released]=1 if mode in ('step','limb') else 0
                released=None
                if mode in ('recapture','limb'):phase='hold';begin=t
                else:
                    index+=1
                    if index<4:released=NAMES[index];phase='unload';begin=t;record('unload-command',limb=released)
                    else:phase='raise';begin=t;record('raise-command')
            elif elapsed>5.:abort='Finite capture load/position gate failed';break
        elif phase=='raise':
            desired_z=START+PITCH*smooth(elapsed/6.)
            if elapsed>8:phase='hold';begin=t
        elapsed=t-begin  # Recompute after every phase transition before using phase clocks.
        if released:
            retained=[n for n in NAMES if n!=released]
            if elapsed>.3 and phase in ('move','close') and min(min(jaw_sides[n].values()) for n in retained)<1000:
                abort='Retained jaw normal-contact gate failed';record('supported-stop-request',limb=released);break
        qtarget=[]
        bodyR=d.xmat[bid].reshape(3,3)
        for n in NAMES:
            foot=targets[n].copy()
            if n==released and phase=='move':
                if mode in ('step','limb'):
                    retreat=.12*(smooth(elapsed/2.) if elapsed<2 else (1. if elapsed<7 else 1-smooth((elapsed-7)/2.)))
                    foot[0]-=retreat
                    foot[2]+=PITCH*smooth((elapsed-2)/5.)
                else:foot[0]-=.035*math.sin(math.pi*smooth(elapsed/4.))**2
            elif n==released and phase=='close' and mode in ('step','limb'):foot[2]+=PITCH
            elif rungs[n]:foot[2]+=PITCH
            if n==released:
                wrist=bodyR.T@(foot-d.xpos[bid])-np.array(HIP[n])-bodyR.T@np.array([OFFSET,0,0])
            else:
                wrist=foot-np.array([desired_x,0,desired_z])-np.array(HIP[n])-np.array([OFFSET,0,0])
            yaw=math.atan2(wrist[1],wrist[0])
            planar=ik(math.hypot(wrist[0],wrist[1]),wrist[2])
            pre=Rotation.from_euler('z',float(d.qpos[qadr[n+'_hip_yaw']])).as_matrix()@Rotation.from_euler('y',float(d.qpos[qadr[n+'_shoulder']]+d.qpos[qadr[n+'_elbow']])).as_matrix()
            wy,wp,wr=Rotation.from_matrix(pre.T@bodyR.T).as_euler('ZYX')
            qtarget.extend([yaw,planar[0],planar[1],wy,wp,wr])
        retained=[n for n in NAMES if n!=released]
        jacobians=[]
        for n in retained:
            jac=np.zeros((3,m.nv));mujoco.mj_jacSite(m,d,jac,None,sid[n]);jacobians.append(jac.T)
        grasp=np.concatenate(jacobians,axis=1)
        controlled_bias=d.qfrc_bias.copy()
        controlled_bias[:3]+=float(m.body_mass.sum())*(35*(np.array([desired_x,0,desired_z])-d.xpos[bid])-12*d.qvel[:3])
        orientation_error=Rotation.from_matrix(bodyR.T).as_rotvec()
        controlled_bias[3:6]+=3000*orientation_error-400*d.qvel[3:6]
        if allocation is None or tuple(retained)!=allocation_key or t-allocation_time>.02:
            allocation,allocation_report=allocate(grasp,controlled_bias,vas,limits,mu,clamp*2,allow_downward=True)
            allocation_key=tuple(retained);allocation_time=t
        force=allocation if allocation is not None else np.linalg.lstsq(grasp[:6],d.qfrc_bias[:6],rcond=1e-8)[0]

        ff=d.qfrc_bias[vas]-(grasp@force)[vas]
        kp=np.tile([0.,0.,0.,2500.,6000.,2500.],4)
        kd=np.tile([20.,25.,25.,80.,200.,80.],4)
        if released and phase in ('move','close'):
            i=NAMES.index(released)*6
            kp[i:i+3]=[8000.,12000.,12000.];kd[i:i+3]=[300.,700.,700.]
        d.ctrl[aids]=np.clip(kp*(np.array(qtarget)-d.qpos[qas])-kd*d.qvel[vas]+ff,-limits,limits)
        for n in NAMES:
            opening=n==released and phase in ('open','move')
            for label in ('a','b'):
                name=n+'_jaw_'+label
                closed=-clamp/200000.
                if n==released and phase=='open':target=closed+(.105-closed)*smooth((elapsed-.5)/1.)
                elif opening:target=.105
                elif n==released and phase=='close':target=.105+(closed-.105)*smooth(elapsed/3.)
                else:target=closed
                d.ctrl[motors[name]]=target
        mujoco.mj_step(m,d)
        support,normals,contactcount,non_grip=contacts()
        mujoco.mj_forward(m,d)
        mujoco.mj_subtreeVel(m,d)
        com_velocity=d.subtree_linvel[bid].copy()
        residual=np.linalg.norm(sum(support.values())+np.array([0,0,-m.body_mass.sum()*9.81])-m.body_mass.sum()*(com_velocity-previous_com_velocity)/DT)
        previous_com_velocity=com_velocity
        if t>1:
            metrics['maxDynamicForceResidualN']=max(metrics['maxDynamicForceResidualN'],float(residual))
            metrics['minRetainedJawSideNormalN']=min(metrics['minRetainedJawSideNormalN'],*[min(jaw_sides[n].values()) for n in retained])
            metrics['maxRetainedGripErrorM']=max(metrics['maxRetainedGripErrorM'],*[float(np.linalg.norm(d.site_xpos[sid[n]]-targets[n]-np.array([0,0,PITCH*rungs[n]]))) for n in retained])
            metrics['minSignedVerticalReactionN']=min(metrics['minSignedVerticalReactionN'],*[float(support[n][2]) for n in retained])
        metrics['maxJawNormalSumN']=max(metrics['maxJawNormalSumN'],*normals.values())
        metrics['maxNonGripCollisionN']=max(metrics['maxNonGripCollisionN'],*(x['forceN'] for x in non_grip),0.)
        tilt=math.acos(np.clip(d.xmat[bid].reshape(3,3)[2,2],-1,1));metrics['maxTiltRad']=max(metrics['maxTiltRad'],tilt)
        drift=float(np.linalg.norm(d.xpos[bid]-np.array([desired_x,0,desired_z])));metrics['maxChassisDriftM']=max(metrics['maxChassisDriftM'],drift)
        if t>1:metrics['minRetainedUpwardSupports']=min(metrics['minRetainedUpwardSupports'],int(sum(support[n][2]>10 for n in retained)))
        for j in LIMITS:metrics['maxTorqueNm'][j]=max(metrics['maxTorqueNm'][j],*[abs(float(d.actuator_force[motors[n+'_'+j]])) for n in NAMES])
        for ji in range(1,m.njnt):
            q=float(d.qpos[int(m.jnt_qposadr[ji])]);violation=max(0.,float(m.jnt_range[ji,0])-q,q-float(m.jnt_range[ji,1]));metrics['maxJointLimitViolation']=max(metrics['maxJointLimitViolation'],violation)
            field='maxJawLimitViolationM' if m.jnt_type[ji]==mujoco.mjtJoint.mjJNT_SLIDE else 'maxHingeLimitViolationRad';metrics[field]=max(metrics[field],violation)
        metrics['maxSolverIterations']=max(metrics['maxSolverIterations'],int(max(d.solver_niter)))
        if step%max(1,round(1/(DT*fps)))==0:
            quat=np.zeros(4);mujoco.mju_mat2Quat(quat,(C@d.xmat[bid].reshape(3,3)@C.T).ravel())
            frames.append({'time':float(d.time),'phase':phase,'position':(C@d.xpos[bid]).tolist(),'quaternion':quat[[1,2,3,0]].tolist(),'quaternionSourceWxyz':d.xquat[bid].tolist(),'joints':{n:{j:float(d.qpos[qadr[n+'_'+j]]) for j in LIMITS} for n in NAMES},'jawOutwardDisplacementM':{n:[float(d.qpos[qadr[n+'_jaw_'+label]]) for label in ('a','b')] for n in NAMES},'gripPositionsSourceM':{n:d.site_xpos[sid[n]].tolist() for n in NAMES},'contactForcesSourceN':{n:force.tolist() for n,force in support.items()},'jawNormalSumN':normals,'jawSideNormalN':{n:dict(v) for n,v in jaw_sides.items()},'dynamicForceResidualN':float(residual),'contactCounts':contactcount,'torquesNm':{n:{j:float(d.actuator_force[motors[n+'_'+j]]) for j in LIMITS} for n in NAMES},'loadAllocation':allocation_report,'nonGripContacts':non_grip,'tiltRad':tilt})
        step+=1
        if tilt>.20 or drift>.16:abort='Pose safety envelope exceeded';record('abort',reason=abort);break
    accepted=bool(complete and metrics['maxPenetrationM']<.002 and metrics['maxNonGripCollisionN']<50 and metrics['maxJointLimitViolation']<.002 and metrics['minRetainedJawSideNormalN']>1000 and metrics['maxRetainedGripErrorM']<.03 and metrics['maxFrictionUtilization']<1.02 and metrics['maxDynamicForceResidualN']<50)
    if complete and not accepted:abort='Contact-quality gate rejected completed phase sequence'
    metrics.update({'retentionGate':'Both jaws >1000 N normal per retained grip, position error <30mm; signed vertical reactions allowed. Positive-reaction count is diagnostic only.','contactQualityAccepted':accepted,'finalSpeedMps':float(np.linalg.norm(d.qvel[:3])),'sequenceComplete':complete,'complete':accepted,'abortReason':abort,'mode':mode,'durationSeconds':float(d.time),'payloadMassKg':payload,'totalMassKg':float(m.body_mass.sum()),'lastLoadAllocation':allocation_report,'controllerRevision':'six-axis-measured-unload-retreat-rise-approach','finalLimbAdvanceM':{n:float(d.site_xpos[sid[n]][2]-targets[n][2]) for n in NAMES},'chassisAdvanceM':float(d.xpos[bid][2]-START),'bodyShiftTargetXM':shift_x,'frictionCoefficient':mu,'jawClosingForceEachN':clamp,'solverSettings':{'cone':'elliptic','impratio':20,'normalSolref':[.002,1],'normalSolimp':[.999,.9999,.0002],'noSlipIterations':0},'candidateDesign':{'dryMassKg':340,'extraMassKg':20,'hipYawTorqueNm':400,'wristRollYawTorqueNm':150,'sharedAssetsUpdated':False},'controllerSpecs':{'wristTorqueNm':400,'jawForceBoundN':8000,'jawPositionKpNPerM':200000,'jawVelocityDampingNsPerM':900},'finalPositionSourceM':d.xpos[bid].tolist(),'finalContactForcesSourceN':{n:f.tolist() for n,f in support.items()},'finalJawNormalSumN':normals,'events':events,'equalityConstraintCount':m.neq,'mocapBodyCount':m.nmocap,'liveQposEdits':False,'appliedBodyForces':False,'modelSha256':hashlib.sha256(xml.encode()).hexdigest(),'contractSha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'mujocoVersion':mujoco.__version__,'warnings':{str(mujoco.mjtWarning(i)):int(d.warning[i].number) for i in range(int(mujoco.mjtWarning.mjNWARNING))},'limitations':['Rigid prelocked payload/cradle; restraint closure not solved.','Coulomb pad/steel friction is an assumed coefficient, not measured hardware data.','Rigid fixed column and rails; structural compliance omitted.','Robot-to-environment collisions enabled; robot self-collision omitted, including bearing adjacency.','Simplified collision primitives approximate manufactured housings.','400 Nm wrist and 8 kN jaw motor bounds are proposed specs, not qualified hardware.','Friction impedance ratio20 and stiff normal contact reduce regularization creep; sensitivity is required.', 'Initial condition already attached; arrival and transition from ground are not simulated here.']})
    return xml,metrics,{'schemaVersion':1,'coordinates':'gltf-y-up poses; explicitly named contactForcesSourceN are source-z-up','scope':'force-driven finite-jaw local contact; no equality grip locks','metrics':metrics,'frames':frames}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['hold','recapture','limb','step'],default='hold');ap.add_argument('--payload-kg',type=float,default=92.928);ap.add_argument('--mu',type=float,default=.65);ap.add_argument('--clamp-n',type=float,default=4000);ap.add_argument('--duration',type=float,default=70);ap.add_argument('--shift-x',type=float,default=0)
    a=ap.parse_args();xml,metrics,trace=simulate(a.mode,a.payload_kg,a.mu,a.clamp_n,a.duration,shift_x=a.shift_x)
    stem=f'candidate-clearance-{a.mode}-{a.payload_kg:g}kg-mu{a.mu:g}'+(f'-sx{a.shift_x:g}' if a.shift_x else '')
    (HERE/(stem+'.xml')).write_text(xml);(HERE/(stem+'-metrics.json')).write_text(json.dumps(metrics,indent=2,allow_nan=False)+'\n');(HERE/(stem+'-trace.json')).write_text(json.dumps(trace,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(metrics,indent=2,allow_nan=False))
if __name__=='__main__':main()
