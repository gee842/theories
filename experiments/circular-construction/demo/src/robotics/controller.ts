import { add, sub, scale, mix, rotateZ, length, clamp } from './math';
import { DEFAULT_ROBOT_CONFIG, TOOL_DOCK_OFFSET, assessStance } from './kinematics';
import type { Vec3, RobotState, RobotOptions, Anchor, Motion, MotionPlan, Obstacle, RailClimber } from './types';

const record=(state:RobotState,message:string):void=>{state.status=message;state.events.push({time:state.elapsed,message});if(state.events.length>160)state.events.shift();};
export function createRobotState(options:RobotOptions):RobotState {
  const {position,yaw=0,id='climber'}=options, config={...DEFAULT_ROBOT_CONFIG,...options.config};
  const limbs=Array.from({length:4},(_,i)=>{
    const point=add(position,rotateZ([(i%2===0?-1:1)*0.58,0.68,(i<2?1:-1)*0.54],yaw));
    return {index:i,position:point,anchor:{id:`${id}-initial-${i}`,position:[...point] as Vec3,normal:rotateZ([0,-1,0],yaw),available:true},mode:'load_verified' as const,tool:false};
  });
  return {id,position:[...position],yaw,config,limbs,motion:null,status:'Commissioned four-grip initial stance',elapsed:0,completedSteps:0,faultCount:0,toolDocked:true,events:[]};
}
const smooth=(t:number):number=>t*t*(3-2*t);
function swingPoint(state:RobotState,start:Vec3,end:Vec3,t:number):Vec3 {
  return add(mix(start,end,smooth(t)),scale(rotateZ([0,-1,0],state.yaw),state.config.swingClearance*Math.sin(Math.PI*t)));
}
function copyPose(state:RobotState):RobotState {
  return {...state,position:[...state.position],limbs:state.limbs.map(l=>({...l,position:[...l.position]}))};
}
function validateMotion(state:RobotState,motion:Motion,obstacles:Obstacle[]):MotionPlan {
  const reasons:string[]=[],candidate=copyPose(state);
  // At most 20 mm of endpoint/body progress per sample, plus 40 samples for the arch.
  const count=Math.max(40,Math.ceil((length(sub(motion.end,motion.start))+Math.PI*state.config.swingClearance)/0.02));
  motion.samples=[];
  for(let i=0;i<=count;i++) {
    const t=i/count,p=motion.kind==='body'?mix(motion.start,motion.end,smooth(t)):swingPoint(state,motion.start,motion.end,t);
    motion.samples.push(p);
    if(motion.kind==='body')candidate.position=p;
    else candidate.limbs[motion.limbIndex!].position=p;
    if(motion.kind==='tool'&&i===count)candidate.limbs[motion.limbIndex!].tool=motion.toolAction==='pick';
    const stance=assessStance(candidate,obstacles,motion.kind==='body'?-1:motion.limbIndex);
    if(stance.status!=='pass') {reasons.push(...stance.reasons, ...(stance.status==='unverified'?['Missing declared capacity: motion not approved']:[]));break;}
  }
  return {status:reasons.length?'fail':'pass',scope:'sampled IK, self/environment collision and quasi-static capacity through motion',reasons:[...new Set(reasons)],...(reasons.length?{}:{motion})};
}
export function planStep(state:RobotState,limbIndex:number,targetAnchor:Anchor,obstacles:Obstacle[]=[],failVerification=false):MotionPlan {
  if(state.motion)return {status:'fail',scope:'step preconditions',reasons:['Another primitive is active']};
  if(!state.limbs[limbIndex])return {status:'fail',scope:'step preconditions',reasons:['Invalid limb index']};
  if(state.limbs.some(l=>l.tool))return {status:'fail',scope:'step preconditions',reasons:['Park the tool before travelling']};
  if(!targetAnchor.available)return {status:'fail',scope:'step preconditions',reasons:['Destination grip unavailable']};
  const motion:Motion={kind:'step',elapsed:0,duration:state.config.stepSeconds,limbIndex,start:[...state.limbs[limbIndex].position],end:[...targetAnchor.position],targetAnchor,failVerification,samples:[]};
  return validateMotion(state,motion,obstacles);
}
export function planBodyMove(state:RobotState,target:Vec3,obstacles:Obstacle[]=[]):MotionPlan {
  if(state.motion||state.limbs.some(l=>l.mode!=='load_verified'))return {status:'fail',scope:'body move preconditions',reasons:['Four verified grips and no active primitive required']};
  return validateMotion(state,{kind:'body',elapsed:0,duration:Math.max(1.2,length(sub(target,state.position))/0.12),start:[...state.position],end:[...target],samples:[]},obstacles);
}
/** Dock stays on the right side of the body with an outward approach corridor. */
export const toolDockPosition=(state:RobotState):Vec3=>add(state.position,rotateZ(TOOL_DOCK_OFFSET,state.yaw));
export function planToolExchange(state:RobotState,limbIndex:number,action:'pick'|'park',obstacles:Obstacle[]=[]):MotionPlan {
  if(state.motion||limbIndex!==1)return {status:'fail',scope:'tool access',reasons:['Tool dock requires the idle upper-right limb']};
  if(action==='pick'&&!state.toolDocked||action==='park'&&!state.limbs[limbIndex].tool)return {status:'fail',scope:'tool custody',reasons:['Tool is not at the requested source']};
  return validateMotion(state,{kind:'tool',elapsed:0,duration:3.4,limbIndex,start:[...state.limbs[limbIndex].position],end:toolDockPosition(state),samples:[],toolAction:action},obstacles);
}
export function beginMotion(state:RobotState,plan:MotionPlan):boolean {
  if(state.motion||plan.status!=='pass'||!plan.motion){if(plan.reasons.length)record(state,`Hold: ${plan.reasons[0]}`);return false;}
  state.motion=plan.motion;
  record(state,plan.motion.kind==='body'?'Shifting body with four fixed clamps':plan.motion.kind==='tool'?`${plan.motion.toolAction==='pick'?'Collecting':'Parking'} tool`:`Unloading limb ${plan.motion.limbIndex!+1}`);
  return true;
}
/** Advance an approved primitive. Body shifts leave every gripper at its exact world position. */
export function advanceMotion(state:RobotState,dt:number):void {
  if(!Number.isFinite(dt)||dt<=0)return;
  state.elapsed+=dt;
  const m=state.motion;if(!m)return;
  m.elapsed=Math.min(m.duration,m.elapsed+dt);const t=m.elapsed/m.duration;
  if(m.kind==='body')state.position=mix(m.start,m.end,smooth(t));
  else {
    const l=state.limbs[m.limbIndex!];
    if(t<0.1){state.status=`Unloading limb ${l.index+1}; three verified supports`;}
    else if(t<0.2){l.mode='free';l.anchor=null;state.status=`Opening clamp ${l.index+1}`;}
    else if(t<0.75){l.mode='approaching';l.position=swingPoint(state,m.start,m.end,(t-0.2)/0.55);state.status=m.kind==='tool'?'Moving to tool dock':`Swinging limb ${l.index+1}; three fixed anchors`;}
    else if(t<0.84){l.position=[...m.end];l.mode='captured';state.status=m.kind==='tool'?'Tool seated in coupler':`Grip ${l.index+1} mechanically captured`;}
    else if(t<0.92){l.position=[...m.end];l.mode='locked';state.status=`Closing positive lock ${l.index+1}`;}
    else {l.position=[...m.end];l.mode='locked';state.status=`Proof-loading grip ${l.index+1}`;}
  }
  if(t>=1){
    if(m.kind==='step'){
      const l=state.limbs[m.limbIndex!];l.position=[...m.end];
      if(m.failVerification){l.mode='fault';l.anchor=null;state.faultCount++;record(state,`Grip ${l.index+1} failed verification; three supports retained`);}
      else {l.mode='load_verified';l.anchor=m.targetAnchor!;state.completedSteps++;record(state,`Grip ${l.index+1} load verified`);}
    }else if(m.kind==='tool'){
      const l=state.limbs[m.limbIndex!];l.anchor=null;l.tool=m.toolAction==='pick';l.mode=l.tool?'tooling':'free';state.toolDocked=!l.tool;record(state,l.tool?'Tool coupled; three anchors carry robot':'Tool parked; recapture fourth grip before travel');
    }else record(state,'Body shift complete; all four anchors remain fixed');
    state.motion=null;
  }
}

/** Demonstration locomotion on two continuous prepared docking rails. Each cycle steps
 * four individual clamps, then shifts the body; rails must be supplied by the caller. */
export function createRailClimber(id:string,railOrigin:Vec3=[0,0,0],initialHeight=1.5):RailClimber {
  const state=createRobotState({id,position:add(railOrigin,[0,-0.68,initialHeight])});
  let nextLimb=0,cycleDelta=0;
  const controller:RailClimber={state,targetHeight:state.position[2],status:'Ready',update(dt,obstacles=[]){
    if(state.motion){advanceMotion(state,dt);controller.status=state.status;return;}
    const difference=controller.targetHeight-state.position[2];
    if(Math.abs(difference)<0.001&&nextLimb===0){controller.status='At destination';return;}
    if(nextLimb===0)cycleDelta=clamp(difference,-0.26,0.26);
    let plan:MotionPlan;
    if(nextLimb<4){
      const l=state.limbs[nextLimb],target=add(l.position,[0,0,cycleDelta]);
      plan=planStep(state,nextLimb,{id:`${id}-rail-${nextLimb%2}-${target[2].toFixed(3)}`,position:target,normal:rotateZ([0,-1,0],state.yaw),available:true},obstacles);
    }else plan=planBodyMove(state,add(state.position,[0,0,cycleDelta]),obstacles);
    if(beginMotion(state,plan)){nextLimb=(nextLimb+1)%5;advanceMotion(state,dt);}
    controller.status=state.status;
  }};
  return controller;
}
