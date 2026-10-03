import {describe,it,expect} from 'vitest';
import {createRobotState,createRailClimber,planStep,planBodyMove,planToolExchange,beginMotion,advanceMotion,solveRobotPose,assessStance} from './index';
import type {Vec3,Anchor} from './types';
import {createRobotVisual} from '../view/robotVisual';
import {Vector3} from 'three';
const robot=()=>createRobotState({position:[0,-0.68,1.5]});
const destination=(p:Vec3):Anchor=>({id:'destination',position:p,normal:[0,-1,0],available:true});

describe('four-limb climbing mechanism',()=>{
  it('has correct rigid link lengths and balanced contact forces in its initial stance',()=>{
    const state=robot(),pose=solveRobotPose(state),stance=assessStance(state);
    expect(pose.check.reasons).toEqual([]);expect(stance.reasons).toEqual([]);
    for(const p of pose.limbs){
      expect(Math.hypot(...p.elbow.map((n,i)=>n-p.shoulder[i]))).toBeCloseTo(state.config.upperLength,8);
      expect(Math.hypot(...p.wrist.map((n,i)=>n-p.elbow[i]))).toBeCloseTo(state.config.foreLength,8);
    }
    expect(stance.forceResidual).toBeLessThan(1e-6);expect(stance.momentResidual).toBeLessThan(1e-6);
  });
  it('rejects unavailable grips, unreachable destinations and blocked swing paths',()=>{
    const state=robot(),original=JSON.stringify(state);
    expect(planStep(state,0,{...destination([-0.58,0,2.3]),available:false}).status).toBe('fail');
    expect(planStep(state,0,destination([-0.58,0,7])).status).toBe('fail');
    expect(planStep(state,0,destination([-0.58,0,2.3]),[{id:'blocked workfront',min:[-1.5,-1.5,1.5],max:[0,0.5,3]}]).status).toBe('fail');
    expect(JSON.stringify(state)).toBe(original);
  });
  it('holds three fixed verified anchors through release, swing, recapture and verification',()=>{
    const state=robot(),fixed=state.limbs.slice(1).map(l=>[...l.position]);
    const plan=planStep(state,0,destination([-0.58,0,2.3]));expect(plan.reasons).toEqual([]);expect(beginMotion(state,plan)).toBe(true);
    const modes=new Set<string>();
    for(let i=0;i<73;i++){
      advanceMotion(state,0.05);modes.add(state.limbs[0].mode);
      expect(state.limbs.slice(1).map(l=>l.position)).toEqual(fixed);
      expect(state.limbs.filter(l=>l.mode==='load_verified').length).toBeGreaterThanOrEqual(3);
      expect(solveRobotPose(state).check.status).toBe('pass');
    }
    expect([...modes]).toEqual(expect.arrayContaining(['free','approaching','captured','locked','load_verified']));
    expect(state.completedSteps).toBe(1);
  });
  it('never slides locked grips during a body move',()=>{
    const state=robot(),fixed=state.limbs.map(l=>[...l.position]);
    const plan=planBodyMove(state,[0,-0.68,1.6]);expect(plan.reasons).toEqual([]);beginMotion(state,plan);
    for(let i=0;i<30;i++){advanceMotion(state,0.05);expect(state.limbs.map(l=>l.position)).toEqual(fixed);}
    expect(state.position[2]).toBeCloseTo(1.6);
  });
  it('holds after a failed verification and can retry while the other three anchors remain fixed',()=>{
    const state=robot(),target=destination([-0.58,0,2.3]);beginMotion(state,planStep(state,0,target,[],true));advanceMotion(state,4);
    expect(state.limbs[0].mode).toBe('fault');expect(state.completedSteps).toBe(0);expect(assessStance(state).anchorCount).toBe(3);
    const retry=planStep(state,0,target);expect(retry.reasons).toEqual([]);beginMotion(state,retry);advanceMotion(state,4);
    expect(state.limbs[0].mode).toBe('load_verified');expect(state.faultCount).toBe(1);
  });
  it('reaches a rail height by actual stance transitions and returns to the seed',()=>{
    const climber=createRailClimber('test',[2,3,0],1.5);climber.targetHeight=2.28;
    for(let i=0;i<1500;i++)climber.update(0.05);
    expect(climber.state.position[2],climber.status).toBeCloseTo(2.28,5);
    expect(climber.state.completedSteps).toBe(12);expect(solveRobotPose(climber.state).check.status).toBe('pass');
    climber.targetHeight=1.5;for(let i=0;i<1500;i++)climber.update(0.05);
    expect(climber.state.position[2],climber.status).toBeCloseTo(1.5,5);expect(climber.state.completedSteps).toBe(24);
  });
  it('requires tool parking and a recaptured fourth grip before travelling',()=>{
    const state=robot(),home=state.limbs[1].anchor!;
    const pick=planToolExchange(state,1,'pick');expect(pick.reasons).toEqual([]);beginMotion(state,pick);advanceMotion(state,4);
    expect(state.limbs[1].tool).toBe(true);expect(planStep(state,0,destination([-0.58,0,2.3])).status).toBe('fail');
    const park=planToolExchange(state,1,'park');expect(park.reasons).toEqual([]);beginMotion(state,park);advanceMotion(state,4);
    expect(state.toolDocked).toBe(true);expect(planBodyMove(state,[0,-0.68,1.6]).status).toBe('fail');
    const returnGrip=planStep(state,1,home);expect(returnGrip.reasons).toEqual([]);beginMotion(state,returnGrip);advanceMotion(state,4);
    expect(assessStance(state).anchorCount).toBe(4);
  });
  it('does not approve unknown capacities or insufficient actuator capacity',()=>{
    const state=robot();state.config.gripForceLimit=null;
    expect(assessStance(state).status).toBe('unverified');expect(planStep(state,0,destination([-0.58,0,2.3])).status).toBe('fail');
    state.config.gripForceLimit=10;expect(assessStance(state).status).toBe('fail');
  });
  it('keeps the rendered shoulder/elbow/wrist hierarchy on the numerical joint positions',()=>{
    const state=createRobotState({position:[4,-2,3],yaw:0.8}),visual=createRobotVisual();visual.update(state);visual.group.updateMatrixWorld(true);
    const pose=solveRobotPose(state);
    for(let i=0;i<4;i++){
      const actual=visual.group.getObjectByName(`Limb ${i+1} wrist and keyed clamp`)!.getWorldPosition(new Vector3());
      expect(actual.distanceTo(new Vector3(...pose.limbs[i].wrist))).toBeLessThan(1e-8);
    }
    visual.dispose();
  });
});
