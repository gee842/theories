import type { Vec3, Obstacle } from './math';
export type { Vec3, Obstacle } from './math';
export type GripMode = 'free'|'approaching'|'captured'|'locked'|'load_verified'|'tooling'|'fault';
export interface Anchor { id: string; position: Vec3; normal: Vec3; available: boolean; }
export interface RobotConfig {
  upperLength: number; foreLength: number; bodyWidth: number; bodyHeight: number; bodyDepth: number;
  linkRadius: number; elbowFlexMin: number; elbowFlexMax: number; shoulderConeMax: number;
  bodyMass: number; upperMass: number; foreMass: number; clampMass: number; toolMass:number;
  gripForceLimit: number|null; gripMomentLimit: number|null; shoulderTorqueLimit: number|null; elbowTorqueLimit: number|null;
  swingClearance: number; stepSeconds: number; capacitySource: 'assumed'|'measured';
}
export interface LimbState { index: number; position: Vec3; anchor: Anchor|null; mode: GripMode; tool: boolean; }
export interface CheckResult { status:'pass'|'fail'|'unverified'; scope:string; reasons:string[]; }
export interface LimbPose { shoulder:Vec3; elbow:Vec3; wrist:Vec3; reachable:boolean; elbowFlex:number; shoulderAngle:number; }
export interface RobotPose { limbs:LimbPose[]; check:CheckResult; }
export interface LimbLoad { index:number; force:Vec3; moment:Vec3; shoulderTorque:number; elbowTorque:number; utilization:number|null; }
export interface StanceAssessment extends CheckResult { anchorCount:number; loads:LimbLoad[]; forceResidual:number; momentResidual:number; maxUtilization:number|null; }
export interface Motion {
  kind:'step'|'body'|'tool'; elapsed:number; duration:number; limbIndex?:number;
  start:Vec3; end:Vec3; targetAnchor?:Anchor; failVerification?:boolean; samples:Vec3[];
  toolAction?:'pick'|'park';
}
export interface RobotState {
  id:string; position:Vec3; yaw:number; config:RobotConfig; limbs:LimbState[];
  motion:Motion|null; status:string; elapsed:number; completedSteps:number; faultCount:number;
  toolDocked:boolean; events:{time:number; message:string}[];
}
export interface MotionPlan extends CheckResult { motion?:Motion; }
export interface RobotOptions { id?:string; position:Vec3; yaw?:number; config?:Partial<RobotConfig>; }
export interface RailClimber { state:RobotState; targetHeight:number; status:string; update(dt:number,obstacles?:Obstacle[]):void; }
