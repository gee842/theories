/** Shared interchange contract. Distances m, times s, masses kg; Z points up. */
export type Vec3 = readonly [number, number, number];
export type ConnectionPhase = 'absent' | 'aligned' | 'captured' | 'final' | 'verified';
export type PartCondition = 'qualified' | 'inspection-required' | 'damaged' | 'quarantined';
export type PartLocation = 'stock' | 'carrier' | 'workfront' | 'installed' | 'inspection-yard';
export type SupportKind = 'stock-rack' | 'carrier' | 'hoist' | 'capture-seat' | 'installed-joint' | 'ground-anchor';
export interface SupportCustody { kind: SupportKind; id: string; }
export interface PartType {
  id: string;
  label: string;
  kind: 'beam' | 'fixture' | 'brace' | 'floor' | 'facade' | 'service';
  dimensions: Vec3;
  massKg: number;
  material: 'steel';
  interfaceFamily: string;
}
export interface ConnectionState {
  id: string;
  end: 'A' | 'B';
  targetId: string;
  phase: ConnectionPhase;
  verifiedAt: number | null;
}
export interface PartInstance {
  id: string;
  typeId: string;
  condition: PartCondition;
  location: PartLocation;
  position: Vec3;
  /** Z-axis orientation. Beam long axis is its local X axis. */
  yaw: number;
  supports: SupportCustody[];
  connections: Record<'A' | 'B', ConnectionState>;
  useCount: number;
  assignedTarget: string | null;
  reserved: boolean;
}
export interface RobotState {
  id: string;
  position: Vec3;
  lockedGrips: number;
  tool: 'parked' | 'guide' | 'driver' | 'inspection';
  mode: 'travel' | 'work' | 'hold';
}
export interface EquipmentState {
  hoistId: string;
  hoistBusy: boolean;
  carrierId: string;
  carrierBusy: boolean;
  /** Carrier chassis origin is on the ground; its restrained load centre is deckHeight above it. */
  carrierPosition: Vec3;
  carrierDeckHeight: number;
  hoistHookPosition: Vec3;
  hoistSlingHeight: number;
  /** Reach of the supplied laboratory XY gantry, including its vertical hook travel. */
  hoistEnvelope: { min: Vec3; max: Vec3 };
}
export interface WorldState {
  schemaVersion: 1;
  time: number;
  revision: number;
  partTypes: Record<string, PartType>;
  parts: Record<string, PartInstance>;
  robots: Record<string, RobotState>;
  equipment: EquipmentState;
  activeFaults: Record<string, { kind: 'mis-seat' | 'grip-unavailable' | 'delivery-delay'; detectedAt: number; message: string }>;
  material: { initialMassKg: number; addedMassKg: number; lostMassKg: number };
  status: 'running' | 'complete';
}
export type EventAction =
  | 'reserve' | 'receive' | 'deliver' | 'attach-hoist' | 'release-carrier' | 'lift'
  | 'guide' | 'capture' | 'fasten' | 'verify' | 'transfer-load' | 'detach-hoist'
  | 'park-tools' | 'retreat' | 'begin-removal' | 'unfasten' | 'release-capture'
  | 'lower' | 'return' | 'inspect-part' | 'qualify-reuse' | 'fault' | 'recover'
  | 'move-carrier' | 'move-hook' | 'move-hoist'
  | 'complete';
export interface EventData {
  targetId?: string;
  yaw?: number;
  end?: 'A' | 'B';
  fault?: 'mis-seat' | 'grip-unavailable' | 'delivery-delay';
  message?: string;
  condition?: PartCondition;
  robotId?: string;
}
/** Events commit at `time`. Motion runs on [time-duration, time]. */
export interface ExecutionEvent {
  id: string;
  sequence: number;
  time: number;
  duration: number;
  action: EventAction;
  partId: string;
  label: string;
  poseFrom?: Vec3;
  poseTo?: Vec3;
  equipmentMotion?: { carrier?: { from: Vec3; to: Vec3 }; hoistHook?: { from: Vec3; to: Vec3 } };
  data: EventData;
}
export interface Scenario {
  id: string;
  seed: number;
  initialWorld: WorldState;
  events: ExecutionEvent[];
  assumptions: string[];
}
export interface Checkpoint { eventId: string; time: number; world: WorldState; }
export interface SimulationTrace {
  scenarioId: string;
  seed: number;
  initialWorld: WorldState;
  events: ExecutionEvent[];
  checkpoints: Checkpoint[];
  finalWorld: WorldState;
  assumptions: string[];
}
