/** Planning time is integer simulation seconds. A plan does not commit a world state. */
export type TaskKind =
  | 'ground-seed' | 'brace' | 'rail-extension' | 'member-placement'
  | 'capture' | 'verification' | 'release' | 'recovery';

export type ResourceKind = 'hoist' | 'carrier' | 'robot' | 'tool' | 'approach-zone';

export interface Workfront {
  id: string;
  /** Maximum tasks simultaneously active at this workfront. */
  capacity: number;
}

export interface ResourceUnit {
  id: string;
  kind: ResourceKind;
  /** Omit for a site-wide resource. */
  workfrontIds?: readonly string[];
}

export interface ResourceRequirement {
  kind: ResourceKind;
  /** A specific unit, such as the approach zone for a bay. */
  resourceId?: string;
  /** Number of interchangeable units; defaults to one. Must be one with resourceId. */
  count?: number;
}

export interface PlanningPart {
  id: string;
  typeId: string;
  /** "allocated" means already associated with an installed or held operation. */
  initialState: 'stock' | 'allocated';
}

export interface PartRequirement {
  partId: string;
  typeId: string;
  /** Allocate consumes stock once; reference addresses an already allocated part. */
  mode: 'allocate' | 'reference';
}

export interface PlanningTask {
  id: string;
  kind: TaskKind;
  workfrontId: string;
  predecessors: readonly string[];
  /** Required ancestors, independently checked against the execution DAG. */
  safetyGateIds?: readonly string[];
  durationS: number;
  parts: readonly PartRequirement[];
  resources: readonly ResourceRequirement[];
  /** The task can use these already held reservations. */
  leaseIds?: readonly string[];
  /** A workflow operation is not mechanical validation. */
  mechanicalStatus: 'unverified';
  description: string;
}

/** Holds equipment/corridor reservations from the start task through the end task. */
export interface ResourceLease {
  id: string;
  startTaskId: string;
  endTaskId: string;
  resources: readonly ResourceRequirement[];
}

export interface TaskGraph {
  id: string;
  workfronts: readonly Workfront[];
  resources: readonly ResourceUnit[];
  parts: readonly PlanningPart[];
  tasks: readonly PlanningTask[];
  leases: readonly ResourceLease[];
  assumptions: readonly string[];
}

export type PlanDiagnosticCode =
  | 'invalid-input' | 'duplicate-id' | 'unknown-reference' | 'dependency-cycle'
  | 'missing-safety-gate' | 'unavailable-resource' | 'part-allocation'
  | 'deadlock' | 'transition-limit';

export interface PlanDiagnostic {
  code: PlanDiagnosticCode;
  message: string;
  taskId?: string;
  referenceId?: string;
}

export type WaitReason =
  | 'workfront' | 'part' | 'lease' | `resource:${ResourceKind}` | 'dependency-or-no-work';

export interface PlannedTask {
  taskId: string;
  status: 'planned' | 'blocked' | 'invalid';
  mechanicalStatus: 'unverified';
  readyAtS?: number;
  startS?: number;
  endS?: number;
  /** Direct task reservation IDs; leased IDs are reported in reservations. */
  resourceIds: readonly string[];
  queueWaitS: number;
  waitByReasonS: Partial<Record<WaitReason, number>>;
  blockedReason?: string;
}

export interface ReservationInterval {
  resourceId: string;
  ownerId: string;
  ownerKind: 'task' | 'lease';
  startS: number;
  endS: number;
}

export interface WorkfrontReport {
  workfrontId: string;
  capacity: number;
  busySlotS: number;
  idleSlotS: number;
  idleByReasonS: Partial<Record<WaitReason, number>>;
  utilization: number;
}

export interface ResourceReport {
  kind: ResourceKind;
  units: number;
  busyUnitS: number;
  idleUnitS: number;
  utilization: number;
}

export interface ThroughputReport {
  /** Sum of all task durations, as if one task ran at a time. */
  serialDurationS: number;
  /** Longest predecessor chain with unlimited resources. */
  precedenceCriticalPathS: number;
  precedenceCriticalPathTaskIds: readonly string[];
  /** Last planned completion; only a full result is a complete makespan. */
  resourceLimitedMakespanS: number;
  resourcePenaltyOverPrecedenceS: number;
  totalReadyQueueWaitS: number;
  peakReadyQueue: number;
  peakParallelTasks: number;
  workfronts: readonly WorkfrontReport[];
  resources: readonly ResourceReport[];
}

export interface ScheduleResult {
  graphId: string;
  status: 'complete' | 'blocked' | 'impossible';
  tasks: readonly PlannedTask[];
  reservations: readonly ReservationInterval[];
  diagnostics: readonly PlanDiagnostic[];
  report: ThroughputReport | null;
}

export interface ScheduleOptions {
  /** Defensive event-loop bound; default is 2 × task count + 2. */
  maxTransitions?: number;
}
