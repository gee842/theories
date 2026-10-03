import { add, sub, scale, dot, length, unit, rotateZ, clamp, cross, capsuleIntersectsBox, segmentDistance, mix } from './math';
import type { Vec3, Obstacle, RobotConfig, RobotState, LimbPose, RobotPose, StanceAssessment, LimbLoad } from './types';

export const DEFAULT_ROBOT_CONFIG: RobotConfig = {
  upperLength:0.73, foreLength:0.68, bodyWidth:0.58, bodyHeight:0.43, bodyDepth:0.3,
  linkRadius:0.046, elbowFlexMin:0.22, elbowFlexMax:2.7, shoulderConeMax:2.75,
  bodyMass:56, upperMass:4.5, foreMass:3, clampMass:2.5, toolMass:6,
  gripForceLimit:1500, gripMomentLimit:240, shoulderTorqueLimit:520, elbowTorqueLimit:360,
  swingClearance:0.23, stepSeconds:3.6, capacitySource:'assumed',
};
export const shoulderOffset = (index:number,c:RobotConfig):Vec3 => [(index%2===0?-1:1)*c.bodyWidth/2,0,(index<2?1:-1)*c.bodyHeight/2];
export const robotMass = (c:RobotConfig):number => c.bodyMass+4*(c.upperMass+c.foreMass+c.clampMass)+c.toolMass;
export const TOOL_DOCK_OFFSET:Vec3=[0.82,-0.12,0.4];

/** Two-link position IK with spherical shoulders, elbow hinge, and a wrist orientation joint.
 * Clamp orientation is rendered; wrist torque/orientation limits are presently unverified. */
export function solveLimb(state:RobotState,index:number,target:Vec3=state.limbs[index].position):LimbPose {
  const c=state.config,offset=shoulderOffset(index,c),shoulder=add(state.position,rotateZ(offset,state.yaw));
  const delta=sub(target,shoulder),r=length(delta),axis=unit(delta);
  const safeR=clamp(r,Math.abs(c.upperLength-c.foreLength)+1e-7,c.upperLength+c.foreLength-1e-7);
  const along=(c.upperLength*c.upperLength-c.foreLength*c.foreLength+safeR*safeR)/(2*safeR);
  const outward=rotateZ([(index%2===0?-1:1),0,(index<2?1:-1)*0.5],state.yaw);
  let bend=sub(outward,scale(axis,dot(outward,axis)));
  if(length(bend)<1e-6)bend=cross(axis,[0,0,1]);
  if(length(bend)<1e-6)bend=cross(axis,[1,0,0]);
  const elbow=add(add(shoulder,scale(axis,along)),scale(unit(bend),Math.sqrt(Math.max(0,c.upperLength*c.upperLength-along*along))));
  const elbowFlex=Math.acos(clamp((r*r-c.upperLength*c.upperLength-c.foreLength*c.foreLength)/(2*c.upperLength*c.foreLength),-1,1));
  const shoulderAngle=Math.acos(clamp(dot(unit(sub(elbow,shoulder)),rotateZ([(index%2===0?-1:1),0,0],state.yaw)),-1,1));
  const reachable=r>Math.abs(c.upperLength-c.foreLength)+0.01&&r<c.upperLength+c.foreLength-0.01&&elbowFlex>=c.elbowFlexMin&&elbowFlex<=c.elbowFlexMax&&shoulderAngle<=c.shoulderConeMax;
  return {shoulder,elbow,wrist:[...target],reachable,elbowFlex,shoulderAngle};
}

export function solveRobotPose(state:RobotState,obstacles:Obstacle[]=[]):RobotPose {
  const limbs=state.limbs.map((_,i)=>solveLimb(state,i)),reasons:string[]=[];
  const c=state.config;
  for(const [i,p] of limbs.entries()) {
    if(!p.reachable)reasons.push(`Limb ${i+1} outside reach/joint envelope`);
    const segments:[[Vec3,Vec3],[Vec3,Vec3]]=[[p.shoulder,p.elbow],[p.elbow,p.wrist]];
    for(const box of obstacles)for(const [a,b] of segments)if(capsuleIntersectsBox(a,b,c.linkRadius,box)) { reasons.push(`Limb ${i+1} intersects ${box.id}`);break; }
  }
  // Separate arms must not intersect. Adjacent links on a single limb intentionally meet.
  for(let i=0;i<4;i++)for(let j=i+1;j<4;j++) {
    const a=limbs[i],b=limbs[j];
    for(const [p,q] of [[a.shoulder,a.elbow],[a.elbow,a.wrist]] as [Vec3,Vec3][])
      for(const [r,s] of [[b.shoulder,b.elbow],[b.elbow,b.wrist]] as [Vec3,Vec3][])
        if(segmentDistance(p,q,r,s)<2*c.linkRadius)reasons.push(`Limbs ${i+1}/${j+1} collide`);
  }
  // Torso is conservatively represented by its world-axis bounding box after yaw.
  const hX=Math.abs(Math.cos(state.yaw))*c.bodyWidth/2+Math.abs(Math.sin(state.yaw))*c.bodyDepth/2;
  const hY=Math.abs(Math.sin(state.yaw))*c.bodyWidth/2+Math.abs(Math.cos(state.yaw))*c.bodyDepth/2;
  const bodyMin=add(state.position,[-hX,-hY,-c.bodyHeight/2]),bodyMax=add(state.position,[hX,hY,c.bodyHeight/2]);
  for(const box of obstacles)if([0,1,2].every(k=>bodyMin[k]<box.max[k]&&bodyMax[k]>box.min[k]))reasons.push(`Torso intersects ${box.id}`);
  const torso:Obstacle={id:'torso',min:[-c.bodyWidth/2,-c.bodyDepth/2,-c.bodyHeight/2],max:[c.bodyWidth/2,c.bodyDepth/2,c.bodyHeight/2]};
  for(const [i,p] of limbs.entries()) {
    const local=(v:Vec3)=>rotateZ(sub(v,state.position),-state.yaw);
    // Trim the upper link near its shoulder socket; test the complete forearm.
    if(capsuleIntersectsBox(local(mix(p.shoulder,p.elbow,0.2)),local(p.elbow),c.linkRadius,torso)||capsuleIntersectsBox(local(p.elbow),local(p.wrist),c.linkRadius,torso))reasons.push(`Limb ${i+1} intersects torso`);
  }
  return {limbs,check:{status:reasons.length?'fail':'pass',scope:'two-link IK, joint envelope, capsule self collision and supplied box obstacles',reasons:[...new Set(reasons)]}};
}

/** A specific, checkable contact-wrench allocation: equal gravity reactions plus equal
 * keyed-clamp moments. This is sufficient when within limits, not an optimizer: failure
 * means this allocation failed, not that every possible load distribution is impossible. */
export function assessStance(state:RobotState,obstacles:Obstacle[]=[],excludedLimb=-1):StanceAssessment {
  const pose=solveRobotPose(state,obstacles),c=state.config;
  const active=state.limbs.filter(l=>l.index!==excludedLimb&&l.mode==='load_verified'&&l.anchor!==null);
  const reasons=[...pose.check.reasons],n=active.length,loads:LimbLoad[]=[];
  if(n<3)reasons.push('At least three verified keyed grips required by this gait policy');
  const weight:Vec3=[0,0,-robotMass(c)*9.81],force:Vec3=n?scale(weight,-1/n):[0,0,0];
  const momentSum=active.reduce<Vec3>((sum,l)=>add(sum,cross(sub(l.position,state.position),force)),[0,0,0]);
  let weightedCenter=scale(state.position,c.bodyMass);
  for(const p of pose.limbs)weightedCenter=add(weightedCenter,add(add(scale(mix(p.shoulder,p.elbow,0.5),c.upperMass),scale(mix(p.elbow,p.wrist,0.5),c.foreMass)),scale(p.wrist,c.clampMass)));
  const toolPosition=state.limbs.find(l=>l.tool)?.position??add(state.position,rotateZ(TOOL_DOCK_OFFSET,state.yaw));
  weightedCenter=add(weightedCenter,scale(toolPosition,c.toolMass));
  const centerOfMass=scale(weightedCenter,1/robotMass(c));
  const gravityMoment=cross(sub(centerOfMass,state.position),weight);
  const moment:Vec3=n?scale(add(momentSum,gravityMoment),-1/n):[0,0,0];
  let maxUtilization=0;
  const missing=[c.gripForceLimit,c.gripMomentLimit,c.shoulderTorqueLimit,c.elbowTorqueLimit].some(v=>v===null||v<=0);
  for(const l of active) {
    const p=pose.limbs[l.index];
    const upperGravity:Vec3=[0,0,-c.upperMass*9.81],foreGravity:Vec3=[0,0,-c.foreMass*9.81],clampGravity:Vec3=[0,0,-c.clampMass*9.81];
    const shoulderMoment=add(add(cross(sub(p.wrist,p.shoulder),force),moment),add(add(cross(sub(mix(p.shoulder,p.elbow,0.5),p.shoulder),upperGravity),cross(sub(mix(p.elbow,p.wrist,0.5),p.shoulder),foreGravity)),cross(sub(p.wrist,p.shoulder),clampGravity)));
    const elbowMoment=add(add(cross(sub(p.wrist,p.elbow),force),moment),add(cross(sub(mix(p.elbow,p.wrist,0.5),p.elbow),foreGravity),cross(sub(p.wrist,p.elbow),clampGravity)));
    const shoulderTorque=length(shoulderMoment),elbowTorque=length(elbowMoment);
    const utilization=missing?null:Math.max(length(force)/c.gripForceLimit!,length(moment)/c.gripMomentLimit!,shoulderTorque/c.shoulderTorqueLimit!,elbowTorque/c.elbowTorqueLimit!);
    if(utilization!==null)maxUtilization=Math.max(maxUtilization,utilization);
    if(utilization!==null&&utilization>1)reasons.push(`Grip ${l.index+1} allocation exceeds assumed wrench/actuator limit`);
    loads.push({index:l.index,force:[...force],moment:[...moment],shoulderTorque,elbowTorque,utilization});
  }
  // The moving/tooling arm still needs actuator capacity to carry its own links and tool.
  for(const l of state.limbs.filter(l=>!active.some(a=>a.index===l.index))) {
    const p=pose.limbs[l.index],upperGravity:Vec3=[0,0,-c.upperMass*9.81],foreGravity:Vec3=[0,0,-c.foreMass*9.81];
    const tipGravity:Vec3=[0,0,-(c.clampMass+(l.tool?c.toolMass:0))*9.81];
    const shoulderTorque=length(add(add(cross(sub(mix(p.shoulder,p.elbow,0.5),p.shoulder),upperGravity),cross(sub(mix(p.elbow,p.wrist,0.5),p.shoulder),foreGravity)),cross(sub(p.wrist,p.shoulder),tipGravity)));
    const elbowTorque=length(add(cross(sub(mix(p.elbow,p.wrist,0.5),p.elbow),foreGravity),cross(sub(p.wrist,p.elbow),tipGravity)));
    const utilization=missing?null:Math.max(shoulderTorque/c.shoulderTorqueLimit!,elbowTorque/c.elbowTorqueLimit!);
    if(utilization!==null)maxUtilization=Math.max(maxUtilization,utilization);
    if(utilization!==null&&utilization>1)reasons.push(`Free limb ${l.index+1} exceeds assumed actuator limit`);
    loads.push({index:l.index,force:[0,0,0],moment:[0,0,0],shoulderTorque,elbowTorque,utilization});
  }
  const forceResidual=length(add(weight,scale(force,n))),momentResidual=length(add(add(momentSum,gravityMoment),scale(moment,n)));
  if(forceResidual>1e-5||momentResidual>1e-5)reasons.push('Contact allocation does not balance external wrench');
  return {status:reasons.length?'fail':missing?'unverified':'pass',scope:`quasi-static keyed-clamp allocation; capacities ${c.capacitySource}; wrist/dynamics/frame reactions unverified`,reasons,anchorCount:n,loads,forceResidual,momentResidual,maxUtilization:missing?null:maxUtilization};
}
