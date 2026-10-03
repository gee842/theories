import { screenConnectorMotion, screenRigidPath } from './geometry';
import type {
  Box, ClearanceEnvelope, ConnectorMotionScreen, Obstacle, OpenSeat, PathScreen, RigidPart, Vec3,
} from './types';

/** A geometric candidate. The beam retains a 3.0 m overall X envelope. */
export const INSTALLED_CENTER: Vec3 = [1.5, 0, 3.327];
export const CLEAR_CENTER: Vec3 = [1.5, 0, 3.777];
export const SAMPLE_STEP = 0.01;

export const BEAM: RigidPart = {
  id: 'reusable-beam-with-end-shoes',
  solids: [
    { id: 'beam-body', min: [-1.43, -0.073, -0.107], max: [1.43, 0.073, 0.147] },
    { id: 'left-shoe', min: [-1.50, -0.065, -0.127], max: [-1.32, 0.065, -0.037] },
    { id: 'right-shoe', min: [1.32, -0.065, -0.127], max: [1.50, 0.065, -0.037] },
  ],
};

export const ENVELOPE: ClearanceEnvelope = {
  poseError: [0.008, 0.010, 0.004],
  partError: [0.002, 0.002, 0.002],
  obstacleClearance: 0.010,
  seatClearance: 0.005,
  floorContactError: 0.006,
};

export const SEATS: readonly OpenSeat[] = [
  { id: 'left-open-seat', shoeId: 'left-shoe', center: [0.09, 0, 3.20], floorZ: 3.20,
    insideLength: 0.24, throatWidth: 0.19, mouthWidth: 0.24, leadInHeight: 0.11,
    openingError: 0.003 },
  { id: 'right-open-seat', shoeId: 'right-shoe', center: [2.91, 0, 3.20], floorZ: 3.20,
    insideLength: 0.24, throatWidth: 0.19, mouthWidth: 0.24, leadInHeight: 0.11,
    openingError: 0.003 },
];

/** Declared fixture solids, including both bays and both sets of robot rails. */
export function fixtureObstacles(): Obstacle[] {
  const obstacles: Obstacle[] = [];
  for (const x of [0, 3]) {
    for (const y of [0, 3]) {
      obstacles.push({ id: `post-${x}-${y}`, min: [x - 0.09, y - 0.09, 0],
        max: [x + 0.09, y + 0.09, 2.85] });
      obstacles.push({ id: `head-${x}-${y}`, min: [x - 0.15, y - 0.15, 2.85],
        max: [x + 0.15, y + 0.15, 3.15] });
    }
    obstacles.push({ id: `longitudinal-rail-${x}`, min: [x - 0.075, 0, 2.915],
      max: [x + 0.075, 3, 3.085] });
    obstacles.push({ id: `brace-rise-${x}`, start: [x, 0, 0.15], end: [x, 3, 2.85], radius: 0.055 });
    obstacles.push({ id: `brace-fall-${x}`, start: [x, 3, 0.15], end: [x, 0, 2.85], radius: 0.055 });
    for (const y of [0, 3]) for (const side of [-1, 1]) {
      const railX = x + side * 0.58;
      obstacles.push({ id: `work-rail-${x}-${y}-${side}`, min: [railX - 0.0375, y - 0.0475, 1.60],
        max: [railX + 0.0375, y + 0.0475, 2.90] });
      for (const z of [1.7, 2.8]) {
        obstacles.push({ id: `rail-arm-${x}-${y}-${side}-${z}`, min: [x + side * 0.31 - 0.25, y - 0.0375, z - 0.0375],
          max: [x + side * 0.31 + 0.25, y + 0.0375, z + 0.0375] });
        obstacles.push({ id: `rail-socket-${x}-${y}-${side}-${z}`, min: [railX - 0.065, y - 0.08, z - 0.04],
          max: [railX + 0.065, y + 0.08, z + 0.04] });
      }
      if (y === 0) {
        obstacles.push({ id: `staging-rail-${x}-${side}`, min: [railX - 0.0275, 0.195, 1.90],
          max: [railX + 0.0275, 0.265, 3.20] });
        for (const z of [2.01, 3.09]) {
          obstacles.push({ id: `staging-socket-${x}-${side}-${z}`, min: [railX - 0.05, 0.18, z - 0.03],
            max: [railX + 0.05, 0.28, z + 0.03] });
        }
      }
    }
  }
  return obstacles;
}

/** Contact hardware is listed separately from collision obstacles. The floor is
 * intended to touch the shoe; cheek/mouth fit is screened analytically. */
export function seatHardware(): Box[] {
  const boxes: Box[] = [];
  for (const seat of SEATS) {
    const x = seat.center[0];
    boxes.push({ id: `${seat.id}-floor`, min: [x - 0.12, -0.15, 3.15], max: [x + 0.12, 0.15, 3.20] });
    boxes.push({ id: `${seat.id}-front-cheek`, min: [x - 0.12, -0.15, 3.20],
      max: [x + 0.12, -0.095, 3.31] });
    boxes.push({ id: `${seat.id}-rear-cheek`, min: [x - 0.12, 0.095, 3.20],
      max: [x + 0.12, 0.15, 3.31] });
  }
  return boxes;
}

/** Outer-end caps bear on the cheek tops with 20 mm nominal uplift play over
 * each shoe. Reversible fastener holes/strength are deliberately unsolved. */
export const CLOSURES: readonly { part: RigidPart; finalPose: Vec3; clearPose: Vec3 }[] = [
  { part: { id: 'left-removable-cap', solids: [{ id: 'left-cap', min: [-0.04, -0.15, -0.02],
    max: [0.04, 0.15, 0.02] }] }, finalPose: [0.01, 0, 3.33], clearPose: [0.01, 0, 3.63] },
  { part: { id: 'right-removable-cap', solids: [{ id: 'right-cap', min: [-0.04, -0.15, -0.02],
    max: [0.04, 0.15, 0.02] }] }, finalPose: [2.99, 0, 3.33], clearPose: [2.99, 0, 3.63] },
];

/** Slim overhead driver access envelope to each cap screw location. A passing
 * path proves clearance of this volume only, not robot reach or operation. */
export const DRIVER: RigidPart = {
  id: 'driver-access-envelope',
  solids: [{ id: 'driver-body-and-bit', min: [-0.03, -0.03, -0.10], max: [0.03, 0.03, 0.10] }],
};

function placedSolids(part: RigidPart, pose: Vec3): Box[] {
  return part.solids.map(s => ({ id: `${part.id}:${s.id}`,
    min: [s.min[0] + pose[0], s.min[1] + pose[1], s.min[2] + pose[2]],
    max: [s.max[0] + pose[0], s.max[1] + pose[1], s.max[2] + pose[2]] }));
}

export interface OpenSeatBenchResult {
  readonly guide: ConnectorMotionScreen;
  readonly lower: ConnectorMotionScreen;
  readonly closurePlacement: readonly PathScreen[];
  readonly closureRemoval: readonly PathScreen[];
  readonly driverAccess: readonly PathScreen[];
  readonly status: 'passed' | 'failed';
}

/** End-to-end geometric sequence: lower into both open seats, place caps,
 * approach each fastener, remove caps, and extract along the reverse path. */
export function runOpenSeatBench(obstacles: readonly Obstacle[] = fixtureObstacles()): OpenSeatBenchResult {
  const guide = screenConnectorMotion({ operation: 'guide', member: BEAM,
    path: [CLEAR_CENTER, INSTALLED_CENTER], seats: SEATS, obstacles,
    closureState: 'removed', envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP });
  const beamAtSeat = placedSolids(BEAM, INSTALLED_CENTER);
  const closurePlacement = CLOSURES.map((closure, i) => screenRigidPath({
    moving: closure.part, path: [closure.clearPose, closure.finalPose],
    obstacles: [...obstacles, ...beamAtSeat,
      ...CLOSURES.filter((_, j) => j < i).flatMap(c => placedSolids(c.part, c.finalPose))],
    envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP,
  }));
  const closedCaps = CLOSURES.flatMap(c => placedSolids(c.part, c.finalPose));
  const driverAccess = CLOSURES.map(c => screenRigidPath({
    moving: DRIVER, path: [[c.finalPose[0], 0, 3.78], [c.finalPose[0], 0, 3.48]],
    obstacles: [...obstacles, ...beamAtSeat, ...closedCaps],
    envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP,
  }));
  const closureRemoval = CLOSURES.map((closure, i) => screenRigidPath({
    moving: closure.part, path: [closure.finalPose, closure.clearPose],
    obstacles: [...obstacles, ...beamAtSeat,
      ...CLOSURES.filter((_, j) => j > i).flatMap(c => placedSolids(c.part, c.finalPose))],
    envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP,
  }));
  const lower = screenConnectorMotion({ operation: 'lower', member: BEAM,
    path: [INSTALLED_CENTER, CLEAR_CENTER], seats: SEATS, obstacles,
    closureState: 'removed', envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP });
  const status = [guide, lower, ...closurePlacement, ...closureRemoval, ...driverAccess]
    .every(r => r.status === 'passed')
    ? 'passed' : 'failed';
  return { guide, lower, closurePlacement, closureRemoval, driverAccess, status };
}

/** Fixed overhead lips turn the same two seats into closed pockets. A straight
 * vertical two-end guide now has no free swept corridor. */
export function screenDualClosedSockets(): ConnectorMotionScreen {
  return screenConnectorMotion({ operation: 'guide', member: BEAM,
    path: [CLEAR_CENTER, INSTALLED_CENTER], seats: SEATS,
    obstacles: [...fixtureObstacles(), ...CLOSURES.flatMap(c => placedSolids(c.part, c.finalPose))],
    closureState: 'removed', envelope: ENVELOPE, maxSampleStep: SAMPLE_STEP });
}
