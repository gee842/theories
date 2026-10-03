/** Geometry-only connector screen. All lengths are metres, with Z up. */
export type Vec3 = readonly [number, number, number];

export interface Box {
  readonly id: string;
  readonly min: Vec3;
  readonly max: Vec3;
}

export interface SegmentObstacle {
  readonly id: string;
  readonly start: Vec3;
  readonly end: Vec3;
  readonly radius: number;
}

export type Obstacle = Box | SegmentObstacle;

/** A rigid part is a union of boxes in coordinates relative to its path pose. */
export interface RigidPart {
  readonly id: string;
  readonly solids: readonly Box[];
}

export interface ClearanceEnvelope {
  /** Maximum centre-position error on each world axis. */
  readonly poseError: Vec3;
  /** Maximum outward error of each solid face. */
  readonly partError: Vec3;
  /** Clearance retained from every non-contact obstacle. */
  readonly obstacleClearance: number;
  /** Minimum remaining clearance inside each seat at worst case. */
  readonly seatClearance: number;
  readonly floorContactError: number;
}

/** An upward-facing seat; its floor and cheeks are permitted contact surfaces. */
export interface OpenSeat {
  readonly id: string;
  readonly shoeId: string;
  readonly center: Vec3;
  readonly floorZ: number;
  readonly insideLength: number;
  readonly throatWidth: number;
  readonly mouthWidth: number;
  readonly leadInHeight: number;
  readonly openingError: number;
}

export type ConnectorOperation = 'guide' | 'lower';

export interface ConnectorMotionInput {
  readonly operation: ConnectorOperation;
  readonly member: RigidPart;
  readonly path: readonly Vec3[];
  readonly seats: readonly OpenSeat[];
  /** Fixtures, rails, braces, equipment and any installed socket covers. */
  readonly obstacles: readonly Obstacle[];
  readonly closureState: 'removed' | 'installed';
  readonly envelope: ClearanceEnvelope;
  readonly maxSampleStep: number;
}

export interface PathCheckInput {
  readonly moving: RigidPart;
  readonly path: readonly Vec3[];
  readonly obstacles: readonly Obstacle[];
  readonly envelope: ClearanceEnvelope;
  readonly maxSampleStep: number;
}

export interface ScreeningIssue {
  readonly code: 'invalid-input' | 'closure-present' | 'collision' | 'seat-fit' | 'seat-contact';
  readonly detail: string;
  readonly sample?: number;
  readonly movingSolidId?: string;
  readonly obstacleId?: string;
  readonly seatId?: string;
}

export interface PathScreen {
  readonly status: 'passed' | 'failed';
  readonly sampleCount: number;
  readonly issues: readonly ScreeningIssue[];
}

export interface ConnectorMotionScreen extends PathScreen {
  readonly operation: ConnectorOperation;
  /** Minimum worst-case lateral clearance among both shoes while in the lead-in. */
  readonly minimumSeatMargin: number | null;
}
