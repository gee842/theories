import type { Vec3 } from '../domain/types';

/** Coordinates are metres in the shared Z-up world frame. */
export interface TrussNode {
  id: string;
  positionM: Vec3;
}

/** A straight, pin-ended axial member. Capacities are caller-supplied axial design values. */
export interface TrussMember {
  id: string;
  nodeA: string;
  nodeB: string;
  areaM2: number;
  elasticModulusPa: number;
  tensionCapacityN: number;
  compressionCapacityN: number;
}

/** An ideal translational restraint; constrained axes cannot displace. */
export interface TrussSupport {
  id: string;
  nodeId: string;
  restrained: readonly [boolean, boolean, boolean];
  kind: 'permanent' | 'temporary';
}

export interface NodalLoad {
  nodeId: string;
  forceN: Vec3;
}

export interface TrussModel {
  nodes: readonly TrussNode[];
  members: readonly TrussMember[];
  supports: readonly TrussSupport[];
}

/** Each stage is independently solved from the undeformed geometry. */
export interface ConstructionStage {
  id: string;
  activeMemberIds: readonly string[];
  activeSupportIds: readonly string[];
  loads: readonly NodalLoad[];
}

export type Axis = 'x' | 'y' | 'z';
export interface FreeDof { nodeId: string; axis: Axis; amplitude: number; }
export interface MechanismMode {
  eigenvalueNPerM: number;
  dominantDofs: FreeDof[];
}

export interface ConditioningDiagnostics {
  freeDofCount: number;
  stiffnessRank: number;
  smallestEigenvalueNPerM: number | null;
  largestEigenvalueNPerM: number | null;
  conditionNumber: number | null;
  relativeRankTolerance: number;
  conditionWarning: boolean;
  eigenSolverConverged: boolean;
  /** Maximum unconstrained degree-of-freedom residual after solving. */
  equilibriumResidualN: number | null;
  /** Norm of all applied loads plus all support reactions. */
  globalForceResidualN: number | null;
  mechanismModes: MechanismMode[];
  messages: string[];
}

export interface MemberResult {
  id: string;
  lengthM: number;
  axialForceN: number | null;
  stressPa: number | null;
  mode: 'tension' | 'compression' | 'zero' | 'unresolved';
  tensionCapacityN: number;
  compressionCapacityN: number;
  capacityN: number | null;
  utilization: number | null;
}

export interface NodeDisplacement { nodeId: string; displacementM: Vec3; }
export interface SupportReaction { supportId: string; nodeId: string; forceN: Vec3; }
export interface SupportPath { supportId: string; memberIds: string[]; }
export interface LoadPathResult {
  nodeId: string;
  appliedForceN: Vec3;
  topologicallyConnectedToRestraint: boolean;
  status: 'direct' | 'transmitted' | 'self-equilibrated' | 'unresolved' | 'disconnected';
  /** One force-carrying route to each reacting support; force can split among routes. */
  supportPaths: SupportPath[];
}

export interface StageResult {
  /** The modeled scope, deliberately narrower than whole-frame or code verification. */
  scope: 'axial-truss-screening-only';
  stageId: string;
  stability: 'stable' | 'mechanism' | 'ill-conditioned';
  capacity: 'pass' | 'fail' | 'unverified';
  /** Passes this axial-truss screen only; it does not verify beams, joints, buckling, or a building. */
  canTransferLoad: boolean;
  diagnostics: ConditioningDiagnostics;
  displacements: NodeDisplacement[];
  members: MemberResult[];
  reactions: SupportReaction[];
  loadPaths: LoadPathResult[];
}
